# Podcast vocabulary notes
Source file: Lex Fridman - Jensen Huang： NVIDIA - The $4 Trillion Company & the AI Revolution ｜ Lex Fridman Podcast #494.opus

**[0.00s] English:** The following is a conversation with Jensen Huang, CEO of NVIDIA, one of the most important  
**Translation:** 

**[6.72s] English:** and influential companies in the history of human civilization. NVIDIA is the engine powering the AI  
**Translation:** Vocabulary: huang: 黄

**[13.32s] English:** revolution, and a lot of its success can be directly attributed to Jensen's sheer force of  
**Translation:** 

**[19.00s] English:** will and his many brilliant bets and decisions as a leader, engineer, and innovator. This is  
**Translation:** Vocabulary: attributed: 归因; innovator: 创新者

**[27.06s] English:** Alex Friedman Podcast, and now, dear friends, here's Jensen Huang.  
**Translation:** 

**[33.08s] English:** You've propelled NVIDIA into a new era in AI, moving beyond its focus on chip-scale design to  
**Translation:** Vocabulary: friedman: 弗里德曼; propelled: 推动

**[40.36s] English:** now rack-scale design. And I think it's fair to say that winning for NVIDIA for a long time used  
**Translation:** 

**[46.00s] English:** to be about building the best GPU possible, and you still do. But now you've expanded that to  
**Translation:** 

**[51.64s] English:** extreme co-design of GPU, CPU, memory, networking, storage, power, cooling,  
**Translation:** 

**[57.06s] English:** software, the rack itself, the pod that you've announced, and even the data center.  
**Translation:** 

**[62.14s] English:** So let's talk about extreme co-design. What is the hardest part of co-designing a system with  
**Translation:** 

**[67.42s] English:** that many complex components and design variables? Yeah, thanks for that question. So first of all,  
**Translation:** 

**[73.66s] English:** the reason why extreme co-design is necessary is because the problem no longer fits inside  
**Translation:** 

**[79.02s] English:** one computer to be accelerated by one GPU. The problem that you're trying to solve is you would  
**Translation:** 

**[87.06s] English:** like to go faster than the number of computers that you add. So you added, you know, 10,000  
**Translation:** 

**[93.52s] English:** computers, but you would like it to go a million times faster. Then all of a sudden, you have to  
**Translation:** 

**[100.94s] English:** take the algorithm, you have to break up the algorithm, you have to refactor it, you have to  
**Translation:** 

**[107.04s] English:** shard the pipeline, you have to shard the data, you have to shard the model. Now, all of a sudden,  
**Translation:** Vocabulary: algorithm: 算法; pipeline: 管道; refactor: 重构; shard: 分片

**[112.98s] English:** when you distribute the problem this way, not just,  
**Translation:** 

**[117.06s] English:** scaling up the problem, but you're distributing the problem.  
**Translation:** 

**[120.00s] English:** then everything gets in the way. This is the Amdahl's law problem, where the amount of speed  
**Translation:** 

**[126.74s] English:** up you have for something depends on how much of the total workload it is. And so if computation  
**Translation:** Vocabulary: computation: 计算; workload: 工作量

**[134.20s] English:** represents 50% of the problem, and I sped up computation infinitely, like a million times,  
**Translation:** 

**[142.96s] English:** I only sped up the total workload by a factor of two. Now, all of a sudden, not only do you have  
**Translation:** Vocabulary: infinitely: 无限地

**[149.54s] English:** to distribute the computation, you have to, you know, shard the pipeline somehow, you also have  
**Translation:** 

**[155.74s] English:** to solve the networking problem. Because you've got all of these computers are all connected  
**Translation:** 

**[160.62s] English:** together. And so distributed computing at the scale that we do, the CPU is a problem, the GPU  
**Translation:** 

**[168.62s] English:** is a problem, the networking is a problem, the switching is a problem. And distributing the  
**Translation:** Vocabulary: computing: 计算

**[174.18s] English:** workload across all these computers are a problem. It's just a massively complex  
**Translation:** 

**[179.36s] English:** computation.  
**Translation:** Vocabulary: massively: 大规模地

**[179.54s] English:** And so we just got to bring every technology to bear. Otherwise, we scale up linearly,  
**Translation:** 

**[187.56s] English:** or we scale up based on the capabilities of Moore's law, which has largely slowed because  
**Translation:** 

**[194.94s] English:** Dennard scaling has slowed. I'm sure there's trade offs there. Plus, you have a complete  
**Translation:** 

**[199.32s] English:** disparate disciplines here. I'm sure you have specialists in each one of these high bandwidth  
**Translation:** Vocabulary: bandwidth: 数据带宽; dennard: Dennard; disciplines: 学科领域; disparate: 不同类

**[203.92s] English:** memory, the network and the NV link, the NICs, the optics and the copper that you're doing,  
**Translation:** 

**[208.96s] English:** the power delivery.  
**Translation:** Vocabulary: optics: 光纤

**[209.54s] English:** The cooling all that. I mean, there's like world experts in each of those. How do you  
**Translation:** 

**[213.48s] English:** get them in a room together to figure out why my staff is so large?  
**Translation:** 

**[217.56s] English:** What's the product? Can you take me through the process of the specialists and the journalists?  
**Translation:** 

**[222.18s] English:** Like, how do you put together the rack when you know this, the set of things you have  
**Translation:** 

**[226.36s] English:** to shove into a rack together? Yeah, like, what does that process look like of designing  
**Translation:** 

**[230.54s] English:** it all together?  
**Translation:** Vocabulary: shove: 推入

**[231.26s] English:** There's the first question, which is what is extreme co design? You're, you were optimizing  
**Translation:** 

**[236.88s] English:** across the entire stack of software.  
**Translation:** Vocabulary: optimizing: 优化

**[238.88s] English:** Yeah.  
**Translation:** 

**[239.88s] English:** And so you're like, oh, okay, because I, you know, I don't like to go out there and  
**Translation:** 

**[240.88s] English:** get like, I'm not like, I'm really into it. But if I go in and I'm like, I want to go  
**Translation:** 

**[241.88s] English:** to every store and look at, you know, I'm really into it. Yeah.  
**Translation:** 

**[242.00s] English:** Yeah.  
**Translation:** 

**[242.08s] English:** And so you have a lot of different recording systems that you, you guys have to, you've  
**Translation:** 

**[242.86s] English:** got to choose like in the office, you've got to, I've got to some kind of domain  
**Translation:** 

**[243.56s] English:** explanation to do it.  
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

**[244.36s] English:** So then I don't have this one end up.  
**Translation:** 

**[244.44s] English:** Yeah, no, I've got this.  
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

**[240.00s] English:** to chips, to systems, to system software, to the algorithms, to the applications. That's  
**Translation:** 

**[244.66s] English:** one layer. The second thing that you and I just talked about goes beyond CPUs and GPUs and  
**Translation:** 

**[250.76s] English:** networking chips and scale-up switches and scale-out switches. And then, of course, you've  
**Translation:** 

**[256.10s] English:** got to include power and cooling and all of that because, you know, all these computers are  
**Translation:** 

**[262.18s] English:** extremely, extremely power-hungry. They do a lot of work, and they're very energy-efficient,  
**Translation:** 

**[268.08s] English:** but they, in aggregate, still consume a lot of power. And so that's one. The first question is,  
**Translation:** Vocabulary: aggregate: 总体

**[273.18s] English:** what is it? The second question is, why is it? And we just spoke about the reason, you know,  
**Translation:** 

**[278.50s] English:** you want to distribute the workloads so that you can exceed the benefit of just increasing the  
**Translation:** 

**[285.58s] English:** number of computers. And then the third question is, how is it? How do you do it? And that's kind  
**Translation:** 

**[294.26s] English:** of the miracle of this company. You know, when you're designing a computer, you have  
**Translation:** 

**[298.02s] English:** to have a lot of power. And so that's one. The second question is, why is it? And we just spoke  
**Translation:** 

**[298.06s] English:** to have an operating system of computers. When you're designing a company, you should first  
**Translation:** 

**[303.14s] English:** think about, what is it that you want the company to produce? You know, I see a lot of companies'  
**Translation:** 

**[307.40s] English:** organization charts, and they all look the same. Hamburger organization charts, software organization  
**Translation:** 

**[312.76s] English:** charts, and car company organization charts, they all look the same. And it doesn't make any sense  
**Translation:** 

**[317.22s] English:** to me. You know, the goal of a company is to be the machinery, the mechanism, the system that  
**Translation:** Vocabulary: machinery: 机器设备

**[323.94s] English:** produces the output. And that output is the product of the company. And that output is the  
**Translation:** 

**[328.04s] English:** that we'd like to create. It is also designed, the architecture of the company should reflect  
**Translation:** 

**[333.26s] English:** the environment by which it exists. It almost directly says what you should do with the  
**Translation:** 

**[339.14s] English:** organization. My direct staff is 60 people. You know, I don't have one-on-ones with them  
**Translation:** 

**[345.04s] English:** because it's impossible. You can't have 60 people on your staff if you're, you know,  
**Translation:** 

**[349.94s] English:** going to get work done. So you still have 60 reports. You still have more. Yeah.  
**Translation:** 

**[353.78s] English:** More. Yeah. And most stars at least have a  
**Translation:** 

**[357.98s] English:** foot in engineering. Almost.  
**Translation:** 

**[360.00s] English:** all of them there's experts in memory there's experts in cpus there's experts in optical all  
**Translation:** 

**[366.40s] English:** yeah gpus and architecture algorithms design so you constantly have an eye on the entire stack  
**Translation:** 

**[373.70s] English:** and you're having like intense discussions about the design of the entire set and no conversation  
**Translation:** 

**[379.42s] English:** is ever one person that's why i don't do one-on-ones we present a problem and all of us  
**Translation:** 

**[385.46s] English:** attack it you know because we're doing extreme code design and literally the company is doing  
**Translation:** 

**[391.26s] English:** extreme code design all the time so even if you're talking about a particular component  
**Translation:** 

**[395.54s] English:** like cooling networking everybody's listening in yeah and they can contribute well this doesn't  
**Translation:** 

**[402.96s] English:** work for the for the power distribution this doesn't exactly this doesn't work for the for  
**Translation:** 

**[407.08s] English:** the memory this doesn't work for this exactly and whoever wants to tune out tune out you know  
**Translation:** 

**[413.48s] English:** yeah and the reason for that is because  
**Translation:** 

**[415.18s] English:** because the people who are on the staff they they know when to pay attention they're supposed  
**Translation:** 

**[420.10s] English:** you know something they could have contributed to they didn't contribute to i'm going to call  
**Translation:** 

**[423.68s] English:** them out you know and so hey come on let's get in here so as you mentioned in videos this company  
**Translation:** 

**[429.52s] English:** is adapting to the environment so which point can you say did the environment change you began  
**Translation:** 

**[435.64s] English:** began adapting sort of secretly in the early days from gpu for gaming maybe the early deep  
**Translation:** 

**[443.68s] English:** learning revolution to we're now going to be the early deep learning revolution to the  
**Translation:** 

**[445.16s] English:** early days from gpu for gaming maybe the early deep learning revolution to we're now going to start  
**Translation:** 

**[445.78s] English:** thinking of it as an ai factory what does nvidia do is produces ai let's build a factory  
**Translation:** 

**[450.70s] English:** i could you could i could reason through it just systematically um we started out as an accelerator  
**Translation:** 

**[457.64s] English:** company but the problem with accelerators is that the application domain is too narrow it has the  
**Translation:** Vocabulary: accelerator: 加速器; accelerators: 加速器

**[463.52s] English:** benefit of being incredibly optimized for the job you know any specialist has that benefit the  
**Translation:** 

**[470.02s] English:** problem with intense specialization is that of course your market reach  
**Translation:** Vocabulary: optimized: 优化

**[475.16s] English:** is narrower but that's that's even fine the problem is  
**Translation:** 

**[480.00s] English:** The market size also dictates your R&D capacity, and your R&D capacity ultimately dictates the influence and impact that you can possibly have in computing.  
**Translation:** Vocabulary: computing: 计算机领域; dictates: 决定; narrower: 更窄

**[494.34s] English:** And so when we first started out as an accelerator, a very specific accelerator, we always knew that that was going to be our first step.  
**Translation:** 

**[502.70s] English:** We had to find a way to become accelerated computing.  
**Translation:** Vocabulary: accelerated: 加速的

**[505.78s] English:** But the problem is when you become a computing company, it's too general purpose, and it takes away from your specialization.  
**Translation:** 

**[513.40s] English:** I connected two words that actually have fundamental tension.  
**Translation:** 

**[519.44s] English:** The better computing company we become, the worse we become as a specialist.  
**Translation:** 

**[523.68s] English:** The more of a specialist, the less capacity we have to do overall computing.  
**Translation:** 

**[529.22s] English:** And I connected those two words together on purpose.  
**Translation:** 

**[532.70s] English:** That the company has to find that really narrow path, step by step by step, to expand our aperture of computing, but not give up on the most important specialization that we had.  
**Translation:** Vocabulary: aperture: 视野

**[546.72s] English:** Okay, so the first step that we took beyond acceleration was we invented the programmable pixel shader.  
**Translation:** 

**[553.00s] English:** So that was the first step towards programmability.  
**Translation:** Vocabulary: pixel: 像素; shader: 着色器

**[556.62s] English:** You know, it was our first journey towards moving into the world of computing.  
**Translation:** 

**[560.58s] English:** The second thing that we did was we...  
**Translation:** 

**[562.70s] English:** We created, we put FP32 into our shaders.  
**Translation:** 

**[567.86s] English:** That FP32 step, IEEE compatible FP32, was a huge step in the direction of computing.  
**Translation:** Vocabulary: compatible: 兼容的; shaders: 着色器

**[576.46s] English:** It was the reason why all of the people who were working on stream processors and, you know, other types of data flow processors discovered us.  
**Translation:** 

**[586.32s] English:** And they said, hey, all of a sudden, you know, we might be able to use this GPU that's incredibly computationally intensive.  
**Translation:** Vocabulary: computationally: 计算上; processors: 处理器

**[591.98s] English:** And it's now.  
**Translation:** 

**[593.24s] English:** You know, compliant with IEEE.  
**Translation:** Vocabulary: compliant: 符合要求

**[594.84s] English:** I can take my software that I was writing, you know, previously on CPUs, and I can...  
**Translation:** 

**[600.00s] English:** you know see about about you know using the gpu for them and which led us to create put c  
**Translation:** 

**[607.24s] English:** on top of fp32 was called we call cg that cg path took us to eventually cuda cuda step by step by  
**Translation:** 

**[616.14s] English:** step um uh with well putting cuda on g-force that that was a strategic decision that was very very  
**Translation:** 

**[624.00s] English:** hard to do because it cost the company enormous amounts of our profits and we couldn't afford it  
**Translation:** 

**[629.80s] English:** at the time but we did it anyways because we wanted to be a computing company a computing  
**Translation:** Vocabulary: computing: 计算

**[635.30s] English:** company has a computing architecture a computing architecture has to be compatible across all of  
**Translation:** 

**[641.14s] English:** the chips that we build can you can you take me to that decision so putting cuda on g-force could  
**Translation:** 

**[645.44s] English:** not afford to do can you explain that decision why why boldly choose to do that anyway yeah you  
**Translation:** 

**[652.42s] English:** explain that excellent that was that was the first i would i would say that that was the first um  
**Translation:** 

**[659.80s] English:** the first strategic decision that that is as close to an existential threat for people who don't know  
**Translation:** 

**[667.78s] English:** it turned out to be spoiler alert one of the most incredibly brilliant decisions ever made by a  
**Translation:** 

**[675.04s] English:** company so cuda turned out to be an incredible foundation for computation uh in this ai  
**Translation:** 

**[681.70s] English:** infrastructure world so so you're just setting the context it turned out to be a good decision  
**Translation:** Vocabulary: computation: 计算

**[687.12s] English:** yeah it turned out to have been good decision i think the  
**Translation:** 

**[689.80s] English:** so so here here's the way it went so we invented this thing called cuda and um uh it expanded the  
**Translation:** 

**[696.30s] English:** the aperture of applications that that we can accelerate with our accelerator the question is  
**Translation:** 

**[702.90s] English:** how do we how do we attract developers to cuda because a computing platform is all about  
**Translation:** Vocabulary: accelerate: 加速; accelerator: 加速器; aperture: 通路

**[710.30s] English:** developers and developers don't come to a computing platform just because you know it  
**Translation:** 

**[718.32s] English:** could perform something interesting and they don't come to a computing platform just because  
**Translation:** 

**[719.80s] English:** they're inputters just because they want to change it if you know what they think the information  
**Translation:** 

**[725.74s] English:** approach is if it's classical information and they can appreciate all kinds of information  
**Translation:** Vocabulary: inputters: 输入者

**[732.32s] English:** and toggles and stuff like that so um i think that i i i think it's really important to differentiate  
**Translation:** 

**[737.96s] English:** between what may come out as information and and what may not and create something that is  
**Translation:** Vocabulary: differentiate: 区分; toggles: 切换按钮

**[742.30s] English:** ommen meant to be and so i'm just going to go ahead and run through some statements overall  
**Translation:** 

**[747.34s] English:** today try something we've talked about a lot today the first thing that we want to do is toücht  
**Translation:** 

**[749.12s] English:** throughaved to avoid collusion with the inflation right so if you're doing like your company or  
**Translation:** 

**[720.00s] English:** they come to a computing platform because the install base is large because a developer like  
**Translation:** Vocabulary: collusion: 勾结

**[725.40s] English:** anybody else wants to develop software that reaches a lot of people so the install base  
**Translation:** 

**[730.14s] English:** is in fact the single most important part of an architecture the architecture could attract  
**Translation:** 

**[736.42s] English:** enormous amounts of criticism for example no architecture has ever attracted more criticism  
**Translation:** 

**[743.12s] English:** than the x86 you know as as a less than less than elegant architecture but yet it is the  
**Translation:** 

**[751.52s] English:** defining architecture of today it gives you an example that in fact so many risk architectures  
**Translation:** 

**[757.84s] English:** which were beautifully architected incredibly well designed by some of the brightest computer  
**Translation:** Vocabulary: architected: 精心设计

**[765.48s] English:** scientists in the world largely failed and so i've given you two examples where one is you know  
**Translation:** 

**[772.14s] English:** one is elegant  
**Translation:** 

**[773.06s] English:** one is elegant  
**Translation:** 

**[773.10s] English:** one is elegant  
**Translation:** 

**[773.12s] English:** the other one's barely aesthetic and so yet x86 survived and install base is everything install  
**Translation:** 

**[779.58s] English:** base defines an architecture not everything else is secondary okay and so there were other  
**Translation:** Vocabulary: aesthetic: 审美

**[785.92s] English:** architectures at the time cuda came out opencl was here there were you know there's several other  
**Translation:** 

**[790.88s] English:** competing architectures but the the thing that the decision that we made that was good was we said  
**Translation:** 

**[795.90s] English:** hey look ultimately it's about um install base and what is the best way we could get a new  
**Translation:** 

**[803.24s] English:** computing architecture into the world by that time frame geforce had become successful we were already  
**Translation:** Vocabulary: computing: 计算

**[810.30s] English:** selling millions and millions of geforce gpus a year and we said you know we we had to put cuda  
**Translation:** 

**[815.86s] English:** on geforce and put it into every single pc whether customers use it or not and use it as a starting  
**Translation:** 

**[825.08s] English:** point of  
**Translation:** 

**[825.90s] English:** cultivating our install base meanwhile we'll go and attract developers and went to universities  
**Translation:** Vocabulary: cultivating: 培养

**[833.70s] English:** and wrote books and taught classes and put cuda everywhere and eventually people will discover  
**Translation:** 

**[840.00s] English:** And at the time, the PC was the primary computing vehicle.  
**Translation:** 

**[843.62s] English:** There was no cloud.  
**Translation:** 

**[844.72s] English:** And we could put a supercomputer in the hands of every researcher in school, every scientist,  
**Translation:** Vocabulary: supercomputer: 超级计算机

**[849.78s] English:** every engineer in school, every student in school, and eventually something amazing will  
**Translation:** 

**[854.78s] English:** happen.  
**Translation:** 

**[855.58s] English:** Well, the problem was CUDA increased our cost of that GPU, which is a consumer product,  
**Translation:** 

**[862.16s] English:** so tremendously it completely consumed all of the company's gross profit dollars.  
**Translation:** Vocabulary: tremendously: 巨大地

**[868.56s] English:** And so at the time, the company was probably worth, I don't know, at the time, $8 billion  
**Translation:** 

**[877.06s] English:** or something, $6, $7 billion or something like that.  
**Translation:** 

**[880.22s] English:** After we launched CUDA, I recognized that it was going to add so much cost, but it was  
**Translation:** 

**[887.88s] English:** something we believed in.  
**Translation:** 

**[890.04s] English:** Our market cap went down to like $1.5 billion.  
**Translation:** 

**[893.32s] English:** And so we were down there for a while.  
**Translation:** 

**[896.96s] English:** And we clawed our way.  
**Translation:** 

**[898.56s] English:** Way back slowly.  
**Translation:** Vocabulary: clawed: 奋力

**[900.54s] English:** But we carried CUDA on GeForce.  
**Translation:** 

**[903.14s] English:** I always say that NVIDIA is the house that GeForce built because it was GeForce that  
**Translation:** 

**[908.36s] English:** took CUDA out to everybody.  
**Translation:** 

**[910.78s] English:** Researchers, scientists, they discovered CUDA on GeForce because they were all, you know,  
**Translation:** 

**[918.10s] English:** many of them were gamers.  
**Translation:** 

**[919.82s] English:** Many of them built their own PCs anyways.  
**Translation:** 

**[922.52s] English:** In a university lab, many of them built clusters themselves, you know, using PC components.  
**Translation:** 

**[928.56s] English:** And so that, you know, that's kind of how we got going.  
**Translation:** Vocabulary: clusters: 计算集群

**[931.58s] English:** And then that became the platform, the foundation for the deep learning revolution.  
**Translation:** 

**[935.18s] English:** That was also another great, great observation.  
**Translation:** 

**[937.60s] English:** Yeah.  
**Translation:** 

**[937.94s] English:** That existential moment.  
**Translation:** 

**[939.48s] English:** Do you remember, like, what were those meetings like?  
**Translation:** 

**[942.76s] English:** What were those discussions like, deciding as a company, risking everything?  
**Translation:** 

**[948.38s] English:** Well, I had to make it clear to the board what we were trying to do.  
**Translation:** 

**[956.04s] English:** And the management team knew our gross margins.  
**Translation:** 

**[958.56s] English:** We were going to get crushed.  
**Translation:** 

**[960.00s] English:** So you could imagine a world where GeForce would carry the burden of CUDA, and none of the gamers would appreciate it, and none of the gamers would pay for it. They only pay a certain price, and it doesn't matter what your cost is.  
**Translation:** 

**[974.54s] English:** And so we increased our cost by 50%, and we were a 35% gross margin company. And so it was quite a difficult decision to make. But you could imagine that someday this would go into workstations, and it would go into supercomputers, and in those segments, maybe we can capture more margin.  
**Translation:** 

**[997.26s] English:** So you could reason your way into being able to afford this, but it still took a decade.  
**Translation:** Vocabulary: segments: 市场部分; supercomputers: 超级计算机; workstations: 工作站

**[1004.54s] English:** But that's more of a conversation with the board, convincing them, but you psychologically. Because NVIDIA has continued to make bold bets that predict the future, and in part, especially now, define the future. So I'm almost looking for wisdom about how you were able to make those decisions, to make leaps like that as a company.  
**Translation:** 

**[1030.60s] English:** Yeah.  
**Translation:** Vocabulary: psychologically: 心理上

**[1034.54s] English:** Well, first of all, I'm informed by a lot of curiosity.  
**Translation:** 

**[1041.30s] English:** At some point, there's a reasoning system that convinces me so clearly this outcome will happen, that this will happen.  
**Translation:** Vocabulary: convinces: 说服

**[1054.62s] English:** And so I believe it in my mind, and when I believe it in my mind, you know how it is. You manifest a future, and that future is so convincing.  
**Translation:** 

**[1064.54s] English:** And there's no way it won't happen. There's a lot of suffering in between, but you've got to believe what you believe.  
**Translation:** Vocabulary: manifest: 显现

**[1072.86s] English:** So you envision the future.  
**Translation:** 

**[1075.48s] English:** Yeah.  
**Translation:** Vocabulary: envision: 构想

**[1075.92s] English:** And you essentially, from a sort of engineering perspective, manifest it.  
**Translation:** 

**[1079.68s] English:** Yeah.  
**Translation:** 

**[1080.00s] English:** You reason about how to get there. You reason about why it must exist. We all reason. The management team will reason about it. We spend a lot of time reasoning about it.  
**Translation:** 

**[1094.76s] English:** The thing that the next part of it is probably a skill thing, which is oftentimes in leadership, the leadership stays quiet or they learn about something and then they do some manifesto and it's a brand new year.  
**Translation:** Vocabulary: manifesto: 宣言; oftentimes: 常常

**[1109.96s] English:** And somehow at the end of the year, next year, we're going to have a brand new plan, big, huge layoff this way, big, huge organization change this way, new mission statement, brand new logos, that kind of stuff.  
**Translation:** 

**[1123.24s] English:** I never do things that way.  
**Translation:** Vocabulary: layoff: 裁员

**[1126.96s] English:** When I learn about something and it's starting to influence how I think, I'll make it very clear to everybody near me that this is interesting.  
**Translation:** 

**[1137.08s] English:** This is going to make a difference.  
**Translation:** 

**[1139.56s] English:** This is going to impact that.  
**Translation:** 

**[1141.70s] English:** And I reason about things step by step by step.  
**Translation:** 

**[1144.36s] English:** Oftentimes, I've already made up my mind, but I'll take every possible opportunity, external information, new insights, new discoveries.  
**Translation:** 

**[1152.70s] English:** New engineering, you know, revelations, new milestones develop.  
**Translation:** Vocabulary: milestones: 重要节点; revelations: 重大发现

**[1157.74s] English:** I'll take those opportunities and I'll use it to shape everybody else's belief system.  
**Translation:** 

**[1165.58s] English:** And I'm doing that literally every single day.  
**Translation:** 

**[1168.72s] English:** I'm doing that with my board.  
**Translation:** 

**[1170.28s] English:** I'm doing that with my management team.  
**Translation:** 

**[1172.14s] English:** I'm doing that with my employees.  
**Translation:** 

**[1173.76s] English:** I'm trying to shape their belief system such that when I come the day I say, hey, let's buy Mellanox.  
**Translation:** Vocabulary: mellanox: 美林诺克斯

**[1182.70s] English:** It's completely obvious to everybody that we absolutely should on the day that on the day that I that I said, hey, guys, let's go all in on deep learning.  
**Translation:** 

**[1194.10s] English:** And let me tell you why.  
**Translation:** 

**[1195.24s] English:** I've already been laying down the bricks to different organizations.  
**Translation:** 

**[1200.00s] English:** inside the company every organization and every everybody many of the people might have heard  
**Translation:** 

**[1206.48s] English:** everything most of the company heard here's of course pieces of it and on the day that i announce  
**Translation:** 

**[1212.98s] English:** it um everybody's kind of bought into many pieces of it and in a lot of ways i like to announce  
**Translation:** 

**[1221.48s] English:** these things and i imagine um that that the employees are kind of saying you know jensen  
**Translation:** 

**[1228.90s] English:** what took you so long and and in fact i've been shaping their belief system for some time  
**Translation:** 

**[1233.80s] English:** and therefore leadership sometimes it looks like you're leading from behind but you've been shaping  
**Translation:** 

**[1240.28s] English:** there you know to the point where on the day that i declared it a hundred percent buy-in but that's  
**Translation:** 

**[1245.62s] English:** what you want you want to bring everybody along you know otherwise we announce something about  
**Translation:** 

**[1250.14s] English:** deep learning and everybody goes what are you talking about you know you announce something  
**Translation:** 

**[1253.94s] English:** about let's go all in on this thing and and your your management team  
**Translation:** 

**[1258.90s] English:** your board your employees your customers they're kind of like where's this coming from you know  
**Translation:** 

**[1263.00s] English:** this is insane and so so gtc in fact if you go back in time you look at look at the keynotes  
**Translation:** 

**[1270.08s] English:** i'm also shaping the belief system of my partners in the industry and and i'm using that to shape  
**Translation:** 

**[1277.84s] English:** you know the belief system of my own employees and and and so by the time that i announced  
**Translation:** 

**[1283.00s] English:** something like for example we just now we just announced grok we've been late  
**Translation:** 

**[1288.90s] English:** i've been talking about the stepping stones for two and a half years you guys just go back and  
**Translation:** 

**[1294.50s] English:** oh my gosh they've been talking about it for two and a half years and so i've been laying the  
**Translation:** 

**[1299.42s] English:** foundation step by step by step so when the time comes you announce it everybody's you know what  
**Translation:** 

**[1303.78s] English:** took you so long but it's not just inside the company you're shaping the landscape the broader  
**Translation:** 

**[1307.42s] English:** global landscape of innovation like putting those ideas out there you really are manifesting reality  
**Translation:** 

**[1312.62s] English:** we don't build computers we actually don't build clouds we don't as it turns out we're  
**Translation:** Vocabulary: manifesting: 显现

**[1317.98s] English:** computing platform companies we don't build computers we don't build clouds we don't build  
**Translation:** 

**[1318.90s] English:** cloud companies we don't build cloud companies we don't build cloud companies we don't build  
**Translation:** 

**[1320.00s] English:** Nobody can buy anything from us. That's the weird thing. We vertically design, vertically integrate  
**Translation:** 

**[1328.26s] English:** to design and optimize, but then we open up the entire platform at every single layer to be  
**Translation:** Vocabulary: integrate: 整合; optimize: 优化; vertically: 纵向

**[1335.08s] English:** integrated into other companies' products and services and clouds and supercomputers and OEM  
**Translation:** 

**[1341.04s] English:** computers. The amazing thing is I can't do what I do without having convinced them first.  
**Translation:** Vocabulary: supercomputers: 超级计算机

**[1348.00s] English:** And so most of GTC is about manifesting a future that by the time that my product is ready,  
**Translation:** 

**[1355.82s] English:** they're going, what took you so long? Yeah. So one of the things you've been a believer  
**Translation:** Vocabulary: believer: 信仰者

**[1362.10s] English:** for a long time is scaling laws broadly defined. So are you still a believer in the scaling laws?  
**Translation:** 

**[1369.62s] English:** Yeah, we have more scaling laws now. So I think you've outlined four of them with pre-training,  
**Translation:** 

**[1374.30s] English:** post-training, test time, and agentic scaling.  
**Translation:** 

**[1376.94s] English:** Scaling. What do you think, when you think about the future, deep future and the near-term future,  
**Translation:** 

**[1384.10s] English:** what are the blockers that you're most concerned about that keep you up at night that you have to  
**Translation:** 

**[1389.58s] English:** overcome in order to keep scaling? Well, we can go back and reflect on  
**Translation:** 

**[1394.08s] English:** what people thought were blockers. So in the beginning, we were the first, the pre-training  
**Translation:** 

**[1399.90s] English:** scaling law. People thought, well, rightfully so, that the amount of data that we have,  
**Translation:** 

**[1406.50s] English:** high quality data, high quality data, high quality data, high quality data, high quality data,  
**Translation:** 

**[1406.92s] English:** data that we have will limit the intelligence that we achieve. And that scaling law was an  
**Translation:** 

**[1412.30s] English:** important, very important scaling law. The larger the model, the correspondingly more data  
**Translation:** 

**[1417.00s] English:** results in a better, results in a smarter AI. And so that was pre-training. And Ilya Suskofer,  
**Translation:** Vocabulary: correspondingly: 相应地

**[1424.84s] English:** Ilya said, we're out of data or something like that. Pre-training is over or something like that.  
**Translation:** 

**[1429.24s] English:** The industry panicked that this is the end of AI. And of course, that's obviously not true.  
**Translation:** 

**[1436.92s] English:** We're going to keep on scaling the amount of data that we have.  
**Translation:** 

**[1440.00s] English:** have to train with, a lot of that data is probably going to be synthetic.  
**Translation:** Vocabulary: synthetic: 合成的

**[1444.34s] English:** And that also confused people. And what people don't realize is that they've kind of forgotten  
**Translation:** 

**[1450.42s] English:** that most of the data that we are training, that we teach each other with, inform each other with,  
**Translation:** 

**[1456.42s] English:** is synthetic. It's synthetic because it didn't come out of nature. You created it. I'm consuming  
**Translation:** 

**[1465.14s] English:** it. I modify it, augment it. I regenerate it. Somebody else consumes it. And so we've now  
**Translation:** Vocabulary: consumes: 消耗; regenerate: 再生

**[1474.32s] English:** reached a level where AI is able to take ground truth, augment it, enhance it, synthetically  
**Translation:** 

**[1485.06s] English:** generate an enormous amount of data. And that part of post-training continues to scale. And so  
**Translation:** Vocabulary: synthetically: 合成地

**[1491.42s] English:** the amount of data that we could use that is human-generated,  
**Translation:** 

**[1495.14s] English:** will be smaller and smaller and smaller. The amount of data that we use to train a model  
**Translation:** 

**[1500.82s] English:** is going to continue to scale to the point where we're no longer limited. Training is no longer  
**Translation:** 

**[1507.82s] English:** limited by data. It's now limited by compute. And the reason for that is most of the data is  
**Translation:** 

**[1512.22s] English:** synthetic. Then the next phase is test time. And I still remember people telling me that  
**Translation:** 

**[1521.04s] English:** inference, oh yeah, that's easy. Pre-training, that's hard.  
**Translation:** Vocabulary: inference: 推理

**[1525.02s] English:** Yeah.  
**Translation:** 

**[1525.12s] English:** These are giant systems that people are talking about. Inference must be easy. And so inference  
**Translation:** 

**[1529.70s] English:** chips are going to be little tiny chips. And they're not like NVIDIA's chips. Oh, those are  
**Translation:** 

**[1534.66s] English:** going to be complicated and expensive. And in the future, inference is going to be the biggest  
**Translation:** 

**[1541.54s] English:** market. And it's going to be easy. And we're going to commoditize. And everybody can build  
**Translation:** 

**[1546.04s] English:** their own chips. And that was always illogical to me because inference is thinking. And I think  
**Translation:** Vocabulary: commoditize: 商品化; illogical: 不合逻辑

**[1554.14s] English:** thinking is hard.  
**Translation:** 

**[1555.00s] English:** Thinking is way harder than reading.  
**Translation:** 

**[1560.00s] English:** is just memorization and generalization, you know, and looking for patterns and relationships.  
**Translation:** 

**[1565.48s] English:** You're reading versus thinking, reasoning, solving problems, taking unexplored experiences,  
**Translation:** Vocabulary: generalization: 概括; memorization: 记忆; unexplored: 未开发

**[1577.22s] English:** new experiences, and breaking it down into decomposing it into, you know, solvable pieces  
**Translation:** 

**[1583.86s] English:** that we then go off either through first principle reasoning or, you know, through  
**Translation:** Vocabulary: decomposing: 分解; solvable: 可解决的

**[1588.72s] English:** previous examples, prior experiences, you know, or just exploration and search and,  
**Translation:** 

**[1596.94s] English:** you know, trying different things.  
**Translation:** 

**[1598.84s] English:** And that whole process of test time scaling inference is really about thinking.  
**Translation:** 

**[1606.84s] English:** And it's about reasoning.  
**Translation:** 

**[1608.38s] English:** It's about planning.  
**Translation:** 

**[1609.18s] English:** It's about search.  
**Translation:** 

**[1610.14s] English:** It's about, and so how could that possibly be compute light?  
**Translation:** 

**[1614.12s] English:** And we were absolutely right about that, you know.  
**Translation:** 

**[1616.12s] English:** So test time scaling is intense.  
**Translation:** 

**[1618.72s] English:** Intensely compute intensive.  
**Translation:** Vocabulary: intensely: 非常

**[1621.00s] English:** Then the question is, okay, now we're at inference and we're at test time scaling.  
**Translation:** 

**[1624.44s] English:** What's beyond that?  
**Translation:** 

**[1626.02s] English:** Well, obviously, we have now created, you know, one agentic person.  
**Translation:** 

**[1632.48s] English:** And that one agentic person has a large language model that we've now, you know, developed.  
**Translation:** 

**[1638.28s] English:** But during test time, that agentic system goes off and does research and bangs on databases  
**Translation:** 

**[1644.84s] English:** and it goes and, you know, uses tools.  
**Translation:** Vocabulary: databases: 数据库

**[1647.94s] English:** And one of the most important things about test time scaling is that it's not just a  
**Translation:** 

**[1648.70s] English:** single agent.  
**Translation:** 

**[1648.74s] English:** One of the most important things it does is spins off and spawns off a whole bunch of  
**Translation:** 

**[1652.10s] English:** sub-agents, which means we're now creating large teams.  
**Translation:** Vocabulary: spawns: 衍生出

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

**[1680.00s] English:** And as we use the agentic systems, they're going to create a lot more data.  
**Translation:** 

**[1684.56s] English:** They're going to create a lot of experiences.  
**Translation:** 

**[1686.28s] English:** Some of it we're going to say, wow, this is really good.  
**Translation:** 

**[1689.76s] English:** We ought to memorize this.  
**Translation:** Vocabulary: memorize: 背下来

**[1691.82s] English:** That data set then comes all the way back to pre-training.  
**Translation:** 

**[1694.92s] English:** We memorize and generalize it.  
**Translation:** Vocabulary: generalize: 泛化

**[1697.10s] English:** We then refine it and fine-tune it back into post-training.  
**Translation:** 

**[1701.96s] English:** Then we enhance it even more with test time.  
**Translation:** Vocabulary: refine: 精炼

**[1704.98s] English:** And the agentic systems put it out into the industry.  
**Translation:** 

**[1710.54s] English:** And so this loop, this cycle, is going to go on and on and on.  
**Translation:** 

**[1714.56s] English:** It kind of comes down to basically intelligence is going to scale by one thing, and that's compute.  
**Translation:** 

**[1721.86s] English:** But there's a tricky thing there that you have to anticipate and predict,  
**Translation:** Vocabulary: anticipate: 预判

**[1725.18s] English:** which is some of these components, it requires different kind of hardware to really do it optimally.  
**Translation:** 

**[1733.08s] English:** So you have to anticipate.  
**Translation:** Vocabulary: optimally: 最优化地

**[1734.32s] English:** You have to anticipate where the AI innovation is going to lead.  
**Translation:** 

**[1737.06s] English:** For example, make sure that's first with sparsity.  
**Translation:** Vocabulary: sparsity: 稀疏性

**[1739.64s] English:** Perfect.  
**Translation:** 

**[1740.08s] English:** With hardware, you can't just pivot on a week's notice.  
**Translation:** 

**[1743.90s] English:** You have to anticipate what that's going to look like.  
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

**[1763.00s] English:** kind of,  
**Translation:** 

**[1763.32s] English:** every three years.  
**Translation:** 

**[1766.08s] English:** And so you need to anticipate what likely is going to happen, you know, two, three years from now.  
**Translation:** 

**[1773.08s] English:** And there's a couple of ways that you could do that.  
**Translation:** 

**[1774.64s] English:** First of all, we could do research internally ourselves.  
**Translation:** Vocabulary: internally: 内部地

**[1776.66s] English:** And that's one of the reasons why we have basic research.  
**Translation:** 

**[1778.70s] English:** We have applied research.  
**Translation:** 

**[1780.00s] English:** We create our own models.  
**Translation:** 

**[1781.50s] English:** And so we have, we have hands on life experience right here.  
**Translation:** 

**[1785.44s] English:** This is part of the co-design that I'm talking about.  
**Translation:** 

**[1788.10s] English:** We're also the only AI company in the world that works with literally every AI company in the world.  
**Translation:** 

**[1791.90s] English:** And to the extent that we can,  
**Translation:** 

**[1793.10s] English:** we try to get a sense of what are the challenges that people are experiencing.  
**Translation:** 

**[1798.98s] English:** So you're listening to the whisper.  
**Translation:** 

**[1800.00s] English:** across the industry, the ad-libs.  
**Translation:** 

**[1802.50s] English:** That's right.  
**Translation:** 

**[1802.98s] English:** You've got to listen and learn from everybody.  
**Translation:** 

**[1805.72s] English:** And then the last part is to have an architecture that's flexible,  
**Translation:** 

**[1810.86s] English:** that can adapt and move with the wind.  
**Translation:** 

**[1813.62s] English:** And one of the benefits of CUDA is that it's, on the one hand,  
**Translation:** 

**[1818.64s] English:** an incredible accelerator.  
**Translation:** Vocabulary: accelerator: 加速器

**[1820.14s] English:** On the other hand, it's really flexible.  
**Translation:** 

**[1822.92s] English:** And so that balance, incredible balance between specialization,  
**Translation:** 

**[1827.36s] English:** otherwise we can't accelerate the CPU,  
**Translation:** 

**[1830.94s] English:** versus generalization so that we can adapt with changing algorithms,  
**Translation:** Vocabulary: accelerate: 加速; generalization: 泛化

**[1835.30s] English:** that's really, really important.  
**Translation:** 

**[1836.76s] English:** That's the reason why CUDA has been so resilient on the one hand,  
**Translation:** Vocabulary: resilient: 坚韧不拔

**[1842.48s] English:** and yet we continue to enhance it.  
**Translation:** 

**[1844.14s] English:** We're at CUDA 13.2,  
**Translation:** 

**[1846.04s] English:** and so we're evolving the architecture so fast  
**Translation:** 

**[1849.16s] English:** that we can stay with the modern algorithms.  
**Translation:** Vocabulary: evolving: 不断发展

**[1855.28s] English:** For example,  
**Translation:** 

**[1857.36s] English:** when Mixture Experts came out,  
**Translation:** 

**[1859.64s] English:** that's the reason why we had MVLink-72 instead of MVLink-8.  
**Translation:** 

**[1863.64s] English:** We could now take an entire 4 trillion, 10 trillion parameter model  
**Translation:** Vocabulary: parameter: 参数; trillion: 万亿

**[1867.80s] English:** and put it in one computing domain as if it's running on one GPU.  
**Translation:** 

**[1875.24s] English:** People probably didn't notice I said it,  
**Translation:** Vocabulary: computing: 计算

**[1879.00s] English:** but if you look at the architecture of the Grace Blackwell racks,  
**Translation:** 

**[1884.24s] English:** it was completely focused on doing one thing,  
**Translation:** Vocabulary: blackwell: 布莱克威尔

**[1887.36s] English:** processing the LLM.  
**Translation:** 

**[1890.04s] English:** All of a sudden, one year later,  
**Translation:** 

**[1892.36s] English:** you're looking at a Vera Rubin rack.  
**Translation:** 

**[1894.42s] English:** It has storage accelerators.  
**Translation:** Vocabulary: accelerators: 加速器; rubin: 鲁宾

**[1897.78s] English:** It has this incredible new CPU called Vera.  
**Translation:** 

**[1900.58s] English:** It has Vera Rubin and MVLink-72 to run the LLMs.  
**Translation:** 

**[1905.88s] English:** It also has this new additional rack called Grok.  
**Translation:** 

**[1909.64s] English:** And so this entire rack system is completely different  
**Translation:** 

**[1914.02s] English:** than the previous one.  
**Translation:** 

**[1916.04s] English:** And it's got all these new things.  
**Translation:** 

**[1917.24s] English:** It's got all these new components in it.  
**Translation:** 

**[1918.32s] English:** And the reason for that is because the last...  
**Translation:** 

**[1920.00s] English:** This one was designed to run MOE large language models, inference, and this one is to run agents, and agents bang on tools.  
**Translation:** 

**[1930.58s] English:** Obviously, the design of the system had to have been done before Cloud Code, Codex, OpenClaw.  
**Translation:** Vocabulary: codex: 代码库; inference: 推断

**[1939.62s] English:** You were anticipating the future, essentially.  
**Translation:** 

**[1941.66s] English:** Yeah.  
**Translation:** Vocabulary: anticipating: 预知

**[1941.88s] English:** And that comes from what?  
**Translation:** 

**[1943.20s] English:** From the whispers, from the understanding what all the state-of-the-art is?  
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

**[1980.00s] English:** I want to be universally smart about everything, past, present, and future, before I make it useful, and so, therefore, I might as well let it go do research.  
**Translation:** Vocabulary: universally: 普适地

**[1989.50s] English:** It's obviously, if it wants to help me, it's got to use my tools.  
**Translation:** 

**[1993.26s] English:** A lot of people would say, AI is going to completely destroy software.  
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
**Translation:** 

**[2012.84s] English:** Like, if I were to create the most amazing agent that we can imagine in the next 10 years, let's say it'd be a humanoid robot.  
**Translation:** 

**[2023.00s] English:** If that humanoid robot were to be created, is it more likely that the humanoid robot comes into my house and uses the tools that I have to do the work that it needs to do?  
**Translation:** Vocabulary: humanoid: 类人形的

**[2034.24s] English:** Or does this hand turn into a 10-pound hammer in one instance?  
**Translation:** 

**[2039.52s] English:** Turns?  
**Translation:** 

**[2039.98s] English:** Turns.  
**Translation:** 

**[2040.00s] English:** to a scalpel in another instance and in order to boil water it beams you know microwaves out of  
**Translation:** Vocabulary: microwaves: 微波; scalpel: 手术刀

**[2047.00s] English:** its fingers you know or is it more likely just to use the microwave you know and the first time it  
**Translation:** 

**[2051.80s] English:** goes up to the microwave it probably doesn't know how to use it but that's okay it's connected to  
**Translation:** Vocabulary: microwave: 微波炉

**[2057.26s] English:** the internet it reads the manual of this microwave reads it instantly becomes an expert and so it  
**Translation:** 

**[2065.06s] English:** uses it and so i i think the i just described in fact almost all of the properties of open claw  
**Translation:** 

**[2073.86s] English:** you know that it's going to use tools that it's going to access files it's going to be able to do  
**Translation:** 

**[2078.84s] English:** research it has io subsystem and when you're done reasoning through it reasoning about it through  
**Translation:** 

**[2084.74s] English:** through it in that way um then you say oh my gosh the impact to the future computing is deeply  
**Translation:** 

**[2093.00s] English:** profound and the reason for that is  
**Translation:** Vocabulary: computing: 计算机; profound: 深刻

**[2095.06s] English:** i think we've just reinvented the computer and then now you say okay when did we reason about  
**Translation:** 

**[2100.60s] English:** that when did we reason about open claw if you take the open claw schematic that i used at gtc  
**Translation:** Vocabulary: schematic: 电路图

**[2107.32s] English:** you will find it two years ago literally two years ago at gtc i was talking about  
**Translation:** 

**[2115.32s] English:** agentic systems that exactly reflect open claw today and and of course the confluence of  
**Translation:** Vocabulary: confluence: 汇合处

**[2124.40s] English:** of  
**Translation:** 

**[2125.00s] English:** of  
**Translation:** 

**[2125.02s] English:** of  
**Translation:** 

**[2125.04s] English:** of  
**Translation:** 

**[2125.06s] English:** of many things had to happen first of all we needed clod and and gpt and you know all of these  
**Translation:** 

**[2131.32s] English:** models to reach a level of capability so so their innovation and their breakthroughs and their  
**Translation:** Vocabulary: breakthroughs: 重大突破; capability: 能力

**[2136.32s] English:** continued advances was really important and then of course somebody had to create a an open source  
**Translation:** 

**[2142.48s] English:** you know um project that that uh was sufficiently robust you know it's sufficiently complete  
**Translation:** Vocabulary: robust: 强壮有力; sufficiently: 足够

**[2150.00s] English:** and that we can all we can all put to put to work and and i think open claw  
**Translation:** 

**[2154.76s] English:** did for did for agentic systems what chat gpt did for generative systems  
**Translation:** Vocabulary: generative: 生成的

**[2160.00s] English:** and i just think it's a very big deal yeah it's a really special moment i'm not exactly sure why  
**Translation:** 

**[2165.46s] English:** it captured so much of the world's attention but it did more than cloud code and codex and so on  
**Translation:** Vocabulary: codex: 书卷

**[2171.82s] English:** because consumers could reach it sure yeah but there's also so much of this is vibes and  
**Translation:** 

**[2177.82s] English:** and peter uh i had a podcast with him a wonderful human being so part of it is also the humans that  
**Translation:** Vocabulary: vibes: 感觉

**[2183.98s] English:** represent the thing and no doubt part of it is memes and the because we're all trying to figure  
**Translation:** 

**[2188.20s] English:** it out there's really serious and complicated security concerns about when you have such  
**Translation:** 

**[2193.44s] English:** powerful technology how do you hand over your data so they can do useful stuff but then there's scary  
**Translation:** 

**[2198.04s] English:** things associated with that and we as a civilization as individual people and as a  
**Translation:** 

**[2202.02s] English:** civilization figuring out how to find that right balance yeah we we uh we jumped on it right away  
**Translation:** 

**[2206.44s] English:** and we sent a bunch of security experts this way and we did this thing called open shell it's it's  
**Translation:** 

**[2212.24s] English:** already been integrated into into open claw and nvidia put forward uh nemo claw  
**Translation:** 

**[2218.18s] English:** yeah exactly they install super easy it makes sure that it's secure we give you two out of three  
**Translation:** 

**[2224.70s] English:** rights agentic systems can can access sensitive information it can execute code and it can  
**Translation:** 

**[2230.20s] English:** communicate externally we could keep things safe if we gave you two out of those three  
**Translation:** Vocabulary: externally: 外部地

**[2237.36s] English:** capabilities at any time but not all three and out of those two out of three capabilities we also  
**Translation:** 

**[2243.24s] English:** give you access control based on based on whatever rights that you're given by  
**Translation:** 

**[2247.92s] English:** enterprise  
**Translation:** 

**[2248.18s] English:** and then we connect it to a policy engine that all these enterprises already have  
**Translation:** Vocabulary: enterprises: 企业

**[2252.86s] English:** and so um we're going to try to do our best to to uh help open claw become a better claw  
**Translation:** 

**[2259.98s] English:** so you eloquently explained how we have a long history of blockers that we thought were going  
**Translation:** Vocabulary: eloquently: 言辞优美地

**[2265.42s] English:** to be blockers and we overcame them but now looking into the future what do you think might  
**Translation:** 

**[2269.14s] English:** be the blockers now that it's clear that agents will be everywhere so it's obviously we're going  
**Translation:** Vocabulary: overcame: 克服了障碍

**[2274.76s] English:** to need compute so what is going to be the blocker for the future for the future for the  
**Translation:** 

**[2278.16s] English:** future so the network's going to have to be structured after that scaling the democracy  
**Translation:** 

**[2279.76s] English:** of that scaling badly though theaporger will take over the  
**Translation:** 

**[2281.22s] English:** the gov  
**Translation:** Vocabulary: theaporger: 道歉者

**[2282.20s] English:** one thing else my my  
**Translation:** 

**[2302.18s] English:** good  
**Translation:** 

**[2303.14s] English:** public  
**Translation:** 

**[2304.28s] English:** but  
**Translation:** 

**[2307.30s] English:** yeah  
**Translation:** 

**[2307.50s] English:** it's  
**Translation:** 

**[2307.72s] English:** going  
**Translation:** 

**[2308.00s] English:** to  
**Translation:** 

**[2280.00s] English:** is a concern, but it's not the only concern. But that's the reason why we're pushing so hard on  
**Translation:** 

**[2285.48s] English:** extreme co-design, so that we can improve the tokens per second, per watt, orders of magnitude  
**Translation:** 

**[2294.80s] English:** every single year. And so in the last 10 years, Moore's law would have progressed computing about  
**Translation:** 

**[2302.18s] English:** 100 times in the last 10 years. We progressed and scaled up computing by a million times in  
**Translation:** Vocabulary: computing: 计算机性能; progressed: 提升

**[2308.02s] English:** the last 10 years. And so we're going to keep on doing that through extreme co-design.  
**Translation:** 

**[2312.96s] English:** So energy efficiency per watt completely affects the revenues of a company. It affects the revenues  
**Translation:** Vocabulary: revenues: 收入

**[2321.46s] English:** of a factory. And we're just going to push that to the limit so that we can keep on driving token  
**Translation:** 

**[2327.28s] English:** costs down as fast as we can. Our computer price is going up, but our token generation effectiveness  
**Translation:** Vocabulary: effectiveness: 效果; token: 代币

**[2336.50s] English:** is going up so much faster. And so we're going to keep on doing that through extreme co-design.  
**Translation:** 

**[2338.02s] English:** The token cost is coming down. It's coming down an order of magnitude every year.  
**Translation:** 

**[2344.68s] English:** So power, that's an interesting one. So the way to try to get around the power blocker is to try to,  
**Translation:** 

**[2351.12s] English:** with the tokens per second per watt, try to make it more and more efficient. Of course,  
**Translation:** 

**[2354.30s] English:** there's the question of how do we get more power. We should also get more power.  
**Translation:** 

**[2357.60s] English:** That's a really complicated one. You've talked about small module nuclear power plants. There's  
**Translation:** Vocabulary: module: 模块

**[2361.46s] English:** all kinds of ideas for energy. How much does it keep you up at night? The bottlenecks in the  
**Translation:** 

**[2368.02s] English:** supply chain of AI, like ASML with EUV lithography machines, GSMC with advanced packaging, like COAS,  
**Translation:** Vocabulary: bottlenecks: 瓶颈; lithography: 光刻

**[2375.28s] English:** and SK Hynix with high bandwidth memory. All the time. And we're working on it all the time.  
**Translation:** 

**[2381.24s] English:** No company in history has ever grown at a scale that we're growing while accelerating that growth.  
**Translation:** Vocabulary: accelerating: 加速; bandwidth: 带宽

**[2389.10s] English:** It's incredible. And it's hard for people to even understand this. In the overall world of AI  
**Translation:** 

**[2395.44s] English:** computing, we're increasing share.  
**Translation:** 

**[2398.02s] English:** And so supply chain, upstream.  
**Translation:** 

**[2400.00s] English:** and downstream are really important to us. I spend a lot of time informing all the CEOs  
**Translation:** 

**[2408.20s] English:** that I work with, what are the dynamics that's going to cause the growth to continue or even  
**Translation:** 

**[2414.78s] English:** accelerate? It's part of the reasons why to the entire right-hand side of me, we're CEOs of  
**Translation:** 

**[2422.26s] English:** practically the entire IT industry upstream and practically the entire  
**Translation:** 

**[2427.30s] English:** infrastructure industry downstream. There were several hundred CEOs and I don't think there's  
**Translation:** 

**[2436.92s] English:** ever been keynotes where several hundred CEOs show up. Part of it is I'm telling them about  
**Translation:** 

**[2443.42s] English:** our business condition now. I'm telling them about the growth drivers in the very near future  
**Translation:** 

**[2449.60s] English:** and what's happening. I'm also describing where are we going to go next so that they could use  
**Translation:** 

**[2457.30s] English:** to inform how they want to invest. I inform them that way like I inform my own employees.  
**Translation:** 

**[2466.16s] English:** Then of course, then I make trips out to them and make sure that, hey, listen, I want you to know  
**Translation:** 

**[2471.82s] English:** this quarter, this coming year, this next year, these things are going to happen.  
**Translation:** 

**[2477.64s] English:** If you look at the CEOs of the DRAM industry, the number one DRAM in the world was DDR memory for  
**Translation:** 

**[2487.30s] English:** CPUs and data centers. About three years ago, I was able to convince several of the CEOs that  
**Translation:** 

**[2496.18s] English:** even though at the time, HBM memory was used quite scarcely and barely by supercomputers,  
**Translation:** 

**[2503.02s] English:** that this was going to be a mainstream memory for data centers in the future. At first, it sounded  
**Translation:** Vocabulary: mainstream: 主流; scarcely: 稀少; supercomputers: 超级计算机

**[2508.30s] English:** ridiculous, but several of the CEOs believed me and decided to invest in building HBM memories.  
**Translation:** 

**[2515.38s] English:** Another memory was  
**Translation:** 

**[2517.30s] English:** rather odd to put into a data center is  
**Translation:** 

**[2520.00s] English:** the low power memories that we use for cell phones.  
**Translation:** 

**[2522.84s] English:** And we wanted them to adapt them  
**Translation:** 

**[2524.74s] English:** for supercomputers in the data center.  
**Translation:** 

**[2527.48s] English:** And they go, cell phone memory for supercomputers?  
**Translation:** 

**[2531.00s] English:** And I explained to them why.  
**Translation:** 

**[2533.26s] English:** Well, look at these two memories,  
**Translation:** 

**[2534.64s] English:** LPDDR5, HBM4.  
**Translation:** 

**[2537.34s] English:** The volumes are so incredible.  
**Translation:** 

**[2539.92s] English:** All three of them had record years in history.  
**Translation:** 

**[2542.24s] English:** And these are 45-year companies.  
**Translation:** 

**[2545.66s] English:** And so, you know, that's part of my job  
**Translation:** 

**[2548.82s] English:** is to inform and shape, inspire, you know?  
**Translation:** 

**[2556.16s] English:** So you're not just manifesting the future  
**Translation:** Vocabulary: manifesting: 显现

**[2558.18s] English:** and maybe inspiring NVIDIA,  
**Translation:** 

**[2561.32s] English:** the different engineers of the company.  
**Translation:** 

**[2563.98s] English:** You're manifesting the supply chain of the future.  
**Translation:** 

**[2566.84s] English:** So you're having conversations with TSMC, with ASML.  
**Translation:** 

**[2570.12s] English:** Upstream, downstream.  
**Translation:** 

**[2571.26s] English:** Upstream, downstream.  
**Translation:** 

**[2572.76s] English:** So that's the thing.  
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

**[2582.22s] English:** there's so much incredibly difficult engineering  
**Translation:** 

**[2585.28s] English:** that happens in the entire semiconductor industry.  
**Translation:** 

**[2588.80s] English:** And it just feels scary  
**Translation:** 

**[2591.82s] English:** how intricate the supply chain is,  
**Translation:** 

**[2595.76s] English:** how many components there are.  
**Translation:** 

**[2596.94s] English:** But it works somehow.  
**Translation:** 

**[2598.64s] English:** Exactly.  
**Translation:** 

**[2599.08s] English:** The deep science, the deep engineering,  
**Translation:** 

**[2601.76s] English:** the incredible manufacturing,  
**Translation:** 

**[2603.24s] English:** and so much of the manufacturing is already robotics.  
**Translation:** 

**[2606.02s] English:** But we have a couple of hundred suppliers  
**Translation:** 

**[2608.78s] English:** that contribute the technology  
**Translation:** Vocabulary: suppliers: 供应商

**[2611.32s] English:** that goes into our 1.3 million component rack.  
**Translation:** 

**[2615.90s] English:** Each rack is 1.3, 1.5 million components.  
**Translation:** 

**[2621.12s] English:** There are 200 suppliers across the Vera Rubin rack.  
**Translation:** 

**[2625.00s] English:** So it's interesting that you don't list that  
**Translation:** Vocabulary: rubin: 维拉·鲁宾

**[2626.64s] English:** as the thing that keeps you up at night  
**Translation:** 

**[2628.00s] English:** in the list of blockers.  
**Translation:** 

**[2629.52s] English:** But I'm doing all the things necessary to...  
**Translation:** 

**[2632.36s] English:** Okay, to...  
**Translation:** 

**[2633.18s] English:** See?  
**Translation:** 

**[2633.88s] English:** I can go to sleep because I checked it off.  
**Translation:** 

**[2635.78s] English:** I said, okay, you know, I go,  
**Translation:** 

**[2637.86s] English:** I can go to sleep.  
**Translation:** 

**[2638.76s] English:** I go...  
**Translation:** 

**[2640.00s] English:** Well, let's see.  
**Translation:** 

**[2641.32s] English:** Let's reason about this.  
**Translation:** 

**[2642.52s] English:** What's important for us?  
**Translation:** 

**[2645.06s] English:** Okay, let's reason about this.  
**Translation:** 

**[2646.84s] English:** Because we changed the system architecture  
**Translation:** 

**[2649.42s] English:** from the original DGX1 that you remembered  
**Translation:** 

**[2652.42s] English:** to MVLink 72 rack scale computing,  
**Translation:** Vocabulary: computing: 计算

**[2656.42s] English:** what does that mean?  
**Translation:** 

**[2658.82s] English:** What does that mean to software?  
**Translation:** 

**[2661.28s] English:** What does that mean to engineering?  
**Translation:** 

**[2662.88s] English:** What does that mean to how we design and test?  
**Translation:** 

**[2665.84s] English:** And what does that mean to the supply chain?  
**Translation:** 

**[2667.24s] English:** Well, one of the things that it meant  
**Translation:** 

**[2670.00s] English:** was we moved supercomputer integration  
**Translation:** 

**[2674.72s] English:** at the data center  
**Translation:** 

**[2676.34s] English:** into supercomputer manufacturing  
**Translation:** 

**[2679.04s] English:** in the supply chain.  
**Translation:** 

**[2682.22s] English:** If you're doing that,  
**Translation:** 

**[2684.26s] English:** you also have to recognize  
**Translation:** 

**[2685.30s] English:** you're going to move one.  
**Translation:** 

**[2686.80s] English:** And if you're in a total footprint  
**Translation:** Vocabulary: footprint: 足迹

**[2691.24s] English:** of whatever data center you're going to build,  
**Translation:** 

**[2694.34s] English:** let's say you would like to have,  
**Translation:** 

**[2696.38s] English:** you know, 50 gigawatts of supercomputers  
**Translation:** 

**[2699.68s] English:** that are running simultaneously  
**Translation:** Vocabulary: gigawatts: 千兆瓦; supercomputers: 超级计算机

**[2701.84s] English:** and it takes one week to manufacture  
**Translation:** 

**[2705.10s] English:** that 50 gigawatts of supercomputers,  
**Translation:** 

**[2708.20s] English:** then each week in the supply chain,  
**Translation:** 

**[2711.58s] English:** the supercomputers are going to need  
**Translation:** 

**[2712.78s] English:** a gigawatt of power.  
**Translation:** 

**[2713.80s] English:** And so we're going to need the supply chain  
**Translation:** Vocabulary: gigawatt: 吉瓦功率

**[2716.12s] English:** to increase the amount of power it has  
**Translation:** 

**[2718.04s] English:** to build, test, to build and test  
**Translation:** 

**[2721.46s] English:** the supercomputers in the supply chain  
**Translation:** 

**[2723.62s] English:** before I ship it.  
**Translation:** 

**[2725.02s] English:** Well, MVLink 72 literally built supercomputers  
**Translation:** 

**[2727.40s] English:** in the supply chain and shipped them,  
**Translation:** 

**[2729.68s] English:** two, three tons at a time per rack.  
**Translation:** 

**[2732.74s] English:** It used to be, they used to come in parts  
**Translation:** 

**[2735.02s] English:** and we used to assemble them inside the data center.  
**Translation:** 

**[2737.72s] English:** But that's impossible now  
**Translation:** Vocabulary: assemble: 组装

**[2738.86s] English:** because MVLink 72 is so dense.  
**Translation:** 

**[2741.18s] English:** And so that's an example.  
**Translation:** 

**[2742.58s] English:** And I would have to go into, you know,  
**Translation:** 

**[2745.08s] English:** I'd fly into the supply chain,  
**Translation:** 

**[2746.86s] English:** go meet my partners and say,  
**Translation:** 

**[2747.80s] English:** hey, I said, guess what?  
**Translation:** 

**[2749.66s] English:** So here's what we're going to do with,  
**Translation:** 

**[2751.40s] English:** this is the way we used to build our DGXs.  
**Translation:** 

**[2754.08s] English:** We're going to build them this way.  
**Translation:** 

**[2755.38s] English:** This is going to be so much better  
**Translation:** 

**[2756.42s] English:** because we're going to need them for inference.  
**Translation:** 

**[2758.92s] English:** The market for inference,  
**Translation:** Vocabulary: inference: 推理

**[2759.68s] English:** inference.  
**Translation:** 

**[2760.00s] English:** is coming. The inflection point for inference is coming. It's going to be a big market.  
**Translation:** Vocabulary: inflection: 转折点

**[2765.48s] English:** And so I first explain to them what's going on, why it's going to happen. And then I ask them  
**Translation:** 

**[2771.18s] English:** to make several billion dollars of capital investments each. And because they trust me  
**Translation:** 

**[2779.90s] English:** and I'm very respectful of them and I give them every opportunity to question me and I spend time  
**Translation:** 

**[2786.14s] English:** to explain things to people and I reason about it. I draw them pictures and I reason about it  
**Translation:** 

**[2790.82s] English:** in first principles. And by the time I'm done with them, there's no what to do.  
**Translation:** 

**[2795.36s] English:** So a lot of it is about relationships and building a shared view of the future.  
**Translation:** 

**[2801.40s] English:** But do you worry about certain bottlenecks? I mean, what are the biggest bottlenecks in  
**Translation:** 

**[2806.32s] English:** the supply chain? Are you worried about ASMLs, EUV tooling? Are you worried about  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[2810.78s] English:** the packaging, co-op packaging of TSMC, about how fast it could scale?  
**Translation:** 

**[2816.04s] English:** Like, what are the biggest bottlenecks in the supply chain?  
**Translation:** 

**[2816.14s] English:** Like you said, you're not only growing incredibly fast, you're accelerating your growth. So  
**Translation:** 

**[2820.62s] English:** it feels like everybody in the supply chain and those are certainly bottlenecks would have to  
**Translation:** 

**[2826.42s] English:** scale up. Are you having conversations with them? Like, how can you scale up this faster?  
**Translation:** 

**[2832.22s] English:** Do you worry about it?  
**Translation:** 

**[2833.28s] English:** No.  
**Translation:** 

**[2833.82s] English:** Okay.  
**Translation:** 

**[2834.46s] English:** Because I told them what I needed. They understood what I need. They told me what  
**Translation:** 

**[2839.64s] English:** they're going to go do. And I believe in what they're going to do.  
**Translation:** 

**[2842.00s] English:** Interesting.  
**Translation:** 

**[2842.52s] English:** Yeah.  
**Translation:** 

**[2842.72s] English:** That's great to hear. So maybe if we can just linger on the power,  
**Translation:** 

**[2846.00s] English:** for a little bit, what are your hopes for how to solve the energy problem?  
**Translation:** 

**[2850.50s] English:** One of the areas that I would love us to talk about and just get the message out,  
**Translation:** 

**[2858.50s] English:** our power grid is designed for the worst case condition with some margin. Well, 99% of the  
**Translation:** 

**[2870.82s] English:** time, we're nowhere near the worst case condition because the worst case condition is a few days in  
**Translation:** 

**[2875.02s] English:** the winter, a few days in the summer. And we're nowhere near the worst case condition because the  
**Translation:** 

**[2875.98s] English:** worst case condition is a few days in the summer and extreme weather.  
**Translation:** 

**[2880.00s] English:** at a time, we're nowhere near the worst case condition and we're probably running around,  
**Translation:** 

**[2884.90s] English:** call it 60% of peak. And so 99% of the time, our power grid has excess power and they're just  
**Translation:** 

**[2895.66s] English:** sitting idle. But they have to be there sitting idle because just in case, when the time comes,  
**Translation:** 

**[2900.98s] English:** hospitals have to be powered and infrastructure has to be powered and airports have to run and  
**Translation:** 

**[2905.20s] English:** so on and so forth. And so the question that I have is whether we could go and help them  
**Translation:** 

**[2911.84s] English:** understand and create contractual agreements and design computer architecture systems,  
**Translation:** 

**[2917.54s] English:** data centers, such that when they need the maximum power for infrastructure in society,  
**Translation:** 

**[2926.60s] English:** that the data centers would get less. But that's in a very rare instance anyways.  
**Translation:** 

**[2931.72s] English:** And during that time, we either have a backup generator for that little part of it,  
**Translation:** 

**[2934.86s] English:** or we have a backup generator for that little part of it.  
**Translation:** 

**[2935.20s] English:** Or we just have our computers shift a workload somewhere else, or we have the computers just  
**Translation:** Vocabulary: generator: 备用发电机; workload: 工作负载

**[2939.74s] English:** run slower. We could degrade our performance, reduce our power consumption, and provide for  
**Translation:** 

**[2947.24s] English:** a slightly longer latency response when somebody asks for an answer. And so I think that that way  
**Translation:** Vocabulary: degrade: 降低; latency: 延迟

**[2955.72s] English:** of using computers, of building data centers, instead of expecting 100% uptime and these  
**Translation:** 

**[2963.40s] English:** contracts that are really, really...  
**Translation:** Vocabulary: uptime: 开机时间

**[2965.20s] English:** quite rigorous. It's putting a lot of pressure on the grid to be able to... Now they're going to  
**Translation:** 

**[2970.48s] English:** have to increase from their maximum. I just want to use their excess. It's just sitting there.  
**Translation:** Vocabulary: rigorous: 严格要求的

**[2976.66s] English:** Yeah, that's not talked about enough. So what's stopping there? Is it regulation? Is it  
**Translation:** 

**[2981.52s] English:** bureaucracy? I think it's a three-way problem. It starts with the end customer. The end customer  
**Translation:** Vocabulary: bureaucracy: 官僚主义

**[2988.28s] English:** puts requirements on the data centers that they can never...  
**Translation:** 

**[2995.20s] English:** Not be available. So that the end customer expects perfection.  
**Translation:** 

**[3000.00s] English:** Now, in order to deliver that perfection, you need a combination of backup generators and your grid power supplier to deliver on perfection.  
**Translation:** 

**[3010.04s] English:** And so everybody's got to have six nines.  
**Translation:** Vocabulary: generators: 发电机组; supplier: 供应商

**[3013.26s] English:** Well, I think, first of all, right now, we ought to have everybody understand that when the customer asks for these things, you have somebody in your data center operations team disconnected from the CEO.  
**Translation:** 

**[3025.38s] English:** I bet the CEO doesn't know this.  
**Translation:** 

**[3026.84s] English:** I'm going to talk to all the CEOs.  
**Translation:** 

**[3028.02s] English:** The CEOs are probably not paying any attention to the contracts that are being signed.  
**Translation:** 

**[3034.32s] English:** And so everybody wants to sign the best contract, of course.  
**Translation:** 

**[3037.26s] English:** And they go down to the cloud service providers and the two contract negotiators.  
**Translation:** Vocabulary: negotiators: 谈判者

**[3044.20s] English:** I could just see them now negotiating these multi-year contracts.  
**Translation:** 

**[3048.96s] English:** Both sides want the best contract.  
**Translation:** 

**[3052.10s] English:** As a result, the CSPs then have to go down to the utilities.  
**Translation:** 

**[3057.10s] English:** And they expect the six nines.  
**Translation:** Vocabulary: utilities: 公共事业

**[3060.18s] English:** And so I think the first thing is just make sure that all of the customers, the CEOs of the customers, realize what they're asking for.  
**Translation:** 

**[3068.74s] English:** Now, the second thing is we have to build data centers that gracefully degrade.  
**Translation:** Vocabulary: degrade: 性能下降

**[3073.50s] English:** And so if the power, if the utility, the grid tells us, listen, we're going to have to back you down to about 80 percent, we're going to say that's no problem at all.  
**Translation:** 

**[3081.64s] English:** We're just going to move our workload around.  
**Translation:** 

**[3083.66s] English:** We're going to make sure that data is never lost.  
**Translation:** 

**[3086.02s] English:** But we can reduce the computing rate and use less energy.  
**Translation:** Vocabulary: computing: 计算

**[3091.58s] English:** The quality of service degrades a little bit.  
**Translation:** 

**[3093.90s] English:** For the critical workloads, I shift that somewhere else right away so I don't have that problem.  
**Translation:** Vocabulary: degrades: 下降; workloads: 负载

**[3099.86s] English:** And so, you know, whoever, whichever data center still has 100 percent uptime.  
**Translation:** 

**[3103.70s] English:** And so how difficult of an engineering problem is that the smart, dynamic allocation of power in the data center?  
**Translation:** Vocabulary: allocation: 电源分配; uptime: 正常运行; whichever: 任一

**[3109.18s] English:** As soon as you could specify, you could engineer it.  
**Translation:** 

**[3112.14s] English:** Beautifully put.  
**Translation:** 

**[3114.30s] English:** So long as it obeys the laws of physics.  
**Translation:** 

**[3116.02s] English:** On first principles, I think we're good.  
**Translation:** 

**[3118.26s] English:** What was the third thing you were mentioning?  
**Translation:** 

**[3120.00s] English:** So the second thing is the data centers. And the third thing is we need utilities to also recognize that this is an opportunity. And and instead of instead of saying, look, it's going to take me five years to increase my grid capability.  
**Translation:** 

**[3137.50s] English:** Uh, if you, if you have, if you're willing to take power of this level of guarantee, I can make them available for you next month and at this price. And so if utilities also offered more segments of power delivery promises, then I think everybody will figure out what to do with it. Yeah. But there's just way too much waste in the, in the grid right now. We should, we should go after it.  
**Translation:** 

**[3163.22s] English:** Uh, you've, uh, highly lauded Elon and, uh, XAICs.  
**Translation:** Vocabulary: lauded: 高度赞扬; segments: 部分

**[3167.50s] English:** He has accomplishment in Memphis in building, um, Colossus supercomputer, probably in record time in just four months. It's now at 200,000 GPUs and growing very quickly. Is there something that you could speak to the, uh, understand about his approach that's instructive to the broadly to all the data center creators that's, um, that enable that kind of accomplishment?  
**Translation:** 

**[3190.30s] English:** His approach to engineering, his approach to the whole management of construction, everything.  
**Translation:** Vocabulary: colossus: 巨无霸; instructive: 有启发的; memphis: Memphis; supercomputer: 超级计算机

**[3195.86s] English:** First of all, Elon is deep.  
**Translation:** 

**[3197.50s] English:** In so many different topics, um, uh, yet he's also a really good systems thinker.  
**Translation:** 

**[3204.54s] English:** And so he's able to think through multiple disciplines and, and, um, uh, he obviously, uh, pushes things, questions, everything where they're number one, is it necessary?  
**Translation:** 

**[3218.62s] English:** Number two, does it have to be done this way?  
**Translation:** Vocabulary: disciplines: 学科领域

**[3221.26s] English:** And in other words, you know, does it have, does it have to take this long?  
**Translation:** 

**[3225.24s] English:** And, and so, so he.  
**Translation:** 

**[3227.50s] English:** He has, he has the, he has the ability, uh, to question everything, uh, to the point where everything is down to its minimal amount that's necessary.  
**Translation:** 

**[3238.16s] English:** You can't take anything else out.  
**Translation:** 

**[3240.00s] English:** And yet the necessary capabilities of the product retains, and so he is as minimalist as you could possibly imagine, and he does it at a system scale.  
**Translation:** 

**[3253.98s] English:** I also love the fact that he is represented. He is present at the point of action. He'll just go there. If there's a problem, he'll just go there and show me the problem.  
**Translation:** Vocabulary: minimalist: 极简主义者

**[3271.12s] English:** When you do all of this in combination, you overcome a lot of previous, this is just the way we do it. I'm waiting for them.  
**Translation:** 

**[3282.98s] English:** I mean, it's just...  
**Translation:** 

**[3283.98s] English:** Everybody has a lot of excuses, and then the last thing is when you act personally with so much urgency, it causes everybody else to act with urgency, and every supplier has a lot of customers going on.  
**Translation:** 

**[3297.98s] English:** Every supplier has a lot of projects going on, and he makes it his business that he's the top priority of everybody else's projects, and so he does that by demonstrating it.  
**Translation:** Vocabulary: supplier: 供应商; urgency: 紧迫感

**[3309.80s] English:** Yeah, I've been in a bunch of those meetings. It's fun to watch because really not enough people.  
**Translation:** 

**[3313.98s] English:** Yeah, I've been in a bunch of those meetings. It's fun to watch because really not enough people.  
**Translation:** 

**[3343.98s] English:** And just building up that intuition from every single task involved in putting together the data center, you start to immediately get a sense at the detailed scale and at the broad system scale of...  
**Translation:** 

**[3360.00s] English:** where the inefficiencies are.  
**Translation:** Vocabulary: inefficiencies: 不效率; intuition: 直觉

**[3361.62s] English:** And so you can make it more and more and more efficient.  
**Translation:** 

**[3364.28s] English:** Plus you have the big hammer of being able to say,  
**Translation:** 

**[3366.88s] English:** let's do it totally different and remove all possible blockers.  
**Translation:** 

**[3370.62s] English:** That's right.  
**Translation:** 

**[3371.50s] English:** Is there parallels in the NVIDIA Extreme Systems  
**Translation:** 

**[3374.16s] English:** co-design approach that you see in the way  
**Translation:** 

**[3376.26s] English:** Elon approaches systems engineering?  
**Translation:** 

**[3378.62s] English:** Well, first of all, co-design is an ultimate  
**Translation:** 

**[3380.74s] English:** systems engineering problem.  
**Translation:** 

**[3382.06s] English:** And so we approach the work that we do from that principle.  
**Translation:** 

**[3386.82s] English:** The other thing that we do, and this is a philosophy that,  
**Translation:** 

**[3393.26s] English:** a thought, a state of mind, I guess,  
**Translation:** 

**[3397.86s] English:** a method that I started 30 years ago,  
**Translation:** 

**[3402.34s] English:** and it's called the speed of light.  
**Translation:** 

**[3404.22s] English:** The speed of light is not just about the speed.  
**Translation:** 

**[3405.92s] English:** The speed of light is my shorthand for what's the limit  
**Translation:** Vocabulary: shorthand: 简化书写

**[3411.24s] English:** of what physics can do.  
**Translation:** 

**[3412.96s] English:** And so everything that we do is compared against this  
**Translation:** 

**[3416.82s] English:** speed of light.  
**Translation:** 

**[3417.76s] English:** Memory speed, math speed, power, cost, time, effort,  
**Translation:** 

**[3425.24s] English:** number of people, manufacturing cycle time.  
**Translation:** 

**[3429.08s] English:** And when you think about latency versus throughput,  
**Translation:** Vocabulary: latency: 延迟; throughput: 吞吐量

**[3432.78s] English:** when you think about cost versus throughput,  
**Translation:** 

**[3435.84s] English:** cost versus capacity, all of these things,  
**Translation:** 

**[3440.14s] English:** you test against the speed of light to achieve  
**Translation:** 

**[3443.76s] English:** all of these different constraints,  
**Translation:** Vocabulary: constraints: 限制条件

**[3447.24s] English:** separately.  
**Translation:** 

**[3448.52s] English:** And then when you consider it together,  
**Translation:** 

**[3451.42s] English:** you know you have to make compromises  
**Translation:** 

**[3452.84s] English:** because a system that achieves extremely low latency  
**Translation:** Vocabulary: compromises: 妥协

**[3456.00s] English:** versus a system that achieves very high throughput  
**Translation:** 

**[3458.96s] English:** are architected fundamentally differently.  
**Translation:** Vocabulary: architected: 设计; fundamentally: 从根本上

**[3461.80s] English:** But you want to know what's the speed of light  
**Translation:** 

**[3464.16s] English:** of a system that achieves high throughput.  
**Translation:** 

**[3467.82s] English:** What's the speed of light of a system  
**Translation:** 

**[3469.58s] English:** that achieves low latency?  
**Translation:** 

**[3472.10s] English:** And then when you think about the total system,  
**Translation:** 

**[3474.28s] English:** you could make trade-offs.  
**Translation:** 

**[3475.96s] English:** And so I,  
**Translation:** 

**[3476.82s] English:** I force everybody to think about what's this,  
**Translation:** 

**[3478.56s] English:** what the first,  
**Translation:** 

**[3479.04s] English:** the first principle.  
**Translation:** 

**[3480.00s] English:** the limits the physical limits um for everything before we you know before we uh do anything  
**Translation:** 

**[3488.08s] English:** and and we test everything against that and so that's a good frame of mind i don't love  
**Translation:** 

**[3494.34s] English:** the other methods which is continuous improvement the problem with continuous improvement it  
**Translation:** 

**[3501.76s] English:** first of all you should engineer something from first principles at the speed you know with speed  
**Translation:** 

**[3507.74s] English:** of light thinking limited only by physical limits and and physics limits and um after that of course  
**Translation:** 

**[3516.50s] English:** you would improve it over time um but i don't like going into a problem and somebody says hey  
**Translation:** 

**[3522.88s] English:** you know it takes 74 days to do this today right now and we can do it for you in 72 days you know  
**Translation:** 

**[3530.10s] English:** i'd rather strip it all back to zero and say first of all explain to me why it's 74 days in the first  
**Translation:** 

**[3535.06s] English:** place and let's know let's think about it and let's think about it and let's think about it  
**Translation:** 

**[3537.74s] English:** what's possible today and if i were to to build it completely from scratch you know how long would  
**Translation:** 

**[3543.80s] English:** it take oftentimes you'd be surprised and might come to six days now the rest of the six days to  
**Translation:** 

**[3550.36s] English:** 74 could be very well reasoned and compromises and you know cost reductions and all kinds of  
**Translation:** Vocabulary: oftentimes: 经常

**[3557.78s] English:** different things but at least you know what they are and then now that you know that six days  
**Translation:** 

**[3562.26s] English:** possible then the conversation from 74 to six  
**Translation:** 

**[3567.74s] English:** surprisingly much more effective in such incredibly complex systems that you're working  
**Translation:** 

**[3572.46s] English:** with is simplicity sometimes a good heuristic to to reach for i mean if i can just i mean the pod  
**Translation:** Vocabulary: heuristic: 启发法; simplicity: 简洁性

**[3581.50s] English:** the vera rubin pod that you announced is just incredible uh we're talking about seven chips  
**Translation:** 

**[3586.48s] English:** seven chip types five purpose built rack types 40 racks 1.2 quadrillion transistors  
**Translation:** Vocabulary: quadrillion: 万亿; transistors: 晶体管

**[3592.06s] English:** nearly 20 000 nvidia dies over 1100 rubin gpus  
**Translation:** 

**[3597.74s] English:** 60 exaflops 10 petabytes per second  
**Translation:** Vocabulary: petabytes: 千兆字节

**[3600.00s] English:** going to scale bandwidth uh that's all just one that's just one pod that's just yeah that's just  
**Translation:** 

**[3607.08s] English:** one five i mean so you have the and then even the the nvl 72 rack alone is 1.3 million components  
**Translation:** Vocabulary: bandwidth: 带宽

**[3615.16s] English:** 1300 chips 4000 pounds crammed into a single 19 inch wide rack and lex we'll probably kind of  
**Translation:** 

**[3620.56s] English:** crank out about 200 of these pods a week just to put in perspective the the amount of different  
**Translation:** Vocabulary: crammed: 塞满; crank: 生产

**[3627.16s] English:** components i suppose simplicity is impossible but is that a metric that you kind of reach for  
**Translation:** 

**[3633.52s] English:** and trying to design things you know the phrase the phrase that i use most often is we we need  
**Translation:** 

**[3639.88s] English:** things to be as complex as necessary but as simple as possible and and so the question is is all that  
**Translation:** 

**[3645.86s] English:** complexity they're necessary and we ought to test for that and we ought to challenge that and then  
**Translation:** Vocabulary: complexity: 复杂性

**[3652.18s] English:** after that everything else above it you know it's gratuitous  
**Translation:** 

**[3655.90s] English:** but some of the most incredible semiconductor industry broadly but what nvidia is doing  
**Translation:** Vocabulary: gratuitous: 多余; semiconductor: 半导体

**[3660.92s] English:** uh some of the greatest engineering in history so these systems are just truly truly marvels  
**Translation:** 

**[3668.98s] English:** of engineering it is the most complex computer the world has ever made yeah the engineering  
**Translation:** Vocabulary: marvels: 奇迹

**[3673.94s] English:** teams i mean i don't know it's not a competition but i don't know if it was like an olympics of  
**Translation:** 

**[3678.20s] English:** engineering teams i mean tsmc does incredible engineering like i said asml at every scale  
**Translation:** 

**[3683.88s] English:** but nvidia is gonna  
**Translation:** 

**[3685.90s] English:** give them a run for their money yeah just incredible incredible teams gold medal medalists  
**Translation:** 

**[3690.22s] English:** in every single every single sport all assembled right here and have to work together and report  
**Translation:** 

**[3695.44s] English:** directly to you this is wonderful uh you've recently traveled to china uh so it's interesting  
**Translation:** Vocabulary: assembled: 聚集

**[3702.62s] English:** to ask you uh china has been incredibly successful in building up its technology sector what do you  
**Translation:** 

**[3708.98s] English:** understand about um how china is able to over the past 10 years build so many incredible world-class  
**Translation:** 

**[3715.90s] English:** companies world-class engineering teams and just this technology  
**Translation:** 

**[3720.00s] English:** ecosystem that produces so many um incredible products a whole bunch of reasons for well first  
**Translation:** 

**[3726.90s] English:** of all let's start let's start with some facts 50 of the world's ai researchers are chinese  
**Translation:** 

**[3732.00s] English:** plus or minus and they're mostly in china still we have many of them here but there's amazing  
**Translation:** 

**[3741.58s] English:** researchers still in china um they their tech industry showed up at precisely the right time  
**Translation:** 

**[3750.00s] English:** at the time of the mobile cloud era their way of contributing with software and so this is a  
**Translation:** 

**[3755.64s] English:** country's incredible science and math really well educated kids um their tech industry was  
**Translation:** 

**[3764.46s] English:** created during the era of software they're very comfortable with modern software  
**Translation:** 

**[3770.08s] English:** china is not one giant economic country it's got many provinces and cities  
**Translation:** 

**[3779.00s] English:** with mayors all competing with each other that's the reason why there's so many ev companies that's  
**Translation:** 

**[3784.42s] English:** the reason why there's so many ai companies that's the reason why there's so many every  
**Translation:** 

**[3788.20s] English:** company you could imagine um they all create some of them and and um as a result they have insane  
**Translation:** 

**[3797.18s] English:** competition internally and you know what remains is an incredible company um they also have a social  
**Translation:** 

**[3809.00s] English:** network where it's family first friend second and company third and so um  
**Translation:** Vocabulary: internally: 内部地

**[3816.08s] English:** the amount of conversation that goes back and forth between they're essentially open source  
**Translation:** 

**[3826.18s] English:** all the time so the fact that they contribute more to open source is so sensible because  
**Translation:** Vocabulary: sensible: 合乎情理

**[3831.80s] English:** they're probably what are we protecting you know my engineers their brothers are in that company  
**Translation:** 

**[3837.28s] English:** their friends are in that company and they're in that company and they're in that company and they're  
**Translation:** 

**[3838.98s] English:** all schoolmates  
**Translation:** 

**[3840.00s] English:** You know, the schoolmate concept is, you know, one schoolmate, your brother for life. And so they share knowledge very, very quickly. And so there's no sense keeping technology hidden. You might as well put it on open source. And so the open source community then amplifies, accelerates the innovation process.  
**Translation:** Vocabulary: accelerates: 加速; amplifies: 放大; schoolmate: 同学; schoolmates: 同学们

**[3862.40s] English:** So you get this rapid, incredible, great talent, rapid innovation because of open source and just, you know, the nature of friends and insane competition among the company.  
**Translation:** 

**[3877.06s] English:** What emerges is incredible stuff.  
**Translation:** 

**[3880.20s] English:** And so this is the fastest innovating country in the world today.  
**Translation:** 

**[3885.32s] English:** And this is something that has everything that I've just said is fundamental to just how the kids were grown.  
**Translation:** Vocabulary: innovating: 不断创新的

**[3891.86s] English:** The fact that they have excellent education, the fact that their parents want them to do well in school, the fact that their culture is that way.  
**Translation:** 

**[3900.28s] English:** These are, you know, these are just the thing about their country.  
**Translation:** 

**[3903.60s] English:** And they showed up at precisely the time when technology is going through that exponential.  
**Translation:** 

**[3909.26s] English:** Plus, culturally, it's pretty cool to be an engineer.  
**Translation:** Vocabulary: culturally: 文化上; exponential: 指数的

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

**[3926.32s] English:** And because we're they're trying to keep us safe.  
**Translation:** 

**[3928.86s] English:** Rule of law governing their country was built out of poverty.  
**Translation:** 

**[3935.30s] English:** And so most of their leaders are incredible engineers.  
**Translation:** 

**[3940.38s] English:** Some of the brightest minds.  
**Translation:** 

**[3942.78s] English:** To take a small tangent, because you mentioned open source, I have to go to perplexity here, who you have been a fan of a long time.  
**Translation:** 

**[3951.14s] English:** I love it.  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[3951.68s] English:** Yeah.  
**Translation:** 

**[3951.86s] English:** And thank you for releasing open source Nematron three super, which you can also use inside perplexity to look stuff up now.  
**Translation:** Vocabulary: nematron: 开源软件; perplexity: 困惑度

**[3959.86s] English:** Thank you.  
**Translation:** 

**[3960.00s] English:** which is a 120 billion parameter open weight MOE model.  
**Translation:** 

**[3965.54s] English:** What's your vision with open source?  
**Translation:** 

**[3969.18s] English:** So you mentioned China with DeepSeek and Minimax  
**Translation:** Vocabulary: minimax: 最大最小值法

**[3973.62s] English:** with all these companies really pushing forward  
**Translation:** 

**[3977.08s] English:** the open source AI movement.  
**Translation:** 

**[3980.38s] English:** And NVIDIA is really leading the way  
**Translation:** 

**[3982.14s] English:** in close to state-of-the-art open source LLMs.  
**Translation:** 

**[3987.16s] English:** What's your vision there?  
**Translation:** 

**[3988.76s] English:** First off,  
**Translation:** 

**[3990.00s] English:** if we're going to be a great AI computing company,  
**Translation:** 

**[3992.60s] English:** we have to understand how AI models are evolving.  
**Translation:** Vocabulary: computing: 计算; evolving: 演变

**[3996.28s] English:** One of the things that I love about Nemotron 3  
**Translation:** 

**[3998.70s] English:** is it's not just a pure transformer model.  
**Translation:** Vocabulary: nemotron: 神经机器

**[4002.60s] English:** It's transformer and SSMs.  
**Translation:** 

**[4005.30s] English:** And we were early in developing the conditional GANs,  
**Translation:** Vocabulary: conditional: 条件性的

**[4011.94s] English:** that progressive GANs,  
**Translation:** 

**[4013.38s] English:** which led step-by-step to diffusion.  
**Translation:** Vocabulary: diffusion: 扩散

**[4015.88s] English:** And so the fact that we're doing basic research  
**Translation:** 

**[4019.02s] English:** and...  
**Translation:** 

**[4020.00s] English:** in model architecture and in different domains  
**Translation:** 

**[4023.06s] English:** gives us visibility into, you know,  
**Translation:** Vocabulary: visibility: 可见性

**[4026.20s] English:** what kind of computing systems  
**Translation:** 

**[4027.54s] English:** would do a good job for future models.  
**Translation:** 

**[4029.36s] English:** And so it is part of our extreme co-design strategy.  
**Translation:** 

**[4033.02s] English:** Second,  
**Translation:** 

**[4034.70s] English:** I think we rightfully recognize  
**Translation:** 

**[4038.36s] English:** that on the one hand,  
**Translation:** 

**[4041.64s] English:** we want world-class models as products  
**Translation:** 

**[4044.82s] English:** and they should be proprietary.  
**Translation:** Vocabulary: proprietary: 专有技术

**[4047.28s] English:** On the other hand,  
**Translation:** 

**[4048.84s] English:** we also want...  
**Translation:** 

**[4050.00s] English:** we want AI to diffuse into every industry  
**Translation:** 

**[4052.34s] English:** and every country,  
**Translation:** Vocabulary: diffuse: 分散

**[4053.70s] English:** every researcher,  
**Translation:** 

**[4055.16s] English:** every student.  
**Translation:** 

**[4057.10s] English:** And if everything is proprietary,  
**Translation:** 

**[4059.58s] English:** it's hard to do research  
**Translation:** 

**[4061.02s] English:** and it's hard to innovate on top of,  
**Translation:** 

**[4064.14s] English:** around,  
**Translation:** Vocabulary: innovate: 创新

**[4064.98s] English:** with.  
**Translation:** 

**[4066.34s] English:** And so open source is fundamentally necessary  
**Translation:** Vocabulary: fundamentally: 从根本上

**[4069.80s] English:** for many industries to join the AI revolution.  
**Translation:** 

**[4074.66s] English:** NVIDIA has the scale  
**Translation:** 

**[4075.74s] English:** and we have the motives  
**Translation:** 

**[4077.50s] English:** to not only...  
**Translation:** 

**[4079.86s] English:** for AI,  
**Translation:** 

**[4081.84s] English:** but for us to be able to do all the work  
**Translation:** 

**[4085.10s] English:** that we have to do to help us  
**Translation:** 

**[4086.46s] English:** to change the world around us.  
**Translation:** 

**[4087.22s] English:** We'll be working on doing some of that.  
**Translation:** 

**[4088.58s] English:** So if we can see that,  
**Translation:** 

**[4090.06s] English:** you know,  
**Translation:** 

**[4090.10s] English:** I think we have a year and a half  
**Translation:** 

**[4092.14s] English:** to do more research  
**Translation:** 

**[4093.58s] English:** and I think that's going to be something  
**Translation:** 

**[4095.12s] English:** that we have to look at for the future.  
**Translation:** 

**[4097.14s] English:** So if we can look at the future,  
**Translation:** 

**[4098.34s] English:** it's going to be very, very, very important  
**Translation:** 

**[4100.40s] English:** to do that.  
**Translation:** 

**[4100.60s] English:** And I'm certainly looking forward to seeing  
**Translation:** 

**[4101.80s] English:** the way that we can do this.  
**Translation:** 

**[4103.42s] English:** I mean...  
**Translation:** 

**[4103.92s] English:** So thank you for all your time.  
**Translation:** 

**[4104.70s] English:** And I think that's it  
**Translation:** 

**[4106.04s] English:** for our discussion today.  
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

**[4080.00s] English:** skills scale and motivation to build and continue to build these ai models for as long as we shall  
**Translation:** 

**[4088.88s] English:** live and so therefore we ought to do that we can open up we can activate every industry every  
**Translation:** 

**[4095.68s] English:** researcher you know every country to be able to join the ai revolution there's the third reason  
**Translation:** 

**[4102.26s] English:** which is from that to recognizing that ai is not just language these ais will likely use  
**Translation:** 

**[4110.54s] English:** tools and models and sub-agents that were trained on other modalities of information  
**Translation:** Vocabulary: modalities: 信息模态

**[4119.28s] English:** maybe it's biology or chemistry or um you know laws of physics or you know fluids and  
**Translation:** 

**[4126.22s] English:** thermodynamics and not all of it is in language structure and so somebody has to go make sure  
**Translation:** Vocabulary: thermodynamics: 热力学

**[4132.24s] English:** that weather prediction biology ai ai for biology physical ai all of that stuff stays  
**Translation:** 

**[4142.64s] English:** can be pushed to the limits and pushed to the frontier we don't build cars but we want to make  
**Translation:** Vocabulary: frontier: 前沿

**[4147.36s] English:** sure every car company has access to great models we don't we don't discover drugs but i want to  
**Translation:** 

**[4152.38s] English:** make sure that lily has the world's best biology ai systems so that they can go use it for  
**Translation:** 

**[4158.18s] English:** discovering drugs so these three fundamental reasons  
**Translation:** 

**[4161.64s] English:** you  
**Translation:** 

**[4162.24s] English:** both in in recognizing that ai is not just language that ai is really broad that we want  
**Translation:** 

**[4167.64s] English:** to engage everybody into the world of ai and then also co-design of ai well i have to say once again  
**Translation:** 

**[4174.02s] English:** thank you uh for open sourcing is really truly open sourcing uh nematron 3 and i appreciate you  
**Translation:** 

**[4179.76s] English:** for saying that we open source the models we open source the weights we open source the data  
**Translation:** Vocabulary: nematron: 神经网络; sourcing: 开源

**[4183.82s] English:** we open source how we created it yeah it's pretty amazing it's really it's really incredible  
**Translation:** 

**[4190.02s] English:** you're originally from  
**Translation:** 

**[4192.24s] English:** taiwan and have a close relationship with tsmc so i have to ask uh tsmc i think uh  
**Translation:** 

**[4200.00s] English:** also is a legendary company in terms of the engineering teams in terms of the  
**Translation:** 

**[4203.70s] English:** incredible engineering work that they do uh what uh what do you understand about tsmc culture and  
**Translation:** 

**[4210.28s] English:** their approach that explains how they're able to achieve this singular unmatched success in uh  
**Translation:** 

**[4217.40s] English:** everything they're doing with semiconductors you know first of all the deepest misunderstanding  
**Translation:** 

**[4222.76s] English:** about tsmc is that that um their technology is all they have that somehow they they have a  
**Translation:** Vocabulary: semiconductors: 半导体

**[4236.06s] English:** really great transistor and if somebody shows up another transistor game over it's the technology  
**Translation:** 

**[4242.90s] English:** and of course you know i don't mean just the transistor and metallization systems the  
**Translation:** Vocabulary: transistor: 晶体管

**[4248.00s] English:** packaging the 3d packaging the silicon photonics that you know all of the  
**Translation:** 

**[4252.62s] English:** technology that they're concerned about is that it's it's a technology that they've  
**Translation:** Vocabulary: photonics: 光子学

**[4252.74s] English:** they're concerned about is that they're concerned about is that it's a technology that they're  
**Translation:** 

**[4252.76s] English:** That technology is really what makes the company special. Their technology makes the company special. But their ability to orchestrate the demands, the dynamic demands of hundreds of companies in the world as they're moving up, shifting out, increasing, decreasing, pushing out, pulling in, changing from customer to customer.  
**Translation:** Vocabulary: orchestrate: 协调; shifting: 变化

**[4282.76s] English:** Wafer starting, wafer stopping, emergency wafer starts. All of this dynamics of the world's complexity as the world is shifting all the time. And somehow they're running a factory with high throughput, high yields, really great costs, excellent customer service.  
**Translation:** 

**[4306.58s] English:** They take their promises seriously.  
**Translation:** Vocabulary: complexity: 复杂性; throughput: 产出率; wafer: 晶圆

**[4310.56s] English:** Because they know that they're helping you.  
**Translation:** 

**[4312.76s] English:** When the wafers were promised to show up, the wafers show up so that you could run your company appropriately.  
**Translation:** Vocabulary: appropriately: 恰当地; wafers: 硅片

**[4320.00s] English:** And so their system, their manufacturing system is completely miraculous. I would say then the second thing is their culture. This culture is simultaneously technology focused on one hand, advancing technology, simultaneously customer service oriented on the other hand.  
**Translation:** 

**[4337.62s] English:** A lot of companies are very customer service oriented, but they're not very technology excellent. They're not at the bleeding edge of technology. There are a lot of companies who are at the bleeding edge of technology, but they're not the best customer service oriented company.  
**Translation:** Vocabulary: advancing: 进步; miraculous: 奇迹; oriented: 导向

**[4351.98s] English:** And so it just depends on somehow they've balanced these two and they're world class of both. And then probably the third thing is the technology that I most value in them, that they created this.  
**Translation:** 

**[4367.62s] English:** Intangible called trust. I trust them to put my company on top of them. That's a very big deal.  
**Translation:** Vocabulary: intangible: 无形

**[4375.24s] English:** Well, they trust. I mean, there's a really close relationship there that you have established and that trust is established based on many years of performance, but there's human relationships involved there as well.  
**Translation:** 

**[4385.14s] English:** Three decades. I don't know how many tens, hundreds of billions of dollars of business we've done through them and we don't have a contract. That's pretty great.  
**Translation:** 

**[4395.32s] English:** Amazing. Okay. There's the story.  
**Translation:** 

**[4398.24s] English:** That in 2013, the founders of TSMC, Morris Chang, offered you the chance to become TSMC's chief executive. And you said you already had a job. Is this story true?  
**Translation:** Vocabulary: chang: chang 氏; founders: 创始人

**[4409.98s] English:** Story is true. I didn't dismiss it, but I was deeply honored. And of course, I knew then, as I know now, TSMC is one of the most consequential companies in history.  
**Translation:** 

**[4423.90s] English:** Yeah.  
**Translation:** Vocabulary: consequential: 有重大影响的

**[4425.78s] English:** And Morris is one of the...  
**Translation:** 

**[4427.62s] English:** The highest regarded executive and business and personal friend that I've had in my life. And for him to ask is...  
**Translation:** 

**[4440.00s] English:** uh, um, I w I was humbled and, and, um, really honored. Um, but, but the work that I'm doing  
**Translation:** 

**[4446.96s] English:** here is really important. And I've seen, you know, in my mind, in ways in my mind's eye,  
**Translation:** 

**[4452.34s] English:** what NVIDIA was going to be and what the impact that we could have. And, um, uh, it was really  
**Translation:** 

**[4458.90s] English:** important work. Uh, and it's my responsibility, you know, my sole responsibility to make this  
**Translation:** 

**[4464.64s] English:** happen. And so I, I, um, uh, I declined it, uh, you know, not, not because it wasn't an  
**Translation:** 

**[4472.62s] English:** incredible offer. Uh, it's an unbelievable offer. Um, but, but I simply couldn't take it.  
**Translation:** 

**[4478.80s] English:** I think NVIDIA, both NVIDIA and TSMC are two of the greatest companies in the history of human  
**Translation:** 

**[4484.82s] English:** civilization and running either one, I'm sure is incredibly complicated effort and takes,  
**Translation:** 

**[4489.94s] English:** you have to truly be all in, uh, everybody at every scale,  
**Translation:** 

**[4494.06s] English:** not just at the,  
**Translation:** 

**[4494.64s] English:** the CEO level, everybody is really truly all in to accomplish this kind of complexity.  
**Translation:** 

**[4500.56s] English:** See, now I can help both companies.  
**Translation:** Vocabulary: complexity: 复杂性

**[4502.16s] English:** Exactly. Um, so NVIDIA is now the most valuable company in the world. I have to ask, what is the  
**Translation:** 

**[4510.26s] English:** NVIDIA's biggest moat as the folks in the tech sector say, the edge you have that  
**Translation:** 

**[4517.34s] English:** protects you from the competition?  
**Translation:** 

**[4520.28s] English:** Our single most important, uh,  
**Translation:** 

**[4524.64s] English:** property as a company is the install base of our computing platform. Our single most important  
**Translation:** 

**[4533.10s] English:** thing is the, today is our, is the install base of CUDA. Now, the reason why, uh,  
**Translation:** 

**[4540.50s] English:** 20, 20 years ago, of course there was no install base, but what makes, and if somebody,  
**Translation:** 

**[4548.04s] English:** if somebody came up with, with a GUDA or TUDA, uh, it wouldn't make any difference at all.  
**Translation:** 

**[4554.64s] English:** And the reason for that is because, because it's never been just about the technology,  
**Translation:** 

**[4559.16s] English:** the technology of  
**Translation:** 

**[4559.90s] English:** .  
**Translation:** 

**[4560.00s] English:** course, was incredible visionary. But it's the fact that the company was dedicated to it,  
**Translation:** Vocabulary: visionary: 远见卓识的人

**[4567.02s] English:** stuck with it, expanded its reach. It wasn't three people that made CUDA successful. It was  
**Translation:** 

**[4574.26s] English:** 43,000 people that made CUDA successful. And the several million developers that believed in us,  
**Translation:** 

**[4581.62s] English:** that trusted that we were going to continue to make CUDA 1, 2, 3, 13, that they decided to port  
**Translation:** 

**[4588.34s] English:** and dedicate their software on top of it, their mountain of software on top of it.  
**Translation:** 

**[4592.88s] English:** And so the install base is the number one most important advantage. That install base,  
**Translation:** 

**[4599.56s] English:** when you amplify it with the velocity of our execution, at the scale that we're talking about,  
**Translation:** 

**[4605.42s] English:** no company in history had ever built systems of this complexity, period.  
**Translation:** 

**[4610.80s] English:** And then to build it once a year is impossible.  
**Translation:** 

**[4616.18s] English:** And that's...  
**Translation:** 

**[4618.34s] English:** Velocity combined with the install base, in the developer's mind,  
**Translation:** 

**[4624.20s] English:** you just can now take a developer's mind. From the developer's perspective, if I support CUDA,  
**Translation:** 

**[4630.98s] English:** tomorrow it will be 10 times better. I just have to wait six months on average.  
**Translation:** 

**[4636.54s] English:** Not only that, if I develop it on CUDA, I reach a few hundred million people,  
**Translation:** 

**[4642.68s] English:** computers. I'm in every cloud. I'm in every computer company. I'm in every single industry.  
**Translation:** 

**[4648.36s] English:** I'm in every single country.  
**Translation:** 

**[4651.00s] English:** So if I create an open source package and I put it on CUDA first,  
**Translation:** 

**[4655.44s] English:** I get these both attributes simultaneously.  
**Translation:** 

**[4660.32s] English:** And not only that,  
**Translation:** Vocabulary: attributes: 特性

**[4662.26s] English:** I trust 100% that NVIDIA is going to keep CUDA around and maintain it and improve it  
**Translation:** 

**[4670.84s] English:** and keep optimizing the libraries for as long as they shall live.  
**Translation:** 

**[4676.88s] English:** You could take that to the bank and that library...  
**Translation:** 

**[4678.20s] English:** You could take that to the bank and that library...  
**Translation:** 

**[4680.00s] English:** You put all that stuff together, if I were a developer today, I would target CUDA first. I would target CUDA most. And that's the reason that I think in the final analysis is our first, that's even our first core advantage.  
**Translation:** 

**[4698.10s] English:** Our second one is our ecosystem. The fact that we vertically integrated this incredibly complex system, but we integrated horizontally into every single company's computers. We're in the Google Cloud, we're in Amazon, we're in Azure. We're ramping up AWS like crazy right now. We're in new companies like CoreWeave and then Scale. We're in supercomputers at Lilly. We're in enterprise computers. We're at the edge in radio base stations.  
**Translation:** Vocabulary: horizontally: 横向集成; supercomputers: 超级计算机; vertically: 纵向集成

**[4727.32s] English:** You know, I'm just...  
**Translation:** 

**[4728.10s] English:** It's just crazy. One architecture is in all these different systems. We're in cars, we're in robots, we're in satellites. We're out in space. And so the fact that you have this one architecture and the ecosystem is so broad, it basically covers every single industry in the world.  
**Translation:** 

**[4743.32s] English:** Well, how does the CUDA install base evolve into the future with AI factories as a moat? Do you think it's possible that NVIDIA of the future is all about the AI factory?  
**Translation:** 

**[4755.54s] English:** Well, the unit of computing...  
**Translation:** Vocabulary: computing: 计算

**[4758.10s] English:** It used to be GPU to us. Then it became a computer. Then it became a cluster. Now it's an entire AI factory. When I see a computer, when I see what NVIDIA builds, in the old days, I visualized the chip. And then when I announced a new product, you know, new generation, like, ladies and gentlemen, we're announcing Ampere today. I pick up the chip.  
**Translation:** 

**[4779.86s] English:** Yeah.  
**Translation:** Vocabulary: ampere: 安培; cluster: 计算集群; visualized: 想象

**[4780.14s] English:** That was my mental model of what I was building. Today, I wouldn't... Picking up the chip is kind of still adorable.  
**Translation:** 

**[4787.56s] English:** Yeah.  
**Translation:** 

**[4788.10s] English:** Adorable. It's not my mental model of what I'm doing. My mental model is this giant gigawatt thing that has power generations connected.  
**Translation:** 

**[4800.00s] English:** to the grid it's got cooling systems and networking of incredible monstrosity you know  
**Translation:** Vocabulary: gigawatt: gig瓦; monstrosity: 奇观外型

**[4805.24s] English:** 10 000 people are in there trying to install it hundreds of networking engineers in there  
**Translation:** 

**[4810.88s] English:** thousands of engineers behind it trying to power it up you know powering up one of those factories  
**Translation:** 

**[4816.18s] English:** as you know it's not somebody going it's on now it takes thousands of people to bring it up so  
**Translation:** 

**[4822.70s] English:** mentally you're actually when you're thinking about a single unit of compute you're like  
**Translation:** 

**[4826.46s] English:** literally when you go to bed at night you're thinking now about collection of racks so pods  
**Translation:** 

**[4832.20s] English:** not individual chips entire infrastructure and i'm hoping my next click is when i'm thinking  
**Translation:** 

**[4836.78s] English:** about building computers it's you know planetary scale that'll be the next click what do you think  
**Translation:** 

**[4842.80s] English:** about the space angle that elon has talked about doing compute in space for solving some of the  
**Translation:** 

**[4850.20s] English:** it makes some of the energy issues in terms of scaling energy easier  
**Translation:** 

**[4856.08s] English:** you  
**Translation:** 

**[4856.46s] English:** cooling issues is not easy you know cooling well there's a large number of engineering  
**Translation:** 

**[4861.36s] English:** complexities involved with that yeah so what you know nvidia has also announced that you're already  
**Translation:** Vocabulary: complexities: 复杂性

**[4867.58s] English:** thinking about that yeah we're already there uh nvidia gpus are the first gpus in space  
**Translation:** 

**[4872.84s] English:** and um i didn't realize it was it was so interesting to i would have declared it maybe  
**Translation:** 

**[4879.68s] English:** we're in space you know little little astronaut suit on one of our gpus  
**Translation:** 

**[4886.46s] English:** but but we've been in space uh it's the right place to do a lot of imaging you know because  
**Translation:** 

**[4892.44s] English:** those satellites have really high resolution imaging systems and they're sweeping the earth  
**Translation:** 

**[4897.30s] English:** you know continuously now and um you want you know centimeter scale you know imaging that is  
**Translation:** Vocabulary: sweeping: 全面扫描

**[4904.76s] English:** done continuously uh for the world so that you know you'll basically have real-time telemetry  
**Translation:** 

**[4910.66s] English:** of everything uh you don't want to beam that back down to earth it's just you know  
**Translation:** Vocabulary: telemetry: 遥测数据

**[4916.34s] English:** you don't want to beam that back down to earth it's just you know you don't want to beam that  
**Translation:** 

**[4916.46s] English:** back down to earth it's just you know you don't want to beam that back down to earth petabytes and petabytes of data  
**Translation:** Vocabulary: petabytes: 千兆字节

**[4918.84s] English:** petabytes and petabytes of data  
**Translation:** 

**[4918.86s] English:** petabytes and petabytes of data you got to just do ai  
**Translation:** 

**[4920.00s] English:** you got to just do ai  
**Translation:** 

**[4920.00s] English:** there at the edge throw away everything you don't need you've seen before didn't change  
**Translation:** 

**[4924.48s] English:** and then just keep the stuff that that you need and so ai ought to be done at the edge  
**Translation:** 

**[4929.12s] English:** um obviously we have we have a 24 7 solar if we put it at the polars and um uh  
**Translation:** 

**[4939.04s] English:** but you know there's no conduction no convection and so you know you're pretty much just radiation  
**Translation:** 

**[4945.44s] English:** and um uh but you know space is big i guess we're just going to put big giant radiators out there  
**Translation:** Vocabulary: conduction: 热传导; convection: 对流; radiators: 散热器

**[4951.92s] English:** how crazy of an idea do you think it is like is this is this five years out 10 years out 20 years  
**Translation:** 

**[4956.88s] English:** out so uh we're talking about blockers for ai scaling you know i'm just so much more practical  
**Translation:** 

**[4962.80s] English:** i i look for where where um uh my next next bucket of opportunities are first  
**Translation:** 

**[4971.28s] English:** meanwhile i'm cultivating space and so i sent i sent engineers  
**Translation:** Vocabulary: cultivating: 培育

**[4975.44s] English:** uh to go work on the problem we're starting we're learning a lot about it  
**Translation:** 

**[4980.40s] English:** how do we do with radiation how do we do with degrading performance how do we deal with um  
**Translation:** Vocabulary: degrading: 性能下降

**[4985.68s] English:** continuous uh testing and attestation of of um defects and and um you know how do we deal with  
**Translation:** 

**[4992.48s] English:** redundancy and how do we degrade uh gracefully and things like that and so we could we could do  
**Translation:** Vocabulary: degrade: 退化; redundancy: 冗余

**[4998.88s] English:** what about software how do you think about software and and redundancy and performance  
**Translation:** 

**[5005.44s] English:** so that so that the computer never breaks it just gets slower you know and um i so we could start  
**Translation:** 

**[5013.68s] English:** doing a lot of engineering exploration up front but in the meantime my my favorite answer is  
**Translation:** 

**[5019.76s] English:** eliminate waste you know we've we've got all that idle power i want to evacuate it as fast as  
**Translation:** Vocabulary: evacuate: 清除; meantime: meantime

**[5025.20s] English:** possible yeah yeah there's a lot of low-hanging fruit here on earth yeah uh that we can utilize  
**Translation:** 

**[5032.24s] English:** uh for the ai scaling uh quick pause  
**Translation:** 

**[5035.44s] English:** quick 30 second thank you to our sponsors check them out in the description  
**Translation:** 

**[5040.00s] English:** It really is the best way to support this podcast.  
**Translation:** Vocabulary: sponsors: 赞助商

**[5042.72s] English:** Go to lexfriedman.com slash sponsors.  
**Translation:** 

**[5046.26s] English:** We got Perplexity for curiosity-driven knowledge exploration, Shopify for selling stuff online,  
**Translation:** 

**[5053.04s] English:** Element for electrolytes, Finn for customer service AI agents, and Quo for a phone system  
**Translation:** 

**[5060.18s] English:** like calls, texts, contacts for your business.  
**Translation:** 

**[5063.86s] English:** Choose wisely, my friends.  
**Translation:** 

**[5065.52s] English:** And now, back to my conversation with Jensen Kwong.  
**Translation:** 

**[5070.00s] English:** Do you think NVIDIA may be worth $10 trillion at some point?  
**Translation:** 

**[5076.00s] English:** Let's ask it this way.  
**Translation:** Vocabulary: trillion: 万亿

**[5077.84s] English:** What does the future of the world look like where that's true?  
**Translation:** 

**[5084.80s] English:** I think that NVIDIA's growth is extremely likely, and in my mind, inevitable.  
**Translation:** 

**[5095.20s] English:** And let me explain why.  
**Translation:** 

**[5096.64s] English:** We're the largest computer company in history.  
**Translation:** 

**[5100.00s] English:** That alone should beg the question, why?  
**Translation:** 

**[5104.24s] English:** And the reason, of course, two reasons.  
**Translation:** 

**[5106.78s] English:** First, two foundational technical reasons.  
**Translation:** 

**[5110.46s] English:** The first reason is that computing went from being a retrieval-based, file retrieval system.  
**Translation:** 

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

**[5125.32s] English:** And we use a recommender system, some smart filter,  
**Translation:** 

**[5129.12s] English:** to figure out.  
**Translation:** Vocabulary: recommender: 推荐系统

**[5130.10s] English:** What to retrieve for you.  
**Translation:** 

**[5131.50s] English:** And so we were a pre-recording, human pre-recording, and file retrieving system.  
**Translation:** Vocabulary: retrieve: 找回; retrieving: 正在找回

**[5136.60s] English:** That's what a computer is, largely.  
**Translation:** 

**[5139.38s] English:** To now, AI computers are contextually aware,  
**Translation:** 

**[5143.42s] English:** which means that it has to process and generate tokens in real time.  
**Translation:** 

**[5147.28s] English:** So we went from a retrieval-based computing system to a generative-based computing system.  
**Translation:** Vocabulary: computing: 计算

**[5153.50s] English:** We're going to need a lot more processing in this new world than in the old world.  
**Translation:** 

**[5157.82s] English:** We need a lot of storage in the old world.  
**Translation:** 

**[5160.00s] English:** old world we need a lot of computation in this new world and so so that's that's the first part  
**Translation:** 

**[5167.40s] English:** of it we fundamentally changed computing in the way how computing is done the only thing that  
**Translation:** Vocabulary: computation: 计算; fundamentally: 根本上

**[5173.00s] English:** would cause it to go back is if this way of computation this way of computing generating  
**Translation:** 

**[5179.52s] English:** information that's contextually relevant situationally aware that is grounded on new  
**Translation:** Vocabulary: situationally: 情境地

**[5186.40s] English:** insight before it generates information this computation intensive way of doing computing  
**Translation:** 

**[5192.36s] English:** would only go back if it's not effective so for the last 10-15 years while working on deep learning  
**Translation:** 

**[5200.06s] English:** if at any single moment i would have come to the conclusion that that you know what this is not  
**Translation:** 

**[5207.70s] English:** going to work out i think this is a dead end or it's not going to scale it's not going to solve  
**Translation:** 

**[5212.00s] English:** this modality not going to be used in this application then of course i would feel very  
**Translation:** 

**[5216.26s] English:** different  
**Translation:** Vocabulary: modality: 治疗方式

**[5216.40s] English:** about it but i think the last five years has given me more confidence than the last 10 years  
**Translation:** 

**[5223.62s] English:** the previous 10 years the second idea is computers because it was a storage system  
**Translation:** 

**[5229.70s] English:** it was largely a warehouse we're now building factories warehouses don't make much money  
**Translation:** 

**[5238.58s] English:** factories directly correlates with a company's revenues  
**Translation:** Vocabulary: correlates: 相关联; revenues: 收入; warehouses: 仓库

**[5244.10s] English:** and so  
**Translation:** 

**[5246.40s] English:** the computer did two things not only did it change the way it did it its purpose in the world  
**Translation:** 

**[5255.08s] English:** changed it's no longer a computer it's a factory it's a factory is used for generation of revenues  
**Translation:** 

**[5262.86s] English:** we're now seeing not only is this factory generating products commodities that people  
**Translation:** 

**[5271.04s] English:** want to consume we're seeing that the commodities are so interesting so  
**Translation:** 

**[5276.26s] English:** valuable so to so many different audiences  
**Translation:** 

**[5280.00s] English:** that the tokens are starting to segment, like iPhones.  
**Translation:** 

**[5283.66s] English:** You have free tokens, you have premium tokens,  
**Translation:** Vocabulary: premium: 高级的

**[5287.88s] English:** and you have several tokens in the middle.  
**Translation:** 

**[5290.26s] English:** And so intelligence, as it turns out,  
**Translation:** 

**[5293.42s] English:** you know, it's a scalable product.  
**Translation:** 

**[5295.40s] English:** There's extremely high intelligence products,  
**Translation:** Vocabulary: scalable: 可扩展的

**[5297.84s] English:** tokens that are used for specialized things.  
**Translation:** 

**[5300.60s] English:** People will be willing to pay, you know,  
**Translation:** 

**[5302.76s] English:** the idea that somebody's willing to pay  
**Translation:** 

**[5304.74s] English:** $1,000 per million tokens is just around the corner.  
**Translation:** 

**[5309.70s] English:** It's not if, it's only when.  
**Translation:** 

**[5312.44s] English:** And so now we're seeing that the commodity  
**Translation:** Vocabulary: commodity: 商品

**[5316.32s] English:** that this factory makes is actually valuable  
**Translation:** 

**[5319.12s] English:** and is revenue generating and profit generating.  
**Translation:** 

**[5322.40s] English:** Now the question is, how many of these factories  
**Translation:** 

**[5324.84s] English:** does the world need?  
**Translation:** 

**[5327.90s] English:** How many tokens does the world need?  
**Translation:** 

**[5331.98s] English:** And how much is society willing to pay for these tokens?  
**Translation:** 

**[5338.88s] English:** And...  
**Translation:** 

**[5339.70s] English:** What would happen to the world's economy  
**Translation:** 

**[5341.82s] English:** if the productivity were to improve so substantially?  
**Translation:** 

**[5346.82s] English:** What would happen?  
**Translation:** 

**[5348.48s] English:** Are we going to discover new drugs, new products, new services?  
**Translation:** 

**[5352.44s] English:** And so when you take these things in combination,  
**Translation:** 

**[5355.64s] English:** I am absolutely certain  
**Translation:** 

**[5357.06s] English:** that the world's GDP is going to accelerate in growth.  
**Translation:** 

**[5362.12s] English:** I'm absolutely certain the percentage of that GDP  
**Translation:** 

**[5366.56s] English:** that will be used for computation,  
**Translation:** Vocabulary: computation: 计算

**[5369.70s] English:** will be a hundred times more than the past  
**Translation:** 

**[5372.52s] English:** because it's no longer a storage unit.  
**Translation:** 

**[5375.60s] English:** It's a product generation unit.  
**Translation:** 

**[5378.48s] English:** And so when you look at it in that context,  
**Translation:** 

**[5381.78s] English:** and then you back into what is NVIDIA's,  
**Translation:** 

**[5385.18s] English:** what does NVIDIA do?  
**Translation:** 

**[5387.78s] English:** And how much of that new economics, new industry,  
**Translation:** 

**[5393.28s] English:** would we have to benefit to address?  
**Translation:** 

**[5396.24s] English:** I think we're going to be a lot, lot bigger.  
**Translation:** 

**[5398.46s] English:** And then the rest of it,  
**Translation:** 

**[5399.62s] English:** we're going to be a lot bigger.  
**Translation:** 

**[5400.00s] English:** To me, is it possible for NVIDIA to be a $3 trillion revenues company in the near future?  
**Translation:** Vocabulary: revenues: 收入; trillion: 万亿

**[5408.56s] English:** The answer is, of course, yes.  
**Translation:** 

**[5410.20s] English:** And the reason for that is because it's not limited by any physical limits.  
**Translation:** 

**[5415.20s] English:** There's nothing that I see that says, gosh, $3 trillion is not possible.  
**Translation:** 

**[5421.22s] English:** And as it turns out, NVIDIA supply chain is the burden is shared by 200 companies.  
**Translation:** 

**[5431.04s] English:** And the fact that we scale out on the backs of with the partnership of this ecosystem, the question is, do we have the energy to do so?  
**Translation:** 

**[5441.34s] English:** And surely we will have the energy to do so.  
**Translation:** 

**[5445.16s] English:** And so all of these things combined, that number is just a number.  
**Translation:** 

**[5451.22s] English:** And I still remember NVIDIA was the first time we crossed a billion dollars.  
**Translation:** 

**[5457.76s] English:** I was reminded of a CEO who told me, Jensen, it's theoretically impossible for a fabulous semiconductor company to exceed a billion dollars.  
**Translation:** 

**[5467.68s] English:** And I won't bore you with why, but of course, it's illogical and there's a lot of evidence we're not.  
**Translation:** Vocabulary: illogical: 不合逻辑; semiconductor: 半导体; theoretically: 理论上

**[5474.74s] English:** And then somebody told me, Jensen, you'll never be more than $25 billion.  
**Translation:** 

**[5479.94s] English:** Because of some other company, somebody told me that you'll never be, you know, because, and then so that those, those aren't principle first principle reason thinking.  
**Translation:** 

**[5492.18s] English:** And the simple, the simple way to think about that is what is it that we make and how large is the opportunity that we can create?  
**Translation:** 

**[5502.02s] English:** Now, NVIDIA is not in the market share business.  
**Translation:** 

**[5504.98s] English:** Almost everything that I just talked about don't exist.  
**Translation:** 

**[5508.68s] English:** That's the part that's hard.  
**Translation:** 

**[5509.94s] English:** You know, if NVIDIA was a, was a, was a $10 billion company trying to take NVIDIA share, then it's easy to see for shareholders.  
**Translation:** 

**[5520.00s] English:** that, oh yeah, if they could just take 10% share, they could be this much larger. But it's hard for  
**Translation:** Vocabulary: shareholders: 股东

**[5528.02s] English:** people to imagine how large we could be because there's nobody I could take share from.  
**Translation:** 

**[5533.78s] English:** You know? And so I think that that's one of the challenges for the world is the imagination of  
**Translation:** 

**[5540.14s] English:** the future. But I got plenty of time and I'll keep reasoning about it and I'll keep talking  
**Translation:** 

**[5544.16s] English:** about it and every single GTC will become more and more real, you know, and then more and more  
**Translation:** 

**[5549.38s] English:** people talk about it in one of these days, you know, we'll get there, but I'm a hundred percent  
**Translation:** 

**[5553.50s] English:** we'll get there. Yeah. This view of, you know, token factories, essentially this token per second  
**Translation:** Vocabulary: token: 代币

**[5559.72s] English:** per watt and every token having value, like it's an actual thing that brings value and it brings  
**Translation:** 

**[5566.10s] English:** different kinds of value, different amounts of value to different people with value. That's the  
**Translation:** 

**[5570.02s] English:** actual product is really can be loosely thought of as the token. And so you have a bunch of token  
**Translation:** 

**[5574.26s] English:** factors and it's very easy. First principle is to imagine a future given all the potential things  
**Translation:** 

**[5579.28s] English:** that AI can solve that you're going to need an exponential number more of token factories.  
**Translation:** 

**[5585.16s] English:** Yeah. And what's really interesting, the reason why I was so excited about it,  
**Translation:** Vocabulary: exponential: 指数的

**[5589.78s] English:** the iPhone of tokens arrived. What do you call it? Wait, are you saying open clause iPhone?  
**Translation:** 

**[5593.86s] English:** Yeah. That's interesting. Agents. Yeah. Agents. True. Agents in general. The iPhone of tokens  
**Translation:** 

**[5600.68s] English:** arrived. It is the fastest growing application in history. It went straight up. Yeah. Went  
**Translation:** 

**[5606.02s] English:** straight up. That says something. Yup. There's no question.  
**Translation:** 

**[5609.28s] English:** Open claw is the iPhone of tokens. Yeah. There's something truly, as you know,  
**Translation:** 

**[5614.58s] English:** something truly special happening from about December where people really woke up to the  
**Translation:** 

**[5620.36s] English:** power of cloud code of codex of open claw. Um, I mean, I've embarrassed to admit that on the way  
**Translation:** 

**[5628.28s] English:** here in the airport, I'm this first time I've done this in public, I was programming quote unquote  
**Translation:** Vocabulary: unquote: 引用结束

**[5636.30s] English:** by talking.  
**Translation:** 

**[5637.96s] English:** Yeah.  
**Translation:** 

**[5639.28s] English:** And I was embarrassed.  
**Translation:** 

**[5640.00s] English:** Because I was pretending like I'm talking to a human colleague.  
**Translation:** Vocabulary: colleague: 同事

**[5643.82s] English:** I'm not sure how I feel about the future where everybody is walking around talking to their AI, but it's such an efficient way to get stuff done.  
**Translation:** 

**[5653.12s] English:** And it's more likely that your AI is bothering you all the time.  
**Translation:** 

**[5657.76s] English:** And the reason for that is because it's getting stuff done so fast.  
**Translation:** 

**[5661.80s] English:** It's reporting back to you, I got that done.  
**Translation:** 

**[5664.34s] English:** What do you want me to do next?  
**Translation:** 

**[5665.52s] English:** You know, that's the part that I think most people don't realize is the person who's going to be chatting with them, texting them most, is their claw, is their lobster.  
**Translation:** Vocabulary: lobster: 龙虾

**[5677.50s] English:** What an incredible future.  
**Translation:** 

**[5679.88s] English:** I read that you attribute a lot of your success to your ability to work harder than anyone and withstand more suffering than anyone.  
**Translation:** Vocabulary: attribute: 归因; withstand: 承受

**[5686.56s] English:** So we can list many of the things that entails.  
**Translation:** 

**[5690.50s] English:** I mean, dealing with failure, the cost of engineering problems we've talked about.  
**Translation:** Vocabulary: entails: 包含

**[5695.52s] English:** The human problems, uncertainty, responsibility, exhaustion, embarrassment, the near-death company moments that you've mentioned.  
**Translation:** 

**[5705.68s] English:** But also the pressure.  
**Translation:** Vocabulary: exhaustion: 疲劳

**[5707.52s] English:** Now as the CEO of this company that economies and nations strategize around, plan their financial allocations around, plan their AI infrastructure around.  
**Translation:** 

**[5723.06s] English:** How do you deal with this much pressure?  
**Translation:** Vocabulary: allocations: 资金分配; strategize: 制定策略

**[5725.52s] English:** What gives you strength given how many nations and peoples depend on you?  
**Translation:** 

**[5737.28s] English:** I'm conscious about the fact that NVIDIA's success is very important to the United States.  
**Translation:** 

**[5746.70s] English:** We generate enormous amounts of tax revenues.  
**Translation:** 

**[5750.88s] English:** We establish technology leadership for our nation.  
**Translation:** Vocabulary: revenues: 税收收入

**[5754.20s] English:** Technology leadership is important.  
**Translation:** 

**[5755.52s] English:** It's important for national security.  
**Translation:** 

**[5757.32s] English:** National security not just in one aspect.  
**Translation:** 

**[5760.00s] English:** of national security, all aspects of national security. When our country is more prosperous,  
**Translation:** 

**[5765.28s] English:** we could do a better job with domestic policies and helping social benefits. Because we're  
**Translation:** 

**[5771.74s] English:** generating so much re-industrialization in the United States, we're creating mountains of jobs.  
**Translation:** 

**[5777.42s] English:** We're helping shift how we build things back to the United States in so many different plants,  
**Translation:** 

**[5787.84s] English:** chips, computers, and of course, these manufactories. I'm completely aware  
**Translation:** Vocabulary: manufactories: 工厂

**[5793.68s] English:** and I have the benefit, and this is a real gift with mainstream investors,  
**Translation:** 

**[5805.54s] English:** teachers, policemen who have somehow, for whatever reason, invested in NVIDIA or because they watched  
**Translation:** 

**[5812.98s] English:** Jim Cramer, bought some stock and now are millionaires.  
**Translation:** 

**[5817.84s] English:** And I am completely aware of that circumstance. I'm aware of the circumstance that NVIDIA  
**Translation:** Vocabulary: circumstance: 情况; millionaires: 百万富翁

**[5826.64s] English:** is central to a very large network of ecosystem partners behind us and downstream from us.  
**Translation:** 

**[5836.74s] English:** And so the way I deal with that is exactly what I just did. I reasoned about  
**Translation:** 

**[5842.94s] English:** what is it that we're doing? What is it causing?  
**Translation:** 

**[5847.84s] English:** What's the impact that has on other people positively or even through great burden,  
**Translation:** 

**[5855.84s] English:** for example, to supply chain? And the question is, therefore, what are you going to do about it?  
**Translation:** 

**[5864.42s] English:** In almost everything that I feel, I break it down. I reason about, okay,  
**Translation:** 

**[5870.16s] English:** what's the circumstance? What has changed? What's hard? And what am I going to do about it?  
**Translation:** 

**[5876.14s] English:** And I break it down.  
**Translation:** 

**[5877.84s] English:** I decompose the problem.  
**Translation:** 

**[5880.00s] English:** And the decomposition of these circumstances turns it into manageable things that I can do.  
**Translation:** Vocabulary: decompose: 分解; decomposition: 分解

**[5889.88s] English:** And the only thing that I, after that, I could do is, did you do it?  
**Translation:** 

**[5893.90s] English:** Did you either do it or did you get somebody else to do it?  
**Translation:** 

**[5897.06s] English:** And if you didn't do it, you reasoned that you need to do it and you didn't do it and you didn't get anybody else to do it, then stop crying about it, you know?  
**Translation:** 

**[5905.58s] English:** And so I'm fairly tough on myself.  
**Translation:** 

**[5913.02s] English:** But I also break things down so that I don't panic.  
**Translation:** 

**[5918.54s] English:** I can go to sleep because I've made the list of things that needed to be done.  
**Translation:** 

**[5923.24s] English:** And I've made sure that everything that could put our company in harm's way, could put my partners in harm's way, put our industry in harm's way, I've told somebody.  
**Translation:** 

**[5934.04s] English:** Everything that I feel.  
**Translation:** 

**[5935.58s] English:** Could put anybody in harm's way, I've told someone.  
**Translation:** 

**[5940.18s] English:** And I've told that someone who could do something about it.  
**Translation:** 

**[5943.42s] English:** And so I've gotten it off my chest.  
**Translation:** 

**[5945.16s] English:** Or I'm doing something about it.  
**Translation:** 

**[5947.32s] English:** And so after that, Lex, what else can you do?  
**Translation:** 

**[5950.54s] English:** So given all the insane, intense amount of suffering on the journey of building up NVIDIA, have you hit low points psychologically?  
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

**[5973.76s] English:** And part of, you know, Lex, part of it is forgetting.  
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

**[5994.90s] English:** One of the things that I do very quickly is I decompose the problem.  
**Translation:** 

**[5996.76s] English:** I reason about the problem.  
**Translation:** 

**[5997.96s] English:** And I share the load with it.  
**Translation:** 

**[5999.72s] English:** When I say.  
**Translation:** 

**[6000.00s] English:** I tell everybody, I'm essentially sharing that burden as quickly as possible. Whatever worries  
**Translation:** 

**[6007.14s] English:** me, tell somebody else, don't just keep it, you know, decompose, don't, don't freak them out,  
**Translation:** 

**[6013.02s] English:** decompose the problem into smaller parts and get people to, and inspire them to be able to go do  
**Translation:** Vocabulary: decompose: 分解

**[6019.66s] English:** something about it. But part of it is just, just forgetting, you know, I, a lot of it is you got  
**Translation:** 

**[6025.64s] English:** to be tough on yourself, you know, just come on, stop crying about it. Let's get going, you know,  
**Translation:** 

**[6030.26s] English:** and then you get out of bed. And then the other part is, is, um, you, you, you're attracted to  
**Translation:** 

**[6036.12s] English:** the next shiny light, the next future, you know, the next opportunity, the next, okay, that's  
**Translation:** 

**[6041.08s] English:** behind us. What's next? And it's a lot, I think, you know, you watch this with great athletes,  
**Translation:** 

**[6046.56s] English:** they, they just worry about the next point. The last point is behind them, the embarrassment,  
**Translation:** 

**[6054.16s] English:** the, you know,  
**Translation:** 

**[6055.64s] English:** you know, and then, and because I do so much of my job publicly, you know, Lex, you do a fair  
**Translation:** 

**[6062.82s] English:** amount of your job publicly too. And so, so I do a lot of my job publicly. And so, um, you know,  
**Translation:** 

**[6068.38s] English:** I, I say a lot of things that, that seem sensible at the time or funny at the time, mostly it's  
**Translation:** Vocabulary: sensible: 合乎情理

**[6073.80s] English:** just because it's funny to me at the time. And then, you know, you reflect on it, it's less  
**Translation:** 

**[6077.92s] English:** funny, but, but yeah, no, trust me. I know, but you basically allow yourself to be pulled by  
**Translation:** 

**[6084.76s] English:** the light of the moment.  
**Translation:** 

**[6085.64s] English:** of the future. Forget the past and just keep, keep, keep working towards that. I mean, you did  
**Translation:** 

**[6090.62s] English:** say there's this kind of famous thing. You said that, um, if you knew how hard it would be to  
**Translation:** 

**[6098.14s] English:** build NVIDIA, uh, it turned out to be, what is it? A million times more hard than you anticipated  
**Translation:** 

**[6104.56s] English:** that you wouldn't do it. Um, but it isn't, you know, when I hear that, that's probably true  
**Translation:** 

**[6112.02s] English:** about everything worth doing, right?  
**Translation:** 

**[6113.68s] English:** Exactly.  
**Translation:** 

**[6115.64s] English:** Because by the way, what I was trying to explain is that there's a, there's a,  
**Translation:** 

**[6120.00s] English:** incredible superpower of being um being being uh have the mind of a child yeah you know and i say  
**Translation:** 

**[6128.76s] English:** to myself oftentimes when i look at something and and almost almost everything um my first  
**Translation:** Vocabulary: oftentimes: 经常; superpower: 超能力

**[6136.54s] English:** thought is how hard can it be you know and so and so you get yourself into that mode how hard could  
**Translation:** 

**[6143.34s] English:** it be and and nobody's ever done it it looks gigantic it's going to cost hundreds of billions  
**Translation:** Vocabulary: gigantic: 巨大的

**[6150.18s] English:** of dollars it's going to take you know all this and you just go yeah but how hard could it be  
**Translation:** 

**[6154.84s] English:** you know yeah how hard could it be yeah and and so so you got to get yourself into that state of  
**Translation:** 

**[6160.00s] English:** mind you don't want to you don't want to actually over simulate everything and all the setbacks and  
**Translation:** 

**[6167.00s] English:** all the trials and tribulations and all the disappointments you don't want to simulate all  
**Translation:** Vocabulary: disappointments: 失望; setbacks: 挫折; simulate: 模拟; tribulations: 磨难

**[6170.86s] English:** that in advance you don't want to know that you don't you don't want to know that you don't want  
**Translation:** 

**[6173.32s] English:** want to go into a new experience thinking it's going to be perfect. It's going to be great.  
**Translation:** 

**[6177.86s] English:** It's going to be incredibly fun. And then while you're there, you need to have endurance. You  
**Translation:** 

**[6184.50s] English:** need to have grit so that when the setbacks actually happened, and those setbacks are  
**Translation:** Vocabulary: endurance: 毅力

**[6189.52s] English:** going to surprise you, the disappointments aren't going to surprise you, the embarrassments are  
**Translation:** 

**[6194.66s] English:** going to surprise you, the humiliations are going to surprise you. Now you just got to turn on the  
**Translation:** Vocabulary: embarrassments: 尴尬; humiliations: 羞辱

**[6200.58s] English:** other bit, which is just forget about it. Move on. Keep moving. And to the extent that  
**Translation:** 

**[6205.78s] English:** my assumptions about the future and why the future is going to manifest,  
**Translation:** Vocabulary: assumptions: 假设; manifest: 显现

**[6215.66s] English:** so long as those assumptions and that input doesn't change or didn't change materially,  
**Translation:** 

**[6222.56s] English:** then I should expect that the output won't change. And so my simulated output of the future  
**Translation:** Vocabulary: simulated: 模拟

**[6228.74s] English:** is still going to happen.  
**Translation:** 

**[6230.58s] English:** And if it's still going to happen, I'm still going to go after it. I believe it's going to,  
**Translation:** 

**[6235.22s] English:** you know, and so there's a combination of two or three human characteristics.  
**Translation:** 

**[6240.00s] English:** the ability to go into a into an experience fresh-minded the ability to forget the setbacks  
**Translation:** 

**[6247.28s] English:** the ability to believe in yourself you know to believe what you believe and stay  
**Translation:** 

**[6253.62s] English:** stay true to that belief um but you're constantly re-evaluating this combination of  
**Translation:** 

**[6261.20s] English:** three four five things i think is is really important for resilience and and um  
**Translation:** 

**[6268.64s] English:** and you know i i'm fortunate that that whatever whatever life experience has led to this i've got  
**Translation:** Vocabulary: resilience: 韧性

**[6275.60s] English:** kind of those four or five things you know i'm always curious always learning i'm always learning  
**Translation:** 

**[6281.22s] English:** from everybody you know i'm always asking what and because i'm humble about about about everything  
**Translation:** 

**[6286.94s] English:** i'm always thinking gosh they did that so nicely they did that so wonderfully you know i wonder  
**Translation:** 

**[6293.30s] English:** what they're thinking through how do they you know so i'm simulating everybody in a lot of ways  
**Translation:** Vocabulary: simulating: 模拟

**[6298.64s] English:** you know emulating almost everybody i watch right you're you're empathetic towards  
**Translation:** 

**[6303.02s] English:** towards everything that they do that that you're observing and respect and  
**Translation:** Vocabulary: empathetic: 感同身受; emulating: 模仿

**[6306.96s] English:** and so you you're constantly learning and you know you're now one of the wealthiest people on earth  
**Translation:** 

**[6314.22s] English:** one of the most successful humans on earth is it harder to be humble and to be able to  
**Translation:** Vocabulary: wealthiest: 最富有的人

**[6320.88s] English:** do you feel the effect of money and power and fame in making it harder for you to  
**Translation:** 

**[6328.64s] English:** sort of be wrong in your own head enough to  
**Translation:** 

**[6334.00s] English:** hear out an opinion of somebody else when it disagrees with you and learn from them  
**Translation:** 

**[6337.84s] English:** those kinds of things um surprisingly no and and i would i would actually go the other way  
**Translation:** 

**[6346.40s] English:** because i do so much of my work publicly when i'm wrong pretty much everybody sees it  
**Translation:** 

**[6353.52s] English:** you get humbled yeah and and uh and when i'm wrong when i'm wrong or  
**Translation:** 

**[6358.64s] English:** when things didn't turn out that way or  
**Translation:** 

**[6360.00s] English:** um you know i mean most of the things that that i say outside um i'm fairly certain about and the  
**Translation:** 

**[6368.40s] English:** reason for that is because because it's going to impact somebody else and i want to be quite  
**Translation:** 

**[6372.70s] English:** concerned about that and quite quite circumspect about that um for stuff that that i'm reasoning  
**Translation:** Vocabulary: circumspect: 谨慎

**[6378.32s] English:** about inside a meeting you know a lot of things could turn out differently and so but it doesn't  
**Translation:** 

**[6384.54s] English:** ever stop me from reasoning the way that the way that i manage and lead uh you know i'm constantly  
**Translation:** 

**[6390.92s] English:** reasoning in front of people and even when i'm talking to you you can kind of see me kind of  
**Translation:** 

**[6394.64s] English:** reasoning through things and i want to make sure that you understand what i'm saying not because  
**Translation:** 

**[6398.34s] English:** i told you because i'm so humble about what i'm about to tell you i kind of show you the steps  
**Translation:** 

**[6404.80s] English:** that i got there and then you could decide whether you believe what i said in the end  
**Translation:** 

**[6408.44s] English:** and so i'm doing that all day long in meetings with all of my employees i'm constantly reasoning  
**Translation:** 

**[6414.30s] English:** through  
**Translation:** 

**[6414.52s] English:** let me tell you let me tell you what how i see it and i reason through it it gives everybody  
**Translation:** 

**[6419.52s] English:** the opportunity to intercept and say i disagree with that part the nice thing about reasoning  
**Translation:** 

**[6425.26s] English:** through things and letting and letting people interact with it is that they don't have to  
**Translation:** 

**[6429.74s] English:** disagree with your outcome they can disagree with your reasoning steps and they could pull me in  
**Translation:** 

**[6436.22s] English:** different directions and then we can reason forward and so we're we're kind of you know  
**Translation:** 

**[6444.48s] English:** collective  
**Translation:** 

**[6444.52s] English:** path searching method and it's really fantastic yeah you have this way about you of when you're  
**Translation:** 

**[6452.92s] English:** explaining stuff i can feel you actually reasoning on the spot about it with a constant open-mindedness  
**Translation:** 

**[6459.98s] English:** where you could i could feel like i could steer your thinking yeah and that's a that's really  
**Translation:** 

**[6465.52s] English:** beautiful that you've been able to maintain that after so many years of success and pain  
**Translation:** 

**[6469.84s] English:** i think sometimes pain makes you close closes you down a bit  
**Translation:** 

**[6474.48s] English:** yeah and i think you maintain tolerance for embarrassment i think it's  
**Translation:** Vocabulary: tolerance: 忍耐

**[6480.00s] English:** That's the tolerance.  
**Translation:** 

**[6481.52s] English:** I mean, that's a real thing.  
**Translation:** 

**[6483.00s] English:** Yeah.  
**Translation:** 

**[6483.50s] English:** There's many years of embarrassing yourself, even those meetings, knowing that there's people around you where you declared one idea and it was shown that that idea was wrong and be able to admit that and to grow from that.  
**Translation:** 

**[6495.34s] English:** That's not, that's very difficult on a human level.  
**Translation:** 

**[6497.86s] English:** Yeah.  
**Translation:** 

**[6498.22s] English:** Well, you know, they knew I was, they knew that recently my first job was, was, you know, cleaning toilets.  
**Translation:** 

**[6504.32s] English:** So I'm glad you maintain that same spirit of Denny's, um, the, the work.  
**Translation:** 

**[6510.30s] English:** I mean, that, that was beautiful.  
**Translation:** 

**[6511.26s] English:** Your whole journey from starting from Denny's is a beautiful one.  
**Translation:** 

**[6514.72s] English:** Uh, let me ask you about video games.  
**Translation:** 

**[6518.22s] English:** So I'm a big gaming fan.  
**Translation:** 

**[6520.56s] English:** Yeah.  
**Translation:** 

**[6521.32s] English:** So I have to say thank you to Nvidia for many years of incredible graphics.  
**Translation:** 

**[6526.92s] English:** Um, by the way, it is, GeForce is our still to this day.  
**Translation:** 

**[6530.74s] English:** Yeah.  
**Translation:** 

**[6531.14s] English:** Our number one marketing strategy.  
**Translation:** 

**[6535.20s] English:** Right.  
**Translation:** 

**[6535.72s] English:** People learn about Nvidia while they're in their teenage years and then they go to college and they know who Nvidia is.  
**Translation:** 

**[6542.14s] English:** And then in the beginning it's just, you know, playing Call of Duty, you know, you know, Fortnite.  
**Translation:** Vocabulary: fortnite: 战术竞技游戏

**[6547.24s] English:** And then later they're using CUDA and then later they're using Nvidia on, you know, Blender and Dassault and Autodesk.  
**Translation:** 

**[6556.26s] English:** I mean, I should say, I mentioned to a friend that I'm, uh, talking with you, he said, oh, they make great gaming.  
**Translation:** Vocabulary: autodesk: Autodesk; dassault: 达索系统

**[6564.32s] English:** I mean, GPUs.  
**Translation:** 

**[6565.22s] English:** Yeah, exactly.  
**Translation:** 

**[6566.54s] English:** Exactly.  
**Translation:** 

**[6567.18s] English:** You know, there's, there's more to it, but, but yeah, yeah.  
**Translation:** 

**[6570.88s] English:** People really love the, it really brought a lot of joy to a lot of people.  
**Translation:** 

**[6574.40s] English:** The, the, the hardware really brings these worlds to life.  
**Translation:** 

**[6578.36s] English:** Uh, there was some controversy around this, uh, with DLSS five.  
**Translation:** 

**[6583.84s] English:** Yeah.  
**Translation:** 

**[6584.02s] English:** Can you explain to me the drama around this?  
**Translation:** 

**[6586.12s] English:** Uh, I guess people, gamers online were concerned that it makes games look like AI slop.  
**Translation:** 

**[6593.68s] English:** Yeah.  
**Translation:** 

**[6594.32s] English:** Uh, what do you think of this drama?  
**Translation:** 

**[6596.28s] English:** Yeah.  
**Translation:** 

**[6597.32s] English:** I think their, their perspective makes.  
**Translation:** 

**[6599.96s] English:** Yeah.  
**Translation:** 

**[6600.00s] English:** sense, and I could see where they're coming from, because I don't love AI slot myself.  
**Translation:** 

**[6605.76s] English:** You know, all of the AI-generated content increasingly looks similar, and they're all  
**Translation:** 

**[6613.14s] English:** beautiful, and I'm empathetic towards what they're thinking. That's just not what DLSS 5  
**Translation:** Vocabulary: empathetic: 同情理解

**[6620.32s] English:** is trying to do. I showed several examples of it, but DLSS 5 is 3D-conditioned, 3D-guided,  
**Translation:** 

**[6630.00s] English:** it's ground-truth, structured data-guided. And so the artist determined the geometry.  
**Translation:** Vocabulary: geometry: 几何结构

**[6636.48s] English:** We are completely truthful to the geometry, maintain so in every single frame.  
**Translation:** 

**[6643.90s] English:** It's conditioned by the textures, the artistry of the artist. And so every single frame,  
**Translation:** Vocabulary: artistry: 艺术风格; truthful: 真实

**[6650.96s] English:** it enhances, but it doesn't change anything. Now, the question is, the question about enhancing,  
**Translation:** 

**[6659.10s] English:** DLSS 5 also...  
**Translation:** Vocabulary: enhances: 提升; enhancing: 提升

**[6660.00s] English:** Because the system is open, you could train your own models to determine, and you could  
**Translation:** 

**[6667.16s] English:** even, in the future, prompt it. You know, I want it to be a toon shader. I want it to  
**Translation:** Vocabulary: shader: 着色器

**[6671.92s] English:** look like this kind of... So you can give it even an example, and it would generate  
**Translation:** 

**[6677.26s] English:** in the style of that, all consistent with the artistry, the style, the intent of the  
**Translation:** 

**[6684.96s] English:** artist. And so all of that is done for the artist.  
**Translation:** 

**[6690.00s] English:** So that they can create something that is more beautiful, but still in the style that  
**Translation:** 

**[6695.94s] English:** they want. I think that they got the impression that the games are going to come out the way  
**Translation:** 

**[6703.40s] English:** the games are, ship the way they do, and then we're going to post-process it. That's not  
**Translation:** 

**[6709.18s] English:** what DLSS is intended to do. DLSS is integrated with the artist. And so it's about giving  
**Translation:** 

**[6715.94s] English:** the artist the tool of AI, the tool of generative AI. They could design it. They could design it.  
**Translation:** Vocabulary: generative: 生成式

**[6720.00s] English:** to use it you know i think people are very sensitive to human faces yeah and we're now  
**Translation:** 

**[6725.04s] English:** living in this moment which i think is a is a beautiful one which is people are sensitive to  
**Translation:** 

**[6729.92s] English:** ai slop yeah it puts a mirror to ourselves to help us realize that what we seek is imperfections what  
**Translation:** 

**[6736.48s] English:** we seek is sometimes not perfect graphics it helps us understand what we find compelling  
**Translation:** Vocabulary: compelling: 有吸引力的

**[6742.64s] English:** in the worlds we create and that's beautiful and as long as it's tools that help us create those  
**Translation:** 

**[6747.66s] English:** worlds yeah that's right it's wonderful that's right it's yet yet another tool and they want  
**Translation:** 

**[6751.84s] English:** the generative uh models to generate the opposite of photo reel yeah it'll do that too  
**Translation:** 

**[6759.90s] English:** and so it's just yet another tool i think the um the gamers might might also appreciate that  
**Translation:** 

**[6766.34s] English:** that um in the last couple years we we introduced uh skin shaders to the game developers  
**Translation:** 

**[6776.66s] English:** and many  
**Translation:** Vocabulary: shaders: 着色器

**[6777.64s] English:** of those games have skin shaders that include subsurface scattering that make skin look more  
**Translation:** 

**[6783.98s] English:** skin like and so the industries game developers are looking for more and more and more tools  
**Translation:** Vocabulary: scattering: 散射; subsurface: 次表面

**[6790.72s] English:** to express their art and so this is just yet more one more tool they get to decide what to use  
**Translation:** 

**[6796.46s] English:** ridiculous question uh what do you think is the greatest or most influential game ever made  
**Translation:** 

**[6801.48s] English:** maybe from nvidia's perspective doom doom unquestionably that was the start of the 3d  
**Translation:** 

**[6808.30s] English:** i would say doom from a from our the intersection of the cultural implication as well as the  
**Translation:** Vocabulary: implication: 影响; intersection: 交汇点

**[6814.60s] English:** industry turning a pc into a gaming device that was a very important moment now of course  
**Translation:** 

**[6820.90s] English:** flight simulation companies were before it and um but they just didn't have the popularity that  
**Translation:** Vocabulary: simulation: 模拟

**[6826.94s] English:** doom did to have made the industry turn the pc from a  
**Translation:** 

**[6831.00s] English:** obviously  
**Translation:** 

**[6831.48s] English:** office automation tool into a personal computer for families and gamers and things like that and  
**Translation:** 

**[6837.36s] English:** so doom was really impactful there from a from an actual  
**Translation:** Vocabulary: automation: 自动化

**[6840.00s] English:** game technology perspective i would say virtual fighter and so we're great friends with both of  
**Translation:** 

**[6846.06s] English:** them you know and then there's games more recently i mean cyberpunk 2077 really nice gpu  
**Translation:** Vocabulary: cyberpunk: 赛博朋克

**[6853.84s] English:** accelerated graphics like fully ray traced fully ray traced um also i like at first i'm a huge fan  
**Translation:** 

**[6861.22s] English:** of skyrim uh elder scrolls and the you know it's been released a long long time ago but people  
**Translation:** Vocabulary: accelerated: 加速; scrolls: 卷轴

**[6867.36s] English:** release mods and they love these i mean it's like a different game and it just allows me to  
**Translation:** 

**[6874.96s] English:** replay the game over and over and you get it makes you realize that you can re-experience  
**Translation:** 

**[6880.98s] English:** in a totally new way the world you already love yeah so i do that all the time one of my favorite  
**Translation:** 

**[6886.66s] English:** things just walk around skyrim we created this thing called rtx mod uh-huh yeah it's a modding  
**Translation:** 

**[6892.14s] English:** tool awesome it allows it allows the community to inject the latest  
**Translation:** 

**[6897.36s] English:** technology into an old game of course like what makes a great video game is not just graphics  
**Translation:** 

**[6903.00s] English:** it's also story and character development but that's right beautiful graphics can add to the  
**Translation:** 

**[6909.08s] English:** the immersion the feeling like it's another place you're transported to  
**Translation:** Vocabulary: immersion: 身临其境; transported: 被带入

**[6914.32s] English:** uh what's uh you said i think accurately that the agi timeline  
**Translation:** 

**[6920.32s] English:** question rests on your definition of agi  
**Translation:** 

**[6925.00s] English:** so let's  
**Translation:** 

**[6927.36s] English:** let me ask you about possible timelines here let's this ridiculous definition perhaps of what agi is  
**Translation:** Vocabulary: timelines: 时间轴

**[6935.04s] English:** but an ai system that's able to essentially do your job so run no start grow and run a successful  
**Translation:** 

**[6948.80s] English:** technology company that's worth a good one or a one no it has to be worth more than a billion  
**Translation:** 

**[6957.36s] English:** dollars more more than a billion dollars  
**Translation:** 

**[6960.00s] English:** so you know you know how hard it is to do all those components so how far are we away from  
**Translation:** 

**[6968.36s] English:** that so we're talking about open claw that does all the incredibly complex stuff that are required  
**Translation:** 

**[6977.22s] English:** to to first of all innovate to find customers to sell to them to to manage to build a team  
**Translation:** Vocabulary: innovate: 创新

**[6984.10s] English:** of some agents some humans all that kind of stuff is this 5 10 15 20 years away i think it's now i  
**Translation:** 

**[6992.52s] English:** think we've achieved agi you think you can have a company run by an ai system like this possible  
**Translation:** 

**[6997.78s] English:** and the reason for that is this you said a billion and you didn't say forever and and so for example  
**Translation:** 

**[7004.26s] English:** it is not out of the question that a claw was able to create a web service  
**Translation:** 

**[7014.10s] English:** some interesting little app that all of a sudden you know a few billion people used  
**Translation:** 

**[7023.98s] English:** for 50 cents and then it went out of business again shortly after now we saw a whole bunch of  
**Translation:** 

**[7030.46s] English:** those type of companies during the internet era and most of those websites were not anything  
**Translation:** 

**[7036.30s] English:** more sophisticated than what open claw could generate today achieve virality and monetize  
**Translation:** Vocabulary: monetize: 变现; sophisticated: 复杂; virality: 病毒式传播

**[7043.12s] English:** that virality yeah  
**Translation:** 

**[7044.10s] English:** it's just i don't know what it is but i did i couldn't have predicted any of those companies  
**Translation:** 

**[7048.18s] English:** at the time either you know you're gonna get a lot of people excited with that statement  
**Translation:** 

**[7052.04s] English:** yeah no it's like what do you mean i could i could just uh launch an agent and uh make a lot  
**Translation:** 

**[7058.26s] English:** of money well by the way it's happening right now right you know that when you go to china  
**Translation:** 

**[7061.92s] English:** uh you're gonna see you're gonna see um a whole bunch of people uh teaching their getting their  
**Translation:** 

**[7067.82s] English:** claws to try to go out and look for jobs and you know do work make money and and i'm not  
**Translation:** 

**[7074.10s] English:** i'm not i'm not actually i wouldn't be surprised if some social thing happened or somebody  
**Translation:** Vocabulary: claws: 爪子

**[7080.00s] English:** created a digital influencer, super, super cute, or some social application that, you know,  
**Translation:** 

**[7087.44s] English:** feeds your little Tomagotchi or something like that. And it becomes an out of the blue and  
**Translation:** Vocabulary: influencer: 意见领袖; tomagotchi: 电子宠物

**[7093.36s] English:** instant success. A lot of people use it for a couple of months and it kind of dies away.  
**Translation:** 

**[7098.84s] English:** Now, the odds of, you know, a hundred thousand of those agents building NVIDIA is zero percent.  
**Translation:** 

**[7106.88s] English:** And, and then, and then the one part that I will, I won't do, and I, and I, I want to make sure we  
**Translation:** 

**[7114.56s] English:** all do is to recognize that people are really worried about their jobs. And, and I just want  
**Translation:** 

**[7122.04s] English:** to remind them that the purpose of your job and the tasks and the tools that you use to do your  
**Translation:** 

**[7130.86s] English:** job are related, not the same. I've been doing my job for 33 years. I'm the longest running tech  
**Translation:** 

**[7136.34s] English:** CEO in the world. I've been doing my job for 33 years. I'm the longest running tech CEO in the  
**Translation:** 

**[7136.86s] English:** world. I've been doing my job for 34 years. And the tools that I've used to do my job has changed  
**Translation:** 

**[7141.52s] English:** continuously in the last 34 years. And sometimes quite dramatically, you know, over the course of  
**Translation:** 

**[7149.72s] English:** a couple of two, three years. And, and the, the, the one story that I, I really want to make sure  
**Translation:** Vocabulary: dramatically: 急剧地

**[7154.70s] English:** that everybody hears is the story that the first job that every, that computer scientists said,  
**Translation:** 

**[7161.64s] English:** AI researchers said was going to go away was radiology because computer vision was going to  
**Translation:** 

**[7166.78s] English:** achieve that. And so, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and,  
**Translation:** 

**[7166.86s] English:** achieve superhuman levels. And it did. Computer vision was superhuman in 2019, 20, maybe, maybe a  
**Translation:** 

**[7176.92s] English:** little bit later, 2020. Okay. And so it's been a long time since computer vision has been superhuman.  
**Translation:** 

**[7182.84s] English:** And so the prediction was radiologists would go away because studying radiology scans was  
**Translation:** Vocabulary: radiologists: 放射科医生; radiology: 放射学

**[7188.76s] English:** thing of the past. AI will do that. Well, they were absolutely right.  
**Translation:** 

**[7194.78s] English:** Computer vision is completely superhuman.  
**Translation:** 

**[7196.86s] English:** every radiology platform and package today.  
**Translation:** 

**[7200.00s] English:** is driven by AI and yet the number of radiologists grew and so the question is  
**Translation:** 

**[7207.12s] English:** why and we now have a shortage of radiologists in the world and so one the  
**Translation:** 

**[7213.28s] English:** alarmist warning went too far and it scared people from doing this profession  
**Translation:** 

**[7221.16s] English:** that is so important to society and so it did harm now why was it wrong the  
**Translation:** 

**[7227.12s] English:** reason why is because the purpose of a radiologist the purpose is to diagnose  
**Translation:** Vocabulary: diagnose: 诊断; radiologist: 放射科医生

**[7232.28s] English:** disease and help patients and doctors diagnose disease and because we're able  
**Translation:** 

**[7239.84s] English:** to study scans is so much faster now you could study more scans you could  
**Translation:** 

**[7244.58s] English:** diagnose better you could you could impatient faster we can see people more  
**Translation:** 

**[7251.54s] English:** the hospitals are making more money you have more patients in the hospital you  
**Translation:** 

**[7255.92s] English:** need more radiologists  
**Translation:** 

**[7257.12s] English:** I mean the the amazing thing is it's so obvious this was going to happen the  
**Translation:** 

**[7263.54s] English:** number of software engineers at Nvidia is going to grow not decline and the  
**Translation:** 

**[7268.82s] English:** reason for that is because the purpose of a software engineer and the task of a  
**Translation:** 

**[7273.14s] English:** software dream of coding are related not the same I wanted my software engineers  
**Translation:** 

**[7277.94s] English:** to solve problems I didn't care how many lines of code they wrote you know but  
**Translation:** 

**[7282.66s] English:** their job their purpose of their job didn't change solving problems working  
**Translation:** 

**[7287.10s] English:** as a team diagnosing problems evaluating the result looking for new  
**Translation:** Vocabulary: diagnosing: 诊断问题; evaluating: 评估结果

**[7292.64s] English:** problems to solve innovation connecting dots you know none of that stuff is  
**Translation:** 

**[7298.32s] English:** going to go away do you think it's possible that let's even take coding you  
**Translation:** 

**[7302.48s] English:** think the number of programmers in the world might increase that yes and the  
**Translation:** 

**[7307.64s] English:** reason for that is this what is the definition of coding  
**Translation:** Vocabulary: programmers: 程序员

**[7311.66s] English:** I believe that is the definition coding as of today is simply specifying the  
**Translation:** 

**[7317.10s] English:** specification, and maybe  
**Translation:** Vocabulary: specification: 规范; specifying: 规定

**[7320.00s] English:** if you want to be rather directive you could even give it an architecture of the software the year  
**Translation:** 

**[7326.52s] English:** you wanted to write so the question is how many people could do that describe a specification for  
**Translation:** 

**[7332.52s] English:** a computer to go telling the computer what to go build how many people i think we just went from  
**Translation:** 

**[7338.56s] English:** 30 million to probably 1 billion and so every every carpenter in the future will be a coder  
**Translation:** Vocabulary: carpenter: 木匠

**[7347.04s] English:** except a carpenter with ai is also an architect they just increased the value that they could  
**Translation:** 

**[7355.04s] English:** deliver to the customer their their artistry just elevated tremendously i believe that every  
**Translation:** Vocabulary: artistry: 艺术造诣; elevated: 提升; tremendously: 极大程度上

**[7364.04s] English:** accountant is you know also your financial analyst also your financial advisor so all of these  
**Translation:** 

**[7370.48s] English:** professions have just been elevated and if i were a carpenter i sees a i see ai i would just  
**Translation:** 

**[7376.72s] English:** completely  
**Translation:** 

**[7377.02s] English:** go berserk you know the services i can bring to my clients if i were a plumber completely go berserk  
**Translation:** Vocabulary: berserk: 狂躁

**[7384.10s] English:** and the people that are currently programmers and software engineers i think they're at the  
**Translation:** 

**[7388.98s] English:** cutting edge of understanding intuitively how to communicate with the agents using natural  
**Translation:** Vocabulary: intuitively: 直觉地

**[7396.80s] English:** language in order to design the best kind of software that's right so over time they'll  
**Translation:** 

**[7402.32s] English:** converge but i think uh there's still value in getting i think  
**Translation:** Vocabulary: converge: 趋于一致

**[7407.02s] English:** uh learning how to program like learning what programming languages are uh the old the old  
**Translation:** 

**[7412.32s] English:** kind of programming uh what what are good practices for programming languages what are  
**Translation:** 

**[7417.80s] English:** design principles for programming languages for large software systems and the reason for that  
**Translation:** 

**[7424.96s] English:** lex and you know that i just say for the audience i think  
**Translation:** 

**[7427.64s] English:** the goal of the goal of specification the artistry of specification the goal and the artistry of it  
**Translation:** 

**[7437.02s] English:** It's going to depend on what problem you're  
**Translation:** 

**[7440.00s] English:** trying to solve. When I'm thinking about giving the company strategies and formulating corporate  
**Translation:** 

**[7447.60s] English:** directions and things that we should do, I describe it at a level that is sufficiently  
**Translation:** Vocabulary: sufficiently: 足够地

**[7455.54s] English:** specific that people generally understand the direction and it's actionable. It's so specific  
**Translation:** 

**[7464.06s] English:** enough that they can take action on it, but I under-specify it on purpose so that enable 43,000  
**Translation:** 

**[7471.70s] English:** amazing people to make it even better than I imagined. And so when I'm working with engineers,  
**Translation:** 

**[7479.30s] English:** when I'm working with people, I think about what problem am I trying to solve? Who am I working  
**Translation:** 

**[7485.84s] English:** with? And the level of specification, the level of architecture definition,  
**Translation:** 

**[7493.80s] English:** you can't just say, I'm going to do this, I'm going to do that. You can't just say, I'm going to do that.  
**Translation:** Vocabulary: specification: 详细说明

**[7494.06s] English:** Relates to that. And so everybody's going to have to learn how, where in the spectrum of  
**Translation:** 

**[7502.56s] English:** coding they want to be. Writing a specification is coding. And so you might decide to be  
**Translation:** 

**[7507.46s] English:** quite prescriptive because there's a very specific outcome you're looking for.  
**Translation:** 

**[7512.36s] English:** You might decide that this is an area you want to be much more exploratory. And so you might  
**Translation:** 

**[7518.02s] English:** under-specify and enable you to go back and forth with the AI to even push your own  
**Translation:** 

**[7523.80s] English:** boundaries of creativity. And so this artistry of where you are in the spectrum,  
**Translation:** Vocabulary: artistry: 艺术造诣

**[7528.80s] English:** this is the future of coding. But just to linger on it outside of coding, I think a lot of people,  
**Translation:** 

**[7534.66s] English:** rightfully so, are worried about their jobs, have a lot of anxiety about their jobs,  
**Translation:** 

**[7540.22s] English:** especially in the white-collar sector. I don't think any of us know what to do  
**Translation:** 

**[7549.98s] English:** with tumultuous times that always come when automations and new technologies,  
**Translation:** Vocabulary: automations: 自动化; tumultuous: 动荡的

**[7553.80s] English:** technology arrives. And I just, first of all, I think  
**Translation:** 

**[7560.00s] English:** we all need to have compassion and the responsibility to feel sort of the burden  
**Translation:** Vocabulary: compassion: 同情心

**[7565.36s] English:** of what the actual suffering feels like for individual people and families that lose their  
**Translation:** 

**[7570.32s] English:** job. I think whenever you have transformative technology like that's coming with artificial  
**Translation:** 

**[7576.04s] English:** intelligence, there's going to be a lot of pain. And I don't know what to do about that  
**Translation:** 

**[7580.20s] English:** pain. Hopefully it creates much more opportunities for those same people  
**Translation:** 

**[7584.14s] English:** for the same kind of job as the tooling evolves and makes them more productive and makes them  
**Translation:** 

**[7593.72s] English:** more fun. Hopefully as it does in the programming, I've been having so much fun programming, I have  
**Translation:** 

**[7598.50s] English:** to say, like I've never had this much fun. So hopefully it makes their job, automates the  
**Translation:** 

**[7603.00s] English:** boring parts and makes the creative parts, the ones that the human beings are responsible for,  
**Translation:** Vocabulary: automates: 自动化

**[7609.00s] English:** but still there's going to be a lot of pain and suffering. So my first recommendation before  
**Translation:** 

**[7613.98s] English:** and this is now how I deal with anxiety. In fact, we just talked about it earlier.  
**Translation:** 

**[7619.48s] English:** Enormous anxiety about the future, enormous anxiety about the pressure,  
**Translation:** 

**[7622.74s] English:** enormous anxiety about uncertainty. I first break it down and then I'm going to tell myself,  
**Translation:** 

**[7629.50s] English:** okay, there are some things you can do something about. There's some things you can't do anything  
**Translation:** 

**[7634.22s] English:** about, but for the stuff that you can do something about, let's reason about it and let's go do it.  
**Translation:** 

**[7639.88s] English:** If we were to hire a new college graduate today,  
**Translation:** 

**[7643.18s] English:** and I have a chance to do it, I'm going to tell myself, I'm going to tell myself, I'm going to tell  
**Translation:** 

**[7643.96s] English:** a choice between two, one that is no clue what AI is, and one that is expert in using AI.  
**Translation:** 

**[7654.04s] English:** I would hire the one who's expert in using AI. If I had an accountant, a marketing person,  
**Translation:** 

**[7661.90s] English:** the one that is expert in using AI, supply chain, customer service, a salesperson,  
**Translation:** 

**[7668.20s] English:** business development, a lawyer, I would hire the one who is expert in using AI.  
**Translation:** 

**[7673.96s] English:** And so I would, I would advise that every college student, every  
**Translation:** 

**[7680.00s] English:** Every teacher should encourage their students to go use AI.  
**Translation:** 

**[7684.34s] English:** Every college student should graduate and be an expert in AI.  
**Translation:** 

**[7688.80s] English:** And everybody, if you're a carpenter, if you're an electrician, go use AI.  
**Translation:** Vocabulary: carpenter: 木匠; electrician: 电工

**[7695.48s] English:** Go see what it can do to transform your current job.  
**Translation:** 

**[7699.80s] English:** Elevate yourself.  
**Translation:** 

**[7701.00s] English:** If I were a farmer, I would absolutely use AI.  
**Translation:** 

**[7703.84s] English:** If I were a pharmacist, I would use AI.  
**Translation:** Vocabulary: pharmacist: 药师

**[7707.20s] English:** I want to see what it could do to elevate my job.  
**Translation:** 

**[7710.00s] English:** So that I could be the innovator to revolutionize this industry myself.  
**Translation:** Vocabulary: elevate: 提升; innovator: 创新者; revolutionize: 革新

**[7716.48s] English:** And so that would be the first thing that I would do.  
**Translation:** 

**[7718.94s] English:** And then I would also help them.  
**Translation:** 

**[7723.62s] English:** It is the case that the technology will dislocate and will eliminate many tasks.  
**Translation:** 

**[7732.02s] English:** And because it will automate it.  
**Translation:** Vocabulary: automate: 自动化; dislocate: 使失业

**[7734.02s] English:** If your job is the task,  
**Translation:** 

**[7736.34s] English:** if your job is the task,  
**Translation:** 

**[7738.54s] English:** then you're very high.  
**Translation:** 

**[7740.00s] English:** You're very highly going to be disrupted.  
**Translation:** Vocabulary: disrupted: 被打乱

**[7742.32s] English:** If your job's purpose includes certain tasks,  
**Translation:** 

**[7748.06s] English:** then it's vital that you go learn how to use AI to automate those tasks.  
**Translation:** 

**[7752.44s] English:** And then there's the world of spectrum in between.  
**Translation:** 

**[7754.86s] English:** And by the way, the beautiful thing about AI,  
**Translation:** 

**[7757.70s] English:** so the chatbot versions,  
**Translation:** 

**[7761.02s] English:** is you can break down, you have anxiety,  
**Translation:** 

**[7764.74s] English:** and you can break down the problem by talking to it.  
**Translation:** 

**[7767.68s] English:** Like I've recently, it's really,  
**Translation:** 

**[7770.00s] English:** it's just incredible how much you can think through your life's problems and through,  
**Translation:** 

**[7774.20s] English:** and I don't mean like therapy problems.  
**Translation:** 

**[7775.74s] English:** I mean, like very practically, okay, I'm worried about my, literally,  
**Translation:** 

**[7779.72s] English:** I'm worried about my job.  
**Translation:** 

**[7780.76s] English:** What are the skills?  
**Translation:** 

**[7781.50s] English:** What are the steps I need to take?  
**Translation:** 

**[7782.72s] English:** How do I get better at AI?  
**Translation:** 

**[7783.92s] English:** Everything you just said, you can literally ask,  
**Translation:** 

**[7786.02s] English:** and it's going to give you a point by point plan.  
**Translation:** 

**[7789.06s] English:** I mean, it's just a great life coach, period.  
**Translation:** 

**[7791.90s] English:** I don't know how to use AI.  
**Translation:** 

**[7793.10s] English:** And the AI goes, well, let me show you.  
**Translation:** 

**[7795.76s] English:** It's very meta, but it's kind of incredible.  
**Translation:** 

**[7799.02s] English:** So people definitely should.  
**Translation:** 

**[7799.86s] English:** Yeah.  
**Translation:** 

**[7800.00s] English:** You can't walk up to Excel and say, I don't know how to use Excel.  
**Translation:** 

**[7802.54s] English:** You're done.  
**Translation:** 

**[7803.10s] English:** I mean, that's really what AI has done for me in all walks of life, is that initial friction of being a beginner, of using a thing for the first time.  
**Translation:** Vocabulary: friction: 初始障碍

**[7811.64s] English:** I can literally ask about any single thing, what are the first steps I need to take?  
**Translation:** 

**[7816.62s] English:** That's right.  
**Translation:** 

**[7817.04s] English:** And that hand-holding that it does, removing the friction of all the experiences that the world offers, like I mentioned to you offline, you mentioned I'm going to China and Taiwan.  
**Translation:** 

**[7830.44s] English:** So awesome.  
**Translation:** Vocabulary: taiwan: 台湾

**[7831.36s] English:** I'm so excited for you.  
**Translation:** 

**[7832.56s] English:** Where do I go?  
**Translation:** 

**[7834.14s] English:** How do I?  
**Translation:** 

**[7834.78s] English:** All of those questions immediately answered.  
**Translation:** 

**[7836.78s] English:** It is beautiful.  
**Translation:** 

**[7837.50s] English:** Well, when you go to Taiwan, just ask AI, what are Jensen's favorite restaurants in Taiwan?  
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

**[7852.78s] English:** And like we also mentioned offline, maybe our paths will cross, which would be really wonderful.  
**Translation:** 

**[7857.78s] English:** Computex.  
**Translation:** Vocabulary: computex: 计算机展览

**[7858.36s] English:** NVIDIA GTC Taiwan.  
**Translation:** 

**[7860.00s] English:** Do you think there are some things about human nature, about human consciousness that is fundamentally non-computational?  
**Translation:** Vocabulary: fundamentally: 本质上

**[7872.62s] English:** Maybe something a chip, no matter how powerful, can never replicate?  
**Translation:** 

**[7877.78s] English:** I don't know if the chip will ever get nervous.  
**Translation:** 

**[7879.84s] English:** And that's the, you know, of course, the conditions by which that causes anxiety or nervousness or whatever emotion.  
**Translation:** 

**[7890.00s] English:** But I believe that AI will be able to recognize those and understand those.  
**Translation:** Vocabulary: nervousness: 紧张感

**[7897.84s] English:** I don't think my chips will feel those.  
**Translation:** 

**[7901.48s] English:** And therefore, how that anxiety, how that feeling, how that excitement, how that, you know, all of those feelings manifest in human performance.  
**Translation:** 

**[7913.84s] English:** For example, extremely amazing human performance, athletic performance.  
**Translation:** 

**[7918.72s] English:** You know, average or lesser.  
**Translation:** 

**[7920.00s] English:** than average, that entire spectrum of human performance that comes out of exactly the  
**Translation:** 

**[7927.50s] English:** same circumstances for different people manifesting in different outcome, manifesting in different  
**Translation:** Vocabulary: manifesting: 显现

**[7934.28s] English:** performance, I don't think there's anything that we're building that would suggest that  
**Translation:** 

**[7942.46s] English:** two different computers being presented with all of exactly the same context, of course  
**Translation:** 

**[7949.34s] English:** it would produce statistically different outcomes, but it's not because it felt different.  
**Translation:** 

**[7954.36s] English:** Yeah, the subjective, boy, there's something truly special about the subjective experience  
**Translation:** 

**[7959.56s] English:** that we humans feel.  
**Translation:** 

**[7963.02s] English:** Like I mentioned to you, I was pretty nervous talking to you, like I mentioned to you, that  
**Translation:** 

**[7968.22s] English:** the hope, the fear, the anxiety, and just life itself, the richness of life, how amazing  
**Translation:** 

**[7974.58s] English:** everything is, how deeply we fall in love, how deeply our hearts get broken.  
**Translation:** 

**[7979.34s] English:** How afraid we are of death, and how much pain we feel when our loved ones pass away.  
**Translation:** 

**[7985.22s] English:** All of that, the whole thing.  
**Translation:** 

**[7987.60s] English:** I know it's very hard to think AI being able to, a computational device being able to do  
**Translation:** 

**[7993.14s] English:** that, but there's so many mysteries about this whole thing that we're yet to uncover  
**Translation:** 

**[7997.70s] English:** that I am open to be surprised.  
**Translation:** 

**[8000.98s] English:** I've been surprised a lot over the past few months and few years.  
**Translation:** 

**[8005.42s] English:** Scaling can create some incredible miracles in the space of intelligence.  
**Translation:** 

**[8009.34s] English:** It has been truly marvelous to watch, so I'm open to surprise.  
**Translation:** 

**[8014.26s] English:** And it's just really important to break down what is intelligence.  
**Translation:** 

**[8018.56s] English:** That word we use all the time, it's not a mysterious word.  
**Translation:** 

**[8023.38s] English:** Intelligence has a meaning, and it's a system that, it's something that we do that includes  
**Translation:** 

**[8032.30s] English:** perception and understanding and reasoning and the ability to do plan.  
**Translation:** 

**[8036.10s] English:** And that loop, that loop.  
**Translation:** 

**[8039.34s] English:** That loop is.  
**Translation:** 

**[8040.00s] English:** is um the fundamentally what intelligence is intelligence is not one word that is exactly  
**Translation:** 

**[8048.48s] English:** equal to humanity and that's i think it's really important to separate the two we have two words  
**Translation:** Vocabulary: fundamentally: 根本上

**[8054.42s] English:** for that i'm not i don't over fantasize about and i don't over romanticize about intelligence  
**Translation:** 

**[8062.34s] English:** intelligence is and people have heard me say it before i actually think intelligence is a commodity  
**Translation:** Vocabulary: commodity: 商品; fantasize: 幻想

**[8068.34s] English:** i'm surrounded by intelligent people and i'm surrounded by intelligent people more intelligent  
**Translation:** 

**[8075.52s] English:** than i am in each one of the spaces that they're in and yet i have a role in that circle it's  
**Translation:** 

**[8083.16s] English:** actually kind of interesting they're more educated than i am they went to better schools than i did  
**Translation:** 

**[8090.50s] English:** they're deeper than in any in the fields that they're in all of them i have 60 of them they're  
**Translation:** 

**[8097.30s] English:** all superhuman to me  
**Translation:** 

**[8098.34s] English:** and somehow i'm sitting in the middle orchestrating all 60 of them and so you got to ask yourself  
**Translation:** 

**[8104.26s] English:** what is what is it about a dishwasher that allows that dishwasher to sit in the middle of super  
**Translation:** 

**[8112.42s] English:** humans does that make sense and so but that's my point my point is intelligence is a is a functional  
**Translation:** Vocabulary: dishwasher: 洗碗机

**[8120.56s] English:** thing humanity is not a not specified functionally it's a much much bigger word  
**Translation:** 

**[8128.34s] English:** and and our life experience our tolerance for pain our determination those are those are different  
**Translation:** Vocabulary: tolerance: 忍耐力

**[8137.10s] English:** words in intelligence and so the the thing that i i want to help the audience understand  
**Translation:** 

**[8142.70s] English:** if i could give them one thing is is intelligence is a word that we've elevated to very high form  
**Translation:** Vocabulary: elevated: 提升

**[8149.70s] English:** over time the the word we should really elevate is humanity character humanity all of those things  
**Translation:** 

**[8158.34s] English:** and that's what i'm trying to do is i'm trying to give them a little bit more of a sense of generosity  
**Translation:** Vocabulary: elevate: 提升; generosity: 慷慨

**[8161.06s] English:** and i'm trying to give them a little bit more of a sense of generosity  
**Translation:** 

**[8160.00s] English:** All of the things that you say just now, I believe those are superhuman powers.  
**Translation:** 

**[8166.62s] English:** And that now intelligence is going to be commoditized because we've spoken about it.  
**Translation:** 

**[8170.78s] English:** The most important thing is your education.  
**Translation:** Vocabulary: commoditized: 商品化

**[8173.34s] English:** Now, even when they said the most important thing is your education, when you went to school, there's more than just knowledge that you gained.  
**Translation:** 

**[8182.32s] English:** But unfortunately, our society has put everything into one single word.  
**Translation:** 

**[8187.58s] English:** And life is more than one word.  
**Translation:** 

**[8190.92s] English:** And I'm just telling you, my life would suggest that being lower on the intelligence curve than everybody around me doesn't change the fact I'm the most successful.  
**Translation:** 

**[8203.02s] English:** And I'm hoping to inspire everybody else that don't let this democratization of intelligence, this commoditization of intelligence...  
**Translation:** 

**[8217.58s] English:** You know, cause you anxiety. You should be inspired by that.  
**Translation:** Vocabulary: commoditization: 商品化; democratization: 民主化

**[8220.08s] English:** Yeah, I think AI will help us celebrate humans more.  
**Translation:** 

**[8223.92s] English:** And I'm certainly humanity and human first.  
**Translation:** 

**[8230.42s] English:** And I think what makes this world incredible is humans forever will be so.  
**Translation:** 

**[8235.86s] English:** And just AI is this incredible tool that makes us humans more powerful.  
**Translation:** 

**[8240.02s] English:** That's exactly right.  
**Translation:** 

**[8242.10s] English:** So much of the success of NVIDIA and the lives of millions...  
**Translation:** 

**[8247.58s] English:** The people that I mentioned depend on you.  
**Translation:** 

**[8251.66s] English:** But you're just one human, like we mentioned, mortal, like all of us.  
**Translation:** 

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

**[8274.28s] English:** This is not a once in a...  
**Translation:** 

**[8277.58s] English:** Once in a lifetime.  
**Translation:** 

**[8279.62s] English:** Once in a lifetime.  
**Translation:** 

**[8280.00s] English:** experience suggests that it has been experienced by many people, just not one person. This is a  
**Translation:** 

**[8287.70s] English:** once-in-a-humanity experience, what I'm going through. NVIDIA is one of the most consequential  
**Translation:** 

**[8293.60s] English:** technology companies in history. We're doing very important work. I take it very seriously.  
**Translation:** Vocabulary: consequential: 有重大影响的

**[8300.76s] English:** And so some of the things that, of course, are practical things, like how do we think about  
**Translation:** 

**[8307.26s] English:** succession planning? And I'm famous in saying that I don't believe in succession planning.  
**Translation:** 

**[8315.96s] English:** And the reason for that isn't because I'm immortal. The reason for that is because  
**Translation:** 

**[8323.70s] English:** if you're worried about succession planning, if you're worried, all that anxiety of succession  
**Translation:** Vocabulary: immortal: 长生不老

**[8330.42s] English:** planning, then what should you do about it? Then you break it all the way back down.  
**Translation:** 

**[8333.76s] English:** The most important thing you should do today, if you care about the future,  
**Translation:** 

**[8337.26s] English:** of your company, post you, is to pass on knowledge, information, insight, skills,  
**Translation:** 

**[8344.98s] English:** experience as often and continuously as you can, which is the reason why I continuously reason  
**Translation:** 

**[8350.34s] English:** about everything in front of my team. Every single meeting is about a reasoning meeting.  
**Translation:** 

**[8356.22s] English:** Every moment I spend inside a company, outside a company, is about passing on knowledge to people  
**Translation:** 

**[8362.02s] English:** as fast as I can. Nothing I learn ever sits on my desk.  
**Translation:** 

**[8367.26s] English:** A fraction of a second. I'm passing that information, that knowledge. Oh my gosh,  
**Translation:** 

**[8372.06s] English:** this is cool. Before I even finish learning all of it myself, I've already pointed it to somebody  
**Translation:** 

**[8377.30s] English:** else. Get on this. This is so cool. You're going to want to learn this. And so I'm constantly  
**Translation:** 

**[8383.02s] English:** passing knowledge, empowering people, elevating the capability of everybody around me so that  
**Translation:** 

**[8389.72s] English:** the outcome that I seek, that I hope for, is that I die on it.  
**Translation:** Vocabulary: capability: 能力; elevating: 提升; empowering: 赋能

**[8396.98s] English:** I die on it. I die on it. I die on it. I die on it. I die on it. I die on it. I die on it. I die on it. I die on it.  
**Translation:** 

**[8397.26s] English:** I die on the job.  
**Translation:** 

**[8400.00s] English:** i die on the job instantaneously yeah and there's no long periods of suffering you know  
**Translation:** 

**[8405.10s] English:** well from a fan perspective uh given your your uh extremely  
**Translation:** Vocabulary: instantaneously: 瞬间

**[8411.36s] English:** um your enormous positive impact on civilization of course i hope you keep going but also it's  
**Translation:** 

**[8419.48s] English:** just fun to watch what he is doing you know it's just the rate of innovation and i'm a huge fan  
**Translation:** 

**[8425.70s] English:** of engineering it's so much incredible engineering is continuously being done by nvidia it's just fun  
**Translation:** 

**[8431.20s] English:** to watch it's a celebration of humanity celebration of great builders the celebration of great  
**Translation:** 

**[8435.92s] English:** engineering so it represents something special uh so i hope you and nvidia keep going what gives  
**Translation:** 

**[8442.80s] English:** you hope about this whole thing we got going on about humanity about the future of humanity when  
**Translation:** 

**[8448.66s] English:** you look out and you think about the future quite a bit when you look out 10 20 50 100 years from  
**Translation:** 

**[8453.80s] English:** now what gives you hope  
**Translation:** 

**[8455.70s] English:** i i've always had i've always had uh uh great confidence in in the in the kindness uh the  
**Translation:** 

**[8467.00s] English:** generosity uh um the compassion the human capacity i've always been extremely confident of that  
**Translation:** Vocabulary: compassion: 同情; generosity: 慷慨

**[8478.42s] English:** sometimes um  
**Translation:** 

**[8480.10s] English:** more so than i should  
**Translation:** 

**[8484.34s] English:** and  
**Translation:** 

**[8485.70s] English:** and i get taken advantage of but it doesn't it doesn't ever cause me not to i start with  
**Translation:** 

**[8492.58s] English:** always uh that that people want want to do good people want to um uh help others and  
**Translation:** 

**[8502.04s] English:** vastly i am proven right  
**Translation:** 

**[8506.12s] English:** constantly proven right and and often uh exceeds my expectations  
**Translation:** 

**[8515.70s] English:** and and so i have complete confidence in the human capacity  
**Translation:** 

**[8520.00s] English:** I think the things that give me incredible hope is what I see as I extrapolate, as what I see now is possible, and as I extrapolate based on the things that we're doing, what will very likely happen.  
**Translation:** 

**[8540.64s] English:** And that there's so many things that we want to solve. There's so many problems we want to solve. There's so many things that we want to build. There's so many good things that we want to do that are now within our reach and within the reach of my lifetime. You just can't possibly not be romantic about that. You know what I'm saying?  
**Translation:** Vocabulary: extrapolate: 推断

**[8565.84s] English:** Yeah, what an exciting time to be alive. Like truly, truly so.  
**Translation:** 

**[8570.32s] English:** How can you not be romantic about that? The fact that it's a reasonable thing to expect the end of disease. It's a reasonable thing to expect. It's a reasonable thing to expect that pollution will be drastically reduced. It's a reasonable thing to expect that traveling at the speed of light is actually in our future.  
**Translation:** Vocabulary: drastically: 急剧地

**[8596.72s] English:** And then, you know, not for long distances, but short distances.  
**Translation:** 

**[8600.32s] English:** You know, people ask me how. Well, first of all, very soon, I'm going to put a humanoid on a spaceship, and it's going to be, you know, my humanoid. And we're going to send it out as soon as possible. And it's going to keep improving and enhancing along the flight.  
**Translation:** Vocabulary: enhancing: 改进; humanoid: 类人机器人

**[8616.60s] English:** And then when it's time, all of my consciousness has already been, you know, so much of my life has been uploaded in the internet. Take all my inbox, take everything that I've done, everything I've said, you know, it's been becoming my AI.  
**Translation:** 

**[8630.32s] English:** And, you know, when the time comes, you know, we'll just send that at the speed of light, catch up with my robot.  
**Translation:** 

**[8640.00s] English:** Oh, that's brilliant.  
**Translation:** 

**[8640.88s] English:** I mean, but for me, that's sort of application-focused.  
**Translation:** 

**[8644.50s] English:** But also, for me, the curiosity-maxing perspective,  
**Translation:** 

**[8649.60s] English:** I just, all of those mysteries,  
**Translation:** 

**[8651.42s] English:** there's so much fascinating scientific questions there.  
**Translation:** 

**[8654.72s] English:** Understanding the biological machine is right around the corner.  
**Translation:** 

**[8658.24s] English:** It's not 10 years, it's five years probably.  
**Translation:** 

**[8660.30s] English:** And the neurobiological machine, the human mind,  
**Translation:** 

**[8663.06s] English:** and cracking physics, theoretical physics open, it's so exciting.  
**Translation:** 

**[8666.42s] English:** Explaining consciousness, that one would be awesome.  
**Translation:** Vocabulary: cracking: 难解的

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

**[8681.48s] English:** And I wish you incredible success this year.  
**Translation:** 

**[8685.84s] English:** I can't wait.  
**Translation:** 

**[8686.36s] English:** As a fan, I can't wait to see what you do next.  
**Translation:** 

**[8688.48s] English:** And hopefully, I'll see you in Taiwan.  
**Translation:** 

**[8690.44s] English:** And thank you so much for talking today.  
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

**[8704.30s] English:** and the research that you do to reveal, you know, for all of us,  
**Translation:** 

**[8709.36s] English:** the amazing people that you've interviewed over the years.  
**Translation:** 

**[8712.78s] English:** I've enjoyed them immensely.  
**Translation:** 

**[8715.08s] English:** And as an innovator to have created this long form, unbelievable,  
**Translation:** Vocabulary: immensely: 极其; innovator: 创新者

**[8722.32s] English:** and yet, you know, it's just captivating.  
**Translation:** 

**[8724.76s] English:** So anyways, thank you for everything you do.  
**Translation:** Vocabulary: captivating: 引人入胜

**[8726.08s] English:** It means the world.  
**Translation:** 

**[8726.68s] English:** Thank you, Jensen.  
**Translation:** 

**[8727.44s] English:** Thank you, Lex.  
**Translation:** 

**[8729.08s] English:** Thank you for listening to this conversation with Jensen Huang.  
**Translation:** Vocabulary: huang: 黄

**[8732.46s] English:** To support this podcast, please check out our sponsor in the description,  
**Translation:** 

**[8735.90s] English:** where you can also find links to contact me, ask questions, give feedback, and so on.  
**Translation:** 

**[8742.24s] English:** And now, let me leave you with some words from Alan Kay.  
**Translation:** 

**[8746.56s] English:** The best way to predict the future is to invent it.  
**Translation:** 

**[8751.10s] English:** Thank you for listening.  
**Translation:** 

**[8752.74s] English:** And I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
