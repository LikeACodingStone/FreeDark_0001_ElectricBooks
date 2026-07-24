# Podcast vocabulary notes
Source file: Lex Fridman - Noam Brown： AI vs Humans in Poker and Games of Strategic Negotiation ｜ Lex Fridman Podcast #344.opus

**[0.00s] English:** A lot of people were saying like, oh, this whole idea of game theory, it's just nonsense.  
**Translation:** 

**[4.00s] English:** And if you really want to make money, you got to like look into the other person's eyes and read their soul and figure out what cards they have.  
**Translation:** 

**[10.60s] English:** But what happened was where we played our bot against four top heads up, no limit, hold'em poker players.  
**Translation:** 

**[16.94s] English:** And the bot wasn't trying to adapt to them.  
**Translation:** Vocabulary: poker: 扑克牌

**[19.46s] English:** It wasn't trying to exploit them.  
**Translation:** 

**[20.78s] English:** It wasn't trying to do these mind games.  
**Translation:** 

**[22.58s] English:** It was just trying to approximate the Nash equilibrium and it crushed them.  
**Translation:** 

**[26.10s] English:** The following is a conversation with Noe Brown, research scientist at FAIR, Facebook AI research group at Meta AI.  
**Translation:** Vocabulary: approximate: 近似; equilibrium: 平衡状态

**[35.40s] English:** He co-created the first AI system that achieved superhuman level performance in no limit Texas hold'em, both heads up and multiplayer.  
**Translation:** 

**[44.04s] English:** And now, recently, he co-created an AI system that can strategically out-negotiate humans using natural language in a popular board game called Diplomacy,  
**Translation:** Vocabulary: diplomacy: 外交; strategically: 策略地; texas: 德克萨斯

**[55.16s] English:** which is a war game.  
**Translation:** 

**[56.10s] English:** That emphasizes negotiation.  
**Translation:** 

**[59.30s] English:** This is the Lex Friedman podcast.  
**Translation:** 

**[61.62s] English:** To support it, please check out our sponsors in the description.  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[64.92s] English:** And now, dear friends, here's Noe Brown.  
**Translation:** 

**[69.04s] English:** You've been a lead on three amazing AI projects.  
**Translation:** 

**[72.80s] English:** So we've got Libratus that solved or at least achieved human level performance on no limit Texas hold'em poker with two players.  
**Translation:** 

**[80.76s] English:** Heads up.  
**Translation:** Vocabulary: libratus: Libratus

**[81.72s] English:** You got Pluribus that solved no limit Texas hold'em poker.  
**Translation:** 

**[86.26s] English:** With six players and just now you have Cicero.  
**Translation:** Vocabulary: pluribus: 多人

**[90.42s] English:** These are all names of systems that solved or achieved human level performance on the game of Diplomacy,  
**Translation:** 

**[97.42s] English:** which for people who don't know, is a popular strategy board game.  
**Translation:** 

**[101.98s] English:** It was loved by JFK, John F.  
**Translation:** 

**[104.70s] English:** Kennedy and Henry Kissinger and many other big famous people in the decade since.  
**Translation:** 

**[112.26s] English:** So let's talk about poker and Diplomacy today.  
**Translation:** 

**[114.62s] English:** First, poker.  
**Translation:** 

**[115.50s] English:** What is the game of no limit Texas hold'em?  
**Translation:** 

**[119.10s] English:** And how is it different from.  
**Translation:** 

**[120.00s] English:** chess well no limit texas hold'em poker is the most popular variant of poker in the world  
**Translation:** 

**[124.40s] English:** so you know you go to a casino you play sit down at the poker table the game that you're playing  
**Translation:** Vocabulary: casino: 赌博场所

**[129.06s] English:** is no limit texas hold'em if you watch movies about poker like casino royale or rounders  
**Translation:** 

**[133.98s] English:** the game that they're playing is no limit texas hold'em poker now it's very different from limit  
**Translation:** Vocabulary: rounders: 德州扑克

**[140.30s] English:** hold'em in that you can bet any amount of chips that you want and so the stakes escalate really  
**Translation:** 

**[145.02s] English:** quickly you start out with like one or two dollars in the pot and then by the end of the  
**Translation:** Vocabulary: escalate: 升级

**[149.48s] English:** hand you've got like a thousand dollars in there maybe so the option to increase the number very  
**Translation:** 

**[154.28s] English:** aggressively very quickly is always there right the no limit aspect is there's no limits to how  
**Translation:** Vocabulary: aggressively: 激进地

**[159.02s] English:** much you can bet you know you in limit hold'em there's like two dollars in the pot you can only  
**Translation:** 

**[164.26s] English:** bet like two dollars but if you got ten thousand dollars in front of you you're always welcome to  
**Translation:** 

**[168.68s] English:** put ten thousand dollars into the pot so i've got a chance to hang out with phil helmuth who plays  
**Translation:** 

**[173.38s] English:** all these different variants of poker  
**Translation:** Vocabulary: helmuth: 菲尔·赫尔姆斯; poker: 扑克牌

**[175.00s] English:** and correct me if i'm wrong but it seems like no limit rewards crazy versus the other ones  
**Translation:** 

**[182.30s] English:** rewards more kind of calculated strategy or or no because you're sort of looking from an  
**Translation:** 

**[188.02s] English:** from an analytic perspective is is strategy also rewarded in no limit texas hold'em i think both  
**Translation:** 

**[195.70s] English:** variants reward strategy but i think what's different about no limit hold'em is it's it's  
**Translation:** Vocabulary: analytic: 分析的; texas: 德克萨斯

**[201.88s] English:** much easier to get jumpy you know you go in there thinking  
**Translation:** 

**[204.86s] English:** you're gonna lose you're gonna play for like a hundred dollars or something and suddenly there's  
**Translation:** Vocabulary: jumpy: 紧张多疑

**[209.54s] English:** like you know a thousand dollars in the pot a lot of people can't handle that can you define jumpy  
**Translation:** 

**[213.48s] English:** when you're playing poker you always want to choose the action that's going to maximize your  
**Translation:** 

**[218.32s] English:** expected value it's kind of like kind of like with investing right like if you're ever in a situation  
**Translation:** 

**[222.46s] English:** where you're the amount of money that's at stake is um is going to have a material impact on your  
**Translation:** 

**[228.34s] English:** life then you're going to play in a more risk averse style you know if somebody makes a huge  
**Translation:** 

**[232.88s] English:** bet you're gonna if you're going to play in a more risk averse style you're going to play in a more  
**Translation:** Vocabulary: averse: 规避风险

**[234.86s] English:** you're playing no limit hold'em and somebody makes a huge bet there might come a point where  
**Translation:** 

**[238.52s] English:** you're like this is too much money  
**Translation:** 

**[240.00s] English:** for me to handle like i can't risk this amount uh and that's what throws a lot of people off  
**Translation:** 

**[244.84s] English:** so that's the big difference i think between no limit and limit what about on the action side  
**Translation:** 

**[251.36s] English:** when you're actually making that big bet that's what i mean by crazy i was i was trying to refer  
**Translation:** 

**[256.52s] English:** to the technical the the technical term of crazy meaning use the big jump in the bet  
**Translation:** 

**[263.68s] English:** to completely throw off the other person in terms of um their ability to reason optimally i think  
**Translation:** 

**[270.54s] English:** that's right i think one of the key strategies in poker is to put the other person into an  
**Translation:** Vocabulary: optimally: 最优化地

**[276.58s] English:** uncomfortable position and if you're doing that then you're you're playing poker well and there's  
**Translation:** 

**[281.14s] English:** a lot of opportunities to do that in no limit hold them you know you can have like fifty dollars in  
**Translation:** 

**[285.78s] English:** there you throw in a thousand dollar bet and um you know that's sometimes if you do it right  
**Translation:** 

**[290.48s] English:** it puts the other person in a really tough spot now it's  
**Translation:** 

**[293.68s] English:** also possible that you make huge mistakes that way and so it's really easy to lose a lot of money  
**Translation:** 

**[297.90s] English:** in no limit hold them if you don't know what you're doing um but there's a lot of upside  
**Translation:** Vocabulary: upside: 潜在收益

**[301.70s] English:** potential too so when you build systems ai systems that play these games we'll talk about poker we'll  
**Translation:** 

**[306.64s] English:** talk about diplomacy are you um are you drawn in in part by the beauty of the game itself  
**Translation:** Vocabulary: diplomacy: 外交; poker: 扑克牌

**[312.58s] English:** ai aside or is it to you primarily a fascinating problem set for the ai to solve i'm drawn in by  
**Translation:** 

**[320.74s] English:** the beauty of the game uh when i i started playing the game i was playing the game and i was playing  
**Translation:** 

**[323.66s] English:** poker when i was in high school and the idea to me that there is a correct an objectively correct  
**Translation:** 

**[330.86s] English:** way of playing poker and if you could figure out what that is then you're you know you're making  
**Translation:** Vocabulary: objectively: 客观地

**[336.30s] English:** unlimited money basically that's like a really fascinating concept to me um and so i was  
**Translation:** 

**[341.74s] English:** fascinated by the strategy of poker even when i was like 16 years old it wasn't until like much  
**Translation:** Vocabulary: fascinated: 着迷

**[347.10s] English:** later that i actually worked on poker ais so there was a sense that you can solve poker like  
**Translation:** 

**[352.06s] English:** uh in the way you can solve chess  
**Translation:** 

**[353.66s] English:** for example or checkers i believe checkers got solved right yeah checkers checkers are  
**Translation:** 

**[358.46s] English:** completely solved optimal strategy  
**Translation:** Vocabulary: optimal: 最佳的

**[360.00s] English:** optimal strategy it's impossible to beat the ai yeah and so in that same way you could technically  
**Translation:** 

**[363.92s] English:** solve chess you could solve chess you could solve poker you could solve poker so this is this gets  
**Translation:** 

**[370.06s] English:** into the concept of a nash equilibrium okay so it is a nash equilibrium okay so in any finite  
**Translation:** 

**[377.30s] English:** two-player zero-sum game there is an optimal strategy that if you play it you are guaranteed  
**Translation:** Vocabulary: equilibrium: 平衡; finite: 有限

**[382.56s] English:** to not lose an expectation no matter what your opponent does and this is kind of a radical  
**Translation:** 

**[388.00s] English:** concept to a lot of people but it's true in chess it's true in poker it's true in any finite  
**Translation:** Vocabulary: expectation: 期望不变

**[393.00s] English:** two-player zero-sum game and to give some intuition for this you can think of rock paper scissors  
**Translation:** 

**[397.92s] English:** in rock paper scissors if you randomly choose between throwing rock paper and scissors with  
**Translation:** Vocabulary: intuition: 直觉

**[403.34s] English:** equal probability then no matter what your opponent does you are not going to lose an  
**Translation:** 

**[407.72s] English:** expectation you're not going to lose an expectation in the long run now the same is true for poker  
**Translation:** 

**[412.94s] English:** there exists some strategy some really complicated strategy that if you play that you are  
**Translation:** 

**[417.80s] English:** guaranteed to lose an expectation and you're not going to lose an expectation in the long run  
**Translation:** 

**[417.98s] English:** and i should say this is for two-player poker six-player poker is a different story yeah it's  
**Translation:** 

**[423.54s] English:** a beautiful giant mess when you say in expectation you're guaranteed not to lose in expectation what  
**Translation:** 

**[430.82s] English:** does in expectation mean poker is a very high variance game so you're going to have hands where  
**Translation:** 

**[435.22s] English:** you win you're going to have hands with your lose even if you're playing the perfect strategy  
**Translation:** Vocabulary: poker: 德州扑克; variance: 波动性

**[437.76s] English:** you can't guarantee that you're going to win every single hand but if you play for long enough  
**Translation:** 

**[442.00s] English:** then you are guaranteed to at least break even and in practice probably win so that's  
**Translation:** 

**[447.96s] English:** an expectation the size of your stack generally speaking now that doesn't include anything about  
**Translation:** 

**[454.02s] English:** the fact that you can go broke it doesn't include any of those kinds of normal real world limitations  
**Translation:** 

**[459.36s] English:** you're talking in a in the theoretical world uh what about this the zero sum aspect how big of a  
**Translation:** 

**[465.20s] English:** constraint is that how big of a constraint is finite so finite's not a huge constraint so i  
**Translation:** Vocabulary: constraint: 限制

**[472.00s] English:** most games that you play are finite in size um it's also true actually that there exists this  
**Translation:** 

**[476.76s] English:** like perfect strategy in  
**Translation:** 

**[477.96s] English:** many infinite games as well technically the game  
**Translation:** 

**[480.00s] English:** has to be compact um there are like some edge cases where you don't have a nash equilibrium  
**Translation:** 

**[485.10s] English:** in a two-player zero-sum game so you can think of a game where you're like you know if we're  
**Translation:** 

**[488.90s] English:** playing a game where whoever names the bigger number is the winner there's no nash equilibrium  
**Translation:** 

**[492.96s] English:** to that game 17 yeah exactly 18 but you beat you win again you're good at this i played a lot of  
**Translation:** 

**[499.22s] English:** games okay uh so that's and then the zero-sum aspect the zero zero-sum aspect so there exists  
**Translation:** 

**[507.10s] English:** a nash equilibrium in non-two-player zero-sum games as well and by the way just to clarify what  
**Translation:** 

**[511.52s] English:** i mean by two-player zero-sum i mean there's two players and whatever one player wins the other  
**Translation:** 

**[515.94s] English:** player loses so if we're playing poker and i win fifty dollars that means that you're losing fifty  
**Translation:** 

**[519.76s] English:** dollars now outside of two-player zero-sum games there still exists nash equilibria but they're  
**Translation:** Vocabulary: equilibria: 均衡状态

**[527.10s] English:** not as meaningful because you know you can think of a game like risk if everybody else at the and  
**Translation:** 

**[533.24s] English:** on the board decides to team up against you and take you out there's no perfect strategy  
**Translation:** 

**[536.98s] English:** you can use to win the game you can't win the game you can't win the game you can't win the game  
**Translation:** 

**[537.08s] English:** that's going to guarantee that you win there there's just nothing you can do so outside of  
**Translation:** 

**[541.78s] English:** two-player zero-sum games there's no guarantee that you're going to win by playing a nash  
**Translation:** 

**[545.62s] English:** equilibrium have you ever tried to model in the other aspects of the game which is like  
**Translation:** 

**[552.08s] English:** the pleasure you draw from playing the game and then if you're a professional poker player  
**Translation:** 

**[557.74s] English:** if you're exciting even if you lose uh the you know the money you would get from the attention  
**Translation:** 

**[565.16s] English:** you get to the sponsor and all that kind of stuff  
**Translation:** 

**[566.96s] English:** is that that would be a fun thing to model to model in or does that make it sort of super  
**Translation:** 

**[572.62s] English:** complex to include the human factor and that's in its full complexity i think you bring up a  
**Translation:** 

**[577.68s] English:** couple good points there so i think a lot of professional poker players i mean they get a  
**Translation:** Vocabulary: complexity: 复杂性; poker: 纸牌游戏

**[582.10s] English:** huge amount of money not from actually playing poker but from the sponsorships and having a  
**Translation:** 

**[586.88s] English:** personality that people want to tune in and watch that that's a big that's a big way to to make a  
**Translation:** 

**[591.74s] English:** name for yourself in poker i just wonder from an ai perspective if you create and we'll talk about  
**Translation:** 

**[596.68s] English:** this more in the future if you're a professional poker player and you're a professional poker player  
**Translation:** 

**[596.96s] English:** or maybe an ai system  
**Translation:** 

**[600.00s] English:** them that also talks trash and all that kind of stuff that that becomes part of the function to  
**Translation:** 

**[604.78s] English:** maximize so it's not just um optimal poker play maybe sometimes you want to be chaotic maybe  
**Translation:** 

**[610.34s] English:** sometimes you want to be suboptimal and you lose um the the chaos and maybe sometimes you want to  
**Translation:** Vocabulary: maximize: 最大化; optimal: 最优化; suboptimal: 次优的

**[616.66s] English:** be overly aggressive because people the audience loves that yeah fascinating i think i think what  
**Translation:** 

**[623.54s] English:** you're getting at here is that there's a difference between making an ai that wins a game and an ai  
**Translation:** 

**[626.88s] English:** that's fun to play with right yeah yeah and we're fun to watch so those are all different things fun  
**Translation:** 

**[631.64s] English:** to play with and fun to watch yeah and i think you know i've i've heard uh talks from like game  
**Translation:** 

**[637.16s] English:** designers and and they say like you know people that work on ai for actual recreational games that  
**Translation:** 

**[641.70s] English:** people play and they say yeah there's a big difference between trying to make an ai that  
**Translation:** Vocabulary: designers: 设计师; recreational: 休闲的

**[645.64s] English:** actually wins and you know you look at a game like civilization um the way that the ai's play is not  
**Translation:** 

**[651.32s] English:** optimal for trying to win they're they're playing a different game they're trying to have  
**Translation:** 

**[655.28s] English:** personalities they're trying to  
**Translation:** 

**[656.62s] English:** you know  
**Translation:** 

**[656.86s] English:** be fun and engaging um and that makes for a better game yeah and we also talk about npcs i just talked  
**Translation:** 

**[663.06s] English:** to todd howard who is the the creator of fallout and the elder scroll series and um starfield the  
**Translation:** Vocabulary: fallout: 废土; scroll: 卷轴; starfield: 星野

**[669.52s] English:** new game coming out and the creator what i think is the greatest game of all time which is skyrim  
**Translation:** 

**[674.26s] English:** and the npcs there the ai that governs that whole game is very interesting but the npcs also are  
**Translation:** 

**[679.58s] English:** super interesting and considering what language models might do to npcs in an open world  
**Translation:** 

**[686.60s] English:** rpg role-playing game it's super exciting yeah honestly i'm i think this is like one of the first  
**Translation:** 

**[693.74s] English:** applications where we're going to see like real consumer interaction with large language models  
**Translation:** 

**[698.34s] English:** um i guess let's um elder scroll six is in development now they're probably like pretty  
**Translation:** 

**[703.40s] English:** close to finishing it but i would not be surprised at all if elder scroll seven was using large  
**Translation:** 

**[708.78s] English:** language models for their npc they're not they're i mean i'm not saying anything i'm not saying  
**Translation:** 

**[713.04s] English:** anything this is me speculating not you no but but  
**Translation:** 

**[716.60s] English:** there's they're just releasing the starfield they do one game  
**Translation:** Vocabulary: speculating: 猜测

**[720.00s] English:** of time yeah and so uh whatever it is whenever the date is i don't know what the date is calm  
**Translation:** 

**[725.72s] English:** down uh but it would be i don't know like uh 2024 25 26 so it's actually very possible that  
**Translation:** 

**[732.80s] English:** would include language models i was listening to this um this talk by a gaming executive  
**Translation:** 

**[738.42s] English:** when i was in grad school and one of the questions that a person in the audience asked is why are all  
**Translation:** 

**[745.06s] English:** these games so focused on fighting and killing and the person responded that it's just so much  
**Translation:** 

**[750.54s] English:** harder to make an ai that can talk with you and cooperate with you than it is to make an ai that  
**Translation:** Vocabulary: cooperate: 协同作战

**[755.08s] English:** can fight you and i think once this technology develops further and you can have a you can reach  
**Translation:** 

**[760.64s] English:** a point where like not every single line of dialogue has to be scripted it unlocks a lot  
**Translation:** 

**[764.92s] English:** of potential for new kinds of games like much more like positive interactions that are not so focused  
**Translation:** 

**[769.88s] English:** on fighting and i'm really looking forward to that it might not be positive it might be just drama  
**Translation:** 

**[774.02s] English:** so you  
**Translation:** 

**[774.64s] English:** you  
**Translation:** 

**[775.06s] English:** will be in like a call of duty game instead of doing the shooting you'll just be hanging out  
**Translation:** 

**[778.70s] English:** and like arguing with an ai about like um like passive aggressive and then you won't be able  
**Translation:** 

**[784.40s] English:** to sleep that night you have to return or continue the argument that you were uh emotionally hurt  
**Translation:** 

**[790.28s] English:** i mean yeah i think that's actually an exciting world whatever whatever is the drama the chaos  
**Translation:** 

**[797.08s] English:** that we love the push and pull of human connection i think it's possible to do that in the video  
**Translation:** 

**[800.94s] English:** game world and i think you could be messier and make more mistakes and you could be more  
**Translation:** 

**[805.06s] English:** you could make more mistakes in the video game world which is why it would be a nice place and and also it doesn't have a deep of a as deep of a real psychological impact because inside video games it's kind of understood that you're in a not a real world so whatever crazy stuff ai does we have some flexibility to play just like with a game of diplomacy it's a game this is not real geopolitics not real war it's a it's a game so you could you can have a little bit of fun um a little bit of chaos okay back to nashor class again for the next four minutes next we're gonna talk a little bit about this uh on the msd  
**Translation:** 

**[815.14s] English:** games it's kind of understood that you're in a not a real world so whatever crazy stuff ai does  
**Translation:** Vocabulary: diplomacy: 外交; flexibility: 灵活性; geopolitics: 地缘政治

**[821.78s] English:** we have some flexibility to play just like with a game of diplomacy it's a game this is not real  
**Translation:** 

**[827.14s] English:** geopolitics not real war it's a it's a game so you could you can have a little bit of fun um a little  
**Translation:** 

**[832.82s] English:** bit of chaos okay back to nash equilibrium uh how do we find the nash equilibrium all right so there's  
**Translation:** 

**[840.00s] English:** different ways to find an actual equilibrium. So the way that we do it is with this process  
**Translation:** Vocabulary: equilibrium: 平衡状态

**[845.44s] English:** called self-play. Basically, we have this algorithm that starts by playing totally randomly,  
**Translation:** 

**[851.68s] English:** and it learns how to play the game by playing against itself. So it will start playing the  
**Translation:** Vocabulary: algorithm: 算法

**[858.56s] English:** game totally randomly, and then if it's playing poker, it'll eventually get to the end of the  
**Translation:** 

**[863.92s] English:** game and make $50. And then it will review all the decisions that it made along the way  
**Translation:** Vocabulary: poker: 扑克牌游戏

**[869.52s] English:** and say, what would have happened if I had chosen this other action instead?  
**Translation:** 

**[874.00s] English:** If I had raised here instead of called, what would the other player have done? And because it's  
**Translation:** 

**[878.80s] English:** playing against a copy of itself, it's able to do that counterfactual reasoning. So it can say,  
**Translation:** 

**[883.28s] English:** okay, well, if I took this action and the other person takes this action, and then I take this  
**Translation:** Vocabulary: counterfactual: 假设情况

**[887.20s] English:** action, and eventually I make $150 instead of 50. And so it updates the regret value for that  
**Translation:** 

**[895.04s] English:** action. Regret is basically like how much does it regret having not played that action in the past?  
**Translation:** 

**[900.48s] English:** And when it encounters that same situation again, it's going to pick actions that have higher  
**Translation:** 

**[905.20s] English:** regret with higher probability. Now, it'll just keep simulating the games this way. It'll keep  
**Translation:** Vocabulary: encounters: 遇到; simulating: 模拟

**[911.76s] English:** accumulating regrets for different situations. And in the long run, if you pick actions that have  
**Translation:** 

**[917.92s] English:** high regret with higher probability in the correct way, it's proven to converge to a Nash equilibrium.  
**Translation:** Vocabulary: accumulating: 累积; converge: 收敛

**[924.64s] English:** Even for super complex games, even for imperfect information games? It's true for all games. It's a  
**Translation:** 

**[929.52s] English:** It's true for chess, it's true for poker, it's particularly useful for poker.  
**Translation:** 

**[933.50s] English:** So this is the method of counterfactual regret minimization?  
**Translation:** 

**[936.38s] English:** This is counterfactual regret minimization.  
**Translation:** Vocabulary: minimization: 最小化

**[937.86s] English:** That doesn't have to do with self-play, it has to do with just any, if you follow this  
**Translation:** 

**[942.46s] English:** kind of process, self-play or not, you'll be able to arrive at an optimal set of actions.  
**Translation:** 

**[948.32s] English:** So this counterfactual regret minimization is a kind of self-play.  
**Translation:** 

**[951.46s] English:** It's a principled kind of self-play that's proven to converge to Nash Equilibria, even  
**Translation:** Vocabulary: equilibria: 纳什均衡; principled: 有原则的

**[955.66s] English:** in imperfect information games.  
**Translation:** 

**[957.14s] English:** Now you can have other forms of self-play, and people use other forms of self-play.  
**Translation:** 

**[960.00s] English:** forms of self-play for perfect information games where you have more flexibility. The algorithm  
**Translation:** 

**[965.26s] English:** doesn't have to be as theoretically sound in order to converge to that class of games because  
**Translation:** Vocabulary: flexibility: 灵活性; theoretically: 理论上

**[970.00s] English:** it's a simpler setting. Sure. So I kind of, in my brain, the word self-play has mapped in neural  
**Translation:** 

**[976.74s] English:** networks, but we're speaking something bigger than just neural networks. It could be anything.  
**Translation:** Vocabulary: neural: 神经的

**[982.20s] English:** The self-playing mechanism is just the mechanism of a system playing itself.  
**Translation:** 

**[986.00s] English:** Exactly. Yeah. Self-play is not tied specifically to neural nets. It's a kind of reinforcement  
**Translation:** Vocabulary: reinforcement: 强化

**[990.48s] English:** learning basically. And I would also say this process of trying to reason, oh, what would the  
**Translation:** 

**[996.26s] English:** value have been if I had taken this other action instead? This is very similar to how humans learn  
**Translation:** 

**[1000.86s] English:** to play a game like poker. You probably played poker before and with your friends, you probably  
**Translation:** 

**[1005.54s] English:** ask like, oh, would you have called me if I raised there? And that's a person trying to do the same  
**Translation:** Vocabulary: poker: 扑克牌游戏

**[1011.54s] English:** kind of learning from a counterfactual that the AI is doing. Okay. And if you do that,  
**Translation:** 

**[1015.90s] English:** at scale, you're going to be able to learn an optimal policy.  
**Translation:** Vocabulary: counterfactual: 假设情景; optimal: 最优

**[1019.72s] English:** Yeah. Now where the neural nets come in, I said like, okay, if it's in that situation again,  
**Translation:** 

**[1024.10s] English:** then it will choose the action that has high regret. Now, the problem is that poker is such  
**Translation:** 

**[1029.00s] English:** a huge game. I think No Limit Texas Hold'em, the version that we were playing has 10 to the 161  
**Translation:** 

**[1034.54s] English:** different decision points, which is more than the number of atoms in the universe squared.  
**Translation:** Vocabulary: texas: 德克萨斯州

**[1038.12s] English:** That's heads up? That's heads up. Yeah. 10 to the 161, you said?  
**Translation:** 

**[1041.58s] English:** Yeah. I mean, it depends on the number of chips that you have, the stacks and everything,  
**Translation:** 

**[1044.10s] English:** but like the version that we were playing,  
**Translation:** 

**[1045.90s] English:** 10 to the 161. Which I assume would be a somewhat simplified version anyway,  
**Translation:** 

**[1050.40s] English:** because I bet there's some like step function you had for like bets.  
**Translation:** 

**[1056.08s] English:** Oh, no, no, no. I'm saying like we played the full game. You can bet whatever amount you want.  
**Translation:** 

**[1059.96s] English:** Now the bot maybe was constrained in like what it considered for bet sizes, but the person on  
**Translation:** 

**[1064.30s] English:** the other side could bet whatever they wanted. Yeah. I mean, 161 plus or minus 10 doesn't matter.  
**Translation:** Vocabulary: constrained: 限制

**[1069.36s] English:** Yeah. And so the way neural nets help out here is, you know, you don't have to run,  
**Translation:** 

**[1075.90s] English:** it's the same exact situation because that's never going to happen again.  
**Translation:** 

**[1078.30s] English:** The odds of you running into the same exact situation.  
**Translation:** 

**[1080.00s] English:** are pretty slim but if you run into a similar situation then you can generalize from other  
**Translation:** Vocabulary: generalize: 概括外推

**[1084.82s] English:** states that you've been in that kind of look like that one and you can say like well these other  
**Translation:** 

**[1088.54s] English:** situations i had high regret for this action and so maybe i should play that action here as well  
**Translation:** 

**[1092.50s] English:** which is the more complex game chess or poker or go or poker do you know that is a controversial  
**Translation:** 

**[1100.26s] English:** question okay um i'm gonna it's like somebody's screaming on reddit right now it depends on which  
**Translation:** 

**[1104.76s] English:** subreddit you're on is it chess or is it poker i'm sure like david silver is gonna get really  
**Translation:** 

**[1108.80s] English:** angry at me yeah i'll i'll say i'm gonna say poker actually and i think for a couple reasons  
**Translation:** Vocabulary: subreddit: 子版块

**[1112.84s] English:** um they're not here to defend themselves so first of all you have the imperfect information aspect  
**Translation:** 

**[1119.24s] English:** and so it's um it we can go into that but like once you introduce imperfect information  
**Translation:** 

**[1125.44s] English:** uh things get much more complicated so we should say maybe you can describe what is seen to the  
**Translation:** 

**[1133.84s] English:** players what is not seen uh in the game of texas hold'em yeah so texas hold'em  
**Translation:** 

**[1138.78s] English:** you get two cards face down that only you see um and so that's the hidden information in the game  
**Translation:** 

**[1144.52s] English:** the other players also all get two cards face down that only they see um and so you have to  
**Translation:** 

**[1149.04s] English:** kind of as you're playing reason about like okay what do they think i have what do they have what  
**Translation:** 

**[1153.82s] English:** do they think i think they have that kind of stuff and um that's that's kind of where bluffing comes  
**Translation:** Vocabulary: bluffing: 虚张声势

**[1159.42s] English:** into play right because the fact that you can bluff the fact that you can bet with a bad hand  
**Translation:** 

**[1164.40s] English:** and still win is because they don't know what your cards are right and that's the  
**Translation:** Vocabulary: bluff: 诈唬

**[1168.78s] English:** that's the key difference between a perfect information game like poker uh sorry like chess  
**Translation:** 

**[1172.54s] English:** and go um and imperfect information games like poker this is what trash talk looks like  
**Translation:** 

**[1180.14s] English:** the implied statement is the game i solved is much tougher but yeah so uh when you're playing  
**Translation:** 

**[1186.78s] English:** i'm just going to do random questions here so when you're playing your opponent under imperfect  
**Translation:** 

**[1192.14s] English:** information is there some degree to which you're trying to estimate the range of hands that they  
**Translation:** 

**[1198.78s] English:** have  
**Translation:** 

**[1210.14s] English:** so  
**Translation:** 

**[1220.22s] English:** so  
**Translation:** 

**[1223.18s] English:** so  
**Translation:** 

**[1226.70s] English:** you  
**Translation:** 

**[1200.00s] English:** or is that not part of the algorithm so how what are the different approaches  
**Translation:** 

**[1204.24s] English:** to the imperfect information game so the key thing to understand about why imperfect information  
**Translation:** Vocabulary: algorithm: 算法

**[1209.68s] English:** makes things difficult is that you have to worry not just about which actions to play  
**Translation:** 

**[1214.56s] English:** but the probability that you're going to play those actions so you think about  
**Translation:** 

**[1219.36s] English:** um rock paper scissors for example rock paper scissors is an imperfect information game  
**Translation:** 

**[1223.68s] English:** um right because you don't know what i'm about to throw i do but yeah usually not yeah yeah and so  
**Translation:** 

**[1229.36s] English:** you can't just say like oh i'm just going to throw a rock every single time because the other person  
**Translation:** 

**[1232.88s] English:** is going to figure that out and notice a pattern and then suddenly you're going to start losing  
**Translation:** 

**[1237.12s] English:** and so you don't just have to figure out like which action to play you have to figure out the  
**Translation:** 

**[1240.16s] English:** probability that you play it and really importantly the value of an action depends on the  
**Translation:** 

**[1245.84s] English:** probability that you're going to play it so if you're playing rock every single time that value  
**Translation:** 

**[1250.72s] English:** is really low but if you're never playing rock you play rock like one percent of the time then  
**Translation:** 

**[1255.92s] English:** suddenly the the other person is probably going to be throwing scissors  
**Translation:** 

**[1259.68s] English:** and when you throw a rock the value of that action is going to be really high now you take that to  
**Translation:** 

**[1264.08s] English:** poker what that means is the value of bluffing for example if you're the kind of person that  
**Translation:** 

**[1269.92s] English:** never bluffs and you have this reputation as somebody that never bluffs and suddenly you  
**Translation:** Vocabulary: bluffs: 诈唬; poker: 纸牌游戏

**[1273.76s] English:** bluff there's a really good chance that that bluff is going to work and you're going to make a lot of  
**Translation:** 

**[1277.20s] English:** money on the other hand if you got a reputation like if they seen you play for a long time and  
**Translation:** 

**[1281.28s] English:** they see oh you're the kind of person that's bluffing all the time when you bluff they're  
**Translation:** 

**[1285.28s] English:** not going to buy it and they're going to call you down you're going to lose a lot of money  
**Translation:** Vocabulary: bluff: 虚张声势; bluffing: 虚张声势

**[1290.16s] English:** finding that balance of how often you should be bluffing is uh the key challenge of a game of  
**Translation:** 

**[1295.92s] English:** poker and um you contrast that with a game like chess it doesn't matter if you're opening with  
**Translation:** 

**[1302.56s] English:** the queen's gambit 10 of the time or 100 of the time the value the expected value is the same  
**Translation:** 

**[1309.44s] English:** so um so that's that's why we need these algorithms that understand not just we have  
**Translation:** Vocabulary: gambit: 开局策略

**[1315.52s] English:** to figure out what actions are good but the probabilities we need to get the exact  
**Translation:** 

**[1318.32s] English:** probabilities correct  
**Translation:** Vocabulary: probabilities: 概率

**[1319.36s] English:** and that's actually  
**Translation:** 

**[1320.00s] English:** when we created the bot, Libratus, Libratus means balanced because the  
**Translation:** Vocabulary: libratus: 平衡的

**[1324.32s] English:** algorithm that we designed was designed to find that right balance of how often  
**Translation:** 

**[1329.06s] English:** it should play each action. The balance of how often in the key sort of  
**Translation:** Vocabulary: algorithm: 算法

**[1332.90s] English:** branching is the bluff or not to bluff. Is that a good crude  
**Translation:** 

**[1337.76s] English:** simplification of the major decision in poker? It's a good simplification. I think  
**Translation:** 

**[1342.44s] English:** that's like the main tension but it's not just how often to bluff or not  
**Translation:** 

**[1347.24s] English:** to bluff. It's like how often should you bet in general? How often should you...  
**Translation:** 

**[1350.54s] English:** What kind of bet should you make? Should you bet big or should you bet  
**Translation:** 

**[1354.44s] English:** small and with which hands? And so this is where the idea of a  
**Translation:** 

**[1359.36s] English:** range comes from because when you're bluffing with a particular hand in a  
**Translation:** 

**[1363.32s] English:** particular spot, you don't want there to be a pattern for the other person to  
**Translation:** 

**[1366.92s] English:** pick up on. You don't want them to figure out, oh, whenever this person is in this  
**Translation:** 

**[1369.98s] English:** spot, they're always bluffing. And so you have to reason about, okay, would I also  
**Translation:** 

**[1374.90s] English:** bet with a good hand in this spot?  
**Translation:** 

**[1377.24s] English:** You want to be unpredictable. So you have to think about what would I do if I had  
**Translation:** 

**[1382.46s] English:** this different set of cards. Is there explicit estimation of like a theory of  
**Translation:** 

**[1388.00s] English:** mind that the other person has about you or is that just a emergent thing that  
**Translation:** Vocabulary: emergent: 自发形成; estimation: 估计; explicit: 明确的

**[1392.40s] English:** happens? The way that the bots handle it that are really successful, they have an  
**Translation:** 

**[1398.60s] English:** explicit theory of mind. So they're explicitly reasoning about what are...  
**Translation:** Vocabulary: explicitly: 明确地

**[1402.88s] English:** What's the common knowledge belief? What do you think I have  
**Translation:** 

**[1407.14s] English:** with you? What do you think you have? What do I think you have? What do you think I  
**Translation:** 

**[1409.38s] English:** think you have? It's explicitly reasoning about them.  
**Translation:** 

**[1412.52s] English:** Is there a multiple us? So maybe that's jumping ahead to six players,  
**Translation:** 

**[1417.16s] English:** but is there a stickiness to the person? So it's an iterative game. You're playing  
**Translation:** 

**[1422.32s] English:** the same person. There's a stickiness to that, right.  
**Translation:** Vocabulary: iterative: 循环迭代; stickiness: 粘性留存

**[1427.24s] English:** You're gathering information as you play. It's not because every hand is a new hand.  
**Translation:** 

**[1433.18s] English:** Is there a continuation in terms of  
**Translation:** Vocabulary: continuation: 连续性

**[1436.36s] English:** estimation?  
**Translation:** 

**[1437.10s] English:** what kind of player I'm facing here?  
**Translation:** 

**[1439.28s] English:** That's a good question.  
**Translation:** 

**[1440.00s] English:** so you could approach the game that way the way that the bots do it they don't and the way that  
**Translation:** 

**[1445.52s] English:** humans approach it also expert human players the way they approach it is to basically assume that  
**Translation:** 

**[1450.88s] English:** you know my strategy so i'm going to try to pick a strategy where even if i were to play it for  
**Translation:** 

**[1457.52s] English:** 10 000 hands and you could figure out exactly what it was you still wouldn't be able to beat  
**Translation:** 

**[1461.12s] English:** it basically what that means is i'm trying to approximate the nash equilibrium i'm trying to  
**Translation:** Vocabulary: approximate: 近似; equilibrium: 平衡状态

**[1464.64s] English:** be perfectly balanced because if if i'm playing the nash equilibrium even if you know what my  
**Translation:** 

**[1469.36s] English:** strategy is like i said i'm still unbeatable in expectation so so that's what that's what the bot  
**Translation:** Vocabulary: expectation: 预期; unbeatable: 不可战胜

**[1474.64s] English:** aims for and that's actually what a lot of expert poker players aim for as well to start by playing  
**Translation:** 

**[1479.76s] English:** the nash equilibrium and then maybe if they spot weaknesses in the way you're playing then they can  
**Translation:** Vocabulary: poker: 扑克牌游戏

**[1483.92s] English:** deviate a little bit to take advantage of that they aim to be unbeatable in expectation okay  
**Translation:** 

**[1490.56s] English:** so who's the greatest poker player of all time and why is it phil hellmuth  
**Translation:** Vocabulary: deviate: 偏离; hellmuth: 海琳穆

**[1494.08s] English:** so this is for phil uh so he's known um  
**Translation:** 

**[1499.12s] English:** at least  
**Translation:** 

**[1499.36s] English:** in part for maybe playing sub optimally and he still wins a lot it's a bit chaotic  
**Translation:** 

**[1506.00s] English:** so maybe can you speak from an ai perspective about the genius of his madness or the madness  
**Translation:** Vocabulary: optimally: 最佳方式

**[1512.88s] English:** of his genius so playing sub optimally playing chaotically um as a way to make you hard to  
**Translation:** 

**[1521.12s] English:** pin down about what your strategy is so okay the thing that i should explain first of all with like  
**Translation:** Vocabulary: chaotically: 混乱地

**[1527.28s] English:** nash equilibrium it doesn't mean that it's  
**Translation:** 

**[1529.12s] English:** predictable the whole point of it is that you're trying to be unpredictable  
**Translation:** Vocabulary: predictable: 可预测的

**[1532.72s] English:** now i think when somebody like phil hamuth might be really successful  
**Translation:** 

**[1536.80s] English:** is not in being unpredictable but in being able to  
**Translation:** 

**[1541.28s] English:** take advantage of the other player and figure out where they're being predictable  
**Translation:** 

**[1545.60s] English:** or guiding the other player into thinking  
**Translation:** 

**[1549.20s] English:** that you have certain weaknesses and then and then understanding how they're going to change  
**Translation:** 

**[1553.28s] English:** their behavior they're going to deviate from a nash equilibrium style of play to try to take  
**Translation:** 

**[1558.08s] English:** take advantage of those perceived weaknesses and then counteract them.  
**Translation:** 

**[1560.00s] English:** exploit them so you kind of get into the mind games there so you think about at least heads  
**Translation:** 

**[1564.38s] English:** up poker as a as a dance between two agents i guess are you playing the cards are you playing  
**Translation:** 

**[1569.30s] English:** the the player so this this gets down to a big argument in the poker community and the academic  
**Translation:** 

**[1574.98s] English:** community for a long time there was this debate of like what's called gto game theory optimal poker  
**Translation:** 

**[1580.26s] English:** or exploitative play and um up until about like 2017 when we did the labratus match i think  
**Translation:** Vocabulary: exploitative: 剥削性; optimal: 最优的

**[1587.42s] English:** actually exploitative play had the advantage a lot of people were saying like oh this whole idea  
**Translation:** 

**[1591.84s] English:** of game theory it's just nonsense and if you really want to make money you got to like look  
**Translation:** 

**[1595.72s] English:** into the other person's eyes and read their soul and figure out what cards they have but what  
**Translation:** 

**[1600.96s] English:** happened was people started adopting the game theory optimal strategy um and they were making  
**Translation:** 

**[1605.96s] English:** good money and they weren't trying to adapt so much to the other player they were just trying  
**Translation:** 

**[1610.60s] English:** to play the nash equilibrium and then what really solidified it i think was the broadest the  
**Translation:** Vocabulary: broadest: 最广泛; equilibrium: 均衡; solidified: 巩固

**[1615.36s] English:** labratus match where we play a lot of games and we're playing a lot of games and we're playing a  
**Translation:** 

**[1617.40s] English:** lot of games and we're playing a lot of games and we're playing a lot of games and we're playing  
**Translation:** 

**[1617.42s] English:** our bot against four top heads up no limit hold'em poker players and the bot wasn't trying to adapt  
**Translation:** 

**[1623.70s] English:** to them it wasn't trying to exploit them it wasn't trying to do these mind games it was just trying  
**Translation:** Vocabulary: poker: 扑克牌

**[1627.94s] English:** to approximate the nash equilibrium and it crushed them i think you know it we were playing for  
**Translation:** 

**[1635.22s] English:** fifty dollar one hundred dollar blinds and over the course of about a hundred twenty thousand  
**Translation:** 

**[1639.22s] English:** hands it made close to two million dollars 120 000 hands 120 000 hands against humans yeah and  
**Translation:** 

**[1645.06s] English:** this was this was fake money to be clear so there was real money at the time and the game was  
**Translation:** 

**[1647.38s] English:** at stake there was two hundred thousand dollars first of all all money is fake but um that's that's  
**Translation:** 

**[1652.36s] English:** that's a different conversation um we give it meaning uh it's an it's a it's a phenomena that  
**Translation:** 

**[1658.64s] English:** gets meaning from our uh complex psychology as a human civilization um it's emerging from the  
**Translation:** 

**[1664.26s] English:** collective intelligence of the human species but that's not what you mean you mean like there's  
**Translation:** 

**[1668.00s] English:** literally you can't you can't buy stuff with it okay can you actually step back and take me  
**Translation:** 

**[1673.04s] English:** through that um competition yeah okay so  
**Translation:** 

**[1677.38s] English:** when i was in grad school um there was  
**Translation:** 

**[1680.00s] English:** thing called the annual computer poker competition where every year all the different research labs  
**Translation:** 

**[1684.48s] English:** that were working on ai for poker would get together they would make a bot they would play  
**Translation:** 

**[1688.00s] English:** them against each other and we made a bot that actually won the 2014 competition the 2016  
**Translation:** 

**[1694.88s] English:** competition and so we decided we're going to take this bot build on it and play against real top  
**Translation:** 

**[1701.68s] English:** professional heads up no limit texas hold'em poker players so we invited four of the world's best  
**Translation:** Vocabulary: texas: 德克萨斯州

**[1707.84s] English:** players in this specialty and we challenged them to 120 000 hands of poker over the course of 20  
**Translation:** 

**[1714.24s] English:** days um and we had two hundred thousand dollar two hundred thousand dollars in prize money at stake  
**Translation:** Vocabulary: specialty: 专门领域

**[1720.08s] English:** where it would basically be divided among them depending on how well they did relative to each  
**Translation:** 

**[1723.60s] English:** other so we wanted to have some incentive for them to play their best did you have a confidence 2014  
**Translation:** Vocabulary: incentive: 激励

**[1730.24s] English:** 16 that this is even possible how much doubt was there so and we did a competition actually in  
**Translation:** 

**[1735.92s] English:** 2015 where we also played against  
**Translation:** 

**[1737.84s] English:** professional poker players and the bot lost by by a pretty sizable margin actually  
**Translation:** 

**[1742.00s] English:** now there were some big improvements from 2015 to 2017 and so can you speak to the improvements  
**Translation:** Vocabulary: sizable: 较大的

**[1747.60s] English:** is it computational nature is it the algorithm the the methods it was it was really an algorithmic  
**Translation:** 

**[1752.16s] English:** approach that was the difference so 2015 it was much more focused on trying to  
**Translation:** Vocabulary: algorithm: 算法; algorithmic: 算法的; computational: 计算的

**[1759.20s] English:** come up with a strategy up front like trying to solve the entire game of poker like and then just  
**Translation:** 

**[1763.92s] English:** have a lookup table where you're saying like oh i'm in this situation what's the  
**Translation:** Vocabulary: lookup: 查找表; poker: 纸牌游戏

**[1767.84s] English:** strategy um the approach that we took in 2017 was much more search based it was trying to say okay  
**Translation:** 

**[1774.08s] English:** well let me in real time try to compute a much better strategy than what i had pre-computed  
**Translation:** 

**[1780.88s] English:** by playing against myself during self-play what is the search space for poker what are you searching  
**Translation:** 

**[1787.76s] English:** over what's that look like there's different actions like raising calling yeah what are the  
**Translation:** 

**[1794.48s] English:** actions um  
**Translation:** 

**[1797.84s] English:** just a search over actions so  
**Translation:** 

**[1800.00s] English:** in a game like chess the the search is like okay i'm in this chess position and i can like you know  
**Translation:** 

**[1805.90s] English:** move these different pieces and see where things end up in poker what you're searching over is  
**Translation:** 

**[1810.16s] English:** the actions that you can take for your hand the probabilities that you take those actions  
**Translation:** 

**[1814.54s] English:** and then also the probabilities that you take other actions with other hands that you might have  
**Translation:** Vocabulary: probabilities: 概率

**[1818.56s] English:** um and and that's kind of like a hard to wrap your head around like why are you searching over  
**Translation:** 

**[1824.28s] English:** these like other hands that you might have and like trying to figure out what you would do with  
**Translation:** 

**[1828.94s] English:** those hands um and the idea is is again you you want to you want to always be balanced and  
**Translation:** 

**[1835.58s] English:** unpredictable and so if your search algorithm is saying like oh i want to raise with this hand  
**Translation:** 

**[1840.94s] English:** well in order to know whether that's a good action like let's say it's a bluff you know let's say you  
**Translation:** 

**[1845.04s] English:** have a bad hand and you're saying like oh i i think i should be betting here with this really  
**Translation:** Vocabulary: bluff: 虚张声势

**[1848.82s] English:** bad hand and bluffing well that that's only a good action if you're also betting with a strong hand  
**Translation:** 

**[1855.20s] English:** otherwise it's an obvious bluff so if your action  
**Translation:** Vocabulary: bluffing: 诈唬

**[1858.08s] English:** is  
**Translation:** 

**[1858.82s] English:** maximizes your unpredictability so that action could be mapped by your opponent to a lot of  
**Translation:** Vocabulary: maximizes: 最大化

**[1864.66s] English:** different hands then that's a good action basically what you want to do is put your  
**Translation:** 

**[1869.30s] English:** opponent into a tough spot so you want them to always have some doubt like should i call here  
**Translation:** 

**[1874.52s] English:** should i fold here and if you are raising in the appropriate balance between bluffs and good hands  
**Translation:** 

**[1880.26s] English:** then you're putting them into that tough spot and so that's what we're trying to do we're always  
**Translation:** Vocabulary: bluffs: 诈唬

**[1883.00s] English:** trying to search for a strategy that would put the opponent into a difficult position can you  
**Translation:** 

**[1887.28s] English:** give a metric that's  
**Translation:** 

**[1888.82s] English:** you're trying to maximize or minimize does this have to do with the regret thing what we're talking  
**Translation:** 

**[1892.58s] English:** about in terms of putting your opponent in a maximally tough spot yeah ultimately what you're  
**Translation:** Vocabulary: maximally: 最大程度地

**[1898.18s] English:** trying to maximize is your expected winnings like your expected value the amount of money that  
**Translation:** 

**[1902.34s] English:** you're going to walk away from assuming that your opponent was playing optimally in response  
**Translation:** Vocabulary: maximize: 最大化; optimally: 最优化

**[1907.38s] English:** so you're going to assume that your opponent is is also playing um like as as well as possible  
**Translation:** 

**[1913.38s] English:** a nash equilibrium approach because if they're not then you're just going to make more money right  
**Translation:** Vocabulary: equilibrium: 纳什均衡

**[1918.82s] English:** anything that deviates  
**Translation:** 

**[1920.00s] English:** it's like by definition the Nash equilibrium is the strategy that does the best in expectation  
**Translation:** Vocabulary: deviates: 偏离; expectation: 期望值

**[1925.56s] English:** and so if you're deviating from that then you're just they're going to lose money and since it's  
**Translation:** 

**[1930.00s] English:** a two-player zero-sum game that means you're going to make money so there's not an explicit  
**Translation:** Vocabulary: deviating: 偏离; explicit: 明确

**[1933.72s] English:** like objective function that maximizes the toughness of the spot they're put in you're  
**Translation:** 

**[1939.10s] English:** always this is not from like a self-play reinforcement learning perspective you're  
**Translation:** Vocabulary: reinforcement: 强化; toughness: 坚韧

**[1944.28s] English:** just trying to maximize winnings and the rest is implicit that's right yeah so we're what we're  
**Translation:** 

**[1949.18s] English:** actually trying to maximize is the expected value given that the opponent is playing optimally in  
**Translation:** Vocabulary: implicit: 含蓄的

**[1953.48s] English:** response to us now in practice what that ends up looking like is it's putting the opponent into  
**Translation:** 

**[1958.44s] English:** difficult situations where there's no obvious decision to be made so the the system doesn't  
**Translation:** 

**[1963.04s] English:** know anything about the difficulty of the situation not at all doesn't care yeah in my  
**Translation:** 

**[1968.06s] English:** head it was getting excited whenever it's making the other the opponent sweat okay so you're in  
**Translation:** 

**[1972.82s] English:** 2015 you didn't do as well so what's the journey from that to a system that in your mind could  
**Translation:** 

**[1979.14s] English:** happen in the future?  
**Translation:** 

**[1979.18s] English:** so 2015 we we got we beat pretty badly and we actually learned a lot from that competition and  
**Translation:** 

**[1986.82s] English:** in particular you know what became clear to me is that the way the humans were approaching the game  
**Translation:** 

**[1991.52s] English:** was very different from how the bot was approaching the game the bot would not be doing search it  
**Translation:** 

**[1997.70s] English:** would just be trying to compute you know it would do like months of self-play it would just be  
**Translation:** 

**[2001.64s] English:** playing against itself for months but then when it's actually playing the game it would just act  
**Translation:** 

**[2005.00s] English:** instantly and the humans when they're in a tough spot they would sit there and they would be  
**Translation:** 

**[2009.18s] English:** there and think for sometimes even like five minutes about whether they're going to call or  
**Translation:** 

**[2014.30s] English:** fold a hand and it became clear to me that that's there's a good chance that that's what missing  
**Translation:** 

**[2020.90s] English:** that's what's missing from our bot so i actually did some initial experiments to try to figure out  
**Translation:** 

**[2025.60s] English:** how much of a difference does this actually make and the difference was huge as a signal to the  
**Translation:** 

**[2030.00s] English:** human player how long you took to think no no i'm not saying that there were any timing tells i was  
**Translation:** 

**[2034.38s] English:** saying when the human like the bot would always act instantly it wouldn't try to come up with a  
**Translation:** 

**[2038.98s] English:** better strategy in real  
**Translation:** 

**[2040.00s] English:** time um over what it had pre-computed during training whereas the human like they have all  
**Translation:** 

**[2045.92s] English:** this intuition about how to play but they're also in real time leveraging their ability to think  
**Translation:** 

**[2052.36s] English:** just to search to plan um and coming up with an even better strategy than what their intuition  
**Translation:** Vocabulary: intuition: 直觉; leveraging: 利用

**[2056.84s] English:** would say so you're saying that there's you're doing that's what you mean by you're doing search  
**Translation:** 

**[2061.22s] English:** also you have an you have a intuition and search on top of that looking for a better solution yeah  
**Translation:** 

**[2068.74s] English:** that's that's what i mean by search that um instead of acting instantly you know a neural net  
**Translation:** 

**[2074.08s] English:** usually gives you a response in like 100 milliseconds or something depends on the size  
**Translation:** Vocabulary: milliseconds: 毫秒; neural: 神经

**[2078.00s] English:** of the of the net but if you can leverage extra computational resources you can possibly get a  
**Translation:** 

**[2084.24s] English:** much better outcome and we did some experiments in small scale versions of poker and what we what  
**Translation:** Vocabulary: computational: 计算的; leverage: 利用; poker: 扑克牌游戏

**[2092.22s] English:** we found was that if you do a little bit of search even just a little bit  
**Translation:** 

**[2097.70s] English:** it was the equivalent of making your you know your pre-computed strategy like you can kind of  
**Translation:** 

**[2104.14s] English:** think of it as your neural net a thousand times bigger with just a little bit of search and it  
**Translation:** 

**[2108.76s] English:** just like blew away all of the research that we had been working on and trying to like scale up  
**Translation:** 

**[2113.20s] English:** this like pre-computed solution it was dwarfed by the benefit that we got from search can you  
**Translation:** 

**[2120.12s] English:** just linger on what you mean by search here you're searching over a space of actions for your hand  
**Translation:** 

**[2127.70s] English:** how are you selecting the other hands to search over is so yeah randomly no it's all the other  
**Translation:** 

**[2134.94s] English:** hands that you could have so when you're playing no limit texas hold'em you've got two face down  
**Translation:** Vocabulary: selecting: 选择; texas: 德克萨斯

**[2138.50s] English:** cards and so that's 52 choose 2 1326 different combinations now that's actually a little bit  
**Translation:** 

**[2144.78s] English:** lower because there's face up cards in the middle and so you can eliminate those as well  
**Translation:** 

**[2147.88s] English:** but you're looking at like around a thousand different possible hands that you can have  
**Translation:** 

**[2151.54s] English:** and so when we're doing when the bot's doing search it's thinking explicitly there are these  
**Translation:** Vocabulary: explicitly: 明确地

**[2156.62s] English:** thousand different hands that you can have and so you're looking at like a thousand different  
**Translation:** 

**[2157.70s] English:** hands that i could have there are these thousand different hands that you could have  
**Translation:** 

**[2160.00s] English:** let me try to figure out what would it be a better strategy than what I've  
**Translation:** 

**[2163.78s] English:** pre-computed for these hands and your hands okay so that search how do you  
**Translation:** 

**[2171.84s] English:** fuse that with what the neural net is telling you or what the the train system  
**Translation:** 

**[2177.94s] English:** is telling you yeah so you kind of like that where the train system comes in is  
**Translation:** 

**[2183.50s] English:** is the value at the end so there's you only look so far ahead you look like  
**Translation:** 

**[2190.26s] English:** maybe you know one round ahead so if you're on the flop you're looking to the  
**Translation:** 

**[2193.10s] English:** start of the turn and at that point you can use the pre-computed solution to  
**Translation:** 

**[2198.92s] English:** figure out what are what's the value here of like of this strategy is it of a  
**Translation:** 

**[2204.44s] English:** single action essentially in that spot you're getting a value or is it the  
**Translation:** 

**[2209.36s] English:** value of the entire series of actions well it's kind of both  
**Translation:** 

**[2213.44s] English:** because you're trying to maximize the value for the hand that you have but in  
**Translation:** 

**[2218.18s] English:** the process in order to maximize the value of the hand that you have you have  
**Translation:** Vocabulary: maximize: 最大化

**[2221.36s] English:** to figure out what would I be doing with all these other hands as well okay but  
**Translation:** 

**[2225.08s] English:** you are you in the search I was going to the end of the game in the broadest we  
**Translation:** Vocabulary: broadest: 最广泛

**[2230.30s] English:** did so we only use search starting on the turn and then we searched all the  
**Translation:** 

**[2235.90s] English:** way to the end of the game the turn the river can we take it through the  
**Translation:** 

**[2241.58s] English:** terminology yeah there's four rounds of  
**Translation:** 

**[2243.32s] English:** poker so there's the pre-flop the flop the turn and the river and so we would  
**Translation:** Vocabulary: poker: 扑克; terminology: 术语

**[2247.76s] English:** start doing search halfway through the game now the first half of the game that  
**Translation:** 

**[2252.18s] English:** was all pre-computed it would just act instantly and then when it got to had  
**Translation:** Vocabulary: halfway: 中途

**[2256.08s] English:** the halfway point then it would always search to the end of the game now we  
**Translation:** 

**[2259.28s] English:** later improved this so wouldn't have to search all the way to the end of the  
**Translation:** 

**[2261.74s] English:** game it would actually search just a few moves ahead but that that came later and  
**Translation:** 

**[2267.14s] English:** that drastically reduced the number the amount of computational resources that we  
**Translation:** Vocabulary: computational: 计算的; drastically: 大幅度地

**[2270.58s] English:** needed but the moves because you can keep betting on  
**Translation:** 

**[2273.32s] English:** top of each other that's what you mean by move so like that's where you don't  
**Translation:** 

**[2276.98s] English:** just get one bet per turn or poker you  
**Translation:** 

**[2280.00s] English:** can have multiple arbitrary number of bets right right i'm trying to think like i'm gonna bet and  
**Translation:** Vocabulary: arbitrary: 任意的

**[2285.46s] English:** then what are you gonna do in response are you gonna raise me are you gonna call and then if  
**Translation:** 

**[2288.68s] English:** you raise what should i do so it's reasoning about that whole process up until the end of the game in  
**Translation:** 

**[2294.40s] English:** the case of labratus so for labratus what's the the most number of re-raises have you ever seen  
**Translation:** 

**[2299.32s] English:** uh you probably cap out at like five or something because at that point you're basically all in you  
**Translation:** 

**[2306.26s] English:** i mean is there like uh interesting patterns like that that you've seen that the game does like you  
**Translation:** 

**[2312.12s] English:** you'll have like alpha zero doing way more sacrifices than humans usually do is there  
**Translation:** Vocabulary: alpha: 阿尔法

**[2317.20s] English:** something like labratus was constantly re-raising or something like that that you noticed there was  
**Translation:** 

**[2323.32s] English:** there was something really interesting that we observed with labratus um so humans when they're  
**Translation:** Vocabulary: labratus: 实验对象

**[2328.32s] English:** playing poker they usually size their bets relative to the size of the pot so you know if the pot has  
**Translation:** 

**[2333.82s] English:** a hundred dollars in there maybe you bet like 75  
**Translation:** 

**[2336.24s] English:** dollars in there maybe you bet like 75 dollars in there maybe you bet like 75 dollars in there maybe you bet like 75  
**Translation:** 

**[2336.26s] English:** dollars or somewhere around somewhere between like 50 and 100 um and with labratus we gave it the  
**Translation:** 

**[2342.74s] English:** option to basically bet whatever it wanted it was actually really easy for us to say like oh if you  
**Translation:** 

**[2347.70s] English:** want you can bet like 10 times the pot and we didn't think it would actually do that it was just  
**Translation:** 

**[2351.30s] English:** like why not give it the option and then during the competition it actually started doing this  
**Translation:** 

**[2356.50s] English:** and by the way this is like a very last minute decision on our part to add this option and so we  
**Translation:** 

**[2360.66s] English:** did not we did not think the bot would do this and i was actually kind of worried when it did start to  
**Translation:** 

**[2366.24s] English:** do this like oh is this a problem like humans don't do this like is it screwing up um but it  
**Translation:** Vocabulary: screwing: 搞砸

**[2370.96s] English:** would put the humans into really difficult spots when it would do that because you know you could  
**Translation:** 

**[2376.00s] English:** imagine like you have the second best hand that's possible given the board and you're thinking like  
**Translation:** 

**[2380.80s] English:** oh you're in a really great spot here and suddenly the bot bets twenty thousand dollars into a you  
**Translation:** 

**[2385.04s] English:** know a thousand dollar pot and and it's basically saying like i have the best hand or i'm bluffing  
**Translation:** Vocabulary: bluffing: 虚张声势

**[2391.76s] English:** and you having the second best hand like now you get a really tough choice to make  
**Translation:** 

**[2396.24s] English:** and so the humans would sometimes think like five or ten minutes about like  
**Translation:** 

**[2400.00s] English:** Like, what do you do?  
**Translation:** 

**[2401.12s] English:** Should I call?  
**Translation:** 

**[2401.94s] English:** Should I fold?  
**Translation:** 

**[2403.20s] English:** And when I saw the humans, like, really struggling with that decision, like, that's when I realized, like, oh, actually, this is maybe a good thing to do after all.  
**Translation:** 

**[2409.54s] English:** And, of course, the system is a no that it's making, again, like we said, that it's putting them in a tough spot.  
**Translation:** 

**[2417.26s] English:** It's just that's part of the optimal, the game theory optimal.  
**Translation:** Vocabulary: optimal: 最优的

**[2421.22s] English:** Right.  
**Translation:** 

**[2421.48s] English:** From the bot's perspective, it's just doing the thing that's going to make it the most money.  
**Translation:** 

**[2425.12s] English:** And the fact that it's putting the humans in a difficult spot, like, that's just, you know, a side effect of that.  
**Translation:** 

**[2432.32s] English:** And this was, I think, the one thing.  
**Translation:** 

**[2435.06s] English:** I mean, there were a few things that the humans walked away from, but this was the number one thing that the humans walked away from the competition saying, like, we need to start doing this.  
**Translation:** 

**[2443.54s] English:** And now these over bets, what are called over bets, have become really common in high level poker play.  
**Translation:** Vocabulary: poker: 纸牌游戏

**[2448.88s] English:** Have you ever talked to somebody like Daniel Negreanu about this?  
**Translation:** 

**[2452.06s] English:** He seems to be a student of the game.  
**Translation:** 

**[2453.82s] English:** I did actually have a conversation.  
**Translation:** 

**[2455.12s] English:** I had a conversation with Daniel Negreanu once.  
**Translation:** 

**[2456.48s] English:** Yeah, I was I was visiting the Isle of Man to talk to poker stars about AI.  
**Translation:** 

**[2463.22s] English:** And Daniel Negreanu was there when we had dinner together with some other people.  
**Translation:** Vocabulary: negreanu: 尼格尔努

**[2467.72s] English:** And, yeah, he was really interested in it.  
**Translation:** 

**[2470.08s] English:** He mentioned that he was, like, you know, excited about, like, learning from these AIs.  
**Translation:** 

**[2474.38s] English:** So he wasn't scared.  
**Translation:** 

**[2475.30s] English:** He was excited.  
**Translation:** 

**[2476.30s] English:** He was excited.  
**Translation:** 

**[2477.08s] English:** And and he he honestly he wanted to play against the bot.  
**Translation:** 

**[2480.00s] English:** He thought he thought he had a decent chance of beating it.  
**Translation:** 

**[2483.08s] English:** I think, you know.  
**Translation:** 

**[2485.12s] English:** This is, like, several years ago when I think it was, like, not as clear to everybody that, you know, the AIs were taking over.  
**Translation:** 

**[2492.56s] English:** I think now people recognize that, like, if you're playing against a bot, there's, like, no chance that you have in a game like poker.  
**Translation:** 

**[2498.62s] English:** So consistently the bots will win.  
**Translation:** 

**[2501.02s] English:** The bots have heads up and in in other variants, too.  
**Translation:** 

**[2505.56s] English:** So multi multi six player Texas Hold'em, no limit Texas Hold'em, the bots win.  
**Translation:** 

**[2511.70s] English:** Yeah, that's the case.  
**Translation:** Vocabulary: texas: 德克萨斯州

**[2512.62s] English:** So I think there is some debate about, like, is it true for everything?  
**Translation:** 

**[2514.92s] English:** Every single variant of poker?  
**Translation:** 

**[2516.16s] English:** I think I think for every single variant of poker, if somebody  
**Translation:** 

**[2520.00s] English:** really put in the effort they can make an ai that would beat all humans at it um we've focused on  
**Translation:** 

**[2525.66s] English:** the most popular variants so heads up no limit texas hold them and then we follow that up with  
**Translation:** 

**[2530.06s] English:** um with uh six player poker as well where we managed to uh make a bot that beat expert human  
**Translation:** 

**[2535.74s] English:** players and i think even there now uh it's pretty clear that humans don't stand a chance see i would  
**Translation:** 

**[2541.12s] English:** love to hook up an ai system that looks at eeg like how like actually tries to optimize the  
**Translation:** Vocabulary: optimize: 优化

**[2548.78s] English:** toughness of the spot it puts a human in and i would i would love to see how different is that  
**Translation:** 

**[2553.94s] English:** from the game theory optimal so you try to maximize the heart rate of the human player  
**Translation:** Vocabulary: maximize: 最大化; optimal: 最优化; toughness: 困境

**[2558.86s] English:** like the freaking out over a long period of time i wonder if there's going to be different  
**Translation:** 

**[2565.78s] English:** strategies that emerge uh that are close in terms of effectiveness because something tells me you  
**Translation:** Vocabulary: effectiveness: 有效性; freaking: 狂躁

**[2572.02s] English:** could still be um achieve superhuman level performance by just making people sweat  
**Translation:** 

**[2577.62s] English:** i feel like  
**Translation:** 

**[2578.76s] English:** that there's a good chance that that is the case yeah if you're able to see like that it's like it's  
**Translation:** 

**[2584.44s] English:** like a decent proxy for score right right um and this is actually like the the common poker wisdom  
**Translation:** Vocabulary: poker: 纸牌游戏; proxy: 代理指标

**[2589.56s] English:** when they're telling where they're teaching players before they were bots and they were  
**Translation:** 

**[2593.32s] English:** trying to teach people how to play poker they would say like the key to the game is to put  
**Translation:** 

**[2596.76s] English:** your opponent into difficult spots it's a good um a good estimate for if you're making the right  
**Translation:** 

**[2601.08s] English:** decision so what else can you say about the fundamental role of search in poker and maybe  
**Translation:** 

**[2608.76s] English:** related to chess and go in these games um what's the role of search to solve in these games  
**Translation:** 

**[2616.92s] English:** yeah i think a lot of people under this is true for the general public and i think it's true for  
**Translation:** 

**[2621.48s] English:** the ai community a lot of people underestimate the importance of search for these kinds of  
**Translation:** 

**[2625.80s] English:** game ai results um an example of this is uh td gammon that came out in 1992 this was the  
**Translation:** Vocabulary: gammon: 背gam; underestimate: 低估

**[2633.48s] English:** the first real instance of a neural net being used in a game ai it's a landmark achievement it was  
**Translation:** 

**[2638.76s] English:** the inspiration for alpha zero  
**Translation:** Vocabulary: alpha: 阿尔法; landmark: 里程碑; neural: 神经

**[2640.00s] English:** and it used search. It used two-ply search to figure out its next move. You got Deep Blue.  
**Translation:** 

**[2646.38s] English:** There, it was very heavily focused on search, looking many, many moves ahead, farther than any  
**Translation:** 

**[2652.54s] English:** human could, and that was key for why it won. And then even with something like AlphaGo, I mean,  
**Translation:** 

**[2658.58s] English:** AlphaGo is commonly hailed as a landmark achievement for neural nets, and it is,  
**Translation:** 

**[2664.54s] English:** but there's also this huge component of search, Monte Carlo tree search to AlphaGo, that was key  
**Translation:** 

**[2669.94s] English:** absolutely essential for the AI to be able to beat top humans. I think a good example of this  
**Translation:** Vocabulary: carlo: 卡洛; monte: 蒙特

**[2676.48s] English:** is you look at the latest versions of AlphaGo, like it was called AlphaZero,  
**Translation:** 

**[2682.08s] English:** and there's this metric called ELO rating, where you can compare different humans,  
**Translation:** 

**[2687.22s] English:** and you can compare bots to humans. Now, a top human player is around 3,600 ELO,  
**Translation:** 

**[2693.00s] English:** maybe a little bit higher now. AlphaZero, the strongest version, is around 5,200 ELO.  
**Translation:** 

**[2699.84s] English:** But if you look at the top humans, you can see that the top humans are around 3,600 ELO,  
**Translation:** 

**[2699.92s] English:** and the top humans are around 3,600 ELO, and the top humans are around 3,600 ELO, and the top humans are around 3,600 ELO.  
**Translation:** 

**[2699.94s] English:** But if you take out the search that's being done at test time, and by the way, what I mean by search  
**Translation:** 

**[2705.14s] English:** is the planning ahead, the thinking of like, oh, if I move my, if I place this stone here,  
**Translation:** 

**[2710.24s] English:** and then he does this, and then you look like five moves ahead, and you see like what the board  
**Translation:** 

**[2713.80s] English:** state looks like. That's what I mean by search. If you take out the search that's done during the  
**Translation:** 

**[2719.12s] English:** game, the ELO rating drops to around 3,000. So even today, what, seven years after AlphaGo,  
**Translation:** 

**[2726.32s] English:** if you take out the Monte Carlo tree search that's being done,  
**Translation:** 

**[2729.68s] English:** at one playing against the human, the bots are not superhuman. Nobody has made a raw neural net  
**Translation:** 

**[2736.50s] English:** that is superhuman in Go. That's worth lingering on. That's quite profound.  
**Translation:** Vocabulary: lingering: 流连; profound: 深邃

**[2743.20s] English:** So without search, that just means looking at the next move and saying, this is the best move. So  
**Translation:** 

**[2749.94s] English:** having a function that estimates accurately what the best move is. That's right. Without search.  
**Translation:** 

**[2755.64s] English:** Yeah. And all these bots, they have what's called a policy network,  
**Translation:** 

**[2759.50s] English:** where it  
**Translation:** 

**[2760.00s] English:** will tell you this is what the neural net thinks is the next best move and it's kind of like a the  
**Translation:** 

**[2767.26s] English:** intuition that a human has you know the human looks at the board and and any go or chess master  
**Translation:** Vocabulary: intuition: 直觉; neural: 神经网络

**[2773.54s] English:** will be able to tell you like oh instantly here's what I think the right move is and the bot is able  
**Translation:** 

**[2778.42s] English:** to do the same thing but just like how a human grandmaster can make a better decision if they  
**Translation:** Vocabulary: grandmaster: 特级大师

**[2783.72s] English:** have more time to think when you add on this Monte Carlo tree search the bot is able to make a better  
**Translation:** 

**[2789.32s] English:** decision yeah I mean of course a human is doing something like search in their brain but it's not  
**Translation:** 

**[2794.94s] English:** I hesitate to draw a hard line but it's not like Monte Carlo tree search it's more like  
**Translation:** 

**[2802.68s] English:** sequential language model generation so it's like a different it's a the neural network is doing the  
**Translation:** Vocabulary: monte: 蒙特卡洛; sequential: 序列的

**[2809.84s] English:** searching and I wonder what the human brain is doing in terms of searching because you're doing  
**Translation:** 

**[2814.24s] English:** that like computation a human is computing they have intuition they've got  
**Translation:** Vocabulary: computation: 计算; computing: 计算

**[2818.66s] English:** you  
**Translation:** 

**[2819.32s] English:** they have a really strong ability to estimate you know amongst the top players of what is good  
**Translation:** 

**[2824.74s] English:** and not position without calculating all the details but they're still doing search in their  
**Translation:** 

**[2829.62s] English:** head but it's a different kind of search have you ever thought about like what is the difference  
**Translation:** 

**[2833.70s] English:** between the human the search that the human is performing versus what computers are doing  
**Translation:** 

**[2840.52s] English:** I have thought a lot about that and I think it's a really important question  
**Translation:** 

**[2843.60s] English:** so the AI in alpha and alphas in alpha go or any of these go AIs  
**Translation:** 

**[2849.32s] English:** they're all doing Monte Carlo tree search which is a particular kind of search and  
**Translation:** Vocabulary: alpha: 测试版本

**[2852.78s] English:** it it's actually a symbolic tabular search it uses the neural net to guide its search but it isn't  
**Translation:** 

**[2859.44s] English:** actually like full full-on neural net now that kind of search is very successful in these kinds  
**Translation:** Vocabulary: symbolic: 象征性的; tabular: 表格形式的

**[2867.12s] English:** of like perfect information board games like chess and go but if you take it to a game like poker for  
**Translation:** 

**[2871.54s] English:** example it doesn't work it can't it can't understand the concept of hidden information  
**Translation:** 

**[2876.10s] English:** it doesn't understand the balance that you have to strike between like  
**Translation:** 

**[2879.32s] English:** the amount that you  
**Translation:** 

**[2880.00s] English:** you're raising versus the amount that you're calling and in every one of these games you see  
**Translation:** 

**[2884.88s] English:** a different kind of search and the human brain is able to plan for all these different games  
**Translation:** 

**[2889.72s] English:** in a very general way um now i think that's one thing that we're missing from ai today and i think  
**Translation:** 

**[2894.58s] English:** it's a really important missing piece the ability to plan and reason more generally um across a wide  
**Translation:** 

**[2901.08s] English:** variety of different settings in a way where the general reasoning makes you better at each one of  
**Translation:** 

**[2908.02s] English:** the games yeah worse yeah so you can kind of think of it as like neural nets today they'll  
**Translation:** Vocabulary: neural: 神经网络

**[2913.00s] English:** give you like transformers for example are super general but you know they'll give you it'll output  
**Translation:** 

**[2918.16s] English:** an answer in like 100 milliseconds and if you tell it like oh you've got five minutes to give  
**Translation:** Vocabulary: milliseconds: 毫秒

**[2922.42s] English:** a decision you know feel free to take more time to make a better decision it's not going to know  
**Translation:** 

**[2926.06s] English:** what to do with that um but a human if you're playing a game like chess they're going to give  
**Translation:** 

**[2931.04s] English:** you a very different answer depending on if you say oh you got 100 milliseconds or you've got five  
**Translation:** 

**[2938.02s] English:** minutes i mean that people have started using right transformers and language models like the  
**Translation:** 

**[2941.70s] English:** in an iterative way that does improve the answer or like showing the work kind of kind of idea yeah  
**Translation:** 

**[2948.10s] English:** they got this thing called chain of thought reasoning and that's i think um super promising  
**Translation:** 

**[2952.10s] English:** right yeah i think and i think it's a good step in the right direction um i i would kind of like say  
**Translation:** 

**[2957.14s] English:** it's similar to monte carlo rollouts in in a game like chess there's a kind of search that you can  
**Translation:** 

**[2961.46s] English:** do where you're saying like i'm going to roll out my intuition and see like without really thinking  
**Translation:** 

**[2967.06s] English:** you know what are the better  
**Translation:** 

**[2968.02s] English:** decisions i can make farther down the path um what would i do if i just acted according to  
**Translation:** 

**[2972.32s] English:** intuition for the next 10 moves um and that gets you an improvement but i think that there's much  
**Translation:** Vocabulary: intuition: 直觉

**[2977.94s] English:** uh much richer kinds of of planning that we could do so when the broadest actually beat the poker  
**Translation:** 

**[2984.02s] English:** players what did that feel like what was that i mean actually on that day what were you feeling  
**Translation:** Vocabulary: broadest: 最广泛的; poker: 扑克

**[2989.74s] English:** like were you nervous i mean poker was one of the games that you thought like is not going to be  
**Translation:** 

**[2996.10s] English:** solvable because it's the human factor so  
**Translation:** Vocabulary: solvable: 可解决的

**[2998.02s] English:** uh at least in the narrative  
**Translation:** 

**[3000.00s] English:** is we tell ourselves the human factor so fundamental to the game of poker yeah the  
**Translation:** 

**[3005.44s] English:** lebronis competition was super stressful for me um also i mean i was working on this like basically  
**Translation:** 

**[3011.76s] English:** continuously for a year leading up to the competition i mean for me it became like very  
**Translation:** 

**[3016.16s] English:** clear like okay this is the search technique this is the approach that we need and then i spent a  
**Translation:** 

**[3020.32s] English:** year working on this pretty much like non-stop oh can we actually get into details like what  
**Translation:** 

**[3024.80s] English:** programming language is it written in what's some interesting uh implementation details that are  
**Translation:** 

**[3030.40s] English:** like fun slash painful yeah so one of the interesting things about lebronis is that we  
**Translation:** Vocabulary: implementation: 实现细节; lebronis: 勒布朗斯

**[3036.08s] English:** had no idea what the bar was to actually beat top humans yeah we could play against like our  
**Translation:** 

**[3040.80s] English:** prior bots and that kind of gives us some sense of like are we making progress are we going in  
**Translation:** 

**[3044.24s] English:** the right direction uh but we had no idea like what the bar actually was and so we threw a huge  
**Translation:** 

**[3049.36s] English:** amount of resources at trying to make the strongest bot possible so we used c plus plus it was  
**Translation:** 

**[3054.64s] English:** paid to us and we made a lot of money and we made a lot of money and we made a lot of money and we  
**Translation:** 

**[3054.76s] English:** made a lot of money and we made a lot of money and we made a lot of money and we made a lot of money  
**Translation:** 

**[3054.78s] English:** parallelized we were using i think like a thousand cpus um maybe maybe more actually um and you know  
**Translation:** 

**[3061.00s] English:** today that sounds like nothing but for a grad student back in 2016 that was a huge amount of  
**Translation:** 

**[3065.76s] English:** resources was still a lot for even any grad student today it's still tough to to get or even  
**Translation:** 

**[3072.24s] English:** to allow yourself to think in that in terms of scale at cmu at mit anything like that yeah and  
**Translation:** 

**[3079.68s] English:** you know talking about terabytes of memory um so it was a very paralyzed um and it had to be very  
**Translation:** 

**[3084.74s] English:** fast too because the more games that you could simulate uh the stronger the bot would be so is  
**Translation:** Vocabulary: paralyzed: 僵化; simulate: 模拟; terabytes: 千兆字节

**[3090.42s] English:** there some like john carmac style like efficiencies you had to come up with like an efficient way to  
**Translation:** 

**[3097.38s] English:** represent the hand all that kind of stuff there are all sorts of optimizations that i had to make  
**Translation:** Vocabulary: efficiencies: 效率; optimizations: 优化

**[3102.26s] English:** to try to get this thing to run as fast as possible they were like how do you minimize  
**Translation:** 

**[3105.86s] English:** the latency how do you like you know package things together so that like you minimize the  
**Translation:** Vocabulary: latency: 延迟

**[3109.94s] English:** amount of communication between the different nodes um how do you like optimize the options  
**Translation:** 

**[3114.70s] English:** so that you can you know try to squeeze out more and more from the game that you're actually playing  
**Translation:** 

**[3120.00s] English:** all these kinds of different decisions that I, you know, had to make.  
**Translation:** 

**[3123.76s] English:** Just a fun question.  
**Translation:** 

**[3125.14s] English:** What IDE did you use for C++ at the time?  
**Translation:** 

**[3130.62s] English:** I think I used Visual Studio, actually.  
**Translation:** 

**[3132.90s] English:** Okay.  
**Translation:** 

**[3133.28s] English:** Yeah.  
**Translation:** 

**[3133.58s] English:** Does that still carry through to today?  
**Translation:** 

**[3135.62s] English:** VS Code is what I use today.  
**Translation:** 

**[3137.14s] English:** It seems like it's pretty popular.  
**Translation:** 

**[3137.90s] English:** It's the community, basically, conversion on.  
**Translation:** 

**[3140.00s] English:** Okay, cool.  
**Translation:** 

**[3140.52s] English:** So you got this super optimized C++ system,  
**Translation:** Vocabulary: optimized: 优化过的

**[3144.86s] English:** and then you show up to the day of competition.  
**Translation:** 

**[3148.18s] English:** Yeah.  
**Translation:** 

**[3148.42s] English:** So humans versus machine.  
**Translation:** 

**[3152.08s] English:** How did it feel throughout the day?  
**Translation:** 

**[3154.42s] English:** Super stressful.  
**Translation:** 

**[3156.00s] English:** I mean, I thought going into it that we had like a 50-50 chance.  
**Translation:** 

**[3160.12s] English:** Basically, I thought if they play in a totally normal style,  
**Translation:** 

**[3164.08s] English:** I think we'll squeak out a win.  
**Translation:** Vocabulary: squeak: 勉强获胜

**[3165.58s] English:** But there's always a chance that they can find some weakness in the bot.  
**Translation:** 

**[3169.94s] English:** And if they do, and we're playing like for 20 days, 120,000 hands of poker.  
**Translation:** Vocabulary: poker: 德州扑克

**[3173.72s] English:** They have a lot of time to find weaknesses in the system.  
**Translation:** 

**[3176.20s] English:** And if they do, we're going to get crushed.  
**Translation:** 

**[3178.42s] English:** And that's actually what happened in the previous competition.  
**Translation:** 

**[3180.42s] English:** The humans, you know, they started out, it wasn't like they were winning from the start.  
**Translation:** 

**[3184.42s] English:** But then they found these weaknesses that they could take advantage of.  
**Translation:** 

**[3187.42s] English:** And for the next, you know, like 10 days, they were just crushing the bot, stealing money from it.  
**Translation:** 

**[3192.42s] English:** What were the weaknesses they found?  
**Translation:** 

**[3194.42s] English:** Like maybe overbetting was effective, that kind of stuff.  
**Translation:** Vocabulary: overbetting: 过度下注

**[3196.42s] English:** So certain betting strategies worked.  
**Translation:** 

**[3198.42s] English:** What they found is, yeah, overbetting, like betting certain amounts,  
**Translation:** 

**[3202.42s] English:** the bot would have a lot of trouble dealing with those sizes.  
**Translation:** 

**[3204.42s] English:** Yeah.  
**Translation:** 

**[3204.92s] English:** And then also when the bot got into really difficult all-in situations,  
**Translation:** 

**[3210.92s] English:** it wasn't able to, because it wasn't doing search,  
**Translation:** 

**[3214.92s] English:** it had to clump different hands together and it wouldn't, it would treat them identically.  
**Translation:** 

**[3218.92s] English:** Yeah.  
**Translation:** Vocabulary: clump: 聚集成团; identically: 一模一样

**[3219.92s] English:** And so it wouldn't be able to distinguish, you know, like having a king high flush versus an ace high flush.  
**Translation:** 

**[3225.92s] English:** And in some situations that really matters a lot.  
**Translation:** Vocabulary: flush: 同花顺

**[3227.92s] English:** And so they could put the bot into those situations and then the bot would just bleed money.  
**Translation:** 

**[3231.92s] English:** Clever humans.  
**Translation:** 

**[3232.92s] English:** Yeah.  
**Translation:** 

**[3233.92s] English:** Okay.  
**Translation:** 

**[3234.92s] English:** I didn't realize it was over 20 days.  
**Translation:** 

**[3236.92s] English:** So...  
**Translation:** 

**[3240.00s] English:** What were the humans like over those 20 days and what was the bot like so we had set up the competition?  
**Translation:** 

**[3246.34s] English:** you know, like I said, there was $200,000 in prize money and  
**Translation:** 

**[3249.66s] English:** They would get paid a fraction of that depending on how well they did relative to each other  
**Translation:** 

**[3253.82s] English:** Yeah, so I was kind of hoping that they wouldn't work together to try to find weaknesses in the bot  
**Translation:** 

**[3258.06s] English:** But they enter the competition with their like number one objective being to beat the bot and they didn't care about like individual glory  
**Translation:** 

**[3264.80s] English:** They were like we're all gonna work as a team to try to take down this bot  
**Translation:** 

**[3267.52s] English:** Yeah, and so they immediately started comparing notes. What they would do is  
**Translation:** 

**[3272.46s] English:** They would coordinate looking at different parts of the strategy to try to try to you know, find out weaknesses  
**Translation:** 

**[3279.38s] English:** And then at the end of the day, we actually sent them a log of all the hands that were played and what?  
**Translation:** 

**[3284.90s] English:** Cards the bot had on each of those hands. Oh, wow. Yeah, that's that's gutsy  
**Translation:** Vocabulary: gutsy: 大胆的

**[3289.12s] English:** Yeah, it was honestly and I'm not sure why we did that in retrospect  
**Translation:** 

**[3291.90s] English:** But I mean, I'm glad we did it because we ended up winning anyway  
**Translation:** Vocabulary: retrospect: 回顾

**[3294.66s] English:** But that if you've ever played poker before like that  
**Translation:** 

**[3297.52s] English:** Is golden information I mean, you know, usually when you play poker you see about a third of the hands to show down  
**Translation:** Vocabulary: poker: 纸牌游戏

**[3303.30s] English:** And to just hand them all the cards that the bot had on every single hand that was  
**Translation:** 

**[3309.54s] English:** Just just a goldmine for them  
**Translation:** Vocabulary: goldmine: 财富之源

**[3311.34s] English:** Yeah  
**Translation:** 

**[3311.68s] English:** And so then they would review the hands and try to see like okay could they find patterns in the bot the weaknesses and could  
**Translation:** 

**[3317.14s] English:** They then then they would coordinate and study together and try to figure out okay now  
**Translation:** 

**[3321.46s] English:** This person's gonna explore this part of the strategy for weaknesses. This person's gonna explore this part of the strategy for weaknesses  
**Translation:** 

**[3327.52s] English:** It's a kind of psychological warfare showing them the hands  
**Translation:** 

**[3331.26s] English:** Yeah, I mean, I'm sure you didn't think of it that way  
**Translation:** 

**[3333.78s] English:** But like doing that means you're confident in the possibility to win. Well, that's that's one way of putting it  
**Translation:** 

**[3339.92s] English:** I wasn't super confident. Yeah, so  
**Translation:** 

**[3342.74s] English:** You know going in like I said, I think I had like 50 50 odds on us winning the  
**Translation:** 

**[3347.08s] English:** When we actually when we announced the competition  
**Translation:** 

**[3349.20s] English:** The poker community decided to gamble on who would win and their initial odds against us were like four to one  
**Translation:** 

**[3354.96s] English:** they they were really convinced that the humans were gonna  
**Translation:** Vocabulary: gamble: 赌博

**[3357.52s] English:** pull out a win  
**Translation:** 

**[3359.52s] English:** the  
**Translation:** 

**[3360.00s] English:** bot ended up winning for three days straight and even then after three days  
**Translation:** 

**[3364.50s] English:** the betting odds were still just 50-50 and then at that point it started to  
**Translation:** 

**[3370.80s] English:** look like the humans were coming back they started to like you know but but  
**Translation:** 

**[3375.06s] English:** poker is a very high variance game and I think what happened is like they thought  
**Translation:** Vocabulary: variance: 波动性

**[3379.80s] English:** that they spotted some weaknesses that weren't actually there and then around  
**Translation:** 

**[3383.16s] English:** day eight it was just very clear that they were getting absolutely crushed and  
**Translation:** 

**[3387.78s] English:** and from that point for I mean for a while there I was super stressed out  
**Translation:** 

**[3391.38s] English:** thinking like oh my god the humans are coming back and we're just they've found  
**Translation:** 

**[3394.68s] English:** weaknesses and now we're just gonna lose the whole thing but no it ended up going  
**Translation:** 

**[3398.76s] English:** in the other direction and the bot ended up like crushing them in the long run  
**Translation:** 

**[3401.90s] English:** how did it feel at the end like as a human being what it as a person who  
**Translation:** 

**[3408.28s] English:** loves appreciates the beauty of the game of poker and as a person who appreciates  
**Translation:** 

**[3413.18s] English:** the beauty of AI is there did you feel a certain  
**Translation:** 

**[3417.78s] English:** kind of way about it uh I felt a lot a lot of things man uh I mean at that  
**Translation:** 

**[3422.90s] English:** point in my life I had spent five years working on this projects and it was a  
**Translation:** 

**[3428.26s] English:** huge sense of accomplishment I mean to spend five years working on something  
**Translation:** 

**[3431.26s] English:** and finally see it succeed yeah I wouldn't trade that for anything in the  
**Translation:** 

**[3435.12s] English:** world yeah because it's a that's a real benchmark it's not like getting some  
**Translation:** Vocabulary: benchmark: 衡量标准

**[3441.28s] English:** percent accuracy on a data set this is like real this is real world yeah it's  
**Translation:** 

**[3446.70s] English:** it's just a game  
**Translation:** 

**[3447.78s] English:** but it's also a game that means a lot to a lot of people.  
**Translation:** 

**[3450.74s] English:** And this is humans doing their best to beat the machine.  
**Translation:** 

**[3453.44s] English:** So this is a real benchmark, unlike anything else.  
**Translation:** 

**[3456.46s] English:** Yeah, and I mean, this is what I had been dreaming about  
**Translation:** 

**[3459.36s] English:** since I was like 16 playing poker with my friends in high school.  
**Translation:** 

**[3463.16s] English:** The idea that you could find a strategy,  
**Translation:** Vocabulary: poker: 纸牌游戏

**[3466.72s] English:** approximate the Nash equilibrium,  
**Translation:** 

**[3468.02s] English:** be able to beat all the poker players in the world with it.  
**Translation:** Vocabulary: approximate: 近似; equilibrium: 平衡

**[3471.02s] English:** So to actually see that come to fruition and be realized,  
**Translation:** 

**[3475.44s] English:** that was kind of magical.  
**Translation:** 

**[3477.78s] English:** Yeah, especially money is on the line.  
**Translation:** 

**[3480.00s] English:** too it's a different it's different than chess and that aspect like people get that's why you  
**Translation:** 

**[3486.20s] English:** want to look at betting markets if you want to actually understand what people really think  
**Translation:** 

**[3491.36s] English:** and in the same sense poker it's really high stakes because it's money and to solve that game  
**Translation:** 

**[3496.74s] English:** that's that's an amazing accomplishment so the leap from that to multi-way six-player poker  
**Translation:** 

**[3503.74s] English:** what's how difficult does that jump and what are some interesting differences between heads up  
**Translation:** 

**[3509.62s] English:** poker and and multi-way poker yeah so i mentioned you know nash equilibrium in two-player zero-sum  
**Translation:** 

**[3515.70s] English:** games if you play that strategy you are guaranteed to not lose an expectation no matter what your  
**Translation:** Vocabulary: expectation: 预期

**[3520.68s] English:** opponent does now once you go to six-player poker you're no longer playing a two-player zero-sum  
**Translation:** 

**[3524.80s] English:** game and so there was a lot of debate among the academic community and among the poker community  
**Translation:** 

**[3528.76s] English:** about how well these techniques would extend beyond just two-player heads up poker now  
**Translation:** 

**[3534.88s] English:** what i had come to realize is that um  
**Translation:** 

**[3538.74s] English:** the  
**Translation:** 

**[3539.60s] English:** techniques actually i thought really would extend to six-player poker because even though in theory  
**Translation:** 

**[3544.48s] English:** they don't give you these guarantees outside of two-player zero-sum games in practice it still  
**Translation:** 

**[3549.70s] English:** gives you a really strong strategy now there were a lot of complications that would come up with  
**Translation:** Vocabulary: guarantees: 保证

**[3554.92s] English:** six-player poker besides like the game theoretic aspect i mean for one the game is just exponentially  
**Translation:** 

**[3560.40s] English:** larger um so the main thing that allowed us to go from two-player to six-player was the idea of  
**Translation:** Vocabulary: exponentially: 成倍地; theoretic: 理论的

**[3567.72s] English:** depth limited search so  
**Translation:** 

**[3568.72s] English:** i said before like you know we would do search we would plan out the bot would plan out like what  
**Translation:** 

**[3574.48s] English:** what it's going to do next and for the next several moves and in libradis that search was done  
**Translation:** 

**[3579.02s] English:** extending all the way to the end of the game so it would have to start um it from from the turn  
**Translation:** Vocabulary: libradis: 丽丝拉迪斯

**[3586.22s] English:** onwards like looking maybe 10 moves ahead um it would have to figure out what it was doing for all  
**Translation:** 

**[3592.34s] English:** those moves now when you get to six-player poker it can't do that exhaustive search anymore because  
**Translation:** Vocabulary: exhaustive: 详尽; onwards: 向前; poker: 扑克

**[3597.36s] English:** the game is just way too large so it's just hard to do that but it's a good idea to do that so i said  
**Translation:** 

**[3598.60s] English:** large.  
**Translation:** 

**[3600.00s] English:** but by only having to look a few moves ahead and then stopping there and substituting a value  
**Translation:** 

**[3605.60s] English:** estimate of like how good is that strategy at that point then we're able to do a much more scalable  
**Translation:** Vocabulary: scalable: 可扩展的; substituting: 替代

**[3611.28s] English:** form of search is there something cool looking at the paper right now is there something cool  
**Translation:** 

**[3617.76s] English:** in the paper in terms of graphics a game tree traversa via monte carlo i think if you go down  
**Translation:** 

**[3623.20s] English:** a bit uh uh figure one an example of equilibrium selection problem ooh so yeah uh what do we know  
**Translation:** 

**[3631.36s] English:** about equilibria when is there's multiple players so when you go outside of two players zero sum  
**Translation:** Vocabulary: equilibria: 多重平衡; equilibrium: 均衡

**[3638.00s] English:** so a national equilibrium is a set of strategies like one strategy for each player  
**Translation:** 

**[3641.60s] English:** where no player has an incentive to switch to a different strategy  
**Translation:** Vocabulary: incentive: 动机

**[3646.48s] English:** and so you can kind of think of it as like imagine you have a game where there's a ring  
**Translation:** 

**[3651.44s] English:** that's actually the visual here you've got a  
**Translation:** 

**[3653.92s] English:** and the object of the game is to be as far away from the other players as possible.  
**Translation:** 

**[3659.76s] English:** A Nash Equilibrium is for all the players to be spaced equally apart around this ring.  
**Translation:** 

**[3664.40s] English:** But there's infinitely many different Nash Equilibria, right? There's infinitely many ways  
**Translation:** 

**[3667.92s] English:** to space four dots along a ring. And if every single player independently computes a Nash  
**Translation:** Vocabulary: computes: 计算; independently: 独立地; infinitely: 无穷地

**[3674.80s] English:** Equilibrium, then there's no guarantee that the joint strategy that they're all playing  
**Translation:** 

**[3679.44s] English:** is going to be a Nash Equilibrium. They're just going to be random dots scattered along this ring  
**Translation:** 

**[3685.44s] English:** rather than four coordinated dots being equally spaced apart. Is it possible to sort of optimally  
**Translation:** 

**[3690.24s] English:** do this kind of selection, to do the selection of the equilibria you're chasing? So is there  
**Translation:** Vocabulary: coordinated: 协调一致; optimally: 最优化地

**[3698.00s] English:** like a meta problem to be solved here? So the meta problem is, in some sense,  
**Translation:** 

**[3703.68s] English:** how do you understand the Nash Equilibria that the other players are going to play?  
**Translation:** 

**[3708.48s] English:** And  
**Translation:** 

**[3709.68s] English:** and even if you do that, again, there's no guarantee that you're going to win. So, you know,  
**Translation:** 

**[3714.56s] English:** if you're playing, if you're playing Risk, like I said, and all the other players decide to team up  
**Translation:** 

**[3720.00s] English:** against you, you're going to lose. Nash equilibrium doesn't help you there. And so there is this big  
**Translation:** 

**[3725.84s] English:** debate about whether Nash equilibrium and all these techniques that compute it are even useful  
**Translation:** 

**[3730.32s] English:** once you go outside of two-player zero-sum games. Now, I think for many games, there is a valid  
**Translation:** 

**[3735.82s] English:** criticism here. And I think when we talk about, when we go to something like diplomacy, we run  
**Translation:** 

**[3740.10s] English:** into this issue that the approach of trying to approximate a Nash equilibrium doesn't really  
**Translation:** Vocabulary: approximate: 近似; diplomacy: 外交

**[3746.58s] English:** work anymore. But it turns out that in six-player poker, because six-player poker is such an  
**Translation:** 

**[3752.06s] English:** adversarial game where none of the players really try to work with each other, the techniques that  
**Translation:** Vocabulary: adversarial: 敌对的; poker: 扑克牌游戏

**[3758.84s] English:** were used in two-player poker to try to approximate an equilibrium, those still end up working in  
**Translation:** 

**[3763.22s] English:** practice in six-player poker as well. There's some deep way in which six-player poker is just  
**Translation:** Vocabulary: equilibrium: 平衡状态

**[3769.52s] English:** a bunch of heads-up poker games in one. It's embedded in it. So the competitiveness,  
**Translation:** 

**[3776.58s] English:** um, is more fundamental to poker than the cooperation.  
**Translation:** Vocabulary: competitiveness: 竞争性; embedded: 嵌入

**[3781.74s] English:** Right. Yeah. Poker is just such an adversarial game. There's no real cooperation. In fact,  
**Translation:** 

**[3785.52s] English:** you're not even allowed to cooperate in poker. It's considered collusion. It's against the rules.  
**Translation:** Vocabulary: collusion: 勾结; cooperate: 合作

**[3789.74s] English:** Um, and so for that reason, the techniques end up working really well. And I think that's  
**Translation:** 

**[3794.26s] English:** true more broadly in extremely adversarial games in general.  
**Translation:** 

**[3798.26s] English:** But that's sort of in practice versus being able to prove something.  
**Translation:** 

**[3802.16s] English:** That's right. Nobody has a proof that that's the case. And it could be that,  
**Translation:** 

**[3805.48s] English:** that six-player poker is just a bunch of heads-up poker.  
**Translation:** 

**[3806.58s] English:** Poker belongs to some class of games where approximating an equilibrium through self-play  
**Translation:** Vocabulary: approximating: 近似求解

**[3812.66s] English:** provably works well. Um, and, you know, there are other classes of games beyond just two-player  
**Translation:** 

**[3818.46s] English:** zero-sum where this is proven to work well. So there are these, you know, kinds of games called  
**Translation:** Vocabulary: provably: 可以证明地

**[3822.48s] English:** potential games, which I won't go into. It's kind of like a complicated concept. But, um,  
**Translation:** 

**[3827.30s] English:** there are classes of games where, uh, this approach to approximating an equilibrium is  
**Translation:** 

**[3833.36s] English:** proven to work well. Now, six-player poker is not known to be a good game. It's not known to be a  
**Translation:** 

**[3836.58s] English:** belong to one of those classes, but it is possible that there is some classic games where  
**Translation:** 

**[3840.00s] English:** It either provably performs well or provably performs not that badly.  
**Translation:** 

**[3844.34s] English:** So what are some interesting things about Pluribus that was able to achieve human-level performance or superhuman-level performance on the six-player version of poker?  
**Translation:** Vocabulary: pluribus: 多人扑克

**[3855.94s] English:** Personally, I think the most interesting thing about Pluribus is that it was so much cheaper than Libratus.  
**Translation:** 

**[3862.00s] English:** I mean, Libratus, if you had to put a price tag on the computational resources that went into it, I would say the final training run took about $100,000.  
**Translation:** Vocabulary: computational: 计算的

**[3870.80s] English:** You go to Pluribus, the final training run would cost like less than $150 on AWS.  
**Translation:** 

**[3877.94s] English:** Is this normalized to computational inflation?  
**Translation:** 

**[3881.60s] English:** So meaning, does this just have to do with the fact that Pluribus was trained like a year later?  
**Translation:** 

**[3889.12s] English:** No, no, no.  
**Translation:** 

**[3889.52s] English:** I mean, first of all, yeah.  
**Translation:** 

**[3892.00s] English:** Computing resources are getting cheaper every day, but you're not going to see a thousand-fold decrease in the computational resources over two years or even anywhere close to that.  
**Translation:** Vocabulary: computing: 计算资源

**[3902.08s] English:** The real improvement was algorithmic improvements, and in particular, the ability to do depth-limited search.  
**Translation:** 

**[3908.42s] English:** So does depth-limited search also work for Libratus?  
**Translation:** Vocabulary: algorithmic: 算法相关的

**[3912.38s] English:** Yeah, yes.  
**Translation:** 

**[3913.14s] English:** So where this depth-limited search came from is I developed this technique and ran it on two-player poker first.  
**Translation:** Vocabulary: poker: 纸牌游戏

**[3921.18s] English:** And that...  
**Translation:** 

**[3921.98s] English:** Reduced the computational resources needed to make an AI that was superhuman from, you know, $100,000 for Libratus to something you could train on your laptop.  
**Translation:** Vocabulary: libratus: Libratus

**[3931.64s] English:** What do you learn from that?  
**Translation:** 

**[3934.42s] English:** From that discovery?  
**Translation:** 

**[3936.60s] English:** What I would take away from that is that algorithmic improvements really do matter.  
**Translation:** 

**[3940.12s] English:** How would you describe the more general case of limited depth search?  
**Translation:** 

**[3944.74s] English:** So it's basically constraining the scale temporal or in some other way of the computation you're doing.  
**Translation:** 

**[3951.46s] English:** In some clever...  
**Translation:** Vocabulary: computation: 计算; constraining: 限制; temporal: 时间的

**[3951.98s] English:** Clever way.  
**Translation:** 

**[3953.30s] English:** So, like, with...  
**Translation:** 

**[3954.88s] English:** Like, how else can you significantly constrain computation, right?  
**Translation:** 

**[3959.36s] English:** Well, I think...  
**Translation:** Vocabulary: constrain: 限制

**[3960.00s] English:** idea is that we want to be able to leverage search as much as possible and the way that we were doing  
**Translation:** 

**[3965.04s] English:** it in the broadest required us to search all the way to the end of the game now if you're playing  
**Translation:** Vocabulary: broadest: 范围最广; leverage: 利用

**[3969.04s] English:** a game like chess the idea that you're going to search always to the end of the game is kind of  
**Translation:** 

**[3973.12s] English:** unimaginable right like there's just so many situations where you just won't be able to use  
**Translation:** Vocabulary: unimaginable: 难以想象

**[3976.24s] English:** search in that case or the cost would be um you know prohibitive and this technique allowed us  
**Translation:** 

**[3983.84s] English:** to leverage search and without having to pay such a huge computational cost for it and be able to  
**Translation:** Vocabulary: computational: 计算的; prohibitive: 昂贵的

**[3989.84s] English:** apply it more broadly so to what degree did you use neural nets for uh labratus and pluribus and  
**Translation:** 

**[3996.64s] English:** more generally what role do neural nets have to play in um in superhuman level performance in  
**Translation:** Vocabulary: neural: 神经; pluribus: 多者

**[4003.52s] English:** poker so we actually did not use neural nets at all for labratus or pluribus and a lot of people  
**Translation:** 

**[4010.64s] English:** found this surprising back in 2017 i think they found it surprising today um that we were able  
**Translation:** Vocabulary: labratus: 实验对象

**[4015.92s] English:** to do this without using any neural nets um and  
**Translation:** 

**[4019.84s] English:** i think the reason for that i mean i think neural nets are um incredibly powerful and the techniques  
**Translation:** 

**[4026.00s] English:** that are used today even for poker ais do rely uh quite heavily on neural nets um but it wasn't  
**Translation:** 

**[4032.56s] English:** the main challenge for poker like i think what neural nets are really good for if you're in a  
**Translation:** 

**[4037.76s] English:** situation where finding features for a value function is really difficult then neural nets  
**Translation:** 

**[4043.84s] English:** are really powerful and this was the problem in go right like the problem in go was that or the  
**Translation:** 

**[4049.84s] English:** problem in go at least was that nobody had a good way of looking at a board and figuring out who  
**Translation:** 

**[4054.88s] English:** was winning or describing um through a simple algorithm who was winning or losing and so there  
**Translation:** 

**[4060.96s] English:** neural nets were super helpful because you could just feed in a ton of different board positions  
**Translation:** 

**[4065.68s] English:** into this neural net and it would be able to predict then who was winning or losing but in poker  
**Translation:** Vocabulary: poker: 扑克牌游戏

**[4071.04s] English:** the features weren't the challenge the challenge was how do you design a scalable algorithm  
**Translation:** 

**[4077.60s] English:** that would allow you to find this  
**Translation:** Vocabulary: algorithm: 算法; scalable: 可扩展的

**[4079.84s] English:** back  
**Translation:** 

**[4080.00s] English:** strategy, that would understand that you have to bluff with the right probability.  
**Translation:** Vocabulary: bluff: 虚张声势

**[4085.66s] English:** So can that be somehow incorporated into the value function, the complexity of poker that  
**Translation:** 

**[4093.54s] English:** you've described?  
**Translation:** Vocabulary: complexity: 复杂性

**[4094.82s] English:** Yeah.  
**Translation:** 

**[4095.12s] English:** So the way the value functions work in poker, like the latest and greatest poker AIs, they  
**Translation:** 

**[4099.36s] English:** do use neural nets for the value function.  
**Translation:** 

**[4101.94s] English:** The way it's done is very different from how it's done in a game like chess or go, because  
**Translation:** 

**[4106.78s] English:** in poker, you have to reason about beliefs.  
**Translation:** 

**[4111.20s] English:** And so the value of a state depends on the beliefs that players have about what the different  
**Translation:** 

**[4118.22s] English:** cards are.  
**Translation:** 

**[4119.28s] English:** Like if you have pocket aces, then whether that's a really, really good hand or just  
**Translation:** 

**[4124.74s] English:** an okay hand depends on whether you know I have pocket aces, right?  
**Translation:** 

**[4128.56s] English:** If you know that I have pocket aces, then if I bet, you're going to fold immediately.  
**Translation:** 

**[4133.44s] English:** But if you think that I have a really bad hand, then I could bet with pocket aces.  
**Translation:** 

**[4136.78s] English:** And make a ton of money.  
**Translation:** 

**[4138.46s] English:** So the value function in poker these days takes the beliefs as an input, which is very  
**Translation:** 

**[4145.72s] English:** different from how chess and go AIs work.  
**Translation:** 

**[4148.86s] English:** So as a person who appreciates the game, who do you think is the greatest poker player  
**Translation:** 

**[4155.28s] English:** of all time?  
**Translation:** 

**[4156.86s] English:** That's a tough question.  
**Translation:** 

**[4159.06s] English:** Can an AI help answer that question?  
**Translation:** 

**[4160.92s] English:** Can you actually analyze the quality of play, right?  
**Translation:** 

**[4164.56s] English:** So the chess engines can...  
**Translation:** 

**[4166.78s] English:** Can give estimates of the quality of play, right?  
**Translation:** 

**[4172.88s] English:** I wonder if there's a...  
**Translation:** 

**[4174.08s] English:** Is there an ELO rating type of system for poker?  
**Translation:** 

**[4177.56s] English:** I suppose you could, but there's just not enough.  
**Translation:** 

**[4180.88s] English:** You would have to play a lot of games, right?  
**Translation:** 

**[4183.50s] English:** A very large number of games, like more than you would in chess.  
**Translation:** 

**[4186.30s] English:** The deterministic game makes it easier to estimate ELO, I think.  
**Translation:** 

**[4190.14s] English:** I think it is much harder to estimate something like ELO rating in poker.  
**Translation:** Vocabulary: deterministic: 确定性的; poker: 纸牌游戏

**[4194.18s] English:** I think it's doable.  
**Translation:** 

**[4195.12s] English:** The problem is that the game is very high.  
**Translation:** Vocabulary: doable: 可行的

**[4196.78s] English:** It's very high variance.  
**Translation:** 

**[4197.74s] English:** So you could play...  
**Translation:** Vocabulary: variance: 方差

**[4199.08s] English:** You could be profitable.  
**Translation:** 

**[4199.94s] English:** You could be profitable.  
**Translation:** 

**[4200.00s] English:** in poker for a year and you could actually be a bad player just because the variance is so high  
**Translation:** 

**[4205.04s] English:** i mean you've got top professional poker players that would lose for a year  
**Translation:** 

**[4208.88s] English:** just because they're on a really bad um bad streak yeah so for elo you have to have a nice clean way  
**Translation:** 

**[4215.28s] English:** of saying if player a played player b and a beats b that says something that's a signal  
**Translation:** Vocabulary: streak: 连败

**[4222.64s] English:** in poker that's a very noisy signal it's a very noisy signal now there is a signal there and so  
**Translation:** 

**[4226.72s] English:** you could do this this calculation it would just be much harder um but the same way that ai's have  
**Translation:** 

**[4233.60s] English:** now taken over chess and you know all the top professional chess players train with with ai's  
**Translation:** 

**[4240.32s] English:** the same is true for poker the game has become a very computational um people train with ai's  
**Translation:** Vocabulary: computational: 计算相关的

**[4247.36s] English:** to try to find out where they're making mistakes um try to learn from the ai's to improve their  
**Translation:** 

**[4251.44s] English:** strategy uh so now yeah so the game has been  
**Translation:** 

**[4256.56s] English:** represented by a lot of people and i think that's a really good example of how the game has been  
**Translation:** 

**[4256.64s] English:** represented by a lot of people and i think that's a really good example of how the game has been  
**Translation:** 

**[4256.72s] English:** evolutionized in the past five years by by the development of ai in this sport the skill with  
**Translation:** 

**[4261.52s] English:** which you avoided the question of the greatest of all time was impressive so my feeling is that it's  
**Translation:** Vocabulary: evolutionized: 进化

**[4266.24s] English:** a difficult it's a difficult question because just like in chess where you can't really compare  
**Translation:** 

**[4272.08s] English:** magnus carlson today to gary kasparov um because the game has evolved so much um the poker players  
**Translation:** Vocabulary: carlson: 卡尔森; kasparov: 卡斯帕罗夫; magnus: 马格努斯

**[4279.36s] English:** today are so far beyond the the skills of like people that were playing even 10 or 20 years ago  
**Translation:** 

**[4286.72s] English:** um so you look at the the kinds of like all-stars that were on espn at like the height of the poker  
**Translation:** 

**[4291.92s] English:** boom pretty much all those players are actually not that good at the game today at least at least  
**Translation:** 

**[4297.60s] English:** the the strategy aspect i mean they might still be good at like reading the player at the other  
**Translation:** 

**[4302.48s] English:** side of the table and trying to figure out like are they bluffing or not but in terms of the  
**Translation:** 

**[4306.16s] English:** actual like computational strategy of the game um a lot of them have really struggled to keep  
**Translation:** Vocabulary: bluffing: 诈唬; struggled: 挣扎

**[4311.12s] English:** up with that development now so for that reason i'll i'll give an answer and i'm going to say that  
**Translation:** 

**[4316.64s] English:** daniel migranio who you actually had on the podcast recently i saw  
**Translation:** Vocabulary: migranio: 米格纳乔

**[4320.00s] English:** a great episode i love this so much and phil's gonna hate this so much and i'm gonna give him  
**Translation:** 

**[4327.04s] English:** i'm gonna give him credit because he is one of the few like old school really strong players that  
**Translation:** 

**[4333.04s] English:** have kept up with the development of ai so he is trying to he's constantly studying the game theory  
**Translation:** 

**[4338.40s] English:** optimal way of playing exactly yeah and i think a lot of a lot of the old school poker players  
**Translation:** Vocabulary: optimal: 最佳; poker: 扑克

**[4343.20s] English:** have just kind of given up on that aspect and and i got to give den the ground you credit for for  
**Translation:** 

**[4347.44s] English:** keeping up with all the developments that are happening in the sport yeah it's fascinating  
**Translation:** 

**[4352.08s] English:** to watch it's fascinating to watch where it's headed um yeah so there you go some love for daniel  
**Translation:** 

**[4359.12s] English:** quick pause bathroom break yeah let's do it let's go from poker to diplomacy  
**Translation:** Vocabulary: diplomacy: 外交

**[4365.36s] English:** what is at a high level the game of diplomacy yeah so i talked a lot about two-player zero-sum games  
**Translation:** 

**[4371.92s] English:** and what's interesting about diplomacy is that it's very different from these like  
**Translation:** 

**[4377.28s] English:** athletes who are playing poker at the top of the table for example these old school players who are  
**Translation:** 

**[4377.44s] English:** adversarial games like chess, go, poker, even Starcraft and Dota, diplomacy has a much bigger  
**Translation:** Vocabulary: adversarial: 敌对竞争; starcraft: 星际争霸

**[4384.34s] English:** cooperative element to it. It's a seven-player game. It was actually created in the 50s,  
**Translation:** 

**[4389.32s] English:** and it takes place before World War I. It's like a map of Europe with seven great powers,  
**Translation:** Vocabulary: cooperative: 合作元素

**[4396.38s] English:** and they're all trying to form alliances with each other. There's a lot of negotiation going on,  
**Translation:** 

**[4402.26s] English:** and so the whole focus of the game is on forming alliances with the other players to take on the  
**Translation:** 

**[4409.48s] English:** other players. England, Germany, Russia, Turkey, Austria, Hungary, Italy, and France. That's right,  
**Translation:** 

**[4415.98s] English:** yeah. So the way the game works is on each turn, you spend about five to 15 minutes  
**Translation:** Vocabulary: austria: 奥地利

**[4423.68s] English:** talking to the other players in private, and you make all sorts of deals with them. You say like,  
**Translation:** 

**[4429.26s] English:** hey, let's work together. Let's team up again.  
**Translation:** 

**[4432.42s] English:** Because the only way that you can make progress is by working with somebody else  
**Translation:** 

**[4436.36s] English:** against the others. And then after that negotiation,  
**Translation:** 

**[4440.00s] English:** period is done all the players simultaneously submit their moves and they're all executed at  
**Translation:** 

**[4446.58s] English:** the same time and so you can tell people like hey i'm going to support you this turn um but then you  
**Translation:** 

**[4452.08s] English:** don't follow through with it and they're only going to figure that out once they see the moves  
**Translation:** 

**[4456.16s] English:** being read off how much of it is natural language like written actual text how much is like um  
**Translation:** 

**[4462.44s] English:** you're actually saying phrases that are structured so there's different ways to play the game you  
**Translation:** 

**[4468.04s] English:** can play it in person and in that case it's all natural language um free form communication  
**Translation:** 

**[4472.76s] English:** there's no constraints on the kinds of deals that you can make the kinds of things that you can  
**Translation:** 

**[4475.76s] English:** discuss um you can also play it online so you can you know send long emails back and forth um you  
**Translation:** 

**[4482.74s] English:** can play it like live online or over voice chat um but the the focus the important thing to  
**Translation:** 

**[4488.50s] English:** understand is that this is unstructured communication you can say whatever you want  
**Translation:** Vocabulary: unstructured: 无结构的

**[4492.04s] English:** um you can make any sorts of deals that you want and everything is done privately so it's not like  
**Translation:** 

**[4498.02s] English:** you're all around the board together having a conversation you're grabbing somebody going  
**Translation:** Vocabulary: privately: 私下里

**[4502.42s] English:** off into a corner and conspiring behind everybody else's back about what you're planning and uh  
**Translation:** 

**[4507.60s] English:** there's no limit in theory to the conversation you can have directly with one person that's right you  
**Translation:** Vocabulary: conspiring: 密谋

**[4513.04s] English:** can make all sorts of um you can talk about anything you can say like hey let's have a long  
**Translation:** 

**[4516.78s] English:** term alliance against this guy you can say like hey can you support me this turn and in return  
**Translation:** 

**[4520.76s] English:** i'll do this other thing for you next turn or um you know yeah just you can talk about like what  
**Translation:** 

**[4526.40s] English:** you talked about with somebody else and go through that and then you can say like hey  
**Translation:** 

**[4528.02s] English:** let's have a long term alliance against this guy you can say like hey can you support me this turn and  
**Translation:** 

**[4529.58s] English:** um you can make any sorts of deals that you want and everything is done privately by somebody else  
**Translation:** 

**[4530.36s] English:** um the way that i would describe the game is that it's kind of like a mix between risk  
**Translation:** 

**[4534.42s] English:** poker and the tv show survivor there's like this big element of like trying to um yeah there's a  
**Translation:** 

**[4541.98s] English:** big social element and and the best way that i would describe the game is that it's really a game  
**Translation:** 

**[4546.50s] English:** about people rather than the pieces so risk because there is a map it's kind of war game like  
**Translation:** 

**[4554.60s] English:** uh poker because there's a game theory  
**Translation:** 

**[4558.02s] English:** component that's very kind of strategic  
**Translation:** Vocabulary: poker: 纸牌游戏

**[4560.00s] English:** so you could convert it into an artificial intelligence problem  
**Translation:** 

**[4563.48s] English:** and then survive it because of the social component,  
**Translation:** 

**[4566.32s] English:** the strong social component.  
**Translation:** 

**[4567.86s] English:** I saw that somebody said online that the internet version of the game  
**Translation:** 

**[4571.66s] English:** has this quality that it's easier to almost do role-playing  
**Translation:** 

**[4576.62s] English:** as opposed to being yourself.  
**Translation:** 

**[4579.62s] English:** You can actually be the –  
**Translation:** 

**[4581.44s] English:** really imagine yourself as the leader of France or Russia and so on,  
**Translation:** 

**[4585.56s] English:** really pretend to be that person.  
**Translation:** 

**[4588.22s] English:** It's actually fun to really lean into being that leader.  
**Translation:** 

**[4592.88s] English:** Yeah, so some players do go this route  
**Translation:** 

**[4594.60s] English:** where they just kind of view it as a strategy game  
**Translation:** 

**[4597.02s] English:** but also a role-playing game where they can act out like,  
**Translation:** 

**[4599.58s] English:** what would I be like if I was a leader of France in 1900?  
**Translation:** 

**[4603.64s] English:** Forfeit right away. No, I'm just kidding.  
**Translation:** 

**[4607.18s] English:** And they sometimes use the old-timey language  
**Translation:** Vocabulary: forfeit: 放弃

**[4609.64s] English:** or how they imagine the elites would talk at that time.  
**Translation:** 

**[4614.98s] English:** Anyway, so what are the different turns of the game?  
**Translation:** 

**[4617.76s] English:** What are the –  
**Translation:** 

**[4618.20s] English:** Yeah, so on every turn,  
**Translation:** 

**[4621.18s] English:** you've got a bunch of different units that you start out with.  
**Translation:** 

**[4624.10s] English:** So you start out controlling just a few units  
**Translation:** 

**[4627.28s] English:** and the object of the game is to gain control of a majority of the map.  
**Translation:** 

**[4630.52s] English:** If you're able to do that, then you've won the game.  
**Translation:** 

**[4633.06s] English:** But like I said, the only way that you're able to do that  
**Translation:** 

**[4635.26s] English:** is by working with other players.  
**Translation:** 

**[4636.88s] English:** So on every turn, you can issue a move order.  
**Translation:** 

**[4639.54s] English:** So for each of your units, you can move them to an adjacent territory  
**Translation:** 

**[4643.04s] English:** or you can keep them where they are  
**Translation:** 

**[4645.88s] English:** or you can support a move,  
**Translation:** 

**[4648.20s] English:** or a hold of a different unit.  
**Translation:** 

**[4651.22s] English:** What are the territories?  
**Translation:** Vocabulary: territories: 领土区域

**[4652.60s] English:** How is the map divided up?  
**Translation:** 

**[4654.26s] English:** It's kind of like Risk,  
**Translation:** 

**[4655.30s] English:** where the map is divided up into like 50 different territories.  
**Translation:** 

**[4659.98s] English:** Now, you can enter a territory  
**Translation:** 

**[4662.04s] English:** if you're moving into that territory with more supports  
**Translation:** 

**[4665.10s] English:** than the person that's in there  
**Translation:** 

**[4666.90s] English:** or the person that's trying to move in there.  
**Translation:** 

**[4668.86s] English:** So if you're moving in and there's somebody already there,  
**Translation:** 

**[4671.66s] English:** then if neither of you have support,  
**Translation:** 

**[4673.44s] English:** it's a one versus one and you'll bounce back  
**Translation:** 

**[4675.10s] English:** and neither of you will make progress.  
**Translation:** 

**[4676.72s] English:** If you have a unit that's –  
**Translation:** 

**[4678.18s] English:** supporting that move into the territory –  
**Translation:** 

**[4680.00s] English:** Then it's a two versus one, and you'll kick them out, and they'll have to retreat somewhere.  
**Translation:** 

**[4684.00s] English:** What does support mean?  
**Translation:** 

**[4684.92s] English:** Support is an action that you can issue in the game.  
**Translation:** 

**[4687.70s] English:** So you can say, this unit, you write down, this unit is supporting this other unit into this territory.  
**Translation:** 

**[4693.14s] English:** Are these units from opposing forces?  
**Translation:** 

**[4696.04s] English:** They could be.  
**Translation:** 

**[4696.68s] English:** They could be.  
**Translation:** 

**[4697.04s] English:** And this is where the interesting aspect of the game comes in.  
**Translation:** 

**[4699.28s] English:** Because you can support your own units into territory, but you can also support other people's units into territories.  
**Translation:** 

**[4705.32s] English:** And so that's what the negotiations really revolve around.  
**Translation:** 

**[4708.40s] English:** But you don't have to do the thing you say you're going to do, right?  
**Translation:** 

**[4712.58s] English:** Yeah.  
**Translation:** 

**[4713.18s] English:** So you can say, I'm going to support you, but then backstab the person.  
**Translation:** 

**[4716.92s] English:** Yeah, that's absolutely right.  
**Translation:** 

**[4718.42s] English:** And that tension is core to the game?  
**Translation:** 

**[4720.88s] English:** That tension is absolutely core to the game.  
**Translation:** 

**[4722.66s] English:** The fact that you can make all sorts of promises, but you have to reason about the fact that they might not trust you if you say you're going to do something.  
**Translation:** 

**[4731.66s] English:** Or they might be lying to you when they say they're going to support you.  
**Translation:** 

**[4736.48s] English:** So maybe just this.  
**Translation:** 

**[4738.40s] English:** To jump back, what's the history of the game in general?  
**Translation:** 

**[4741.32s] English:** Is it true that Henry Kissinger loved the game and JFK and all those?  
**Translation:** 

**[4745.38s] English:** I've heard a bunch of different people that.  
**Translation:** 

**[4747.32s] English:** Or is that just one of those things that the cool kids say they do, but they don't actually play?  
**Translation:** 

**[4751.44s] English:** So the game was created in the 50s.  
**Translation:** 

**[4753.34s] English:** Yeah.  
**Translation:** 

**[4754.56s] English:** And from what I understand, it was JFK's.  
**Translation:** 

**[4758.02s] English:** It was played in the JFK White House, Henry Kissinger's favorite game.  
**Translation:** 

**[4760.96s] English:** I don't know if it's true, but that's definitely what I've heard.  
**Translation:** 

**[4763.66s] English:** It's interesting that they went with World War I when it was created.  
**Translation:** 

**[4767.92s] English:** It was created after World War II.  
**Translation:** 

**[4769.58s] English:** So the story that I've heard for the creation of the game is it was created by somebody that had looked at the history of the 20th century.  
**Translation:** 

**[4779.24s] English:** And they saw World War I as a failure of diplomacy.  
**Translation:** 

**[4783.52s] English:** So they saw the fact that this war broke out as the diplomats of all these countries really failed to prevent a war.  
**Translation:** Vocabulary: diplomacy: 外交; diplomats: 外交官

**[4791.32s] English:** And he wanted to create a game that would basically teach people about diplomacy.  
**Translation:** 

**[4796.84s] English:** And.  
**Translation:** 

**[4797.92s] English:** It's really fascinating that like in his.  
**Translation:** 

**[4799.96s] English:** It's really fascinating that like in his.  
**Translation:** 

**[4800.00s] English:** ideal version of the game of diplomacy nobody actually wins the game because the whole point  
**Translation:** 

**[4804.48s] English:** is that if somebody is about to win then the other players should be able to work together  
**Translation:** 

**[4808.00s] English:** to stop that person from winning and so the ideal version of the game is just one where nobody  
**Translation:** 

**[4813.12s] English:** actually wins and you know it kind of has a nice like wholesome take-home message then that  
**Translation:** Vocabulary: wholesome: 有益身心

**[4817.36s] English:** you know war war is ultimately futile and uh and uh that optimal that futile optimal could be  
**Translation:** 

**[4826.00s] English:** achieved through great diplomacy so uh is there some asymmetry in in terms of which is more  
**Translation:** Vocabulary: asymmetry: 不对称; futile: 徒劳; optimal: 最优

**[4833.20s] English:** powerful russia versus germany versus france and so on so i think the general consensus is that  
**Translation:** 

**[4840.32s] English:** france is the strongest power in the game but the beautiful thing about diplomacy is that it's it's  
**Translation:** 

**[4844.80s] English:** self-balancing right so it's the fact that france has an inherent advantage from the beginning  
**Translation:** 

**[4849.20s] English:** means that the other players are less likely to work with it i saw that russia has four units  
**Translation:** 

**[4854.64s] English:** versus four of something  
**Translation:** 

**[4856.00s] English:** that the others have three of something that's true yeah so russia starts off with four units  
**Translation:** 

**[4859.68s] English:** while all the other players start with three but russia is also in a much more vulnerable position  
**Translation:** 

**[4864.48s] English:** because they have to like um they have a lot more neighbors as well got it larger territory more uh  
**Translation:** 

**[4870.08s] English:** yeah right more border to defend okay uh what else is what else is important to know about the rules  
**Translation:** 

**[4877.60s] English:** so there there's how many rounds are there like is this iterative game  
**Translation:** Vocabulary: iterative: 循环进行的

**[4881.92s] English:** is there is it is it finite you just keep going indefinitely  
**Translation:** 

**[4885.36s] English:** usually the  
**Translation:** Vocabulary: finite: 有限; indefinitely: 无限地

**[4886.00s] English:** game lasts uh i would say about 15 or 20 turns um there's in theory no limit it could last longer  
**Translation:** 

**[4893.36s] English:** but at some point i mean if you're playing a house game with friends at some point you just  
**Translation:** 

**[4896.40s] English:** get tired and you all agree like okay we're going to end the game here and call it a draw  
**Translation:** 

**[4900.24s] English:** um if you're playing online there's usually like set limits on when the game will actually end  
**Translation:** 

**[4904.88s] English:** and what's the end what's the termination condition like this does one country have  
**Translation:** 

**[4910.96s] English:** to conquer everything else so if somebody is able to actually gain control of a majority of the map  
**Translation:** 

**[4916.00s] English:** then then they've won the game and that is a solo victory as it's called now  
**Translation:** 

**[4920.00s] English:** Now that pretty rarely happens, especially with strong players, because like I said,  
**Translation:** 

**[4923.32s] English:** the game is designed to incentivize the other players to put a stop to that and all work  
**Translation:** 

**[4927.40s] English:** together to stop the superpower.  
**Translation:** Vocabulary: incentivize: 激励; superpower: 超级力量

**[4930.58s] English:** Usually what ends up happening is that, you know, all the players agree to a draw and  
**Translation:** 

**[4934.78s] English:** then the score, the win is divided among the remaining players.  
**Translation:** 

**[4940.28s] English:** There's a lot of different scoring systems.  
**Translation:** 

**[4941.62s] English:** The one that we used in our research basically gives a score relative to how much control  
**Translation:** 

**[4949.08s] English:** you have of the map.  
**Translation:** 

**[4949.76s] English:** So the more that you control, the higher you score.  
**Translation:** 

**[4952.76s] English:** What's the history of using this game as a benchmark for AI research?  
**Translation:** 

**[4957.90s] English:** Do people use it?  
**Translation:** Vocabulary: benchmark: 衡量标准

**[4959.76s] English:** Yeah.  
**Translation:** 

**[4960.16s] English:** So people have been working on AI for diplomacy since about the 80s.  
**Translation:** Vocabulary: diplomacy: 外交

**[4965.24s] English:** There was some really exciting research back then, but the approach that was taken was  
**Translation:** 

**[4970.12s] English:** very different from what we see today.  
**Translation:** 

**[4971.62s] English:** I mean, the research in the 80s was a very rule-based approach, kind of a heuristic approach.  
**Translation:** 

**[4976.14s] English:** It was very in line with the kind of research that was being done in the 80s.  
**Translation:** Vocabulary: heuristic: 启发式方法

**[4979.20s] English:** You know,  
**Translation:** 

**[4979.70s] English:** basically trying to encode human knowledge into the strategy of the AI.  
**Translation:** Vocabulary: encode: 编码

**[4983.48s] English:** Sure.  
**Translation:** 

**[4983.98s] English:** And, you know, it's understandable.  
**Translation:** Vocabulary: understandable: 容易理解的

**[4986.26s] English:** I mean, the game is so incredibly different and so much more complicated than the kinds of games that  
**Translation:** 

**[4992.84s] English:** people were working on, like chess and go and poker, that it was honestly even hard to start making any  
**Translation:** 

**[5000.88s] English:** progress in diplomacy.  
**Translation:** 

**[5002.22s] English:** Can you just formulate what is the problem from an AI perspective and why is it hard?  
**Translation:** 

**[5007.58s] English:** Why is it a challenging game to solve?  
**Translation:** 

**[5009.70s] English:** So there's a lot of aspects in diplomacy that make it a huge challenge.  
**Translation:** 

**[5013.64s] English:** First of all, you have the natural language components.  
**Translation:** 

**[5016.74s] English:** And I think this really is what makes it arguably the most difficult game among the major benchmarks.  
**Translation:** Vocabulary: arguably: 可能地说; benchmarks: 衡量标准

**[5023.88s] English:** The fact that you have to, it's not about moving pieces on the board.  
**Translation:** 

**[5029.74s] English:** Your action space is basically all the different sentences that you could communicate to somebody else in this game.  
**Translation:** 

**[5036.16s] English:** And is there, can we just like linger on that?  
**Translation:** 

**[5039.34s] English:** So,  
**Translation:** 

**[5040.00s] English:** is part of it like the ambiguity in the language if it was like very strict if you narrow the set  
**Translation:** 

**[5049.02s] English:** of possible sentences you could do would that simplify the game significantly the the real  
**Translation:** Vocabulary: ambiguity: 模糊性; simplify: 简化

**[5053.32s] English:** difficulty is the breadth of things that you can talk about um you could have natural language in  
**Translation:** 

**[5060.08s] English:** other games and like settlers of katan for example like you could have a natural language  
**Translation:** 

**[5063.62s] English:** settlers of katan ai but the things that you're going to talk about are basically like am i  
**Translation:** 

**[5067.74s] English:** treating you two sheep for a wood or three sheep for a wood um whereas in a game like diplomacy  
**Translation:** 

**[5072.88s] English:** the breadth of conversations that you're going to have are like you know am i going to support  
**Translation:** 

**[5077.88s] English:** you are you going to support me in return which units are going to do what uh what did this other  
**Translation:** 

**[5082.86s] English:** person promise you uh they're lying because they told this other person that they're going to do  
**Translation:** 

**[5087.52s] English:** this instead um if you help me out this turn then in the future i'll do these things that will help  
**Translation:** 

**[5092.88s] English:** you out um the the depth and breadth of these  
**Translation:** 

**[5097.26s] English:** conversations are going to be like the breadth of conversations that you're going to have  
**Translation:** 

**[5097.72s] English:** um you could approach it and we actually consider doing this like you you know having a simplified  
**Translation:** 

**[5108.18s] English:** language to make this complexity uh smaller but ultimately we thought the most impactful  
**Translation:** Vocabulary: complexity: 复杂性

**[5115.70s] English:** way of doing this research would be to address the natural language component head-on and just  
**Translation:** 

**[5121.82s] English:** try to go for the full game up front just looking at sample games and what the conversations look  
**Translation:** 

**[5127.24s] English:** like  
**Translation:** 

**[5127.72s] English:** like greetings england this should prove to be a fun game since all the private press is going to  
**Translation:** 

**[5133.24s] English:** be made public at the end at the least it will be interesting to see if the press changes because  
**Translation:** 

**[5138.82s] English:** of that anyway good okay so there's like uh yeah that's just kind of like the generic greetings at  
**Translation:** 

**[5143.60s] English:** the beginning of the game i think that the meat comes a little bit later when you're starting to  
**Translation:** 

**[5146.80s] English:** talk about like specific strategy and stuff i agree there are a lot of advantages to the two  
**Translation:** 

**[5152.80s] English:** of us keeping in touch and our nations make strong natural allies and we're going to have a lot of  
**Translation:** 

**[5157.72s] English:** things that we're going to analyze in the middle game so that kind of stuff  
**Translation:** 

**[5160.00s] English:** uh making friends making enemies yeah or like if you look at the next line so the person's saying  
**Translation:** 

**[5164.76s] English:** like i've heard uh bits about a lepanto and an octopus opening and basically telling austria  
**Translation:** Vocabulary: austria: 奥地利; octopus: 章鱼

**[5170.02s] English:** like hey just a heads up you know i've heard these whispers about like what might be going  
**Translation:** 

**[5173.66s] English:** on behind your back yeah so there's all kinds of complexities in that in the in the language of  
**Translation:** Vocabulary: complexities: 复杂性; whispers: 流言

**[5182.04s] English:** that right like to interpret what that what the heck that means it's hard for us humans but for  
**Translation:** 

**[5186.54s] English:** it's even harder because you have to understand like at every level the the semantics of that  
**Translation:** Vocabulary: interpret: 解释; semantics: 语义

**[5191.62s] English:** right i mean there's the there's a complexity in understanding when somebody is saying this to me  
**Translation:** 

**[5195.56s] English:** what does that mean and then there's also the complexity of like should i be telling this  
**Translation:** 

**[5199.56s] English:** person this like i've overheard these these whispers should i be telling this person that  
**Translation:** 

**[5203.36s] English:** like hey you might be getting attacked by by this other power okay so what how we're supposed to  
**Translation:** 

**[5211.16s] English:** think about okay so that's the natural language how do you even begin trying to solve this game  
**Translation:** 

**[5216.02s] English:** it seems  
**Translation:** 

**[5216.54s] English:** like it seems like the taurine tests on steroids yeah and i mean there's there's the natural  
**Translation:** 

**[5221.48s] English:** language aspect and then even besides the natural language aspect you also have the the cooperative  
**Translation:** Vocabulary: cooperative: 合作型; steroids: 类固醇; taurine: 牛磺酸

**[5226.62s] English:** elements of the game and i think this is actually um something that i find really interesting if you  
**Translation:** 

**[5231.46s] English:** look at all the previous game ai uh breakthroughs they've all happened in these purely adversarial  
**Translation:** Vocabulary: adversarial: 敌对的; breakthroughs: 突破

**[5236.88s] English:** games where you don't actually need to understand how humans play the game it's all just ai versus  
**Translation:** 

**[5242.02s] English:** ai right like you look at uh checkers chess go  
**Translation:** 

**[5246.46s] English:** you look at uh checkers chess go  
**Translation:** 

**[5246.52s] English:** poker starcraft dota 2 like in some of those cases they leveraged human data but they never  
**Translation:** Vocabulary: leveraged: 利用; poker: 扑克; starcraft: 星际争霸

**[5252.86s] English:** needed to they were always just trying to have a scalable algorithm that then they could throw  
**Translation:** 

**[5260.02s] English:** a lot of computational resources at a lot of memory at and then eventually it would converge  
**Translation:** Vocabulary: algorithm: 算法; computational: 计算的; converge: 收敛; scalable: 可扩展的

**[5264.78s] English:** to an approximation of a nash equilibrium this perfect strategy that in a two-player zero-sum  
**Translation:** 

**[5271.48s] English:** game guarantees that they're going to be able to not lose to any opponent so you can't leverage  
**Translation:** Vocabulary: approximation: 近似; equilibrium: 均衡; guarantees: 保证; leverage: 利用

**[5276.44s] English:** self-play to solve this game you you can leverage self-play but  
**Translation:** 

**[5280.00s] English:** no longer sufficient to beat humans so how do you integrate the human into the loop of this  
**Translation:** Vocabulary: integrate: 融合

**[5285.12s] English:** so what you have to do is incorporate human data um and to kind of give you some intuition for why  
**Translation:** 

**[5291.20s] English:** this is the case like imagine you're playing a negotiation game like like diplomacy um but  
**Translation:** Vocabulary: diplomacy: 外交; incorporate: 融合; intuition: 直觉

**[5295.68s] English:** you're training completely from scratch without any human data the ai is not going to suddenly  
**Translation:** 

**[5302.08s] English:** like figure out how to communicate in english it's going to figure out some weird robot language  
**Translation:** 

**[5307.12s] English:** that only it will understand and then when you stick that in a game with six other humans  
**Translation:** 

**[5311.84s] English:** they're going to think this person's talking gibberish and they're just going to ally with  
**Translation:** Vocabulary: gibberish: 胡言乱语

**[5314.96s] English:** each other and team up against the bot or not even team up against the bot but just not work  
**Translation:** 

**[5318.80s] English:** with the bot and so in order to be able to play this game with humans it has to understand the  
**Translation:** 

**[5324.72s] English:** human way of playing the game not this machine way of playing the game yeah yeah that's fascinating  
**Translation:** 

**[5330.56s] English:** so right that that's a there's a nuanced thing to understand because the  
**Translation:** Vocabulary: nuanced: 细腻的

**[5336.64s] English:** a chess  
**Translation:** 

**[5337.12s] English:** playing program doesn't need to play like a human to beat a human exactly but here you have to play  
**Translation:** 

**[5342.80s] English:** like a human in order to beat them or at least you have to understand how humans play the game  
**Translation:** 

**[5346.88s] English:** so that you can understand how to work with them if they have certain expectations about what does  
**Translation:** 

**[5351.44s] English:** it mean to be a good ally what does it mean to have like a reciprocal relationship where we're  
**Translation:** 

**[5356.32s] English:** working together you have to abide by those conventions and if you don't they're just  
**Translation:** Vocabulary: abide: 遵守; conventions: 规定; reciprocal: 互惠

**[5361.04s] English:** going to work with somebody else instead do you think of this as a clean in some deep  
**Translation:** 

**[5367.04s] English:** sense of the spirit of the touring test as formulated by alan touring is it is some sense  
**Translation:** 

**[5372.40s] English:** this is what the touring test actually looks like so because of open-ended natural language  
**Translation:** 

**[5379.84s] English:** conversation seems like very difficult to evaluate like here at a high stakes where  
**Translation:** Vocabulary: evaluate: 评估

**[5386.08s] English:** humans are trying to win a game that seems like how you actually perform the touring test i think  
**Translation:** 

**[5392.16s] English:** it's different from the touring test like the way that the touring test is formulated it's about  
**Translation:** 

**[5397.04s] English:** how do you distinguish a human from a machine and seeing oh  
**Translation:** 

**[5400.00s] English:** Could the machine successfully pass as a human in this adversarial setting where the player is trying to figure out whether it's a machine or a human?  
**Translation:** Vocabulary: adversarial: 对抗的

**[5408.92s] English:** Whereas in diplomacy, it's not about trying to figure out whether this player is a human or a machine.  
**Translation:** 

**[5414.12s] English:** It's ultimately about whether I can work with this player, regardless of whether they are a human or a machine.  
**Translation:** Vocabulary: diplomacy: 外交艺术

**[5419.98s] English:** And can the machine do that better than a human can?  
**Translation:** 

**[5422.74s] English:** Yeah, I'm going to think about that, but that just feels like the implied requirement for that is for the machine to be human-like.  
**Translation:** 

**[5434.52s] English:** I think that's true, that if you're going to play in this human game, you have to somehow adapt to the human surroundings and the human play style.  
**Translation:** 

**[5444.52s] English:** And to win, you have to adapt.  
**Translation:** Vocabulary: surroundings: 环境

**[5447.26s] English:** So you can't, if you're the outsider, if you're not human-like, I feel like that's a losing.  
**Translation:** 

**[5452.74s] English:** I think that's correct, yeah.  
**Translation:** Vocabulary: outsider: 局外人

**[5455.74s] English:** Yeah, so okay.  
**Translation:** 

**[5459.10s] English:** What are the complexities here?  
**Translation:** Vocabulary: complexities: 复杂性

**[5460.76s] English:** What was your approach to it?  
**Translation:** 

**[5462.58s] English:** Before I get to that, one thing I should explain, like why we decided to work on diplomacy.  
**Translation:** 

**[5467.40s] English:** So basically what happened is in 2019, I was wrapping up the work on six-player poker on Pluribus and was trying to think about what to work on next.  
**Translation:** 

**[5478.02s] English:** And I had been seeing like all these other breakthroughs happening in AI.  
**Translation:** Vocabulary: breakthroughs: 重大突破; pluribus: 一桌六人; poker: 扑克牌游戏

**[5481.56s] English:** I mean, like 2019.  
**Translation:** 

**[5482.74s] English:** You have StarCraft, you have AlphaStar beating humans in StarCraft, you've got the Dota 2 stuff happening at OpenAI, you have GPT-2 or GPT-3 coming, I think it was GPT-2 at the time, and it became clear that AI was progressing really, really rapidly.  
**Translation:** Vocabulary: progressing: 快速发展

**[5499.50s] English:** And people were throwing out these like other games about, you know, what should be the next challenge for multi-agent AI, and I just felt like we had to aim bigger.  
**Translation:** 

**[5510.84s] English:** If you look at a game like Chalice.  
**Translation:** Vocabulary: chalice: 圣杯

**[5513.28s] English:** Or a game like Go, they took decades for researchers to ultimately reach superhuman performance at.  
**Translation:** 

**[5519.52s] English:** I mean, like chess.  
**Translation:** 

**[5520.00s] English:** took 40 years of ai research go took another 20 years um and we we thought that diplomacy would  
**Translation:** 

**[5528.80s] English:** be this incredibly difficult challenge that could easily take a decade to make an ai that could play  
**Translation:** 

**[5534.00s] English:** competently um but we felt like that was that was a goal worth aiming for um and so honestly i was  
**Translation:** 

**[5540.80s] English:** kind of reluctant to work on it at first because i thought it was like too far out of the realm of  
**Translation:** Vocabulary: competently: 熟练地; reluctant: 不愿意

**[5545.44s] English:** possibility but you know i was talking to a co-worker of mine adam lear and he was basically  
**Translation:** 

**[5549.36s] English:** saying like yeah why not aim for it you know we'll learn some interesting things along the  
**Translation:** 

**[5552.80s] English:** way and maybe it'll be possible um and so so we decided to go for it and i think i think it was  
**Translation:** 

**[5558.00s] English:** the right choice considering just how much progress there there was in ai and that that  
**Translation:** 

**[5563.44s] English:** progress has continued in the years since so winning in diplomacy what does that really  
**Translation:** 

**[5569.12s] English:** look like it means talking to six other players six other entities agents and convincing  
**Translation:** Vocabulary: diplomacy: 外交

**[5579.52s] English:** and convincing them of stuff that you want them to be convinced of  
**Translation:** 

**[5583.44s] English:** like what what exactly i'm trying to get like to deeply understand what the problem is  
**Translation:** 

**[5589.36s] English:** ultimately the problem is it's simple to to quantify right like you're going to play this  
**Translation:** 

**[5594.96s] English:** game with humans and you want your score on average to be um as high as possible you know  
**Translation:** Vocabulary: quantify: 量化

**[5601.20s] English:** if you can say like i am winning more than any any human alive um then you're a champion diplomacy  
**Translation:** 

**[5609.84s] English:** now ultimately we haven't we didn't reach that we got to human level performance we actually  
**Translation:** 

**[5613.44s] English:** so we played about 40 games with with real humans online uh the bot came in second out of all  
**Translation:** 

**[5619.92s] English:** players that played five or more games and um so not like number one but way way higher than well  
**Translation:** 

**[5626.72s] English:** what was the expertise level are they beginners are they intermediate players advanced players  
**Translation:** 

**[5632.80s] English:** that's a great question and so i think this kind of goes into how do you measure the performance in  
**Translation:** 

**[5637.52s] English:** diplomacy and i would argue that when you're measuring the performance in diplomacy you're going to measure the performance in diplomacy and i would argue that when you're  
**Translation:** 

**[5639.20s] English:** measuring performance  
**Translation:** 

**[5640.00s] English:** in a game like this you don't actually want to measure it in games with all expert players  
**Translation:** 

**[5645.60s] English:** it's kind of like if you're developing a self-driving car you don't want to measure  
**Translation:** 

**[5649.68s] English:** that car on the road with a bunch of expert stunt drivers yeah you want to put it on a road of like  
**Translation:** 

**[5655.20s] English:** an actual american city and see is this car crashing less often than an expert driver would  
**Translation:** 

**[5660.96s] English:** yeah so so that's the metric that we've used we we're saying like we're going to stick this game  
**Translation:** 

**[5666.32s] English:** we're going to stick this bot in games with a wide variety of skill levels and then are we doing  
**Translation:** 

**[5671.68s] English:** better than a strong or expert human player would in the same situation that's quite brilliant  
**Translation:** 

**[5677.68s] English:** because i played a lot of sports in my life like i did tennis judo whatever and it's somehow almost  
**Translation:** 

**[5684.40s] English:** easier to go against experts almost always i don't know i think they're more predictable  
**Translation:** 

**[5689.52s] English:** in the quality of play that the space of strategies you're operating under is narrower  
**Translation:** Vocabulary: narrower: 范围较小; predictable: 可预测的

**[5695.36s] English:** against experts  
**Translation:** 

**[5696.64s] English:** it's more fun it's really frustrating to go against beginners also because beginners talk  
**Translation:** 

**[5700.56s] English:** trash to you when they somehow do beat you so that's a human thing that they add doesn't have  
**Translation:** 

**[5705.92s] English:** to be worried about that but yeah the variance in strategies right is greater especially with  
**Translation:** Vocabulary: variance: 差异

**[5711.12s] English:** natural language it's just all over the place then yeah and and honestly when you look at  
**Translation:** 

**[5717.28s] English:** what makes a good human diplomacy player um obviously they're able to handle themselves  
**Translation:** Vocabulary: diplomacy: 外交艺术

**[5721.92s] English:** in games with other expert humans but where they really shine is when they're playing with these  
**Translation:** 

**[5725.76s] English:** weak players  
**Translation:** 

**[5726.64s] English:** and they know how to take advantage of the fact that they're a weak player that they won't be able  
**Translation:** 

**[5731.28s] English:** to like pull off a stab as well or that um they have certain tendencies and they can take them  
**Translation:** 

**[5736.08s] English:** under their wing and persuade them to do things that might not even be in their interest um  
**Translation:** 

**[5740.96s] English:** the really good diplomacy players are able to to take advantage of the fact that  
**Translation:** 

**[5745.36s] English:** they're in that there are some weak players in the game okay so if you have to incorporate human  
**Translation:** 

**[5749.28s] English:** play data how do you do that how do you do that in order to train in the ai system to play diplomacy  
**Translation:** Vocabulary: incorporate: 合并

**[5755.12s] English:** yeah so that's that's really the crux of the problem how do we  
**Translation:** 

**[5760.00s] English:** leverage the benefits of self-play that have been so successful in all these  
**Translation:** Vocabulary: leverage: 利用

**[5764.72s] English:** other previous games while keeping the strategy as as human compatible as  
**Translation:** 

**[5769.64s] English:** possible and so what we did is we first trained a language model and then we  
**Translation:** Vocabulary: compatible: 易于理解的

**[5775.64s] English:** made that language model controllable on a set of in a set of intents what we  
**Translation:** 

**[5781.08s] English:** call intents which are basically like an action that we want to play and an  
**Translation:** 

**[5784.40s] English:** action that we would like the other player to play and so this gives us a  
**Translation:** 

**[5788.10s] English:** way to generate dialogue that's not just trying to imitate the human style  
**Translation:** 

**[5792.08s] English:** whatever a human would say in the situation but to actually give it a an  
**Translation:** 

**[5796.26s] English:** intent of purpose in its communication we can talk about a specific move or we  
**Translation:** 

**[5800.76s] English:** can make a specific request and the determination of what that move is that  
**Translation:** 

**[5805.74s] English:** we're discussing comes from strategic a strategic reasoning model that uses  
**Translation:** 

**[5811.16s] English:** reinforcement learning and planning so the computing the intents for all the  
**Translation:** 

**[5816.22s] English:** players how do they interact with each other how do they interact with each  
**Translation:** Vocabulary: computing: 计算; reinforcement: 强化

**[5818.08s] English:** other how is that done just as a starting point is that with reinforcement  
**Translation:** 

**[5823.36s] English:** learning or is that just optimal determining what the optimal is for  
**Translation:** Vocabulary: optimal: 最优的

**[5826.46s] English:** intents it's a combination of reinforcement learning and planning  
**Translation:** 

**[5831.56s] English:** actually very similar to how you approach how we approached poker and how  
**Translation:** Vocabulary: poker: 纸牌游戏

**[5836.18s] English:** people approached like chess and go as well we're using self-play and and  
**Translation:** 

**[5841.20s] English:** search to try to figure out what are what is an optimal move for us and what  
**Translation:** 

**[5846.26s] English:** is a desirable move that we would like this other player to make and then we're  
**Translation:** 

**[5848.08s] English:** going to start to play now the difference between the way that we  
**Translation:** Vocabulary: desirable: 值得称赞的

**[5852.40s] English:** approached reinforcement learning and search in this game versus those  
**Translation:** 

**[5855.88s] English:** previous games is that we have to keep it human compatible we have to  
**Translation:** 

**[5859.20s] English:** understand how the other person is likely to play rather than just assuming  
**Translation:** 

**[5863.72s] English:** that they're going to play like a machine and how language gets them to  
**Translation:** 

**[5867.60s] English:** play in a way that maximize the chance of following the intent you want them to  
**Translation:** 

**[5873.40s] English:** follow okay how do you do that how do you how do you connect language to intent  
**Translation:** Vocabulary: maximize: 最大化

**[5878.08s] English:** so the way that our  
**Translation:** 

**[5880.00s] English:** and planning is done is actually not using language.  
**Translation:** 

**[5883.06s] English:** So we're coming up with this plan for the action  
**Translation:** 

**[5886.62s] English:** that we're going to play and the other person is going to play  
**Translation:** 

**[5889.10s] English:** and then we feed that action into the dialogue model  
**Translation:** 

**[5891.48s] English:** that will then send a message according to those plans.  
**Translation:** 

**[5894.22s] English:** So the language model there is mapping action to message  
**Translation:** 

**[5900.46s] English:** one word at a time.  
**Translation:** 

**[5904.08s] English:** Basically one message at a time.  
**Translation:** 

**[5905.46s] English:** So we'll feed into the dialogue model  
**Translation:** 

**[5907.30s] English:** like here are the actions that you should be discussing.  
**Translation:** 

**[5909.16s] English:** Here is the content of the message that we would like you to send  
**Translation:** 

**[5914.58s] English:** and then it will actually generate a message that corresponds to that.  
**Translation:** 

**[5918.06s] English:** Okay. Does this actually work?  
**Translation:** Vocabulary: corresponds: 相符

**[5919.74s] English:** It works surprisingly well.  
**Translation:** 

**[5921.28s] English:** Okay. Oh, man.  
**Translation:** 

**[5924.90s] English:** The number of ways it probably goes horribly.  
**Translation:** 

**[5927.42s] English:** I would have imagined it goes horribly wrong.  
**Translation:** Vocabulary: horribly: 极其糟糕地

**[5931.18s] English:** So how the heck is it effective at all?  
**Translation:** 

**[5933.94s] English:** I mean there are a lot of ways that this could fail.  
**Translation:** 

**[5935.68s] English:** So for example, I mean,  
**Translation:** 

**[5937.38s] English:** you could have a situation where you're basically like we don't tell the language model  
**Translation:** 

**[5944.36s] English:** like here are the pieces of our action or the other person's action  
**Translation:** 

**[5947.78s] English:** that you should be communicating.  
**Translation:** 

**[5949.28s] English:** And so like let's say you're about to attack somebody.  
**Translation:** 

**[5951.28s] English:** You probably don't want to tell them that you're going to attack them,  
**Translation:** 

**[5954.02s] English:** but there's nothing in the language.  
**Translation:** 

**[5955.90s] English:** Like the language model is not very smart at the end of the day.  
**Translation:** 

**[5957.64s] English:** So it doesn't really have a way of knowing like,  
**Translation:** 

**[5960.26s] English:** well, what should I be talking about?  
**Translation:** 

**[5961.60s] English:** Should I tell this person that I'm about to attack them or not?  
**Translation:** 

**[5965.10s] English:** So we have to like develop a lot of other techniques,  
**Translation:** 

**[5967.36s] English:** that deal with that.  
**Translation:** 

**[5969.66s] English:** Like one of the things we do, for example,  
**Translation:** 

**[5971.06s] English:** is we try to calculate if I'm going to send this message,  
**Translation:** 

**[5974.66s] English:** what would I expect the other person to do in response?  
**Translation:** 

**[5977.36s] English:** So if it's a message like, hey, I'm going to attack you this turn,  
**Translation:** 

**[5980.26s] English:** they're probably going to, you know, attack us or defend against that attack.  
**Translation:** 

**[5984.96s] English:** And so we have a way of recognizing like, hey,  
**Translation:** 

**[5987.36s] English:** sending this message is a negative expected value action,  
**Translation:** 

**[5992.16s] English:** and we should not send this message.  
**Translation:** 

**[5994.76s] English:** So yes, for particular kinds of messages,  
**Translation:** 

**[5997.16s] English:** you have like an extra function that does the.  
**Translation:** 

**[6000.00s] English:** uh estimates the value of that message yeah so we have these kinds of filters that like so it's a  
**Translation:** 

**[6006.08s] English:** filter so there's a there's a good and is that filter in your network or is it rule-based that's  
**Translation:** 

**[6012.04s] English:** that's a that's a neural network so we're well it's a it's a combination it's a neural network  
**Translation:** Vocabulary: neural: 神经网络

**[6015.76s] English:** but it's also using planning um it's trying to compute like what is the policy that the other  
**Translation:** 

**[6022.24s] English:** players are going to play given that this message um has been sent and then is that better than not  
**Translation:** 

**[6027.86s] English:** sending the message or i feel like that's how my brain works too like there's a language model that  
**Translation:** 

**[6032.56s] English:** generates random crap and then there's these other neural nets that are essentially filters  
**Translation:** 

**[6038.34s] English:** at least that's when i tweet i'll usually my process of tweeting i'll think of something  
**Translation:** 

**[6044.30s] English:** and it's hilarious to me and then about five seconds later the filter network comes in and  
**Translation:** Vocabulary: tweeting: 发推特

**[6049.70s] English:** says no no that's not funny at all i mean there's some something interesting to that kind of process  
**Translation:** 

**[6055.10s] English:** so you have a set of actions that you  
**Translation:** 

**[6057.00s] English:** you  
**Translation:** 

**[6057.84s] English:** you want you have an intent that you want to achieve an intent that you want your opponent  
**Translation:** 

**[6063.42s] English:** to achieve then you generate messages and then you evaluate if those messages will achieve the  
**Translation:** 

**[6069.14s] English:** the goal you want yeah and we're filtering for several things we're filtering like is this a  
**Translation:** Vocabulary: evaluate: 评估

**[6076.68s] English:** sensible message you know so sometimes language models will send will generate messages that are  
**Translation:** 

**[6080.84s] English:** just like totally nonsense um and we try to filter those out we also try to filter out messages that  
**Translation:** Vocabulary: sensible: 合乎情理

**[6087.70s] English:** that are basically lies um so you know diplomacy has this reputation as a game that's really about  
**Translation:** 

**[6093.38s] English:** um deception and lying but we try to actually minimize the amount that the bot would lie  
**Translation:** Vocabulary: deception: 欺骗; diplomacy: 外交

**[6099.46s] English:** um this was actually mostly a or are you no i'm just kidding i mean like part of the reason for  
**Translation:** 

**[6107.38s] English:** this is that we actually found that lying would make the bot perform worse in the long run it  
**Translation:** 

**[6113.22s] English:** would end up with a lower score because once the bot lies um  
**Translation:** 

**[6117.70s] English:** people would never trust it again and  
**Translation:** 

**[6120.00s] English:** And trust is a huge aspect of the game of diplomacy.  
**Translation:** 

**[6121.92s] English:** I'm taking notes here because I think this applies to life lessons, too.  
**Translation:** 

**[6126.98s] English:** Oh, I think it's a really, yeah, really strong.  
**Translation:** 

**[6128.50s] English:** So, like, lying is a dangerous thing to do.  
**Translation:** 

**[6130.84s] English:** Like, you want to avoid obvious lying.  
**Translation:** 

**[6134.98s] English:** Yeah, I mean, I think when people play diplomacy for the first time, they approach it as a game of deception and lying.  
**Translation:** 

**[6141.26s] English:** And they, ultimately, if you talk to top diplomacy players, what they'll tell you is that diplomacy is a game about trust.  
**Translation:** 

**[6147.68s] English:** And being able to build trust in an environment that encourages people to not trust anyone.  
**Translation:** 

**[6153.14s] English:** So, that's the ultimate tension in diplomacy.  
**Translation:** 

**[6156.14s] English:** How can this AI reason about whether you are being honest in your communication?  
**Translation:** 

**[6161.08s] English:** And how can the AI persuade you that it is being honest when it is telling you that, hey, I'm actually going to support you this turn?  
**Translation:** 

**[6167.80s] English:** Is there some sense, I don't know if you step back and think, that this process will indirectly help us study human psychology?  
**Translation:** 

**[6177.68s] English:** So, like, if trust is the ultimate goal, wouldn't that help us understand what are the fundamental aspects of forming trust between humans and between humans and AI?  
**Translation:** 

**[6189.82s] English:** I mean, that's a really, really important question that's much bigger than strategy games.  
**Translation:** 

**[6195.04s] English:** It's how can, that's fundamental to the human-robot interaction problem.  
**Translation:** 

**[6199.36s] English:** How do we form trust between intelligent entities?  
**Translation:** 

**[6203.54s] English:** So, one of the things I'm really excited about with diplomacy.  
**Translation:** 

**[6207.68s] English:** There's never really been a good domain to investigate these kinds of questions.  
**Translation:** 

**[6213.56s] English:** And diplomacy gives us a domain where trust is really at the center of it.  
**Translation:** 

**[6219.12s] English:** And it's not just like you've hired a bunch of mechanical Turkers that are being paid and trying to get through the task as quickly as possible.  
**Translation:** Vocabulary: diplomacy: 外交

**[6226.94s] English:** You have these people that are really invested in the outcome of the game, and they're really trying to do the best that they can.  
**Translation:** 

**[6232.86s] English:** And so, I'm really excited that we're able to, we actually, like, have put a lot of effort into this.  
**Translation:** 

**[6236.96s] English:** So, I'm really excited that we're able to, we actually, like, have put a lot of effort into this.  
**Translation:** 

**[6237.68s] English:** We're open sourcing all of our models.  
**Translation:** Vocabulary: sourcing: 采购

**[6240.00s] English:** We're open sourcing all of the code and we're making the data that we've used available  
**Translation:** 

**[6246.28s] English:** to researchers so that they can investigate these kinds of questions.  
**Translation:** 

**[6251.08s] English:** So the data of the different, the human and the AI play of diplomacy and the models that  
**Translation:** 

**[6256.04s] English:** you use for the generation of the messages and the filtering.  
**Translation:** 

**[6259.98s] English:** Yeah, not just even the data of the AI playing with the humans, but all the training data  
**Translation:** 

**[6265.50s] English:** that we used to train the AI to understand how humans play the game.  
**Translation:** 

**[6270.48s] English:** We're setting up a system where researchers will be able to apply to be able to gain access  
**Translation:** 

**[6275.64s] English:** to that data and be able to use it in their own research.  
**Translation:** 

**[6278.22s] English:** We should say, what is the name of the system?  
**Translation:** 

**[6281.16s] English:** We're calling the bot Cicero.  
**Translation:** Vocabulary: cicero: 西塞罗

**[6282.42s] English:** Cicero.  
**Translation:** 

**[6283.42s] English:** And what's the name, like you're open sourcing, what's the name of the repository and the  
**Translation:** Vocabulary: repository: 代码仓库

**[6288.74s] English:** project?  
**Translation:** 

**[6289.74s] English:** Is it also just called Cicero, the big project or are you still coming up with a name?  
**Translation:** 

**[6293.78s] English:** The data set comes from this website.  
**Translation:** 

**[6295.50s] English:** It's called webdiplomacy.net is the site that's been online for like 20 years now.  
**Translation:** Vocabulary: webdiplomacy: 网络外交

**[6299.58s] English:** And it's one of the main sites that people use to play diplomacy on it.  
**Translation:** 

**[6302.94s] English:** We've got like 50,000 games of diplomacy with, you know, natural language communication,  
**Translation:** 

**[6309.36s] English:** over 10 million messages.  
**Translation:** 

**[6311.30s] English:** So it's a pretty massive data set that people can use to, we're hoping that the academic  
**Translation:** 

**[6316.04s] English:** community and the research community is able to use it for all sorts of interesting research  
**Translation:** 

**[6320.74s] English:** questions.  
**Translation:** 

**[6321.74s] English:** So do you, from having studied this game, is this a success?  
**Translation:** 

**[6325.48s] English:** Is this a sufficiently rich problem space to explore this kind of human AI interaction?  
**Translation:** Vocabulary: sufficiently: 足够地

**[6331.24s] English:** Yeah, absolutely.  
**Translation:** 

**[6332.56s] English:** And I think it's maybe the best data set that I can think of out there to investigate these  
**Translation:** 

**[6338.56s] English:** kinds of questions of negotiation, trust, persuasion.  
**Translation:** 

**[6344.24s] English:** I wouldn't say it's the best data set in the world for human AI interaction.  
**Translation:** Vocabulary: persuasion: 说服

**[6348.76s] English:** That's a very broad field.  
**Translation:** 

**[6349.80s] English:** But I think that it's definitely up there as like, you know, if you're really interested  
**Translation:** 

**[6353.30s] English:** in language models interacting with humans.  
**Translation:** 

**[6355.36s] English:** In, you know, a setting where their incentives are not fully aligned, this seems  
**Translation:** Vocabulary: aligned: 目标一致; incentives: 动机

**[6360.00s] English:** like an ideal data set for investigating that so you have um you have a paper with some impressive  
**Translation:** 

**[6367.62s] English:** results and just an impressive paper they're taking this problem on what's the most exciting  
**Translation:** 

**[6372.74s] English:** thing to you in terms of the results from the the paper well i think there's ideas or results  
**Translation:** 

**[6379.70s] English:** yeah i think there's a few aspects of the results and um that i think are really exciting so first  
**Translation:** 

**[6385.82s] English:** of all the fact that we were able to achieve such strong performance um i was surprised by  
**Translation:** 

**[6391.86s] English:** and pleasantly surprised by um so we played 40 games of diplomacy with real humans and the bot  
**Translation:** Vocabulary: diplomacy: 国际外交; pleasantly: 愉快地

**[6398.06s] English:** placed second out of all players that have played five or more games so it's about 80 players total  
**Translation:** 

**[6403.78s] English:** um 19 of whom played five or more games and the bot was ranked second out of those players  
**Translation:** 

**[6408.40s] English:** um and the bot was was really good in two dimensions one being able to establish  
**Translation:** 

**[6415.58s] English:** um  
**Translation:** Vocabulary: dimensions: 维度

**[6415.80s] English:** strong connections with the other players on the board being able to like persuade them to work  
**Translation:** 

**[6420.48s] English:** with it um being able to coordinate with them about like how it's going to work with them  
**Translation:** 

**[6424.50s] English:** and then also the raw tactical and strategic aspects of the game you know being able to  
**Translation:** 

**[6430.64s] English:** understand what the other players are likely to do being able to model their behavior  
**Translation:** Vocabulary: tactical: 战术的

**[6434.98s] English:** and respond appropriately to that the bot also really excelled at what are some interesting  
**Translation:** 

**[6440.70s] English:** things that the bot said by the way you're allowed to swear in the um  
**Translation:** Vocabulary: appropriately: 恰当地; excelled: 表现出色

**[6445.80s] English:** like are there rules to what you're allowed to say or not in diplomacy you can say whatever you  
**Translation:** 

**[6450.38s] English:** want i think the site will get very angry at you if you start like threatening somebody  
**Translation:** 

**[6454.16s] English:** and we actually like if you threaten somebody you're supposed to do it politely yeah politely  
**Translation:** 

**[6459.92s] English:** you know like keep it in character um the the bot we actually had a researcher watching the bot 24  
**Translation:** Vocabulary: politely: 礼貌地; threaten: 威胁

**[6465.72s] English:** 7 for well whenever we play a game we had a bot watching it to make sure that it wouldn't go off  
**Translation:** 

**[6470.16s] English:** the rails and start like threatening somebody or something like that i would just love it if the  
**Translation:** 

**[6473.42s] English:** boss started like mocking mocking the bot or something like that i would just love it if the  
**Translation:** 

**[6475.80s] English:** bot started mocking everybody like some weird quirky strategies would emerge that have you  
**Translation:** Vocabulary: quirky: 古怪的

**[6480.00s] English:** seen anything interesting that you huh that's a weird that's a that's a weird behavior either  
**Translation:** 

**[6486.14s] English:** the filter or the language model that was weird to you that was yeah there were definitely like  
**Translation:** 

**[6492.52s] English:** things that the bot would would do that were not in line with like how humans would approach the  
**Translation:** 

**[6498.80s] English:** game and that in a good way the humans actually you know we've talked to some expert diplomacy  
**Translation:** 

**[6504.14s] English:** players about these results and their takeaway is that well maybe humans are approaching this  
**Translation:** 

**[6508.52s] English:** the wrong way and this is actually like the right way to play the game um so what's required to win  
**Translation:** Vocabulary: takeaway: 收获

**[6514.90s] English:** like what um what does it mean to mess up or to exploit the suboptimal behavior of a player  
**Translation:** 

**[6520.82s] English:** like um is there uh is there optimally rational behavior and irrational behavior that you need to  
**Translation:** Vocabulary: irrational: 不合逻辑; optimally: 最优化地; suboptimal: 次优的

**[6527.64s] English:** estimate that kind of stuff like what what stands out to you like is there a crack that you can  
**Translation:** 

**[6532.62s] English:** exploit is there like um a weakness that you can exploit in the game  
**Translation:** 

**[6537.98s] English:** that  
**Translation:** 

**[6538.50s] English:** that everybody's looking for well i think you're asking kind of two questions there so one like  
**Translation:** 

**[6545.90s] English:** modeling the irrationality and the suboptimality of humans um you can't in diplomacy you can't  
**Translation:** 

**[6553.78s] English:** treat all the other players like they're machines and if you do that you're you're going to end up  
**Translation:** Vocabulary: diplomacy: 外交; irrationality: 非理性; suboptimality: 次优化

**[6558.26s] English:** playing really poorly and so we actually ran this experiment so we we trained a bot in a two-player  
**Translation:** 

**[6564.00s] English:** zero-sum version of diplomacy um the same way that you might approach a game like  
**Translation:** 

**[6568.50s] English:** chasser poker and the bot was superhuman it would crush any competitor and then we took that same  
**Translation:** 

**[6573.90s] English:** training approach and we trained a bot for the full seven player version of the game through  
**Translation:** Vocabulary: poker: 纸牌游戏

**[6577.98s] English:** self-play without any human data and we stuck it in a game with six humans and it got destroyed  
**Translation:** 

**[6583.20s] English:** even in the version of the game where there's no explicit natural language communication  
**Translation:** Vocabulary: explicit: 明确的

**[6587.12s] English:** it still got destroyed because it just wouldn't be able to understand how the other players were  
**Translation:** 

**[6591.88s] English:** approaching the game and be able to to work with that can you just link on that meaning like there's  
**Translation:** 

**[6597.38s] English:** an individual  
**Translation:** 

**[6598.50s] English:** there's an individual personality  
**Translation:** 

**[6600.00s] English:** each player and then you're supposed to remember that but what do you mean it's not able to  
**Translation:** 

**[6603.18s] English:** understand uh the players well it would for example expect the human to support it in a  
**Translation:** 

**[6610.12s] English:** certain way when the human would simply like think like no i'm not supposed to support you here um  
**Translation:** 

**[6616.34s] English:** it's kind of like you know if you develop a self-driving car and it's trained completely  
**Translation:** 

**[6620.54s] English:** from scratch with other self-driving cars it might learn to drive on the left side of the road  
**Translation:** 

**[6624.42s] English:** that's a totally reasonable thing to do if you're with these other self-driving cars that are also  
**Translation:** 

**[6628.58s] English:** driving on the left side of the road but if you put it in an american city it's going to crash  
**Translation:** 

**[6632.66s] English:** but i guess the intuition i'm trying to build up is why does it then crush a human player on  
**Translation:** Vocabulary: intuition: 直觉

**[6636.84s] English:** heads up this is multiple this is an aspect of two players zero sum versus games that involve  
**Translation:** 

**[6643.94s] English:** cooperation so in a two player zero sum game um you can do self-play from scratch and you will  
**Translation:** 

**[6650.78s] English:** arrive at the nash equilibrium where you don't have to worry about the other player playing in  
**Translation:** 

**[6657.04s] English:** a very human suboptimal style  
**Translation:** Vocabulary: equilibrium: 纳什均衡; suboptimal: 次优的

**[6658.48s] English:** that's just going to be that the only way that deviating from a nash equilibrium  
**Translation:** 

**[6662.08s] English:** um would would change things is if it helped you so i what's the dynamic of cooperation that's  
**Translation:** Vocabulary: deviating: 偏离

**[6669.38s] English:** effective in diplomacy do you always have to to have one friend in the game you always  
**Translation:** 

**[6675.46s] English:** want to maximize your friends and minimize your enemies  
**Translation:** Vocabulary: diplomacy: 外交; maximize: 最大化

**[6679.04s] English:** got it and boy and the the lying comes into play there  
**Translation:** 

**[6688.48s] English:** so the more friends you have the better yeah i mean i guess you have to attack somebody or else  
**Translation:** 

**[6694.28s] English:** you're not going to make progress right so that's the tension but this is too real this is too real  
**Translation:** 

**[6699.86s] English:** this is too too close to geopolitics of actual military conflict in the world okay uh that's  
**Translation:** Vocabulary: geopolitics: 地缘政治

**[6707.16s] English:** fascinating so that cooperation element is what makes the game really really hard yeah and to  
**Translation:** 

**[6712.34s] English:** give you an example of how this suboptimality and irrationality comes into play there's a really  
**Translation:** Vocabulary: irrationality: 非理性; suboptimality: 次优性

**[6718.48s] English:** common situation in  
**Translation:** 

**[6720.00s] English:** game of diplomacy um there where one player starts to win and they're like at the point where they're  
**Translation:** 

**[6725.54s] English:** controlling about half the map yeah um and the remaining players who have all been fighting each  
**Translation:** 

**[6729.86s] English:** other the whole game all have to like work together now to stop this other player from winning or else  
**Translation:** 

**[6734.40s] English:** everybody's going to lose um and it's kind of like you know game of thrones like i don't know  
**Translation:** 

**[6739.40s] English:** if you've seen the show like you know you got the the others coming from the north and like all the  
**Translation:** 

**[6742.42s] English:** people have to start you work out the differences and stop them from from taking over um and the bot  
**Translation:** 

**[6749.52s] English:** will do this like the bot will work with the other players to stop the superpower from winning  
**Translation:** Vocabulary: superpower: 超强势力

**[6753.36s] English:** but if it doesn't really if it's trained from scratch or it doesn't really have a good grounding  
**Translation:** 

**[6758.30s] English:** in how humans approach it it will also at the same time attack the other players with its extra units  
**Translation:** 

**[6763.92s] English:** so all the units that are not necessary to stop the superpower from winning it will use those to  
**Translation:** 

**[6768.54s] English:** grab as many centers as possible from the other players and in totally rational play the other  
**Translation:** 

**[6775.34s] English:** players should just live with that you know they have to understand like hey a score of one is  
**Translation:** 

**[6779.50s] English:** better than a score of zero so um so okay he's grabbed my centers but i i'll just deal with it  
**Translation:** 

**[6785.48s] English:** but humans don't act that way right the human gets really angry at the bot and ends up throwing the  
**Translation:** 

**[6791.40s] English:** game because you know i'm going to screw you over because you did something that's not fair to me  
**Translation:** 

**[6797.48s] English:** got it and are you supposed to model that is the bot supposed to model that kind of  
**Translation:** 

**[6802.36s] English:** human frustration yeah exactly and so that is something that seems almost impossible to model  
**Translation:** 

**[6809.50s] English:** purely from scratch without any human data it's a very cultural thing yeah um and so you need  
**Translation:** 

**[6815.02s] English:** human data to be able to understand that hey that's how humans behave and you have to work  
**Translation:** 

**[6819.58s] English:** around that it might be suboptimal it might be irrational but but that's an aspect of humanity  
**Translation:** 

**[6824.62s] English:** that you have to have you have to deal with so how difficult is it to train on human data given  
**Translation:** Vocabulary: irrational: 不合常理; suboptimal: 次优的

**[6829.74s] English:** that human data is very limited versus what us a purely self-play mechanism can generate  
**Translation:** 

**[6835.26s] English:** that's actually one of the major challenges that we faced in the research that we had a good amount  
**Translation:** 

**[6839.48s] English:** of human data  
**Translation:** 

**[6840.00s] English:** about 50 000 games what we try to do is leverage as much self-play as possible while still leveraging  
**Translation:** Vocabulary: leverage: 利用; leveraging: 利用

**[6847.04s] English:** the human data so what we do is we do self-play very similar to how it's been done in poker and go  
**Translation:** 

**[6854.16s] English:** but we try to regularize the self-play towards the human data basically the way to think about it is  
**Translation:** Vocabulary: poker: 扑克牌游戏

**[6860.96s] English:** um we penalize the bot for choosing actions that are very unlikely under how under the human data  
**Translation:** 

**[6871.76s] English:** set and how do you know is there is this some kind of function that says this is human-like and not  
**Translation:** Vocabulary: penalize: 处罚

**[6878.16s] English:** yeah so we we train a bot through supervised learning to model the human play as much as  
**Translation:** 

**[6883.60s] English:** possible so we basically like train a neural net um on those 50 000 games and that gives us an  
**Translation:** Vocabulary: neural: 神经网络; supervised: 监督学习

**[6889.28s] English:** approximate that gives us a policy that allows us to train a bot to model the human play as much as  
**Translation:** 

**[6890.88s] English:** possible so we basically like train a neural net um on those 50 000 games and that gives us an  
**Translation:** Vocabulary: approximate: 近似

**[6890.96s] English:** approximate that gives us a policy that resembles to some extent how humans actually play the game  
**Translation:** 

**[6894.08s] English:** now this isn't a perfect model of human play because we don't have unlimited data we don't  
**Translation:** 

**[6898.80s] English:** have unlimited neural net capacity but it gives us some approximation uh is there some data on  
**Translation:** 

**[6904.56s] English:** the internet that's useful besides just diplomacy so on the language side of things is there some  
**Translation:** Vocabulary: approximation: 近似; diplomacy: 外交

**[6909.76s] English:** can you go to like reddit and um so sort of background model formulation that that's  
**Translation:** 

**[6916.88s] English:** useful for the game of diplomacy yeah absolutely and so for the language model which uh  
**Translation:** 

**[6920.88s] English:** um it's kind of like a separate question you know we didn't use the language model during  
**Translation:** 

**[6924.24s] English:** self-play training but we pre-trained the language model on you know tons of internet data  
**Translation:** 

**[6931.12s] English:** um as much as possible and then we fine-tuned it specifically on the diplomacy games  
**Translation:** 

**[6935.60s] English:** so we are able to like leverage the wider data set in order to uh fill in some of the gaps in  
**Translation:** 

**[6941.52s] English:** like how communication happens more broadly um besides just like specifically in these diplomacy  
**Translation:** 

**[6946.32s] English:** games okay cool so what what's some what are some interesting things that came to life from  
**Translation:** 

**[6950.80s] English:** this from this work uh to you like what are some insights about um about games where in the  
**Translation:** 

**[6960.00s] English:** natural language is involved and deep cooperation is involved?  
**Translation:** 

**[6964.38s] English:** Well, I think there's a few insights.  
**Translation:** 

**[6966.00s] English:** So first of all, the fact that you can't rely purely or even  
**Translation:** 

**[6971.74s] English:** largely on self-play, that you really  
**Translation:** 

**[6973.50s] English:** have to have an understanding of how humans approach the game,  
**Translation:** 

**[6977.12s] English:** I think that that's one of the major conclusions  
**Translation:** 

**[6979.12s] English:** that I'm drawing from this work.  
**Translation:** 

**[6981.04s] English:** And that is, I think, applicable more broadly  
**Translation:** 

**[6983.70s] English:** to a lot of different games.  
**Translation:** 

**[6984.96s] English:** So we've actually already taken the approaches  
**Translation:** 

**[6986.80s] English:** that we've used in diplomacy and tried them  
**Translation:** 

**[6988.70s] English:** on a cooperative card game called Hanabi.  
**Translation:** 

**[6991.78s] English:** And we've had a lot of success in that game as well.  
**Translation:** Vocabulary: cooperative: 合作的

**[6995.48s] English:** On the language side, I think the fact  
**Translation:** 

**[6999.22s] English:** that we were able to control the language model  
**Translation:** 

**[7003.08s] English:** through this intense approach was very effective.  
**Translation:** 

**[7007.18s] English:** And it allowed us, instead of just imitating  
**Translation:** Vocabulary: imitating: 模仿

**[7009.92s] English:** how humans would communicate, we're  
**Translation:** 

**[7011.80s] English:** able to go beyond that and able to feed into it  
**Translation:** 

**[7015.96s] English:** superhuman.  
**Translation:** 

**[7016.80s] English:** So that's one of the strategies that it can then  
**Translation:** 

**[7022.02s] English:** generate messages corresponding to.  
**Translation:** 

**[7024.54s] English:** Is there something you could say about detecting whether a person  
**Translation:** 

**[7027.66s] English:** or AI is lying or not?  
**Translation:** 

**[7030.66s] English:** The bot doesn't explicitly try to calculate whether somebody  
**Translation:** Vocabulary: explicitly: 明确地

**[7035.52s] English:** is lying or not.  
**Translation:** 

**[7036.72s] English:** But what it will do is try to predict what actions they're  
**Translation:** 

**[7040.62s] English:** going to take given the communications,  
**Translation:** 

**[7043.02s] English:** given the messages that they've sent to us.  
**Translation:** 

**[7045.06s] English:** So given our conversation, what do I  
**Translation:** 

**[7046.68s] English:** need to do to make sure that they're lying or not?  
**Translation:** 

**[7048.84s] English:** So basically, there is a calculation about whether you're  
**Translation:** 

**[7051.42s] English:** lying to me in that.  
**Translation:** 

**[7053.22s] English:** If you're, based on your messages,  
**Translation:** 

**[7055.44s] English:** if I think you're going to attack me this turn,  
**Translation:** 

**[7057.78s] English:** even though your messages say that you're not,  
**Translation:** 

**[7059.94s] English:** then essentially the bot is predicting that you're lying.  
**Translation:** 

**[7063.60s] English:** But it doesn't view it as lying the same way  
**Translation:** 

**[7066.96s] English:** that we would view it as lying.  
**Translation:** 

**[7068.70s] English:** But you could probably reformulate  
**Translation:** 

**[7070.68s] English:** with all the same data and make a classifier lying or not.  
**Translation:** 

**[7076.56s] English:** That was not something that we were focused on.  
**Translation:** 

**[7078.40s] English:** But I think that it is possible that  
**Translation:** 

**[7080.00s] English:** you know if you came up with some measurements of like what does it mean to tell a lie because  
**Translation:** 

**[7084.86s] English:** there's a spectrum right like if you're withholding some information is that a lie  
**Translation:** Vocabulary: withholding: 隐瞒信息

**[7089.80s] English:** um if you're mostly telling the truth but you forgot to mention this like one action out of  
**Translation:** 

**[7094.14s] English:** like 10 is that a lie um it's hard to draw the line but you know if you're willing to do that  
**Translation:** 

**[7099.04s] English:** and then you could possibly use it to uh to this feels like an argument inside a relationship now  
**Translation:** 

**[7105.38s] English:** what constitutes a lie um depends what you mean by the definition of the word is okay um  
**Translation:** 

**[7113.50s] English:** still it's fascinating because trust and lying is all intermixed into this and it's language models  
**Translation:** 

**[7121.22s] English:** that are becoming more and more sophisticated it's just a fascinating space to explore  
**Translation:** Vocabulary: intermixed: 掺杂; sophisticated: 复杂

**[7125.58s] English:** um what what what do you see as the future of this work um that is inspired by the  
**Translation:** 

**[7135.36s] English:** the breakthrough performance that you're getting here with diplomacy?  
**Translation:** Vocabulary: diplomacy: 外交

**[7141.26s] English:** I think there's a few different directions to take this work.  
**Translation:** 

**[7145.36s] English:** I think really what it's showing us is the potential that language models have.  
**Translation:** 

**[7150.82s] English:** I mean, I think a lot of people didn't think that this kind of result was possible even  
**Translation:** 

**[7154.24s] English:** today, despite all the progress that's been made in language models.  
**Translation:** 

**[7157.62s] English:** And so it shows us how we can leverage the power of things like self-play on top of language  
**Translation:** 

**[7163.84s] English:** models to get increasingly better performance.  
**Translation:** Vocabulary: leverage: 利用

**[7167.64s] English:** And the ceiling is really much higher than what we have right now.  
**Translation:** 

**[7172.46s] English:** Is this transferable somehow to chatbots for the more general task of dialogue?  
**Translation:** Vocabulary: chatbots: 聊天机器人; transferable: 可转移的

**[7180.70s] English:** There is a kind of negotiation here, a dance between entities that are trying to cooperate  
**Translation:** 

**[7186.38s] English:** and at the same time a little bit adversarial, which I think maps somewhat to the general  
**Translation:** Vocabulary: adversarial: 对立的; cooperate: 合作

**[7193.84s] English:** you know, the entire process of Reddit or like internet communication.  
**Translation:** 

**[7200.00s] English:** You're cooperating, you're adversarial, you're having debates, you're having camaraderie, all that kind of stuff.  
**Translation:** Vocabulary: camaraderie: 同甘共苦; cooperating: 合作

**[7206.70s] English:** I think one of the things that's really useful about diplomacy is that we have a well-defined value function.  
**Translation:** 

**[7212.82s] English:** There is a well-defined score that the bot is trying to optimize.  
**Translation:** 

**[7216.06s] English:** And in a setting like a general chatbot setting, it would need that kind of objective in order to fully leverage the techniques that we've developed.  
**Translation:** 

**[7227.00s] English:** What about what we talked about earlier with NPCs inside video games?  
**Translation:** 

**[7233.44s] English:** How can it be used to create, for Elder Scrolls VI, more compelling NPCs that you could talk to?  
**Translation:** 

**[7243.18s] English:** Instead of committing all kinds of violence with a sword and fighting dragons, just sit in a tavern and drink all day and talk to the chatbot.  
**Translation:** Vocabulary: compelling: 引人入胜; dragons: 龙; scrolls: 卷轴; tavern: 酒馆

**[7251.54s] English:** The way that we've approached AI and diplomacy is you condition the language on an intent.  
**Translation:** 

**[7256.34s] English:** Now, that intent...  
**Translation:** Vocabulary: diplomacy: 外交

**[7257.00s] English:** The intent in diplomacy is an action, but it doesn't have to be.  
**Translation:** 

**[7260.52s] English:** And you can imagine you could have NPCs in video games or the metaverse or whatever where there's some intent or there's some objective that they're trying to maximize and you can specify what that is.  
**Translation:** Vocabulary: maximize: 最大化; metaverse: 元宇宙

**[7273.32s] English:** And then the language can correspond to that intent.  
**Translation:** 

**[7277.50s] English:** Now, I'm not saying that this is happening imminently, but I'm saying that this is a future application potentially of this direction of research.  
**Translation:** Vocabulary: correspond: 符合

**[7284.76s] English:** So, what's the more general formulation?  
**Translation:** 

**[7287.00s] English:** Making self-play be able to scale the way self-play does and still maintain human-like behavior.  
**Translation:** 

**[7293.72s] English:** The way that we've approached self-play in diplomacy is we're trying to come up with good intents to condition the language model on.  
**Translation:** 

**[7304.02s] English:** And the space of intents is actions that can be played in the game.  
**Translation:** 

**[7307.66s] English:** Now, there is the potential to have a broader set of intents.  
**Translation:** 

**[7311.46s] English:** Things like long-term cooperation or long-term objectives.  
**Translation:** 

**[7317.00s] English:** Or, you know, gossip about what another player was saying.  
**Translation:** 

**[7320.00s] English:** saying. These are things that we're currently not conditioning the language model on. And so  
**Translation:** 

**[7324.24s] English:** it's not able to, we're not able to control it to say like, oh, you should be talking about this  
**Translation:** 

**[7328.86s] English:** thing right now. But it's quite possible that you could expand the scope of intents to be able to  
**Translation:** 

**[7334.44s] English:** allow it to talk about those things. Now, in the process of doing that, the self-play would become  
**Translation:** 

**[7339.06s] English:** much more complicated. And so that is a potential for future work. Okay, the increasing the number  
**Translation:** 

**[7344.90s] English:** of intents. I still am not quite clear how you keep the self-play integrated into the human  
**Translation:** 

**[7353.84s] English:** world. I'm a little bit loose on understanding how you do that. So we train in neural nets to  
**Translation:** Vocabulary: neural: 神经网络

**[7361.18s] English:** imitate the human data as closely as possible. And that's what we call the anchor policy.  
**Translation:** 

**[7367.04s] English:** And now when we're doing self-play, the problem with the anchor policy is that it's not a perfect  
**Translation:** 

**[7373.00s] English:** approximation of how humans actually play.  
**Translation:** 

**[7374.90s] English:** Because we don't have infinite data, because we don't have unlimited neural network capacity,  
**Translation:** Vocabulary: approximation: 近似

**[7379.80s] English:** it's actually a relatively suboptimal approximation of how humans actually play.  
**Translation:** 

**[7384.52s] English:** And we can improve that approximation by adding planning and RL. And so what we do is we get a  
**Translation:** Vocabulary: suboptimal: 次优的

**[7392.76s] English:** better approximation, a better model of human play by during the self-play process, we say,  
**Translation:** 

**[7399.86s] English:** you can deviate from this human anchor policy if there is an  
**Translation:** Vocabulary: deviate: 偏离

**[7404.70s] English:** action that you want to take. And so that's what we're doing. And so that's what we're doing.  
**Translation:** 

**[7404.88s] English:** It's not an action that has particularly high expected value, but it would have to be a really  
**Translation:** 

**[7411.44s] English:** high expected value in order to deviate from this human-like policy. So you basically say,  
**Translation:** 

**[7417.56s] English:** try to maximize your expected value while at the same time, stay as close as possible to the human  
**Translation:** Vocabulary: maximize: 最大化

**[7422.66s] English:** policy. And there is a parameter that controls the relative weighting of those competing objectives.  
**Translation:** 

**[7430.26s] English:** So the question I have is how sophisticated can the anchor policy,  
**Translation:** Vocabulary: parameter: 参数; sophisticated: 复杂的

**[7434.88s] English:** to have a policy that approximates human behavior, right?  
**Translation:** 

**[7439.84s] English:** Yeah.  
**Translation:** Vocabulary: approximates: 近似于

**[7440.00s] English:** so as you increase the number of intents as you generalize the the space in which this is  
**Translation:** 

**[7446.66s] English:** applicable and given that the human data is limited try to anticipate a policy that works for  
**Translation:** Vocabulary: anticipate: 预想; generalize: 泛化

**[7454.54s] English:** in much larger number of cases like how how difficult is the process of forming a damn good  
**Translation:** 

**[7460.92s] English:** anchor policy well it really comes down to how much human data you have so it's all about scaling  
**Translation:** 

**[7466.32s] English:** the human data i think the more human data you have the better and i think that that's going to  
**Translation:** 

**[7471.22s] English:** be the major bottleneck in in scaling to to more complicated um domains but that said you know  
**Translation:** Vocabulary: bottleneck: 瓶颈

**[7478.52s] English:** there might be the potential just like in the language model where we leveraged you know tons  
**Translation:** 

**[7482.68s] English:** of data on the internet and then specialized it for diplomacy um there is the future potential  
**Translation:** Vocabulary: diplomacy: 外交; leveraged: 利用

**[7487.78s] English:** that you can leverage huge amounts of data across the board and then specialize it in the data set  
**Translation:** 

**[7493.54s] English:** that you have for diplomacy and in that way you're essentially augmenting  
**Translation:** Vocabulary: augmenting: 增加; leverage: 利用; specialize: 专门化

**[7496.30s] English:** the amount of data that you have to what degree does this apply to the general the real world  
**Translation:** 

**[7505.02s] English:** diplomacy the geopolitics you know there's a game theory has a history of being applied to  
**Translation:** Vocabulary: geopolitics: 地缘政治

**[7511.96s] English:** understand and to give us hope about nuclear weapons for example the mutually assured  
**Translation:** 

**[7516.78s] English:** destruction is a game theoretic concept that you can formulate some people say it's oversimplified  
**Translation:** Vocabulary: oversimplified: 过于简化; theoretic: 理论的

**[7522.96s] English:** but nevertheless here we are and we somehow haven't blown out  
**Translation:** 

**[7526.06s] English:** ourselves  
**Translation:** 

**[7526.30s] English:** up do you see a future where this kind of this kind of system can be used to help us make  
**Translation:** 

**[7534.52s] English:** decisions geopolitical decisions in the world well like i said the original motivation for  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[7540.92s] English:** the game of diplomacy was the failures of world war one the diplomatic failures that led to war  
**Translation:** 

**[7545.68s] English:** and the real take-home message of diplomacy is that you know if people approach diplomacy the  
**Translation:** 

**[7553.08s] English:** right way then war is ultimately  
**Translation:** 

**[7556.06s] English:** unsuccessful um the way that i see it war is  
**Translation:** Vocabulary: unsuccessful: 不成功

**[7560.00s] English:** an inherently negative some game right there's always a better outcome than war for all the  
**Translation:** 

**[7564.72s] English:** parties involved and my hope is that you know as ai progresses then maybe this technology could be  
**Translation:** 

**[7571.80s] English:** used to help people make better decisions um across the board and you know hopefully avoid  
**Translation:** 

**[7578.82s] English:** negative some outcomes like war yeah i would look i mean i just came back from ukraine i'm going back  
**Translation:** 

**[7584.72s] English:** there uh on deep personal levels think a lot about  
**Translation:** 

**[7590.04s] English:** how peace can be achieved and i'm a big believer in conversation  
**Translation:** 

**[7596.18s] English:** leaders getting together and having conversations and trying to understand each other  
**Translation:** 

**[7601.34s] English:** yeah it's fascinating to think um whether each one of those leaders can run a simulation ahead  
**Translation:** Vocabulary: simulation: 模拟

**[7607.30s] English:** of time like if i'm an asshole what are the possible consequences if i'm nice what are the  
**Translation:** 

**[7614.34s] English:** possible consequences if i'm not nice what are the possible consequences if i'm not nice  
**Translation:** Vocabulary: asshole: 混蛋

**[7614.72s] English:** consequences. My guess is that if the President of the United States got together with Vladimir  
**Translation:** 

**[7623.96s] English:** Zelensky and Vladimir Putin, that there would be significant benefits to the President of the  
**Translation:** Vocabulary: vladimir: 弗拉基米尔; zelensky: 泽连斯基

**[7632.50s] English:** United States not having the ego of kind of playing down, of giving away a lot of chips  
**Translation:** 

**[7638.78s] English:** for the future success of a world. So giving a lot of power to the two presidents of the  
**Translation:** 

**[7644.72s] English:** competing nations to achieve peace. That's my guess. But it'd be nice to run a bunch of  
**Translation:** 

**[7650.34s] English:** simulations. But then you have to have human data, right? Because the game of diplomacy is  
**Translation:** Vocabulary: diplomacy: 外交艺术

**[7655.96s] English:** fundamentally different than geopolitics. You need data. I guess that's the question I have.  
**Translation:** 

**[7662.06s] English:** How transferable is this to, I don't know, any kind of negotiation, right? To any kind of  
**Translation:** Vocabulary: fundamentally: 根本上; geopolitics: 地缘政治; transferable: 可转移

**[7668.50s] English:** local...  
**Translation:** 

**[7668.74s] English:** Some local, I don't know, a bunch of lawyers arguing at a divorce, like divorce lawyers.  
**Translation:** 

**[7675.52s] English:** How transferable is this to all kinds of human negotiation?  
**Translation:** 

**[7678.80s] English:** Well, I feel like this isn't...  
**Translation:** 

**[7680.00s] English:** question that's unique to diplomacy i mean i think you look at rl breakthroughs reinforcement learning  
**Translation:** 

**[7684.48s] English:** breakthroughs in previous games as well like you know ai for starcraft ai for atari you haven't  
**Translation:** Vocabulary: breakthroughs: 重大突破; reinforcement: 强化学习; starcraft: 星际争霸

**[7689.52s] English:** really seen it deployed in the real world because you have these problems of it's really hard to  
**Translation:** 

**[7694.56s] English:** collect a lot of data and you don't have you don't have a well-defined action space you don't have a  
**Translation:** Vocabulary: deployed: 部署

**[7701.60s] English:** well-defined reward function these are all things that you really need for reinforcement learning  
**Translation:** 

**[7707.12s] English:** and planning to be really successful today now there are some domains where you do have that  
**Translation:** 

**[7712.72s] English:** code generation is one example theorem proving mathematics that's another example where you  
**Translation:** 

**[7717.60s] English:** have a well-defined action space you have a well-defined reward function  
**Translation:** Vocabulary: theorem: 定理

**[7721.12s] English:** and those are the kinds of domains where i can see rl in the short term  
**Translation:** 

**[7725.44s] English:** being incredibly powerful but yeah i think that those are the barriers to deploying this  
**Translation:** Vocabulary: barriers: 障碍; deploying: 部署

**[7732.00s] English:** at scale in the real world but the hope is that in the long run we'll be able to get there  
**Translation:** 

**[7736.96s] English:** you  
**Translation:** 

**[7737.12s] English:** will see diplomacy feels like closer to the real world than does starcraft  
**Translation:** 

**[7742.40s] English:** like because it's natural language right you're operating in the space of intense  
**Translation:** 

**[7746.08s] English:** and in the space of natural language that feels very close to the real world  
**Translation:** 

**[7749.36s] English:** and it also feels like you could get data on that from the internet yeah and that's why i do think  
**Translation:** 

**[7755.76s] English:** that diplomacy is taking a big step closer to the real world than anything that's came before  
**Translation:** 

**[7761.36s] English:** in terms of game ai breakthroughs the fact that you know we're we're communicating in natural  
**Translation:** 

**[7766.96s] English:** language we've we're leveraging the fact that we have this like general data set of uh dialogue and  
**Translation:** 

**[7773.52s] English:** and communication from a breadth of the internet um that is that is a big step in that direction  
**Translation:** Vocabulary: leveraging: 利用

**[7779.60s] English:** we're not 100 there but um but we're getting closer at least so if we actually return back  
**Translation:** 

**[7784.72s] English:** to poker and chess are some of the ideas that you're learning here with diplomacy  
**Translation:** Vocabulary: diplomacy: 外交艺术; poker: 纸牌游戏

**[7790.00s] English:** could you construct ai systems that play like humans like um make for  
**Translation:** 

**[7796.96s] English:** a fun opponent in a game of chess  
**Translation:** 

**[7800.00s] English:** Yeah, absolutely. We've already started looking into this direction a bit. So we tried to use the techniques that we've developed for diplomacy to make chess and go AIs. And what we found is that it led to much more human like strong chess and go players. The way that AIs like Stockfish today play is in a very inhuman style. It's very strong, but it's very different from how humans play.  
**Translation:** 

**[7824.30s] English:** And so we can take the techniques that we've developed for diplomacy, we do something similar in chess and go, and we end up with a bot that's both strong and human like.  
**Translation:** Vocabulary: stockfish: 国际象棋程序

**[7837.88s] English:** To elaborate on this a bit, like one way to approach making a human like AI for chess is to collect a bunch of human games, like a bunch of human grandmaster games, and just to supervise learning on those games.  
**Translation:** 

**[7851.90s] English:** But the problem is that if you do that, what you end up doing is you end up doing a lot of different things.  
**Translation:** Vocabulary: elaborate: 详述; grandmaster: 特级大师; supervise: 监督

**[7854.28s] English:** What you end up with is an AI that's substantially weaker than the human grandmasters that you've trained on, because the neural net is not able to approximate the nuance of the strategy.  
**Translation:** 

**[7865.92s] English:** This goes back to the planning thing that I mentioned, the search thing that I talked about before, that these human grandmasters, when they're playing, they're using search and they're using planning.  
**Translation:** Vocabulary: approximate: 近似; grandmasters: 特级大师; neural: 神经; nuance: 细微差别

**[7875.36s] English:** And the neural net alone, unless you have a massive neural net that's like a thousand times bigger than what we have right now, it's not able to approximate that.  
**Translation:** 

**[7884.28s] English:** Those details very effectively.  
**Translation:** 

**[7886.64s] English:** And on the other hand, you can leverage search and planning very heavily, but then what you end up with is an AI that plays in a very different style from how humans play the game.  
**Translation:** 

**[7897.48s] English:** Now, if you strike this intermediate balance by setting the regularization parameters correctly and say you can do planning, but try to keep it close to the human policy, then you end up with an AI that plays in both a very human like style and a very strong style.  
**Translation:** Vocabulary: leverage: 利用

**[7914.16s] English:** And.  
**Translation:** 

**[7914.28s] English:** You can actually even tune it to have a certain ELO rating.  
**Translation:** 

**[7918.30s] English:** So you can say play in the style of like a.  
**Translation:** 

**[7920.00s] English:** 2800 elo human um i wonder if you could do specific type of humans or categories of humans  
**Translation:** 

**[7926.02s] English:** so not just skill but style yeah i think so and so this is this is where the the research gets  
**Translation:** 

**[7933.22s] English:** interesting like you know one of the things that i was thinking about is and this is actually already  
**Translation:** 

**[7937.60s] English:** being done i think there's a researcher at the university of toronto that's working on this  
**Translation:** 

**[7940.66s] English:** um is to make an ai that plays in the style of a particular player like magnus carlson for example  
**Translation:** 

**[7946.88s] English:** you can make an ai that plays like magnus carlson and then where i think this gets interesting is  
**Translation:** 

**[7951.24s] English:** like hey maybe you're up against magnus carlson in the world championship or something you can  
**Translation:** Vocabulary: carlson: 卡尔森; magnus: Magnus

**[7955.62s] English:** play against this magnus carlson bot to prepare against the real magnus carlson and you can try  
**Translation:** 

**[7960.92s] English:** to explore strategies that he might struggle with um and try to figure out like how do you beat this  
**Translation:** 

**[7966.86s] English:** player in particular um on the other hand you can also have magnus carlson working with this bot to  
**Translation:** 

**[7971.90s] English:** try to figure out where he's weak um and where he needs to improve his strategy  
**Translation:** 

**[7975.90s] English:** um  
**Translation:** 

**[7976.88s] English:** and so i can envision this future where data on specific chess and go players becomes extremely  
**Translation:** Vocabulary: envision: 想象

**[7984.16s] English:** valuable because you can use that data to create specific models of how these particular players  
**Translation:** 

**[7989.36s] English:** play so increasingly human-like behavior and bots however as you've mentioned makes cheating  
**Translation:** 

**[7996.10s] English:** cheat detection much harder it it does yeah the way that cheat detection works  
**Translation:** 

**[8001.80s] English:** in a game like poker and a game like chess and go from what i understand  
**Translation:** Vocabulary: detection: 检测; poker: 扑克

**[8005.76s] English:** is  
**Translation:** 

**[8006.88s] English:** trying to see like is this person making moves that are very common among chess ais or you know  
**Translation:** 

**[8014.48s] English:** ais in general um but very uncommon among top human players  
**Translation:** 

**[8020.56s] English:** and if you have the development of these ais that play in a very strong style but also very human  
**Translation:** Vocabulary: uncommon: 不常见

**[8027.20s] English:** like style then that poses serious challenges for cheat detection and it makes you now ask yourself  
**Translation:** 

**[8033.52s] English:** a hard question about what is the role of ai systems as they play a very strong role as the  
**Translation:** 

**[8035.04s] English:** role of ai system as they're able to detect and you know fn that's really important i think that's  
**Translation:** 

**[8035.72s] English:** really important because that's where it gets to and that's where you have to focus on and why you're  
**Translation:** 

**[8035.84s] English:** making decisions as an AI system because that's what i'm trying to focus on right now is in terms of how to  
**Translation:** 

**[8036.38s] English:** work with your AI system and your AI system and your AI system as a whole if you have any questions  
**Translation:** 

**[8036.80s] English:** as they become more and more integrated in our society.  
**Translation:** 

**[8040.00s] English:** This kind of human-AI integration has some deep ethical issues that we should be aware of.  
**Translation:** 

**[8049.80s] English:** And also, it's a kind of cybersecurity challenge, right?  
**Translation:** 

**[8053.72s] English:** One of the assumptions we have when we play games is that there's a trust that it's only humans involved.  
**Translation:** Vocabulary: assumptions: 假设; cybersecurity: 网络安全

**[8060.42s] English:** And the better AI systems we create, which makes it super exciting, human-like AI systems with different styles of humans is really exciting.  
**Translation:** 

**[8069.52s] English:** But then we have to have the defenses better and better and better if we're to trust that we can enjoy human versus human game in a deeply fair way.  
**Translation:** 

**[8080.46s] English:** It's fascinating. It's just humbling.  
**Translation:** 

**[8084.46s] English:** Yeah, I think there's a lot of negative potential for this kind of technology.  
**Translation:** Vocabulary: humbling: 令人谦卑

**[8088.40s] English:** But at the same time, there's a lot of upside for it as well.  
**Translation:** 

**[8091.78s] English:** So, for example, right now, it's really hard to learn how to get better in games like chess and poker and Go  
**Translation:** Vocabulary: upside: 有利因素

**[8097.78s] English:** because the way that the AI is used.  
**Translation:** 

**[8099.52s] English:** The way that the AI plays is so foreign and incomprehensible.  
**Translation:** Vocabulary: incomprehensible: 难以理解

**[8102.36s] English:** But if you have these AIs that are playing, you can say, like, oh, I'm a 2000 Elo human.  
**Translation:** 

**[8106.54s] English:** How do I get to 2200?  
**Translation:** 

**[8108.08s] English:** Now you can have an AI that plays in the style of a 2200 Elo human, and that will help you get better.  
**Translation:** 

**[8114.26s] English:** Or you mentioned this problem of how do you know that you're actually playing with humans when you're playing online in video games?  
**Translation:** 

**[8121.74s] English:** Well, now we have the potential of populating these virtual worlds with agents, like AI agents,  
**Translation:** 

**[8129.52s] English:** that are actually fun to play with.  
**Translation:** 

**[8130.72s] English:** And you don't have to always be playing with other humans to have a fun time.  
**Translation:** 

**[8136.38s] English:** So, yeah, a lot of upside potential, too.  
**Translation:** 

**[8138.64s] English:** And I think with any sort of tool, there's the potential for a lot of greatness and a lot of downsides as well.  
**Translation:** 

**[8144.42s] English:** So in the paper that I got a chance to look at, there's a section on ethical considerations.  
**Translation:** Vocabulary: downsides: 负面后果; greatness: 卓越成就

**[8150.56s] English:** What's in that section?  
**Translation:** 

**[8151.66s] English:** What are some ethical considerations here?  
**Translation:** 

**[8153.54s] English:** Is it some of the stuff we already talked about?  
**Translation:** 

**[8155.46s] English:** There's some things that we've already talked about.  
**Translation:** 

**[8157.64s] English:** I think specific to...  
**Translation:** 

**[8159.52s] English:** Thank you.  
**Translation:** 

**[8160.00s] English:** diplomacy, there's also the challenge that the game is... There is a deception aspect to the  
**Translation:** 

**[8166.40s] English:** game. And so developing language models that are capable of deception is, I think, a dicey issue  
**Translation:** Vocabulary: deception: 欺骗; dicey: 棘手; diplomacy: 外交

**[8174.24s] English:** and something that makes research on diplomacy particularly challenging. So those kinds of issues  
**Translation:** 

**[8183.52s] English:** of like, should we even be developing AIs that are capable of lying to people? That's something  
**Translation:** 

**[8187.44s] English:** that we have to think carefully about. That's so cool. I mean, you have to do  
**Translation:** 

**[8191.92s] English:** that kind of stuff in order to figure out where the ethical lines are. But I can see in the future,  
**Translation:** 

**[8196.16s] English:** it being illegal to have a consumer product that lies. Like your personal assistant AI system is  
**Translation:** 

**[8206.24s] English:** not allowed, you always have to tell the truth. But if I ask it, did I get fatter over the past  
**Translation:** 

**[8212.56s] English:** month? I sure as hell want that AI system to lie to me. So that's something that we have to think  
**Translation:** 

**[8217.42s] English:** about. There's a trade-off between lying and being nice. We have to somehow find...  
**Translation:** 

**[8223.74s] English:** What is the ethics in that? And we're back to discussions inside relationships.  
**Translation:** 

**[8227.26s] English:** Anyway, what were you saying? Oh, yeah. I was saying like, yeah,  
**Translation:** 

**[8229.74s] English:** that's kind of going to the question of like, what is a lie? Is it a white lie, a bad lie? Is  
**Translation:** 

**[8233.82s] English:** it an ethical lie? Those kinds of questions. Boy, we return time and time again to deep  
**Translation:** 

**[8240.94s] English:** human questions as we design AI systems. That's exactly what they do. They put a mirror to humanity  
**Translation:** 

**[8246.46s] English:** to help us understand the truth. Yeah.  
**Translation:** 

**[8246.64s] English:** To help us understand ourselves.  
**Translation:** 

**[8248.88s] English:** There's also the issue of like, in these diplomacy experiments, in order to do  
**Translation:** 

**[8254.32s] English:** a fair comparison, what we found is that there's an inherent anti-AI bias in these kinds of games.  
**Translation:** 

**[8260.64s] English:** So we actually played a tournament in a non-language version of the game  
**Translation:** 

**[8264.88s] English:** where we told the participants like, hey, in every single game, there's going to be an AI.  
**Translation:** 

**[8269.36s] English:** And what we found is that the humans would spend basically the entire game trying to  
**Translation:** 

**[8273.76s] English:** figure out who the bot was. And then as soon as they thought they figured it out, they would all  
**Translation:** 

**[8276.64s] English:** team up and try to kill it. And  
**Translation:** 

**[8280.00s] English:** So overcoming that inherent anti-AI bias is a challenge.  
**Translation:** 

**[8285.52s] English:** On the flip side, I think when robots become the enemy, that's when we get to heal our human divisions and then we can become one.  
**Translation:** 

**[8296.40s] English:** As long as we have one enemy, it's that Reagan thing when aliens show up.  
**Translation:** 

**[8300.72s] English:** That's when we put our side, our divisions, and we become one human species.  
**Translation:** Vocabulary: reagan: 里根时期

**[8305.40s] English:** We might have our differences, but we're at least all human.  
**Translation:** 

**[8307.40s] English:** At least we all hate the robots.  
**Translation:** 

**[8310.36s] English:** No, no, no, no.  
**Translation:** 

**[8311.64s] English:** I think there will be actually in the future something like a civil rights movement for robots.  
**Translation:** 

**[8315.44s] English:** I think that's the fascinating thing about AI systems is they force us to ask ethical questions about what is sentience,  
**Translation:** 

**[8324.76s] English:** how do we feel about systems that are capable of suffering or capable of displaying suffering,  
**Translation:** Vocabulary: sentience: 感知能力

**[8330.12s] English:** and how do we design products that show emotion and not?  
**Translation:** 

**[8333.74s] English:** How do we feel about that?  
**Translation:** 

**[8335.00s] English:** Lying is another topic.  
**Translation:** 

**[8336.36s] English:** Are we?  
**Translation:** 

**[8337.40s] English:** Going to allow bots to lie and not?  
**Translation:** 

**[8340.18s] English:** And where's the balance between being nice and telling the truth?  
**Translation:** 

**[8344.64s] English:** I mean, these are all fascinating human questions.  
**Translation:** 

**[8347.04s] English:** It's so exciting to be in the century when we create systems that take these philosophical questions that have been asked for centuries  
**Translation:** Vocabulary: philosophical: 哲学的

**[8356.96s] English:** and now we can engineer them inside systems where you really have to answer them  
**Translation:** 

**[8362.22s] English:** because you'll have transformational impact on human society,  
**Translation:** 

**[8366.54s] English:** depending on what you design inside those systems.  
**Translation:** 

**[8369.84s] English:** It's fascinating.  
**Translation:** 

**[8371.46s] English:** And like you said, I feel like diplomacy is a step towards the direction of the real world,  
**Translation:** 

**[8375.92s] English:** applying these RL methods towards the real world.  
**Translation:** Vocabulary: diplomacy: 外交

**[8378.68s] English:** From all the breakthrough performances in Go and chess and StarCraft and Dota,  
**Translation:** 

**[8384.36s] English:** this feels like the real world.  
**Translation:** 

**[8386.76s] English:** Especially now my mind's been on war and military conflict.  
**Translation:** 

**[8390.40s] English:** This feels like it can give us some deep insights about human behavior at the large geopolitical scale.  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[8396.54s] English:** What do you think?  
**Translation:** 

**[8400.00s] English:** is the breakthrough or the directions of work  
**Translation:** 

**[8408.16s] English:** that will take us towards solving intelligence,  
**Translation:** 

**[8410.96s] English:** towards creating AGI systems.  
**Translation:** 

**[8413.44s] English:** You've been a part of creating,  
**Translation:** 

**[8416.10s] English:** by the way, we should say a part of great teams that do this,  
**Translation:** 

**[8421.14s] English:** of creating systems that achieve breakthrough performances  
**Translation:** 

**[8424.64s] English:** on before-thought unsolvable problems  
**Translation:** Vocabulary: unsolvable: 无法解决的

**[8428.18s] English:** like poker, multiplayer poker, diplomacy.  
**Translation:** 

**[8432.92s] English:** We're taking steps towards that direction.  
**Translation:** Vocabulary: poker: 纸牌游戏

**[8435.58s] English:** What do you think it takes to go all the way  
**Translation:** 

**[8437.32s] English:** to create superhuman-level intelligence?  
**Translation:** 

**[8440.68s] English:** There's a lot of people trying to figure that out right now.  
**Translation:** 

**[8443.66s] English:** I should say the amount of progress that's been made,  
**Translation:** 

**[8446.48s] English:** especially in the past few years, is truly phenomenal.  
**Translation:** 

**[8449.40s] English:** You look at where AI was 10 years ago  
**Translation:** Vocabulary: phenomenal: 非凡的

**[8452.18s] English:** and the idea that you can have AIs that can generate language  
**Translation:** 

**[8455.08s] English:** and generate images the way they're doing today  
**Translation:** 

**[8457.06s] English:** and able to...  
**Translation:** 

**[8458.18s] English:** to play a game like diplomacy was just unthinkable,  
**Translation:** 

**[8461.84s] English:** even five years ago, let alone 10 years ago.  
**Translation:** 

**[8467.02s] English:** Now, there are aspects of AI that I think are still lacking.  
**Translation:** 

**[8472.26s] English:** I think there's general agreements  
**Translation:** 

**[8475.24s] English:** that one of the major issues with AI today  
**Translation:** 

**[8477.56s] English:** is that it's very data inefficient.  
**Translation:** 

**[8479.40s] English:** It requires a huge number of samples of training examples  
**Translation:** Vocabulary: inefficient: 低效的

**[8484.00s] English:** to be able to train.  
**Translation:** 

**[8485.32s] English:** You look at an AI that plays Go  
**Translation:** 

**[8487.30s] English:** and it needs...  
**Translation:** 

**[8488.12s] English:** millions of games of Go  
**Translation:** 

**[8489.74s] English:** to learn how to play the game well.  
**Translation:** 

**[8491.74s] English:** Whereas a human can pick it up and like, you know,  
**Translation:** 

**[8493.74s] English:** I don't know, how many games does a human Go player,  
**Translation:** 

**[8495.74s] English:** Go grandmaster play in their lifetime?  
**Translation:** Vocabulary: grandmaster: 围棋特级大师

**[8497.74s] English:** Probably, you know,  
**Translation:** 

**[8499.74s] English:** in the thousands or tens of thousands, I guess.  
**Translation:** 

**[8501.74s] English:** So that's one issue.  
**Translation:** 

**[8503.74s] English:** Data efficiency.  
**Translation:** 

**[8505.74s] English:** Overcoming this challenge of data efficiency.  
**Translation:** 

**[8507.74s] English:** And this is particularly important  
**Translation:** 

**[8509.74s] English:** if we want to deploy AI systems  
**Translation:** 

**[8511.74s] English:** in real-world settings  
**Translation:** Vocabulary: deploy: 部署

**[8513.74s] English:** where they're interacting with humans.  
**Translation:** 

**[8515.74s] English:** Because, you know, for example, with robotics,  
**Translation:** 

**[8517.74s] English:** it's really hard to generate a huge...  
**Translation:** 

**[8520.00s] English:** number of samples it's it's a different story when you're working in these you know totally  
**Translation:** 

**[8525.12s] English:** virtual games where you can play a million games and it's no big deal i was planning on just  
**Translation:** 

**[8529.20s] English:** launching like a thousand of these robots in austin i don't think it's illegal for legged  
**Translation:** 

**[8533.92s] English:** robots to roam the streets and just collect data that's not the worst that could happen yeah i kind  
**Translation:** 

**[8539.36s] English:** of mean that's one way to overcome the data efficiency problem it's like scale it yeah  
**Translation:** 

**[8543.60s] English:** like i actually tried to see if there's a law against robots like legged robots just operating  
**Translation:** 

**[8550.88s] English:** in in this in the streets of a major city and there isn't i couldn't find any so um i'll take  
**Translation:** 

**[8557.20s] English:** it all the way to the supreme court robot rights okay anyway sorry you were saying so  
**Translation:** 

**[8564.00s] English:** so what are the ideas we're getting becoming more data efficient uh i mean that's that's the  
**Translation:** 

**[8569.12s] English:** trillion dollar question in ai today i mean if you can figure out how to make ai systems more  
**Translation:** 

**[8573.12s] English:** more data efficient then that's a huge breakthrough so nobody really knows right now it could be just  
**Translation:** 

**[8579.52s] English:** a jagged  
**Translation:** 

**[8580.00s] English:** gigantic background model language model and then you do um the training becomes like prompting that  
**Translation:** Vocabulary: gigantic: 巨大的; jagged: 参差不齐的; prompting: 提示

**[8586.72s] English:** model to um to essentially do a kind of quarrying a search into the space of the things that's  
**Translation:** 

**[8593.68s] English:** learned to customize that to whatever problem you're trying to solve so maybe if you form a  
**Translation:** 

**[8598.48s] English:** large enough language model you can go quite quite a long way that you know i think there's some  
**Translation:** 

**[8603.52s] English:** truth to that i mean you look at the way humans approach um a game like poker they're not coming  
**Translation:** Vocabulary: poker: 纸牌游戏

**[8608.32s] English:** at it from scratch they're coming at it from the ground up they're coming at it from the ground up  
**Translation:** 

**[8609.28s] English:** they're coming at it from the ground up they're coming at it from the ground up they're coming at  
**Translation:** 

**[8609.52s] English:** they're coming at it with a huge amount of background knowledge about you know how humans  
**Translation:** 

**[8614.24s] English:** work how the world works um the idea of money so they're able to leverage that kind of information  
**Translation:** Vocabulary: leverage: 利用

**[8621.28s] English:** to uh to pick up the game faster so it's not really a fair comparison to then compare it to an  
**Translation:** 

**[8626.80s] English:** ai that's like learning from scratch and maybe one of the ways that we address this sample complexity  
**Translation:** Vocabulary: complexity: 样本复杂性

**[8631.36s] English:** problem is by allowing ais to leverage that general knowledge across a ton of different domains  
**Translation:** 

**[8637.92s] English:** so like i said you did uh  
**Translation:** 

**[8639.52s] English:** so like i said you did uh  
**Translation:** 

**[8640.00s] English:** a lot of incredible work in the space of research and actually building systems what advice would  
**Translation:** 

**[8645.28s] English:** you give to uh let's start with beginners what advice would you give to beginners interested  
**Translation:** 

**[8650.32s] English:** in machine learning just they're at the very start of their journey they're in high school  
**Translation:** 

**[8654.16s] English:** and college thinking like this seems like a fascinating world what advice would you give them  
**Translation:** 

**[8660.24s] English:** um i i would say that there are a lot of people working on similar aspects of machine learning  
**Translation:** 

**[8667.52s] English:** and to not be afraid to try something a bit different my own path in ai is pretty atypical  
**Translation:** 

**[8675.52s] English:** for a machine learning researcher today i mean i started out working on game theory and um  
**Translation:** Vocabulary: atypical: 不典型

**[8681.28s] English:** and then shifting more towards reinforcement learning as time went on and that actually had  
**Translation:** 

**[8685.52s] English:** a lot of benefits i think because it allowed me to look at these problems in a very different way  
**Translation:** Vocabulary: reinforcement: 强化; shifting: 转变

**[8689.84s] English:** from the way a lot of machine learning researchers view it and that comes with  
**Translation:** 

**[8697.12s] English:** drawbacks  
**Translation:** Vocabulary: drawbacks: 缺点

**[8697.52s] English:** in some respects like i think there's definitely aspects of machine learning where you know i'm  
**Translation:** 

**[8701.92s] English:** weaker than most of the researchers out there but i think that diversity of perspective um you know  
**Translation:** 

**[8707.52s] English:** when i'm working with my teammates um there's something that i'm bringing to the table and  
**Translation:** 

**[8711.28s] English:** something that they're bringing to the table and that kind of collaboration becomes very fruitful  
**Translation:** 

**[8714.56s] English:** for that reason so there could be problems like like poker like you've chosen diplomacy there  
**Translation:** 

**[8720.96s] English:** could be problems like that still out there that you can just tackle even if it seems extremely  
**Translation:** Vocabulary: diplomacy: 外交

**[8725.60s] English:** difficult  
**Translation:** 

**[8727.52s] English:** um i think that there's a lot of challenges challenges left and i think having a diversity  
**Translation:** 

**[8732.48s] English:** of viewpoints and backgrounds is really helpful for working together to figure out how to tackle  
**Translation:** 

**[8739.68s] English:** those kinds of challenges as a beginner so that i i would say that's that's more for like a grad  
**Translation:** Vocabulary: viewpoints: 观点

**[8744.72s] English:** student they already built up a base like a complete beginner what's a good journey so for  
**Translation:** 

**[8749.44s] English:** you that was doing some more on the math side of things doing game theory all that so it's basically  
**Translation:** 

**[8755.36s] English:** build up a foundation in something so basically building that foundation and so that's where you  
**Translation:** 

**[8757.34s] English:** So programming, mathematics, it can even be.  
**Translation:** 

**[8760.00s] English:** physics but build build that foundation yeah i would say build a strong foundation in math and  
**Translation:** 

**[8765.92s] English:** computer science and statistics and these kinds of areas but but don't be afraid to try something  
**Translation:** 

**[8771.14s] English:** that's different and learn something that's different from you know the the thing that  
**Translation:** 

**[8774.96s] English:** everybody else is doing to get into machine learning um you know there's there's value  
**Translation:** 

**[8778.48s] English:** in having a different background than everybody else um yeah so but certainly having a strong  
**Translation:** 

**[8785.70s] English:** math background especially in things like linear algebra and statistics and probability um are  
**Translation:** Vocabulary: algebra: 代数

**[8790.72s] English:** incredibly helpful today for for learning about and understanding machine learning do you think  
**Translation:** 

**[8795.76s] English:** one day we'll be able to since you're taking steps from poker to diplomacy one day we'll be able to  
**Translation:** Vocabulary: poker: 纸牌游戏

**[8800.92s] English:** uh figure out how to live life optimally well what is it like in in poker and diplomacy you  
**Translation:** 

**[8809.48s] English:** need a value function you need to have a reward system and so what does it mean to live a life  
**Translation:** Vocabulary: optimally: 最优化地

**[8814.14s] English:** that's optimal so  
**Translation:** 

**[8815.34s] English:** okay  
**Translation:** Vocabulary: optimal: 最佳的

**[8815.68s] English:** so then you can exactly like lay down a reward function being like i want to be rich  
**Translation:** 

**[8821.56s] English:** or i want to be um i want to be in a happy relationship and then you'll say well  
**Translation:** 

**[8828.54s] English:** do x you know there's there's a lot of uh talk today about in in ai safety circles about like  
**Translation:** 

**[8836.22s] English:** misspecification of you know reward functions so you you say like okay my objective is to be rich  
**Translation:** Vocabulary: misspecification: 规格错误

**[8842.76s] English:** and maybe the ai tells you like okay well if you want to maximize  
**Translation:** 

**[8845.32s] English:** the probability that you're rich go rob a bank sure uh and so you want to is that is that really  
**Translation:** Vocabulary: maximize: 最大化

**[8850.08s] English:** what you want is your objective really to be rich at all costs or is it more nuanced than that so the  
**Translation:** 

**[8855.34s] English:** unintended consequences yeah yeah so yeah that that that's so maybe life is more about defining  
**Translation:** Vocabulary: nuanced: 复杂多面; unintended: 意外产生

**[8865.64s] English:** the reward function that minimizes the unintended consequences than it is about the actual policy  
**Translation:** 

**[8872.12s] English:** that gets you to the reward function maybe life is just about the fact that you're rich and you're  
**Translation:** Vocabulary: minimizes: 最小化

**[8875.32s] English:** constantly updating the reward function i think  
**Translation:** 

**[8880.00s] English:** one of the challenges in life is is figuring out exactly what that reward function is sometimes  
**Translation:** 

**[8884.60s] English:** it's pretty hard to specify the same way that you know trying to handcraft the optimal policy in a  
**Translation:** 

**[8889.82s] English:** game like chess is really difficult um it's not so clear-cut what the reward function is for  
**Translation:** Vocabulary: handcraft: 手工制作

**[8894.26s] English:** for life i think one day ai will figure it out  
**Translation:** 

**[8897.92s] English:** and i wonder what that would be until then i just really appreciate the kind of work you're doing  
**Translation:** 

**[8905.76s] English:** and um it's it's really fascinating taking a leap into a more and more real world like  
**Translation:** 

**[8911.68s] English:** um problem space and just achieving incredible results by applying reinforcement learning no  
**Translation:** Vocabulary: reinforcement: 强化学习

**[8920.42s] English:** since i saw you work on poker you've been a constant inspiration it's an honor to get to  
**Translation:** 

**[8925.30s] English:** finally talk to you and uh this is really fun thanks for having me thanks for listening to  
**Translation:** Vocabulary: poker: 纸牌游戏

**[8930.32s] English:** this conversation with no brown to support this podcast please check out our sponsors in the  
**Translation:** 

**[8934.92s] English:** description  
**Translation:** Vocabulary: sponsors: 赞助商

**[8935.76s] English:** and now let me leave you with some words from sanzu and the art of war the whole secret lies  
**Translation:** 

**[8943.06s] English:** in confusing the enemy so that he cannot fathom our real intent thank you for listening and hope  
**Translation:** Vocabulary: cannot: 无法; fathom: 理解

**[8950.76s] English:** to see you next time  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
