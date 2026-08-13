# Podcast vocabulary notes
Source file: Lex Fridman - Sergey Levine： Robotics and Machine Learning ｜ Lex Fridman Podcast #108.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Sergey Levine, a professor at Berkeley and a world-class researcher in deep learning, reinforcement learning, robotics, and computer vision.  
**Translation:** 

**[10.38s] English:** Including the development of algorithms for end-to-end training of neural network policies that combine perception and control,  
**Translation:** 

**[17.60s] English:** Scalable algorithms for inverse reinforcement learning, and, in general, deep RL algorithms.  
**Translation:** 

**[23.52s] English:** Quick summary of the ads: Two sponsors, Cash App and ExpressVPN.  
**Translation:** Vocabulary: inverse: 逆向的; reinforcement: 强化; scalable: 可扩展的; sponsors: 赞助商

**[27.98s] English:** Please consider supporting the podcast by downloading Cash App and using code LEXPODCAST, and signing up at expressvpn.com/lexpod.  
**Translation:** 

**[38.46s] English:** Click the links, buy the stuff. It's the best way to support this podcast and, in general, the journey I'm on.  
**Translation:** Vocabulary: expressvpn: 迅捷vpn

**[46.22s] English:** If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcasts, follow on Spotify, support it on Patreon, or connect with me on Twitter at @LexFriedman.  
**Translation:** 

**[57.32s] English:** I do.  
**Translation:** Vocabulary: patreon: Patreon支持; subscribe: 订阅

**[57.98s] English:** As usual, I'll do a few minutes of ads now, and never any ads in the middle that can break the flow of the conversation.  
**Translation:** 

**[63.60s] English:** This show is presented by Cash App, the number-one finance app in the App Store.  
**Translation:** 

**[68.38s] English:** When you get it, use code LEXPODCAST.  
**Translation:** 

**[71.62s] English:** Cash App lets you send money to friends, buy Bitcoin, and invest in the stock market with as little as $1.  
**Translation:** 

**[78.02s] English:** Since Cash App offers fractional share trading, let me mention that the order-execution algorithm that works behind the scenes,...  
**Translation:** 

**[84.76s] English:** To create the abstraction of fractional orders.  
**Translation:** Vocabulary: abstraction: 抽象; algorithm: 算法; fractional: 分割的

**[87.98s] English:** It's an algorithmic marvel.  
**Translation:** 

**[90.16s] English:** So, big props to the Cash App engineers for taking a step up to the next layer of abstraction in the stock market.  
**Translation:** Vocabulary: algorithmic: 算法的; marvel: 奇迹; props: 称赞

**[95.84s] English:** Making trading more accessible for new investors and diversification much easier.  
**Translation:** 

**[101.48s] English:** So, again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST, you get $10.  
**Translation:** Vocabulary: diversification: 风险分散

**[109.36s] English:** And Cash App will also donate $10 to FIRST,  
**Translation:** 

**[112.30s] English:** An organization that is helping to advance robotics and STEM education for young people.  
**Translation:** Vocabulary: donate: 捐赠; robotics: 机器人技术

**[117.98s] English:** So, thanks again to Cash App, and how you're helping to change the world.  
**Translation:** 

**[119.66s] English:** This show is presented by Cash App, the number-one finance app in the App Store.  
**Translation:** 

**[120.00s] English:** Is also sponsored by ExpressVPN.  
**Translation:** 

**[123.72s] English:** Get it at expressvpn.com/lexpod.  
**Translation:** Vocabulary: expressvpn: 迅捷vpn; sponsored: 赞助

**[124.24s] English:** Thanks again to our sponsors.  
**Translation:** 

**[125.08s] English:** Cash App is a powerful source of information and insight for the future of our business and for our customers.  
**Translation:** Vocabulary: sponsors: 赞助商

**[127.70s] English:** To support this podcast:  
**Translation:** 

**[127.78s] English:** Cash App is an opportunity to help others make a difference in the world.  
**Translation:** 

**[129.26s] English:** And to get an extra three months free.  
**Translation:** 

**[130.50s] English:** This show is presented by Cash App, the number-one finance app in the App Store.  
**Translation:** 

**[132.22s] English:** On a one-year package.  
**Translation:** 

**[133.16s] English:** Ronald Reagan is the number-one finance app in the App Store.  
**Translation:** 

**[134.10s] English:** I've been using ExpressVPN for many years.  
**Translation:** 

**[135.26s] English:** Thank you for watching this video.  
**Translation:** 

**[136.02s] English:** If you haven't subscribed to our channel yet, please subscribe to our channel. And we'll see you next time.  
**Translation:** 

**[137.34s] English:** I love it.  
**Translation:** Vocabulary: subscribe: 订阅; subscribed: 已订阅

**[138.02s] English:** Thanks for watching this video.  
**Translation:** 

**[138.56s] English:** And next time, we'll talk about how Cash App can help a person take a step further and help a child achieve success.  
**Translation:** 

**[138.58s] English:** I think ExpressVPN is the best VPN out there.  
**Translation:** 

**[140.00s] English:** So, thanks again to our sponsors, and we'll see you next time.  
**Translation:** 

**[141.88s] English:** They told me to say it.  
**Translation:** 

**[143.04s] English:** But it happens to be true, in my humble opinion.  
**Translation:** Vocabulary: humble: 谦逊

**[145.98s] English:** It doesn't log your data.  
**Translation:** 

**[147.32s] English:** It's crazy fast, and it's easy to use.  
**Translation:** 

**[150.06s] English:** Literally, just one big power-on button.  
**Translation:** 

**[152.80s] English:** Again, it's probably obvious to you.  
**Translation:** 

**[154.78s] English:** But I should say it again.  
**Translation:** 

**[156.48s] English:** It's really important that they don't log your data.  
**Translation:** 

**[159.98s] English:** It works on Linux and every other operating system.  
**Translation:** 

**[163.20s] English:** But Linux, of course, is the best operating system.  
**Translation:** 

**[166.56s] English:** Shout out to my favorite flavor, Ubuntu MATE 20.04.  
**Translation:** 

**[170.54s] English:** Once again, get it at expressvpn.com/lexpod.  
**Translation:** 

**[174.02s] English:** To support this podcast:  
**Translation:** 

**[175.46s] English:** And to get an extra three months free.  
**Translation:** 

**[178.36s] English:** On a one-year package.  
**Translation:** 

**[180.00s] English:** And now, here's my conversation with Sergei Levine.  
**Translation:** 

**[185.26s] English:** What's the difference between a state-of-the-art human,  
**Translation:** 

**[188.60s] English:** Such as you and I,  
**Translation:** 

**[189.92s] English:** Well, I don't know if we qualify as state-of-the-art humans.  
**Translation:** 

**[191.92s] English:** But which is better: a state-of-the-art human or a state-of-the-art robot?  
**Translation:** 

**[196.10s] English:** That's a very interesting question.  
**Translation:** 

**[198.68s] English:** Robot capability is kind of a,  
**Translation:** 

**[202.26s] English:** I think it's a very tricky thing to understand.  
**Translation:** 

**[205.10s] English:** Because there are some things that are difficult.  
**Translation:** Vocabulary: tricky: 棘手的

**[208.08s] English:** That we wouldn't think are difficult.  
**Translation:** 

**[209.16s] English:** And some things are easy to understand.  
**Translation:** 

**[209.84s] English:** And there's also a really big gap.  
**Translation:** 

**[214.24s] English:** Between the capabilities of robots,  
**Translation:** Vocabulary: capabilities: 能力

**[216.12s] English:** In terms of hardware and their physical capabilities,  
**Translation:** 

**[218.68s] English:** And the capabilities of robots.  
**Translation:** 

**[220.28s] English:** In terms of what they can do autonomously.  
**Translation:** 

**[222.54s] English:** There is a little video.  
**Translation:** Vocabulary: autonomously: 独立地

**[224.10s] English:** That I think robotics researchers really like to show,  
**Translation:** 

**[227.18s] English:** Especially, robotics learning researchers like myself,  
**Translation:** Vocabulary: robotics: 机器人技术

**[228.84s] English:** From 2004, from Stanford,  
**Translation:** 

**[231.78s] English:** Which demonstrates a prototype robot called PR1.  
**Translation:** Vocabulary: prototype: 样品; stanford: 斯坦福大学

**[235.34s] English:** And the PR1 was a robot that was designed.  
**Translation:** 

**[237.08s] English:** As a home-assistance robot.  
**Translation:** 

**[239.04s] English:** And there's this beautiful,  
**Translation:** 

**[239.84s] English:** Beautiful,  
**Translation:** 

**[240.00s] English:** Video showing the PR version, tidying up a living room, putting away toys, and at the end, bringing  
**Translation:** 

**[245.70s] English:** A beer for the person sitting on the couch, which looks really amazing. And then the punchline is:  
**Translation:** Vocabulary: punchline: 笑点

**[253.02s] English:** That this robot is entirely controlled by a person. So, in some ways, the gap between a  
**Translation:** 

**[258.46s] English:** State-of-the-art human and a state-of-the-art robot, if the robot has a human brain, is actually  
**Translation:** 

**[262.68s] English:** Not that large. Now, obviously, human bodies are sophisticated and very robust and resilient.  
**Translation:** 

**[267.30s] English:** Many ways, but on the whole, if we're willing to spend a bit of money and do a bit of engineering,  
**Translation:** Vocabulary: resilient: 有弹性的; robust: 强壮的; sophisticated: 复杂的

**[272.44s] English:** We can kind of close the hardware gap, almost. But the intelligence gap? That one is very wide.  
**Translation:** 

**[280.10s] English:** And when you say "hardware," you're referring to the physical, sort of the actuators,  
**Translation:** Vocabulary: actuators: 执行器

**[283.80s] English:** The actual body of the robot, as opposed to the hardware on which the cognition,  
**Translation:** 

**[288.04s] English:** The hardware of the nervous system. Yes, exactly. I'm referring to the body rather than the mind.  
**Translation:** Vocabulary: cognition: 认知

**[294.02s] English:** So, that means that the work is cut out for us.  
**Translation:** 

**[297.30s] English:** While we can still make the body better, we kind of know that the big bottleneck right now is really  
**Translation:** Vocabulary: bottleneck: 瓶颈

**[301.06s] English:** The mind. And how big is that gap? How big is the difference in your sense of ability to learn?  
**Translation:** 

**[309.66s] English:** Ability to reason, ability to perceive the world: the gap between humans and our best robots?  
**Translation:** Vocabulary: perceive: 感知

**[316.88s] English:** The gap is very large, and the gap becomes even larger the more unexpected the event.  
**Translation:** 

**[321.68s] English:** Events can happen in the world. So, essentially, the spectrum along which you can measure,...  
**Translation:** 

**[327.30s] English:** The size of that gap is the spectrum of how open the world is. If you control everything, in the  
**Translation:** 

**[333.12s] English:** World very tightly; if you put the robot in, like in a factory, and you tell it where everything is,  
**Translation:** 

**[337.36s] English:** And you rigidly program its motion, then it can do things—you know, one might even say,  
**Translation:** 

**[342.50s] English:** In a superhuman way, it can move faster, it's stronger, it can lift up a car, and things like that.  
**Translation:** Vocabulary: rigidly: 严格地

**[346.22s] English:** That. But as soon as anything starts to vary in the environment, it'll trip us up. And if many,  
**Translation:** 

**[351.92s] English:** Many things vary, like they would. For example, in your kitchen, then things are pretty much  
**Translation:** 

**[356.76s] English:** Wide open.  
**Translation:** 

**[357.28s] English:** Now, again, we're going to stick.  
**Translation:** 

**[360.00s] English:** A bit on the philosophical questions, but uh, how much on the human side of cognitive abilities?  
**Translation:** 

**[367.20s] English:** In your sense, is nature versus nurture? So, how much of it is a product of?  
**Translation:** Vocabulary: cognitive: 认知; nurture: 养育; philosophical: 哲学的

**[374.56s] English:** Evolution, and how much of it is something we'll learn "from scratch" — yeah, from the day we're  
**Translation:** 

**[380.94s] English:** Born, I'll read into your question as asking about the implications of this for AI.  
**Translation:** Vocabulary: implications: 含义; scratch: 从头开始

**[386.14s] English:** Because I'm not a biologist, I can't really speak authoritatively, so and to linger on it if.  
**Translation:** 

**[392.02s] English:** If it's all about learning, then there's more hope for AI, yeah. So, the way I look at it,...  
**Translation:** Vocabulary: authoritatively: 有权威地; biologist: 生物学家; linger: 停留

**[399.54s] English:** This is that, um, you know, well, first of all, biology is very messy, and it's if you ask the  
**Translation:** 

**[407.02s] English:** Question: How does a person do something, or how does a person's mind do something? You can come.  
**Translation:** 

**[411.56s] English:** Up with a bunch of hypotheses, and oftentimes you can find support for many different ones.  
**Translation:** 

**[415.66s] English:** Conflicting hypotheses.  
**Translation:** Vocabulary: conflicting: 相互矛盾的; hypotheses: 假设; oftentimes: 经常

**[416.14s] English:** Um, one way that we can approach the question of what the implications of this are for AI.  
**Translation:** 

**[423.18s] English:** Is there something sufficient we can think about? So, for example, maybe a person is born very, very good.  
**Translation:** 

**[429.74s] English:** At some things, like, for example, recognizing faces, there's a very strong evolutionary pressure to do so.  
**Translation:** 

**[433.74s] English:** That, if you can recognize your mother's face, then you're more likely to survive, and therefore people,...  
**Translation:** Vocabulary: evolutionary: 进化的

**[439.08s] English:** Are good at this, but we can also ask: "What's the minimum sufficient thing, right?" And one.  
**Translation:** 

**[444.38s] English:** Of the ways that we can study the minimal sufficient thing, we can study the  
**Translation:** Vocabulary: minimal: 最少的

**[446.14s] English:** Things that we can study include the minimal sufficient condition, for example, by seeing what people do.  
**Translation:** 

**[448.24s] English:** In unusual situations, if you present them with things that evolution couldn't have prepared them for.  
**Translation:** 

**[452.16s] English:** For, you know, our daily lives actually do this to us all the time. We didn't evolve to deal with  
**Translation:** 

**[457.96s] English:** You know, automobiles and space flight, and whatever—so there are all these situations that we can find.  
**Translation:** Vocabulary: automobiles: 汽车; evolve: 进化

**[462.88s] English:** Ourselves in, uh, and we do very well there. Like, I can give you a joystick to control a robotic arm.  
**Translation:** 

**[469.40s] English:** Which you've never used before, and you might be pretty bad for the first couple of seconds, but  
**Translation:** Vocabulary: joystick: 操纵杆; robotic: 机械臂的

**[472.84s] English:** If I tell you like your life depends on using this robotic arm, to do things that you're  
**Translation:** 

**[476.14s] English:** Like, open this door. You'll probably manage it, even though you've  
**Translation:** 

**[480.00s] English:** Ever seen this device before? You've never used the joystick controllers, and you'll kind of muddle.  
**Translation:** 

**[483.86s] English:** Through it, and that's not, uh, your evolved natural ability—that's your flexibility.  
**Translation:** Vocabulary: evolved: 进化; flexibility: 灵活性; muddle: 混淆

**[490.14s] English:** Adaptability, and that's exactly where our current robotic systems really kind of fall flat, but I  
**Translation:** 

**[495.00s] English:** Wonder how much, generally speaking, of what we think of as common sense pre-trained models actually possess underneath all.  
**Translation:** Vocabulary: adaptability: 适应性; underneath: 在……下面

**[503.26s] English:** Of that, so that ability to adapt to a joystick is something that requires you to have a kind of, you know, I'm human.  
**Translation:** 

**[512.60s] English:** So, it's hard for me to introspect all the knowledge I have about the world, but it seems like there  
**Translation:** Vocabulary: introspect: 自我反省

**[517.60s] English:** Might be an iceberg under the amount of knowledge we actually bring to the table that's  
**Translation:** 

**[523.36s] English:** Kind of an open question, I think there's absolutely an iceberg of  
**Translation:** Vocabulary: iceberg: 隐藏部分

**[526.30s] English:** Knowledge that we bring to the table, but I think it's very likely that iceberg of knowledge is.  
**Translation:** 

**[531.50s] English:** Actually, it builds up over our lifetimes.  
**Translation:** Vocabulary: lifetimes: 一生

**[533.02s] English:** Because we have a lot of prior experience to draw on, and it kind of makes  
**Translation:** 

**[539.80s] English:** Sense that the right way for us to, you know, optimize our efficiency and evolutionary process.  
**Translation:** Vocabulary: evolutionary: 进化; optimize: 优化

**[546.26s] English:** Fitness and so on is to utilize all that experience to build up the best iceberg we can.  
**Translation:** 

**[552.08s] English:** Can get, uh, and that's actually one of the things that sounds a lot like what machines do.  
**Translation:** Vocabulary: utilize: 利用

**[556.64s] English:** Learning actually does, I think that for modern machine learning, it's actually a really big  
**Translation:** 

**[560.32s] English:** Challenge to take this unstructured, massive experience and build the best iceberg.  
**Translation:** Vocabulary: unstructured: 无结构的

**[563.02s] English:** Experience and distill out something that looks like a common-sense understanding of the world.  
**Translation:** 

**[567.60s] English:** And perhaps part of that isn't because something about machine learning itself is.  
**Translation:** Vocabulary: distill: 提炼

**[572.80s] English:** Broken or hard, but because we've been a little too rigid in subscribing to a very supervised, very  
**Translation:** 

**[579.34s] English:** A rigid notion of learning, you know, kind of the input-output X's go to Y's sort of model.  
**Translation:** Vocabulary: subscribing: 订阅; supervised: 监管

**[583.46s] English:** And maybe what we really need to do is to view the world more as a massive experience.  
**Translation:** 

**[591.08s] English:** That is not necessarily providing.  
**Translation:** 

**[593.02s] English:** Any rigid supervision, but sort of providing many, many instances of things that could be.  
**Translation:** 

**[596.52s] English:** And then you take that and you distill it into some sort of common sense.  
**Translation:** 

**[600.00s] English:** Understanding. I see. Well, you're painting an optimistic, beautiful picture, especially from this perspective.  
**Translation:** 

**[606.16s] English:** From a robotics perspective, because that means we just need to invest and build better learning.  
**Translation:** Vocabulary: optimistic: 乐观; robotics: 机器人技术

**[610.70s] English:** Algorithms figure out how we can get access to more and more data for those learning algorithms.  
**Translation:** 

**[617.30s] English:** To extract signals from and then accumulate that iceberg of knowledge—it's a beautiful picture.  
**Translation:** Vocabulary: accumulate: 累积; extract: 提取; iceberg: 知识冰山

**[623.94s] English:** It's a hopeful one. I think it's potentially a little bit more than just that, and this is...  
**Translation:** 

**[629.32s] English:** Where we perhaps reach the limits of our current understanding. But one thing that I think is  
**Translation:** 

**[634.64s] English:** The research community hasn't really resolved in a satisfactory way how much it matters where.  
**Translation:** 

**[640.48s] English:** That experience comes from. Do you just download everything on the internet and cram it in?  
**Translation:** Vocabulary: satisfactory: 令人满意的

**[645.66s] English:** Essentially, the 21st-century analog of the giant language model, and then see what happens? Or  
**Translation:** 

**[652.80s] English:** Does it actually matter whether your machine physically experiences the world in the sense?  
**Translation:** Vocabulary: analog: 模拟物

**[658.42s] English:** That is actually what it attempts to do?  
**Translation:** 

**[659.32s] English:** It observes the outcome of its actions and kind of augments its experience that way.  
**Translation:** Vocabulary: augments: 增强; observes: 观察

**[663.60s] English:** That it chooses which parts of the world it gets to interact with, observe, and learn from.  
**Translation:** 

**[670.32s] English:** Right. It may be that the world is so complex that simply obtaining a large mass of data is not enough.  
**Translation:** 

**[676.78s] English:** Samples of the world is a very difficult way to go. But if you are actually interacting with the  
**Translation:** 

**[683.70s] English:** World, and essentially performing this sort of hard negative mining by attempting what you think.  
**Translation:** Vocabulary: interacting: 互动

**[687.62s] English:** Might work, observing the...  
**Translation:** 

**[689.32s] English:** Sometimes, happy and sometimes sad outcomes of that, and augmenting your understanding using that.  
**Translation:** Vocabulary: augmenting: 增加; outcomes: 结果

**[695.14s] English:** Experience, and you're just doing this continually for many years; maybe that sort of data in some  
**Translation:** 

**[700.20s] English:** Sense is actually much more favorable to obtaining a common-sense understanding. One reason we might  
**Translation:** 

**[705.32s] English:** Think that this is true is that what we associate with common sense or lack of common sense is often  
**Translation:** 

**[712.46s] English:** Characterized by the ability to reason about kinds of counterfactual questions, like "If I were to  
**Translation:** Vocabulary: counterfactual: 假设情况

**[719.32s] English:** Take a shot at eating an egg, and I wanted to know what would happen to it; I would probably  
**Translation:** 

**[720.00s] English:** This bottle of water is sitting on the table. Everything is fine if I were to knock it over, which I'm not going to do.  
**Translation:** 

**[724.12s] English:** We don't see the same response that we get anywhere else.  
**Translation:** 

**[725.04s] English:** But if I were to do that, what would happen?  
**Translation:** 

**[727.34s] English:** And I know that nothing good would happen from that.  
**Translation:** 

**[729.96s] English:** If you were to take a shot at eating an egg and you thought, "Oh, I'm going to eat," begin to read.  
**Translation:** 

**[730.24s] English:** But if I have a bad understanding of the world, I might think that that's a good way for me to, like, you know, gain more utility.  
**Translation:** 

**[735.60s] English:** If I actually go about my daily life doing the things that my current understanding of the world suggests will give me high utility, in some ways, I'll get exactly the right supervision to tell me not to do those bad things and to keep doing the good things.  
**Translation:** Vocabulary: supervision: 监督; utility: 效用

**[739.64s] English:** As it's called, or if you were to take a shot at eating an egg and you thought there was an  
**Translation:** 

**[743.20s] English:** An example of having an egg that did not get eaten: what is this?  
**Translation:** 

**[746.72s] English:** What is this?  
**Translation:** 

**[748.00s] English:** What is this?  
**Translation:** 

**[748.56s] English:** What is this?  
**Translation:** 

**[749.00s] English:** What is this?  
**Translation:** 

**[749.24s] English:** What is this?  
**Translation:** 

**[749.28s] English:** What is this?  
**Translation:** 

**[752.72s] English:** So, there's a spectrum between IID, random walk through the space of data, and then there's what we humans do.  
**Translation:** 

**[761.02s] English:** Well, I don't even know if we do it optimally, but that might be beyond us.  
**Translation:** Vocabulary: optimally: 最优化地

**[765.20s] English:** What?  
**Translation:** 

**[765.60s] English:** So, this open question that you raised: where do you think intelligent systems that would be able to deal with this world fall?  
**Translation:** 

**[776.26s] English:** Can we do a pretty good job by reading all of Wikipedia, sort of randomly sampling it, like language models do?  
**Translation:** 

**[783.64s] English:** Or do we have to be exceptionally selective and intelligent about which aspects of the world we interact with?  
**Translation:** Vocabulary: exceptionally: 特别地; selective: 有选择的

**[791.70s] English:** So, I think this is, first, an open scientific problem.  
**Translation:** 

**[794.48s] English:** And I don't have, like, a clear...  
**Translation:** 

**[795.60s] English:** I don't have a clear answer, but I can speculate a little bit.  
**Translation:** 

**[797.84s] English:** And what I would speculate is that you don't need to be super, super careful.  
**Translation:** Vocabulary: speculate: 猜测

**[803.28s] English:** I think it's less about, like, being careful to avoid the useless stuff and more about making sure that you hit on the really important stuff.  
**Translation:** 

**[811.54s] English:** So, perhaps it's okay if you spend part of your day just, you know, guided by your curiosity, visiting interesting regions of your state space.  
**Translation:** 

**[819.88s] English:** But it's important for you to, you know, every once in a while, make sure that you really try out the...  
**Translation:** 

**[825.60s] English:** Solutions that your current model of the world suggests might be effective, and observe whether those solutions are working as you expect or not.  
**Translation:** 

**[832.42s] English:** And perhaps some of that is really essential to have a kind of perpetual improvement loop.  
**Translation:** 

**[840.00s] English:** The actual improvement loop is really like that—that's really the key, the key that's going to  
**Translation:** Vocabulary: perpetual: 永续的

**[843.80s] English:** Potentially, distinguish the best current methods from the best methods of tomorrow in a sense.  
**Translation:** 

**[848.38s] English:** How important do you think exploration or totally out-of-the-box thinking is?  
**Translation:** 

**[852.28s] English:** Thinking about exploration in this space as you jump to totally different domains, so you kind of mentioned,...  
**Translation:** 

**[860.18s] English:** There's an optimization problem you kind of explore the specifics of a particular strategy.  
**Translation:** Vocabulary: optimization: 最优化问题

**[865.58s] English:** Whatever the thing you're trying to solve, how important is it to explore totally outside of?  
**Translation:** 

**[871.16s] English:** The strategies that have been working for you so far, what's your intuition there? Yeah, I think it's...  
**Translation:** Vocabulary: intuition: 直觉

**[875.84s] English:** A very problem-dependent kind of question, and I think that, you know, in some ways,  
**Translation:** 

**[881.20s] English:** That question gets at one of the big differences between, um, sort of the classic formulation of a  
**Translation:** 

**[890.24s] English:** Reinforcement learning problem, and some of the sort of more open-ended.  
**Translation:** 

**[895.28s] English:** Reformulations of that problem have been explored in recent years, so classically,  
**Translation:** Vocabulary: reinforcement: 加强

**[898.74s] English:** Reinforcement learning is framed as a problem of maximizing utility, like any kind of rational decision-making.  
**Translation:** 

**[903.52s] English:** AI agent, and then anything you do is in service to maximizing that utility.  
**Translation:** Vocabulary: maximizing: 最大化; utility: 效用

**[907.38s] English:** But, a very interesting kind of way to look at it; I'm not necessarily saying this is the best way to.  
**Translation:** 

**[915.56s] English:** Look at it, but an interesting alternative way to look at these problems as something where.  
**Translation:** 

**[919.78s] English:** You can first explore the world however you please, and then, afterwards, you will be tasked.  
**Translation:** 

**[925.02s] English:** With something and that might suggest a somewhat different solution, so if you don't know,  
**Translation:** 

**[929.48s] English:** What you're going to be tasked with doing, and you just want to prepare yourself optimally for.  
**Translation:** 

**[933.10s] English:** Whatever your uncertain future holds, maybe then you will choose to attain some sort of coverage.  
**Translation:** Vocabulary: attain: 获得; optimally: 最优化地

**[938.48s] English:** Build up, sort of, an arsenal of cognitive tools, if you will, such that later on when someone tells  
**Translation:** 

**[944.34s] English:** You now, your job is to fetch the coffee for me. You'll be well prepared to undertake that task.  
**Translation:** Vocabulary: arsenal: 武器库; cognitive: 认知; undertake: 承担

**[948.92s] English:** And that you see that as the modern formulation of the reinforcement learning problem as a kind of  
**Translation:** 

**[955.02s] English:** The more multitask-oriented the general intelligence formulation,  
**Translation:** 

**[960.00s] English:** I think that's one possible vision of where things might be headed.  
**Translation:** 

**[964.44s] English:** I don't think that's by any means the mainstream or standard way of doing things.  
**Translation:** 

**[968.10s] English:** And it's not like I had to.  
**Translation:** 

**[969.80s] English:** But I like it.  
**Translation:** 

**[970.60s] English:** It's a beautiful vision.  
**Translation:** 

**[971.68s] English:** So, maybe actually take a step back.  
**Translation:** 

**[974.10s] English:** What is the goal of robotics?  
**Translation:** 

**[976.56s] English:** What's the general problem in robotics we're trying to solve?  
**Translation:** Vocabulary: robotics: 机器人学

**[978.90s] English:** You actually kind of painted two pictures here.  
**Translation:** 

**[981.12s] English:** One of the narrow ones, or one of the general ones.  
**Translation:** 

**[983.22s] English:** What, in your view, is the biggest problem with robotics?  
**Translation:** 

**[986.44s] English:** Again, ridiculously philosophical, high-level questions.  
**Translation:** Vocabulary: philosophical: 关于人生观的; ridiculously: 极其

**[990.00s] English:** I think that, you know, maybe there are two ways I can answer this question.  
**Translation:** 

**[994.40s] English:** One is that there's a very pragmatic problem: what would make robots maximally useful?  
**Translation:** Vocabulary: maximally: 最大程度上; pragmatic: 实用的

**[1003.82s] English:** And there, the answer might be something like a system that can perform whatever task a human user sets for it.  
**Translation:** 

**[1017.02s] English:** You know, within the physical constraints, of course.  
**Translation:** Vocabulary: constraints: 物理限制

**[1019.24s] English:** If you tell it to teleport to another planet, it probably can't do that.  
**Translation:** 

**[1022.48s] English:** But if you ask it to do something that's within its physical capability, then potentially with a little bit of additional training or a little bit of additional trial and error, it ought to be able to figure it out—in much the same way as a human teleoperator ought to figure out how to drive the robot to do that.  
**Translation:** Vocabulary: capability: 能力; teleoperator: 远程操作员; teleport: 瞬间移动

**[1036.62s] English:** That's kind of a very pragmatic view of what it would take to solve the robotics problem, if we will.  
**Translation:** 

**[1044.58s] English:** But I think that there is a second answer.  
**Translation:** 

**[1047.02s] English:** And that answer is a lot closer to why.  
**Translation:** 

**[1049.12s] English:** I want to work on robotics, which is not so much about what it would take to do a really good job in the world of robotics, but more the other way around.  
**Translation:** 

**[1058.08s] English:** What robotics can bring to the table to help us understand artificial intelligence.  
**Translation:** 

**[1064.44s] English:** So, your dream fundamentally is to understand intelligence.  
**Translation:** 

**[1069.10s] English:** Yes, I think that's the dream for many people who actually work in this space.  
**Translation:** 

**[1073.16s] English:** I think that there is something very pragmatic and very useful about studying robotics.  
**Translation:** Vocabulary: robotics: 机器人学

**[1078.36s] English:** But I do think that a lot of people who go.  
**Translation:** 

**[1080.00s] English:** Into this field, actually, you know, the things that they draw inspiration from are the potential.  
**Translation:** 

**[1086.04s] English:** For robots to help us learn about intelligence and about ourselves is so fascinating.  
**Translation:** 

**[1092.38s] English:** That robotics is basically the space by which you can get closer to understanding the fundamentals.  
**Translation:** Vocabulary: fundamentals: 基础原理

**[1099.00s] English:** Of artificial intelligence, so, what is it about robotics that's different from some of the other?  
**Translation:** 

**[1104.76s] English:** Approaches so, if we look at some of the early breakthroughs in deep learning or in the computer sciences,  
**Translation:** Vocabulary: approaches: 方法; breakthroughs: 突破

**[1109.72s] English:** Vision, space, and natural language processing: there are really nice, clean benchmarks that a lot  
**Translation:** 

**[1115.20s] English:** Of people who competed on, and thereby came up with a lot of brilliant ideas, what's the fundamental?  
**Translation:** Vocabulary: benchmarks: 参考标准; competed: 竞争

**[1119.08s] English:** Difference to you between computer vision, purely defined by ImageNet, and kind of the bigger picture?  
**Translation:** 

**[1124.74s] English:** Robotics: There are a couple of things, though. One is that with robotics, you kind of have  
**Translation:** 

**[1131.98s] English:** Um, you kind of have to take away many of the crutches, so you have to deal with both the  
**Translation:** 

**[1138.20s] English:** The particular  
**Translation:** Vocabulary: crutches: 辅助工具

**[1139.56s] English:** The particular  
**Translation:** 

**[1139.72s] English:** Problems of perception control, and so on, but you also have to deal with the integration of those.  
**Translation:** Vocabulary: perception: 感知

**[1143.28s] English:** Things, and, you know, classically we've always thought of the integration as kind of a separate process.  
**Translation:** 

**[1148.20s] English:** Problem: So, a classic kind of modular engineering approach is to solve the individual sub-  
**Translation:** Vocabulary: modular: 模块化的

**[1152.52s] English:** Problems, then wire them together, and then the whole thing works. Um, and one of the things that  
**Translation:** 

**[1156.90s] English:** We've been seeing over the last couple of decades, is that maybe studying the thing as a whole...  
**Translation:** 

**[1161.76s] English:** Might lead to very different solutions than if we were to study the parts and wire them.  
**Translation:** 

**[1166.14s] English:** Together, so the integrative nature of robotics research.  
**Translation:** Vocabulary: integrative: 综合性的; robotics: 机器人学

**[1169.72s] English:** Helps us see, you know, different perspectives on the problem. Another part of the answer is that.  
**Translation:** 

**[1176.12s] English:** With robotics, um, it casts a certain uh paradox into very clever relief, so that this is.  
**Translation:** Vocabulary: paradox: 矛盾; perspectives: 观点

**[1182.36s] English:** Sometimes referred to as Moravec's paradox, the idea that in artificial intelligence, things that are easy for humans are hard for machines, and vice versa.  
**Translation:** 

**[1188.76s] English:** Are very hard for people, can be very easy for machines, and vice versa; things that are very easy,...  
**Translation:** Vocabulary: versa: 相反

**[1193.32s] English:** For people, it can be very hard for machines, so you know, uh, integral and differential calculus is a  
**Translation:** 

**[1199.56s] English:** Really, a good example of this, by the way, is one of the things I'm proud to say:  
**Translation:** Vocabulary: calculus: 微积分; differential: 微分; integral: 积分

**[1200.00s] English:** It's pretty difficult to learn for people, but if you program a computer to do it, it can derive derivatives and integrals for you all day long without any trouble.  
**Translation:** 

**[1202.66s] English:** Most up-to-date research and validation of the  
**Translation:** Vocabulary: derivatives: 导数; derive: 推导; integrals: 积分; validation: 验证

**[1208.12s] English:** Whereas, some things, like drinking from a cup of water, are very easy for a person to do, but very hard for a robot to deal with.  
**Translation:** 

**[1216.48s] English:** And sometimes, when we see such blatant discrepancies, they give us a really strong hint that we're missing something important.  
**Translation:** Vocabulary: blatant: 明显的; discrepancies: 差异

**[1222.80s] English:** So, if we really try to zero in on those discrepancies, we might find that little bit that we're missing.  
**Translation:** 

**[1227.78s] English:** And it's not that we need to make machines better or worse at math and better at drinking water, but just that by studying those discrepancies, we might find some new insight.  
**Translation:** 

**[1229.12s] English:** Theory is the fact that if you are a robot, you can actually work incredibly well, but you don't  
**Translation:** 

**[1229.20s] English:** Be able to do as much as that, you can, and you have to be able to do it all at once, and that's  
**Translation:** 

**[1229.26s] English:** Is  
**Translation:** 

**[1237.80s] English:** So, that could be in any space.  
**Translation:** 

**[1240.26s] English:** It doesn't have to be robotics, but you're saying, I mean, it's kind of interesting that robotics seems to have a lot of those discrepancies.  
**Translation:** 

**[1249.24s] English:** So, the Hans-Marva paradox is probably referring to the space of physical interaction.  
**Translation:** 

**[1256.54s] English:** Like you said, objects.  
**Translation:** 

**[1257.78s] English:** Object manipulation, walking, and all the kinds of stuff we do in the physical world.  
**Translation:** Vocabulary: manipulation: 操作

**[1263.70s] English:** How do you make sense of it if you were to try to disentangle the Marva paradox, like why is there such a gap in our intuition about it?  
**Translation:** 

**[1277.30s] English:** Why do you think manipulating objects is so hard, given everything you've learned from applying reinforcement learning in this space?  
**Translation:** Vocabulary: disentangle: 解开; intuition: 直觉; manipulating: 操作; paradox: 悖论; reinforcement: 强化

**[1285.70s] English:** Yeah.  
**Translation:** 

**[1286.08s] English:** I think that one reason.  
**Translation:** 

**[1288.78s] English:** Is maybe that for many of the other problems we've studied in AI and computer science and so on, the notion of input, output, and supervision is much, much cleaner.  
**Translation:** 

**[1302.38s] English:** So, computer vision, for example, deals with very complex inputs, but it's comparatively a bit easier—at least up to some level of abstraction—to cast it as a very tightly supervised problem.  
**Translation:** Vocabulary: abstraction: 抽象; comparatively: 相对而言; inputs: 输入; supervised: 监督式; supervision: 监督

**[1314.46s] English:** It's comparatively much, much harder to cast robotic mechanics.  
**Translation:** 

**[1317.78s] English:** So, I think manipulation has a very tightly supervised problem.  
**Translation:** Vocabulary: robotic: 机器人

**[1319.98s] English:** So, I think manipulation has a very tightly supervised problem.  
**Translation:** 

**[1320.40s] English:** You can do it.  
**Translation:** 

**[1321.30s] English:** It just doesn't seem to work all that well.  
**Translation:** 

**[1323.30s] English:** So, you could say that maybe we get a labeled data set where we know exactly which  
**Translation:** Vocabulary: labeled: 标记好的

**[1327.04s] English:** Motor commands to send, and then we train on that.  
**Translation:** 

**[1329.12s] English:** But, for various reasons, that's not actually such a great solution.  
**Translation:** 

**[1333.44s] English:** And it also doesn't seem to be even remotely similar to how people and animals learn to.  
**Translation:** 

**[1337.50s] English:** Do things, because we're not told by our parents: here's how you fire your muscles.  
**Translation:** Vocabulary: remotely: 遥远地

**[1342.58s] English:** In order to walk.  
**Translation:** 

**[1344.38s] English:** We do get some guidance, but the really low-level, detailed stuff, we figure out mostly on our own.  
**Translation:** 

**[1349.32s] English:** Own.  
**Translation:** 

**[1349.54s] English:** And that's what you mean by tightly coupled: that every single little sub-action gets a  
**Translation:** 

**[1354.46s] English:** Supervised signal of whether it's a good one or not.  
**Translation:** 

**[1357.12s] English:** Right.  
**Translation:** 

**[1357.52s] English:** So, in computer vision, you could sort of imagine up to a level of abstraction that...  
**Translation:** 

**[1361.38s] English:** Maybe somebody told you this is a car, and this is a cat, and this is a dog—in motor.  
**Translation:** 

**[1365.66s] English:** Control: It's very clear that that was not the case.  
**Translation:** 

**[1369.06s] English:** If we look at some of the sub-spaces of robotics, that, again, as you said, integrate  
**Translation:** Vocabulary: integrate: 融合; robotics: 机器人学

**[1377.14s] English:** All of them together.  
**Translation:** 

**[1377.90s] English:** And then we get to see how this beautiful mess interplays.  
**Translation:** 

**[1380.94s] English:** So, there's nevertheless still a perception.  
**Translation:** 

**[1383.86s] English:** So it's a computer vision problem, broadly speaking, understanding the environment.  
**Translation:** Vocabulary: broadly: 大致; perception: 看法

**[1389.72s] English:** Then there's also a kind of categorization of the space, maybe you can correct me on this.  
**Translation:** 

**[1394.16s] English:** Then there's prediction, in trying to anticipate what things are going to do into the future.  
**Translation:** Vocabulary: anticipate: 预知; categorization: 分类

**[1400.44s] English:** In order for you to be able to act in that world.  
**Translation:** 

**[1404.42s] English:** And then there's also this game-theoretic aspect.  
**Translation:** 

**[1407.90s] English:** The game-theoretic aspect of how your actions will change the behavior of others.  
**Translation:** 

**[1413.92s] English:** In this kind of space, and this is bigger than reinforcement learning.  
**Translation:** Vocabulary: reinforcement: 强化学习

**[1418.16s] English:** This is just a broad look at the problem in robotics.  
**Translation:** 

**[1420.82s] English:** What's the hardest problem here?  
**Translation:** 

**[1422.90s] English:** Or is what you said true—that when you start to look at all of them together, that's a  
**Translation:** 

**[1432.42s] English:** Whole other thing?  
**Translation:** 

**[1434.18s] English:** You can't even say which one is harder individually.  
**Translation:** 

**[1437.54s] English:** Right.  
**Translation:** Vocabulary: individually: 单独地

**[1437.66s] English:** Right.  
**Translation:** 

**[1437.70s] English:** Right.  
**Translation:** 

**[1437.72s] English:** Right.  
**Translation:** 

**[1437.74s] English:** Right.  
**Translation:** 

**[1437.76s] English:** Right.  
**Translation:** 

**[1437.78s] English:** Right.  
**Translation:** 

**[1437.80s] English:** Right.  
**Translation:** 

**[1437.86s] English:** Right.  
**Translation:** 

**[1437.88s] English:** Right.  
**Translation:** 

**[1437.90s] English:** Right.  
**Translation:** 

**[1437.94s] English:** Right.  
**Translation:** 

**[1437.96s] English:** Right.  
**Translation:** 

**[1437.98s] English:** Right.  
**Translation:** 

**[1438.00s] English:** Right.  
**Translation:** 

**[1438.02s] English:** Right.  
**Translation:** 

**[1438.04s] English:** Right.  
**Translation:** 

**[1438.06s] English:** Right.  
**Translation:** 

**[1438.10s] English:** Right.  
**Translation:** 

**[1438.12s] English:** Right.  
**Translation:** 

**[1438.16s] English:** Right.  
**Translation:** 

**[1438.18s] English:** Right.  
**Translation:** 

**[1438.20s] English:** Right.  
**Translation:** 

**[1438.22s] English:** Right.  
**Translation:** 

**[1438.24s] English:** Right.  
**Translation:** 

**[1438.26s] English:** Right.  
**Translation:** 

**[1438.28s] English:** Right.  
**Translation:** 

**[1438.30s] English:** Right.  
**Translation:** 

**[1438.32s] English:** Right.  
**Translation:** 

**[1440.00s] English:** Do they all together? I think when you look at them all together, some things actually become easier.  
**Translation:** 

**[1444.88s] English:** And I think that's actually pretty important. So, in 2014, we had  
**Translation:** 

**[1451.50s] English:** Some work; basically, our first work on end-to-end reinforcement learning for robotic manipulation.  
**Translation:** 

**[1457.32s] English:** Skills from vision, which, you know, at the time, seemed a little inflammatory.  
**Translation:** 

**[1462.74s] English:** And it's controversial in the robotics world. But other than the inflammatory and controversial part of it,  
**Translation:** 

**[1469.14s] English:** The point that we were actually trying to make in that work is that, for the particular case of  
**Translation:** 

**[1474.08s] English:** Combining perception and control, you could actually do better if you treat them together.  
**Translation:** 

**[1478.02s] English:** Than if you try to separate them. And the way that we tried to demonstrate this is, we picked,  
**Translation:** Vocabulary: perception: 感知

**[1481.96s] English:** You know, a fairly simple motor control task where a robot had to insert a little red trapezoid into  
**Translation:** 

**[1487.60s] English:** A trapezoidal hole. And we had our separate solution, which involved first detecting the  
**Translation:** Vocabulary: detecting: 检测; insert: 插入; trapezoid: 梯形; trapezoidal: 梯形的

**[1493.54s] English:** Hole using a pose detector, and then actuating the arm to put it in. And then, our end-to-end  
**Translation:** 

**[1498.28s] English:** Solution, which just...  
**Translation:** Vocabulary: actuating: 使动作; detector: 检测器

**[1499.14s] English:** And one of the things we observed is that if you use the end-to-end solution,  
**Translation:** 

**[1505.62s] English:** Essentially, the pressure on the perception part of the model is actually lower. Like,  
**Translation:** 

**[1508.44s] English:** It doesn't have to figure out exactly where the thing is in 3D space. It just needs to figure out  
**Translation:** 

**[1512.28s] English:** Where it is, you know, distributing the errors in such a way that the horizontal difference matters.  
**Translation:** Vocabulary: distributing: 分配; horizontal: 水平

**[1517.48s] English:** More than the vertical difference, because vertically, it just pushes it down all the way.  
**Translation:** 

**[1520.46s] English:** Until it can't go any further. And there, perceptual errors are a lot less harmful.  
**Translation:** Vocabulary: perceptual: 感知的; vertical: 垂直的; vertically: 垂直地

**[1524.44s] English:** Whereas, perpendicular to the direction of motion, perceptual errors are much more harmful.  
**Translation:** 

**[1528.34s] English:** So, the point is that if you combine these two things, you can trade off errors between the  
**Translation:** Vocabulary: perpendicular: 垂直

**[1533.70s] English:** Components should optimally work together to best accomplish the task, and the individual components can actually be weaker.  
**Translation:** 

**[1539.32s] English:** While still leading to better overall performance.  
**Translation:** Vocabulary: optimally: 最佳地

**[1541.94s] English:** That's a profound idea. I mean, in the context of pegs and similar items, it's quite simple.  
**Translation:** 

**[1548.40s] English:** It's almost tempting to overlook, but that seems to be, at least intuitively, an idea that should...  
**Translation:** Vocabulary: intuitively: 直觉上; overlook: 忽视; profound: 深奥; tempting: 诱人

**[1555.98s] English:** Generalize to basically all aspects.  
**Translation:** 

**[1558.34s] English:** So, perception and control.  
**Translation:** Vocabulary: generalize: 泛化; perception: 感知

**[1560.00s] English:** Of course.  
**Translation:** 

**[1560.56s] English:** That one strengthens the other.  
**Translation:** Vocabulary: strengthens: 增强

**[1561.98s] English:** Yeah, and people who have studied perceptual heuristics in humans and animals find things like that all the time.  
**Translation:** 

**[1568.78s] English:** So, one very well-known example is something called the gaze heuristic, which is a little trick that you can use to intercept a flying object.  
**Translation:** Vocabulary: heuristic: 启发法; heuristics: 启发法; intercept: 拦截

**[1577.22s] English:** So, if you want to catch a ball, for instance, you could try to localize it in 3D space, estimate its velocity, estimate the effect of wind resistance, and solve a complex system of differential equations in your head.  
**Translation:** 

**[1586.26s] English:** Or you can maintain a running speed so that the object stays in the same position within your field of view.  
**Translation:** Vocabulary: differential: 微分的; equations: 方程; estimate: 估算

**[1593.90s] English:** So, if it dips a little bit, you speed up.  
**Translation:** 

**[1595.52s] English:** If it rises a little bit, you slow down.  
**Translation:** 

**[1598.08s] English:** And if you follow the simple rule, you'll actually arrive at exactly the place where the object lands, and you'll catch it.  
**Translation:** 

**[1602.80s] English:** And humans use it when they play baseball.  
**Translation:** 

**[1605.10s] English:** Human pilots use it when they fly airplanes to figure out if they're about to collide with someone.  
**Translation:** 

**[1609.18s] English:** Frogs use this to catch insects, and so on.  
**Translation:** Vocabulary: collide: 相撞

**[1611.50s] English:** So, this is something that actually happens in nature.  
**Translation:** 

**[1613.56s] English:** And I'm sure this is just one instance of something we were able to.  
**Translation:** 

**[1616.26s] English:** Identify just because all the scientists were able to identify because it's so prevalent, but there are probably many others.  
**Translation:** 

**[1621.78s] English:** Do you have a canonical problem, just so we can zoom in as we talk about robotics? Do you have a simple, clean, and beautiful representative problem in robotics that you think about when you're thinking about some of these problems?  
**Translation:** Vocabulary: canonical: 典范问题; prevalent: 普遍存在的; robotics: 机器人学

**[1635.84s] English:** We talked about robotic manipulation.  
**Translation:** 

**[1638.36s] English:** To me, that seems intuitively correct, at least the robotics community has converged on that as a space.  
**Translation:** 

**[1646.26s] English:** That's the canonical problem. If you agree, then maybe zoom in on some particular aspect of that problem that you just like. Like, if we solve that problem perfectly, it'll unlock a major step toward human-level intelligence.  
**Translation:** 

**[1664.08s] English:** I don't think I have a really great answer to that.  
**Translation:** Vocabulary: unlock: 解锁

**[1666.14s] English:** And I think partly the reason I don't have a great answer kind of has to do with the fact that the difficulty is really in the flexibility.  
**Translation:** 

**[1675.84s] English:** And adaptability, rather than doing a particular thing, really is key.  
**Translation:** Vocabulary: adaptability: 适应性; flexibility: 灵活性

**[1680.00s] English:** Well, so, um, it's hard to just say, "Oh, if you can, I don't know, like shuffle a deck of cards," and expect someone to do it easily.  
**Translation:** 

**[1687.32s] English:** Fast as, like a Vegas casino dealer, then you'll be very proficient; it's really the ability.  
**Translation:** Vocabulary: casino: 赌场; proficient: 熟练; shuffle: 洗牌; vegas: 赌城

**[1694.66s] English:** To quickly figure out how to do some arbitrary new thing well enough to, you know, move on.  
**Translation:** 

**[1703.98s] English:** On to the next arbitrary thing, but the source of newness and uncertainty, have you found any?  
**Translation:** Vocabulary: arbitrary: 随意的

**[1711.68s] English:** Problems in which it's easy to generate new kinds of newness, this is, yeah.  
**Translation:** 

**[1719.78s] English:** Yeah, so a few years ago, uh, if you had asked me this question around 2016 maybe I would...  
**Translation:** 

**[1726.94s] English:** Have you probably said that robotic grasping is a really great example of that, because it's a  
**Translation:** 

**[1731.98s] English:** Task with great real-world utility.  
**Translation:** Vocabulary: grasping: 抓取; robotic: 机器人; utility: 实用性

**[1733.66s] English:** Like, you'll get a lot of money if you can do it well. What is robotic grasping? Picking up anything.  
**Translation:** 

**[1739.66s] English:** Object with a robotic hand, exactly. So, you will get a lot of money if you do it well, because  
**Translation:** 

**[1744.78s] English:** Lots of people want to run warehouses with robots, and it's highly non-trivial because  
**Translation:** 

**[1749.16s] English:** Uh, very different objects will require very different grasping strategies, but actually, since  
**Translation:** Vocabulary: warehouses: 仓库

**[1755.82s] English:** Then, people have gotten really good at building systems to solve this problem, uh, to the point  
**Translation:** 

**[1761.52s] English:** Where I'm not actually sure how much more progress.  
**Translation:** 

**[1763.64s] English:** We can make that our main guiding thing, but it's kind of interesting to see.  
**Translation:** 

**[1770.70s] English:** The kinds of methods that have actually worked well in that space because  
**Translation:** 

**[1773.86s] English:** Robotic grasping has classically been regarded very much as, um, kind of almost like a geometry.  
**Translation:** 

**[1780.24s] English:** Problem, so, uh, people who have studied the history of computer vision will find this.  
**Translation:** Vocabulary: geometry: 几何; regarded: 视为

**[1785.56s] English:** Very familiar, that it's kind of in the same way that, in the early days of computer vision, people  
**Translation:** 

**[1789.74s] English:** Thought of it very much as an inverse graphics thing in robotic grasping, people.  
**Translation:** Vocabulary: inverse: 反向的

**[1793.64s] English:** Thought of it as an inverse physics problem, essentially you  
**Translation:** 

**[1796.76s] English:** You look at what's in front of you, figure out the shapes, then  
**Translation:** 

**[1800.00s] English:** And use your best estimate of the laws of physics to figure out where to put your fingers, and you  
**Translation:** 

**[1803.92s] English:** Pick up the thing. And it turns out that what works really well for robotic grasping, instantiated in  
**Translation:** Vocabulary: estimate: 估算; instantiated: 实现

**[1809.26s] English:** Many different recent works, including ours and others from many other labs, is to use  
**Translation:** 

**[1815.26s] English:** Learning methods with some combination of either exhaustive simulation or actual real-world examples.  
**Translation:** Vocabulary: exhaustive: 详尽的

**[1821.00s] English:** Trial and error. And it turns out that those things actually work really well. And then you...  
**Translation:** 

**[1824.08s] English:** Don't have to worry about solving geometry problems or physics problems. So, what are,  
**Translation:** 

**[1830.24s] English:** Just by the way, in the grasping, what are the difficulties that have been worked on? So, one is  
**Translation:** 

**[1836.06s] English:** Like the materials of things, maybe occlusions and the perception side. Why is it so difficult?  
**Translation:** Vocabulary: grasping: 理解; occlusions: 遮挡; perception: 感知

**[1842.26s] English:** Why is picking stuff up such a difficult problem? Yeah, it's a difficult problem because the number  
**Translation:** 

**[1849.40s] English:** Of the things that you might have to deal with, or the variety of things you have to deal with, is  
**Translation:** 

**[1853.14s] English:** Extremely large.  
**Translation:** 

**[1854.60s] English:** And often, things that work for one class of objects won't work for other classes of objects.  
**Translation:** 

**[1860.22s] English:** So, if you get really good at picking up boxes, and now you have to pick up plastic bags,  
**Translation:** 

**[1866.16s] English:** You know, you just need to employ a very different strategy. And there are many properties of objects.  
**Translation:** Vocabulary: employ: 采用

**[1873.04s] English:** That are more than just their geometry. It has to do with, you know, the bits that are easier.  
**Translation:** 

**[1878.30s] English:** To pick up the bits that are hard to pick up, the bits that are more flexible, the bits that will,...  
**Translation:** Vocabulary: flexible: 柔软的; geometry: 几何

**[1881.54s] English:** Cause the thing to pivot, bend, and drop.  
**Translation:** 

**[1884.08s] English:** So, there are all these little details that come up, but the task is still kind of characterization.  
**Translation:** 

**[1898.74s] English:** As one task, it's like there's a very clear notion of you did it or you didn't do it.  
**Translation:** 

**[1903.80s] English:** So, in terms of spilling things, there creeps in this notion that starts to sound and feel like  
**Translation:** Vocabulary: creeps: 悄悄出现

**[1911.14s] English:** Common sense reasoning. Do you think,  
**Translation:** 

**[1914.08s] English:** Solving the general problem of robotics requires  
**Translation:** Vocabulary: robotics: 机器人学

**[1920.00s] English:** Common sense reasoning requires general intelligence, this kind of human-level capability of.  
**Translation:** 

**[1927.26s] English:** You know, like you said, be robust and deal with uncertainty, but also be able to sort of reason.  
**Translation:** Vocabulary: capability: 能力; robust: 健壮的

**[1933.16s] English:** And assimilate different pieces of knowledge that you have, um, yeah. What are you doing?  
**Translation:** 

**[1940.56s] English:** Thoughts on the needs of common sense reasoning in the space of the general robotics problem.  
**Translation:** Vocabulary: assimilate: 吸收

**[1947.68s] English:** So, I'm going to slightly dodge that question and say that I think — maybe actually.  
**Translation:** 

**[1951.94s] English:** It's the other way around: studying robotics can help us understand how to build complex systems.  
**Translation:** Vocabulary: dodge: 回避

**[1957.56s] English:** Common sense into our AI systems: One way to think about common sense is that and why our current  
**Translation:** 

**[1964.14s] English:** Systems might lack common sense because common sense is an emergent property.  
**Translation:** Vocabulary: emergent: 涌现的

**[1968.88s] English:** Actually, having to interact with a particular world or universe and get things done.  
**Translation:** 

**[1974.94s] English:** In that universe, you might think that for instance, if you're a robot, you're going to have  
**Translation:** 

**[1977.68s] English:** An image captioning system, uh, maybe it looks at pictures of the world and types out  
**Translation:** 

**[1984.66s] English:** English sentences, so it kind of deals with our world, and then you can easily construct.  
**Translation:** Vocabulary: captioning: 图片字幕

**[1990.42s] English:** Situations where image captioning systems do things that defy common sense, like give it a  
**Translation:** 

**[1994.64s] English:** Picture of a person wearing a fur coat, and we'll say it's a teddy bear, but I think what's really  
**Translation:** Vocabulary: teddy: 泰迪熊

**[1999.24s] English:** Happening in those settings is that the system doesn't actually live in our world; it lives in  
**Translation:** 

**[2004.50s] English:** Its own world that consists of pixels and English sentences.  
**Translation:** Vocabulary: pixels: 像素

**[2006.82s] English:** And it doesn't actually consist of, you know, having to put on a fur coat in the winter, so you  
**Translation:** 

**[2011.60s] English:** Don't get cold, so perhaps the reason for the disconnect is that the systems we have now.  
**Translation:** Vocabulary: disconnect: 联系中断

**[2018.66s] English:** Simply, they inhabit a different universe, and if we build AI systems that are forced to deal with  
**Translation:** 

**[2023.42s] English:** All of the messiness and complexity of our universe — maybe they will have to acquire common...  
**Translation:** Vocabulary: complexity: 复杂性; inhabit: 居住; messiness: 混乱

**[2028.08s] English:** Sense to essentially maximize their utility, whereas the systems we're building now don't.  
**Translation:** 

**[2033.02s] English:** They have to do that, so they can take some shortcuts.  
**Translation:** Vocabulary: maximize: 最大程度利用; shortcuts: 捷径; utility: 实用性

**[2034.38s] English:** That's fascinating.  
**Translation:** 

**[2036.82s] English:** You've sort of reframed it a couple of times already.  
**Translation:** Vocabulary: reframed: 重新表述

**[2040.00s] English:** The role of robotics in this whole thing, and for some reason, I don't know if my way of thinking is  
**Translation:** 

**[2045.76s] English:** Common, but I thought we needed to understand and solve intelligence in order to solve robotics.  
**Translation:** Vocabulary: robotics: 机器人技术

**[2051.74s] English:** And you're kind of framing it as: no robotics is one of the best ways to just study artificial.  
**Translation:** 

**[2057.96s] English:** Intelligence and build, sort of like robotics, is like the right space in which you get to explore.  
**Translation:** Vocabulary: framing: 设定框架

**[2065.54s] English:** Some of the fundamental learning mechanisms, fundamentally sort of multi-modal and multi-task.  
**Translation:** 

**[2072.16s] English:** Aggregation of knowledge mechanisms that are required for general intelligence that's really  
**Translation:** Vocabulary: aggregation: 知识整合; fundamentally: 本质上

**[2077.06s] English:** An interesting way to think about it, but let me ask about learning: can the general sort of robotics  
**Translation:** 

**[2083.10s] English:** The epitome of the robotics problem might be solved purely through learning, perhaps end-to-end learning.  
**Translation:** Vocabulary: epitome: 典范

**[2091.38s] English:** Sort of learning from scratch, as opposed to injecting.  
**Translation:** 

**[2095.54s] English:** Human expertise, rules, and heuristics, and so on, I think that in terms of the spirit of the  
**Translation:** Vocabulary: heuristics: 启发式; injecting: 注入; scratch: 从头开始

**[2101.96s] English:** Question: I would say yes, uh, I mean, I think that, though, in some ways, it's maybe like  
**Translation:** 

**[2108.22s] English:** An overly sharp dichotomy, like you know, I think that in some ways, when we build algorithms,  
**Translation:** Vocabulary: dichotomy: 二元对立; overly: 过于

**[2114.60s] English:** You know, at some point a person does something like "Yeah, there's always that one person.  
**Translation:** 

**[2120.60s] English:** Computer, a person, uh, you know, implemented TensorFlow.  
**Translation:** Vocabulary: implemented: 实现

**[2124.68s] English:** Uh  
**Translation:** 

**[2125.54s] English:** But, yeah, I think that, in terms of the point you're making, I do think the answer is...  
**Translation:** 

**[2129.84s] English:** Is yes, I think that we can solve many problems that have previously required meticulous effort.  
**Translation:** 

**[2136.20s] English:** Manual engineering through automated optimization techniques, and actually, one thing I will say is that...  
**Translation:** Vocabulary: automated: 自动化; meticulous: 细致的; optimization: 优化

**[2141.18s] English:** This topic is: I don't think this is actually a very radical or very new idea; I think people  
**Translation:** 

**[2145.78s] English:** Have I been thinking about automated optimization techniques as a way to do control?  
**Translation:** 

**[2151.02s] English:** For a very, very long time, and in some ways, I think that's a very radical or new idea.  
**Translation:** 

**[2155.54s] English:** And, in some ways, I think that's a very radical or new idea because what's changed is really more the name.  
**Translation:** 

**[2157.84s] English:** Because what's changed is really more the name, so you know, today we would say that, oh,...  
**Translation:** 

**[2159.84s] English:** So, you know, today we would say, "Oh,  
**Translation:** 

**[2160.00s] English:** My robot does machine learning, it does reinforcement learning; maybe in the 1960s.  
**Translation:** 

**[2164.72s] English:** You'd say, "Oh, my robot is doing optimal control." And maybe the difference between typing out a  
**Translation:** Vocabulary: optimal: 最佳; reinforcement: 强化学习

**[2170.56s] English:** System of differential equations and doing feedback linearization versus training in  
**Translation:** 

**[2175.08s] English:** Neural net: Maybe it's not such a large difference. It's just pushing the optimization.  
**Translation:** Vocabulary: differential: 微分的; equations: 方程; neural: 神经的

**[2179.34s] English:** Deeper and deeper into the thing. Well, it's interesting you think that way.  
**Translation:** 

**[2183.90s] English:** But, especially with deep learning, the accumulation of experiences in data form.  
**Translation:** Vocabulary: accumulation: 累积

**[2191.34s] English:** To form deep representations starts to feel like knowledge, as opposed to optimal control.  
**Translation:** 

**[2199.40s] English:** So, this feels like there's an accumulation of knowledge through the learning process.  
**Translation:** Vocabulary: representations: 表征

**[2203.06s] English:** Yes. Yeah. So I think that is a good point. That one big difference between learning-based systems,...  
**Translation:** 

**[2207.94s] English:** And classical optimal control systems are based on predefined models, whereas in principle, learning-based systems should be able to adapt and optimize through experience.  
**Translation:** Vocabulary: optimize: 优化; predefined: 预定义

**[2212.36s] English:** Get better and better the more they do.  
**Translation:** 

**[2213.90s] English:** Right. And I do think that that's actually a very, very powerful difference.  
**Translation:** 

**[2218.12s] English:** So, if we look back at the world of expert systems and symbolic AI, and so on, of using logic to  
**Translation:** 

**[2225.36s] English:** Accumulate expertise, human expertise, human-encoded expertise: do you think that will?  
**Translation:** Vocabulary: accumulate: 累积; symbolic: 符号化的

**[2231.90s] English:** Have you had a role at some point in deep learning, machine learning, or reinforcement learning?  
**Translation:** 

**[2238.20s] English:** Incredible results and breakthroughs, and just inspired thousands.  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[2243.90s] English:** Maybe millions of researchers. But there's this less popular option now, but it used to be popular.  
**Translation:** 

**[2251.66s] English:** The idea of symbolic AI: do you think it will have a role?  
**Translation:** 

**[2255.28s] English:** I think, in some ways, the descendants of symbolic AI actually already have a role. So  
**Translation:** 

**[2264.84s] English:** This is the highly biased history from my perspective. You say that, well,  
**Translation:** Vocabulary: descendants: 后代

**[2269.96s] English:** Initially, we thought that rational decision-making involves logical  
**Translation:** 

**[2273.88s] English:** Manipulation. So, you have some model of the world expressed in terms of logic. You have  
**Translation:** Vocabulary: manipulation: 操控

**[2280.00s] English:** Have a query, like "What action do I take in order for X to be true?" and then you manipulate.  
**Translation:** 

**[2285.42s] English:** Your logical symbolic representation to get an answer. What that turned into somewhere in the  
**Translation:** Vocabulary: manipulate: 操作

**[2289.82s] English:** The 1990s is, well, instead of building predicates and statements that have true or false,  
**Translation:** 

**[2295.76s] English:** Values, we'll build probabilistic systems where things have probabilities associated, and  
**Translation:** Vocabulary: predicates: 谓词; probabilistic: 概率的; probabilities: 概率

**[2301.94s] English:** Probabilities of being true and false, and that turned into Bayes nets. And that provided a sort of  
**Translation:** 

**[2306.18s] English:** A boost to what were really still essentially logical inference systems, just probabilistic.  
**Translation:** Vocabulary: inference: 推理

**[2311.16s] English:** Logical inference systems. And then people said, "Well, let's actually learn the individual.  
**Translation:** 

**[2317.02s] English:** Probabilities inside these models. And then people said, "Well, let's not even specify the nodes in.  
**Translation:** Vocabulary: specify: 指定

**[2322.38s] English:** The models: let's just put a big neural net in there. But in many ways, I see these as actually.  
**Translation:** 

**[2326.86s] English:** Kind of descendants from the same idea, it's essentially instantiating rational decisions.  
**Translation:** Vocabulary: instantiating: 实例化; neural: 神经

**[2330.70s] English:** Making by means of some inference process, and learning by means of an optimization process.  
**Translation:** 

**[2336.94s] English:** So, in a sense, I would say, yes, it has a place. And in many ways, that place is, you know,  
**Translation:** Vocabulary: optimization: 优化过程

**[2342.82s] English:** It already holds that place. It's already in there. Yeah, it's just by a different perspective, it looks  
**Translation:** 

**[2347.36s] English:** Slightly different than it was before. Yeah, but there are some things that we can think about.  
**Translation:** 

**[2351.60s] English:** That makes this a little bit more obvious. For example, if I train a big neural net model to predict what  
**Translation:** 

**[2356.70s] English:** What will happen in response to my robot's actions, and then I run probabilistic inference, meaning I  
**Translation:** 

**[2361.78s] English:** Invert that model to figure out the actions that lead to some plausible outcome. Like, to me, that  
**Translation:** 

**[2366.18s] English:** Is a kind of logic. You have a model of the world that just happens to be expressed by a neural net.  
**Translation:** Vocabulary: invert: 反向思考; plausible: 合乎情理的

**[2371.10s] English:** And you are doing some inference procedure or manipulation on that model to figure out  
**Translation:** 

**[2377.88s] English:** The answer to a query that you have is its interpretability, it's the  
**Translation:** Vocabulary: interpretability: 可解释性; manipulation: 操作

**[2381.66s] English:** Explainability, though, seems to be lacking more so because the nice thing about sort of expert  
**Translation:** 

**[2387.24s] English:** Systems are ones you can follow the reasoning of, and that to us, mere humans, is somehow compelling.  
**Translation:** Vocabulary: compelling: 有说服力的; explainability: 可解释性

**[2393.96s] English:** It would; it's just, I don't know what to make of this.  
**Translation:** 

**[2400.00s] English:** The fact that there is a human desire for intelligent systems to be able to  
**Translation:** 

**[2406.16s] English:** Convey, in a poetic way, to us why it made the decisions it did—like tell a convincing story.  
**Translation:** 

**[2415.04s] English:** And perhaps that's like a silly human thing, like we shouldn't expect that of intelligence.  
**Translation:** Vocabulary: poetic: 诗意的

**[2422.32s] English:** Systems like we should be super happy that there are intelligent systems out there, but uh,...  
**Translation:** 

**[2428.08s] English:** If I were to sort of psychoanalyze the researchers at the time, I would say they were experts.  
**Translation:** 

**[2433.20s] English:** Systems connected to that part that desires an AI researcher's focus on systems being explainable.  
**Translation:** 

**[2440.00s] English:** I mean, maybe on that topic, do you have any hopes that sort of inference-based learning is possible?  
**Translation:** Vocabulary: desires: 希望

**[2448.00s] English:** Systems will be as explainable as the dream was, with expert systems, for example.  
**Translation:** 

**[2454.88s] English:** I think it's a very complicated question because I think that  
**Translation:** 

**[2458.08s] English:** Some ways the question of explainability is, um, kind of very closely tied to the question of  
**Translation:** 

**[2465.04s] English:** Of, like, performance: you know, why do you want your system to explain itself so well?  
**Translation:** 

**[2470.00s] English:** That when it screws up, you can kind of figure out why it did it right, but in some ways, that  
**Translation:** 

**[2475.60s] English:** That's a much bigger problem, actually. Like, your system might screw up, and then it might keep screwing up.  
**Translation:** Vocabulary: screwing: 损坏; screws: 螺丝

**[2480.56s] English:** In how it explains itself, uh, or you might have some bug somewhere so that it's not actually doing...  
**Translation:** 

**[2488.08s] English:** It's right, and so I think that's a really good way to view that problem—is really as a problem.  
**Translation:** 

**[2491.84s] English:** As a bigger problem of verification and validation, um, of which explainability is sort of one component.  
**Translation:** 

**[2499.20s] English:** I see; I just see it differently. I see explainability—you put it beautifully.  
**Translation:** Vocabulary: explainability: 可解释性; validation: 验证; verification: 核实

**[2503.92s] English:** I think you actually summarize the field of explainability, but to me, there's another aspect.  
**Translation:** 

**[2508.72s] English:** Of explainability, which is like storytelling, that has nothing to do with errors or with like the  
**Translation:** Vocabulary: storytelling: 叙述艺术; summarize: 概括

**[2518.08s] English:** It doesn't use errors.  
**Translation:** 

**[2520.00s] English:** As elements of its story, as opposed to a fundamental need for explainability when errors occur.  
**Translation:** 

**[2527.06s] English:** It occurs, but it's just that for other intelligent systems to be in our world, we seem to want to  
**Translation:** 

**[2532.40s] English:** Tell each other stories, and that's true in the political world; that's true in the academic world.  
**Translation:** 

**[2539.02s] English:** And that, you know, neural networks are less capable of doing that, or perhaps they're equally  
**Translation:** 

**[2544.82s] English:** Capable of storytelling, storytelling—maybe it doesn't matter what the fundamentals of the system are.  
**Translation:** Vocabulary: fundamentals: 基本原理; neural: 神经的

**[2549.76s] English:** Are you just need to be a good storyteller? Maybe, one specific story I can tell you about.  
**Translation:** 

**[2555.08s] English:** In that space is actually about some work that was done by my former collaborator, who's now  
**Translation:** Vocabulary: collaborator: 合作者; storyteller: 讲故事的人

**[2560.80s] English:** Professor at MIT named Jacob Andreas, Jacob actually works in natural language processing, but he had  
**Translation:** 

**[2566.10s] English:** This idea to do a little bit of work in reinforcement learning and how natural language can  
**Translation:** Vocabulary: andreas: 雅各布; reinforcement: 强化学习

**[2571.44s] English:** Basically, structure the internals of policies trained with RL, and one of the things he did is  
**Translation:** 

**[2577.52s] English:** He set up a model that  
**Translation:** Vocabulary: internals: 内部机制

**[2579.76s] English:** Attempts to perform some task that's defined by a reward function, but the model reads in a natural  
**Translation:** 

**[2585.52s] English:** Language instruction, so this is a pretty common thing to do in instruction-following tasks. So, you tell  
**Translation:** 

**[2589.46s] English:** It's like, you know, go to the red house, and then it's supposed to go to the red house, but then one of the  
**Translation:** 

**[2594.12s] English:** Things that Jacob did is that he treated that sentence not as a command from a person, but as a representation.  
**Translation:** 

**[2600.38s] English:** Of the internal, state-of-mind of this policy, essentially, so that when  
**Translation:** 

**[2606.94s] English:** It was faced with a new task. What it would do is that it would be able to do a little bit of a  
**Translation:** 

**[2609.76s] English:** Task, and then it would basically try to think of possible language descriptions, attempting to do them.  
**Translation:** 

**[2614.16s] English:** And see if they led to the right outcome, so it would kind of think out loud, like, "You know, I'm  
**Translation:** 

**[2617.60s] English:** Faced with this new task, what am I going to do? Let me go to the red house. Oh, that didn't work. Let me  
**Translation:** 

**[2621.44s] English:** Go to the blue room, or something. Let me go to the green plant, and once it gets some reward, it  
**Translation:** 

**[2626.40s] English:** Would say, "Oh, go to the green plant—that's what's working. I'm going to go to the green plant.  
**Translation:** 

**[2629.44s] English:** Then, you could look at the string that it came up with, and that was a description of how it thought.  
**Translation:** 

**[2632.56s] English:** It should solve the problem, so you could basically incorporate language as an internal solution.  
**Translation:** 

**[2637.92s] English:** State, and you can start getting a handle on these kinds of things. So that's what Jacob did.  
**Translation:** Vocabulary: incorporate: 合并

**[2639.76s] English:** You can start getting a handle on these kinds of things, so that's what Jacob did so.  
**Translation:** 

**[2640.00s] English:** Things, and then what I was kind of trying to get to is that also if you add to the reward function,...  
**Translation:** 

**[2645.86s] English:** The convincingness of that story, so I have another reward signal of, like  
**Translation:** 

**[2652.10s] English:** People who review that story, how much they like it, so that you know; initially, that could be a  
**Translation:** Vocabulary: convincingness: 说服力

**[2660.48s] English:** Hyper parameters are sort of hard-coded, heuristic-type things, but it's an interesting notion of...  
**Translation:** 

**[2666.20s] English:** The convincingness of the story becomes part of the reward function in the objective function of the  
**Translation:** Vocabulary: hyper: 过度的

**[2672.80s] English:** Explainability: It's in the world of, uh, sort of Twitter and fake news, which might be a scary notion.  
**Translation:** 

**[2678.84s] English:** That, uh, the nature of truth may not be as important as the convincingness of how.  
**Translation:** Vocabulary: explainability: 可解释性

**[2685.18s] English:** Convincing you are, in telling the story around the facts? Let me ask: the basic question.  
**Translation:** 

**[2694.46s] English:** You're one of the world's  
**Translation:** 

**[2696.18s] English:** Class, researchers in reinforcement learning and deep reinforcement learning.  
**Translation:** 

**[2699.04s] English:** Certainly, in the robotic space, what is reinforcement learning? I think that  
**Translation:** Vocabulary: reinforcement: 强化; robotic: 机器人

**[2704.88s] English:** What reinforcement learning refers to today is really just the kind of modern  
**Translation:** 

**[2709.96s] English:** Incarnation of learning-based control: so, classically, reinforcement learning has a much  
**Translation:** Vocabulary: incarnation: 化身

**[2714.72s] English:** More narrowly, it's literally learning from reinforcement, like.  
**Translation:** 

**[2719.12s] English:** The thing does something, and then it gets a reward or punishment. But, really, I think the way the term is used can be confusing.  
**Translation:** Vocabulary: narrowly: 狭义地

**[2723.80s] English:** Is it used today, and is it used to reform?  
**Translation:** 

**[2726.16s] English:** More broadly, the focus is on learning-based control, so some kind of system that's supposed to be controlling.  
**Translation:** Vocabulary: broadly: 广泛地

**[2730.98s] English:** Something, and it uses data to get better. What does "control" mean, so this action is the fundamental.  
**Translation:** 

**[2737.82s] English:** Element, yeah, it means making rational decisions now, and rational decisions are decisions that  
**Translation:** 

**[2742.50s] English:** Maximize a measure of utility, and sequentially, so you made decisions time and time again.  
**Translation:** 

**[2748.18s] English:** Now, like so, it's easier to see that kind of idea in the space of, maybe, games and the space of robotics.  
**Translation:** Vocabulary: maximize: 最大化; robotics: 机器人学; sequentially: 依次地; utility: 效用

**[2756.16s] English:** Do you see it bigger? Than that, is it applicable?  
**Translation:** 

**[2760.00s] English:** Like, where are the limits of the applicability of reinforcement learning?  
**Translation:** Vocabulary: applicability: 适用性

**[2764.52s] English:** Yeah, so rational decision-making is essentially the encapsulation of the AI problem viewed through a particular lens.  
**Translation:** 

**[2773.02s] English:** So, any problem that we would want a machine to solve, an intelligent machine, can likely be represented as a decision-making problem.  
**Translation:** Vocabulary: encapsulation: 抽象概括

**[2780.50s] English:** Classifying images is a decision-making problem, although not a sequential one, typically.  
**Translation:** 

**[2785.44s] English:** You know, controlling a chemical plant is a decision-making problem.  
**Translation:** Vocabulary: sequential: 顺序的

**[2790.00s] English:** Deciding what videos to recommend on YouTube is a decision-making problem.  
**Translation:** 

**[2793.64s] English:** And one of the really appealing things about reinforcement learning is, if it does encapsulate the range of all these decision-making problems,  
**Translation:** Vocabulary: appealing: 吸引人的; encapsulate: 概括; reinforcement: 强化学习

**[2801.80s] English:** Perhaps working on reinforcement learning is one of the ways to address a very broad range of AI problems.  
**Translation:** 

**[2809.86s] English:** But what is the fundamental difference between reinforcement learning and supervised machine learning?  
**Translation:** Vocabulary: supervised: 监督学习

**[2817.76s] English:** So, reinforcement learning can be...  
**Translation:** 

**[2820.00s] English:** It can be viewed as a generalization of supervised machine learning.  
**Translation:** Vocabulary: generalization: 泛化

**[2822.54s] English:** You can certainly cast supervised learning as a reinforcement learning problem.  
**Translation:** 

**[2825.66s] English:** You can just say your loss function is the negative of your reward.  
**Translation:** 

**[2828.74s] English:** But you have stronger assumptions.  
**Translation:** 

**[2830.18s] English:** You have the assumption that someone actually told you what the correct answer was, that your data was IID, and so on.  
**Translation:** Vocabulary: assumption: 假定; assumptions: 假定

**[2836.02s] English:** So, you could view reinforcement learning as essentially relaxing some of those assumptions.  
**Translation:** 

**[2840.34s] English:** Now, that's not always a very productive way to look at it, because if you actually have a supervised learning problem,  
**Translation:** 

**[2844.26s] English:** You'll probably solve it much more effectively by using supervised learning methods, because it's easier.  
**Translation:** 

**[2850.00s] English:** You can view reinforcement learning as a generalization of that.  
**Translation:** 

**[2852.44s] English:** No, for sure.  
**Translation:** 

**[2853.20s] English:** But they're fundamentally different.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2855.60s] English:** That's a mathematical statement.  
**Translation:** 

**[2857.18s] English:** That's absolutely correct.  
**Translation:** 

**[2858.64s] English:** But it seems that reinforcement learning, the kind of tools we bring to the table today, is becoming increasingly important.  
**Translation:** 

**[2864.30s] English:** So, maybe down the line, everything will be a reinforcement learning problem.  
**Translation:** 

**[2868.90s] English:** Just like you said, image classification should be mapped to a reinforcement learning problem.  
**Translation:** 

**[2873.60s] English:** But today, the tools and ideas, the way we think about them, are different.  
**Translation:** 

**[2878.98s] English:** Sort of...  
**Translation:** 

**[2880.00s] English:** Supervised learning has been used very effectively to solve basic narrow AI problems.  
**Translation:** 

**[2886.04s] English:** Reinforcement learning kind of represents the dream of AI; it's very much so in the research.  
**Translation:** 

**[2893.86s] English:** Space, now, is in sort of capturing the imagination of people about what we can do with intelligent.  
**Translation:** Vocabulary: reinforcement: 强化

**[2899.06s] English:** Systems, but it hasn't yet had as wide of an impact as the supervised learning approaches.  
**Translation:** 

**[2904.90s] English:** So, in a more practical sense, my question is about what gap do you see?  
**Translation:** Vocabulary: approaches: 方法; supervised: 监督

**[2911.84s] English:** Between the more general reinforcement learning and the very specific, it's sequential decision-making.  
**Translation:** 

**[2918.44s] English:** Making one sequence at a time in the sequence of supervised learning, so from a practical perspective,...  
**Translation:** Vocabulary: sequential: 顺序的

**[2924.00s] English:** Standpoint: I think that one thing that is, you know, potentially a little tough now, and this  
**Translation:** 

**[2929.66s] English:** Is, I think, something that we'll see. This is a gap that we might see closing over the next couple of  
**Translation:** Vocabulary: standpoint: 立场

**[2933.80s] English:** Years.  
**Translation:** 

**[2934.04s] English:** Is  
**Translation:** 

**[2934.88s] English:** The ability of reinforcement learning algorithms to effectively utilize  
**Translation:** 

**[2938.30s] English:** Large amounts of prior data, so one of the reasons why it's a bit difficult today.  
**Translation:** Vocabulary: utilize: 利用

**[2942.86s] English:** To use reinforcement learning for all the things that we might want to use it for.  
**Translation:** 

**[2946.68s] English:** Is that in most of the settings where we want to do rational decision making?  
**Translation:** 

**[2951.16s] English:** It's a little bit tough to just deploy some policy that does crazy stuff and learns purely.  
**Translation:** 

**[2957.62s] English:** Through trial and error, it's much easier to collect a lot of data and logs on some.  
**Translation:** Vocabulary: deploy: 部署

**[2962.56s] English:** Other policies that you've got, and then maybe you can use reinforcement learning to do that.  
**Translation:** 

**[2964.88s] English:** You know, if you can get a good policy out of that, then you deploy it and let it kind of fine-tune.  
**Translation:** 

**[2969.26s] English:** Little bit, but algorithmically it's quite difficult to do that, so I think that once we figure out how,...  
**Translation:** 

**[2974.86s] English:** To get reinforcement learning to bootstrap effectively from large data sets, then we'll  
**Translation:** Vocabulary: algorithmically: 按照算法; bootstrap: 启动; reinforcement: 强化

**[2980.26s] English:** See a very, very rapid growth in applications of these technologies, so this is what's referred to.  
**Translation:** 

**[2985.64s] English:** As off-policy reinforcement learning, or offline RL or batch RL, and I think we're seeing a lot of  
**Translation:** 

**[2991.30s] English:** Research right now is bringing us closer and closer to that.  
**Translation:** 

**[2994.88s] English:** Maybe paint the picture of the different methods she said, uh, off-policy, what's  
**Translation:** 

**[3000.00s] English:** Value-based reinforcement learning? What's policy-based? What's model-based? What's off-policy?  
**Translation:** 

**[3004.46s] English:** On-policy? What are the different categories of reinforcement learning?  
**Translation:** 

**[3008.10s] English:** So, one way we can think about reinforcement learning is that it's, in some very fundamental ways,  
**Translation:** 

**[3013.98s] English:** Way, it's about learning models that can answer kinds of what-if questions. So, what would happen,...  
**Translation:** 

**[3020.92s] English:** If I take this action that I haven't taken before? And you do that, of course, from experience.  
**Translation:** 

**[3025.72s] English:** From the data, and oftentimes you do it in a loop. So, you build a model that answers these "what-if" scenarios.  
**Translation:** Vocabulary: oftentimes: 经常; scenarios: 假设情况

**[3030.38s] English:** Questions? Use it to figure out the best action you can take, and then go and try taking that.  
**Translation:** 

**[3034.98s] English:** And see if the outcome agrees with what you predicted. So, the different kinds of techniques,...  
**Translation:** 

**[3041.04s] English:** Basically, refer to different ways of doing it. So, model-based methods answer a question of what.  
**Translation:** 

**[3046.84s] English:** State what you would get; basically, what would happen to the world if you were to take a certain action.  
**Translation:** 

**[3050.78s] English:** Value-based methods they answer the question of what value you would get, meaning what utility.  
**Translation:** 

**[3055.44s] English:** You would get, and so you can do that in a loop. So, model-based methods answer a question of  
**Translation:** Vocabulary: utility: usefulness

**[3055.72s] English:** What value would you get? But in a sense, they're not really all that different because...  
**Translation:** 

**[3059.26s] English:** They're both really just answering these what-if questions. Now, unfortunately for us,  
**Translation:** 

**[3064.84s] English:** With current machine learning methods, answering "what-if" questions can be really hard.  
**Translation:** 

**[3067.98s] English:** Because they are really questions about things that didn't happen. If you wanted to answer,  
**Translation:** 

**[3073.18s] English:** What if questions about things that did happen, you wouldn't need a learned model. You would just  
**Translation:** 

**[3076.00s] English:** Repeat the thing that worked before. And that's really a big part of why RL is a little bit tough.  
**Translation:** 

**[3083.40s] English:** So, if you have a purely  
**Translation:** 

**[3085.18s] English:** On-premise model, you don't have to answer a lot of questions about things that didn't happen.  
**Translation:** 

**[3085.70s] English:** So, if you have a purely on-premise model, you don't have to answer a lot of questions about things that didn't happen.  
**Translation:** 

**[3085.72s] English:** Then you go and try doing those mistaken things.  
**Translation:** 

**[3093.44s] English:** And then you observe the counterexamples.  
**Translation:** 

**[3095.34s] English:** That will teach you not to do those things again.  
**Translation:** Vocabulary: counterexamples: 反例

**[3097.48s] English:** If you have a bunch of off-policy data,  
**Translation:** 

**[3099.44s] English:** Data, and you just want to synthesize.  
**Translation:** Vocabulary: synthesize: 合成

**[3101.28s] English:** The best policy you can out of that data.  
**Translation:** 

**[3103.66s] English:** Then, you really have to deal with  
**Translation:** 

**[3105.10s] English:** The challenges of making these  
**Translation:** 

**[3107.08s] English:** Counterfactual queries.  
**Translation:** Vocabulary: counterfactual: 假设情况的; queries: 问题

**[3108.10s] English:** First of all, what's a policy?  
**Translation:** 

**[3110.16s] English:** A policy is  
**Translation:** 

**[3111.66s] English:** A model, or some  
**Translation:** 

**[3114.12s] English:** Kind of function that maps,  
**Translation:** 

**[3115.64s] English:** From observations of the world to actions.  
**Translation:** 

**[3120.00s] English:** So, in reinforcement learning, we often refer to the current configuration of the world as the state.  
**Translation:** Vocabulary: configuration: 状态; reinforcement: 强化学习

**[3126.22s] English:** So, we say that the state kind of encompasses everything you need to fully define where the world is at right now.  
**Translation:** 

**[3131.22s] English:** And depending on how we formulate the problem, we might say that you either get to see the state or you get to see an observation, which is some snapshot or piece of the state.  
**Translation:** Vocabulary: encompasses: 包括; snapshot: 快照

**[3139.88s] English:** So, policy just includes everything in it in order to be able to act in this world.  
**Translation:** 

**[3145.82s] English:** Yes.  
**Translation:** 

**[3146.02s] English:** And so, what does "off-policy" mean?  
**Translation:** 

**[3148.70s] English:** So, the terms "on-policy" and "off-policy" refer to how you get your data.  
**Translation:** 

**[3153.48s] English:** So, if you get your data from somebody else who was doing some other stuff, maybe you get your data from a manually programmed system that was just running in the world before.  
**Translation:** 

**[3164.46s] English:** That's referred to as off-policy data.  
**Translation:** 

**[3166.42s] English:** But if you get the data by actually acting in the world based on what your current policy thinks is good, we call that "on-policy" data.  
**Translation:** 

**[3172.90s] English:** And, obviously, policy data is more useful to you because if your current policy makes some bad decisions.  
**Translation:** 

**[3178.70s] English:** You will actually see that those decisions are bad off-policy data, however, might be much easier to obtain, because maybe that's all the log data that you have from before.  
**Translation:** 

**[3188.58s] English:** So, we talk about offline methods for autonomous vehicles, which you can envision as off-policy approaches in robotic spaces where there are already a ton of robots, but they don't get the luxury of exploring based on a reinforcement learning framework.  
**Translation:** Vocabulary: approaches: 方法; autonomous: 自主的; envision: 想象; robotic: 机器人的

**[3206.14s] English:** So, how do we make it open again?  
**Translation:** 

**[3208.70s] English:** Question: But how do we make off-policy methods work?  
**Translation:** 

**[3212.24s] English:** Yeah, so this is something that has been kind of a big open problem for a while, and in the last few years, people have made a little bit of progress on that.  
**Translation:** 

**[3221.70s] English:** You know, I can tell you about it, and it's not by any means solved yet, but I can tell you some of the things that, for example, we've done to try to address some of the challenges.  
**Translation:** 

**[3229.58s] English:** It turns out that one really big challenge with off-policy reinforcement learning is that you can't really trust your models to give accurate predictions.  
**Translation:** 

**[3238.70s] English:** For any possible action.  
**Translation:** Vocabulary: reinforcement: 强化

**[3240.00s] English:** So, if I've never tried to, and in my data set I never saw somebody steering the car off the road onto the sidewalk, my value function or my model is probably not going to predict the right thing if I ask what would happen if I were to steer the car off the road onto the sidewalk.  
**Translation:** 

**[3255.50s] English:** So, one of the important things you have to do to get off-policy RL to work is that you have to be able to figure out whether a given action will result in a trustworthy prediction or not.  
**Translation:** Vocabulary: sidewalk: 人行道; steering: 转向; trustworthy: 可靠的

**[3264.88s] English:** And you can use kinds of distribution estimation methods or density estimation methods to try to figure that out.  
**Translation:** 

**[3272.20s] English:** So, you could figure out that, well, this action, my model is telling me that it's great, but it looks totally different from anything I've taken before.  
**Translation:** Vocabulary: density: 密度; estimation: 估计

**[3277.96s] English:** So, my model is probably not correct.  
**Translation:** 

**[3279.94s] English:** And you can incorporate regularization terms into your learning objective, which will essentially tell you not to ask those questions that your model is unable to answer.  
**Translation:** Vocabulary: incorporate: 合并

**[3290.46s] English:** What would lead to breakthroughs in this space, do you think?  
**Translation:** 

**[3293.74s] English:** What is needed?  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[3295.20s] English:** Is this a data set question?  
**Translation:** 

**[3297.44s] English:** Do we need to collect large benchmark data sets that allow us to explore the space?  
**Translation:** Vocabulary: benchmark: 参考标准

**[3303.50s] English:** Is it a new kind of methodology?  
**Translation:** 

**[3308.32s] English:** What's your sense like?  
**Translation:** Vocabulary: methodology: 方法论

**[3309.70s] English:** Or maybe coming together in a space of robotics and defining the right problem to be working on?  
**Translation:** 

**[3314.62s] English:** I think, for off-policy reinforcement learning in particular, it's very much an algorithms question right now.  
**Translation:** Vocabulary: robotics: 机器人技术

**[3319.36s] English:** And, you know, this is something that I think is great because an algorithmic question is, you know,  
**Translation:** 

**[3324.30s] English:** That just takes some very smart people to get together and think about it really hard.  
**Translation:** Vocabulary: algorithmic: 算法的

**[3328.98s] English:** Whereas, if it was like a data problem or a hardware problem, that would take some serious engineering.  
**Translation:** 

**[3334.62s] English:** So, that's why I'm pretty excited about that problem, because I think we're in a position where we can make some real progress on it just by coming up with the right algorithms. In terms of which algorithms they could be, you know, the problems at their core are very related to problems in things like causal inference.  
**Translation:** Vocabulary: causal: 因果; inference: 推理

**[3351.20s] English:** Right.  
**Translation:** 

**[3351.42s] English:** Because, what you're really dealing with, are situations where.  
**Translation:** 

**[3354.30s] English:** You have a statistical model that's trying to make predictions about things I hadn't seen before.  
**Translation:** 

**[3360.00s] English:** And if it's a model that's generalizing properly, it will make good predictions.  
**Translation:** 

**[3364.46s] English:** If it's a model that picks up on spurious correlations, it will not generalize properly.  
**Translation:** 

**[3368.92s] English:** And then you have an arsenal of tools you could use.  
**Translation:** 

**[3371.12s] English:** You could, for example, figure out what regions are where it's trustworthy.  
**Translation:** 

**[3374.44s] English:** Or, on the other hand, you could try to make it generalize better somehow, or some combination of the two.  
**Translation:** Vocabulary: generalize: 泛化; trustworthy: 可靠

**[3380.44s] English:** Is there room for mixing, sort of, where most of it—like 90-95%—is off-policy?  
**Translation:** 

**[3389.52s] English:** You already have the data set.  
**Translation:** 

**[3391.28s] English:** And then you get to send the robot out to do a little exploration.  
**Translation:** 

**[3395.96s] English:** What's the role of mixing them together?  
**Translation:** 

**[3399.12s] English:** Yeah, absolutely.  
**Translation:** 

**[3399.82s] English:** I think that this is something you actually described very well at the beginning of our discussion when you talked about the iceberg.  
**Translation:** 

**[3407.24s] English:** This is the iceberg.  
**Translation:** 

**[3408.32s] English:** The 99% of your prior experience—that's your iceberg.  
**Translation:** 

**[3411.52s] English:** You'd use that for off-policy reinforcement learning.  
**Translation:** 

**[3413.70s] English:** And then, of course, if you've never opened that particular kind of door with that particular lock,...  
**Translation:** Vocabulary: reinforcement: 强化

**[3419.52s] English:** Then you have to go out and fiddle with it a little bit.  
**Translation:** 

**[3422.12s] English:** And that's that additional 1% to help you figure out a new task.  
**Translation:** Vocabulary: fiddle: 调整

**[3425.18s] English:** And I think that's actually a pretty good recipe going forward.  
**Translation:** 

**[3428.26s] English:** Is this, to you, the most exciting space in reinforcement learning now?  
**Translation:** Vocabulary: recipe: 方案

**[3432.84s] English:** Or is there...?  
**Translation:** 

**[3433.50s] English:** And maybe taking a step back—not just now, but what, to you, is the most beautiful idea?  
**Translation:** 

**[3440.08s] English:** I apologize for the romanticized question, but what is the beautiful idea or concept in reinforcement learning?  
**Translation:** 

**[3446.92s] English:** In general, I actually think....  
**Translation:** 

**[3449.52s] English:** I think that one of the things that is a very beautiful idea in reinforcement learning is...  
**Translation:** 

**[3452.86s] English:** Is just the idea that you can obtain a near-optimal control or a near-optimal policy.  
**Translation:** 

**[3461.30s] English:** Without actually having a complete model of the world.  
**Translation:** 

**[3465.60s] English:** This is, you know, it's something that feels perhaps a bit obvious.  
**Translation:** 

**[3470.80s] English:** If you just hear the term reinforcement learning, or you think about trial-and-error learning.  
**Translation:** 

**[3475.28s] English:** But from a controls perspective, it's a very weird thing because classically,  
**Translation:** 

**[3479.52s] English:** I don't think it's a very good idea.  
**Translation:** 

**[3480.00s] English:** You know, we think about engineered systems and controlling engineered systems as the problem of writing down some equations and then figuring out, given these equations, basically solve for X, figure out the thing that maximizes its performance.  
**Translation:** Vocabulary: equations: 方程式; maximizes: 最大化

**[3496.22s] English:** And the theory of reinforcement learning actually gives us a mathematically principled framework to reason about, you know, optimizing some quantity when you don't actually know the equations that govern that system.  
**Translation:** 

**[3508.58s] English:** And to me, that actually seems kind of elegant, you know, very elegant—something that doesn't become immediately obvious, at least in the mathematical sense.  
**Translation:** 

**[3520.20s] English:** Does it make sense to you that it works at all?  
**Translation:** 

**[3523.38s] English:** Well, I think it makes sense when you take some time to think about it, but it is a little surprising.  
**Translation:** 

**[3528.68s] English:** Well, then taking a step into the more deeper representations, which is also very surprising.  
**Translation:** 

**[3538.42s] English:** Yeah.  
**Translation:** Vocabulary: representations: 表现形式

**[3538.58s] English:** The richness of the state space—the space of environments that this kind of approach can operate in.  
**Translation:** 

**[3546.26s] English:** Can you maybe say what deep reinforcement learning is?  
**Translation:** 

**[3550.72s] English:** Well, deep reinforcement learning simply refers to taking reinforcement learning algorithms and combining them with high-capacity neural network representations, which is, you know, kind of an arbitrary thing at first.  
**Translation:** 

**[3563.88s] English:** Just take these two components and stick them together.  
**Translation:** Vocabulary: arbitrary: 随意; neural: 神经; reinforcement: 强化

**[3566.12s] English:** But the reason that it's.  
**Translation:** 

**[3567.48s] English:** It's something that has become so important in recent years that reinforcement learning faces an exacerbated version of a problem that has faced many other machine learning techniques.  
**Translation:** Vocabulary: exacerbated: 加剧的

**[3579.92s] English:** So, if you go back to, like, the early 2000s or the late 1990s, we'll see a lot of research on machine learning methods that have some very appealing mathematical properties, such as reducing convex optimization problems, for instance.  
**Translation:** 

**[3594.66s] English:** But they require very special inputs.  
**Translation:** Vocabulary: appealing: 吸引人的; convex: 凸的; inputs: 输入; mathematical: 数学的; optimization: 优化

**[3596.98s] English:** They require a representation of the input that is.  
**Translation:** 

**[3600.00s] English:** Clean in some way, like, for example, clean in the sense that the classes in your multi-class  
**Translation:** 

**[3605.76s] English:** Classification problems can be separated linearly. So they have some kind of good representation.  
**Translation:** 

**[3610.02s] English:** And we call this a feature representation. And for a long time, people were very worried about  
**Translation:** Vocabulary: classification: 分类问题

**[3614.22s] English:** Features in the world of supervised learning, because somebody had to actually build those.  
**Translation:** 

**[3617.74s] English:** Features. So, you couldn't just take an image and plug it into your logistic regression or your  
**Translation:** Vocabulary: logistic: 逻辑; regression: 回归; supervised: 监督

**[3621.76s] English:** SVM, or something. Someone had to take that image and process it using some handwritten code.  
**Translation:** 

**[3626.04s] English:** And then, neural nets came along, and they could actually learn the features. Suddenly, we  
**Translation:** 

**[3630.92s] English:** Could apply learning directly to the raw inputs, which was great for images, but it was even more beneficial for other types of data.  
**Translation:** 

**[3635.78s] English:** Great for all the other fields where people hadn't come up with good features yet.  
**Translation:** Vocabulary: beneficial: 有益的

**[3639.62s] English:** And one of those fields was actually reinforcement learning, because in reinforcement learning,  
**Translation:** 

**[3642.98s] English:** The notion of features: if you don't use neural nets and you have to design your own features,  
**Translation:** 

**[3646.52s] English:** It is very, very opaque. Like, it's very hard to imagine. For example, if I'm playing chess or  
**Translation:** 

**[3652.64s] English:** Go. What is a feature with which I can represent?  
**Translation:** Vocabulary: opaque: 不透明的

**[3656.04s] English:** The value function for Go, or even the optimal policy for Go, is linear. Like, I don't even know.  
**Translation:** 

**[3661.76s] English:** How to start thinking about it? And people tried all sorts of things. They would write down, you  
**Translation:** Vocabulary: linear: 线性的; optimal: 最优的

**[3665.00s] English:** Know that an expert chess player looks for whether the knight is in the middle of the board or not. So,  
**Translation:** 

**[3669.20s] English:** That's a feature. Is the knight in the middle of the board? And they would write these, like, long lists of  
**Translation:** Vocabulary: knight: 骑士

**[3673.36s] English:** Kind of arbitrary, made-up stuff. And that was really kind of getting us nowhere.  
**Translation:** 

**[3677.70s] English:** And that's a little bit easier; chess is a little more accessible than the robotics problem.  
**Translation:** Vocabulary: arbitrary: 主观随意; robotics: 机器人技术

**[3681.74s] English:** Absolutely.  
**Translation:** 

**[3682.32s] English:** Right. There are at least experts in the different features.  
**Translation:** 

**[3686.04s] English:** For chess. But still, like, the neural network there, to me, that's—I mean, you put it eloquently.  
**Translation:** 

**[3694.44s] English:** And almost made it seem like a natural step to add neural networks. But the fact that neural  
**Translation:** Vocabulary: eloquently: 流利地; neural: 神经

**[3700.06s] English:** Networks are able to discover features in the control problem; it's very interesting.  
**Translation:** 

**[3705.68s] English:** Hopeful. I'm not sure what to think about it, but it feels hopeful that the control problem has.  
**Translation:** 

**[3711.92s] English:** Features to be learned. Like,  
**Translation:** 

**[3716.04s] English:** I guess my question is: Is it surprising to you how far?  
**Translation:** 

**[3720.00s] English:** The deep side of deep reinforcement learning was able to, like, shed light on the space of problems that have been.  
**Translation:** 

**[3725.12s] English:** Able to tackle from, especially in games with Alpha Star and Alpha Zero, and just the  
**Translation:** Vocabulary: alpha: 阿尔法; reinforcement: 强化; tackle: 应对

**[3734.70s] English:** The representation power there, and in the robotic space, and what are your senses of the limits of?  
**Translation:** 

**[3741.88s] English:** This representation power and the control context; I think that, in regard to the limits, here.  
**Translation:** Vocabulary: robotic: 机器人相关的

**[3749.74s] English:** I think that one thing that makes it a little hard to fully answer this question is because, um,...  
**Translation:** 

**[3756.92s] English:** In settings where we would like to push these things to the limit, we encounter other bottlenecks.  
**Translation:** Vocabulary: bottlenecks: 瓶颈; encounter: 遇到

**[3763.38s] English:** So, like, the reason I can't get my robot to learn how to, you know, do the dishes.  
**Translation:** 

**[3771.88s] English:** In the kitchen, it's not because its neural net is not big enough; it's because when you try to  
**Translation:** 

**[3778.02s] English:** Actually, we do trial and error and try to do trial and error and try to do trial and error and try to.  
**Translation:** 

**[3779.72s] English:** And error learning, reinforcement learning, directly in the real world, where you have the  
**Translation:** 

**[3784.78s] English:** Potential to gather these large, highly varied, and complex data sets, you start running into  
**Translation:** 

**[3790.52s] English:** Other problems. Like one problem you run into very quickly, it'll first sound like a very pragmatic  
**Translation:** Vocabulary: pragmatic: 实用; varied: 多样

**[3796.44s] English:** Problem, but it actually turns out to be a pretty deep scientific problem. Take the robot and put it in  
**Translation:** 

**[3800.24s] English:** In your kitchen, have it try to learn to do the dishes with trial and error. It'll break all your dishes.  
**Translation:** 

**[3803.96s] English:** And then we'll have no more dishes to clean. Now, you might think this is a very practical issue.  
**Translation:** 

**[3808.86s] English:** But there's something to this, which is that if you have a person trying to do this, a person will  
**Translation:** 

**[3812.86s] English:** Have some degree of common sense. They'll break one dish and will be a little more careful with  
**Translation:** 

**[3816.00s] English:** The next one. And if they break all of them, they're going to go and get more, or something.  
**Translation:** 

**[3819.92s] English:** Like that, so there's all sorts of scaffolding that comes very naturally to us for our learning.  
**Translation:** 

**[3826.16s] English:** Process. Like, if I have to learn something through trial and error, I have the common sense to know.  
**Translation:** Vocabulary: scaffolding: 辅助结构

**[3830.96s] English:** That I have to try multiple times. If I screw something up, I ask for help or I reset things.  
**Translation:** 

**[3835.84s] English:** Or something like that. And all of that is kind of outside of the  
**Translation:** 

**[3838.86s] English:** Classic reinforcement.  
**Translation:** 

**[3840.00s] English:** Learning problem formulation. There are other things that can also be categorized as:  
**Translation:** Vocabulary: categorized: 归类; reinforcement: 强化

**[3845.24s] English:** Kind of scaffolding, but they are very important. For example, where do you get your rewards?  
**Translation:** 

**[3848.66s] English:** Function? If I want to learn how to pour a cup of water, well, how do I know if I've done it correctly?  
**Translation:** Vocabulary: rewards: 奖励

**[3854.44s] English:** Correctly? Now, that probably requires an entire computer vision system to be built just to  
**Translation:** 

**[3858.40s] English:** Determine that, and that seems a little bit inelegant. So, there are all sorts of things like  
**Translation:** Vocabulary: inelegant: 不优雅

**[3862.70s] English:** This starts to come up when we think through what we really need for reinforcement learning.  
**Translation:** 

**[3866.40s] English:** To happen at scale in the real world, and many of these things actually suggest a little bit of a  
**Translation:** 

**[3871.50s] English:** Shortcoming in the problem formulation, and a few deeper questions that we have to resolve.  
**Translation:** 

**[3876.18s] English:** That's really interesting. I talked to, like, David Silver about AlphaZero, and it seems like  
**Translation:** Vocabulary: shortcoming: 不足之处

**[3882.22s] English:** There's no limit at all in the context when there are no broken dishes.  
**Translation:** 

**[3889.82s] English:** So, in the case of Go, it's really about just scaling compute. So  
**Translation:** Vocabulary: compute: 计算

**[3895.40s] English:** Again, like, the bottleneck is the amount of money you're willing to invest in compute.  
**Translation:** 

**[3900.82s] English:** And then, perhaps, the different challenges around how difficult it is to scale compute.  
**Translation:** Vocabulary: bottleneck: 瓶颈

**[3906.30s] English:** Maybe. But there, there's no limit, and it's interesting. Now, we move to the real world.  
**Translation:** 

**[3911.20s] English:** And there are the broken dishes, there's all of it, and the reward function, as you mentioned,  
**Translation:** 

**[3916.16s] English:** That's really nice. So, how do we push forward there? Do you think,  
**Translation:** 

**[3921.12s] English:** There's this kind of sample efficiency question that people,  
**Translation:** 

**[3925.40s] English:** Bring up, you know, not having to break 100,000 dishes. Is this an algorithm question?  
**Translation:** 

**[3932.64s] English:** Is this a data selection, like, question? What do you think? How do we not break it?  
**Translation:** Vocabulary: algorithm: 算法

**[3939.58s] English:** Too many dishes? Yeah. Well, one way we can think about that is that  
**Translation:** 

**[3947.16s] English:** Maybe we need to be better at reusing our data, building that iceberg. So perhaps,  
**Translation:** Vocabulary: iceberg: 数据宝库; reusing: 重复利用

**[3955.40s] English:** Perhaps it's too much to hope that you can have a machine.  
**Translation:** 

**[3960.00s] English:** That, in isolation, in a vacuum, without anything else,  
**Translation:** Vocabulary: vacuum: 真空

**[3964.40s] English:** Can you just master complex tasks in minutes?  
**Translation:** 

**[3967.28s] English:** The way that people do.  
**Translation:** 

**[3968.62s] English:** But perhaps it also doesn't have to.  
**Translation:** 

**[3969.82s] English:** Perhaps what it really needs to do is  
**Translation:** 

**[3971.02s] English:** Is there an existence, a lifetime?  
**Translation:** 

**[3973.50s] English:** Where it does many things,  
**Translation:** 

**[3975.30s] English:** And the previous things that it has done.  
**Translation:** 

**[3977.04s] English:** Prepare it to do new things more efficiently.  
**Translation:** Vocabulary: efficiently: 高效地

**[3980.08s] English:** And the study of these kinds of questions,...  
**Translation:** 

**[3982.94s] English:** Typically, it falls under categories.  
**Translation:** 

**[3984.38s] English:** Like multitask learning or meta-learning,  
**Translation:** 

**[3987.06s] English:** But they all fundamentally deal  
**Translation:** Vocabulary: fundamentally: 本质上

**[3988.30s] English:** With the same general theme,  
**Translation:** 

**[3990.36s] English:** Which is the user experience for doing other things?  
**Translation:** 

**[3994.02s] English:** To learn to do new things efficiently and quickly.  
**Translation:** 

**[3997.20s] English:** So, what do you think about?  
**Translation:** 

**[3998.94s] English:** If we just look at the one particular case study,  
**Translation:** 

**[4001.26s] English:** Of a Tesla Autopilot that has quickly approaching...  
**Translation:** Vocabulary: approaching: 靠近

**[4004.86s] English:** Towards a million vehicles on the road,  
**Translation:** 

**[4007.48s] English:** Where some percentage of the time,  
**Translation:** 

**[4009.54s] English:** 30-40% of the time is driven using computer vision.  
**Translation:** 

**[4013.68s] English:** Multitask, Hydranet, right?  
**Translation:** Vocabulary: multitask: 多任务处理

**[4017.80s] English:** And then the other percent,  
**Translation:** 

**[4019.70s] English:** That's what they call it: Hydranet.  
**Translation:** Vocabulary: hydranet: 水管网

**[4022.70s] English:** The other percent is human-controlled.  
**Translation:** 

**[4026.24s] English:** From the human side, how can we use that data?  
**Translation:** 

**[4029.80s] English:** What's your sense?  
**Translation:** 

**[4030.64s] English:** So, like, what's the signal?  
**Translation:** 

**[4034.12s] English:** Do you have any ideas in this autonomous vehicle space?  
**Translation:** 

**[4036.12s] English:** When can people lose their lives?  
**Translation:** Vocabulary: autonomous: 自主的

**[4037.86s] English:** You know, it's a safety-critical environment.  
**Translation:** 

**[4041.42s] English:** So, how do we use that data?  
**Translation:** 

**[4043.88s] English:** So, I think that actually the kind of problems,  
**Translation:** 

**[4046.96s] English:** So, I think that actually the kind of problems,  
**Translation:** 

**[4047.66s] English:** That come up when we want systems that are reliable.  
**Translation:** 

**[4050.66s] English:** That come up when we want systems that are reliable.  
**Translation:** 

**[4053.66s] English:** And that can kind of understand the limits.  
**Translation:** 

**[4055.32s] English:** Of their capabilities,  
**Translation:** Vocabulary: capabilities: 能力

**[4056.66s] English:** They're actually very similar to the kind of problems,  
**Translation:** 

**[4058.22s] English:** That come up when we're doing  
**Translation:** 

**[4059.72s] English:** Off-policy reinforcement learning.  
**Translation:** 

**[4061.10s] English:** So, as I mentioned before,  
**Translation:** Vocabulary: reinforcement: 强化

**[4061.98s] English:** In off-policy reinforcement learning,  
**Translation:** 

**[4063.68s] English:** The big problem is, you need to know.  
**Translation:** 

**[4066.16s] English:** When you can trust the predictions of your model,  
**Translation:** 

**[4068.28s] English:** Because, if you're trying to evaluate some pattern,  
**Translation:** Vocabulary: evaluate: 评估

**[4071.46s] English:** Of behavior for which your model  
**Translation:** 

**[4072.54s] English:** Doesn't give you an accurate prediction,  
**Translation:** 

**[4074.04s] English:** Then, you shouldn't use that to modify your policy.  
**Translation:** 

**[4076.56s] English:** Then, you shouldn't use that to modify your policy.  
**Translation:** 

**[4077.48s] English:** Which is very similar to the problem.  
**Translation:** 

**[4078.52s] English:** That we're faced with when we actually then  
**Translation:** 

**[4080.00s] English:** Deploy that thing. And we want to decide whether we trust it in the moment or not. So perhaps we,  
**Translation:** 

**[4085.82s] English:** Just need to do a better job of figuring out that part. And that's a very deep research question.  
**Translation:** Vocabulary: deploy: 部署

**[4089.40s] English:** Of course. But it's also a question that a lot of people are working on, so I'm pretty optimistic.  
**Translation:** 

**[4092.46s] English:** That we can make some progress on that over the next few years. What's the role of simulation?  
**Translation:** 

**[4096.96s] English:** In reinforcement learning, deep reinforcement learning, or like how?  
**Translation:** 

**[4101.44s] English:** Is it essential? It has been essential for the breakthroughs so far, for some interesting developments.  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[4107.34s] English:** Breakthroughs. Do you think it's a crutch that we rely on? I mean, again, this connects to our...  
**Translation:** 

**[4113.32s] English:** Off-policy discussion. But do you think we can ever get rid of simulation? Or do you think...  
**Translation:** Vocabulary: crutch: 拐杖

**[4118.72s] English:** Simulation will actually take over? Will it create more and more realistic simulations that will  
**Translation:** 

**[4122.36s] English:** Allow us to solve actual real-world problems, like transferring the models we learn in simulation.  
**Translation:** Vocabulary: simulations: 模拟; transferring: 转移

**[4128.10s] English:** To solve real-world problems? Yeah. I think that simulation is a very pragmatic tool that we  
**Translation:** 

**[4132.90s] English:** Can be used to get a lot of useful stuff to work right now. But I think that in the long run,  
**Translation:** Vocabulary: pragmatic: 实用的

**[4137.34s] English:** We will need to build machines that can learn from real data, because that's the only way that  
**Translation:** 

**[4142.68s] English:** We'll get them to improve perpetually. Because if we can't have our machines learn from real data,  
**Translation:** Vocabulary: perpetually: 永远地

**[4148.12s] English:** If they have to rely on simulated data, eventually the simulator becomes the bottleneck.  
**Translation:** 

**[4152.36s] English:** In fact, this is a general thing. If your machine has any bottleneck that is built by humans,  
**Translation:** Vocabulary: bottleneck: 瓶颈; simulated: 模拟; simulator: 模拟器

**[4158.02s] English:** That doesn't improve from data; it will eventually be the thing that holds it back.  
**Translation:** 

**[4162.96s] English:** And if you're entirely reliant on your simulator, that'll be the bottleneck. If you're entirely...  
**Translation:** Vocabulary: reliant: 依赖的

**[4166.34s] English:** Reliant on a simulator, that'll be the bottleneck. If you're entirely reliant on a simulator, that'll  
**Translation:** 

**[4167.32s] English:** Be the bottleneck. So, simulation is very useful. It's very pragmatic, but it's not a substitute.  
**Translation:** Vocabulary: substitute: 替代品

**[4174.74s] English:** For being able to utilize real experience. And this is, by the way, something that I  
**Translation:** 

**[4181.42s] English:** Think is quite relevant now, especially in the context of some of the things we've discussed.  
**Translation:** 

**[4186.08s] English:** Because some of these kinds of scaffolding issues that I mentioned, such as broken dishes,...  
**Translation:** 

**[4190.30s] English:** And the unknown reward function; these are not problems that you would ever stumble upon.  
**Translation:** Vocabulary: scaffolding: 辅助知识; stumble: 偶然发现

**[4195.44s] English:** When working in a purely  
**Translation:** 

**[4196.96s] English:** Simulated environment is fine, but they become very apparent when we try to  
**Translation:** 

**[4200.00s] English:** To actually run these things in the real world, uh, to throw a brief wrench into our discussion, let  
**Translation:** 

**[4205.16s] English:** Me, ask: Do you think we're living in a simulation? Oh, I have no idea. Do you think that's a useful question?  
**Translation:** Vocabulary: wrench: 干扰

**[4210.86s] English:** A thing to even think about regarding the fundamental physics of reality.  
**Translation:** 

**[4216.86s] English:** Or, from another perspective, the reason I think the simulation hypothesis is interesting is it's to  
**Translation:** Vocabulary: hypothesis: 假说

**[4224.74s] English:** Think about how difficult it is to create a sort of virtual reality game-type situation.  
**Translation:** 

**[4232.16s] English:** That will be sufficiently convincing to us, or sufficiently enjoyable that we wouldn't.  
**Translation:** Vocabulary: sufficiently: 足够地

**[4238.78s] English:** Want to leave? I mean, that's actually a practical engineering challenge, and I personally really...  
**Translation:** 

**[4244.90s] English:** Enjoy virtual reality, but it's quite far away. But I kind of think about what it would take for me to.  
**Translation:** 

**[4250.40s] English:** Want to spend more time in virtual reality versus the real world?  
**Translation:** 

**[4253.86s] English:** You.  
**Translation:** 

**[4254.74s] English:** And that's a pretty clean question, because at that point we've reached  
**Translation:** 

**[4262.00s] English:** If I want to live in a virtual reality, that means we're just a few years away where the majority of the  
**Translation:** 

**[4267.46s] English:** Population lives in a virtual reality, and that's how we create the simulation. Right? You don't need  
**Translation:** 

**[4271.76s] English:** To actually simulate the known aspects of quantum gravity and just every aspect of it,  
**Translation:** Vocabulary: gravity: 引力; quantum: 量子; simulate: 模拟

**[4279.30s] English:** The universe, and that's an interesting question for reinforcement learning, too.  
**Translation:** 

**[4282.74s] English:** Is it if you want to make sufficiently?  
**Translation:** Vocabulary: reinforcement: 强化

**[4284.74s] English:** Realistic simulations that may blend the difference between the real world and  
**Translation:** 

**[4290.34s] English:** The simulation, therefore, just are some of the things we've been talking about—kind of the problems.  
**Translation:** Vocabulary: simulations: 模拟

**[4296.86s] English:** Go away. If we can create actually interesting, rich simulations, it's an interesting question, and it  
**Translation:** 

**[4301.80s] English:** Actually, I think your question casts your previous one in a very interesting light because in  
**Translation:** 

**[4307.28s] English:** Some ways, asking whether we can: um, the more practical version of this, like  
**Translation:** 

**[4313.86s] English:** You know, we can build simulations, but we can't do that in a very interesting way, and I think that's  
**Translation:** 

**[4314.74s] English:** That's a great question. I think it's a great question, and it's a really good question.  
**Translation:** 

**[4318.12s] English:** Um, I think we end up using a lot of like.  
**Translation:** 

**[4320.00s] English:** The world, and it's kind of interesting to think about this in terms of what this might imply if true.  
**Translation:** 

**[4325.80s] English:** It kind of implies that it's easier to create the universe than it is to create a brain.  
**Translation:** Vocabulary: implies: 意味着

**[4329.64s] English:** And that seems like, put this way, it seems kind of weird the aspect of the simulation.  
**Translation:** 

**[4336.34s] English:** Most interesting to me is the simulation of other humans that seems to be  
**Translation:** 

**[4342.08s] English:** A complexity that makes the robotics problem harder. Now, I don't know if every robotics person  
**Translation:** 

**[4349.86s] English:** Agrees with that notion, just as a quick aside, what are your thoughts about when the human  
**Translation:** Vocabulary: complexity: 复杂性; robotics: 机器人学

**[4356.80s] English:** Enters the picture of the robotics problem: How does that change the reinforcement learning problem?  
**Translation:** 

**[4361.92s] English:** The learning problem, in general, yeah, I think that's a pretty complex question and...  
**Translation:** 

**[4368.76s] English:** I guess, for a while, my hope had been that if we build these robotic learning systems, that  
**Translation:** 

**[4377.04s] English:** That are multitask and utilize lots of  
**Translation:** Vocabulary: multitask: 多任务; robotic: 机器人; utilize: 利用

**[4379.86s] English:** Prior data and that learn from their own experience, the bit where they have to interact.  
**Translation:** 

**[4384.48s] English:** With people, it will probably be handled in much the same way as all the other bits, so if they have...  
**Translation:** 

**[4389.24s] English:** Prior experience of interacting with people, and they can learn from their own experiences of.  
**Translation:** 

**[4393.20s] English:** Interacting with people for this new task might be enough, now, of course, there if it's not.  
**Translation:** Vocabulary: interacting: 交往

**[4399.04s] English:** Enough; there are many other things we can do, and there's quite a bit of research in that area.  
**Translation:** 

**[4401.96s] English:** Area, but I think it's worth a shot to see whether the multi-agent interaction is effective.  
**Translation:** 

**[4409.00s] English:** Ability to understand the the the the the the the the the the the the the the the the the the the  
**Translation:** 

**[4409.84s] English:** That other beings in the world have their own goals, intentions, and thoughts, and so on.  
**Translation:** 

**[4415.70s] English:** Whether that kind of understanding can emerge automatically from simply learning to do things.  
**Translation:** 

**[4422.18s] English:** With this, we can maximize utility by ensuring that the information arising from the data is accurate. You've mentioned something about gravity.  
**Translation:** Vocabulary: maximize: 最大化; utility: 实用性

**[4428.86s] English:** Sort of, um, that you don't need to explicitly inject anything into the system; they can be.  
**Translation:** 

**[4434.44s] English:** Learned from the data, and gravity is an example of something that could be learned from data.  
**Translation:** Vocabulary: explicitly: 明确地; gravity: 引力; inject: 注入

**[4438.50s] English:** Sort of like the physics of the system.  
**Translation:** 

**[4439.84s] English:** Sort of like the physics of the system.  
**Translation:** 

**[4440.00s] English:** World, like, what are the limits of what we can learn from data? Do you really think?  
**Translation:** 

**[4449.60s] English:** We can ask that in a very simple, clean way: do you really think we can learn gravity from?  
**Translation:** 

**[4455.66s] English:** Just data, like the idea of the laws of gravity — so something that I think is a common, kind of  
**Translation:** 

**[4463.18s] English:** A pitfall when thinking about prior knowledge and learning is to assume that just because  
**Translation:** 

**[4470.04s] English:** We know something, then it's better to tell the machine about that rather than have it figure it out.  
**Translation:** 

**[4475.48s] English:** It can handle on its own in many cases, things that are important and affect many of the events that the  
**Translation:** 

**[4483.80s] English:** The machine will experience are actually pretty easy to learn. Like, for example, if things happen every time you  
**Translation:** 

**[4488.86s] English:** Drop something, it falls down, like yeah. You might not get the, you know, kind.  
**Translation:** 

**[4493.16s] English:** Of the Newton's version, not Einstein's version, but it'll be pretty good, and it will probably  
**Translation:** 

**[4497.44s] English:** Be sufficient for you to act rationally in the world because you see the phenomenon all the time.  
**Translation:** 

**[4503.10s] English:** So, things that are readily apparent from the data, we might not need to specify those by hand.  
**Translation:** 

**[4507.98s] English:** Might actually be easier to let the machine figure them out; it just feels like there might be a  
**Translation:** Vocabulary: readily: 容易地; specify: 指定

**[4512.00s] English:** Space of many local minima, in terms of theories of this world that we would discover.  
**Translation:** 

**[4519.32s] English:** And get stuck on, "yeah, of course," Newtonian.  
**Translation:** Vocabulary: minima: 局部最小值; newtonian: 牛顿力学的

**[4522.44s] English:** Mechanical  
**Translation:** 

**[4523.16s] English:** Is not necessarily easy to come by, yeah, and well, in fact, in some fields of science, for example.  
**Translation:** 

**[4531.52s] English:** Human civilizations are often filled with these local optima, so, for example, if you think about how  
**Translation:** 

**[4536.32s] English:** People, uh, tried to figure out biology and medicine for the longest time, the kind of rules.  
**Translation:** Vocabulary: civilizations: 人类文明; optima: 局部最优解

**[4543.02s] English:** Like the kinds of principles that serve us very well in our day-to-day lives actually serve us.  
**Translation:** 

**[4547.00s] English:** Very poorly in understanding medicine and biology, we had kind of very superstitious beliefs.  
**Translation:** Vocabulary: superstitious: 迷信的

**[4552.46s] English:** And, weird.  
**Translation:** 

**[4553.16s] English:** Ideas about how the body worked until the advent of the modern scientific method.  
**Translation:** Vocabulary: advent: 出现

**[4556.72s] English:** So, that does seem to be, you know.  
**Translation:** 

**[4560.00s] English:** A failing of this approach, but it's also a failing of human intelligence, arguably.  
**Translation:** Vocabulary: arguably: 或许

**[4562.96s] English:** Maybe, as an aside, the idea of self-play is fascinating in reinforcement learning.  
**Translation:** 

**[4569.52s] English:** Learning to create a competitive context in which agents can operate.  
**Translation:** Vocabulary: reinforcement: 强化

**[4574.28s] English:** Play against each other in, uh, sort of at the same skill level, and thereby increasing  
**Translation:** 

**[4579.92s] English:** Each other's skill level seems to be this kind of self-improving mechanism.  
**Translation:** 

**[4584.10s] English:** Is exceptionally powerful in the context where it could be applied.  
**Translation:** 

**[4587.84s] English:** First of all, is it beautiful to you that this mechanism works as well as it does?  
**Translation:** Vocabulary: exceptionally: 特别地

**[4593.90s] English:** And it can also be generalized to other contexts, like in the robotic space or anything that's  
**Translation:** 

**[4601.94s] English:** Applicable to the real world, I think that it's a very interesting idea, but I suspect that...  
**Translation:** Vocabulary: generalized: 泛化; robotic: 类人

**[4609.62s] English:** The bottleneck to actually generalizing it to the robotic setting is actually going to be the same.  
**Translation:** 

**[4614.64s] English:** As the bottleneck for everything else that  
**Translation:** Vocabulary: bottleneck: 瓶颈; generalizing: 推广

**[4617.22s] English:** We need to  
**Translation:** 

**[4617.82s] English:** Be able to build machines that can get better and better through natural interaction with the world.  
**Translation:** 

**[4624.48s] English:** And once we can do that, they can go out and play with each other.  
**Translation:** 

**[4628.76s] English:** Play with people; they can play with the natural environment, but before we get there, we've got  
**Translation:** 

**[4634.28s] English:** All these other problems we've got—we have to get out of the way. So, there's no shortcut around that.  
**Translation:** 

**[4637.72s] English:** You have to interact with a natural environment, because in a self-play setting,  
**Translation:** Vocabulary: shortcut: 捷径

**[4642.84s] English:** You still need a mediating mechanism, so the reason that, you know, self-play...  
**Translation:** 

**[4647.68s] English:** Works for a board game is because the rules of that board game mediate the interaction between  
**Translation:** Vocabulary: mediate: 调和; mediating: 调解的

**[4652.54s] English:** The agents' behavior, so the kind of intelligent behavior that will emerge, depends very heavily on the  
**Translation:** 

**[4657.38s] English:** Nature of that mediating mechanism, so on the side of reward functions, that's coming up with good...  
**Translation:** 

**[4663.30s] English:** The reward function seems to be the thing we associate with general intelligence, like human beings.  
**Translation:** 

**[4669.98s] English:** Seems to value the idea of developing our own reward functions, of arriving at meaning.  
**Translation:** 

**[4676.66s] English:** And so on.  
**Translation:** 

**[4677.68s] English:** Yet, for reinforcement learning, we are  
**Translation:** Vocabulary: reinforcement: 强化

**[4680.00s] English:** Often, we kind of specify that's the given. What's your sense of how we develop good reward functions?  
**Translation:** 

**[4688.92s] English:** Yeah, I think that's a very complicated and very deep question. And you're completely right that.  
**Translation:** Vocabulary: specify: 指定

**[4693.24s] English:** Classically, in reinforcement learning, this question has kind of been treated as a non-issue.  
**Translation:** 

**[4699.26s] English:** That you sort of treat the reward as this external thing that comes from some other source.  
**Translation:** 

**[4704.80s] English:** Of your biology, and you kind of don't worry about it. And I do think that that's actually.  
**Translation:** 

**[4709.48s] English:** A little bit of a mistake that we should worry about, and we can approach it in a few ways.  
**Translation:** 

**[4714.24s] English:** Different ways. We can approach it, for instance, by thinking of reward as a communication medium.  
**Translation:** 

**[4718.92s] English:** We can say, "Well, how does a person communicate to a robot what its objective is?" You can approach  
**Translation:** 

**[4723.90s] English:** It also has more of an intrinsic motivation aspect. You could say, can we write down?  
**Translation:** 

**[4729.56s] English:** Kind of a general objective that leads to good capability? For example, can you write down  
**Translation:** Vocabulary: capability: 能力; intrinsic: 内在的

**[4736.14s] English:** Some objectives are such that, even in the absence of any other task, if you maximize the reward,  
**Translation:** 

**[4739.48s] English:** If you minimize that objective, you'll sort of learn useful things. This is something that has  
**Translation:** Vocabulary: maximize: 最大化; objectives: 目标

**[4744.34s] English:** Sometimes been called unsupervised reinforcement learning, which I think is a really fascinating.  
**Translation:** 

**[4748.38s] English:** Area of research, especially today. We've done a bit of work on that recently. One of the things,  
**Translation:** Vocabulary: unsupervised: 无监督的

**[4753.32s] English:** We've studied whether we can have some notion of unsupervised reinforcement learning by means of  
**Translation:** 

**[4761.56s] English:** Information-theoretic quantities, like, for instance, minimizing a Bayesian measure of,  
**Translation:** Vocabulary: bayesian: 贝叶斯的; minimizing: 最小化; reinforcement: 强化

**[4766.04s] English:** Surprise! This is an idea that was, you know, pioneered actually in the  
**Translation:** 

**[4769.48s] English:** Digital neuroscience community, by folks like Carl Friston. And we've done some work recently that.  
**Translation:** Vocabulary: friston: 弗里斯顿; neuroscience: 神经科学; pioneered: 开创

**[4774.00s] English:** Shows that you can actually learn pretty interesting skills by essentially behaving  
**Translation:** 

**[4778.62s] English:** In a way that allows you to make accurate predictions about the world, it seems a little  
**Translation:** Vocabulary: behaving: 行为

**[4782.88s] English:** Circular, like doing the things that will lead to you getting the right answer for prediction.  
**Translation:** 

**[4788.76s] English:** But you can, you know, by doing this, you can sort of discover stable niches in the world. You can  
**Translation:** Vocabulary: niches: 特定市场

**[4793.18s] English:** Discover that if you're playing Tetris, then, correctly, clearing the rows will let  
**Translation:** 

**[4798.24s] English:** You play Tetris for longer.  
**Translation:** 

**[4799.48s] English:** Keep the board.  
**Translation:** 

**[4800.00s] English:** Nice and clean, which sort of satisfies some desire for order in the world, and as a result,  
**Translation:** 

**[4804.80s] English:** Get some degree of leverage over your domain. So, we're exploring that pretty actively.  
**Translation:** 

**[4808.72s] English:** Is there a role for a human notion of curiosity, in itself being the reward, sort of discovering...?  
**Translation:** Vocabulary: actively: 积极地; leverage: 利用

**[4815.88s] English:** New things about the world? So, one of the things that I'm pretty  
**Translation:** 

**[4820.80s] English:** Interested in is actually whether discovering new things can, in fact, be an emergent property.  
**Translation:** Vocabulary: emergent: 涌现的

**[4827.36s] English:** Of some other objective that quantifies capability. So, new things for the sake of new.  
**Translation:** 

**[4832.40s] English:** Things, maybe, might not be the right answer by itself, but perhaps we can figure out an objective.  
**Translation:** Vocabulary: capability: 能力; quantifies: 量化

**[4839.42s] English:** For which discovering new things is actually the natural consequence. That's something we're  
**Translation:** 

**[4844.84s] English:** Working on it right now, but I don't have a clear answer for you there yet; that's still a work in progress.  
**Translation:** 

**[4848.24s] English:** Progress. You mean that it's just a curious observation to see sort of creative patterns?  
**Translation:** 

**[4856.54s] English:** Of curiosity?  
**Translation:** 

**[4857.36s] English:** On the way to optimizing for a particular measure of capability.  
**Translation:** 

**[4865.02s] English:** Is there any way to understand or anticipate unexpected, unintended consequences of?  
**Translation:** Vocabulary: anticipate: 预知; optimizing: 优化; unintended: 未预见的

**[4874.12s] English:** Particular reward functions sort of anticipate the kinds of strategies that might be developed.  
**Translation:** 

**[4881.64s] English:** And try to avoid highly detrimental strategies?  
**Translation:** 

**[4885.64s] English:** Yeah.  
**Translation:** 

**[4886.76s] English:** So.  
**Translation:** 

**[4887.36s] English:** Classically, this has been pretty hard in reinforcement learning because it's  
**Translation:** 

**[4891.68s] English:** Difficult for a designer to have good intuition about what a learning algorithm will do.  
**Translation:** 

**[4895.68s] English:** Come up with a solution when they give it an objective. There are ways to mitigate that. One way to  
**Translation:** 

**[4900.48s] English:** Mitigate it is to actually define an objective that says, for example, "don't do weird stuff." You can  
**Translation:** Vocabulary: mitigate: 减轻

**[4906.16s] English:** Actually, quantify it and say, just don't enter situations that have a low probability of success.  
**Translation:** 

**[4911.52s] English:** The distribution of states you've seen before. It turns out that it's actually one very good way to.  
**Translation:** 

**[4916.32s] English:** Do off-policy reinforcement. It's a very good way to do so. It's also a good way to  
**Translation:** 

**[4916.52s] English:** Do off-policy reinforcement. It's a good way to do so. It's a good way to do  
**Translation:** Vocabulary: reinforcement: 强化

**[4916.76s] English:** Off-policy reinforcement learning is a good way to do it, actually.  
**Translation:** 

**[4919.32s] English:** So.  
**Translation:** 

**[4920.00s] English:** Can do some things like that if we slowly venture in, speaking about reward functions.  
**Translation:** 

**[4926.72s] English:** Into greater and greater levels of intelligence, there's, uh, I mean, Steve Russell thinks about this.  
**Translation:** Vocabulary: venture: 尝试

**[4932.42s] English:** The alignment of AI systems with us humans: So, how do we ensure that AGI systems align with us humans?  
**Translation:** 

**[4942.68s] English:** It's kind of a reward function question of specifying the behavior of AI systems, such that  
**Translation:** Vocabulary: align: 使一致; alignment: 对齐; specifying: 规定

**[4952.64s] English:** Their success aligns with the broader intended interests of human beings, don't you?  
**Translation:** 

**[4960.46s] English:** Do you have any thoughts on this? Do you have any concerns about where reinforcement learning fits into this?  
**Translation:** Vocabulary: aligns: 一致

**[4965.34s] English:** Are you really focused on the current moment, given that we are quite far away and trying to solve the  
**Translation:** 

**[4970.30s] English:** Robotics problem; I don't have a great answer.  
**Translation:** Vocabulary: robotics: 机器人学

**[4972.66s] English:** To this, but um, you know, and I do think that this is a problem that's important to figure out.  
**Translation:** 

**[4978.70s] English:** For my part, I'm actually a bit more concerned about the other side of this equation.  
**Translation:** 

**[4984.56s] English:** Uh, you know, maybe rather than unintended consequences for objectives that are  
**Translation:** 

**[4991.50s] English:** Specified too well, I'm actually more worried right now about unintended consequences for.  
**Translation:** Vocabulary: objectives: 目标; specified: 规定; unintended: 未预见

**[4995.44s] English:** Objectives that are not optimized well enough, which might become a very pressing problem.  
**Translation:** 

**[5000.76s] English:** When we, for instance,  
**Translation:** Vocabulary: optimized: 优化

**[5002.30s] English:** You know,  
**Translation:** 

**[5002.64s] English:** Try to use these techniques for safety-critical systems, like cars and aircraft, and so on. I think.  
**Translation:** 

**[5008.74s] English:** At some point, we'll face the issue of objectives being optimized too well, but right now I think  
**Translation:** 

**[5013.28s] English:** We're more likely to face the issue of them not being optimized well enough, but you don't  
**Translation:** 

**[5017.66s] English:** Think that unintended consequences can arise, even when you're far from optimality—sort of like in this case.  
**Translation:** 

**[5022.02s] English:** Path to it, oh, no. I think unintended consequences can absolutely arise; it's just that I think right now,  
**Translation:** Vocabulary: optimality: 最佳状态

**[5027.90s] English:** The bottleneck for improving reliability, safety, and things like that.  
**Translation:** 

**[5032.64s] English:** Is there more that systems which need to work better and optimize their objectives better?  
**Translation:** Vocabulary: bottleneck: 瓶颈; optimize: 优化; reliability: 可靠性

**[5038.12s] English:** Do you have any thoughts?  
**Translation:** 

**[5040.00s] English:** Do you have concerns about existential threats posed by human-level artificial intelligence? If we put on our hats and look 10, 20, 100, or 500 years into the future, do you have concerns about existential threats from AI systems?  
**Translation:** Vocabulary: existential: 根本的

**[5055.38s] English:** I think there are absolutely existential threats for AI systems, just like there are for any powerful technology.  
**Translation:** 

**[5060.36s] English:** But I think that these kinds of problems can take many forms, and some of those forms will come down to people with nefarious intent.  
**Translation:** Vocabulary: intent: 意图; nefarious: 邪恶的

**[5073.74s] English:** Some of them will come down to AI systems that have some fatal flaws, and some of them will, of course, come down to AI systems that are too capable in some way.  
**Translation:** 

**[5084.80s] English:** But among this set of potential concerns, I would actually be much more concerned about the future.  
**Translation:** 

**[5090.36s] English:** I'm more concerned about the first two right now, and principally the one involving nefarious humans, because, you know, just through all of human history, actually, it's the nefarious humans that have been the problem, not the nefarious machines, than I am about the others.  
**Translation:** 

**[5101.48s] English:** And I think that right now, the best that I can do to make sure things go well is to, you know, build the best technology I can and also, hopefully, promote responsible use of that technology.  
**Translation:** Vocabulary: principally: 主要地

**[5113.44s] English:** Do you think RL systems have something to teach us humans?  
**Translation:** 

**[5118.30s] English:** You said "nefarious humans.  
**Translation:** 

**[5120.36s] English:** Getting us in trouble.  
**Translation:** 

**[5121.14s] English:** I mean, machine learning systems have, in some ways, revealed to us the ethical flaws in our data.  
**Translation:** 

**[5128.10s] English:** In that same kind of way, can reinforcement learning teach us about ourselves?  
**Translation:** 

**[5132.52s] English:** Has it taught anything?  
**Translation:** Vocabulary: reinforcement: 强化

**[5134.28s] English:** What have you learned about yourself from trying to build robots and reinforcement learning systems?  
**Translation:** 

**[5142.66s] English:** I'm not sure what I've learned about myself, but maybe part of the answer to your question might be: you know, the fact that I'm a robot.  
**Translation:** 

**[5150.36s] English:** I'm not sure what I've learned about myself, but maybe part of the answer to your question might be: you know, that I'm a robot.  
**Translation:** 

**[5160.00s] English:** You know, healthcare, education, social media, etc., and I think we will see some interesting stuff.  
**Translation:** Vocabulary: healthcare: 医疗

**[5165.48s] English:** Emerge there, uh, we will see. Uh, for instance, what kind of behaviors will these systems come up with?  
**Translation:** 

**[5170.32s] English:** In situations where there is interaction with humans, and where they have, you know,  
**Translation:** 

**[5176.30s] English:** The possibility of influencing human behavior—I think we're not quite there yet, but you know, maybe in.  
**Translation:** 

**[5181.10s] English:** The next few years, we'll see some interesting stuff coming out in that area. I hope so. Outside,...  
**Translation:** Vocabulary: influencing: 影响

**[5184.48s] English:** The research space, because the exciting space where this could be observed is sort of large.  
**Translation:** 

**[5190.32s] English:** Companies that deal with large data, and I hope there's some transparency because, and one of the  
**Translation:** 

**[5195.48s] English:** Things that are unclear when I look at social networks and just online is why an algorithm  
**Translation:** 

**[5200.92s] English:** Did something, or whether you know, even an algorithm was involved, and that'd be interesting.  
**Translation:** Vocabulary: algorithm: 计算程序

**[5206.20s] English:** As a researcher, just to observe the results of algorithms,  
**Translation:** 

**[5212.90s] English:** To open up.  
**Translation:** 

**[5214.48s] English:** Up that data to, or at least be sufficiently transparent about the behavior of these systems.  
**Translation:** 

**[5219.68s] English:** In the real world, what's your sense? I don't know if you looked at the blog post "Bitter Lesson.  
**Translation:** Vocabulary: sufficiently: 足够地; transparent: 透明

**[5225.60s] English:** By Everett Sutton, where it looks at sort of the big lesson of researching AI and in  
**Translation:** 

**[5233.84s] English:** Reinforcement learning is that simple, methods general in nature that leverage computation seem  
**Translation:** Vocabulary: computation: 计算; leverage: 利用; reinforcement: 强化; researching: 研究

**[5239.92s] English:** To work well, so basically, don't try to do any kind of fancy algorithms; just wait for computation to.  
**Translation:** 

**[5246.08s] English:** Get fast, do you share this kind of intuition? I think the high-level idea makes a lot of sense.  
**Translation:** Vocabulary: intuition: 直觉

**[5254.16s] English:** I'm not sure that my takeaway would be that we don't need to work on algorithms; I think that  
**Translation:** 

**[5258.56s] English:** My takeaway would be that we should work on general algorithms.  
**Translation:** Vocabulary: takeaway: 主要观点

**[5263.44s] English:** And actually, I think that this idea of needing to better automate...  
**Translation:** 

**[5270.56s] English:** The acquisition of experience in the real world.  
**Translation:** Vocabulary: acquisition: 获取; automate: 自动化

**[5274.40s] English:** Actually, it follows pretty naturally from Rich Sutton's conclusion. So, if the claim is  
**Translation:** 

**[5280.00s] English:** Is that an automated general method?  
**Translation:** Vocabulary: automated: 自动化的

**[5283.12s] English:** Plus, data leads to good results.  
**Translation:** 

**[5286.18s] English:** Then it makes sense that we should build general methods.  
**Translation:** 

**[5288.12s] English:** And we should build the kind of methods.  
**Translation:** 

**[5289.76s] English:** That we can deploy and get them to go out there.  
**Translation:** Vocabulary: deploy: 部署

**[5291.52s] English:** And they can collect their experience autonomously.  
**Translation:** 

**[5294.38s] English:** I think that one place where I think.  
**Translation:** Vocabulary: autonomously: 独立地

**[5296.86s] English:** That is the current state of things.  
**Translation:** 

**[5298.74s] English:** Falls a little bit short of that.  
**Translation:** 

**[5299.86s] English:** Is actually the going out there?  
**Translation:** 

**[5301.58s] English:** And collecting the data autonomously,  
**Translation:** 

**[5303.20s] English:** Which is easy to do in a simulated board game.  
**Translation:** 

**[5306.00s] English:** But it's very hard to do in the real world.  
**Translation:** Vocabulary: simulated: 模拟的

**[5307.24s] English:** Yeah, it keeps coming back to this one problem, right?  
**Translation:** 

**[5311.20s] English:** So, your mind is focused there now in this real world.  
**Translation:** 

**[5315.68s] English:** It just seems scary: this step of collecting the data.  
**Translation:** 

**[5321.66s] English:** And it seems unclear to me how we can do it effectively.  
**Translation:** 

**[5325.24s] English:** Well, you know, there are 7 billion people in the world.  
**Translation:** 

**[5328.24s] English:** Each of them had to do that at some point in their lives.  
**Translation:** 

**[5330.92s] English:** And we should leverage that experience.  
**Translation:** 

**[5332.58s] English:** That they've all done.  
**Translation:** Vocabulary: leverage: 利用

**[5334.48s] English:** We should be able to try to collect that kind of data.  
**Translation:** 

**[5338.06s] English:** Okay, big questions.  
**Translation:** 

**[5342.28s] English:** Maybe stepping back through your life,  
**Translation:** 

**[5345.22s] English:** What book or books—technical, fictional, or philosophical—  
**Translation:** Vocabulary: fictional: 小说; philosophical: 哲学的

**[5350.10s] English:** Had a big impact on the way you saw the world.  
**Translation:** 

**[5354.08s] English:** On the way you thought about the world,  
**Translation:** 

**[5355.64s] English:** Your life, in general?  
**Translation:** 

**[5357.48s] English:** Hmm.  
**Translation:** 

**[5359.36s] English:** And maybe what books, if it's different,  
**Translation:** 

**[5362.00s] English:** Would you recommend that people consider reading?  
**Translation:** 

**[5363.78s] English:** On their own intellectual journey?  
**Translation:** 

**[5366.16s] English:** It could be...  
**Translation:** 

**[5367.24s] English:** I don't know if this is a scientifically particularly meaningful answer.  
**Translation:** 

**[5379.32s] English:** But the honest answer is that I actually found  
**Translation:** Vocabulary: scientifically: 科学地

**[5382.90s] English:** A lot of the work by Isaac Asimov.  
**Translation:** 

**[5385.70s] English:** To be very inspiring when I was younger.  
**Translation:** 

**[5387.54s] English:** I don't know if that has anything to do with AI, necessarily.  
**Translation:** 

**[5390.86s] English:** You don't think it had a ripple effect in your life?  
**Translation:** Vocabulary: ripple: 波纹效应

**[5392.80s] English:** Maybe it did.  
**Translation:** 

**[5396.12s] English:** But, yeah, I think,  
**Translation:** 

**[5397.24s] English:** I think that a vision of a future...  
**Translation:** 

**[5400.00s] English:** Where, well, first of all, an artificial intelligence system or artificial robotic systems have, you know, kind of a big place and a big role in society, and where we try to imagine the sort of limiting case of technological advancement and how that might play out in our future history.  
**Translation:** Vocabulary: advancement: 进步; robotic: 机器人

**[5424.16s] English:** But, yeah, I think that was in some way influential. I don't really know how, but I would recommend it. I mean, if nothing else, you'd be well entertained.  
**Translation:** 

**[5436.92s] English:** When did you first fall in love with the idea of artificial intelligence and get captivated by this field?  
**Translation:** Vocabulary: captivated: 着迷; entertained: 娱乐; influential: 有影响力的

**[5444.58s] English:** So, my honest answer here is actually that I only really started to think about it as something that I might want to do.  
**Translation:** 

**[5453.40s] English:** Actually, in graduate school, pretty late. And a big part of that was that until, you know, somewhere around 2009-2010, it just wasn't really high on my priority list because I didn't think we'd see very substantial advances in my lifetime.  
**Translation:** Vocabulary: advances: 进展

**[5470.78s] English:** And, you know, maybe in terms of my career, the time when I really decided I wanted to work on this was when I actually took a seminar course that was taught by Professor Andrew.  
**Translation:** 

**[5483.40s] English:** And, you know, at that point, I, of course, had some kind of decent understanding of the technical things involved.  
**Translation:** Vocabulary: seminar: 研讨会

**[5490.18s] English:** But one of the things that really resonated with me was when he said, in the opening lecture, something to the effect of, "Well, he used to have graduate students come to him and talk about how they wanted to work on AI.  
**Translation:** 

**[5499.42s] English:** And he would kind of chuckle and give them some math problems to deal with.  
**Translation:** Vocabulary: chuckle: 轻笑

**[5502.38s] English:** But now, he's actually thinking that this is an area where we might see substantial advances in our lifetime.  
**Translation:** 

**[5507.46s] English:** And that kind of got me thinking, because, you know, in some abstract sense, yeah—like you can kind of imagine.  
**Translation:** 

**[5513.40s] English:** But, in a very real sense, when someone who had been working on that kind of stuff their whole career suddenly says that.  
**Translation:** 

**[5520.00s] English:** But, yeah, like that—that had some effect on me.  
**Translation:** 

**[5523.66s] English:** Yeah, this might be a special moment in the history of the field; this is where we might see some interesting breakthroughs.  
**Translation:** 

**[5533.82s] English:** So, in the space of advice, what would you recommend to someone who is interested in getting started in machine learning or reinforcement learning—maybe an undergraduate student or even younger?  
**Translation:** Vocabulary: breakthroughs: 重大进展; reinforcement: 强化学习; undergraduate: 本科生

**[5544.62s] English:** Or, how are the first steps to take? And further on, what are the steps to take on that journey?  
**Translation:** 

**[5552.54s] English:** So, something that I think is important to do is to not be afraid to spend time imagining the kind of outcome that you might like to see.  
**Translation:** 

**[5565.88s] English:** So, you know, one outcome might be a successful career, a large paycheck, or something, or state-of-the-art results on some benchmark.  
**Translation:** 

**[5573.30s] English:** But, hopefully, that's not the thing.  
**Translation:** Vocabulary: benchmark: 标准; paycheck: 工资条

**[5574.62s] English:** That's like the main driving force for someone.  
**Translation:** 

**[5577.42s] English:** But I think that if someone who's a student considering a career in AI takes a little while, sits down, and thinks, "What do I really want to see?  
**Translation:** 

**[5587.34s] English:** What I want to see a machine do?  
**Translation:** 

**[5588.66s] English:** What do I want to see a robot do?  
**Translation:** 

**[5590.24s] English:** What do I want to do?  
**Translation:** 

**[5590.92s] English:** And what I want to see is a natural language system—just like imagine it, you know, almost like a commercial for a future product or something, or like something that you'd like to see in the world.  
**Translation:** 

**[5600.92s] English:** And then actually sit down and think about the steps that are necessary to get there.  
**Translation:** 

**[5604.66s] English:** And hopefully, that thing is not a better number on ImageNet classification.  
**Translation:** Vocabulary: classification: 分类

**[5608.86s] English:** It's like an actual thing that we can't do today.  
**Translation:** 

**[5611.44s] English:** That would be really awesome—whether it's a robot butler, or a, you know, a really awesome health-care decision-making support system—whatever it is that you find inspiring.  
**Translation:** Vocabulary: butler: 男仆

**[5621.28s] English:** And I think that, by thinking about that and then backtracking from there and imagining the steps needed to get there, we will actually lead to much better research.  
**Translation:** 

**[5628.04s] English:** It will lead to rethinking the assumptions.  
**Translation:** Vocabulary: assumptions: 前提; backtracking: 逆向思考

**[5630.14s] English:** It will lead to working on the bottlenecks that other people aren't working on.  
**Translation:** 

**[5634.62s] English:** And then, naturally, we turned to you to talk about reward functions.  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[5640.00s] English:** And you just give some advice on looking forward to how you'd like to see what kinds of changes.  
**Translation:** 

**[5645.12s] English:** You would like to make a difference in the world. What do you think is a ridiculous big question: What do you think?  
**Translation:** 

**[5649.66s] English:** Is the meaning of life what is the meaning of your life? What gives you fulfillment and purpose?  
**Translation:** 

**[5656.02s] English:** Happiness and meaning — that's a very big question, um.  
**Translation:** Vocabulary: fulfillment: 满足感

**[5662.06s] English:** What's the reward function under which you're operating? Yeah, I think one thing that does give...  
**Translation:** 

**[5669.42s] English:** You know, if not meaning, at least some degree of satisfaction or confidence that I'm working.  
**Translation:** 

**[5675.58s] English:** On a problem that really matters, I feel like it's less important to me to actually solve it.  
**Translation:** 

**[5680.60s] English:** A problem, but it's quite nice to take things to spend my time on that I believe really.  
**Translation:** 

**[5687.80s] English:** Matter, and you know, I try pretty hard to look for that. I don't know if it's easy to answer this.  
**Translation:** 

**[5694.58s] English:** But, if you're successful, what does that look like?  
**Translation:** 

**[5699.42s] English:** What's the big dream now? Of course, success is built on top of success, and you keep going forever.  
**Translation:** 

**[5706.80s] English:** But what is the dream, yeah? So, one very concrete thing, or maybe as concrete as it's going to get.  
**Translation:** 

**[5714.80s] English:** Here is what we see: machines that actually get better and better the longer they are used.  
**Translation:** 

**[5722.34s] English:** Exists in the world, and that kind of seems like, on the surface, one might even think that's  
**Translation:** 

**[5726.66s] English:** Something that we have today, but I think we really don't appreciate it as much as we should.  
**Translation:** 

**[5729.42s] English:** Um, there is an unending complexity in the universe, and to date, all of the machines that  
**Translation:** Vocabulary: complexity: 复杂性

**[5738.66s] English:** We've been able to build, but not sort of improve up to the limit of that complexity; they they  
**Translation:** 

**[5744.10s] English:** They hit a wall somewhere. Maybe they hit a wall because they're in a simulator that has that.  
**Translation:** Vocabulary: simulator: 模拟器

**[5748.88s] English:** Only a very limited, very uh, pale imitation of the real world, or they hit a wall because they  
**Translation:** 

**[5753.22s] English:** Relying on a labeled data set, but they never hit the wall of running out of stuff to see.  
**Translation:** Vocabulary: imitation: 模仿; labeled: 标注的

**[5758.56s] English:** Like they never hit the wall of running out of stuff to see.  
**Translation:** 

**[5759.42s] English:** Like, they never hit the wall of running out of stuff to see.  
**Translation:** 

**[5760.00s] English:** So, you know, I'd like to build a machine that can go as far as possible in that regard.  
**Translation:** 

**[5764.70s] English:** Runs up against the ceiling of the complexity of the universe.  
**Translation:** Vocabulary: ceiling: 上限

**[5767.90s] English:** Yes.  
**Translation:** 

**[5769.30s] English:** Well, I don't think there's a better way to end it, Sergey.  
**Translation:** 

**[5771.84s] English:** Thank you so much.  
**Translation:** 

**[5772.52s] English:** It's a huge honor.  
**Translation:** 

**[5773.54s] English:** I can't wait to see the amazing work that you have to publish.  
**Translation:** 

**[5778.84s] English:** And in the education space, in terms of reinforcement learning, thank you for inspiring the world.  
**Translation:** Vocabulary: reinforcement: 强化

**[5782.92s] English:** Thank you for the great research you do.  
**Translation:** 

**[5784.42s] English:** Thank you.  
**Translation:** 

**[5785.36s] English:** Thanks for listening to this conversation with Sergey Levine.  
**Translation:** 

**[5788.12s] English:** And thank you to our sponsors, Cash App and ExpressVPN.  
**Translation:** Vocabulary: levine: 列文; sponsors: 赞助商

**[5793.42s] English:** Please consider supporting this podcast by downloading Cash App and using code LEXPODCAST, and signing up at expressvpn.com/lexpod.  
**Translation:** 

**[5804.30s] English:** Click all the links, buy all the stuff.  
**Translation:** 

**[5807.62s] English:** It's the best way to support this podcast and the journey I'm on.  
**Translation:** 

**[5811.82s] English:** If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcasts, and support on Patreon.  
**Translation:** Vocabulary: patreon: 支持平台; subscribe: 订阅

**[5818.12s] English:** Or connect with me on Twitter at @LexFriedman, spelled F-R-I-D-M-A-N, if you can figure it out without using the letter E.  
**Translation:** 

**[5828.92s] English:** And now, let me leave you with some words from Salvador Dalí.  
**Translation:** Vocabulary: salvador: 萨尔瓦多·达利

**[5833.38s] English:** Intelligence without ambition is a bird without wings.  
**Translation:** 

**[5838.54s] English:** Thank you for listening, and I hope to see you next time.  
**Translation:** 

**[5848.12s] English:** Transcription by CastingWords.  
**Translation:** Vocabulary: transcription: 录音文本


<!-- TRANSCRIPTION_COMPLETE -->
