# Podcast vocabulary notes
Source file: Lex Fridman - Richard Karp： Algorithms and Computational Complexity ｜ Lex Fridman Podcast #111.opus

**[0.00s] English:** The following is a conversation with Richard Karp, a professor at Berkeley and one of the most important figures in the history of theoretical computer science.  
**Translation:** 

**[8.82s] English:** In 1985, he received the Turing Award for his research in the theory of algorithms, including the development of the Admin's Karp algorithm for solving the max flow problem on networks, Hopcroft-Karp algorithm for finding maximum cardinality matchings in bipartite graphs, and his landmark paper in complexity theory called Reducibility Among Combinatorial Problems, in which he proved 21 problems to be NP-complete.  
**Translation:** 

**[38.44s] English:** Thank you.  
**Translation:** 

**[38.82s] English:** This paper was probably the most important catalyst in the explosion of interest in the study of NP-completeness and the P versus NP problem in general.  
**Translation:** Vocabulary: catalyst: 推动因素

**[48.76s] English:** Quick summary of the ads.  
**Translation:** 

**[50.24s] English:** Two sponsors, 8sleep Mattress and Cash App.  
**Translation:** Vocabulary: mattress: 床垫; sponsors: 赞助商

**[53.46s] English:** Please consider supporting this podcast by going to 8sleep.com slash Lex and downloading Cash App and using code LexPodcast.  
**Translation:** 

**[62.84s] English:** Click the links, buy the stuff.  
**Translation:** 

**[64.58s] English:** It really is the best way to support this podcast.  
**Translation:** 

**[67.68s] English:** If you enjoy this thing.  
**Translation:** 

**[68.82s] English:** Subscribe on YouTube, review it with five stars on Apple Podcasts, support it on Patreon, or connect with me on Twitter at Lex Friedman.  
**Translation:** 

**[76.78s] English:** As usual, I'll do a few minutes of ads now and never any ads in the middle that can break the flow of the conversation.  
**Translation:** Vocabulary: subscribe: 订阅

**[82.68s] English:** This show is sponsored by 8sleep and its Pod Pro Mattress that you can check out at 8sleep.com slash Lex to get $200 off.  
**Translation:** 

**[92.40s] English:** It controls temperature with an app.  
**Translation:** 

**[95.72s] English:** It can cool down to as low as 55 degrees.  
**Translation:** 

**[98.20s] English:** And each side of the bed separately.  
**Translation:** 

**[100.98s] English:** Research shows that temperature has a big impact on the quality of our sleep.  
**Translation:** 

**[105.24s] English:** Anecdotally, it's been a game changer for me.  
**Translation:** Vocabulary: anecdotally: 个人经验

**[107.82s] English:** I love it.  
**Translation:** 

**[108.74s] English:** It's been a couple of weeks now.  
**Translation:** 

**[110.18s] English:** I've just been really enjoying it.  
**Translation:** 

**[112.44s] English:** Both in the fact that I'm getting better sleep and that it's a smart mattress, essentially.  
**Translation:** 

**[118.00s] English:** I kind of imagine this being the early days.  
**Translation:** 

**[120.00s] English:** of artificial intelligence being a part of every aspect of our lives, and certainly infusing AI  
**Translation:** Vocabulary: infusing: 渗透

**[125.66s] English:** in one of the most important aspects of life, which is sleep, I think has a lot of potential  
**Translation:** 

**[131.04s] English:** for being beneficial. The Pod Pro is packed with sensors that track heart rate, heart rate  
**Translation:** 

**[136.90s] English:** variability, and respiratory rate, showing it all in their app. The app's health metrics are amazing,  
**Translation:** 

**[144.10s] English:** but the cooling alone is honestly worth the money. I don't always sleep, but when I do,  
**Translation:** Vocabulary: respiratory: 呼吸; variability: 变化

**[148.98s] English:** I choose the Eight Sleep Pod Pro mattress. Check it out at eightsleep.com slash lex to get $200  
**Translation:** 

**[155.76s] English:** off. And remember, just visiting the site and considering the purchase helps convince the  
**Translation:** Vocabulary: eightsleep: 八睡

**[161.78s] English:** folks at Eight Sleep that this silly old podcast is worth sponsoring in the future.  
**Translation:** 

**[167.04s] English:** This show is also presented by the great and powerful Cash App, the number one finance app  
**Translation:** Vocabulary: sponsoring: 赞助

**[174.34s] English:** in the App Store. When you get it, use code LEXPODCAST. Cash App lets you  
**Translation:** 

**[178.96s] English:** send money to friends, buy Bitcoin, and invest in the stock market with as little as $1.  
**Translation:** 

**[184.32s] English:** It's one of the best designed interfaces of an app that I've ever used. To me, good design is when  
**Translation:** 

**[189.90s] English:** everything is easy and natural. Bad design is when the app gets in the way, either because it's buggy  
**Translation:** Vocabulary: buggy: 不稳定; interfaces: 界面

**[196.20s] English:** or because it tries too hard to be helpful. I'm looking at you, Clippy from Microsoft,  
**Translation:** 

**[201.54s] English:** even though I love you. Anyway, there's a big part of my brain and heart that loves to design things  
**Translation:** 

**[207.20s] English:** and also to appreciate great design.  
**Translation:** 

**[208.96s] English:** So again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST,  
**Translation:** 

**[215.56s] English:** you get $10. And Cash App will also donate $10 to FIRST, an organization that is helping to advance  
**Translation:** 

**[221.52s] English:** robotics and STEM education for young people around the world. And now, here's my conversation  
**Translation:** 

**[227.58s] English:** with Richard Karp. You wrote that at the age of 13, you were first exposed to plane geometry  
**Translation:** 

**[234.80s] English:** and was wonderstruck by the power and elegance of form of proof.  
**Translation:** Vocabulary: elegance: 优美; geometry: 几何; wonderstruck: 惊叹

**[238.96s] English:** You wrote that at the age of 13, you were first exposed to plane geometry and was wonderstruck by the power  
**Translation:** 

**[239.96s] English:** and elegance of form of proof.  
**Translation:** 

**[240.00s] English:** Are there problems, proofs, properties, ideas in plain geometry that from that time that you remember being mesmerized by or just enjoying to go through to prove various aspects?  
**Translation:** 

**[252.36s] English:** So Michael Rabin told me this story about an experience he had when he was a young student who was tossed out of his classroom for bad behavior and was wandering through the corridors of his school and came upon two older students who were studying the problem of finding the shortest distance between two non-overlapping circles.  
**Translation:** Vocabulary: corridors: 走廊; mesmerized: 着迷

**[282.36s] English:** And Michael thought about it and said you take the straight line between the two centers and the segment between the two circles is the shortest because a straight line is the shortest distance between the two centers and any other line connecting the circles would be on a longer line.  
**Translation:** 

**[307.46s] English:** And I thought and he thought and I agreed that this was just interesting.  
**Translation:** 

**[312.36s] English:** Elegance, the pure reasoning could come up with such a result.  
**Translation:** 

**[317.62s] English:** Certainly the shortest distance from the two centers of the circles is a straight line.  
**Translation:** 

**[325.50s] English:** Could you once again say what's the next step in that proof?  
**Translation:** 

**[329.28s] English:** Well, any segment joining the two circles, if you extend it by taking the radius on each side, you get a third.  
**Translation:** 

**[342.36s] English:** The third segment with a path with three edges, which connects the two centers, and this has to be at least as long as the shortest path, which is the straight line.  
**Translation:** 

**[353.74s] English:** The straight line. Yeah. Wow. Yeah, that is that's quite, quite simple. So what what is it?  
**Translation:** 

**[360.00s] English:** that elegance that you just find compelling? Well, just that you could establish a fact  
**Translation:** 

**[369.92s] English:** about geometry beyond dispute by pure reasoning. I also enjoyed the challenge of solving puzzles in  
**Translation:** Vocabulary: compelling: 令人信服; elegance: 优雅; geometry: 几何学

**[382.56s] English:** plain geometry. It was much more fun than the earlier mathematics courses, which were mostly  
**Translation:** 

**[388.40s] English:** about arithmetic operations and manipulating them. Was there something about geometry itself,  
**Translation:** Vocabulary: arithmetic: 算术; manipulating: 操作

**[395.84s] English:** the slightly visual component of it? Oh, yes, absolutely. Although  
**Translation:** 

**[401.84s] English:** I lacked three-dimensional vision. I wasn't very good at three-dimensional vision. You mean being  
**Translation:** 

**[407.84s] English:** able to visualize three-dimensional objects? Three-dimensional objects or surfaces,  
**Translation:** 

**[414.32s] English:** hyperplanes, and so on. So, there  
**Translation:** Vocabulary: hyperplanes: 高维平面; visualize: 可视化

**[418.40s] English:** I didn't have an intuition. But, for example, the fact that the sum of the angles of a triangle is  
**Translation:** 

**[427.84s] English:** 180 degrees is proved convincingly, and it comes as a surprise that that can be done.  
**Translation:** Vocabulary: convincingly: 令人信服地; triangle: 三角形

**[439.28s] English:** Why is that surprising? Well, it is a surprising  
**Translation:** 

**[448.40s] English:** idea, I suppose. Why is that proof difficult? It's not. That's the point. It's so easy,  
**Translation:** 

**[454.80s] English:** and yet it's so convincing. Do you remember what is the proof that it adds up to 180?  
**Translation:** 

**[463.28s] English:** You start at a corner and draw a line parallel to the opposite side,  
**Translation:** 

**[476.16s] English:** and that line sort of...  
**Translation:** 

**[478.40s] English:** ...trisects the...  
**Translation:** Vocabulary: trisects: 三等分

**[480.00s] English:** angle between the other two sides, and you get a half plane which has to add up to 180  
**Translation:** 

**[492.50s] English:** degrees, and the angles, by the equality of alternate angles, what's it called, you get  
**Translation:** 

**[505.14s] English:** a correspondence between the angles created along the side of the triangle and the three angles of  
**Translation:** 

**[513.06s] English:** the triangle. Has geometry had an impact on, when you look into the future of your work with  
**Translation:** Vocabulary: correspondence: 对应关系; geometry: 几何学

**[519.84s] English:** combinatorial algorithms, has it had some kind of impact in terms of, yeah, being able, the puzzles,  
**Translation:** 

**[526.64s] English:** the visual aspects that were first so compelling to you? Not Euclidean geometry particularly. I  
**Translation:** Vocabulary: combinatorial: 组合算法; compelling: 令人着迷; euclidean: 欧几里得的

**[534.64s] English:** think  
**Translation:** 

**[535.14s] English:** I use tools like linear programming and integer programming a lot, but those require  
**Translation:** Vocabulary: integer: 整数

**[545.48s] English:** high-dimensional visualization, and so I tend to go by the algebraic properties.  
**Translation:** 

**[553.20s] English:** Right, you go by the linear algebra and not by the visualization.  
**Translation:** Vocabulary: algebra: 代数; algebraic: 代数的; visualization: 可视化

**[558.68s] English:** Well, the interpretation in terms of, for example, finding the highest point on a  
**Translation:** 

**[565.14s] English:** polyhedron, as in linear programming, is motivating. But again, I don't have the  
**Translation:** Vocabulary: motivating: 激励人心; polyhedron: 多面体

**[575.52s] English:** high-dimensional intuition that would particularly inform me, so I sort of lean on the algebra.  
**Translation:** 

**[584.82s] English:** So to linger on that point, what kind of visualization do you do when you're trying to  
**Translation:** Vocabulary: intuition: 直觉

**[591.80s] English:** think about, well, get to combinatorial algorithms?  
**Translation:** 

**[594.80s] English:** Algorithms, but just algorithms in general.  
**Translation:** 

**[597.26s] English:** Yeah.  
**Translation:** 

**[597.62s] English:** What kind of, what's inside your mind when you're  
**Translation:** 

**[600.00s] English:** or thinking about designing algorithms, or even just tackling any mathematical problem?  
**Translation:** 

**[609.40s] English:** Well, I think that usually an algorithm involves a repetition of some inner loop.  
**Translation:** Vocabulary: algorithm: 算法; mathematical: 数学的; repetition: 重复; tackling: 解决

**[619.34s] English:** And so I can sort of visualize the distance from the desired solution  
**Translation:** 

**[626.18s] English:** as iteratively reducing until you finally hit the exact solution.  
**Translation:** Vocabulary: visualize: 想象

**[633.16s] English:** And try to take steps that get you closer to the...  
**Translation:** 

**[635.64s] English:** Try to take steps that get closer and having the certainty of converging.  
**Translation:** Vocabulary: converging: 趋向一致

**[641.40s] English:** So it's basically the mechanics of the algorithm is often very simple.  
**Translation:** 

**[649.10s] English:** But especially when you're trying something out on the computer.  
**Translation:** 

**[653.24s] English:** So for example,  
**Translation:** 

**[655.66s] English:** um,  
**Translation:** 

**[656.18s] English:** I did some work on the traveling salesman problem.  
**Translation:** 

**[659.10s] English:** And I could see there was a particular function that had to be minimized.  
**Translation:** 

**[664.54s] English:** And it was fascinating to see the successive approaches to the optimum.  
**Translation:** 

**[671.78s] English:** You mean, so first of all,  
**Translation:** Vocabulary: optimum: 最佳; successive: 相继

**[673.02s] English:** traveling salesman problem is where you have to visit every city without ever...  
**Translation:** 

**[680.34s] English:** Only once.  
**Translation:** 

**[681.30s] English:** Yeah, that's right.  
**Translation:** 

**[682.26s] English:** Find the shortest path through a set of cities.  
**Translation:** 

**[684.96s] English:** Yeah.  
**Translation:** 

**[685.24s] English:** Uh, which is sort of a canonical, a standard, a really nice problem that's really hard in computer science.  
**Translation:** Vocabulary: canonical: 标准范例

**[691.08s] English:** Right, exactly, yes.  
**Translation:** 

**[692.34s] English:** Uh, so can you say again, what was nice about the objective...  
**Translation:** 

**[695.52s] English:** Being able to think about the objective function there and maximizing it or minimizing it?  
**Translation:** 

**[701.44s] English:** Well, it's just that the, um, as the algorithm proceeded,  
**Translation:** Vocabulary: maximizing: 最大化; minimizing: 最小化

**[705.90s] English:** it was...  
**Translation:** 

**[707.10s] English:** You were making progress, continual progress, and eventually getting to the optimum point.  
**Translation:** Vocabulary: continual: 不间断的

**[713.54s] English:** So there's two...  
**Translation:** 

**[715.24s] English:** Two parts, maybe.  
**Translation:** 

**[717.04s] English:** Maybe you can correct me with...  
**Translation:** 

**[718.34s] English:** First is, like, getting an intuition.  
**Translation:** Vocabulary: intuition: 直觉

**[720.00s] English:** about what the solution would look like and or even maybe coming up with a solution and two is  
**Translation:** 

**[726.10s] English:** proving that this thing is actually going to be pretty good what part is harder for you  
**Translation:** 

**[732.86s] English:** where's the magic happen is it in the first sets of intuitions or is it in the detail the messy  
**Translation:** 

**[740.12s] English:** details of actually showing that it is going to get to the exact solution and it's going to run  
**Translation:** 

**[747.74s] English:** at this at a certain complexity well the magic is just the fact that it  
**Translation:** 

**[755.18s] English:** that the gap from the optimum decreases monotonically and you can see it happening  
**Translation:** Vocabulary: complexity: 复杂性; monotonically: 单调地

**[763.62s] English:** and various metrics of what's going on are improving all along until finally you hit the  
**Translation:** 

**[772.30s] English:** optimum perhaps later we'll talk about the assignment problem and i can okay  
**Translation:** 

**[777.64s] English:** okay  
**Translation:** 

**[777.74s] English:** illustrate illustrates a little better yeah now zooming out again as you write don knuth  
**Translation:** Vocabulary: illustrate: 举例说明; illustrates: 举例说明

**[784.00s] English:** has called attention to a breed of people who derive great aesthetic pleasure from contemplating  
**Translation:** 

**[791.48s] English:** the structure of computational processes so don calls these folks geeks and you're right that you  
**Translation:** Vocabulary: aesthetic: 审美; computational: 计算的; contemplating: 思考; geeks: 极客

**[797.42s] English:** remember the moment you realized you were such a person you were shown the hungarian algorithm to  
**Translation:** 

**[803.28s] English:** solve the assignment problem right so perhaps you can explain what the assignment problem is  
**Translation:** Vocabulary: algorithm: 算法; hungarian: 哈茂德

**[807.74s] English:** and what uh the hungarian algorithm is so in the assignment problem you have uh n boys and n girls  
**Translation:** 

**[820.20s] English:** and you are given the desirability of uh or the cost of matching  
**Translation:** 

**[829.32s] English:** the i boy with the j girl for all i and j you're given a matrix of numbers and you want to  
**Translation:** 

**[838.48s] English:** find the one-to-one  
**Translation:** Vocabulary: matrix: 矩阵

**[857.76s] English:** so  
**Translation:** 

**[860.08s] English:** so  
**Translation:** 

**[861.20s] English:** so  
**Translation:** 

**[863.04s] English:** so  
**Translation:** 

**[863.72s] English:** so  
**Translation:** 

**[864.54s] English:** so  
**Translation:** 

**[865.28s] English:** so  
**Translation:** 

**[867.28s] English:** so  
**Translation:** 

**[867.56s] English:** so  
**Translation:** 

**[867.64s] English:** so  
**Translation:** 

**[867.66s] English:** so  
**Translation:** 

**[840.00s] English:** matching of the boys with the girls such that the sum of the associated costs  
**Translation:** 

**[847.30s] English:** will be minimized so the the best way to match the boys with the girls or men  
**Translation:** 

**[854.08s] English:** with jobs or any two sets not any possible matching is possible or yeah  
**Translation:** Vocabulary: minimized: 最小化

**[861.30s] English:** all one-to-one correspondences are permissible if there is a connection  
**Translation:** 

**[867.96s] English:** that is not allowed then you can think of it as having an infinite cost so what  
**Translation:** Vocabulary: correspondences: 对应关系

**[876.54s] English:** you do is to depend on the observation that the identity of the optimal  
**Translation:** 

**[888.08s] English:** assignment or as we call it the optimal permutation is not changed if you  
**Translation:** Vocabulary: optimal: 最优; permutation: 排列

**[896.10s] English:** subtract  
**Translation:** 

**[897.96s] English:** a constant from any row or column of the matrix you can see that the comparison  
**Translation:** Vocabulary: subtract: 减去

**[906.60s] English:** between the different assignments is not changed by that because you're peeing on  
**Translation:** 

**[913.26s] English:** if you decrease a particular row all the elements of a row by some constant all  
**Translation:** 

**[918.78s] English:** solutions decrease by the cost of that by an amount equal to that constant so  
**Translation:** 

**[925.38s] English:** the idea of the algorithm is to start with the  
**Translation:** Vocabulary: algorithm: 算法

**[927.96s] English:** matrix of non-negative numbers and keep subtracting from rows or from our entire  
**Translation:** 

**[937.68s] English:** columns in such a way that you subtract the same constant from all the elements  
**Translation:** Vocabulary: subtracting: 减去

**[945.72s] English:** of that row or column while maintaining the property that all the elements are  
**Translation:** 

**[955.68s] English:** non-negative  
**Translation:** 

**[957.96s] English:** simple yeah  
**Translation:** 

**[960.00s] English:** And so what you have to do is find small moves which will decrease the total cost while subtracting constants from rows or columns.  
**Translation:** Vocabulary: constants: 常数

**[977.60s] English:** And there's a particular way of doing that by computing the kind of shortest path through the elements in the matrix.  
**Translation:** 

**[983.50s] English:** And you just keep going in this way until you finally get a full permutation of zeros while the matrix is non-negative.  
**Translation:** Vocabulary: computing: 计算; matrix: 矩阵

**[994.94s] English:** And then you know that that has to be the cheapest.  
**Translation:** 

**[998.66s] English:** Is that as simple as it sounds?  
**Translation:** 

**[1002.46s] English:** So the shortest path through the matrix part.  
**Translation:** 

**[1005.14s] English:** Yeah, the simplicity lies in how you find...  
**Translation:** Vocabulary: simplicity: 简单性

**[1009.86s] English:** I oversimplified slightly what you...  
**Translation:** 

**[1013.50s] English:** You will end up subtracting a constant from some rows or columns and adding the same constant back to other rows and columns.  
**Translation:** Vocabulary: oversimplified: 简化的过多

**[1023.72s] English:** So as not to reduce any of the zero elements, you leave them unchanged.  
**Translation:** 

**[1034.80s] English:** But each individual step modifies several rows and columns by the same amount.  
**Translation:** Vocabulary: modifies: 修改; unchanged: 未变

**[1044.08s] English:** But overall, it decreases the cost.  
**Translation:** 

**[1046.60s] English:** So there's something about that elegance that made you go,  
**Translation:** Vocabulary: elegance: 优雅

**[1050.72s] English:** Aha, this is a beautiful...  
**Translation:** 

**[1052.28s] English:** It's amazing that something like this, something so simple can solve a problem like this.  
**Translation:** 

**[1058.04s] English:** Yeah, it's really cool.  
**Translation:** 

**[1059.38s] English:** If I had mechanical ability, I would probably like to do woodworking or other activities where you sort of shape something into something.  
**Translation:** 

**[1073.50s] English:** Beautiful and orderly.  
**Translation:** 

**[1074.84s] English:** And there's something about the orderly, systematic nature of it.  
**Translation:** 

**[1080.00s] English:** of that iterative algorithm that is pleasing to me so what do you think  
**Translation:** 

**[1086.60s] English:** about this idea of geeks as Duncan it calls them what do you think of is it  
**Translation:** Vocabulary: algorithm: 迭代算法; geeks: 极客; iterative: 迭代的

**[1093.12s] English:** something specific to a mindset that allows you to discover the elegance and  
**Translation:** 

**[1100.00s] English:** computational processes or is this all of us can all of us discover this beauty  
**Translation:** Vocabulary: computational: 计算方法; mindset: 思维模式

**[1104.66s] English:** we born this way I think so I always like to play with numbers I I used to  
**Translation:** 

**[1114.02s] English:** amuse myself by multiplying four digit decimal numbers in my head and putting  
**Translation:** Vocabulary: decimal: 小数; digit: 位数; multiplying: 乘法

**[1122.00s] English:** myself to sleep by starting with one and doubling the number as long as I could  
**Translation:** 

**[1127.16s] English:** go and testing my memory my ability to retain the information and I also read  
**Translation:** 

**[1133.38s] English:** somewhere that you  
**Translation:** 

**[1134.14s] English:** you  
**Translation:** 

**[1134.64s] English:** wrote that you enjoyed showing off to your friends by I believe multiplying  
**Translation:** 

**[1141.30s] English:** four-digit numbers right a couple of four-digit numbers yeah I had a summer  
**Translation:** 

**[1148.62s] English:** job at a beach resort outside of Boston and the other employee I was the barker  
**Translation:** 

**[1157.68s] English:** at a skee-ball game yeah I used to I used to sit at a microphone microphone  
**Translation:** Vocabulary: microphone: 麦克风

**[1164.12s] English:** I used to sit at a microphone microphone  
**Translation:** 

**[1164.62s] English:** saying come one come all come in and play skee-ball five cents to play a  
**Translation:** 

**[1169.18s] English:** nickel to win and so on that's what a barker I was gonna I wasn't sure if I  
**Translation:** 

**[1173.38s] English:** should know but Barker that's you're the the charming outgoing person is getting  
**Translation:** Vocabulary: charming: 风趣迷人; nickel: 镍币; outgoing: 外向

**[1179.74s] English:** people to come in yeah well I wasn't particularly charming but I could be  
**Translation:** 

**[1184.22s] English:** very repetitious and loud and the other employees were sort of juvenile delinquents who had no  
**Translation:** Vocabulary: delinquents: 不良少年; juvenile: 青少年

**[1194.42s] English:** yeah well I wasn't particularly charming but I could be very repetitious and loud and the other employees were sort of juvenile delinquents who had no  
**Translation:** 

**[1194.48s] English:** academic bent but somehow I found that I could impress  
**Translation:** 

**[1200.00s] English:** them by uh by uh performing this mental melter of mental arithmetic you know there's something  
**Translation:** 

**[1207.20s] English:** to that that you know one of some of the most popular videos on the internet is um there's a  
**Translation:** Vocabulary: arithmetic: 算术

**[1215.94s] English:** there's a youtube channel called numberphile that shows off different mathematical ideas  
**Translation:** 

**[1220.10s] English:** i see there's still something really profoundly interesting to people about math the the beauty  
**Translation:** Vocabulary: mathematical: 数学的; profoundly: 深刻地

**[1226.68s] English:** of it something even if they don't understand the basic concept even being discussed there's  
**Translation:** 

**[1233.88s] English:** something compelling to it what do you think that is any lessons you drew from the your early teen  
**Translation:** Vocabulary: compelling: 有吸引力的

**[1240.12s] English:** years when you were showing off to your friends with the numbers like is what is it that attracts  
**Translation:** 

**[1247.32s] English:** us to the beauty of mathematics do you think the general population not just the computer  
**Translation:** 

**[1253.68s] English:** scientists and mathematicians  
**Translation:** 

**[1255.92s] English:** i think that it you know you can do amazing things you can test whether large numbers are prime  
**Translation:** Vocabulary: mathematicians: 数学家

**[1262.98s] English:** you can uh um you can solve little puzzles about cannibals and missionaries  
**Translation:** 

**[1272.08s] English:** yeah and uh that's the kind of achievement it's it's it's puzzle solving and at a higher level  
**Translation:** Vocabulary: cannibals: 食人者

**[1280.62s] English:** the fact that you can you can do this reasoning that you can prove in an  
**Translation:** 

**[1284.96s] English:** absolutely  
**Translation:** 

**[1285.92s] English:** ironclad way that the some of the angles of the triangle is 180 degrees  
**Translation:** 

**[1291.28s] English:** yeah it's a nice escape from the messiness of the real world where nothing can be proved so  
**Translation:** Vocabulary: ironclad: 铁板钉钉; messiness: 混乱; triangle: 三角形

**[1298.32s] English:** and we'll talk about it but sometimes the ability to map the real world into such problems where  
**Translation:** 

**[1303.68s] English:** you can't prove it is this is a powerful step yeah it's amazing that we can do another attribute of  
**Translation:** Vocabulary: attribute: 属性

**[1309.64s] English:** geeks is they they're not necessarily uh endowed with emotional intelligence  
**Translation:** 

**[1315.92s] English:** so they can live in a world of abstractions without having  
**Translation:** Vocabulary: abstractions: 抽象; endowed: 赋予; geeks: 极客

**[1320.00s] English:** to master the complexities of dealing with people.  
**Translation:** 

**[1326.84s] English:** Just to link on the historical note, as a PhD student in 1955,  
**Translation:** Vocabulary: complexities: 复杂性

**[1331.68s] English:** you joined the computational lab at Harvard,  
**Translation:** 

**[1334.14s] English:** where Howard Aiken had built the Mark I and the Mark IV computers.  
**Translation:** Vocabulary: aiken: 艾克恩; computational: 计算的

**[1339.36s] English:** Just to take a step back into that history, what were those computers like?  
**Translation:** 

**[1343.38s] English:** The Mark IV filled a large room, much bigger than this large office that we're talking in now.  
**Translation:** 

**[1356.96s] English:** And you could walk around inside it.  
**Translation:** 

**[1359.22s] English:** There were rows of relays.  
**Translation:** 

**[1363.22s] English:** You could just walk around the interior,  
**Translation:** 

**[1364.96s] English:** and the machine would sometimes fail because of bugs,  
**Translation:** 

**[1373.10s] English:** which led to a lot of problems.  
**Translation:** 

**[1373.36s] English:** It literally meant flying creatures landing on the switches.  
**Translation:** 

**[1379.34s] English:** So I never used that machine for any practical purpose.  
**Translation:** 

**[1386.30s] English:** The lab eventually acquired one of the earlier commercial computers.  
**Translation:** 

**[1394.70s] English:** This was already in the 60s?  
**Translation:** 

**[1396.54s] English:** No, in the mid-50s.  
**Translation:** 

**[1397.80s] English:** In the mid-50s?  
**Translation:** 

**[1398.24s] English:** Or late 50s.  
**Translation:** 

**[1399.78s] English:** There was already commercial computers in the...  
**Translation:** 

**[1401.72s] English:** Yeah, we had a UNIVAC.  
**Translation:** 

**[1402.82s] English:** A UNIVAC with 2,000 words of storage.  
**Translation:** 

**[1407.32s] English:** And so you had to work hard to allocate the memory properly.  
**Translation:** Vocabulary: allocate: 分配

**[1412.22s] English:** Also, the excess time from one word to another  
**Translation:** 

**[1415.96s] English:** depended on the number of the particular words.  
**Translation:** 

**[1421.34s] English:** And so there was an art to sort of arranging the storage allocation  
**Translation:** 

**[1426.12s] English:** to make fetching data rapid.  
**Translation:** Vocabulary: allocation: 分配; fetching: 获取

**[1430.56s] English:** Were you attracted to this?  
**Translation:** 

**[1432.82s] English:** No, I wasn't attracted to it.  
**Translation:** 

**[1433.82s] English:** I was attracted to the fact that it was actually a physical world implementation of mathematics.  
**Translation:** 

**[1437.52s] English:** So it's a mathematical machine that's actually...  
**Translation:** Vocabulary: implementation: 实现; mathematical: 数学的

**[1440.00s] English:** actually doing the math physically?  
**Translation:** 

**[1443.16s] English:** No, not at all.  
**Translation:** 

**[1444.80s] English:** I think I was attracted to the underlying algorithms.  
**Translation:** 

**[1450.86s] English:** But did you draw any inspiration?  
**Translation:** 

**[1452.86s] English:** So could you have imagined, like what did you imagine  
**Translation:** 

**[1457.22s] English:** was the future of these giant computers?  
**Translation:** 

**[1460.10s] English:** Could you have imagined that 60 years later  
**Translation:** 

**[1462.00s] English:** we'd have billions of these computers all over the world?  
**Translation:** 

**[1465.80s] English:** I couldn't imagine that.  
**Translation:** 

**[1468.02s] English:** But there was a sense in the laboratory  
**Translation:** 

**[1472.82s] English:** that this was the wave of the future.  
**Translation:** 

**[1476.12s] English:** In fact, my mother influenced me.  
**Translation:** 

**[1478.48s] English:** She told me that data processing was going to be really big,  
**Translation:** 

**[1482.30s] English:** and I should get into it.  
**Translation:** 

**[1486.20s] English:** She's a smart woman.  
**Translation:** 

**[1487.26s] English:** Yeah, she was a smart woman.  
**Translation:** 

**[1489.08s] English:** And there was just a feeling that this  
**Translation:** 

**[1492.58s] English:** was going to change the world.  
**Translation:** 

**[1494.02s] English:** But I didn't think of it in terms of personal computing.  
**Translation:** 

**[1497.14s] English:** I hadn't thought of it that way.  
**Translation:** Vocabulary: computing: 计算机计算

**[1498.02s] English:** I had no anticipation that we would  
**Translation:** 

**[1501.62s] English:** be walking around with computers in our pockets  
**Translation:** Vocabulary: anticipation: 预期

**[1504.32s] English:** or anything like that.  
**Translation:** 

**[1506.16s] English:** Did you see computers as tools, as mathematical mechanisms  
**Translation:** 

**[1512.84s] English:** to analyze sort of the theoretical computer science?  
**Translation:** 

**[1516.56s] English:** Or is the AI folks, which is an entire other community  
**Translation:** 

**[1521.02s] English:** of dreamers, as something that could one day have  
**Translation:** 

**[1524.84s] English:** human-level intelligence?  
**Translation:** 

**[1526.88s] English:** Well, AI wasn't very much.  
**Translation:** 

**[1527.96s] English:** It wasn't very much on my radar.  
**Translation:** 

**[1529.58s] English:** I did read Turing's paper about the Turing test  
**Translation:** 

**[1536.66s] English:** computing and intelligence.  
**Translation:** Vocabulary: turing: 图灵

**[1538.12s] English:** Yeah, the Turing test.  
**Translation:** 

**[1540.34s] English:** What did you think about that paper?  
**Translation:** 

**[1541.88s] English:** Was that just like science fiction?  
**Translation:** 

**[1545.66s] English:** I thought that it wasn't a very good test  
**Translation:** 

**[1548.30s] English:** because it was too subjective.  
**Translation:** 

**[1550.46s] English:** So I didn't feel that the Turing test was really the right way  
**Translation:** 

**[1557.06s] English:** to calculate.  
**Translation:** 

**[1557.84s] English:** Yeah.  
**Translation:** 

**[1557.96s] English:** I thought it was a very good test.  
**Translation:** 

**[1560.00s] English:** could be the to linger on that do you think it's pot because you've come up with some incredible  
**Translation:** 

**[1565.02s] English:** tests later on tests on algorithms right yeah that are uh like strong reliable robust across  
**Translation:** 

**[1573.72s] English:** a bunch of different classes of algorithms but returning to this emotional mess that is  
**Translation:** Vocabulary: robust: 坚固可靠

**[1580.32s] English:** intelligence do you think it's possible to come up with a test that's as ironclad as  
**Translation:** 

**[1586.70s] English:** some of the computational complexity work well i think the greater question is whether it's  
**Translation:** Vocabulary: complexity: 复杂性; computational: 计算的; ironclad: 坚不可摧

**[1593.36s] English:** possible to achieve human level level intelligence right so that's so first of all let me at the  
**Translation:** 

**[1601.14s] English:** philosophical do you think it's possible to create algorithms that reason and would  
**Translation:** Vocabulary: philosophical: 哲学上的

**[1609.84s] English:** seem to us to have the same kind of intelligence as human beings it's an open question  
**Translation:** 

**[1616.30s] English:** um  
**Translation:** 

**[1617.18s] English:** it seems to me that um most of the achievements have  
**Translation:** 

**[1624.42s] English:** uh acquire operate within a very limited set of ground rules and for a very limited precise task  
**Translation:** 

**[1634.70s] English:** which is a quite different situation from the processes that go on in the minds of humans which  
**Translation:** 

**[1642.56s] English:** where they have to sort of function in changing environments and  
**Translation:** 

**[1646.70s] English:** they have emotions they have um um physical attributes for acquire for exploring their  
**Translation:** 

**[1658.04s] English:** environment um they have intuition they have desires um emotions and i don't see anything  
**Translation:** Vocabulary: attributes: 生理特征; intuition: 直觉

**[1669.78s] English:** in the current achievements of what's called ai that come close to that capability and i think it's  
**Translation:** 

**[1676.70s] English:** about they don't think there's any  
**Translation:** Vocabulary: capability: 能力

**[1677.98s] English:** so  
**Translation:** 

**[1686.18s] English:** um  
**Translation:** 

**[1690.38s] English:** yeah  
**Translation:** 

**[1690.76s] English:** uh  
**Translation:** 

**[1693.24s] English:** um  
**Translation:** 

**[1701.50s] English:** um  
**Translation:** 

**[1704.48s] English:** um  
**Translation:** 

**[1704.92s] English:** um  
**Translation:** 

**[1705.12s] English:** um  
**Translation:** 

**[1705.64s] English:** um  
**Translation:** 

**[1705.82s] English:** um  
**Translation:** 

**[1705.92s] English:** um  
**Translation:** 

**[1706.16s] English:** um  
**Translation:** 

**[1706.18s] English:** um  
**Translation:** 

**[1706.22s] English:** um  
**Translation:** 

**[1706.24s] English:** um  
**Translation:** 

**[1706.26s] English:** um  
**Translation:** 

**[1706.48s] English:** um  
**Translation:** 

**[1680.00s] English:** computer program which surpasses a six-month-old child in terms of comprehension of the world  
**Translation:** 

**[1688.72s] English:** do you think this complexity of human intelligence all the cognitive abilities  
**Translation:** Vocabulary: cognitive: 认知; comprehension: 理解; surpasses: 超越

**[1696.64s] English:** we have all the emotion do you think that could be reduced one day or just  
**Translation:** 

**[1701.78s] English:** fundamentally can it be reduced to a set of algorithms or an algorithm  
**Translation:** Vocabulary: algorithm: 算法; fundamentally: 从根本上

**[1706.26s] English:** so can a Turing machine achieve human level intelligence I am doubtful about that I guess  
**Translation:** 

**[1716.20s] English:** the argument in favor of it is that the human brain seems to achieve  
**Translation:** Vocabulary: doubtful: 怀疑

**[1723.98s] English:** what we call intelligence cognitive abilities of different kinds and if you buy the premise  
**Translation:** 

**[1733.08s] English:** that the human brain is just an enormous  
**Translation:** Vocabulary: premise: 前提

**[1736.24s] English:** interconnected set of switches so to speak then in principle you should be  
**Translation:** 

**[1742.72s] English:** able to diagnose what that interconnection structure is like  
**Translation:** Vocabulary: diagnose: 诊断; interconnected: 相互连接的; interconnection: 连接结构

**[1747.00s] English:** characterize the individual switches and build a simulation outside but why  
**Translation:** 

**[1755.92s] English:** that may be true in principle that cannot be the way we're eventually going  
**Translation:** Vocabulary: cannot: 不能; characterize: 描述; simulation: 模拟

**[1760.00s] English:** to tackle this problem it's you know you know  
**Translation:** 

**[1765.22s] English:** that's the way we're going to tackle this problem it's no you know that's  
**Translation:** 

**[1766.18s] English:** that's the way we're going to tackle this problem it's no you know that's  
**Translation:** 

**[1766.22s] English:** does not seem like a feasible way to go about it so there is however an  
**Translation:** Vocabulary: feasible: 可行的

**[1771.04s] English:** does not seem like a feasible way to go about it so there is however an  
**Translation:** 

**[1771.06s] English:** existence proof that if you believe that the brain is is just a network of  
**Translation:** 

**[1781.30s] English:** neurons operating by rules I guess you could say that that's an existence proof  
**Translation:** 

**[1786.52s] English:** of the ability to build the capabilities of a mechanism but it would be almost  
**Translation:** 

**[1794.34s] English:** of the mechanism but it would be almost impossible to acquire a  
**Translation:** 

**[1796.16s] English:** impossible to acquire a the information unless we got enough  
**Translation:** 

**[1800.00s] English:** the information unless we got enough  
**Translation:** 

**[1800.00s] English:** insight into the operation of the brain but there's so much mystery there do you think  
**Translation:** 

**[1805.28s] English:** what do you make of consciousness for example there's something as an example of something  
**Translation:** 

**[1810.88s] English:** we completely have no clue about the fact that we have this subjective experience right is it  
**Translation:** 

**[1816.08s] English:** possible that this network of uh this circuit of switches is able to create something like  
**Translation:** 

**[1823.28s] English:** consciousness to know to know its own identity yeah to know to know the algorithm to know itself  
**Translation:** Vocabulary: algorithm: 计算方法

**[1830.16s] English:** to know itself i think if you try to define that rigorously you'd have a lot of trouble yeah  
**Translation:** 

**[1839.28s] English:** so i know that there are many who  
**Translation:** Vocabulary: rigorously: 严格地

**[1846.32s] English:** believe that general intelligence can be  
**Translation:** 

**[1851.84s] English:** achieved and there are even some who are feel certain that the singularity will come and  
**Translation:** 

**[1859.76s] English:** we're  
**Translation:** 

**[1860.00s] English:** will be surpassed by the machines which will then learn more and more about themselves and  
**Translation:** Vocabulary: surpassed: 超越

**[1865.28s] English:** reduce humans to an inferior breed i am doubtful that this will ever be achieved  
**Translation:** 

**[1872.64s] English:** just for the fun of it could you linger on why  
**Translation:** Vocabulary: doubtful: 怀疑; inferior: 低等

**[1876.96s] English:** what's your intuition why you're doubtful so there are quite a few people that are extremely worried  
**Translation:** 

**[1882.80s] English:** about this uh existential threat of artificial intelligence of us being left behind by the super  
**Translation:** Vocabulary: existential: 存在主义的; intuition: 直觉

**[1889.76s] English:** intelligent new species what's your intuition why that's not quite likely just because  
**Translation:** 

**[1899.76s] English:** none of the achievements in speech or robotics or natural language processing or creation of  
**Translation:** 

**[1910.64s] English:** flexible computer assistance or any of that comes anywhere near close to that level of cognition  
**Translation:** 

**[1919.76s] English:** you  
**Translation:** Vocabulary: cognition: 认知

**[1920.00s] English:** What do you think about ideas of sort of, if we look at Moore's Law and exponential improvement to allow us, that would surprise us?  
**Translation:** 

**[1929.32s] English:** Sort of our intuition fall apart with exponential improvement because, I mean, we're not able to kind of, we kind of think in linear improvement.  
**Translation:** Vocabulary: exponential: 指数的

**[1937.98s] English:** Yeah.  
**Translation:** 

**[1938.20s] English:** We're not able to imagine a world that goes from the Mark I computer to an iPhone X.  
**Translation:** 

**[1946.20s] English:** Yeah.  
**Translation:** 

**[1946.40s] English:** So do you think we could be really surprised by the exponential growth?  
**Translation:** 

**[1953.58s] English:** Or on the flip side, is it possible that also intelligence is actually way, way, way, way harder, even with exponential improvement, to be able to crack?  
**Translation:** 

**[1966.86s] English:** I don't think any constant factor improvement could change things.  
**Translation:** 

**[1973.90s] English:** I mean, given our current context.  
**Translation:** 

**[1976.40s] English:** I mean, given the comprehension of how the, of what cognition requires, it seems to me that multiplying the speed of the switches by a factor of a thousand or a million will not be useful until we really understand the organizational principle behind the network of switches.  
**Translation:** Vocabulary: comprehension: 理解; multiplying: 增加

**[2000.86s] English:** Well, let's jump into the network of switches and talk about common interpretation.  
**Translation:** 

**[2006.40s] English:** So we can do some combinatorial algorithms, if we could.  
**Translation:** Vocabulary: combinatorial: 组合算法

**[2009.56s] English:** Let's step back for the very basics.  
**Translation:** 

**[2011.70s] English:** What are combinatorial algorithms?  
**Translation:** 

**[2013.64s] English:** What are some major examples of problems they aim to solve?  
**Translation:** 

**[2016.98s] English:** A combinatorial algorithm is one which deals with a system of discrete objects that can occupy various states or take on various values from,  
**Translation:** 

**[2035.32s] English:** from the,  
**Translation:** 

**[2035.50s] English:** from the,  
**Translation:** 

**[2036.40s] English:** discrete set of values.  
**Translation:** 

**[2040.00s] English:** and need to be arranged or selected in such a way  
**Translation:** Vocabulary: discrete: 离散的

**[2047.48s] English:** as to minimize some cost function  
**Translation:** 

**[2053.06s] English:** or to prove the existence of some combinatorial  
**Translation:** 

**[2058.32s] English:** configuration.  
**Translation:** 

**[2060.00s] English:** So an example would be coloring the vertices of a graph.  
**Translation:** Vocabulary: configuration: 配置; vertices: 顶点

**[2064.96s] English:** What's a graph?  
**Translation:** 

**[2067.24s] English:** Let's step back.  
**Translation:** 

**[2068.02s] English:** So it's fun to ask one of the greatest computer scientists  
**Translation:** 

**[2075.56s] English:** of all time the most basic questions  
**Translation:** 

**[2077.32s] English:** in the beginning of most books.  
**Translation:** 

**[2079.22s] English:** But for people who might not know, but in general,  
**Translation:** 

**[2082.00s] English:** how you think about it, what is a graph?  
**Translation:** 

**[2084.76s] English:** A graph, that's simple.  
**Translation:** 

**[2087.22s] English:** It's a set of points, certain pairs of which  
**Translation:** 

**[2091.24s] English:** are joined by lines called edges.  
**Translation:** 

**[2094.96s] English:** And they sort of represent the edges  
**Translation:** 

**[2098.02s] English:** in different applications, represent  
**Translation:** 

**[2100.54s] English:** the interconnections between discrete objects.  
**Translation:** 

**[2105.88s] English:** So they could be the interconnections  
**Translation:** Vocabulary: interconnections: 相互连接

**[2108.58s] English:** between switches in a digital circuit  
**Translation:** 

**[2112.42s] English:** or interconnections indicating the communication patterns  
**Translation:** 

**[2116.38s] English:** of a human community.  
**Translation:** 

**[2119.26s] English:** And they could be directed or undirected.  
**Translation:** 

**[2121.36s] English:** And then, as you've mentioned before, might have costs.  
**Translation:** 

**[2125.50s] English:** Right.  
**Translation:** 

**[2126.00s] English:** They can be directed or undirected.  
**Translation:** 

**[2127.40s] English:** Yeah.  
**Translation:** 

**[2128.02s] English:** It can be, you can think of them as, if you think,  
**Translation:** 

**[2132.70s] English:** if a graph were representing a communication network,  
**Translation:** 

**[2136.54s] English:** then the edge could be undirected,  
**Translation:** 

**[2138.70s] English:** meaning that information could flow along it  
**Translation:** 

**[2141.82s] English:** in both directions.  
**Translation:** 

**[2143.20s] English:** Or it could be directed with only one way of communication.  
**Translation:** 

**[2146.92s] English:** A road system is another example of a graph  
**Translation:** 

**[2149.74s] English:** with weights on the edges.  
**Translation:** 

**[2152.14s] English:** And then a lot of problems of optimizing  
**Translation:** 

**[2157.96s] English:** the efficiency of such a graph.  
**Translation:** 

**[2160.00s] English:** networks or learning about the performance of such networks are the object of combinatorial  
**Translation:** 

**[2170.56s] English:** algorithms.  
**Translation:** 

**[2171.56s] English:** So it could be scheduling classes at a school where the vertices, the nodes of the network  
**Translation:** 

**[2182.68s] English:** are the individual classes and the edges indicate the constraints which say that certain classes  
**Translation:** Vocabulary: constraints: 限制; vertices: 顶点

**[2190.00s] English:** cannot take place at the same time or certain teachers are available only for certain classes,  
**Translation:** 

**[2196.78s] English:** etc.  
**Translation:** Vocabulary: cannot: 不能

**[2198.38s] English:** Or I talked earlier about the assignment problem of matching the boys with the girls where  
**Translation:** 

**[2208.26s] English:** you have the error graph with an edge from each boy to each girl with a weight indicating  
**Translation:** 

**[2216.20s] English:** the cost.  
**Translation:** 

**[2218.20s] English:** Or in...  
**Translation:** 

**[2220.00s] English:** logical design of computers, you might want to find a set of so-called gates, switches  
**Translation:** 

**[2229.08s] English:** that perform logical functions which can be interconnected to realize some function.  
**Translation:** Vocabulary: interconnected: 相互连接

**[2235.24s] English:** So you might ask, how many gates do you need in order to...  
**Translation:** 

**[2245.38s] English:** for a circuit to...  
**Translation:** 

**[2249.34s] English:** give a yes output if at least a given number of its inputs are ones and no if fewer are  
**Translation:** 

**[2261.58s] English:** present.  
**Translation:** 

**[2262.58s] English:** My favorite is probably all the work with network flows.  
**Translation:** 

**[2266.68s] English:** So anytime you have...  
**Translation:** Vocabulary: anytime: 任何时间

**[2269.26s] English:** I don't know why it's so compelling, but there's something just beautiful about it.  
**Translation:** 

**[2272.42s] English:** It seems like there's so many applications and communication networks...  
**Translation:** Vocabulary: compelling: 极具吸引力的

**[2276.42s] English:** Mm-hmm.  
**Translation:** 

**[2277.46s] English:** ...in traffic...  
**Translation:** 

**[2278.42s] English:** Yeah.  
**Translation:** 

**[2279.22s] English:** ...in the world.  
**Translation:** 

**[2280.22s] English:** Right.  
**Translation:** 

**[2280.00s] English:** flow that you can map into these and then you can think of pipes and water going through pipes and  
**Translation:** 

**[2285.52s] English:** you can optimize it in different ways there's something always visually and intellectually  
**Translation:** 

**[2291.04s] English:** compelling to me about it and of course you've done work there yeah yeah so um so there  
**Translation:** Vocabulary: intellectually: 智力上; optimize: 优化

**[2299.12s] English:** the edges represent uh channels along which some commodity can flow it might be  
**Translation:** 

**[2304.96s] English:** gas it might be water it might be information maybe supply chain as well like products  
**Translation:** Vocabulary: commodity: 商品

**[2313.44s] English:** being products flowing from one operation to another yeah and the edges have a capacity  
**Translation:** 

**[2320.16s] English:** which is the rate at which the commodity can flow and a central problem is to determine  
**Translation:** 

**[2329.04s] English:** given a network of these channels in this case the edges are communication channels  
**Translation:** 

**[2334.96s] English:** um the uh the challenge is to find the maximum rate at which the  
**Translation:** 

**[2343.28s] English:** information can flow along these channels to get from a source to a destination and  
**Translation:** 

**[2349.60s] English:** that's that's a fundamental combinatorial problem that i i've worked on uh jointly with  
**Translation:** Vocabulary: combinatorial: 组合的

**[2357.28s] English:** the scientist jack edmunds we i think we're the first to give a formal proof that  
**Translation:** 

**[2363.60s] English:** uh this maximum  
**Translation:** 

**[2364.96s] English:** flow problem through a network can be solved in polynomial time which uh i remember the first  
**Translation:** 

**[2372.00s] English:** time i learned that just learning that in um maybe even grad school i don't think it was even  
**Translation:** 

**[2380.48s] English:** undergrad no algorithm yeah do network flows get taught in in um basic algorithms courses  
**Translation:** 

**[2390.08s] English:** yes probably okay so yeah i've i remember being very surprised that max flow is a  
**Translation:** Vocabulary: algorithm: 算法; undergrad: 本科生

**[2394.96s] English:** polynomial time algorithm yeah that there's a nice fast algorithm that solves max flow  
**Translation:** 

**[2400.00s] English:** But so there is an algorithm named after you, an admins, the admin carp algorithm for max flow.  
**Translation:** Vocabulary: admin: 管理员; polynomial: 多项式

**[2408.46s] English:** So what was it like tackling that problem and trying to arrive at a polynomial time solution?  
**Translation:** 

**[2415.64s] English:** And maybe you can describe the algorithm.  
**Translation:** Vocabulary: tackling: 应对

**[2417.26s] English:** Maybe you can describe what's the running time complexity that you showed.  
**Translation:** 

**[2420.72s] English:** Yeah.  
**Translation:** 

**[2421.60s] English:** Well, first of all, what is a polynomial time algorithm?  
**Translation:** 

**[2425.38s] English:** Perhaps we could discuss that.  
**Translation:** 

**[2428.26s] English:** So, yeah, let's actually just even, yeah, what is algorithmic complexity?  
**Translation:** 

**[2434.16s] English:** What are the major classes of algorithm complexity?  
**Translation:** Vocabulary: algorithmic: 算法相关的; complexity: 复杂度

**[2438.16s] English:** So in a problem like the assignment problem or scheduling schools or any of these applications,  
**Translation:** 

**[2448.16s] English:** you have a set of input data, which might, for example, be,  
**Translation:** 

**[2456.50s] English:** um,  
**Translation:** 

**[2457.32s] English:** uh,  
**Translation:** 

**[2458.26s] English:** a set of vertices connected by edges with the end you're given for each edge,  
**Translation:** 

**[2464.68s] English:** the capacity of the edge.  
**Translation:** Vocabulary: vertices: 顶点

**[2467.16s] English:** And, um,  
**Translation:** 

**[2468.68s] English:** you have,  
**Translation:** 

**[2469.44s] English:** um,  
**Translation:** 

**[2470.14s] English:** algorithms,  
**Translation:** 

**[2471.02s] English:** which are,  
**Translation:** 

**[2471.74s] English:** uh,  
**Translation:** 

**[2472.20s] English:** think of them as computer programs with operations such as addition,  
**Translation:** 

**[2477.64s] English:** subtraction,  
**Translation:** Vocabulary: subtraction: 减法

**[2478.62s] English:** multiplication,  
**Translation:** 

**[2479.38s] English:** division,  
**Translation:** Vocabulary: multiplication: 乘法

**[2480.00s] English:** comparison of numbers and so on.  
**Translation:** 

**[2482.80s] English:** Um,  
**Translation:** 

**[2483.36s] English:** and you're trying to construct an algorithm,  
**Translation:** 

**[2486.96s] English:** um,  
**Translation:** 

**[2488.26s] English:** based on those operations,  
**Translation:** 

**[2492.50s] English:** which will determine in a minimum number of computational steps,  
**Translation:** Vocabulary: computational: 计算的

**[2497.18s] English:** the answer to the problem.  
**Translation:** 

**[2498.40s] English:** In this case,  
**Translation:** 

**[2499.02s] English:** the computational step is one of those operations.  
**Translation:** 

**[2503.30s] English:** And the answer to the problem is,  
**Translation:** 

**[2505.36s] English:** let's say the,  
**Translation:** 

**[2506.50s] English:** um,  
**Translation:** 

**[2507.64s] English:** the configuration of the network that carries the maximum amount of flow.  
**Translation:** 

**[2514.76s] English:** And an algorithm is said to run in polynomial time.  
**Translation:** Vocabulary: algorithm: 算法; configuration: 配置

**[2518.26s] English:** It,  
**Translation:** 

**[2520.14s] English:** if,  
**Translation:** 

**[2521.06s] English:** uh,  
**Translation:** 

**[2521.16s] English:** if you want to say actually a cycle where,  
**Translation:** 

**[2524.50s] English:** uh,  
**Translation:** 

**[2526.20s] English:** if,  
**Translation:** 

**[2526.60s] English:** if,  
**Translation:** 

**[2528.62s] English:** if you,  
**Translation:** 

**[2529.80s] English:** if,  
**Translation:** 

**[2531.64s] English:** um,  
**Translation:** 

**[2532.56s] English:** if you don't actually see the equal of the percentage of flow records in the wake ofати  
**Translation:** 

**[2535.72s] English:** effect,  
**Translation:** 

**[2536.12s] English:** you want to do a test,  
**Translation:** 

**[2538.24s] English:** but the result,  
**Translation:** 

**[2538.66s] English:** uh,  
**Translation:** 

**[2538.96s] English:** is that,  
**Translation:** 

**[2540.24s] English:** um,  
**Translation:** 

**[2540.64s] English:** these graphs are distinct Lowell here.  
**Translation:** Vocabulary: lowell: 洛威尔

**[2542.50s] English:** And the,  
**Translation:** 

**[2543.32s] English:** uh,  
**Translation:** 

**[2544.16s] English:** these graphs are distinct Lowell here.  
**Translation:** 

**[2546.14s] English:** Uh,  
**Translation:** 

**[2546.50s] English:** these graphs are distinct lowell here.  
**Translation:** 

**[2547.34s] English:** I'm going to use style,  
**Translation:** 

**[2547.80s] English:** uh,  
**Translation:** 

**[2520.00s] English:** If, as a function of the size of the input, the number of vertices, the number of edges, and so on,  
**Translation:** 

**[2528.66s] English:** the number of basic computational steps grows only on some fixed power of that size.  
**Translation:** 

**[2536.26s] English:** A linear algorithm would execute a number of steps linearly proportional to the size.  
**Translation:** 

**[2544.58s] English:** Quadratic algorithm would be steps proportional to the square of the size, and so on.  
**Translation:** 

**[2550.00s] English:** And algorithms whose running time is bounded by some fixed power of the size are called polynomial algorithms.  
**Translation:** Vocabulary: quadratic: 平方的

**[2560.02s] English:** And that's supposed to be a relatively fast class of algorithms.  
**Translation:** 

**[2564.78s] English:** That's right. Theoreticians take that to be the definition of an algorithm being efficient.  
**Translation:** Vocabulary: theoreticians: 理论学家

**[2572.98s] English:** And we're interested in which problems can be solved by such efficiency.  
**Translation:** 

**[2580.86s] English:** One can argue whether that's the right definition of efficient,  
**Translation:** 

**[2585.76s] English:** because you could have an algorithm whose running time is the 10,000th power of the size of the input,  
**Translation:** 

**[2592.52s] English:** and that wouldn't be really efficient.  
**Translation:** 

**[2594.82s] English:** And in practice, it's oftentimes reducing from an n-squared algorithm to an n log n or a linear time  
**Translation:** 

**[2603.58s] English:** is practically the jump that you want to make to allow a real-world system,  
**Translation:** Vocabulary: oftentimes: 经常

**[2610.00s] English:** to solve a problem.  
**Translation:** 

**[2611.12s] English:** Yeah, that's also true, because especially as we get very large networks,  
**Translation:** 

**[2615.78s] English:** the size can be in the millions, and then anything above n log n,  
**Translation:** 

**[2623.72s] English:** where n is the size, would be too much for a practical solution.  
**Translation:** 

**[2629.94s] English:** Okay, so that's polynomial time algorithms.  
**Translation:** 

**[2632.42s] English:** What other classes of algorithms are there?  
**Translation:** 

**[2636.16s] English:** What's...  
**Translation:** 

**[2637.32s] English:** So that usually they...  
**Translation:** 

**[2639.06s] English:** They designate...  
**Translation:** 

**[2640.00s] English:** eight polynomials of the letter p yeah there's also np np complete and np hard yeah so can you  
**Translation:** 

**[2647.58s] English:** try to disentangle those and by trying to define them simply right so a polynomial time algorithm  
**Translation:** 

**[2656.46s] English:** is one which whose running time is bounded by a polynomial in the size of the input  
**Translation:** Vocabulary: algorithm: 算法; disentangle: 理清; polynomial: 多项式

**[2662.44s] English:** uh there's then there's that the class of such algorithms is called p in the worst case by the  
**Translation:** 

**[2670.40s] English:** way we should say right yeah so for every case of the problem and that's very important that  
**Translation:** 

**[2674.50s] English:** in this theory um when we measure the complexity of an algorithm we really measure the number of  
**Translation:** 

**[2684.64s] English:** the growth of the number of steps in the worst case so you may have an algorithm that  
**Translation:** 

**[2690.52s] English:** run  
**Translation:** 

**[2692.42s] English:** very rapidly in most cases but if there's any case where it gets into a very long computation  
**Translation:** 

**[2699.28s] English:** that would increase the computational complexity by this measure and that's a very important issue  
**Translation:** 

**[2707.30s] English:** because there are as we may discuss later there are some very important algorithms which don't  
**Translation:** 

**[2713.84s] English:** have a good standing from the point of view of their worst case performance and yet are very  
**Translation:** 

**[2718.96s] English:** effective so so uh  
**Translation:** 

**[2722.42s] English:** theoreticians are interested in p the class of problem solvable in polynomial time  
**Translation:** 

**[2727.20s] English:** then there's um uh np which is the class of problems  
**Translation:** Vocabulary: solvable: 可解决的

**[2734.18s] English:** which may be hard to solve but where the where where when confronted with a solution  
**Translation:** 

**[2743.40s] English:** you can check it in polynomial time let me give you an example there  
**Translation:** 

**[2748.68s] English:** so if we look at the assignment problem uh  
**Translation:** 

**[2752.42s] English:** So you have n boys, you have n girls, the number of numbers that you need to write down to specify.  
**Translation:** 

**[2760.00s] English:** problem instances n squared. And the question is, how many steps are needed to solve it?  
**Translation:** 

**[2771.52s] English:** And Jack Edmonds and I were the first to show that it could be done in time n cubed.  
**Translation:** Vocabulary: edmonds: 埃德蒙兹

**[2780.16s] English:** Earlier algorithms required n to the fourth.  
**Translation:** 

**[2783.84s] English:** So as a polynomial function of the size of the input, this is a fast algorithm.  
**Translation:** Vocabulary: algorithm: 算法; polynomial: 多项式

**[2790.00s] English:** Now to illustrate the class np, the question is, how long would it take to  
**Translation:** 

**[2798.16s] English:** verify that a solution is optimal? So for example, if the input was a graph, we might want to  
**Translation:** Vocabulary: illustrate: 举例说明; optimal: 最佳的; verify: 验证

**[2810.80s] English:** find the largest clique in the graph. Or a clique is a set of vertices such that any vertex,  
**Translation:** 

**[2818.72s] English:** each vertex in the set,  
**Translation:** Vocabulary: clique: 完整子集; vertex: 顶点; vertices: 顶点

**[2820.00s] English:** is adjacent to each of the others. So the clique is a complete subgraph.  
**Translation:** 

**[2827.84s] English:** Yeah, so if it's a Facebook social network, everybody's friends  
**Translation:** Vocabulary: subgraph: 子图

**[2832.96s] English:** with everybody else. It's a close clique.  
**Translation:** 

**[2834.80s] English:** That would be what's called a complete graph, it would be.  
**Translation:** 

**[2837.60s] English:** No, I mean, within that clique.  
**Translation:** 

**[2839.92s] English:** Within that clique, yeah. They're all friends.  
**Translation:** 

**[2845.36s] English:** So a complete graph is when...  
**Translation:** 

**[2846.96s] English:** Everybody is friendly.  
**Translation:** 

**[2848.56s] English:** Everybody is friends with everybody.  
**Translation:** 

**[2849.16s] English:** Everybody is friendly.  
**Translation:** 

**[2849.44s] English:** Everybody is friendly.  
**Translation:** 

**[2849.76s] English:** Everybody is friends with everybody.  
**Translation:** 

**[2850.32s] English:** Yeah. So the problem might be to determine whether in a given graph there exists a  
**Translation:** 

**[2858.72s] English:** clique of a certain size. Now that turns out to be a very hard problem. But if somebody hands you a  
**Translation:** 

**[2868.16s] English:** clique and asks you to check whether it is... Hands you a set of vertices and asks you to check  
**Translation:** 

**[2876.08s] English:** whether it's a clique, you could do that. But if somebody hands you a set of vertices and asks you  
**Translation:** 

**[2879.20s] English:** to check whether it's a clique, you could do that.  
**Translation:** 

**[2880.00s] English:** simply by exhaustively looking at all of the edges  
**Translation:** 

**[2882.94s] English:** between the vertices in the clique  
**Translation:** 

**[2885.24s] English:** and verifying that they're all there.  
**Translation:** Vocabulary: verifying: 验证

**[2888.06s] English:** And that's a polynomial time algorithm.  
**Translation:** 

**[2890.44s] English:** That's a polynomial.  
**Translation:** 

**[2891.58s] English:** So the problem of finding the clique  
**Translation:** 

**[2897.70s] English:** appears to be extremely hard.  
**Translation:** 

**[2899.30s] English:** But the problem of verifying a clique  
**Translation:** 

**[2902.98s] English:** to see if it reaches a target number of vertices  
**Translation:** 

**[2908.28s] English:** is easy to verify.  
**Translation:** 

**[2911.74s] English:** So finding the clique is hard.  
**Translation:** 

**[2914.22s] English:** Checking it is easy.  
**Translation:** 

**[2915.78s] English:** Problems of that nature are called  
**Translation:** 

**[2919.02s] English:** non-deterministic polynomial time algorithms.  
**Translation:** 

**[2922.50s] English:** And that's the class NP.  
**Translation:** 

**[2925.72s] English:** And what about NP-complete and NP-hard?  
**Translation:** 

**[2928.38s] English:** OK.  
**Translation:** 

**[2929.60s] English:** Let's talk about problems where you're getting a yes or no  
**Translation:** 

**[2933.18s] English:** answer rather than a numerical value.  
**Translation:** Vocabulary: numerical: 数值的

**[2935.46s] English:** So either there is a perfect.  
**Translation:** 

**[2938.26s] English:** matching of the boys with the girls or there isn't.  
**Translation:** 

**[2944.20s] English:** It's clear that every problem in P is also in NP.  
**Translation:** 

**[2950.56s] English:** If you can solve the problem exactly,  
**Translation:** 

**[2952.60s] English:** then you can certainly verify the solution.  
**Translation:** 

**[2957.56s] English:** On the other hand, there are problems in the class NP.  
**Translation:** Vocabulary: verify: 验证

**[2963.82s] English:** This is the class of problems that are easy to check,  
**Translation:** 

**[2967.16s] English:** although they may be hard to solve.  
**Translation:** 

**[2967.78s] English:** OK.  
**Translation:** 

**[2968.18s] English:** OK.  
**Translation:** 

**[2968.22s] English:** OK.  
**Translation:** 

**[2968.26s] English:** OK.  
**Translation:** 

**[2968.76s] English:** OK.  
**Translation:** 

**[2969.26s] English:** OK.  
**Translation:** 

**[2969.76s] English:** It's not at all clear that problems in NP lie in P.  
**Translation:** 

**[2973.78s] English:** So for example, if we're looking at scheduling classes  
**Translation:** 

**[2977.48s] English:** at a school, the fact that you can verify  
**Translation:** 

**[2983.62s] English:** when handed a schedule for the school,  
**Translation:** 

**[2985.78s] English:** whether it meets all the requirements,  
**Translation:** 

**[2987.88s] English:** it doesn't mean that you can find the schedule rapidly.  
**Translation:** 

**[2991.40s] English:** So intuitively, NP, non-deterministic polynomial,  
**Translation:** 

**[2995.32s] English:** checking rather than finding.  
**Translation:** Vocabulary: intuitively: 直觉上; polynomial: 多项式

**[2996.64s] English:** is going to be  
**Translation:** 

**[3000.00s] English:** harder than is going to include is easier checking is easier and therefore the class  
**Translation:** 

**[3008.10s] English:** of problems that can be checked appears to be much larger than the class of problems that can  
**Translation:** 

**[3013.40s] English:** be solved and then you keep adding appears to and uh sort of these uh additional words that  
**Translation:** 

**[3021.64s] English:** designate that we don't know for sure yet we don't know for sure so the theoretical question  
**Translation:** 

**[3026.86s] English:** which is considered to be the most central problem in theoretical computer science or at  
**Translation:** 

**[3033.08s] English:** least computational complexity theory combinatorial algorithm theory the question is whether p is  
**Translation:** 

**[3041.42s] English:** equal to np if p were equal to np it would be amazing it would mean that um every  
**Translation:** Vocabulary: algorithm: 算法; combinatorial: 组合; complexity: 复杂性; computational: 计算

**[3049.84s] English:** problem where a solution can be rapidly checked  
**Translation:** 

**[3056.86s] English:** can actually be solved in polynomial time we don't really believe that's true  
**Translation:** 

**[3062.54s] English:** if you're scheduling classes at a school it's uh we expect that if somebody hands you a  
**Translation:** 

**[3071.34s] English:** satisfying schedule you can verify that it works that doesn't mean that you should be able to find  
**Translation:** 

**[3077.54s] English:** such a schedule so intuitively np encompasses a lot more problems than p so can uh we take  
**Translation:** 

**[3086.82s] English:** a look at the question and we'll see if we can find a solution to this problem  
**Translation:** Vocabulary: encompasses: 包括

**[3086.86s] English:** small tangent and break apart that intuition so do you first of all think that the biggest  
**Translation:** 

**[3094.06s] English:** sort of open problem in computer science maybe mathematics is whether p equals np do you think  
**Translation:** Vocabulary: intuition: 直觉; tangent: 旁白

**[3100.72s] English:** p equals np or do you think p is not equal to np if you had to bet all your money on it  
**Translation:** 

**[3107.94s] English:** i would bet that p is unequal to np simply because there are problems that have been  
**Translation:** Vocabulary: unequal: 不相等

**[3114.60s] English:** around for centuries and have been studied in the past and i think that's a good question  
**Translation:** 

**[3116.86s] English:** i would bet that p is unequal to np if you had to bet all your money on it  
**Translation:** 

**[3120.00s] English:** the last 50 years since the p versus np was stated and no polynomial time algorithms have  
**Translation:** 

**[3129.52s] English:** been found for these easy to check problems so one one example is a problem that goes back  
**Translation:** 

**[3137.44s] English:** to the mathematician gauss who was interested in factoring large numbers so we know what a number  
**Translation:** 

**[3147.12s] English:** is prime if it doesn't if it cannot be written as the product of two or more numbers unequal to one  
**Translation:** Vocabulary: cannot: 不能; factoring: 分解; mathematician: 数学家

**[3156.24s] English:** so if we can factor the number like 91 it's 7 times 13. um but if i give you  
**Translation:** 

**[3167.92s] English:** 20 digit or 30 digit numbers you're probably going to be at a loss to  
**Translation:** Vocabulary: digit: 位数

**[3173.04s] English:** have any idea whether they can be factored  
**Translation:** 

**[3176.72s] English:** so  
**Translation:** Vocabulary: factored: 分解

**[3177.12s] English:** the problem of factoring very large numbers is does not appear to have an efficient solution  
**Translation:** 

**[3186.80s] English:** but once you have found the factors express the number as a product the two  
**Translation:** 

**[3194.96s] English:** smaller numbers you can quickly verify that they are factors of the number  
**Translation:** 

**[3199.76s] English:** and your intuition is a lot of people finding you know  
**Translation:** Vocabulary: verify: 验证

**[3202.80s] English:** this a lot of brilliant people have tried to find algorithms for this one particular problem  
**Translation:** 

**[3206.72s] English:** there's many others like it that are really well studied and it would be great  
**Translation:** 

**[3211.44s] English:** to find an efficient algorithm for right and in fact um we have  
**Translation:** 

**[3219.36s] English:** some results that i was instrumental in obtaining following up on work by the mathematician stephen  
**Translation:** Vocabulary: algorithm: 算法

**[3226.24s] English:** cook to show that within the class np of easy to check problems there's a huge number of problems  
**Translation:** 

**[3236.56s] English:** that are equivalent in the sense that either  
**Translation:** 

**[3240.00s] English:** all of them or none of them lie in P.  
**Translation:** 

**[3243.22s] English:** And this happens only if P is equal to NP.  
**Translation:** 

**[3246.42s] English:** So if P is unequal to NP, we would also  
**Translation:** 

**[3249.94s] English:** know that virtually all the standard combinatorial  
**Translation:** Vocabulary: combinatorial: 组合的; unequal: 不等的

**[3258.60s] English:** problems, if P is unequal to NP, none of them  
**Translation:** 

**[3263.14s] English:** can be solved in polynomial time.  
**Translation:** 

**[3265.90s] English:** Can you explain how that's possible to tie together  
**Translation:** 

**[3269.44s] English:** so many problems in a nice bunch,  
**Translation:** 

**[3272.26s] English:** that if one is proven to be efficient, then all are?  
**Translation:** 

**[3276.58s] English:** The first and most important stage of progress  
**Translation:** 

**[3280.60s] English:** was a result by Stephen Cook, who  
**Translation:** 

**[3287.32s] English:** showed that a certain problem called the satisfiability  
**Translation:** 

**[3291.28s] English:** problem of propositional logic is as hard as any problem  
**Translation:** 

**[3298.24s] English:** in the class P.  
**Translation:** Vocabulary: propositional: 命题的

**[3299.44s] English:** So the propositional logic problem  
**Translation:** 

**[3303.04s] English:** is expressed in terms of expressions involving  
**Translation:** 

**[3308.98s] English:** the logical operations AND, OR, and NOT operating on variables  
**Translation:** 

**[3316.84s] English:** that can be either true or false.  
**Translation:** 

**[3319.28s] English:** So an instance of the problem would be some formula  
**Translation:** 

**[3324.52s] English:** involving AND, OR, and NOT, and the question would  
**Translation:** 

**[3329.24s] English:** be whether there is an assignment of truth values  
**Translation:** 

**[3332.48s] English:** to the variables in the problem that  
**Translation:** 

**[3335.06s] English:** would make the formula true.  
**Translation:** 

**[3337.46s] English:** So for example, if I take the formula A, OR, B, and A,  
**Translation:** 

**[3343.52s] English:** OR, NOT, B, and NOT, A, OR, B, and NOT, A, OR, NOT, B,  
**Translation:** 

**[3349.28s] English:** and take the conjunction of all four of those so-called  
**Translation:** Vocabulary: conjunction: 联合

**[3353.16s] English:** expressions, you can determine that no assignment of truth  
**Translation:** 

**[3358.48s] English:** values to the variables  
**Translation:** 

**[3360.00s] English:** A and B will allow that conjunction of what are called clauses to be true.  
**Translation:** 

**[3368.88s] English:** So that's an example of a formula in propositional logic involving expressions based on the operations and, or, and not.  
**Translation:** 

**[3383.30s] English:** That's an example of a problem which is not satisfiable.  
**Translation:** 

**[3387.10s] English:** There is no solution that satisfies all of those constraints.  
**Translation:** Vocabulary: constraints: 限制条件

**[3391.24s] English:** And that's like one of the cleanest and fundamental problems in computer science.  
**Translation:** 

**[3395.30s] English:** It's like a nice statement of a really hard problem.  
**Translation:** 

**[3397.68s] English:** It's a nice statement of a really hard problem.  
**Translation:** 

**[3400.12s] English:** And what Cook showed is that every problem in NP can be re-expressed as an instance of the satisfiability problem.  
**Translation:** 

**[3416.30s] English:** So,  
**Translation:** 

**[3417.10s] English:** to do that,  
**Translation:** 

**[3418.48s] English:** he used the observation that a very simple abstract machine called the Turing machine can be used to describe any algorithm.  
**Translation:** 

**[3434.00s] English:** An algorithm for any realistic computer can be translated into an equivalent algorithm on one of these Turing machines,  
**Translation:** Vocabulary: algorithm: 算法; turing: 图灵机

**[3445.70s] English:** which are extremely simple.  
**Translation:** 

**[3447.10s] English:** So a Turing machine,  
**Translation:** 

**[3448.78s] English:** there's a tape and you can walk along that tape and you have basic instructions,  
**Translation:** 

**[3455.56s] English:** a finite list of instructions,  
**Translation:** Vocabulary: finite: 有限的

**[3457.66s] English:** which say,  
**Translation:** 

**[3458.48s] English:** which say if you're reading a particular symbol on the tape and you're in a particular state,  
**Translation:** 

**[3465.34s] English:** then you can move to a different state and change the state of the number that you are,  
**Translation:** 

**[3471.96s] English:** the element that you were looking at,  
**Translation:** 

**[3473.58s] English:** the cell of the tape that you were looking at.  
**Translation:** 

**[3475.50s] English:** And that was like a metaphor.  
**Translation:** Vocabulary: metaphor: 比喻

**[3476.92s] English:** And a mathematical construct that Turing put together to,  
**Translation:** 

**[3480.00s] English:** Represent all possible computation.  
**Translation:** Vocabulary: computation: 计算; mathematical: 数学的

**[3482.14s] English:** All possible computation.  
**Translation:** 

**[3483.38s] English:** Now, one of these so-called Turing machines is too simple to be useful in practice.  
**Translation:** 

**[3489.22s] English:** But for theoretical purposes, we can depend on the fact that an algorithm for any computer can be translated into one that would run on a Turing machine.  
**Translation:** 

**[3501.06s] English:** And then using that fact, he could sort of describe any possible non-deterministic polynomial time algorithm.  
**Translation:** Vocabulary: polynomial: 多项式

**[3515.48s] English:** Any algorithm for a problem in P could be expressed as a sequence of moves of the Turing machine described in terms of reading a symbol on the tape.  
**Translation:** 

**[3531.06s] English:** While you're in a given state and moving to a new state and leaving behind a new symbol.  
**Translation:** 

**[3540.06s] English:** And given that fact that any non-deterministic polynomial time algorithm can be described by a list of such instructions, you could translate the problem into the language of the satisfiability problem.  
**Translation:** 

**[3558.76s] English:** Is that amazing to you, by the way?  
**Translation:** 

**[3560.34s] English:** If you take yourself back when you were first thinking about this space of problems, how amazing is that?  
**Translation:** 

**[3566.56s] English:** It's astonishing.  
**Translation:** Vocabulary: astonishing: 令人惊讶的

**[3567.54s] English:** When you look at Cook's proof, it's not too difficult to sort of figure out why this is so.  
**Translation:** 

**[3578.44s] English:** But the implications are staggering.  
**Translation:** Vocabulary: staggering: 令人震惊的

**[3581.90s] English:** It tells us that this, of all the problems in P, all the problems where solutions are easy to check,  
**Translation:** 

**[3589.26s] English:** they can.  
**Translation:** 

**[3590.34s] English:** They can all be rewritten in terms of the satisfiability problem.  
**Translation:** 

**[3597.58s] English:** Yes.  
**Translation:** Vocabulary: rewritten: 重新表述

**[3600.00s] English:** In adding so much more weight to the P equals NP question,  
**Translation:** 

**[3606.78s] English:** because all it takes is to show that one algorithm in this class.  
**Translation:** Vocabulary: algorithm: 算法

**[3611.16s] English:** So the P versus NP can be re-expressed as simply asking  
**Translation:** 

**[3615.22s] English:** whether the satisfiability problem of propositional logic  
**Translation:** Vocabulary: propositional: 命题的

**[3618.90s] English:** is solvable in polynomial time.  
**Translation:** 

**[3623.22s] English:** But there's more.  
**Translation:** Vocabulary: polynomial: 多项式

**[3624.86s] English:** I encountered Cook's paper when he published it in a conference in 1971.  
**Translation:** 

**[3634.04s] English:** Yeah, so when I saw Cook's paper and saw this reduction  
**Translation:** Vocabulary: encountered: 遇到

**[3640.46s] English:** of each of the problems in NP by a uniform method  
**Translation:** 

**[3645.44s] English:** to the satisfiability problem of propositional logic,  
**Translation:** 

**[3651.20s] English:** that meant that the satisfiability problem was,  
**Translation:** 

**[3654.86s] English:** was a universal combinatorial problem.  
**Translation:** 

**[3659.30s] English:** And it occurred to me, through experience I had had  
**Translation:** 

**[3664.02s] English:** in trying to solve other combinatorial problems,  
**Translation:** Vocabulary: combinatorial: 组合的

**[3667.00s] English:** that there were many other problems  
**Translation:** 

**[3669.88s] English:** which seemed to have that universal structure.  
**Translation:** 

**[3675.94s] English:** And so I began looking for reductions  
**Translation:** 

**[3680.86s] English:** from the satisfiability  
**Translation:** 

**[3683.14s] English:** to the universal problem.  
**Translation:** 

**[3684.84s] English:** And it's just that,  
**Translation:** 

**[3687.00s] English:** there are other problems.  
**Translation:** 

**[3690.16s] English:** One of the other problems would be  
**Translation:** 

**[3693.04s] English:** the so-called integer programming problem of  
**Translation:** 

**[3697.40s] English:** solving a,  
**Translation:** 

**[3698.60s] English:** determining whether there's a solution to  
**Translation:** 

**[3702.46s] English:** a set of linear inequalities  
**Translation:** Vocabulary: inequalities: 不等式

**[3704.78s] English:** involving integer variables.  
**Translation:** 

**[3707.84s] English:** Just like linear programming,  
**Translation:** Vocabulary: integer: 整数

**[3709.20s] English:** but there's a constraint that the variables must remain integers.  
**Translation:** 

**[3713.24s] English:** Integers.  
**Translation:** Vocabulary: constraint: 限制; integers: 整数

**[3714.04s] English:** Integers. Integers, in fact, must remain integers. Integers, in fact, must remain because,  
**Translation:** 

**[3714.16s] English:** Integers, in fact, must remain because,  
**Translation:** 

**[3714.84s] English:** be the 0 or 1. It could only take on those values. And that makes the problem much harder.  
**Translation:** 

**[3720.00s] English:** yes that makes the problem much harder and it was not difficult to show that the satisfiability  
**Translation:** 

**[3729.22s] English:** problem can be restated as an integer programming problem so can you pause on that was that one of  
**Translation:** 

**[3735.80s] English:** the first problem mappings that you tried to do and how hard is that mapping you said it wasn't  
**Translation:** Vocabulary: restated: 重新表述

**[3740.98s] English:** hard to show but you know that's a that's a big leap it is a big leap yeah well let me let me give  
**Translation:** 

**[3750.74s] English:** you another example another problem in NP is whether a graph contains a clique of a given size  
**Translation:** Vocabulary: clique: 团块

**[3759.30s] English:** and now the question is can we reduce the propositional logic problem  
**Translation:** 

**[3770.98s] English:** to the problem of whether there's a clique of a certain size well if you look at the propositional  
**Translation:** Vocabulary: propositional: 命题的

**[3780.40s] English:** logic problem it can be expressed as a number of clauses each of which is a of the form a or B or  
**Translation:** 

**[3794.56s] English:** C where a is either one of the variables in the problem or the negation of one of the variables  
**Translation:** Vocabulary: negation: 否定

**[3800.48s] English:** you  
**Translation:** 

**[3800.98s] English:** and the an instance of the propositional logic problem can be rewritten using operations of  
**Translation:** Vocabulary: rewritten: 重写

**[3813.96s] English:** Boolean logic can be re be written as the conjunction of a set of clauses the end of a  
**Translation:** 

**[3822.34s] English:** set of ors where each clause is a disjunction an or of variables or negated variables  
**Translation:** Vocabulary: boolean: 布尔; conjunction: 合取; disjunction: 析取; negated: 否定

**[3830.98s] English:** so the question of in the satisfiability  
**Translation:** 

**[3839.96s] English:** you  
**Translation:** 

**[3842.02s] English:** you  
**Translation:** 

**[3843.96s] English:** you  
**Translation:** 

**[3845.96s] English:** you  
**Translation:** 

**[3847.96s] English:** you  
**Translation:** 

**[3849.96s] English:** you  
**Translation:** 

**[3851.96s] English:** you  
**Translation:** 

**[3853.96s] English:** you  
**Translation:** 

**[3855.96s] English:** you  
**Translation:** 

**[3857.96s] English:** you  
**Translation:** 

**[3859.96s] English:** you  
**Translation:** 

**[3840.00s] English:** problem is whether those clauses can be simultaneously satisfied. Now, to satisfy  
**Translation:** 

**[3847.94s] English:** all those clauses, you have to find one of the terms in each clause which is going to be true  
**Translation:** 

**[3857.94s] English:** in your truth assignment, but you can't make the same variable both true and false. So, if you have  
**Translation:** 

**[3865.56s] English:** the variable a in one clause, and you want to satisfy that clause by making a true, you can't  
**Translation:** 

**[3874.66s] English:** also make the complement of a true in some other clause. And so, the goal is to make every single  
**Translation:** 

**[3881.22s] English:** clause true if it's possible to satisfy this, and the way you make it true is at least...  
**Translation:** 

**[3888.36s] English:** One term in the clause must be true. Got it.  
**Translation:** 

**[3893.84s] English:** So, now we...  
**Translation:** 

**[3895.56s] English:** To convert this problem to something called the independent set problem, where you're just sort of  
**Translation:** 

**[3902.20s] English:** asking for a set of vertices in a graph such that no two of them are adjacent, sort of the opposite  
**Translation:** Vocabulary: vertices: 顶点

**[3909.64s] English:** of the clique problem. So, we've seen that we can now express that as finding...  
**Translation:** 

**[3925.56s] English:** a set of terms, one in each clause, without picking both the variable and the negation of  
**Translation:** Vocabulary: clique: 子群; negation: 否定

**[3937.48s] English:** that variable. Because if the variable is assigned the truth value, the negated variable has to have  
**Translation:** 

**[3944.20s] English:** the opposite truth value. And so, we can construct the graph where the vertices are the terms,  
**Translation:** Vocabulary: negated: 否定了的

**[3955.56s] English:** in all of the clauses, and you have...  
**Translation:** 

**[3960.00s] English:** an edge between two occurrences of terms, either if they're both in the same clause,  
**Translation:** Vocabulary: occurrences: 出现次数

**[3979.54s] English:** because you're only picking one element from each clause, and also an edge between them  
**Translation:** 

**[3985.90s] English:** if they represent opposite values of the same variable, because you can't make a variable  
**Translation:** 

**[3991.28s] English:** both true and false.  
**Translation:** 

**[3993.38s] English:** And so you get a graph where you have all of these occurrences of variables, you have  
**Translation:** 

**[3998.46s] English:** edges, which mean that you're not allowed to choose both ends of the edge, either because  
**Translation:** 

**[4005.52s] English:** they're in the same clause or they're negations of one another.  
**Translation:** Vocabulary: negations: 否定形式

**[4010.18s] English:** Right.  
**Translation:** 

**[4010.86s] English:** And that's a, first of all, sort of to zoom out, that's a really powerful example.  
**Translation:** 

**[4015.90s] English:** The whole idea that you could take a graph and connect it to a logic equation somehow  
**Translation:** 

**[4023.44s] English:** and do that mapping for all possible formulations of a particular problem on a graph.  
**Translation:** Vocabulary: equation: 方程

**[4030.18s] English:** Yeah.  
**Translation:** 

**[4030.84s] English:** I mean, that still is hard for me to believe that that's possible.  
**Translation:** 

**[4038.26s] English:** Like, what do you make of that, that there's such a union of, there's such a friendship,  
**Translation:** 

**[4045.90s] English:** among all these problems across, that somehow are akin to combinatorial algorithms, that  
**Translation:** 

**[4054.18s] English:** they're all somehow related?  
**Translation:** 

**[4055.74s] English:** Yeah.  
**Translation:** 

**[4055.92s] English:** I know it can be proven.  
**Translation:** 

**[4058.24s] English:** Yeah.  
**Translation:** 

**[4058.60s] English:** But what do you make of it, that that's true?  
**Translation:** 

**[4062.88s] English:** Well, that they just have the same expressive power.  
**Translation:** Vocabulary: expressive: 表达能力强

**[4066.82s] English:** You can take any one of them and translate it into the terms of the other.  
**Translation:** 

**[4072.66s] English:** The fact that they have the same expressive power.  
**Translation:** 

**[4075.68s] English:** Yeah.  
**Translation:** 

**[4075.76s] English:** Yeah.  
**Translation:** 

**[4075.86s] English:** Yeah.  
**Translation:** 

**[4075.88s] English:** Yeah.  
**Translation:** 

**[4075.90s] English:** And that also somehow means that they can be translatable.  
**Translation:** 

**[4078.88s] English:** Right.  
**Translation:** Vocabulary: translatable: 可翻译的

**[4079.32s] English:** Yeah.  
**Translation:** 

**[4079.48s] English:** Yeah.  
**Translation:** 

**[4080.00s] English:** Yeah.  
**Translation:** 

**[4080.32s] English:** Yeah.  
**Translation:** 

**[4080.00s] English:** And what I did in the 1971 paper was to take 21 fundamental problems, commonly occurring problems of packing, covering, matching, and so forth, lying in the class NP, and show that the satisfiability problem can be re-expressed as any of those.  
**Translation:** 

**[4104.20s] English:** That any of those have the same expressive power.  
**Translation:** 

**[4108.54s] English:** And that was like throwing down the gauntlet of saying, there's probably many more problems like this.  
**Translation:** 

**[4115.88s] English:** Right.  
**Translation:** 

**[4116.26s] English:** But that's just saying that, look, they're all the same.  
**Translation:** 

**[4119.52s] English:** They're all the same, but not exactly.  
**Translation:** 

**[4123.28s] English:** They're all the same in terms of whether they are rich enough to express any of the others.  
**Translation:** 

**[4133.38s] English:** But that doesn't mean that they have the same computational complexity.  
**Translation:** 

**[4137.90s] English:** But.  
**Translation:** 

**[4138.54s] English:** What we can say is that either all of these problems or none of them are solvable in polynomial time.  
**Translation:** Vocabulary: polynomial: 多项式

**[4145.76s] English:** Yeah, so where does NP completeness and NP hard classify?  
**Translation:** 

**[4151.02s] English:** Oh, that's just a small technicality.  
**Translation:** Vocabulary: classify: 分类; completeness: 完备性; technicality: 技术细节

**[4153.70s] English:** So when we're talking about decision problems, that means that the answer is just yes or no.  
**Translation:** 

**[4160.60s] English:** There is a clique of size 15 or there's not a clique of size 15.  
**Translation:** Vocabulary: clique: 团块

**[4166.38s] English:** On the other hand, an optimization problem.  
**Translation:** 

**[4168.54s] English:** The problem would be asking, find the largest clique.  
**Translation:** Vocabulary: optimization: 最优化问题

**[4172.82s] English:** The answer would not be yes or no.  
**Translation:** 

**[4174.94s] English:** It would be 15.  
**Translation:** 

**[4178.68s] English:** So when you're asking for the.  
**Translation:** 

**[4182.56s] English:** When you're putting a valuation on the different solutions and you're asking for the one with the highest valuation, that's an optimization problem.  
**Translation:** 

**[4191.12s] English:** And there's a very close affinity between the two kinds of problems.  
**Translation:** 

**[4195.16s] English:** But the counterpart of.  
**Translation:** Vocabulary: affinity: 亲和力; counterpart: 对应物

**[4198.54s] English:** Being the hardest.  
**Translation:** 

**[4200.00s] English:** decision problem, the hardest yes-no problem,  
**Translation:** 

**[4204.26s] English:** the counterpart of that is  
**Translation:** 

**[4208.10s] English:** to minimize or maximize an objective  
**Translation:** Vocabulary: maximize: 最大化

**[4212.26s] English:** function. And so a problem that's hardest in the class  
**Translation:** 

**[4216.18s] English:** when viewed in terms of optimization, those are  
**Translation:** 

**[4220.26s] English:** called NP-hard rather than NP-complete.  
**Translation:** 

**[4224.12s] English:** And NP-complete is for decision problems.  
**Translation:** 

**[4226.16s] English:** So if somebody  
**Translation:** 

**[4231.94s] English:** shows that P equals NP, what do you  
**Translation:** 

**[4236.16s] English:** think that proof will look like if you were to put  
**Translation:** 

**[4240.18s] English:** on yourself, if it's possible to show that as  
**Translation:** 

**[4244.12s] English:** a proof or to demonstrate an algorithm?  
**Translation:** 

**[4248.52s] English:** All I can say is that it will involve concepts  
**Translation:** Vocabulary: algorithm: 算法

**[4251.98s] English:** that we do not now have and approaches that we don't have.  
**Translation:** 

**[4256.16s] English:** Do you think those concepts are out there in terms of inside  
**Translation:** 

**[4259.78s] English:** complexity theory, inside of computational analysis of  
**Translation:** 

**[4264.14s] English:** algorithms? Do you think there's concepts that are totally outside of the box that we haven't  
**Translation:** Vocabulary: complexity: 复杂性; computational: 计算的

**[4268.26s] English:** considered yet? I think that if there is a proof that P is  
**Translation:** 

**[4272.26s] English:** equal to NP or that P is not equal to NP,  
**Translation:** 

**[4275.72s] English:** it'll depend on concepts that are now  
**Translation:** 

**[4279.76s] English:** outside the box. Now if that's shown either way, P  
**Translation:** 

**[4284.00s] English:** equals NP or P not,  
**Translation:** 

**[4286.16s] English:** actually P equals NP, what impact, you kind of mentioned it a little bit, but can you  
**Translation:** 

**[4293.12s] English:** linger on it? What kind of impact would it have on theoretical computer science and perhaps  
**Translation:** 

**[4299.20s] English:** software-based systems in general? Well, I think it would have enormous  
**Translation:** 

**[4304.08s] English:** impact on the world in either way case. If P is unequal to NP, which is what we expect,  
**Translation:** 

**[4313.12s] English:** then we know that for the great  
**Translation:** Vocabulary: unequal: 不相等

**[4316.10s] English:** majority of the combinatorial problems that come up, since they're  
**Translation:** 

**[4320.00s] English:** known to be NP-complete, we're not going to be able to solve them by efficient algorithms.  
**Translation:** Vocabulary: combinatorial: 组合的

**[4327.72s] English:** However, there's a little bit of hope in that it may be that we can solve most instances.  
**Translation:** 

**[4336.50s] English:** All we know is that if a problem is not NP, then it can't be solved efficiently on all  
**Translation:** Vocabulary: efficiently: 高效地

**[4342.02s] English:** instances.  
**Translation:** 

**[4342.52s] English:** But basically, if we find that P is unequal to NP, it will mean that we can't expect always  
**Translation:** 

**[4355.16s] English:** to get the optimal solutions to these problems, and we have to depend on heuristics that perhaps  
**Translation:** 

**[4361.52s] English:** work most of the time or give us good approximate solutions.  
**Translation:** Vocabulary: approximate: 近似; heuristics: 启发式; optimal: 最优

**[4367.76s] English:** So we would turn our eye towards the heuristics.  
**Translation:** 

**[4371.94s] English:** Yes.  
**Translation:** 

**[4372.52s] English:** A little bit more acceptance and comfort on our hearts.  
**Translation:** 

**[4376.40s] English:** Exactly.  
**Translation:** 

**[4377.60s] English:** Okay, so let me ask a romanticized question.  
**Translation:** 

**[4382.20s] English:** What to you is one of the most or the most beautiful combinatorial algorithm in your  
**Translation:** Vocabulary: algorithm: 算法

**[4388.50s] English:** own life or just in general in the field that you've ever come across or have developed  
**Translation:** 

**[4393.26s] English:** yourself?  
**Translation:** 

**[4393.74s] English:** I like the stable matching problem or the stable marriage problem very much.  
**Translation:** 

**[4402.52s] English:** What's the stable matching problem?  
**Translation:** 

**[4405.16s] English:** Yeah.  
**Translation:** 

**[4406.08s] English:** Imagine that you want to marry off N boys with N girls.  
**Translation:** 

**[4416.86s] English:** And each boy has an ordered list of his preferences among the girls, his first choice, his second  
**Translation:** 

**[4423.62s] English:** choice, through her Nth choice.  
**Translation:** 

**[4431.00s] English:** And...  
**Translation:** 

**[4431.60s] English:** Each girl...  
**Translation:** 

**[4432.40s] English:** Each girl also has an ordering of the boys, the first choice, second choice, and so on.  
**Translation:** 

**[4437.44s] English:** And we'll say...  
**Translation:** 

**[4440.00s] English:** And we will say that a matching, a one-to-one matching of the boys with the girls is stable if there are no two couples in the matching, such that the boy in the first couple prefers the girl in the second couple to her mate, and she prefers the boy to her current mate.  
**Translation:** 

**[4466.88s] English:** In other words, if there is, the matching is stable if there is no pair who want to run away with each other, leaving their partners behind.  
**Translation:** 

**[4478.46s] English:** Gotcha.  
**Translation:** 

**[4483.30s] English:** Actually, this is relevant to matching residents with hospitals and some other real-life problems, although not quite in the form that I described.  
**Translation:** 

**[4496.88s] English:** So it turns out that there is, for any set of preferences, a stable matching exists, and moreover, it can be computed by a simple algorithm in which each boy starts making proposals to girls, and if a girl receives a proposal, she accepts it tentatively,  
**Translation:** 

**[4525.30s] English:** but she can...  
**Translation:** Vocabulary: algorithm: 算法; computed: 计算; tentatively: 暂且

**[4526.88s] English:** drop it if she can end it, she can drop it later if she gets a better proposal from her point of view, and the boys start going down their list, proposing to their first, second, third choices, until stopping when a proposal is accepted.  
**Translation:** 

**[4549.94s] English:** But the girls, meanwhile, are watching the proposals that are coming into them, and the girl will drop it.  
**Translation:** 

**[4556.88s] English:** It's a pretty wine-dense evening for a couple of us.  
**Translation:** 

**[4557.24s] English:** But it's a very fun afternoon for us.  
**Translation:** 

**[4557.30s] English:** And I think it's going to be a great day for everyone, just like it was for me, because I think it's going to be a good time for everyone watching.  
**Translation:** 

**[4563.94s] English:** Yeah, exactly.  
**Translation:** 

**[4564.14s] English:** I think it's going to be a good time for everyone.  
**Translation:** 

**[4564.24s] English:** Yeah, absolutely.  
**Translation:** 

**[4560.00s] English:** if she gets a better proposal and the boys never go back through they never go back yeah so once  
**Translation:** 

**[4567.94s] English:** they've been denied they don't try again they don't they don't they don't try again because  
**Translation:** 

**[4574.90s] English:** the girls are always improving their status as they get more as they receive better and better  
**Translation:** 

**[4582.04s] English:** proposals the boys are going down their list starting with their top preferences and um  
**Translation:** 

**[4589.98s] English:** one can prove that uh that the process will come to an end where everybody will get matched with  
**Translation:** 

**[4602.04s] English:** somebody and you'll you won't have any pair that want to abscond from each other do you find the  
**Translation:** Vocabulary: abscond: 逃跑

**[4610.84s] English:** proof or the algorithm itself beautiful or is it the fact that with the simplicity of just  
**Translation:** 

**[4617.00s] English:** the two marching i mean  
**Translation:** Vocabulary: simplicity: 简单性

**[4619.74s] English:** the  
**Translation:** 

**[4619.96s] English:** the  
**Translation:** 

**[4619.98s] English:** the simplicity of the underlying rule of the algorithm is that the beautiful part  
**Translation:** 

**[4623.58s] English:** both i i would say um and you also have the observation that you might ask uh who is better  
**Translation:** 

**[4632.34s] English:** off the boys who are doing the proposing or the girls who are reacting to proposals  
**Translation:** 

**[4637.08s] English:** and it turns out that it's it's the boys who are doing the doing the best that is each boy  
**Translation:** 

**[4643.70s] English:** is doing at least as well as uh he could do in any other staple matching  
**Translation:** 

**[4649.48s] English:** so there's a sort of lesson for the boys that you should go out and be proactive and make those  
**Translation:** Vocabulary: staple: 主要产品

**[4657.08s] English:** proposals go for broke i don't i don't know if the this is directly mappable philosophically to  
**Translation:** 

**[4664.38s] English:** our society but uh certainly seems like a compelling notion and like you said there's  
**Translation:** Vocabulary: compelling: 有说服力; philosophically: 从哲学角度看

**[4670.44s] English:** probably a lot of actual real world problems that this could be mapped to yeah well you get you you  
**Translation:** 

**[4675.88s] English:** get uh complications for example  
**Translation:** 

**[4679.48s] English:** what  
**Translation:** 

**[4680.00s] English:** happens when a husband and wife want to be assigned to the same hospital so you  
**Translation:** 

**[4684.88s] English:** you you have to take those constraints into account and then the problem  
**Translation:** 

**[4691.32s] English:** becomes NP hard or what why is it a problem for the husband and wife to be  
**Translation:** 

**[4698.24s] English:** assigned to the same hospital no it's desirable so that or at least go to the  
**Translation:** 

**[4703.28s] English:** same city so you can't if you're if you're assigning residents to hospitals  
**Translation:** Vocabulary: assigning: 分配; desirable: 理想的

**[4709.32s] English:** and then you have some preferences for the husband and wife or for the  
**Translation:** 

**[4714.04s] English:** hospitals the residents have their own preferences references residents both  
**Translation:** 

**[4720.72s] English:** male and female have their own preferences the hospitals have their  
**Translation:** 

**[4725.92s] English:** preferences but if if resident a the boy is going to Philadelphia then you'd like  
**Translation:** 

**[4737.44s] English:** his wife how  
**Translation:** 

**[4739.08s] English:** you'd like his wife how  
**Translation:** 

**[4739.30s] English:** be also also to be assigned to a hospital in Philadelphia so which step  
**Translation:** 

**[4745.00s] English:** makes it a NP hard problem the imagine the fact that you have this additional  
**Translation:** 

**[4749.50s] English:** constraint that it's not just the preferences of individuals but the fact  
**Translation:** 

**[4755.68s] English:** that the two partners to a marriage have to go to have to be assigned to the same  
**Translation:** 

**[4761.78s] English:** place I'm being a little dense the was sort of  
**Translation:** 

**[4769.06s] English:** in there there's this  
**Translation:** 

**[4781.80s] English:** the  
**Translation:** 

**[4784.34s] English:** if let's say there's two  
**Translation:** 

**[4787.84s] English:** partners or I have once the second super  
**Translation:** 

**[4790.38s] English:** undergraduate or private university with empathy and with  
**Translation:** Vocabulary: empathy: 同理心; undergraduate: 本科生

**[4796.26s] English:** everything aspect because it doesn' t Lord perfect 붙a her  
**Translation:** 

**[4797.62s] English:** little constraint will make it an NP-hard problem.  
**Translation:** 

**[4800.00s] English:** well yeah okay by the way the algorithm you mentioned wasn't was one of yours and no no  
**Translation:** 

**[4808.14s] English:** that was due to gail and shapley and uh my friend david gail passed away before he could get part  
**Translation:** Vocabulary: algorithm: 算法; shapley: 沙普利

**[4816.84s] English:** of the nobel prize but uh his partner shapley uh shared in a nobel prize with somebody else for  
**Translation:** 

**[4823.84s] English:** economics for for economics uh for ideas stemming from the stable matching idea  
**Translation:** Vocabulary: nobel: 诺贝尔; stemming: 源自

**[4831.34s] English:** so you've also have developed yourself some elegant beautiful algorithms again picking  
**Translation:** 

**[4838.92s] English:** your children so the the the robin carp algorithm for string searching pattern matching  
**Translation:** 

**[4843.98s] English:** edmund carp algorithm for max flows we mentioned hopcroft carp algorithm for finding  
**Translation:** 

**[4848.62s] English:** maximum cardinality matchings in bipartite graphs is there ones that  
**Translation:** Vocabulary: bipartite: 二分图; cardinality: 基数

**[4853.82s] English:** stand out to you as ones you're most proud of or just um whether it's beauty elegance or  
**Translation:** 

**[4862.16s] English:** just being the right discovery development in your life that you're especially proud of  
**Translation:** Vocabulary: elegance: 优雅

**[4868.60s] English:** i like the robin carp algorithm because it illustrates the power of randomization  
**Translation:** 

**[4875.12s] English:** so um the the problem there is  
**Translation:** Vocabulary: illustrates: 举例说明; randomization: 随机化

**[4883.82s] English:** to um  
**Translation:** 

**[4887.80s] English:** is to decide whether a given long string of symbols from some alphabet contains a given word  
**Translation:** 

**[4899.04s] English:** whether a particular word occurs within some very much longer word  
**Translation:** 

**[4905.28s] English:** and so the the idea of the algorithm is to associate  
**Translation:** 

**[4913.82s] English:** with the word that we're looking for a fingerprint some  
**Translation:** 

**[4920.00s] English:** some number or some combinatorial object that describes that word, and then to  
**Translation:** Vocabulary: combinatorial: 组合的; fingerprint: 指纹

**[4930.90s] English:** look for an occurrence of that same fingerprint as you slide along the  
**Translation:** 

**[4934.70s] English:** longer word. And what we do is we associate with each word a number. So we,  
**Translation:** 

**[4946.70s] English:** first of all, we think of the letters that occur in a word as the digits of it,  
**Translation:** 

**[4951.78s] English:** let's say a decimal, or whatever base, here. Whatever number, or different  
**Translation:** Vocabulary: decimal: 小数; digits: 位数

**[4960.34s] English:** symbols there are. Jed Macosko That's the base of the numbers, yeah.  
**Translation:** 

**[4963.10s] English:** 45 00ig.:00.304 Right. So every word can then be thought of as a number with the  
**Translation:** 

**[4969.56s] English:** letters being the digits of that number, and then we pick a random prime number  
**Translation:** 

**[4976.22s] English:** and insert that number. And we know that the numbers are a number. It's sort of  
**Translation:** Vocabulary: insert: 插入

**[4976.58s] English:** relative to the number of our alien relatives we live together, although  
**Translation:** 

**[4976.68s] English:** range and we take that word viewed as a number and take the remainder on  
**Translation:** Vocabulary: alien: 外星人

**[4985.38s] English:** dividing the dividing that number by the prime so coming up with a nice hash  
**Translation:** 

**[4993.78s] English:** function it's a it's a kind of hash function yeah um it gives you a little  
**Translation:** 

**[4999.30s] English:** shortcut for for that particular word yeah so that's the that's the it's very  
**Translation:** 

**[5006.56s] English:** different than the in other algorithms of its kind that we're trying to do  
**Translation:** 

**[5011.80s] English:** search string matching yeah which usually are combinatorial and don't  
**Translation:** 

**[5018.50s] English:** involve the idea of taking a random fingerprint yes and doing the  
**Translation:** 

**[5024.92s] English:** fingerprinting has two advantages one is that as we slide along the long word  
**Translation:** 

**[5030.88s] English:** digit by digit we can we keep a window of a  
**Translation:** Vocabulary: digit: 位数字

**[5036.38s] English:** search engine number and so that means that in our search engine number it first  
**Translation:** 

**[5036.54s] English:** in size, the size of the word we're looking for.  
**Translation:** 

**[5040.00s] English:** and we compute the fingerprint of every stretch of that length.  
**Translation:** 

**[5047.52s] English:** And it turns out that just a couple of arithmetic operations  
**Translation:** Vocabulary: arithmetic: 算术; fingerprint: 指纹

**[5051.04s] English:** will take you from the fingerprint of one part  
**Translation:** 

**[5054.58s] English:** to what you get when you slide over by one position.  
**Translation:** 

**[5059.80s] English:** So the computation of all the fingerprints is simple.  
**Translation:** 

**[5065.62s] English:** And secondly, it's unlikely if the prime is chosen randomly from a certain range  
**Translation:** Vocabulary: computation: 计算; fingerprints: 指纹

**[5073.92s] English:** that you will get two of the segments in question having the same fingerprint.  
**Translation:** 

**[5081.24s] English:** And so there's a small probability of error which can be checked after the fact  
**Translation:** Vocabulary: segments: 段落

**[5085.68s] English:** and also the ease of doing the computation  
**Translation:** 

**[5088.52s] English:** because you're working with these fingerprints  
**Translation:** 

**[5090.44s] English:** which are remainders modulo some big prime.  
**Translation:** 

**[5095.62s] English:** So that's the magical thing about randomized algorithms  
**Translation:** Vocabulary: modulo: 模; randomized: 随机化; remainders: 余数

**[5097.82s] English:** is that if you add a little bit of randomness  
**Translation:** 

**[5102.38s] English:** it somehow allows you to take a pretty naive approach  
**Translation:** Vocabulary: naive: 幼稚; randomness: 随机性

**[5104.98s] English:** a simple looking approach  
**Translation:** 

**[5106.82s] English:** and allow it to run extremely well.  
**Translation:** 

**[5110.78s] English:** So can you maybe take a step back and say  
**Translation:** 

**[5113.94s] English:** what is a randomized algorithm, this category of algorithms?  
**Translation:** Vocabulary: algorithm: 算法

**[5118.26s] English:** Well, it's just the ability to draw a random number  
**Translation:** 

**[5122.40s] English:** from such...  
**Translation:** 

**[5125.62s] English:** from some range or to associate a random number with some object  
**Translation:** 

**[5131.62s] English:** or to draw at random from some set.  
**Translation:** 

**[5135.42s] English:** So another example is very simple.  
**Translation:** 

**[5141.94s] English:** If we're conducting a presidential election  
**Translation:** Vocabulary: conducting: 进行选举

**[5144.98s] English:** and we would like to pick the winner  
**Translation:** 

**[5150.04s] English:** in principle, we could draw  
**Translation:** 

**[5155.62s] English:** a random sample of all of the voters in the country.  
**Translation:** 

**[5160.00s] English:** And if it was of substantial size, say a few thousand, then the most popular candidate in that group would be very likely to be the correct choice that would come out of counting all the millions of votes.  
**Translation:** 

**[5175.88s] English:** Now, of course, we can't do this because, first of all, everybody has to feel that his or her vote counted.  
**Translation:** 

**[5181.78s] English:** And secondly, we can't really do a purely random sample from that population.  
**Translation:** 

**[5186.68s] English:** And I guess, thirdly, there could be a tie, in which case we wouldn't have a significant difference between two candidates.  
**Translation:** 

**[5196.42s] English:** But those things aside, if you didn't have all that messiness of human beings, you could prove that that kind of random picking would come up.  
**Translation:** Vocabulary: messiness: 杂乱程度

**[5203.26s] English:** You just said random picking would solve the problem with a very low probability of error.  
**Translation:** 

**[5211.26s] English:** Another example is testing whether a number is prime.  
**Translation:** 

**[5214.42s] English:** So if I want to test whether 17 is prime, I could pick any number between 1 and 17 and raise it to the 16th power modulo 17, and you should get back the original number.  
**Translation:** 

**[5234.64s] English:** That's a famous formula due to Fermat.  
**Translation:** Vocabulary: fermat: 费马; modulo: 模

**[5239.12s] English:** It's called Fermat's Little Theorem.  
**Translation:** 

**[5242.18s] English:** If you take any a...  
**Translation:** 

**[5244.42s] English:** Any number a in the range 0 through n minus 1, and raise it to the n minus 1th power modulo n, you'll get back the number a.  
**Translation:** 

**[5260.68s] English:** If a is prime.  
**Translation:** 

**[5263.48s] English:** So if you don't get back the number a, that's a proof that a number is not prime.  
**Translation:** 

**[5269.48s] English:** Wow.  
**Translation:** 

**[5272.16s] English:** And you can show that...  
**Translation:** 

**[5274.42s] English:** That suitably defined the...  
**Translation:** Vocabulary: suitably: 适当地

**[5280.00s] English:** The probability that you will get a value unequaled, you will get a violation of Fermat's result is very high.  
**Translation:** 

**[5294.28s] English:** And so this gives you a way of rapidly proving that a number is not prime.  
**Translation:** Vocabulary: unequaled: 无可比拟的

**[5300.72s] English:** It's a little more complicated than that because there are certain values of n where something a little more elaborate has to be done.  
**Translation:** 

**[5308.60s] English:** But that's the basic idea.  
**Translation:** 

**[5310.90s] English:** Taking an identity that holds for primes and therefore, if it ever fails on any instance for a non-prime, you know that the number is not prime.  
**Translation:** 

**[5323.32s] English:** It's a quick choice, a fast choice, fast proof that a number is not prime.  
**Translation:** 

**[5328.86s] English:** Can you maybe elaborate a little bit more?  
**Translation:** 

**[5331.02s] English:** What's your intuition why randomness works so well and results in such simple algorithms?  
**Translation:** Vocabulary: elaborate: 详细说明; intuition: 直觉; randomness: 随机性

**[5337.46s] English:** Well, the example of conduction.  
**Translation:** 

**[5340.00s] English:** It's like conducting an election where you could take, in theory, you could take a sample and depend on the validity of the sample to really represent the whole.  
**Translation:** Vocabulary: conducting: 进行选举; conduction: 传导; validity: 有效性

**[5349.12s] English:** It's just the basic fact of statistics, which gives a lot of opportunities.  
**Translation:** 

**[5357.16s] English:** And I actually exploited that sort of random sampling idea in designing an algorithm for counting the number of solutions.  
**Translation:** Vocabulary: algorithm: 算法; exploited: 利用

**[5370.00s] English:** That satisfy a particular formula and propositional logic.  
**Translation:** 

**[5377.62s] English:** A particular, so some version of the satisfiability problem?  
**Translation:** Vocabulary: propositional: 命题逻辑的

**[5384.00s] English:** A version of the satisfiability problem.  
**Translation:** 

**[5387.74s] English:** Is there some interesting insight that you want to elaborate on?  
**Translation:** 

**[5390.64s] English:** Like what some aspect of that algorithm that might be useful to describe?  
**Translation:** 

**[5397.12s] English:** So you have a...  
**Translation:** 

**[5400.00s] English:** collection of formulas and you want to count the number of solutions that  
**Translation:** 

**[5414.58s] English:** satisfy at least one of the formulas and you can count the number of solutions  
**Translation:** Vocabulary: formulas: 公式

**[5423.32s] English:** that satisfy any particular one of the formulas but you have to account for the  
**Translation:** 

**[5429.48s] English:** fact that that solution might be counted many times if it solves more than one of  
**Translation:** 

**[5437.34s] English:** the formulas and so what you do is you sample from the formulas according to  
**Translation:** 

**[5447.54s] English:** the number of solutions that satisfy each individual one in that way you draw  
**Translation:** 

**[5454.04s] English:** a random solution but then you correct by looking at the number of  
**Translation:** 

**[5459.44s] English:** of formulas that satisfy that random solution, and don't double count.  
**Translation:** 

**[5469.02s] English:** So you can think of it this way.  
**Translation:** 

**[5471.88s] English:** You have a matrix of zeros and ones, and you want to know how many columns of that matrix  
**Translation:** Vocabulary: matrix: 矩阵

**[5478.86s] English:** contain at least one 1.  
**Translation:** 

**[5482.56s] English:** And you can count in each row how many ones there are.  
**Translation:** 

**[5487.06s] English:** So what you can do is draw from the rows according to the number of 1s.  
**Translation:** 

**[5491.74s] English:** If a row has more 1s, it gets drawn more frequently.  
**Translation:** 

**[5496.12s] English:** But then if you draw from that row, you have to go up the column and looking at where that  
**Translation:** 

**[5503.24s] English:** same 1 is repeated in different rows, and only count it as a success or a hit if it's  
**Translation:** 

**[5511.62s] English:** the earliest row that contains the 1.  
**Translation:** 

**[5516.18s] English:** And that's it.  
**Translation:** 

**[5517.04s] English:** That gives you a robust statistical list.  
**Translation:** 

**[5520.00s] English:** of the total number of columns that contain at least one of the ones.  
**Translation:** Vocabulary: robust: 强壮的

**[5524.50s] English:** So that is an example of the same principle  
**Translation:** 

**[5528.90s] English:** that was used in studying random sampling.  
**Translation:** 

**[5533.28s] English:** Another viewpoint is that if you have a phenomenon  
**Translation:** 

**[5538.66s] English:** that occurs almost all the time,  
**Translation:** 

**[5542.48s] English:** then if you sample one of the occasions where it occurs,  
**Translation:** 

**[5548.10s] English:** and you're looking for an occurrence,  
**Translation:** 

**[5552.60s] English:** a random occurrence is likely to work.  
**Translation:** 

**[5554.98s] English:** So that comes up in solving identities,  
**Translation:** 

**[5559.56s] English:** solving algebraic identities.  
**Translation:** 

**[5562.80s] English:** You get two formulas that may look very different.  
**Translation:** Vocabulary: algebraic: 代数的

**[5566.36s] English:** You want to know if they're really identical.  
**Translation:** 

**[5569.04s] English:** What you can do is just pick a random value  
**Translation:** 

**[5572.74s] English:** and evaluate the formulas at that value  
**Translation:** 

**[5575.92s] English:** and see if they agree.  
**Translation:** Vocabulary: evaluate: 评估; formulas: 公式

**[5578.74s] English:** And you depend on the fact that if the formulas are distinct,  
**Translation:** 

**[5584.04s] English:** then they're going to disagree a lot.  
**Translation:** 

**[5586.82s] English:** And so therefore, a random choice will exhibit the disagreement.  
**Translation:** 

**[5592.24s] English:** If there are many ways for the two to disagree,  
**Translation:** 

**[5596.04s] English:** and you only need to find one disagreement,  
**Translation:** 

**[5598.60s] English:** then random choice is likely to yield it.  
**Translation:** 

**[5602.72s] English:** And in general, so we've just talked about randomized algorithms,  
**Translation:** 

**[5606.04s] English:** but we can look at the probabilistic algorithms,  
**Translation:** Vocabulary: probabilistic: 概率性的; randomized: 随机化的

**[5608.10s] English:** the analysis of algorithms.  
**Translation:** 

**[5609.78s] English:** And that gives us an opportunity to step back.  
**Translation:** 

**[5612.24s] English:** And as we've said,  
**Translation:** 

**[5614.06s] English:** everything we've been talking about is worst-case analysis.  
**Translation:** 

**[5617.10s] English:** Right.  
**Translation:** 

**[5617.84s] English:** Could you maybe comment on the usefulness  
**Translation:** 

**[5623.14s] English:** and the power of worst-case analysis  
**Translation:** 

**[5625.22s] English:** versus best-case analysis, average case, probabilistic?  
**Translation:** 

**[5630.94s] English:** How do we think about the future of theoretical computer science,  
**Translation:** 

**[5634.24s] English:** computer science,  
**Translation:** 

**[5635.84s] English:** and the kind of analysis we're doing?  
**Translation:** 

**[5638.08s] English:** How do we think about the future of algorithms?  
**Translation:** 

**[5639.12s] English:** Does worst-case  
**Translation:** 

**[5640.00s] English:** analysis still have a place an important place or do we want to try to move  
**Translation:** 

**[5644.20s] English:** forward towards kind of average case analysis yeah and what are the  
**Translation:** 

**[5648.00s] English:** challenges there so if worst-case analysis shows that a an algorithm is  
**Translation:** Vocabulary: algorithm: 算法

**[5653.92s] English:** always good that that's fine if worst-case analysis is used to show  
**Translation:** 

**[5663.34s] English:** that the problem that the solution is not always good then you have to step  
**Translation:** 

**[5670.60s] English:** back and do something else to ask how often will you get a good solution this  
**Translation:** 

**[5676.06s] English:** is just to pause on that for a second that that's so beautifully put because I  
**Translation:** 

**[5680.72s] English:** think we tend to judge algorithms we throw them in the trash the moment  
**Translation:** 

**[5685.90s] English:** there's their worst case is shown to be bad right and and and that's unfortunate  
**Translation:** 

**[5690.64s] English:** I think we  
**Translation:** 

**[5693.34s] English:** a good example is going back to the satisfiability problem there are very  
**Translation:** 

**[5700.78s] English:** powerful programs called SAT solvers which in practice fairly reliably solve  
**Translation:** 

**[5708.84s] English:** instances with many millions of variables that arise in a digital design  
**Translation:** Vocabulary: reliably: 可靠地; solvers: 求解器

**[5713.82s] English:** or in proving programs correct and other applications and so in in many  
**Translation:** 

**[5723.04s] English:** applications  
**Translation:** 

**[5723.28s] English:** in many applications  
**Translation:** 

**[5723.32s] English:** application areas, even though satisfiability, as we've already discussed, is NP-complete,  
**Translation:** 

**[5730.36s] English:** the SAT solvers will work so well that the people in that discipline tend to think of  
**Translation:** 

**[5737.90s] English:** satisfiability as an easy problem. So, in other words, just for some reason that we don't entirely  
**Translation:** 

**[5746.10s] English:** understand, the instances that people formulate in designing digital circuits or other applications  
**Translation:** 

**[5753.30s] English:** are such that satisfiability is  
**Translation:** Vocabulary: circuits: 电路

**[5760.00s] English:** not hard to check and even searching for a satisfying solution can be done  
**Translation:** 

**[5767.92s] English:** efficiently in practice and there are many examples for example we talked  
**Translation:** Vocabulary: efficiently: 高效地

**[5775.30s] English:** about the traveling salesman problem so just to refresh our memories the problem  
**Translation:** 

**[5781.84s] English:** is you've got a set of cities you have pairwise distances between cities then  
**Translation:** Vocabulary: pairwise: 两两之间

**[5788.80s] English:** you want to find a tour through all the cities that minimizes the total the  
**Translation:** 

**[5793.80s] English:** total cost of all the edges traversed all of all the trips between cities the  
**Translation:** Vocabulary: minimizes: 最小化

**[5799.06s] English:** problem is NP hard but people using integer programming codes together with  
**Translation:** 

**[5807.70s] English:** some other mathematical tricks can solve  
**Translation:** Vocabulary: integer: 整数; mathematical: 数学的

**[5814.92s] English:** geometric instances of the problem where the cities are let's say point  
**Translation:** 

**[5818.80s] English:** in the plane and get optimal solutions to problems with tens of thousands of  
**Translation:** 

**[5824.50s] English:** cities actually it'll take a few computer months to solve a problem of  
**Translation:** 

**[5829.78s] English:** that size but for problems of size a thousand or two it'll rapidly get  
**Translation:** 

**[5834.68s] English:** optimal solutions provably optimal solutions even though again we know that  
**Translation:** 

**[5841.98s] English:** it's unlikely to that the traveling salesman problem can be solved in  
**Translation:** Vocabulary: optimal: 最优化的; provably: 可证明地

**[5846.64s] English:** polynomial time  
**Translation:** 

**[5848.80s] English:** there are methodologies like rigorous systematic methodologies for you said in  
**Translation:** Vocabulary: methodologies: 方法论; polynomial: 多项式; rigorous: 严谨的

**[5857.56s] English:** practice in practice this algorithm that's pretty good are there systematic  
**Translation:** 

**[5860.98s] English:** ways of saying in practice this one is pretty good so in other words average  
**Translation:** 

**[5864.92s] English:** case analysis or you've also mentioned that average case kind of requires you  
**Translation:** 

**[5869.92s] English:** to understand what the typical cases typical instances and that might be  
**Translation:** 

**[5874.36s] English:** really difficult that's very difficult so after I did my original  
**Translation:** 

**[5878.80s] English:** work on  
**Translation:** 

**[5880.00s] English:** and showing all these problems to be NP-complete,  
**Translation:** 

**[5886.36s] English:** I looked around for a way to shed some positive light on combinatorial algorithms.  
**Translation:** 

**[5893.94s] English:** And what I tried to do was to study problems, behavior on the average or with high probability.  
**Translation:** 

**[5904.14s] English:** But I had to make some assumptions about what's the probability space,  
**Translation:** Vocabulary: assumptions: 假设

**[5909.62s] English:** what's the sample space, what do we mean by typical problems?  
**Translation:** 

**[5913.80s] English:** That's very hard to say.  
**Translation:** 

**[5915.36s] English:** So I took the easy way out and made some very simplistic assumptions.  
**Translation:** 

**[5920.44s] English:** So I assumed, for example, that if we were generating a graph  
**Translation:** Vocabulary: simplistic: 简单化的

**[5923.64s] English:** with a certain number of vertices and edges,  
**Translation:** 

**[5926.96s] English:** then we would generate the graph by simply choosing one edge at a time at random  
**Translation:** Vocabulary: vertices: 顶点

**[5933.64s] English:** until we got the right number of edges.  
**Translation:** 

**[5936.50s] English:** That's a particular model of random graph.  
**Translation:** 

**[5939.62s] English:** That has been studied mathematically a lot.  
**Translation:** 

**[5943.02s] English:** And within that model, I could prove all kinds of wonderful things.  
**Translation:** Vocabulary: mathematically: 用数学方法

**[5947.58s] English:** I and others who also worked on this.  
**Translation:** 

**[5950.40s] English:** So we could show that we know exactly how many edges there have to be  
**Translation:** 

**[5956.66s] English:** in order for there to be a so-called Hamiltonian circuit.  
**Translation:** 

**[5963.92s] English:** That's a cycle that visits each vertex exactly once.  
**Translation:** Vocabulary: hamiltonian: 哈密顿回路; vertex: 顶点

**[5969.62s] English:** We know that if the number of edges is a little bit more than n log n,  
**Translation:** 

**[5977.56s] English:** where n is the number of vertices,  
**Translation:** 

**[5978.92s] English:** then such a cycle is very likely to exist.  
**Translation:** 

**[5984.12s] English:** And we can give a heuristic that will find it with high probability.  
**Translation:** 

**[5988.94s] English:** And the community in which I was working got a lot of results along these lines.  
**Translation:** 

**[5998.30s] English:** But.  
**Translation:** 

**[5999.62s] English:** I think that's it for the questions.  
**Translation:** 

**[6001.26s] English:** Thank you.  
**Translation:** 

**[6001.94s] English:** Bye.  
**Translation:** 

**[6000.00s] English:** The field tended to be rather lukewarm about accepting these results as meaningful, because  
**Translation:** Vocabulary: lukewarm: 态度一般

**[6007.64s] English:** we were making such a simplistic assumption about the kinds of graphs that we would be  
**Translation:** 

**[6012.54s] English:** dealing with.  
**Translation:** Vocabulary: assumption: 简单假设

**[6013.54s] English:** So, we could show all kinds of wonderful things, it was a great playground, I enjoyed doing  
**Translation:** 

**[6018.06s] English:** it. But after a while, I concluded that it didn't have a lot of bite in terms of the  
**Translation:** 

**[6029.92s] English:** practical application.  
**Translation:** 

**[6030.92s] English:** Okay, so there's too much into the world of toy problems.  
**Translation:** 

**[6035.06s] English:** Yeah.  
**Translation:** 

**[6036.06s] English:** Okay. But, all right, is there a way to find nice, representative, real-world, impactful  
**Translation:** 

**[6044.46s] English:** instances of a problem on which to demonstrate that analogies exist?  
**Translation:** 

**[6048.04s] English:** The algorithm is good. So, this is kind of like the machine learning world, that's kind  
**Translation:** Vocabulary: algorithm: 算法; analogies: 类比

**[6051.74s] English:** of what they, at its best, tries to do is find a dataset from the real world and show  
**Translation:** 

**[6058.22s] English:** the performance. All the conferences are all focused on beating the performance on that  
**Translation:** Vocabulary: conferences: 学术会议; dataset: 数据集

**[6065.74s] English:** real-world dataset. Is there an equivalent in the complexity analysis?  
**Translation:** 

**[6072.02s] English:** Not really. Don Knuth started to collect data.  
**Translation:** Vocabulary: complexity: 复杂性

**[6078.02s] English:** There are examples of graphs coming from various places. So, he would have a whole zoo of  
**Translation:** 

**[6084.72s] English:** different graphs that he could choose from, and he could study the performance of algorithms  
**Translation:** 

**[6089.98s] English:** on different types of graphs. And...  
**Translation:** 

**[6093.72s] English:** But there, it's really important and compelling to be able to define a class of graphs. The  
**Translation:** Vocabulary: compelling: 令人信服的

**[6102.02s] English:** actual act of defining a class of graphs that you're interested in, it seems to be a non-trivial  
**Translation:** 

**[6107.28s] English:** step.  
**Translation:** 

**[6107.78s] English:** If we're talking about instances that we should care about in the real world.  
**Translation:** 

**[6111.48s] English:** Yeah. There's nothing available there that would be analogous to the training set for  
**Translation:** Vocabulary: analogous: 类比的

**[6118.88s] English:** supervised learning.  
**Translation:** 

**[6120.00s] English:** You know, where you sort of assume that the world has given you a bunch of examples to work with.  
**Translation:** Vocabulary: supervised: 监督学习

**[6129.90s] English:** We don't really have that for problems, for combinatorial problems on graphs and networks.  
**Translation:** 

**[6138.04s] English:** You know, there's been a huge growth, a big growth of data sets available.  
**Translation:** Vocabulary: combinatorial: 组合的

**[6143.18s] English:** Do you think some aspect of theoretical computer science, I might be contradicting my own question while saying it, but will there be some aspect, an empirical aspect of theoretical computer science, which will allow the fact that these data sets are huge, we'll start using them for analysis?  
**Translation:** 

**[6163.66s] English:** Sort of, you know, if you want to say something about a graph algorithm, you might take a social network like Facebook.  
**Translation:** 

**[6173.72s] English:** Yeah.  
**Translation:** 

**[6173.88s] English:** And looking at subgraphs of that and prove something about the Facebook graph and be respected and at the same time be respected in the theoretical computer science community.  
**Translation:** Vocabulary: subgraphs: 子图

**[6183.80s] English:** That hasn't been achieved yet, I'm afraid.  
**Translation:** 

**[6185.76s] English:** Is that P equals NP, is that impossible?  
**Translation:** 

**[6190.94s] English:** Is it impossible to publish a successful paper in the theoretical computer science community that shows some performance on a real world data set?  
**Translation:** 

**[6203.18s] English:** Or is that really just, those are two different worlds?  
**Translation:** 

**[6205.74s] English:** They haven't really come together.  
**Translation:** 

**[6207.86s] English:** I would say that there is a field of experimental algorithmics where people, sometimes they're given some family of examples.  
**Translation:** Vocabulary: algorithmics: 算法研究

**[6219.76s] English:** Sometimes they just generate them at random and they report on performance.  
**Translation:** 

**[6226.68s] English:** But there's no convincing evidence that the sample.  
**Translation:** 

**[6233.18s] English:** Is representative of anything at all.  
**Translation:** 

**[6237.20s] English:** So let me ask in terms of breakthrough.  
**Translation:** 

**[6240.00s] English:** and open problems what are the most compelling open problems to you and what possible breakthroughs  
**Translation:** 

**[6247.00s] English:** do you see in the near term in terms of theoretical computer science well there are all kinds of  
**Translation:** Vocabulary: breakthroughs: 重大突破; compelling: 极具吸引力的

**[6254.66s] English:** relationships among complexity classes that can be studied just to mention one thing i wrote a  
**Translation:** 

**[6262.58s] English:** paper with richard lipton in 1979 where we asked the following question  
**Translation:** Vocabulary: complexity: 复杂性

**[6270.62s] English:** if you take a problem a combinatorial problem in mp let's say and you  
**Translation:** 

**[6283.02s] English:** um choose a and you pick the size of the problem  
**Translation:** Vocabulary: combinatorial: 组合的

**[6291.24s] English:** and  
**Translation:** 

**[6292.58s] English:** uh say it's a traveling salesman problem but of size 52 and you ask  
**Translation:** 

**[6299.50s] English:** could you get an efficient a small boolean circuit tailored for that size 52  
**Translation:** 

**[6308.60s] English:** where you could feed the edges of the graph in in as boolean inputs and get as an output  
**Translation:** Vocabulary: boolean: 布尔; tailored: 定制的

**[6316.44s] English:** the question of whether or not there's a tour of a certain length and that would in other words  
**Translation:** 

**[6322.56s] English:** briefly what you would say in that case is that the problem has small circuits polynomial size circuits  
**Translation:** Vocabulary: circuits: 电路; polynomial: 多项式

**[6329.48s] English:** now we know that if p is equal to np then in fact these problems will have small circuits but what  
**Translation:** 

**[6339.96s] English:** about the converse could a problem have small circuits meaning that it's that an algorithm  
**Translation:** Vocabulary: algorithm: 算法; converse: 逆命题

**[6345.32s] English:** tailored to any particular size could work well and yet not be a polynomial time algorithm that is  
**Translation:** 

**[6352.56s] English:** you couldn't write it as a single uniform algorithm good for all sizes just to clarify small circuits  
**Translation:** 

**[6359.48s] English:** for  
**Translation:** 

**[6360.00s] English:** problem of particular size or even further constraint small circuit for a particular  
**Translation:** 

**[6366.96s] English:** for no for all the inputs of that size of that size is that a trivial problem for a particular  
**Translation:** 

**[6372.16s] English:** instance of so coming up an automated way of coming up with a circuit i guess that's that  
**Translation:** Vocabulary: automated: 自动化

**[6378.72s] English:** would be that would be that would be hard yeah yeah but you know but there's the existential  
**Translation:** 

**[6384.64s] English:** question everybody talks nowadays about every existential questions uh existential challenges  
**Translation:** Vocabulary: existential: 存在主义的

**[6393.36s] English:** yeah um you could ask the question um does the hamiltonian circuit problem have  
**Translation:** 

**[6406.32s] English:** a small circuit for for every size for each size a different small circuit  
**Translation:** Vocabulary: hamiltonian: 哈密尔顿

**[6413.12s] English:** in other words could you tailor  
**Translation:** 

**[6414.64s] English:** solutions depending on the size and and get polynomial size even if p is not equal to np  
**Translation:** 

**[6422.64s] English:** right and that would be fascinating if that's true yeah what we proved is that if that were possible  
**Translation:** 

**[6434.72s] English:** then something strange would happen in complexity theory some high high level class which i could  
**Translation:** 

**[6444.64s] English:** describe um something strange would happen so um i'll take a stab at describing what i mean  
**Translation:** 

**[6452.88s] English:** let's go there so we have to define this hierarchy in which the first level of the hierarchy is p  
**Translation:** Vocabulary: hierarchy: 等级制度

**[6461.36s] English:** and the second level is np and what is np np involves statements of the form there exists  
**Translation:** 

**[6469.28s] English:** a something such that something holds  
**Translation:** 

**[6473.12s] English:** um so  
**Translation:** 

**[6475.60s] English:** for example um um there exists the colorings  
**Translation:** 

**[6480.64s] English:** so  
**Translation:** 

**[6482.64s] English:** so  
**Translation:** 

**[6486.64s] English:** so  
**Translation:** 

**[6488.64s] English:** so  
**Translation:** 

**[6490.64s] English:** so  
**Translation:** 

**[6492.64s] English:** so  
**Translation:** 

**[6494.64s] English:** so  
**Translation:** 

**[6496.64s] English:** so  
**Translation:** 

**[6498.64s] English:** so  
**Translation:** 

**[6500.64s] English:** so  
**Translation:** 

**[6502.64s] English:** so  
**Translation:** 

**[6480.00s] English:** such that a graph can be colored with only that number  
**Translation:** 

**[6485.16s] English:** of colors, or there exists a Hamiltonian circuit.  
**Translation:** 

**[6489.18s] English:** There's a statement about this graph.  
**Translation:** 

**[6490.86s] English:** Yeah.  
**Translation:** 

**[6492.36s] English:** So the NP deals with statements of that kind,  
**Translation:** 

**[6502.96s] English:** that there exists a solution.  
**Translation:** 

**[6506.32s] English:** Now, you could imagine a more complicated expression, which  
**Translation:** 

**[6513.50s] English:** says, for all x, there exists a y such  
**Translation:** 

**[6519.16s] English:** that some proposition holds involving both x and y.  
**Translation:** 

**[6527.26s] English:** So that would say, for example, in game theory,  
**Translation:** 

**[6530.16s] English:** for all strategies for the first player,  
**Translation:** 

**[6535.04s] English:** there exists a strategy.  
**Translation:** 

**[6536.30s] English:** For the second player, such that the first player wins.  
**Translation:** 

**[6539.64s] English:** That would be at the second level of the hierarchy.  
**Translation:** 

**[6543.48s] English:** The third level would be, there exists an a such that for all b,  
**Translation:** 

**[6547.18s] English:** there exists a c that something holds.  
**Translation:** 

**[6549.38s] English:** And you can imagine going higher and higher in the hierarchy.  
**Translation:** 

**[6552.86s] English:** And you'd expect that the complexity classes that  
**Translation:** 

**[6557.80s] English:** correspond to those different cases would get bigger and bigger.  
**Translation:** Vocabulary: complexity: 复杂性; correspond: 对应

**[6565.34s] English:** Yeah.  
**Translation:** 

**[6565.84s] English:** Yeah.  
**Translation:** 

**[6566.28s] English:** Or they'd get harder and harder to solve.  
**Translation:** 

**[6571.16s] English:** Harder and harder, right.  
**Translation:** 

**[6572.46s] English:** Harder and harder to solve.  
**Translation:** 

**[6575.46s] English:** And what Lifted and I showed was that if NP had small circuits,  
**Translation:** Vocabulary: circuits: 电路

**[6581.70s] English:** then this hierarchy would collapse down  
**Translation:** 

**[6584.28s] English:** to the second level.  
**Translation:** 

**[6586.32s] English:** In other words, you wouldn't get any more mileage  
**Translation:** 

**[6588.52s] English:** by complicating your expressions with three quantifiers,  
**Translation:** Vocabulary: complicating: 使复杂; mileage: 里程; quantifiers: 量词

**[6591.66s] English:** or four quantifiers, or any number.  
**Translation:** 

**[6595.52s] English:** I'm not sure.  
**Translation:** 

**[6596.08s] English:** I don't know what to make of that exactly.  
**Translation:** 

**[6597.88s] English:** Well, I think it would be evidence that  
**Translation:** 

**[6600.00s] English:** And NP doesn't have small circuits because something so bizarre would happen.  
**Translation:** 

**[6607.16s] English:** But again, it's only evidence, not proof.  
**Translation:** 

**[6609.16s] English:** Well, yeah, that's not even evidence because you're saying P is not equal to NP because something bizarre has to happen.  
**Translation:** 

**[6619.74s] English:** I mean, that's proof by the lack of bizarreness in our science.  
**Translation:** Vocabulary: bizarreness: 怪异性

**[6626.32s] English:** But it seems like just the very notion of P equals NP would be bizarre.  
**Translation:** 

**[6633.26s] English:** So any way you arrive at it, there's no way.  
**Translation:** 

**[6636.16s] English:** You have to fight the dragon at some point.  
**Translation:** 

**[6638.60s] English:** Yeah, okay.  
**Translation:** Vocabulary: dragon: 龙

**[6639.46s] English:** Well, anyway, for whatever it's worth, that's what we proved.  
**Translation:** 

**[6643.42s] English:** Awesome.  
**Translation:** 

**[6644.26s] English:** So that's a potential space of open, interesting problems.  
**Translation:** 

**[6649.48s] English:** Yeah.  
**Translation:** 

**[6649.94s] English:** Let me ask you about this other world of machine learning, of deep learning.  
**Translation:** 

**[6657.08s] English:** What's your thoughts on the history and the current progress of machine learning field that's often progressed sort of separately as a space of ideas and space of people than the theoretical computer science or just even computer science world?  
**Translation:** Vocabulary: progressed: 发展

**[6672.48s] English:** Yeah, it's really very different from the theoretical computer science world because the results about algorithmic performance tend to be empirical.  
**Translation:** 

**[6685.32s] English:** It's more akin.  
**Translation:** Vocabulary: algorithmic: 算法相关的; empirical: 基于经验的

**[6686.32s] English:** It's more akin to the world of SAT solvers where we observe that for formulas arising in practice, the solver does well.  
**Translation:** 

**[6696.06s] English:** So it's of that type.  
**Translation:** Vocabulary: formulas: 数学公式; solver: 求解器; solvers: 求解器

**[6697.92s] English:** It's where we're moving into the empirical evaluation of algorithms.  
**Translation:** 

**[6705.34s] English:** Now, it's clear that there have been huge successes in image processing, robotics, natural language processing, a little less so.  
**Translation:** 

**[6715.44s] English:** Yeah.  
**Translation:** 

**[6716.32s] English:** It's across the spectrum of game playing.  
**Translation:** 

**[6719.94s] English:** Yeah.  
**Translation:** 

**[6720.00s] English:** Yeah.  
**Translation:** 

**[6720.02s] English:** Yeah.  
**Translation:** 

**[6720.04s] English:** Yeah.  
**Translation:** 

**[6720.06s] English:** Yeah.  
**Translation:** 

**[6720.08s] English:** Yeah.  
**Translation:** 

**[6720.10s] English:** Yeah.  
**Translation:** 

**[6720.14s] English:** Yeah.  
**Translation:** 

**[6720.16s] English:** Yeah.  
**Translation:** 

**[6720.00s] English:** is another one they've been great successes um and one of those effects is that it's not too  
**Translation:** 

**[6729.00s] English:** hard to become a millionaire if you can get a reputation in machine learning and there'll be  
**Translation:** 

**[6733.04s] English:** all kinds of companies that will be willing to offer you the moon because they they think that  
**Translation:** 

**[6738.64s] English:** if they have ai at their disposal then they can solve all kinds of problems um but there are  
**Translation:** 

**[6748.66s] English:** limitations one is that the solutions that you get by from to supervised learning problems  
**Translation:** Vocabulary: disposal: 处置; supervised: 监督

**[6764.80s] English:** through convolutional neural networks seem to perform amazingly well even for inputs that are  
**Translation:** 

**[6777.76s] English:** outside the training  
**Translation:** Vocabulary: convolutional: 卷积; neural: 神经

**[6778.64s] English:** set um but we don't have any theoretical understanding of why that's true  
**Translation:** 

**[6787.26s] English:** secondly the solutions the the networks that you get  
**Translation:** 

**[6793.32s] English:** are very hard to understand and so very little insight comes out  
**Translation:** 

**[6798.68s] English:** so yeah yeah they may seem to work on your training set and you may be able to discover  
**Translation:** 

**[6806.96s] English:** whether your photos are correct or not and so you may be able to discover whether your photos  
**Translation:** 

**[6808.44s] English:** are correct or not and so you may be able to discover whether your photos are correct or  
**Translation:** 

**[6808.64s] English:** occur in a different sample of inputs or not um but we don't really know what's going on we don't  
**Translation:** 

**[6817.86s] English:** know the the features that distinguish the photographs or the objects are are um not easy  
**Translation:** 

**[6826.44s] English:** to characterize well it's interesting because you mentioned coming up with a small circuit  
**Translation:** 

**[6832.86s] English:** yeah to solve a particular size problem yeah it seems that neural networks are kind of  
**Translation:** Vocabulary: characterize: 刻画

**[6838.44s] English:** small circuits  
**Translation:** 

**[6840.00s] English:** a way yeah uh but they're not programs sort of like the the things you've designed are algorithms  
**Translation:** 

**[6845.76s] English:** programs right algorithms neural networks aren't able to develop algorithms to solve a problem  
**Translation:** 

**[6854.00s] English:** as well they are more of a function they are algorithms it's just that they're  
**Translation:** 

**[6859.36s] English:** uh but sort of uh yeah it's a it could be a semantic question but there's not  
**Translation:** 

**[6866.32s] English:** a algorithmic style manipulation of the input perhaps you could argue there is yeah well  
**Translation:** Vocabulary: algorithmic: 算法的; manipulation: 操作; semantic: 语义的

**[6876.08s] English:** it feels a lot more like a function of the input it's a yeah it's a function it's a computable  
**Translation:** 

**[6882.40s] English:** function it's um you and once you have the network you can simulate it on a given input and figure  
**Translation:** Vocabulary: computable: 可计算的; simulate: 模拟

**[6889.70s] English:** out the output but what you you know if you're if you're trying to recognize images  
**Translation:** 

**[6896.32s] English:** then you don't know what features of the image are really being uh  
**Translation:** 

**[6904.18s] English:** determinant of of what the circuit is doing the circuit is  
**Translation:** 

**[6910.96s] English:** sort of a very intricate and you know it's not clear that the the you know the the simple  
**Translation:** Vocabulary: determinant: 决定因素

**[6919.42s] English:** characteristics that you're looking for the the edges of the objects or whatever they may be  
**Translation:** 

**[6925.00s] English:** you know  
**Translation:** 

**[6926.32s] English:** not emerging from the structure of the circuit well it's not clear to us humans but it's clear  
**Translation:** 

**[6931.56s] English:** to the circuit yeah well right i mean uh it's not clear to sort of the um the elephant how the human  
**Translation:** 

**[6943.60s] English:** brain works but it's clear to us humans we can explain to each other our reasoning and that's  
**Translation:** 

**[6949.52s] English:** why the cognitive science the psychology field exists maybe maybe the whole thing of being  
**Translation:** Vocabulary: cognitive: 认知

**[6955.04s] English:** explainable to humans is a little bit overrated oh maybe yeah i guess  
**Translation:** 

**[6960.00s] English:** You can say the same thing about our brain, that when we perform acts of cognition, we have no idea how we do it, really.  
**Translation:** Vocabulary: cognition: 认知

**[6968.68s] English:** We do, though.  
**Translation:** 

**[6969.56s] English:** I mean, at least for the visual system, the auditory system, and so on, we do get some understanding of the principles that they operate under.  
**Translation:** Vocabulary: auditory: 听觉

**[6980.32s] English:** But for many deeper cognitive tasks, we don't have that.  
**Translation:** 

**[6985.60s] English:** That's right.  
**Translation:** 

**[6986.00s] English:** Let me ask, you've also been doing work on bioinformatics.  
**Translation:** 

**[6993.02s] English:** Does it amaze you that the fundamental building blocks, if we take a step back and look at us humans, the building blocks used by evolution to build us intelligent human beings is all contained there in our DNA?  
**Translation:** Vocabulary: bioinformatics: 生物信息学

**[7007.76s] English:** It's amazing.  
**Translation:** 

**[7009.32s] English:** And what's really amazing is that we are beginning to learn.  
**Translation:** 

**[7016.00s] English:** How to edit DNA, which is very, very, very fascinating, this ability to take a sequence, find it in the genome, and do something to it.  
**Translation:** 

**[7039.02s] English:** I mean, that's really taking our biological system towards the worlds of algorithms.  
**Translation:** Vocabulary: genome: 基因组

**[7043.86s] English:** Yeah.  
**Translation:** 

**[7046.00s] English:** And that raises a lot of questions.  
**Translation:** 

**[7049.44s] English:** You have to distinguish between doing it on an individual or doing it on somebody's germline, which means that all of their descendants will be affected.  
**Translation:** 

**[7059.84s] English:** So that's like an ethical...  
**Translation:** Vocabulary: descendants: 后代; germline: 生殖细胞

**[7062.12s] English:** Yeah.  
**Translation:** 

**[7062.54s] English:** So it raises very severe ethical questions.  
**Translation:** 

**[7065.82s] English:** And even doing it on individuals is...  
**Translation:** 

**[7076.00s] English:** So there's a lot of hubris involved that...  
**Translation:** Vocabulary: hubris: 傲慢

**[7080.00s] English:** you can assume that knocking out a particular gene is going to be beneficial  
**Translation:** 

**[7085.22s] English:** because you don't know what the side effects are going to be.  
**Translation:** 

**[7088.80s] English:** So we have this wonderful new world of gene editing,  
**Translation:** 

**[7099.66s] English:** which is very, very impressive.  
**Translation:** 

**[7103.34s] English:** And it could be used in agriculture.  
**Translation:** 

**[7107.36s] English:** It could be used in medicine.  
**Translation:** 

**[7110.00s] English:** It could be used in medicine in various ways.  
**Translation:** 

**[7112.24s] English:** But very serious ethical problems arise.  
**Translation:** 

**[7116.96s] English:** What are, to you, the most interesting places where algorithms,  
**Translation:** 

**[7122.78s] English:** sort of the ethical side is an exceptionally challenging thing  
**Translation:** Vocabulary: exceptionally: 特别

**[7125.98s] English:** that I think we're going to have to tackle with all of genetic engineering.  
**Translation:** 

**[7131.44s] English:** But on the algorithmic side, there's a lot of benefit that's possible.  
**Translation:** Vocabulary: algorithmic: 算法相关的

**[7135.06s] English:** So is there areas where you see exciting possibilities,  
**Translation:** 

**[7140.00s] English:** for algorithms to help model, optimize, study biological systems?  
**Translation:** Vocabulary: optimize: 优化

**[7146.72s] English:** Yeah, I mean, we can certainly analyze genomic data to figure out  
**Translation:** 

**[7153.36s] English:** which genes are operative in the cell and under what conditions  
**Translation:** Vocabulary: genomic: 基因组的; operative: 起作用的

**[7158.46s] English:** and which proteins affect one another,  
**Translation:** 

**[7161.98s] English:** which proteins physically interact.  
**Translation:** 

**[7166.92s] English:** We can sequence proteins and modify them.  
**Translation:** 

**[7170.00s] English:** them um is there some aspect of that that's a computer science problem or is that still  
**Translation:** 

**[7176.74s] English:** fundamentally a biology problem well it's a big data it's a statistical big data problem for sure  
**Translation:** 

**[7184.32s] English:** so you know the biological data sets are increasing our ability to  
**Translation:** Vocabulary: fundamentally: 从根本上

**[7190.44s] English:** study our ancestry by to study the tendencies towards disease  
**Translation:** 

**[7200.00s] English:** to personalize treatment according to what's in our genomes  
**Translation:** Vocabulary: ancestry: 家族起源; genomes: 基因组

**[7206.82s] English:** and what tendencies for disease we have,  
**Translation:** 

**[7210.14s] English:** to be able to predict what troubles might come upon us in the future  
**Translation:** 

**[7214.48s] English:** and anticipate them, to understand whether you, for a woman,  
**Translation:** 

**[7224.98s] English:** whether her proclivity for breast cancer is so strong enough  
**Translation:** Vocabulary: anticipate: 预知; proclivity: 倾向

**[7232.84s] English:** that you would want to take action to avoid it.  
**Translation:** 

**[7237.76s] English:** You dedicate your 1985 Turing Award lecture to the memory of your father.  
**Translation:** Vocabulary: turing: 图灵奖

**[7244.60s] English:** What's your fondest memory of your dad?  
**Translation:** 

**[7252.62s] English:** Seeing him standing in front of me,  
**Translation:** 

**[7254.96s] English:** in front of a class at the blackboard,  
**Translation:** 

**[7257.84s] English:** drawing perfect circles by hand  
**Translation:** 

**[7262.32s] English:** and showing his ability to attract the interest  
**Translation:** 

**[7271.26s] English:** of the motley collection of eighth-grade students that he was teaching.  
**Translation:** Vocabulary: motley: 杂色的

**[7278.68s] English:** When did you get a chance to see him draw the perfect circles?  
**Translation:** 

**[7283.62s] English:** On rare occasions.  
**Translation:** 

**[7284.96s] English:** I would get a chance to sneak into his classroom and observe it.  
**Translation:** 

**[7293.10s] English:** And I think he was at his best in the classroom.  
**Translation:** 

**[7296.34s] English:** I think he really came to life  
**Translation:** 

**[7297.88s] English:** and had fun not only teaching,  
**Translation:** 

**[7304.26s] English:** but engaging in chit-chat with the students  
**Translation:** 

**[7309.84s] English:** and ingratiating himself with the students.  
**Translation:** 

**[7313.84s] English:** And I think he was a great teacher.  
**Translation:** 

**[7314.88s] English:** And I think he was a great teacher.  
**Translation:** 

**[7314.96s] English:** What I inherited from that is a great desire  
**Translation:** 

**[7319.88s] English:** to be a part of the community.  
**Translation:** Vocabulary: inherited: 继承

**[7320.00s] English:** to be a teacher i retired recently and a lot of my former students came students who's with whom  
**Translation:** 

**[7330.08s] English:** i had done research or who had read my papers or who had been in my classes and when they talked  
**Translation:** 

**[7336.40s] English:** about about me um they talked not about my 1979 paper or my 1992 paper but about what they what  
**Translation:** 

**[7351.08s] English:** came away in my classes and not just the details but just the approach and the the manner of  
**Translation:** 

**[7358.68s] English:** teaching and so i sort of take pride in the at least in my early years as a faculty member at  
**Translation:** 

**[7366.32s] English:** brittany  
**Translation:** 

**[7366.40s] English:** historically i was exemplary in preparing my lectures and i always came in prepared to the  
**Translation:** 

**[7376.34s] English:** teeth and able therefore to deviate according to what happened in the class and to really um  
**Translation:** Vocabulary: deviate: 偏离; exemplary: 模范的; historically: 历史上

**[7382.88s] English:** really provide a model for the students so is there advice you can give out  
**Translation:** 

**[7391.96s] English:** for others on how to be a good teacher  
**Translation:** 

**[7396.40s] English:** so preparation is one thing you've mentioned being exceptionally well prepared but there are  
**Translation:** 

**[7400.72s] English:** other things pieces of advice that you can impart well the top three would be preparation preparation  
**Translation:** Vocabulary: exceptionally: 特别地

**[7407.28s] English:** and preparation why is preparation so important i guess uh is uh it's because it gives you the  
**Translation:** 

**[7413.84s] English:** ease to deal with any situation that comes up in the in the classroom and uh you know if you're  
**Translation:** 

**[7421.92s] English:** if you discover that you're not getting through one way you can do it another way if the student's  
**Translation:** 

**[7426.40s] English:** have questions you can handle the questions ultimately you're also feeling the the the crowd  
**Translation:** 

**[7434.16s] English:** the students of what they're struggling with what they're picking up just looking at them  
**Translation:** 

**[7438.88s] English:** through the questions but even  
**Translation:** 

**[7440.00s] English:** just through their eyes yeah and because of the preparation you can uh you can dance you can dance  
**Translation:** 

**[7446.10s] English:** you can you can say it another way or give another angle are there in particular ideas and algorithms  
**Translation:** 

**[7454.66s] English:** of computer science that you find were big aha moments for students where they for some reason  
**Translation:** 

**[7461.70s] English:** once they got it it clicked for them and they fell in love with computer science or is it individual  
**Translation:** 

**[7467.56s] English:** is it different for everybody it's different for everybody you have to work differently with  
**Translation:** 

**[7472.22s] English:** students some some of them just don't don't need much influence you you know they they're just  
**Translation:** 

**[7481.04s] English:** running with what they're doing and they just need an ear now and then others need a little  
**Translation:** 

**[7485.72s] English:** prodding others need to be persuaded to collaborate among themselves rather than working alone  
**Translation:** Vocabulary: collaborate: 合作; prodding: 督促

**[7492.14s] English:** um they have their personal ups and downs so  
**Translation:** 

**[7497.56s] English:** you know you have to have to deal with each student as a human being and uh bring out the  
**Translation:** 

**[7505.68s] English:** best humans are complicated yeah perhaps a silly question if you could relive a moment in your life  
**Translation:** 

**[7513.74s] English:** outside of family because it made you truly happy or perhaps because it changed the direction of  
**Translation:** Vocabulary: relive: 重新体验

**[7519.44s] English:** your life in a profound way what moment would you pick i was kind of a lazy student as an  
**Translation:** 

**[7527.10s] English:** undergraduate  
**Translation:** Vocabulary: profound: 深刻; undergraduate: 本科生

**[7527.56s] English:** and even in my first year in graduate school and i think it was when i started doing research  
**Translation:** 

**[7536.24s] English:** i had a couple of summer jobs where i was able to contribute and i had an idea  
**Translation:** 

**[7543.92s] English:** and then there was one particular course on mathematical methods and operations research  
**Translation:** 

**[7550.22s] English:** where i just gobbled up the material and i scored 20 points higher than anybody else in the class  
**Translation:** Vocabulary: gobbled: 消化; mathematical: 数学的

**[7557.56s] English:** and came to the attention of the faculty  
**Translation:** 

**[7560.00s] English:** and it made me realize that I had some ability that it was going somewhere.  
**Translation:** 

**[7568.82s] English:** You realize you're pretty good at this thing.  
**Translation:** 

**[7572.02s] English:** I don't think there's a better way to end it, Richard.  
**Translation:** 

**[7574.28s] English:** It was a huge honor.  
**Translation:** 

**[7575.28s] English:** Thank you for decades of incredible work.  
**Translation:** 

**[7578.10s] English:** Thank you for talking to me.  
**Translation:** 

**[7578.98s] English:** Thank you.  
**Translation:** 

**[7579.32s] English:** It's been a great pleasure.  
**Translation:** 

**[7580.96s] English:** You're a superb interviewer.  
**Translation:** 

**[7584.74s] English:** I'll stop it.  
**Translation:** 

**[7586.58s] English:** Thanks for listening to this conversation with Richard Karp.  
**Translation:** 

**[7589.18s] English:** And thank you to our sponsors, Eight Sleep and Cash App.  
**Translation:** 

**[7593.96s] English:** Please consider supporting this podcast by going to eightsleep.com slash Lex  
**Translation:** Vocabulary: eightsleep: 八睡; sponsors: 赞助商

**[7598.58s] English:** to check out their awesome mattress and downloading Cash App and using code Lex podcast.  
**Translation:** 

**[7606.00s] English:** Click the links, buy the stuff, even just visiting the site,  
**Translation:** Vocabulary: mattress: 床垫

**[7609.76s] English:** but also considering the purchase helps them know that this podcast is worth supporting in the future.  
**Translation:** 

**[7615.48s] English:** It really is the best way to support this journey I'm on.  
**Translation:** 

**[7619.18s] English:** If you enjoy this thing, subscribe on YouTube, review it with five stars on Apple podcast,  
**Translation:** 

**[7624.14s] English:** support it on Patreon, connect with me on Twitter at Lex Friedman, if you can figure out how to spell that.  
**Translation:** 

**[7631.28s] English:** And now let me leave you with some words from Isaac Asimov.  
**Translation:** 

**[7635.56s] English:** I do not fear computers.  
**Translation:** 

**[7637.84s] English:** I fear lack of them.  
**Translation:** 

**[7640.42s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 

**[7649.18s] English:** Bye.  
**Translation:** 

**[7649.84s] English:** Bye.  
**Translation:** 

**[7649.88s] English:** Bye.  
**Translation:** 

**[7650.18s] English:** Bye.  
**Translation:** 

**[7650.22s] English:** Bye.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
