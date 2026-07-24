# Podcast vocabulary notes
Source file: Lex Fridman - Peter Norvig： Artificial Intelligence： A Modern Approach ｜ Lex Fridman Podcast #42.opus

**[0.00s] English:** The following is a conversation with Peter Norvig.  
**Translation:** 

**[2.82s] English:** He's the director of research at Google and the co-author with Stuart Russell of the book  
**Translation:** 

**[7.54s] English:** Artificial Intelligence and Modern Approach that educated and inspired a whole generation  
**Translation:** 

**[13.64s] English:** of researchers, including myself, to get into the field of artificial intelligence.  
**Translation:** 

**[18.90s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[21.70s] English:** If you enjoy it, subscribe on YouTube, give it five stars on iTunes, support on Patreon,  
**Translation:** Vocabulary: subscribe: 订阅

**[26.76s] English:** or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.  
**Translation:** 

**[32.64s] English:** And now, here's my conversation with Peter Norvig.  
**Translation:** Vocabulary: friedman: 弗里德曼

**[37.50s] English:** Most researchers in the AI community, including myself, own all three editions, red, green,  
**Translation:** 

**[42.60s] English:** and blue, of the Artificial Intelligence and Modern Approach.  
**Translation:** 

**[46.48s] English:** It's a field-defining textbook, as many people are aware, that you wrote with Stuart Russell.  
**Translation:** 

**[51.84s] English:** How has the book changed, and how have you changed in relation to it from the first  
**Translation:** 

**[56.74s] English:** edition to the second to the third, and now fourth edition as you work on it?  
**Translation:** 

**[60.84s] English:** Yeah, so it's been a lot of years, a lot of changes.  
**Translation:** 

**[64.28s] English:** One of the things changing from the first to maybe the second or third was just the  
**Translation:** 

**[70.26s] English:** rise of computing power, right?  
**Translation:** Vocabulary: computing: 计算能力

**[72.86s] English:** So I think in the first edition, we said, here's predicate logic, but that only goes  
**Translation:** 

**[81.92s] English:** so far because pretty soon you have millions of...  
**Translation:** Vocabulary: predicate: 谓词

**[86.74s] English:** Short little predicate expressions, and they couldn't possibly fit in memory.  
**Translation:** 

**[91.16s] English:** So we're going to use first-order logic that's more concise.  
**Translation:** Vocabulary: concise: 简洁明了

**[95.36s] English:** And then we quickly realized, oh, predicate logic is pretty nice because there are really  
**Translation:** 

**[101.50s] English:** fast SAT solvers and other things.  
**Translation:** Vocabulary: solvers: 求解器

**[104.20s] English:** And look, there's only millions of expressions, and that fits easily into memory, or maybe  
**Translation:** 

**[108.58s] English:** even billions fit into memory now.  
**Translation:** 

**[110.82s] English:** So that was a change of the type of technology we needed just because the hardware expanded.  
**Translation:** 

**[116.74s] English:** Even to the second edition, the resource constraints were loosened.  
**Translation:** Vocabulary: constraints: 限制; loosened: 放宽

**[120.00s] English:** significantly for the second yeah and that was early 2000s second edition right so 95 was the  
**Translation:** 

**[126.30s] English:** first and then uh 2000 2001 or so and then moving on from there i think we're starting to see that  
**Translation:** 

**[133.76s] English:** again with the gpus and then more specific type of uh machinery like the tpus and you're seeing  
**Translation:** 

**[143.14s] English:** custom asics and so on uh for deep learning so we're seeing another advance in terms of the  
**Translation:** Vocabulary: machinery: 机械设备

**[149.00s] English:** hardware then i think another thing that we especially noticed this time around is in all  
**Translation:** 

**[155.96s] English:** three of the first editions we kind of said well we're going to find ai as maximizing expected  
**Translation:** Vocabulary: maximizing: 最大化

**[161.76s] English:** utility and you tell me your utility function and now we've got 27 chapters worth of cool techniques  
**Translation:** 

**[169.30s] English:** for how to optimize that i think in this edition we're saying more you know what  
**Translation:** Vocabulary: optimize: 优化

**[174.54s] English:** maybe that optimization part is the easy part and the hard part  
**Translation:** 

**[179.00s] English:** is deciding what is my utility function what do i want and if i'm a collection of agents or a  
**Translation:** Vocabulary: optimization: 优化

**[185.36s] English:** society what do we want as a whole so you touch that topic in this edition you get a little bit  
**Translation:** 

**[190.90s] English:** more into utility yeah that's really interesting on a technical level we're almost pushing the  
**Translation:** 

**[196.52s] English:** philosophical i guess it is philosophical right so we we've always had a philosophy chapter which  
**Translation:** 

**[201.86s] English:** i was uh glad to that we were supporting and now it's less  
**Translation:** Vocabulary: philosophical: 人生观的

**[209.00s] English:** kind of the uh you know chinese room type argument and more of these uh ethical and societal type  
**Translation:** 

**[216.80s] English:** issues so we get into uh the issues of fairness and bias and uh and just the issue of aggregating  
**Translation:** Vocabulary: aggregating: 聚合; societal: 社会的

**[224.66s] English:** utilities so how do you encode human values into a utility function is this something that you can  
**Translation:** 

**[231.72s] English:** do purely through data in a learned way or is there some systematic obviously there's no good  
**Translation:** Vocabulary: encode: 编码; utilities: 公共事业

**[237.66s] English:** answers yet there's just  
**Translation:** 

**[239.00s] English:** uh  
**Translation:** 

**[240.00s] English:** beginnings to this uh to even opening right so there is no one answer yes there are techniques  
**Translation:** 

**[245.68s] English:** uh to try to learn that so we talk about inverse reinforcement learning right so reinforcement  
**Translation:** Vocabulary: inverse: 逆向; reinforcement: 强化

**[251.44s] English:** learning uh you take some actions you get some rewards and you figure out what actions you should  
**Translation:** 

**[256.96s] English:** take in inverse reinforcement learning you observe somebody taking actions and you figure out uh well  
**Translation:** 

**[265.28s] English:** that this must be what they were trying to do if they did this action it must be because they want  
**Translation:** 

**[270.16s] English:** of course there's restrictions to that right so lots of people  
**Translation:** 

**[274.32s] English:** take actions that are self-destructive or they're they're suboptimal in certain ways so you don't  
**Translation:** 

**[279.36s] English:** want to learn that right you want to somehow learn the the perfect actions rather than the  
**Translation:** Vocabulary: suboptimal: 次优的

**[285.28s] English:** ones they actually take so so that's a challenge for that field then another big part of it is  
**Translation:** 

**[293.52s] English:** just kind of uh theoretical of saying uh what can we accomplish and so you look at like the  
**Translation:** 

**[300.00s] English:** this work on the uh programs to uh predict recidivism and decide uh you know who should  
**Translation:** 

**[309.52s] English:** get parole or who should get bail or whatever uh and how are you going to evaluate that and  
**Translation:** Vocabulary: evaluate: 评估; parole: 假释; recidivism: 再犯

**[315.04s] English:** one of the big issues is fairness across protected classes protected classes being things like  
**Translation:** 

**[322.00s] English:** sex and race and so on and uh so two things you want is you want to say well if i get a score of  
**Translation:** 

**[330.00s] English:** say uh six out of ten then i want that to mean the same whether no matter what race i'm on yes  
**Translation:** 

**[337.28s] English:** right so i want to have a sixty percent chance of uh uh reoccurring uh regardless  
**Translation:** Vocabulary: reoccurring: 再次发生的

**[343.68s] English:** uh and the makers of the uh one of the makers of a commercial program to do that says that's  
**Translation:** 

**[348.96s] English:** what we're trying to optimize and look we achieved that we've uh we've reached that kind of uh  
**Translation:** Vocabulary: optimize: 优化

**[354.80s] English:** balance and then on the other side you also want to say uh well if  
**Translation:** 

**[360.00s] English:** If it makes mistakes, I want that to affect both sides of the protected class equally.  
**Translation:** 

**[367.20s] English:** And it turns out they don't do that, right?  
**Translation:** 

**[369.00s] English:** So they're twice as likely to make a mistake that would harm a black person over a white person.  
**Translation:** 

**[374.66s] English:** So that seems unfair.  
**Translation:** 

**[376.16s] English:** So you'd like to say, well, I want to achieve both those goals.  
**Translation:** 

**[379.36s] English:** And then it turns out you do the analysis and it's theoretically impossible to achieve both those goals.  
**Translation:** 

**[384.14s] English:** So you have to trade them off one against the other.  
**Translation:** Vocabulary: theoretically: 理论上

**[386.44s] English:** So that analysis is really helpful to know what you can aim for and how much you can get.  
**Translation:** 

**[392.32s] English:** You can't have everything.  
**Translation:** 

**[393.94s] English:** But the analysis certainly can't tell you where should we make that tradeoff point.  
**Translation:** 

**[398.76s] English:** But nevertheless, then we can, as humans, deliberate where that tradeoff should be.  
**Translation:** Vocabulary: deliberate: 仔细考虑; tradeoff: 权衡

**[403.10s] English:** Yeah, so at least now we're arguing in an informed way.  
**Translation:** 

**[405.68s] English:** We're not asking for something impossible.  
**Translation:** 

**[407.88s] English:** We're saying here's where we are and here's what we aim for.  
**Translation:** 

**[411.82s] English:** And this strategy is better than that strategy.  
**Translation:** 

**[415.40s] English:** So that's...  
**Translation:** 

**[416.74s] English:** I would argue is a really powerful and really important first step.  
**Translation:** 

**[420.34s] English:** But it's a doable one, sort of removing undesirable degrees of bias in systems in terms of protected classes.  
**Translation:** 

**[428.94s] English:** And then there's something I listened to your commencement speech.  
**Translation:** Vocabulary: doable: 可行的; undesirable: 不希望的

**[432.56s] English:** There's some fuzzier things like you mentioned angry birds.  
**Translation:** 

**[436.70s] English:** Do you want to create systems that feed the dopamine enjoyment, that feed, that optimize for you returning to the system?  
**Translation:** Vocabulary: dopamine: 多巴胺; fuzzier: 更模糊

**[446.74s] English:** Enjoying the moment of playing the game, of getting likes or whatever, this kind of thing, or some kind of long-term improvement?  
**Translation:** 

**[454.88s] English:** Right.  
**Translation:** 

**[455.30s] English:** Are you even thinking about that?  
**Translation:** 

**[459.44s] English:** That's really going to the philosophical area.  
**Translation:** Vocabulary: philosophical: 哲学的

**[463.22s] English:** I think that's a really important issue, too.  
**Translation:** 

**[465.74s] English:** Certainly thinking about that.  
**Translation:** 

**[466.78s] English:** I don't think about that as an AI issue as much.  
**Translation:** 

**[471.88s] English:** But as you say, the point is we've built...  
**Translation:** 

**[476.44s] English:** We've built this society and this infrastructure...  
**Translation:** 

**[480.00s] English:** where we say we have a marketplace for attention. And we've decided as a society that we like  
**Translation:** Vocabulary: marketplace: 交易平台

**[488.60s] English:** things that are free. And so we want all apps on our phone to be free. And that means they're all  
**Translation:** 

**[494.90s] English:** competing for your attention. And then eventually they make some money some way through ads or in  
**Translation:** 

**[500.58s] English:** game sales or whatever. But they can only win by defeating all the other apps by instilling your  
**Translation:** 

**[508.76s] English:** attention. And we built a marketplace where it seems like they're working against you rather  
**Translation:** Vocabulary: defeating: 击败; instilling: 灌输

**[517.26s] English:** than working with you. And I'd like to find a way where we can change the playing field so you feel  
**Translation:** 

**[523.24s] English:** more like, well, these things are on my side. Yes, they're letting me have some fun in the  
**Translation:** 

**[529.16s] English:** short term, but they're also helping me in the long term rather than competing against me.  
**Translation:** 

**[534.68s] English:** And those aren't necessarily conflicting objectives. They're just  
**Translation:** 

**[537.72s] English:** interesting.  
**Translation:** 

**[538.76s] English:** The incentives, the direct current incentives as we try to figure out this whole new world  
**Translation:** Vocabulary: incentives: 激励措施

**[543.00s] English:** seem to be on the easier part of that, which is feeding the dopamine, the rush.  
**Translation:** 

**[549.30s] English:** Right.  
**Translation:** 

**[549.80s] English:** But so maybe take a quick step back at the beginning of the Artificial Intelligence,  
**Translation:** 

**[557.90s] English:** the Modern Approach book of writing. So here you are in the 90s when you first  
**Translation:** 

**[562.68s] English:** sat down with Stuart to write the book to cover an entire field, which is one of the  
**Translation:** 

**[568.76s] English:** only books that has successfully done that for AI and actually in a lot of other computer science  
**Translation:** 

**[573.66s] English:** fields. It's a huge undertaking. So it must have been quite daunting. What was that process like?  
**Translation:** 

**[582.12s] English:** Did you envision that you would be trying to cover the entire field?  
**Translation:** Vocabulary: daunting: 令人望而生畏; envision: 构想; undertaking: 艰巨任务

**[587.02s] English:** Was there a systematic approach to it that was more step by step? How did it feel?  
**Translation:** 

**[591.80s] English:** So I guess it came about, you know, I'd go to lunch with the other AI faculty at Berkeley and we'd say,  
**Translation:** Vocabulary: berkeley: 伯克利

**[598.76s] English:** you know, the field has changed.  
**Translation:** 

**[600.00s] English:** seems like the current books are a little bit behind nobody's come out with a new book recently  
**Translation:** 

**[605.14s] English:** we should do that and everybody said yeah yeah that's a great thing to do and we never did  
**Translation:** 

**[609.58s] English:** anything right and then i ended up heading off to industry i went to sun lab so i thought well  
**Translation:** 

**[616.54s] English:** that's the end of my possible academic publishing career but i met stewart again at a conference  
**Translation:** 

**[623.36s] English:** like a year later and said you know that book we were always talking about you guys must be  
**Translation:** 

**[628.82s] English:** half done with it by now right and he said well we keep talking we never do anything so i said  
**Translation:** 

**[634.70s] English:** well you know we should do it and i think the reason is that we all felt it was a time where  
**Translation:** 

**[642.14s] English:** the field was changing and that was in two ways so you know the good old-fashioned ai was based  
**Translation:** 

**[651.04s] English:** primarily on boolean logic and you had a few tricks to deal with uncertainty and it was based  
**Translation:** Vocabulary: boolean: 真值逻辑

**[657.72s] English:** primarily on  
**Translation:** 

**[658.82s] English:** knowledge engineering that the way you got something done is you went out you interviewed  
**Translation:** 

**[662.30s] English:** an expert and you wrote down by hand everything they knew and we saw in in 95 that the field was  
**Translation:** 

**[669.88s] English:** changing in in two ways one we're moving more towards probability rather than boolean logic  
**Translation:** 

**[676.02s] English:** and we're moving more towards machine learning rather than knowledge engineering uh and the  
**Translation:** 

**[681.58s] English:** other books uh hadn't caught that wave they were still in the uh more in the in the old school  
**Translation:** 

**[687.48s] English:** although so certainly they had  
**Translation:** 

**[688.82s] English:** part of that on the way but we said if we start now completely taking that point of view we can  
**Translation:** 

**[696.08s] English:** have a different kind of book and we were able to put that together and uh what was literally the  
**Translation:** 

**[703.22s] English:** process if you remember what did you start writing a chapter did you outline yeah i guess i guess we  
**Translation:** 

**[709.52s] English:** did an outline and then we sort of assigned chapters to each person at the time uh i had  
**Translation:** 

**[717.30s] English:** moved to boston and steward  
**Translation:** 

**[718.82s] English:** was in berkeley  
**Translation:** 

**[720.00s] English:** So basically, we did it over the internet, and that wasn't the same as doing it today.  
**Translation:** 

**[727.88s] English:** It meant dial-up lines and telnetting in, and you telnetted into one shell, and you  
**Translation:** 

**[739.54s] English:** typed cat file name, and you hoped it was captured at the other end.  
**Translation:** Vocabulary: telnetted: 远程登录; telnetting: 远程登录

**[743.42s] English:** And certainly, you're not sending images and figures back and forth.  
**Translation:** 

**[747.16s] English:** Right, right.  
**Translation:** 

**[747.94s] English:** That didn't work.  
**Translation:** 

**[748.50s] English:** But did you anticipate where the field would go from that day, from the 90s?  
**Translation:** Vocabulary: anticipate: 预想

**[757.58s] English:** Did you see the growth into learning-based methods, into data-driven methods that followed  
**Translation:** 

**[765.12s] English:** in the future decades?  
**Translation:** 

**[767.02s] English:** We certainly thought that learning was important.  
**Translation:** 

**[771.86s] English:** I guess we missed it as being as important as it is today.  
**Translation:** 

**[777.92s] English:** We missed it.  
**Translation:** 

**[778.48s] English:** We missed it.  
**Translation:** 

**[778.50s] English:** We missed this idea of big data.  
**Translation:** 

**[780.10s] English:** We missed the idea of deep learning hadn't been invented yet.  
**Translation:** 

**[784.40s] English:** We could have taken the book from a complete machine learning point of view right from  
**Translation:** 

**[791.58s] English:** the start.  
**Translation:** 

**[792.32s] English:** We chose to do it more from a point of view of we're going to first develop different  
**Translation:** 

**[797.10s] English:** types of representations, and we're going to talk about different types of environments.  
**Translation:** Vocabulary: environments: 环境类型

**[803.22s] English:** Is it fully observable or partially observable, and is it deterministic or  
**Translation:** 

**[808.38s] English:** stateless?  
**Translation:** Vocabulary: deterministic: 决定论的; observable: 可观测的; stateless: 无状态的

**[808.50s] English:** It's deterministic and so on, and we made it more complex along those axes rather than  
**Translation:** 

**[814.14s] English:** focusing on the machine learning axis first.  
**Translation:** 

**[817.68s] English:** Do you think there's some sense in which the deep learning craze is extremely successful  
**Translation:** 

**[824.02s] English:** for a particular set of problems, and eventually it's going to, in the general case, hit challenges?  
**Translation:** Vocabulary: craze: 狂热

**[832.18s] English:** In terms of the difference between perception systems and robots that have to act in the  
**Translation:** 

**[838.38s] English:** world, do you think we're going to be able to do that?  
**Translation:** 

**[840.00s] English:** going to return to ai a modern approach type breadth in addition five and six yeah in uh in  
**Translation:** 

**[850.16s] English:** future decades do you think deep learning will take its place as a chapter in this bigger  
**Translation:** 

**[854.64s] English:** is in this bigger uh view of ai yeah i think we don't know yet how it's all going to play out  
**Translation:** 

**[860.40s] English:** so uh in the new edition uh we have a chapter on deep learning uh we got ian goodfellow to be the  
**Translation:** Vocabulary: goodfellow: 好费尔

**[868.36s] English:** guest author for that chapter so he said he could condense his whole deep learning book  
**Translation:** 

**[874.02s] English:** into one chapter i think he did a great job we were also encouraged that he's you know we gave  
**Translation:** Vocabulary: condense: 浓缩

**[880.90s] English:** him the old neural net chapter and said have fun with it modernize that and he said you know half  
**Translation:** 

**[888.30s] English:** of that was okay that certainly there's lots of new things that have been developed but some of  
**Translation:** Vocabulary: modernize: 现代化; neural: 神经

**[898.36s] English:** the things that have been developed that have been developed in the past that have been developed  
**Translation:** 

**[902.18s] English:** in the past are still there and so i think we'll gain a better understanding of what you can do  
**Translation:** 

**[908.14s] English:** there i think we'll need to incorporate all the things we can do with the other technologies  
**Translation:** 

**[914.26s] English:** right so deep learning started out convolutional networks and uh very close to perception uh and  
**Translation:** Vocabulary: convolutional: 卷积网络; incorporate: 整合

**[923.02s] English:** it's since moved to be uh to be able to do more with actions and some degree of longer-term planning  
**Translation:** 

**[928.36s] English:** but we need to do a better job with uh representation and reasoning and uh one-shot  
**Translation:** 

**[934.88s] English:** learning and so on and i think we don't know yet how that's going to play out so do you think  
**Translation:** 

**[941.68s] English:** looking at the some success but certainly uh eventual demise a partial demise of experts  
**Translation:** Vocabulary: demise: 消亡; eventual: 最终的

**[951.42s] English:** to symbolic uh systems in the 80s do you think there is kernels of wisdom in the work that was  
**Translation:** 

**[958.36s] English:** done there with logic and  
**Translation:** Vocabulary: kernels: 精华; symbolic: 符号的

**[960.00s] English:** reasoning, and so on that will rise again, in your view?  
**Translation:** 

**[965.66s] English:** So certainly, I think the idea of representation and reasoning is crucial, that sometimes you  
**Translation:** 

**[972.68s] English:** just don't have enough data about the world to learn de novo.  
**Translation:** 

**[976.92s] English:** So you've got to have some idea of representation, whether that was programmed in or told or  
**Translation:** 

**[983.94s] English:** whatever, and then be able to take steps of reasoning.  
**Translation:** 

**[987.72s] English:** I think the problem with the good old-fashioned AI was, one, we tried to base everything on  
**Translation:** 

**[998.32s] English:** these symbols that were atomic, and that's great if you're trying to define the properties  
**Translation:** 

**[1005.96s] English:** of a triangle, because they have necessary and sufficient conditions, but things in the  
**Translation:** Vocabulary: triangle: 三角形

**[1011.24s] English:** real world don't.  
**Translation:** 

**[1011.94s] English:** The real world is messy and doesn't have sharp edges, and atomic symbols do.  
**Translation:** 

**[1017.72s] English:** That was a poor match.  
**Translation:** 

**[1020.74s] English:** And then the other aspect was that the reasoning was universal and applied anywhere, which  
**Translation:** 

**[1029.96s] English:** in some sense is good, but it also means there's no guidance as to where to apply it.  
**Translation:** 

**[1035.16s] English:** And so you started getting these paradoxes like, well, if I have a mountain and I remove  
**Translation:** Vocabulary: paradoxes: 矛盾

**[1041.46s] English:** one grain of sand, then it's still a mountain.  
**Translation:** 

**[1044.80s] English:** But if I do that repeatedly, at some point, it's not.  
**Translation:** 

**[1047.72s] English:** And with logic, there's nothing to stop you from applying things repeatedly.  
**Translation:** 

**[1057.02s] English:** But maybe with something like deep learning, and I don't really know what the right name  
**Translation:** 

**[1063.36s] English:** for it is, we could separate out those ideas.  
**Translation:** 

**[1065.98s] English:** So one, we could say a mountain isn't just an atomic notion, it's something like word  
**Translation:** 

**[1075.38s] English:** embedding.  
**Translation:** 

**[1077.72s] English:** It has a more...  
**Translation:** Vocabulary: embedding: 嵌入

**[1080.00s] English:** complex representation yeah and secondly we could somehow learn yeah there's this rule that you can  
**Translation:** 

**[1086.36s] English:** remove one grain of sand and you can do that a bunch of times but you can't do it a near infinite  
**Translation:** 

**[1091.32s] English:** amount of times but on the other hand when you're doing induction on the integer sure then it's fine  
**Translation:** 

**[1096.68s] English:** to do it an infinite number of times and if we could somehow we have to learn when these strategies  
**Translation:** Vocabulary: induction: 归纳; integer: 整数

**[1103.02s] English:** are applicable rather than having the strategies be completely neutral and available everywhere  
**Translation:** 

**[1110.16s] English:** anytime you use neural networks anytime you learn from data form representation from data in an  
**Translation:** Vocabulary: anytime: 随时; neural: 神经

**[1115.74s] English:** automated way it's not very explainable as to uh or it's not introspective to us humans  
**Translation:** 

**[1123.72s] English:** in terms of uh how this neural network sees the world where why does it succeed so brilliantly  
**Translation:** Vocabulary: automated: 自动化; brilliantly: 出色地; introspective: 反思的

**[1130.98s] English:** on so many in so many cases  
**Translation:** 

**[1132.76s] English:** and fail so miserably in surprising ways and small so what do you think is this is um  
**Translation:** Vocabulary: miserably: 糟糕地

**[1138.94s] English:** the future there can simply more data better data more organized data solve that problem  
**Translation:** 

**[1145.58s] English:** or is there elements of symbolic systems that need to be brought in which are a little bit  
**Translation:** Vocabulary: symbolic: 符号系统

**[1151.16s] English:** more explainable yeah so i prefer to talk about trust and uh validation and verification rather  
**Translation:** 

**[1160.60s] English:** than just about explainability  
**Translation:** Vocabulary: explainability: 可解释性; validation: 验证; verification: 核实

**[1162.26s] English:** and that  
**Translation:** 

**[1162.74s] English:** i think uh explanations are one tool that you use towards those goals  
**Translation:** 

**[1167.40s] English:** and i think it is important issue that we don't want to use these systems unless we trust them  
**Translation:** 

**[1173.88s] English:** and we want to understand where they work and where they don't work and in an explanation can  
**Translation:** 

**[1178.90s] English:** be part of that right so i apply for a loan and i get denied i want some explanation of why and  
**Translation:** 

**[1186.46s] English:** you have in europe we have the gdpr that says you're required to be able to get that  
**Translation:** 

**[1193.70s] English:** but on the other hand explanation alone is not enough right so you know we were used to  
**Translation:** 

**[1199.78s] English:** de-  
**Translation:** 

**[1200.00s] English:** with people and with organizations and corporations and so on and they can give  
**Translation:** 

**[1205.34s] English:** you an explanation then you have no guarantee that that explanation relates  
**Translation:** 

**[1209.12s] English:** to reality right right so the bank can tell me well you didn't get the loan  
**Translation:** 

**[1213.60s] English:** because you didn't have enough collateral and that may be true or it may  
**Translation:** Vocabulary: collateral: 抵押物

**[1217.58s] English:** be true that they just didn't like my religion or or something else I can't  
**Translation:** 

**[1222.80s] English:** tell from the explanation and that's that's true whether the decision was  
**Translation:** 

**[1227.02s] English:** made by computer or by a person so I want more  
**Translation:** 

**[1233.02s] English:** I do want to have the explanations and I want to be able to have a conversation  
**Translation:** 

**[1236.74s] English:** to go back and forth and said well you gave this explanation but what about  
**Translation:** 

**[1240.96s] English:** this and what would have happened if this had happened and what would I need  
**Translation:** 

**[1245.96s] English:** to change that so I think a conversation is a better way to think about it than  
**Translation:** 

**[1250.92s] English:** just an explanation as a single output and I think we need testing of various  
**Translation:** 

**[1256.92s] English:** cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1257.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1258.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1259.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1260.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1261.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1262.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1263.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1264.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1265.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1266.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1267.02s] English:** testing of various cases and I think we need testing of various cases and I think we need  
**Translation:** 

**[1268.02s] English:** I can't tell if I'm only looking at my case, but if I look across all the cases, then I can detect a pattern, right?  
**Translation:** 

**[1275.24s] English:** So you want to have that kind of capability.  
**Translation:** Vocabulary: capability: 能力

**[1277.96s] English:** You want to have these adversarial testing, right?  
**Translation:** 

**[1281.10s] English:** So we thought we were doing pretty good at object recognition in images.  
**Translation:** Vocabulary: adversarial: 对抗性的

**[1285.78s] English:** We said, look, we're at sort of pretty close to human-level performance on ImageNet and so on.  
**Translation:** 

**[1291.14s] English:** And then you start seeing these adversarial images, and you say, wait a minute, that part is nothing like human performance.  
**Translation:** 

**[1299.50s] English:** You can mess with it really easily.  
**Translation:** 

**[1300.86s] English:** You can mess with it really easily, right?  
**Translation:** 

**[1302.74s] English:** And, yeah, you can do that to humans too, right?  
**Translation:** 

**[1305.62s] English:** In a different way, perhaps.  
**Translation:** 

**[1307.14s] English:** Right.  
**Translation:** 

**[1307.46s] English:** Humans don't know what color the dress was.  
**Translation:** 

**[1309.38s] English:** Right.  
**Translation:** 

**[1310.42s] English:** And so they're vulnerable to certain attacks that are different than the attacks on the machines.  
**Translation:** 

**[1315.68s] English:** But, you know, the attacks on the machines are so striking, they really change.  
**Translation:** 

**[1320.00s] English:** the way you think about what we've done right and the way i think about it is i think part of  
**Translation:** 

**[1326.08s] English:** the problem is we're seduced by uh our low dimensional metaphors right yeah so you know  
**Translation:** 

**[1334.64s] English:** you like that phrase you look in uh in a textbook and you say okay now we've mapped out the space  
**Translation:** Vocabulary: metaphors: 比喻; seduced: 迷惑

**[1340.24s] English:** and you know uh cat is here and dog is here and maybe there's a tiny little spot in the middle  
**Translation:** 

**[1347.36s] English:** where you can't tell the difference but mostly we've got it all covered and if you believe that  
**Translation:** 

**[1351.60s] English:** metaphor uh then you say well we're nearly there and uh you know there's only going to be a couple  
**Translation:** 

**[1357.36s] English:** adversarial images but i think that's the wrong metaphor and what you should really say is it's  
**Translation:** Vocabulary: metaphor: 比喻

**[1362.40s] English:** not a 2d flat space that we've got mostly covered it's a million dimension space and uh cat is this  
**Translation:** 

**[1369.12s] English:** string that goes out in this crazy path and if you step a little bit off the path in any direction  
**Translation:** Vocabulary: dimension: 维度

**[1375.68s] English:** you're in nowhere's  
**Translation:** 

**[1377.36s] English:** land and you don't know what's going to happen and so i think that's where we are and and now  
**Translation:** 

**[1382.08s] English:** we've got to deal with that so uh it wasn't so much an explanation but it was an understanding  
**Translation:** 

**[1388.16s] English:** of what the models are and what they're doing and now we can start exploring how do you fix that  
**Translation:** 

**[1392.72s] English:** yeah validating the robustness of the system so on but take it back to the this uh this word trust  
**Translation:** 

**[1399.60s] English:** uh do you think we're a little too hard on our robots in terms of uh the standards we apply so  
**Translation:** Vocabulary: robustness: 坚固性; validating: 验证

**[1406.88s] English:** you know  
**Translation:** 

**[1407.36s] English:** of uh there's a dance there's a there's a there's a dance in non-verbal and verbal  
**Translation:** 

**[1414.24s] English:** communication between humans you know if we apply the same kind of standard in terms of humans  
**Translation:** 

**[1420.32s] English:** you know we trust each other pretty quickly  
**Translation:** 

**[1423.28s] English:** uh you know you and i haven't met before and there's some degree of trust right that nothing's  
**Translation:** 

**[1429.04s] English:** gonna go crazy wrong and yet to ai when we look at ai systems where we seem to approach skepticism  
**Translation:** Vocabulary: skepticism: 怀疑态度

**[1436.88s] English:** always always yeah and it's like they have a lot of  
**Translation:** 

**[1440.00s] English:** to prove through a lot of hard work that they're even worthy of even inkling of our trust do it  
**Translation:** Vocabulary: inkling: 一丝

**[1446.56s] English:** what do you what do you think about that how how do we break that barrier close that gap i think  
**Translation:** 

**[1451.36s] English:** that's right i think that's a big issue uh just listening uh my friend uh mark moffitt is a  
**Translation:** 

**[1457.92s] English:** naturalist and he says uh the most amazing thing about humans is that you can walk into a coffee  
**Translation:** 

**[1464.56s] English:** shop or a busy street in a city and there's lots of people around you that you've never met before  
**Translation:** Vocabulary: naturalist: 自然学家

**[1471.92s] English:** and you don't kill each other yeah he says chimpanzees cannot do that yeah right right  
**Translation:** 

**[1478.48s] English:** if a chimpanzee's in a situation where here's some that aren't from my tribe  
**Translation:** Vocabulary: cannot: 不能

**[1485.44s] English:** bad things happen especially in a coffee shop there's delicious food around you know yeah  
**Translation:** 

**[1489.36s] English:** yeah but but we humans have figured that out yeah right uh and you know for the most  
**Translation:** 

**[1494.56s] English:** part for the most part we still go to war we still do terrible things uh but for the most  
**Translation:** 

**[1498.64s] English:** part we've learned to trust each other and live together uh so that's going to be important for  
**Translation:** 

**[1504.72s] English:** our uh our ai systems as well and i also i think uh you know a lot of the emphasis is on ai uh but  
**Translation:** 

**[1513.68s] English:** in many cases uh ai is part of the technology but isn't really the main thing so a lot of  
**Translation:** 

**[1520.24s] English:** what we've seen is more due to communications technology  
**Translation:** 

**[1525.12s] English:** than ai ai technology yeah you want to make these good decisions but the reason uh we're able to have  
**Translation:** 

**[1532.16s] English:** any kind of system at all is we've got the communication so that we're collecting the data  
**Translation:** 

**[1537.52s] English:** and so that we can reach lots of people around the world i think that's a bigger change that  
**Translation:** 

**[1543.28s] English:** we're dealing with speaking of reaching a lot of people around the world on the side of education  
**Translation:** 

**[1549.60s] English:** you've uh one of the many things in terms of education you've done you've taught  
**Translation:** 

**[1554.56s] English:** uh intro to artificial intelligence course that signed up a hundred thousand 160 000 students  
**Translation:** 

**[1560.00s] English:** is one of the first successful example of a massive of a MOOC massive open online course  
**Translation:** Vocabulary: intro: 入门课程

**[1566.02s] English:** what did you learn from that experience uh what do you think is the future of MOOCs of education  
**Translation:** 

**[1572.24s] English:** online yeah it was a great fun doing it particularly uh being right at the start  
**Translation:** 

**[1578.22s] English:** just because it was exciting and new but it also meant that we had less competition  
**Translation:** 

**[1583.52s] English:** right so uh one of the things you hear about uh well the problem with MOOCs is uh the completion  
**Translation:** 

**[1590.70s] English:** rates are are so low so it must be a failure and and i gotta admit i'm a prime contributor right i  
**Translation:** 

**[1597.68s] English:** probably uh started 50 different courses that i haven't finished but i got exactly what i wanted  
**Translation:** 

**[1603.62s] English:** out of them because i had never intended to finish them i just wanted to dabble in a little bit  
**Translation:** 

**[1608.64s] English:** either to see the topic matter or just to see the pedagogy of how are they doing this class  
**Translation:** Vocabulary: dabble: 浅尝辄止; pedagogy: 教学法

**[1613.52s] English:** so i guess the main thing i learned is when i came in i thought uh the challenge was information  
**Translation:** 

**[1622.48s] English:** saying if i'm just uh take the stuff i want you to know and i'm very clear and explain it well  
**Translation:** 

**[1629.92s] English:** then my job is done and good things are going to happen uh and then in doing the course i learned  
**Translation:** 

**[1636.96s] English:** well yeah you got to have the information but really the motivation is the most important thing  
**Translation:** 

**[1642.58s] English:** that  
**Translation:** 

**[1643.52s] English:** if students don't stick with it it doesn't matter how good the content is  
**Translation:** 

**[1648.08s] English:** and i think being one of the first classes we were helped by uh sort of exterior motivation  
**Translation:** 

**[1656.46s] English:** so we tried to do a good job of making it enticing and setting up uh ways for uh you know the  
**Translation:** Vocabulary: enticing: 诱惑; exterior: 外部

**[1664.04s] English:** community to work with each other to make it more motivating but really a lot of it was hey this is  
**Translation:** 

**[1668.56s] English:** a new thing and i'm really excited to be part of a new thing and so the students brought their own  
**Translation:** Vocabulary: motivating: 激励的

**[1673.52s] English:** and so i think this is great because there's lots of people around the world who have never had this  
**Translation:** 

**[1680.00s] English:** for, you know, would never have the opportunity to go to Stanford and take a class or go to MIT  
**Translation:** 

**[1688.34s] English:** or go to one of the other schools. But now we can bring that to them. And if they bring their  
**Translation:** 

**[1694.10s] English:** own motivation, they can be successful in a way they couldn't before. But that's really just the  
**Translation:** 

**[1699.80s] English:** top tier of people that are ready to do that. The rest of the people just don't see or don't have  
**Translation:** 

**[1708.38s] English:** the motivation and don't see how if they push through and were able to do it, what advantage  
**Translation:** 

**[1713.22s] English:** that would get them. So I think we got a long way to go before we're able to do that. And I think  
**Translation:** 

**[1718.22s] English:** some of it is based on technology, but more of it's based on the idea of community, that you got  
**Translation:** 

**[1724.28s] English:** to actually get people together. Some of the getting together can be done online. I think  
**Translation:** 

**[1729.62s] English:** some of it really has to be done in person in order to build that type of community and trust.  
**Translation:** 

**[1736.58s] English:** You know, there's an intentional  
**Translation:** 

**[1737.72s] English:** measure.  
**Translation:** Vocabulary: intentional: 故意的

**[1738.38s] English:** There's a mechanism that we've developed a short attention span, especially younger people,  
**Translation:** 

**[1743.84s] English:** because sort of shorter and shorter videos online. There's a whatever the way the brain  
**Translation:** 

**[1751.64s] English:** is developing now, and with people that have grown up with the internet, they have quite  
**Translation:** 

**[1757.52s] English:** a short attention span. So and I would say I had the same when I was growing up too,  
**Translation:** 

**[1762.32s] English:** probably for different reasons. So I probably wouldn't have learned as much as I have if I  
**Translation:** 

**[1767.72s] English:** wasn't forced to sit in a physical classroom, sort of bored, sometimes falling asleep, but sort of  
**Translation:** 

**[1774.38s] English:** forcing myself through that process. So sometimes extremely difficult computer science courses.  
**Translation:** 

**[1779.86s] English:** What's the difference in your view between in person education experience, which you,  
**Translation:** 

**[1787.54s] English:** first of all, yourself had and you yourself taught and online education?  
**Translation:** 

**[1791.90s] English:** And how do we close that gap if it's even possible?  
**Translation:** 

**[1794.10s] English:** Yeah. So I think there's two issues. One is,  
**Translation:** 

**[1797.72s] English:** whether it's in person, or  
**Translation:** 

**[1800.00s] English:** online so sort of the physical location and then the other is kind of the  
**Translation:** 

**[1805.24s] English:** affiliation right so you stuck with it in part because you were in the  
**Translation:** Vocabulary: affiliation: 隶属关系

**[1811.88s] English:** classroom and you saw everybody else was suffering right the same way you were  
**Translation:** 

**[1816.52s] English:** but also because you were enrolled you had paid tuition sort of everybody was  
**Translation:** Vocabulary: enrolled: 注册

**[1822.82s] English:** expecting you to stick with it society parents yeah because peers right and so  
**Translation:** 

**[1829.78s] English:** those are two separate things I mean you could certainly imagine I pay a huge  
**Translation:** 

**[1833.58s] English:** amount of tuition and everybody signed up and says yes you're doing this but  
**Translation:** 

**[1839.26s] English:** then I'm in my room and my classmates are in different rooms right we could  
**Translation:** 

**[1843.52s] English:** have things set up that way so it's not just the online versus offline I think  
**Translation:** 

**[1849.06s] English:** what's more important is the commitment that you've made  
**Translation:** 

**[1852.82s] English:** and certainly it is important to have that kind of informal you know I meet  
**Translation:** 

**[1860.18s] English:** people outside of class we talk together because we're all in it together I think  
**Translation:** Vocabulary: informal: 非正式的

**[1865.44s] English:** that's really important both in keeping your motivation and also that's where  
**Translation:** 

**[1871.10s] English:** some of the most important learning goes on so you want to have that maybe you  
**Translation:** 

**[1875.82s] English:** you know especially now we start getting into higher bandwidths and augmented  
**Translation:** 

**[1880.92s] English:** reality and virtual reality you might  
**Translation:** Vocabulary: augmented: 增强; bandwidths: 带宽

**[1882.80s] English:** you might want to have that maybe you know especially now we start getting into higher bandwidths and augmented reality and virtual reality you might  
**Translation:** 

**[1882.82s] English:** be able to get that without being in the same physical place do you think it's  
**Translation:** 

**[1886.38s] English:** possible we'll see a course at Stanford for example that for students enrolled  
**Translation:** 

**[1894.32s] English:** students is only online in the near future or literally sort of that's part  
**Translation:** Vocabulary: stanford: 斯坦福大学

**[1899.00s] English:** of the curriculum and there is no yeah so you're starting to see that I know  
**Translation:** 

**[1902.86s] English:** Georgia Tech has a master's that's done that way oftentimes it's sort of they're  
**Translation:** Vocabulary: oftentimes: 经常

**[1908.58s] English:** creeping in in terms of a master's program or sort of further  
**Translation:** 

**[1912.80s] English:** education yeah considering the constraints of  
**Translation:** Vocabulary: constraints: 限制; creeping: 悄悄地

**[1915.44s] English:** students and so on but I mean literally is it possible that we  
**Translation:** 

**[1920.00s] English:** you know stanford mit berkeley all these places go online only in uh in the next few decades  
**Translation:** 

**[1927.18s] English:** yeah probably not because you know they've got a big uh commitment to a physical campus  
**Translation:** 

**[1932.60s] English:** sure right there's there's a momentum that's both financial and cultural right and and then  
**Translation:** 

**[1939.28s] English:** there are certain things that's just hard to do uh virtually right so you know we're in a field  
**Translation:** 

**[1947.16s] English:** uh where uh if you have your own computer and your own paper and so on uh you can do the work  
**Translation:** 

**[1954.92s] English:** anywhere uh but if you're in a biology lab or something uh you know you don't have all the  
**Translation:** 

**[1961.14s] English:** right stuff at home right so our field programming you've also done a lot of you've done a lot of  
**Translation:** 

**[1968.20s] English:** programming yourself in 2001 you wrote a great article about programming called teach yourself  
**Translation:** 

**[1975.60s] English:** programming in 10 years  
**Translation:** 

**[1977.16s] English:** sort of response to all the books that say teach yourself programming 21 days  
**Translation:** 

**[1981.14s] English:** so if you're giving advice to someone getting into programming today this is a few years since  
**Translation:** 

**[1986.16s] English:** you've written that article what's the best way to undertake that journey i think there's lots  
**Translation:** 

**[1991.54s] English:** of different ways and i think programming means more things now and i guess you know when i wrote  
**Translation:** Vocabulary: undertake: 承担

**[1998.98s] English:** that article i was thinking more about becoming a professional software engineer and i thought  
**Translation:** 

**[2006.20s] English:** that's a  
**Translation:** 

**[2006.98s] English:** you  
**Translation:** 

**[2007.16s] English:** , know sort of a career-long field of study but i think there's lots of things now that people can  
**Translation:** 

**[2014.06s] English:** do where programming is a part of solving what they want to solve without achieving that professional  
**Translation:** 

**[2023.00s] English:** level status right so i'm not going to be going and writing a million lines of code but you know  
**Translation:** 

**[2028.52s] English:** i'm a biologist or a physicist or something or even a historian and i've got some data and i want  
**Translation:** 

**[2036.28s] English:** to ask a question of that and i'm going to ask a question of that and i'm going to ask a question of that  
**Translation:** Vocabulary: biologist: 生物学家; physicist: 物理学家

**[2037.16s] English:** and i'm going to ask a question of that and i'm going to ask a question of that data and i think for that  
**Translation:** 

**[2039.96s] English:** data and i think for that  
**Translation:** 

**[2040.00s] English:** you don't need 10 years, right? So there are many shortcuts to being able to answer those  
**Translation:** 

**[2047.04s] English:** kinds of questions. And you see today a lot of emphasis on learning to code, teaching kids how  
**Translation:** Vocabulary: shortcuts: 捷径

**[2055.08s] English:** to code. I think that's great, but I wish they would change the message a little bit, right?  
**Translation:** 

**[2062.06s] English:** So I think code isn't the main thing. I don't really care if you know the syntax of JavaScript  
**Translation:** Vocabulary: syntax: 语法规则

**[2067.90s] English:** or if you can connect these blocks together in this visual language. But what I do care about  
**Translation:** 

**[2074.48s] English:** is that you can analyze a problem, you can think of a solution, you can carry out, you know,  
**Translation:** 

**[2083.98s] English:** make a model, run that model, test the model, see the results, verify that they're reasonable,  
**Translation:** 

**[2093.20s] English:** ask questions, and answer them, right? So it's more modeling and problem solving,  
**Translation:** Vocabulary: verify: 验证合理

**[2097.90s] English:** and you use coding in order to do that. But it's not just learning coding for its own sake.  
**Translation:** 

**[2104.34s] English:** That's really interesting. So it's actually almost, in many cases, it's learning to work  
**Translation:** 

**[2109.14s] English:** with data, to extract something useful out of data. So when you say problem solving,  
**Translation:** 

**[2113.64s] English:** you really mean taking some kind of, maybe collecting some kind of data set,  
**Translation:** 

**[2117.70s] English:** cleaning it up, and saying something interesting about it, which is useful in all kinds of domains.  
**Translation:** 

**[2122.72s] English:** And, you know, and I see myself being stuck sometimes,  
**Translation:** 

**[2127.90s] English:** in kind of the old ways, right? So, you know, I'll be working on a project,  
**Translation:** 

**[2133.28s] English:** maybe with a younger employee, and we say, oh, well, here's this new package that could help  
**Translation:** 

**[2139.66s] English:** solve this problem. And I'll go and I'll start reading the manuals. And, you know, I'll be  
**Translation:** 

**[2145.20s] English:** two hours into reading the manuals. And then my colleague comes back and says, I'm done.  
**Translation:** 

**[2151.14s] English:** You know, I downloaded the package, I installed it, I tried calling some things,  
**Translation:** 

**[2155.12s] English:** the first one didn't work, the second one didn't work.  
**Translation:** 

**[2157.90s] English:** I'm done. And I say, but I have...  
**Translation:** 

**[2160.00s] English:** under questions about how does this work and how does that work and they say who cares right i don't  
**Translation:** 

**[2164.32s] English:** need to understand the whole thing i understand i answered my question it's a big complicated  
**Translation:** 

**[2168.62s] English:** package i don't understand the rest of it but i got the right answer and i'm just it's hard for me  
**Translation:** 

**[2173.88s] English:** to get into that mindset i want to understand the whole thing and you know if they wrote a manual  
**Translation:** 

**[2178.94s] English:** i should probably read it and but that's not necessarily the right way i think i have to get  
**Translation:** Vocabulary: mindset: 思维模式

**[2184.32s] English:** used to dealing with more being more comfortable with uncertainty and not knowing everything  
**Translation:** 

**[2191.78s] English:** yeah so i struggle with the same instead of the the spectrum between donald don knuth yeah  
**Translation:** Vocabulary: knuth: 高斯斯

**[2197.56s] English:** it's kind of the very you know before you can say anything about a problem you really have to get  
**Translation:** 

**[2203.14s] English:** down to the machine code assembly yeah versus exactly what you said i've i have several  
**Translation:** 

**[2209.54s] English:** students in my group that uh you know at 20 years old and they can solve  
**Translation:** 

**[2214.22s] English:** a  
**Translation:** 

**[2214.30s] English:** almost any problem within a few hours that would take me probably weeks  
**Translation:** 

**[2218.10s] English:** because I would try to, as you said, read the manual.  
**Translation:** 

**[2221.06s] English:** So do you think the nature of mastery,  
**Translation:** 

**[2224.34s] English:** you're mentioning biology, sort of outside disciplines,  
**Translation:** Vocabulary: disciplines: 学科领域

**[2228.54s] English:** applying programming, but computer scientists.  
**Translation:** 

**[2233.62s] English:** So over time, there's higher and higher levels of abstraction available now.  
**Translation:** Vocabulary: abstraction: 抽象

**[2238.46s] English:** So with this week, there's the TensorFlow Summit, right?  
**Translation:** 

**[2243.22s] English:** So if you're not particularly into deep learning,  
**Translation:** 

**[2247.52s] English:** but you're still a computer scientist,  
**Translation:** 

**[2249.00s] English:** you can accomplish an incredible amount with TensorFlow  
**Translation:** 

**[2252.94s] English:** without really knowing any fundamental internals of machine learning.  
**Translation:** 

**[2257.20s] English:** Do you think the nature of mastery is changing,  
**Translation:** Vocabulary: internals: 内部机制

**[2260.62s] English:** even for computer scientists,  
**Translation:** 

**[2262.34s] English:** like what it means to be an expert programmer?  
**Translation:** Vocabulary: programmer: 程序员

**[2265.60s] English:** Yeah, I think that's true.  
**Translation:** 

**[2267.64s] English:** You know, we never really should have focused on programmers, right?  
**Translation:** 

**[2271.38s] English:** Because it's still a skill.  
**Translation:** 

**[2273.22s] English:** And what we really want to focus on is the result.  
**Translation:** 

**[2276.60s] English:** So we built this ecosystem where the...  
**Translation:** 

**[2280.00s] English:** The way you can get stuff done is by programming it yourself.  
**Translation:** 

**[2283.74s] English:** At least when I started, you know, library functions meant you had square root, and that was about it.  
**Translation:** 

**[2290.50s] English:** Right?  
**Translation:** 

**[2290.84s] English:** Everything else you built from scratch.  
**Translation:** 

**[2292.74s] English:** And then we built up an ecosystem where a lot of times, well, you can download a lot of stuff that does a big part of what you need.  
**Translation:** 

**[2299.66s] English:** And so now it's more a question of assembly rather than manufacturing.  
**Translation:** 

**[2306.78s] English:** And that's a different way of looking at problems.  
**Translation:** 

**[2311.86s] English:** From another perspective in terms of mastery and looking at programmers or people that reason about problems in a computational way.  
**Translation:** 

**[2319.80s] English:** So Google, you know, from the hiring perspective, from the perspective of hiring or building a team of programmers, how do you determine if someone's a good programmer?  
**Translation:** Vocabulary: computational: 计算相关; programmers: 程序员

**[2329.98s] English:** Or if somebody, again, I want to move away from the word programmer.  
**Translation:** 

**[2335.48s] English:** But somebody who can.  
**Translation:** 

**[2336.78s] English:** Solve problems of large scale data and so on.  
**Translation:** 

**[2339.76s] English:** What's, what's, how do you build a team like that through the interviewing process?  
**Translation:** 

**[2343.92s] English:** Yeah.  
**Translation:** 

**[2344.30s] English:** And I, and I think as a company grows, you get more expansive in the types of people you're looking for.  
**Translation:** Vocabulary: expansive: 视野宽广

**[2353.84s] English:** Right?  
**Translation:** 

**[2354.18s] English:** So I think, you know, in the early days we'd interview people and the question we were trying to ask is how close are they to Jeff Dean?  
**Translation:** 

**[2364.72s] English:** And most people were pretty far away.  
**Translation:** 

**[2366.78s] English:** But we'd take the ones that were, you know, not that far away.  
**Translation:** 

**[2369.32s] English:** And so we got kind of a homogeneous group of people who are really great programmers.  
**Translation:** 

**[2374.30s] English:** Then as a company grows, you say, well, we don't want everybody to be the same, to have the same skill set.  
**Translation:** Vocabulary: homogeneous: 成分相同

**[2380.40s] English:** And so now we're hiring biologists in our health areas and we're hiring physicists and we're hiring mechanical engineers and we're hiring, you know, social scientists and ethnographers.  
**Translation:** 

**[2396.18s] English:** And.  
**Translation:** Vocabulary: biologists: 生物学家; ethnographers: 人类学家; physicists: 物理学家

**[2396.78s] English:** People with different backgrounds who bring.  
**Translation:** 

**[2400.00s] English:** different skills so you have mentioned that you uh still may partake in code reviews  
**Translation:** Vocabulary: partake: 参与

**[2407.06s] English:** given that you have a wealth of experience as you've also mentioned it uh what errors do you  
**Translation:** 

**[2414.82s] English:** often see and tend to highlight in the code of junior developers of people coming up now  
**Translation:** 

**[2419.30s] English:** given your background from blisp to a couple decades of programming yeah that's a great  
**Translation:** 

**[2426.70s] English:** question you know sometimes i try to look at the flexibility of the design of uh yes you know this  
**Translation:** Vocabulary: flexibility: 灵活性

**[2435.56s] English:** api solves this problem but uh where is it going to go in the future who else is going to want to  
**Translation:** 

**[2440.82s] English:** call this and uh you know are you making it easier for them to do that it's a matter of uh design  
**Translation:** 

**[2448.84s] English:** is it documentation is it is it uh sort of an amorphous thing you can't really put it yeah  
**Translation:** 

**[2454.80s] English:** it's just how it feels  
**Translation:** Vocabulary: amorphous: 无定形的

**[2456.16s] English:** if you put yourself in the shoes of a developer would you use this kind of thing i think it is  
**Translation:** 

**[2460.14s] English:** how you feel right and so yeah documentation is good uh but it's but it's more a design  
**Translation:** 

**[2465.44s] English:** question right if you get the design right then people will figure it out whether the  
**Translation:** 

**[2470.60s] English:** documentation is good or not and if the design is wrong uh then it'll be harder to use how have uh  
**Translation:** 

**[2477.52s] English:** you yourself changed as a programmer over the years as in in a way you already started to say  
**Translation:** 

**[2485.32s] English:** sort of  
**Translation:** 

**[2485.90s] English:** you  
**Translation:** 

**[2486.16s] English:** , you want to read the manual you want to understand the core of the syntax to the how  
**Translation:** Vocabulary: syntax: 语法规则

**[2491.46s] English:** the language is supposed to be used and so on but um what's the evolution been like from the 80s 90s  
**Translation:** 

**[2499.10s] English:** to today i guess one thing is you don't have to worry about uh the small details of efficiency  
**Translation:** 

**[2505.80s] English:** as much as you used to right so like i remember uh i did my uh list book in the 90s and one of  
**Translation:** 

**[2513.86s] English:** the things i wanted to do was say uh  
**Translation:** 

**[2516.16s] English:** here's how you do an object system and uh  
**Translation:** 

**[2519.88s] English:** basically  
**Translation:** 

**[2520.28s] English:** i'm gonna do it in this case  
**Translation:** 

**[2523.12s] English:** i'm gonna do it in this case  
**Translation:** 

**[2526.72s] English:** you know  
**Translation:** 

**[2527.88s] English:** yeah  
**Translation:** 

**[2528.16s] English:** uh  
**Translation:** 

**[2528.60s] English:** so  
**Translation:** 

**[2529.10s] English:** it's  
**Translation:** 

**[2529.82s] English:** it's  
**Translation:** 

**[2530.26s] English:** it's  
**Translation:** 

**[2530.74s] English:** kinda  
**Translation:** 

**[2531.16s] English:** you know  
**Translation:** 

**[2531.60s] English:** like  
**Translation:** 

**[2531.84s] English:** it's  
**Translation:** 

**[2532.26s] English:** like  
**Translation:** 

**[2532.44s] English:** you know  
**Translation:** 

**[2532.96s] English:** it's  
**Translation:** 

**[2533.38s] English:** like  
**Translation:** 

**[2533.72s] English:** it's  
**Translation:** 

**[2534.20s] English:** like  
**Translation:** 

**[2534.58s] English:** it's  
**Translation:** 

**[2535.14s] English:** almost  
**Translation:** 

**[2536.40s] English:** like  
**Translation:** 

**[2536.74s] English:** the  
**Translation:** 

**[2537.08s] English:** way  
**Translation:** 

**[2537.52s] English:** of  
**Translation:** 

**[2537.82s] English:** it's  
**Translation:** 

**[2538.24s] English:** uh  
**Translation:** 

**[2538.72s] English:** i  
**Translation:** 

**[2539.36s] English:** think  
**Translation:** 

**[2539.74s] English:** it's  
**Translation:** 

**[2540.22s] English:** pretty  
**Translation:** 

**[2540.50s] English:** uh  
**Translation:** 

**[2541.04s] English:** interesting  
**Translation:** 

**[2541.62s] English:** if  
**Translation:** 

**[2542.30s] English:** you  
**Translation:** 

**[2542.82s] English:** want to  
**Translation:** 

**[2543.40s] English:** uh  
**Translation:** 

**[2544.02s] English:** think  
**Translation:** 

**[2544.66s] English:** about  
**Translation:** 

**[2545.28s] English:** things  
**Translation:** 

**[2545.86s] English:** it's  
**Translation:** 

**[2520.00s] English:** basically we're going to make it so each object is a hash table and you look up the methods and  
**Translation:** 

**[2524.82s] English:** here's how it works and then i said of course the real common lisp object system is much more  
**Translation:** 

**[2531.46s] English:** complicated it's got all these efficiency type issues and this is just a toy nobody would do  
**Translation:** 

**[2537.14s] English:** this in real life and it turns out python pretty much did exactly what i said yeah and said uh  
**Translation:** 

**[2544.96s] English:** objects are just dictionaries and yeah they have a few little tricks as well but mostly you know  
**Translation:** 

**[2552.14s] English:** the thing that would have been 100 times too slow in the 80s is now plenty fast for most everything  
**Translation:** 

**[2558.62s] English:** so you had to as a programmer let go of perhaps an obsession that i remember coming up with of  
**Translation:** Vocabulary: obsession: 痴迷; programmer: 程序员

**[2566.00s] English:** trying to write efficient code yeah that to say you know what really matters is the total time  
**Translation:** 

**[2573.68s] English:** it takes to get the  
**Translation:** 

**[2574.94s] English:** project done and most of that's going to be the programmer time yeah uh so if you're a little bit  
**Translation:** 

**[2579.78s] English:** less efficient but it makes it easier to understand and modify then that's the right trade-off so  
**Translation:** 

**[2585.98s] English:** you've written quite a bit about lisp your book on programming is in lisp you you have a lot of  
**Translation:** 

**[2591.16s] English:** code out there that's in lisp so myself and people who don't know what lisp is should look it up  
**Translation:** 

**[2597.60s] English:** it's my favorite language for many ai researchers it is a favorite language the favorite language  
**Translation:** 

**[2603.20s] English:** they never use these days  
**Translation:** 

**[2604.92s] English:** so what part of the lisp do you find most beautiful and powerful so i think the beautiful  
**Translation:** 

**[2609.62s] English:** part is the simplicity that in half a page you can define the whole language  
**Translation:** Vocabulary: simplicity: 简洁性

**[2614.94s] English:** and other languages don't have that so you feel like you can hold everything in your head and  
**Translation:** 

**[2623.30s] English:** then you know a lot of people say well then that's too simple you know here's all these  
**Translation:** 

**[2629.42s] English:** things i want to do and uh you know my java or python or whatever has  
**Translation:** 

**[2634.92s] English:** 100 or 200 or 300 different syntax rules and don't i need all those  
**Translation:** Vocabulary: syntax: 句法

**[2640.00s] English:** And Lisp's answer was, no, we're only going to give you eight or so syntax rules, but we're going to allow you to define your own.  
**Translation:** 

**[2648.68s] English:** And so that was a very powerful idea.  
**Translation:** 

**[2651.34s] English:** And I think this idea of saying I can start with my problem and with my data, and then I can build the language I want for that problem and for that data, and then I can make Lisp define that language.  
**Translation:** 

**[2667.90s] English:** So you're sort of mixing levels and saying I'm simultaneously a programmer in a language and a language designer, and that allows a better match between your problem and your eventual code.  
**Translation:** Vocabulary: eventual: 最终的

**[2683.70s] English:** And I think Lisp had done that better than other languages.  
**Translation:** 

**[2687.42s] English:** Yeah, it's a very elegant implementation of functional programming.  
**Translation:** Vocabulary: implementation: 实现

**[2691.02s] English:** But why do you think Lisp has not had the mass adoption and success of languages like Python?  
**Translation:** 

**[2696.98s] English:** Is it the parentheses?  
**Translation:** Vocabulary: parentheses: 圆括号

**[2697.90s] English:** Is it all the parentheses?  
**Translation:** 

**[2701.58s] English:** Yeah.  
**Translation:** 

**[2702.40s] English:** So I think a couple of things.  
**Translation:** 

**[2704.94s] English:** So one was I think it was designed for a single programmer or a small team and a skilled programmer who had the good taste to say, well, I am doing language design, and I have to make good choices.  
**Translation:** 

**[2721.70s] English:** And if you make good choices, that's great.  
**Translation:** 

**[2723.34s] English:** If you make bad choices, you can hurt yourself.  
**Translation:** 

**[2727.90s] English:** And it can be hard for other people on the team to understand it.  
**Translation:** 

**[2731.08s] English:** So I think there was a limit to the scale of the size of a project in terms of number of people that Lisp was good for.  
**Translation:** 

**[2738.66s] English:** And as an industry, we kind of grew beyond that.  
**Translation:** 

**[2742.88s] English:** I think it is in part the parentheses.  
**Translation:** 

**[2745.46s] English:** You know, one of the jokes is the acronym for Lisp is lots of irritating, silly parentheses.  
**Translation:** 

**[2753.56s] English:** My acronym was Lisp is syntactically pure.  
**Translation:** Vocabulary: acronym: 缩写; irritating: 令人烦躁的; syntactically: 语法上

**[2757.90s] English:** But Lisp says when people write, you can feel good and want it.  
**Translation:** 

**[2759.12s] English:** And everybody does kind of Stupid,  
**Translation:** 

**[2760.26s] English:** but Lisp is making it a customer friendly всю  
**Translation:** 

**[2763.44s] English:** language.  
**Translation:** 

**[2764.66s] English:** So if they can make community feel like it,  
**Translation:** 

**[2765.86s] English:** then it could play a huge role in the organization.  
**Translation:** 

**[2768.98s] English:** So I think the Lisp program is the only one with an actual ...  
**Translation:** 

**[2773.16s] English:** and that's a huge part of the bold task to say,  
**Translation:** 

**[2774.80s] English:** listen,  
**Translation:** 

**[2775.52s] English:** ourppy is not only that,  
**Translation:** 

**[2776.68s] English:** we are,  
**Translation:** 

**[2777.50s] English:** it's the environment,  
**Translation:** 

**[2778.70s] English:** and we have to make it so that other people like us can,  
**Translation:** 

**[2780.62s] English:** we don't really use our people to do our stuff.  
**Translation:** 

**[2782.52s] English:** It's just so incredible.  
**Translation:** 

**[2783.32s] English:** But there's also a nice little훈  
**Translation:** 

**[2784.76s] English:** when the company comes in Mcı Camps are really we large on individualśniej,  
**Translation:** 

**[2786.58s] English:** and we're sometimesальные sports.  
**Translation:** 

**[2787.38s] English:** And when we're selling things,  
**Translation:** 

**[2760.00s] English:** and atoms but i remember you know so we had the the ai textbook and uh because we did it in the  
**Translation:** 

**[2768.12s] English:** 90s we had uh we had pseudocode in the book but then we said well we'll have lisp online because  
**Translation:** 

**[2773.46s] English:** that's the language of ai at the time and i remember some of the students complaining because  
**Translation:** Vocabulary: pseudocode: 示例代码

**[2778.42s] English:** they hadn't had lisp before and they didn't quite understand what was going on and i remember one  
**Translation:** 

**[2783.12s] English:** student complained i don't understand how this pseudocode corresponds to this lisp and there  
**Translation:** Vocabulary: corresponds: 符合

**[2789.50s] English:** was a one-to-one correspondence between the the uh symbols in the code and the pseudocode and the  
**Translation:** 

**[2795.86s] English:** only thing difference was the parentheses so i said it must be that for some people a certain  
**Translation:** Vocabulary: correspondence: 一一对应

**[2801.44s] English:** number of left parentheses shuts off their brain yeah it's very it's very possible in that sense  
**Translation:** 

**[2807.06s] English:** and python just goes the other way and so so that was the point at which i said okay can't have only  
**Translation:** 

**[2812.66s] English:** lisp that's a language yeah because i you know i don't want to you know you only got 10 or 12 or  
**Translation:** 

**[2817.82s] English:** 15 weeks or whatever it is to teach  
**Translation:** 

**[2819.50s] English:** ai and i don't want to waste two weeks of that teaching lisp so i say i gotta have another  
**Translation:** 

**[2823.90s] English:** language java was the most popular language at the time i started doing that and then i said  
**Translation:** 

**[2828.80s] English:** it's really hard to have a one-to-one correspondence between the pseudocode and the java because java is  
**Translation:** 

**[2835.00s] English:** so verbose uh so then i said i'm gonna do a survey and find the language that's most like  
**Translation:** Vocabulary: verbose: 啰嗦

**[2840.94s] English:** my pseudocode and turned out python basically was my pseudocode somehow i had channeled uh guido  
**Translation:** 

**[2849.50s] English:** designed a pseudocode that was the same as python although i hadn't heard of python  
**Translation:** Vocabulary: channeled: 转移至

**[2853.62s] English:** at that point uh and from then on uh that's what i've been using because it's been a good match  
**Translation:** 

**[2859.18s] English:** so what's the story in python behind pi tudes your github repository with puzzles and exercises  
**Translation:** Vocabulary: repository: 代码仓库

**[2868.18s] English:** and python is pretty fun yeah just it it seems like fun uh you know you know i like uh doing  
**Translation:** 

**[2874.42s] English:** puzzles and i like uh being an educator i did a class with udacity  
**Translation:** Vocabulary: educator: 教育者

**[2879.50s] English:** uh you  
**Translation:** 

**[2880.00s] English:** gassy 212 i think it was it was basically problem solving uh uh using python and looking at different  
**Translation:** 

**[2888.02s] English:** problems this pi tudes feed that class in terms of the exercises i was wondering what the yeah so  
**Translation:** 

**[2893.00s] English:** the class the class came first yeah some of the stuff that's in pi tudes was write-ups of what  
**Translation:** 

**[2897.84s] English:** was in the class and then some of it was just continuing to uh to work on new problems so  
**Translation:** 

**[2904.32s] English:** what's the organizing madness of pi tudes is it just a collection of cool exercises just whatever  
**Translation:** 

**[2910.46s] English:** i thought was fun okay awesome so you were the director of search quality at google from 2001  
**Translation:** 

**[2917.00s] English:** to 2005 in the early days uh when there's just a few employees and when the when the company was  
**Translation:** 

**[2923.82s] English:** growing like crazy right so i mean google revolutionized the way we discover share and  
**Translation:** 

**[2933.44s] English:** aggregate  
**Translation:** Vocabulary: aggregate: 聚合; revolutionized: 革新

**[2934.32s] English:** knowledge so just this is uh this is one of the fundamental aspects of civilization right  
**Translation:** 

**[2941.36s] English:** is information being shared and there's different mechanisms throughout history but google is just  
**Translation:** 

**[2945.74s] English:** 10x improve that right and you're a part of that right people discovering that information so what  
**Translation:** 

**[2952.16s] English:** were some of the challenges on a philosophical or the technical level in those early days  
**Translation:** Vocabulary: philosophical: 哲学的

**[2957.20s] English:** it definitely was an exciting time and as you say we were doubling in size every year  
**Translation:** 

**[2964.32s] English:** and the challenges were we wanted to get the right answers right and uh we had to figure out  
**Translation:** 

**[2971.28s] English:** what that meant we had to implement that and we had to make it all uh efficient and uh  
**Translation:** 

**[2979.68s] English:** we had to keep on testing and seeing if we were delivering good answers  
**Translation:** 

**[2984.00s] English:** and now when you say good answers it means whatever people are typing in in terms of  
**Translation:** 

**[2988.08s] English:** keywords in terms of that kind of thing that the the results they get are ordered by the design team  
**Translation:** Vocabulary: keywords: 关键词

**[2994.16s] English:** desirability for them of those results like they're like the first thing they click on will  
**Translation:** 

**[2998.68s] English:** likely be the thing that they were  
**Translation:** 

**[3000.00s] English:** actually looking for right one of the metrics we had was focused on the first thing uh some of it  
**Translation:** 

**[3005.38s] English:** was focused on the whole page some of it was focused on you know top three or so  
**Translation:** 

**[3010.40s] English:** so we looked at a lot of different metrics for for how well we were doing and we broke it down  
**Translation:** 

**[3016.76s] English:** into subclasses of you know maybe here's a type of uh of uh query that we're not doing well on  
**Translation:** 

**[3023.44s] English:** then we try to fix that uh early on we started to realize that we were in an adversarial position  
**Translation:** 

**[3029.76s] English:** right so we started thinking uh well we're kind of like the card catalog in the library  
**Translation:** Vocabulary: adversarial: 敌对的

**[3035.46s] English:** right so the books are here and we're off to the side and we're just reflecting what's there  
**Translation:** 

**[3041.96s] English:** and then we realized every time we make a change the webmasters make a change and it's a game  
**Translation:** Vocabulary: webmasters: 网站管理员

**[3049.26s] English:** theoretic and so we had to think not only uh is this the right move for us to make now but also  
**Translation:** 

**[3056.02s] English:** if we make this move what's the counter move going to be  
**Translation:** Vocabulary: theoretic: 理论的

**[3059.76s] English:** is that going to get us into a work worse place in which case we won't make that move we'll make  
**Translation:** 

**[3063.94s] English:** a different move and did you find i mean i assume with the popularity and the growth of the internet  
**Translation:** 

**[3069.22s] English:** that people were creating new content so you're almost helping guide the creation yeah so that's  
**Translation:** 

**[3074.88s] English:** certainly true right so we we definitely changed uh the structure of the network right so if you  
**Translation:** 

**[3081.44s] English:** think back you know in the in the very early days uh larry and sergey had the page rank paper  
**Translation:** 

**[3087.60s] English:** and john kleinberg  
**Translation:** Vocabulary: kleinberg: Klein伯格

**[3089.76s] English:** had this uh hubs and authorities model which says the web is made out of these uh hubs which will be  
**Translation:** 

**[3100.16s] English:** my page of cool links about dogs or whatever and people would just list links uh and then there'd  
**Translation:** 

**[3107.12s] English:** be authorities which were the ones uh the page about dogs that most people link to that doesn't  
**Translation:** 

**[3113.28s] English:** happen anymore people don't bother to say my page of cool links because we took over that function  
**Translation:** 

**[3119.76s] English:** later on  
**Translation:** 

**[3130.00s] English:** so  
**Translation:** 

**[3131.20s] English:** but  
**Translation:** 

**[3133.20s] English:** uh  
**Translation:** 

**[3135.20s] English:** i  
**Translation:** 

**[3135.28s] English:** i  
**Translation:** 

**[3137.32s] English:** i  
**Translation:** 

**[3139.28s] English:** i  
**Translation:** 

**[3141.28s] English:** do  
**Translation:** 

**[3143.28s] English:** i  
**Translation:** 

**[3145.28s] English:** do  
**Translation:** 

**[3147.28s] English:** see  
**Translation:** 

**[3120.00s] English:** So we changed the way that worked.  
**Translation:** 

**[3123.32s] English:** Did you imagine back then that the Internet would be as massively vibrant as it is today?  
**Translation:** Vocabulary: massively: 规模极大; vibrant: 充满活力

**[3128.78s] English:** I mean, it was already growing quickly, but it's just another.  
**Translation:** 

**[3132.68s] English:** I don't know if you've ever.  
**Translation:** 

**[3134.56s] English:** Today, if you sit back and just look at the Internet with wonder, the amount of content that's just constantly being created, constantly being shared and deployed.  
**Translation:** 

**[3144.24s] English:** Yeah, it's always been surprising to me.  
**Translation:** Vocabulary: deployed: 发布

**[3147.12s] English:** I guess I'm not very good at predicting the future in the future.  
**Translation:** 

**[3150.54s] English:** And I remember, you know, being a graduate student in 1980 or so.  
**Translation:** 

**[3155.88s] English:** And, you know, we had the ARPANET.  
**Translation:** 

**[3159.12s] English:** And then there was this proposal to commercialize it and have this Internet.  
**Translation:** 

**[3165.52s] English:** And this crazy Senator Gore thought that might be a good idea.  
**Translation:** 

**[3170.76s] English:** And I remember thinking, oh, come on.  
**Translation:** 

**[3173.10s] English:** You can't expect a commercial company to understand this technology.  
**Translation:** 

**[3177.76s] English:** They'll never be able to do it.  
**Translation:** 

**[3179.36s] English:** Yeah, OK, we can have this dot com domain, but it won't go anywhere.  
**Translation:** 

**[3183.12s] English:** So I was wrong.  
**Translation:** 

**[3184.56s] English:** Al Gore was right.  
**Translation:** 

**[3185.60s] English:** At the same time, the nature of what it means to be a commercial company has changed, too.  
**Translation:** 

**[3190.02s] English:** So Google, at its founding, is different than, you know, what companies were before, I think.  
**Translation:** 

**[3196.70s] English:** Right. So there's all these business models that are so different than what was possible back then.  
**Translation:** Vocabulary: founding: 创立

**[3203.08s] English:** So in terms of predicting the future, what do you think it takes to build a system?  
**Translation:** 

**[3207.12s] English:** That approach is human level intelligence.  
**Translation:** 

**[3209.94s] English:** You've talked about, of course, that, you know, we shouldn't be so obsessed about creating human level intelligence.  
**Translation:** 

**[3216.30s] English:** We just create systems that are very useful for humans.  
**Translation:** 

**[3219.24s] English:** But what do you think it takes to approach that level?  
**Translation:** 

**[3224.88s] English:** Right. So certainly I don't think human level intelligence is one thing.  
**Translation:** 

**[3229.50s] English:** Right. So I think there's lots of different tasks, lots of different capabilities.  
**Translation:** 

**[3233.96s] English:** I also don't think that should be the goal.  
**Translation:** 

**[3236.28s] English:** Right.  
**Translation:** 

**[3236.72s] English:** So.  
**Translation:** 

**[3237.04s] English:** You know, I wouldn't want to create a.  
**Translation:** 

**[3240.80s] English:** calculator that could do multiplication at human level right that would be a step backwards and so  
**Translation:** Vocabulary: backwards: 倒退; multiplication: 乘法

**[3246.48s] English:** for many things we should be aiming far beyond human level uh for other things uh maybe human  
**Translation:** 

**[3252.64s] English:** level is a good level to aim at uh and for others we'd say well let's not bother doing this because  
**Translation:** 

**[3258.16s] English:** we are we already have humans can take on those tasks so as you say i like to focus on what what's  
**Translation:** 

**[3264.96s] English:** a useful tool and and in some cases being on human level is an important part of crossing  
**Translation:** 

**[3271.84s] English:** that threshold to make the tool useful so we see in things like these uh personal assistants now  
**Translation:** 

**[3279.20s] English:** that you get either on your phone or on a speaker that sits on the table  
**Translation:** 

**[3284.40s] English:** you want to be able to have a conversation with those and and i think as an industry  
**Translation:** 

**[3289.68s] English:** we haven't quite figured out what the right model is for what these things can do  
**Translation:** 

**[3294.96s] English:** we're aiming towards well you just have a conversation with them the way you can with  
**Translation:** 

**[3298.56s] English:** a person right uh but we haven't delivered on that model yet right so you can ask it  
**Translation:** 

**[3304.00s] English:** what's the weather you can ask it play some nice songs uh and uh you know five or six other things  
**Translation:** 

**[3311.44s] English:** and then you run out of stuff that it can do in terms of a deep meaningful connection so  
**Translation:** 

**[3316.48s] English:** you've mentioned the movie her as one of your favorite ai movies do you think it's possible  
**Translation:** 

**[3321.12s] English:** for a human being to fall in love with an ai system ai assistant does that work for you  
**Translation:** 

**[3324.96s] English:** you mentioned so taking this big leap from uh what's the weather to you know having a deep  
**Translation:** 

**[3330.64s] English:** connection yeah i i think uh as people that's what we love to do and i i was at a showing of her where  
**Translation:** 

**[3339.44s] English:** we had a panel discussion and and somebody asked me uh what other movie do you think her is similar  
**Translation:** 

**[3345.84s] English:** to and my answer was uh life of brian which which is not a science fiction movie uh but both movies  
**Translation:** 

**[3354.96s] English:** are about wanting to believe in something that's not necessarily real  
**Translation:** 

**[3360.00s] English:** yeah by the way for people don't know it's monty python yeah yeah that's brilliantly put right so  
**Translation:** Vocabulary: brilliantly: 妙哉

**[3365.64s] English:** so i mean i think that's just the way we are we we want to trust we want to believe we want to  
**Translation:** 

**[3371.56s] English:** fall in love and uh it doesn't necessarily take that much right so uh you know my kids uh fell  
**Translation:** 

**[3379.08s] English:** in love with their teddy bear and the teddy bear was not very interactive right so that's all us  
**Translation:** 

**[3384.42s] English:** pushing our feelings onto our devices and our things and i think that that's what we like to  
**Translation:** Vocabulary: interactive: 互动; teddy: 泰迪熊

**[3391.68s] English:** do so we'll continue to do that so yeah as human beings we long for that connection and just ai has  
**Translation:** 

**[3397.26s] English:** to uh do a little bit of work to uh to catch us in the other end yeah and certainly you know  
**Translation:** 

**[3403.28s] English:** if you can get to uh dog level a lot of people have invested a lot of uh love in their pets in  
**Translation:** 

**[3409.62s] English:** their pets some some people as i've been told in working with autonomous vehicles  
**Translation:** 

**[3414.42s] English:** have invested a lot of love into their inanimate cars yeah so it it really doesn't take much yeah  
**Translation:** 

**[3420.60s] English:** so what is a good test to linger on a topic that may be silly or a little bit philosophical what  
**Translation:** Vocabulary: inanimate: 无生命的; philosophical: 哲学的

**[3427.96s] English:** is a good test of intelligence in your view is natural conversation like in the touring test a  
**Translation:** 

**[3434.52s] English:** good a good test put another way what would impress you yeah if you saw a computer do it  
**Translation:** 

**[3441.56s] English:** these days yeah i mean i get impressed all the time  
**Translation:** 

**[3444.42s] English:** right but i'm really impressed you know go playing uh starcraft playing uh those are all pretty cool  
**Translation:** Vocabulary: starcraft: 星际争霸

**[3452.92s] English:** you know and i think uh sure conversation is important i think uh  
**Translation:** 

**[3461.06s] English:** you know we sometimes have these tests where it's easy to fool the system where you can have a  
**Translation:** 

**[3468.36s] English:** chat bot that can have a conversation but you never uh it never gets into a situation  
**Translation:** 

**[3474.40s] English:** where it has to be deep enough that uh it really reveals itself as being intelligent or  
**Translation:** 

**[3480.00s] English:** not i think uh you know turing suggested that uh but i think if he were alive he'd say you know i  
**Translation:** 

**[3488.32s] English:** didn't really mean that seriously right yeah and i think uh you know this is just my opinion but  
**Translation:** Vocabulary: turing: 图灵

**[3495.28s] English:** i think turing's point was not that uh this test of conversation is a good test i think his point  
**Translation:** 

**[3502.32s] English:** was having a test is the right thing so rather than having the philosopher say oh no ai is  
**Translation:** 

**[3509.04s] English:** impossible you should say well we'll just have a test and then the result of that will will tell us  
**Translation:** 

**[3513.92s] English:** the answer and doesn't necessarily have to be a conversation test that's right and coming up a new  
**Translation:** 

**[3518.48s] English:** better test as the technology evolves is probably the right way do you worry as a lot of the general  
**Translation:** 

**[3524.88s] English:** public does about not a lot but some vocal part of the general public about the existential threat of  
**Translation:** Vocabulary: existential: 根本的; vocal: 直言不讳的

**[3532.48s] English:** artificial intelligence so looking farther into the future as you said most of us are not able  
**Translation:** 

**[3537.76s] English:** to predict much so we're not going to be able to predict what's going to happen in the future  
**Translation:** 

**[3539.04s] English:** so when shrouded in such mystery there's a concern of well you think start thinking about worst case  
**Translation:** 

**[3544.96s] English:** is that something that occupies your mind space much so i certainly think about threats i think  
**Translation:** Vocabulary: shrouded: 笼罩

**[3551.76s] English:** about dangers and i think any new technology has positives and negatives and if it's a powerful  
**Translation:** 

**[3560.72s] English:** technology it can be used for bad as well as for good so i'm certainly not worried about  
**Translation:** Vocabulary: positives: 正面影响

**[3567.12s] English:** the robot apocalypse  
**Translation:** 

**[3569.76s] English:** and the terminator type scenarios i am worried about change in employment and uh are we going  
**Translation:** Vocabulary: apocalypse: 世界末日; scenarios: 情景; terminator: 终结者

**[3579.12s] English:** to be able to react fast enough to deal with that i think we're you know we're already seeing it  
**Translation:** 

**[3583.60s] English:** today where a lot of people are are disgruntled about uh the way income inequality is working and  
**Translation:** Vocabulary: disgruntled: 不满; inequality: 不平等

**[3591.36s] English:** and automation could help accelerate those kinds of problems i see powerful technologies can always  
**Translation:** 

**[3597.84s] English:** be used as weapons  
**Translation:** Vocabulary: accelerate: 加速; automation: 自动化

**[3599.04s] English:** uh  
**Translation:** 

**[3599.76s] English:** you  
**Translation:** 

**[3600.00s] English:** whether they're robots or drones or whatever uh some of that uh we're seeing due to ai a lot of  
**Translation:** 

**[3606.58s] English:** it uh you don't need ai and i don't know what's uh what's the worst threat if it's a autonomous  
**Translation:** Vocabulary: autonomous: 自主的; drones: 无人机

**[3613.62s] English:** drone or uh it's uh crisper technology becoming available or we have lots of uh threats to face  
**Translation:** 

**[3621.26s] English:** and some of them involve ai and some of them don't so the threats that technology presents  
**Translation:** 

**[3627.08s] English:** are you for the most part optimistic about technology also alleviating those threats  
**Translation:** 

**[3632.82s] English:** or creating new opportunities or protecting us from the more detrimental effects of these yeah  
**Translation:** Vocabulary: alleviating: 减轻; optimistic: 乐观

**[3638.84s] English:** i don't know it again it's hard to predict the future and uh yes as a society so far we've  
**Translation:** 

**[3645.64s] English:** survived uh nuclear and other things of course uh only societies that have survived are having  
**Translation:** 

**[3653.88s] English:** this conversation so uh maybe that's uh  
**Translation:** 

**[3657.08s] English:** yeah what problem stands out to you as exciting challenging impactful to work on in the near  
**Translation:** 

**[3664.40s] English:** future for yourself for the community in broadly so i you know we talked about these uh assistance  
**Translation:** 

**[3672.00s] English:** and conversation i think that's a great area i think uh combining uh common sense reasoning  
**Translation:** 

**[3680.14s] English:** with the power of data is a great area in which application  
**Translation:** 

**[3687.08s] English:** in in conversation relations just broadly just in general yeah as a programmer i'm interested in  
**Translation:** Vocabulary: programmer: 程序员

**[3693.92s] English:** programming tools both in terms of uh you know the current systems we have today with with tensorflow  
**Translation:** 

**[3700.94s] English:** and so on can we make them much easier to use for broader class of people and also can we apply  
**Translation:** 

**[3707.62s] English:** machine learning to the more traditional type of programming right so you know when you go to  
**Translation:** 

**[3714.20s] English:** google and you uh type in a  
**Translation:** 

**[3717.08s] English:** query and you spell something wrong it says did you mean  
**Translation:** 

**[3720.00s] English:** And the reason we're able to do that is because lots of other people made a similar error and then they corrected it.  
**Translation:** 

**[3726.26s] English:** We should be able to go into our code bases and our bug fix bases.  
**Translation:** 

**[3730.94s] English:** And when I type a line of code, it should be able to say, did you mean such and such?  
**Translation:** 

**[3735.12s] English:** If you type this today, you're probably going to type in this bug fix tomorrow.  
**Translation:** 

**[3740.38s] English:** Yeah, that's a really exciting application of almost an assistant for the coding programming experience at every level.  
**Translation:** 

**[3748.28s] English:** So I think I could safely speak for the entire AI community.  
**Translation:** 

**[3755.08s] English:** First of all, for thanking you for the amazing work you've done, certainly for the amazing work you've done with AI, a modern approach book.  
**Translation:** 

**[3763.00s] English:** I think we're all looking forward very much for the fourth edition and then the fifth edition and so on.  
**Translation:** 

**[3768.34s] English:** So, Peter, thank you so much for talking today.  
**Translation:** 

**[3771.40s] English:** Yeah, thank you. Pleasure.  
**Translation:** 

**[3778.28s] English:** Thank you.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
