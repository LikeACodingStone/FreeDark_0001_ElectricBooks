# Podcast vocabulary notes
Source file: Lex Fridman - Sergey Levine： Robotics and Machine Learning ｜ Lex Fridman Podcast #108.opus

**[0.00s] English:** The following is a conversation with Sergey Levine, a professor at Berkeley and a world-class researcher in deep learning, reinforcement learning, robotics, and computer vision,  
**Translation:** 

**[10.38s] English:** including the development of algorithms for end-to-end training of neural network policies that combine perception and control,  
**Translation:** 

**[17.60s] English:** scalable algorithms for inverse reinforcement learning, and, in general, deep RL algorithms.  
**Translation:** 

**[23.52s] English:** Quick summary of the ads. Two sponsors, Cash App and ExpressVPN.  
**Translation:** Vocabulary: inverse: 逆向; reinforcement: 强化; scalable: 可扩展; sponsors: 赞助商

**[27.98s] English:** Please consider supporting the podcast by downloading Cash App and using code LEXPODCAST and signing up at expressvpn.com slash lexpod.  
**Translation:** 

**[38.46s] English:** Click the links, buy the stuff. It's the best way to support this podcast and, in general, the journey I'm on.  
**Translation:** Vocabulary: expressvpn: 快速 vpn

**[46.22s] English:** If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcasts, follow on Spotify, support it on Patreon, or connect with me on Twitter at Lex Friedman.  
**Translation:** 

**[57.32s] English:** I do.  
**Translation:** Vocabulary: subscribe: 订阅

**[57.98s] English:** As usual, I'll do a few minutes of ads now and never any ads in the middle that can break the flow of the conversation.  
**Translation:** 

**[63.60s] English:** This show is presented by Cash App, the number one finance app in the App Store.  
**Translation:** 

**[68.38s] English:** When you get it, use code LEXPODCAST.  
**Translation:** 

**[71.62s] English:** Cash App lets you send money to friends, buy Bitcoin, and invest in the stock market with as little as $1.  
**Translation:** 

**[78.02s] English:** Since Cash App does fractional share trading, let me mention that the order execution algorithm that works behind the scenes  
**Translation:** 

**[84.76s] English:** to create the abstraction of the fractional orders.  
**Translation:** Vocabulary: abstraction: 抽象; algorithm: 算法; fractional: 分割的

**[87.98s] English:** It's an algorithmic marvel.  
**Translation:** 

**[90.16s] English:** So big props to the Cash App engineers for taking a step up to the next layer of abstraction over the stock market,  
**Translation:** Vocabulary: algorithmic: 算法; marvel: 奇迹; props: 称赞

**[95.84s] English:** making trading more accessible for new investors and diversification much easier.  
**Translation:** 

**[101.48s] English:** So again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST, you get $10.  
**Translation:** Vocabulary: diversification: 风险分散

**[109.36s] English:** And Cash App will also donate $10 to FIRST,  
**Translation:** 

**[112.30s] English:** an organization that is helping to advance robotics and STEM education for young people.  
**Translation:** 

**[117.98s] English:** So thanks again to Cash App, and how you're helping to change the world.  
**Translation:** 

**[119.66s] English:** This show is presented by Cash App, the number one finance app in the App Store.  
**Translation:** 

**[124.24s] English:** Thanks again to our sponsors.  
**Translation:** 

**[125.08s] English:** Cash App is a powerful source of information and information for the future of our business and for our customers.  
**Translation:** 

**[127.78s] English:** Cash App is an opportunity to help others make a difference in the world.  
**Translation:** 

**[130.50s] English:** This show is presented by Cash App, the number one finance app in the App Store.  
**Translation:** 

**[133.16s] English:** Ronald Reagan, the number one finance app in the App Store.  
**Translation:** 

**[135.26s] English:** Thank you for watching this video.  
**Translation:** 

**[136.02s] English:** If you haven't subscribed to our channel yet, please subscribe to our channel, and we'll see you next time.  
**Translation:** 

**[138.02s] English:** Thanks for watching this video.  
**Translation:** Vocabulary: subscribed: 订阅了

**[138.56s] English:** And next time, we'll talk about how Cash App can help a person take a step further and help a child to achieve success.  
**Translation:** 

**[140.00s] English:** So thanks again to our sponsors, and we'll see you next time.  
**Translation:** 

**[120.00s] English:** is also sponsored by ExpressVPN.  
**Translation:** 

**[123.72s] English:** Get it at expressvpn.com slash lexpod  
**Translation:** 

**[127.70s] English:** to support this podcast  
**Translation:** 

**[129.26s] English:** and to get an extra three months free  
**Translation:** 

**[132.22s] English:** on a one-year package.  
**Translation:** 

**[134.10s] English:** I've been using ExpressVPN for many years.  
**Translation:** 

**[137.34s] English:** I love it.  
**Translation:** 

**[138.58s] English:** I think ExpressVPN is the best VPN out there.  
**Translation:** 

**[141.88s] English:** They told me to say it,  
**Translation:** 

**[143.04s] English:** but it happens to be true in my humble opinion.  
**Translation:** 

**[145.98s] English:** It doesn't log your data.  
**Translation:** 

**[147.32s] English:** It's crazy fast and it's easy to use.  
**Translation:** 

**[150.06s] English:** Literally just one big power on button.  
**Translation:** 

**[152.80s] English:** Again, it's probably obvious to you,  
**Translation:** 

**[154.78s] English:** but I should say it again.  
**Translation:** 

**[156.48s] English:** It's really important that they don't log your data.  
**Translation:** 

**[159.98s] English:** It works on Linux and every other operating system,  
**Translation:** 

**[163.20s] English:** but Linux, of course, is the best operating system.  
**Translation:** 

**[166.56s] English:** Shout out to my favorite flavor, Ubuntu Mate 2004.  
**Translation:** 

**[170.54s] English:** Once again, get it at expressvpn.com slash lexpod  
**Translation:** Vocabulary: expressvpn: 快速vpn

**[174.02s] English:** to support this podcast  
**Translation:** 

**[175.46s] English:** and to get an extra three months free  
**Translation:** 

**[178.36s] English:** on a one-year package.  
**Translation:** 

**[180.00s] English:** And now, here's my conversation with Sergei Levine.  
**Translation:** 

**[185.26s] English:** What's the difference between a state-of-the-art human,  
**Translation:** 

**[188.60s] English:** such as you and I,  
**Translation:** 

**[189.92s] English:** well, I don't know if we qualify as state-of-the-art humans,  
**Translation:** 

**[191.92s] English:** but a state-of-the-art human and a state-of-the-art robot?  
**Translation:** 

**[196.10s] English:** That's a very interesting question.  
**Translation:** 

**[198.68s] English:** Robot capability is, it's kind of a,  
**Translation:** Vocabulary: capability: 能力

**[202.26s] English:** I think it's a very tricky thing to understand  
**Translation:** 

**[205.10s] English:** because there are some things that are difficult  
**Translation:** 

**[208.08s] English:** that we wouldn't think are difficult  
**Translation:** 

**[209.16s] English:** and some things that are easy to understand.  
**Translation:** 

**[209.84s] English:** And there's also a really big gap  
**Translation:** 

**[214.24s] English:** between capabilities of robots  
**Translation:** 

**[216.12s] English:** in terms of hardware and their physical capability  
**Translation:** 

**[218.68s] English:** and capabilities of robots  
**Translation:** 

**[220.28s] English:** in terms of what they can do autonomously.  
**Translation:** 

**[222.54s] English:** There is a little video  
**Translation:** Vocabulary: autonomously: 独立地

**[224.10s] English:** that I think robotics researchers really like to show,  
**Translation:** 

**[227.18s] English:** especially robotics learning researchers like myself  
**Translation:** 

**[228.84s] English:** from 2004 from Stanford,  
**Translation:** 

**[231.78s] English:** which demonstrates a prototype robot called the PR1.  
**Translation:** Vocabulary: prototype: 样品; stanford: 斯坦福大学

**[235.34s] English:** And the PR1 was a robot that was designed  
**Translation:** 

**[237.08s] English:** as a home assistance robot.  
**Translation:** 

**[239.04s] English:** And there's this beautiful,  
**Translation:** 

**[239.84s] English:** beautiful,  
**Translation:** 

**[240.00s] English:** video showing the PR one, tidying up a living room, putting away toys, and at the end, bringing  
**Translation:** 

**[245.70s] English:** a beer to the person sitting on the couch, which looks really amazing. And then the punchline is  
**Translation:** Vocabulary: punchline: 笑点

**[253.02s] English:** that this robot is entirely controlled by a person. So in some ways, the gap between a  
**Translation:** 

**[258.46s] English:** state-of-the-art human and a state-of-the-art robot, if the robot has a human brain, is actually  
**Translation:** 

**[262.68s] English:** not that large. Now, obviously, human bodies are sophisticated and very robust and resilient in  
**Translation:** 

**[267.30s] English:** many ways, but on the whole, if we're willing to spend a bit of money and do a bit of engineering,  
**Translation:** Vocabulary: resilient: 坚韧; robust: 强壮; sophisticated: 复杂

**[272.44s] English:** we can kind of close the hardware gap, almost. But the intelligence gap, that one is very wide.  
**Translation:** 

**[280.10s] English:** And when you say hardware, you're referring to the physical, sort of the actuators,  
**Translation:** Vocabulary: actuators: 执行器

**[283.80s] English:** the actual body of the robot, as opposed to the hardware on which the cognition,  
**Translation:** 

**[288.04s] English:** the hardware of the nervous system. Yes, exactly. I'm referring to the body rather than the mind.  
**Translation:** Vocabulary: cognition: 认知

**[294.02s] English:** So that means that the work is cut out for us.  
**Translation:** 

**[297.30s] English:** While we can still make the body better, we kind of know that the big bottleneck right now is really  
**Translation:** Vocabulary: bottleneck: 瓶颈

**[301.06s] English:** the mind. And how big is that gap? How big is the difference in your sense of ability to learn,  
**Translation:** 

**[309.66s] English:** ability to reason, ability to perceive the world between humans and our best robots?  
**Translation:** Vocabulary: perceive: 感知

**[316.88s] English:** The gap is very large, and the gap becomes larger the more unexpected  
**Translation:** 

**[321.68s] English:** events can happen in the world. So essentially, the spectrum along which you can measure,  
**Translation:** 

**[327.30s] English:** the size of that gap is the spectrum of how open the world is. If you control everything in the  
**Translation:** 

**[333.12s] English:** world very tightly, if you put the robot in like a factory, and you tell it where everything is,  
**Translation:** 

**[337.36s] English:** and you rigidly program its motion, then it can do things, you know, one might even say,  
**Translation:** 

**[342.50s] English:** in a superhuman way, it can move faster, it's stronger, it can lift up a car and things like  
**Translation:** 

**[346.22s] English:** that. But as soon as anything starts to vary in the environment, now it'll trip up. And if many,  
**Translation:** 

**[351.92s] English:** many things vary, like they would, like in your kitchen, for example, then things are pretty much  
**Translation:** 

**[356.76s] English:** wide open.  
**Translation:** 

**[357.28s] English:** Now, again, we're going to stick  
**Translation:** 

**[360.00s] English:** a bit on the philosophical questions but uh how much on the human side of the cognitive abilities  
**Translation:** 

**[367.20s] English:** in your sense is nature versus nurture so so how much of it is a product of  
**Translation:** Vocabulary: cognitive: 认知; nurture: 养育; philosophical: 哲学的

**[374.56s] English:** evolution and how much of it is something we'll learn from sort of scratch yeah from the day we're  
**Translation:** 

**[380.94s] English:** born i'm going to read into your question as asking about the implications of this for ai  
**Translation:** 

**[386.14s] English:** because i'm not a biologist i can't really like speak authoritatively so and to linger on it if  
**Translation:** 

**[392.02s] English:** if it's so if it's all about learning then there's more hope for ai yeah so the way that i look at  
**Translation:** Vocabulary: authoritatively: 有权威地; biologist: 生物学家

**[399.54s] English:** this is that um you know well first of course biology is very messy and it's if you ask the  
**Translation:** 

**[407.02s] English:** question how does a person do something or how does a person's mind do something um you can come  
**Translation:** 

**[411.56s] English:** up with a bunch of hypotheses and oftentimes you can find support for many different often  
**Translation:** 

**[415.66s] English:** conflicting hypotheses  
**Translation:** Vocabulary: hypotheses: 假设; oftentimes: 经常

**[416.14s] English:** um one way that we can approach the question of of what the implications of this for ai are  
**Translation:** 

**[423.18s] English:** is we can think about what's sufficient so you know maybe a person is from birth very very good  
**Translation:** 

**[429.74s] English:** at some things like for example recognizing faces there's a very strong evolutionary pressure to do  
**Translation:** 

**[433.74s] English:** that if you can recognize your mother's face then you're more likely to survive and therefore people  
**Translation:** 

**[439.08s] English:** are good at this but we can also ask like what's what's the minimum sufficient thing right and one  
**Translation:** 

**[444.38s] English:** of the ways that we can study the minimal sufficient thing is that we can study the  
**Translation:** 

**[446.14s] English:** things that we can study the minimal sufficient thing is we could for example see what people do  
**Translation:** 

**[448.24s] English:** in unusual situations if you present them with things that evolution couldn't have prepared them  
**Translation:** 

**[452.16s] English:** for you know our daily lives actually do this to us all the time we we didn't evolve to deal with  
**Translation:** 

**[457.96s] English:** you know automobiles and space flight and whatever so there are all these situations that we can find  
**Translation:** 

**[462.88s] English:** ourselves in uh and we do very well there like i can give you a joystick to control a robotic arm  
**Translation:** 

**[469.40s] English:** which you've never used before and you might be pretty bad for the first couple of seconds but  
**Translation:** Vocabulary: joystick: 操纵杆

**[472.84s] English:** if i tell you like your life depends on using this robotic arm to like you know do things that you're  
**Translation:** 

**[476.14s] English:** like open this door you'll probably manage it even though you've  
**Translation:** 

**[480.00s] English:** ever seen this device before you've never used the joystick controllers and you'll kind of muddle  
**Translation:** 

**[483.86s] English:** through it and that's not uh your evolved natural ability that's your your flexibility your  
**Translation:** Vocabulary: flexibility: 适应能力; muddle: 搞乱

**[490.14s] English:** adaptability and that's exactly where our current robotic systems really kind of fall flat but i  
**Translation:** 

**[495.00s] English:** wonder how much general almost what we think of as common sense pre-trained models underneath all  
**Translation:** Vocabulary: adaptability: 适应能力

**[503.26s] English:** of that so that ability to adapt to a joystick is requires you to have a kind of you know i'm human  
**Translation:** 

**[512.60s] English:** so it's hard for me to introspect all the knowledge i have about the world but it seems like there  
**Translation:** 

**[517.60s] English:** might be an iceberg underneath of the amount of knowledge we actually bring to the table that's  
**Translation:** 

**[523.36s] English:** kind of the open question i think there's absolutely there's absolutely an iceberg of  
**Translation:** Vocabulary: iceberg: 冰山一角

**[526.30s] English:** knowledge that we bring to the table but i think it's very likely that iceberg of knowledge is  
**Translation:** 

**[531.50s] English:** actually built up over our lifetimes  
**Translation:** Vocabulary: lifetimes: 一生积累

**[533.02s] English:** because we have you know we have a lot of prior experience to draw on uh and it kind of makes  
**Translation:** 

**[539.80s] English:** sense that the right way for us to you know to optimize uh our our efficiency our evolutionary  
**Translation:** Vocabulary: evolutionary: 进化; optimize: 优化

**[546.26s] English:** fitness and so on is to utilize uh all that experience to to build up the best iceberg we  
**Translation:** 

**[552.08s] English:** can get uh and that's actually one of you know while that sounds an awful lot like what machine  
**Translation:** 

**[556.64s] English:** learning actually does i think that for modern machine learning it's actually a really big  
**Translation:** 

**[560.32s] English:** challenge to take this unstructured massive experience and to build up the best iceberg  
**Translation:** Vocabulary: unstructured: 无结构

**[563.02s] English:** experience and distill out something that looks like a common sense understanding of the world  
**Translation:** 

**[567.60s] English:** and perhaps part of that isn't it's not because something about machine learning itself is is  
**Translation:** Vocabulary: distill: 提炼

**[572.80s] English:** broken or hard but because we've been a little too rigid in subscribing to a very supervised very  
**Translation:** 

**[579.34s] English:** rigid notion of learning you know kind of the input output x's go go to y's sort of model  
**Translation:** Vocabulary: subscribing: 订阅; supervised: 监督

**[583.46s] English:** and maybe what we really need to uh to do is to view the world more as like a massive experience  
**Translation:** 

**[591.08s] English:** that is not necessarily providing  
**Translation:** 

**[593.02s] English:** any rigid supervision but sort of providing many many instances of things that could be  
**Translation:** 

**[596.52s] English:** and then you take that and you distill it into some sort of common sense  
**Translation:** Vocabulary: supervision: 监督

**[600.00s] English:** understanding. I see. Well, you're painting an optimistic, beautiful picture, especially from  
**Translation:** 

**[606.16s] English:** the robotics perspective, because that means we just need to invest and build better learning  
**Translation:** Vocabulary: optimistic: 乐观的

**[610.70s] English:** algorithms, figure out how we can get access to more and more data for those learning algorithms  
**Translation:** 

**[617.30s] English:** to extract signal from and then accumulate that iceberg of knowledge. It's a beautiful picture.  
**Translation:** 

**[623.94s] English:** It's a hopeful one. I think it's potentially a little bit more than just that. And this is  
**Translation:** 

**[629.32s] English:** where we perhaps reach the limits of our current understanding. But one thing that I think that  
**Translation:** 

**[634.64s] English:** the research community hasn't really resolved in a satisfactory way is how much it matters where  
**Translation:** 

**[640.48s] English:** that experience comes from. Do you just download everything on the internet and cram it into  
**Translation:** Vocabulary: satisfactory: 令人满意的

**[645.66s] English:** essentially the 21st century analog of the giant language model and then see what happens? Or  
**Translation:** 

**[652.80s] English:** does it actually matter whether your machine physically experiences the world in the sense  
**Translation:** Vocabulary: analog: 模拟物

**[658.42s] English:** that it actually attempts to do that?  
**Translation:** 

**[659.32s] English:** It observes the outcome of its actions and kind of augments its experience that way.  
**Translation:** Vocabulary: augments: 增强; observes: 观察

**[663.60s] English:** That it chooses which parts of the world it gets to interact with and observe and learn from.  
**Translation:** 

**[670.32s] English:** Right. It may be that the world is so complex that simply obtaining a large mass of sort of  
**Translation:** 

**[676.78s] English:** samples of the world is a very difficult way to go. But if you are actually interacting with the  
**Translation:** 

**[683.70s] English:** world and essentially performing this sort of hard negative mining by attempting what you think  
**Translation:** 

**[687.62s] English:** might work, observing the...  
**Translation:** 

**[689.32s] English:** Sometimes happy and sometimes sad outcomes of that and augmenting your understanding using that  
**Translation:** Vocabulary: augmenting: 增加

**[695.14s] English:** experience and you're just doing this continually for many years, maybe that sort of data in some  
**Translation:** 

**[700.20s] English:** sense is actually much more favorable to obtaining a common sense understanding. One reason we might  
**Translation:** 

**[705.32s] English:** think that this is true is that what we associate with common sense or lack of common sense is often  
**Translation:** 

**[712.46s] English:** characterized by the ability to reason about kind of counterfactual questions. Like if I were to  
**Translation:** Vocabulary: counterfactual: 假设情况

**[719.32s] English:** take a shot at eating an egg and I wanted to know what would happen to it, I would probably  
**Translation:** 

**[724.12s] English:** not see the same response that we get anywhere else.  
**Translation:** 

**[729.96s] English:** If you were to take a shot at eating an egg and you thought, oh, I'm going to eat begin to read  
**Translation:** 

**[739.64s] English:** as it's called, or if you were to take a shot at eating an egg and you thought there was an  
**Translation:** 

**[743.20s] English:** example of having an egg that did not get eaten, what is this?  
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

**[720.00s] English:** This bottle of water sitting on the table, everything is fine if I were to knock it over, which I'm not going to do.  
**Translation:** 

**[725.04s] English:** But if I were to do that, what would happen?  
**Translation:** 

**[727.34s] English:** And I know that nothing good would happen from that.  
**Translation:** 

**[730.24s] English:** But if I have a bad understanding of the world, I might think that that's a good way for me to, like, you know, gain more utility.  
**Translation:** 

**[735.60s] English:** If I actually go about my daily life doing the things that my current understanding of the world suggests will give me high utility, in some ways I'll get exactly the right supervision to tell me not to do those bad things and to keep doing the good things.  
**Translation:** Vocabulary: supervision: 监督

**[752.72s] English:** So there's a spectrum between IID, random walk through the space of data, and then there's what we humans do.  
**Translation:** 

**[761.02s] English:** Well, I don't even know if we do it optimal, but that might be beyond.  
**Translation:** Vocabulary: optimal: 最优化的

**[765.20s] English:** What?  
**Translation:** 

**[765.60s] English:** So this open question that you raised, where do you think systems, intelligent systems that would be able to deal with this world fall?  
**Translation:** 

**[776.26s] English:** Can we do pretty well by reading all of Wikipedia, sort of randomly sampling it like language models do?  
**Translation:** 

**[783.64s] English:** Or do we have to be exceptionally selective and intelligent about which aspects of the world we interact with?  
**Translation:** Vocabulary: exceptionally: 特别地; selective: 选择性的

**[791.70s] English:** So I think this is, first, an open scientific problem.  
**Translation:** 

**[794.48s] English:** And I don't have, like, a clear...  
**Translation:** 

**[795.60s] English:** I don't have a clear answer, but I can speculate a little bit.  
**Translation:** 

**[797.84s] English:** And what I would speculate is that you don't need to be super, super careful.  
**Translation:** Vocabulary: speculate: 猜测

**[803.28s] English:** I think it's less about, like, being careful to avoid the useless stuff and more about making sure that you hit on the really important stuff.  
**Translation:** 

**[811.54s] English:** So perhaps it's okay if you spend part of your day just, you know, guided by your curiosity, visiting interesting regions of your state space.  
**Translation:** 

**[819.88s] English:** But it's important for you to, you know, every once in a while, make sure that you really try out the...  
**Translation:** 

**[825.60s] English:** solutions that your current model of the world suggests might be effective and observe whether those solutions are working as you expect or not.  
**Translation:** 

**[832.42s] English:** And perhaps some of that is really essential to have kind of a perpetual improvement loop.  
**Translation:** 

**[840.00s] English:** actual improvement loop is really like that that's really the key the key that's going to  
**Translation:** Vocabulary: perpetual: 永续的

**[843.80s] English:** potentially distinguish the best current methods from the best methods of tomorrow in a sense  
**Translation:** 

**[848.38s] English:** how important do you think is exploration or total out of the box  
**Translation:** 

**[852.28s] English:** thinking exploration in this space as you jump to totally different domains so you kind of mentioned  
**Translation:** 

**[860.18s] English:** there's an optimization problem you kind of kind of explore the specifics of a particular strategy  
**Translation:** Vocabulary: optimization: 最优化问题

**[865.58s] English:** whatever the thing you're trying to solve how important is it to explore totally outside of  
**Translation:** 

**[871.16s] English:** the strategies that have been working for you so far what's your intuition there yeah i think it's  
**Translation:** Vocabulary: intuition: 直觉

**[875.84s] English:** a very problem dependent kind of question and i think that that's actually you know in some ways  
**Translation:** 

**[881.20s] English:** that question gets at um one of the big differences between uh sort of the classic formulation of a  
**Translation:** 

**[890.24s] English:** reinforcement learning problem and uh some of the sort of more open-ended  
**Translation:** 

**[895.28s] English:** reformulations of that problem that have been explored in recent years so classically  
**Translation:** Vocabulary: reinforcement: 强化

**[898.74s] English:** reinforcement learning is framed as a problem of maximizing utility like any kind of rational  
**Translation:** 

**[903.52s] English:** ai agent and then anything you do is in service to maximizing that utility  
**Translation:** Vocabulary: maximizing: 最大化

**[907.38s] English:** but a very interesting kind of way to look at um i'm not necessarily saying this the best way to  
**Translation:** 

**[915.56s] English:** look at it but an interesting alternative way to look at these problems as um as something where  
**Translation:** 

**[919.78s] English:** you first get to explore the world however you please and then afterwards you will be tasked  
**Translation:** 

**[925.02s] English:** with doing something and that might suggest a somewhat different solution so if you don't know  
**Translation:** 

**[929.48s] English:** what you're going to be tasked with doing and you just want to prepare yourself optimally for  
**Translation:** 

**[933.10s] English:** whatever your uncertain future holds maybe then you will choose to attain some sort of coverage  
**Translation:** Vocabulary: optimally: 最佳地

**[938.48s] English:** build up sort of an arsenal of cognitive tools if you will such that later on when someone tells  
**Translation:** 

**[944.34s] English:** you now your job is to fetch the coffee for me you'll be well prepared to undertake that task  
**Translation:** Vocabulary: arsenal: 武器库; cognitive: 认知; undertake: 承担

**[948.92s] English:** and that you see that as the modern formulation of the reinforcement learning problem as a kind of  
**Translation:** 

**[955.02s] English:** the more multi-task the general intelligence kind of formulation  
**Translation:** 

**[960.00s] English:** I think that's one possible vision of where things might be headed.  
**Translation:** 

**[964.44s] English:** I don't think that's by any means the mainstream or standard way of doing things.  
**Translation:** 

**[968.10s] English:** And it's not like if I had to.  
**Translation:** 

**[969.80s] English:** But I like it.  
**Translation:** 

**[970.60s] English:** It's a beautiful vision.  
**Translation:** 

**[971.68s] English:** So maybe actually take a step back.  
**Translation:** 

**[974.10s] English:** What is the goal of robotics?  
**Translation:** 

**[976.56s] English:** What's the general problem robotics we're trying to solve?  
**Translation:** 

**[978.90s] English:** You actually kind of painted two pictures here.  
**Translation:** 

**[981.12s] English:** One of sort of the narrow, one of the general.  
**Translation:** 

**[983.22s] English:** What in your view is the big problem of robotics?  
**Translation:** 

**[986.44s] English:** Again, ridiculously philosophical high level questions.  
**Translation:** Vocabulary: philosophical: 哲学性的; ridiculously: 荒谬地

**[990.00s] English:** I think that, you know, maybe there are two ways I can answer this question.  
**Translation:** 

**[994.40s] English:** One is there's a very pragmatic problem, which is like what would make robots, what would sort of maximize the usefulness of robots?  
**Translation:** Vocabulary: maximize: 最大化; pragmatic: 实用的

**[1003.82s] English:** And there the answer might be something like a system where a system that can perform whatever task a human user sets for it.  
**Translation:** 

**[1017.02s] English:** You know, within the physical constraints, of course.  
**Translation:** Vocabulary: constraints: 物理限制

**[1019.24s] English:** If you tell it to teleport to another planet, it probably can't do that.  
**Translation:** 

**[1022.48s] English:** But if you ask it to do something that's within its physical capability, then potentially with a little bit of additional training or a little bit of additional trial and error, it ought to be able to figure it out in much the same way as like a human teleoperator ought to figure out how to drive the robot to do that.  
**Translation:** Vocabulary: capability: 能力; teleoperator: 远程操作员; teleport: 瞬间移动

**[1036.62s] English:** That's kind of a very pragmatic view of what it would take to kind of solve the robotics problem, if we will.  
**Translation:** 

**[1044.58s] English:** But I think that there is a second answer.  
**Translation:** 

**[1047.02s] English:** And that answer, that answer is a lot closer to why.  
**Translation:** 

**[1049.12s] English:** I want to work on robotics, which is that I think it's less about what it would take to do a really good job in the world of robotics, but more the other way around.  
**Translation:** 

**[1058.08s] English:** What robotics can bring to the table to help us understand artificial intelligence.  
**Translation:** 

**[1064.44s] English:** So your dream fundamentally is to understand intelligence.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[1069.10s] English:** Yes, I think that's the dream for many people who actually work in this space.  
**Translation:** 

**[1073.16s] English:** I think that there is there's something very pragmatic and very useful about studying robotics.  
**Translation:** 

**[1078.36s] English:** But I do think that a lot of people that go.  
**Translation:** 

**[1080.00s] English:** into this field actually uh you know the things that they draw inspiration from are the potential  
**Translation:** 

**[1086.04s] English:** for robots to like help us learn about intelligence and about ourselves so that's that's fascinating  
**Translation:** 

**[1092.38s] English:** that robotics is basically the space by which you can get closer to understanding the fundamentals  
**Translation:** Vocabulary: fundamentals: 基本原理

**[1099.00s] English:** of artificial intelligence so what is it about robotics that's different from some of the other  
**Translation:** 

**[1104.76s] English:** approaches so if we look at some of the early breakthroughs in deep learning or in the computer  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[1109.72s] English:** vision space and natural language processing there's really nice clean benchmarks that a lot  
**Translation:** 

**[1115.20s] English:** of people competed on and thereby came up with a lot of brilliant ideas what's the fundamental  
**Translation:** Vocabulary: benchmarks: 参考标准

**[1119.08s] English:** difference to you between computer vision purely defined an image net and kind of the bigger  
**Translation:** 

**[1124.74s] English:** robotics problem so there are a couple of things uh one is that with robotics um you kind of have  
**Translation:** 

**[1131.98s] English:** um you kind of have to take away many of the crutches so you have to deal with with both the  
**Translation:** 

**[1138.20s] English:** the the particular  
**Translation:** Vocabulary: crutches: 辅助工具

**[1139.56s] English:** the particular  
**Translation:** 

**[1139.72s] English:** problems of perception control and so on but you also have to deal with the integration of those  
**Translation:** 

**[1143.28s] English:** things and uh you know classically we've always thought of the integration as kind of a separate  
**Translation:** 

**[1148.20s] English:** problem so a classic kind of modular engineering approach is that we solve the individual sub  
**Translation:** Vocabulary: modular: 模块化

**[1152.52s] English:** problems then wire them together and then the whole thing works um and one of the things that  
**Translation:** 

**[1156.90s] English:** we've been seeing over the last couple of decades is that well maybe studying the thing as a whole  
**Translation:** 

**[1161.76s] English:** might lead to just like very different solutions than if we were to study the parts and wire them  
**Translation:** 

**[1166.14s] English:** together so the integrative nature of robotics research  
**Translation:** Vocabulary: integrative: 综合的

**[1169.72s] English:** helps us see you know different perspectives on the problem uh another part of the answer is that  
**Translation:** 

**[1176.12s] English:** with robotics um it it casts a certain uh paradox into very clever relief so that this is  
**Translation:** Vocabulary: perspectives: 观点

**[1182.36s] English:** sometimes referred to as a morovics paradox the idea that in artificial intelligence things that  
**Translation:** 

**[1188.76s] English:** are very hard for people can be very easy for machines and vice versa things that are very easy  
**Translation:** Vocabulary: versa: 相互

**[1193.32s] English:** for people can be very hard for machines so you know uh integral and differential calculus is a  
**Translation:** 

**[1199.56s] English:** really good example of this by the way one of the things that i'm proud to say i guess is the  
**Translation:** Vocabulary: calculus: 微积分; differential: 微分; integral: 积分

**[1202.66s] English:** most up-to-date research and validation of the  
**Translation:** 

**[1229.12s] English:** theory is the fact that if you are a robot you can actually work incredibly well but you don't  
**Translation:** Vocabulary: validation: 验证

**[1229.20s] English:** be able to do as much as that you can and you have to be able to do it all at once and that's  
**Translation:** 

**[1229.26s] English:** is-  
**Translation:** 

**[1200.00s] English:** It's pretty difficult to learn for people, but if you program a computer to do it, it can derive derivatives and integrals for you all day long without any trouble.  
**Translation:** 

**[1208.12s] English:** Whereas some things like, you know, drinking from a cup of water, very easy for a person to do, very hard for a robot to deal with.  
**Translation:** Vocabulary: derivatives: 导数; integrals: 积分

**[1216.48s] English:** And sometimes when we see such blatant discrepancies, they give us a really strong hint that we're missing something important.  
**Translation:** 

**[1222.80s] English:** So if we really try to zero in on those discrepancies, we might find that little bit that we're missing.  
**Translation:** Vocabulary: blatant: 明显的; discrepancies: 差异

**[1227.78s] English:** And it's not that we need to make machines better or worse at math and better at drinking water, but just that by studying those discrepancies, we might find some new insight.  
**Translation:** 

**[1237.80s] English:** So that could be in any space.  
**Translation:** 

**[1240.26s] English:** It doesn't have to be robotics, but you're saying, I mean, it's kind of interesting that robotics seems to have a lot of those discrepancies.  
**Translation:** 

**[1249.24s] English:** So the Hans-Marva paradox is probably referring to the space of the physical interaction.  
**Translation:** 

**[1256.54s] English:** Like you said, objects.  
**Translation:** 

**[1257.78s] English:** Object manipulation, walking, all the kind of stuff we do in the physical world.  
**Translation:** Vocabulary: manipulation: 操作

**[1263.70s] English:** How do you make sense, if you were to try to disentangle the Marva paradox, like why is there such a gap in our intuition about it?  
**Translation:** 

**[1277.30s] English:** Why do you think manipulating objects is so hard from everything you've learned from applying reinforcement learning in this space?  
**Translation:** Vocabulary: disentangle: 解开; intuition: 直觉; manipulating: 操作; reinforcement: 强化

**[1285.70s] English:** Yeah.  
**Translation:** 

**[1286.08s] English:** I think that one reason.  
**Translation:** 

**[1288.78s] English:** Is maybe that for many of the other problems that we've studied in AI and computer science and so on, the notion of input, output and supervision is much, much cleaner.  
**Translation:** 

**[1302.38s] English:** So computer vision, for example, deals with very complex inputs, but it's comparatively a bit easier, at least up to some level of abstraction, to cast it as a very tightly supervised problem.  
**Translation:** Vocabulary: abstraction: 抽象; comparatively: 相对而言; supervised: 监督; supervision: 监管

**[1314.46s] English:** It's comparatively much, much harder to cast robotic mechanics.  
**Translation:** 

**[1317.78s] English:** So I think manipulation has a very tightly supervised problem.  
**Translation:** 

**[1319.98s] English:** So I think manipulation has a very tightly supervised problem.  
**Translation:** 

**[1320.40s] English:** You can do it.  
**Translation:** 

**[1321.30s] English:** It just doesn't seem to work all that well.  
**Translation:** 

**[1323.30s] English:** So you could say that, well, maybe we get a labeled data set where we know exactly which  
**Translation:** 

**[1327.04s] English:** motor commands to send, and then we train on that.  
**Translation:** 

**[1329.12s] English:** But for various reasons, that's not actually such a great solution.  
**Translation:** 

**[1333.44s] English:** And it also doesn't seem to be even remotely similar to how people and animals learn to  
**Translation:** 

**[1337.50s] English:** do things, because we're not told by our parents, here's how you fire your muscles  
**Translation:** Vocabulary: remotely: 遥远地

**[1342.58s] English:** in order to walk.  
**Translation:** 

**[1344.38s] English:** We do get some guidance, but the really low-level detailed stuff, we figure out mostly on our  
**Translation:** 

**[1349.32s] English:** own.  
**Translation:** 

**[1349.54s] English:** And that's what you mean by tightly coupled, that every single little sub-action gets a  
**Translation:** 

**[1354.46s] English:** supervised signal of whether it's a good one or not.  
**Translation:** 

**[1357.12s] English:** Right.  
**Translation:** 

**[1357.52s] English:** So while in computer vision, you could sort of imagine up to a level of abstraction that  
**Translation:** 

**[1361.38s] English:** maybe somebody told you this is a car, and this is a cat, and this is a dog, in motor  
**Translation:** 

**[1365.66s] English:** control, it's very clear that that was not the case.  
**Translation:** 

**[1369.06s] English:** If we look at sort of the sub-spaces of robotics that, again, as you said, robotics integrates  
**Translation:** Vocabulary: integrates: 融合

**[1377.14s] English:** all of them together.  
**Translation:** 

**[1377.90s] English:** And then we get to see how this beautiful mess interplays.  
**Translation:** 

**[1380.94s] English:** So there's nevertheless still perception.  
**Translation:** 

**[1383.86s] English:** So it's the computer vision problem, broadly speaking, understanding the environment.  
**Translation:** 

**[1389.72s] English:** Then there's also, maybe you can correct me on this kind of categorization of the space.  
**Translation:** 

**[1394.16s] English:** Then there's prediction in trying to anticipate what things are going to do into the future  
**Translation:** Vocabulary: anticipate: 预知; categorization: 分类

**[1400.44s] English:** in order for you to be able to act in that world.  
**Translation:** 

**[1404.42s] English:** And then there's also this game theoretic aspect.  
**Translation:** Vocabulary: theoretic: 理论的

**[1407.90s] English:** The game theoretic aspect of how your actions will change the behavior of others.  
**Translation:** 

**[1413.92s] English:** In this kind of space, and this is bigger than reinforcement learning.  
**Translation:** Vocabulary: reinforcement: 强化学习

**[1418.16s] English:** This is just broadly looking at the problem in robotics.  
**Translation:** 

**[1420.82s] English:** What's the hardest problem here?  
**Translation:** 

**[1422.90s] English:** Or is what you said true that when you start to look at all of them together, that's a  
**Translation:** 

**[1432.42s] English:** whole other thing?  
**Translation:** 

**[1434.18s] English:** You can't even say which one individually is harder.  
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

**[1440.00s] English:** them all together? I think when you look at them all together, some things actually become easier.  
**Translation:** 

**[1444.88s] English:** And I think that's actually pretty important. So we had, you know, back in 2014, we had  
**Translation:** 

**[1451.50s] English:** some work, basically our first work on end-to-end reinforcement learning for robotic manipulation  
**Translation:** 

**[1457.32s] English:** skills from vision, which, you know, at the time was something that seemed a little inflammatory  
**Translation:** Vocabulary: inflammatory: 激进; manipulation: 操作

**[1462.74s] English:** and controversial in the robotics world. But other than the inflammatory and controversial part of it,  
**Translation:** 

**[1469.14s] English:** the point that we were actually trying to make in that work is that for the particular case of  
**Translation:** 

**[1474.08s] English:** combining perception and control, you could actually do better if you treat them together  
**Translation:** 

**[1478.02s] English:** than if you try to separate them. And the way that we tried to demonstrate this is we picked,  
**Translation:** 

**[1481.96s] English:** you know, a fairly simple motor control task where a robot had to insert a little red trapezoid into  
**Translation:** 

**[1487.60s] English:** a trapezoidal hole. And we had our separated solution, which involved first detecting the  
**Translation:** Vocabulary: detecting: 检测; insert: 插入; trapezoid: 梯形; trapezoidal: 梯形的

**[1493.54s] English:** hole using a pose detector and then actuating the arm to put it in. And then our end-to-end  
**Translation:** 

**[1498.28s] English:** solution, which just...  
**Translation:** Vocabulary: actuating: 驱动; detector: 检测器

**[1499.14s] English:** And one of the things we observed is that if you use the end-to-end solution,  
**Translation:** 

**[1505.62s] English:** essentially the pressure on the perception part of the model is actually lower. Like,  
**Translation:** 

**[1508.44s] English:** it doesn't have to figure out exactly where the thing is in 3D space. It just needs to figure out  
**Translation:** 

**[1512.28s] English:** where it is, you know, distributing the errors in such a way that the horizontal difference matters  
**Translation:** Vocabulary: horizontal: 水平方向

**[1517.48s] English:** more than the vertical difference, because vertically it just pushes it down all the way  
**Translation:** 

**[1520.46s] English:** until it can't go any further. And there, perceptual errors are a lot less harmful,  
**Translation:** Vocabulary: perceptual: 感知上的; vertical: 垂直的; vertically: 垂直地

**[1524.44s] English:** whereas perpendicular to the direction of motion, perceptual errors are much more harmful.  
**Translation:** 

**[1528.34s] English:** So, the point is that if you combine these two things, you can trade off errors between the  
**Translation:** Vocabulary: perpendicular: 垂直

**[1533.70s] English:** components optimally to best accomplish the task, and the components can actually be weaker  
**Translation:** 

**[1539.32s] English:** while still leading to better overall performance.  
**Translation:** Vocabulary: optimally: 最优化地

**[1541.94s] English:** That's a profound idea. I mean, in the space of pegs and things like that, it's quite simple.  
**Translation:** 

**[1548.40s] English:** It almost is tempting to overlook, but that seems to be, at least intuitively, an idea that should  
**Translation:** Vocabulary: intuitively: 直觉上; overlook: 忽略; profound: 深奥

**[1555.98s] English:** generalize to basically all aspects.  
**Translation:** 

**[1558.34s] English:** So, perception and control.  
**Translation:** Vocabulary: generalize: 泛化

**[1560.00s] English:** Of course.  
**Translation:** 

**[1560.56s] English:** That one strengthens the other.  
**Translation:** 

**[1561.98s] English:** Yeah, and people who have studied sort of perceptual heuristics in humans and animals find things like that all the time.  
**Translation:** 

**[1568.78s] English:** So one very well-known example is something called the gaze heuristic, which is a little trick that you can use to intercept a flying object.  
**Translation:** Vocabulary: heuristic: 启发法; heuristics: 启发法; intercept: 拦截

**[1577.22s] English:** So if you want to catch a ball, for instance, you could try to localize it in 3D space, estimate its velocity, estimate the effect of wind resistance, solve a complex system of differential equations in your head.  
**Translation:** 

**[1586.26s] English:** Or you can maintain a running speed so that the object stays in the same position as in your field of view.  
**Translation:** Vocabulary: differential: 微分方程; equations: 方程式

**[1593.90s] English:** So if it dips a little bit, you speed up.  
**Translation:** 

**[1595.52s] English:** If it rises a little bit, you slow down.  
**Translation:** 

**[1598.08s] English:** And if you follow the simple rule, you'll actually arrive at exactly the place where the object lands and you'll catch it.  
**Translation:** 

**[1602.80s] English:** And humans use it when they play baseball.  
**Translation:** 

**[1605.10s] English:** Human pilots use it when they fly airplanes to figure out if they're about to collide with somebody.  
**Translation:** 

**[1609.18s] English:** Frogs use this to catch insects and so on and so on.  
**Translation:** Vocabulary: collide: 相撞

**[1611.50s] English:** So this is something that actually happens in nature.  
**Translation:** 

**[1613.56s] English:** And I'm sure this is just one instance of it that we were able to.  
**Translation:** 

**[1616.26s] English:** Identify just because all the scientists were able to identify because it's so prevalent, but there are probably many others.  
**Translation:** 

**[1621.78s] English:** Do you have a, just so we can zoom in as we talk about robotics, do you have a canonical problem, sort of a simple, clean, beautiful representative problem in robotics that you think about when you're thinking about some of these problems?  
**Translation:** Vocabulary: canonical: 典范问题; prevalent: 普遍存在的

**[1635.84s] English:** We talked about robotic manipulation.  
**Translation:** 

**[1638.36s] English:** To me, that seems intuitively, at least the robotics community has converged towards that as a space.  
**Translation:** Vocabulary: converged: 汇聚; manipulation: 操作

**[1646.26s] English:** That's the canonical problem, if you agree, then maybe do you zoom in, in some particular aspect of that problem that you just like, like, if we solve that problem perfectly, it'll unlock a major step in towards human level intelligence.  
**Translation:** 

**[1664.08s] English:** I don't think I have like a really great answer to that.  
**Translation:** 

**[1666.14s] English:** And I think partly the reason I don't have a great answer kind of has to do with the, it has to do with the fact that the difficulty is really in the flexibility.  
**Translation:** 

**[1675.84s] English:** And adaptability, rather than in doing a particular thing, really, really.  
**Translation:** Vocabulary: adaptability: 适应性; flexibility: 灵活性

**[1680.00s] English:** well so um it's hard to just say like oh if you can i don't know like shuffle a deck of cards as  
**Translation:** 

**[1687.32s] English:** fast as like a vegas uh casino dealer then you'll you'll be very proficient it's really the ability  
**Translation:** Vocabulary: casino: 赌场; proficient: 熟练; shuffle: 洗牌; vegas: 拉斯维加斯

**[1694.66s] English:** to quickly figure out how to do some arbitrary new thing well enough to like you know to move  
**Translation:** 

**[1703.98s] English:** on to the next arbitrary thing but the the source of newness and uncertainty have you found uh  
**Translation:** Vocabulary: arbitrary: 随意的

**[1711.68s] English:** problems in which it's easy to uh generate new newnessness this is yeah new types of newness  
**Translation:** 

**[1719.78s] English:** yeah so a few years ago uh so if you had asked me this question around like 2016 maybe i would  
**Translation:** Vocabulary: newnessness: 新颖性

**[1726.94s] English:** have probably said that robotic grasping is a really great uh example of that because it's a  
**Translation:** 

**[1731.98s] English:** task with great real world utility  
**Translation:** Vocabulary: grasping: 抓取

**[1733.66s] English:** like you will get a lot of money if you can do it well what is robotic grasping picking up any  
**Translation:** 

**[1739.66s] English:** object with a robotic hand exactly so you will get a lot of money if you do it well because  
**Translation:** 

**[1744.78s] English:** lots of people want to run warehouses with robots and it's highly non-trivial because  
**Translation:** 

**[1749.16s] English:** uh very different objects uh will require very different grasping strategies but actually since  
**Translation:** Vocabulary: warehouses: 仓库

**[1755.82s] English:** then people have gotten really good at building systems to solve this problem uh to the point  
**Translation:** 

**[1761.52s] English:** where i'm not actually sure how much more progress  
**Translation:** 

**[1763.64s] English:** we can make uh with that as like the main guiding uh thing but it's kind of interesting to see  
**Translation:** 

**[1770.70s] English:** the kind of methods that have actually worked well in that space because  
**Translation:** 

**[1773.86s] English:** robotic grasping classically used to be regarded very much as um kind of almost like a geometry  
**Translation:** 

**[1780.24s] English:** problem so uh people who have uh studied the history of computer vision will find this  
**Translation:** Vocabulary: geometry: 几何问题

**[1785.56s] English:** very familiar that it's kind of in the same way that in the early days of computer vision people  
**Translation:** 

**[1789.74s] English:** thought of it very much as like an inverse graphics thing in robotic grasping people  
**Translation:** Vocabulary: inverse: 逆向的

**[1793.64s] English:** thought of it as an inverse physics problem essentially you  
**Translation:** 

**[1796.76s] English:** you look at what's in front of you figure out the shapes then  
**Translation:** 

**[1800.00s] English:** and use your best estimate of the laws of physics to figure out where to put your fingers and you  
**Translation:** 

**[1803.92s] English:** pick up the thing. And it turns out that what works really well for robotic grasping instantiated in  
**Translation:** Vocabulary: instantiated: 实现

**[1809.26s] English:** many different recent works, including our own, but also ones from many other labs is to use  
**Translation:** 

**[1815.26s] English:** learning methods with some combination of either exhaustive simulation or like actual real world  
**Translation:** Vocabulary: exhaustive: 详尽; simulation: 模拟

**[1821.00s] English:** trial and error. And it turns out that those things actually work really well. And then you  
**Translation:** 

**[1824.08s] English:** don't have to worry about solving geometry problems or physics problems. So what are,  
**Translation:** 

**[1830.24s] English:** just by the way, in the grasping, what are the difficulties that have been worked on? So one is  
**Translation:** 

**[1836.06s] English:** like the materials of things, maybe occlusions and the perception side. Why is it such a difficult,  
**Translation:** Vocabulary: occlusions: 遮挡物

**[1842.26s] English:** why is picking stuff up such a difficult problem? Yeah, it's a difficult problem because the number  
**Translation:** 

**[1849.40s] English:** of things that you might have to deal with or the variety of things that you have to deal with is  
**Translation:** 

**[1853.14s] English:** extremely large.  
**Translation:** 

**[1854.60s] English:** And oftentimes things that work for one class of objects won't work for other classes of objects.  
**Translation:** Vocabulary: oftentimes: 经常

**[1860.22s] English:** So if you, if you get really good at picking up boxes and now you have to pick up plastic bags,  
**Translation:** 

**[1866.16s] English:** you know, you just need to employ a very different strategy. And there are many properties of objects  
**Translation:** 

**[1873.04s] English:** that are more than just their geometry. It has to do with, you know, the bits that, that are easier  
**Translation:** 

**[1878.30s] English:** to pick up, the bits that are hard to pick up, the bits that are more flexible, the bits that will  
**Translation:** 

**[1881.54s] English:** cause the thing to pivot and bend and drop.  
**Translation:** 

**[1884.08s] English:** So there's all these little details that come up, but the task is still kind of can be characterized  
**Translation:** 

**[1898.74s] English:** as one task. Like there's a very clear notion of you did it or you didn't do it.  
**Translation:** 

**[1903.80s] English:** So in terms of spilling things, there creeps in this notion that starts to sound and feel like  
**Translation:** Vocabulary: creeps: 慢慢出现

**[1911.14s] English:** common sense reasoning. Do you think,  
**Translation:** 

**[1914.08s] English:** solving the general problem of robotics requires  
**Translation:** 

**[1920.00s] English:** common sense reasoning requires general intelligence this kind of human level capability of  
**Translation:** 

**[1927.26s] English:** you know like you said be robust and deal with uncertainty but also be able to sort of reason  
**Translation:** Vocabulary: capability: 能力; robust: 健壮

**[1933.16s] English:** and assimilate different pieces of knowledge that you have um yeah what what are you what are your  
**Translation:** 

**[1940.56s] English:** thoughts on the needs of common sense reasoning in the space of uh the general robotics problem  
**Translation:** Vocabulary: assimilate: 吸收

**[1947.68s] English:** so i'm going to slightly dodge that question and say that i think i think maybe actually  
**Translation:** 

**[1951.94s] English:** it's the other way around is that studying robotics can help us understand how to put  
**Translation:** Vocabulary: dodge: 回避

**[1957.56s] English:** common sense into our ai systems one way to think about common sense is that and and why our current  
**Translation:** 

**[1964.14s] English:** systems might lack common sense is that common sense is a property is an emergent property of  
**Translation:** Vocabulary: emergent: 涌现的

**[1968.88s] English:** actually having to interact with a particular world a particular universe and get things done  
**Translation:** 

**[1974.94s] English:** in that universe so you might think that for instance if you're a robot you're going to have  
**Translation:** 

**[1977.68s] English:** an image captioning system uh maybe it looks at pictures of of the world and it types out  
**Translation:** 

**[1984.66s] English:** english sentences so it kind of it kind of deals with our world and then you can easily construct  
**Translation:** Vocabulary: captioning: 图片说明

**[1990.42s] English:** situations where image captioning systems do things that defy common sense like give it a  
**Translation:** 

**[1994.64s] English:** picture of a person wearing a fur coat and we'll say it's a teddy bear but i think what's really  
**Translation:** Vocabulary: teddy: 泰迪熊

**[1999.24s] English:** happening in those settings is that the system doesn't actually live in our world it lives in  
**Translation:** 

**[2004.50s] English:** its own world that consists of pixels and english sentences  
**Translation:** Vocabulary: pixels: 像素

**[2006.82s] English:** and doesn't actually consist of like you know having to put on a fur coat in the winter so you  
**Translation:** 

**[2011.60s] English:** don't get cold so perhaps the the reason for the disconnect is that the systems that we have now  
**Translation:** Vocabulary: disconnect: 联系中断

**[2018.66s] English:** simply inhabit a different universe and if we build ai systems that are forced to deal with  
**Translation:** 

**[2023.42s] English:** all of the messiness and complexity of our universe maybe they will have to acquire common  
**Translation:** Vocabulary: complexity: 复杂性; messiness: 混乱

**[2028.08s] English:** sense to essentially maximize their utility whereas the systems we're building now don't  
**Translation:** 

**[2033.02s] English:** have to do that they can take some shortcut  
**Translation:** Vocabulary: maximize: 最大化; shortcut: 捷径

**[2034.38s] English:** that's fascinating  
**Translation:** 

**[2036.82s] English:** you've a couple times already sort of reframed  
**Translation:** Vocabulary: reframed: 重新表述

**[2040.00s] English:** the role of robotics in this whole thing and for some reason i don't know if my way of thinking is  
**Translation:** 

**[2045.76s] English:** common but i thought like we need to understand and solve intelligence in order to solve robotics  
**Translation:** 

**[2051.74s] English:** and you're kind of framing it as no robotics is one of the best ways to just study artificial  
**Translation:** 

**[2057.96s] English:** intelligence and build sort of like robotics is like the right space in which you get to explore  
**Translation:** 

**[2065.54s] English:** some of the fundamental learning mechanisms fundamental sort of multi-modal multi-task  
**Translation:** 

**[2072.16s] English:** aggregation of knowledge mechanisms that are required for general intelligence that's really  
**Translation:** Vocabulary: aggregation: 聚合

**[2077.06s] English:** interesting way to think about it but let me ask about learning can the general sort of robotics  
**Translation:** 

**[2083.10s] English:** the epitome of the robotics problem be solved purely through learning perhaps end-to-end learning  
**Translation:** Vocabulary: epitome: 典范

**[2091.38s] English:** sort of learning from scratch as opposed to injecting  
**Translation:** 

**[2095.54s] English:** human expertise and rules and heuristics and so on i think that in terms of the spirit of the  
**Translation:** Vocabulary: heuristics: 启发式; injecting: 注入

**[2101.96s] English:** question i i would say yes uh i mean i think that though in some ways it's maybe like  
**Translation:** 

**[2108.22s] English:** an overly sharp dichotomy like you know i think that in some ways when we build algorithms we  
**Translation:** Vocabulary: dichotomy: 对立二分

**[2114.60s] English:** you know at some point a person does something like yeah there's always a person turned on the  
**Translation:** 

**[2120.60s] English:** computer a person uh uh you know implemented uh tensorflow  
**Translation:** 

**[2124.68s] English:** uh  
**Translation:** 

**[2125.54s] English:** but yeah i think that in terms of in terms of the point that you're getting and i do think the answer  
**Translation:** 

**[2129.84s] English:** is yes i think that i think that we can solve many problems that have previously required meticulous  
**Translation:** 

**[2136.20s] English:** manual engineering through automated optimization techniques and actually one thing i will say on  
**Translation:** Vocabulary: automated: 自动化; meticulous: 细致的; optimization: 优化

**[2141.18s] English:** this topic is i don't think this is actually a very radical or very new idea i think people  
**Translation:** 

**[2145.78s] English:** have uh have been thinking about automated optimization techniques as a way to do control  
**Translation:** 

**[2151.02s] English:** for a very very long time and in some ways i think that's a very radical or very new idea  
**Translation:** 

**[2155.54s] English:** and in some ways i think that's a very radical or very new idea because what's changed is really more the name  
**Translation:** 

**[2157.84s] English:** because what's changed is really more the name so you know today we would say that oh  
**Translation:** 

**[2159.84s] English:** so you know today we would say that oh  
**Translation:** 

**[2160.00s] English:** my robot does machine learning, it does reinforcement learning, maybe in the 1960s,  
**Translation:** 

**[2164.72s] English:** you'd say, oh, my robot is doing optimal control. And maybe the difference between typing out a  
**Translation:** Vocabulary: optimal: 最优化; reinforcement: 强化学习

**[2170.56s] English:** system of differential equations and doing feedback linearization versus training in  
**Translation:** 

**[2175.08s] English:** neural net, maybe it's not such a large difference. It's just pushing the optimization  
**Translation:** Vocabulary: differential: 微分方程

**[2179.34s] English:** deeper and deeper into the thing. Well, it's interesting you think that way,  
**Translation:** 

**[2183.90s] English:** but especially with deep learning, that the accumulation of experiences in data form  
**Translation:** Vocabulary: accumulation: 积累

**[2191.34s] English:** to form deep representations starts to feel like knowledge as opposed to optimal control.  
**Translation:** 

**[2199.40s] English:** So this feels like there's an accumulation of knowledge through the learning process.  
**Translation:** 

**[2203.06s] English:** Yes. Yeah. So I think that is a good point, that one big difference between learning-based systems  
**Translation:** 

**[2207.94s] English:** and classic optimal control systems is that learning-based systems in principle should  
**Translation:** 

**[2212.36s] English:** get better and better the more they do.  
**Translation:** 

**[2213.90s] English:** Right. And I do think that that's actually a very, very powerful difference.  
**Translation:** 

**[2218.12s] English:** So if we look back at the world of expert systems and symbolic AI and so on, of using logic to  
**Translation:** 

**[2225.36s] English:** accumulate expertise, human expertise, human-encoded expertise, do you think that will  
**Translation:** Vocabulary: accumulate: 累积; symbolic: 符号化的

**[2231.90s] English:** have a role at some point? Deep learning, machine learning, reinforcement learning has shown  
**Translation:** 

**[2238.20s] English:** incredible results and breakthroughs and just inspired thousands,  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[2243.90s] English:** maybe millions of researchers. But there's this less popular now, but it used to be a popular  
**Translation:** 

**[2251.66s] English:** idea of symbolic AI. Do you think that will have a role?  
**Translation:** 

**[2255.28s] English:** I think in some ways, the descendants of symbolic AI actually already have a role. So  
**Translation:** 

**[2264.84s] English:** this is the highly biased history from my perspective. You say that, well,  
**Translation:** Vocabulary: descendants: 后代

**[2269.96s] English:** initially we thought that rational decision-making involves logical  
**Translation:** 

**[2273.88s] English:** manipulation. So you have some model of the world expressed in terms of logic. You have  
**Translation:** Vocabulary: manipulation: 操控

**[2280.00s] English:** have some query, like what action do I take in order for x to be true? And then you manipulate  
**Translation:** 

**[2285.42s] English:** your logical symbolic representation to get an answer. What that turned into somewhere in the  
**Translation:** Vocabulary: manipulate: 操控

**[2289.82s] English:** 1990s is, well, instead of building kind of predicates and statements that have true or false  
**Translation:** 

**[2295.76s] English:** values, we'll build probabilistic systems where things have probabilities associated and  
**Translation:** Vocabulary: predicates: 谓词; probabilistic: 概率的; probabilities: 概率

**[2301.94s] English:** probabilities of being true and false, and that turned into Bayes nets. And that provided sort of  
**Translation:** 

**[2306.18s] English:** a boost to what were really still essentially logical inference systems, just probabilistic  
**Translation:** Vocabulary: inference: 推理

**[2311.16s] English:** logical inference systems. And then people said, well, let's actually learn the individual  
**Translation:** 

**[2317.02s] English:** probabilities inside these models. And then people said, well, let's not even specify the nodes in  
**Translation:** 

**[2322.38s] English:** the models. Let's just put a big neural net in there. But in many ways, I see these as actually  
**Translation:** 

**[2326.86s] English:** kind of descendants from the same idea. It's essentially instantiating rational decision  
**Translation:** Vocabulary: instantiating: 实例化; neural: 神经

**[2330.70s] English:** making by means of some inference process and learning by means of an optimization process.  
**Translation:** 

**[2336.94s] English:** So in a sense, I would say, yes, it has a place. And in many ways, that place is, you know,  
**Translation:** Vocabulary: optimization: 优化过程

**[2342.82s] English:** it already holds that place. It's already in there. Yeah, it's just by different, it looks  
**Translation:** 

**[2347.36s] English:** slightly different than it was before. Yeah, but there are some things that we can think about  
**Translation:** 

**[2351.60s] English:** that make this a little bit more obvious. Like if I train a big neural net model to predict what  
**Translation:** 

**[2356.70s] English:** will happen in response to my robot's actions, and then I run probabilistic inference, meaning I  
**Translation:** 

**[2361.78s] English:** invert that model to figure out the actions that lead to some plausible outcome. Like, to me, that  
**Translation:** 

**[2366.18s] English:** is a kind of logic. You have a model of the world that just happens to be expressed by a neural net,  
**Translation:** Vocabulary: invert: 反向思考; plausible: 合乎情理

**[2371.10s] English:** and you are doing some inference procedure, some sort of manipulation on that model to figure out  
**Translation:** 

**[2377.88s] English:** the answer to a query that you have. It's the interpretability, it's the  
**Translation:** Vocabulary: interpretability: 可解释性

**[2381.66s] English:** explainability, though, that seems to be lacking more so because the nice thing about sort of expert  
**Translation:** 

**[2387.24s] English:** systems is you can follow the reasoning of the system that to us, mere humans is somehow compelling.  
**Translation:** Vocabulary: compelling: 有说服力的; explainability: 可解释性

**[2393.96s] English:** It would, it's just, I don't know what to make of this.  
**Translation:** 

**[2400.00s] English:** fact that uh there's a human desire for intelligence systems to be able to  
**Translation:** 

**[2406.16s] English:** convey in a poetic way to us why it made the decisions it did like tell a convincing story  
**Translation:** 

**[2415.04s] English:** and perhaps that's like um a silly human thing like we shouldn't expect that of intelligence  
**Translation:** 

**[2422.32s] English:** systems like we should be super happy that there's intelligent systems out there but uh  
**Translation:** 

**[2428.08s] English:** if i were to sort of psychoanalyze the researchers at the time i would say expert  
**Translation:** 

**[2433.20s] English:** systems connected to that part that desire of ai researchers for systems to be explainable  
**Translation:** 

**[2440.00s] English:** i mean maybe on that topic do you have a hope that sort of inferences of learning based  
**Translation:** Vocabulary: inferences: 推断

**[2448.00s] English:** systems will be as explainable as the dream was with expert systems for example  
**Translation:** 

**[2454.88s] English:** i think it's a very complicated question because i think that  
**Translation:** 

**[2458.08s] English:** some ways the question of explainability is um kind of very closely tied to the question of  
**Translation:** 

**[2465.04s] English:** of like performance like you know why do you want your system to explain itself well so that it's so  
**Translation:** 

**[2470.00s] English:** that when it screws up you can kind of figure out why it did it right but but in some ways that  
**Translation:** 

**[2475.60s] English:** that's a much bigger problem actually like your system might screw up and then it might screw up  
**Translation:** 

**[2480.56s] English:** in how it explains itself uh or you might have some bug somewhere so that it's not actually doing  
**Translation:** 

**[2488.08s] English:** it right and so i think that's a really good way to view that problem is really as a problem  
**Translation:** 

**[2491.84s] English:** as a bigger problem of verification and validation um of which explainability is sort of one component  
**Translation:** 

**[2499.20s] English:** i see i i just see it differently i see explainability you you put it beautifully  
**Translation:** Vocabulary: validation: 确认有效性; verification: 验证

**[2503.92s] English:** i think you actually summarize the field of explainability but to me there's another aspect  
**Translation:** 

**[2508.72s] English:** of explainability which is like storytelling that has nothing to do with errors or with like the  
**Translation:** Vocabulary: explainability: 解释性; storytelling: 讲故事; summarize: 总结

**[2518.08s] English:** it doesn't it uses errors  
**Translation:** 

**[2520.00s] English:** as as uh elements of its story as opposed to a fundamental need to be explainable when errors  
**Translation:** 

**[2527.06s] English:** occur it's just that for other intelligence systems to be in our world we seem to want to  
**Translation:** 

**[2532.40s] English:** tell each other stories and that that's true in the political world that's true in the academic world  
**Translation:** 

**[2539.02s] English:** and that i you know neural networks are less capable of doing that or perhaps they're equally  
**Translation:** 

**[2544.82s] English:** capable of storytelling storytelling maybe it doesn't matter what the fundamentals of the system  
**Translation:** Vocabulary: fundamentals: 基本原理; neural: 神经网络

**[2549.76s] English:** are you just need to be a good storyteller maybe one specific story i can tell you about  
**Translation:** 

**[2555.08s] English:** in that space is actually about some work that was done by by my former collaborator who's now  
**Translation:** Vocabulary: collaborator: 合作者; storyteller: 讲故事的人

**[2560.80s] English:** professor at mit named jacob andreas jacob actually works in natural language processing but he had  
**Translation:** 

**[2566.10s] English:** this idea to do a little bit of work in reinforcement learning and how on how natural language can  
**Translation:** Vocabulary: andreas: 雅各布; reinforcement: 强化学习

**[2571.44s] English:** basically structure the internals of policies trained with rl and one of the things he did is  
**Translation:** 

**[2577.52s] English:** he set up a model that  
**Translation:** Vocabulary: internals: 内部结构

**[2579.76s] English:** attempts to perform some task that's defined by a reward function but the model reads in a natural  
**Translation:** 

**[2585.52s] English:** language instruction so this is a pretty common thing to do in instruction following so you tell  
**Translation:** 

**[2589.46s] English:** it like you know go to the red house and then it's supposed to go to the red house but then one of the  
**Translation:** 

**[2594.12s] English:** things that jacob did is he treated that sentence not as a command from a person but as a representation  
**Translation:** 

**[2600.38s] English:** of the internal kind of uh state of the of the of the mind of this policy essentially so that when  
**Translation:** 

**[2606.94s] English:** it was faced with a new task what it would do is it would be able to do a little bit of a  
**Translation:** 

**[2609.76s] English:** task and then it would basically try to think of possible language descriptions attempt to do them  
**Translation:** 

**[2614.16s] English:** and see if they led to the right outcome so it would kind of think out loud like you know i'm  
**Translation:** 

**[2617.60s] English:** faced with this new task what am i going to do let me go to the red house oh that didn't work let me  
**Translation:** 

**[2621.44s] English:** go to the blue uh room or something let me go to the green plant and once it got some reward it  
**Translation:** 

**[2626.40s] English:** would say oh go to the green plant that's what's working i'm going to go to the green plant and  
**Translation:** 

**[2629.44s] English:** then you could look at the string that it came up with and that was a description of how it thought  
**Translation:** 

**[2632.56s] English:** it should solve the problem so you could do you could basically incorporate language as internal  
**Translation:** 

**[2637.92s] English:** state and you can start getting some handle on these kind of things so that's what jacob did so  
**Translation:** Vocabulary: incorporate: 合并

**[2639.76s] English:** you can start getting some handle on these kind of things so that's what jacob did so  
**Translation:** 

**[2640.00s] English:** things and then what i was kind of trying to get to is that also if you add to the reward function  
**Translation:** 

**[2645.86s] English:** the convincingness of that story so i have another reward signal of like  
**Translation:** 

**[2652.10s] English:** people who review that story how much they like it so that you know initially that could be a  
**Translation:** Vocabulary: convincingness: 说服力

**[2660.48s] English:** hyper parameter sort of hard-coded heuristic type of thing but it's an interesting notion of  
**Translation:** 

**[2666.20s] English:** the convincingness of the story becoming part of the reward function the objective function of the  
**Translation:** Vocabulary: heuristic: 启发式; hyper: 超; parameter: 参数

**[2672.80s] English:** explainability it's in the world of uh sort of twitter and fake news that might be a scary notion  
**Translation:** 

**[2678.84s] English:** that uh the the nature of truth may not be as important as the convincingness of the how  
**Translation:** Vocabulary: explainability: 可解释性

**[2685.18s] English:** convincing you are in telling the story around the facts well let me ask um the the basic question  
**Translation:** 

**[2694.46s] English:** you're one of the world  
**Translation:** 

**[2696.18s] English:** class researchers in reinforcement learning deep reinforcement learning  
**Translation:** 

**[2699.04s] English:** certainly in the robotic space what is reinforcement learning i think that  
**Translation:** Vocabulary: reinforcement: 强化学习

**[2704.88s] English:** what reinforcement learning refers to today is really just the uh uh kind of the modern  
**Translation:** 

**[2709.96s] English:** incarnation of learning-based control so classically reinforcement learning has a much  
**Translation:** Vocabulary: incarnation: 化身

**[2714.72s] English:** more narrow definition which is that it's you know literally learning from reinforcement like  
**Translation:** 

**[2719.12s] English:** the thing does something and then it gets a reward or punishment but really i think the way the term  
**Translation:** 

**[2723.80s] English:** is used today is it's used to reform  
**Translation:** 

**[2726.16s] English:** more broadly to learning-based control so some kind of system that's supposed to be controlling  
**Translation:** 

**[2730.98s] English:** something and it uses data to get better and what does control mean so this action is the fundamental  
**Translation:** 

**[2737.82s] English:** element yeah it means making rational decisions now and rational decisions are decisions that  
**Translation:** 

**[2742.50s] English:** maximize a measure of utility and sequentially so you made decisions time and time and time again  
**Translation:** 

**[2748.18s] English:** now like so it's easier to see that kind of idea in the space of maybe games in the space of robotics  
**Translation:** Vocabulary: maximize: 最大化; sequentially: 依次

**[2756.16s] English:** do you see it bigger than that is it applicable  
**Translation:** 

**[2760.00s] English:** Like, where are the limits of the applicability of reinforcement learning?  
**Translation:** Vocabulary: applicability: 适用范围

**[2764.52s] English:** Yeah, so rational decision-making is essentially the encapsulation of the AI problem viewed through a particular lens.  
**Translation:** 

**[2773.02s] English:** So any problem that we would want a machine to do, an intelligent machine, can likely be represented as a decision-making problem.  
**Translation:** Vocabulary: encapsulation: 封装

**[2780.50s] English:** Classifying images is a decision-making problem, although not a sequential one, typically.  
**Translation:** 

**[2785.44s] English:** You know, controlling a chemical plant is a decision-making problem.  
**Translation:** Vocabulary: sequential: 顺序的

**[2790.00s] English:** Deciding what videos to recommend on YouTube is a decision-making problem.  
**Translation:** 

**[2793.64s] English:** And one of the really appealing things about reinforcement learning is, if it does encapsulate the range of all these decision-making problems,  
**Translation:** Vocabulary: appealing: 吸引人的; encapsulate: 概括

**[2801.80s] English:** perhaps working on reinforcement learning is, you know, one of the ways to reach a very broad swath of AI problems.  
**Translation:** 

**[2809.86s] English:** But what is the fundamental difference between reinforcement learning and maybe supervised machine learning?  
**Translation:** Vocabulary: supervised: 监督学习; swath: 范围

**[2817.76s] English:** So reinforcement learning can be...  
**Translation:** 

**[2820.00s] English:** It can be viewed as a generalization of supervised machine learning.  
**Translation:** Vocabulary: generalization: 泛化; reinforcement: 强化

**[2822.54s] English:** You can certainly cast supervised learning as a reinforcement learning problem.  
**Translation:** 

**[2825.66s] English:** You can just say your loss function is the negative of your reward.  
**Translation:** 

**[2828.74s] English:** But you have stronger assumptions.  
**Translation:** 

**[2830.18s] English:** You have the assumption that someone actually told you what the correct answer was, that your data was IID and so on.  
**Translation:** Vocabulary: assumption: 假设; assumptions: 假设

**[2836.02s] English:** So you could view reinforcement learning as essentially relaxing some of those assumptions.  
**Translation:** 

**[2840.34s] English:** Now, that's not always a very productive way to look at it, because if you actually have a supervised learning problem,  
**Translation:** 

**[2844.26s] English:** you'll probably solve it much more effectively by using supervised learning methods, because it's easier.  
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
**Translation:** Vocabulary: mathematical: 数学的

**[2858.64s] English:** But it seems that reinforcement learning, the kind of tools we bring to the table today, of today,  
**Translation:** 

**[2864.30s] English:** so maybe down the line, everything will be a reinforcement learning problem.  
**Translation:** 

**[2868.90s] English:** Just like you said, image classification should be mapped to a reinforcement learning problem.  
**Translation:** 

**[2873.60s] English:** But today, the tools and ideas, the way we think about them are different.  
**Translation:** 

**[2878.98s] English:** Sort of...  
**Translation:** 

**[2880.00s] English:** supervised learning has been used very effectively to solve basic narrow ai problems  
**Translation:** 

**[2886.04s] English:** reinforcement learning kind of represents the dream of ai it's very much so in the research  
**Translation:** 

**[2893.86s] English:** space now in sort of captivating the imagination of people of what we can do with intelligent  
**Translation:** 

**[2899.06s] English:** systems but it hasn't yet had as wide of an impact as the supervised learning approaches  
**Translation:** 

**[2904.90s] English:** so that so that my question comes from the more practical sense like what do you see is the gap  
**Translation:** 

**[2911.84s] English:** between the more general reinforcement learning and the very specific yes it's sequential decision  
**Translation:** 

**[2918.44s] English:** making with one sequence one step in the sequence of the supervised learning so from a practical  
**Translation:** Vocabulary: sequential: 顺序的

**[2924.00s] English:** standpoint i think that one one thing that is uh you know potentially a little tough now and this  
**Translation:** 

**[2929.66s] English:** is i think something that we'll see this is a gap that we might see closing over the next couple of  
**Translation:** Vocabulary: standpoint: 立场

**[2933.80s] English:** years  
**Translation:** 

**[2934.04s] English:** is  
**Translation:** 

**[2934.88s] English:** the ability of reinforcement learning algorithms to effectively utilize  
**Translation:** 

**[2938.30s] English:** large amounts of prior data so one of the reasons why it's a bit difficult today  
**Translation:** 

**[2942.86s] English:** to use reinforcement learning for all the things that we might want to use it for  
**Translation:** 

**[2946.68s] English:** is that in most of the settings where we want to do rational decision making  
**Translation:** Vocabulary: reinforcement: 强化

**[2951.16s] English:** it's a little bit tough to just deploy some policy that does crazy stuff and learns purely  
**Translation:** 

**[2957.62s] English:** through trial and error it's much easier to collect a lot of data a lot of logs of some  
**Translation:** Vocabulary: deploy: 部署

**[2962.56s] English:** other policy that you've got and then maybe you can use reinforcement learning to do that  
**Translation:** 

**[2964.88s] English:** you know if you can get a good policy out of that then you deploy it and let it kind of fine-tune a  
**Translation:** 

**[2969.26s] English:** little bit but algorithmically it's quite difficult to do that so i think that once we figure out how  
**Translation:** 

**[2974.86s] English:** to get reinforcement learning to bootstrap effectively from large data sets then we'll  
**Translation:** Vocabulary: algorithmically: 按照算法; bootstrap: 启动

**[2980.26s] English:** see a very very rapid growth in applications of these technologies so this is what's referred to  
**Translation:** 

**[2985.64s] English:** as off policy reinforcement learning or offline rl or batch rl and i think we're seeing a lot of  
**Translation:** 

**[2991.30s] English:** research right now that that's bringing us closer and closer to that  
**Translation:** 

**[2994.88s] English:** maybe paint the picture of the different methods she said uh off policy what's  
**Translation:** 

**[3000.00s] English:** value-based reinforcement learning? What's policy-based? What's model-based? What's off-policy,  
**Translation:** 

**[3004.46s] English:** on-policy? What are the different categories of reinforcement learning?  
**Translation:** 

**[3008.10s] English:** So one way we can think about reinforcement learning is that it's, in some very fundamental  
**Translation:** 

**[3013.98s] English:** way, it's about learning models that can answer kind of what-if questions. So what would happen  
**Translation:** 

**[3020.92s] English:** if I take this action that I hadn't taken before? And you do that, of course, from experience,  
**Translation:** 

**[3025.72s] English:** from data. And oftentimes you do it in a loop. So you build a model that answers these what-if  
**Translation:** Vocabulary: oftentimes: 经常

**[3030.38s] English:** questions, use it to figure out the best action you can take, and then go and try taking that  
**Translation:** 

**[3034.98s] English:** and see if the outcome agrees with what you predicted. So the different kinds of techniques  
**Translation:** 

**[3041.04s] English:** basically refer to different ways of doing it. So model-based methods answer a question of what  
**Translation:** 

**[3046.84s] English:** state you would get, basically what would happen to the world if you were to take a certain action.  
**Translation:** 

**[3050.78s] English:** Value-based methods, they answer the question of what value you would get, meaning what utility  
**Translation:** 

**[3055.44s] English:** you would get. And so you can do that in a loop. So model-based methods answer a question of  
**Translation:** 

**[3055.72s] English:** what value you would get. But in a sense, they're not really all that different because  
**Translation:** 

**[3059.26s] English:** they're both really just answering these what-if questions. Now, unfortunately for us,  
**Translation:** 

**[3064.84s] English:** with current machine learning methods, answering what-if questions can be really hard  
**Translation:** 

**[3067.98s] English:** because they are really questions about things that didn't happen. If you wanted to answer  
**Translation:** 

**[3073.18s] English:** what-if questions about things that did happen, you wouldn't need a learned model. You would just  
**Translation:** 

**[3076.00s] English:** repeat the thing that worked before. And that's really a big part of why RL is a little bit tough.  
**Translation:** 

**[3083.40s] English:** So if you have a purely  
**Translation:** 

**[3085.18s] English:** on-premise model, you don't have to answer a lot of questions about things that didn't happen.  
**Translation:** 

**[3085.70s] English:** So if you have a purely on-premise model, you don't have to answer a lot of questions about things that didn't happen.  
**Translation:** 

**[3085.72s] English:** Then you go and try doing those mistaken things.  
**Translation:** 

**[3093.44s] English:** And then you observe the counterexamples  
**Translation:** 

**[3095.34s] English:** that will teach you not to do those things again.  
**Translation:** Vocabulary: counterexamples: 反例

**[3097.48s] English:** If you have a bunch of off-policy  
**Translation:** 

**[3099.44s] English:** data and you just want to synthesize  
**Translation:** Vocabulary: synthesize: 合成

**[3101.28s] English:** the best policy you can out of that data,  
**Translation:** 

**[3103.66s] English:** then you really have to deal with  
**Translation:** 

**[3105.10s] English:** the challenges of making these  
**Translation:** 

**[3107.08s] English:** counterfactual queries.  
**Translation:** Vocabulary: counterfactual: 假设情况的

**[3108.10s] English:** First of all, what's a policy?  
**Translation:** 

**[3110.16s] English:** A policy is  
**Translation:** 

**[3111.66s] English:** a model or some  
**Translation:** 

**[3114.12s] English:** kind of function that maps,  
**Translation:** 

**[3115.64s] English:** from observations of the world to actions.  
**Translation:** 

**[3120.00s] English:** So in reinforcement learning, we often refer to the current configuration of the world as the state.  
**Translation:** Vocabulary: configuration: 状态; reinforcement: 强化

**[3126.22s] English:** So we say the state kind of encompasses everything you need to fully define where the world is at at the moment.  
**Translation:** 

**[3131.22s] English:** And depending on how we formulate the problem, we might say you either get to see the state or you get to see an observation, which is some snapshot, some piece of the state.  
**Translation:** Vocabulary: encompasses: 包括一切; snapshot: 快照

**[3139.88s] English:** So policy just includes everything in it in order to be able to act in this world.  
**Translation:** 

**[3145.82s] English:** Yes.  
**Translation:** 

**[3146.02s] English:** And so what does off policy mean?  
**Translation:** 

**[3148.70s] English:** So the terms on policy and off policy refer to how you get your data.  
**Translation:** 

**[3153.48s] English:** So if you get your data from somebody else who was doing some other stuff, maybe you get your data from some manually programmed system that was just running in the world before.  
**Translation:** 

**[3164.46s] English:** That's referred to as off policy data.  
**Translation:** 

**[3166.42s] English:** But if you got the data by actually acting in the world based on what your current policy thinks is good, we call that on policy data.  
**Translation:** 

**[3172.90s] English:** And obviously on policy data is more useful to you because if your current policy makes some bad decisions.  
**Translation:** 

**[3178.70s] English:** You will actually see that those decisions are bad off policy data, however, might be much easier to obtain, because maybe that's all the log data that you have from before.  
**Translation:** 

**[3188.58s] English:** So we talk about offline talked about autonomous vehicles so you can envision off policy kind of approaches in robotic spaces where there's already a ton of robots out there, but they don't get the luxury of being able to explore based on reinforcement learning framework.  
**Translation:** Vocabulary: autonomous: 自主; envision: 想象

**[3206.14s] English:** So how do we make again open?  
**Translation:** 

**[3208.70s] English:** Question, but how do we make off policy methods work?  
**Translation:** 

**[3212.24s] English:** Yeah, so this is something that has been kind of a big open problem for a while, and in the last few years, people have made a little bit of progress on that.  
**Translation:** 

**[3221.70s] English:** You know, I can tell you about and it's not by any means solved yet, but I can tell you some of the things that, for example, we've done to try to address some of the challenges.  
**Translation:** 

**[3229.58s] English:** It turns out that one really big challenge with off policy reinforcement learning is that you can't really trust your models to give accurate predictions.  
**Translation:** 

**[3238.70s] English:** For any possible action.  
**Translation:** 

**[3240.00s] English:** So if I've never tried to, if in my data set I never saw somebody steering the car off the road onto the sidewalk, my value function or my model is probably not going to predict the right thing if I ask what would happen if I were to steer the car off the road onto the sidewalk.  
**Translation:** 

**[3255.50s] English:** So one of the important things you have to do to get off policy RL to work is you have to be able to figure out whether a given action will result in a trustworthy prediction or not.  
**Translation:** Vocabulary: steering: 方向盘操作

**[3264.88s] English:** And you can use kind of distribution estimation methods, kind of density estimation methods to try to figure that out.  
**Translation:** 

**[3272.20s] English:** So you could figure out that, well, this action, my model is telling me that it's great, but it looks totally different from any action I've taken before.  
**Translation:** Vocabulary: density: 密度; estimation: 估计

**[3277.96s] English:** So my model is probably not correct.  
**Translation:** 

**[3279.94s] English:** And you can incorporate regularization terms into your learning objective that will essentially tell you not to ask those questions that your model is unable to answer.  
**Translation:** Vocabulary: incorporate: 合并

**[3290.46s] English:** What would lead to breakthroughs in this space, do you think?  
**Translation:** 

**[3293.74s] English:** Like what's needed?  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[3295.20s] English:** Is this a data set question?  
**Translation:** 

**[3297.44s] English:** Do we need to collect big benchmark data sets that allow us to explore the space?  
**Translation:** Vocabulary: benchmark: 参考标准

**[3303.50s] English:** Is it a new kinds of methodologies?  
**Translation:** 

**[3308.32s] English:** Like what's your sense?  
**Translation:** Vocabulary: methodologies: 方法论

**[3309.70s] English:** Or maybe coming together in a space of robotics and defining the right problem to be working on?  
**Translation:** 

**[3314.62s] English:** I think for off policy reinforcement learning in particular, it's very much an algorithms question right now.  
**Translation:** Vocabulary: reinforcement: 强化

**[3319.36s] English:** And, you know, this is something that I think is great because an algorithms question is, you know,  
**Translation:** 

**[3324.30s] English:** that that just takes some very smart people to get together and think about it really hard.  
**Translation:** 

**[3328.98s] English:** Whereas if it was like a data problem or a hardware problem, that would take some serious engineering.  
**Translation:** 

**[3334.62s] English:** So that's why I'm pretty excited about that problem, because I think that we're in a position where we can make some real progress on it just by coming up with the right algorithms in terms of which algorithms they could be, you know, the problems at their core are very related to problems in, you know, things like like causal inference.  
**Translation:** Vocabulary: inference: 推断

**[3351.20s] English:** Right.  
**Translation:** 

**[3351.42s] English:** Because what you're really dealing with is situations where.  
**Translation:** 

**[3354.30s] English:** You have a model, a statistical model that's trying to make predictions about things that I hadn't seen before.  
**Translation:** 

**[3360.00s] English:** And if it's a model that's generalizing properly, that'll make good predictions.  
**Translation:** Vocabulary: generalizing: 泛化

**[3364.46s] English:** If it's a model that picks up on spurious correlations, that will not generalize properly.  
**Translation:** 

**[3368.92s] English:** And then you have an arsenal of tools you could use.  
**Translation:** Vocabulary: arsenal: 武器库; correlations: 相关性; generalize: 泛化; spurious: 虚假的

**[3371.12s] English:** You could, for example, figure out what are the regions where it's trustworthy.  
**Translation:** 

**[3374.44s] English:** Or, on the other hand, you could try to make it generalize better somehow, or some combination of the two.  
**Translation:** 

**[3380.44s] English:** Is there room for mixing, sort of, where most of it, like 90-95% is off policy?  
**Translation:** 

**[3389.52s] English:** You already have the data set.  
**Translation:** 

**[3391.28s] English:** And then you get to send the robot out to do a little exploration.  
**Translation:** 

**[3395.96s] English:** What's that role of mixing them together?  
**Translation:** 

**[3399.12s] English:** Yeah, absolutely.  
**Translation:** 

**[3399.82s] English:** I think that this is something that you actually described very well at the beginning of our discussion when you talked about the iceberg.  
**Translation:** Vocabulary: iceberg: 冰山一角

**[3407.24s] English:** This is the iceberg.  
**Translation:** 

**[3408.32s] English:** The 99% of your prior experience, that's your iceberg.  
**Translation:** 

**[3411.52s] English:** You'd use that for off-policy reinforcement learning.  
**Translation:** 

**[3413.70s] English:** And then, of course, if you've never opened that particular kind of door with that particular lock,  
**Translation:** 

**[3419.52s] English:** then you have to go out and fiddle with it a little bit.  
**Translation:** 

**[3422.12s] English:** And that's that additional 1% to help you figure out a new task.  
**Translation:** Vocabulary: fiddle: 调整

**[3425.18s] English:** And I think that's actually a pretty good recipe going forward.  
**Translation:** 

**[3428.26s] English:** Is this, to you, the most exciting space of reinforcement learning now?  
**Translation:** 

**[3432.84s] English:** Or is there...  
**Translation:** 

**[3433.50s] English:** And maybe taking a step back, not just now, but what, to you, is the most beautiful idea?  
**Translation:** 

**[3440.08s] English:** I apologize for the romanticized question, but the beautiful idea or concept in reinforcement learning?  
**Translation:** 

**[3446.92s] English:** In general, I actually think...  
**Translation:** Vocabulary: reinforcement: 强化

**[3449.52s] English:** I think that one of the things that is a very beautiful idea in reinforcement learning  
**Translation:** 

**[3452.86s] English:** is just the idea that you can obtain a near-optimal control or a near-optimal policy  
**Translation:** 

**[3461.30s] English:** without actually having a complete model of the world.  
**Translation:** 

**[3465.60s] English:** This is, you know, it's something that feels perhaps kind of obvious  
**Translation:** 

**[3470.80s] English:** if you just hear the term reinforcement learning or you think about trial and error learning.  
**Translation:** 

**[3475.28s] English:** But from a controls perspective, it's a very weird thing because classically,  
**Translation:** 

**[3479.52s] English:** I don't think it's a very good idea.  
**Translation:** 

**[3480.00s] English:** You know, we think about engineered systems and controlling engineered systems as the problem of writing down some equations and then figuring out, given these equations, you know, basically solve for X, figure out the thing that maximizes its performance.  
**Translation:** Vocabulary: equations: 方程式; maximizes: 最大化

**[3496.22s] English:** And the theory of reinforcement learning actually gives us a mathematically principled framework to reason about, you know, optimizing some quantity when you don't actually know the equations that govern that system.  
**Translation:** 

**[3508.58s] English:** And to me, that actually seems kind of, you know, very elegant, not something that sort of becomes immediately obvious, at least in the mathematical sense.  
**Translation:** Vocabulary: mathematical: 数学的

**[3520.20s] English:** Does it make sense to you that it works at all?  
**Translation:** 

**[3523.38s] English:** Well, I think it makes sense when you take some time to think about it, but it is a little surprising.  
**Translation:** 

**[3528.68s] English:** Well, then taking a step into the more deeper representations, which is also very surprising.  
**Translation:** 

**[3538.42s] English:** Yeah.  
**Translation:** 

**[3538.58s] English:** The richness of the state space, the space of environments that this kind of approach can operate in.  
**Translation:** 

**[3546.26s] English:** Can you maybe say what is deep reinforcement learning?  
**Translation:** 

**[3550.72s] English:** Well, deep reinforcement learning simply refers to taking reinforcement learning algorithms and combining them with high capacity neural net representations, which is, you know, kind of, it might at first seem like a pretty arbitrary thing.  
**Translation:** 

**[3563.88s] English:** Just take these two components and stick them together.  
**Translation:** Vocabulary: arbitrary: 随意; neural: 神经

**[3566.12s] English:** But the reason that it's.  
**Translation:** 

**[3567.48s] English:** It's something that has become so important in recent years is that reinforcement learning, it kind of faces an exacerbated version of a problem that has faced many other machine learning techniques.  
**Translation:** Vocabulary: exacerbated: 加剧的; reinforcement: 强化学习

**[3579.92s] English:** So if you if we go back to, like, you know, the early 2000s or the late 90s, we'll see a lot of research on machine learning methods that have some very appealing mathematical properties like they reduce the convex optimization problems, for instance.  
**Translation:** 

**[3594.66s] English:** But they require very special inputs.  
**Translation:** Vocabulary: appealing: 吸引人的; convex: 凸的; optimization: 优化

**[3596.98s] English:** They require a representation of the input that is.  
**Translation:** 

**[3600.00s] English:** clean in some way, like, for example, clean in the sense that the classes in your multi-class  
**Translation:** 

**[3605.76s] English:** classification problem separate linearly. So they have some kind of good representation,  
**Translation:** 

**[3610.02s] English:** and we call this a feature representation. And for a long time, people were very worried about  
**Translation:** 

**[3614.22s] English:** features in the world of supervised learning because somebody had to actually build those  
**Translation:** 

**[3617.74s] English:** features. So you couldn't just take an image and plug it into your logistic regression or your  
**Translation:** Vocabulary: logistic: 逻辑; regression: 回归; supervised: 监督

**[3621.76s] English:** SVM or something. Someone had to take that image and process it using some handwritten code.  
**Translation:** 

**[3626.04s] English:** And then neural nets came along and they could actually learn the features. And suddenly we  
**Translation:** 

**[3630.92s] English:** could apply learning directly to the raw inputs, which was great for images, but it was even more  
**Translation:** 

**[3635.78s] English:** great for all the other fields where people hadn't come up with good features yet.  
**Translation:** 

**[3639.62s] English:** And one of those fields was actually reinforcement learning because in reinforcement learning,  
**Translation:** 

**[3642.98s] English:** the notion of features, if you don't use neural nets and you have to design your own features,  
**Translation:** 

**[3646.52s] English:** is very, very opaque. Like, it's very hard to imagine, like, let's say I'm playing chess or  
**Translation:** 

**[3652.64s] English:** Go. What is a feature with which I can represent?  
**Translation:** Vocabulary: opaque: 不透明的

**[3656.04s] English:** The value function for Go or even the optimal policy for Go linearly. Like, I don't even know  
**Translation:** 

**[3661.76s] English:** how to start thinking about it. And people tried all sorts of things. They would write down, you  
**Translation:** Vocabulary: optimal: 最优的

**[3665.00s] English:** know, an expert chess player looks for whether the knight is in the middle of the board or not. So  
**Translation:** 

**[3669.20s] English:** that's a feature. Is knight in middle of board? And they would write these, like, long lists of  
**Translation:** 

**[3673.36s] English:** kind of arbitrary made up stuff. And that was really kind of getting us nowhere.  
**Translation:** 

**[3677.70s] English:** And that's a little, chess is a little more accessible than the robotics problem.  
**Translation:** 

**[3681.74s] English:** Absolutely.  
**Translation:** 

**[3682.32s] English:** Right. There's at least experts in the different features.  
**Translation:** 

**[3686.04s] English:** For chess. But still, like, the neural network there, to me, that's, I mean, you put it eloquently  
**Translation:** 

**[3694.44s] English:** and almost made it seem like a natural step to add neural networks. But the fact that neural  
**Translation:** Vocabulary: eloquently: 言辞优美; neural: 神经网络

**[3700.06s] English:** networks are able to discover features in the control problem, it's very interesting. It's  
**Translation:** 

**[3705.68s] English:** hopeful. I'm not sure what to think about it, but it feels hopeful that the control problem has  
**Translation:** 

**[3711.92s] English:** features to be learned. Like,  
**Translation:** 

**[3716.04s] English:** I guess my question is, is it surprising to you how far  
**Translation:** 

**[3720.00s] English:** the deep side of deep reinforcement learning was able to like what the space of problems has been  
**Translation:** 

**[3725.12s] English:** able to tackle from especially in games with with the alpha star and and uh alpha zero and just the  
**Translation:** Vocabulary: alpha: 阿尔法; reinforcement: 强化

**[3734.70s] English:** the representation power there and in the robotic space and what what is your sense of the limits of  
**Translation:** 

**[3741.88s] English:** this representation power and the control context i think that in regard to the limits uh that here  
**Translation:** 

**[3749.74s] English:** i think that one thing that makes it a little hard to fully answer this question is because um  
**Translation:** 

**[3756.92s] English:** in settings where we would like to push push these things to the limit we encounter other bottlenecks  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[3763.38s] English:** so like the reason that i can't get uh my robot to learn how to like i don't know do the dishes  
**Translation:** 

**[3771.88s] English:** in the kitchen it's not because its neural net is not big enough it's because when you try to  
**Translation:** 

**[3778.02s] English:** actually do trial and error and try to do trial and error and try to do trial and error and try to  
**Translation:** 

**[3779.72s] English:** and error learning, reinforcement learning directly in the real world where you have the  
**Translation:** 

**[3784.78s] English:** potential to gather these large, highly varied and complex data sets, you start running into  
**Translation:** 

**[3790.52s] English:** other problems. Like one problem you run into very quickly, it'll first sound like a very pragmatic  
**Translation:** Vocabulary: pragmatic: 实用导向的

**[3796.44s] English:** problem, but it actually turns out to be a pretty deep scientific problem. Take the robot, put it in  
**Translation:** 

**[3800.24s] English:** your kitchen, have it try to learn to do the dishes with trial and error. It'll break all your dishes  
**Translation:** 

**[3803.96s] English:** and then we'll have no more dishes to clean. Now, you might think this is a very practical issue,  
**Translation:** 

**[3808.86s] English:** but there's something to this, which is that if you have a person trying to do this, a person will  
**Translation:** 

**[3812.86s] English:** have some degree of common sense. They'll break one dish, they'll be a little more careful with  
**Translation:** 

**[3816.00s] English:** the next one. And if they break all of them, they're going to go and get more or something  
**Translation:** 

**[3819.92s] English:** like that. So there's all sorts of scaffolding that comes very naturally to us for our learning  
**Translation:** 

**[3826.16s] English:** process. Like if I have to learn something through trial and error, I have the common sense to know  
**Translation:** Vocabulary: scaffolding: 辅助结构

**[3830.96s] English:** that I have to try multiple times. If I screw something up, I ask for help or I reset things  
**Translation:** 

**[3835.84s] English:** or something like that. And all of that is kind of outside of the  
**Translation:** 

**[3838.86s] English:** classic reinforcement.  
**Translation:** 

**[3840.00s] English:** learning problem formulation. There are other things that can also be categorized as  
**Translation:** Vocabulary: categorized: 归类

**[3845.24s] English:** kind of scaffolding, but are very important. Like, for example, where do you get your reward  
**Translation:** 

**[3848.66s] English:** function? If I want to learn how to pour a cup of water, well, how do I know if I've done it  
**Translation:** 

**[3854.44s] English:** correctly? Now, that probably requires an entire computer vision system to be built just to  
**Translation:** 

**[3858.40s] English:** determine that, and that seems a little bit inelegant. So there are all sorts of things like  
**Translation:** Vocabulary: inelegant: 不优雅

**[3862.70s] English:** this that start to come up when we think through what we really need to get reinforcement learning  
**Translation:** 

**[3866.40s] English:** to happen at scale in the real world, and many of these things actually suggest a little bit of a  
**Translation:** Vocabulary: reinforcement: 强化

**[3871.50s] English:** shortcoming in the problem formulation and a few deeper questions that we have to resolve.  
**Translation:** 

**[3876.18s] English:** That's really interesting. I talked to, like, David Silver about AlphaZero, and it seems like  
**Translation:** Vocabulary: shortcoming: 缺点

**[3882.22s] English:** there's no, again, we haven't hit the limit at all in the context when there's no broken dishes.  
**Translation:** 

**[3889.82s] English:** So in the case of Go, it's really about just scaling compute. So  
**Translation:** 

**[3895.40s] English:** again, like, the bottleneck is the amount of money you're willing to invest in compute,  
**Translation:** 

**[3900.82s] English:** and then maybe the different, the scaffolding around how difficult it is to scale compute,  
**Translation:** Vocabulary: bottleneck: 瓶颈

**[3906.30s] English:** maybe. But there, there's no limit, and it's interesting. Now we move to the real world,  
**Translation:** 

**[3911.20s] English:** and there's the broken dishes, there's all the, and the reward function, like you mentioned,  
**Translation:** 

**[3916.16s] English:** that's really nice. So what, how do we push forward there? Do you think,  
**Translation:** 

**[3921.12s] English:** there's this kind of sample efficiency question that people,  
**Translation:** 

**[3925.40s] English:** bring up of, you know, not having to break 100,000 dishes. Is this an algorithm question?  
**Translation:** 

**[3932.64s] English:** Is this a data selection, like, question? What do you think? How do we, how do we not break  
**Translation:** Vocabulary: algorithm: 算法

**[3939.58s] English:** too many dishes? Yeah. Well, one way we can think about that is that  
**Translation:** 

**[3947.16s] English:** maybe we need to be better at reusing our data, building that iceberg. So perhaps,  
**Translation:** Vocabulary: iceberg: 数据宝库; reusing: 重复利用

**[3955.40s] English:** perhaps it's too much to hope that you can have a machine  
**Translation:** 

**[3960.00s] English:** that in isolation, in the vacuum, without anything else,  
**Translation:** Vocabulary: vacuum: 真空

**[3964.40s] English:** can just master complex tasks in minutes  
**Translation:** 

**[3967.28s] English:** the way that people do.  
**Translation:** 

**[3968.62s] English:** But perhaps it also doesn't have to.  
**Translation:** 

**[3969.82s] English:** Perhaps what it really needs to do  
**Translation:** 

**[3971.02s] English:** is have an existence, a lifetime,  
**Translation:** 

**[3973.50s] English:** where it does many things,  
**Translation:** 

**[3975.30s] English:** and the previous things that it has done  
**Translation:** 

**[3977.04s] English:** prepare it to do new things more efficiently.  
**Translation:** 

**[3980.08s] English:** And the study of these kinds of questions  
**Translation:** 

**[3982.94s] English:** typically falls under categories  
**Translation:** 

**[3984.38s] English:** like multitask learning or meta-learning,  
**Translation:** 

**[3987.06s] English:** but they all fundamentally deal  
**Translation:** Vocabulary: fundamentally: 本质上

**[3988.30s] English:** with the same general theme,  
**Translation:** 

**[3990.36s] English:** which is use experience for doing other things  
**Translation:** 

**[3994.02s] English:** to learn to do new things efficiently and quickly.  
**Translation:** 

**[3997.20s] English:** So what do you think about,  
**Translation:** Vocabulary: efficiently: 高效地

**[3998.94s] English:** if we just look at the one particular case study  
**Translation:** 

**[4001.26s] English:** of a Tesla autopilot that has quickly approaching  
**Translation:** 

**[4004.86s] English:** towards a million vehicles on the road,  
**Translation:** 

**[4007.48s] English:** where some percentage of the time,  
**Translation:** 

**[4009.54s] English:** 30, 40% of the time is driven using the computer vision,  
**Translation:** 

**[4013.68s] English:** multitask, hydranet, right?  
**Translation:** Vocabulary: multitask: 多任务处理

**[4017.80s] English:** And then the other percent,  
**Translation:** 

**[4019.70s] English:** that's what they call it, hydranet,  
**Translation:** Vocabulary: hydranet: 水管网

**[4022.70s] English:** the other percent is human controlled.  
**Translation:** 

**[4026.24s] English:** From the human side, how can we use that data?  
**Translation:** 

**[4029.80s] English:** What's your sense?  
**Translation:** 

**[4030.64s] English:** So like, what's the signal,  
**Translation:** 

**[4034.12s] English:** do you have ideas in this autonomous vehicle space  
**Translation:** 

**[4036.12s] English:** when people can lose their lives?  
**Translation:** Vocabulary: autonomous: 自主

**[4037.86s] English:** You know, it's a safety critical environment.  
**Translation:** 

**[4041.42s] English:** So how do we use that data?  
**Translation:** 

**[4043.88s] English:** So I think that actually the kind of problems,  
**Translation:** 

**[4046.96s] English:** So I think that actually the kind of problems,  
**Translation:** 

**[4047.66s] English:** that come up when we want systems that are reliable  
**Translation:** 

**[4050.66s] English:** that come up when we want systems that are reliable  
**Translation:** 

**[4053.66s] English:** and that can kind of understand the limits  
**Translation:** 

**[4055.32s] English:** of their capabilities,  
**Translation:** 

**[4056.66s] English:** they're actually very similar to the kind of problems  
**Translation:** 

**[4058.22s] English:** that come up when we're doing  
**Translation:** 

**[4059.72s] English:** off-policy reinforcement learning.  
**Translation:** 

**[4061.10s] English:** So as I mentioned before,  
**Translation:** Vocabulary: reinforcement: 强化

**[4061.98s] English:** in off-policy reinforcement learning,  
**Translation:** 

**[4063.68s] English:** the big problem is you need to know  
**Translation:** 

**[4066.16s] English:** when you can trust the predictions of your model,  
**Translation:** 

**[4068.28s] English:** because if you're trying to evaluate some pattern  
**Translation:** Vocabulary: evaluate: 评估

**[4071.46s] English:** of behavior for which your model  
**Translation:** 

**[4072.54s] English:** doesn't give you an accurate prediction,  
**Translation:** 

**[4074.04s] English:** then you shouldn't use that to modify your policy.  
**Translation:** 

**[4076.56s] English:** Then you shouldn't use that to modify your policy.  
**Translation:** 

**[4077.48s] English:** Which is very similar to the problem  
**Translation:** 

**[4078.52s] English:** that we're faced when we actually then  
**Translation:** 

**[4080.00s] English:** deploy that thing. And we want to decide whether we trust it in the moment or not. So perhaps we  
**Translation:** 

**[4085.82s] English:** just need to do a better job of figuring out that part. And that's a very deep research question,  
**Translation:** Vocabulary: deploy: 部署

**[4089.40s] English:** of course. But it's also a question that a lot of people are working on. So I'm pretty optimistic  
**Translation:** 

**[4092.46s] English:** that we can make some progress on that over the next few years. What's the role of simulation  
**Translation:** Vocabulary: optimistic: 乐观; simulation: 模拟

**[4096.96s] English:** in reinforcement learning, deep reinforcement learning, reinforcement learning? Like how  
**Translation:** 

**[4101.44s] English:** essential is it? It's been essential for the breakthroughs so far, for some interesting  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[4107.34s] English:** breakthroughs. Do you think it's a crutch that we rely on? I mean, again, this connects to our  
**Translation:** 

**[4113.32s] English:** off-policy discussion. But do you think we can ever get rid of simulation? Or do you think  
**Translation:** Vocabulary: crutch: 拐杖

**[4118.72s] English:** simulation will actually take over? Will it create more and more realistic simulations that will  
**Translation:** 

**[4122.36s] English:** allow us to solve actual real-world problems, like transfer the models we learn in simulation  
**Translation:** 

**[4128.10s] English:** to real-world problems? Yeah. I think that simulation is a very pragmatic tool that we  
**Translation:** 

**[4132.90s] English:** can use to get a lot of useful stuff to work right now. But I think that in the long run,  
**Translation:** Vocabulary: pragmatic: 实用的

**[4137.34s] English:** we will need to build machines that can learn from real data, because that's the only way that  
**Translation:** 

**[4142.68s] English:** we'll get them to improve perpetually. Because if we can't have our machines learn from real data,  
**Translation:** Vocabulary: perpetually: 永远地

**[4148.12s] English:** if they have to rely on simulated data, eventually the simulator becomes the bottleneck.  
**Translation:** 

**[4152.36s] English:** In fact, this is a general thing. If your machine has any bottleneck that is built by humans and  
**Translation:** Vocabulary: bottleneck: 瓶颈; simulated: 模拟; simulator: 模拟器

**[4158.02s] English:** that doesn't improve from data, it will eventually be the thing that holds it back.  
**Translation:** 

**[4162.96s] English:** And if you're entirely reliant on your simulator, that'll be the bottleneck. If you're entirely  
**Translation:** 

**[4166.34s] English:** reliant on a simulator, that'll be the bottleneck. If you're entirely reliant on a simulator, that'll  
**Translation:** 

**[4167.32s] English:** be the bottleneck. So simulation is very useful. It's very pragmatic, but it's not a substitute  
**Translation:** 

**[4174.74s] English:** for being able to utilize real experience. And this is, by the way, this is something that I  
**Translation:** 

**[4181.42s] English:** think is quite relevant now, especially in the context of some of the things we've discussed,  
**Translation:** 

**[4186.08s] English:** because some of these kind of scaffolding issues that I mentioned, things like the broken dishes  
**Translation:** 

**[4190.30s] English:** and the unknown reward function, these are not problems that you would ever stumble on  
**Translation:** Vocabulary: scaffolding: 辅助知识

**[4195.44s] English:** when working in a purely  
**Translation:** 

**[4196.96s] English:** simulated kind of environment. But they become very apparent when we try to  
**Translation:** 

**[4200.00s] English:** to actually run these things uh in the real world to throw a brief wrench into our discussion let  
**Translation:** 

**[4205.16s] English:** me ask do you think we're living in a simulation oh i have no idea do you think that's a useful  
**Translation:** Vocabulary: wrench: 干扰

**[4210.86s] English:** thing to even think about about the the the the fundamental physics nature of reality  
**Translation:** 

**[4216.86s] English:** or another perspective the reason i think the simulation hypothesis is interesting is it's to  
**Translation:** Vocabulary: hypothesis: 假设; simulation: 模拟

**[4224.74s] English:** think about how difficult is it to create sort of a virtual reality game type situation  
**Translation:** 

**[4232.16s] English:** that will be sufficiently convincing to us humans or sufficiently enjoyable that would we wouldn't  
**Translation:** Vocabulary: sufficiently: 足够地

**[4238.78s] English:** want to leave i mean that's actually a practical engineering challenge and i i personally really  
**Translation:** 

**[4244.90s] English:** enjoy virtual reality but it's quite far away but i kind of think about what would it take for me to  
**Translation:** 

**[4250.40s] English:** want to spend more time in virtual reality versus the real world  
**Translation:** 

**[4253.86s] English:** you  
**Translation:** 

**[4254.74s] English:** and that's a that's a sort of a nice clean question because at that point we've reached  
**Translation:** 

**[4262.00s] English:** if i want to live in a virtual reality that means we're just a few years away where majority of the  
**Translation:** 

**[4267.46s] English:** population lives in a virtual reality and that's how we create the simulation right you don't need  
**Translation:** 

**[4271.76s] English:** to actually simulate the you know the quantum gravity and just every aspect of the of the  
**Translation:** Vocabulary: gravity: 引力; simulate: 模拟

**[4279.30s] English:** universe and that's a that's an interesting question for reinforcement learning too  
**Translation:** 

**[4282.74s] English:** is if you want to make sufficiently  
**Translation:** Vocabulary: reinforcement: 强化

**[4284.74s] English:** realistic simulations that may it blend the difference between sort of the real world and  
**Translation:** 

**[4290.34s] English:** the simulation thereby just are the some of the things we've been talking about kind of the problems  
**Translation:** 

**[4296.86s] English:** go away if we can create actually interesting rich simulations it's an interesting question and it  
**Translation:** 

**[4301.80s] English:** actually i think your question casts your previous question to in a very interesting light because in  
**Translation:** 

**[4307.28s] English:** some ways asking whether we can um well the more the more kind of practical version of this like  
**Translation:** 

**[4313.86s] English:** you know can we build simulations and we can't do that in a very interesting way and i think that's  
**Translation:** 

**[4314.74s] English:** that's a great question i think i think this is a great question and it's a really good question  
**Translation:** 

**[4318.12s] English:** um i think we end up using a lot of like  
**Translation:** 

**[4320.00s] English:** world and it's kind of interesting to think about this about what this implies if true  
**Translation:** 

**[4325.80s] English:** it kind of implies that it's easier to create the universe than it is to create a brain  
**Translation:** 

**[4329.64s] English:** and that seems like put this way it seems kind of weird the aspect of the simulation  
**Translation:** 

**[4336.34s] English:** most interesting to me is the simulation of other humans that seems to be  
**Translation:** 

**[4342.08s] English:** a complexity that makes the robotics problem harder now i don't know if every robotics person  
**Translation:** 

**[4349.86s] English:** agrees with that notion just as a quick aside what are your thoughts about when the human  
**Translation:** 

**[4356.80s] English:** enters the picture of the robotics problem how does that change the reinforcement learning problem  
**Translation:** 

**[4361.92s] English:** the learning problem in general yeah i think that's a it's a kind of a complex question and  
**Translation:** 

**[4368.76s] English:** i guess my hope for a while had been that if we build these robotic learning systems that  
**Translation:** 

**[4377.04s] English:** that are multi-task that utilize lots of  
**Translation:** 

**[4379.86s] English:** prior data and that learn from their own experience the bit where they have to interact  
**Translation:** 

**[4384.48s] English:** with people will be perhaps handled in much the same way as all the other bits so if they have  
**Translation:** 

**[4389.24s] English:** prior experience of interacting with people and they can learn from their own experience of  
**Translation:** 

**[4393.20s] English:** interacting with people for this new task maybe that'll be enough now of course there if it's not  
**Translation:** 

**[4399.04s] English:** enough there are many other things we can do and there's quite a bit of research in that in that  
**Translation:** 

**[4401.96s] English:** area but i think it's worth a shot to see whether the uh the the multi-agent interaction the the  
**Translation:** 

**[4409.00s] English:** ability to understand the the the the the the the the the the the the the the the the the the the  
**Translation:** 

**[4409.84s] English:** that other beings in the world have their own goals intentions and thoughts and so on  
**Translation:** 

**[4415.70s] English:** whether that kind of understanding can emerge automatically from simply learning to do things  
**Translation:** 

**[4422.18s] English:** with and maximize utility that information arises from the data you've said something about gravity  
**Translation:** Vocabulary: gravity: 引力; maximize: 最大化

**[4428.86s] English:** sort of um that you don't need to explicitly inject anything into the system they can be  
**Translation:** 

**[4434.44s] English:** learned from the data and gravity is an example of something that could be learned from data  
**Translation:** Vocabulary: explicitly: 明确地

**[4438.50s] English:** sort of like the physics of the system  
**Translation:** 

**[4439.84s] English:** sort of like the physics of the system  
**Translation:** 

**[4440.00s] English:** world like what what are the limits of what we can learn from data do you really do you think  
**Translation:** 

**[4449.60s] English:** we can so uh a very simple clean way to ask that is do you really think we can learn gravity from  
**Translation:** 

**[4455.66s] English:** just data the idea the the laws of gravity so so something that i think is a common um kind of  
**Translation:** 

**[4463.18s] English:** pitfall when thinking about prior knowledge and learning is to assume that just because  
**Translation:** Vocabulary: pitfall: 陷阱

**[4470.04s] English:** we know something then that it's better to tell the machine about that rather than have it figure  
**Translation:** 

**[4475.48s] English:** it out on its own in many cases things that are important that affect many of the events that the  
**Translation:** 

**[4483.80s] English:** machine will experience are actually pretty easy to learn like you know if things if every time you  
**Translation:** 

**[4488.86s] English:** drop something it falls down like yeah you might not get the you know you might get kind  
**Translation:** 

**[4493.16s] English:** of the newton's version not einstein's version but it'll be pretty good and it will probably  
**Translation:** 

**[4497.44s] English:** be sufficient for you to act rationally in the world because you see the phenomenon all the time  
**Translation:** 

**[4503.10s] English:** so things that are readily apparent from the data we might not need to specify those by hand it  
**Translation:** 

**[4507.98s] English:** might actually be easier to let the machine figure them out it just feels like that there might be a  
**Translation:** 

**[4512.00s] English:** space of many local local minima in terms of theories of this world that we would discover  
**Translation:** 

**[4519.32s] English:** and get stuck on yeah of course newtonian  
**Translation:** Vocabulary: newtonian: 牛顿力学

**[4522.44s] English:** mechanical  
**Translation:** 

**[4523.16s] English:** is not necessarily easy to come by yeah and well in fact uh in in some fields of science for example  
**Translation:** 

**[4531.52s] English:** human civilizations that sell full of these local optima so for example if you uh think about how  
**Translation:** 

**[4536.32s] English:** people uh tried to figure out biology and medicine you know for the longest time the kind of rules  
**Translation:** 

**[4543.02s] English:** like the kind of uh principles that serve us very well in our day-to-day lives actually serve us  
**Translation:** 

**[4547.00s] English:** very poorly in understanding uh medicine and biology we had kind of very uh superstitious  
**Translation:** Vocabulary: superstitious: 迷信的

**[4552.46s] English:** and weird  
**Translation:** 

**[4553.16s] English:** ideas about how the body worked until the advent of the modern scientific method  
**Translation:** 

**[4556.72s] English:** so that does seem to be you know  
**Translation:** 

**[4560.00s] English:** a failing of this approach but it's also a failing of human intelligence arguably  
**Translation:** Vocabulary: arguably: 可以说

**[4562.96s] English:** maybe a small aside but some you know the idea of self-play is fascinating in reinforcement  
**Translation:** 

**[4569.52s] English:** learning sort of these competitive creating a competitive context in which agents can  
**Translation:** Vocabulary: reinforcement: 强化

**[4574.28s] English:** play against each other in uh sort of at the same skill level and thereby increasing  
**Translation:** 

**[4579.92s] English:** each other's skill level it seems to be this kind of self-improving mechanism  
**Translation:** 

**[4584.10s] English:** is exceptionally powerful in the context where it could be applied  
**Translation:** 

**[4587.84s] English:** first of all is that beautiful to you that this mechanism work as well as it does  
**Translation:** Vocabulary: exceptionally: 特别

**[4593.90s] English:** and also can be generalized to other contexts like in the robotic space or anything that's  
**Translation:** 

**[4601.94s] English:** applicable to the real world i think that um it's a very interesting idea and i but i suspect that  
**Translation:** Vocabulary: generalized: 泛化

**[4609.62s] English:** the bottleneck to actually generalizing it to the robotic setting is actually going to be the same  
**Translation:** 

**[4614.64s] English:** as as the bottleneck for everything else that  
**Translation:** Vocabulary: bottleneck: 瓶颈; generalizing: 泛化

**[4617.22s] English:** we need to  
**Translation:** 

**[4617.82s] English:** be able to build machines that can get better and better through natural interaction with the world  
**Translation:** 

**[4624.48s] English:** and once we can do that then they can go out and play with they can play with each other they can  
**Translation:** 

**[4628.76s] English:** play with people they can play with the natural environment uh but before we get there we've got  
**Translation:** 

**[4634.28s] English:** all these other problems we've got we have to get out of the way so there's no shortcut around that  
**Translation:** 

**[4637.72s] English:** you have to interact with a natural environment that well because in a in a self-play setting  
**Translation:** Vocabulary: shortcut: 捷径

**[4642.84s] English:** you still need a mediating mechanism so the the reason that um you know self-play  
**Translation:** 

**[4647.68s] English:** works for a board game is because the rules of that board game mediate the interaction between  
**Translation:** Vocabulary: mediate: 调解; mediating: 调节

**[4652.54s] English:** the agents so the kind of intelligent behavior that will emerge depends very heavily on the  
**Translation:** 

**[4657.38s] English:** nature of that mediating mechanism so on the side of reward functions that's uh coming up with good  
**Translation:** 

**[4663.30s] English:** reward function seems to be the thing that we associate with uh general intel like human beings  
**Translation:** 

**[4669.98s] English:** seem to value the idea of developing our own reward functions of uh you know arriving at meaning  
**Translation:** 

**[4676.66s] English:** and so on  
**Translation:** 

**[4677.68s] English:** yet for reinforcement learning we are  
**Translation:** 

**[4680.00s] English:** often kind of specify that's the given. What's your sense of how we develop good reward functions?  
**Translation:** 

**[4688.92s] English:** Yeah, I think that's a very complicated and very deep question. And you're completely right that  
**Translation:** 

**[4693.24s] English:** classically in reinforcement learning, this question has kind of been treated as a non-issue,  
**Translation:** 

**[4699.26s] English:** that you sort of treat the reward as this external thing that comes from some other bit  
**Translation:** Vocabulary: reinforcement: 强化

**[4704.80s] English:** of your biology, and you kind of don't worry about it. And I do think that that's actually  
**Translation:** 

**[4709.48s] English:** a little bit of a mistake that we should worry about it. And we can approach it in a few  
**Translation:** 

**[4714.24s] English:** different ways. We can approach it, for instance, by thinking of reward as a communication medium.  
**Translation:** 

**[4718.92s] English:** We can say, well, how does a person communicate to a robot what its objective is? You can approach  
**Translation:** 

**[4723.90s] English:** it also as sort of more of an intrinsic motivation medium. You could say, can we write down  
**Translation:** 

**[4729.56s] English:** kind of a general objective that leads to good capability? Like, for example, can you write down  
**Translation:** Vocabulary: capability: 能力; intrinsic: 内在的

**[4736.14s] English:** some objectives such that even in the absence of any other task, if you maximize the reward,  
**Translation:** 

**[4739.48s] English:** if you minimize that objective, you'll sort of learn useful things. This is something that has  
**Translation:** 

**[4744.34s] English:** sometimes been called unsupervised reinforcement learning, which I think is a really fascinating  
**Translation:** 

**[4748.38s] English:** area of research, especially today. We've done a bit of work on that recently. One of the things  
**Translation:** Vocabulary: unsupervised: 无监督的

**[4753.32s] English:** we've studied is whether we can have some notion of unsupervised reinforcement learning by means of  
**Translation:** 

**[4761.56s] English:** information theoretic quantities, like, for instance, minimizing a Bayesian measure of  
**Translation:** Vocabulary: bayesian: 贝叶斯的; minimizing: 最小化; theoretic: 理论的

**[4766.04s] English:** surprise. This is an idea that was, you know, pioneered actually in the  
**Translation:** 

**[4769.48s] English:** digital neuroscience community by folks like Carl Friston. And we've done some work recently that  
**Translation:** Vocabulary: neuroscience: 神经科学; pioneered: 开创

**[4774.00s] English:** shows that you can actually learn pretty interesting skills by essentially behaving  
**Translation:** 

**[4778.62s] English:** in a way that allows you to make accurate predictions about the world. It seems a little  
**Translation:** 

**[4782.88s] English:** circular, like do the things that will lead to you getting the right answer for prediction.  
**Translation:** 

**[4788.76s] English:** But you can, you know, by doing this, you can sort of discover stable niches in the world. You can  
**Translation:** Vocabulary: niches: 细分市场

**[4793.18s] English:** discover that if you're playing Tetris, then correctly, you know, clearing the rows will let  
**Translation:** 

**[4798.24s] English:** you play Tetris for longer.  
**Translation:** 

**[4799.48s] English:** Keep the board.  
**Translation:** 

**[4800.00s] English:** nice and clean, which sort of satisfies some desire for order in the world, and as a result,  
**Translation:** 

**[4804.80s] English:** get some degree of leverage over your domain. So we're exploring that pretty actively.  
**Translation:** 

**[4808.72s] English:** Is there a role for a human notion of curiosity in itself being the reward, sort of discovering  
**Translation:** Vocabulary: leverage: 影响力

**[4815.88s] English:** new things about the world? So one of the things that I'm pretty  
**Translation:** 

**[4820.80s] English:** interested in is actually whether discovering new things can actually be an emergent property  
**Translation:** Vocabulary: emergent: 涌现

**[4827.36s] English:** of some other objective that quantifies capability. So new things for the sake of new  
**Translation:** 

**[4832.40s] English:** things maybe might not by itself be the right answer, but perhaps we can figure out an objective  
**Translation:** 

**[4839.42s] English:** for which discovering new things is actually the natural consequence. That's something we're  
**Translation:** 

**[4844.84s] English:** working on right now, but I don't have a clear answer for you there yet that's still a work in  
**Translation:** 

**[4848.24s] English:** progress. You mean just that it's a curious observation to see sort of creative patterns  
**Translation:** 

**[4856.54s] English:** of curiosity?  
**Translation:** 

**[4857.36s] English:** On the way to optimize for a particular measure of capability.  
**Translation:** 

**[4865.02s] English:** Is there ways to understand or anticipate unexpected, unintended consequences of  
**Translation:** Vocabulary: anticipate: 预知; capability: 能力; optimize: 优化; unintended: 未预见的

**[4874.12s] English:** particular reward functions, sort of anticipate the kind of strategies that might be developed  
**Translation:** 

**[4881.64s] English:** and try to avoid highly detrimental strategies?  
**Translation:** 

**[4885.64s] English:** Yeah.  
**Translation:** 

**[4886.76s] English:** So.  
**Translation:** 

**[4887.36s] English:** Classically, this is something that has been pretty hard in reinforcement learning because it's  
**Translation:** 

**[4891.68s] English:** difficult for a designer to have good intuition about, you know, what a learning algorithm will  
**Translation:** Vocabulary: algorithm: 学习算法; intuition: 直觉; reinforcement: 强化

**[4895.68s] English:** come up with when they give it some objective. There are ways to mitigate that. One way to  
**Translation:** 

**[4900.48s] English:** mitigate it is to actually define an objective that says, like, don't do weird stuff. You can  
**Translation:** Vocabulary: mitigate: 减轻

**[4906.16s] English:** actually quantify it and say, just like, don't enter situations that have low probability under  
**Translation:** 

**[4911.52s] English:** the distribution of states you've seen before. It turns out that that's actually one very good way to  
**Translation:** 

**[4916.32s] English:** do off-policy reinforcement. It's a very good way to do off-policy reinforcement. It's a good way to  
**Translation:** 

**[4916.52s] English:** do off-policy reinforcement. It's a good way to do off-policy reinforcement. It's a good way to do  
**Translation:** 

**[4916.76s] English:** off-policy reinforcement. It's a good way to do off-policy reinforcement learning, actually.  
**Translation:** 

**[4919.32s] English:** So.  
**Translation:** 

**[4920.00s] English:** can do some things like that if we uh slowly venture in speaking about reward functions  
**Translation:** 

**[4926.72s] English:** into greater and greater levels of intelligence there's uh i mean steve russell thinks about this  
**Translation:** 

**[4932.42s] English:** the alignment of ai systems with us humans so how do we ensure that agi systems align with us humans  
**Translation:** 

**[4942.68s] English:** it's a it's kind of a reward function question of specifying the behavior of ai systems such that  
**Translation:** Vocabulary: align: 使一致; alignment: 对齐; specifying: 规定

**[4952.64s] English:** their success aligns with this with the broader intended success interest of human beings do you  
**Translation:** 

**[4960.46s] English:** have thoughts on this do you have kind of concerns of where reinforcement learning fits into this or  
**Translation:** Vocabulary: aligns: 一致

**[4965.34s] English:** are you really focused on the current moment of us being quite far away and trying to solve the  
**Translation:** 

**[4970.30s] English:** robotics problem i don't have a great answer  
**Translation:** 

**[4972.66s] English:** to this but um you know and i do think that this is a problem that's that's important to figure out  
**Translation:** 

**[4978.70s] English:** for my part i'm actually a bit more concerned about the other side of the of this equation that  
**Translation:** Vocabulary: equation: 方程

**[4984.56s] English:** uh you know maybe rather than unintended consequences for uh objectives that are  
**Translation:** 

**[4991.50s] English:** specified too well i'm actually more worried right now about unintended consequences for  
**Translation:** Vocabulary: specified: 指定; unintended: 未预见

**[4995.44s] English:** objectives that are not optimized well enough uh which might become a very pressing problem  
**Translation:** 

**[5000.76s] English:** when we for instance  
**Translation:** 

**[5002.30s] English:** you know  
**Translation:** 

**[5002.64s] English:** try to use these techniques for safety critical systems like cars and aircraft and so on i think  
**Translation:** 

**[5008.74s] English:** at some point we'll face the issue of objectives being optimized too well but right now i think  
**Translation:** 

**[5013.28s] English:** we're we're more likely to face the issue of them not being optimized well enough but you don't  
**Translation:** Vocabulary: optimized: 优化过度

**[5017.66s] English:** think unintended consequences can arise even when you're far from optimality sort of like on the  
**Translation:** 

**[5022.02s] English:** path to it oh no i think unintended consequences can absolutely arise it's just i think right now  
**Translation:** Vocabulary: optimality: 最佳状态

**[5027.90s] English:** the bottleneck for improving reliability safety and things like that  
**Translation:** 

**[5032.64s] English:** is more with systems that like need to work better that need to optimize their objective better  
**Translation:** Vocabulary: bottleneck: 瓶颈; optimize: 优化; reliability: 可靠性

**[5038.12s] English:** do you have thoughts  
**Translation:** 

**[5040.00s] English:** Do you have concerns about existential threats of human-level intelligence that if we put on our hat of looking in 10, 20, 100, 500 years from now, do you have concerns about existential threats of AI systems?  
**Translation:** Vocabulary: existential: 根本的

**[5055.38s] English:** I think there are absolutely existential threats for AI systems, just like there are for any powerful technology.  
**Translation:** 

**[5060.36s] English:** But I think that these kinds of problems can take many forms, and some of those forms will come down to people with nefarious intent.  
**Translation:** Vocabulary: nefarious: 邪恶的

**[5073.74s] English:** Some of them will come down to AI systems that have some fatal flaws, and some of them will, of course, come down to AI systems that are too capable in some way.  
**Translation:** 

**[5084.80s] English:** But among this set of potential concerns, I would actually be much more concerned about the future.  
**Translation:** 

**[5090.36s] English:** I'm more concerned about the first two right now, and principally the one with nefarious humans, because, you know, just through all of human history, actually, it's the nefarious humans that have been the problem, not the nefarious machines, than I am about the others.  
**Translation:** 

**[5101.48s] English:** And I think that right now, the best that I can do to make sure things go well is to, you know, build the best technology I can and also hopefully promote responsible use of that technology.  
**Translation:** Vocabulary: principally: 主要地

**[5113.44s] English:** Do you think RL systems has something to teach us humans?  
**Translation:** 

**[5118.30s] English:** You said nefarious humans.  
**Translation:** 

**[5120.36s] English:** Getting us in trouble.  
**Translation:** 

**[5121.14s] English:** I mean, machine learning systems have, in some ways, have revealed to us the ethical flaws in our data.  
**Translation:** 

**[5128.10s] English:** In that same kind of way, can reinforcement learning teach us about ourselves?  
**Translation:** 

**[5132.52s] English:** Has it taught something?  
**Translation:** Vocabulary: reinforcement: 强化学习

**[5134.28s] English:** What have you learned about yourself from trying to build robots and reinforcement learning systems?  
**Translation:** 

**[5142.66s] English:** I'm not sure what I've learned about myself, but maybe part of the answer to your question might be, you know, the fact that I'm a robot.  
**Translation:** 

**[5150.36s] English:** I'm not sure what I've learned about myself, but maybe part of the answer to your question might be, you know, that I'm a robot.  
**Translation:** 

**[5160.00s] English:** you know healthcare education social media etc and i think we will see some interesting stuff  
**Translation:** Vocabulary: healthcare: 医疗卫生

**[5165.48s] English:** emerge there uh we will see uh for instance what kind of behaviors these systems come up with  
**Translation:** 

**[5170.32s] English:** in situations where there is interaction with humans and uh and where they have you know  
**Translation:** 

**[5176.30s] English:** possibility of influencing human behavior i think we're not quite there yet but you know maybe in  
**Translation:** 

**[5181.10s] English:** the next few years we'll see some interesting stuff coming out in that area i hope outside  
**Translation:** 

**[5184.48s] English:** the research space because the the exciting space where this could be observed is uh sort of large  
**Translation:** 

**[5190.32s] English:** companies that deal with large data and i hope there's some transparency because and one of the  
**Translation:** 

**[5195.48s] English:** things that's unclear when i look at social networks and just online is why an algorithm  
**Translation:** 

**[5200.92s] English:** did something or whether you know even an algorithm was involved and that'd be interesting  
**Translation:** 

**[5206.20s] English:** as a from a research perspective just to uh to observe the results of algorithms  
**Translation:** 

**[5212.90s] English:** to open up  
**Translation:** 

**[5214.48s] English:** up that data to or to at least be sufficiently transparent about the behavior of these systems  
**Translation:** 

**[5219.68s] English:** in the real world what's your sense i don't know if you looked at the blog post bitter lesson  
**Translation:** Vocabulary: sufficiently: 足够地; transparent: 透明

**[5225.60s] English:** by everett sutton where it looks at sort of the big lesson of uh researching ai and in  
**Translation:** 

**[5233.84s] English:** reinforcement learning is that simple methods general methods that leverage computation seem  
**Translation:** Vocabulary: computation: 计算; leverage: 利用

**[5239.92s] English:** to work well so basically don't try to do any kind of fancy algorithms just wait for computation to  
**Translation:** 

**[5246.08s] English:** get fast do you share this kind of intuition i think the high level idea makes a lot of sense  
**Translation:** Vocabulary: intuition: 直觉

**[5254.16s] English:** i'm not sure that my takeaway would be that we don't need to work on algorithms i think that  
**Translation:** 

**[5258.56s] English:** my takeaway would be that we should work on general algorithms  
**Translation:** Vocabulary: takeaway: 收获

**[5263.44s] English:** and actually i think that this idea of needing to better automate  
**Translation:** 

**[5270.56s] English:** the acquisition of experience in the real world  
**Translation:** Vocabulary: automate: 自动化

**[5274.40s] English:** actually follows pretty naturally from rich sutton's conclusion so if the claim is  
**Translation:** 

**[5280.00s] English:** is that automated general methods  
**Translation:** Vocabulary: automated: 自动化

**[5283.12s] English:** plus data leads to good results,  
**Translation:** 

**[5286.18s] English:** then it makes sense that we should build general methods  
**Translation:** 

**[5288.12s] English:** and we should build the kind of methods  
**Translation:** 

**[5289.76s] English:** that we can deploy and get them to go out there  
**Translation:** Vocabulary: deploy: 部署

**[5291.52s] English:** and collect their experience autonomously.  
**Translation:** 

**[5294.38s] English:** I think that one place where I think  
**Translation:** Vocabulary: autonomously: 独立地

**[5296.86s] English:** that the current state of things  
**Translation:** 

**[5298.74s] English:** falls a little bit short of that  
**Translation:** 

**[5299.86s] English:** is actually the going out there  
**Translation:** 

**[5301.58s] English:** and collecting the data autonomously,  
**Translation:** 

**[5303.20s] English:** which is easy to do in a simulated board game,  
**Translation:** 

**[5306.00s] English:** but very hard to do in the real world.  
**Translation:** Vocabulary: simulated: 模拟的

**[5307.24s] English:** Yeah, it keeps coming back to this one problem, right?  
**Translation:** 

**[5311.20s] English:** So your mind is focused there now in this real world.  
**Translation:** 

**[5315.68s] English:** It just seems scary, this step of collecting the data.  
**Translation:** 

**[5321.66s] English:** And it seems unclear to me how we can do it effectively.  
**Translation:** 

**[5325.24s] English:** Well, you know, 7 billion people in the world,  
**Translation:** 

**[5328.24s] English:** each of them had to do that at some point in their lives.  
**Translation:** 

**[5330.92s] English:** And we should leverage that experience  
**Translation:** 

**[5332.58s] English:** that they've all done.  
**Translation:** 

**[5334.48s] English:** We should be able to try to collect that kind of data.  
**Translation:** 

**[5338.06s] English:** Okay, big questions.  
**Translation:** 

**[5342.28s] English:** Maybe stepping back through your life,  
**Translation:** 

**[5345.22s] English:** what book or books, technical or fiction or philosophical,  
**Translation:** Vocabulary: philosophical: 哲学的

**[5350.10s] English:** had a big impact on the way you saw the world,  
**Translation:** 

**[5354.08s] English:** on the way you thought about the world,  
**Translation:** 

**[5355.64s] English:** your life in general?  
**Translation:** 

**[5357.48s] English:** Hmm.  
**Translation:** 

**[5359.36s] English:** And maybe what books, if it's different,  
**Translation:** 

**[5362.00s] English:** would you recommend people consider reading  
**Translation:** 

**[5363.78s] English:** on their own intellectual journey?  
**Translation:** 

**[5366.16s] English:** It could be...  
**Translation:** 

**[5367.24s] English:** I don't know if this is a scientifically particularly meaningful answer,  
**Translation:** 

**[5379.32s] English:** but the honest answer is that I actually found  
**Translation:** Vocabulary: scientifically: 科学地

**[5382.90s] English:** a lot of the work by Isaac Hasimov  
**Translation:** 

**[5385.70s] English:** to be very inspiring when I was younger.  
**Translation:** 

**[5387.54s] English:** I don't know if that has anything to do with AI necessarily.  
**Translation:** 

**[5390.86s] English:** You don't think it had a ripple effect in your life?  
**Translation:** Vocabulary: ripple: 波纹效应

**[5392.80s] English:** Maybe it did.  
**Translation:** 

**[5396.12s] English:** But yeah, I think,  
**Translation:** 

**[5397.24s] English:** I think that a vision of a future...  
**Translation:** 

**[5400.00s] English:** Where, well, first of all, artificial, I might say artificial intelligence system, artificial robotic systems have, you know, kind of a big place, a big role in society and where we try to imagine the sort of the limiting case of technological advancement and how that might play out in our future history.  
**Translation:** Vocabulary: advancement: 进步

**[5424.16s] English:** But yeah, I think that that was in some way influential. I don't really know how, but I would recommend it. I mean, if nothing else, you'd be well entertained.  
**Translation:** 

**[5436.92s] English:** When did you first yourself like fall in love with the idea of artificial intelligence, get captivated by this field?  
**Translation:** Vocabulary: captivated: 着迷

**[5444.58s] English:** So my honest answer here is actually that I only really started to think about it as something that I might want to do.  
**Translation:** 

**[5453.40s] English:** Actually, in graduate school, pretty late. And a big part of that was that until, you know, somewhere around 2009, 2010, it just wasn't really high on my priority list because I didn't think that it was something where we're going to see very substantial advances in my lifetime.  
**Translation:** 

**[5470.78s] English:** And, you know, maybe in terms of my career, the time when I really decided I wanted to work on this was when I actually took a seminar course that was taught by Professor Andrew.  
**Translation:** 

**[5483.40s] English:** And, you know, at that point, I, of course, had some kind of like a decent understanding of the technical things involved.  
**Translation:** 

**[5490.18s] English:** But one of the things that really resonated with me was when he said in the opening lecture, something to the effect of like, well, he used to have graduate students come to him and talk about how they want to work on AI.  
**Translation:** 

**[5499.42s] English:** And he would kind of chuckle and give them some math problem to deal with.  
**Translation:** 

**[5502.38s] English:** But now he's actually thinking that this is an area where we might see like substantial advances in our lifetime.  
**Translation:** 

**[5507.46s] English:** And that kind of got me thinking because, you know, in some abstract sense, yeah, like you can kind of imagine.  
**Translation:** 

**[5513.40s] English:** But in a very real sense, when someone who had been working on that kind of stuff their whole career suddenly says that.  
**Translation:** 

**[5520.00s] English:** But yeah, like that, that had some effect on me.  
**Translation:** 

**[5523.66s] English:** Yeah, this might be a special moment in the history of the field that this is where we might see some interesting breakthroughs.  
**Translation:** 

**[5533.82s] English:** So in the space of advice, somebody who's interested in getting started in machine learning or reinforcement learning, what advice would you give to maybe an undergraduate student or maybe even younger?  
**Translation:** Vocabulary: breakthroughs: 重大突破; reinforcement: 强化学习; undergraduate: 本科生

**[5544.62s] English:** Or how, what are the first steps to take? And further on, what are the steps to take on that journey?  
**Translation:** 

**[5552.54s] English:** So something that I think is important to do is to not be afraid to like spend time imagining the kind of outcome that you might like to see.  
**Translation:** 

**[5565.88s] English:** So, you know, one outcome might be a successful career, a large paycheck or something, or state of the art results on some benchmark.  
**Translation:** 

**[5573.30s] English:** But hopefully that's not the thing.  
**Translation:** Vocabulary: benchmark: 标准测试; paycheck: 工资单

**[5574.62s] English:** That's like the main driving force for somebody.  
**Translation:** 

**[5577.42s] English:** But I think that if someone who's a student considering a career in AI, like takes a little while, sits down and thinks like, what do I really want to see?  
**Translation:** 

**[5587.34s] English:** What I want to see a machine do?  
**Translation:** 

**[5588.66s] English:** What do I want to see a robot do?  
**Translation:** 

**[5590.24s] English:** What do I want to do?  
**Translation:** 

**[5590.92s] English:** And what I want to see a natural language system, just like imagine, you know, imagine it almost like a commercial for a future product or something or like something that you'd like to see in the world.  
**Translation:** 

**[5600.92s] English:** And then actually sit down and think about the steps that are necessary to get there.  
**Translation:** 

**[5604.66s] English:** And hopefully that thing is not a better number on ImageNet classification.  
**Translation:** 

**[5608.86s] English:** It's like it's probably like an actual thing that we can't do today.  
**Translation:** 

**[5611.44s] English:** That would be really awesome, whether it's a robot butler or a, you know, a really awesome health care decision making support system, whatever it is that you find inspiring.  
**Translation:** 

**[5621.28s] English:** And I think that thinking about that and then backtracking from there and imagining the steps needed to get there will actually lead to much better research.  
**Translation:** 

**[5628.04s] English:** It'll lead to rethinking the assumptions.  
**Translation:** Vocabulary: assumptions: 前提; backtracking: 逆向思考

**[5630.14s] English:** It'll lead to working on the bottlenecks that other people aren't working on.  
**Translation:** 

**[5634.62s] English:** And then naturally to turn to you, we've talked about reward functions.  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[5640.00s] English:** and you just give an advice on looking forward how you'd like to see what what kind of change  
**Translation:** 

**[5645.12s] English:** you would like to make in the world what do you think ridiculous big question what do you think  
**Translation:** 

**[5649.66s] English:** is the meaning of life what is the meaning of your life what gives you fulfillment purpose  
**Translation:** 

**[5656.02s] English:** happiness and meaning that's a very big question um  
**Translation:** Vocabulary: fulfillment: 满足感

**[5662.06s] English:** what's the reward function under which you're operating yeah i think one thing that does give  
**Translation:** 

**[5669.42s] English:** you know if not meaning at least satisfaction is uh some degree of confidence uh that i'm working  
**Translation:** 

**[5675.58s] English:** on a problem that really matters i feel like it's less important to me to like actually solve  
**Translation:** 

**[5680.60s] English:** a problem but it's it's quite nice to uh take things to spend my time on that i believe really  
**Translation:** 

**[5687.80s] English:** matter and you know i i try pretty hard to to look for that i don't know if it's easy to answer this  
**Translation:** 

**[5694.58s] English:** but if you're successful what does that look like  
**Translation:** 

**[5699.42s] English:** what's the big dream now of course success is built on top of success and you keep going forever  
**Translation:** 

**[5706.80s] English:** but what is the dream yeah so one very concrete thing or maybe as concrete as it's going to get  
**Translation:** 

**[5714.80s] English:** here is is to see machines that actually get better and better the you know the longer they  
**Translation:** 

**[5722.34s] English:** exist in the world and that kind of seems like on the surface one might even think that that's  
**Translation:** 

**[5726.66s] English:** something that we have today but i think we really don't i think that  
**Translation:** 

**[5729.42s] English:** um there is uh unending uh complexity in the universe and to date all of the machines that  
**Translation:** 

**[5738.66s] English:** we've been able to build don't sort of improve up to the limit of that complexity they they  
**Translation:** 

**[5744.10s] English:** they hit a wall somewhere maybe they hit a wall because they're in a simulator that has that is  
**Translation:** Vocabulary: complexity: 复杂性; simulator: 模拟器

**[5748.88s] English:** only a very limited very uh pale imitation of the real world or they hit a wall because they  
**Translation:** 

**[5753.22s] English:** rely on a labeled data set but they they never hit the wall of like running out of stuff to see  
**Translation:** Vocabulary: imitation: 模仿品

**[5758.56s] English:** like they never hit the wall of like running out of stuff to see like they never hit the wall of  
**Translation:** 

**[5759.42s] English:** like they never hit the wall of like running out of stuff to see  
**Translation:** 

**[5760.00s] English:** So, you know, I'd like to build a machine that can go as far as possible in that regard.  
**Translation:** 

**[5764.70s] English:** Runs up against the ceiling of the complexity of the universe.  
**Translation:** 

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

**[5778.84s] English:** And in education space, in terms of reinforcement learning, thank you for inspiring the world.  
**Translation:** Vocabulary: reinforcement: 强化学习

**[5782.92s] English:** Thank you for the great research you do.  
**Translation:** 

**[5784.42s] English:** Thank you.  
**Translation:** 

**[5785.36s] English:** Thanks for listening to this conversation with Sergey Levine.  
**Translation:** 

**[5788.12s] English:** And thank you to our sponsors, Cash App and ExpressVPN.  
**Translation:** Vocabulary: levine: 利文; sponsors: 赞助商

**[5793.42s] English:** Please consider supporting this podcast by downloading Cash App and using code LEXPODCAST and signing up at expressvpn.com slash lexpod.  
**Translation:** 

**[5804.30s] English:** Click all the links, buy all the stuff.  
**Translation:** 

**[5807.62s] English:** It's the best way to support this podcast and the journey I'm on.  
**Translation:** 

**[5811.82s] English:** If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple Podcasts, support on Patreon.  
**Translation:** Vocabulary: subscribe: 订阅

**[5818.12s] English:** Or connect with me on Twitter at Lex Friedman, spelled somehow, if you can figure out how, without using the letter E, just F-R-I-D-M-A-N.  
**Translation:** 

**[5828.92s] English:** And now, let me leave you with some words from Salvador Dali.  
**Translation:** Vocabulary: friedman: 弗里德曼; salvador: 萨尔瓦多

**[5833.38s] English:** Intelligence without ambition is a bird without wings.  
**Translation:** 

**[5838.54s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 

**[5848.12s] English:** Transcription by CastingWords  
**Translation:** Vocabulary: transcription: 录音转写


<!-- TRANSCRIPTION_COMPLETE -->
