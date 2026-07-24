# Podcast vocabulary notes
Source file: Lex Fridman - Jim Keller： The Future of Computing, AI, Life, and Consciousness ｜ Lex Fridman Podcast #162.opus

**[0.00s] English:** The following is a conversation with Jim Keller, his second time on the podcast.  
**Translation:** 

**[5.06s] English:** Jim is a legendary microprocessor architect and is widely seen as one of the greatest engineering minds of the computing age.  
**Translation:** Vocabulary: computing: 计算机; microprocessor: 微处理器

**[14.60s] English:** In a peculiar twist of space-time in our simulation, Jim is also a brother-in-law of Jordan Peterson.  
**Translation:** 

**[21.58s] English:** We talk about this and about computing, artificial intelligence, consciousness, and life.  
**Translation:** Vocabulary: peterson: 乔纳森·佩里森; simulation: 模拟

**[28.36s] English:** Quick mention of our sponsors.  
**Translation:** 

**[31.32s] English:** Athletic Greens All-in-One Nutrition Drink, Brooklyn & Sheets, ExpressVPN, and Belcampo Grass-Fed Meat.  
**Translation:** Vocabulary: belcampo: 贝尔坎普牧场; sponsors: 赞助商

**[39.58s] English:** Click the sponsor links to get a discount and to support this podcast.  
**Translation:** 

**[43.58s] English:** As a side note, let me say that Jim is someone who, on a personal level, inspired me to be myself.  
**Translation:** 

**[49.86s] English:** There was something in his words, on and off the mic, or perhaps that he even paid attention to me at all,  
**Translation:** 

**[56.20s] English:** that almost told me, you're alright kid.  
**Translation:** 

**[59.16s] English:** A kind of pat on the back that can make the difference between a mind that flourishes  
**Translation:** 

**[63.20s] English:** and a mind that is broken down by the cynicism of the world.  
**Translation:** Vocabulary: cynicism: 世故悲观; flourishes: 茁壮成长

**[68.10s] English:** So I guess that's just my brief few words of thank you to Jim,  
**Translation:** 

**[71.74s] English:** and in general, gratitude for the people who have given me a chance on this podcast, in my work, and in life.  
**Translation:** 

**[78.58s] English:** If you enjoy this thing, subscribe on YouTube, review it on Apple Podcasts, follow on Spotify,  
**Translation:** 

**[84.28s] English:** support it on Patreon, or connect with me on Twitter at Lex Friedman.  
**Translation:** Vocabulary: subscribe: 订阅

**[88.36s] English:** And now, here's my conversation with Jim Keller.  
**Translation:** 

**[93.24s] English:** What's the value and effectiveness of theory versus engineering, this dichotomy,  
**Translation:** Vocabulary: dichotomy: 对立面; effectiveness: 有效性

**[97.84s] English:** in building good software or hardware systems?  
**Translation:** 

**[103.44s] English:** Well, good design is both.  
**Translation:** 

**[106.36s] English:** I guess that's pretty obvious.  
**Translation:** 

**[108.68s] English:** But engineering, do you mean, you know, reduction of practice of known methods?  
**Translation:** 

**[113.30s] English:** And then science is the pursuit of discovering things that people don't understand.  
**Translation:** 

**[117.56s] English:** Or software.  
**Translation:** 

**[118.16s] English:** Solving unknown problems.  
**Translation:** 

**[120.00s] English:** definitions are interesting here but i was thinking more in theory constructing models  
**Translation:** 

**[125.24s] English:** that kind of generalize about how things work and engineering is actually building stuff the  
**Translation:** 

**[132.90s] English:** pragmatic like okay we have these nice models but how do we actually get things to work maybe  
**Translation:** Vocabulary: generalize: 泛化; pragmatic: 务实

**[138.24s] English:** economics is a nice example like economists have all these models of how the economy works and  
**Translation:** 

**[143.74s] English:** how different policies will have an effect but then there's the actual okay let's call it  
**Translation:** Vocabulary: economists: 经济学家

**[149.76s] English:** engineering of like actually deploying the policies so computer design is almost all  
**Translation:** 

**[155.02s] English:** engineering and reduction of practice of known methods now because of the complexity of the  
**Translation:** Vocabulary: complexity: 复杂性; deploying: 部署

**[161.58s] English:** computers we built you know you could think you're well we'll just go write some code and then we'll  
**Translation:** 

**[167.00s] English:** verify it and we'll put it together and then you find out that the combination of all that stuff  
**Translation:** Vocabulary: verify: 验证

**[171.70s] English:** is complicated and then you have to be inventive to figure out how to do it right so that's that's  
**Translation:** 

**[177.76s] English:** definitely has happens a lot  
**Translation:** Vocabulary: inventive: 富有创造力的

**[179.06s] English:** and then every so often some big idea happens but it might be one person and that idea is in what  
**Translation:** 

**[187.46s] English:** in the space of engineering or is it in the space well i'll give you an example so one of the limits  
**Translation:** 

**[192.04s] English:** of computer performance is branch prediction so and there's there's a whole bunch of ideas about  
**Translation:** 

**[197.64s] English:** how good you could predict a branch and people said there's a limit to it it's an asymptotic  
**Translation:** Vocabulary: asymptotic: 渐近的

**[202.28s] English:** curve and somebody came up with a better way to do branch prediction it was a lot better  
**Translation:** 

**[207.14s] English:** and he published a paper  
**Translation:** 

**[209.06s] English:** on it and every computer in the world now uses it and it was one idea so the the engineers who  
**Translation:** 

**[215.94s] English:** build branch prediction hardware were happy to drop the one kind of training array and put it  
**Translation:** 

**[220.90s] English:** in another one so it was it was a real idea and branch prediction is as one of the key problems  
**Translation:** 

**[228.42s] English:** underlying all of sort of the lowest level of software it boils down to branch prediction boils  
**Translation:** 

**[234.02s] English:** down to uncertainty computers are limited by you know single thread computers limited by two things  
**Translation:** 

**[239.06s] English:** so you can't predict what's going to happen and you can't predict what's going to happen and you can't predict  
**Translation:** 

**[240.00s] English:** Predictability of the path of the branches and predictability of the locality of data.  
**Translation:** 

**[245.44s] English:** So we have predictors that now predict both of those pretty well.  
**Translation:** Vocabulary: predictors: 预测器

**[249.28s] English:** So memory is, you know, a couple hundred cycles away, local cache is a couple cycles away.  
**Translation:** 

**[254.66s] English:** When you're executing fast, virtually all the data has to be in the local cache.  
**Translation:** Vocabulary: cache: 本地缓存; executing: 执行

**[259.08s] English:** So a simple program says, you know, add one to every element in an array.  
**Translation:** 

**[263.40s] English:** It's really easy to see what the stream of data will be.  
**Translation:** 

**[266.76s] English:** But you might have a more complicated program that, you know, says, get an element of this  
**Translation:** 

**[270.76s] English:** array, look at something, make a decision, go get another element, it's kind of random.  
**Translation:** 

**[275.28s] English:** And you can think, that's really unpredictable.  
**Translation:** 

**[277.86s] English:** And then you make this big predictor that looks at this kind of pattern and you realize,  
**Translation:** Vocabulary: predictor: 预测器

**[281.26s] English:** well, if you get this data and this data, then you probably want that one.  
**Translation:** 

**[284.26s] English:** And if you get this one and this one and this one, you probably want that one.  
**Translation:** 

**[287.76s] English:** And is that theory or is that engineering?  
**Translation:** 

**[290.02s] English:** Like the paper that was written, was it asymptotic kind of discussion or is it more like, here's  
**Translation:** 

**[295.66s] English:** a hack that works well?  
**Translation:** 

**[296.74s] English:** It's a little bit of both.  
**Translation:** 

**[299.22s] English:** Like there's information theory in it, I think, somewhere.  
**Translation:** 

**[301.50s] English:** Okay.  
**Translation:** 

**[302.50s] English:** So it's actually trying to prove some kind of stuff.  
**Translation:** 

**[303.98s] English:** Yeah.  
**Translation:** 

**[304.98s] English:** But once you know the method, implementing it is an engineering problem.  
**Translation:** 

**[309.66s] English:** Now there's a flip side of this, which is in a big design team, what percentage of people  
**Translation:** Vocabulary: implementing: 执行

**[314.54s] English:** think their plan or their life's work is engineering versus inventing things?  
**Translation:** 

**[323.60s] English:** So lots of companies will reward you for filing patents.  
**Translation:** 

**[326.74s] English:** Yes.  
**Translation:** 

**[327.74s] English:** Many big companies get stuck because to get promoted, you have to come up with something  
**Translation:** 

**[331.74s] English:** new.  
**Translation:** 

**[333.06s] English:** And then what happens is everybody's trying to do some random new thing, 99% of which  
**Translation:** 

**[337.52s] English:** doesn't matter, and the basics get neglected.  
**Translation:** 

**[343.26s] English:** Or there's a dichotomy.  
**Translation:** Vocabulary: dichotomy: 对立面; neglected: 被忽视

**[345.62s] English:** They think like the cell library and the basic CAD tools or basic software validation methods,  
**Translation:** 

**[353.40s] English:** that's simple stuff.  
**Translation:** Vocabulary: validation: 验证方法

**[354.74s] English:** They want to work on the exciting stuff.  
**Translation:** 

**[356.26s] English:** Yeah.  
**Translation:** 

**[356.54s] English:** And then they spend lots of time trying to figure out how to patent something.  
**Translation:** 

**[360.00s] English:** and that's mostly useless but the breakthroughs on simple stuff no no you know you have to do  
**Translation:** Vocabulary: breakthroughs: 重大进展; patent: 专利

**[366.90s] English:** the simple stuff really well if you're building a building out of bricks you want great bricks  
**Translation:** 

**[372.52s] English:** so you go to two places to sell bricks so one guy says yeah they're over there in an ugly pile and  
**Translation:** 

**[377.96s] English:** the other guy is like lovingly tells you about the 50 kinds of bricks and how hard they are and how  
**Translation:** 

**[382.44s] English:** beautiful they are and how square they are and you know which one you can buy bricks from which is  
**Translation:** Vocabulary: lovingly: 深情地

**[388.46s] English:** going to make a better house so you're talking about the craftsman the person who understands  
**Translation:** 

**[393.06s] English:** bricks who loves breaks who loves the variety that's a good word you know good engineering  
**Translation:** Vocabulary: craftsman: 手艺人

**[397.22s] English:** is great craftsmanship and when you start thinking engineering is about invention  
**Translation:** 

**[404.12s] English:** and set up a system that rewards invention the craftsmanship gets neglected okay so maybe one  
**Translation:** Vocabulary: craftsmanship: 手工技艺

**[412.22s] English:** perspective is the theory the science overemphasizes invention and engineering  
**Translation:** 

**[418.46s] English:** emphasizes craftsmanship and therefore like so if you it doesn't matter what you do theory well  
**Translation:** Vocabulary: overemphasizes: 过分强调

**[424.32s] English:** everybody does like read the tech rags they're always talking about some breakthrough or intervention  
**Translation:** 

**[428.62s] English:** innovation and everybody thinks that's the most important thing but the number of innovative ideas  
**Translation:** 

**[433.78s] English:** is actually relatively low we need them right an innovation creates a whole new opportunity like  
**Translation:** 

**[439.88s] English:** when when some guy invented the Internet right like that was a big thing the million people that  
**Translation:** 

**[446.84s] English:** wrote software against that were  
**Translation:** 

**[448.46s] English:** mostly doing engineering software writing so the elaboration of that idea was huge  
**Translation:** Vocabulary: elaboration: 详细阐述

**[453.32s] English:** i don't know if you know brendan and i he wrote javascript in 10 days and that's an interesting  
**Translation:** 

**[458.82s] English:** story it makes me wonder and it was you know famously for many years considered to be a pretty  
**Translation:** Vocabulary: brendan: 布兰登

**[465.16s] English:** crappy programming language still is perhaps it's been improving sort of consistently but  
**Translation:** 

**[471.42s] English:** the interesting thing about that guy is you know he doesn't get any awards  
**Translation:** Vocabulary: crappy: 糟糕的

**[476.94s] English:** you don't get a nobel prize or a  
**Translation:** 

**[480.00s] English:** metal or uh preventing a crappy piece of you know that software code that well that is currently the  
**Translation:** Vocabulary: nobel: 诺贝尔奖

**[487.48s] English:** number one programming language in the world and runs now is increasingly running the back end of  
**Translation:** 

**[493.32s] English:** the internet does he does he know why everybody uses it like that would be an interesting thing  
**Translation:** 

**[499.00s] English:** was it the right thing at the right time because like when stuff like javascript came out like  
**Translation:** 

**[505.02s] English:** there's a move from you know writing c programs and c++ to let's call it what they call managed  
**Translation:** 

**[510.98s] English:** code frameworks where you write simple code it might be interpreted it has lots of libraries  
**Translation:** 

**[516.44s] English:** productivity is high you don't have to be an expert so you know java was supposed to solve  
**Translation:** Vocabulary: interpreted: 解释执行

**[521.26s] English:** all the world's problems it was complicated javascript came out you know after a bunch of  
**Translation:** 

**[525.90s] English:** other scripting languages i'm not an expert on it but yeah was it the right thing at the right time  
**Translation:** 

**[531.10s] English:** or was there something you know clever because he wasn't the  
**Translation:** 

**[534.96s] English:** only one  
**Translation:** 

**[535.02s] English:** there's a few elements and maybe if he figured out what it was no then he'd get a prize  
**Translation:** 

**[540.66s] English:** like that constructive theory yeah you know maybe his problem is he hasn't defined this  
**Translation:** 

**[546.58s] English:** or he just needs a good promoter well i think there was a bunch of blog posts written about  
**Translation:** 

**[552.36s] English:** it which is like wrong is right which is like doing the crappy thing fast just like  
**Translation:** Vocabulary: promoter: 推广者

**[559.94s] English:** hacking together the thing that answers some of the needs and then iterating over time  
**Translation:** 

**[564.84s] English:** literally  
**Translation:** Vocabulary: hacking: 临时凑合

**[564.96s] English:** listening to developers like listening to people who actually use the thing this is something you  
**Translation:** 

**[569.02s] English:** can do more in software but the right time like you have to sense you have to have a good instinct  
**Translation:** Vocabulary: instinct: 直觉

**[575.02s] English:** of when is the right time for the right tool and make it super simple and just get it out there  
**Translation:** 

**[582.42s] English:** the problem is this is true with hardware this is less true with software is there's backward  
**Translation:** Vocabulary: backward: 落后

**[587.56s] English:** compatibility that just drags behind you as you know as you try to fix all the mistakes of the  
**Translation:** 

**[593.46s] English:** past but the the timing  
**Translation:** Vocabulary: compatibility: 过去问题

**[594.96s] English:** it was good there's something about that it wasn't accidental you have to like  
**Translation:** 

**[600.00s] English:** give yourself over to the you have to have this like broad sense of what's needed now  
**Translation:** 

**[606.64s] English:** both scientifically and like the community and just like this it was obvious that uh there was  
**Translation:** 

**[615.00s] English:** no the interesting thing about javascript is everything that ran in the browser at the time  
**Translation:** 

**[620.68s] English:** like java and and i think other like scheme other programming languages they were all in a separate  
**Translation:** 

**[628.20s] English:** external container and then javascript was literally just injected into the web page it was  
**Translation:** 

**[634.78s] English:** the dumbest possible thing in running in the same thread as everything else and like uh it was  
**Translation:** 

**[641.50s] English:** inserted as a comment so javascript code is inserted as a comment in the html code and it  
**Translation:** 

**[647.86s] English:** was i mean it's there's it's either genius or super dumb but it's like right so it has no  
**Translation:** 

**[653.86s] English:** apparatus for like a virtual machine and container it just executed in the frame  
**Translation:** 

**[658.20s] English:** work of the program that's already running and it was that's cool and then uh because something  
**Translation:** 

**[662.68s] English:** about that accessibility the ease of its use uh resulted in then developers innovating of how to  
**Translation:** Vocabulary: accessibility: 易于使用; innovating: 创新

**[670.46s] English:** actually use it i mean i don't even know what to make of that but it does seem to echo across  
**Translation:** 

**[676.30s] English:** different software like stories of different software php has the same story really crappy  
**Translation:** Vocabulary: crappy: 糟糕的

**[681.76s] English:** language they just took over the world well we just have a joke that the random length instructions  
**Translation:** 

**[688.06s] English:** that we use are not the same as the random length instructions that we use are the same as the  
**Translation:** 

**[688.18s] English:** variable length instruction sets always one even though they're obviously worse like nobody knows  
**Translation:** 

**[693.80s] English:** why x86 is arguably the worst architecture you know on the planet it's one of the most popular  
**Translation:** Vocabulary: arguably: 据说

**[699.58s] English:** ones well i mean isn't isn't that also the story of risk versus i mean is that simplicity there's  
**Translation:** 

**[706.38s] English:** something about simplicity that us in this evolutionary process is valued if it's simple  
**Translation:** Vocabulary: evolutionary: 进化; simplicity: 简单

**[714.26s] English:** it's uh gets it spreads faster it seems like  
**Translation:** 

**[718.04s] English:** or is that not always true  
**Translation:** 

**[720.00s] English:** that sound like it's true yeah it could be simple as good but too simple as bad so why did risk win  
**Translation:** 

**[725.22s] English:** you think so far did risk win in the long arc of history we don't know so who's gonna win what  
**Translation:** 

**[732.88s] English:** what's risk what's cisc and who's gonna win in that space in these instruction sets ai software  
**Translation:** 

**[738.20s] English:** is gonna win but there'll be little computers that run little programs like normal all over the place  
**Translation:** 

**[743.58s] English:** but but we're we're going through another transformation so but you think instruction  
**Translation:** 

**[749.58s] English:** sets underneath it all will change yeah they evolve slowly they don't matter very much  
**Translation:** 

**[754.98s] English:** they don't matter very much okay i mean the limits of performance are you know predictability of  
**Translation:** 

**[760.44s] English:** instructions and data i mean that's the big thing and then the usability of it is some you know  
**Translation:** Vocabulary: usability: 易用性

**[766.52s] English:** quality of design quality of tools availability like right now x86 is proprietary with intel and  
**Translation:** 

**[776.00s] English:** amd but they can change it any way they want independently  
**Translation:** Vocabulary: independently: 自主决定; proprietary: 专有技术

**[778.56s] English:** right  
**Translation:** 

**[779.58s] English:** right arm is proprietary to arm and they won't let anybody else change it so it's like a sole point  
**Translation:** 

**[785.52s] English:** and risk 5 is open source so anybody can change it which is super cool but that also might mean  
**Translation:** 

**[791.68s] English:** it gets changed in too many random ways that there's no common subset of it that people can use  
**Translation:** 

**[797.56s] English:** do you like open or do you like closed like if you were to bet all your money on one or the other  
**Translation:** 

**[802.12s] English:** risk 5 versus no idea it's case dependent well x86 oddly enough when intel first started developing it  
**Translation:** 

**[808.16s] English:** they licensed it like seven years ago or something like that i don't know i don't know i don't know i don't know i don't know  
**Translation:** 

**[809.58s] English:** but it states now it at least a hundred percent for many people of people so it was the open mettre la objeto  
**Translation:** 

**[812.92s] English:** and then they moved faster than others and also bought one or two of them  
**Translation:** 

**[817.24s] English:** but there was seven different people making x86 because at the time there was  
**Translation:** 

**[821.96s] English:** 6502 and z80s and you know 8086 and you could argue everybody thought z80 was the better  
**Translation:** 

**[829.44s] English:** instruction set but that was proprietary proprietary to one place oh and the 6 800  
**Translation:** 

**[835.92s] English:** so there's like five different four five different microprocessors  
**Translation:** 

**[838.64s] English:** Until when?  
**Translation:** 

**[840.00s] English:** open got the market share because people felt like they had multiple sources from it and then  
**Translation:** 

**[844.92s] English:** over time it narrowed down to two players so why you as a historian uh why did intel win for so  
**Translation:** Vocabulary: narrowed: 减少到

**[853.32s] English:** long with uh with their processors i mean they were great their process development was great  
**Translation:** 

**[860.64s] English:** so it's just looking back to javascript and brandon ike is uh in microsoft and netscape and  
**Translation:** Vocabulary: brandon: 布兰登; netscape: 网景; processors: 处理器

**[866.60s] English:** all these uh internet browsers microsoft won the browser game because they aggressively stole  
**Translation:** 

**[873.70s] English:** other people's ideas like right after they did it you know i i don't know if intel was stealing  
**Translation:** Vocabulary: aggressively: 积极地; browsers: 浏览器

**[880.16s] English:** other people's ideas they started making a good way stealing just to clarify they started making  
**Translation:** 

**[884.60s] English:** rams random access memories yes and then at the time when the japanese manufacturers came up  
**Translation:** 

**[892.18s] English:** you know they were getting out competed on that and they pivoted the microprocessors  
**Translation:** 

**[896.36s] English:** and  
**Translation:** Vocabulary: microprocessors: 微处理器; pivoted: 转型

**[896.60s] English:** they made the first you know integrated microprocessor programs it was the uh  
**Translation:** 

**[902.20s] English:** 4004 or something who was behind that pivot that's a hell of a pivot andy grove and he was great  
**Translation:** 

**[908.60s] English:** that's a hell of a pivot right and then they led semiconductor industry like they were just a  
**Translation:** 

**[914.68s] English:** little company ibm all kinds of big companies had boatloads of money and they out innovated  
**Translation:** 

**[919.88s] English:** everybody out of the innovative okay yeah yeah so it's not like marketing it's not any other stuff  
**Translation:** 

**[926.12s] English:** they're  
**Translation:** 

**[926.36s] English:** processor designs were pretty good um i think the you know core 2 was probably the first one i thought  
**Translation:** 

**[934.52s] English:** was great it was a really fast processor and then haswell was great what makes a great processor and  
**Translation:** Vocabulary: haswell: 酷睿处理器; processor: 处理器

**[941.72s] English:** that well oh if you just look at it's performance versus everybody else it's you know the size of it  
**Translation:** 

**[947.48s] English:** the you know usability of it so it's not specific some kind of element that makes  
**Translation:** Vocabulary: usability: 易用性

**[951.96s] English:** you beautiful it's just like literally just raw performance is that how you think about  
**Translation:** 

**[956.36s] English:** processors is just like raw performance?  
**Translation:** 

**[959.46s] English:** Of course.  
**Translation:** 

**[960.00s] English:** it's like a horse race the fastest one wins now you don't care how  
**Translation:** 

**[965.68s] English:** well there's the fastest in the environment like you know for years you made the fastest one you  
**Translation:** 

**[972.72s] English:** could and then people started to have power limits so then you made the fastest at the  
**Translation:** 

**[976.32s] English:** right power point and then and then when we started doing multi-processors like if you could  
**Translation:** 

**[982.32s] English:** scale your processors more than the other guy you could be 10 faster on like a single thread but you  
**Translation:** Vocabulary: processors: 处理器

**[987.16s] English:** have more threads so there's lots of variability and then arm really explored like you know they  
**Translation:** 

**[995.66s] English:** have the a series and the r series and the m series like a family of processors for all these  
**Translation:** Vocabulary: variability: 多样性

**[1000.94s] English:** different design points from like unbelievably small and simple and so then when you're doing  
**Translation:** 

**[1005.72s] English:** the design it's sort of like this big palette of cpus like they're the only ones with a credible  
**Translation:** Vocabulary: credible: 可信的; palette: 调色板; unbelievably: 难以置信地

**[1011.18s] English:** you know top to bottom palette and what do you mean a credible top to bottom well  
**Translation:** 

**[1017.16s] English:** there's people who make microcontrollers that are small but they don't have a fast one there's  
**Translation:** 

**[1020.54s] English:** people make fast processors but don't have a little a medium one or a small one is that hard to do  
**Translation:** 

**[1025.86s] English:** that full palette that's that seems like a it's a lot of different so what's the difference in  
**Translation:** 

**[1030.34s] English:** uh the arm folks and intel in terms of the way they're approaching this problem well intel  
**Translation:** 

**[1037.34s] English:** almost all their processor designs were you know very custom high-end you know for the last 15  
**Translation:** 

**[1042.82s] English:** 20 years the fastest horse possible yeah in one horse race  
**Translation:** 

**[1047.16s] English:** yeah and the architecture they're really good but the company itself was fairly insular to what's  
**Translation:** Vocabulary: insular: 孤陋寡闻

**[1053.76s] English:** going on in the industry with cad tools and stuff and there's this debate about custom design versus  
**Translation:** 

**[1058.40s] English:** synthesis and how do you approach that i'd say intel was slow on the getting to synthesize  
**Translation:** Vocabulary: synthesis: 综合; synthesize: 合成

**[1064.30s] English:** processors arm came in from the bottom and they generated ip which went to all kinds of customers  
**Translation:** 

**[1070.40s] English:** so they had very little say in how the customer implemented their ip so arm is super friendly to  
**Translation:** 

**[1077.16s] English:** synthesis ip environment whereas intel  
**Translation:** 

**[1080.00s] English:** said we're going to make this great client chip server chip with our own cad tools with our own  
**Translation:** 

**[1084.76s] English:** process with our own you know other supporting ip and everything only works with our stuff  
**Translation:** 

**[1089.84s] English:** so is that um is arm winning the mobile platform space in terms of process and so  
**Translation:** 

**[1098.22s] English:** in that and what you're describing is why they're winning well they had lots of people doing lots of  
**Translation:** 

**[1104.98s] English:** different experiments so they controlled the processor architecture and ip but they let people  
**Translation:** Vocabulary: processor: 处理器

**[1110.10s] English:** put in lots of different chips and there was a lot of variability in what happened there  
**Translation:** 

**[1114.24s] English:** whereas intel when they made their mobile their foray into mobile they had one team doing one  
**Translation:** Vocabulary: foray: 尝试

**[1119.72s] English:** part right so it wasn't 10 experiments and then their mindset was pc mindset microsoft software  
**Translation:** 

**[1127.06s] English:** mindset and that brought a whole bunch of things along that uh the mobile world the embedded world  
**Translation:** Vocabulary: embedded: 嵌入式; mindset: 思维模式

**[1131.74s] English:** don't do do you think it was possible for intel to pivot  
**Translation:** 

**[1134.82s] English:** hopefully  
**Translation:** 

**[1134.98s] English:** hard and win the mobile market that's a hell of a difficult thing to do right for a huge company to  
**Translation:** 

**[1141.12s] English:** just pivot i mean so interesting to because we'll talk about your current work it's like  
**Translation:** 

**[1147.96s] English:** it's clear that pcs were dominating for several decades like desktop computers and then mobile  
**Translation:** 

**[1155.46s] English:** it's unclear it's a leadership question like that like apple under steve jobs when he came back they  
**Translation:** 

**[1163.16s] English:** pivoted multiple times  
**Translation:** 

**[1164.98s] English:** you know they built ipads and itunes and phones and tablets and great macs like like who knew  
**Translation:** Vocabulary: pivoted: 调整方向

**[1171.24s] English:** computers should be made out of aluminum nobody knew that but they're great it's super fun though  
**Translation:** 

**[1177.32s] English:** steve yeah steve jobs like they pivoted multiple times and uh you know the old intel they they did  
**Translation:** Vocabulary: aluminum: 铝合金

**[1184.16s] English:** that multiple times they made drams and processors and processes and i gotta ask this what was it  
**Translation:** 

**[1191.24s] English:** like working with steve jobs i didn't work with him did you interact with him i didn't work with him  
**Translation:** Vocabulary: drams: 动态随机存取内存; processors: 处理器

**[1194.98s] English:** twice i said hi to him twice in the cafeteria  
**Translation:** 

**[1200.00s] English:** did you say hi he said hey fellas he was friendly he was wandering around and with somebody he  
**Translation:** 

**[1208.34s] English:** couldn't find a table because the cafeteria was was packed and i gave my table but i worked for  
**Translation:** 

**[1214.22s] English:** mike culbert who talked to like mike mike was the unofficial cto of apple and a brilliant guy and  
**Translation:** Vocabulary: culbert: 库伯特; unofficial: 非正式的

**[1220.40s] English:** he worked for steve for 25 years maybe more and he talked to steve multiple times a day  
**Translation:** 

**[1225.34s] English:** and he was one of the people who could put up with steve's let's say brilliance and intensity  
**Translation:** Vocabulary: brilliance: 卓越智慧

**[1230.68s] English:** and and steve really liked him and steve trusted mike to translate the shit he thought up  
**Translation:** 

**[1238.42s] English:** into engineering products at work and then mike ran a group called platform architecture and i  
**Translation:** 

**[1243.32s] English:** was in that group so many times i'd be sitting with mike and the phone would ring it'd be steve  
**Translation:** 

**[1248.62s] English:** and mike would hold the phone like this because steve would be yelling about something or other  
**Translation:** 

**[1252.12s] English:** yeah and then he would translate and he'd translate and then he would  
**Translation:** 

**[1255.32s] English:** say steve wants us to do this so was steve a good engineer or no i don't know he was a great  
**Translation:** 

**[1262.94s] English:** idea guy idea person he's a really good selector for talent yeah that seems to be one of the key  
**Translation:** 

**[1269.16s] English:** elements of leadership right and then he was a really good first principles guy like like  
**Translation:** Vocabulary: selector: 选择者

**[1273.62s] English:** somebody say something couldn't be done and he would just think that's obviously wrong right  
**Translation:** 

**[1279.98s] English:** but you know maybe it's hard to do maybe it's expensive to do maybe we need different  
**Translation:** 

**[1285.32s] English:** people you know there's like a whole bunch of you know if you want to do something hard  
**Translation:** 

**[1288.46s] English:** you know maybe it takes time maybe you have to iterate there's a whole bunch of things  
**Translation:** 

**[1292.42s] English:** you could think about but saying it can't be done is stupid how would you compare so it seems like  
**Translation:** 

**[1298.84s] English:** elon musk is more engineering centric but it's also i think he considers himself a designer too  
**Translation:** 

**[1305.52s] English:** he has a design mind steve jobs feels like he's much more idea space design space versus engineering  
**Translation:** 

**[1312.28s] English:** yeah just make it happen like the world should be this way  
**Translation:** 

**[1315.32s] English:** just figure it out but but he used computers you know he had computer people  
**Translation:** 

**[1320.00s] English:** talk to him all the time like mike was a really good computer guy he knew what computers could do  
**Translation:** 

**[1324.72s] English:** computer meaning computer hardware like hardware software all the pieces the whole thing and then  
**Translation:** 

**[1329.36s] English:** he would you know have an idea about what could we do with this next that was grounded in reality it  
**Translation:** 

**[1335.92s] English:** wasn't like he was you know just finger painting on the wall and wishing somebody would interpret  
**Translation:** 

**[1340.48s] English:** it like so he had this interesting connection because you know he wasn't a computer architect  
**Translation:** Vocabulary: interpret: 解释

**[1346.96s] English:** or designer but he had an intuition from the computers we had to what could happen  
**Translation:** 

**[1352.72s] English:** and essentially you say intuition because it seems like he was pissing off a lot of engineers  
**Translation:** Vocabulary: intuition: 直觉

**[1359.92s] English:** in his intuition about what can and can't be done those the like the what is all these  
**Translation:** 

**[1366.32s] English:** stories about like floppy disks and all that kind of stuff like yeah so in in steve the first round  
**Translation:** Vocabulary: floppy: 软盘

**[1371.92s] English:** like he'd go into a lab and look at what's going on and hate it and  
**Translation:** 

**[1376.96s] English:** uh fire people or or ask somebody in the elevator what they're doing for apple and you know not be  
**Translation:** 

**[1382.88s] English:** happy when he came back my impression was is he surrounded himself with a relatively small group  
**Translation:** 

**[1389.44s] English:** of people yes and didn't really interact outside of that as much and then the joke was you'd see  
**Translation:** 

**[1395.04s] English:** like somebody moving a prototype through the quad with a with a black blanket over it and that was  
**Translation:** 

**[1401.04s] English:** because it was secret you know partly from steve because they didn't want steve to see it until it  
**Translation:** Vocabulary: prototype: 样品

**[1405.76s] English:** was ready yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah  
**Translation:** 

**[1406.96s] English:** the dynamic with johnny ive and steve is interesting it's like you don't wanna  
**Translation:** Vocabulary: wanna: 想

**[1414.32s] English:** he ruins as many ideas as he generates yeah yeah it's a dangerous kind of line to walk  
**Translation:** 

**[1421.92s] English:** if you have a lot of ideas like like gordon bell was famous for ideas  
**Translation:** 

**[1426.56s] English:** right and it wasn't that the percentage of good ideas was way higher than anybody else  
**Translation:** 

**[1431.28s] English:** it was he had so many ideas and and he was also good at talking to people about it and getting the  
**Translation:** 

**[1436.96s] English:** facts right and you know seeing through stuff  
**Translation:** 

**[1440.00s] English:** whereas elon was like hey i want to build rockets so steve would hire a bunch of rocket guys and  
**Translation:** 

**[1446.04s] English:** elon would go read rocket manuals so elon is a better engineer a sense like or like more uh  
**Translation:** 

**[1452.80s] English:** like a love and passion for the manuals yeah and the details the details the craftsmanship too  
**Translation:** Vocabulary: craftsmanship: 工艺水准

**[1460.14s] English:** right well i guess you had craftsmanship too but of a different kind what do you make of the  
**Translation:** 

**[1465.20s] English:** just the standard for just a little longer what do you make of like the anger and the passion  
**Translation:** 

**[1469.76s] English:** and all that the the firing and the mood swings and the madness the you know being emotional and  
**Translation:** 

**[1477.78s] English:** all that that's steve and i i guess elon too so what is that a is that a bug or a feature  
**Translation:** 

**[1483.06s] English:** it's a feature so there's a graph which is uh y-axis productivity yeah x-axis at zero it's chaos  
**Translation:** 

**[1491.94s] English:** yeah and infinity it's complete order yeah right so as you go from the you know the  
**Translation:** 

**[1499.76s] English:** as you improve order you improve productivity yeah and at some point productivity peaks  
**Translation:** 

**[1505.92s] English:** and then it goes back down again too much order nothing can happen yes but the question is is  
**Translation:** 

**[1511.62s] English:** how close to the chaos is that no no here's the thing is once you start moving in a direction  
**Translation:** 

**[1516.52s] English:** order the force vector to drive you towards order is unstoppable oh and every organization will  
**Translation:** 

**[1523.54s] English:** move to the place where their productivity is stymied by order so you need uh so the question  
**Translation:** 

**[1529.76s] English:** of course like because it also feels really good as you get more organized and productivity  
**Translation:** Vocabulary: stymied: 阻碍

**[1535.44s] English:** goes up the organization feels it they orient towards it right to hire more people they  
**Translation:** 

**[1541.16s] English:** get more guys who can run process you get bigger right and then inevitably inevitably  
**Translation:** Vocabulary: inevitably: 必然; orient: 导向

**[1547.90s] English:** the organization gets captured by the bureaucracy that manages all the processes right and then  
**Translation:** 

**[1554.16s] English:** humans really like that and so if you just walk into a room and say guys love what you're  
**Translation:** Vocabulary: bureaucracy: 官僚体系

**[1559.34s] English:** doing  
**Translation:** 

**[1559.76s] English:** you  
**Translation:** 

**[1560.00s] English:** but i need you to have less order if you don't have some force behind that nothing will happen  
**Translation:** 

**[1567.60s] English:** i can't tell you on how many levels that's profound so so that's why i'd say it's a feature  
**Translation:** Vocabulary: profound: 深奥

**[1573.64s] English:** now could you be nicer about it i don't know i don't know any good examples of being nicer about  
**Translation:** 

**[1579.74s] English:** it well that the funny thing is to get stuff done you need people who can manage stuff and manage  
**Translation:** 

**[1585.52s] English:** people because humans are complicated they need lots of care and feeding that you need to tell  
**Translation:** 

**[1588.74s] English:** they look nice and they're doing good stuff and pat them on the back right i don't know you tell  
**Translation:** 

**[1594.36s] English:** me is that is that needed oh yeah humans need that i had a friend he started to manage a group and he  
**Translation:** 

**[1598.78s] English:** said i figured it out you have to praise them before they do anything i was waiting until they  
**Translation:** 

**[1604.30s] English:** were done and they're always mad at me now i tell them what a great job they're doing while they're  
**Translation:** 

**[1608.46s] English:** doing it but then you get stuck in that trap because then when you're not doing something  
**Translation:** 

**[1612.12s] English:** how do you confront these people i think a lot of people that had trauma in their childhood  
**Translation:** 

**[1616.50s] English:** would disagree with you successful people  
**Translation:** Vocabulary: confront: 面对; trauma: 创伤

**[1618.46s] English:** that you need to first do the rough stuff and then be nice later i don't know okay but you know  
**Translation:** 

**[1624.12s] English:** engineering companies are full of adults who had all kinds of range of childhoods  
**Translation:** 

**[1627.50s] English:** you know most people had okay childhoods well i don't know if uh and lots of people only work  
**Translation:** 

**[1633.70s] English:** for praise which is weird you mean like everybody i'm not that interested in this but uh well you  
**Translation:** 

**[1641.56s] English:** you're you're probably looking for somebody's approval even still yeah maybe i should  
**Translation:** 

**[1648.46s] English:** think about that maybe somebody who's no longer with this kind of thing i don't know i used to call  
**Translation:** 

**[1654.54s] English:** up my dad and tell him what i was doing he was he was very excited about engineering and stuff  
**Translation:** 

**[1658.46s] English:** you got his approval uh yeah a lot i was lucky like he he decided i was smart and unusual as a  
**Translation:** 

**[1666.86s] English:** kid and that was okay when i was really young so when i like did poorly in school i was dyslexic i  
**Translation:** 

**[1672.54s] English:** didn't read until i was third or fourth grade and they didn't care my parents were like oh he'll be  
**Translation:** Vocabulary: dyslexic: 阅读困难

**[1678.46s] English:** so  
**Translation:** 

**[1680.00s] English:** i was lucky that was cool is he still with us you miss him sure yeah he had parkinson's and  
**Translation:** 

**[1689.88s] English:** then cancer his last 10 years were tough and i killed him killing a man like that's hard  
**Translation:** 

**[1697.10s] English:** the mind well it's pretty good um parkinson's causes slow dementia and uh the the chemotherapy  
**Translation:** Vocabulary: chemotherapy: 化疗; dementia: 痴呆

**[1706.00s] English:** i think accelerated it but it was like hallucinogenic dementia so he was clever  
**Translation:** 

**[1712.46s] English:** and funny and interesting and was it was pretty unusual do you remember conversations  
**Translation:** Vocabulary: accelerated: 加速; hallucinogenic: 幻觉

**[1719.10s] English:** from that time like what do you have fond memories of the guy yeah oh yeah anything come to mind  
**Translation:** 

**[1727.54s] English:** a friend told me one time i could draw a computer on the whiteboard faster than anybody you'd ever  
**Translation:** Vocabulary: whiteboard: 白板

**[1731.96s] English:** met and i said you should meet my dad like when i was a kid he'd come up  
**Translation:** 

**[1736.00s] English:** home and say i was driving by this bridge and i was thinking about it and he pulled out a piece  
**Translation:** 

**[1739.42s] English:** of paper and he draw the whole bridge he was a mechanical engineer yeah and he would just draw  
**Translation:** 

**[1744.40s] English:** the whole thing and then he would tell me about it and tell me how he would have changed it  
**Translation:** 

**[1747.78s] English:** and he had this you know idea that he could understand and conceive anything and i just  
**Translation:** 

**[1753.98s] English:** grew up with that so that was natural so if you know like when i interview people i ask them to  
**Translation:** Vocabulary: conceive: 构思

**[1759.24s] English:** draw a picture of something they did on a whiteboard and it's really interesting like  
**Translation:** 

**[1762.98s] English:** some people draw a little box you know and then they'll say and then this talks to this and yeah  
**Translation:** 

**[1768.44s] English:** i'll be like oh this is frustrating and i had this other guy come in one time he says  
**Translation:** 

**[1772.02s] English:** well i designed a floating point in this chip but i'd really like to tell you how the whole  
**Translation:** Vocabulary: frustrating: 令人沮丧的

**[1775.76s] English:** thing works and then tell you how the floating point works inside of it do you mind if i do  
**Translation:** 

**[1778.82s] English:** that he covered two whiteboards in like 30 minutes and i hired him like yeah he was great  
**Translation:** 

**[1784.16s] English:** this crossman i mean that's the crossmanship to that yeah but also the the mental agility  
**Translation:** 

**[1789.34s] English:** to understand the whole thing right put the pieces in contact  
**Translation:** Vocabulary: agility: 灵活; crossmanship: 技巧

**[1792.96s] English:** you know real view of the balance of how the design worked because if you don't understand  
**Translation:** 

**[1800.00s] English:** it properly when you start to draw it you'll you'll fill up half the whiteboard with like a  
**Translation:** 

**[1804.26s] English:** little piece of it and you know like your ability to lay it out in an understandable way it takes a  
**Translation:** 

**[1809.58s] English:** lot of understanding so and be able to so zoom into the detail and then zoom out and zoom out  
**Translation:** Vocabulary: understandable: 容易理解的

**[1814.74s] English:** really fast and what about the impossible thing you see your dad believed that uh you can do  
**Translation:** 

**[1821.12s] English:** anything that's a weird feature for a craftsman yeah it seems that that uh echoes in your own  
**Translation:** 

**[1830.02s] English:** behavior like that's that's the well it's not that anybody can do anything right now  
**Translation:** 

**[1834.92s] English:** right it's that if you work at it you can get better at it and there might not be a limit  
**Translation:** 

**[1840.80s] English:** and they did funny things like like he always wanted to play piano so at the end of his life  
**Translation:** 

**[1846.98s] English:** he started playing the piano when he had parkinson's and he was terrible  
**Translation:** 

**[1850.48s] English:** you  
**Translation:** 

**[1851.12s] English:** but he thought if he really worked at it in this life maybe the next life he'd be better at it  
**Translation:** 

**[1855.24s] English:** he might be onto something yeah he enjoyed doing it yeah so that's pretty funny  
**Translation:** 

**[1862.38s] English:** do you think the perfect is the enemy of the good in hardware and software engineering  
**Translation:** 

**[1867.54s] English:** it's like we were talking about javascript a little bit and the messiness of the 10-day  
**Translation:** 

**[1872.68s] English:** building process yeah let's you know creative tension right  
**Translation:** Vocabulary: messiness: 杂乱程度

**[1876.90s] English:** hmm so creative tension is you have two different ideas  
**Translation:** 

**[1881.12s] English:** that you can't do both right and and but the fact that you want to do both  
**Translation:** 

**[1887.60s] English:** causes you to go try to solve that problem that's the creative part so if you're building computers  
**Translation:** 

**[1894.96s] English:** like some people say we have the schedule and anything that doesn't fit in the schedule we  
**Translation:** 

**[1898.80s] English:** can't do right so they throw out the perfect because they have a schedule  
**Translation:** 

**[1904.08s] English:** i hate that right then there's other people to say we need to get this perfectly right  
**Translation:** 

**[1909.76s] English:** and no matter what you know more people more money right and there's a really clear idea  
**Translation:** 

**[1917.00s] English:** about what you want some people are really good at articulating it right  
**Translation:** Vocabulary: articulating: 表达清楚

**[1920.00s] English:** so let's call that the perfect yeah yeah all right but that's also terrible because they never ship  
**Translation:** 

**[1925.50s] English:** anything you never hit any goals so now you have the now you have your framework yes you can't  
**Translation:** 

**[1930.62s] English:** throw out stuff because you can't get it done today because maybe you get it done tomorrow  
**Translation:** 

**[1933.90s] English:** the next project right you can't so you have to i work with a guy that i really like working with  
**Translation:** 

**[1940.22s] English:** but he over filters his ideas over filters he'd start thinking about something and as soon as  
**Translation:** 

**[1946.98s] English:** you figure out what's wrong with it you'd throw it out and then i start thinking about it and i  
**Translation:** 

**[1951.38s] English:** you know you come up with an idea and then you find out what's wrong with it and then you give  
**Translation:** 

**[1955.70s] English:** it a little time to set because sometimes you know you figure out how to tweak it or maybe that idea  
**Translation:** Vocabulary: tweak: 调整

**[1960.06s] English:** helps some other idea so idea generation is really funny so you have to give your idea space like  
**Translation:** 

**[1967.08s] English:** spaciousness of mind is key but you also have to execute programs and get shit done and then it  
**Translation:** Vocabulary: spaciousness: 开阔感

**[1973.68s] English:** turns out computer engineering is fun because it takes you know 100 people to  
**Translation:** 

**[1976.96s] English:** build a computer 200 or 300 whatever the number is and people are so variable about you know  
**Translation:** 

**[1983.80s] English:** temperament and you know skill sets and stuff that in a big organization you find that the people who  
**Translation:** 

**[1990.68s] English:** love the perfect ideas and the people that want to get stuffed on yesterday and people like to  
**Translation:** Vocabulary: temperament: 性格

**[1995.08s] English:** come up with ideas and people like to let's say shoot down ideas and it takes the whole  
**Translation:** 

**[2000.28s] English:** it takes a large group of people some are good at generating ideas some are good at filtering ideas  
**Translation:** 

**[2005.84s] English:** and then all  
**Translation:** 

**[2006.96s] English:** in that uh giant mess you're somehow i guess the goal is for that giant mess of people  
**Translation:** 

**[2013.40s] English:** to uh find the perfect path through the the tension the creative tension but like how do  
**Translation:** 

**[2019.14s] English:** you know when you said there's some people good at articulating what perfect looks like what a  
**Translation:** 

**[2023.94s] English:** good design is like if you're sitting in a in a room and uh you have a set of ideas about like  
**Translation:** 

**[2031.52s] English:** how to design a better processor how do you know this is  
**Translation:** 

**[2036.96s] English:** this is something special here this is a good idea  
**Translation:** 

**[2040.00s] English:** try this have you ever brainstormed idea with a couple people that were really smart and you kind  
**Translation:** Vocabulary: brainstormed: 集思广益

**[2044.90s] English:** of go into it and you you don't quite understand it and you're working on it and then you start  
**Translation:** 

**[2050.36s] English:** you know talking about it putting on the whiteboard maybe it takes days or weeks and then  
**Translation:** 

**[2056.40s] English:** your brain starts to kind of synchronize it's really weird like you start to see what each  
**Translation:** 

**[2062.02s] English:** other is thinking and and it starts to work like you can see work like my talent in computer design  
**Translation:** Vocabulary: synchronize: 同步

**[2070.88s] English:** is i can i can see how computers work in my head like really well and i know other people can do  
**Translation:** 

**[2076.32s] English:** that too and when you're working with people that can do that like it is kind of a an amazing  
**Translation:** 

**[2083.38s] English:** experience and then and every once in a while you get to that place and then you find the flaw  
**Translation:** 

**[2089.02s] English:** which is kind of funny because you you can you can fool yourself  
**Translation:** 

**[2092.02s] English:** but the two of you kind of drifted along yeah yeah direction that was useless yeah that happens  
**Translation:** 

**[2098.86s] English:** too like you have to because you know the the nice thing about computer design there's always  
**Translation:** 

**[2104.38s] English:** reduction of practice like you come up with your good ideas and i know some architects who really  
**Translation:** 

**[2109.60s] English:** love ideas and then they work on them and they put it on the shelf they go work on the next idea  
**Translation:** 

**[2114.10s] English:** and put on the shelf they never reduce it to practice so they find out what's good and bad  
**Translation:** 

**[2118.62s] English:** because almost every time i've done something really new  
**Translation:** 

**[2121.86s] English:** you  
**Translation:** 

**[2122.02s] English:** by the time it's done like the good parts are good but i know all the flaws like  
**Translation:** 

**[2127.02s] English:** yeah would you say your career just your own experience is your career defined by  
**Translation:** 

**[2132.68s] English:** mostly by flaws or by successes like if again there's great tension between those  
**Translation:** 

**[2137.40s] English:** if you haven't tried hard yeah right and done something new  
**Translation:** 

**[2143.64s] English:** right then you're not going to be facing the challenges when you build it then you find out  
**Translation:** 

**[2149.96s] English:** all the problems with it and  
**Translation:** 

**[2151.86s] English:** and but when you look back do you see problems or okay oh when i look back um what do you i think  
**Translation:** 

**[2158.62s] English:** earlier in my career  
**Translation:** 

**[2160.00s] English:** like eb5 was the second alpha chip uh i was so embarrassed about the mistakes i could barely  
**Translation:** 

**[2166.94s] English:** talk about it and it was in the guinness book of world records and it was the fastest processor on  
**Translation:** 

**[2171.62s] English:** the planet yeah so it was and at some point i realized that was really a bad mental framework  
**Translation:** Vocabulary: guinness: 吉尼斯纪录; processor: 处理器

**[2178.32s] English:** to deal with like doing something new we did a bunch of new things and some worked out great  
**Translation:** 

**[2182.06s] English:** and some were bad and we learned a lot from it and then the next one we learned a lot that also  
**Translation:** 

**[2188.44s] English:** eb6 also had some really cool things in it i think the proportion of good stuff went up  
**Translation:** 

**[2193.96s] English:** but it had a couple fatal flaws in it that were painful and then uh yeah you learned to channel  
**Translation:** 

**[2202.60s] English:** the pain into like pride not pride really just uh realization about how the world works okay how  
**Translation:** 

**[2210.26s] English:** that kind of idea set works life is suffering that's the reality what uh no it's not well i  
**Translation:** Vocabulary: realization: 觉悟

**[2217.34s] English:** know the buddha said that and  
**Translation:** 

**[2218.44s] English:** a couple other people are stuck on it no it's you know there's this kind of weird combination  
**Translation:** Vocabulary: buddha: 佛陀

**[2223.62s] English:** of good and bad you know light and darkness that you have to tolerate and you know deal with yeah  
**Translation:** 

**[2230.34s] English:** there's definitely lots of suffering in the world depends on the perspective it seems like there's  
**Translation:** Vocabulary: tolerate: 忍受

**[2234.34s] English:** way more darkness but uh that makes the light part really nice what uh computing hardware  
**Translation:** 

**[2241.48s] English:** or um just any kind of even software design are you uh do you find beautiful  
**Translation:** 

**[2248.44s] English:** from your own work from other people's work that you're just uh we were just talking about the  
**Translation:** 

**[2255.46s] English:** the battleground of flaws and mistakes and errors but things that were just beautifully done is  
**Translation:** Vocabulary: battleground: 战场

**[2262.64s] English:** there something that pops to mind well when things are beautifully done usually there's a well set  
**Translation:** 

**[2270.46s] English:** thought out set of abstraction layers so the whole thing works in unison nicely yes and and when i  
**Translation:** Vocabulary: abstraction: 抽象层; unison: 协调一致

**[2278.44s] English:** say abstraction layer that means  
**Translation:** 

**[2280.00s] English:** different components when they work together they work independently they don't have to know what  
**Translation:** Vocabulary: independently: 彼此无关

**[2285.76s] English:** the other one is doing so that decoupling yeah so the famous one was the network stack like there's  
**Translation:** 

**[2291.68s] English:** a seven layer network stack you know data transport and protocol and all the layers and the  
**Translation:** Vocabulary: decoupling: 解耦

**[2296.48s] English:** innovation was is when they really wrote got that right because networks before that didn't define  
**Translation:** 

**[2301.60s] English:** those very well the layers could innovate independently and occasionally the layer  
**Translation:** Vocabulary: innovate: 创新

**[2307.44s] English:** boundary would would you know the interface would be upgraded and that that let you know  
**Translation:** 

**[2312.40s] English:** the the design space breathe and you could do something new in layer seven without having to  
**Translation:** Vocabulary: interface: 接口; upgraded: 升级

**[2318.32s] English:** worry about how layer four worked right and so good design does that and you see it in processor  
**Translation:** 

**[2323.92s] English:** designs when we did the zen design at amd we made several components very modular and you know my  
**Translation:** Vocabulary: modular: 模块化; processor: 处理器

**[2333.12s] English:** insistence at the top was i wanted all the interfaces defined before we wrote the  
**Translation:** 

**[2337.44s] English:** l for the pieces one of the verification leads said if we do this right i can test the pieces  
**Translation:** Vocabulary: insistence: 坚持; interfaces: 接口; verification: 验证

**[2343.60s] English:** so well independently when we put it together we won't find all these interaction bugs because the  
**Translation:** 

**[2348.24s] English:** floating point knows how the cache works and i was a little skeptical but he was mostly right  
**Translation:** Vocabulary: cache: 缓存; skeptical: 怀疑

**[2354.08s] English:** that the modularity of the design greatly improved the quality  
**Translation:** 

**[2358.80s] English:** is that universally true in general would you say about good designs the modularity  
**Translation:** Vocabulary: modularity: 模块化; universally: 普遍地

**[2362.72s] English:** is like usually we talked about this before humans are only so smart like  
**Translation:** 

**[2366.88s] English:** and we're not getting  
**Translation:** 

**[2367.44s] English:** in any smarter right but the complexity of things is going up yeah so you know a beautiful design  
**Translation:** 

**[2375.44s] English:** can't be bigger than the person doing it it's just you know their piece of it like the odds  
**Translation:** Vocabulary: complexity: 复杂性

**[2380.80s] English:** of you doing a really beautiful design of something that's way too hard for you is slow  
**Translation:** 

**[2385.12s] English:** right if it's way too simple for you it's not that interesting it's like well anybody could do that  
**Translation:** 

**[2390.48s] English:** but when you get the right match of your your expertise and you know mental power to the right  
**Translation:** 

**[2396.88s] English:** right design size. That's cool, but that's not big  
**Translation:** 

**[2400.00s] English:** enough to make a meaningful impact in the world so now you have to have some framework to design  
**Translation:** 

**[2405.44s] English:** the pieces so that the whole thing is big and harmonious but you know when you put it together  
**Translation:** 

**[2413.44s] English:** it's you know sufficiently sufficiently interesting to to be used and you know so  
**Translation:** 

**[2419.36s] English:** that's like a beautiful design is matching the limits of that human cognitive capacity  
**Translation:** Vocabulary: cognitive: 认知; sufficiently: 足够

**[2427.92s] English:** to uh to the module you can create and creating a nice interface between those modules  
**Translation:** 

**[2432.96s] English:** and thereby do you think there's a limit to the kind of beautiful complex systems we can  
**Translation:** Vocabulary: interface: 接口; module: 模块

**[2437.28s] English:** build with this kind of modular design it's like uh you know if we build increasingly  
**Translation:** 

**[2445.76s] English:** more complicated you can think of like the internet okay let's scale it down well you  
**Translation:** Vocabulary: modular: 模块化的

**[2450.96s] English:** can think of like social network like twitter as one computing system  
**Translation:** 

**[2457.28s] English:** and but  
**Translation:** 

**[2457.92s] English:** those are little modules yeah right but it's built on it's built on so many components  
**Translation:** 

**[2463.68s] English:** nobody at twitter even understands right so that's so so if an alien showed up and looked  
**Translation:** Vocabulary: alien: 外星人

**[2468.56s] English:** at twitter he wouldn't just see twitter as a beautiful simple thing that everybody uses  
**Translation:** 

**[2472.96s] English:** which is really big you would see the networks it runs on the fiber optics the data is transported  
**Translation:** Vocabulary: optics: 光纤; transported: 传输

**[2479.04s] English:** to the computers the whole thing is so bloody complicated nobody twitter understands it and  
**Translation:** 

**[2483.76s] English:** so i think that's what the alien would sees so yeah if an alien showed up and looked at twitter  
**Translation:** 

**[2488.64s] English:** or looked at the various different networked systems that you can see on earth  
**Translation:** 

**[2493.44s] English:** so imagine they were really smart they could comprehend the whole thing and then they sort of  
**Translation:** Vocabulary: comprehend: 理解; networked: 联网的

**[2498.40s] English:** you know evaluated the human and thought this is really interesting no human on this planet  
**Translation:** 

**[2502.64s] English:** comprehends the system they build no individual well would they even see individual humans  
**Translation:** Vocabulary: comprehends: 理解; evaluated: 评估

**[2508.72s] English:** like we humans are very human-centric entity-centric  
**Translation:** 

**[2512.64s] English:** and so we think of us as the organ as the central organism and the networks as  
**Translation:** 

**[2517.92s] English:** It's just the connection of organisms.  
**Translation:** 

**[2520.00s] English:** from a perspective of an alien from an outside perspective it seems like yeah yeah i get it  
**Translation:** 

**[2526.88s] English:** we're the ants and they'd see the ant colony the ant colony yeah or the result of production of  
**Translation:** 

**[2532.00s] English:** the ant colony which is like cities and yeah it's it's uh yeah in that sense humans are pretty  
**Translation:** 

**[2539.14s] English:** impressive the modularity that we're able to and the and how robust we are to noise and mutation  
**Translation:** 

**[2545.80s] English:** all that kind of stuff well that's because it's stress tested all the time yeah you know you build  
**Translation:** Vocabulary: modularity: 模块化; mutation: 变异; robust: 健壮

**[2549.84s] English:** all these cities with buildings and you get earthquakes occasionally and wars you know some  
**Translation:** 

**[2553.64s] English:** you know wars earthquakes viruses every once in a while you know changes in business plans for  
**Translation:** 

**[2559.62s] English:** you know like shipping or something like like as long as it's all stress tested then  
**Translation:** 

**[2564.96s] English:** it keeps adapting to the the situation so that's that's a curious phenomenon  
**Translation:** 

**[2571.36s] English:** well let's go let's talk about moore's law a little bit it's uh uh at the broad view of  
**Translation:** 

**[2579.42s] English:** moore's law  
**Translation:** 

**[2579.84s] English:** where it's just exponential improvement of uh computing capability uh like open ai for example  
**Translation:** 

**[2586.62s] English:** recently uh published this kind of papers looking at the exponential improvement in the training  
**Translation:** Vocabulary: capability: 能力; computing: 计算; exponential: 指数的

**[2594.76s] English:** efficiency of neural networks for like image net and all that kind of stuff we just got better on  
**Translation:** 

**[2599.46s] English:** this this is purely software aside just figuring out better tricks and algorithms for training  
**Translation:** Vocabulary: neural: 神经网络

**[2606.02s] English:** neural networks and that seems to be improving uh  
**Translation:** 

**[2609.42s] English:** significantly faster than the moore's law prediction you know so that's in the software  
**Translation:** 

**[2614.44s] English:** space like what do you think if moore's law continues or if the general version of moore's  
**Translation:** 

**[2621.80s] English:** law continues do you think that comes mostly from the hardware from the software some mix of the two  
**Translation:** 

**[2627.00s] English:** some interesting totally uh so not not the reduction of the size of the transistor kind  
**Translation:** 

**[2632.98s] English:** of thing but more in the uh uh in the totally interesting kinds of innovations in the hardware  
**Translation:** Vocabulary: innovations: 创新

**[2639.42s] English:** space all that  
**Translation:** 

**[2640.00s] English:** kind of stuff well there's like a half a dozen things going on in that graph so one is there's  
**Translation:** 

**[2647.20s] English:** initial innovations that had a lot of head room to be exploited so you know the efficiency of  
**Translation:** 

**[2653.12s] English:** the networks is improved dramatically and then the decomposability of those and the use going  
**Translation:** Vocabulary: decomposability: 可分解性; dramatically: 显著地; exploited: 利用

**[2659.52s] English:** you know they started running on one computer then multiple computers and multiple gpus and  
**Translation:** 

**[2663.76s] English:** arrays of gpus and they're up to thousands and at some point so so it's sort of like they were  
**Translation:** 

**[2670.80s] English:** consumed they were going from like a single computer application to a thousand computer  
**Translation:** 

**[2674.96s] English:** application so that's not really a moore's law thing that's an independent vector how many  
**Translation:** 

**[2679.76s] English:** computers can i put on this problem because the computers themselves are getting better  
**Translation:** 

**[2684.08s] English:** on like a moore's law rate but their ability to go from one to ten to a hundred to a thousand  
**Translation:** 

**[2689.28s] English:** yeah you know was something and then multiplied by you know the amount of  
**Translation:** 

**[2693.76s] English:** compute it took to resolve like alex net to resnet to transformers it's it's been quite  
**Translation:** Vocabulary: multiplied: 增加

**[2699.76s] English:** you know steady improvements but those are like s curves aren't they yeah that's the exactly kind of  
**Translation:** 

**[2704.40s] English:** s curves that are underlying moore's law from the very beginning so so what what's the biggest what's  
**Translation:** 

**[2710.08s] English:** the most uh productive uh rich source of s curves in in the future do you think is it  
**Translation:** 

**[2717.12s] English:** hardware is it software or is it so hardware is going to move along relatively slowly like  
**Translation:** 

**[2723.76s] English:** you know double performance every two years there's still i like how you call that slow  
**Translation:** 

**[2729.44s] English:** yeah that's the slow version the snail's pace of moore's law maybe we should we should uh we should  
**Translation:** 

**[2736.16s] English:** trademark that one that's whereas the scaling by number of computers you know can go much faster  
**Translation:** 

**[2743.20s] English:** you know i'm sure at some point google had a you know their initial search engine was running on a  
**Translation:** 

**[2748.16s] English:** laptop you know like yeah and at some point they really worked on scaling that and then they factored  
**Translation:** 

**[2754.08s] English:** the indexer from you know this piece and this piece and this  
**Translation:** Vocabulary: factored: 拆分

**[2757.04s] English:** piece and they spread the data on more and more things and  
**Translation:** 

**[2760.00s] English:** You know, they did a dozen innovations, but as they scaled up the number of computers on that,  
**Translation:** Vocabulary: innovations: 创新

**[2765.34s] English:** they kept finding new bottlenecks in their software and their schedulers and made them rethink.  
**Translation:** 

**[2771.62s] English:** Like, it seems insane to do a scheduler across a thousand computers to schedule parts of it  
**Translation:** Vocabulary: bottlenecks: 瓶颈; scheduler: 调度器; schedulers: 调度器

**[2776.62s] English:** and then send the results to one computer.  
**Translation:** 

**[2778.50s] English:** But if you want to schedule a million searches, that makes perfect sense.  
**Translation:** 

**[2783.40s] English:** So the scaling by just quantity is probably the richest thing.  
**Translation:** 

**[2788.24s] English:** But then as you scale quantity, like a network that was great on 100 computers may be completely the wrong one.  
**Translation:** 

**[2796.46s] English:** You may pick a network that's 10 times slower on 10,000 computers, like per computer.  
**Translation:** 

**[2802.16s] English:** But if you go from 100 to 10,000, that's 100 times.  
**Translation:** 

**[2805.68s] English:** So that's one of the things that happened when we did Internet scaling, is the efficiency went down, not up.  
**Translation:** 

**[2812.46s] English:** The future of computing is inefficiency, not efficiency.  
**Translation:** Vocabulary: computing: 计算; inefficiency: 低效率

**[2815.40s] English:** But scale, inefficient scale.  
**Translation:** 

**[2817.52s] English:** It's scaling.  
**Translation:** Vocabulary: inefficient: 低效的

**[2818.46s] English:** Scaling faster than inefficiency bites you.  
**Translation:** 

**[2821.76s] English:** And as long as there's dollar value there.  
**Translation:** 

**[2823.88s] English:** Like, scaling costs lots of money.  
**Translation:** 

**[2825.64s] English:** But Google showed, Facebook showed, everybody showed that the scale was where the money was at.  
**Translation:** 

**[2831.28s] English:** So it was worth it financially.  
**Translation:** 

**[2833.64s] English:** Do you think, is it possible that, like, basically the entirety of Earth will be like a computing surface?  
**Translation:** Vocabulary: entirety: 全部; financially: 经济上

**[2841.72s] English:** Like, this table will be doing computing.  
**Translation:** 

**[2844.24s] English:** This hedgehog will be doing computing.  
**Translation:** Vocabulary: hedgehog: 刺猬

**[2846.08s] English:** Like, everything really inefficient.  
**Translation:** 

**[2848.24s] English:** I mean, I mean, I think, you know, the science fiction books, they call it computronium.  
**Translation:** Vocabulary: computronium: 计算用的高级材料

**[2852.02s] English:** Computronium?  
**Translation:** 

**[2852.44s] English:** We turn everything into computing.  
**Translation:** 

**[2854.38s] English:** Well, most of the elements aren't very good for anything.  
**Translation:** 

**[2857.72s] English:** Like, you're not going to make a computer out of iron.  
**Translation:** 

**[2859.72s] English:** Like, you know, silicon and carbon have, like, nice structures.  
**Translation:** 

**[2865.02s] English:** You know, we'll see what you can do with the rest of it.  
**Translation:** 

**[2868.28s] English:** People talk about, well, maybe we can turn the sun into a computer.  
**Translation:** 

**[2871.02s] English:** But it's hydrogen.  
**Translation:** 

**[2873.40s] English:** And a little bit of helium.  
**Translation:** 

**[2875.46s] English:** What I mean is more like, actually, just.  
**Translation:** 

**[2878.24s] English:** Adding computers to everything.  
**Translation:** 

**[2879.90s] English:** Oh.  
**Translation:** 

**[2880.00s] English:** okay so you're just converting all the mass of the universe into computer no no so not using  
**Translation:** 

**[2885.60s] English:** to be ironic from the simulation point of view is like the simulator build mass to simulate like  
**Translation:** Vocabulary: converting: 转换; simulate: 模拟; simulation: 仿真; simulator: 模拟器

**[2891.84s] English:** yeah i mean yeah so i mean ultimately this is all heading towards the simulation yeah well  
**Translation:** 

**[2896.56s] English:** i i think i might have told you this story at tesla they were deciding so they want to measure  
**Translation:** 

**[2900.80s] English:** the current coming out of the battery and they decide between putting the resistor in there  
**Translation:** 

**[2904.64s] English:** and putting a computer with a sensor in there and the computer was faster than the computer i worked  
**Translation:** Vocabulary: resistor: 电阻; sensor: 传感器

**[2912.16s] English:** on in 1982 and we chose the computer because it was cheaper than the resistor so so sure this  
**Translation:** 

**[2920.24s] English:** hedgehog you know it costs 13 and we can put a you know an ai that's as smart as you in there  
**Translation:** 

**[2925.28s] English:** for five bucks it'll have one you know so computers will be you know be everywhere  
**Translation:** 

**[2931.60s] English:** i was hoping it wouldn't be smarter than me because  
**Translation:** Vocabulary: bucks: 美元

**[2934.64s] English:** everything's going to be smarter than you but you were saying it's inefficient i thought it  
**Translation:** 

**[2938.32s] English:** was better to have a lot of dumb well well moore's law will slowly compact that stuff so even the  
**Translation:** Vocabulary: inefficient: 低效的

**[2943.12s] English:** dumb things will be smarter than us the dumb things are going to be smart or they're going  
**Translation:** 

**[2946.16s] English:** to be smart enough to talk to something that's really smart you know it's like well just remember  
**Translation:** 

**[2953.52s] English:** like a big computer chip yeah you know it's like an inch by an inch and you know 40 microns thick  
**Translation:** 

**[2960.80s] English:** it doesn't take very much very many atoms to make a high power computer  
**Translation:** 

**[2965.36s] English:** and 10 000 of them can fit in the shoebox but you know you have the the cooling and power problems  
**Translation:** 

**[2971.28s] English:** but you know people are working on that but they still can't write uh compelling poetry or music  
**Translation:** Vocabulary: compelling: 引人入胜的

**[2977.52s] English:** or uh understand what love is or have a fear of mortality so so we're still winning neither can  
**Translation:** 

**[2983.84s] English:** most of humanity so well they can write books about it so uh but but speaking about this uh  
**Translation:** 

**[2994.64s] English:** i think that's a really good point and i think that's a really good point and i think that's  
**Translation:** 

**[3000.00s] English:** You are now the CTO of TenStore, as of two months ago.  
**Translation:** 

**[3008.50s] English:** They build hardware for deep learning.  
**Translation:** 

**[3013.44s] English:** How do you build scalable and efficient deep learning?  
**Translation:** Vocabulary: scalable: 可扩展的

**[3016.14s] English:** This is such a fascinating space.  
**Translation:** 

**[3017.58s] English:** Yeah, yeah.  
**Translation:** 

**[3017.90s] English:** So it's interesting.  
**Translation:** 

**[3018.86s] English:** So up until recently, I thought there was two kinds of computers.  
**Translation:** 

**[3022.38s] English:** There are serial computers that run like C programs, and then there's parallel computers.  
**Translation:** 

**[3026.56s] English:** So the way I think about it is, you know, parallel computers have given parallelism.  
**Translation:** 

**[3032.08s] English:** Like GPUs are great because you have a million pixels.  
**Translation:** 

**[3034.62s] English:** And modern GPUs run a program on every pixel.  
**Translation:** Vocabulary: pixel: 像素; pixels: 像素

**[3037.52s] English:** They call it the shader program, right?  
**Translation:** 

**[3039.38s] English:** So or like finite element analysis.  
**Translation:** Vocabulary: finite: 有限的; shader: 着色器

**[3042.50s] English:** You build something, you know, you make this into little tiny chunks.  
**Translation:** 

**[3045.52s] English:** You give each chunk to a computer.  
**Translation:** 

**[3047.02s] English:** So you're given all these chunks.  
**Translation:** 

**[3048.42s] English:** You have parallelism like that.  
**Translation:** 

**[3050.06s] English:** But most C programs, you write this linear narrative, and you have to make it go fast.  
**Translation:** 

**[3055.20s] English:** To make it go fast.  
**Translation:** 

**[3056.36s] English:** You predict all the branches, all the data fetches, and you run that more in parallel.  
**Translation:** 

**[3060.26s] English:** But that's found parallelism.  
**Translation:** 

**[3063.98s] English:** AI is, I'm still trying to decide how fundamental this is.  
**Translation:** 

**[3068.28s] English:** It's a given parallelism problem.  
**Translation:** 

**[3070.52s] English:** But the way people describe the neural networks, and then how they write them in PyTorch, it makes graphs.  
**Translation:** 

**[3077.96s] English:** Yeah.  
**Translation:** Vocabulary: neural: 神经的

**[3078.30s] English:** That might be fundamentally different than the GPU kind of.  
**Translation:** 

**[3081.70s] English:** Parallelism.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3082.28s] English:** Yeah, it might be.  
**Translation:** 

**[3083.72s] English:** Because when you run the GPU program.  
**Translation:** 

**[3085.94s] English:** On all the pixels, you're running, you know, it depends, you know, this group of pixels, say it's background blue, and it runs a really simple program.  
**Translation:** 

**[3093.98s] English:** This pixel is, you know, some patch of your face.  
**Translation:** 

**[3096.80s] English:** So you have some really interesting shader program to give you the impression of translucency.  
**Translation:** 

**[3101.50s] English:** But the pixels themselves don't talk to each other.  
**Translation:** Vocabulary: translucency: 透明感

**[3103.88s] English:** There's no graph.  
**Translation:** 

**[3105.98s] English:** Right.  
**Translation:** 

**[3106.42s] English:** So you do the image, and then you do the next image, and you do the next image.  
**Translation:** 

**[3111.16s] English:** And you run 8 million pixels, 8 million programs every time.  
**Translation:** 

**[3115.56s] English:** And modern day.  
**Translation:** 

**[3115.92s] English:** GPUs have like 6,000 thread engines in them.  
**Translation:** 

**[3119.84s] English:** So.  
**Translation:** 

**[3120.00s] English:** To get 8 million pixels, each one runs a program on 10 or 20 pixels.  
**Translation:** 

**[3126.18s] English:** And that's how they work.  
**Translation:** 

**[3128.02s] English:** There's no graph.  
**Translation:** 

**[3129.48s] English:** But you think graph might be a totally new way to think about hardware?  
**Translation:** 

**[3134.90s] English:** So Rajat Ghadori and I have been having this conversation about given versus found parallelism.  
**Translation:** 

**[3140.66s] English:** And then the kind of walk is we got more transistors.  
**Translation:** 

**[3143.96s] English:** Like computers way back when did stuff on scalar data.  
**Translation:** Vocabulary: scalar: 标量; transistors: 晶体管

**[3147.24s] English:** Now we did it on vector data, famous vector machines.  
**Translation:** 

**[3150.58s] English:** Now we're making computers that operate on matrices.  
**Translation:** Vocabulary: matrices: 矩阵

**[3154.32s] English:** And then the category we said that was next was spatial.  
**Translation:** 

**[3158.86s] English:** Like imagine you have so much data that you want to do the compute on this data.  
**Translation:** Vocabulary: spatial: 空间数据

**[3163.42s] English:** And then when it's done, it says send the result to this pile of data on some software on that.  
**Translation:** 

**[3168.88s] English:** And it's better to think about it spatially than to move all the data to a central processor and do all the work.  
**Translation:** Vocabulary: processor: 处理单元; spatially: 空间上

**[3177.24s] English:** So spatially, you mean moving in the space of data as opposed to moving the data?  
**Translation:** 

**[3182.46s] English:** Yeah, you have a petabyte data space spread across some huge array of computers.  
**Translation:** Vocabulary: petabyte: 千兆字节

**[3188.68s] English:** And when you do a computation somewhere, you send the result of that computation or maybe a pointer to the next program to some other piece of data and do it.  
**Translation:** 

**[3196.56s] English:** But I think a better word might be graph.  
**Translation:** Vocabulary: computation: 计算

**[3198.80s] English:** And all the AI neural networks are graphs.  
**Translation:** 

**[3201.62s] English:** Do some computation, send the result here.  
**Translation:** Vocabulary: neural: 神经网络

**[3203.98s] English:** Do another computation.  
**Translation:** 

**[3205.18s] English:** Do a data transformation.  
**Translation:** 

**[3206.02s] English:** Do emerging.  
**Translation:** 

**[3207.24s] English:** Do a pooling.  
**Translation:** 

**[3208.16s] English:** Do another computation.  
**Translation:** 

**[3210.38s] English:** Is it possible to compress and say how we make this thing efficient, this whole process efficient, this different?  
**Translation:** Vocabulary: compress: 压缩

**[3217.10s] English:** So first, the fundamental elements in the graphs are things like metrics, multiplies, convolutions, data manipulations, and data movements.  
**Translation:** 

**[3225.66s] English:** Yeah.  
**Translation:** Vocabulary: convolutions: 卷积; manipulations: 操作; multiplies: 乘法

**[3226.08s] English:** So GPUs emulate those things with their little singles, you know, basically running a single-threaded program.  
**Translation:** 

**[3232.44s] English:** Yeah.  
**Translation:** Vocabulary: emulate: 模拟

**[3232.78s] English:** And then there's, you know, NVIDIA calls it a warp where they group a bunch of programs that are similar.  
**Translation:** 

**[3237.24s] English:** So for efficiency and instruction.  
**Translation:** 

**[3240.00s] English:** use and then at a higher level you kind of you take this graph and you say this part of the  
**Translation:** 

**[3245.72s] English:** graph is a matrix multiplier which runs on these 32 threads but the model at the bottom was built  
**Translation:** Vocabulary: matrix: 矩阵; multiplier: 乘法器

**[3252.54s] English:** for running programs on pixels not executing graphs so it's emulation ultimately yes so is  
**Translation:** 

**[3259.68s] English:** it possible to build something that natively runs graphs yes so that's what ten store did  
**Translation:** Vocabulary: emulation: 模拟; executing: 执行; natively: 原生; pixels: 像素

**[3264.68s] English:** so where are we on that how like in the history of that effort are we in the early days yeah I  
**Translation:** 

**[3272.44s] English:** think so ten store & started by a friend of mine acute Bonni and I I was his first investor so  
**Translation:** Vocabulary: investor: 投资者

**[3279.14s] English:** I've been you know kind of following him and talking to him about it for years and in the  
**Translation:** 

**[3284.92s] English:** fall when I was considering things to do I decided you know the we we held a conference last year  
**Translation:** 

**[3291.56s] English:** with a friend organized it and and we  
**Translation:** 

**[3294.68s] English:** wanted to bring in thinkers and two of the people were andre carpacci and chris latner and andre  
**Translation:** Vocabulary: thinkers: 思想家

**[3301.84s] English:** gave this talk it's on youtube called software 2.0 which i think is great which is we went from  
**Translation:** 

**[3308.68s] English:** programmed computers where you write programs to data program computers you know like the future  
**Translation:** 

**[3314.80s] English:** is you know of software is data programs the networks and i think that's true and then  
**Translation:** 

**[3321.82s] English:** chris has been work he worked on lovm the low level virtual machine which became the  
**Translation:** 

**[3327.56s] English:** intermediate representation for all compilers and now he's working on another project called  
**Translation:** 

**[3332.96s] English:** mlir which is mid-level intermediate representation which is essentially under the graph about how do  
**Translation:** Vocabulary: compilers: 编译器

**[3340.70s] English:** you represent that kind of computation and then coordinate large numbers of potentially  
**Translation:** 

**[3345.14s] English:** heterogeneous computers and i would say technically tens torrents you know  
**Translation:** Vocabulary: computation: 计算; coordinate: 协调; heterogeneous: 异构; torrents: 文件流

**[3351.74s] English:** you know  
**Translation:** 

**[3351.82s] English:** two pillars of those those those two ideas software 2.0 and mid-level representation  
**Translation:** 

**[3357.36s] English:** but it's in service of executing  
**Translation:** 

**[3360.00s] English:** graph programs the hardware is designed to do that so it's including the hardware piece yeah  
**Translation:** 

**[3365.66s] English:** and then the other cool thing is for a relatively small amount of money they did a test chip and two  
**Translation:** 

**[3371.54s] English:** production chips so it's like a super effective team and and unlike some ai startups where if you  
**Translation:** Vocabulary: startups: 创业公司

**[3378.96s] English:** don't build the hardware to run the software that they really want to do then you have to fix it by  
**Translation:** 

**[3383.90s] English:** writing lots more software so the hardware naturally does matrix multiply convolution  
**Translation:** Vocabulary: convolution: 卷积; matrix: 矩阵; multiply: 乘法

**[3389.68s] English:** the data manipulations and the data movement between processing elements that that you can  
**Translation:** 

**[3396.36s] English:** see in the graph which i think is all pretty clever and that's that's what i'm working on now  
**Translation:** Vocabulary: manipulations: 数据操作

**[3404.66s] English:** so uh the i think it's called the grace call processor introduced last year it's uh you know  
**Translation:** 

**[3412.34s] English:** there's a bunch of measures of performance  
**Translation:** Vocabulary: processor: 处理器

**[3413.68s] English:** we're talking about horses it seems to outperform 368 trillion operations per second seems to  
**Translation:** 

**[3420.20s] English:** outperform nvidia's tesla t4 system so these are just numbers what do they actually mean in real  
**Translation:** 

**[3426.90s] English:** world performance like what are the metrics for you that you're chasing in in your horse race like  
**Translation:** 

**[3432.46s] English:** what do you care about well first so the the native language of you know people who write  
**Translation:** 

**[3438.64s] English:** ai network programs is pytorch now pytorch tensorflow there's a couple others  
**Translation:** 

**[3443.30s] English:** you  
**Translation:** 

**[3443.68s] English:** the pytorch has one over tensorflow which is just i'm not an expert on that  
**Translation:** 

**[3447.32s] English:** i know many people who have switched from tensorflow to pytorch yeah and there's technical  
**Translation:** 

**[3452.36s] English:** reasons for it and i use both both are still awesome both are still awesome but the deepest  
**Translation:** 

**[3457.96s] English:** love is for pytorch currently yeah there's more love for that and that that may change  
**Translation:** 

**[3462.34s] English:** so the first thing is when they write their programs can the hardware execute it pretty  
**Translation:** 

**[3468.08s] English:** much as it was written right so pytorch turns into a graph we have a graph that's a graph that's a  
**Translation:** 

**[3473.68s] English:** graph compiler that makes that graph then it fractions the graph down so if you have big  
**Translation:** 

**[3477.86s] English:** matrix multiply we turn it in the right size chunk  
**Translation:** Vocabulary: fractions: 分割

**[3480.00s] English:** to run on the processing elements it hooks all the graph up it lays out all the data  
**Translation:** 

**[3484.96s] English:** there's a couple of mid-level representations of it that are also simulatable so that if you're  
**Translation:** Vocabulary: simulatable: 可模拟的

**[3491.20s] English:** writing the code you can see how it's going to go through the machine which is pretty cool and  
**Translation:** 

**[3495.84s] English:** then at the bottom it schedules kernels like mass data manipulation data movement kernels  
**Translation:** Vocabulary: kernels: 内核; manipulation: 操作

**[3501.60s] English:** which do this stuff so we don't have to run write a little program to do matrix multiply because we  
**Translation:** 

**[3507.36s] English:** have a big matrix multiplier like there's no simd program for that but that there is scheduling for  
**Translation:** Vocabulary: matrix: 矩阵; multiplier: 乘法器; multiply: 相乘

**[3513.60s] English:** that right so the one of the goals is if you write a piece of pytorch code that looks pretty  
**Translation:** 

**[3520.56s] English:** reasonable you should be able to compile it run it on the hardware without having to tweak it and  
**Translation:** Vocabulary: tweak: 调整

**[3525.28s] English:** and do all kinds of crazy things to get performance there's not a lot of intermediate steps  
**Translation:** 

**[3529.92s] English:** it's running directly as like on a gpu if you write a large matrix multiply naively you'll  
**Translation:** Vocabulary: naively: 生硬地

**[3534.64s] English:** get five to ten percent of the peak performance of the gpu  
**Translation:** 

**[3537.36s] English:** hmm right and then there's a bunch there's a bunch of people published papers on this and i  
**Translation:** 

**[3541.60s] English:** read them about what steps do you have to do and it goes from pretty reasonable well transpose one  
**Translation:** 

**[3547.52s] English:** of the matrices so you do row order not column ordered you know block it so that you can put a  
**Translation:** Vocabulary: matrices: 矩阵; transpose: 转置

**[3553.52s] English:** block of the matrix on different sms you know groups of threads but some of it gets into little  
**Translation:** 

**[3560.56s] English:** details like you have to schedule it just so so you don't have register conflicts so the the the  
**Translation:** 

**[3566.48s] English:** they call them kudos  
**Translation:** 

**[3567.36s] English:** ninjas i love it to get to the optimal point you either write a pre use a pre written library which  
**Translation:** Vocabulary: kudos: 赞美; ninjas: 高手; optimal: 最佳

**[3576.16s] English:** is a good strategy for some things or you have to be an expert in micro architecture to program it  
**Translation:** 

**[3582.08s] English:** right so the optimization step is way more complicated with the gps so our our goal is  
**Translation:** Vocabulary: optimization: 优化步骤

**[3586.64s] English:** if you write pytorch that's good pytorch you can do it now there's as the networks are evolving  
**Translation:** 

**[3592.72s] English:** you know they've changed from convolutional to matrix multiply people are talking about  
**Translation:** Vocabulary: convolutional: 卷积的; evolving: 演变

**[3597.36s] English:** additional graphs you're talking about very large matrices you're talking about  
**Translation:** 

**[3600.00s] English:** about sparsity we're talking about problems that scale across many many chips so the the native  
**Translation:** Vocabulary: sparsity: 稀疏性

**[3608.80s] English:** you know data item is as a packet like so you send the packet to a processor it gets processed  
**Translation:** 

**[3614.40s] English:** it does a bunch of work and then it may send packets to other processors and and they execute  
**Translation:** Vocabulary: processed: 处理; processor: 处理器; processors: 处理器

**[3619.12s] English:** in like a data flow graph kind of methodology got it we have a big network on chip and then  
**Translation:** 

**[3624.88s] English:** 16 the next second chip has 16 ethernet ports to hook lots of them together and it's the same graph  
**Translation:** Vocabulary: ethernet: 以太网; methodology: 方法论

**[3630.32s] English:** compiler across multiple chips so that's where the scale comes in so it's built to scale naturally  
**Translation:** 

**[3635.04s] English:** now my experience with scaling is as you scale you run into lots of interesting problems  
**Translation:** 

**[3640.64s] English:** so scaling is a mountain to climb yeah so the hardware is built to do this and then  
**Translation:** 

**[3645.84s] English:** we're in the process of is there a software part to this with ethernet and all that well the  
**Translation:** 

**[3652.88s] English:** you know the protocol at the bottom you know we  
**Translation:** 

**[3654.88s] English:** send you know it's an ethernet phi but the protocol basically says send the packet from  
**Translation:** 

**[3660.56s] English:** here to there it's all point to point the header bit says which processor to send it to and we  
**Translation:** 

**[3666.00s] English:** basically take a packet off our on-chip network put an ethernet header on it send it to the other  
**Translation:** 

**[3672.00s] English:** end to strip the header off and send it to the local thing it's pretty straightforward  
**Translation:** 

**[3676.00s] English:** human human interaction is pretty straightforward too but when you get a million of us we could  
**Translation:** Vocabulary: straightforward: 简单明了

**[3679.60s] English:** we do some crazy stuff together yeah it could be fun so is that the goal is  
**Translation:** 

**[3684.88s] English:** scale so like for example i've been recently doing a bunch of robots at home for my own  
**Translation:** 

**[3690.40s] English:** personal pleasure uh am i going to ever use test store or is this more for there's all kinds of  
**Translation:** 

**[3696.56s] English:** problems like there's small inference problems or small training problems or big training problems  
**Translation:** Vocabulary: inference: 推断

**[3701.28s] English:** what's the big goal is it the big infant uh training problems or the small training problems  
**Translation:** 

**[3706.64s] English:** one of the goals is the scale from 100 milliwatts to a you know to a megawatt you know so like  
**Translation:** Vocabulary: megawatt: 兆瓦; milliwatts: 毫瓦

**[3712.64s] English:** really have some range on the problems. The same kind of AI programs work at all different levels.  
**Translation:** 

**[3720.00s] English:** the natural since the natural data item is a packet that we can move around it's built to scale  
**Translation:** 

**[3726.30s] English:** but so many people have you know small problems right right but but uh you know like inside that  
**Translation:** 

**[3734.20s] English:** phone is a small problem to solve so do you see testosterone potentially being inside a phone  
**Translation:** 

**[3739.60s] English:** well the power efficiency of local memory local computation and the way we built it is pretty good  
**Translation:** 

**[3745.68s] English:** and then there's a lot of efficiency on being able to do conditional graphs and sparsity  
**Translation:** Vocabulary: computation: 计算; conditional: 条件性的; sparsity: 稀疏性

**[3750.72s] English:** i think it's it's for complicated networks i want to go in a small factor it's going to be quite  
**Translation:** 

**[3756.30s] English:** good um but we have to prove that that's a that's a fun problem and that's the early days of the  
**Translation:** 

**[3761.74s] English:** company right it's a couple years you said but you think you invested you think they're legit  
**Translation:** 

**[3767.06s] English:** yeah as you join well that's well it's also it's a really interesting place to be  
**Translation:** Vocabulary: legit: 正规

**[3772.44s] English:** like the ai world is exploding you know  
**Translation:** 

**[3775.68s] English:** and i looked at some other opportunities like build a faster processor which people want  
**Translation:** Vocabulary: exploding: 蓬勃发展; processor: 处理器

**[3780.82s] English:** yes but that's more on an incremental path than what's going to happen in ai in the next 10 years  
**Translation:** 

**[3786.90s] English:** so this is kind of you know an exciting place to be part of the revolutions will be happening in  
**Translation:** Vocabulary: incremental: 逐步的; revolutions: 革命性变化

**[3794.12s] English:** the very space and then lots of people are working on it but there's lots of technical reasons why  
**Translation:** 

**[3798.26s] English:** some of them you know aren't going to work out that well and and you know that's that's interesting  
**Translation:** 

**[3803.40s] English:** and there's also the same  
**Translation:** 

**[3804.74s] English:** problem  
**Translation:** 

**[3805.68s] English:** about getting the basics right like we've talked to customers about exciting features  
**Translation:** 

**[3809.62s] English:** and at some point we realized that each and i was realizing they want to hear first about memory  
**Translation:** 

**[3815.24s] English:** bandwidth local bandwidth compute intensity programmability they want to know the basics  
**Translation:** 

**[3820.14s] English:** power management how the network ports work what are the basics do all the basics work  
**Translation:** Vocabulary: bandwidth: 带宽

**[3825.36s] English:** because it's easy to say we've got this great idea you know the crack gpt3  
**Translation:** 

**[3829.54s] English:** but the people we talk to want to say if i buy the  
**Translation:** 

**[3835.68s] English:** pc express card with our chip on it if you buy the card you plug it  
**Translation:** 

**[3840.00s] English:** in your machine to download the drive or how long does it take me to get my network to run  
**Translation:** 

**[3843.84s] English:** right right you know that's a real question it's a very basic question so yeah is there an answer  
**Translation:** 

**[3849.92s] English:** to that yet or is it trying to our goal is like an hour okay when can i buy a test for it uh pretty  
**Translation:** 

**[3856.92s] English:** soon for my for the small case training yeah pretty soon months good i love the idea of you  
**Translation:** 

**[3863.82s] English:** inside the room with uh karpathy andre karpathy and chris ladner uh very um very interesting very  
**Translation:** Vocabulary: karpathy: 卡帕西; ladner: 拉德纳

**[3874.84s] English:** brilliant people very out of the box thinkers but also like first principles thinkers well they both  
**Translation:** 

**[3880.56s] English:** get stuff done they only get stuff done to get their own projects done they they talk about it  
**Translation:** Vocabulary: thinkers: 思考者

**[3886.42s] English:** clearly they educate large numbers of people and they've created platforms for other people to go  
**Translation:** 

**[3890.74s] English:** do their stuff on yeah the the clear thinking  
**Translation:** 

**[3893.82s] English:** that's able to be communicated is kind of impressive it's kind of remarkable to  
**Translation:** 

**[3898.32s] English:** yeah i'm a fan well let me ask because uh i talked to chris actually a lot  
**Translation:** 

**[3904.28s] English:** these days he's been uh one of the just to give him a shout out and he's been so  
**Translation:** 

**[3910.04s] English:** supportive as a human being so everybody's quite different like great engineers are different but  
**Translation:** 

**[3917.78s] English:** he's been like sensitive to the human element in a way that's been fascinating like he was one of  
**Translation:** 

**[3923.00s] English:** the early people  
**Translation:** 

**[3923.66s] English:** you  
**Translation:** 

**[3923.80s] English:** you  
**Translation:** 

**[3923.82s] English:** on this stupid podcast that i do to say like don't quit this thing and also talk to whoever  
**Translation:** 

**[3931.98s] English:** the hell you want to talk to that kind of from a legit engineer to get like props and be like you  
**Translation:** Vocabulary: legit: 正经; props: 赞美

**[3938.78s] English:** can do this that was i mean that's what a good leader does right to just kind of let a little  
**Translation:** 

**[3944.00s] English:** kid do his thing like go go do it let's see let's see see what turns out that that's a that's a  
**Translation:** 

**[3953.80s] English:** sense about he used to be he now i think stepped away from google right he said sci-fi  
**Translation:** 

**[3960.00s] English:** i think uh what what's really impressive to you about the things that chris has worked on because  
**Translation:** 

**[3965.84s] English:** it's that we mentioned the optimization the compiler design stuff the llvm uh then there's  
**Translation:** 

**[3972.52s] English:** he's also at google worked at the tpu stuff he's obviously worked on swift so the programming  
**Translation:** Vocabulary: optimization: 优化

**[3980.02s] English:** language side talking about people that work in the entirety of the stack yeah yeah uh what uh  
**Translation:** 

**[3986.02s] English:** from your time interacting with chris and knowing the guy what's really impressive to you  
**Translation:** Vocabulary: entirety: 全部

**[3990.44s] English:** it just inspires you well well like llvm became you know the platform the de facto platform for  
**Translation:** 

**[4000.16s] English:** you know compilers like it's it's amazing and you know it was good code quality good design  
**Translation:** Vocabulary: compilers: 编译器; facto: 事实上的; inspires: 启发

**[4005.74s] English:** choices he hit the right level of abstraction there's a little bit of the right time the right  
**Translation:** 

**[4010.74s] English:** place and then he built a new programming language called swift which you know  
**Translation:** 

**[4016.02s] English:** after you know let's say some adoption resistance became very successful i don't know that much  
**Translation:** 

**[4021.86s] English:** about his work at google although i know that you know that was a typical they started tensorflow  
**Translation:** 

**[4028.66s] English:** stuff and they you know it was new is you know they they wrote a lot of code and then at some  
**Translation:** 

**[4033.22s] English:** point it needed to be refactored to be you know because it its development slowed down white  
**Translation:** Vocabulary: refactored: 重新整理

**[4039.46s] English:** pie torch started a little later and then passed it so he did a lot of work on that and then his  
**Translation:** 

**[4044.50s] English:** idea about mlir was you know it was a lot of work on that and then his idea about mlir was you know  
**Translation:** 

**[4046.00s] English:** which is what people started to realize is the complexity of the software stack above the low  
**Translation:** 

**[4050.90s] English:** level ir was getting so high that forcing the features of that into the level was was putting  
**Translation:** Vocabulary: complexity: 复杂性

**[4057.02s] English:** too much of a burden on it so he's splitting that into multiple pieces and that was one of the  
**Translation:** 

**[4062.22s] English:** inspirations for our software stack where we have several intermediate representations that are all  
**Translation:** 

**[4067.32s] English:** executable and you can look at them and do transformations on them before you lower the  
**Translation:** 

**[4072.56s] English:** level so that was i think we started  
**Translation:** Vocabulary: executable: 可执行文件; transformations: 转换

**[4076.00s] English:** before mlir really got you know far enough along  
**Translation:** 

**[4080.00s] English:** to use uh but we're interested in that he's really excited about that malaria he's that's that's his  
**Translation:** 

**[4085.76s] English:** like little baby so he yeah and there seems to be some profound ideas on that that are really useful  
**Translation:** 

**[4091.68s] English:** so so each one of those things has been as the world of software gets more and more complicated  
**Translation:** Vocabulary: profound: 深奥的

**[4097.68s] English:** how do we create the right abstraction levels to simplify it in a way that people can now work  
**Translation:** 

**[4102.56s] English:** independently on different levels of it so i would say all all three of those projects lovm swift and  
**Translation:** Vocabulary: abstraction: 抽象; independently: 独立地; simplify: 简化

**[4109.44s] English:** mlir did that successfully so i'm interested was what he's going to do next in the same kind of way  
**Translation:** 

**[4114.64s] English:** yes so on the either the tpu or maybe the nvidia gpu side how does 10 story you think  
**Translation:** 

**[4123.60s] English:** or the ideas underlying it doesn't have to be test or just this kind of graph focused  
**Translation:** 

**[4130.40s] English:** uh graph centric hardware deep learning centric hardware beat nvidia's  
**Translation:** 

**[4139.12s] English:** do you think  
**Translation:** 

**[4139.44s] English:** is possible for it to basically overtake nvidia sure what's what's that process look like what's  
**Translation:** Vocabulary: overtake: 超越

**[4145.68s] English:** that uh journey look like you think well gpus were built to run shader programs on millions of pixels  
**Translation:** 

**[4152.24s] English:** not to run graphs yes so there's a hypothesis that says the way the graphs you know are built  
**Translation:** Vocabulary: hypothesis: 假设; pixels: 像素; shader: 着色器

**[4160.16s] English:** is going to be really interesting to be inefficient on computing this  
**Translation:** 

**[4164.00s] English:** and then the the primitives is not a simdy program it's matrix multiply convolution  
**Translation:** Vocabulary: computing: 计算; convolution: 卷积; inefficient: 低效; matrix: 矩阵; multiply: 乘法; primitives: 基本函数

**[4169.92s] English:** and then the data manipulations are fairly extensive about like how do you do a fast  
**Translation:** 

**[4174.56s] English:** transpose with a program i don't know if you've ever written a transpose program  
**Translation:** Vocabulary: manipulations: 数据操作; transpose: 转置矩阵

**[4178.64s] English:** they're ugly and slow but in hardware you can do really well i gotta give you an example so when  
**Translation:** 

**[4184.72s] English:** gpu accelerators first started doing triangles like so you have a triangle which maps on the  
**Translation:** Vocabulary: accelerators: 加速器; triangle: 三角形; triangles: 三角形

**[4189.60s] English:** set of pixels so you build it's very easy straightforward to build a hardware engine  
**Translation:** 

**[4194.08s] English:** that'll find all those pixels and it's kind of weird because you walk along the triangle to get  
**Translation:** 

**[4198.00s] English:** at the edge, and then you have to go back.  
**Translation:** 

**[4200.00s] English:** down to the next row and walk along and then you have to decide on the edge if the line of the  
**Translation:** 

**[4204.92s] English:** triangle is like half on the pixel what's the pixel color because it's half of this pixel and  
**Translation:** 

**[4210.36s] English:** half the next one that's called rasterization and you're saying that could be done in uh in  
**Translation:** Vocabulary: pixel: 像素; rasterization: 栅格化

**[4215.50s] English:** hard no that's an example of that operation as a software program is really bad i've written a  
**Translation:** 

**[4222.56s] English:** program that did rasterization the hardware that does it is actually less code than the software  
**Translation:** 

**[4227.92s] English:** program that does it and it's way faster right so there are certain times when the abstraction  
**Translation:** 

**[4234.98s] English:** you have rasterize a triangle you know execute a graph you know components of a graph but the  
**Translation:** Vocabulary: abstraction: 抽象; rasterize: 栅格化

**[4241.58s] English:** right thing to do in the hardware software boundary is for the hardware to naturally do it  
**Translation:** 

**[4245.58s] English:** and so the gpu is really optimized for the rasterization of triangles well no that's just  
**Translation:** 

**[4251.00s] English:** well like in a modern you know that's a small piece of modern gpus what they did is  
**Translation:** 

**[4257.92s] English:** that they still rasterize triangles when you're running a game but for the most part  
**Translation:** 

**[4261.98s] English:** most of the computation in the area the gpu is running shader programs but they're single  
**Translation:** 

**[4266.54s] English:** threaded programs on pixels not graphs let's be honest let's say i don't actually know the the  
**Translation:** Vocabulary: computation: 计算; threaded: 线程

**[4272.34s] English:** math behind shader uh shading and lighting and all that kind of stuff i don't know what  
**Translation:** 

**[4276.86s] English:** they look like little simple floating point programs or complicated ones you can have  
**Translation:** Vocabulary: shader: 着色器程序

**[4281.64s] English:** instructions in a shader program but i don't have a good intuition why it could be parallelized so  
**Translation:** 

**[4287.16s] English:** easily  
**Translation:** Vocabulary: intuition: 直觉

**[4287.92s] English:** no it's because you have eight million pixels in every single so when you have a light right  
**Translation:** 

**[4292.12s] English:** yeah that comes down the angle you know the amount of light like like say this is a line  
**Translation:** Vocabulary: pixels: 像素

**[4298.24s] English:** of pixels across this table right the amount of light on each pixel is subtly different  
**Translation:** 

**[4303.30s] English:** and each pixel is responsible for figuring out figuring it out so that pixel says i'm this pixel  
**Translation:** Vocabulary: subtly: 微妙地

**[4308.40s] English:** i know the angle of the light i know the occlusion i know the color i am like every  
**Translation:** 

**[4312.74s] English:** single pixel here is a different color every single pixel gets a different amount of light  
**Translation:** Vocabulary: occlusion: 遮挡

**[4316.26s] English:** every single pixel  
**Translation:** 

**[4317.92s] English:** So it has a subtly different translucency.  
**Translation:** Vocabulary: translucency: 透明感

**[4320.00s] English:** so to make it look realistic the solution was you run a separate program on every pixel see but i  
**Translation:** 

**[4325.50s] English:** thought there's like reflection from all over the place is every pixel yeah but there is so so you  
**Translation:** 

**[4329.84s] English:** build a reflection map which also has some pixelated thing and then when the pixel is looking  
**Translation:** 

**[4335.32s] English:** at the reflection map has to calculate what the normal of the surface is and it does it per pixel  
**Translation:** Vocabulary: pixel: 像素; pixelated: 像素化

**[4340.32s] English:** by the way there's boatloads of hacks on that you know like you may have a lower resolution  
**Translation:** 

**[4344.24s] English:** light map reflection map there's all these you know tax they do but at the end of the day it's  
**Translation:** Vocabulary: boatloads: 很多; hacks: 技巧

**[4350.32s] English:** per pixel computation and it's so happening you can map uh graph like computation onto the this  
**Translation:** 

**[4358.38s] English:** pixel central you can do floating point programs on convolutions and matrices and and nvidia  
**Translation:** Vocabulary: convolutions: 卷积; matrices: 矩阵

**[4364.12s] English:** invested for years in cuda first for hpc and then they got lucky with the ai trend but do you think  
**Translation:** 

**[4370.56s] English:** they're going to essentially not be able to hardcore pivot  
**Translation:** Vocabulary: hardcore: 坚定转向

**[4374.22s] English:** out of their we'll see that's always interesting how often do big companies hardcore pivot occasionally  
**Translation:** 

**[4381.60s] English:** how much do you know about nvidia folks some some yeah well it's um i'm curious as well who's  
**Translation:** 

**[4390.26s] English:** ultimately as a well they've they've innovated several times but they've also worked really  
**Translation:** 

**[4394.40s] English:** hard on mobile they worked really hard on radios you know you know they're fundamentally a gpu  
**Translation:** Vocabulary: fundamentally: 本质上; innovated: 创新

**[4399.40s] English:** company well they tried to pivot there's an interesting little uh  
**Translation:** 

**[4404.22s] English:** game and play in autonomous vehicles right with or a semi-autonomous like playing with tesla and so  
**Translation:** Vocabulary: autonomous: 自主

**[4410.86s] English:** on and seeing that's a dipping a toe into that kind of pivot they came out with this platform  
**Translation:** 

**[4416.88s] English:** which is interesting technically yeah but it was like a three thousand watt you know you know  
**Translation:** 

**[4422.40s] English:** thousand watt three three thousand dollar you know gpu platform i don't know if it's interesting  
**Translation:** 

**[4426.96s] English:** technically it's interesting philosophically i i technically i don't know if it's the execution  
**Translation:** Vocabulary: philosophically: 哲学上

**[4431.72s] English:** the craftsmanship is there i'm not sure  
**Translation:** 

**[4434.22s] English:** but i didn't get a sense they were repurposing gpus for an automotive solution right it's not a  
**Translation:** Vocabulary: automotive: 汽车相关; craftsmanship: 技艺; repurposing: 重新利用

**[4439.66s] English:** real  
**Translation:** 

**[4440.00s] English:** they didn't they didn't build a ground-up solution right like the like the chips inside tesla are  
**Translation:** 

**[4445.80s] English:** pretty cheap like mobileye has been doing this they're they're doing the classic work from the  
**Translation:** 

**[4449.80s] English:** simplest thing yeah you know they were building 40 square millimeter chips and nvidia their  
**Translation:** Vocabulary: millimeter: 毫米; mobileye: 摩比视

**[4455.06s] English:** solution had two 800 millimeter chips and two 200 millimeter chips and you know like boatloads  
**Translation:** 

**[4461.18s] English:** are really expensive drams and and you know it's a really different approach the mobile i fit the  
**Translation:** Vocabulary: drams: 药片

**[4468.28s] English:** let's say automotive cost and form factor and then they added features as it was economically  
**Translation:** 

**[4473.32s] English:** viable and nvidia said take the biggest thing and we're going to go make it work you know and and  
**Translation:** Vocabulary: economically: 经济上

**[4479.56s] English:** that's also influenced like waymo there's a whole bunch of autonomous startups where they have a  
**Translation:** 

**[4484.08s] English:** 5 000 watt server in their trunk right and but that's that's because they think well 5 000 watts  
**Translation:** Vocabulary: startups: 创业公司; watts: 瓦特

**[4490.44s] English:** and you know ten thousand dollars is okay because it's replacing a driver elon's approach was that  
**Translation:** 

**[4495.88s] English:** port has to be cheap enough  
**Translation:** 

**[4498.28s] English:** and mobileye was like we need to fit in the bomb and you know cost structure that  
**Translation:** 

**[4507.86s] English:** car companies do so they may sell you a gps for 1500 bucks but the bomb for that's like 25 dollars  
**Translation:** 

**[4514.90s] English:** well and uh for mobileye it seems like neural networks were not first-class citizens like the  
**Translation:** 

**[4522.32s] English:** computation they didn't start out as a yeah it was a cv problem you know yeah and did classic cv  
**Translation:** Vocabulary: computation: 计算; neural: 神经

**[4528.28s] English:** and found stop lights and lines and they were really good at it yeah and they never i mean i  
**Translation:** 

**[4533.00s] English:** don't know what's happening now but they never fully pivoted i mean it's like it's the nvidia  
**Translation:** Vocabulary: pivoted: 转向

**[4537.08s] English:** thing then as opposed to so if you look at the new tesla work it's like neural networks from the  
**Translation:** 

**[4543.56s] English:** ground up yeah right yeah and even tesla started with a lot of cv stuff in it and andre's basically  
**Translation:** 

**[4548.92s] English:** been eliminating it you know move it move everything into the network so uh without  
**Translation:** 

**[4556.20s] English:** this isn't like confidential stuff but you  
**Translation:** Vocabulary: confidential: 机密的

**[4558.28s] English:** sitting on a porch  
**Translation:** 

**[4560.00s] English:** looking over the world, looking at the work that Andre is doing,  
**Translation:** Vocabulary: andre: 安德烈

**[4563.72s] English:** that Elon is doing with Tesla Autopilot.  
**Translation:** 

**[4566.12s] English:** Do you like the trajectory of where things are going on the hardware side?  
**Translation:** Vocabulary: trajectory: 发展趋势

**[4568.98s] English:** Well, they're making serious progress.  
**Translation:** 

**[4570.88s] English:** I like the videos of people driving the beta stuff.  
**Translation:** 

**[4574.12s] English:** Like, it's taken some pretty complicated intersections and all that,  
**Translation:** 

**[4577.00s] English:** but it's still an intervention per drive.  
**Translation:** Vocabulary: intersections: 交叉口

**[4580.76s] English:** I mean, I have the current Autopilot, my Tesla.  
**Translation:** 

**[4583.60s] English:** I use it every day.  
**Translation:** 

**[4584.38s] English:** Do you have full self-driving beta or no?  
**Translation:** 

**[4586.36s] English:** No.  
**Translation:** 

**[4586.78s] English:** So you like where this is going?  
**Translation:** 

**[4588.66s] English:** They're making progress.  
**Translation:** 

**[4589.36s] English:** It's taken longer than anybody thought.  
**Translation:** 

**[4592.28s] English:** You know, my wonder was, is hardware 3, is it enough computing?  
**Translation:** Vocabulary: computing: 计算能力

**[4598.98s] English:** Off by 2, off by 5, off by 10, off by 100.  
**Translation:** 

**[4602.36s] English:** Yeah.  
**Translation:** 

**[4603.00s] English:** And I thought it probably wasn't enough, but they're doing pretty well with it now.  
**Translation:** 

**[4609.74s] English:** Yeah.  
**Translation:** 

**[4609.98s] English:** And one thing is the data set gets bigger, the training gets better,  
**Translation:** 

**[4614.94s] English:** and then there's this interesting thing is you sort of train  
**Translation:** 

**[4618.26s] English:** and build an arbitrary cycle.  
**Translation:** 

**[4619.36s] English:** So I use a network that solves the problem,  
**Translation:** 

**[4621.26s] English:** and then you refactor the network down to the thing that you can afford to ship.  
**Translation:** 

**[4626.12s] English:** Right.  
**Translation:** Vocabulary: refactor: 重构

**[4626.66s] English:** So the goal isn't to build a network that fits in the phone.  
**Translation:** 

**[4630.52s] English:** It's to build something that actually works.  
**Translation:** 

**[4634.88s] English:** And then how do you make that most effective on the hardware you have?  
**Translation:** 

**[4639.74s] English:** And they seem to be doing that much better than a couple of years ago.  
**Translation:** 

**[4643.70s] English:** Well, the one really important thing is also what they're doing well is how to iterate that quickly,  
**Translation:** 

**[4648.76s] English:** which means.  
**Translation:** 

**[4649.56s] English:** It's not just about one-time deployment, one building.  
**Translation:** 

**[4652.30s] English:** It's constantly iterating the network and trying to automate as many steps as possible, right?  
**Translation:** Vocabulary: automate: 自动化; deployment: 部署

**[4656.68s] English:** Yeah.  
**Translation:** 

**[4657.46s] English:** And that's actually the principles of the software 2.0, like you mentioned with Andre.  
**Translation:** 

**[4665.20s] English:** It's not just, I mean, I don't know what the actual, his description of software 2.0 is.  
**Translation:** 

**[4670.78s] English:** If it's just high-level philosophical or there's specifics.  
**Translation:** Vocabulary: philosophical: 哲学性的

**[4673.26s] English:** But the interesting thing about what that actually looks in the real world is,  
**Translation:** 

**[4678.50s] English:** it's that.  
**Translation:** 

**[4680.00s] English:** uh what i think andre calls the data engine it's like it's the iterative improvement of the thing  
**Translation:** 

**[4686.28s] English:** you have a neural network that uh does stuff fails on a bunch of things and learns from it  
**Translation:** Vocabulary: iterative: 迭代; neural: 神经

**[4692.72s] English:** over and over and over so you're constantly discovering edge cases so it's very much about  
**Translation:** 

**[4697.14s] English:** uh like data engineering like figuring out it's kind of what you were talking about with  
**Translation:** 

**[4703.16s] English:** test point is you have the data landscape you have to walk along that data landscape in a way that  
**Translation:** 

**[4708.22s] English:** uh that's constantly improving the the the neural network and that that feels like that's  
**Translation:** 

**[4713.88s] English:** the central piece of yeah so and there's two pieces of it like you you find edge cases that  
**Translation:** 

**[4720.42s] English:** don't work and then you define something that goes get you data for that but then the other  
**Translation:** 

**[4724.90s] English:** constraint is whether you have to label it or not like the the amazing thing about like the gpt3  
**Translation:** 

**[4729.40s] English:** stuff is it's unsupervised so there's essentially infinite amount of data now there's obviously  
**Translation:** Vocabulary: unsupervised: 无需监督

**[4734.14s] English:** infinite amount of data available from cars of people who successfully drive  
**Translation:** 

**[4738.22s] English:** but you know the the current pipelines are mostly running on labeled data which is human limited  
**Translation:** Vocabulary: pipelines: 数据处理流程

**[4743.98s] English:** so when that becomes on unsupervised right it'll create unlimited amount of data which then they'll  
**Translation:** 

**[4753.16s] English:** scale now the networks that may use that data might be way too big for cars but then there'll  
**Translation:** 

**[4758.68s] English:** be the transformation from now we have unlimited data i know exactly what i want now can i turn  
**Translation:** 

**[4762.98s] English:** that into something that fits in the car and that that process is going to happen all over the  
**Translation:** 

**[4768.22s] English:** place every time you get to the place where you have unlimited data and that's what software 2.0  
**Translation:** 

**[4773.40s] English:** is about unlimited data training networks to do stuff without humans writing code to do it  
**Translation:** 

**[4779.98s] English:** and ultimately also trying to discover like you're saying the self-supervised formulation of the  
**Translation:** 

**[4786.72s] English:** problem so the unsupervised formulation of the problem like uh you know in driving there's this  
**Translation:** 

**[4791.56s] English:** really interesting thing which is you look at a scene that's before you  
**Translation:** 

**[4798.22s] English:** and you have data about what a successful  
**Translation:** 

**[4800.00s] English:** human driver did in that scene you know one second later it's a little piece of data that  
**Translation:** 

**[4806.02s] English:** you can use just like with gpt3 as training currently even though tesla says they're using  
**Translation:** 

**[4811.98s] English:** that it's an open question to me how much how far can you can you sell all of the driving with just  
**Translation:** 

**[4817.98s] English:** that self-supervised piece of data and like i i think that's what common ai is doing that's what  
**Translation:** 

**[4825.90s] English:** common ai is doing but the question is how how much data so what common ai doesn't have  
**Translation:** 

**[4831.54s] English:** is as good of a data engine for example as tesla does that's where the like the organization of  
**Translation:** 

**[4837.94s] English:** the data uh i mean as far as i know i haven't talked to george but they do have the data  
**Translation:** 

**[4843.58s] English:** the question is how much data is needed because we say infinite very loosely here uh it's it's  
**Translation:** 

**[4851.34s] English:** and then the other question which you said i don't know if you think it's still an  
**Translation:** 

**[4855.88s] English:** open question is are we on the right order of magnitude for the compute necessary um that is  
**Translation:** 

**[4862.84s] English:** is this is it like what elon said this chip that's in there now is enough to do full self-driving  
**Translation:** 

**[4868.14s] English:** or do we need another order of magnitude i think nobody actually knows the answer to that question  
**Translation:** 

**[4872.88s] English:** i like the confidence that elon has but yeah we'll see oh and there's another funny thing is you  
**Translation:** 

**[4878.96s] English:** don't learn to drive with infinite amounts of data you learn to drive with an intellectual  
**Translation:** 

**[4883.68s] English:** framework that understands physics and  
**Translation:** 

**[4885.88s] English:** color and horizontal surfaces and laws and roads and you know all your your experience from  
**Translation:** Vocabulary: horizontal: 水平的

**[4894.26s] English:** manipulating your environment like like there's so many factors go into that so then when you  
**Translation:** 

**[4899.52s] English:** learn to drive like driving is a subset of this conceptual framework that you have  
**Translation:** Vocabulary: conceptual: 概念性的; manipulating: 操控

**[4904.98s] English:** right and so with self-driving cars right now we're we're teaching them to drive with driving  
**Translation:** 

**[4910.12s] English:** data you never teach a human to do that you teach a human all kinds of interesting things  
**Translation:** 

**[4915.60s] English:** like  
**Translation:** 

**[4915.88s] English:** language like don't do that you know watch out you know there's all kinds of  
**Translation:** 

**[4920.00s] English:** stuff going on well this is where you i think previous time we talked about where you poetically  
**Translation:** 

**[4925.28s] English:** uh disagreed with my naive uh notion about humans i i just think that humans will make this whole  
**Translation:** Vocabulary: naive: 幼稚; poetically: 诗意地

**[4934.00s] English:** driving thing really difficult yeah all right i said humans don't move that slow it's a ballistics  
**Translation:** 

**[4939.96s] English:** problem it's a ballistic humans are ballistics problem which is like poetry to me it's very  
**Translation:** Vocabulary: ballistic: 弹道学; ballistics: 弹道

**[4944.38s] English:** it's very possible that in driving they're indeed purely a ballistics problem i and i think that's  
**Translation:** 

**[4949.28s] English:** probably the right way to think about it but i still they still continue to surprise me those  
**Translation:** 

**[4954.62s] English:** damn pedestrians the cyclists other humans and other cars and yeah but it's going to be one of  
**Translation:** 

**[4960.14s] English:** these compensating things so the like when you're driving you have an intuition about what humans  
**Translation:** Vocabulary: compensating: 补偿现象; cyclists: 骑自行车的人; intuition: 直觉; pedestrians: 行人

**[4965.96s] English:** are going to do but you don't have 360 cameras and radars and you have an attention problem so you  
**Translation:** 

**[4971.36s] English:** so so the self-driving car comes in with no attention problem 360 cameras right now a bunch  
**Translation:** 

**[4977.42s] English:** of other features yeah so they'll  
**Translation:** 

**[4979.14s] English:** yeah  
**Translation:** 

**[4979.28s] English:** wipe out a whole class of accidents right and you know you know emergency braking with radar  
**Translation:** 

**[4985.54s] English:** and especially as it gets you know ai enhanced will eliminate collisions yeah right but then you  
**Translation:** Vocabulary: collisions: 碰撞

**[4991.20s] English:** have the other problems of these unexpected things where you know you think your human  
**Translation:** 

**[4994.54s] English:** intuition is helping but then the cars also have you know a set of hardware features that you're  
**Translation:** 

**[4999.98s] English:** not even close to and the key thing of course is uh if you wipe out a huge number of kind of  
**Translation:** 

**[5006.44s] English:** accidents then it might be just way safer than  
**Translation:** 

**[5009.14s] English:** than a human driver even though even if humans are still a problem that's hard to figure out  
**Translation:** 

**[5013.84s] English:** yeah that's probably what happens autonomous cars will have a small number of accidents humans  
**Translation:** 

**[5018.98s] English:** would have avoided but they'll wipe they'll get rid of the bulk of them what do you think about  
**Translation:** 

**[5025.42s] English:** uh like tesla's dojo efforts or it can be bigger than tesla in general it's kind of like the tennis  
**Translation:** 

**[5033.64s] English:** torrent trying to innovate like this is the dichotomy like should a company try to from  
**Translation:** 

**[5038.70s] English:** scratch build its own  
**Translation:** Vocabulary: dichotomy: 对立统一; innovate: 创新

**[5040.00s] English:** neural network training hardware well first i think it's great so we need lots of experiments  
**Translation:** 

**[5046.22s] English:** right and there's lots of startups working on this and they're pursuing different things  
**Translation:** Vocabulary: neural: 神经网络; startups: 初创公司

**[5050.80s] English:** you know i was there when we started dojo and it was sort of like what's the unconstrained  
**Translation:** 

**[5055.98s] English:** computer solution to go do very large training problems yeah and then there's fun stuff like  
**Translation:** Vocabulary: unconstrained: 不受限制的

**[5062.98s] English:** you know we said well we have this 10 000 watt board to cool well you go talk to guys at spacex  
**Translation:** 

**[5069.02s] English:** and they think 10 000 watts is a really small number not a big number yeah and and there's  
**Translation:** 

**[5074.12s] English:** brilliant people working on it i'm curious to see how it'll come out i i couldn't tell you you know  
**Translation:** 

**[5078.40s] English:** i know it pivoted a few times since i left so so the cooling does seem to be a big problem i do  
**Translation:** Vocabulary: pivoted: 转变方向

**[5084.78s] English:** like what elon said about it which is like we don't want to do the thing unless it's way better  
**Translation:** 

**[5090.26s] English:** than the alternative whatever the alternative is so it has to be way better than like racks of gpus  
**Translation:** 

**[5096.92s] English:** yeah and then and the other  
**Translation:** 

**[5098.90s] English:** thing  
**Translation:** 

**[5099.02s] English:** is just like you know you know the tesla autonomous driving hardware it was only serving  
**Translation:** 

**[5104.70s] English:** one software stack and the hardware team and the software team were tightly coupled you know if  
**Translation:** 

**[5110.14s] English:** you're building a general purpose ai solution and you know there's so many different customers with  
**Translation:** 

**[5114.34s] English:** so many different needs now something andre said is i think this is amazing 10 years ago  
**Translation:** 

**[5120.64s] English:** like vision recommendation language were completely different disciplines he said  
**Translation:** 

**[5127.46s] English:** the people literally couldn't talk  
**Translation:** Vocabulary: disciplines: 学科

**[5128.90s] English:** to each other and three years ago it was all neural networks but the very different neural networks  
**Translation:** 

**[5134.64s] English:** and recently it's converging on one set of networks they vary a lot in size obviously they vary in data  
**Translation:** Vocabulary: converging: 趋于一致

**[5140.40s] English:** varying outputs but the technology has converged a good bit yeah these transformers behind gpt-3  
**Translation:** 

**[5147.24s] English:** it seems like they could be applied to video they could be applied to a lot of yeah and it's like and  
**Translation:** Vocabulary: converged: 趋于一致

**[5150.96s] English:** they're all really simple it was like to literally replace letters with pixels yeah it does vision  
**Translation:** 

**[5157.16s] English:** it's amazing so yeah but i think it's a really good thing to be able to use this technology to really  
**Translation:** Vocabulary: pixels: 像素

**[5158.78s] English:** So and then side.  
**Translation:** 

**[5160.00s] English:** actually improves the thing so the bigger it gets the more compute you throw at it the better it  
**Translation:** 

**[5164.80s] English:** gets and the more data you have the better it gets so so so then you start to wonder well is that a  
**Translation:** 

**[5171.54s] English:** fundamental thing or is is this just another step to some fundamental understanding about this kind  
**Translation:** 

**[5177.00s] English:** of computation which is really interesting us humans don't want to believe that that kind of  
**Translation:** 

**[5182.04s] English:** thing will achieve conceptual understanding as you were saying like you'll figure out physics  
**Translation:** Vocabulary: computation: 计算; conceptual: 概念

**[5185.50s] English:** but maybe it will maybe it probably will well it's worse than that a little it'll understand  
**Translation:** 

**[5191.60s] English:** physics in ways that we can't understand i like your stephen wolfram talk where he said you know  
**Translation:** Vocabulary: wolfram: 沃夫曼

**[5196.50s] English:** there's three generations of physics there was physics by reasoning well big things should fall  
**Translation:** 

**[5201.22s] English:** faster than small things right that's reasoning and then there's physics by equations like you  
**Translation:** Vocabulary: equations: 数学公式

**[5207.32s] English:** know but the number of programs in the world that are solved with the single equations relatively  
**Translation:** 

**[5211.54s] English:** low almost all programs have you know more than a one line of code maybe a hundred  
**Translation:** 

**[5215.40s] English:** maybe a hundred but the number of programs in the world that are solved with a single  
**Translation:** 

**[5215.48s] English:** million lines of code so he said now we're going to physics by equation which is his project which  
**Translation:** Vocabulary: equation: 方程

**[5220.98s] English:** is cool i might point out there was there was two two generations of physics before reasoning  
**Translation:** 

**[5228.18s] English:** habit like all animals you know no things fall and you know birds fly and you know predators  
**Translation:** Vocabulary: predators: 捕食者

**[5234.88s] English:** know how to you know solve a differential equation to cut off a accelerating you know  
**Translation:** 

**[5240.40s] English:** curving animal path yeah and then there was uh you know the gods did it right so yeah right so  
**Translation:** Vocabulary: accelerating: 加速; differential: 微分

**[5249.66s] English:** there was you know there's five generations now software 2.0 says programming things is not the  
**Translation:** 

**[5256.42s] English:** last step data so there's going to be a physics past stevens wolfram's comp that's not explainable  
**Translation:** 

**[5265.12s] English:** that's not explainable and and actually there's no reason  
**Translation:** 

**[5269.98s] English:** that  
**Translation:** 

**[5270.40s] English:** i can see well that even that's a limit like there's something beyond that i mean they're  
**Translation:** 

**[5275.76s] English:** usually like usually when you have this hierarchy it's not like well if you have this step in this  
**Translation:** Vocabulary: hierarchy: 等级制度

**[5279.68s] English:** step  
**Translation:** 

**[5280.00s] English:** and this step and they're all qualitatively different and conceptually different it's not  
**Translation:** Vocabulary: conceptually: 概念上; qualitatively: 质量上

**[5284.36s] English:** obvious why you know six is the right number of hierarchy steps and not seven or eight or  
**Translation:** 

**[5288.78s] English:** well then it's probably impossible for us to to comprehend something that's beyond the thing  
**Translation:** 

**[5295.82s] English:** that's not explainable yeah but the thing but the thing that you know understands the thing  
**Translation:** 

**[5301.68s] English:** that's not explainable to us will conceive the next one and like i'm not sure why there's a limit  
**Translation:** Vocabulary: conceive: 构思

**[5307.74s] English:** to it uh click your brain hurts that's a sad story if we look at our own brain which is an  
**Translation:** 

**[5316.88s] English:** interesting uh illustrative example in your work with testorant and trying to design uh deep  
**Translation:** Vocabulary: illustrative: 说明性的

**[5324.28s] English:** learning architectures uh do you do you think about the brain at all maybe from a hardware  
**Translation:** 

**[5332.00s] English:** designer perspective if you could uh change something about the brain what would you change  
**Translation:** 

**[5337.36s] English:** or do you think about the brain at all  
**Translation:** 

**[5337.72s] English:** funny question like how would you so your brain is really weird like you know your cerebral cortex  
**Translation:** Vocabulary: cerebral: 大脑的; cortex: 皮层

**[5343.86s] English:** where we think we do most of our thinking is what like six or seven neurons thick yeah like  
**Translation:** 

**[5349.08s] English:** that's weird like all the big networks are way bigger than that like way deeper so that seems  
**Translation:** 

**[5355.02s] English:** odd and then you know when you're thinking if it's if if the input generates a result you can  
**Translation:** 

**[5361.40s] English:** lose it goes really fast but if it can't that generates an output that's interesting which  
**Translation:** 

**[5366.02s] English:** turns into an input and then your brain  
**Translation:** 

**[5367.72s] English:** it's the point where you mull things over for days and how many trips through your brain is that right  
**Translation:** 

**[5372.82s] English:** like it's you know 300 milliseconds or something to get through seven levels of neurons i forget  
**Translation:** 

**[5378.08s] English:** the number exactly but then it does it over and over and over as it searches and the brain clearly  
**Translation:** Vocabulary: milliseconds: 毫秒; neurons: 神经元

**[5384.58s] English:** is looks like some kind of graph because you have a neuron with you know connections and it talks to  
**Translation:** 

**[5388.64s] English:** other ones and it's locally very computationally intense but it's also does sparse computations  
**Translation:** Vocabulary: computationally: 计算上; computations: 计算; neuron: 神经元; sparse: 稀疏

**[5395.36s] English:** across a pretty big area  
**Translation:** 

**[5397.72s] English:** there's a lot of messy biological  
**Translation:** 

**[5400.00s] English:** type of things and it's it's meaning like first of all there's mechanical chemical and electrical  
**Translation:** 

**[5405.44s] English:** signals it's all that's going on then the there's a the asynchronicity of signals and there's like  
**Translation:** Vocabulary: asynchronicity: 信号不同步

**[5413.02s] English:** there's just a lot of variability that seems continuous and messy and just a mess of biology  
**Translation:** 

**[5418.14s] English:** and it's unclear whether that's a good thing or it's a bad thing because it if it's a good thing  
**Translation:** Vocabulary: variability: 变化性

**[5426.26s] English:** that we need to run the entirety of the evolution well we're gonna have to start with basic bacteria  
**Translation:** 

**[5431.44s] English:** to create some imagine we could control you could build a brain with 10 layers would that be better  
**Translation:** Vocabulary: bacteria: 细菌; entirety: 全部

**[5436.24s] English:** or worse or more more connections or less connections or you know we don't know to what  
**Translation:** 

**[5441.54s] English:** level our brains are optimized but if i was changing things like yeah like you know you  
**Translation:** Vocabulary: optimized: 优化

**[5446.70s] English:** can only hold like seven numbers in your head yeah like why not a hundred or a million never  
**Translation:** 

**[5452.08s] English:** thought of that like and why can't like why can't we have like a floating point  
**Translation:** 

**[5456.16s] English:** for that like why can't we have like a floating point for that like why can't we have like a  
**Translation:** 

**[5456.24s] English:** processor that can compute anything we want like and see it all properly like that would be kind of  
**Translation:** Vocabulary: processor: 处理器

**[5462.02s] English:** fun and why can't we we see in four or eight dimensions like like it's you know 3d is kind  
**Translation:** 

**[5468.68s] English:** of a drag like all the hard mass transforms are up in multiple dimensions so there's you know you  
**Translation:** Vocabulary: dimensions: 维度; transforms: 转换

**[5474.96s] English:** could imagine a rain architecture that you know you could enhance with a whole bunch of features  
**Translation:** 

**[5480.98s] English:** that would be you know really useful for thinking about things it's possible that the limitations  
**Translation:** 

**[5485.74s] English:** you're  
**Translation:** 

**[5486.14s] English:** describing are actually essential for like the constraints are essential for creating  
**Translation:** Vocabulary: constraints: 限制条件

**[5492.00s] English:** like the depth of intelligence like that the ability to reason you know it's hard to say  
**Translation:** 

**[5498.96s] English:** because like your brain is clearly a parallel processor you know yeah you know 10 billion  
**Translation:** 

**[5504.72s] English:** neurons talking to each other at a relatively low clock rate but it produces something that  
**Translation:** 

**[5510.48s] English:** looks like a serial thought process it's a serial narrative in your head that's true but then  
**Translation:** Vocabulary: neurons: 神经元

**[5516.14s] English:** there are people famously who are visual thinkers like i  
**Translation:** 

**[5520.00s] English:** think i'm a relatively visual thinker i can imagine any object and rotate it in my head  
**Translation:** Vocabulary: rotate: 旋转; thinkers: 思考者

**[5524.88s] English:** and look at it and there are people who say they don't think that way at all and recently i read  
**Translation:** 

**[5530.68s] English:** an article about people people who say they don't have a they don't have a voice in their head  
**Translation:** 

**[5535.18s] English:** they they can talk but when they you know it's like well what are you thinking  
**Translation:** 

**[5540.78s] English:** they'll they'll describe something that's visual so that's curious  
**Translation:** 

**[5546.12s] English:** now if if you're saying if we dedicated more hardware to holding information like you know  
**Translation:** 

**[5555.50s] English:** 10 numbers or a million numbers like would that just distract us from our ability to form this  
**Translation:** Vocabulary: distract: 分散注意力

**[5562.58s] English:** kind of singular identity like it dissipates somehow right but but maybe you know future  
**Translation:** 

**[5568.84s] English:** humans will have many identities that have some higher level organization but can actually do  
**Translation:** Vocabulary: dissipates: 消散

**[5573.86s] English:** lots more things in parallel yeah there's no  
**Translation:** 

**[5576.12s] English:** reason if we're thinking modularly there's no reason we can't have multiple consciousnesses  
**Translation:** Vocabulary: consciousnesses: 多个意识; modularly: 模块化地

**[5580.10s] English:** in one brain yeah and maybe there's some way to make it faster so that the the you know the the  
**Translation:** 

**[5586.52s] English:** area the computation could could still have a unified feel to it but while still having way  
**Translation:** Vocabulary: computation: 计算

**[5594.84s] English:** more ability to do parallel stuff at the same time could definitely be improved could be improved  
**Translation:** 

**[5599.64s] English:** yeah okay well it's it's pretty good right now actually people don't give it enough credit the  
**Translation:** 

**[5604.74s] English:** thing is pretty nice  
**Translation:** 

**[5606.12s] English:** the you know the the fact that the right ends seem to be  
**Translation:** 

**[5609.94s] English:** and give a nice like spark of uh beauty to the whole experience so i don't know i don't know if  
**Translation:** 

**[5618.82s] English:** it can be improved easily it could be more beautiful i don't know how i yeah what do you  
**Translation:** 

**[5624.44s] English:** mean what do you mean how all the ways you can't imagine no but that's the whole point i wouldn't  
**Translation:** 

**[5629.82s] English:** be able to imagine the fact that i can imagine ways in in in which it could be more beautiful  
**Translation:** 

**[5634.42s] English:** means that the other way around i don't know i don't know i don't know i don't know i don't know  
**Translation:** 

**[5636.12s] English:** you know you know ian banks his stories so the man  
**Translation:** 

**[5639.94s] English:** you  
**Translation:** 

**[5640.00s] English:** the super smart ai's there live mostly live in the world of what they call infinite fun  
**Translation:** 

**[5647.36s] English:** because they can create arbitrary worlds so they interact and you know the story has it they  
**Translation:** 

**[5654.48s] English:** interact in the normal world and they're very smart and they can do all kinds of stuff and  
**Translation:** 

**[5658.88s] English:** you know a given mind can you know talk to a million humans at the same time because we're  
**Translation:** 

**[5662.32s] English:** very slow and for reasons you know artificial the story they're interested in people and doing stuff  
**Translation:** 

**[5668.16s] English:** but they mostly live in this this other land of thinking my inclination is to think that the  
**Translation:** 

**[5675.92s] English:** ability to create infinite fun will um will not be so fun that's sad well there's so many things  
**Translation:** Vocabulary: inclination: 倾向

**[5683.20s] English:** to do imagine be able to make a star move planets around yeah yeah but because we can imagine that  
**Translation:** 

**[5689.92s] English:** is why life is fun if we can if we actually were able to do it it would be a slippery slope  
**Translation:** 

**[5694.88s] English:** where fun wouldn't even have a meeting because we just consistently  
**Translation:** 

**[5698.88s] English:** desensitize ourselves by the infinite amounts of fun we're having  
**Translation:** Vocabulary: desensitize: 麻木

**[5703.92s] English:** and the sadness uh the the dark stuff is what makes it fun i think i mean that could be the  
**Translation:** 

**[5709.76s] English:** russian it could be the could be the fun makes it fun and sadness makes it bittersweet  
**Translation:** Vocabulary: bittersweet: 苦中带甜

**[5716.40s] English:** yeah that's true fun could be uh the thing that makes it fun so what do you think about the  
**Translation:** 

**[5721.52s] English:** expansion not through the biology side but through the bci the brain computer interfaces  
**Translation:** Vocabulary: interfaces: 人机接口

**[5727.20s] English:** now you got a chance to  
**Translation:** 

**[5728.40s] English:** check out the neural link stuff it's super interesting like like humans like  
**Translation:** 

**[5734.16s] English:** like our thoughts to manifest this action you know like like as a kid you know like shooting  
**Translation:** 

**[5739.92s] English:** a rifle was super fun driving a mini bike doing things and then computer games i think for a lot  
**Translation:** Vocabulary: manifest: 显现

**[5746.40s] English:** of kids became the thing where they you know they can do what they want they can fly a plane they  
**Translation:** 

**[5751.36s] English:** can do this they can do this right but you have to have this physical interaction now imagine you know  
**Translation:** 

**[5758.16s] English:** you could just imagine stuff  
**Translation:** 

**[5760.00s] English:** and it happens right like really richly and interestingly like we kind of do  
**Translation:** 

**[5767.26s] English:** that when we dream like dream dreams are funny because like if you have some  
**Translation:** 

**[5771.10s] English:** control or awareness in your dreams like it's very realistic looking or not  
**Translation:** 

**[5777.08s] English:** realistic depends on the dream but you can also manipulate that and you know  
**Translation:** 

**[5783.10s] English:** what's possible there is this is odd and the fact that nobody understands it's  
**Translation:** Vocabulary: manipulate: 操控

**[5787.60s] English:** hilarious but do you think it's possible to expand that capability  
**Translation:** 

**[5792.88s] English:** through computing sure is there some interesting so from a hardware designer  
**Translation:** Vocabulary: capability: 能力; computing: 计算

**[5797.68s] English:** perspective is there do you think you'll present totally new challenges in the  
**Translation:** 

**[5801.76s] English:** kind of hardware that required that like so this hardware isn't standalone  
**Translation:** Vocabulary: standalone: 独立运行

**[5806.66s] English:** computing well this is not working with the brain today computer games are  
**Translation:** 

**[5811.10s] English:** rendered by GPUs right right so but you've seen the GAN stuff yeah right  
**Translation:** 

**[5816.58s] English:** where  
**Translation:** 

**[5817.60s] English:** um trained neural networks render realistic images but there's no pixels  
**Translation:** Vocabulary: neural: 神经网络; pixels: 像素; render: 生成

**[5822.04s] English:** no triangles no shaders no light maps no nothing so the future of graphics is  
**Translation:** 

**[5827.68s] English:** probably AI right yes now that AI is heavily trained by lots of real data  
**Translation:** Vocabulary: shaders: 着色器; triangles: 三角形

**[5834.40s] English:** right so if you have an interface with a AI renderer  
**Translation:** 

**[5839.62s] English:** right so if you say render a cat it won't say well how tall is the cat and  
**Translation:** Vocabulary: interface: 人机界面; renderer: 渲染器

**[5844.72s] English:** how big you know it'll render a cat and you might say well a little bigger a  
**Translation:** 

**[5847.60s] English:** little smaller you know make it a tabby shorter hair you know like you could  
**Translation:** Vocabulary: tabby: 条纹猫

**[5851.86s] English:** tweak it like the the amount of data you'll have to send to interact with a  
**Translation:** 

**[5858.34s] English:** very powerful AI renderer could be low but the question is for brain computer  
**Translation:** Vocabulary: tweak: 调整

**[5864.10s] English:** interfaces would need to render not onto a screen but render onto the brain and  
**Translation:** 

**[5871.00s] English:** like directly so there's a bandwidth we could do it both ways I mean our eyes are  
**Translation:** Vocabulary: bandwidth: 带宽; interfaces: 接口

**[5874.78s] English:** really good sensors they could render onto a screen  
**Translation:** 

**[5877.60s] English:** and we could feel like we're part  
**Translation:** 

**[5880.00s] English:** participating in it you know they're gonna they're gonna have you know like the oculus kind of stuff  
**Translation:** 

**[5884.62s] English:** it's going to be so good when a projection to your eyes you think it's real you know they're  
**Translation:** Vocabulary: oculus: 头戴式显示器; projection: 投影

**[5889.72s] English:** slowly solving those problems and i suspect when the renderer of that information into your head  
**Translation:** 

**[5897.80s] English:** is also ai mediated either they'll be able to give you the cues that you know you really want  
**Translation:** 

**[5904.32s] English:** for depth and all kinds of stuff like your your brain is partly faking your your visual field  
**Translation:** 

**[5910.32s] English:** right like your eyes are twitching around but you don't notice that occasionally they blank you  
**Translation:** 

**[5914.84s] English:** don't notice that you know there's all kinds of things like you think you see over here but you  
**Translation:** 

**[5919.34s] English:** don't really see there yeah it's all fabricated yeah so a peripheral vision is fascinating so if  
**Translation:** Vocabulary: fabricated: 虚构; peripheral: 边缘

**[5925.94s] English:** you have an ai renderer that's trained to understand exactly how you see and the kind of  
**Translation:** 

**[5933.00s] English:** things that enhance the  
**Translation:** 

**[5934.26s] English:** the  
**Translation:** 

**[5934.30s] English:** the  
**Translation:** 

**[5934.32s] English:** the realism of the experience could be super real actually  
**Translation:** 

**[5937.30s] English:** so i don't know what the limits that are but obviously if if we have a brain interface that  
**Translation:** 

**[5947.04s] English:** goes in inside your you know visual cortex in a better way than your eyes do which is possible  
**Translation:** 

**[5952.80s] English:** it's a lot of neurons yeah um maybe that'll be even cooler but the really cool thing is it has  
**Translation:** Vocabulary: cortex: 皮层; neurons: 神经元

**[5961.28s] English:** to do with the the infinite fun that you were referring to which is  
**Translation:** 

**[5964.30s] English:** the infinite fun that you were referring to which is  
**Translation:** 

**[5964.78s] English:** our brains seem to be very limited and like you said computations also very plastic  
**Translation:** 

**[5969.74s] English:** very plastic yeah yeah so it's a it's a com interesting combination  
**Translation:** Vocabulary: computations: 计算能力

**[5974.78s] English:** the the interesting open question is the limits of that neuroplasticity like how  
**Translation:** 

**[5980.14s] English:** how flexible is that thing because we don't we haven't really tested it  
**Translation:** Vocabulary: neuroplasticity: 神经可塑性

**[5984.70s] English:** we know about the experiments where they they put like a pressure pad on somebody's head  
**Translation:** 

**[5988.94s] English:** and had a visual transducer pressurize it and somebody slowly learned to see yep  
**Translation:** Vocabulary: pressurize: 加压; transducer: 转换器

**[5994.30s] English:** it's like it's especially at a young age if you throw a lot at it like what what can it  
**Translation:** 

**[6000.00s] English:** can it completely so can you like arbitrarily expand it with computing power so  
**Translation:** Vocabulary: arbitrarily: 任意; computing: 计算

**[6007.12s] English:** connected to the internet directly somehow yeah the answer is probably yes so the problem with  
**Translation:** 

**[6012.66s] English:** biology and ethics is like there's a mess there like us humans are perhaps unwilling to take  
**Translation:** 

**[6019.80s] English:** risks in uh into directions that are full of uncertainty so it's like 90 of the population  
**Translation:** 

**[6027.56s] English:** is unwilling to take risks the other 10 is rushing into the risks unaided by any infrastructure  
**Translation:** Vocabulary: unwilling: 不愿意

**[6033.04s] English:** whatsoever and you know and that that's where all the fun happens in you know society there's  
**Translation:** 

**[6039.02s] English:** been huge transformations yeah in the last you know a couple thousand years yeah it's funny i  
**Translation:** Vocabulary: transformations: 巨大变革

**[6044.36s] English:** mean i got a chance to interact with uh uh this is matthew johnson from johns hopkins he's doing  
**Translation:** 

**[6049.70s] English:** this large-scale study of psychedelics it's it's becoming more and more i've gotten a chance to  
**Translation:** Vocabulary: matthew: 马修; psychedelics: 致幻剂

**[6054.88s] English:** interact with that community of scientists working on psychedelics  
**Translation:** 

**[6057.42s] English:** but because of that that opened the door to me to all these uh what are they called psychonauts  
**Translation:** Vocabulary: psychonauts: 精神探索者

**[6063.56s] English:** the people who like you said the 10 percent who like i don't care i don't know if there's a science  
**Translation:** 

**[6069.16s] English:** behind this i'm taking this spaceship to if i'm be the first on mars i'll be uh the you know you  
**Translation:** 

**[6075.54s] English:** know psychedelics interesting in the sense that in another dimension uh like you said it's a way to  
**Translation:** 

**[6082.00s] English:** explore the the limits of the human mind like what is this thing capable of  
**Translation:** Vocabulary: dimension: 维度

**[6087.42s] English:** doing because you kind of like when you dream you detach it i don't know exactly in your science of  
**Translation:** 

**[6092.92s] English:** it but you detach your like reality from what your mind the images your mind is able to conjure up and  
**Translation:** Vocabulary: conjure: 召唤

**[6100.86s] English:** your mind goes into weird places and like entities appear somehow freudian type of like trauma is  
**Translation:** 

**[6108.82s] English:** probably connected in there somehow but you start to have like these weird vivid worlds that like  
**Translation:** Vocabulary: freudian: 弗洛伊德式的; trauma: 创伤

**[6113.96s] English:** so do you actively dream do you  
**Translation:** 

**[6117.42s] English:** why not  
**Translation:** 

**[6120.00s] English:** hours of dreams and i it's like really useful time i know i don't i haven't uh i don't for  
**Translation:** 

**[6125.70s] English:** some reason i just knock out and uh i have sometimes like anxiety inducing kind of like  
**Translation:** Vocabulary: inducing: 引起

**[6131.68s] English:** very pragmatic like nightmare type of dreams but not nothing fun nothing nothing fun nothing fun  
**Translation:** 

**[6139.88s] English:** i i try i i unfortunately have mostly have fun in uh the waking world which is very limited in  
**Translation:** Vocabulary: pragmatic: 实际

**[6147.78s] English:** the amount of fun you can have it's not that limited either yeah that's why we'll have to talk  
**Translation:** 

**[6153.26s] English:** yeah i need instructions uh yeah well there's like a manual for that you might want to  
**Translation:** 

**[6159.56s] English:** i looked it up i'll ask you on what uh what did you dream you know years ago and i read about you  
**Translation:** 

**[6166.52s] English:** know like you know a book about how to have you know become aware of your dreams i worked on it  
**Translation:** 

**[6173.84s] English:** for a while like there's this trick about you know imagine you can see your hands and look  
**Translation:** 

**[6177.76s] English:** out and and i got somewhat good at it like but my mostly when i'm thinking about things or working  
**Translation:** 

**[6184.62s] English:** on problems i i i prep myself before i go to sleep it's like i i pull into my mind all the  
**Translation:** 

**[6192.88s] English:** things i want to work on or think about and then that let's say greatly improves the chances that  
**Translation:** 

**[6199.98s] English:** i'll work on that while i'm sleeping and then and then i also you know basically ask to  
**Translation:** 

**[6207.76s] English:** remember it and i often remember very detailed within the dream yeah or outside the dream well  
**Translation:** 

**[6215.52s] English:** to bring it up in in my dreaming and then remember it when i wake up  
**Translation:** 

**[6219.30s] English:** it's just it's more of a meditative practice you say you know to prepare yourself to do that  
**Translation:** 

**[6227.66s] English:** like if you go to you know the sleep still gnashing your teeth about some random thing  
**Translation:** 

**[6232.88s] English:** that happened that you're not that really interested in you'll dream about it  
**Translation:** Vocabulary: gnashing: 磨牙

**[6237.76s] English:** that's really interesting maybe but you can  
**Translation:** 

**[6240.00s] English:** direct your dreams somewhat by prepping you know i'm going to have to try that it's really  
**Translation:** Vocabulary: prepping: 预先准备

**[6245.66s] English:** interesting like the most important the interesting not like uh what what did this guy send an email  
**Translation:** 

**[6252.06s] English:** kind of like stupid worry stuff but like fundamental problems you're actually concerned  
**Translation:** 

**[6255.84s] English:** about yeah prepping and interesting things you're worried about or books you're reading or you know  
**Translation:** 

**[6259.92s] English:** some great conversation you had or some some adventure you want to have like there's there's  
**Translation:** 

**[6264.14s] English:** a lot of space there and and it seems to work that you know my percentage of interesting dreams  
**Translation:** 

**[6274.28s] English:** and memories went up is there uh is that the source of uh if you were able to deconstruct  
**Translation:** Vocabulary: deconstruct: 拆解

**[6282.00s] English:** like where some of your best ideas came from is there a process that's at the core of that  
**Translation:** 

**[6288.94s] English:** like so some people you know walk and think some people like in the shower the best  
**Translation:** 

**[6293.62s] English:** ideas came from like is there a process that's at the core of that like so some people you know  
**Translation:** 

**[6294.12s] English:** ideas hit him if you talk about like newton apple hitting him on the head no i i found out a long  
**Translation:** 

**[6299.94s] English:** time ago i'm i'm i process things somewhat slowly so like in college i had friends who could study  
**Translation:** 

**[6305.60s] English:** at the last minute get an a next day i can't do that at all so i always front loaded all the work  
**Translation:** 

**[6310.68s] English:** like i do all the problems early you know for finals like the last three days i wouldn't look  
**Translation:** 

**[6316.24s] English:** at a book because i want you know because like a new fact day before finals may screw up my  
**Translation:** 

**[6322.34s] English:** understanding of what i thought i knew so my my goal was to always get it in and and give it time  
**Translation:** 

**[6328.44s] English:** to soak and i used to you know i remember when we were doing like 3d calculus i would have these  
**Translation:** Vocabulary: calculus: 微积分

**[6334.30s] English:** amazing dreams of 3d surfaces with normal you know calculating the gradient and this is like  
**Translation:** 

**[6339.02s] English:** all come up so it was like really fun like very visual and uh and if i got cycles of that that  
**Translation:** Vocabulary: gradient: 梯度

**[6346.56s] English:** was useful um and the other is just don't over filter your ideas like i like that  
**Translation:** 

**[6352.34s] English:** process of brainstorming where lots of ideas can happen i like people who have lots of ideas  
**Translation:** Vocabulary: brainstorming: 头脑风暴

**[6357.10s] English:** and then just let them sit then there's a yeah i'll let them sit  
**Translation:** 

**[6360.00s] English:** it and let it breathe a little bit and then reduce it to practice like at some point you really have  
**Translation:** 

**[6366.92s] English:** to does it really work like you know is this real or not right but you but you have to do both  
**Translation:** 

**[6374.82s] English:** there's creative tension there like how do you be both open and you know precise have you had  
**Translation:** 

**[6380.84s] English:** ideas that you just that sit in your mind for like years yeah before that sure that's it's an  
**Translation:** 

**[6388.04s] English:** interesting uh way to is generate ideas and just let them sit let them sit there for a while  
**Translation:** 

**[6394.44s] English:** i think i have a few of those ideas you know it was so funny  
**Translation:** 

**[6399.22s] English:** yeah i think that's you know creativity uh this one or something for the slow thinkers in the  
**Translation:** Vocabulary: thinkers: 思考者

**[6407.10s] English:** in the room i suppose as i some people like you said are just like like the yeah it's really  
**Translation:** 

**[6413.94s] English:** interesting there's so much diversity in how people think yeah you know  
**Translation:** 

**[6418.02s] English:** how fast or slow they are how well they remember or don't like you know i'm not super good at  
**Translation:** 

**[6423.10s] English:** remembering facts but processes and methods like in our engineering i went to penn state and almost  
**Translation:** 

**[6428.70s] English:** all our engineering uh tests were open book i could remember the page and not the formula  
**Translation:** 

**[6433.98s] English:** but as soon as i saw the formula i could remember the whole method if i if i learned it yeah no so  
**Translation:** 

**[6440.62s] English:** it's it's a funny where some people could you know i just watched friends like flipping through the  
**Translation:** 

**[6445.38s] English:** book trying to find the formula even knowing the formula and then i could remember the formula  
**Translation:** 

**[6448.02s] English:** knowing that they'd done just as much work and i would just open the book and i was on page 27  
**Translation:** 

**[6452.30s] English:** bottom half i could see the whole thing visually yeah and you know and you have to learn that about  
**Translation:** 

**[6458.56s] English:** yourself and figure out what the function optimally i had a friend who who was always  
**Translation:** 

**[6462.74s] English:** concerned he didn't know how he came up with ideas he had lots of ideas but he said they just  
**Translation:** Vocabulary: optimally: 最优化地

**[6467.34s] English:** sort of popped up like you'd be working on something you have this idea like where does  
**Translation:** 

**[6471.46s] English:** it come from but you can have more awareness of it like yeah like like like how you  
**Translation:** 

**[6478.02s] English:** how your brain works is a little murky as you go  
**Translation:** 

**[6480.00s] English:** down from the voice in your head or the obvious visualizations like when you visualize something  
**Translation:** Vocabulary: murky: 模糊不清; visualizations: 想象画面; visualize: 想象

**[6484.96s] English:** how does that happen yes you know if i say you know visualize volcano it's easy to do right  
**Translation:** 

**[6490.16s] English:** and what does it actually look like when you visualize it i can visualize to the point where  
**Translation:** 

**[6493.76s] English:** i don't see it very much out of my eyes and i see the colors of the thing i'm visualizing  
**Translation:** 

**[6498.08s] English:** yeah but there's like there's a shape there's a texture there's a color but there's also  
**Translation:** Vocabulary: visualizing: 想象

**[6501.68s] English:** conceptual visualization like what are you actually visualizing when you're visualizing  
**Translation:** 

**[6506.48s] English:** volcano just like with peripheral vision you think you see the whole thing yeah yeah that's  
**Translation:** Vocabulary: conceptual: 概念; peripheral: 边缘; visualization: 可视化

**[6510.56s] English:** a good way to say it you know you have this kind of almost peripheral vision of your visualizations  
**Translation:** 

**[6516.00s] English:** they're like these ghosts but if you know if you if you work on it you can get a pretty high level  
**Translation:** 

**[6521.20s] English:** of detail and somehow you can walk along those visualizations to come up with an idea which is uh  
**Translation:** 

**[6526.48s] English:** but weird but when you're thinking about solving problems  
**Translation:** 

**[6530.88s] English:** like you're putting information and you're exercising the stuff you do know  
**Translation:** 

**[6535.60s] English:** you're sort of  
**Translation:** 

**[6536.48s] English:** easing the area that's you don't understand and don't know but you can almost you know feel  
**Translation:** 

**[6544.40s] English:** you know that process happening you know that's that's how i like like like i know sometimes when  
**Translation:** 

**[6551.20s] English:** i'm working really hard on something like like i get really hot when i'm sleeping and you know it's  
**Translation:** 

**[6555.60s] English:** like we got the blank throw i wake up with all the blankets are on the floor and and you know  
**Translation:** 

**[6560.72s] English:** every time it's while i wake up and think wow that was great you know are you able to uh  
**Translation:** 

**[6566.32s] English:** just  
**Translation:** 

**[6566.48s] English:** to reverse engineer what the hell happened there oh sometimes it's vivid dreams and sometimes it's  
**Translation:** 

**[6571.04s] English:** just kind of like you say like shadow thinking that you you sort of have this feeling you're  
**Translation:** 

**[6575.60s] English:** you're going through this stuff but it's it's not that obvious isn't that so amazing that the mind  
**Translation:** 

**[6580.16s] English:** just does all these little experiments i never you know i thought i always thought um it's like  
**Translation:** 

**[6585.36s] English:** a river that you can't you're just there for the ride but you're right if you prep it no it's it's  
**Translation:** 

**[6591.20s] English:** all understandable meditation really helps you you got to start figuring out you need to learn language  
**Translation:** Vocabulary: understandable: 容易理解的

**[6596.48s] English:** mind and there's  
**Translation:** 

**[6600.00s] English:** multiple levels of it but the abstractions again right it's somewhat comprehensible  
**Translation:** Vocabulary: abstractions: 抽象; comprehensible: 可理解的

**[6605.08s] English:** and observable and feelable or whatever the right word is you know it's you know you're  
**Translation:** 

**[6612.24s] English:** not along for the ride you are the ride i have to ask you hardware engineer working on neural  
**Translation:** Vocabulary: feelable: 可感知的; neural: 神经的; observable: 可观测的

**[6618.58s] English:** networks now what's consciousness what the hell is that thing is that is that just some little  
**Translation:** 

**[6625.12s] English:** weird quirk of our particular uh computing device or is it something fundamental that  
**Translation:** Vocabulary: computing: 计算; quirk: 怪异特性

**[6630.64s] English:** we really need to crack open if we're to to uh build like good computers do you ever think  
**Translation:** 

**[6636.96s] English:** about consciousness like why it feels like something to be i know it's it's it's really  
**Translation:** 

**[6641.12s] English:** weird so yeah i mean everything about it's weird first it's a half a second behind reality  
**Translation:** 

**[6649.84s] English:** right it's a post-hoc narrative about what happened you've already  
**Translation:** 

**[6654.36s] English:** done something  
**Translation:** 

**[6655.12s] English:** stuff by the time you're conscious of it and your consciousness generally is a single threaded  
**Translation:** Vocabulary: threaded: 单一线程

**[6660.86s] English:** thing but we know your brain is 10 billion neurons running some crazy parallel thing  
**Translation:** 

**[6666.94s] English:** and there's a really big sorting thing going on there it also seems to be really reflective in  
**Translation:** Vocabulary: neurons: 神经元; reflective: 反思的

**[6673.12s] English:** the sense that you create a space in your head right like we don't really see anything right  
**Translation:** 

**[6679.46s] English:** like photons hit your eyes it gets turned into signals it goes through multiple layers of neurons  
**Translation:** Vocabulary: photons: 光子

**[6685.12s] English:** you know like i'm so curious that you know that looks glassy and that looks not glassy like  
**Translation:** 

**[6690.64s] English:** like how the resolution of your vision is so high you have to go through all this processing  
**Translation:** 

**[6694.94s] English:** where for most of it it looks nothing like vision right like like there's no theater in your mind  
**Translation:** 

**[6702.24s] English:** right so we we have a world in our heads we're literally just isolated behind our sensors  
**Translation:** Vocabulary: isolated: 独立存在

**[6711.26s] English:** but we can look at it speculate about  
**Translation:** 

**[6715.12s] English:** it speculated about alternatives problem-solve what if  
**Translation:** Vocabulary: speculate: 猜测; speculated: 猜测

**[6720.00s] English:** There's so many things going on, and that process is lagging reality.  
**Translation:** 

**[6726.30s] English:** And it's single-threaded, even though the underlying thing is massively parallel.  
**Translation:** Vocabulary: lagging: 落后于; massively: 大规模地

**[6730.50s] English:** So it's so curious.  
**Translation:** 

**[6732.74s] English:** So imagine you're building an AI computer.  
**Translation:** 

**[6734.54s] English:** If you wanted to replicate humans, well, you'd have huge arrays of neural networks,  
**Translation:** 

**[6738.24s] English:** and apparently only six or seven deep, which is hilarious.  
**Translation:** Vocabulary: neural: 神经元的

**[6742.42s] English:** They don't even remember seven numbers, but I think we can upgrade that a lot.  
**Translation:** 

**[6745.24s] English:** And then somewhere in there, you would train the network to create basically the world that you live in.  
**Translation:** 

**[6752.78s] English:** So it tells stories to itself about the world that it's perceiving.  
**Translation:** 

**[6756.82s] English:** Well, create the world, tell stories in the world,  
**Translation:** Vocabulary: perceiving: 感知

**[6760.88s] English:** and then have many dimensions of side shows to it.  
**Translation:** 

**[6767.66s] English:** We have an emotional structure.  
**Translation:** Vocabulary: dimensions: 维度

**[6769.42s] English:** We have a biological structure.  
**Translation:** 

**[6771.42s] English:** And that seems hierarchical, too.  
**Translation:** Vocabulary: hierarchical: 等级分明的

**[6772.66s] English:** If you're hungry, it dominates your thing.  
**Translation:** 

**[6775.24s] English:** If you're thinking, if you're mad, it dominates your thinking.  
**Translation:** Vocabulary: dominates: 支配

**[6778.86s] English:** And we don't know if that's important to consciousness or not,  
**Translation:** 

**[6781.28s] English:** but it certainly disrupts, intrudes in the consciousness.  
**Translation:** Vocabulary: disrupts: 扰乱; intrudes: 侵入

**[6785.84s] English:** So there's lots of structure to that.  
**Translation:** 

**[6787.96s] English:** And we like to dwell on the past.  
**Translation:** Vocabulary: dwell: 停留

**[6789.86s] English:** We like to think about the future.  
**Translation:** 

**[6791.26s] English:** We like to imagine.  
**Translation:** 

**[6792.18s] English:** We like to fantasize.  
**Translation:** 

**[6794.58s] English:** And the somewhat circular observation of that is the thing we call consciousness.  
**Translation:** Vocabulary: fantasize: 幻想

**[6801.66s] English:** Now, if you created a computer system that did all things,  
**Translation:** 

**[6803.86s] English:** created worldviews,  
**Translation:** 

**[6804.90s] English:** created,  
**Translation:** 

**[6805.24s] English:** created future alternate histories,  
**Translation:** 

**[6807.58s] English:** dwelled on past events accurately or semi-accurately.  
**Translation:** 

**[6812.92s] English:** Well, consciousness just spring up like natural.  
**Translation:** Vocabulary: dwelled: 停留于过去

**[6815.32s] English:** Well, would that look and feel conscious to you?  
**Translation:** 

**[6818.06s] English:** Like you seem conscious to me, but I don't.  
**Translation:** 

**[6819.80s] English:** Off of the external observer sense.  
**Translation:** 

**[6821.76s] English:** Do you think a thing that looks conscious is conscious?  
**Translation:** Vocabulary: observer: 观察者

**[6824.92s] English:** Like, do you, again, this is like an engineering kind of question, I think,  
**Translation:** 

**[6829.24s] English:** because, like,  
**Translation:** 

**[6833.86s] English:** I don't know.  
**Translation:** 

**[6834.46s] English:** If we want to engineer consciousness,  
**Translation:** 

**[6836.72s] English:** is it okay to engineer something that just looks conscious?  
**Translation:** 

**[6839.34s] English:** Yes.  
**Translation:** 

**[6840.00s] English:** or is there a difference between  
**Translation:** 

**[6842.54s] English:** well we have all consciousness because it's a super  
**Translation:** 

**[6844.78s] English:** effective way to manage our affairs  
**Translation:** 

**[6846.52s] English:** yeah it's a social element  
**Translation:** 

**[6848.62s] English:** well it gives us a planning system  
**Translation:** 

**[6850.48s] English:** you know we have a huge amount of stuff  
**Translation:** 

**[6852.76s] English:** like when we're talking  
**Translation:** 

**[6854.18s] English:** like the reason we can talk really fast is we're modeling  
**Translation:** 

**[6856.72s] English:** each other a really high level of detail  
**Translation:** 

**[6858.96s] English:** and consciousness is required for that  
**Translation:** 

**[6860.60s] English:** well all those  
**Translation:** 

**[6862.66s] English:** components together manifest consciousness  
**Translation:** 

**[6864.70s] English:** right  
**Translation:** 

**[6866.32s] English:** so if we make intelligent beings that we want  
**Translation:** 

**[6868.80s] English:** to interact with that we're like  
**Translation:** 

**[6870.12s] English:** wondering what they're thinking  
**Translation:** 

**[6871.78s] English:** looking forward to seeing them  
**Translation:** 

**[6874.16s] English:** when they interact with them  
**Translation:** 

**[6876.14s] English:** they're interesting, surprising  
**Translation:** 

**[6877.78s] English:** you know fascinating  
**Translation:** 

**[6880.04s] English:** you know they will probably  
**Translation:** 

**[6882.02s] English:** feel conscious like we do and we'll  
**Translation:** 

**[6884.00s] English:** perceive them as conscious  
**Translation:** 

**[6885.02s] English:** I don't know why not  
**Translation:** Vocabulary: perceive: 感知

**[6887.86s] English:** but you never know  
**Translation:** 

**[6888.82s] English:** another fun question on this because  
**Translation:** 

**[6891.66s] English:** from a computing  
**Translation:** 

**[6894.24s] English:** perspective we're trying to create something that's  
**Translation:** Vocabulary: computing: 计算

**[6896.14s] English:** human like or super human like  
**Translation:** 

**[6897.56s] English:** right  
**Translation:** 

**[6898.80s] English:** let me ask you about aliens  
**Translation:** 

**[6900.68s] English:** aliens  
**Translation:** 

**[6901.58s] English:** do you think  
**Translation:** 

**[6905.18s] English:** there's intelligent alien civilizations  
**Translation:** Vocabulary: alien: 外星的; civilizations: 文明

**[6907.64s] English:** out there and do you think  
**Translation:** 

**[6909.84s] English:** their  
**Translation:** 

**[6911.14s] English:** technology, their computing  
**Translation:** 

**[6913.84s] English:** their AI bots  
**Translation:** 

**[6915.66s] English:** their chips  
**Translation:** 

**[6917.92s] English:** are of the same nature  
**Translation:** 

**[6919.98s] English:** as ours  
**Translation:** 

**[6920.56s] English:** I have no idea  
**Translation:** 

**[6922.80s] English:** if there's lots of aliens out there that have been awfully quiet  
**Translation:** 

**[6925.92s] English:** there's  
**Translation:** Vocabulary: awfully: 非常

**[6927.80s] English:** speculation about  
**Translation:** 

**[6928.80s] English:** why  
**Translation:** Vocabulary: speculation: 猜测

**[6929.80s] English:** there seems to be more than enough planets  
**Translation:** 

**[6933.72s] English:** out there  
**Translation:** 

**[6934.72s] English:** there's a lot  
**Translation:** 

**[6935.72s] English:** yeah  
**Translation:** 

**[6936.72s] English:** um  
**Translation:** 

**[6937.72s] English:** there's intelligent life on this planet that seems quite different  
**Translation:** 

**[6940.16s] English:** you know like  
**Translation:** 

**[6941.16s] English:** you know dolphins seem like plausibly understandable  
**Translation:** Vocabulary: plausibly: 合情合理; understandable: 容易理解

**[6944.48s] English:** octopuses don't seem understandable at all  
**Translation:** 

**[6946.44s] English:** if they live longer than a year maybe they would be running the planet  
**Translation:** Vocabulary: octopuses: 八臂章鱼

**[6950.92s] English:** they seem really smart  
**Translation:** 

**[6952.62s] English:** and their neural architecture is completely different than ours  
**Translation:** 

**[6956.58s] English:** now who knows how they perceive things  
**Translation:** 

**[6958.14s] English:** I mean that's the question is for us  
**Translation:** 

**[6960.00s] English:** intelligent beings we might not be able to perceive other kinds of intelligence if they  
**Translation:** 

**[6963.90s] English:** become sufficiently different than us yeah like we live in the current constrained world you know  
**Translation:** Vocabulary: constrained: 限制较多; sufficiently: 足够

**[6969.06s] English:** it's three-dimensional geometry and the geometry defines a certain amount of physics and you know  
**Translation:** 

**[6975.18s] English:** you know there's like how time work seems to work like there's so many things that seem like a whole  
**Translation:** Vocabulary: geometry: 几何学

**[6981.40s] English:** bunch of the input parameters to the you know another conscious being are the same yes like  
**Translation:** 

**[6986.84s] English:** if it's biological biological things seem to be in a relatively narrow temperature range  
**Translation:** 

**[6991.64s] English:** right because you know organics don't aren't stable too cold or too hot you know so so there's  
**Translation:** 

**[6998.94s] English:** if you specify the list of things that input to that but as soon as we make really smart  
**Translation:** Vocabulary: organics: 有机物

**[7006.96s] English:** you know beings and they go solve about how to think about a billion numbers at the same time  
**Translation:** 

**[7012.82s] English:** and and how to think in n dimensions there's a funny science fiction  
**Translation:** Vocabulary: dimensions: 多维空间

**[7016.84s] English:** book where the all the society had uploaded into this matrix and at some point some some of the  
**Translation:** 

**[7023.14s] English:** beans in the matrix thought I wonder if there's intelligent life out there so they had to do a  
**Translation:** Vocabulary: matrix: 数据矩阵

**[7028.52s] English:** whole bunch of work to figure out like how to make a physical thing because their matrix was  
**Translation:** 

**[7033.16s] English:** self-sustaining and they made a little spaceship and they traveled to another planet when they got  
**Translation:** 

**[7038.02s] English:** there there was like life running around but there was no intelligent life and then they figured out  
**Translation:** 

**[7043.42s] English:** that there was these huge you know organic  
**Translation:** 

**[7046.84s] English:** matrix all over the planet inside there were intelligent beings had uploaded themselves and  
**Translation:** 

**[7051.82s] English:** into that matrix so everywhere intelligent life was soon as it got smart it up leveled itself into  
**Translation:** 

**[7062.34s] English:** something way more interesting than 3d geometry and yeah it escaped whatever this is better yeah  
**Translation:** 

**[7069.34s] English:** the the essence of what we think of as an intelligent being I tend to like the thought  
**Translation:** 

**[7076.84s] English:** that the organism like humans aren't the organisms  
**Translation:** 

**[7080.00s] English:** I like the notion of, like, Richard Dawkins and memes that ideas themselves are the organisms, like, that are just using our minds to evolve.  
**Translation:** Vocabulary: dawkins: 道金斯

**[7091.24s] English:** So, like, we're just, like, meat receptacles for ideas to breed and multiply and so on.  
**Translation:** 

**[7098.32s] English:** And maybe those are the aliens.  
**Translation:** Vocabulary: multiply: 繁殖; receptacles: 容器

**[7102.16s] English:** So, Jordan Peterson has a line that says, you know, you think you have ideas, but ideas have you.  
**Translation:** 

**[7109.14s] English:** Yeah.  
**Translation:** Vocabulary: peterson: 佩特森

**[7109.68s] English:** Right?  
**Translation:** 

**[7110.08s] English:** Good line.  
**Translation:** 

**[7110.54s] English:** And then we know about the phenomenon of groupthink, and there are so many things that constrain us.  
**Translation:** 

**[7117.88s] English:** But I think you can examine all that and not be completely owned by the ideas and completely sucked into groupthink.  
**Translation:** Vocabulary: constrain: 限制; groupthink: 团体思维

**[7125.92s] English:** And part of your responsibility as a human is to escape that kind of phenomena, which isn't, you know, it's one of the creative tension things again.  
**Translation:** 

**[7135.78s] English:** You're constructed by it, but you can still observe it.  
**Translation:** 

**[7139.56s] English:** And you can think.  
**Translation:** 

**[7140.00s] English:** You can think about it.  
**Translation:** 

**[7140.72s] English:** And you can make choices about, to some level, how constrained you are by it.  
**Translation:** 

**[7146.94s] English:** And, you know, it's useful to do that.  
**Translation:** Vocabulary: constrained: 限制

**[7151.78s] English:** And, but at the same time, and it could be by doing that, you know, the group in society you're part of becomes collectively even more interesting.  
**Translation:** 

**[7163.92s] English:** So, you know, so the outside observer will think, wow, you know, all these Lex's running around.  
**Translation:** Vocabulary: observer: 观察者

**[7170.00s] English:** With all these really independent ideas have created something even more interesting in the aggregate.  
**Translation:** 

**[7175.96s] English:** So, so I, so I don't know.  
**Translation:** Vocabulary: aggregate: 整体

**[7178.42s] English:** I'm, those are lenses to look at the situation.  
**Translation:** 

**[7181.82s] English:** That'll give you some inspiration, but I don't think they're constraints.  
**Translation:** Vocabulary: constraints: 限制

**[7185.16s] English:** Right.  
**Translation:** 

**[7185.80s] English:** You know.  
**Translation:** 

**[7186.36s] English:** As a small little quirk of history, it seems like you're related to Jordan Peterson, like you mentioned.  
**Translation:** 

**[7194.60s] English:** He's going through some rough stuff now.  
**Translation:** Vocabulary: quirk: 历史趣事

**[7197.34s] English:** Is there some comment you can make about that?  
**Translation:** 

**[7200.00s] English:** the roughness of the human journey, the ups and downs.  
**Translation:** Vocabulary: roughness: 坎坷

**[7204.28s] English:** Well, I became an expert in benzo withdrawal,  
**Translation:** 

**[7211.00s] English:** which is you took benzo to Aspen and at some point they interact with GABA circuits  
**Translation:** Vocabulary: aspen: 白桦树; benzo: 苯二氮卓; circuits: 电路; withdrawal: 戒断

**[7217.94s] English:** to reduce anxiety and do a hundred other things.  
**Translation:** 

**[7222.02s] English:** There's actually no known list of everything they do  
**Translation:** 

**[7225.04s] English:** because they interact with so many parts of your body.  
**Translation:** 

**[7227.22s] English:** And then once you're on them, you habituate to them and you have a dependency.  
**Translation:** 

**[7232.68s] English:** It's not like you're a drug dependency where you're trying to get high.  
**Translation:** 

**[7235.22s] English:** It's a metabolic dependency.  
**Translation:** 

**[7238.90s] English:** And then if you discontinue them, there's a funny thing called kindling,  
**Translation:** 

**[7245.36s] English:** which is if you stop them and then you'll have a horrible withdrawal symptoms.  
**Translation:** Vocabulary: discontinue: 停止; kindling: 柴火

**[7249.92s] English:** If you go back on them at the same level, you won't be stable.  
**Translation:** 

**[7253.18s] English:** And that unfortunately happened to him.  
**Translation:** 

**[7255.54s] English:** Because it's so deeply integrated.  
**Translation:** 

**[7257.34s] English:** It literally changes the size and numbers of neurotransmitter sites in your brain.  
**Translation:** 

**[7263.50s] English:** So there's a process called the Ashton Protocol  
**Translation:** 

**[7267.06s] English:** where you taper it down slowly over two years.  
**Translation:** Vocabulary: ashton: 阿什顿协议

**[7270.38s] English:** The people that go through that go through unbelievable hell.  
**Translation:** 

**[7273.80s] English:** And what Jordan went through seemed to be worse  
**Translation:** 

**[7275.58s] English:** because on advice of doctors, you know,  
**Translation:** 

**[7278.50s] English:** well, stop taking these and take this.  
**Translation:** 

**[7280.24s] English:** It was a disaster.  
**Translation:** 

**[7281.76s] English:** And he got some, you know, it was pretty tough.  
**Translation:** 

**[7286.26s] English:** It seems to be...  
**Translation:** 

**[7287.22s] English:** It seems to be doing quite a bit better intellectually.  
**Translation:** Vocabulary: intellectually: 智力上

**[7289.20s] English:** You can see his brain clicking back together.  
**Translation:** 

**[7292.02s] English:** I spent a lot of time with him.  
**Translation:** 

**[7292.92s] English:** I've never seen anybody suffer so much.  
**Translation:** 

**[7294.90s] English:** Well, his brain is also like this powerhouse, right?  
**Translation:** Vocabulary: powerhouse: 动力源

**[7297.70s] English:** So I wonder, does a brain that's able to think deeply about the world suffer more  
**Translation:** 

**[7304.08s] English:** through these kinds of withdrawals?  
**Translation:** Vocabulary: withdrawals: 戒断症状

**[7305.28s] English:** Like...  
**Translation:** 

**[7306.22s] English:** I don't know.  
**Translation:** 

**[7306.62s] English:** I've watched videos of people going through withdrawal.  
**Translation:** 

**[7309.46s] English:** They all seem to suffer unbelievably.  
**Translation:** Vocabulary: unbelievably: 难以置信地

**[7314.04s] English:** And, you know, my heart goes out to everybody.  
**Translation:** 

**[7317.22s] English:** And there's some funny math about this.  
**Translation:** 

**[7319.30s] English:** Some doctor said...  
**Translation:** 

**[7320.00s] English:** as best he can tell you know there's the standard recommendations don't take them for more than a  
**Translation:** 

**[7324.56s] English:** month and then taper over a couple of weeks many doctors prescribe them endlessly which is against  
**Translation:** 

**[7330.24s] English:** the protocol but it's common right and then something like 75 percent of people when they  
**Translation:** Vocabulary: endlessly: 无止尽地; prescribe: 开药

**[7336.96s] English:** taper it's you know half the people have difficulty but 75 percent get off okay 20 percent have severe  
**Translation:** 

**[7343.32s] English:** difficulty and five percent have life-threatening difficulty and if you're one of those it's really  
**Translation:** 

**[7348.80s] English:** bad and the stories that people have on this is heartbreaking and and tough so you put some of  
**Translation:** 

**[7355.54s] English:** the fault that the doctors they just not know what the hell they're doing oh no it's hard to say it's  
**Translation:** Vocabulary: heartbreaking: 令人心碎

**[7360.82s] English:** it's one of those commonly prescribed things like one doctor said what happens is if you're  
**Translation:** 

**[7366.40s] English:** prescribed them for a reason and then you have a hard time getting off the protocol basically says  
**Translation:** Vocabulary: prescribed: 医生开的药

**[7371.22s] English:** you're either crazy or dependent and you get kind of pushed into a different treatment regime you're  
**Translation:** 

**[7378.50s] English:** a drug  
**Translation:** 

**[7378.78s] English:** addict or a psychiatric patient and so like one doctor said you know i prescribed them for 10  
**Translation:** 

**[7384.96s] English:** years thinking i was helping my patients and i realized i was really harming them  
**Translation:** 

**[7388.22s] English:** and you know the the awareness of that is slowly coming up um the fact that they're casually  
**Translation:** 

**[7396.72s] English:** prescribed to people is horrible and it's bloody scary and some people are stable on them but  
**Translation:** Vocabulary: casually: 随意地

**[7405.08s] English:** they're on them for life like once you know it's another one of those drugs that  
**Translation:** 

**[7408.78s] English:** they're on but benzo's long range have real impacts on your personality people talk about  
**Translation:** 

**[7413.18s] English:** the benzo bubble where you get disassociated from reality and your friends a little bit  
**Translation:** 

**[7418.06s] English:** it's it's it's it's really terrible the mind is terrifying we're talking about how how the infinite  
**Translation:** Vocabulary: benzo: 苯并氮卓; disassociated: 脱离现实; terrifying: 恐怖的

**[7423.90s] English:** possibility of fun but like it's the infinite possibility of suffering too which is one of the  
**Translation:** 

**[7429.34s] English:** dangers of uh like expansion of the human mind it's like i wonder if all the possible human  
**Translation:** 

**[7437.26s] English:** experiences that it  
**Translation:** 

**[7438.78s] English:** it's like i wonder if all the possible human experiences that  
**Translation:** 

**[7440.00s] English:** computer can have is it mostly fun or is it mostly suffering so like if you if you uh brute force  
**Translation:** 

**[7448.10s] English:** expand the set of possibilities like are you going to run into some trouble in terms of like torture  
**Translation:** Vocabulary: brute: 粗暴

**[7455.08s] English:** and suffering and so on maybe our human brain is just protecting us from much more possible pain  
**Translation:** 

**[7461.02s] English:** and suffering maybe the space of pain is like much larger than we could possibly imagine and that the  
**Translation:** 

**[7468.26s] English:** world's in a balance you know all the all the literature on religion and stuff is you know the  
**Translation:** 

**[7474.66s] English:** struggle between good and evil is is balanced for very finely tuned for reasons that are complicated  
**Translation:** 

**[7480.58s] English:** but that's a that's a long philosophical conversation uh speaking of balance that's  
**Translation:** 

**[7485.90s] English:** complicated i i wonder because we're living through one of the more important moments in  
**Translation:** Vocabulary: philosophical: 哲学的

**[7490.92s] English:** human history with this particular virus it seems like pandemics have at least the ability to  
**Translation:** 

**[7498.26s] English:** kill off most of the human population at their worst and they're they're just fascinating because  
**Translation:** Vocabulary: pandemics: 大规模疫情

**[7504.36s] English:** there's so many viruses in this world there's so many i mean viruses basically around the world  
**Translation:** 

**[7508.46s] English:** in the sense that uh they've been around very long time they're everywhere they seem to be  
**Translation:** 

**[7514.28s] English:** extremely powerful and they're just in a distributed kind of way but at the same time  
**Translation:** 

**[7518.26s] English:** they're not intelligent and they're not even living do you have a like high level thoughts  
**Translation:** 

**[7522.76s] English:** about this virus that uh uh like in terms of you being fascinated or terrified or  
**Translation:** 

**[7528.26s] English:** someone between so i believe in frameworks right so like one of them is evolution  
**Translation:** Vocabulary: fascinated: 着迷

**[7535.04s] English:** like we're evolved creatures right yes and one of the things about evolution is it's hyper  
**Translation:** 

**[7541.58s] English:** competitive and it's not competitive out of a sense of evil it's competitive in the sense of  
**Translation:** Vocabulary: hyper: 过度的

**[7546.18s] English:** there's endless variation and variations that work better when and then over time there's so  
**Translation:** 

**[7552.24s] English:** many levels of that competition you know like multicellular life probably partly exists because  
**Translation:** 

**[7558.08s] English:** of  
**Translation:** 

**[7558.26s] English:** you know the  
**Translation:** 

**[7560.00s] English:** the competition between you know different kinds of life forms and we know sex partly exists to  
**Translation:** 

**[7565.68s] English:** scramble our genes so that we have you know genetic variation against the invasion of the  
**Translation:** Vocabulary: scramble: 打乱

**[7572.64s] English:** bacteria and the viruses and it's endless like i read some funny statistic like the density of  
**Translation:** 

**[7579.00s] English:** viruses and bacteria in the ocean is really high and one-third of the bacteria die every day because  
**Translation:** Vocabulary: bacteria: 细菌; density: 密度; statistic: 统计数据

**[7584.08s] English:** the viruses invaded them like one-third of them wow like like i don't know if that number is true  
**Translation:** 

**[7590.88s] English:** but it was like this like there's like the amount of competition and what's going on is stunning  
**Translation:** 

**[7596.08s] English:** and there's a theory as we age we slowly accumulate bacterias and viruses and as our  
**Translation:** 

**[7602.52s] English:** immune system kind of goes down you know that's what slowly kills us and it just feels so peaceful  
**Translation:** Vocabulary: accumulate: 积累; bacterias: 细菌; immune: 免疫系统

**[7608.88s] English:** from a human perspective when we sit back and are able to have a relaxed conversation  
**Translation:** 

**[7614.08s] English:** and and there's wars going on out there like right now you're you're harboring how many bacteria and  
**Translation:** Vocabulary: harboring: 携带

**[7620.98s] English:** you know the ones many of them are parasites on you and some of them are helpful and some of them  
**Translation:** 

**[7626.50s] English:** are modifying your behavior and some of them are you know it's just really it's really wild  
**Translation:** Vocabulary: modifying: 改变行为; parasites: 寄生虫

**[7631.20s] English:** but you know this particular manifestation is unusual you know in the demographic how it hit  
**Translation:** 

**[7638.28s] English:** and the political you know response that it engendered and you know the health care response  
**Translation:** Vocabulary: demographic: 人口统计; engendered: 引起; manifestation: 表现

**[7643.00s] English:** it engendered and uh  
**Translation:** 

**[7644.08s] English:** technology it's gendered it's kind of wild yeah the communication on twitter that it uh  
**Translation:** 

**[7649.66s] English:** every level all that kind of stuff at every single level yeah but but what usually kills  
**Translation:** 

**[7654.20s] English:** life the big extinctions are caused by um meteors and volcanoes that's the one you're worried about  
**Translation:** Vocabulary: extinctions: 物种灭绝; volcanoes: 火山

**[7660.66s] English:** as opposed to human created bombs that we uh solar flares are another good one can't you know  
**Translation:** 

**[7666.50s] English:** occasionally solar flares hit the planet so it's nature yeah it's all pretty wild  
**Translation:** Vocabulary: flares: 太阳flare

**[7674.08s] English:** another historic moment this is perhaps outside but perhaps within your uh  
**Translation:** 

**[7680.00s] English:** space of frameworks that you think about  
**Translation:** 

**[7683.16s] English:** that just happened I guess a couple  
**Translation:** 

**[7685.12s] English:** weeks ago is I don't know if you're  
**Translation:** 

**[7687.14s] English:** paying attention at all  
**Translation:** 

**[7688.02s] English:** the GameStop and  
**Translation:** 

**[7690.28s] English:** WallStreetBets  
**Translation:** 

**[7692.28s] English:** so it's  
**Translation:** 

**[7695.10s] English:** really fascinating there's kind of  
**Translation:** 

**[7697.10s] English:** a theme to this conversation we have today  
**Translation:** 

**[7698.76s] English:** because it's like neural networks  
**Translation:** 

**[7700.48s] English:** it's cool how  
**Translation:** 

**[7702.86s] English:** there's a large number of people  
**Translation:** 

**[7704.90s] English:** in a distributed way  
**Translation:** 

**[7706.16s] English:** almost having a kind of fun  
**Translation:** 

**[7709.24s] English:** were able to  
**Translation:** 

**[7710.96s] English:** take on the powerful elites  
**Translation:** 

**[7712.98s] English:** elite hedge  
**Translation:** 

**[7715.16s] English:** funds centralized powers  
**Translation:** 

**[7716.82s] English:** and overpower them  
**Translation:** 

**[7718.90s] English:** do you have  
**Translation:** 

**[7720.34s] English:** thoughts on this whole saga  
**Translation:** 

**[7722.46s] English:** I don't know enough about finance  
**Translation:** 

**[7724.90s] English:** but it was like the Elon  
**Translation:** 

**[7726.20s] English:** you know Robin Hood guy when they talked  
**Translation:** 

**[7729.12s] English:** yeah what did you think about that  
**Translation:** 

**[7730.48s] English:** well the Robin Hood guy didn't know how the  
**Translation:** 

**[7732.88s] English:** finance system worked that was clear  
**Translation:** 

**[7734.82s] English:** right he was treating like the  
**Translation:** 

**[7736.82s] English:** people who settled the transactions as a black  
**Translation:** 

**[7738.96s] English:** box and suddenly somebody called him up and  
**Translation:** 

**[7741.38s] English:** say hey black box calling you your  
**Translation:** 

**[7743.68s] English:** transaction volume means you need to put  
**Translation:** 

**[7745.38s] English:** out three billion dollars right now and  
**Translation:** 

**[7746.94s] English:** he's like I don't have three billion  
**Translation:** 

**[7747.84s] English:** dollars like I don't even make any money  
**Translation:** 

**[7749.88s] English:** on these trades why do I owe three  
**Translation:** 

**[7751.12s] English:** billion dollars while you're sponsoring  
**Translation:** Vocabulary: sponsoring: 赞助

**[7752.30s] English:** the trade so so there was a set of  
**Translation:** 

**[7754.60s] English:** abstractions that you know I don't think  
**Translation:** 

**[7757.34s] English:** either like like now we understand it  
**Translation:** 

**[7759.40s] English:** like this happens in chip design like  
**Translation:** 

**[7761.24s] English:** you buy wafers from TSMC or Samsung or  
**Translation:** 

**[7764.50s] English:** Intel and you know they say it works  
**Translation:** Vocabulary: wafers: 晶圆

**[7766.84s] English:** like this and you do your design based on  
**Translation:** 

**[7768.68s] English:** that and then chip comes back and  
**Translation:** 

**[7770.06s] English:** doesn't work and then suddenly you  
**Translation:** 

**[7771.98s] English:** started having to open the black boxes  
**Translation:** 

**[7773.66s] English:** the transistors really work like they  
**Translation:** 

**[7775.68s] English:** said you know what's the real issue so  
**Translation:** Vocabulary: transistors: 晶体管

**[7778.48s] English:** so the there's a whole set of things  
**Translation:** 

**[7783.08s] English:** that created this opportunity and  
**Translation:** 

**[7785.00s] English:** somebody spotted it now people spot  
**Translation:** 

**[7787.88s] English:** these kinds of opportunities all the  
**Translation:** 

**[7789.50s] English:** times there's been flash crashes there  
**Translation:** 

**[7791.48s] English:** has been you know there's always short  
**Translation:** 

**[7793.44s] English:** squeezes are fairly regular every CEO I  
**Translation:** 

**[7796.10s] English:** know hates the shorts  
**Translation:** Vocabulary: squeezes: 挤压

**[7798.14s] English:** mm-hmm  
**Translation:** 

**[7798.64s] English:** because they're they're manipulating  
**Translation:** Vocabulary: manipulating: 操控

**[7800.00s] English:** They're trying to manipulate their stock in a way that they make money and, you know, deprive value from both, you know, the company and the investors.  
**Translation:** 

**[7808.90s] English:** So the fact that, you know, some of these stocks were so short, it's hilarious, that this hasn't happened before.  
**Translation:** Vocabulary: manipulate: 操控

**[7817.30s] English:** I don't know why.  
**Translation:** 

**[7817.90s] English:** And I don't actually know why some serious hedge funds didn't do it to other hedge funds.  
**Translation:** 

**[7823.34s] English:** And some of the hedge funds actually made a lot of money on this.  
**Translation:** 

**[7826.30s] English:** Yes.  
**Translation:** 

**[7826.38s] English:** So my guess is we know 5% of what really happened and that a lot of the players don't know what happened.  
**Translation:** 

**[7834.80s] English:** And the people who probably made the most money aren't the people that they're talking about.  
**Translation:** 

**[7839.56s] English:** Yeah.  
**Translation:** 

**[7840.60s] English:** Do you think there was something – I mean, this is the cool kind of Elon, you're the same kind of conversationalist, which is like first principles questions of like what the hell happened.  
**Translation:** Vocabulary: conversationalist: 谈话者

**[7855.96s] English:** Just.  
**Translation:** 

**[7856.38s] English:** Just very basic questions of like was there something shady going on?  
**Translation:** Vocabulary: shady: 可疑的

**[7860.88s] English:** What, you know, who are the parties involved?  
**Translation:** 

**[7863.64s] English:** It's the basic questions that everybody wants to know about.  
**Translation:** 

**[7866.28s] English:** Yeah.  
**Translation:** 

**[7866.48s] English:** So, like, we're in a very hyper-competitive world, right?  
**Translation:** 

**[7870.18s] English:** But transactions like buying and selling stock is a trust event.  
**Translation:** 

**[7873.34s] English:** You know, I trust the company represented themselves properly.  
**Translation:** 

**[7876.22s] English:** You know, I bought the stock because I think it's going to go up.  
**Translation:** 

**[7879.44s] English:** I trust that the regulations are solid.  
**Translation:** 

**[7882.40s] English:** Now, inside of that, there's all kinds of places.  
**Translation:** 

**[7886.38s] English:** You know, humans over-trust.  
**Translation:** 

**[7888.84s] English:** And, you know, this exposed, let's say, some weak points in the system.  
**Translation:** 

**[7894.24s] English:** I don't know if it's going to get corrected.  
**Translation:** 

**[7897.32s] English:** I don't know if we have close to the real story.  
**Translation:** 

**[7901.82s] English:** My suspicion is we don't.  
**Translation:** 

**[7904.40s] English:** And listen to that guy.  
**Translation:** 

**[7905.74s] English:** He was like a little wide-eyed about it.  
**Translation:** 

**[7907.52s] English:** And then he did this.  
**Translation:** 

**[7908.28s] English:** And then he did that.  
**Translation:** 

**[7909.04s] English:** And I was like, I think you should know more about your business than that.  
**Translation:** 

**[7913.96s] English:** But, again, there's many businesses.  
**Translation:** 

**[7915.96s] English:** When.  
**Translation:** 

**[7916.52s] English:** Like this layer is really stable.  
**Translation:** 

**[7918.44s] English:** You stop paying attention to it.  
**Translation:** 

**[7920.00s] English:** mm-hmm you pay attention to the stuff that's bugging you or new mm-hmm you  
**Translation:** 

**[7924.56s] English:** don't pay attention to the stuff that just seems to work all the time you just  
**Translation:** 

**[7927.28s] English:** you know sky's blue every day California and we're what's wall things you know it  
**Translation:** Vocabulary: california: 加利福尼亚

**[7932.36s] English:** rains there was like we do somebody go bring in the lawn furniture you know  
**Translation:** 

**[7937.46s] English:** like it's getting wet you don't know it's getting wet yeah it does I was blue  
**Translation:** 

**[7940.82s] English:** for 100 days and now it's you know so but part of the problem here with Vlad  
**Translation:** 

**[7946.40s] English:** this the CEO Robin Hood is the scaling is that we've been talking about is  
**Translation:** 

**[7951.04s] English:** there's a lot of yeah unexpected things that happen with the scaling and you  
**Translation:** 

**[7956.28s] English:** have to be I think the scaling forces you to then return to the fundamentals  
**Translation:** Vocabulary: fundamentals: 基础原理

**[7961.28s] English:** well it's interesting because when you buy and sell stocks the scaling is you  
**Translation:** 

**[7965.30s] English:** know the stocks to only move in a certain range and if you buy a stock you  
**Translation:** 

**[7968.28s] English:** can only lose that amount of money on the short short market you can lose a  
**Translation:** 

**[7971.84s] English:** lot more than you can benefit like it has oh it has a weird cause you know  
**Translation:** 

**[7976.38s] English:** cost function or whatever the right word for that is so he was trading in a  
**Translation:** 

**[7980.40s] English:** market where he wasn't actually capitalized for the downside if it got  
**Translation:** Vocabulary: capitalized: 融资; downside: 风险

**[7984.66s] English:** outside a certain range now whether something nefarious has happened I have  
**Translation:** 

**[7989.94s] English:** no idea but at some point the financial risk to both him and his customers was  
**Translation:** Vocabulary: nefarious: 不法的

**[7996.66s] English:** way outside of his financial capacity and his understanding how the system  
**Translation:** 

**[8000.56s] English:** work was clearly weak or or he didn't represent himself I you know I don't  
**Translation:** 

**[8005.60s] English:** know the person  
**Translation:** 

**[8006.22s] English:** there's when I listen to him Nick yeah it could have been the surprise question  
**Translation:** 

**[8010.06s] English:** was like and then these guys called and you know it sounded like he was treating  
**Translation:** 

**[8014.56s] English:** stuff as a black box maybe he shouldn't have but maybe his whole pile of experts  
**Translation:** 

**[8018.88s] English:** somewhere else and it was going on I don't know yep I mean this is this is  
**Translation:** 

**[8024.32s] English:** one of the qualities of a good leader is under fire you have to perform and that  
**Translation:** 

**[8029.44s] English:** means to think clearly and to speak clearly and he dropped the ball on those  
**Translation:** 

**[8034.82s] English:** things because  
**Translation:** 

**[8036.22s] English:** and understand the problem quickly learn and understand the problem like  
**Translation:** 

**[8040.00s] English:** at this like basic level like what the hell happened and my guess is you know at some level  
**Translation:** 

**[8048.40s] English:** it was amateurs trading against you know experts slash insiders slash people with you know special  
**Translation:** 

**[8053.86s] English:** information outsiders versus insiders yeah and the insiders you know my guess is the next time  
**Translation:** Vocabulary: amateurs: 业余人士; insiders: 内部人员; outsiders: 外部人员

**[8060.60s] English:** this happens we'll make money on it the insiders always win well well they have more tools and  
**Translation:** 

**[8066.54s] English:** more incentive i mean this always happens like the outsiders are doing this for fun the insiders  
**Translation:** 

**[8071.24s] English:** are doing this 24 7 but there's numbers in the outsiders this is the interesting thing well  
**Translation:** 

**[8077.02s] English:** there's numbers on the insiders too like different kind of numbers different kind of numbers  
**Translation:** 

**[8082.84s] English:** but this could be a new era because i don't know at least i didn't expect that  
**Translation:** 

**[8087.40s] English:** a bunch of redditors could you know there's uh you know millions of people can get surprised  
**Translation:** Vocabulary: redditors: Reddit用户

**[8091.80s] English:** attack the next one will be a surprise but don't you think the the the crowd the  
**Translation:** 

**[8096.52s] English:** people are planning the next attack we'll see but it has to be a surprise can't be the same game  
**Translation:** 

**[8102.36s] English:** as to the like it could be there's a very large number of games to play and they can be  
**Translation:** 

**[8109.56s] English:** agile about it i don't know i'm not an expert right that's a good question how the space of  
**Translation:** Vocabulary: agile: 灵活

**[8114.40s] English:** games how how restricted is it yeah and the system is so complicated it could be relatively  
**Translation:** 

**[8120.86s] English:** unrestricted and also like you know during the last couple financial crashes you know what set  
**Translation:** Vocabulary: unrestricted: 自由度高

**[8127.58s] English:** it off was you know sets of derivative events where you know you know nassim talib's you know  
**Translation:** 

**[8133.86s] English:** thing is they're they're they're trying to lower volatility in the short run by creating tail  
**Translation:** Vocabulary: derivative: 派生事件; volatility: 波动性

**[8140.18s] English:** events and systems always evolve towards that and then they always crash like the s curve is the  
**Translation:** 

**[8146.64s] English:** you know star low ramp plateau crash  
**Translation:** Vocabulary: plateau: 平台期

**[8150.72s] English:** you  
**Translation:** 

**[8150.86s] English:** it's 100 effective in the long run let me ask you some advice to put on your profound hat  
**Translation:** Vocabulary: profound: 深奥的

**[8160.00s] English:** what uh there's a bunch of young folks who listen to this thing for no good reason whatsoever  
**Translation:** 

**[8166.42s] English:** undergraduate students maybe high school students maybe just young folks young at heart uh looking  
**Translation:** Vocabulary: undergraduate: 本科生; whatsoever: 无论如何

**[8173.26s] English:** for uh the next steps to take in life what advice would you give to a young person today about life  
**Translation:** 

**[8180.18s] English:** maybe career but also life in general get good at some stuff well get to know yourself right  
**Translation:** 

**[8187.44s] English:** get good at something that you're actually interested in you have to love what you're  
**Translation:** 

**[8191.58s] English:** doing to get good at it you really got to find that don't waste all your time doing stuff that's  
**Translation:** 

**[8195.94s] English:** just boring or bland or numbing right don't let old people screw you  
**Translation:** 

**[8202.12s] English:** well people get talked into doing all kinds of shit and racking up huge student you know  
**Translation:** Vocabulary: bland: 平淡; numbing: 麻木

**[8208.38s] English:** student debts and like there's so much crap going on you know and that drains your time and drains  
**Translation:** 

**[8214.48s] English:** you know the eric weinstein you know thesis that you know the old  
**Translation:** Vocabulary: weinstein: 埃里克·温斯莱特

**[8217.44s] English:** generation won't let go yeah they're trapping all the young people i think there's some truth to  
**Translation:** 

**[8222.04s] English:** that yeah sure just because you're old doesn't mean you stop thinking i know lots of really  
**Translation:** 

**[8227.82s] English:** original yeah old people i'm an old person so um but you have to be conscious about it you can fall  
**Translation:** 

**[8236.20s] English:** into the ruts and then do that you know when i hear young people spouting opinions that sounds  
**Translation:** Vocabulary: spouting: 发表

**[8242.36s] English:** like they come from fox news or cnn i think they've been captured by groupthink and memes and  
**Translation:** 

**[8247.44s] English:** i suppose to think on their own you know so if you find yourself repeating what everybody else is  
**Translation:** Vocabulary: groupthink: 团体思维

**[8252.16s] English:** saying you're not going to have a good life like like that's not how the world works and maybe  
**Translation:** 

**[8257.96s] English:** it seems safe but it puts you at great jeopardy for well being boring or unhappy or how long did  
**Translation:** Vocabulary: jeopardy: 危险

**[8266.30s] English:** it take you to find the thing that um you have fun with oh i don't know i've been a fun person  
**Translation:** 

**[8272.94s] English:** since i was pretty little so everything i've gone through a couple periods of depression in my life  
**Translation:** 

**[8277.44s] English:** for a good reason or for uh the reason  
**Translation:** 

**[8280.00s] English:** that doesn't make any sense yeah like some some things are hard like you go through mental  
**Translation:** 

**[8286.96s] English:** transitions in high school i was depressed really depressed for a year and i think i had my first  
**Translation:** 

**[8292.72s] English:** midlife crisis at 26. i kind of thought is this all there is like i was working at a job that i  
**Translation:** Vocabulary: midlife: 中年; transitions: 转变

**[8298.56s] English:** loved and but i was going to work and all my time was consumed what's what's the escape out of that  
**Translation:** 

**[8305.12s] English:** depression what's the answer to is is this all there is well a friend of mine i asked him because  
**Translation:** 

**[8311.76s] English:** he was working his ass off i said what's your work-life balance like like there's you know work  
**Translation:** 

**[8317.12s] English:** friends family personal time are you balancing in that and he said work eighty percent family  
**Translation:** Vocabulary: balancing: 平衡

**[8322.80s] English:** twenty percent and i try to i try to find some time to sleep like there's no personal time  
**Translation:** 

**[8329.04s] English:** there's no passionate time like he's you know young people are often passionate about work  
**Translation:** 

**[8334.48s] English:** so not  
**Translation:** 

**[8335.12s] English:** certainly like that but you need to you need to have some space in your life for different things  
**Translation:** 

**[8341.68s] English:** and that's that creates uh that makes you resistant to the whole the the the dip  
**Translation:** 

**[8348.40s] English:** the the deep dips into depression kind of thing yeah well you have to get to know yourself too  
**Translation:** 

**[8352.88s] English:** meditation helps some physical something physically intense helps like the weird  
**Translation:** 

**[8359.84s] English:** places your mind goes kind of thing like and why does it happen why do you do what you do like  
**Translation:** 

**[8364.96s] English:** true  
**Translation:** 

**[8365.12s] English:** triggers like the things that cause your mind to go to different places kind of thing or  
**Translation:** 

**[8370.80s] English:** like events like your upbringing for better or worse whether your parents are great people or not  
**Translation:** 

**[8375.60s] English:** you you you come into you know adulthood with all kinds of emotional burdens yeah and you can  
**Translation:** Vocabulary: upbringing: 教育背景

**[8383.28s] English:** see some people are so bloody stiff and restrained and they think you know the world's fundamentally  
**Translation:** 

**[8387.60s] English:** negative like you maybe that you have unexplored territory yeah or you're afraid of something  
**Translation:** Vocabulary: fundamentally: 根本上; restrained: 拘谨; unexplored: 未开发

**[8395.12s] English:** uh definitely afraid of quite a few things then you gotta go face them  
**Translation:** 

**[8400.00s] English:** like what's the worst thing that can happen you're gonna die right like that's inevitable  
**Translation:** 

**[8405.90s] English:** you might as well get over that like a hundred percent that's right like people are worried  
**Translation:** 

**[8410.34s] English:** about the virus but you know the human condition is pretty deadly there's something about  
**Translation:** 

**[8415.22s] English:** embarrassment that's i've competed a lot in my life and i think the if i'm too introspective  
**Translation:** 

**[8421.90s] English:** the thing i'm most afraid of is being like humiliated i think nobody cares about that  
**Translation:** Vocabulary: humiliated: 羞辱; introspective: 内省

**[8427.96s] English:** look you're the only person on the planet that cares about you being humiliated so it's  
**Translation:** 

**[8432.64s] English:** a really useless thought it is it's like uh you're all humiliated something happened in  
**Translation:** 

**[8440.26s] English:** a room full of people and they walk out and they didn't think about it one more second  
**Translation:** 

**[8443.74s] English:** or maybe somebody told a funny story to somebody else and then it dissipates it throughout  
**Translation:** Vocabulary: dissipates: 消散

**[8447.42s] English:** yeah that's yeah no i know it too i mean i've been really embarrassed about that nobody  
**Translation:** 

**[8453.66s] English:** cared about myself yeah it's a funny thing so the worst thing  
**Translation:** 

**[8457.74s] English:** all time  
**Translation:** 

**[8457.96s] English:** is just uh yeah but that's a cage and then you have to get out of it yeah like once you here's  
**Translation:** 

**[8463.52s] English:** the thing once you find something like that you have to be determined to break it because  
**Translation:** 

**[8469.12s] English:** otherwise you'll just you know so you accumulate that kind of junk and then you die as a you know  
**Translation:** Vocabulary: accumulate: 积攒

**[8473.78s] English:** a mess so the goal i guess it's always it's like a cage within a cage i guess the goal is to die  
**Translation:** 

**[8479.42s] English:** in the biggest possible cage well ideally you'd have no cage well you know people do get enlightened  
**Translation:** Vocabulary: enlightened: 觉悟

**[8486.28s] English:** i've got a few it's great  
**Translation:** 

**[8487.96s] English:** you found a few there's a few out there i don't know of course sir all right I either outreach  
**Translation:** 

**[8493.64s] English:** middle school dog or the gang leader Nothing fun nothing honest you're out there going  
**Translation:** 

**[8494.64s] English:** either that or you know it's  
**Translation:** 

**[8495.50s] English:** a great sales pitch there's like enlightened people write books and doing all kinds of  
**Translation:** 

**[8497.74s] English:** stuff it's a good way to solve book i'll give you that you've never met somebody you this  
**Translation:** 

**[8502.24s] English:** thought they just kill me like there's like mental clarity humor no 100% but i just feel  
**Translation:** 

**[8509.32s] English:** like they're living in a bigger cage they have their own there  
**Translation:** 

**[8512.02s] English:** You still think there's a cage?  
**Translation:** 

**[8513.64s] English:** There's still a cage?  
**Translation:** 

**[8515.44s] English:** …you secretly suspect there's always a cage?  
**Translation:** 

**[8517.16s] English:** There's nothing outside the universe.  
**Translation:** 

**[8520.00s] English:** outside the cage uh you were you were you worked in a bunch of companies uh you led a lot of amazing  
**Translation:** 

**[8531.74s] English:** teams um i don't i'm not sure if you've ever been like at the early stages of a startup  
**Translation:** 

**[8538.50s] English:** but do you have advice for uh somebody that wants to uh do a startup or build a company  
**Translation:** 

**[8547.70s] English:** like build a strong team of engineers that are passionate just want to  
**Translation:** 

**[8551.86s] English:** solve a big problem like is there uh more specifically on that point  
**Translation:** 

**[8558.10s] English:** you have to be really good at stuff if you're going to lead and build a team you better be  
**Translation:** 

**[8563.80s] English:** really interested in how people work and think the people or the solution to the problem so  
**Translation:** 

**[8569.16s] English:** there's two things right one is how people work and the other is actually there's there's quite  
**Translation:** 

**[8574.32s] English:** a few successful startups it's pretty clear the founders don't know anything about people  
**Translation:** 

**[8577.70s] English:** like the idea was so powerful that it propelled them but i suspect somewhere early they they  
**Translation:** Vocabulary: founders: 创业者的; propelled: 推动; startups: 初创公司

**[8584.24s] English:** hired some people who understood people because people really need a lot of care and feeding to  
**Translation:** 

**[8589.04s] English:** collaborate and work together and feel engaged and work hard you know like startups are all about  
**Translation:** Vocabulary: collaborate: 合作

**[8595.00s] English:** outproducing other people like you're nimble because you don't have any legacy you don't have  
**Translation:** 

**[8600.52s] English:** you know a bunch of people who are depressed about life you know just showing up you know  
**Translation:** Vocabulary: nimble: 灵活; outproducing: 超越生产

**[8605.72s] English:** so startups have a lot of advantages that way  
**Translation:** 

**[8607.70s] English:** you know do you like the steve jobs talked about this idea of a players and b players i don't know  
**Translation:** 

**[8615.18s] English:** if you uh know this formulation yeah no um the organizations that get taken over by b player  
**Translation:** 

**[8622.52s] English:** leaders often really underperform their heresy players that said in big organizations there's  
**Translation:** Vocabulary: heresy: 异端; underperform: 表现差

**[8630.90s] English:** so much work to do like and there's so many people who are happy to do what you know like  
**Translation:** 

**[8635.08s] English:** the leadership or the big idea people who can see the big idea people who can see the big idea people  
**Translation:** 

**[8637.70s] English:** who can see the big idea people who can see the big idea people consider menial jobs  
**Translation:** 

**[8640.00s] English:** And, you know, you need a place for them, but you need an organization that both values and rewards them, but doesn't let them take over the leadership of it.  
**Translation:** 

**[8648.64s] English:** Got it.  
**Translation:** 

**[8648.96s] English:** But so you need to have an organization that's resistant to that.  
**Translation:** Vocabulary: resistant: 抵抗力强的

**[8651.98s] English:** But in the early days, the notion with Steve was that like one B player in a room of A players will be like destructive to the whole.  
**Translation:** 

**[8662.92s] English:** I've seen that happen.  
**Translation:** 

**[8664.28s] English:** I don't know if it's like always true.  
**Translation:** 

**[8666.28s] English:** Like, you know, you run into people who are clearly B players, but they think they're A players.  
**Translation:** 

**[8671.52s] English:** And so they have a loud voice at the table and they make lots of demands for that.  
**Translation:** 

**[8675.02s] English:** But there's other people who are like, I know who I am.  
**Translation:** 

**[8677.38s] English:** I just want to work with, you know, cool people on cool shit and just tell me what to do and I'll go get it done.  
**Translation:** 

**[8682.20s] English:** You know, so you have to, again, this is like people skills, like what kind of person is it?  
**Translation:** 

**[8687.26s] English:** You know, I've met some really great people I love working with that weren't the biggest ID people, the most productive ever, but they show up, they get it done.  
**Translation:** 

**[8695.82s] English:** You know.  
**Translation:** 

**[8696.28s] English:** They create connection and community that people value.  
**Translation:** 

**[8700.02s] English:** It's pretty diverse.  
**Translation:** 

**[8701.96s] English:** I don't think there's a recipe for that.  
**Translation:** 

**[8704.80s] English:** I got to ask you about love.  
**Translation:** 

**[8706.84s] English:** I heard you're into this now.  
**Translation:** 

**[8708.64s] English:** Into this love thing?  
**Translation:** 

**[8709.48s] English:** Yeah.  
**Translation:** 

**[8710.14s] English:** Do you think this is your solution to your depression?  
**Translation:** 

**[8713.22s] English:** No, I'm just trying to, like you said, delight in people on occasion, trying to sell a book.  
**Translation:** 

**[8716.92s] English:** I'm writing a book about love.  
**Translation:** 

**[8718.06s] English:** You're writing a book about love?  
**Translation:** 

**[8718.88s] English:** No, I'm not.  
**Translation:** 

**[8719.98s] English:** I'm not.  
**Translation:** 

**[8720.32s] English:** A friend of mine, he's going to tell me, he said,  
**Translation:** 

**[8726.10s] English:** you should really write a book about your management philosophy.  
**Translation:** 

**[8729.16s] English:** He said, it'd be a short book.  
**Translation:** 

**[8734.78s] English:** Well, that one was sold pretty well.  
**Translation:** 

**[8737.78s] English:** What role do you think love, family, friendship, all that kind of human stuff play in a successful life?  
**Translation:** 

**[8744.32s] English:** You've been exceptionally successful in the space of running teams, building cool shit in this world, creating some amazing things.  
**Translation:** 

**[8753.28s] English:** Did love get in the way?  
**Translation:** Vocabulary: exceptionally: 非常

**[8754.74s] English:** Did love help?  
**Translation:** 

**[8756.10s] English:** Did family get in the way?  
**Translation:** 

**[8757.72s] English:** Did family help?  
**Translation:** 

**[8759.16s] English:** Friendship?  
**Translation:** 

**[8759.78s] English:** You want to?  
**Translation:** 

**[8760.00s] English:** engineers answer please so like first love is functional right it's functional in what way  
**Translation:** 

**[8766.88s] English:** so we habituate ourselves to the environment and actually jordan told me jordan peterson told me  
**Translation:** 

**[8772.84s] English:** this line so you go through life and you just get used to everything except for the things you love  
**Translation:** Vocabulary: habituate: 习惯

**[8777.50s] English:** they they remain new like this is really useful for you know like like other people's children  
**Translation:** 

**[8784.00s] English:** and dogs and you know trees you just don't pay that much attention to your own kids you're  
**Translation:** 

**[8788.80s] English:** monitoring them really closely like and if they go off a little bit because you love them if you're  
**Translation:** 

**[8794.16s] English:** smart if you're going to be a successful parent you notice it right away you don't habituate  
**Translation:** 

**[8800.00s] English:** to just things you love and if you want to be successful at work if you don't love it  
**Translation:** 

**[8806.88s] English:** you're not going to put the time in somebody else it's somebody else that loves it like  
**Translation:** 

**[8811.80s] English:** because it's new and interesting and that lets you go to the next level  
**Translation:** 

**[8815.76s] English:** so it's the thing it's just a  
**Translation:** 

**[8818.80s] English:** function that generates newness and novelty and uh surprises you know those guys it's really  
**Translation:** 

**[8825.00s] English:** interesting right and there's people figured out lots of you know frameworks for this you know like  
**Translation:** 

**[8830.08s] English:** like humans seem to go in partnership go through you know interest like somebody suddenly somebody's  
**Translation:** 

**[8835.30s] English:** interesting and then you're infatuated with them and then you're in love with them and then you  
**Translation:** Vocabulary: infatuated: 一见钟情

**[8840.60s] English:** you know different people have ideas about parental love or mature love like you go through  
**Translation:** 

**[8845.08s] English:** a cycle of that which keeps us together and it's you know  
**Translation:** 

**[8848.80s] English:** super functional for creating families and and creating communities and making you support  
**Translation:** 

**[8854.10s] English:** somebody despite the fact that you don't love them like and and it can be really enriching  
**Translation:** Vocabulary: enriching: 充实的

**[8862.52s] English:** you know now now in the work-life balance scheme if all you do is work you think you  
**Translation:** 

**[8870.18s] English:** may be optimizing your work potential but if you don't love your work or you don't have  
**Translation:** Vocabulary: optimizing: 最大化

**[8876.20s] English:** family and friends and things you care about  
**Translation:** 

**[8878.80s] English:** your brain is  
**Translation:** 

**[8880.00s] English:** well balanced like everybody knows the experience of you works on something all week you went home  
**Translation:** 

**[8885.12s] English:** and took two days off and you came back in the odds of you working on the thing you picking  
**Translation:** 

**[8890.24s] English:** up right where you left off is zero your brain refactored it but being in love is great it's  
**Translation:** 

**[8899.20s] English:** like changes the color of the light in the room it creates a spaciousness that's that's different  
**Translation:** Vocabulary: refactored: 重组; spaciousness: 宽敞感

**[8905.44s] English:** it helps you think it makes you strong bukowski had this line about love being a fog that  
**Translation:** 

**[8912.48s] English:** dissipates with the first light of reality in the morning that's that's depressing i think it's the  
**Translation:** Vocabulary: bukowski: Bukowski; dissipates: 消散

**[8918.32s] English:** other way around it lasts well you like you said it's a function it's a thing that generally be  
**Translation:** 

**[8923.12s] English:** the light that actually enlivens your world and creates the interest and the power and the  
**Translation:** Vocabulary: enlivens: 使生动

**[8927.84s] English:** strengths and the to go do something well it's like like that sounds like you know there's like  
**Translation:** 

**[8934.72s] English:** physical level  
**Translation:** 

**[8935.44s] English:** emotional love intellectual love spiritual yeah right isn't it all the same thing kind of nope  
**Translation:** 

**[8940.96s] English:** you should differentiate that maybe that's your problem in your book you should you should refine  
**Translation:** Vocabulary: differentiate: 区分; refine: 精炼

**[8945.52s] English:** that a little bit different chapters yeah there's different chapters what's that what's these are  
**Translation:** 

**[8949.92s] English:** aren't these just different layers of the same thing or the stack uh physical people people some  
**Translation:** 

**[8955.76s] English:** people are addicted to physical love and they have no idea about emotional or intellectual love  
**Translation:** 

**[8961.68s] English:** i don't know if they're the same things i think they're different that's true they could be  
**Translation:** 

**[8964.80s] English:** different  
**Translation:** 

**[8965.44s] English:** it'd be it i guess the ultimate goal is for it to be the same well if you want something to be bigger  
**Translation:** 

**[8969.36s] English:** and interesting you should find all its components and differentiate them not cloning together  
**Translation:** 

**[8974.32s] English:** like people do this all the time they yeah the modularity get your abstraction layers right and  
**Translation:** Vocabulary: abstraction: 抽象层; modularity: 模块化

**[8979.44s] English:** then you can you have room to breathe well maybe you can write the forward to my book about love  
**Translation:** 

**[8984.64s] English:** or the afterwards you really tried i feel like lex has made a lot of progress in this book  
**Translation:** 

**[8993.36s] English:** uh well you have things in your life that you love  
**Translation:** 

**[8995.28s] English:** yeah yeah you know so and they are you're right they're modular it's  
**Translation:** Vocabulary: modular: 模块化的

**[9000.00s] English:** it's quite well there and you can have multiple things with the same person or the same thing and  
**Translation:** 

**[9005.92s] English:** yeah but yeah depending on the moment of the day yeah there's like what pokoski described  
**Translation:** 

**[9012.96s] English:** is that moment you go from being in love to having a different kind of love yeah right  
**Translation:** 

**[9018.16s] English:** and that's the transition but when it happens if you read the owner's manual and you believed it  
**Translation:** 

**[9022.64s] English:** you would have said oh this happened it doesn't mean it's not love it's a different kind of love  
**Translation:** 

**[9027.36s] English:** but but maybe there's something better about that as you grow old if all you do is regret how you  
**Translation:** 

**[9035.92s] English:** used to be it's sad right you should have learned a lot of things because like who you can be in  
**Translation:** 

**[9042.32s] English:** your future self is actually more interesting and possibly delightful than you know being a mad kid  
**Translation:** 

**[9049.36s] English:** in love with the the next person like that's super fun when it happens but that's that's  
**Translation:** 

**[9056.80s] English:** you know  
**Translation:** 

**[9057.36s] English:** five percent of the possibility yeah that's right there's a lot more fun to be had in the  
**Translation:** 

**[9064.04s] English:** long lasting stuff yeah or meaning you know if that's thing which is a kind of fun it's a deeper  
**Translation:** 

**[9069.72s] English:** kind of fun and it's surprising you know that's like like the thing i like is surprises you know  
**Translation:** 

**[9076.52s] English:** and you just never know what's going to happen yeah but you have to look carefully you have to  
**Translation:** 

**[9080.76s] English:** work at it you have to think about it yeah yeah you have to see the surprises when they happen  
**Translation:** 

**[9086.12s] English:** right you have to be looking for all kinds of different honzing in your life you have to focus  
**Translation:** 

**[9086.80s] English:** on all kinds of things because you're not gonna go out before you kind of watch the pulling you'll  
**Translation:** 

**[9087.32s] English:** boy from the branching perspective you mentioned regrets uh do you have regrets about your own  
**Translation:** 

**[9095.34s] English:** trajectory oh yeah of course yeah some of it's painful but you want to hear the painful stuff  
**Translation:** 

**[9101.00s] English:** i'd say like in terms of working with people when people did stuff i didn't like especially  
**Translation:** 

**[9109.02s] English:** if it was a bit nefarious i took it personally and i also felt it was personal about them  
**Translation:** 

**[9114.96s] English:** but a lot of times like humans are you know most humans are a mess right and then  
**Translation:** Vocabulary: nefarious: 不法的

**[9120.00s] English:** And they act out and they do stuff.  
**Translation:** 

**[9122.20s] English:** And the psychologist I heard a long time ago said, you tend to think somebody does something to you.  
**Translation:** 

**[9128.84s] English:** But really what they're doing is they're doing what they're doing while they're in front of you.  
**Translation:** 

**[9133.10s] English:** It's not that much about you.  
**Translation:** 

**[9135.36s] English:** Yeah.  
**Translation:** 

**[9135.74s] English:** Right.  
**Translation:** 

**[9135.98s] English:** And as I got more interested and, you know, when I work with people, I think about them and probably analyze them and understand them a little bit.  
**Translation:** 

**[9146.60s] English:** And then when they do stuff, I'm way less surprised.  
**Translation:** 

**[9148.86s] English:** And I'm way, you know, and if it's bad, I'm way less hurt.  
**Translation:** 

**[9152.00s] English:** And I react way less.  
**Translation:** 

**[9153.94s] English:** Like, I sort of expect everybody's got their shit.  
**Translation:** 

**[9157.20s] English:** Yeah.  
**Translation:** 

**[9157.48s] English:** And it's not about you as much.  
**Translation:** 

**[9159.10s] English:** It's not about me that much.  
**Translation:** 

**[9160.72s] English:** It's like, you know, you do something and you think you're embarrassed, but nobody cares.  
**Translation:** 

**[9165.08s] English:** Like, and somebody's really mad at you.  
**Translation:** 

**[9166.82s] English:** The odds of it being about you.  
**Translation:** 

**[9169.42s] English:** No, they're getting mad the way they're doing that because of some pattern they learned.  
**Translation:** 

**[9173.24s] English:** And, you know, and maybe you can help them if you care enough about it.  
**Translation:** 

**[9176.70s] English:** Or you could see it coming instead.  
**Translation:** 

**[9178.86s] English:** Like, I wish I was way better at that.  
**Translation:** 

**[9182.62s] English:** I'm a bit of a hothead.  
**Translation:** Vocabulary: hothead: 易怒之人

**[9184.94s] English:** You regret that?  
**Translation:** 

**[9185.98s] English:** You said with Steve that was a feature, not a bug.  
**Translation:** 

**[9188.86s] English:** Yeah.  
**Translation:** 

**[9189.20s] English:** Well, he was using it as the counterforce to orderliness that would crush his orderliness.  
**Translation:** Vocabulary: counterforce: 制衡力量; orderliness: 条理性

**[9193.40s] English:** Well, you were doing the same.  
**Translation:** 

**[9195.08s] English:** Eh, maybe.  
**Translation:** 

**[9195.94s] English:** I don't think my vision was big enough.  
**Translation:** 

**[9198.90s] English:** It was more like I just got pissed off and did stuff.  
**Translation:** Vocabulary: pissed: 生气

**[9203.80s] English:** I'm sure that's what Steve.  
**Translation:** 

**[9205.30s] English:** Yeah.  
**Translation:** 

**[9206.00s] English:** You're telling.  
**Translation:** 

**[9206.70s] English:** I don't know if it had the.  
**Translation:** 

**[9208.86s] English:** It didn't have the amazing effect of creating the trillion dollar company.  
**Translation:** 

**[9212.36s] English:** It was more like I just got pissed off and left and or made enemies that he shouldn't have.  
**Translation:** Vocabulary: trillion: 万亿

**[9218.32s] English:** And yeah, it's hard.  
**Translation:** 

**[9220.44s] English:** Like, I didn't really understand politics until I worked at Apple, where, you know, Steve was a master player of politics and his staff had to be, or they wouldn't survive him.  
**Translation:** 

**[9228.78s] English:** And it was definitely part of the culture.  
**Translation:** 

**[9231.36s] English:** And then I've been in companies where they say it's political, but it's all, you know, fun and games compared to Apple.  
**Translation:** 

**[9236.90s] English:** And it's not that.  
**Translation:** 

**[9238.48s] English:** The.  
**Translation:** 

**[9238.70s] English:** The people at Apple are bad people.  
**Translation:** 

**[9240.00s] English:** people it's just they operated politically at a higher level you know it's not like oh somebody  
**Translation:** Vocabulary: politically: 政治上

**[9246.18s] English:** said something bad about somebody somebody else which is most politics it's you know they they  
**Translation:** 

**[9252.78s] English:** had strategies about accomplishing their goals sometimes you know over the dead bodies of their  
**Translation:** Vocabulary: accomplishing: 完成目标

**[9258.84s] English:** enemies you know with sophistication yeah more Game of Thrones sophistication and like a big  
**Translation:** 

**[9266.22s] English:** time factor rather than a you know well that requires a lot of control over your emotions  
**Translation:** Vocabulary: sophistication: 复杂程度

**[9271.26s] English:** I think uh to to have a bigger strategy in the way you behave yeah and it's it's it's effective  
**Translation:** 

**[9278.16s] English:** in the sense that coordinating thousands of people to do really hard things where many of  
**Translation:** Vocabulary: coordinating: 协调

**[9283.92s] English:** the people in there don't understand themselves much less how they're participating yeah creates  
**Translation:** 

**[9288.66s] English:** all kinds of you know drama and problems that you know our solution is political in nature like how  
**Translation:** 

**[9296.16s] English:** do you get rid of them you know and so it's it's it's it's it's it's it's it's it's it's it's it's it's  
**Translation:** 

**[9296.20s] English:** how do you convince people how do you leverage them how do you motivate them how do you get rid  
**Translation:** Vocabulary: leverage: 利用

**[9299.86s] English:** of them how you know like there's there's so many layers of that that are interesting and even though  
**Translation:** 

**[9305.56s] English:** some some of it let's say may be tough it's not uh evil unless you know you use that skill to evil  
**Translation:** 

**[9314.68s] English:** purposes which some people obviously do but but it's a skill set that operates you know and I wish  
**Translation:** 

**[9320.02s] English:** I'd you know I was interested in it but I'd you know it was sort of like I'm an engineer I do my  
**Translation:** 

**[9325.42s] English:** thing and you know there's there's times when I could have had a way bigger impact  
**Translation:** 

**[9331.18s] English:** if I you know knew how to if I paid more attention and knew more about that  
**Translation:** 

**[9336.52s] English:** yeah about the human layer of the stack yeah that human political power you know expression  
**Translation:** 

**[9342.10s] English:** layer of the stack just complicated and there's lots to know about it I mean people are good at  
**Translation:** 

**[9346.96s] English:** it they're just amazing and when they're good at it and let's say relatively kind and oriented  
**Translation:** 

**[9355.36s] English:** in a good direction you can really feel you can get lots of stuff done in  
**Translation:** Vocabulary: oriented: 方向明确

**[9360.00s] English:** things that you never thought possible but all people like that also have some pretty hard edges  
**Translation:** 

**[9366.58s] English:** because you know it's a heavy lift and i wish i'd spent more time like that when i was younger  
**Translation:** 

**[9371.78s] English:** but maybe i wasn't ready you know i was a wide-eyed kid for 30 years it's a little bit of a kid i know  
**Translation:** 

**[9379.10s] English:** what do you hope your legacy is when there's a when there's a book like a hitchhiker's guide  
**Translation:** 

**[9387.30s] English:** to the galaxy and this is like a one sentence entry about you know they're from like that guy  
**Translation:** 

**[9392.08s] English:** lived at some point there's not many you know not many people would be remembered uh you're one of  
**Translation:** 

**[9398.24s] English:** the sparkling little human creatures that had a big impact on the world how do you hope you'll  
**Translation:** 

**[9405.54s] English:** be remembered my daughter was trying to get uh she edited my wikipedia page to say that i was a  
**Translation:** Vocabulary: sparkling: 光彩照人

**[9411.08s] English:** legend and a guru but they took it out so she put it back in she's 15.  
**Translation:** 

**[9417.30s] English:** i think i think that was probably the best part of my legacy  
**Translation:** 

**[9420.86s] English:** she got her sister they were all excited they were like trying to put it in the references  
**Translation:** 

**[9426.40s] English:** because there's articles in that on the title calling you that so in the eyes of your kids  
**Translation:** 

**[9430.80s] English:** you're a legend well they're pretty skeptical because they know be better than that they're  
**Translation:** 

**[9436.12s] English:** like dad so yeah that's that's super that kind of stuff is super fun in terms of the big legend  
**Translation:** Vocabulary: skeptical: 怀疑

**[9442.64s] English:** stuff i don't care they don't care legacy i don't really care there's just an  
**Translation:** 

**[9447.30s] English:** engineer yeah they've been thinking about building a big pyramid so i had a debate with a friend about  
**Translation:** 

**[9453.70s] English:** whether pyramids or craters are cooler and he realized that there's craters everywhere but you  
**Translation:** 

**[9459.54s] English:** know they built a couple pyramids 5 000 years ago and they remember you for a while still talking  
**Translation:** Vocabulary: pyramids: 金字塔

**[9463.74s] English:** about it i think that would be cool uh those aren't easy to build oh i know and they don't  
**Translation:** 

**[9470.68s] English:** actually know how they built them which is great they're uh it's either uh agi or  
**Translation:** 

**[9477.30s] English:** aliens could be involved so i think  
**Translation:** 

**[9480.00s] English:** I think you're going to have to figure out quite a few more things than just the basics of civil engineering.  
**Translation:** 

**[9486.40s] English:** So I guess you hope your legacy is pyramids.  
**Translation:** 

**[9490.06s] English:** That would be cool.  
**Translation:** 

**[9492.14s] English:** And my Wikipedia page getting updated by my daughter periodically.  
**Translation:** 

**[9496.30s] English:** Those two things would pretty much make it.  
**Translation:** 

**[9498.64s] English:** Jim, it's a huge honor talking to you again.  
**Translation:** 

**[9500.62s] English:** I hope we talk many more times in the future.  
**Translation:** 

**[9502.76s] English:** I can't wait to see what you do with Tense Torrent.  
**Translation:** 

**[9506.12s] English:** I can't wait to use it.  
**Translation:** 

**[9507.18s] English:** But I can't wait for you to revolutionize yet another space in computing.  
**Translation:** 

**[9513.22s] English:** It's a huge honor to talk to you.  
**Translation:** Vocabulary: computing: 计算机领域; revolutionize: 革新

**[9514.80s] English:** Thanks for talking today.  
**Translation:** 

**[9515.62s] English:** This was fun.  
**Translation:** 

**[9517.10s] English:** Thanks for listening to this conversation with Jim Keller.  
**Translation:** 

**[9519.88s] English:** And thank you to our sponsors, Athletic Greens, All-in-One Nutrition Drink, Brooklyn & Sheets, ExpressVPN, and Belcampo Grass-Fed Meat.  
**Translation:** Vocabulary: belcampo: 贝尔坎普牧场; sponsors: 赞助商

**[9530.08s] English:** Click the sponsor links to get a discount and to support this podcast.  
**Translation:** 

**[9534.00s] English:** And now, let me leave you with some words from Alan.  
**Translation:** 

**[9537.34s] English:** Turing.  
**Translation:** 

**[9538.32s] English:** Those who can imagine anything can create the impossible.  
**Translation:** Vocabulary: turing: 图灵

**[9543.20s] English:** Thank you for listening and hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
