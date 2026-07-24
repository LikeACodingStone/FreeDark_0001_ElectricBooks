# Podcast vocabulary notes
Source file: Lex Fridman - State of AI in 2026： LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI ｜ Lex Fridman Podcast #490.opus

**[0.00s] English:** The following is a conversation all about the state-of-the-art in artificial intelligence,  
**Translation:** 

**[4.98s] English:** including some of the exciting technical breakthroughs and developments in AI that  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[9.34s] English:** happened over the past year, and some of the interesting things we think might happen this  
**Translation:** 

**[14.94s] English:** upcoming year. At times, it does get super technical, but we do try to make sure that  
**Translation:** Vocabulary: upcoming: 即将来临的

**[21.10s] English:** it remains accessible to folks outside the field without ever dumbing it down. It is a great honor  
**Translation:** 

**[28.28s] English:** and pleasure to be able to do this kind of episode with two of my favorite people in the AI  
**Translation:** 

**[34.16s] English:** community, Sebastian Rashka and Nathan Lambert. They are both widely respected machine learning  
**Translation:** 

**[42.12s] English:** researchers and engineers who also happen to be great communicators, educators, writers, and  
**Translation:** Vocabulary: communicators: 沟通者; educators: 教育者

**[48.04s] English:** Twitterers, ex-posters. Sebastian is the author of two books I highly recommend for beginners and  
**Translation:** 

**[55.50s] English:** experts alike. First is Build a  
**Translation:** 

**[58.26s] English:** Large Language Model from Scratch, and Build a Reasoning Model from Scratch. I truly believe  
**Translation:** 

**[66.12s] English:** in the machine learning computer science world, the best way to learn and understand something  
**Translation:** 

**[71.52s] English:** is to build it yourself from scratch. Nathan is the post-training lead at the Allen Institute for  
**Translation:** 

**[79.78s] English:** AI and author of the definitive book on reinforcement learning from human feedback.  
**Translation:** Vocabulary: definitive: 权威性的; reinforcement: 强化

**[86.32s] English:** Both of them have great  
**Translation:** 

**[88.24s] English:** ex-accounts, great sub-stacks. Sebastian has courses on YouTube, Nathan has a podcast,  
**Translation:** Vocabulary: nathan: 内森; sebastian: 塞巴斯蒂安

**[94.90s] English:** and everyone should absolutely follow all of those. This is the Lex Friedman Podcast. To support it,  
**Translation:** 

**[101.50s] English:** please check out our sponsors in the description where you can also find links to contact me,  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[107.12s] English:** ask questions, get feedback, and so on. And now, dear friends, here's Sebastian Rashka and Nathan  
**Translation:** 

**[115.36s] English:** Lambert.  
**Translation:** Vocabulary: lambert: 拉姆伯特

**[118.24s] English:** Useful lens to look at all  
**Translation:** 

**[120.00s] English:** this through is the deep seek so-called deep seek moment this happened about a year ago in january  
**Translation:** 

**[126.38s] English:** 2025 when the open weight chinese company deep seek released deep seek r1 that i think it's fair  
**Translation:** 

**[133.62s] English:** to say surprised everyone with uh near or at state-of-the-art performance with allegedly  
**Translation:** Vocabulary: allegedly: 据说

**[140.36s] English:** much less compute for much cheaper and from then to today the ai competition has gotten insane  
**Translation:** 

**[148.34s] English:** both on the research level on the product level it's just been accelerating let's discuss all  
**Translation:** Vocabulary: accelerating: 加速

**[153.02s] English:** this today and maybe let's start with some spicy questions if we can uh who is winning  
**Translation:** 

**[159.60s] English:** at the international level would you say it's a set of companies in china or the set of companies  
**Translation:** 

**[165.80s] English:** in the united states and sebastian nathan it's good to see you guys uh so sebastian who do you  
**Translation:** 

**[172.52s] English:** think is winning um so winning is a very broad uh you know term i would say you mentioned  
**Translation:** 

**[178.34s] English:** the deep seek moment and i do think deep seek is definitely winning the hearts of the people who  
**Translation:** 

**[182.72s] English:** work on open weight models because they share these as open models um winning i think has  
**Translation:** 

**[188.84s] English:** multiple time scales to it we have today we have next year we have in 10 years one thing i know for  
**Translation:** 

**[194.48s] English:** sure is that um i don't think nowadays 2026 that there will be any company who is let's say having  
**Translation:** 

**[202.64s] English:** access to a technology that no other company has access to and that is mainly because researchers  
**Translation:** 

**[208.34s] English:** are frequently changing jobs changing labs they rotate so i don't think there will be a clear  
**Translation:** 

**[215.00s] English:** winner in terms of technology access however i do think there will be uh the differentiating  
**Translation:** 

**[220.90s] English:** factor will be budget and hardware constraints so i don't think the ideas will be proprietary but  
**Translation:** Vocabulary: constraints: 限制; differentiating: 区分的; proprietary: 专有的

**[227.16s] English:** the way or the resources that are needed to implement them and so i don't see currently  
**Translation:** 

**[234.30s] English:** take it all scenario where a winner takes it all i can't see that at the moment  
**Translation:** 

**[238.34s] English:** uh nathan what do you think  
**Translation:** 

**[240.00s] English:** You see the labs put different energy into what they're trying to do. And I think to demarcate the point in time when we're recording this, the hype over Anthropix Cloud Opus 4.5 model has been absolutely insane, which is just, I mean, I've used it and built stuff in the last few weeks.  
**Translation:** Vocabulary: anthropix: 人工智障; demarcate: 划分

**[256.98s] English:** And it's almost gotten to the point where it feels like a bit of a meme in terms of the hype. And it's kind of funny because this is very organic. And then if we go back a few months ago, we can get the release date in the notes as Gemini 3 from Google got released. And it seemed like the marketing and just like wow factor of that release was super high.  
**Translation:** 

**[277.32s] English:** But then at the end of November, Cloud Opus 4.5 was released and the hype has been growing. But Gemini 3 was before this. And it kind of feels like people don't really talk about it as much.  
**Translation:** 

**[286.72s] English:** Even though when it came out, everybody was like, this is Gemini's moment to retake kind of Google's structural advantages in AI. And Gemini 3 is a fantastic model, and I still use it. It's just kind of differentiation is lower. And I agree with Sebastian, what you're saying with all these, like, the idea space is very fluid, but culturally Anthropix is known for betting very hard on code, which is Cloud Code thing is working out for them right now.  
**Translation:** 

**[312.28s] English:** So I think that even if the ideas flow pretty freely, so much of this is bottleneck.  
**Translation:** Vocabulary: bottleneck: 瓶颈; culturally: 文化上; differentiation: 差异化; gemini: 金星; retake: 夺回; sebastian: 西贝柳斯

**[316.72s] English:** By human effort and kind of culture of organizations where Anthropix seems to at least be presenting as the least chaotic. It's a bit of an advantage. And if they can keep doing that for a while.  
**Translation:** 

**[327.30s] English:** But on the other side of things, there's a lot of ominous technology from China where there's way more labs than DeepSeek. So DeepSeek kicked off a movement within China, I say kind of similar to how ChatGPT kicked off a movement in the US where everything had a chatbot.  
**Translation:** Vocabulary: ominous: 令人不安的

**[342.98s] English:** There's now tons of tech companies in China that are releasing.  
**Translation:** 

**[346.72s] English:** very strong frontier openweight models to the point where I would say that DeepSeq is  
**Translation:** Vocabulary: frontier: 前沿; openweight: 大模型

**[350.90s] English:** kind of losing its crown as the preeminent open model maker in China and the likes of  
**Translation:** 

**[355.48s] English:** Z.AI with their GLM models, Minimax's models.  
**Translation:** Vocabulary: preeminent: 首屈一指

**[360.00s] English:** Kimmy Moonshot, especially in the last few months, has shown more brightly. The new DeepSeek models  
**Translation:** 

**[365.68s] English:** are still very strong, but that's kind of a, it could look back as a big narrative point where  
**Translation:** Vocabulary: brightly: 光芒四射; moonshot: 雄心壮志

**[370.90s] English:** in 2025 DeepSeek came and then it kind of provided this platform for way more Chinese companies that  
**Translation:** 

**[376.26s] English:** are releasing these fantastic models to kind of have this new type of operation. So these models  
**Translation:** 

**[381.42s] English:** from these Chinese companies are open weights. And depending on this trajectory of business models  
**Translation:** 

**[386.38s] English:** that these American companies are doing could be at risk. But currently, a lot of people are paying  
**Translation:** Vocabulary: trajectory: 发展趋势

**[391.44s] English:** for AI software in the U.S. and historically in China and other parts of the world, people don't  
**Translation:** 

**[396.26s] English:** pay a lot for software. So some of these models like DeepSeek have the love of the people because  
**Translation:** Vocabulary: historically: 历史上

**[401.78s] English:** they are open weight. How long do you think the Chinese companies keep releasing open weight  
**Translation:** 

**[406.52s] English:** models? I would say for a few years. I think that like in the U.S., there's not a clear business  
**Translation:** 

**[412.24s] English:** model for it. I have been writing about open models for a while and these Chinese  
**Translation:** 

**[416.24s] English:** companies have realized it. So I get inbound from some of them and they're smart and realize  
**Translation:** 

**[420.14s] English:** the same constraints, which is that a lot of U.S. tech companies and other IT companies won't pay  
**Translation:** 

**[424.68s] English:** for an API subscription to Chinese companies for security concerns. This has been a longstanding  
**Translation:** 

**[429.86s] English:** habit in tech. And the people at these companies then see open weight models as an ability to  
**Translation:** 

**[436.32s] English:** influence and take part of a huge growing AI expenditure market in the U.S. And they're  
**Translation:** Vocabulary: expenditure: 支出

**[441.36s] English:** very realistic about this and it's working for them. And I think that the government will see  
**Translation:** 

**[446.06s] English:** that.  
**Translation:** 

**[446.24s] English:** But that is building a lot of influence internationally in terms of uptake of the  
**Translation:** 

**[450.66s] English:** technology. So there's going to be a lot of incentives to keep it going. But building these  
**Translation:** Vocabulary: incentives: 激励; uptake: 采纳

**[455.24s] English:** models and doing the research is very expensive. So at some point, I expect consolidation. But I  
**Translation:** 

**[460.66s] English:** don't expect that to be a story of 2026, where there will be more open model builders throughout  
**Translation:** Vocabulary: consolidation: 合并

**[465.74s] English:** 2026 than there were in 2025. And a lot of the notable ones will be in China.  
**Translation:** 

**[470.44s] English:** You were going to say something?  
**Translation:** 

**[471.02s] English:** Yes. You mentioned DeepSeek losing its crown. I do think,  
**Translation:** 

**[475.42s] English:** to some extent, yes. But we also have to consider, though,  
**Translation:** 

**[479.64s] English:** the  
**Translation:** 

**[479.74s] English:** ...  
**Translation:** 

**[480.00s] English:** still i would say slightly ahead and the other ones it's not that deep seek got worse it's just  
**Translation:** 

**[485.52s] English:** like the other ones are using the ideas from deep seek for example you mentioned kimmy same  
**Translation:** 

**[490.14s] English:** architecture they're training it and then again we have this leapfrogging where they might be at  
**Translation:** 

**[494.86s] English:** some point in time a bit better because they have the more recent model and i think this comes back  
**Translation:** Vocabulary: leapfrogging: 后来居上

**[499.44s] English:** to the fact that there won't be a clear winner it will just be like like that one person releases  
**Translation:** 

**[505.38s] English:** something the other one comes in and the the recent the most recent model is probably always  
**Translation:** 

**[509.34s] English:** the best model yeah we'll also see the chinese companies have different incentives so like  
**Translation:** 

**[513.58s] English:** deep seek is very secretive where some of these startups are like the mini maxes and z.ai's of  
**Translation:** Vocabulary: startups: 初创公司

**[519.68s] English:** the world those two literally have filed ipo paperwork and they're trying to get western  
**Translation:** 

**[525.54s] English:** mindshare and do a lot of outreach there so i don't know if these incentives will kind of change  
**Translation:** Vocabulary: mindshare: 思想份额

**[529.36s] English:** the model development because deep seek famously is built by a hedge fund high flyer capital and  
**Translation:** 

**[534.50s] English:** we don't know exactly what we don't know what they use the models for or if they care about this  
**Translation:** 

**[538.88s] English:** they're  
**Translation:** 

**[539.32s] English:** secret in terms of communication they're not secret in terms of the technical reports that  
**Translation:** 

**[543.10s] English:** describe how their models work they're still open on that front and we should also say on the opus  
**Translation:** 

**[548.42s] English:** four five hype there's the layer of something being the darling of the x echo chamber on twitter  
**Translation:** 

**[558.26s] English:** echo chamber and the actual amount of people that are using the model i think it's probably  
**Translation:** 

**[563.82s] English:** fair to say that chad gpt and gemini are focused on the broad user base that just  
**Translation:** Vocabulary: gemini: 双子座模型

**[569.32s] English:** want to solve problems in their daily lives and that user base is gigantic so the hype about the  
**Translation:** 

**[575.88s] English:** coding may not be representative of the actual use i would say also um a lot of the usage patterns are  
**Translation:** Vocabulary: gigantic: 巨大的

**[582.84s] English:** like you said name recognition brand uh and stuff but also muscle memory almost where um you know  
**Translation:** 

**[589.32s] English:** like chad has been around for a long time people just got used to using it and it's kind of like  
**Translation:** 

**[593.64s] English:** almost like a flywheel they recommend it to other users and that stuff one interesting point is also  
**Translation:** 

**[599.32s] English:** the optimization of it  
**Translation:** Vocabulary: flywheel: 飞轮; optimization: 优化

**[600.00s] English:** lms for example chat gpt has a memory feature right and so you may have a subscription and you  
**Translation:** 

**[606.66s] English:** use it for personal stuff but i don't know if you want to use that same thing at work you know  
**Translation:** Vocabulary: subscription: 订阅

**[610.66s] English:** because that's the boundary between private and work if you're working at a company they might  
**Translation:** 

**[614.24s] English:** not allow that or you may not want that and i think that's also an interesting point where  
**Translation:** 

**[618.66s] English:** you might have multiple subscriptions one one is just clean code it keeps has nothing of your  
**Translation:** 

**[623.88s] English:** personal images that you or hobby projects in there it's just like the work thing and then  
**Translation:** 

**[628.24s] English:** the other one is your personal thing so i think that's also something where two different use  
**Translation:** 

**[632.58s] English:** cases and it doesn't mean you only have to have one it's i think the future is also multiple ones  
**Translation:** 

**[638.06s] English:** what model do you think won 2025 and what model do you think is going to win 26 i think in the  
**Translation:** 

**[643.94s] English:** context of a consumer chatbots is a question of are you willing to bet on gemini over chat gpt  
**Translation:** Vocabulary: chatbots: 对话机器人

**[650.06s] English:** which i would say in my gut feels like a bit of a risky bet because open ai has been the incumbent  
**Translation:** 

**[656.30s] English:** and there's so many benefits to that  
**Translation:** Vocabulary: incumbent: 现任者

**[658.24s] English:** in tech but i think the momentum if you look at 2025 was on gemini's side but they were starting  
**Translation:** 

**[665.00s] English:** from such a low point i think on rip bard and these earlier attempts of getting started i think  
**Translation:** 

**[672.34s] English:** huge credit for them for powering through the organizational chaos to make that happen  
**Translation:** 

**[677.44s] English:** but also it's hard to bet against chat to open ai because they always come off the cast  
**Translation:** 

**[682.26s] English:** as so chaotic but they're very good at landing things and i think like personally i have very  
**Translation:** 

**[688.24s] English:** good reviews of gpt 5 but it had to have saved them so much money with the headline feature being  
**Translation:** 

**[693.92s] English:** a router where most users are no longer charging like charging their gpu costs as much so i think  
**Translation:** 

**[700.30s] English:** it's very hard to dissociate the things that i like out of models versus the things that are  
**Translation:** Vocabulary: dissociate: 分离; router: 路由器

**[705.40s] English:** going to actually be a general public differentiator what do you think about 2026 who's going to win  
**Translation:** 

**[712.42s] English:** i'll say something even though it's risky i will say that i think gemini will continue  
**Translation:** Vocabulary: differentiator: 区分因素; gemini: 金星

**[716.14s] English:** to take progress on chat gpt i think  
**Translation:** 

**[718.24s] English:** it's going to continue to take progress on chat gpt i think  
**Translation:** 

**[720.00s] English:** operating at such extreme scales and like google has the ability to separate that research and  
**Translation:** 

**[726.20s] English:** product a bit better where you hear so much about open ai being chaotic operationally and chasing  
**Translation:** 

**[731.26s] English:** the high impact thing which is a very startup culture and then on the software and enterprise  
**Translation:** 

**[735.52s] English:** side i think anthropic will have continued to success as they've again and again been set up  
**Translation:** 

**[741.10s] English:** for that and obviously google's cloud has a lot of offerings but i think this kind of like gemini  
**Translation:** 

**[746.36s] English:** name brand is important for them to build and google's cloud will continue to do well as but  
**Translation:** 

**[751.28s] English:** that's kind of a more complex thing to explain in the ecosystem because that's competing with  
**Translation:** 

**[756.74s] English:** the likes of azure and aws rather than on the model provider side so in infrastructure you  
**Translation:** 

**[762.66s] English:** think gpu's give an advantage largely because the margin on nvidia chips is insane and google can  
**Translation:** 

**[770.12s] English:** develop everything from top to bottom to fit their stack and not have to pay this margin and they've  
**Translation:** 

**[776.14s] English:** had a  
**Translation:** 

**[776.34s] English:** head start in building data centers so all of these things that have both high lead times and  
**Translation:** 

**[780.40s] English:** very hard margins on high costs google has a just kind of a historical advantage there and if there's  
**Translation:** 

**[786.38s] English:** going to be a new paradigm it's most likely to come from open ai where they're kind of their  
**Translation:** Vocabulary: paradigm: 范式

**[790.40s] English:** research division again and again has kind of shown this ability to land a new research idea  
**Translation:** 

**[795.74s] English:** or a product i think like deep research so we're a 01 thinking models like all these definitional  
**Translation:** Vocabulary: definitional: 定义性的

**[802.14s] English:** things have come from open ai and that's got to be one of their top traits as an organization so  
**Translation:** 

**[808.24s] English:** it's kind of hard to bet against that but i think a lot of this year will be about scale and  
**Translation:** 

**[812.82s] English:** optimizing what could be described as low-hanging fruit in models and clearly there's a trade-off  
**Translation:** 

**[818.76s] English:** between intelligence and speed this was what chad gpt5 was trying to solve behind the scenes  
**Translation:** 

**[826.84s] English:** it's like do people actually want intelligence the broad public or do they want speed  
**Translation:** 

**[831.64s] English:** you  
**Translation:** 

**[832.14s] English:** i think it's a nice variety actually or the option to have a toggle there  
**Translation:** 

**[835.70s] English:** i mean first for my personal usage most of the time when i  
**Translation:** Vocabulary: toggle: 切换按钮

**[840.00s] English:** something up i use ggpt to ask a quick question get the information i want it fast for you know  
**Translation:** 

**[844.80s] English:** most daily tasks i use the quick model nowadays i think the auto mode is pretty good where you  
**Translation:** 

**[849.92s] English:** don't have to specifically say thinking or you know non-thinking and stuff then again i also  
**Translation:** 

**[854.64s] English:** sometimes want the pro mode very often what i do is when i have something written i put it into  
**Translation:** 

**[859.92s] English:** ggpt and say hey do a very thorough check is are all my references correct are all my thoughts  
**Translation:** 

**[865.84s] English:** correct uh did i make any formatting mistakes and are the figure numbers wrong or something like  
**Translation:** Vocabulary: formatting: 格式

**[870.80s] English:** that and i don't need that right away it's something okay i finish my stuff maybe have  
**Translation:** 

**[875.84s] English:** dinner let it run come back and go through this and i think see this is where i think it's  
**Translation:** 

**[880.80s] English:** important to have this option i would go crazy if for each query i would have to wait 30 minutes or  
**Translation:** 

**[885.20s] English:** 10 minutes that's me yeah um i'm like saying over here losing my mind that you use the router and  
**Translation:** 

**[891.52s] English:** the non-thinking model i'm like how do you how do you live with how do you live with that yeah  
**Translation:** 

**[895.84s] English:** like my reaction i'm been heavily on chat gpt for a while um never touched five non-thinking i find  
**Translation:** 

**[903.36s] English:** it its tone and then its propensity of errors it's just like has a higher likelihood of errors some  
**Translation:** 

**[908.80s] English:** of this is from back when opening i released 03 which was the first model to do this deep search  
**Translation:** Vocabulary: likelihood: 可能性; propensity: 倾向性

**[914.56s] English:** and find many sources and integrate them for you so i became habituated with that so i will only  
**Translation:** 

**[919.12s] English:** use gpt 5.2 thinking or pro when i'm finding any sort of information query for work whether that's  
**Translation:** Vocabulary: habituated: 习惯; integrate: 整合

**[925.68s] English:** a  
**Translation:** 

**[925.84s] English:** paper or some code reference that i found and it's just like i will regularly have like five pro  
**Translation:** 

**[932.24s] English:** queries going simultaneously each looking for one specific paper or feedback on the equation  
**Translation:** 

**[936.96s] English:** or something i have a fun example where i just needed to answer as fast as possible  
**Translation:** Vocabulary: equation: 方程

**[941.76s] English:** for this podcast before i was going on the trip um i have like a local gpu running at  
**Translation:** 

**[947.20s] English:** home and i wanted to run a long uh rl experiment and usually i also unplug things because you  
**Translation:** 

**[953.20s] English:** never know if you're not at home you don't want to have things plugged in  
**Translation:** 

**[955.68s] English:** and i accidentally unplugged the gp it was like my wife was already in the car  
**Translation:** Vocabulary: unplugged: 未插电

**[960.00s] English:** and it's like oh dang and then basically i wanted as fast as possible a bash script that runs my  
**Translation:** 

**[966.44s] English:** different uh experiments in the evaluation and i did something i know i learned how to use the bash  
**Translation:** 

**[972.18s] English:** uh interface or bash terminal but in that moment i just needed like 10 seconds give me the command  
**Translation:** 

**[978.60s] English:** this is a hilarious situation but yeah so what did you use so i did the non-thinking fastest model  
**Translation:** Vocabulary: interface: 用户界面

**[983.98s] English:** it gave me the bash command i to chain different scripts to each other and then the thing is like  
**Translation:** 

**[990.40s] English:** you have the t thing where you want to route this to a log file top of my head i was just like in a  
**Translation:** 

**[996.14s] English:** hurry i could have thought about it myself by the way i don't know if there's a representative case  
**Translation:** 

**[999.54s] English:** wife waiting in the car you have to run you unplug the gpu you have to generate a bash script this  
**Translation:** 

**[1004.24s] English:** sounds like a movie like impossible i use gemini for that so i use thinking for all the information  
**Translation:** 

**[1009.20s] English:** stuff and then gemini for fast things or stuff that i could sometimes google  
**Translation:** Vocabulary: gemini: 双子座

**[1013.28s] English:** which is  
**Translation:** 

**[1013.98s] English:** like it's good at explaining things and i trust that it has this kind of background of knowledge  
**Translation:** 

**[1018.34s] English:** and it's simple and the gemini app has gotten a lot better and it's good for that sort of things  
**Translation:** 

**[1022.50s] English:** and then for code and any sort of philosophical discussion i use claude opus 4.5 also always with  
**Translation:** Vocabulary: philosophical: 哲学讨论

**[1028.64s] English:** extended thinking extended thinking and inference time scaling is just a way to make the models  
**Translation:** 

**[1033.00s] English:** marginally smarter and i will always edge on that side when the progress is very high because you  
**Translation:** Vocabulary: inference: 推断; marginally: 略微

**[1039.34s] English:** don't know when that'll unlock a new use case and then sometimes use grok for  
**Translation:** 

**[1042.96s] English:** real  
**Translation:** 

**[1043.96s] English:** time information or finding something on ai twitter that i knew i saw and i need to dig up and i just  
**Translation:** 

**[1049.34s] English:** fixated on although when grok 4 came out the grok for what is super heavy which was like their pro  
**Translation:** 

**[1056.58s] English:** variant was actually very good and i was pretty impressed with it and i just kind of like muscle  
**Translation:** 

**[1060.52s] English:** memory lost track of it with having the chat to bt app open so i used many different things yeah  
**Translation:** 

**[1065.84s] English:** i actually do use grok for heavy for debugging for like hardcore debugging and the other ones can't  
**Translation:** 

**[1073.80s] English:** solve for debugging but i use grok for heavy for debugging and i use grok for heavy for debugging for  
**Translation:** Vocabulary: hardcore: hardcore

**[1073.96s] English:** I find that it's the best.  
**Translation:** 

**[1076.68s] English:** It's interesting because you say  
**Translation:** 

**[1078.02s] English:** ChagiPT is the best interface.  
**Translation:** 

**[1080.00s] English:** uh for me for that same reason but this could be just momentum uh gemini is the better interface  
**Translation:** 

**[1087.36s] English:** for me i think because i fell in love with their best needle in the haystack if i ever put something  
**Translation:** 

**[1093.84s] English:** that has a lot of context but i'm looking for very specific kinds of information make sure it  
**Translation:** Vocabulary: haystack: 针尖

**[1097.82s] English:** tracks all of it i find at least uh the gemini for me has been uh the best so it's funny with  
**Translation:** 

**[1105.38s] English:** some of these models if they win your heart over for one particular feature at one on a one  
**Translation:** 

**[1110.68s] English:** particular day for that particular query that prompt you're like this model is better and so  
**Translation:** 

**[1116.90s] English:** you'll just stick with it for a bit until it does something really dumb there's like a threshold  
**Translation:** Vocabulary: threshold: 临界点

**[1122.10s] English:** effect some smart thing and then you fall in love with it and then it does some dumb thing and you're  
**Translation:** 

**[1127.20s] English:** like you know what i'm going to switch and try claude and chad gpt and all that kind of stuff  
**Translation:** 

**[1130.72s] English:** this is exactly like you use it until it breaks until you have a problem and then  
**Translation:** 

**[1135.22s] English:** you're like i'm going to switch and try claude and chad gpt and all that kind of stuff  
**Translation:** 

**[1135.36s] English:** then you change uh the lm and i think it's the same how we use anything like our favorite text  
**Translation:** 

**[1141.60s] English:** editor operating systems or the browser i mean there are so many browser options safari firefox  
**Translation:** 

**[1146.94s] English:** chrome all the characterly similar but then there are edge cases maybe extensions you want to use  
**Translation:** 

**[1152.70s] English:** and then you switch but i don't think there is any one who types the same thing like the website  
**Translation:** Vocabulary: extensions: 扩展

**[1158.86s] English:** into different browsers and compares them you only do that when the website doesn't render if  
**Translation:** 

**[1162.56s] English:** something breaks i think so that's that's a good point i think  
**Translation:** Vocabulary: browsers: 浏览器; render: 渲染

**[1165.20s] English:** you use it until it breaks and then you explore other options i think on the long context thing  
**Translation:** 

**[1169.64s] English:** i was also a gemini user for this but the gpt 5.2 release blog had like crazy long context scores  
**Translation:** Vocabulary: gemini: Gemini

**[1175.04s] English:** where a lot of people were like did they just figure out some algorithmic change it went from  
**Translation:** 

**[1179.44s] English:** like 30 to like 70 or something in this minor model update so it's also very hard to keep  
**Translation:** Vocabulary: algorithmic: 算法的

**[1184.38s] English:** track of all of these things but now i'm look more favorably at gpt 5.2 is long context so  
**Translation:** 

**[1190.64s] English:** it's just kind of like how do i actually get to testing this  
**Translation:** 

**[1195.20s] English:** never-ending battle it's interesting that none of us talked about  
**Translation:** 

**[1200.00s] English:** Chinese models from a user usage perspective. What does that say? Does that mean the Chinese  
**Translation:** 

**[1205.74s] English:** models are not as good? Or does that mean we're just very biased and US focused?  
**Translation:** 

**[1211.34s] English:** I do think that that's currently the discrepancy between just the model and the platform. So I  
**Translation:** Vocabulary: discrepancy: 差异

**[1217.02s] English:** think the open models, they are more known for the open weights, not the platform yet.  
**Translation:** 

**[1221.28s] English:** There are also a lot of companies that are willing to sell you the open model inference  
**Translation:** Vocabulary: inference: 推断结果

**[1224.94s] English:** at a very low cost. I think like OpenRouter, it's easy to do the look at multi-model things. You  
**Translation:** 

**[1229.58s] English:** could run deep seek on perplexity. I think all of us sitting here are like, we use OpenAI GPT-5  
**Translation:** Vocabulary: perplexity: 困惑程度

**[1235.36s] English:** Pro consistently. We're all willing to pay for the marginal intelligence gain. And anyone that's  
**Translation:** 

**[1240.56s] English:** like these models from the US are better. And in terms of the outputs, I think that the question  
**Translation:** Vocabulary: marginal: 边际的

**[1247.00s] English:** is, will they stay better for this year and for years going? But it's like, so long as they're  
**Translation:** 

**[1252.24s] English:** better, I'm going to pay for it to use them. I think there's also analysis that shows that the  
**Translation:** 

**[1257.12s] English:** way that the Chinese  
**Translation:** 

**[1259.56s] English:** models are served, you could argue due to expert controls or not, is that they use fewer GPUs for  
**Translation:** 

**[1264.70s] English:** replica, which makes them slower and have different errors. And it's like speed and  
**Translation:** 

**[1269.20s] English:** intelligence. If these things are in your favor as a user, I think in the US, a lot of users will  
**Translation:** 

**[1273.40s] English:** go for this. And I think that that is something that will spur these Chinese companies to want  
**Translation:** 

**[1279.16s] English:** to compete in other ways, whether it's like free or substantially lower costs, or it'll breed  
**Translation:** 

**[1284.78s] English:** creativity in terms of offerings, which is good for the ecosystem. But I just think  
**Translation:** 

**[1289.56s] English:** the simple thing is the US models are currently better, and we use them. And I try these other  
**Translation:** 

**[1294.06s] English:** open models, and I'm like, fun, but I don't go back to it.  
**Translation:** 

**[1298.50s] English:** We didn't really mention programming. That's another use case that a lot of people deeply  
**Translation:** 

**[1304.10s] English:** care about. So I use basically half and half cursor and clog code, because I find them to be  
**Translation:** 

**[1310.94s] English:** like fundamentally different experience and both useful. What do you guys, you program quite a bit.  
**Translation:** Vocabulary: fundamentally: 根本上

**[1316.40s] English:** So what do you use? What's the current vibe?  
**Translation:** 

**[1319.56s] English:** I  
**Translation:** 

**[1320.00s] English:** use the codex plugin for vs code you know it's very convenient it's just like a plugin and then  
**Translation:** 

**[1324.62s] English:** it's a chat interface that has access to your repository i know that cloud code is i think a  
**Translation:** Vocabulary: codex: 代码库; interface: 界面; repository: 仓库

**[1329.72s] English:** bit different it's a bit more agentic it touches more things it does a whole project for you  
**Translation:** 

**[1333.08s] English:** i'm not quite there yet where i'm comfortable with that because maybe i'm a control freak but  
**Translation:** 

**[1339.26s] English:** i still would like to see a bit what's going on and codex is kind of like right now for me like  
**Translation:** 

**[1344.38s] English:** the sweet spot where it is helping me but it is not taking completely over i should mention one  
**Translation:** 

**[1350.06s] English:** of the reasons i do use cloud code is to build the skill of programming with english i mean the  
**Translation:** 

**[1355.78s] English:** experience is fundamentally different you're as opposed to micromanaging the details of the  
**Translation:** Vocabulary: micromanaging: 过度管理

**[1361.34s] English:** process of the generation of the code and uh looking at the diff which you can in cursor  
**Translation:** 

**[1366.88s] English:** if that's the idea you use and and in changing altering looking and reading the code and  
**Translation:** Vocabulary: altering: 修改

**[1373.72s] English:** understanding the code.  
**Translation:** 

**[1374.38s] English:** code deeply as you progress versus just kind of like thinking in this design space and just  
**Translation:** 

**[1382.52s] English:** guiding it at this macro level, which I think is another way of thinking about the programming  
**Translation:** 

**[1389.82s] English:** process. Also, we should say that cloud code, it just seems to be somehow a better utilization of  
**Translation:** 

**[1397.14s] English:** Cloud Opus 4.5. It's a good side-by-side for people to do. So you can have cloud code open,  
**Translation:** 

**[1402.08s] English:** you can have cursor open, you can have VS Code open, and you can select the same models on all  
**Translation:** 

**[1405.80s] English:** of them and ask questions. It's very interesting. The cloud code is way better in that domain. It's  
**Translation:** 

**[1411.66s] English:** remarkable. All right. We should say that both of you are legit on multiple fronts, researchers,  
**Translation:** Vocabulary: legit: 正牌

**[1417.86s] English:** programmers, educators, tweeters, and on the book front too. So Nathan, at some point soon,  
**Translation:** 

**[1427.82s] English:** hopefully has an RLHF book coming out. It's available for pre-order. And  
**Translation:** Vocabulary: educators: 教育者; programmers: 程序员; tweeters: 推特用户

**[1432.06s] English:** there's a full digital pre-print. I'm just making it pretty and better organized for  
**Translation:** 

**[1436.24s] English:** the physical thing, which is a lot of why I do it because it's fun.  
**Translation:** 

**[1440.00s] English:** to create things that you think are excellent in the physical form when so much of our life is  
**Translation:** 

**[1444.32s] English:** digital. I should say, going to perplexity here, Sebastian Roschka is a machine learning researcher  
**Translation:** Vocabulary: perplexity: 困惑

**[1449.16s] English:** and author known for several influential books. A couple of them that I wanted to mention, which is  
**Translation:** 

**[1454.00s] English:** a book I highly recommend, Build a Large Language Model from Scratch, and the new one, Build a  
**Translation:** 

**[1460.30s] English:** Reasoning Model from Scratch. So I'm really excited about that. Building stuff from scratch is one of  
**Translation:** 

**[1466.18s] English:** the most powerful ways of learning. Honestly, building an element from scratch is a lot of fun.  
**Translation:** 

**[1470.32s] English:** It's also a lot to learn. And like you said, it's probably the best way to learn how something  
**Translation:** 

**[1474.14s] English:** really works because you can look at figures, but figures can have mistakes. You can look at  
**Translation:** 

**[1479.26s] English:** concepts, explanations, but you might misunderstand them. But if you see there is code and the code  
**Translation:** 

**[1486.88s] English:** works, you know it's correct. I mean, there's no misunderstanding. It's precise. Otherwise,  
**Translation:** Vocabulary: misunderstand: 误解

**[1491.14s] English:** it wouldn't work. And I think that's kind of like the beauty behind coding. It is kind of like  
**Translation:** 

**[1495.38s] English:** it doesn't lie.  
**Translation:** 

**[1496.56s] English:** It's math, basically. So even though with math, I think you can have mistakes in a book you would  
**Translation:** 

**[1501.42s] English:** never notice because you're not running the math when you are reading the book. You can't verify  
**Translation:** Vocabulary: verify: 验证正确性

**[1505.78s] English:** this. And with code, what's nice is you can verify it. Yeah, I agree with you about the element from  
**Translation:** 

**[1510.84s] English:** scratch book. It's nice to tune out everything else, the internet and so on, and just focus on  
**Translation:** 

**[1515.56s] English:** the book. But, you know, I read several like, you know, history books. It's just less lonely  
**Translation:** 

**[1524.16s] English:** somehow. It's really more fun.  
**Translation:** 

**[1526.18s] English:** For example, on the programming front, I think it's genuinely more fun to program with an  
**Translation:** 

**[1530.80s] English:** LLM. And I think it's genuinely more fun to read with an LLM. But you're right, like this  
**Translation:** 

**[1537.80s] English:** distraction should be minimized. So it's you use the LLM to basically enrich the experience,  
**Translation:** 

**[1545.74s] English:** maybe add more context. Maybe the guy just the rate of aha moments for me in a small  
**Translation:** Vocabulary: distraction: 分心

**[1552.04s] English:** scale is really high with LLMs.  
**Translation:** 

**[1554.56s] English:** A hundred percent.  
**Translation:** 

**[1555.32s] English:** And I also want to correct myself.  
**Translation:** 

**[1557.22s] English:** I'm not suggesting not to use LLMs.  
**Translation:** 

**[1560.00s] English:** doing it in multiple passes like one pass just offline focus mode and then after that uh i mean  
**Translation:** 

**[1565.76s] English:** i also take notes but i i try to resist the urge to immediately look things up i do a second pass  
**Translation:** 

**[1573.10s] English:** it's just like for me more structured this way and i get let i mean sometimes things are answered  
**Translation:** 

**[1577.56s] English:** in the chapter but sometimes also it just helps to let it sink in and think about it other people  
**Translation:** 

**[1582.76s] English:** have different preferences i would highly recommend using llms when reading books for me  
**Translation:** 

**[1586.96s] English:** it's just it's not the first thing to do it's like the second pass my way of recommendation  
**Translation:** 

**[1590.86s] English:** is to say i do the opposite i like to use the lm at the beginning to lay out the full context of  
**Translation:** 

**[1596.82s] English:** like what is this world that i'm now stepping into but i try to avoid clicking out of the lm  
**Translation:** 

**[1603.74s] English:** into the world of like twitter blogs and because then you're now down this rabbit hole you're  
**Translation:** 

**[1610.56s] English:** reading somebody's opinion there's a flame war about a particular topic and all of a sudden  
**Translation:** 

**[1614.90s] English:** you're no longer you're now in the  
**Translation:** 

**[1616.74s] English:** in the  
**Translation:** 

**[1616.94s] English:** in the  
**Translation:** 

**[1616.96s] English:** realm of the internet and read it and so on but if you're purely letting the lm give you the  
**Translation:** 

**[1623.72s] English:** context of why this matters what are the big picture ideas but sometimes books themselves  
**Translation:** 

**[1629.08s] English:** are good at doing that but not always so this is why i like the chat gpt app that gives the ai  
**Translation:** 

**[1634.42s] English:** a home in your computer when you are folk you can focus on it rather than just being another tab in  
**Translation:** 

**[1639.70s] English:** my mess of internet options and i think claude code in these particular does a good job of making  
**Translation:** 

**[1646.04s] English:** that a joy where  
**Translation:** 

**[1646.94s] English:** it seems very engaging as a product design to be an interface that your ai will then go out into the  
**Translation:** Vocabulary: interface: 人机界面

**[1653.60s] English:** world and it's something that is very kind of intangible between it and codex is that it just  
**Translation:** 

**[1658.08s] English:** feels kind of warm and engaging where codex can often be as good from open ai but it just kind of  
**Translation:** Vocabulary: codex: 代码本; intangible: 无形

**[1663.56s] English:** like feels a little bit rougher on the edges whereas like claude code is makes it fun to  
**Translation:** 

**[1668.14s] English:** build things particularly from scratch where you just don't like you don't have to care but you  
**Translation:** 

**[1671.98s] English:** trust that it'll make something like obviously this is good for websites and kind of you know  
**Translation:** 

**[1676.92s] English:** refreshing tooling and stuff like this which i  
**Translation:** 

**[1680.00s] English:** use it for or data analysis so i my blog we scrape hugging face we keep the download numbers for every  
**Translation:** 

**[1685.42s] English:** data set and model over time now so we have them and it's like claude was just like yeah i've made  
**Translation:** Vocabulary: scrape: 抓取

**[1689.94s] English:** use of that data no problem and i was like that would have taken me days and it's like then i  
**Translation:** 

**[1694.04s] English:** have enough situational awareness to be like okay these trends obviously make sense and you can  
**Translation:** Vocabulary: situational: 情境的

**[1697.70s] English:** check things because that's just the kind of wonderful interface where you can have an  
**Translation:** 

**[1701.74s] English:** intermediary and not have to do the kind of awful low-level work that you would have to do to  
**Translation:** 

**[1706.60s] English:** maintain different web projects and do this stuff all right so we just talked about a bunch of the  
**Translation:** 

**[1711.94s] English:** closed weight models let's talk about the open ones uh so tell me about the landscape of open  
**Translation:** 

**[1719.08s] English:** lm models which are interesting ones which stand out to you and why we already mentioned deep seek  
**Translation:** 

**[1724.44s] English:** do you want to see how many we can name off the top of our head yeah without looking at notes  
**Translation:** 

**[1728.28s] English:** deep seek kimmy minimax z.ai antling we're just going chinese  
**Translation:** 

**[1735.96s] English:** you  
**Translation:** Vocabulary: minimax: 极小极大

**[1736.60s] English:** let's throw in mistral ai gemma um yeah gpt oss the open source model by chat gpt actually  
**Translation:** 

**[1745.34s] English:** nvidia nimotron had a or nvidia had a very cool one nimotron 3 um there's a lot of stuff especially  
**Translation:** Vocabulary: gemma: 宝石; nimotron: 尼莫tron

**[1750.56s] English:** at the end of the year quen one maybe the one oh yeah quen was the name the obvious name i was  
**Translation:** 

**[1754.42s] English:** i was trying to get through that you can get at least 10 chinese and at least 10 western i think  
**Translation:** 

**[1758.66s] English:** that i mean opening i released their first open model since gpt2 that was when i when i meant  
**Translation:** 

**[1764.66s] English:** talked when i was writing about opening i  
**Translation:** 

**[1766.60s] English:** was open model released they're all like don't forget about gpt2 which i thought was really funny  
**Translation:** 

**[1770.72s] English:** because it's just such a different time but gpt oss is actually a very strong model and does some  
**Translation:** 

**[1775.52s] English:** things that the other models don't do very well and i think that selfishly i'll promote a bunch  
**Translation:** 

**[1782.04s] English:** of like western companies so both in the us and europe have these like fully open models so i work  
**Translation:** 

**[1787.04s] English:** at allen institute for ai we've been building olmo which releases data and code and all of this  
**Translation:** 

**[1791.76s] English:** and now we have actual competition for people that are trying to release everything so that other people can take advantage of it  
**Translation:** 

**[1796.60s] English:** train these models. So there's the Institute for Foundation Models.  
**Translation:** 

**[1800.00s] English:** slash LM360, which is like had their K2 models of various types. Aperdis is a Swiss research  
**Translation:** Vocabulary: swiss: 瑞士的

**[1807.10s] English:** consortium. Hugging Face has small LM, which is very popular. NVIDIA's Nematron has started  
**Translation:** 

**[1813.92s] English:** releasing data as well. And then Stanford's Marin Community Project, which is kind of making it so  
**Translation:** Vocabulary: consortium: 合作组织; marin: 马林; nematron: 内马tron

**[1819.48s] English:** there's a pipeline for people to open a GitHub issue and implement a new idea and then have it  
**Translation:** 

**[1823.66s] English:** run in a stable language modeling stack. So this space, that list was way smaller in 2024. So I  
**Translation:** Vocabulary: pipeline: 流程

**[1831.32s] English:** think it was just AI2. So that's a great thing for more people to get involved in to understand  
**Translation:** 

**[1835.74s] English:** language models, which doesn't really have a Chinese company that has an analog. While I'm  
**Translation:** Vocabulary: analog: 类比物

**[1842.02s] English:** talking, I'll say that the Chinese open language models tend to be much bigger, and that gives them  
**Translation:** 

**[1848.02s] English:** this higher peak performance as MOEs, where a lot of these things that we like a lot, whether it was  
**Translation:** 

**[1852.44s] English:** Gemma.  
**Translation:** 

**[1853.66s] English:** And Nematron have tended to be smaller models from the US, which is starting to change from  
**Translation:** 

**[1858.70s] English:** US and Europe. Mistral Large 3 came out, which was a giant MOE model, very similar to DeepSeek  
**Translation:** 

**[1864.40s] English:** architecture in December. And then a startup, RCAI, and both Nematron and NVIDIA have teased  
**Translation:** 

**[1872.40s] English:** MOE models of this way bigger than 100 billion parameters, like this 400 billion parameter range  
**Translation:** 

**[1877.76s] English:** coming in this Q1 2026 timeline. So I think this kind of balance is set to change  
**Translation:** Vocabulary: parameter: 参数

**[1883.30s] English:** in the future.  
**Translation:** 

**[1883.66s] English:** This year, in terms of what people are using the Chinese versus US open models for, which I'm  
**Translation:** 

**[1889.34s] English:** personally going to be very excited to watch.  
**Translation:** 

**[1892.50s] English:** First of all, huge props for being able to name so many of these. Did you actually name Lama?  
**Translation:** Vocabulary: props: 称赞

**[1898.94s] English:** No.  
**Translation:** 

**[1899.66s] English:** I feel like this was not on purpose.  
**Translation:** 

**[1903.18s] English:** RIP Lama.  
**Translation:** 

**[1904.90s] English:** All right. Can you mention what are some interesting models that stand out? So you mentioned  
**Translation:** 

**[1908.72s] English:** QN3 is obviously a standout.  
**Translation:** 

**[1911.36s] English:** So I would say the year's almost book-ended.  
**Translation:** Vocabulary: standout: 突出者

**[1913.66s] English:** Rockahi in December was updated by both DeepSeek version 3 and R1, and then, on the other hand,  
**Translation:** 

**[1917.50s] English:** in December DeepSeek version 3.2, because  
**Translation:** 

**[1920.00s] English:** What I like about those is they always have an interesting architecture tweak that others don't have.  
**Translation:** 

**[1924.66s] English:** But otherwise, if you want to go with, you know, like the familiar but really good performance,  
**Translation:** Vocabulary: tweak: 调整

**[1929.80s] English:** QN3 and like Nathan said, also GPT-OSS.  
**Translation:** 

**[1933.24s] English:** And I think GPT-OSS, what's interesting about it is kind of like the first public or like open-weight model  
**Translation:** Vocabulary: nathan: 纳森

**[1939.80s] English:** that was really trained with tool use in mind,  
**Translation:** 

**[1942.74s] English:** which I do think is kind of a little bit of a paradigm shift where the ecosystem was not quite ready for it.  
**Translation:** Vocabulary: paradigm: 范式

**[1947.82s] English:** So with tool use, I mean that the LLM is able to do a web search to call a Python interpreter.  
**Translation:** 

**[1952.72s] English:** And I do think it's a standout because I think it's a huge unlock  
**Translation:** Vocabulary: interpreter: 解释器

**[1956.96s] English:** because one of the most common complaints about LLMs are, for example, hallucinations, right?  
**Translation:** 

**[1963.36s] English:** And so in my opinion, one of the best ways to solve hallucinations is to not try to always remember information  
**Translation:** Vocabulary: hallucinations: 妄想回应

**[1969.18s] English:** or make things up.  
**Translation:** 

**[1971.08s] English:** For math, why not use a calculator app or Python?  
**Translation:** 

**[1974.10s] English:** If I asked the LLM who won the soccer World Cup,  
**Translation:** 

**[1977.66s] English:** in 1998, instead of just trying to memorize, it could go do a search.  
**Translation:** Vocabulary: memorize: 背诵记忆

**[1982.94s] English:** I think mostly it's usually still a Google search.  
**Translation:** 

**[1985.90s] English:** So GPD, GPT-OSS, they would do a tool call to Google, maybe find the FIFA website, find, okay, it was France.  
**Translation:** 

**[1993.42s] English:** It would get you that information reliably instead of just trying to memorize it.  
**Translation:** 

**[1997.04s] English:** So I think it's a huge unlock, which I think right now is not fully utilized yet by the open source, open-weight ecosystem.  
**Translation:** Vocabulary: reliably: 可靠地; utilized: 利用

**[2004.50s] English:** A lot of people don't use tool call modes.  
**Translation:** 

**[2007.66s] English:** It's because I think it's first, it's a trust thing.  
**Translation:** 

**[2010.30s] English:** You don't want to run this on your computer where it has access to tools, could wipe your hard drive or whatever.  
**Translation:** 

**[2014.50s] English:** So you want to maybe containerize that.  
**Translation:** Vocabulary: containerize: 容器化

**[2017.42s] English:** But I do think, you know, that that is like a really important step for the upcoming years to have this ability.  
**Translation:** 

**[2024.04s] English:** So a few quick things.  
**Translation:** Vocabulary: upcoming: 即将来临的

**[2026.32s] English:** First of all, thank you for defining what you mean by tool use.  
**Translation:** 

**[2029.86s] English:** I think that's a great thing to do in general for the concepts we're talking about.  
**Translation:** 

**[2033.04s] English:** Even things as sort of well established as MOEs.  
**Translation:** 

**[2037.66s] English:** You have to say that means mixture of X.  
**Translation:** 

**[2040.00s] English:** person. You kind of have to build up an intuition for people what that means, how it's actually  
**Translation:** 

**[2044.96s] English:** utilized, what are the different flavors. So what does it mean that there's just such explosion of  
**Translation:** Vocabulary: intuition: 直觉

**[2050.18s] English:** open models? What's your intuition? If you're releasing an open model, you want people to use  
**Translation:** 

**[2055.60s] English:** it as the first and foremost thing. And then after that comes things like transparency and trust. I  
**Translation:** Vocabulary: foremost: 首要的

**[2060.22s] English:** think when you look at China, the biggest reason is that they want people around the world to use  
**Translation:** 

**[2065.88s] English:** these models. And I think a lot of people will not. If you look outside of the US, a lot of people  
**Translation:** 

**[2070.04s] English:** will not pay for software, but they might have computing resources where you can put a model on  
**Translation:** 

**[2073.28s] English:** it and run it. I think there can also be data that you don't want to send to the cloud. So the number  
**Translation:** Vocabulary: computing: 计算资源

**[2078.50s] English:** one thing is getting people to use models, use AI or use your AI that might not be able to do it  
**Translation:** 

**[2083.94s] English:** without having access to the model. I guess we should state explicitly. So we've been talking  
**Translation:** Vocabulary: explicitly: 明确地

**[2088.50s] English:** about these Chinese models and open weight models. Oftentimes, the way they're run is locally.  
**Translation:** 

**[2095.76s] English:** So  
**Translation:** Vocabulary: oftentimes: 经常

**[2095.86s] English:** it's not like you're sending your data to China or to Silicon Valley, whoever developed the model.  
**Translation:** 

**[2104.36s] English:** A lot of American startups make money by hosting these models from China and selling tokens. It's  
**Translation:** Vocabulary: startups: 初创公司

**[2109.88s] English:** called selling tokens, which means somebody will call the model to do some piece of work. I think  
**Translation:** 

**[2115.84s] English:** the other reason is for US companies, open AI is so GPU deprived. They're at the limits of the GPUs.  
**Translation:** 

**[2122.82s] English:** Whenever they make a release, they're always talking about like our GPUs are hurting.  
**Translation:** 

**[2125.56s] English:** And I think there's like, in one of these like GPT OSS release sessions, Sam Altman said like,  
**Translation:** Vocabulary: altman: 萨姆·阿尔特曼

**[2131.88s] English:** oh, we're releasing this because we can use your GPUs. We don't have to use our GPUs and open AI  
**Translation:** 

**[2137.46s] English:** can still get distribution out of this, which is another very real thing. It doesn't cost them  
**Translation:** 

**[2142.84s] English:** anything. And for the user, I think also, I mean, there are users who just use the model locally,  
**Translation:** 

**[2148.16s] English:** how they would use GPD, but also for companies, I think it's a huge unlock to have these models  
**Translation:** 

**[2152.60s] English:** because you can customize them, you can train them, you can,  
**Translation:** 

**[2155.56s] English:** add post training, add more data, like specialize them into, let's say,  
**Translation:** Vocabulary: specialize: 专门化

**[2160.00s] English:** law medical models whatever you have and the appeal you mentioned llama the appeal of the  
**Translation:** 

**[2165.30s] English:** open weight models from china is that the open weight models are also the licenses are even  
**Translation:** Vocabulary: llama: 羊驼

**[2170.80s] English:** friendlier i think they are just unrestricted open source licenses where if you use something  
**Translation:** 

**[2175.02s] English:** like llama or gemma there are some strings attached i think it's like a upper limit in  
**Translation:** Vocabulary: friendlier: 更友好; unrestricted: 无限制

**[2179.30s] English:** terms of how many users you have and then if you exceed i don't know so many million users you have  
**Translation:** 

**[2184.00s] English:** to report your finance situation to let's say meta or something like that and i think well  
**Translation:** 

**[2189.84s] English:** it is a free model but there are strings attached and people do like things where strings are not  
**Translation:** 

**[2196.06s] English:** attached so i think that's also one of the reasons besides performance why the open weight models  
**Translation:** 

**[2201.62s] English:** from china are so popular because you you can just use them there's no there's no catch in that sense  
**Translation:** 

**[2205.72s] English:** the ecosystem has gotten better on that front but mostly downstream of these new providers providing  
**Translation:** 

**[2211.04s] English:** such open licenses that was funny when you pulled up perplexity it said kimmy k2 thinking hosted in  
**Translation:** 

**[2215.28s] English:** the u.s which is just like an exact i've never seen this but it's an exact example of what we're  
**Translation:** Vocabulary: kimmy: 金米; perplexity: 困惑

**[2219.36s] English:** talking about  
**Translation:** 

**[2219.84s] English:** where people are sensitive to this like kimmy k2 thinking and kimmy k2 is a model that is very  
**Translation:** 

**[2224.60s] English:** popular people say that has very good like creative writing and also in doing some software  
**Translation:** 

**[2229.50s] English:** things there's just these little quirks that people pick up on with different models that  
**Translation:** Vocabulary: quirks: 怪癖

**[2233.18s] English:** they like uh what are some interesting ideas that some of these models have explored that you can  
**Translation:** 

**[2239.18s] English:** speak to like that particular interesting to you maybe you can go chronologically i mean there was  
**Translation:** Vocabulary: chronologically: 按时间顺序

**[2243.96s] English:** of course deep seek um deep seek r1 that came out in january if we just focus on 2025 however  
**Translation:** 

**[2249.86s] English:** was based on deep secretion three which came out the year um before in december 2020 there multiple  
**Translation:** 

**[2256.32s] English:** things on the architecture side what is fascinating is you can still i mean that's what i do with my  
**Translation:** 

**[2260.88s] English:** from scratch coding projects you can still start with gpd2 and you can add things to that model to  
**Translation:** 

**[2266.00s] English:** make it into this other model so it's all still kind of like the same lineage the same it is a  
**Translation:** 

**[2271.28s] English:** very close uh relationship between those but on top of my head deep seek what was uh  
**Translation:** Vocabulary: lineage: 血统

**[2276.32s] English:** unique there is the mixture of x and not i mean they were not inventing mixture of x uh with x  
**Translation:** 

**[2277.24s] English:** um the допek™ in addition to that there's also паль接 чего n даже varl 근데 auch das auch typeノ  
**Translation:** 

**[2278.98s] English:** inventing mixtrop experts.  
**Translation:** 

**[2280.00s] English:** We can maybe talk a bit more what mixture of experts means, but just to list these things first before we dive into detail, mixture of experts, but then they also had multi-head latent attention, which is a tweak to the attention mechanism, where this was, I would say, 2025, the main distinguishing factor between these open weight models, different tweaks to make inference or KV cache size.  
**Translation:** Vocabulary: cache: 缓存; distinguishing: 区分; inference: 推理; tweak: 调整; tweaks: 调整

**[2306.12s] English:** We can also define KV cache in a few moments, but to kind of make it more economical, to have long context, to shrink the KV cache size.  
**Translation:** 

**[2314.48s] English:** So what are tweaks that we can do?  
**Translation:** Vocabulary: economical: 经济的

**[2316.70s] English:** And most of them focused on the attention mechanism.  
**Translation:** 

**[2318.94s] English:** There is multi-head latent attention in DeepSeq.  
**Translation:** 

**[2321.98s] English:** There is group query attention, which is still very popular.  
**Translation:** 

**[2324.66s] English:** It's not invented by any of those models.  
**Translation:** 

**[2326.44s] English:** It goes back a few years, but that would be the other option.  
**Translation:** 

**[2330.10s] English:** Sliding window attention, I think, almost reuses it, if I remember correctly.  
**Translation:** Vocabulary: reuses: 重复使用

**[2334.08s] English:** So there are these different tweaks.  
**Translation:** 

**[2336.16s] English:** That make the models different.  
**Translation:** 

**[2338.46s] English:** Otherwise, I put them all together in an article once, where I just compared them.  
**Translation:** 

**[2344.10s] English:** They are very surprisingly similar.  
**Translation:** 

**[2345.54s] English:** It's just different numbers in terms of how many repetitions of the transformer block you have in the center.  
**Translation:** 

**[2351.78s] English:** And just little knobs that people tune.  
**Translation:** Vocabulary: knobs: 调节旋钮; repetitions: 重复次数

**[2354.88s] English:** But what's so nice about it is it works no matter what.  
**Translation:** 

**[2358.36s] English:** You can tweak things.  
**Translation:** 

**[2359.18s] English:** You can move the normalization layers around.  
**Translation:** 

**[2361.82s] English:** You get some performance gains.  
**Translation:** 

**[2366.12s] English:** But actually, what it does to the model, if you move something around, ablation studies doesn't make it better or worse.  
**Translation:** 

**[2372.72s] English:** But there are so many, let's say, ways you can implement a transformer and make it still work.  
**Translation:** Vocabulary: ablation: 切除试验

**[2376.38s] English:** Big ideas that are still prevalent is mixture of experts, multi-head latent attention, sliding window attention, group query attention.  
**Translation:** 

**[2384.50s] English:** And then at the end of the year, we saw a focus on making the attention mechanism scale linearly with inference token prediction.  
**Translation:** Vocabulary: prevalent: 普遍; token: 令牌

**[2392.50s] English:** So there were QEN3Next, for example.  
**Translation:** 

**[2395.52s] English:** Which?  
**Translation:** 

**[2396.00s] English:** Added a gated delta net.  
**Translation:** 

**[2397.38s] English:** It's kind of inspired by state.  
**Translation:** Vocabulary: delta: 三角洲

**[2400.00s] English:** space models where you have a fixed state that you keep updating but it makes essentially this  
**Translation:** 

**[2404.26s] English:** attention cheaper or it replaces attention with a cheaper operation and it may be is it useful to  
**Translation:** 

**[2410.12s] English:** step back and talk about transform architecture in general yeah so maybe we should start with the  
**Translation:** 

**[2416.10s] English:** gpt2 architecture the transformer that was derived from the attention is all you need paper  
**Translation:** 

**[2420.78s] English:** so the attention uh is all you need paper had a transformer architecture that had two parts an  
**Translation:** 

**[2426.32s] English:** encoder and a decoder and gpt went just focusing in on the decoder part it is essentially a still  
**Translation:** 

**[2434.08s] English:** a neural network um and it has this attention mechanism inside and you predict one token at  
**Translation:** 

**[2440.70s] English:** a time you pass it through an embedding layer there's the transformer block the transformer  
**Translation:** Vocabulary: embedding: 嵌入层; neural: 神经

**[2444.90s] English:** block has attention modules and a fully connected layer and there are some normalization layers in  
**Translation:** 

**[2450.12s] English:** between but it's essentially neural network layers with this attention mechanism so coming from gpt2  
**Translation:** 

**[2455.24s] English:** when we  
**Translation:** 

**[2456.02s] English:** you  
**Translation:** 

**[2456.30s] English:** move on to gpt oss there is for example the mixture of experts um layer it's not invented  
**Translation:** 

**[2461.68s] English:** by gpt oss it's a few years old um but it is essentially a tweak to make the model larger  
**Translation:** Vocabulary: tweak: 微调

**[2468.62s] English:** without consuming more compute in each forward pass so there is this a fully connected layer and  
**Translation:** 

**[2475.76s] English:** if listeners are familiar with um multi-layer perceptrons you can think of a mini multi-layer  
**Translation:** Vocabulary: listeners: 听众; perceptrons: 感知器

**[2481.64s] English:** perceptron a fully connected neural network layer inside the transformer and it's very  
**Translation:** 

**[2486.04s] English:** expensive and it's very expensive to use it but it's a very expensive layer and it's very expensive  
**Translation:** Vocabulary: perceptron: 感知器

**[2486.30s] English:** because it's fully connected if you have thousand inputs thousand outputs that's like a one million  
**Translation:** 

**[2490.68s] English:** connections and it's a very expensive part in this transformer and the idea is to kind of expand that  
**Translation:** 

**[2497.90s] English:** into multiple feed forward networks so instead of having one let's say you have 256 but it would  
**Translation:** 

**[2504.28s] English:** make it way more expensive because now you have 256 but you don't use all of them at the same time  
**Translation:** 

**[2508.80s] English:** so you now have a router that says okay based on this input token it would be useful to use  
**Translation:** 

**[2514.42s] English:** this fully connected network so you can use this as a router and you can use this as a network and  
**Translation:** Vocabulary: router: 路由器; token: 令牌

**[2516.30s] English:** in that context it's called an expert so a mixture of experts  
**Translation:** 

**[2520.00s] English:** means you have multiple experts and depending on what your input is let's say it's more math heavy  
**Translation:** 

**[2526.00s] English:** it would use different experts compared to let's say translating input text from english to spanish  
**Translation:** 

**[2531.60s] English:** it would maybe console different experts it's not quite clear i mean it's clear cut to say okay this  
**Translation:** 

**[2536.72s] English:** is only an expert for math and for spanish is a bit more fuzzy but the idea is essentially that  
**Translation:** 

**[2542.72s] English:** you pack more knowledge into the network but not all the knowledge is used all the time  
**Translation:** Vocabulary: fuzzy: 模糊的

**[2547.36s] English:** that would be very wasteful so you're kind of like during the token generation you're  
**Translation:** 

**[2551.84s] English:** more selective there's a router that selects which tokens should go to which expert it's  
**Translation:** Vocabulary: selective: 有选择; wasteful: 浪费

**[2557.52s] English:** more complexity it's harder to train there's a lot of you know that can go wrong like collapse  
**Translation:** 

**[2562.32s] English:** and everything so i think that's why almost three still uses uh dense i mean you have i  
**Translation:** Vocabulary: complexity: 复杂性

**[2566.80s] English:** think all the models with mixture of experts but dense models where dense means also also  
**Translation:** 

**[2572.24s] English:** it's jargon there's a distinction between dense and sparse so mixture of experts is  
**Translation:** Vocabulary: jargon: 专业术语; sparse: 稀疏的

**[2577.04s] English:** considered a good example of a good example of a good example of a good example of a good example  
**Translation:** 

**[2577.34s] English:** it's sparse because we have a lot of experts but only few of them are active so that's called sparse  
**Translation:** 

**[2582.30s] English:** and then dense would be the opposite where you only have like one fully connected module and  
**Translation:** 

**[2586.14s] English:** it's always you know utilized so maybe maybe this is a good place to also talk about kvcash but  
**Translation:** Vocabulary: module: 模块; utilized: 被利用

**[2591.26s] English:** actually before that even zooming out like fundamentally how many new ideas have been  
**Translation:** 

**[2597.90s] English:** implemented from from gpt2 to today like how different really are these architectures picture  
**Translation:** Vocabulary: fundamentally: 从根本上

**[2605.74s] English:** like the mixture of experts  
**Translation:** 

**[2607.34s] English:** um the attention mechanism in gpt oss that would be the group query attention mechanism so it's a  
**Translation:** 

**[2612.54s] English:** slight tweak from multi-head attention to group query attention so that we have two i think they  
**Translation:** 

**[2617.42s] English:** replaced a layer norm by rms norm but it's just like a different normalization layer and not a  
**Translation:** 

**[2622.86s] English:** big change it's just like a tweak um the non-linear activation function people familiar in  
**Translation:** 

**[2628.70s] English:** with deep new networks i mean it's the same as changing sigmoid with relu it's it's not changing  
**Translation:** Vocabulary: sigmoid: S形函数; tweak: 微调

**[2633.58s] English:** the network fundamentally it's just like a tweak like a little little tweak  
**Translation:** 

**[2637.34s] English:** um and that's about it i would say it's not really  
**Translation:** 

**[2640.00s] English:** fundamentally that different it's still the same same architecture so you can convert one from one  
**Translation:** 

**[2645.04s] English:** uh you can go from one into the other by just adding these these changes basically  
**Translation:** 

**[2649.54s] English:** it's fundamentally is still the same architecture yep so for example you mentioned my book earlier  
**Translation:** 

**[2654.42s] English:** that's a gpd2 model in the book because it's simple and it's very small um so 124 120 million  
**Translation:** 

**[2660.50s] English:** parameters approximately but in the bonus materials i do have almost three from scratch  
**Translation:** 

**[2665.20s] English:** gemma three from scratch and other types of from scratch models and i always started with my gpd2  
**Translation:** Vocabulary: gemma: 宝石样本

**[2669.72s] English:** model and just you know tweak the or edit different components and you get from one to  
**Translation:** 

**[2674.06s] English:** the other it's like it's kind of like a lineage in a sense yeah can you build up an intuition for  
**Translation:** Vocabulary: intuition: 直觉; lineage: 血缘

**[2679.26s] English:** people because sort of when you zoom out you look at it there's so much rapid advancement in the ai  
**Translation:** 

**[2685.14s] English:** world and at the same time fundamentally the architectures have not changed so where is all  
**Translation:** Vocabulary: advancement: 进步

**[2693.38s] English:** the turbulence the turmoil of the advancement happening where where's the gain  
**Translation:** 

**[2699.70s] English:** to be had so there are the different stages where you develop the network or train the network you  
**Translation:** Vocabulary: turmoil: 混乱

**[2705.30s] English:** have the pre-training now um back then they it was just pre-training with gpd2 now you have  
**Translation:** 

**[2710.60s] English:** pre-training mid-training and post-training um so i think right now we are in the post-training  
**Translation:** 

**[2716.74s] English:** focus stage i mean pre-training still gives you um advantages if you scale it up to better higher  
**Translation:** 

**[2722.72s] English:** quality data but then we have capability unlocks that were not there with gpd2 for example  
**Translation:** Vocabulary: capability: 能力

**[2729.70s] English:** chat gpt it is basically a gpd3 model and gpd3 is the same as gpd2 in terms of architecture  
**Translation:** 

**[2735.68s] English:** what was new was adding the supervised fine tuning and the reinforcement learning with  
**Translation:** Vocabulary: reinforcement: 强化学习; supervised: 监督细调

**[2741.20s] English:** human feedback so it's more on the algorithmic side rather than the architecture i would say  
**Translation:** 

**[2745.16s] English:** the systems also change a lot i think if you listen to nvidia's announcements they talk about  
**Translation:** Vocabulary: algorithmic: 算法相关的

**[2748.78s] English:** these things like you now do fp8 you can now do fp4 and what is happening is these labs are  
**Translation:** 

**[2754.62s] English:** figuring out how to utilize more compute to put it into one model which lets them train faster  
**Translation:** 

**[2759.24s] English:** and  
**Translation:** 

**[2759.70s] English:** that  
**Translation:** 

**[2760.00s] English:** less than put more data in and then you can find better configurations faster by doing this so you  
**Translation:** 

**[2765.26s] English:** can look at like the essentially the tokens per second per gpu is a metric that you look at when  
**Translation:** Vocabulary: configurations: 配置

**[2770.18s] English:** you're doing large-scale training and you could get you can go from like 10k to 13k by turning  
**Translation:** 

**[2775.48s] English:** on fp8 training which means they're using less memory per parameter in the model and by saving  
**Translation:** Vocabulary: parameter: 参数

**[2781.42s] English:** less information you do less communication you can train faster so all these like system things  
**Translation:** 

**[2786.12s] English:** underpin way faster experimentation on data and algorithms that is kind of like it's this it's  
**Translation:** Vocabulary: experimentation: 实验; underpin: 支撑

**[2793.38s] English:** this kind of loop that keeps going where it's kind of hard to describe when you look at the  
**Translation:** 

**[2798.94s] English:** architecture and they're exactly the same but the code base used to train these models is going to  
**Translation:** 

**[2803.00s] English:** be vastly different and you could probably like i don't the gpus are different but you probably  
**Translation:** 

**[2808.12s] English:** train gpt oss 20b way faster in wall clock time than gpt2 was trained at the time like you said  
**Translation:** 

**[2815.00s] English:** they had for example in the  
**Translation:** 

**[2815.98s] English:** mix  
**Translation:** 

**[2816.10s] English:** of experts this envy of fp4 optimization for example where you get more throughput but i do  
**Translation:** 

**[2821.84s] English:** think this is for the speed this is true but uh it doesn't give the model new capabilities in a  
**Translation:** Vocabulary: optimization: 优化; throughput: 吞吐量

**[2827.58s] English:** sense it's just how much can we make make the computation coarser without suffering in terms of  
**Translation:** 

**[2834.24s] English:** model performance degradation um but i do think i mean there are alternatives popping up to the  
**Translation:** Vocabulary: computation: 计算; degradation: 退化

**[2839.34s] English:** transformer there's text diffusion models uh completely different paradigm um and there's  
**Translation:** 

**[2844.48s] English:** also i mean though text diffusion  
**Translation:** Vocabulary: diffusion: 扩散; paradigm: 范式

**[2845.96s] English:** models might use transformer architectures but it's not an auto auto regressive um transformer  
**Translation:** 

**[2850.48s] English:** and also mamba models uh it's a state space model but they do have trade-offs and uh what's right is  
**Translation:** Vocabulary: mamba: 马姆巴; regressive: 倒退的

**[2856.90s] English:** there's nothing that has replaced the auto regressive transformer as state-of-the-art model  
**Translation:** 

**[2862.34s] English:** so like for state-of-the-art you would still do that go with that thing but there are no alternatives  
**Translation:** 

**[2867.56s] English:** for the cheaper and like alternatives that are kind of um making compromises but it's not just  
**Translation:** 

**[2873.92s] English:** one architecture anymore there are  
**Translation:** Vocabulary: compromises: 妥协

**[2875.96s] English:** little ones coming up but if we talk about the state of the art it's pretty much  
**Translation:** 

**[2880.00s] English:** Still, the transformer architecture, autoregressive, derived from GPT-2, essentially.  
**Translation:** Vocabulary: autoregressive: 自回归

**[2886.06s] English:** I guess the big question here is, we talked quite a bit here on the architecture behind the pre-training.  
**Translation:** 

**[2892.04s] English:** Are the scaling laws holding strong across pre-training, post-training, inference, contact size, data, synthetic data?  
**Translation:** Vocabulary: inference: 推理; synthetic: 合成

**[2900.70s] English:** I like to start with the technical definition of scaling law, which kind of informs all of this.  
**Translation:** 

**[2904.58s] English:** The scaling law is a power-law relationship between, you can think of the x-axis,  
**Translation:** 

**[2908.80s] English:** so kind of what you are scaling as a combination of compute and data, which are kind of similar.  
**Translation:** 

**[2914.86s] English:** And then the y-axis is like the held-out prediction accuracy over next tokens.  
**Translation:** 

**[2919.64s] English:** We talked about models being autoregressive.  
**Translation:** 

**[2921.38s] English:** It's like if you keep a set of text that the model has not seen, how accurate will it get when you will train?  
**Translation:** 

**[2927.72s] English:** And the idea of scaling laws came when people figured out that that was a very predictable relationship.  
**Translation:** 

**[2933.42s] English:** And I think that that technical term is continuing.  
**Translation:** Vocabulary: predictable: 可预测的

**[2938.14s] English:** And then the question...  
**Translation:** 

**[2938.80s] English:** And then the question is, what do users get out of it?  
**Translation:** 

**[2940.88s] English:** And then there are more types of scaling where OpenAI's O1 was famous for introducing inference time scaling.  
**Translation:** 

**[2947.46s] English:** And I think less famously for also showing that you can scale reinforcement learning training  
**Translation:** Vocabulary: reinforcement: 强化学习

**[2952.12s] English:** and get kind of this log x-axis and then a linear increase in performance on y-axis.  
**Translation:** 

**[2957.56s] English:** So there's kind of these three axes now where the traditional scaling laws are talked about for pre-training,  
**Translation:** 

**[2962.84s] English:** which is how big your model is and how big your data set is.  
**Translation:** 

**[2965.44s] English:** And then scaling reinforcement learning, which is like,  
**Translation:** 

**[2968.22s] English:** how long can you do this?  
**Translation:** 

**[2968.80s] English:** How long can you do this trial and error learning that we will talk about?  
**Translation:** 

**[2971.68s] English:** We'll define more of this.  
**Translation:** 

**[2972.76s] English:** And then this inference time compute, which is just letting the model generate more tokens on a specific problem.  
**Translation:** 

**[2977.56s] English:** So I'm kind of bullish where they're all really still working,  
**Translation:** 

**[2981.44s] English:** but the low-hanging fruit has mostly been taken,  
**Translation:** Vocabulary: bullish: 看涨

**[2983.64s] English:** especially in the last year on reinforcement learning with verifiable rewards,  
**Translation:** 

**[2988.18s] English:** which is this RLVR and then inference time scaling,  
**Translation:** Vocabulary: verifiable: 可验证的

**[2990.72s] English:** which is just why these models feel so different to use,  
**Translation:** 

**[2993.80s] English:** where previously you would get that first token immediately.  
**Translation:** Vocabulary: token: 令牌

**[2996.32s] English:** And now they'll go off for seconds,  
**Translation:** 

**[2998.80s] English:** minutes or even hours.  
**Translation:** 

**[3000.00s] English:** generating these hidden thoughts before giving you the first word of your answer and that's all  
**Translation:** 

**[3004.70s] English:** about this inference time scaling which is such a wonderful kind of step function in terms of how  
**Translation:** 

**[3010.58s] English:** the models change abilities they kind of enabled this tool use stuff and enabled this much better  
**Translation:** 

**[3015.02s] English:** software engineering that we were talking about and this is when we say enabled almost entirely  
**Translation:** 

**[3021.06s] English:** downstream of the fact that this reinforced learning with verifiable rewards training just  
**Translation:** 

**[3025.52s] English:** kind of let the models pick up these skills very easily so let the models learn so if you look at  
**Translation:** Vocabulary: reinforced: 加强

**[3031.94s] English:** the reasoning process when the models are generating a lot of tokens what it will be often  
**Translation:** 

**[3035.44s] English:** doing is it tries a tool it looks at what it gets back it tries another api it sees what it gets  
**Translation:** 

**[3040.46s] English:** back and if it solves the problem so the models when you're training them very quickly learn to  
**Translation:** 

**[3044.70s] English:** do this and then at the end of the day that gives this kind of general foundation where the model  
**Translation:** 

**[3050.40s] English:** can use cli commands very nicely in your repo and handle git for you and move things around  
**Translation:** 

**[3055.50s] English:** and organize things or search to find more information which if we're sitting in these  
**Translation:** 

**[3060.96s] English:** chairs a year ago it's something that we didn't really think of the models being doing so this  
**Translation:** 

**[3065.52s] English:** is just kind of something that has happened this year and has totally transformed how we think of  
**Translation:** 

**[3070.18s] English:** using ai which i think is very magical it's such an interesting evolution and just so unlock so  
**Translation:** 

**[3077.08s] English:** much value but it's like it's not clear what the next avenue will be in terms of unlocking stuff  
**Translation:** Vocabulary: unlocking: 解锁

**[3083.00s] English:** like this i think that there's there's we'll get to  
**Translation:** 

**[3085.50s] English:** continual learning later but there's a lot of buzz around certain areas of ai but no one knows when  
**Translation:** Vocabulary: continual: 连续的

**[3089.36s] English:** the next step function will really come so you you've actually said quite a lot of things there  
**Translation:** 

**[3094.78s] English:** and said profound things quickly it would be nice to unpack them a little bit you said you're  
**Translation:** Vocabulary: profound: 深奥

**[3101.14s] English:** bullish basically on every version of scaling so we just even start at the beginning pre-training  
**Translation:** 

**[3107.84s] English:** are we kind of implying that the low-hanging fruit on pre-training scaling has been picked  
**Translation:** Vocabulary: bullish: 乐观; implying: 暗示

**[3115.50s] English:** is is pre-training hit a plateau or is even pre-training still  
**Translation:** 

**[3120.00s] English:** you're bullish on pre-training has gotten extremely expensive i think to scale up pre-training  
**Translation:** 

**[3125.42s] English:** it's also implying that you're going to serve a very large model to the users so i think that  
**Translation:** 

**[3130.82s] English:** it's been loosely established the likes of gpt4 and similar models were around one trillion like  
**Translation:** Vocabulary: trillion: 万亿

**[3136.96s] English:** this order of trillion parameters at the biggest size there's a lot of rumors that they've actually  
**Translation:** 

**[3140.44s] English:** gotten smaller as training has gotten more efficient you want to make the model smaller  
**Translation:** 

**[3144.96s] English:** because then your costs of serving go down proportionally these models the cost of training  
**Translation:** 

**[3150.18s] English:** them is really low relative to the cost of serving them to hundreds of millions of users i think deep  
**Translation:** Vocabulary: proportionally: 按比例

**[3154.90s] English:** seek had this famous number of about five million dollars for pre-training at cloud market rates i  
**Translation:** 

**[3160.24s] English:** think almost three section 2.4 in the paper we just detailed how long we had the gpu clusters  
**Translation:** 

**[3166.28s] English:** sitting around for training which includes engineering issues multiple seeds and it was  
**Translation:** 

**[3171.90s] English:** like about two million dollars to rent the cluster to like deal with all the  
**Translation:** Vocabulary: cluster: 计算集群

**[3174.74s] English:** problems and problems and problems and problems and problems and problems and problems and  
**Translation:** 

**[3174.94s] English:** headaches of training a model so these models are pretty like a lot of people could get one to ten  
**Translation:** 

**[3181.70s] English:** million dollars to train a model but the recurring costs of serving millions of users is really  
**Translation:** 

**[3187.08s] English:** billions of dollars of compute i think that you can look at close like a thousand gpu rental you  
**Translation:** Vocabulary: recurring: 重复发生的

**[3192.18s] English:** can pay a hundred grand a day for and these companies could have millions of gpus like you  
**Translation:** 

**[3197.68s] English:** can look at how much these things cost to sit around so that's kind of a big thing and then  
**Translation:** 

**[3202.18s] English:** it's like if scaling is actually giving you a  
**Translation:** 

**[3204.72s] English:** better model like is it going to be financially worth it and i think it'll kind of slowly will  
**Translation:** Vocabulary: financially: 经济效益

**[3208.90s] English:** push it out as ai solves more compelling tasks so like the likes of cloud opus 4.5 making cloud code  
**Translation:** 

**[3214.74s] English:** just work for things i think i launched this project called like the atom project which is  
**Translation:** Vocabulary: compelling: 有吸引力的

**[3220.20s] English:** like american truly open models in july and that was like a true vibe coded website and like i have  
**Translation:** 

**[3227.14s] English:** a job um make plots and stuff and then i came back to refresh it in the last few weeks and it's like  
**Translation:** 

**[3232.60s] English:** cloud opus 4.5 versus whatever model and i'm like oh my god i'm like oh my god i'm like oh my god i'm  
**Translation:** 

**[3234.72s] English:** like oh my god it's a model at the time it was like just crushed all the issues that it had from  
**Translation:** 

**[3237.98s] English:** building in june and july and like  
**Translation:** 

**[3240.00s] English:** It might be a bigger model.  
**Translation:** 

**[3241.44s] English:** There's a lot of things that go into this, but that's like there's still progress coming.  
**Translation:** 

**[3244.58s] English:** So what you're speaking to is the nuance of the y-axis of the scaling laws, that the way it's experienced versus on a benchmark, the actual intelligence might be different.  
**Translation:** Vocabulary: benchmark: 参考标准; nuance: 细微差别

**[3254.08s] English:** But still, your intuition about pre-training, if you scale the size of compute, will the models get better?  
**Translation:** 

**[3261.86s] English:** Not whether it's financially viable, but just from the law aspect of it, do you think the models will get smarter?  
**Translation:** Vocabulary: intuition: 直觉

**[3268.04s] English:** Yeah. And I think that there's, and this sometimes comes off as like, almost like disillusioned from people, leadership, AI companies saying this, but they're like, it's held for 13 orders of magnitude of computers or something.  
**Translation:** 

**[3280.70s] English:** Like, why would it ever end?  
**Translation:** Vocabulary: disillusioned: 失望

**[3281.68s] English:** So I think fundamentally, it is pretty unlikely to stop.  
**Translation:** 

**[3285.68s] English:** It's just like, eventually, we're not even going to be able to test the bigger scales because of all the problems that come with more compute.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[3291.04s] English:** I think that there's a lot of talk on how 2026 is a year when very large Blackwell compute clusters.  
**Translation:** 

**[3298.04s] English:** It's like gigawatt scale facilities, hyperscalers are coming online.  
**Translation:** Vocabulary: clusters: 计算集群; gigawatt: 兆瓦; hyperscalers: 超大规模服务商

**[3302.26s] English:** And these were all contracts for power and data centers that were signed and sought out in like 22 and 2023.  
**Translation:** 

**[3311.10s] English:** So before or right after ChatGPT.  
**Translation:** 

**[3313.86s] English:** So it took this two to three year lead time to build these bigger clusters to train the models.  
**Translation:** 

**[3318.12s] English:** Well, there's obviously immense interest in building even more data centers than that.  
**Translation:** Vocabulary: immense: 巨大

**[3321.98s] English:** So that is like kind of the crux that people are saying is like these new clusters are coming.  
**Translation:** 

**[3326.04s] English:** The labs are going to have more compute for training.  
**Translation:** 

**[3328.16s] English:** They're going to utilize this, but it's not a given.  
**Translation:** 

**[3331.08s] English:** And it's like, I've seen so much progress that I expect it.  
**Translation:** 

**[3334.26s] English:** And I expect a little bit bigger models.  
**Translation:** 

**[3335.94s] English:** And I expect, I would say it's more like we will see a $2,000 subscription this year.  
**Translation:** Vocabulary: subscription: 订购服务

**[3342.16s] English:** We've seen $200 subscriptions.  
**Translation:** 

**[3343.74s] English:** It's like that can 10x again.  
**Translation:** 

**[3345.36s] English:** And these are the kind of things that could come.  
**Translation:** 

**[3347.64s] English:** And they're all downstream of this like bit bigger model that offers just a little bit more cutting edge.  
**Translation:** 

**[3353.26s] English:** So, you know, it's reported that XAI is going to hit that one gigawatt scale.  
**Translation:** 

**[3358.04s] English:** Early 26.  
**Translation:** 

**[3360.00s] English:** and full 2 gigawatt by year-end,  
**Translation:** 

**[3364.10s] English:** how do you think they'll utilize that  
**Translation:** 

**[3365.88s] English:** in the context of scaling laws?  
**Translation:** 

**[3369.24s] English:** Is a lot of that inference?  
**Translation:** Vocabulary: inference: 推断

**[3370.88s] English:** Is a lot of that training?  
**Translation:** 

**[3372.80s] English:** It ends up being all of the above.  
**Translation:** 

**[3375.72s] English:** So I think that all of your decisions  
**Translation:** 

**[3377.92s] English:** when you're training a model  
**Translation:** 

**[3379.02s] English:** come back to pre-training.  
**Translation:** 

**[3380.64s] English:** So if you're going to scale RL on a model,  
**Translation:** 

**[3382.92s] English:** you still need to decide on your architecture  
**Translation:** 

**[3384.70s] English:** that enables this.  
**Translation:** 

**[3385.74s] English:** We were talking about other architectures  
**Translation:** 

**[3388.02s] English:** than using different types of attention  
**Translation:** 

**[3389.86s] English:** and we're also talking about  
**Translation:** 

**[3390.84s] English:** mixture of experts models.  
**Translation:** 

**[3392.10s] English:** The sparse nature of MOE models  
**Translation:** 

**[3393.62s] English:** makes it much more efficient to do generation,  
**Translation:** Vocabulary: sparse: 稀疏

**[3398.36s] English:** which becomes a big part of post-training.  
**Translation:** 

**[3400.82s] English:** And it's like,  
**Translation:** 

**[3401.28s] English:** you need to have your architecture ready  
**Translation:** 

**[3403.04s] English:** so that you can actually scale up this compute.  
**Translation:** 

**[3405.70s] English:** I still think most of the compute  
**Translation:** 

**[3407.36s] English:** is going in at pre-training  
**Translation:** 

**[3409.44s] English:** because you can still make a model better.  
**Translation:** 

**[3411.40s] English:** You still want to go and revisit this.  
**Translation:** 

**[3413.26s] English:** You still want the best-based model that you can.  
**Translation:** 

**[3415.80s] English:** And in a few years, that'll saturate  
**Translation:** 

**[3417.32s] English:** and the RL compute will just go longer.  
**Translation:** 

**[3419.86s] English:** Is there people who disagree with you  
**Translation:** 

**[3421.46s] English:** that say, basically, pre-training is dead?  
**Translation:** 

**[3425.88s] English:** It's all about scaling inference,  
**Translation:** 

**[3428.76s] English:** scaling post-training, scaling context,  
**Translation:** 

**[3431.02s] English:** continual learning, scaling data, synthetic data.  
**Translation:** Vocabulary: continual: 持续的; synthetic: 合成的

**[3434.96s] English:** People vibe that way and describe it in that way,  
**Translation:** 

**[3437.38s] English:** but I think it's not the practice that is happening.  
**Translation:** 

**[3439.82s] English:** It's just the general vibe of people saying,  
**Translation:** 

**[3441.74s] English:** this thing is dead.  
**Translation:** 

**[3442.32s] English:** The excitement is elsewhere.  
**Translation:** 

**[3443.32s] English:** So the low-hanging fruit in RL is elsewhere.  
**Translation:** 

**[3445.52s] English:** For example, we released our model in November  
**Translation:** 

**[3447.90s] English:** for every company has deadlines.  
**Translation:** Vocabulary: deadlines: 截止日期

**[3449.74s] English:** It's like, oh, we're going to do this.  
**Translation:** 

**[3449.84s] English:** Our deadline was November 20th.  
**Translation:** 

**[3451.46s] English:** And for that, our RL run was five days,  
**Translation:** 

**[3453.86s] English:** which compared to 2024 is a very long time  
**Translation:** 

**[3457.04s] English:** to just be doing post-training at a model  
**Translation:** 

**[3458.92s] English:** of 30 billion parameters.  
**Translation:** 

**[3460.36s] English:** It's not a big model.  
**Translation:** 

**[3461.48s] English:** And then in December, we had another release,  
**Translation:** 

**[3463.18s] English:** which was just, we let the RL run go  
**Translation:** 

**[3465.22s] English:** for another three and a half weeks  
**Translation:** 

**[3466.86s] English:** and the model got notably better, so we release it.  
**Translation:** 

**[3469.44s] English:** And that's a big amount of time to just allocate  
**Translation:** 

**[3472.20s] English:** to something that is going to be your peak for the year.  
**Translation:** 

**[3476.36s] English:** So it's like, there's these types of decisions  
**Translation:** 

**[3479.08s] English:** that happen.  
**Translation:** 

**[3479.72s] English:** And when they're,  
**Translation:** 

**[3480.00s] English:** training a model where they just like can't they can't leave it forever you have to keep you have  
**Translation:** 

**[3484.82s] English:** to keep pulling in the improvements you have from your researchers so that's like you redo pre-training  
**Translation:** 

**[3489.22s] English:** you'll do this post-training for a month but then you need to give it to your users you need to do  
**Translation:** 

**[3494.16s] English:** safety testing so it's kind of just like i think there's a lot in place that reinforces this cycle  
**Translation:** Vocabulary: reinforces: 加强

**[3499.42s] English:** of just keep updating the models there's things to improve you get a new compute cluster that lets  
**Translation:** 

**[3504.64s] English:** you do something maybe more stably or faster it's like you hear a lot about blackwell having  
**Translation:** Vocabulary: cluster: 计算集群; stably: 稳定地

**[3509.88s] English:** rollout issues where at ai2 most of the models were pre-training around like one to two thousand  
**Translation:** 

**[3515.18s] English:** gpus but when you're pre-training on 10 000 or 100 000 gpus you hit very different failures so  
**Translation:** Vocabulary: rollout: 发布

**[3520.36s] English:** gpus are known to break in weird ways and doing 100 000 gpu run is like you're pretty much guaranteed  
**Translation:** 

**[3525.46s] English:** to always have at least one gpu that is down and you need to have your training code handle that  
**Translation:** 

**[3529.34s] English:** redundancy which is just a very different problem whereas like what we're doing like i'm playing  
**Translation:** 

**[3533.40s] English:** with post-training on djx spark or you have your book it's like or people learning ml it's like  
**Translation:** 

**[3538.24s] English:** what they're battling to train  
**Translation:** 

**[3539.78s] English:** you  
**Translation:** 

**[3539.88s] English:** biggest models is just like mass distributed scale and it's a very different but that's  
**Translation:** 

**[3547.48s] English:** somewhat different than like are these like that's a systems problem in order to enable the scaling  
**Translation:** 

**[3553.08s] English:** laws especially at pre-training you need all these gpus at once when we shift to reinforcement  
**Translation:** 

**[3558.28s] English:** learning it actually lends itself to heterogeneous compute because you have many copies of the model  
**Translation:** Vocabulary: heterogeneous: 异构计算; reinforcement: 强化学习

**[3563.64s] English:** and to do a primer for a language model reinforcement learning what you're doing is  
**Translation:** 

**[3569.84s] English:** you have two sets of gpus one is you can call it the actor and one you call the learner the learner  
**Translation:** 

**[3576.04s] English:** is where your actual reinforcement learning updates are going to do these are traditionally  
**Translation:** 

**[3579.66s] English:** policy gradient algorithms proximal policy optimization ppo and group relative policy  
**Translation:** Vocabulary: gradient: 梯度; optimization: 优化; proximal: 近似的

**[3586.42s] English:** optimization grpo are the two popular classes and on the other side you're going to have actors  
**Translation:** 

**[3591.98s] English:** which are generating  
**Translation:** 

**[3593.50s] English:** you're going to have actors which are generating  
**Translation:** 

**[3593.62s] English:** you're going to have actors which are generating  
**Translation:** 

**[3593.64s] English:** completions and these completions are the things that you're going to grade  
**Translation:** 

**[3596.78s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** Vocabulary: completions: 完成任务; optimizing: 优化奖励

**[3599.42s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3605.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3607.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3609.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3611.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3613.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3615.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3617.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3619.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3621.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3623.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3625.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3627.40s] English:** so reinforcement learning is all about optimizing reward  
**Translation:** 

**[3600.00s] English:** And in practice, what you can do is that you can have a lot of different actors in different parts of the world doing different types of problems.  
**Translation:** 

**[3607.32s] English:** And then you send it back to this highly networked compute cluster to do this actual learning where you take the gradients and you need to have a tightly meshed network where you can do different types of parallelism and spread out your model for efficient training.  
**Translation:** 

**[3621.44s] English:** So there's just like a lot of every different type of training and serving has these considerations you need to scale.  
**Translation:** Vocabulary: gradients: 梯度; networked: 网络化

**[3627.84s] English:** Like we talked about pre-training, we talked about RL, and then inference time scaling is like, how do you serve a model that's thinking for an hour to 100 million users?  
**Translation:** 

**[3635.68s] English:** I'm like, I don't really know about that, but I know that's a hard problem.  
**Translation:** Vocabulary: inference: 推理

**[3639.26s] English:** And in order to give people this intelligence, there's all the systems problems and we need more compute and you need more stable compute to do it.  
**Translation:** 

**[3646.34s] English:** But you're bullish on all of these kinds of scaling is what I'm hearing on the inference, on the reasoning, even on the pre-training.  
**Translation:** Vocabulary: bullish: 乐观

**[3654.02s] English:** Yeah, so that's a big can of worms here.  
**Translation:** 

**[3656.54s] English:** But so that's basically two.  
**Translation:** 

**[3657.98s] English:** The knobs are the training and the inference scaling where you can get gains.  
**Translation:** 

**[3662.84s] English:** And so in a world where we had, let's say, infinite compute resources, you want to do all of them.  
**Translation:** Vocabulary: knobs: 调节旋钮

**[3667.86s] English:** So you have training, you have inference scaling, and training is like a hierarchy.  
**Translation:** 

**[3672.60s] English:** It's pre-training, mid-training, post-training.  
**Translation:** Vocabulary: hierarchy: 等级体系

**[3674.84s] English:** Changing the model size, more training data, making training a bigger model gives you more knowledge in the model.  
**Translation:** 

**[3680.36s] English:** The model, let's say, has a better, it's like a better base model back in the day, or still we call it foundation model.  
**Translation:** 

**[3687.10s] English:** And it unknocks.  
**Translation:** 

**[3687.98s] English:** But you don't, let's say, have the model be able to solve your most complex tasks during pre-training or after pre-training.  
**Translation:** 

**[3696.56s] English:** You still have these other unlock phases where you have mid-training or non-context, for example, post-training with LRVR that unlocks capabilities that the model has in terms of just knowledge in the pre-training.  
**Translation:** 

**[3707.74s] English:** And I think, sure, if you do more pre-training, you get a better base model that you can unlock later.  
**Translation:** 

**[3713.34s] English:** But like Nathan said, it just becomes too expensive.  
**Translation:** 

**[3715.34s] English:** So we don't have infinite compute.  
**Translation:** Vocabulary: nathan: 纳森

**[3716.72s] English:** So you have to decide, do I want to spend that compute more on...  
**Translation:** 

**[3720.00s] English:** making the model larger but you know it's like a trade-off it's it's like an ideal world you want  
**Translation:** 

**[3724.62s] English:** to do all of them and i think in that sense scaling is still pretty much alive you would  
**Translation:** 

**[3728.76s] English:** still get a better model but like we saw with gpd 4.5 it's just not worth it i mean it's like  
**Translation:** 

**[3733.22s] English:** because you can let's say you can unlock more performance with other techniques at that current  
**Translation:** 

**[3738.48s] English:** moment especially um if you look at inference scaling that's one of the biggest gains this  
**Translation:** 

**[3743.48s] English:** year with 01 um where it took a smaller model further than pre-training a larger model like  
**Translation:** 

**[3750.20s] English:** gpd 4.5 so it's like i wouldn't say pre-training scaling is dead it's just like there are other  
**Translation:** 

**[3755.00s] English:** more attractive ways to scale right now at the moment but at some point you know you will still  
**Translation:** 

**[3760.10s] English:** want to make some progress on the pre-training the thing is also to consider um where you where  
**Translation:** 

**[3766.10s] English:** do you want to spend your money if you spend it more on the pre-training it's like a fixed cost  
**Translation:** 

**[3770.02s] English:** you train the model and then it has this capability forever  
**Translation:** Vocabulary: capability: 能力

**[3773.02s] English:** you  
**Translation:** 

**[3773.46s] English:** can always use it and so forth with inference scaling you don't spend money during training  
**Translation:** Vocabulary: inference: 推理

**[3778.98s] English:** you spend money later per query and then it's also like the math how long is my model going  
**Translation:** 

**[3783.70s] English:** to be on the market if i replace it in half a year maybe it's not worth spending five million  
**Translation:** 

**[3789.28s] English:** ten million hundred million dollars on the training it longer maybe it's just i will just  
**Translation:** 

**[3794.16s] English:** do more inference scaling and get the performance from there it maybe cost me two million in terms  
**Translation:** 

**[3799.24s] English:** of user queries it becomes a question of how many users you have and then doing the math  
**Translation:** 

**[3803.46s] English:** scaling and i think that's also where it's interesting where ggpt is in a position i think  
**Translation:** 

**[3807.14s] English:** they have a lot of users where they need to go a bit cheaper where they have that gpd5 model that  
**Translation:** 

**[3811.54s] English:** is a bit smaller other companies that have i say if your customers have other uh other trade-offs  
**Translation:** 

**[3818.18s] English:** for example there was also the math olympiad or some of these these math uh problems where  
**Translation:** 

**[3824.58s] English:** chgbt or maybe they had a proprietary model and i'm pretty sure it's just like a model it has  
**Translation:** Vocabulary: olympiad: 数学奥林匹克; proprietary: 专有模型

**[3829.22s] English:** been maybe fine-tuned a little bit more but most of it was during inference scaling to  
**Translation:** 

**[3833.46s] English:** achieve this peak performance in certain tasks where you don't need that all the time and but  
**Translation:** 

**[3837.94s] English:** yeah long story short i do think  
**Translation:** 

**[3840.48s] English:** All of these pre-training, mid-training, post-training,  
**Translation:** 

**[3843.76s] English:** inference scaling, they are all still things you want to do.  
**Translation:** 

**[3846.58s] English:** It's just finding, at the moment in this year,  
**Translation:** 

**[3849.18s] English:** it's finding the right ratio that gives you the best bang for the buck, basically.  
**Translation:** 

**[3852.96s] English:** I think this might be a good place to define pre-training,  
**Translation:** 

**[3855.32s] English:** mid-training, and post-training.  
**Translation:** 

**[3858.04s] English:** So pre-training is the classic training,  
**Translation:** 

**[3860.16s] English:** one next token prediction at a time.  
**Translation:** 

**[3861.86s] English:** You have a big corpus of data.  
**Translation:** Vocabulary: token: 标记

**[3863.52s] English:** And Nathan also has very interesting insights there because of OMO3.  
**Translation:** 

**[3867.34s] English:** It's a big portion of the paper focuses on the right data mix.  
**Translation:** 

**[3871.26s] English:** So pre-training is essentially just across entropy loss training  
**Translation:** 

**[3875.06s] English:** on next token prediction on a vast corpus of internet data,  
**Translation:** Vocabulary: entropy: 混乱程度

**[3879.36s] English:** books, papers, and so forth.  
**Translation:** 

**[3881.16s] English:** It has changed a little bit over the years in the sense  
**Translation:** 

**[3883.88s] English:** people used to throw in everything they can.  
**Translation:** 

**[3886.80s] English:** Now, it's not just raw data.  
**Translation:** 

**[3888.76s] English:** It's also synthetic data where people, let's say, rephrase certain things.  
**Translation:** 

**[3894.46s] English:** So synthetic data doesn't necessarily mean purely  
**Translation:** Vocabulary: rephrase: 改述; synthetic: 合成

**[3897.34s] English:** AI made up data.  
**Translation:** 

**[3899.02s] English:** It's also taking something from an article, Wikipedia article,  
**Translation:** 

**[3902.50s] English:** and then rephrasing it as a Q&A question or summarizing it,  
**Translation:** 

**[3908.74s] English:** rewording it, and making better data that way.  
**Translation:** Vocabulary: rephrasing: 改述; summarizing: 总结

**[3912.22s] English:** Because I think of it also like with humans.  
**Translation:** 

**[3915.06s] English:** If someone, let's say, reads the book compared to a messy,  
**Translation:** 

**[3918.22s] English:** I don't know, no offense, but like Reddit post or something like that.  
**Translation:** 

**[3920.88s] English:** I do think you learn.  
**Translation:** 

**[3923.14s] English:** No offense, but I think...  
**Translation:** 

**[3925.26s] English:** There's going to be a post about this, Sebastian.  
**Translation:** 

**[3927.94s] English:** Some Reddit data is very coveted and excellent for training.  
**Translation:** 

**[3931.00s] English:** You just have to filter it.  
**Translation:** Vocabulary: coveted: 备受追捧

**[3932.38s] English:** Yeah.  
**Translation:** 

**[3932.80s] English:** I think that's the idea.  
**Translation:** 

**[3934.48s] English:** I think it's like if someone took that and rephrases that  
**Translation:** 

**[3939.14s] English:** in a, let's say, more concise and structured way,  
**Translation:** Vocabulary: concise: 简洁; rephrases: 改写

**[3942.42s] English:** I think it's higher quality data that gets the LLM maybe the same.  
**Translation:** 

**[3947.38s] English:** You get the same LLM out of it at the end,  
**Translation:** 

**[3949.32s] English:** but it gets there faster.  
**Translation:** 

**[3950.44s] English:** It trains faster because, let's say,  
**Translation:** 

**[3952.84s] English:** if the grammar and the punctuation is correct,  
**Translation:** 

**[3955.32s] English:** it already learns the correct way,  
**Translation:** 

**[3956.98s] English:** versus getting information from a messy way and then...  
**Translation:** 

**[3960.00s] English:** learning later how to correct that and stuff like that so i think that is how pre-training evolved  
**Translation:** 

**[3964.78s] English:** and how um how still while why scaling still works is that it's not about just the amount of data  
**Translation:** 

**[3972.72s] English:** it's also the tricks to make that data better for you in a sense and mid-training is i mean it used  
**Translation:** 

**[3980.08s] English:** to be called a pre-training it's i think it's called mid-training because it was awkward to  
**Translation:** 

**[3983.82s] English:** have pre-training and post-training but nothing in the middle right it sounds a bit weird you  
**Translation:** 

**[3987.06s] English:** have pre-training and post-training but what's the actual training so the mid-training is usually  
**Translation:** 

**[3991.24s] English:** similar to pre-training but you know it's a bit more i would say specialized in pre-training it's  
**Translation:** 

**[3996.78s] English:** the same algorithm but what you do is you focus for example on long contact like it's one example  
**Translation:** 

**[4002.24s] English:** you have long context documents the reason you don't do that during just pure pre-training is  
**Translation:** Vocabulary: algorithm: 算法

**[4006.88s] English:** because you don't have that many long context documents you have a specific phase and one  
**Translation:** 

**[4011.56s] English:** problem of lms is also still it's a neural network it has the problem of catastrophic forgetting so  
**Translation:** Vocabulary: catastrophic: 灾难性的; neural: 神经的

**[4016.64s] English:** you teach  
**Translation:** 

**[4017.04s] English:** it something it forgets other things and you want to it's not 100 forgetting but you know it's like  
**Translation:** 

**[4022.68s] English:** no free lunch you can't it's also the same with humans if you ask me some math i learned 10 years  
**Translation:** 

**[4027.22s] English:** ago i don't know i would have to look at it again nathan was actually saying that he's consuming so  
**Translation:** Vocabulary: nathan: 纳森

**[4031.40s] English:** much content that there's a catastrophic forgetting issue yeah i'm like trying to learn so much about  
**Translation:** 

**[4036.04s] English:** ai i was like i was learning about pre-training parallelism i'm like i lost something and i don't  
**Translation:** 

**[4040.80s] English:** know what it was i don't want to anthropomorphize lms but it's i think the same kind of in that  
**Translation:** 

**[4045.88s] English:** sense how humans learn  
**Translation:** Vocabulary: anthropomorphize: 赋予人类特征

**[4047.04s] English:** i mean the quantity is not always better because yeah you it's like being selective and i and the  
**Translation:** 

**[4052.68s] English:** mid-training is being selective in terms of quality content at the end so the last thing  
**Translation:** Vocabulary: selective: 挑揀

**[4057.20s] English:** the lms seen is the quality stuff and then post-training is all the fine-tuning supervised  
**Translation:** 

**[4062.82s] English:** fine-tuning dpo reinforcement learning with verifiable rewards with human feedback and so  
**Translation:** Vocabulary: reinforcement: 强化学习; supervised: 监督学习; verifiable: 可验证的

**[4070.92s] English:** forth so the refinement stages and it's also interesting it's like the cost thing right i  
**Translation:** 

**[4075.04s] English:** mean it's like pre-training you spend a lot of money  
**Translation:** Vocabulary: refinement: 精炼阶段

**[4077.04s] English:** on that right now rl a bit less rl  
**Translation:** 

**[4080.00s] English:** you don't really i would say teach it knowledge it's more like unlocking the knowledge it's more  
**Translation:** Vocabulary: unlocking: 解锁知识

**[4084.34s] English:** like a skill learning like how to solve problems with the knowledge that it has from pre-training  
**Translation:** 

**[4088.26s] English:** there are actually three papers this year or last year 2025 on rl for pre-training but i i mean i  
**Translation:** 

**[4095.76s] English:** don't think anyone does that in production toy examples for now examples right but to generalize  
**Translation:** 

**[4100.46s] English:** rl post-training is more like the skill unlock where pre-training is like soaking up the knowledge  
**Translation:** Vocabulary: generalize: 泛化

**[4105.96s] English:** essentially a few things that could be helpful for people a lot of people get like think of  
**Translation:** 

**[4112.38s] English:** synthetic data as being bad for training the models you mentioned like the deep sea got almost  
**Translation:** 

**[4116.54s] English:** ocr which is optical character recognition paper a lot of labs did ai2 had one that had multiple and  
**Translation:** 

**[4125.06s] English:** the reason that each of these labs has these is because there's vast amounts of pdfs and other  
**Translation:** 

**[4130.08s] English:** digital documents on the web that are in formats that aren't encoded with text easily so you use  
**Translation:** 

**[4134.84s] English:** these almost cr these  
**Translation:** Vocabulary: encoded: 编码

**[4135.96s] English:** or deep seek ocr and we called our almost cr to extract what can be trillions of tokens of  
**Translation:** 

**[4141.42s] English:** candidate data for pre-training and pre-training data set sizes on the order of trillions is  
**Translation:** Vocabulary: trillions: 万亿

**[4148.70s] English:** measured in trillions of tokens smaller models from researchers can be something like five to  
**Translation:** 

**[4153.78s] English:** ten trillion um quen is documented going up to like 50 trillion and there's rumors that these  
**Translation:** Vocabulary: trillion: 万亿

**[4159.10s] English:** closed labs can go to like 100 trillion tokens and just getting this potential data to put in  
**Translation:** 

**[4163.38s] English:** i think they they have a very big funnel and then the data  
**Translation:** Vocabulary: funnel: 筛选渠道

**[4165.94s] English:** you actually train the model on is a small percentage of this like the  
**Translation:** 

**[4168.64s] English:** this character recognition data would be described as synthetic data for pre-training  
**Translation:** 

**[4173.56s] English:** in a lab and then there's also the things like chat gpt now gives wonderful answers and you can  
**Translation:** 

**[4179.34s] English:** train on those best answers and that's synthetic data it's very different than like early chat gpt  
**Translation:** 

**[4184.56s] English:** lots of hallucinations data when people became grounded in synthetic data one interesting  
**Translation:** 

**[4189.10s] English:** question is if i recall correctly almost three was trained with less data than specifically some  
**Translation:** Vocabulary: hallucinations: 幻觉; synthetic: 合成的

**[4194.56s] English:** other open weight models maybe even more than that i think that's a good question i think that's a good  
**Translation:** 

**[4195.78s] English:** answer i think that's a good answer i think that's a good answer i think that's a good answer  
**Translation:** 

**[4195.94s] English:** even almost two but you still got better performance and that might be one of the examples  
**Translation:** 

**[4200.00s] English:** all the data help it's mostly down to data quality i think if we had more compute we would train  
**Translation:** 

**[4204.18s] English:** for longer i think we'd ultimately see that as a like just like something we would want to do and  
**Translation:** 

**[4209.54s] English:** especially with big models you need to have more compute because we talk about having more  
**Translation:** 

**[4213.80s] English:** parameters we talk about knowledge and essentially there's a ratio where big models can absorb  
**Translation:** 

**[4217.40s] English:** more from data and then you're gonna you get more benefit out of this it's it's like one of these  
**Translation:** 

**[4222.30s] English:** any logarithmic graph in your mind is like a small model will level off sooner if you're measuring  
**Translation:** 

**[4227.60s] English:** tons of tokens and bigger and bigger models need more but mostly is we aren't training that big of  
**Translation:** Vocabulary: logarithmic: 对数的

**[4233.18s] English:** models right now ai2 and getting the highest quality data we can is the natural starting  
**Translation:** 

**[4238.04s] English:** point is there something to be said uh about the topic of data quality is there some low-hanging  
**Translation:** 

**[4243.18s] English:** fruit there still where the quality could be improved it's like turning the crank so i think  
**Translation:** 

**[4247.76s] English:** historically in the open there's been like a canonical best pre-training data set that has  
**Translation:** Vocabulary: canonical: 典范; crank: 把手; historically: 历史上

**[4253.02s] English:** moved around between who has the most recent one or the best recent effort like ai2  
**Translation:** 

**[4257.54s] English:** is the most recent one or the best recent effort like ai2 is the most recent one or the best recent  
**Translation:** 

**[4257.58s] English:** up  
**Translation:** 

**[4262.62s] English:** project which has been kind of like a which is it stands for data comp language model there's  
**Translation:** 

**[4267.82s] English:** been data comp for other machine learning projects and they have had a very strong data set and a lot  
**Translation:** 

**[4273.90s] English:** of it is the internet is becoming fairly closed off so we have common crawl which i think is  
**Translation:** 

**[4279.10s] English:** hundreds of trillions of tokens and you filter it and it looks like being a lot of scientific  
**Translation:** 

**[4283.42s] English:** work where you're training classifiers and making decisions based on how do you  
**Translation:** Vocabulary: trillions: 万亿

**[4287.52s] English:** you prune down this this data set into the highest quality stuff and the stuff that suits your tasks  
**Translation:** 

**[4292.66s] English:** so previously language models were tested a lot more on like knowledge and just kind of  
**Translation:** Vocabulary: prune: 修剪

**[4297.86s] English:** conversational things but now they're expected to do math and code so to train a reasoning model  
**Translation:** 

**[4302.18s] English:** you need to remix your whole data set and there's a lot of actually wonderful scientific methods  
**Translation:** Vocabulary: conversational: 对话相关

**[4306.56s] English:** here where you can you can like take your gigantic data set you sample a lot of really tiny things  
**Translation:** 

**[4311.46s] English:** from different sources so you say you have github stack exchange reddit wikipedia you can sample  
**Translation:** Vocabulary: gigantic: 巨大的

**[4317.00s] English:** small things from them and you train small models on each of these mix  
**Translation:** 

**[4320.00s] English:** and measure their performance on your evaluations.  
**Translation:** Vocabulary: evaluations: 评估

**[4322.20s] English:** And you can just do like basic linear regression  
**Translation:** 

**[4323.98s] English:** and it's like, here's your optimal dataset.  
**Translation:** Vocabulary: dataset: 数据集; optimal: 最佳的; regression: 回归分析

**[4326.00s] English:** But if your evaluations change,  
**Translation:** 

**[4327.48s] English:** your dataset changes a lot.  
**Translation:** 

**[4328.66s] English:** So a lot of OMO3 was new sources for reasoning  
**Translation:** 

**[4331.64s] English:** to be better at math and code.  
**Translation:** 

**[4333.76s] English:** And then you do this mixing procedure  
**Translation:** 

**[4335.34s] English:** and it gives you the answer.  
**Translation:** 

**[4336.46s] English:** And I think that's a lot of that's happened  
**Translation:** 

**[4337.86s] English:** at labs this year.  
**Translation:** 

**[4339.20s] English:** It's like, there's new hot things,  
**Translation:** 

**[4340.50s] English:** whether it's like coding environments  
**Translation:** Vocabulary: environments: 环境

**[4342.24s] English:** or web navigation,  
**Translation:** 

**[4343.30s] English:** and you just need to bring in new data.  
**Translation:** Vocabulary: navigation: 导航

**[4344.62s] English:** You need to change your whole pre-training  
**Translation:** 

**[4345.98s] English:** so that your post-training can work better  
**Translation:** 

**[4347.64s] English:** and stuff like this.  
**Translation:** 

**[4348.88s] English:** So that's like the constant re-evolution  
**Translation:** 

**[4351.68s] English:** and the re-determining of what they care about  
**Translation:** 

**[4353.76s] English:** for their models.  
**Translation:** 

**[4355.36s] English:** Are there fun anecdotes of what sources of data  
**Translation:** 

**[4359.10s] English:** are particularly high quality that we wouldn't expect?  
**Translation:** Vocabulary: anecdotes: 趣闻轶事

**[4361.46s] English:** You mentioned Reddit sometimes can be a source.  
**Translation:** 

**[4365.04s] English:** Reddit was very useful.  
**Translation:** 

**[4367.22s] English:** I think that like PDFs is definitely one.  
**Translation:** 

**[4371.40s] English:** Especially Archive.  
**Translation:** 

**[4372.52s] English:** Yeah, so like AI2 has run Semantic Scholar  
**Translation:** 

**[4374.96s] English:** for a long time,  
**Translation:** Vocabulary: semantic: 语义的

**[4375.86s] English:** which is a, like you can say,  
**Translation:** 

**[4378.88s] English:** is a competitor to Google Scholar  
**Translation:** 

**[4380.48s] English:** with a lot more features.  
**Translation:** 

**[4381.86s] English:** And to do this,  
**Translation:** 

**[4382.92s] English:** AI2 has found and scraped a lot of PDFs  
**Translation:** 

**[4385.24s] English:** for openly accessible papers  
**Translation:** Vocabulary: scraped: 抓取

**[4386.68s] English:** that might not be like behind the closed paid garden  
**Translation:** 

**[4390.24s] English:** of a certain publisher.  
**Translation:** 

**[4391.60s] English:** So like truly open scientific PDFs.  
**Translation:** 

**[4394.30s] English:** And if you like, you sit on all of these  
**Translation:** 

**[4395.56s] English:** and you process it  
**Translation:** 

**[4396.38s] English:** and you can get value out of it.  
**Translation:** 

**[4398.14s] English:** And I think that like a lot of that style of work  
**Translation:** 

**[4401.74s] English:** has been done by the Frontier Labs much earlier.  
**Translation:** Vocabulary: frontier: 前沿

**[4404.18s] English:** And it's just like,  
**Translation:** 

**[4405.08s] English:** you need to have a pretty skilled researcher  
**Translation:** 

**[4407.72s] English:** that understands,  
**Translation:** 

**[4408.88s] English:** how things change models  
**Translation:** 

**[4410.26s] English:** and they bring it in and they clean it.  
**Translation:** 

**[4411.96s] English:** And that's a lot of labor that,  
**Translation:** 

**[4414.10s] English:** like I think of a lot of Frontier Labs  
**Translation:** 

**[4415.66s] English:** when they scale researchers a lot more,  
**Translation:** 

**[4417.10s] English:** it goes into data.  
**Translation:** 

**[4418.76s] English:** You have people like,  
**Translation:** 

**[4419.56s] English:** if you want to be,  
**Translation:** 

**[4420.06s] English:** if you join a Frontier Lab and you want to have impact,  
**Translation:** 

**[4421.82s] English:** the best way to do it is just make,  
**Translation:** 

**[4423.56s] English:** find new data that's better.  
**Translation:** 

**[4425.44s] English:** And then like the fancy,  
**Translation:** 

**[4426.46s] English:** glamorous algorithmic things,  
**Translation:** Vocabulary: algorithmic: 算法的; glamorous: 华丽的

**[4428.04s] English:** like figuring out how to make a one  
**Translation:** 

**[4430.24s] English:** is like the sexiest thought of a scientist.  
**Translation:** 

**[4432.72s] English:** It's like, oh, I figured out to scale RL.  
**Translation:** 

**[4434.92s] English:** And there's a group that did that.  
**Translation:** 

**[4435.92s] English:** But I think most of the contributions is like,  
**Translation:** 

**[4437.96s] English:** on the data side.  
**Translation:** 

**[4438.36s] English:** I'm going to make,  
**Translation:** 

**[4438.88s] English:** the data better or,  
**Translation:** 

**[4440.00s] English:** going to make the infrastructure better so that everybody in my team can run experiments five  
**Translation:** 

**[4443.88s] English:** percent faster at the same time i think it's also one of the closest guarded secrets what your  
**Translation:** 

**[4448.06s] English:** training data is for legal reasons and so there's also i think a lot of work that goes into hiding  
**Translation:** 

**[4452.48s] English:** what your trading data was essentially like trying the model to not give away the sources because  
**Translation:** 

**[4458.40s] English:** of legal reasons the other thing to be complete is that some people are trying to train on only  
**Translation:** 

**[4462.74s] English:** licensed data where common crawl is a scrape of like the whole internet so um if i i host multiple  
**Translation:** Vocabulary: scrape: 抓取

**[4469.22s] English:** websites i'm happy to have them train language models but i'm not explicitly licensing what  
**Translation:** 

**[4475.18s] English:** governs it and therefore this like the common crawl is largely unlicensed which means that  
**Translation:** Vocabulary: unlicensed: 未授权

**[4479.60s] English:** your consent really hasn't been provided for how to use the data there's another idea where you can  
**Translation:** 

**[4484.08s] English:** train language models only on data that has been licensed explicitly so that the kind of governing  
**Translation:** Vocabulary: explicitly: 明确地

**[4489.24s] English:** contract is provided and i'm not sure if apparatus is the copyright thing or the license thing i know  
**Translation:** 

**[4494.10s] English:** that the reason that they did it was for an eu compliance thing where they wanted to make sure  
**Translation:** 

**[4498.06s] English:** that their model  
**Translation:** 

**[4499.22s] English:** um fit one of those checks and also on that note also for example there's also the distinction  
**Translation:** 

**[4505.54s] English:** between um the licensing so some people like you said they just purchased the license let's say they  
**Translation:** 

**[4512.52s] English:** buy a book online let's say an amazon kindle book or let's say a money book or something and then  
**Translation:** Vocabulary: kindle: 电子书

**[4517.26s] English:** use that in the training data and that is like the gray zone because you paid for the content  
**Translation:** 

**[4520.42s] English:** and you might want to train it but then there are also restrictions where even that shouldn't be  
**Translation:** 

**[4525.66s] English:** allowed and so that that is like where where it gets a bit fuzzy and  
**Translation:** 

**[4529.22s] English:** yeah i think that is right now it's still a hot topic and also big companies like openai they  
**Translation:** Vocabulary: fuzzy: 模糊

**[4534.88s] English:** approached private companies for their proprietary data and private companies they become more and  
**Translation:** 

**[4540.74s] English:** more let's say uh protective of their data because they know okay this is going to be my mode in in a  
**Translation:** Vocabulary: proprietary: 专有技术

**[4547.02s] English:** few years and i do think um that's like the interesting question where if lms become more  
**Translation:** 

**[4554.02s] English:** commoditized and i think a lot of people learn about lms so there will be a lot more people able  
**Translation:** Vocabulary: commoditized: 商品化

**[4558.08s] English:** to train lms of course there will be a lot more people able to train lms so there will be a lot more  
**Translation:** 

**[4559.22s] English:** people able to train lms so there will be a lot more people able to train lms so there will be a lot  
**Translation:** 

**[4560.00s] English:** But if you think of big industries like pharmaceutical industries, law, finance industries, I do think they at some point will hire people from other frontier labs to build their in-house models on their proprietary data, which will be then again another unlock with pre-training that is currently not there.  
**Translation:** 

**[4577.80s] English:** Because even if you wanted to, you can't get that data.  
**Translation:** Vocabulary: frontier: 前沿; pharmaceutical: 制药

**[4580.82s] English:** You can't get access to clinical trials most of the time in these types of things.  
**Translation:** 

**[4584.48s] English:** So I do think scaling in that sense might be still pretty much alive.  
**Translation:** 

**[4588.14s] English:** If you also look in domain specific applications, because we are still right now in this year, just looking at general purpose LLMs on ChurchPD, Anthropic and so forth.  
**Translation:** 

**[4597.78s] English:** They are just general purpose.  
**Translation:** 

**[4598.98s] English:** They're not even, I think, scratching the surface of what an LLM can do if it is really specifically trained and designed for a specific task.  
**Translation:** 

**[4606.50s] English:** I think on the data thing, this is one of the things where this happened in 2025 and we totally forget it, is Anthropic lost in court and was owed $1.5 billion to authors.  
**Translation:** Vocabulary: scratching: 浅尝辄止

**[4616.16s] English:** Anthropic, I think, bought thousands of books.  
**Translation:** 

**[4618.16s] English:** And scanned them and was cleared legally for that because they bought the books and that is kind of going through the system.  
**Translation:** 

**[4625.36s] English:** And then the other side, they also torrented some books.  
**Translation:** 

**[4627.30s] English:** And I think this torrenting was the path where the court said that they were then culpable to pay this billions of dollars to authors, which is just like such a mind-boggling lawsuit that kind of just came and went.  
**Translation:** Vocabulary: culpable: 应负责任; torrented: 通过BT下载; torrenting: 正在通过BT下载

**[4637.88s] English:** Like that is so much money from the VC ecosystem.  
**Translation:** 

**[4641.78s] English:** These are court cases that will define the future of human civilization because it's clearly that data drives a lot of this.  
**Translation:** 

**[4647.80s] English:** And there's this very complicated human tension of, I mean, you can empathize.  
**Translation:** 

**[4651.96s] English:** You're both authors.  
**Translation:** Vocabulary: empathize: 感同身受

**[4653.72s] English:** Yeah.  
**Translation:** 

**[4654.36s] English:** There's some degree to which, I mean, you put your heart and soul and your sweat and tears into the writing that you do.  
**Translation:** 

**[4662.76s] English:** It feels a little bit like theft for somebody to train your data without giving you credit.  
**Translation:** 

**[4668.60s] English:** And like Nathan said, also two layers to it.  
**Translation:** 

**[4671.52s] English:** Someone might buy the book and then train on it, which could be argued fair or not fair.  
**Translation:** 

**[4676.46s] English:** But then the tree straight.  
**Translation:** 

**[4677.80s] English:** There are companies who.  
**Translation:** 

**[4680.00s] English:** use pirated books where it's not even compensating the author is that that is i think where people  
**Translation:** Vocabulary: compensating: 赔偿

**[4684.64s] English:** got a bit angry about it specifically there has to be some kind of competition scheme this is  
**Translation:** 

**[4688.80s] English:** like moving towards towards something like spotify streaming did originally for music  
**Translation:** 

**[4694.64s] English:** you know what does that competition look like you have to define those kinds of models you have to  
**Translation:** 

**[4698.24s] English:** think through all of that uh one other thing i think people are generally curious about i'd  
**Translation:** 

**[4703.04s] English:** love to get your thoughts as lms are used more and more if you look at even archive but github  
**Translation:** 

**[4708.96s] English:** more and more of the data is generated by lms what do you do in that kind of world  
**Translation:** 

**[4716.14s] English:** is how big of a problem is that largest problems infrastructure and systems but from an ai point  
**Translation:** 

**[4722.84s] English:** of view it's kind of inevitable so it's basically lm generated data that's curated by humans  
**Translation:** 

**[4728.34s] English:** essentially right yes and i think that a lot of open source contributors are legitimately burning  
**Translation:** 

**[4732.94s] English:** out if you have a popular open source repo somebody's like oh i want to do open source ai  
**Translation:** Vocabulary: contributors: 贡献者; legitimately: 确实

**[4737.66s] English:** it's good for my career  
**Translation:** 

**[4738.96s] English:** they just vibe code something and they throw it into the you might get more of this than i do  
**Translation:** 

**[4745.26s] English:** so i have a case study here i have a repository called ml extent uh that i developed as a student  
**Translation:** 

**[4753.20s] English:** around 15 years 10 years ago and it is a reasonably popular library still for certain  
**Translation:** Vocabulary: reasonably: 相当

**[4758.70s] English:** algorithms i think especially like frequent data mining stuff and there was recently i think two  
**Translation:** 

**[4764.54s] English:** or three people who submitted a lot of prs in a very short amount of time i do think that  
**Translation:** 

**[4768.96s] English:** lms have been involved in submitting these prs me as the maintainer there are two things first i'm  
**Translation:** 

**[4774.20s] English:** a bit overwhelmed like i don't have time to read through it because especially it's an older library  
**Translation:** Vocabulary: maintainer: 维护者; submitting: 提交

**[4778.76s] English:** that is not a priority for me at the same time i kind of also appreciate it because i think  
**Translation:** 

**[4783.50s] English:** something people forget is it's not just using the lm there's still a human you have a human  
**Translation:** 

**[4788.24s] English:** layer that verifies something and and that is in a sense also how data is labeled right so that's  
**Translation:** 

**[4793.26s] English:** like um one of the most expensive things is get getting labeled data for rl back and human  
**Translation:** Vocabulary: verifies: 验证

**[4798.96s] English:** back phases  
**Translation:** 

**[4800.00s] English:** And this is kind of like that where it goes through phases  
**Translation:** 

**[4803.50s] English:** and then you get actually higher quality data out of it.  
**Translation:** 

**[4806.38s] English:** So I don't mind it in a sense.  
**Translation:** 

**[4808.10s] English:** It can feel overwhelming, but I do think there is also value in it.  
**Translation:** 

**[4811.46s] English:** It feels like there's a fundamental difference between raw LLM-generated data  
**Translation:** 

**[4815.64s] English:** and LLM-generated data with human in the loop that does some kind of verification,  
**Translation:** 

**[4820.84s] English:** even if that verification is a small percent of the lines of code.  
**Translation:** Vocabulary: verification: 验证

**[4825.64s] English:** I think this goes with anything where people think also sometimes,  
**Translation:** 

**[4831.44s] English:** oh, I can just use an LLM to learn about XYZ, which is true.  
**Translation:** 

**[4835.08s] English:** You can, but there might be a person who is an expert  
**Translation:** 

**[4838.00s] English:** who might have used an LLM to write specific code.  
**Translation:** 

**[4841.42s] English:** There is kind of like this human work that went into it to make it nice  
**Translation:** 

**[4845.34s] English:** and throwing out the not-so-nice part to make it kind of like pre-digested for you,  
**Translation:** 

**[4849.78s] English:** and that saves you time.  
**Translation:** 

**[4850.62s] English:** And I think that's the value add where you have someone  
**Translation:** 

**[4854.94s] English:** who's...  
**Translation:** 

**[4855.64s] English:** filtering things or even using the LLMs correctly.  
**Translation:** 

**[4858.90s] English:** I think this is still labor that you get for free.  
**Translation:** 

**[4861.92s] English:** If you, for example, read an article, let's say a Substake article,  
**Translation:** 

**[4865.60s] English:** I could maybe ask an LLM to give me opinions on that,  
**Translation:** 

**[4868.48s] English:** but I wouldn't even maybe know what to ask.  
**Translation:** 

**[4870.88s] English:** I think there is still value in reading that article compared to me going to the LLM  
**Translation:** 

**[4875.22s] English:** because you are the expert.  
**Translation:** 

**[4876.92s] English:** You select what knowledge is actually spot-on, should be included,  
**Translation:** 

**[4880.90s] English:** and you give me this executive summary.  
**Translation:** 

**[4885.22s] English:** And this is...  
**Translation:** 

**[4885.62s] English:** kind of a huge value add because now I don't have to waste three,  
**Translation:** 

**[4889.70s] English:** five hours to go through this myself,  
**Translation:** 

**[4892.34s] English:** maybe get some incorrect information and so on.  
**Translation:** 

**[4894.90s] English:** And so I think that's also where the future still is for writers,  
**Translation:** 

**[4898.76s] English:** even though there are LLMs that expert can kind of like save your time.  
**Translation:** 

**[4903.88s] English:** It's kind of fascinating to actually watch,  
**Translation:** 

**[4906.00s] English:** and I'm sure you guys do this,  
**Translation:** 

**[4907.46s] English:** but for me to look at the difference between the summary and the original content,  
**Translation:** 

**[4914.66s] English:** even if it's a page-long summary,  
**Translation:** 

**[4915.46s] English:** if it's a page-long summary of a page-long content,  
**Translation:** 

**[4918.18s] English:** it's interesting to see...  
**Translation:** 

**[4920.00s] English:** How the summary, LMB summary, takes the edge off.  
**Translation:** 

**[4923.54s] English:** Like, what is the signal it removes from the thing?  
**Translation:** 

**[4927.24s] English:** The voice is what I talk about a lot.  
**Translation:** 

**[4929.66s] English:** Voice.  
**Translation:** 

**[4930.16s] English:** Well, voice, I would love to hear what you mean by voice.  
**Translation:** 

**[4932.48s] English:** That's really powerful.  
**Translation:** 

**[4933.24s] English:** But sometimes there's, like, literally insights.  
**Translation:** 

**[4935.68s] English:** Like, in removing an insight, you're actually fundamentally changing the meaning of the thing.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[4940.38s] English:** So I'm continuously disappointed how bad LLMs are at really getting to the core insights, which is what a great summary does.  
**Translation:** 

**[4951.52s] English:** Even if you go, and I have these extensive, extremely elaborate prompts where I'm, like, really trying to dig for the insights, and it's still not quite there, which, I mean, that's a whole deep philosophical question about what is human knowledge and wisdom and what does it mean to be insightful and so on.  
**Translation:** Vocabulary: elaborate: 详细; philosophical: 哲学的

**[4969.94s] English:** But when you talk about the voice, what do you mean?  
**Translation:** 

**[4971.92s] English:** So when I write, I think a lot of what I'm trying to do is take what you think as a researcher, which is very raw, which a researcher is trying to encapsulate an idea at the frontier of their understanding.  
**Translation:** Vocabulary: encapsulate: 概括; frontier: 前沿

**[4984.38s] English:** And they're trying to put what is a feeling into words.  
**Translation:** 

**[4988.04s] English:** And I think that my writing, I tried to do this as the writing, which makes it come across as raw, but also high information in a way that it's, like, some people will get it and some won't.  
**Translation:** 

**[4997.12s] English:** And that's kind of the nature of research.  
**Translation:** 

**[4998.72s] English:** And I think this is something.  
**Translation:** 

**[4999.94s] English:** But language models don't do well.  
**Translation:** 

**[5001.86s] English:** Particularly, they're all trained with this reinforcement learning from human feedback, which is designed to take feedback from a lot of people and, in a way, average how the model behaves from this.  
**Translation:** Vocabulary: reinforcement: 强化

**[5010.62s] English:** And I think that there's, it's going to be hard for a model to be very incisive when there's that sort of filter in it.  
**Translation:** 

**[5017.78s] English:** And I think this is kind of a wonderful fundamental problem for researchers in RLHF is, like, this provides so much utility in making the models better.  
**Translation:** Vocabulary: incisive: 尖锐

**[5027.10s] English:** But also the problem formulation.  
**Translation:** 

**[5029.94s] English:** It's kind of, like, there's this knot in it that you can't get past.  
**Translation:** 

**[5033.50s] English:** So that's what I think of is, like, these language models don't have this prior and their deep expression that they're trying to get at.  
**Translation:** 

**[5040.00s] English:** i don't think it's impossible to do i think there's stories of models that really shock people  
**Translation:** 

**[5044.66s] English:** like i think of like i would love to have tried bing sydney and does like does that have more  
**Translation:** 

**[5050.44s] English:** voice because it would so often go off the rails on people and what is historically obviously a  
**Translation:** Vocabulary: historically: 历史上

**[5055.48s] English:** scary way like telling a reporter to leave his wife is a crazy model to potentially put in general  
**Translation:** 

**[5060.26s] English:** general adoption but that's kind of like a trade-off like is this rlhf process like in some  
**Translation:** 

**[5066.40s] English:** ways adding limitations that's a terrifying place to be as one of these frontier labs and  
**Translation:** 

**[5072.00s] English:** and companies because millions of people are using them there was a lot of backlash last year with  
**Translation:** Vocabulary: backlash: 强烈反对; terrifying: 令人恐惧的

**[5077.68s] English:** the gpt 4.0 getting removed and i personally never used the model but i've talked to people  
**Translation:** 

**[5083.20s] English:** at open ai where they're to the point where they get emails from users that might be detecting  
**Translation:** Vocabulary: detecting: 检测

**[5088.60s] English:** subtle differences in the deployments in the middle of the night and they email them and  
**Translation:** 

**[5092.24s] English:** they're like my friend is different and they like find these people employees emails  
**Translation:** Vocabulary: deployments: 部署方式

**[5096.38s] English:** and send them things because they're so attached to this set what is a set of model weights and  
**Translation:** 

**[5103.22s] English:** a configuration that is deployed to the users we see this with tiktok you open it i don't use  
**Translation:** Vocabulary: configuration: 配置; deployed: 部署

**[5108.34s] English:** tiktok supposedly in like five minutes the algorithm gets you it's like it's locked in  
**Translation:** 

**[5112.54s] English:** and i don't like those are language models doing recommendations like i think there are ways that  
**Translation:** Vocabulary: algorithm: 算法

**[5117.10s] English:** you can do this with the language model within like five minutes of chatting with it the model  
**Translation:** 

**[5120.82s] English:** just gets you and that is something that people aren't really ready for like i think like  
**Translation:** 

**[5125.82s] English:** kids  
**Translation:** 

**[5126.38s] English:** like don't give that to kids like don't give that to kids at least until we know what's happening  
**Translation:** 

**[5130.14s] English:** there's also going to be this mechanism what's going to happen with these llms is they're used  
**Translation:** 

**[5134.44s] English:** more and more unfortunately the nature of the human condition is such that people commit suicide  
**Translation:** 

**[5140.30s] English:** and so what journalists would do is they will report extensively on the people who commit  
**Translation:** 

**[5144.86s] English:** suicide and they would very likely link it to the llms because they have that data about the  
**Translation:** 

**[5150.42s] English:** conversations if you're really struggling in your life if you're depressed if you're thinking about  
**Translation:** 

**[5156.28s] English:** suicide you're going to probably talk to llms about it  
**Translation:** 

**[5160.00s] English:** So what journalists will do is they will say, well, the suicide was committed because of the LLM.  
**Translation:** 

**[5164.94s] English:** And that's going to lead to the companies, because of legal issues and so on, more and more and more taking the edge off of the LLM.  
**Translation:** 

**[5173.34s] English:** So it's going to be as generic as possible.  
**Translation:** 

**[5176.04s] English:** It's so difficult to operate in this space because, of course, you don't want an LLM to cause harm to humans at that level.  
**Translation:** 

**[5183.42s] English:** But also, this is also the nature of the human experience, is to have a rich conversation, a fulfilling conversation, one that challenges you from which you grow.  
**Translation:** 

**[5194.20s] English:** You need that edge.  
**Translation:** Vocabulary: fulfilling: 充实的

**[5196.32s] English:** And that's something extremely difficult for AI researchers on the RLHF front to actually have to solve, because you're actually dealing with the human condition.  
**Translation:** 

**[5206.72s] English:** A lot of researchers at these companies are so well-motivated.  
**Translation:** 

**[5210.10s] English:** And there's definitely the likes of Anthropic and OpenAI are cultural.  
**Translation:** 

**[5213.42s] English:** They really so want to do good through this for the world.  
**Translation:** 

**[5218.22s] English:** And it's such a, I'm like, I don't want to work on this.  
**Translation:** 

**[5221.58s] English:** Because on the one hand, a lot of people see AI as a health ally, as somebody they can talk to about their health confidentially.  
**Translation:** Vocabulary: confidentially: 保密地

**[5227.88s] English:** But then it bleeds all the way into this, talking about mental health and things, where it's heartbreaking that this will be the thing where somebody goes over the edge, but other people might be saved.  
**Translation:** 

**[5242.06s] English:** And I'm like, I don't.  
**Translation:** Vocabulary: heartbreaking: 令人心碎

**[5242.98s] English:** There's.  
**Translation:** 

**[5243.42s] English:** Things that as a researcher training models, it's like, I don't want to train image generation models and release them openly because I don't want to enable somebody to have a tool on their laptop that can harm other people.  
**Translation:** 

**[5254.16s] English:** Like, I don't have the infrastructure at my company to do that safely, but it's like, like, there's a lot of areas like this where it's just, it needs people that will approach it with the complexity and just kind of conviction of like, it's just such a hard problem.  
**Translation:** 

**[5267.86s] English:** But also we, as a society, as users of these technologies need to make sure that we're having the complicated conversations.  
**Translation:** Vocabulary: complexity: 复杂性

**[5272.22s] English:** Yeah.  
**Translation:** 

**[5272.34s] English:** Yeah.  
**Translation:** 

**[5272.58s] English:** Yeah.  
**Translation:** 

**[5272.82s] English:** Yeah.  
**Translation:** 

**[5272.88s] English:** Yeah.  
**Translation:** 

**[5273.12s] English:** Yeah.  
**Translation:** 

**[5273.14s] English:** Yeah.  
**Translation:** 

**[5273.24s] English:** Yeah.  
**Translation:** 

**[5273.42s] English:** Fascination about Empress is just fearmongering big tech is, is causing harm to humans or stealing your data, all that.  
**Translation:** 

**[5280.00s] English:** of stuff. It's more complicated than that. And you're right. There's a very large number of  
**Translation:** Vocabulary: empress: 皇后; fascination: 着迷; fearmongering: 散布恐慌

**[5284.10s] English:** people inside these companies, many of which you know, many of which I know, that deeply care about  
**Translation:** 

**[5289.02s] English:** helping people. They are considering the full human experience of people from across the world,  
**Translation:** 

**[5293.84s] English:** not just Silicon Valley, people across the United States, people across the world, what that means,  
**Translation:** 

**[5298.32s] English:** what their needs are. It's really difficult to design this one system that is able to help all  
**Translation:** 

**[5303.62s] English:** these different kinds of people across the different age groups, cultures, mental states,  
**Translation:** 

**[5308.72s] English:** mental conditions, all that kind of stuff.  
**Translation:** 

**[5311.38s] English:** I wish that the timing of AI was different with the relationship of big tech to the average person.  
**Translation:** 

**[5316.88s] English:** So like big tech's reputation was so low. And with how AI is so expensive, it's like inevitably  
**Translation:** Vocabulary: inevitably: 必然地

**[5321.98s] English:** going to be a big tech thing where it takes so many resources. And people say the US is  
**Translation:** 

**[5326.38s] English:** quote unquote betting the economy on AI with this build out. And it's like to have these  
**Translation:** Vocabulary: unquote: 引用结束

**[5330.84s] English:** be intertwined at the same time, it just makes for such a hard communication environment.  
**Translation:** 

**[5335.64s] English:** It would be good for me to go talk to more people.  
**Translation:** Vocabulary: intertwined: 错综复杂

**[5338.24s] English:** In the world that hate big tech and see AI as a continuation of this.  
**Translation:** 

**[5342.90s] English:** And one of the things you actually recommend, one of the antidotes that you talk about  
**Translation:** Vocabulary: antidotes: 解毒剂; continuation: 延续

**[5347.78s] English:** is to find agency in this whole system, as opposed to sort of sitting back in a powerless  
**Translation:** 

**[5355.18s] English:** way and consuming the AI slop as it quickly, rapidly takes over the internet.  
**Translation:** 

**[5360.66s] English:** More fine agency by using it to build stuff, build apps, build. So one that actually has a lot of  
**Translation:** 

**[5368.24s] English:** value. It helps you build intuition, but two, it's empowering because you can understand how it  
**Translation:** Vocabulary: empowering: 赋予力量; intuition: 直觉

**[5372.86s] English:** works, what the weaknesses are and allows you, it gives your voice power to say like, this is  
**Translation:** 

**[5377.64s] English:** fucked up. This is bad. This is bad use of the technology. And this is good use of technology.  
**Translation:** 

**[5382.02s] English:** And you're more plugged into the system then. So you can understand it better and you can  
**Translation:** 

**[5386.52s] English:** steer it better. I think it's a good point. You brought up agency instead of ignoring it and  
**Translation:** 

**[5392.06s] English:** saying, okay, I'm not going to use it. I think it's probably long-term healthier to say, okay,  
**Translation:** 

**[5397.14s] English:** it's out there. I can't do it. I can't do it. I can't do it. I can't do it. I can't do it. I can't  
**Translation:** 

**[5398.24s] English:** do it. I can't do it. I can't put it back. You know, like internet.  
**Translation:** 

**[5400.00s] English:** computers back then when they came out how do i make best use of it and how does it help me to  
**Translation:** 

**[5405.16s] English:** up level myself the one thing i worry here though is like if you just fully use it for something you  
**Translation:** 

**[5410.40s] English:** love to do the the thing you love to do is not no longer there and that could potentially i feel  
**Translation:** 

**[5415.46s] English:** likely to burn out for example if i use an lm to do all my coding for me now there's no coding i'm  
**Translation:** 

**[5421.60s] English:** just managing something that is coding for me two years let's say later if i just do that eight  
**Translation:** 

**[5427.14s] English:** hours a day i have something code for me do i feel fulfilled still like is this like yeah i mean  
**Translation:** 

**[5434.34s] English:** is this like hurting me in terms of being excited about my job excited about what i'm doing am i  
**Translation:** Vocabulary: fulfilled: 满足

**[5440.96s] English:** still proud to build something so there's a on that topic of enjoyment it's quite interesting  
**Translation:** 

**[5446.18s] English:** we should just throw this in there that there's this recent survey of about 791 professional  
**Translation:** 

**[5451.76s] English:** developers professional meaning 10 plus years of experience that's a long time  
**Translation:** 

**[5456.48s] English:** you  
**Translation:** 

**[5457.14s] English:** yeah that's a junior developer uh yeah in this day and age uh so the the results here on many  
**Translation:** 

**[5465.06s] English:** fronts are uh surprising so they break it down by junior and senior developers but i mean it just  
**Translation:** 

**[5472.36s] English:** shows that both junior senior developers use ai generated code in code they ship so this is not  
**Translation:** 

**[5482.46s] English:** just for fun sort of intermediate kind of learning things this is code they ship  
**Translation:** 

**[5487.14s] English:** and so it's 25 percent like most of them use around 50 or more and what's interesting is for  
**Translation:** 

**[5494.90s] English:** the category of over 50 of your code that you ship as ai generated senior developers are much more  
**Translation:** 

**[5501.72s] English:** likely to do so but you don't want ai to take away the thing you love yeah i think it speaks to my  
**Translation:** 

**[5507.56s] English:** experience these particular results i'm about to say so together about 80 of people find it either  
**Translation:** 

**[5512.96s] English:** somewhat more enjoyable or significantly more enjoyable to use and i think that's a really good  
**Translation:** 

**[5517.14s] English:** way to use ai as part of the work i think  
**Translation:** 

**[5520.00s] English:** depends on the task um from my personal usage for example i have a website where i sometimes tweak  
**Translation:** 

**[5527.36s] English:** things on the website i personally don't enjoy this so in that sense if the ai can help me to  
**Translation:** Vocabulary: tweak: 调整

**[5533.20s] English:** implement something on my website i'm all here for it it's great but then at the same time when  
**Translation:** 

**[5538.96s] English:** i solve a complex problem well if there's a bug and i hunt this bug and i find the bug it's the  
**Translation:** 

**[5545.28s] English:** best feeling in the world it's like you get so much joy like oh it's like you feel like great  
**Translation:** 

**[5550.32s] English:** but now if you don't even think about thinking about the bug you just go directly to the lm  
**Translation:** 

**[5555.36s] English:** well you never have this kind of feeling right but then there could be the middle ground where  
**Translation:** 

**[5560.40s] English:** well you try yourself you can't find it you use the llm and then you don't get frustrated because  
**Translation:** 

**[5565.04s] English:** it helps you and you move on to something that you enjoy and so i think looking at these statistics i  
**Translation:** 

**[5569.60s] English:** think also the difference is what is not factored in it's averaging over all the different scenarios  
**Translation:** Vocabulary: factored: 考虑进去; scenarios: 情景

**[5575.28s] English:** where we don't so we don't know if it's for the core task or if it's for something mundane that  
**Translation:** 

**[5580.72s] English:** people would not have enjoyed otherwise so in a sense ai is really great for doing mundane things  
**Translation:** Vocabulary: mundane: 平凡事务

**[5586.48s] English:** that um take a lot of work so for example my wife the other day uh she has like a podcast for like  
**Translation:** 

**[5592.80s] English:** book like book discussions book club and she was like transferring show notes from spotify to  
**Translation:** Vocabulary: transferring: 转移

**[5598.48s] English:** youtube and then the links somehow broke and she had in some episodes because they discussed so  
**Translation:** 

**[5603.84s] English:** many books like 100 links  
**Translation:** 

**[5605.28s] English:** or something and it would have been really painful to go in there and fix each link manually and so  
**Translation:** 

**[5610.80s] English:** i suggested hey let's try chat gpt we copied the text into chat gpt and it fixed them and  
**Translation:** 

**[5616.56s] English:** instead of two hours going from link to link fixing that you know it made that type of work  
**Translation:** 

**[5621.68s] English:** much more seamless there was no frustration fixed i think everyone has a use case where  
**Translation:** Vocabulary: seamless: 天衣无缝

**[5626.32s] English:** ai is useful for something like that that would be really boring really mundane  
**Translation:** 

**[5630.88s] English:** i for me personally since we're talking about coding  
**Translation:** 

**[5634.08s] English:** uh and you mentioned  
**Translation:** 

**[5635.28s] English:** debugging uh what a lot of the source of the enjoyment for me  
**Translation:** 

**[5640.00s] English:** more on the cursor side than the clog code side is the i have a friend i have a co what's that  
**Translation:** 

**[5646.80s] English:** called a pair programmer like it's less lonely you you made debugging sound like this great  
**Translation:** Vocabulary: programmer: 搭档程序员

**[5653.96s] English:** joy no i would say i would say debugging is like a drink of water after you've been going through  
**Translation:** 

**[5660.48s] English:** a desert for four days so like you're you skip the whole desert part where you're suffering  
**Translation:** 

**[5666.58s] English:** so like there sometimes it's nice to have a friend who's who can't really find the bug but  
**Translation:** 

**[5672.40s] English:** can give you some intuition about the code and you're together with that friend going to the  
**Translation:** Vocabulary: intuition: 直觉

**[5678.24s] English:** desert and then together find that drink of water so at least for me uh maybe it speaks to the  
**Translation:** 

**[5684.08s] English:** loneliness of the programming experience it's that is a source of joy it's maybe also related  
**Translation:** 

**[5689.60s] English:** to delayed gratification i'm a person who you know even as a kid i like the idea of christmas  
**Translation:** 

**[5696.36s] English:** present  
**Translation:** Vocabulary: christmas: 圣诞节; gratification: 满足感

**[5696.56s] English:** having them getting them better than actually getting the presents i would look forward to the  
**Translation:** 

**[5703.56s] English:** day i get the presents but then it's over and i'm disappointed and maybe it's something like  
**Translation:** 

**[5707.58s] English:** also with let's say food i think food tastes better when you're really hungry uh and with  
**Translation:** 

**[5713.32s] English:** yeah you're right with debugging it is not always you know uh great it's like often frustrating but  
**Translation:** Vocabulary: frustrating: 令人沮丧的

**[5719.94s] English:** um then if you can solve it then it's great but there's also like a sweet goldilocks zone if it's  
**Translation:** 

**[5725.82s] English:** too hard and it's not it's not it's not it's not it's not it's not it's not it's not it's not  
**Translation:** Vocabulary: goldilocks: 不难也不易

**[5726.56s] English:** it's you know wasting your time but i think that is another challenge though how will people learn  
**Translation:** 

**[5733.36s] English:** i mean the chart we looked at um we saw that more senior developers are shipping more ai generated  
**Translation:** 

**[5740.68s] English:** code than the junior ones and i think it's very interesting because intuitively you would think  
**Translation:** 

**[5744.70s] English:** it's the junior developers because they don't know let's say how to do the thing yet because  
**Translation:** Vocabulary: intuitively: 直觉上

**[5749.26s] English:** they are more junior and so they use ai to do that thing it could either mean the ai is not  
**Translation:** 

**[5753.58s] English:** good enough yet to solve that task but it could also mean  
**Translation:** 

**[5756.56s] English:** experts are more effective at using it they know  
**Translation:** 

**[5760.00s] English:** where and better how to use it and review the code and they trust the code then more  
**Translation:** 

**[5764.20s] English:** and so i think one issue in the society in the future will be though how do you become an expert  
**Translation:** 

**[5770.22s] English:** if you never try to do the thing yourself and i think one way it's always like for me how i learn  
**Translation:** 

**[5777.18s] English:** is by trying things myself like math textbooks if you look at the solutions yeah you learn something  
**Translation:** 

**[5783.48s] English:** but i think you learn actually better if you try first and then you appreciate the solution  
**Translation:** 

**[5788.74s] English:** differently because you know how to put it into your mental framework and um if lms are here all  
**Translation:** 

**[5794.42s] English:** the time would you actually go through the length at struggling would you be willing to struggle  
**Translation:** 

**[5800.20s] English:** because struggle is not nice right i mean it's struggling and if you use the lm to do everything  
**Translation:** 

**[5805.32s] English:** at some point you will never really take the next step and then you will maybe not get that unlock  
**Translation:** 

**[5810.46s] English:** that you would get as an expert using an lm so it's like you know it's like i think there's like  
**Translation:** 

**[5815.22s] English:** a goldilocks sweet spot where maybe maybe the trick here  
**Translation:** 

**[5818.68s] English:** you know it's like i think there's like a goldilocks sweet spot where maybe maybe the trick here is  
**Translation:** 

**[5818.72s] English:** you make dedicated offline time where you study two hours a day and the rest of the day use lms but  
**Translation:** 

**[5824.56s] English:** i think it's important also for people to still invest in themselves in my opinion to not just  
**Translation:** 

**[5829.36s] English:** you know lm everything yeah there is and uh we together civilization that we each individually  
**Translation:** Vocabulary: individually: 单独地

**[5834.32s] English:** have to find that goldilocks zone yeah uh and in the programming context as developers now we've  
**Translation:** 

**[5839.28s] English:** had this fascinating conversation that started with pre-training and mid-training let's get to  
**Translation:** 

**[5844.64s] English:** post-training a lot of fun stuff in post-training  
**Translation:** 

**[5848.66s] English:** so what are some of the interesting ideas in post-training the biggest one from 2025 is  
**Translation:** 

**[5854.48s] English:** learning this reinforced learning with verifiable rewards you can scale up the training there which  
**Translation:** 

**[5859.82s] English:** means doing a lot of this kind of iterative generate grade loop and that lets the models  
**Translation:** Vocabulary: iterative: 迭代; reinforced: 强化; verifiable: 可验证

**[5865.24s] English:** learn both interesting behaviors on the tool use and software side this could be searching  
**Translation:** 

**[5870.46s] English:** running commands on their own and seeing the outputs and then also that training enables  
**Translation:** 

**[5875.42s] English:** this inference time scaling very nicely and it just gives you a lot of opportunity to do a lot of  
**Translation:** 

**[5878.66s] English:** different things and it's just turned out that this  
**Translation:** Vocabulary: inference: 推断

**[5880.00s] English:** paradigm was very nicely linked in this where it's this kind of rl training enables inference  
**Translation:** 

**[5884.28s] English:** time scaling but inference time scaling could have been found in different ways so it's kind  
**Translation:** Vocabulary: paradigm: 范式

**[5888.24s] English:** of this perfect storm of the models change a lot and the way that they're trained is a major factor  
**Translation:** 

**[5894.28s] English:** in doing so and this has changed how people approach post-training dramatically describe  
**Translation:** Vocabulary: dramatically: 显著地

**[5900.76s] English:** rlvr popularized by deep seek r1 can you describe how it works yeah fun fact um i was on the team  
**Translation:** 

**[5907.82s] English:** that came up with the term rlvr which is from our two to three work before deep seek which is  
**Translation:** Vocabulary: popularized: 普及

**[5912.98s] English:** we don't take a lot of credit for the being the people to popularize the scaling rl but as fun as  
**Translation:** 

**[5918.78s] English:** what academics get as an aside is the ability to name and influence the discourse because the  
**Translation:** Vocabulary: discourse: 话语; popularize: 普及

**[5925.10s] English:** closed labs can only say so much that one of the things you can do as an academic is like you might  
**Translation:** 

**[5930.06s] English:** not have the compute to train the model but you can frame things in a way that ends up being i  
**Translation:** 

**[5935.34s] English:** describe it as like a community can come together  
**Translation:** 

**[5937.82s] English:** around this rlvr term which is very fun and then deep seek is the people that did the training  
**Translation:** 

**[5942.50s] English:** breakthrough which is they scaled the reinforcement learning which was you have the model generate  
**Translation:** 

**[5947.94s] English:** answers and then grade the completion if it was right and then that accuracy is your reward for  
**Translation:** Vocabulary: reinforcement: 强化学习

**[5955.24s] English:** reinforcement learning so reinforcement learning is classically an agent that acts in an environment  
**Translation:** 

**[5960.88s] English:** and the environment gives it a state and a reward back and you try to maximize this reward  
**Translation:** 

**[5966.06s] English:** in the case of language models  
**Translation:** 

**[5967.82s] English:** the reward is normally accuracy on a set of verifiable tasks whether it's math problems  
**Translation:** 

**[5973.74s] English:** coding tasks and it starts to get blurry with things like factual domains like that is also  
**Translation:** 

**[5980.22s] English:** in some ways verifiable or constraints on your instruction like respond only with words that  
**Translation:** Vocabulary: blurry: 模糊; constraints: 限制; verifiable: 可验证

**[5986.38s] English:** start with a like all of these things are verifiable in some way and the core idea of  
**Translation:** 

**[5992.06s] English:** this is you find a lot more of these problems that are verifiable and you let the model try it  
**Translation:** 

**[5997.82s] English:** many times while taking these rl steps  
**Translation:** 

**[6000.00s] English:** these RL gradient updates,  
**Translation:** Vocabulary: gradient: 梯度

**[6003.50s] English:** the infrastructure evolved from this reinforced learning  
**Translation:** 

**[6005.98s] English:** from human feedback,  
**Translation:** Vocabulary: reinforced: 加强的

**[6007.60s] English:** where in that era,  
**Translation:** 

**[6008.42s] English:** the score they were trying to optimize  
**Translation:** 

**[6009.70s] English:** was a learned reward model of aggregate human preferences.  
**Translation:** 

**[6013.08s] English:** So you kind of change the problem domains  
**Translation:** Vocabulary: aggregate: 综合

**[6016.12s] English:** and that let the optimization go on to much bigger scales,  
**Translation:** 

**[6019.44s] English:** which kind of kickstarted a major change  
**Translation:** Vocabulary: kickstarted: 启动; optimization: 优化

**[6021.92s] English:** in what the models can do and how people use them.  
**Translation:** 

**[6024.68s] English:** What kind of domains is RLVR amenable to?  
**Translation:** Vocabulary: amenable: 适合的

**[6028.48s] English:** Math and code are the famous ones.  
**Translation:** 

**[6030.22s] English:** And then there's a lot of work  
**Translation:** 

**[6032.52s] English:** kind of on what is called the rubrics,  
**Translation:** 

**[6034.42s] English:** which is related to a word people might have heard  
**Translation:** Vocabulary: rubrics: 分类标准

**[6036.48s] English:** as LLM as a judge,  
**Translation:** 

**[6037.68s] English:** which is like for each problem,  
**Translation:** 

**[6040.16s] English:** I'll have a set of problems in my training data set.  
**Translation:** 

**[6042.72s] English:** I'll then have another language model and ask it,  
**Translation:** 

**[6046.08s] English:** what would a good answer to this problem look like?  
**Translation:** 

**[6048.68s] English:** And then you can try the problem a bunch of times  
**Translation:** 

**[6050.80s] English:** over and over again  
**Translation:** 

**[6051.72s] English:** and assign a score based on this rubric.  
**Translation:** Vocabulary: rubric: 评分标准

**[6053.80s] English:** So that's not necessarily verifiable  
**Translation:** 

**[6055.20s] English:** like a math and code domain,  
**Translation:** 

**[6056.72s] English:** but this rubrics idea  
**Translation:** 

**[6058.20s] English:** and other scientific,  
**Translation:** 

**[6060.24s] English:** that it might be a little bit more vague  
**Translation:** 

**[6062.62s] English:** is where a lot of the attention is,  
**Translation:** 

**[6064.44s] English:** where they're trying to push this set of methods  
**Translation:** 

**[6066.64s] English:** into these kind of more open-ended domains  
**Translation:** 

**[6069.42s] English:** where the models can learn a lot more.  
**Translation:** 

**[6071.16s] English:** I think that's called reinforcement running  
**Translation:** Vocabulary: reinforcement: 强化

**[6072.66s] English:** with AI feedback, right?  
**Translation:** 

**[6073.96s] English:** That's the older term from it  
**Translation:** 

**[6075.12s] English:** that was coined in Anthropics constitutional AI paper.  
**Translation:** 

**[6078.72s] English:** So it's like a lot of these things come in cycles.  
**Translation:** Vocabulary: anthropics: 人类中心主义

**[6081.38s] English:** Also just one step back for the RLVR.  
**Translation:** 

**[6084.42s] English:** So I think the interesting, beautiful thing here  
**Translation:** 

**[6086.52s] English:** is that you ask the LLM,  
**Translation:** 

**[6088.82s] English:** let's say a math question,  
**Translation:** 

**[6090.00s] English:** and then you know the correct answer  
**Translation:** 

**[6091.58s] English:** and you let the LLM, like you said, figure it out.  
**Translation:** 

**[6094.32s] English:** But how it does that,  
**Translation:** 

**[6095.50s] English:** I mean, you don't really constrain it much.  
**Translation:** Vocabulary: constrain: 限制

**[6097.42s] English:** There are some constraints you can add,  
**Translation:** 

**[6098.88s] English:** like use the same language,  
**Translation:** 

**[6100.72s] English:** don't switch between Spanish and English.  
**Translation:** 

**[6102.50s] English:** But let's say you're pretty much hands-off.  
**Translation:** 

**[6104.88s] English:** You only give the question and the answer.  
**Translation:** 

**[6107.86s] English:** And then the LLM has to, you know,  
**Translation:** 

**[6109.64s] English:** just the task to arrive at the right answer.  
**Translation:** 

**[6112.54s] English:** But the beautiful thing here is  
**Translation:** 

**[6113.76s] English:** what happens in practice  
**Translation:** 

**[6115.02s] English:** is that the LLM will do a step-by-step description.  
**Translation:** 

**[6118.40s] English:** Like, you know, like as a student  
**Translation:** 

**[6119.34s] English:** or like as a...  
**Translation:** 

**[6120.00s] English:** yeah mathematician how you would derive the solution it will give you or it will  
**Translation:** 

**[6124.42s] English:** use those steps and that helps actually the model to improve its own accuracy and then like you said  
**Translation:** 

**[6130.88s] English:** the inference scaling so inference scaling loosely means basically spending more compute during  
**Translation:** 

**[6136.12s] English:** using the lm during inference and here the inference scaling is that the model would use  
**Translation:** Vocabulary: inference: 推理

**[6141.70s] English:** more tokens and also i think in the r1 paper they showed the longer they train the model the longer  
**Translation:** 

**[6146.80s] English:** the responses are they they grow over time they use more tokens so it becomes more expensive  
**Translation:** 

**[6151.52s] English:** becomes more expensive for simple tasks but these explanations they help the model with the accuracy  
**Translation:** 

**[6156.52s] English:** they're also interesting a lot of papers showing what the model explains does not necessarily have  
**Translation:** 

**[6161.76s] English:** to be correct or maybe it's even unrelated to the answer but for some reason it still helps the  
**Translation:** 

**[6166.20s] English:** model like this is the fact that it is um explaining and i think it's also again i don't  
**Translation:** 

**[6171.36s] English:** want to anthropomorphize these elements but it's kind of like how we humans operate right if there's  
**Translation:** 

**[6176.50s] English:** a complex model it's not a complex model it's a complex model it's a complex model it's a complex  
**Translation:** Vocabulary: anthropomorphize: 拟人化

**[6176.78s] English:** math problem let's say in a math class you usually have a notepaper and you do it step by step you  
**Translation:** 

**[6182.36s] English:** cross out things and the model also self-corrects and that that was i think the aha moment in the  
**Translation:** Vocabulary: notepaper: 笔记本

**[6187.72s] English:** r1 paper they called it aha moment because the model itself recognized it made a mistake and  
**Translation:** 

**[6192.06s] English:** then said ah i did something wrong and so let me try and i think that's just so cool that  
**Translation:** 

**[6197.18s] English:** this falls out of just giving it the correct answer and having it figure out how to do it  
**Translation:** 

**[6202.58s] English:** it kind of does in a sense what a human would do although  
**Translation:** 

**[6206.48s] English:** lms don't think like humans it's kind of like an interesting coincidence and it and the other  
**Translation:** 

**[6211.86s] English:** nice side effect is it's great for us humans often to see these steps it builds trust but also we  
**Translation:** Vocabulary: coincidence: 巧合

**[6218.22s] English:** learn we can double check things there's a lot in here i think some of the debate there's been a lot  
**Translation:** 

**[6222.80s] English:** of debate this year on if the language models like these aha i think the aha moments are kind of fake  
**Translation:** 

**[6227.68s] English:** because in pre-training you essentially have seen the whole internet so you have definitely seen  
**Translation:** 

**[6232.78s] English:** people explaining their work even even verbally like a transcript of a  
**Translation:** Vocabulary: transcript: 录音记录; verbally: 口头地

**[6236.48s] English:** lecture you try this oh i messed this up and what reinforcement learning is  
**Translation:** 

**[6240.00s] English:** this rlvr is very good at doing is amplifying these behaviors because they're very useful in  
**Translation:** Vocabulary: amplifying: 增强; reinforcement: 强化

**[6244.32s] English:** enabling the model to think longer and to check its work and i agree that it is very beautiful  
**Translation:** 

**[6249.92s] English:** that this training kind of the model learns to amplify this in a way that is just so useful at  
**Translation:** 

**[6254.24s] English:** the final answers being better i can give you also a hands-on example i was training the grand 3 base  
**Translation:** 

**[6260.08s] English:** model with rlvr on math 500 the base model had an accuracy of about 15 just 50 steps like in a few  
**Translation:** 

**[6269.20s] English:** minutes with rlvr the model went from 15 to 50 accuracy and the model you can't tell me it's  
**Translation:** 

**[6276.08s] English:** learning anything about fundamentally about math and the coin example is weird because there's been  
**Translation:** Vocabulary: fundamentally: 本质上

**[6280.32s] English:** two papers this year one of which i was on that talks about data contamination in quinn and  
**Translation:** 

**[6284.40s] English:** specifically that they train on a lot of this special mid-training phase that we have like  
**Translation:** Vocabulary: contamination: 污染

**[6288.80s] English:** a minute on because it's weird and so they train on problems that are almost identical exactly and  
**Translation:** 

**[6294.08s] English:** so you can see that basically the rl it's not teaching the model any new knowledge  
**Translation:** 

**[6299.20s] English:** about math you can't do that in 50 steps so the knowledge is already there in the pre-training  
**Translation:** 

**[6302.72s] English:** you're just unlocking it i still disagree with the kind of premise because there's a lot of weird  
**Translation:** Vocabulary: premise: 前提; unlocking: 解锁

**[6306.80s] English:** complexities that you can't prove because one of the things that points to weirdness is that if you  
**Translation:** 

**[6312.48s] English:** take the quinn 3 so-called base model and you can you could google on the screen you could google  
**Translation:** Vocabulary: complexities: 复杂性; weirdness: 怪异性

**[6317.44s] English:** like math data set hugging face and you could take a problem and what you do if you put it into quen  
**Translation:** 

**[6322.40s] English:** 3 base the all these math problems have words so it'd be like alice has five apples and takes one  
**Translation:** 

**[6328.16s] English:** and gives three to five apples and takes three to five apples and takes three to five apples and  
**Translation:** 

**[6329.18s] English:** whoever and there are these word problems with these quen based models why people are suspicious  
**Translation:** 

**[6333.50s] English:** of them is if you change the numbers but keep the words quen will produce like a very high  
**Translation:** 

**[6339.34s] English:** without tools will produce a very high accuracy like decimal representation  
**Translation:** Vocabulary: decimal: 小数表示

**[6343.50s] English:** of the answer which means there's some like at some time it was shown problems that were almost  
**Translation:** 

**[6348.30s] English:** identical to the test set and it was using tools to get a very high precision answer  
**Translation:** 

**[6353.58s] English:** but a language model without tools will never actually have this so it's kind of been this  
**Translation:** 

**[6359.18s] English:** big debate in the  
**Translation:** 

**[6360.00s] English:** research community is like how much of these reinforced learning papers that are training  
**Translation:** 

**[6364.10s] English:** on quen and measuring specifically on this like math benchmark where there's been multiple papers  
**Translation:** Vocabulary: benchmark: 参考标准; reinforced: 强化

**[6369.30s] English:** talking about contamination it's like how much can you believe them and i think this is what  
**Translation:** 

**[6372.94s] English:** caused the reputation of rlvr being about formatting because you can get these gains so  
**Translation:** Vocabulary: formatting: 格式化

**[6377.66s] English:** quickly and therefore it must already be in the model but there's a lot of complexity here that  
**Translation:** 

**[6382.00s] English:** we it's not really like controlled experimentation so you don't really know but if it weren't true  
**Translation:** Vocabulary: complexity: 复杂性; experimentation: 实验

**[6388.30s] English:** um i would say distillation wouldn't work right i mean distillation can work to some extent but  
**Translation:** 

**[6393.04s] English:** the thing is that is i think the biggest problem in lm research this contamination because we  
**Translation:** Vocabulary: distillation: 蒸馏

**[6397.92s] English:** don't know what's in the data it's unless you have a new data set it's really impossible and  
**Translation:** 

**[6402.18s] English:** the same you mentioned um math the math data set which is you have a question and an answer and  
**Translation:** 

**[6407.34s] English:** an explanation is given but then also even something simpler like mmlu which is a multiple  
**Translation:** 

**[6412.22s] English:** choice benchmark if you just change the format slightly um like i don't know you  
**Translation:** 

**[6418.30s] English:** use a dot instead of a parenthesis or something like that the model accuracy will vastly differ  
**Translation:** 

**[6424.60s] English:** i think that that could be like a model issue rather than a general issue it's not even malicious  
**Translation:** Vocabulary: parenthesis: 括号

**[6430.04s] English:** by the developers of the lm like hey we want to cheat at that benchmark it's just it has seen  
**Translation:** 

**[6433.88s] English:** something at some point and i think the only fair way to evaluate an lm is to have a new  
**Translation:** Vocabulary: evaluate: 评估

**[6437.98s] English:** benchmark that is after the cutoff date when the lm was deployed can we lay out what would be the  
**Translation:** 

**[6445.02s] English:** sort of the recipe of all the things that would be going to post-training  
**Translation:** Vocabulary: cutoff: 截止日期; deployed: 部署

**[6448.30s] English:** and you mentioned our rlvr was a really exciting effective thing maybe we should elaborate rlhf  
**Translation:** 

**[6454.70s] English:** still has a really important component to play what kind of other ideas are there on post-training  
**Translation:** Vocabulary: elaborate: 详细说明

**[6460.24s] English:** i think you can kind of take this in order i think you can view it as what made o1 which is  
**Translation:** 

**[6465.88s] English:** this first reasoning model possible or what will the latest model be and they actually have you're  
**Translation:** 

**[6472.18s] English:** going to have similar interventions at these where you start with mid-training and the thing that is  
**Translation:** 

**[6478.30s] English:** rumored to enable o1  
**Translation:** 

**[6480.00s] English:** in similar models is really careful data curation where you're providing a broad set of like what  
**Translation:** 

**[6485.88s] English:** is called reasoning traces which is just the model generating words in a forward process  
**Translation:** Vocabulary: curation: 资料整理

**[6491.60s] English:** that is reflecting like breaking down a problem into intermediate steps and trying to solve them  
**Translation:** 

**[6496.66s] English:** so at mid-training you need to have data that is similar to this to make it so that when you move  
**Translation:** 

**[6501.98s] English:** into post-training primarily with this verifiable rewards it can learn and then what is happening  
**Translation:** 

**[6508.46s] English:** today is you're figuring out which problems to give the model and how long you can train it for  
**Translation:** Vocabulary: verifiable: 可验证的

**[6515.78s] English:** and like how much inference you can enable the model to use when solving these verifiable  
**Translation:** 

**[6520.90s] English:** problems so as models get better certain problems are no longer like the model will solve them 100%  
**Translation:** Vocabulary: inference: 推断

**[6528.26s] English:** of the time and therefore there's very little signal in this if we pull if we look at the grpo  
**Translation:** 

**[6532.68s] English:** equation this one is famous for this because essentially the reward given to the agent  
**Translation:** Vocabulary: equation: 方程

**[6537.78s] English:** is  
**Translation:** 

**[6538.46s] English:** based on how good a given action action is a completion is relative to the other answers to  
**Translation:** 

**[6544.62s] English:** that same problem so if all the problems get the same answer there's no signal in these types of  
**Translation:** 

**[6548.38s] English:** algorithms so what they're doing is they're finding harder problems which is why you hear  
**Translation:** 

**[6552.50s] English:** about things like scientific domains which is like that's so hard like getting anything right there  
**Translation:** 

**[6557.62s] English:** if you have a lab or something it just generates so many tokens or much harder software problems so  
**Translation:** 

**[6562.74s] English:** the frontier models are all pushing into these harder domains and they can train on more problems  
**Translation:** 

**[6568.46s] English:** and they can learn more skills at once the rlhf link to this is kind of like rlhf has been and  
**Translation:** Vocabulary: frontier: 前沿

**[6574.30s] English:** still is kind of like the finishing touch on the models where it makes the models more useful  
**Translation:** 

**[6577.98s] English:** by improving the organization or style or tone there's different things that resonates to  
**Translation:** 

**[6583.38s] English:** different audiences like some people like a really quirky model and rlhf could be good at  
**Translation:** 

**[6587.22s] English:** enabling that personality and some people hate this like markdown bulleted list thing that the  
**Translation:** Vocabulary: bulleted: 项目符号; markdown: Markdown; quirky: 古怪

**[6594.02s] English:** models do but it's actually really good for quickly parsing information in rlhf  
**Translation:** 

**[6598.46s] English:** this human feedback stage is really great  
**Translation:** Vocabulary: parsing: 解析

**[6600.00s] English:** for just give putting this into the model at the end of the day so it's what it made chat gpt so  
**Translation:** 

**[6606.58s] English:** magical for people and that use has actually remained fairly stable this formatting can also  
**Translation:** Vocabulary: formatting: 格式化

**[6612.26s] English:** help the models get better at math problems for example so it's like the border between style  
**Translation:** 

**[6619.92s] English:** and formatting and like the method that you use to answer a problem is actually  
**Translation:** 

**[6624.88s] English:** they're all very closely linked in terms of when you're training these models which is why  
**Translation:** 

**[6629.86s] English:** rlhf can still say make a model better at math but these verifiable domains are a much more  
**Translation:** Vocabulary: verifiable: 可验证的

**[6634.80s] English:** direct process to doing this because this kind of makes more sense with the problem formulation  
**Translation:** 

**[6639.94s] English:** which is why it kind of ends up all forming together but to summarize it's like mid-training  
**Translation:** 

**[6643.78s] English:** is give the model the skills it needs to then learn rl and verifiable rewards is let the model  
**Translation:** 

**[6650.60s] English:** try a lot of times so put a lot of compute into trial and error learning across hard problems and  
**Translation:** 

**[6655.48s] English:** then rlhf would be like finish the model make it easy to use  
**Translation:** 

**[6659.28s] English:** you  
**Translation:** 

**[6659.86s] English:** and kind of just round the model out can you comment on the amount of compute required for rlvr  
**Translation:** 

**[6665.26s] English:** it's only gotten up and up so i think grok4 was famous for saying they use a similar amount of  
**Translation:** 

**[6671.48s] English:** compute for pre-training and post-training back to the scaling discussion they involve very different  
**Translation:** 

**[6676.68s] English:** hardware for scaling pre-training is very compute bound which is like this flops discussion which is  
**Translation:** Vocabulary: flops: 浮点运算

**[6681.46s] English:** just how many matrix multiplications can you get through in one time and because rl you're  
**Translation:** 

**[6686.26s] English:** generating these answers you're trying the model in the real world environments  
**Translation:** Vocabulary: environments: 实际环境; matrix: 矩阵; multiplications: 乘法

**[6689.86s] English:** it ends up being much more memory bound because you're generating long sequences  
**Translation:** 

**[6693.28s] English:** and the attention mechanisms have this behavior where you get a quadratic increase in memory  
**Translation:** Vocabulary: quadratic: 二次的

**[6699.30s] English:** as you're getting to longer sequences so the compute becomes very different so you when in  
**Translation:** 

**[6704.70s] English:** pre-training we would talk about a model i think if we go back to like the fighting administration  
**Translation:** 

**[6708.30s] English:** executive order it's like 10 to the 25th flops to train a model if you're using flops in post-training  
**Translation:** 

**[6713.98s] English:** it's a lot weirder because the reality is just like how many hours are you allocating how many  
**Translation:** Vocabulary: allocating: 分配时间

**[6718.28s] English:** gpus for and it's a lot more complicated as you get to the early stage of the game so it's  
**Translation:** 

**[6719.86s] English:** Amen.  
**Translation:** 

**[6720.00s] English:** I think in terms of time, the RL compute is getting much closer  
**Translation:** 

**[6723.52s] English:** because you just can't put it all into one system.  
**Translation:** 

**[6726.78s] English:** Pre-training is so computationally dense  
**Translation:** 

**[6728.74s] English:** where all the GPUs are talking to each other  
**Translation:** Vocabulary: computationally: 计算上

**[6730.54s] English:** and it's extremely efficient,  
**Translation:** 

**[6731.68s] English:** where RL has all these moving parts  
**Translation:** 

**[6733.12s] English:** and it can just take a long time  
**Translation:** 

**[6734.48s] English:** to generate a sequence of 100,000 tokens.  
**Translation:** 

**[6737.34s] English:** If you think about GPT-5.2 Pro taking an hour,  
**Translation:** 

**[6741.38s] English:** it's like, what if your training run has a sample for an hour  
**Translation:** 

**[6743.86s] English:** and you have to make it so that's handled efficiently?  
**Translation:** 

**[6746.56s] English:** So I think in GPU hours or just wall clock hours,  
**Translation:** Vocabulary: efficiently: 高效地

**[6749.46s] English:** the RL runs are probably approaching the number of days as pre-training,  
**Translation:** 

**[6754.42s] English:** but they probably aren't using as many GPUs at the same time.  
**Translation:** 

**[6757.68s] English:** There's rules of thumb where in labs,  
**Translation:** 

**[6759.26s] English:** it's like you don't want your pre-training runs  
**Translation:** 

**[6760.98s] English:** to last more than like a month  
**Translation:** 

**[6762.48s] English:** because they fail catastrophically.  
**Translation:** Vocabulary: catastrophically: 灾难性地

**[6764.50s] English:** And if you were planning a huge cluster to be held for two months  
**Translation:** 

**[6767.52s] English:** and then it fails on day 50,  
**Translation:** Vocabulary: cluster: 会议集群

**[6770.64s] English:** the opportunity costs are just so big.  
**Translation:** 

**[6772.68s] English:** So you kind of don't want to just,  
**Translation:** 

**[6774.50s] English:** people don't want to put all their eggs in one basket,  
**Translation:** 

**[6776.70s] English:** which is like GPT-4 was like the ultimate YOLO run.  
**Translation:** 

**[6779.32s] English:** And nobody ever wanted to do it before  
**Translation:** 

**[6780.86s] English:** where it took like three months to train  
**Translation:** 

**[6782.64s] English:** and everybody was shocked that it worked  
**Translation:** 

**[6784.50s] English:** where I think people are a little bit more cautious and incremental now.  
**Translation:** 

**[6787.54s] English:** So RLVR is more, let's say,  
**Translation:** 

**[6790.62s] English:** unlimited how much you can train and get still benefit  
**Translation:** 

**[6793.04s] English:** where RLHF, because it's a preference tuning,  
**Translation:** 

**[6795.80s] English:** you reach a certain point where it doesn't really make sense  
**Translation:** 

**[6798.44s] English:** to spend more RL budget on that.  
**Translation:** 

**[6800.78s] English:** So just a step back with preference tuning.  
**Translation:** 

**[6803.34s] English:** So there are multiple people that can give multiple,  
**Translation:** 

**[6806.52s] English:** let's say, explanations for the same thing  
**Translation:** 

**[6807.90s] English:** and they can both be correct,  
**Translation:** 

**[6808.90s] English:** but at some point you learn a certain style  
**Translation:** 

**[6811.06s] English:** and it doesn't make sense to iterate on it.  
**Translation:** 

**[6814.44s] English:** My favorite example is like if relatives ask me  
**Translation:** 

**[6817.26s] English:** what laptop they should buy,  
**Translation:** 

**[6818.74s] English:** I give them an explanation or ask them like,  
**Translation:** 

**[6820.64s] English:** yeah, what is your use case?  
**Translation:** 

**[6822.62s] English:** Like they, for example, prioritize battery,  
**Translation:** Vocabulary: prioritize: 优先考虑

**[6825.64s] English:** life and storage.  
**Translation:** 

**[6826.90s] English:** Other people like us, for example,  
**Translation:** 

**[6828.12s] English:** we would prioritize RAM and compute.  
**Translation:** 

**[6830.88s] English:** And so, but both answers are correct,  
**Translation:** 

**[6833.12s] English:** but different people require different answers.  
**Translation:** 

**[6835.18s] English:** And with preference tuning,  
**Translation:** 

**[6836.36s] English:** well, you're trying to average somehow,  
**Translation:** 

**[6837.80s] English:** like you are,  
**Translation:** 

**[6838.90s] English:** asking the data label,  
**Translation:** 

**[6840.00s] English:** us to give you the right or not the right the preferred answer and then you train on that but  
**Translation:** 

**[6844.64s] English:** at some point yeah you learn that average preferred answer and there's no i think reason to  
**Translation:** 

**[6849.52s] English:** keep training longer on it because you know it's just the style where with our lvr you literally  
**Translation:** 

**[6854.64s] English:** give the model well you let the model solve more and more complex difficult problems and so i think  
**Translation:** 

**[6860.64s] English:** that it makes more sense to allocate more budget long term to lrvr and also that right now we are  
**Translation:** 

**[6867.76s] English:** in lr vr 1.0 land where it's still like that simple thing where we have a question and answer  
**Translation:** 

**[6875.04s] English:** but we don't do anything with the one stuff in between so there was a i mean multiple research  
**Translation:** 

**[6880.32s] English:** papers also by google for example on process reward models that also give scores for the  
**Translation:** 

**[6885.92s] English:** explanation how correct is the explanation and i think that will be the next thing let's say  
**Translation:** 

**[6891.20s] English:** our lvr 2.0 for this year focusing in between question and answer like how to leverage that  
**Translation:** 

**[6897.60s] English:** in the right way and i think that will be the next thing let's say our lvr 2.0 for this year focusing in between question and answer like how to leverage that in  
**Translation:** Vocabulary: leverage: 利用

**[6897.74s] English:** information the explanation to improve the explanation and help it to get better accuracy  
**Translation:** 

**[6902.30s] English:** but then so that's one angle and there was a deep seek math version two paper where they also had  
**Translation:** 

**[6908.78s] English:** interesting uh inference scaling there where well first they had um developed models that grade  
**Translation:** 

**[6914.94s] English:** themselves a separate model and i think that that will be one aspect and the other like  
**Translation:** Vocabulary: inference: 推断

**[6919.50s] English:** nathan mentioned it will be for our lrvr branching into other domains  
**Translation:** 

**[6923.66s] English:** the place where people are excited are value functions which is very pretty similar  
**Translation:** 

**[6927.58s] English:** so process reward models are kind of like process reward models assign how good something is to each  
**Translation:** 

**[6934.94s] English:** kind of intermediate step in a reasoning process where value functions apply value to every token  
**Translation:** Vocabulary: token: 标记

**[6939.98s] English:** the language model generates both of these have been largely unproven in the language modeling  
**Translation:** 

**[6946.86s] English:** in this reasoning model era people are more optimistic about value functions forever  
**Translation:** Vocabulary: optimistic: 乐观; unproven: 未证实

**[6951.50s] English:** for whatever reason now i think process reward models were tried a lot more in this pre-01 pre  
**Translation:** 

**[6957.42s] English:** reasoning model era and a lot of people had a lot of head  
**Translation:** 

**[6960.00s] English:** with them so i think a lot of it is the human nature of like value models have a very deep  
**Translation:** 

**[6965.22s] English:** history in reinforcement learning they're one of the first things that were core to like deep  
**Translation:** Vocabulary: reinforcement: 强化

**[6970.00s] English:** reinforcement learning existing is like training value models in this so right now the literature  
**Translation:** 

**[6974.60s] English:** people are excited about trying value models but there's very little proof in it and there are  
**Translation:** 

**[6978.72s] English:** negative examples in trying to scale up process reward models these things don't always hold in  
**Translation:** 

**[6983.40s] English:** the future i think we came to this discussion by talking about scaling and a simple way to  
**Translation:** 

**[6988.82s] English:** summarize what you're saying with like you don't want to do too much rlhf which is eventually the  
**Translation:** 

**[6992.82s] English:** signal scales is people have worked on rlhf for language models for years especially in intense  
**Translation:** 

**[6997.30s] English:** interest after chat gbt and this the first release of a reasoning model trained with rlvr opening  
**Translation:** 

**[7003.64s] English:** eyes 01 had a scaling plot where if you increase the training compute logarithmically you get a  
**Translation:** 

**[7008.74s] English:** linear increase in evaluations and this has been reproduced multiple times i think deep seek had a  
**Translation:** 

**[7013.44s] English:** plot like this but there's no scaling law for rlhf where if you log increase the compute you get  
**Translation:** Vocabulary: evaluations: 评估; reproduced: 复制

**[7018.64s] English:** something like this and you can do it in a linear way so i think that's a really good point  
**Translation:** 

**[7018.80s] English:** performance in fact the seminal scaling paper for rlhf is scaling laws for reward model over  
**Translation:** Vocabulary: seminal: 开创性的

**[7023.96s] English:** optimization so it's like that's a big line to draw with rlvr and the methods we have now and  
**Translation:** 

**[7029.82s] English:** in the future like they will follow the scaling paradigm which is like the best runs you can let  
**Translation:** Vocabulary: optimization: 优化; paradigm: 范式

**[7036.36s] English:** to run for an extra 10x and you get a few x performance but you can't do this with rlhf  
**Translation:** 

**[7040.98s] English:** and that is just going to be field defining and how people approach them where i'm a shill for  
**Translation:** Vocabulary: shill: 代言人

**[7046.64s] English:** people academically to do rlhf and that's a good point i think that's a good point i think that's a  
**Translation:** 

**[7048.78s] English:** good way to describe it is like to do the best rlhf you might not need the extra 10 or 100x of  
**Translation:** Vocabulary: academically: 学术上

**[7054.28s] English:** compute but to do the best rlvr you do so i think there's a what i say is a seminal paper from what  
**Translation:** 

**[7061.90s] English:** was a meta internship it's called it's like the art of scaling reinforcement learning with language  
**Translation:** 

**[7066.66s] English:** models they're what they describe as a framework is scale rl and their incremental experiment  
**Translation:** 

**[7071.90s] English:** was like 10 000 b 200 hours which is like thousands or tens of thousands of dollars per experiment  
**Translation:** Vocabulary: incremental: 逐步的

**[7078.60s] English:** and they do a lot of that  
**Translation:** 

**[7080.00s] English:** Which is just like, this cost is not accessible to the average academic, which is a hard equilibrium where it's trying to figure out how to learn from each community.  
**Translation:** 

**[7091.20s] English:** I was wondering if we could take at this point a bit of a tangent and talk about education and learning.  
**Translation:** 

**[7097.42s] English:** If you're somebody listening to this who's a smart person, interested in programming, interested in AI, so I presume building something from scratch is a good beginning.  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[7107.32s] English:** Can you just take me through what you would recommend people do?  
**Translation:** 

**[7112.00s] English:** I would personally start, like you said, implementing a simple model from scratch that you can run on your computer.  
**Translation:** Vocabulary: implementing: 执行

**[7117.90s] English:** The goal is not, if you build a model from scratch, to have something you use every day for your personal projects.  
**Translation:** 

**[7123.96s] English:** It's not going to be your personal assistant replacing an existing open-weight model or Chachapiti.  
**Translation:** Vocabulary: chachapiti: 查查皮蒂

**[7128.76s] English:** It's to see what exactly goes into the LLM, what exactly comes out of the LLM, how the pre-training works in that sense, on your own computer preferably.  
**Translation:** 

**[7138.00s] English:** And then you learn about the pre-training, the supervised fine-tuning, the attention mechanism.  
**Translation:** Vocabulary: preferably: 最好; supervised: 监督

**[7143.86s] English:** You get a solid understanding of how things work.  
**Translation:** 

**[7146.54s] English:** But at some point, you will reach a limit because small models can only do so much.  
**Translation:** 

**[7150.58s] English:** And the problem with learning about LLMs at scale is, I would say, it's exponentially more complex to make a larger model because it's not that the model just becomes larger.  
**Translation:** 

**[7160.62s] English:** You have to now think about sharding your parameters across multiple GPUs.  
**Translation:** Vocabulary: exponentially: 成指数地; sharding: 分割存储

**[7164.40s] English:** Even for the KV cache, there are multiple ways you can implement it.  
**Translation:** 

**[7167.32s] English:** One is just to understand how it works, just to grow the cache.  
**Translation:** Vocabulary: cache: 缓存

**[7171.56s] English:** It's like a cache you grow step-by-step by, let's say, concatenating lists, growing it.  
**Translation:** 

**[7176.50s] English:** But then that wouldn't be optimal in GPUs.  
**Translation:** Vocabulary: concatenating: 连接; optimal: 最优

**[7179.04s] English:** You wouldn't do that.  
**Translation:** 

**[7179.60s] English:** You would pre-allocate a tensor and then fill it in.  
**Translation:** 

**[7182.16s] English:** But that adds, again, another 20, 30 lines of code.  
**Translation:** 

**[7185.14s] English:** And for each thing, you add so much code.  
**Translation:** 

**[7187.30s] English:** And I think the trick with the book is basically to understand how the LLM works.  
**Translation:** 

**[7191.44s] English:** It's not going to be your production-level LLM.  
**Translation:** 

**[7193.68s] English:** But once you have that, you can understand the production-level LLM.  
**Translation:** 

**[7196.56s] English:** So you're trying to...  
**Translation:** 

**[7197.32s] English:** You're always building LLM that's going to fit on one GPU.  
**Translation:** 

**[7200.00s] English:** Yes, most of them I have.  
**Translation:** 

**[7202.08s] English:** I have some bonus materials on some MOE models.  
**Translation:** 

**[7204.96s] English:** I think one or two of them, they may require multiple GPUs,  
**Translation:** 

**[7208.06s] English:** but the goal is to have it on one GPU.  
**Translation:** 

**[7210.68s] English:** And the beautiful thing is also you can self-verify.  
**Translation:** 

**[7214.02s] English:** It's almost like RLVR when you code these from scratch.  
**Translation:** 

**[7217.38s] English:** You can take an existing model from the Hugging Phase Transformer library.  
**Translation:** 

**[7221.96s] English:** So the Hugging Phase Transformer library is great,  
**Translation:** 

**[7224.28s] English:** but if you want to learn about LLMs,  
**Translation:** 

**[7225.96s] English:** I think that's not the best place to start  
**Translation:** 

**[7227.86s] English:** because the code is so complex because it has to fit so many use cases.  
**Translation:** 

**[7232.32s] English:** Also, some people use it in production.  
**Translation:** 

**[7233.68s] English:** It has to be really sophisticated, and it's really intertwined and really hard.  
**Translation:** Vocabulary: intertwined: 错综复杂; sophisticated: 高级

**[7237.62s] English:** It's not linear to read.  
**Translation:** 

**[7239.06s] English:** It was started as a fine-tuning library,  
**Translation:** 

**[7241.18s] English:** and then it grew to be the standard representation  
**Translation:** 

**[7243.78s] English:** of every model architecture and the way it is loaded.  
**Translation:** 

**[7248.02s] English:** So Hugging Phase is the default place to get a model,  
**Translation:** 

**[7250.56s] English:** and Transformers is the software that enables it  
**Translation:** 

**[7253.04s] English:** so people can easily load a model and do something basic with it.  
**Translation:** 

**[7256.42s] English:** And all Frontier Labs?  
**Translation:** Vocabulary: frontier: 前沿

**[7257.86s] English:** All Frontier Labs that have open-weight models  
**Translation:** 

**[7259.86s] English:** have a Hugging Phase Transformers version of it,  
**Translation:** 

**[7261.86s] English:** like from DeepSeq to GPT-OSS.  
**Translation:** 

**[7263.86s] English:** That's like the canonical weight that you can load there.  
**Translation:** Vocabulary: canonical: 标准的

**[7267.86s] English:** But again, also even Transformers, the library is not used in production.  
**Translation:** 

**[7270.86s] English:** People use then SGLang or VLLM, and it adds another layer of complexity.  
**Translation:** Vocabulary: complexity: 复杂性

**[7275.86s] English:** We should say that the Transformers library has like 400 models.  
**Translation:** 

**[7279.86s] English:** So it's the one library that tries to implement a lot of LLMs,  
**Translation:** 

**[7283.86s] English:** and so you have a huge code base, basically.  
**Translation:** 

**[7286.86s] English:** It's like huge.  
**Translation:** 

**[7287.86s] English:** It's, I don't know, maybe millions, hundreds of thousands of lines of code.  
**Translation:** 

**[7291.86s] English:** And it's like understanding the part that you want to understand  
**Translation:** 

**[7294.86s] English:** is finding the needle in the haystack.  
**Translation:** 

**[7296.86s] English:** But what's beautiful about it is you have a working implementation,  
**Translation:** Vocabulary: haystack: haystack; implementation: 实施方案

**[7299.86s] English:** and so you can work backwards from it.  
**Translation:** 

**[7301.86s] English:** What I would recommend doing, or what I also do,  
**Translation:** Vocabulary: backwards: 逆向

**[7303.86s] English:** is if I want to understand, for example, how OMO3 is implemented,  
**Translation:** 

**[7307.86s] English:** I would look at the weights in the model hub, the config file,  
**Translation:** 

**[7311.86s] English:** and then you can see, oh, they use so many layers.  
**Translation:** 

**[7313.86s] English:** They use, let's say, group query attention or multihead attention in that case.  
**Translation:** Vocabulary: multihead: 多头注意力

**[7317.86s] English:** And you see all the components in like a human reader.  
**Translation:** 

**[7320.00s] English:** I don't know, 100 lines of config file.  
**Translation:** 

**[7322.46s] English:** And then you start, let's say, with your GPT-2 model and add these things, you know.  
**Translation:** 

**[7326.08s] English:** And the cool thing here is you can then load the pre-trained weights and see if they work in your model.  
**Translation:** 

**[7332.24s] English:** And you want to match the same output that you get with a transformer model.  
**Translation:** 

**[7335.54s] English:** And then you can use that as a, basically as a verifiable reward to make your architecture correct.  
**Translation:** Vocabulary: verifiable: 可验证的

**[7340.78s] English:** And then it's kind of, sometimes it takes me a day to, with OMO3, the challenge was rope for the position embeddings.  
**Translation:** 

**[7348.42s] English:** They had a yarn extension and there was some custom scaling there and I couldn't quite match these things.  
**Translation:** Vocabulary: embeddings: 位置嵌入

**[7355.86s] English:** And in this struggle, you kind of understand things.  
**Translation:** 

**[7358.20s] English:** But the cool thing is, at the end, you know you have it correct because you can unit test it.  
**Translation:** 

**[7362.52s] English:** You can check against the reference implementation.  
**Translation:** 

**[7365.10s] English:** And I think that's maybe one of the best ways to learn, really, like to basically reverse engineer something.  
**Translation:** 

**[7370.98s] English:** I think that that is something that everybody that's interested in getting to AI today should do.  
**Translation:** 

**[7375.80s] English:** And I think that's why I liked your book.  
**Translation:** 

**[7376.98s] English:** Because I came to language models from this RL and robotics field.  
**Translation:** 

**[7381.88s] English:** I never had taken the time to just learn all the fundamentals.  
**Translation:** Vocabulary: fundamentals: 基础知识

**[7386.00s] English:** And this transformer architecture I described as being so fundamental as deep learning was a thing that I had to learn in the past.  
**Translation:** 

**[7393.12s] English:** And people need to do this.  
**Translation:** 

**[7394.80s] English:** I think that where a lot of people kind of get overwhelmed is how do I apply this to have impact or find a career path?  
**Translation:** 

**[7403.42s] English:** Because AI and language models make this fundamental stuff.  
**Translation:** 

**[7406.98s] English:** It's so accessible and people with motivation will learn it.  
**Translation:** 

**[7410.00s] English:** And then it's like, how do I get the cycles on goal to contribute to research?  
**Translation:** 

**[7414.60s] English:** And I think that I'm actually fairly optimistic in this because the field moves so fast that a lot of times the best people don't fully solve a problem because there's a bigger, lower, like a bigger problem to solve.  
**Translation:** 

**[7426.00s] English:** That's very low hanging fruit.  
**Translation:** Vocabulary: optimistic: 乐观

**[7426.94s] English:** So they move on.  
**Translation:** 

**[7428.22s] English:** And I think that a lot of what I was trying to do in this RLHF book is like take post-training techniques and just describe how people think about them.  
**Translation:** 

**[7436.32s] English:** Influencing.  
**Translation:** 

**[7436.96s] English:** The model and what people are doing and then.  
**Translation:** 

**[7440.00s] English:** It's remarkable how many things I just think are just like people stop studying them or don't.  
**Translation:** 

**[7445.66s] English:** So I think people trying to get narrow after doing the fundamentals is good.  
**Translation:** 

**[7450.98s] English:** And then reading the relevant papers and being engaged in the ecosystem, it's like you actually, the proximity that random people have online from the leading researchers, like no one knows who all the anonymous account on X and ML is very popular for whatever reason.  
**Translation:** 

**[7467.14s] English:** And no one knows who all these people are.  
**Translation:** Vocabulary: proximity: 近距离

**[7468.56s] English:** Like it could just be random people that study the stuff deeply, especially with the AI tools and just be like, I don't understand this.  
**Translation:** 

**[7474.16s] English:** Keep digging into it.  
**Translation:** 

**[7475.24s] English:** I think is a very useful thing.  
**Translation:** 

**[7477.36s] English:** But there's a lot of research areas that just like are maybe three papers that you need to read.  
**Translation:** 

**[7482.90s] English:** And then one of the authors will probably email you back.  
**Translation:** 

**[7485.60s] English:** But you have to put in a lot of effort into these emails to understand the field.  
**Translation:** 

**[7490.46s] English:** Like I think it would be for a newcomer easily weeks of work to feel like they can truly grasp like what is a very narrow area.  
**Translation:** 

**[7497.38s] English:** But I think going in.  
**Translation:** Vocabulary: newcomer: 新来者

**[7498.72s] English:** Narrow after you have the fundamentals be very useful to people because it's like I became very interested in character training, which is like how you make the model funny or sarcastic or serious.  
**Translation:** 

**[7510.96s] English:** And like, what do you do to the data to do this?  
**Translation:** Vocabulary: fundamentals: 基础知识; sarcastic: 讽刺的

**[7512.98s] English:** And it's like a student at Oxford reached out to me.  
**Translation:** 

**[7516.56s] English:** It's like, hey, I'm interested in this.  
**Translation:** 

**[7517.54s] English:** And I advised him.  
**Translation:** 

**[7518.48s] English:** And I was like, that paper now exists.  
**Translation:** 

**[7519.94s] English:** And it's like, I don't know.  
**Translation:** 

**[7521.48s] English:** There's like two or three people in the world that were very interested in this.  
**Translation:** 

**[7525.08s] English:** He's a PhD student, which gives you an advantage.  
**Translation:** 

**[7527.26s] English:** But like.  
**Translation:** 

**[7528.56s] English:** For me, that was a topic I was waiting for someone to be like, hey, I have time to spend cycles on this.  
**Translation:** 

**[7532.98s] English:** And I'm sure there's a lot more very narrow things where you're just like, oh, it doesn't make sense that there was no answer to this.  
**Translation:** 

**[7538.46s] English:** And I think that it's just like there's so much information coming that people are like, I can't grab onto any of these.  
**Translation:** 

**[7544.46s] English:** But if you just actually stick in an area, I think there's a lot of interesting things to learn.  
**Translation:** 

**[7548.78s] English:** Yeah, I think you can't try to do it all because it would be very overwhelming and you would burn out if you try to keep up with everything.  
**Translation:** 

**[7554.94s] English:** For me, for example, I haven't kept up with computer vision a long time.  
**Translation:** 

**[7557.52s] English:** Just focused on LMS.  
**Translation:** 

**[7558.56s] English:** Coming back to your book.  
**Translation:** 

**[7560.00s] English:** For example, I think this is also a really great book  
**Translation:** 

**[7562.08s] English:** and a really good bang for the buck  
**Translation:** 

**[7563.58s] English:** because you want to learn about RLHF.  
**Translation:** 

**[7565.78s] English:** I wouldn't go out there and read RLHF papers  
**Translation:** 

**[7568.30s] English:** because you would be spending two years.  
**Translation:** 

**[7570.38s] English:** Some of them contradict.  
**Translation:** Vocabulary: contradict: 相互矛盾

**[7571.24s] English:** I just edited the book and I was like,  
**Translation:** 

**[7573.20s] English:** there's a chapter where I had to be like,  
**Translation:** 

**[7575.70s] English:** X papers say one thing and X papers say another thing  
**Translation:** 

**[7578.44s] English:** and we'll see what comes out to be true.  
**Translation:** 

**[7581.48s] English:** What are some of the,  
**Translation:** 

**[7582.38s] English:** just to go through some of the table of contents,  
**Translation:** 

**[7584.00s] English:** some of the ideas we might have missed  
**Translation:** 

**[7585.10s] English:** in the bigger picture of the post-training.  
**Translation:** 

**[7587.06s] English:** So first of all, you do the problem setup,  
**Translation:** 

**[7588.60s] English:** training overview, what are preferences,  
**Translation:** Vocabulary: setup: 设置

**[7590.58s] English:** preferences data in the optimization tools,  
**Translation:** 

**[7593.48s] English:** reward modeling, regularization, instruction tuning,  
**Translation:** Vocabulary: optimization: 优化

**[7596.90s] English:** rejection sampling, reinforcement learning,  
**Translation:** 

**[7599.42s] English:** i.e. policy gradients, direct alignment algorithms,  
**Translation:** Vocabulary: alignment: 对齐; gradients: 梯度; reinforcement: 强化; rejection: 拒绝

**[7603.10s] English:** then constitutional AI and AI feedback,  
**Translation:** 

**[7605.84s] English:** reasoning and inference time scaling,  
**Translation:** Vocabulary: inference: 推理

**[7608.12s] English:** tool use and function calling,  
**Translation:** 

**[7609.54s] English:** synthetic data and distillation evaluation,  
**Translation:** Vocabulary: distillation: 提炼; synthetic: 合成

**[7612.28s] English:** and then open question section,  
**Translation:** 

**[7614.34s] English:** over optimization style and information,  
**Translation:** 

**[7616.54s] English:** and then product UX,  
**Translation:** 

**[7618.60s] English:** character and post-training.  
**Translation:** 

**[7620.42s] English:** So what are some ideas worth mentioning  
**Translation:** 

**[7622.60s] English:** that connect both the educational component  
**Translation:** 

**[7624.48s] English:** and the research component?  
**Translation:** 

**[7625.88s] English:** You mentioned the character training,  
**Translation:** 

**[7627.32s] English:** which is pretty interesting.  
**Translation:** 

**[7628.24s] English:** Character training is interesting  
**Translation:** 

**[7629.24s] English:** because there's so little out of it,  
**Translation:** 

**[7630.52s] English:** but we talk about how people engage with these models  
**Translation:** 

**[7633.20s] English:** and we feel good using them because they're positive,  
**Translation:** 

**[7636.86s] English:** but that can go too far.  
**Translation:** 

**[7638.02s] English:** It could be too positive.  
**Translation:** 

**[7639.16s] English:** And it's like, essentially,  
**Translation:** 

**[7640.54s] English:** it's how do you change your data  
**Translation:** 

**[7642.26s] English:** or decision-making to make it exactly what you want?  
**Translation:** 

**[7646.54s] English:** And OpenAI has this thing called a model,  
**Translation:** 

**[7648.58s] English:** which is essentially their internal guideline  
**Translation:** 

**[7651.76s] English:** for what they want the model to do,  
**Translation:** 

**[7653.60s] English:** and they publish this to developers.  
**Translation:** 

**[7655.42s] English:** So essentially, you can know  
**Translation:** 

**[7656.66s] English:** what is a failure of OpenAI's training,  
**Translation:** 

**[7659.60s] English:** which is like they have the intentions  
**Translation:** 

**[7660.98s] English:** and they haven't met it yet,  
**Translation:** 

**[7662.38s] English:** versus what is something that they actually wanted to do  
**Translation:** 

**[7665.04s] English:** and that you don't like.  
**Translation:** 

**[7666.02s] English:** And that transparency is very nice,  
**Translation:** 

**[7667.38s] English:** but all the methods for curating these documents  
**Translation:** Vocabulary: curating: 策展

**[7670.32s] English:** and how easy it is to follow them is not very well known.  
**Translation:** 

**[7673.44s] English:** I think the way the book is designed  
**Translation:** 

**[7674.84s] English:** is that the reinforcement learning chapter  
**Translation:** 

**[7676.26s] English:** is obviously what people want  
**Translation:** 

**[7677.52s] English:** because everybody hears about it.  
**Translation:** 

**[7678.40s] English:** It's about it with RLVR,  
**Translation:** 

**[7679.58s] English:** and it's the same thing.  
**Translation:** 

**[7680.00s] English:** same algorithms and the same math but it's just like you can use it in very different documents  
**Translation:** 

**[7685.42s] English:** so i think the core of rlhf is like how messy preferences are is essentially a rehash of a  
**Translation:** 

**[7692.48s] English:** paper i wrote years ago but this is essentially the chapter that will tell you why rlhf is never  
**Translation:** Vocabulary: rehash: 旧事重提

**[7697.56s] English:** ever fully solvable because like the way that even rl is set up is that um it assumes that  
**Translation:** 

**[7707.18s] English:** preferences can be quantified and that multiple preferences can be reduced to single values and  
**Translation:** Vocabulary: quantified: 量化; solvable: 可解

**[7713.82s] English:** i think it relates in the economics literature to the von neumann morganston utility theorem  
**Translation:** 

**[7718.66s] English:** and like that is the chapter where all of that philosophical economic and like psychological  
**Translation:** Vocabulary: neumann: 冯·诺伊曼; philosophical: 哲学的; theorem: 定理

**[7724.08s] English:** context it tells you what gets compressed into doing rlhf so it's like you have all of this and  
**Translation:** 

**[7729.28s] English:** then later in the book it's like you use this rl math to make the number go up and i think that  
**Translation:** Vocabulary: compressed: 压缩

**[7733.52s] English:** that's why i think it would be very rewarding for people to do research on is because it's  
**Translation:** 

**[7737.18s] English:** like quantifying preferences is something that is just like humans have designed the problem  
**Translation:** Vocabulary: quantifying: 量化

**[7743.18s] English:** in order to make preferences studyable but there's kind of fundamental debates on like  
**Translation:** 

**[7747.14s] English:** an example is in a language model response you have different things you care about whether  
**Translation:** Vocabulary: studyable: 可研究的

**[7751.82s] English:** it's accuracy or in style and when you're collecting the data they all get compressed  
**Translation:** 

**[7755.72s] English:** into like i like this more than another and it's like like that is happening and there's a lot of  
**Translation:** 

**[7760.88s] English:** there's a lot of research in other areas of the world that go into like how should you actually  
**Translation:** 

**[7765.78s] English:** do this i think  
**Translation:** 

**[7767.18s] English:** social choice theory is the subfield of economics around how you should aggregate preferences  
**Translation:** 

**[7772.92s] English:** and there's like i was i went to a workshop that published a white paper i'm like how can you think  
**Translation:** Vocabulary: aggregate: 汇总

**[7778.70s] English:** about using social choice theory for rlhf so i mostly would want people that get excited about  
**Translation:** 

**[7783.82s] English:** the math to come and have things that they can stumble into and learn this kind of broader  
**Translation:** 

**[7788.02s] English:** context i think there's a fun thing i just keep a list of all the tech reports that i like of  
**Translation:** 

**[7792.94s] English:** reasoning models so in the in chapter 14 which is kind of like a short summary of what's going on in the  
**Translation:** 

**[7797.18s] English:** memory of rlvr there's just like a gigantic table where i just  
**Translation:** 

**[7800.00s] English:** like list every single reasoning model that i like so there's just like i think in education  
**Translation:** Vocabulary: gigantic: 巨大的

**[7804.60s] English:** a lot of it needs to be like at this point it's like what i like because the language models are  
**Translation:** 

**[7809.36s] English:** so good at the math where it's like famous paper direct preference optimization which is like a  
**Translation:** Vocabulary: optimization: 优化

**[7814.88s] English:** much simpler way of solving the problem than rl um the derivations and the appendix skip steps of  
**Translation:** 

**[7820.48s] English:** math and it's like i tried for this book like i redid the derivations and i'm like what the heck  
**Translation:** Vocabulary: appendix: 附录; derivations: 推导

**[7824.80s] English:** is this log trick that they use to change the math but doing it with language models they're  
**Translation:** 

**[7829.60s] English:** like this is the log trick and i'm like i don't know if i like this that the math is so commoditized  
**Translation:** Vocabulary: commoditized: 商品化

**[7835.94s] English:** i think like some of the struggle and reading this appendix and following the math i think is  
**Translation:** 

**[7840.44s] English:** good for learning and i yeah so we're actually returning to this often just on the topic of  
**Translation:** 

**[7846.84s] English:** education you both have brought up the word struggle quite a bit so there is value if you're  
**Translation:** 

**[7854.16s] English:** not struggling as part of this process you're not fully following the  
**Translation:** 

**[7859.60s] English:** proper process for learning i suppose some of the providers are starting to work on models for  
**Translation:** 

**[7864.56s] English:** education which are designed to not give actually i haven't used them but i would guess they're  
**Translation:** 

**[7869.32s] English:** designed to not give all the information at once right and make people work to do this so i think  
**Translation:** 

**[7873.82s] English:** you could train models to do this and it would be a wonderful contribution where like all of this  
**Translation:** 

**[7877.68s] English:** stuff in the book you have to reevaluate every decision for it which is such a great example i  
**Translation:** 

**[7881.98s] English:** think there's there's a chance you work on an ai too which i which i was like oh i think this  
**Translation:** 

**[7886.16s] English:** makes sense i do something like that uh did that the other day and i'm like oh i'm gonna do this  
**Translation:** 

**[7889.60s] English:** this way and then i said okay i'm ready to go and i'm gonna take this right to the person who's  
**Translation:** 

**[7891.66s] English:** going to teach me how to use it and that it makes sense and i thought okay i'm gonna elaborate on  
**Translation:** 

**[7893.10s] English:** why and then i have to figure out like what other ways to work on models and things like that for  
**Translation:** Vocabulary: elaborate: 详细解释

**[7895.62s] English:** example i sometimes for my pastime play video games like i like uh video games with uh puzzles  
**Translation:** 

**[7898.28s] English:** so you know like zelda and metroid and there's this new game where i got stuck and i already got  
**Translation:** Vocabulary: pastime: 业余爱好; zelda: 塞尔达

**[7901.22s] English:** stuck and was okay i you know i don't want to struggle for like two uh two days and so i used  
**Translation:** 

**[7905.72s] English:** an llm but then you say hey please don't uh add any spoilers just you know i'm here and there what  
**Translation:** Vocabulary: spoilers: 剧透

**[7911.04s] English:** do i have to do next and the same thing you can do i guess for math where you say okay i'm here at  
**Translation:** 

**[7915.18s] English:** this point i'm getting stuck don't give me the full solution but what is something i could do  
**Translation:** 

**[7919.60s] English:** trying  
**Translation:** 

**[7920.00s] English:** you know like where you kind of carefully probe it but the problem here is i think it requires  
**Translation:** 

**[7924.74s] English:** discipline and a lot of people do math for like i mean a lot of people who enjoy math but there  
**Translation:** 

**[7929.68s] English:** also a lot of people who need to do it for their homework and then it's like the shortcut and  
**Translation:** 

**[7933.70s] English:** yeah we can develop an educational llm but the other llm is still there and there's still a  
**Translation:** 

**[7938.58s] English:** temptation to use the other llms i think a lot of people especially in college they they understand  
**Translation:** Vocabulary: temptation: 诱惑

**[7943.02s] English:** the stuff they're passionate about they're self-aware about it and they understand it  
**Translation:** 

**[7946.54s] English:** shouldn't be easy like i think we just have to develop a good taste about research taste like  
**Translation:** 

**[7952.78s] English:** school taste about stuff that you should be struggling on and stuff you shouldn't be  
**Translation:** 

**[7959.16s] English:** struggling on which is tricky to know because sometimes you don't have good um long-term vision  
**Translation:** 

**[7964.78s] English:** about what would be actually useful to you in your career but you have to you have to develop that  
**Translation:** 

**[7971.08s] English:** i was talking to maybe my fiancee or friends about this and it's like there's this  
**Translation:** Vocabulary: fiancee: 未婚妻

**[7976.30s] English:** brief  
**Translation:** 

**[7976.52s] English:** 10-year window where all of the homework and all the exams could be digital but before that  
**Translation:** 

**[7981.72s] English:** everybody had to do all the exams in blue book because there was another way and now after ai  
**Translation:** 

**[7985.82s] English:** everybody's going to need to be in blue books and oral exams because everybody could cheat so easily  
**Translation:** 

**[7989.58s] English:** it's like this brief generation that had a different education system like like everything  
**Translation:** 

**[7994.54s] English:** could be digital and but you still couldn't cheat and now it's just gonna go back it's just very  
**Translation:** 

**[7999.62s] English:** funny you mentioned character training just zooming out on a more general topic for that  
**Translation:** 

**[8006.28s] English:** topic  
**Translation:** 

**[8006.52s] English:** how much compute was required and in general to contribute as a researcher  
**Translation:** 

**[8011.22s] English:** are there places where not too much compute is required where you can actually contribute as an  
**Translation:** 

**[8017.48s] English:** individual researcher for on the character training thing i think this research is built  
**Translation:** 

**[8022.24s] English:** on fine-tuning about 7 billion parameter models with laura which is like a essentially you only  
**Translation:** Vocabulary: parameter: 参数

**[8028.56s] English:** fine-tune a small subset of the weights of the model i don't know exactly how many  
**Translation:** 

**[8032.36s] English:** gpu hours that would take but it's doable not doable for me but i think it's doable for me  
**Translation:** Vocabulary: doable: 可行的

**[8036.52s] English:** for every academic so the situation for some academics is like so dire that  
**Translation:** 

**[8040.00s] English:** the only work you can do is doing inference where you have closed models or open models and you get  
**Translation:** Vocabulary: inference: 推断

**[8044.82s] English:** completions from them and you can look at them and understand the models and that's very well  
**Translation:** 

**[8048.70s] English:** suited to evaluation which you become you want to be the best at creating representative problems  
**Translation:** Vocabulary: completions: 完成例句

**[8055.08s] English:** that the models fail on or show certain abilities which i think that you can break through with this  
**Translation:** 

**[8060.62s] English:** so i've like i think that the top end goal for a researcher working on evaluation if you want to  
**Translation:** 

**[8066.86s] English:** have career momentum is the frontier labs pick up your evaluation so it's like you don't need to  
**Translation:** 

**[8071.92s] English:** have every project do this but if you go from a small university with no compute and you figure  
**Translation:** Vocabulary: frontier: 前沿

**[8076.22s] English:** out something that claude struggles with and then the next claude model has it in the blog post like  
**Translation:** 

**[8080.56s] English:** there there's your career rocket ship i think that that's hard but it's like if you want to  
**Translation:** 

**[8085.66s] English:** the maximum possible impact with minimum compute it's something like that which is just get very  
**Translation:** 

**[8091.00s] English:** narrow and it takes learning of where the models are going so you need to like build a tool that  
**Translation:** 

**[8096.80s] English:** tests where not claude 4.5 will fail if you're going to do a research if i'm going to start a  
**Translation:** 

**[8101.56s] English:** research project i need to think where the models in eight months are going to be struggling  
**Translation:** 

**[8105.04s] English:** but what about developing totally novel ideas this is a trade-off i think that if you're doing  
**Translation:** 

**[8110.84s] English:** a phd you could also be like it's too risky to work in language models i'm going way longer term  
**Translation:** 

**[8117.00s] English:** which is like what is what is the thing that's going to define language model development in  
**Translation:** 

**[8121.90s] English:** 10 years which i think that i end up being a person that's pretty practical i mean i went to  
**Translation:** 

**[8126.64s] English:** my  
**Translation:** 

**[8126.80s] English:** phd where it's like i got into berkeley worst case i get a master's and i go work in tech  
**Translation:** 

**[8131.22s] English:** it's like i'm very practical about it so i'm like the life afforded to people to work at these ai  
**Translation:** 

**[8137.06s] English:** companies the amount of like open ai's average compensation is over a million dollars in stock  
**Translation:** 

**[8142.04s] English:** a year for employee any normal person in the u.s to get into this ai lab is transformative for  
**Translation:** 

**[8148.70s] English:** your life so i'm pretty practical of like there's still a lot of upward mobility working in language  
**Translation:** Vocabulary: mobility: 晋升机会

**[8153.12s] English:** models if you're focused and the outcomes it's like look at these jobs but  
**Translation:** 

**[8156.80s] English:** from a research perspective the transformative impact and these  
**Translation:** 

**[8160.00s] English:** academic awards and be the next Yann LeCun is from not working, not caring about language  
**Translation:** 

**[8165.72s] English:** model development very much. It's a big financial sacrifice in that case.  
**Translation:** 

**[8169.40s] English:** So I get to work with some awesome students and they're like, should I go work in an AI lab? And  
**Translation:** 

**[8174.24s] English:** I'm like, you're getting a PhD at a top school or you're going to leave to go to a lab? I'm like,  
**Translation:** 

**[8178.96s] English:** I don't know. If you go work at a top lab, I don't blame you. Don't go work at some random  
**Translation:** 

**[8183.42s] English:** startup that might go to zero. But if you're going to open AI, I'm like, it could be worth  
**Translation:** 

**[8187.88s] English:** leaving a PhD for. Let's more rigorously think through this. So where would you give a  
**Translation:** 

**[8194.20s] English:** recommendation for people to do a research contribution? So the options are academia.  
**Translation:** Vocabulary: academia: 学术界

**[8198.56s] English:** So get a PhD, spend five years publishing. Compute resources are constrained. There's  
**Translation:** 

**[8206.70s] English:** research labs that are more focused on open weight models. And so working there or closed  
**Translation:** Vocabulary: constrained: 资源有限

**[8217.50s] English:** labs.  
**Translation:** 

**[8217.88s] English:** Frontier labs, research labs, open AI, anthropic, XAI, so on.  
**Translation:** Vocabulary: frontier: 前沿

**[8224.56s] English:** The two gradients are the more closed, the more money you tend to get. But also you get less  
**Translation:** 

**[8230.58s] English:** credit. So in terms of building a portfolio of things that you've done, it's very clear of what  
**Translation:** Vocabulary: gradients: 梯度差异

**[8239.06s] English:** you have done as an academic and you have done this. And versus if you are going to go trade this  
**Translation:** 

**[8245.54s] English:** fairly reasonable progression for being a  
**Translation:** Vocabulary: progression: 发展顺序

**[8247.86s] English:** cog in the machine, which could also be very fun. So I think it's very different career paths.  
**Translation:** 

**[8252.96s] English:** But the opportunity cost for being a researcher is very high because PhD students are paid  
**Translation:** 

**[8257.94s] English:** essentially nothing. So I think it ends up rewarding people that have a fairly stable  
**Translation:** 

**[8262.12s] English:** safety net and they realize that they can operate in the long term, which is they want to do very  
**Translation:** 

**[8267.16s] English:** interesting work and get a very interesting job. So it is a fairly, like it is a privileged  
**Translation:** 

**[8272.20s] English:** position to be like, I'm going to see out my PhD and figure it out after because I want to do this.  
**Translation:** Vocabulary: privileged: 特殊机会

**[8276.88s] English:** And I think a lot of academics are going to be like, I'm going to do this. And I think a lot of  
**Translation:** 

**[8277.54s] English:** academics are going to want to be like, at the same time, the academic  
**Translation:** 

**[8280.00s] English:** ecosystem is getting bombarded by funding getting cut and stuff so there's just like so many  
**Translation:** 

**[8285.12s] English:** different trade-offs where i understand plenty of people that are like i can't deal with this  
**Translation:** Vocabulary: bombarded: 受到攻击

**[8290.08s] English:** funding search i grant got cut for no reason by the government or i don't know what's going to  
**Translation:** 

**[8295.86s] English:** happen so i think there's a lot of uncertainty and trade-offs that in my opinion favor just like  
**Translation:** 

**[8300.94s] English:** take the take the well-paying job with meaningful impact because like not also like you're getting  
**Translation:** 

**[8306.06s] English:** paid to sit around at open ai you're building like the cutting edge of things that are  
**Translation:** 

**[8310.32s] English:** changing millions of people's relationship to tech but publication wise they're being more  
**Translation:** 

**[8317.10s] English:** secretive increasingly so so you're publishing less and less and less and less and so you're  
**Translation:** 

**[8321.38s] English:** you are having a positive impact at scale but it's you're a cog in the machine i think it's  
**Translation:** 

**[8328.32s] English:** honestly it hasn't changed that much uh so i have been in academia i'm not in academia anymore  
**Translation:** Vocabulary: academia: 高等教育

**[8334.32s] English:** at the same time i wouldn't want to  
**Translation:** 

**[8336.02s] English:** you know i'm not in academia anymore i'm not in academia anymore i'm not in academia anymore  
**Translation:** 

**[8336.04s] English:** miss my time in academia but what i wanted to say before i get to that part i think it hasn't  
**Translation:** 

**[8340.80s] English:** changed that much i was working in um like i was using ai or machine learning methods for  
**Translation:** 

**[8347.16s] English:** applications and computational biology with collaborators and a lot of people went from  
**Translation:** 

**[8353.48s] English:** academia directly to google and i think it's the same thing back then the professors were like  
**Translation:** Vocabulary: collaborators: 合作者; computational: 计算的

**[8358.58s] English:** you know sad that their students went into industry because they couldn't carry on their  
**Translation:** 

**[8364.22s] English:** legacy in that sense and i think it's the same thing back then the professors were like you know  
**Translation:** 

**[8366.00s] English:** i think it's the same thing it's like it hasn't changed i think that much the only thing that has  
**Translation:** 

**[8370.78s] English:** changed is the scale but you know cool stuff was always developed in industry that was closed you  
**Translation:** 

**[8376.12s] English:** couldn't talk about it and i think the difference now is um well your preference do you like to talk  
**Translation:** 

**[8382.74s] English:** about your work publish or you know you you are more in a closed lab uh the that's one difference  
**Translation:** 

**[8389.84s] English:** the compensation of course but it's always been like that i think so it really depends on you know  
**Translation:** 

**[8395.96s] English:** where you feel comfortable and it's also nothing is forever the only thing right now is  
**Translation:** 

**[8400.00s] English:** there's a third option which is i'm starting a startup that's a lot of people doing startups  
**Translation:** 

**[8406.08s] English:** very risky move uh but can be high is a high risk high reward type of situation where joining an  
**Translation:** Vocabulary: startups: 创业公司

**[8412.48s] English:** industry lab i think is pretty safe you know also upward mobility honestly i think if once you have  
**Translation:** 

**[8418.08s] English:** been at a industry lab it will be easier to find future jobs but then again you know you know it's  
**Translation:** Vocabulary: mobility: 晋升机会

**[8424.24s] English:** like yeah how much do you enjoy the team and working on propriety things versus how do you  
**Translation:** 

**[8431.68s] English:** like the publishing work i mean publishing is stressful it is um you know like acceptance rate  
**Translation:** Vocabulary: propriety: 私有事物

**[8438.72s] English:** at conferences can be arbitrary can be very frustrating but also high reward if you have a  
**Translation:** 

**[8443.20s] English:** paper published you feel good because your name is on there you have a high accomplishment and you  
**Translation:** Vocabulary: arbitrary: 主观随意; conferences: 学术会议; frustrating: 令人沮丧

**[8447.84s] English:** know i feel like my friends who are professors seem on average happier than my friends who work  
**Translation:** 

**[8452.16s] English:** at a frontier lab to be just  
**Translation:** Vocabulary: frontier: 前沿

**[8454.24s] English:** totally honest because that's just grounding and the frontier labs definitely do this  
**Translation:** 

**[8459.76s] English:** 996 which essentially is shorthand for work all the time can you describe 996 this culture that's  
**Translation:** Vocabulary: shorthand: 简写

**[8465.44s] English:** i believe you could say invented in china and uh adopted in silicon valley what's what's 996 it's  
**Translation:** 

**[8472.16s] English:** 9 00 a.m to 9 00 p.m and six days a week six days a week what is that 72 hours okay so what  
**Translation:** 

**[8478.64s] English:** is this basically the standard in ai companies in silicon valley  
**Translation:** 

**[8483.76s] English:** more and more  
**Translation:** 

**[8484.24s] English:** this kind of grind mindset yeah i mean not maybe not exactly like that but i think there is a trend  
**Translation:** 

**[8489.76s] English:** towards it and it's interesting i think it almost flipped because when i was in academia i felt like  
**Translation:** Vocabulary: academia: 学术界; grind: 苦干; mindset: 心态

**[8495.44s] English:** that because as a professor you had to write grants you had to do you had to teach and you had  
**Translation:** 

**[8500.64s] English:** to do your research it's like three jobs in one and it is more than a full-time job if you want to  
**Translation:** 

**[8505.60s] English:** be successful and um i feel like now like nathan just the professors in comparison to a lab i think  
**Translation:** 

**[8512.64s] English:** they have less  
**Translation:** Vocabulary: nathan: 纳森

**[8514.24s] English:** like even maybe pressure or workload than at a frontier lab because they work a lot they're just  
**Translation:** 

**[8518.32s] English:** so fulfilled but like working with  
**Translation:** Vocabulary: fulfilled: 满足; workload: 工作量

**[8520.00s] English:** students and having a constant runway of mentorship and like a mission that is very  
**Translation:** 

**[8524.60s] English:** people oriented i think in an era when things are moving very fast and very chaotic it's very  
**Translation:** Vocabulary: mentorship: 导师制; oriented: 以...为导向

**[8529.68s] English:** rewarding to people yeah and i think as a startup i think it's a pressure it's like you have to make  
**Translation:** 

**[8535.92s] English:** it and it's like it is really important that people put in the time but well it is really  
**Translation:** 

**[8540.76s] English:** hard because you have to deliver constantly and i've been at a startup i had a good time but  
**Translation:** 

**[8546.10s] English:** i don't know if i could do it forever it's like a interesting pace uh and it's exactly like we  
**Translation:** 

**[8551.92s] English:** talked about in the beginning these models are leapfrogging each other and they are just constantly  
**Translation:** 

**[8556.96s] English:** like trying to take the next step compared to the competitors it's just ruthless i think right now  
**Translation:** Vocabulary: leapfrogging: 超越; ruthless: 残酷

**[8562.04s] English:** i think this leapfrogging nature and having multiple players is actually an underrated  
**Translation:** 

**[8566.30s] English:** driver of language modeling process where competition is so deeply ingrained to people  
**Translation:** Vocabulary: ingrained: 根深蒂固

**[8573.26s] English:** and these companies have intentionally created  
**Translation:** 

**[8576.00s] English:** very strong culture like anthropic is known to be so culturally like deeply committed and  
**Translation:** Vocabulary: culturally: 文化上

**[8582.72s] English:** organized i mean like we hear so little from them and everybody it's anthropic seems very aligned  
**Translation:** 

**[8587.84s] English:** and it's like being at a culture that is super tight and having this competitive dynamic is like  
**Translation:** Vocabulary: aligned: 一致

**[8595.00s] English:** talk about a thing that's going to make you work hard and create things that are better so i think  
**Translation:** 

**[8600.50s] English:** that this but that comes at the cost of human capital which is like you can only do this for  
**Translation:** 

**[8605.46s] English:** so long  
**Translation:** 

**[8605.98s] English:** And people are definitely burning out.  
**Translation:** 

**[8607.84s] English:** I think I wrote a post on burnout.  
**Translation:** 

**[8610.66s] English:** I tread in and out of this myself, especially trying to be a manager of full-mode training.  
**Translation:** Vocabulary: burnout: 职业倦怠

**[8616.28s] English:** It's a crazy job doing this.  
**Translation:** 

**[8618.00s] English:** The book Apple in China by Patrick McGee, he talked about how hard the Apple engineers  
**Translation:** 

**[8622.66s] English:** worked to set up the supply chains in China.  
**Translation:** 

**[8624.68s] English:** And he was like, they had saving marriage programs.  
**Translation:** 

**[8627.82s] English:** And he told in a podcast, he was like, people died from this level of working hard.  
**Translation:** 

**[8632.94s] English:** So I think that it's just like, it's a perfect environment for creating progress  
**Translation:** 

**[8637.96s] English:** based on human expense.  
**Translation:** 

**[8640.00s] English:** And I it's there's going to be a lot.  
**Translation:** 

**[8642.00s] English:** There's a lot of the human expense is the nine nine six that we started this with, which is like people do really grind.  
**Translation:** 

**[8648.40s] English:** I also read this book.  
**Translation:** Vocabulary: grind: 辛苦工作

**[8649.50s] English:** I think that a quote word for if someone had to go home to spend time with their family to save the marriage.  
**Translation:** 

**[8655.08s] English:** And it's crazy.  
**Translation:** 

**[8656.20s] English:** Then colleagues say, OK, this is like red alert for this situation.  
**Translation:** 

**[8659.94s] English:** We have to let that person go home this weekend.  
**Translation:** 

**[8662.32s] English:** And but at the same time, I don't think they were forced to work.  
**Translation:** 

**[8665.68s] English:** It's really they were so passionate about the product, I guess, that it is it is you get into that mindset.  
**Translation:** 

**[8670.66s] English:** And I had that sometimes as an academic, but also as an independent person.  
**Translation:** 

**[8674.28s] English:** I have that sometimes I overwork and it's unhealthy.  
**Translation:** Vocabulary: overwork: 过度工作

**[8677.38s] English:** I had, you know, I had back issues.  
**Translation:** 

**[8678.82s] English:** I had neck issues because I did not take the breaks that I maybe should have taken.  
**Translation:** 

**[8682.44s] English:** But it's not because no one forced me to.  
**Translation:** 

**[8684.42s] English:** It's because I wanted to work because that's what open AI and they're like, they want to do this work.  
**Translation:** 

**[8689.02s] English:** Yeah, but there's also there's also a feeling of fervor that's building, especially in Silicon Valley,  
**Translation:** 

**[8694.92s] English:** aligned with this.  
**Translation:** Vocabulary: fervor: 热情

**[8695.68s] English:** The scaling laws idea where there's this hype where the world will be transformed on a scale of weeks and you want to be at the center of it.  
**Translation:** 

**[8703.42s] English:** And then, you know, I have this great fortune of having conversations with a wide variety of human beings.  
**Translation:** 

**[8712.16s] English:** And from there, I get to see all these bubbles and echo chambers across the world.  
**Translation:** 

**[8717.02s] English:** And it's fascinating to see how we humans form them.  
**Translation:** 

**[8719.72s] English:** And I think it's fair to say that Silicon Valley is a kind of echo chamber, a kind of.  
**Translation:** 

**[8725.68s] English:** I think bubbles are actually really useful and effective.  
**Translation:** 

**[8731.84s] English:** It's not necessarily a negative thing because you could be ultra productive.  
**Translation:** 

**[8734.74s] English:** It could be the Steve Jobs reality distortion field because you just convince each other the breakthroughs are imminent.  
**Translation:** Vocabulary: breakthroughs: 重大突破; distortion: 扭曲; ultra: 超极

**[8743.14s] English:** And by convincing each other of that, you make the breakthroughs imminent.  
**Translation:** 

**[8748.60s] English:** Bernhobart wrote a book classifying bubbles, but essentially one of them is financial bubbles, which is like speculation, which is bad.  
**Translation:** Vocabulary: speculation: 投机

**[8754.56s] English:** And the other one is.  
**Translation:** 

**[8755.68s] English:** Like, I don't know the term, but effectively for build outs because it pushes people to build these things.  
**Translation:** 

**[8759.66s] English:** And I do.  
**Translation:** 

**[8760.00s] English:** think ai is in this but i worry about it transitioning to a financial bubble which is  
**Translation:** Vocabulary: transitioning: 转变

**[8764.34s] English:** like it's yeah but also in the space of ideas that bubble you are doing a reality distortion  
**Translation:** 

**[8771.26s] English:** field and that means you are deviating from reality and if you go too far from reality  
**Translation:** Vocabulary: deviating: 偏离现实

**[8777.24s] English:** while also working you know 996 and you might miss some fundamental aspects of the human experience  
**Translation:** 

**[8785.88s] English:** including in silicon valley this is a common problem in silicon valley it's like  
**Translation:** 

**[8789.38s] English:** it's a very specific geographic area you might not understand the midwest perspective the full  
**Translation:** 

**[8795.64s] English:** experience of all the other different humans in the united states and across the world and you  
**Translation:** 

**[8800.98s] English:** and you speak a certain way to each other you convince each other of a certain thing  
**Translation:** 

**[8804.72s] English:** and that that can get you into real trouble whether ai is a big success and becomes a powerful  
**Translation:** 

**[8810.30s] English:** technology or it's not in either trajectory you can get yourself into trouble so you have to  
**Translation:** 

**[8817.10s] English:** consider all of that here you are  
**Translation:** Vocabulary: trajectory: 发展趋势

**[8819.20s] English:** you can get yourself into trouble so you have to consider all of that here you are  
**Translation:** 

**[8819.36s] English:** you can get yourself into trouble so you have to consider all of that here you are  
**Translation:** 

**[8819.38s] English:** a young person trying to say what you want to do with your life the thing that is i don't even  
**Translation:** 

**[8824.32s] English:** really understand this but the sf ai memes have gotten to the point where permanent underclass  
**Translation:** Vocabulary: underclass: 社会底层

**[8830.10s] English:** was one of them which was the idea that the last six months of 2025 was the only time to build a  
**Translation:** 

**[8836.06s] English:** durable value in ai startup or model otherwise all the value will be captured by existing companies  
**Translation:** Vocabulary: durable: 持久的

**[8841.86s] English:** and you will therefore be poor which like that's an example of the sf thing that goes so far i still  
**Translation:** 

**[8848.76s] English:** think for young people it's a good thing to do it's a good thing to do it's a good thing to do it's a  
**Translation:** 

**[8849.36s] English:** good thing to do it's a good thing to do it's a good thing to do it's a good thing to do it's a good thing  
**Translation:** 

**[8849.38s] English:** for young people that going to be able to tap into it if you are really passionate about wanting to  
**Translation:** 

**[8853.94s] English:** have an impact in ai like being physically an sf is the most likely place for you going to do this  
**Translation:** 

**[8859.50s] English:** but it has it has trade-offs i think stuff is an incredible place but there is a bit of a bubble  
**Translation:** 

**[8866.24s] English:** and if you go into that bubble which is extremely valuable just get out also read history books  
**Translation:** 

**[8873.72s] English:** read literature uh visit other places in the world twitter is not and substack is  
**Translation:** Vocabulary: substack: 订阅平台

**[8879.34s] English:** not the entire  
**Translation:** 

**[8880.00s] English:** world i think i would say one of my one people i worked with is moving to sf and it's like i need  
**Translation:** 

**[8885.08s] English:** to get him a copy of the season of the witch which is a history of sf from like 1960 to 1985 which  
**Translation:** 

**[8891.22s] English:** goes through like the hippie revolution like they all the um gays kind of taking over the city and  
**Translation:** Vocabulary: hippie: 嬉皮士; witch: 女巫

**[8898.56s] English:** that culture emerging and then the hiv aids crisis and other things and it's just like that is so  
**Translation:** 

**[8903.60s] English:** recent and so much turmoil and hurt but also like love and sf and it's like no one knows about this  
**Translation:** Vocabulary: turmoil: 动荡

**[8910.22s] English:** it's a great book season of the witch i recommend it a bunch of my sf friends were who do get out  
**Translation:** 

**[8915.88s] English:** recommended it to me and i think that it's just like living there like i lived there and i didn't  
**Translation:** 

**[8921.10s] English:** appreciate this context and it's just like so recent yeah okay let's uh we talked a lot about  
**Translation:** 

**[8929.12s] English:** we talked a lot about a lot of things uh certainly about  
**Translation:** 

**[8933.60s] English:** the things that were exciting last year but this year uh one of the things you guys mentioned is  
**Translation:** 

**[8939.48s] English:** exciting is uh the scaling of texas fusion models and it's just a different exploration of texas  
**Translation:** Vocabulary: texas: 德克萨斯州

**[8944.14s] English:** fusion can you talk about what that is and what the possibility holds sort of different kinds of  
**Translation:** 

**[8950.38s] English:** approaches than the current llms yeah so we talked a lot about the transformer architecture and the  
**Translation:** 

**[8956.40s] English:** autoregressive transformer architecture specifically like gpt and it doesn't mean no one else is  
**Translation:** 

**[8961.42s] English:** working on anything else so people are  
**Translation:** Vocabulary: autoregressive: 自回归

**[8963.60s] English:** always on the let's say lookout for the next big thing because i think it would be almost like um  
**Translation:** 

**[8969.58s] English:** yeah stupid not to because sure right now the transformer architecture is the thing and it  
**Translation:** 

**[8974.30s] English:** works best and there's right now nothing else out there but you know it's always a good idea to not  
**Translation:** 

**[8979.46s] English:** put all your eggs into one basket so people are developing other things alternatives to the um  
**Translation:** 

**[8984.52s] English:** autoregressive transformer one of them would be for example text diffusion models and listeners  
**Translation:** 

**[8990.26s] English:** may know diffusion models from the image generation like  
**Translation:** Vocabulary: diffusion: 扩散模型; listeners: 听众

**[8993.60s] English:** diffusion popularized it there was like a paper on generating images back then people used gans the  
**Translation:** 

**[8999.22s] English:** generative adversarial  
**Translation:** Vocabulary: adversarial: 对抗的

**[9000.00s] English:** networks and then there was this diffusion process where you iteratively denoise an image and that  
**Translation:** 

**[9005.36s] English:** resulted in really good quality images over time stable diffusion was a company other companies  
**Translation:** 

**[9010.38s] English:** build their own diffusion models and then people are now like okay can we try this also for text  
**Translation:** 

**[9015.32s] English:** doesn't you know make intuitive sense yet because it feels like okay it's not something continuous  
**Translation:** Vocabulary: intuitive: 直观的

**[9020.12s] English:** like a pixel that we can differentiate it's like a discrete text so how do we implement that  
**Translation:** 

**[9024.40s] English:** denoising process but it's kind of like similar to uh the bird models by google like when you go  
**Translation:** Vocabulary: denoising: 去噪; differentiate: 区分; discrete: 离散; pixel: 像素

**[9031.84s] English:** back to the original transformer and so they were like the encoder and the decoder the decoder is  
**Translation:** 

**[9036.44s] English:** what we are using right now in gpt and so forth the encoder it's more like um a parallel let's say  
**Translation:** 

**[9043.28s] English:** technique where you have multiple tokens that you fill in in parallel instead so gpt models they do  
**Translation:** 

**[9048.64s] English:** auto regressive one token at a time you complete the sentence one token at a time and in bird  
**Translation:** Vocabulary: regressive: 倒退; token: 令牌

**[9053.88s] English:** models you  
**Translation:** 

**[9054.32s] English:** have  
**Translation:** 

**[9054.38s] English:** a text let's say a sentence that has gaps you like mask them out and then one iteration is  
**Translation:** 

**[9061.00s] English:** filling in these gaps and text diffusion is kind of like that where you are starting with let's say  
**Translation:** Vocabulary: iteration: 迭代

**[9066.94s] English:** some random text and then you are filling in the missing parts or you're refining them iteratively  
**Translation:** 

**[9071.88s] English:** and you have multiple iterations and the cool thing here is that this can do multiple tokens  
**Translation:** Vocabulary: iterations: 迭代; refining: 精炼

**[9077.14s] English:** at the same time so it's kind of like the promise of having it more efficient now the the trade-off  
**Translation:** 

**[9082.52s] English:** is of course well how good is  
**Translation:** 

**[9084.30s] English:** the quality it might be faster and then now you have this dimension of the denoising process the  
**Translation:** 

**[9089.66s] English:** more steps you do the better the text becomes um and people you know i mean you can scale in  
**Translation:** Vocabulary: dimension: 维度

**[9096.38s] English:** different ways they try to see if that is maybe a valid alternative to the auto-regressive model  
**Translation:** 

**[9102.62s] English:** in terms of giving you the same quality for less compute right now i think it's you know there are  
**Translation:** 

**[9108.54s] English:** papers that suggest okay if you want to get the same quality you uh have to crank up the denoising  
**Translation:** 

**[9113.98s] English:** steps you have to crank up the denoising steps you have to crank up the denoising steps you have to crank up the denoising steps  
**Translation:** Vocabulary: crank: 调高

**[9114.22s] English:** and then you end up spending the same compute you would spend on an auto-regressive model  
**Translation:** 

**[9118.62s] English:** um the other downside is  
**Translation:** Vocabulary: downside: 缺点

**[9120.00s] English:** is well it's parallel which sounds appealing but some tasks are not parallel like you know like  
**Translation:** 

**[9125.02s] English:** reasoning tasks tool use maybe where you have to ask a code interpreter to give you an intermediate  
**Translation:** Vocabulary: appealing: 吸引人的; interpreter: 解释者

**[9130.32s] English:** result and that is kind of tricky with diffusion models so there are some hybrids but the main  
**Translation:** 

**[9134.62s] English:** idea is can we parallelize it and so interesting avenue i think right now there are mostly research  
**Translation:** Vocabulary: diffusion: 扩散模型

**[9141.20s] English:** uh let's say models out there like lada and some other ones i saw some by startup some deployed  
**Translation:** 

**[9146.70s] English:** models there is no big uh diffusion model at scale yet like you know like gemini chat gpd scale  
**Translation:** Vocabulary: deployed: 部署

**[9152.94s] English:** on that level but there was an announcement by google or like a site where they said they are  
**Translation:** 

**[9157.92s] English:** launching gemini diffusion and they put it into context of their i think nano 2 model and that  
**Translation:** Vocabulary: gemini: Gemini模型

**[9165.02s] English:** they said basically for the same quality on most benchmarks we can generate things much faster so  
**Translation:** 

**[9170.62s] English:** you mentioned what's next i don't think the text diffusion model is going to replace auto regressive  
**Translation:** Vocabulary: benchmarks: 衡量标准; regressive: 后退的

**[9175.40s] English:** lms but it will be  
**Translation:** 

**[9176.68s] English:** something maybe for quick cheap at scale tasks maybe the free tier in future will be something  
**Translation:** 

**[9183.66s] English:** like that i think there's a couple examples where it's i've heard that it's actually been started to  
**Translation:** 

**[9188.34s] English:** be used i think to paint an example of why this is so much better for example when gpt5 is taking 30  
**Translation:** 

**[9195.08s] English:** minutes to respond is generating one token at a time and this diffusion idea is essentially  
**Translation:** 

**[9199.48s] English:** generate all of those completion all of those tokens in the completion in one batch which is  
**Translation:** Vocabulary: token: 令牌

**[9204.12s] English:** why it could be way faster and i think it could be  
**Translation:** 

**[9206.68s] English:** the startups i'm hearing are like code startups where you have a code base and you have somebody  
**Translation:** Vocabulary: startups: 创业公司

**[9212.28s] English:** that's effectively vibe coding and they say make this change and a code diff is essentially a huge  
**Translation:** 

**[9218.30s] English:** reply from the model but it doesn't have to have that much external context and you can get it  
**Translation:** 

**[9223.40s] English:** really fast by using these diffusion models so that's what i've heard of one example is that  
**Translation:** 

**[9227.02s] English:** they use these text diffusion to generate really long diffs because doing it with a auto regressive  
**Translation:** 

**[9232.50s] English:** model would take minutes and that time for like a user-facing product causes a lot of  
**Translation:** 

**[9236.68s] English:** return so like every second you lose a lot of users so i think  
**Translation:** 

**[9240.00s] English:** I don't think that it's going to be this thing where it's going to grow and have some applications.  
**Translation:** 

**[9244.22s] English:** But I actually thought that different types of models were going to be used for different things sooner than they have been.  
**Translation:** 

**[9249.20s] English:** So I kind of trade off.  
**Translation:** 

**[9251.00s] English:** I think that the tool use point is the one that's stopping them from being most general purpose.  
**Translation:** 

**[9257.50s] English:** Because like cloud code and this hatching PTA with search, the autoregressive chain is interrupted with some external tool.  
**Translation:** 

**[9265.50s] English:** And I don't know how to do that with the diffusion setup.  
**Translation:** Vocabulary: autoregressive: 自回归; diffusion: 扩散; hatching: 孵化; setup: 设置

**[9268.26s] English:** So what's the future of tool use this year and in the coming years?  
**Translation:** 

**[9272.62s] English:** Do you think there's going to be a lot of developments there?  
**Translation:** 

**[9274.82s] English:** How that's integrated to the entire stack?  
**Translation:** 

**[9277.16s] English:** I do think right now, I mean, it's mostly on the proprietary LLM side.  
**Translation:** Vocabulary: proprietary: 私有产权的

**[9281.44s] English:** But I think we will see more of that in the open source tooling.  
**Translation:** 

**[9284.62s] English:** And I think it is a huge unlock because then you can really outsource certain tasks from just memorization to actual, you know,  
**Translation:** Vocabulary: memorization: 记忆; outsource: 外包

**[9293.98s] English:** like instead of having the LLM memorize what is 23 plus 5,  
**Translation:** 

**[9297.64s] English:** just use a calculator.  
**Translation:** Vocabulary: memorize: 记忆

**[9298.36s] English:** So you think that can help solve hallucination?  
**Translation:** 

**[9302.04s] English:** Not solve it, but reduce it.  
**Translation:** Vocabulary: hallucination: 幻觉

**[9303.96s] English:** So still the LLM needs to know what, like when to ask for a tool call.  
**Translation:** 

**[9309.58s] English:** And the second one is, well, it doesn't mean the Internet is always correct.  
**Translation:** 

**[9313.52s] English:** You can do a web search.  
**Translation:** 

**[9314.88s] English:** But let's say I asked who won the World Cup in, let's say, 1998.  
**Translation:** 

**[9319.10s] English:** It still needs to find the right website and get the right information.  
**Translation:** 

**[9321.66s] English:** So you can still go to the incorrect website and give me incorrect information.  
**Translation:** 

**[9325.10s] English:** So I don't think it will fully solve that.  
**Translation:** 

**[9327.66s] English:** But it is improving it in that sense.  
**Translation:** 

**[9330.28s] English:** And so another cool paper earlier this year, I think it was December 31st.  
**Translation:** 

**[9336.60s] English:** It's not technically 2026, but close.  
**Translation:** 

**[9339.84s] English:** So like the recursive language model, that's a cool idea to kind of take this even a bit further.  
**Translation:** 

**[9347.14s] English:** So just to explain.  
**Translation:** Vocabulary: recursive: 递归

**[9348.34s] English:** So, Nathan, you also mentioned earlier, it's harder to do cool research in academia because of the compute budget.  
**Translation:** 

**[9354.76s] English:** If I recall correctly, they did everything with GPT-5.  
**Translation:** Vocabulary: academia: 学术界

**[9357.40s] English:** Right.  
**Translation:** 

**[9357.46s] English:** Right.  
**Translation:** 

**[9357.48s] English:** Right.  
**Translation:** 

**[9357.60s] English:** So they didn't even use local models.  
**Translation:** 

**[9359.00s] English:** But the idea is.  
**Translation:** 

**[9360.00s] English:** let's say if a long context task instead of having the llm solve all of it in like one shot or even  
**Translation:** 

**[9365.80s] English:** like in a chain you break it down into subtasks you have the llm decide when like what is a good  
**Translation:** 

**[9372.00s] English:** let's say subtask and then recursively call an llm to solve that and i think something like that  
**Translation:** Vocabulary: recursively: 递归地

**[9378.50s] English:** also then adding tools and you know each one maybe you have like a huge q and a task each one goes to  
**Translation:** 

**[9384.36s] English:** the web and gathers information and then you pull it at the end together and stitch it back together  
**Translation:** 

**[9388.80s] English:** like where i think there's going to be a lot of unlock using things like that where you you  
**Translation:** 

**[9395.74s] English:** necessarily not necessarily improve the llm itself you improve how the llm is used and what the llm  
**Translation:** 

**[9400.44s] English:** can use one downside right now with tool use is you have to give the llm permission to use tools  
**Translation:** 

**[9406.30s] English:** and that will take some trust especially if you want to unlock things like having an llm answer  
**Translation:** Vocabulary: downside: 缺点

**[9413.08s] English:** emails for you or not even answer but just sort them for you or select them for you or something  
**Translation:** 

**[9416.82s] English:** like that i don't know if i would  
**Translation:** 

**[9418.70s] English:** you  
**Translation:** 

**[9418.80s] English:** give an llm access to my emails right i mean it's like a huge risk i think i think there's a cool  
**Translation:** 

**[9424.40s] English:** one last point on the tool use thing i think that you hinted at this and we've both come at this in  
**Translation:** 

**[9429.84s] English:** our own ways is that the open versus closed models use tools in very different ways where open models  
**Translation:** 

**[9435.32s] English:** people go to hugging face and you download the model and then the person's gonna be like oh what  
**Translation:** 

**[9438.78s] English:** tool do i want and i don't know exa is my search preferred search provider but somebody else might  
**Translation:** 

**[9443.96s] English:** care for a different search startup where you release a model it needs to be useful for multiple  
**Translation:** 

**[9448.12s] English:** tools for multiple tools and i think that's a really good point i think that's a really good  
**Translation:** 

**[9448.70s] English:** point i think that's a really good point i think that's a really good point i think that's a really good point  
**Translation:** 

**[9449.24s] English:** use cases which is really hard because you're making like a general reasoning engine model  
**Translation:** 

**[9454.00s] English:** which is actually what gpt oss is good for but on the closed models you're deeply integrating  
**Translation:** 

**[9459.76s] English:** the specific tool into your experience and i think that open models will struggle to replicate some  
**Translation:** Vocabulary: integrating: 深度融合

**[9465.04s] English:** of the things that i like to do with closed models which will be like i don't know you  
**Translation:** 

**[9469.12s] English:** can reference a mix of public and private information and something that i keep trying  
**Translation:** 

**[9474.32s] English:** every three to six months i try like codex on the web which is just probably what's going to happen  
**Translation:** 

**[9478.68s] English:** something a model to make an update.  
**Translation:** Vocabulary: codex: 代码库

**[9480.00s] English:** to some github repository that i have and it's just like like that set of secure cloud environment  
**Translation:** 

**[9485.72s] English:** is just so nice for just like send it off and do this thing and come back to me and these will  
**Translation:** Vocabulary: repository: 代码仓库

**[9492.32s] English:** probably help define some of the local open and closed niches but i think initially because there  
**Translation:** 

**[9500.34s] English:** was such a rush to get these tool use working that the open models were on the back foot which  
**Translation:** Vocabulary: niches: 细分市场

**[9504.58s] English:** is kind of inevitable i think there's so much research there's so many resources in these  
**Translation:** 

**[9508.14s] English:** frontier labs but will be fun when the open models solve this because it's going to necessitate like  
**Translation:** Vocabulary: frontier: 前沿; necessitate: 要求

**[9513.46s] English:** a bit more flexible and potentially interesting model that might work with this recursive idea  
**Translation:** 

**[9517.78s] English:** to like be an orchestrator and a tool used model so hopefully the necessity drives some interesting  
**Translation:** Vocabulary: necessity: 必要性; orchestrator: 指挥者; recursive: 递归的

**[9523.74s] English:** innovation there so continual learning uh this is a long-standing topic important problem i think  
**Translation:** 

**[9532.40s] English:** that increases in importance as the cost of training of the models goes up so can you explain  
**Translation:** Vocabulary: continual: 不间断的

**[9537.52s] English:** what continual learning is and what it's all about  
**Translation:** 

**[9538.14s] English:** how important it might be this year and in the coming years to make progress  
**Translation:** 

**[9542.58s] English:** this relates a lot to this kind of sf zeitgeist of what is agi what is which is artificial general  
**Translation:** 

**[9549.12s] English:** intelligence and what is asi artificial super intelligence and what are the language models  
**Translation:** Vocabulary: zeitgeist: 时代精神

**[9553.56s] English:** that we have today capable of doing i think the language models can solve a lot of tasks  
**Translation:** 

**[9558.52s] English:** but a key milestone among the ai community is essentially when ai could replace any remote  
**Translation:** Vocabulary: milestone: 关键里程碑

**[9564.76s] English:** worker taking in information and solving digital tasks and solving digital tasks  
**Translation:** 

**[9568.14s] English:** and doing them and the limitation that's highlighted by people is that a language model will not learn  
**Translation:** Vocabulary: highlighted: 突出显示

**[9574.86s] English:** from feedback the same way that an employee is so if you hire an editor the editor will mess up but  
**Translation:** 

**[9580.24s] English:** you will tell them and if you hired a good editor they don't do it again but language models don't  
**Translation:** 

**[9584.10s] English:** have this ability to modify themselves and learn very quickly so the idea is if we're going to  
**Translation:** 

**[9589.60s] English:** actually get to something that is a true like general adaptable intelligence that can go into  
**Translation:** Vocabulary: adaptable: 灵活多变

**[9594.30s] English:** any remote work scenario it needs to be able to learn quickly from feedback and  
**Translation:** 

**[9598.14s] English:** from job learning  
**Translation:** 

**[9600.00s] English:** I'm personally more bullish on language models by being able to just provide them with very good  
**Translation:** 

**[9604.66s] English:** context. You said, like, you maybe offline said that, like, you can write extensive documents  
**Translation:** Vocabulary: bullish: 乐观

**[9610.02s] English:** to models where you say, I have all this information. Here's all the blog posts I've  
**Translation:** 

**[9614.38s] English:** ever written. I like this type of writing. My voice is based on this. But a lot of people don't  
**Translation:** 

**[9619.30s] English:** provide this to models. And the models weren't designed to, like, take this amount of context  
**Translation:** 

**[9624.18s] English:** previously, like the agentic models are just starting. So it's this kind of trade off of  
**Translation:** 

**[9628.72s] English:** do we need to update the weights of this model with this continual learning thing to make them  
**Translation:** 

**[9633.24s] English:** learn fast? Or the counter argument is we just need to provide them with more context and  
**Translation:** 

**[9637.74s] English:** information and they will have the appearance of learning fast by just having a lot of context and  
**Translation:** 

**[9642.10s] English:** being very smart. So we should mention the terminology here. So continual learning refers  
**Translation:** Vocabulary: terminology: 术语

**[9647.74s] English:** to changing the weights continuously so that the model adapts, adjusts based on the new incoming  
**Translation:** 

**[9656.44s] English:** information does so continually and rapidly and frequently.  
**Translation:** Vocabulary: incoming: 新来的

**[9658.72s] English:** And so on. And then the thing you mentioned on the other side of it is generally  
**Translation:** 

**[9665.76s] English:** be referred to as in context learning. As you learn stuff, there's a huge context window.  
**Translation:** 

**[9672.08s] English:** You can just keep loading it with extra information every time you prompt the system, which I think  
**Translation:** 

**[9676.82s] English:** both are legitimately can be seen as learning. It's just a different place where you're doing  
**Translation:** Vocabulary: legitimately: 合乎道理

**[9683.54s] English:** the learning.  
**Translation:** 

**[9684.54s] English:** I think to be honest with you, continual learning, the updating of weights, we  
**Translation:** Vocabulary: continual: 连续的

**[9688.44s] English:** already have that in different flavors. I mean, if you think about how, so I think the distinction  
**Translation:** 

**[9694.36s] English:** here is, do you do that on a personalized custom model for each person or do you on a global  
**Translation:** 

**[9700.68s] English:** model scale? And I think we have that already with going from GPT-5 to 5.1 and 5.2. It's maybe  
**Translation:** 

**[9707.92s] English:** not immediate, but it is like a curated update, a quick created update where there was feedback by  
**Translation:** 

**[9713.00s] English:** the things that couldn't do feedback by the community. They updated the weights next model  
**Translation:** 

**[9717.62s] English:** and so forth.  
**Translation:** 

**[9718.44s] English:** So it is, I mean,  
**Translation:** 

**[9720.00s] English:** like a flavor of that um other even finer grade example a finer grained example is like rlvr you  
**Translation:** 

**[9727.36s] English:** run it it updates the problem is you can't just do that for each person because it would be too  
**Translation:** 

**[9732.96s] English:** expensive to update the weights for each person and i think that's the problem so unless you get  
**Translation:** 

**[9737.68s] English:** i i mean even at openai scale building data centers it would be too expensive i think  
**Translation:** 

**[9743.12s] English:** that is only feasible once you have something on the device where the cost is on the consumer  
**Translation:** Vocabulary: feasible: 可行的

**[9748.16s] English:** like what apple tried to do with apple foundation models putting them on the phone and then they  
**Translation:** 

**[9752.88s] English:** learn from the experience a bit of a related topic but uh this kind of uh maybe anthropomorphized  
**Translation:** Vocabulary: anthropomorphized: 拟人化

**[9759.68s] English:** term but memory what are different ideas of the mechanism of how to add memory to these systems  
**Translation:** 

**[9765.52s] English:** as you're increasingly seeing so so personalized memory especially so right now it's mostly like  
**Translation:** 

**[9771.36s] English:** context basically stuffing things into the context and then just recalling that but again  
**Translation:** 

**[9778.16s] English:** well it's expensive because you have to like i mean you can cache it but still you spend tokens  
**Translation:** Vocabulary: cache: 缓存; recalling: 回忆; stuffing: 填充

**[9786.00s] English:** on that and the second one is you can only do so much i think it's more like a preference and or  
**Translation:** 

**[9791.36s] English:** style i mean a lot of people do that when they solve math problems you say it's basically you  
**Translation:** 

**[9796.08s] English:** can add previous knowledge and stuff but you also give it certain preference pumps do what i  
**Translation:** 

**[9801.28s] English:** preferred last time whatever like something like that but it does it doesn't unlock new capabilities  
**Translation:** 

**[9807.20s] English:** so for that  
**Translation:** 

**[9808.96s] English:** one thing people do use still is laura laura adapters these are basically instead of updating  
**Translation:** Vocabulary: adapters: 转换器

**[9814.16s] English:** the whole weight matrix there are two smaller weight matrices um that you kind of have in  
**Translation:** 

**[9818.96s] English:** parallel or overlay it's like the delta but um yeah you you can do that to some extent but then again  
**Translation:** Vocabulary: delta: 变化量; matrices: 矩阵; matrix: 矩阵

**[9825.68s] English:** it is economics so there were also papers for example laura learns less but forgets less it's  
**Translation:** 

**[9833.52s] English:** like you know it's no free lunch if you want to learn more you need to use more weights but it  
**Translation:** 

**[9838.16s] English:** is more expensive and then again if you  
**Translation:** 

**[9840.00s] English:** learn more you forget more and it's like you have to find that goldilocks zone basically  
**Translation:** Vocabulary: goldilocks: 刚好合适

**[9844.66s] English:** we haven't really mentioned it much but uh implied in this discussion is context length  
**Translation:** 

**[9849.40s] English:** also is there a lot of innovations that's possible there i think the colloquially accepted thing is  
**Translation:** Vocabulary: colloquially: 口语上; innovations: 创新

**[9856.16s] English:** that it's a compute and data problem where you can and sometimes like small architecture things  
**Translation:** 

**[9861.94s] English:** which are like attention variance so if you have we talked about like hybrid attention models which  
**Translation:** Vocabulary: variance: 变化

**[9867.14s] English:** is essentially if you have what looks like a state space model within your transformer and  
**Translation:** 

**[9871.90s] English:** like those are better suited because you have to spend less compute to model the furthest along  
**Translation:** Vocabulary: furthest: 最远的

**[9877.98s] English:** token and i think that but those aren't free because they have to be accompanied by a lot of  
**Translation:** 

**[9883.84s] English:** compute or um the right data so how many sequences of 100 000 tokens do you have in the world and  
**Translation:** Vocabulary: token: 令牌

**[9891.78s] English:** where do you get these and i think it just ends up being pretty expensive to scale them so we've  
**Translation:** 

**[9896.44s] English:** gotten to  
**Translation:** 

**[9897.08s] English:** pretty quickly to like a million tokens of input context length and i would expect it to keep  
**Translation:** 

**[9901.94s] English:** increasing and like get to like 2 million or 5 million this year but i don't expect it to go to  
**Translation:** 

**[9906.24s] English:** like 100 million that would be like a true breakthrough and i think those breakthroughs  
**Translation:** 

**[9910.96s] English:** are possible like the continual learning thing i think of as a research problem where you could  
**Translation:** Vocabulary: breakthroughs: 重大突破; continual: 持续的

**[9914.88s] English:** there could be a breakthrough that just makes transformers work way better at this and it's  
**Translation:** 

**[9919.62s] English:** cheap like these things could happen with so much scientific attention but turning the crank it'll  
**Translation:** 

**[9924.42s] English:** be consistent increases  
**Translation:** 

**[9927.08s] English:** over time i think also looking at the extremes i think there's again no free lunch so the one  
**Translation:** Vocabulary: extremes: 两端

**[9931.70s] English:** extreme to make it cheap you have a let's say an r and n that has a single state a state where you  
**Translation:** 

**[9936.04s] English:** save everything from the previous stuff it's like a specific uh fixed size thing so you never really  
**Translation:** 

**[9942.34s] English:** grow the memory because it's you are stuffing everything into one state but then the longer  
**Translation:** 

**[9948.20s] English:** the context gets the more information you forget because you can't you can't keep i mean compress  
**Translation:** Vocabulary: compress: 压缩; stuffing: 填充

**[9952.70s] English:** everything into one state then on the other hand you have the transformers which try to remember  
**Translation:** 

**[9957.08s] English:** every token which is great sometimes if you want to look up  
**Translation:** 

**[9960.00s] English:** specific information but very expensive because you have the kv cache that grows the dot product  
**Translation:** 

**[9965.08s] English:** that grows but then yeah like you said the mamba layers i mean they kind of have the same problem  
**Translation:** Vocabulary: cache: 缓存; mamba: 蟒蛇

**[9970.16s] English:** i would say like an rnn you try to compress everything into one state you're a bit more  
**Translation:** 

**[9973.56s] English:** selective there but then i think it's like this goldilocks zone again with unimotron 3 they found  
**Translation:** Vocabulary: goldilocks: 刚好; selective: 挑拣

**[9979.38s] English:** like a good ratio of how many attention layers do you need for the global information where  
**Translation:** 

**[9984.16s] English:** everything is accessible compared to having these compressed states and i think that's how  
**Translation:** Vocabulary: compressed: 压缩状态

**[9989.14s] English:** i think we will scale more by finding better let's say ratios in goldilocks zone like between  
**Translation:** 

**[9995.26s] English:** um like computing uh making it cheap enough to run but then also making it powerful  
**Translation:** Vocabulary: computing: 计算

**[10001.62s] English:** enough to be useful and one more plug here um the recursive language model paper that is one  
**Translation:** 

**[10008.68s] English:** of the papers that tries to kind of address the long context thing so what they found is  
**Translation:** Vocabulary: recursive: 递归

**[10012.94s] English:** essentially instead of stuffing everything into this long context um if you break it up into the  
**Translation:** 

**[10018.12s] English:** smaller um  
**Translation:** 

**[10019.12s] English:** multiple smaller tasks so you save memory by having multiple smaller calls you can get actually  
**Translation:** 

**[10024.36s] English:** better accuracy than having the llm try everything all at once i mean it's a new paradigm we will see  
**Translation:** Vocabulary: paradigm: 范式

**[10030.44s] English:** you know there might be other flavors of that so i think with that we will still make improvement  
**Translation:** 

**[10036.32s] English:** on long context but then also like nathan said i think the problem is for pre-training itself we  
**Translation:** 

**[10041.56s] English:** don't have as many long context documents as other documents so it's harder to study basically um how  
**Translation:** 

**[10049.12s] English:** short in length will it take to"?  
**Translation:** 

**[10060.12s] English:** and there's some rules of thumb where you're just like essentially doubling the training  
**Translation:** 

**[10063.38s] English:** context length takes like 2x compute and then you can normally like 2 to 4x the context length  
**Translation:** 

**[10069.84s] English:** again so i think a lot of it ends up being kind of compute bound at pre-training which is in this  
**Translation:** 

**[10075.08s] English:** like we talked about this everyone talks about this big increase in compute for the top lab  
**Translation:** 

**[10079.12s] English:** this year.  
**Translation:** 

**[10080.00s] English:** And that should reflect in some longer context windows.  
**Translation:** 

**[10082.30s] English:** But I think on the post-training side, there's some more interesting things, which is as  
**Translation:** 

**[10085.28s] English:** we have agents, the agents are going to manage this context on their own, where now people  
**Translation:** 

**[10089.72s] English:** that use Cloud Code a lot dread the compaction, which is when Cloud takes its entire full  
**Translation:** 

**[10094.36s] English:** 100,000 tokens of work and compacts it into a bulleted list.  
**Translation:** Vocabulary: bulleted: 项目符号列表

**[10097.94s] English:** But what the next models will do, I'm sure people are already working on this, is essentially  
**Translation:** 

**[10104.00s] English:** the model can control when it compacts and how.  
**Translation:** Vocabulary: compacts: 压缩

**[10106.28s] English:** So you can essentially train your RL algorithm where compaction is an action, where it shortens  
**Translation:** 

**[10111.80s] English:** the history.  
**Translation:** Vocabulary: algorithm: 算法; compaction: 压缩

**[10112.52s] English:** And then the problem formulation will be, I want to keep the maximum evaluation scores  
**Translation:** 

**[10117.98s] English:** that I have gotten while the model compacts its history to the minimum length, because  
**Translation:** 

**[10122.86s] English:** then you have the minimum amount of tokens that you need to do this kind of compounding  
**Translation:** 

**[10127.20s] English:** autoregressive prediction.  
**Translation:** Vocabulary: autoregressive: 自回归; compounding: 复合

**[10128.78s] English:** So there's actually pretty nice problem setups in this, where these agentic models learn  
**Translation:** 

**[10133.04s] English:** to use their context in a different way than just planning.  
**Translation:** Vocabulary: setups: 情景设置

**[10136.28s] English:** One interesting, also recent example would be DeepSeq version 3.2, where they had like  
**Translation:** 

**[10141.92s] English:** the sparse attention mechanism, where they have essentially like a very efficient, small,  
**Translation:** Vocabulary: sparse: 稀疏的

**[10146.90s] English:** lightweight indexer.  
**Translation:** 

**[10148.28s] English:** And instead of attending to all the tokens, it selects, okay, what tokens do I actually  
**Translation:** Vocabulary: lightweight: 轻量级的

**[10151.60s] English:** need?  
**Translation:** 

**[10152.00s] English:** It's, I mean, it's almost comes back to the original idea of attention, where you are  
**Translation:** 

**[10157.30s] English:** selective, but attention is always on.  
**Translation:** 

**[10159.30s] English:** You have maybe zero weight on some of them, but you use them all.  
**Translation:** Vocabulary: selective: 有选择的

**[10161.54s] English:** But they are even more like, okay, let's just mask that out or like not even do that.  
**Translation:** 

**[10166.28s] English:** And even with sliding window attention, Olmo, that is also kind of like that idea.  
**Translation:** 

**[10170.98s] English:** You have that rolling window where you keep it fixed, because you don't need everything  
**Translation:** 

**[10174.02s] English:** all the time.  
**Translation:** 

**[10174.86s] English:** Occasionally, some layers you might, but it's wasteful.  
**Translation:** 

**[10177.96s] English:** But right now, I think, yeah, if you use everything, you're on the safe side, it gives you the  
**Translation:** Vocabulary: wasteful: 浪费的

**[10182.70s] English:** best bang for the buck, because you never miss information.  
**Translation:** 

**[10184.98s] English:** And right now, I think this year will be more also the year figuring out, like you said,  
**Translation:** 

**[10189.54s] English:** how to be more smart about that.  
**Translation:** 

**[10191.38s] English:** I think right now, people want to have the next state of the art, and the state of the  
**Translation:** 

**[10195.44s] English:** art is.  
**Translation:** 

**[10196.28s] English:** It happens to be the brute force, expensive thing.  
**Translation:** Vocabulary: brute: 野蛮

**[10199.56s] English:** And then.  
**Translation:** 

**[10200.00s] English:** Once you have that, like you said, keep that accuracy,  
**Translation:** 

**[10203.36s] English:** but let's see how we can do that cheaper now, like tricks.  
**Translation:** 

**[10206.80s] English:** Yeah, all this scaling thing.  
**Translation:** 

**[10208.70s] English:** The reason we get the quad 4.5 Sonnet model first  
**Translation:** 

**[10212.32s] English:** is because you can train it faster  
**Translation:** 

**[10213.96s] English:** and you're not hitting these compute walls as soon,  
**Translation:** 

**[10215.98s] English:** and they can just try a lot more things and get the model faster  
**Translation:** 

**[10218.92s] English:** even though the bigger model is actually better.  
**Translation:** 

**[10221.66s] English:** I think we should say that there's a lot of exciting stuff  
**Translation:** 

**[10223.86s] English:** going on in the AI space.  
**Translation:** 

**[10226.16s] English:** My mind has recently been really focused on robotics,  
**Translation:** 

**[10230.00s] English:** so we have today really almost entirely didn't talk about robotics.  
**Translation:** 

**[10234.24s] English:** There's a lot of stuff on image gen, video generation.  
**Translation:** 

**[10239.40s] English:** I think it's fair to say that the most exciting research work  
**Translation:** 

**[10243.60s] English:** in terms of the amount, intensity, fervor is in the LLM space,  
**Translation:** Vocabulary: fervor: 热情

**[10249.24s] English:** which is why I think it's justified for us to really focus on the LLM  
**Translation:** 

**[10252.30s] English:** that we're discussing.  
**Translation:** 

**[10253.86s] English:** But it would be nice to bring in some certain things that might be useful.  
**Translation:** 

**[10257.02s] English:** For example, world models.  
**Translation:** 

**[10259.48s] English:** There's growing.  
**Translation:** 

**[10260.00s] English:** Excitement on that.  
**Translation:** 

**[10261.10s] English:** Do you think there will be any use in this coming year  
**Translation:** 

**[10264.92s] English:** for world models in the LLM space?  
**Translation:** 

**[10267.70s] English:** Yes, I do think so.  
**Translation:** 

**[10269.48s] English:** Also with LLMs, what's an interesting thing here is I think  
**Translation:** 

**[10272.20s] English:** if we unlock more LLM capabilities,  
**Translation:** 

**[10274.90s] English:** it also automatically unlocks all the other fields  
**Translation:** 

**[10277.50s] English:** because, well, not unlocks, but makes progress faster  
**Translation:** 

**[10280.52s] English:** because a lot of researchers and engineers use LLMs,  
**Translation:** 

**[10283.98s] English:** like we said, for coding.  
**Translation:** 

**[10284.92s] English:** So even if they work on robotics,  
**Translation:** 

**[10286.70s] English:** if you optimize these LLMs that help you with coding,  
**Translation:** 

**[10289.48s] English:** you know, it's like,  
**Translation:** Vocabulary: optimize: 优化

**[10290.08s] English:** it pays off.  
**Translation:** 

**[10291.14s] English:** But then, yes, world models are interesting.  
**Translation:** 

**[10294.26s] English:** It's basically where you have the model run a simulation of the world,  
**Translation:** 

**[10299.12s] English:** in a sense, like a little toy thing of the real thing,  
**Translation:** Vocabulary: simulation: 模拟

**[10302.08s] English:** which can, again, unlock capabilities  
**Translation:** 

**[10304.88s] English:** that the LLM is not aware of.  
**Translation:** 

**[10308.14s] English:** It can simulate things.  
**Translation:** 

**[10309.90s] English:** And I think, see, this is like something,  
**Translation:** Vocabulary: simulate: 模拟

**[10312.02s] English:** I think LLMs, they just happen to work well by pre-training  
**Translation:** 

**[10316.80s] English:** and then doing the next token prediction.  
**Translation:** Vocabulary: token: 令牌

**[10318.76s] English:** But we could do...  
**Translation:** 

**[10320.00s] English:** this even a bit you know like sophisticated in a sense so what i'm saying is like with uh there's  
**Translation:** Vocabulary: sophisticated: 复杂高级

**[10325.68s] English:** like uh i think it was by meta a paper uh coda world models um so where they basically apply  
**Translation:** 

**[10331.76s] English:** the concept of world models to llms again where they and so instead of just having next token  
**Translation:** 

**[10336.80s] English:** prediction and verifiable rewards checking the answer correctness they also make sure the  
**Translation:** 

**[10341.76s] English:** intermediate variables are correct you know like it's kind of like a the model is learning basically  
**Translation:** Vocabulary: correctness: 正确性; verifiable: 可验证的

**[10347.14s] English:** the code environment in a sense and i think this makes a lot of sense it's just like expensive to  
**Translation:** 

**[10351.96s] English:** do but uh this is like making things more sophisticated like modeling um like modeling  
**Translation:** 

**[10360.42s] English:** the whole thing not just the result and uh so it can add more uh value i remember when i was a grad  
**Translation:** 

**[10367.90s] English:** student there is a um so there's a competition called casp i think where they do a protein  
**Translation:** 

**[10375.62s] English:** structure prediction like they  
**Translation:** 

**[10377.12s] English:** predict the structure of a protein that is not solved yet and at that point so in a sense this  
**Translation:** 

**[10384.04s] English:** is actually great and i think we need something like that for llms also where you do the benchmark  
**Translation:** 

**[10389.14s] English:** but no one does so you hand in the results but no one knows the solution and then after the fact  
**Translation:** Vocabulary: benchmark: 评估标准

**[10392.96s] English:** someone revealed that but uh alpha fold when it came out it crushed uh you know this benchmark i  
**Translation:** 

**[10400.14s] English:** mean there are also multiple very uh iterations but i remember the first one um i'm not an  
**Translation:** Vocabulary: alpha: 阿尔法; iterations: 版本

**[10407.12s] English:** expert in that subfield but the first one explicitly modeled the physical um interactions of  
**Translation:** 

**[10412.30s] English:** the you know the physics of the molecule also like the angles impossible angles and then in the next  
**Translation:** Vocabulary: explicitly: 明确地

**[10417.60s] English:** version i think they got rid of this so and just with brute force scaling it up and i think with  
**Translation:** 

**[10422.04s] English:** llms we are currently in this brute force scaling because it just happens to work but i do think  
**Translation:** Vocabulary: brute: 粗暴

**[10426.08s] English:** also at some point it might make sense to bring back this thing and i think with cold with world  
**Translation:** 

**[10432.04s] English:** models i think that is where i think that might be actually quite cool um i mean  
**Translation:** 

**[10437.12s] English:** yeah and of course also for robotics that is  
**Translation:** 

**[10440.00s] English:** completely unrelated from LLMs.  
**Translation:** 

**[10443.30s] English:** Yeah, yeah.  
**Translation:** 

**[10443.76s] English:** And robotics is very explicit.  
**Translation:** Vocabulary: explicit: 明确的

**[10445.86s] English:** So there's the problem of locomotion or manipulation.  
**Translation:** 

**[10448.08s] English:** Locomotion is much more solid,  
**Translation:** Vocabulary: locomotion: 移动; manipulation: 操作

**[10449.48s] English:** especially in the learning domain.  
**Translation:** 

**[10451.26s] English:** But there's a lot of value,  
**Translation:** 

**[10452.58s] English:** just like with the initial protein folding systems,  
**Translation:** 

**[10454.70s] English:** bringing in the traditional model-based methods.  
**Translation:** 

**[10458.30s] English:** So it's unlikely that you can just learn the manipulation  
**Translation:** 

**[10464.00s] English:** or the whole body local manipulation problem end-to-end.  
**Translation:** 

**[10467.76s] English:** That's the dream.  
**Translation:** 

**[10468.82s] English:** But then you realize,  
**Translation:** 

**[10470.84s] English:** when you look at the magic of the human hand  
**Translation:** 

**[10472.84s] English:** and the complexity of the real world,  
**Translation:** 

**[10474.72s] English:** you realize it's really hard to learn this all the way through  
**Translation:** 

**[10477.52s] English:** the way, I guess, AlphaFold 2 did.  
**Translation:** 

**[10480.38s] English:** I'm excited about the robotic learning space  
**Translation:** 

**[10482.56s] English:** because I think it's collectively getting supercharged  
**Translation:** 

**[10486.12s] English:** by all the excitement and investment  
**Translation:** 

**[10487.78s] English:** in language models generally,  
**Translation:** 

**[10489.52s] English:** where they're getting the infrastructure  
**Translation:** 

**[10490.96s] English:** for training transformers,  
**Translation:** 

**[10492.38s] English:** which is a general modeling thing,  
**Translation:** 

**[10494.20s] English:** is becoming world-class industrial tools  
**Translation:** 

**[10498.82s] English:** where wherever that was a limitation for robotics,  
**Translation:** 

**[10502.26s] English:** it's just way better.  
**Translation:** 

**[10503.22s] English:** There's way more compute.  
**Translation:** 

**[10504.28s] English:** And then on top of that,  
**Translation:** 

**[10505.22s] English:** they take these language models  
**Translation:** 

**[10506.38s] English:** and use them as central units  
**Translation:** 

**[10508.82s] English:** where you can do interesting explorative work  
**Translation:** 

**[10510.82s] English:** around something that already works.  
**Translation:** Vocabulary: explorative: 探索性的工作

**[10513.32s] English:** And then I see it emerging as,  
**Translation:** 

**[10515.76s] English:** kind of like we talked about  
**Translation:** 

**[10517.38s] English:** Hugging Face transformers and Hugging Face.  
**Translation:** 

**[10519.14s] English:** I think when I was at Hugging Face,  
**Translation:** 

**[10520.24s] English:** I was trying to get this to happen,  
**Translation:** 

**[10521.46s] English:** but it was too early.  
**Translation:** 

**[10522.32s] English:** It's like these open robotic models on Hugging Face  
**Translation:** 

**[10526.14s] English:** and having people be able to contribute data  
**Translation:** 

**[10528.14s] English:** and find out what's going on.  
**Translation:** 

**[10528.64s] English:** And I think that's a really good thing.  
**Translation:** 

**[10528.66s] English:** I think that's a really good thing.  
**Translation:** 

**[10528.72s] English:** I think that's a really good thing.  
**Translation:** 

**[10528.82s] English:** I think we're much closer now  
**Translation:** 

**[10531.02s] English:** that the investment in robotics  
**Translation:** 

**[10532.74s] English:** and I think self-driving cars is related  
**Translation:** 

**[10534.88s] English:** and it enables this,  
**Translation:** 

**[10536.22s] English:** where it's like once you get to the point  
**Translation:** 

**[10537.64s] English:** where you can have this sort of ecosystem  
**Translation:** 

**[10539.16s] English:** where somebody can download a robotics model  
**Translation:** 

**[10541.36s] English:** and maybe fine-tune it to their robot  
**Translation:** 

**[10543.10s] English:** or share data sets across the world.  
**Translation:** 

**[10545.46s] English:** And there's some data,  
**Translation:** 

**[10546.30s] English:** there's some work in this area,  
**Translation:** 

**[10548.40s] English:** like RTX, I think it was a few years ago  
**Translation:** 

**[10550.44s] English:** where people are starting to do that.  
**Translation:** 

**[10552.06s] English:** But I think once they have this ecosystem,  
**Translation:** 

**[10553.60s] English:** it'll look very different.  
**Translation:** 

**[10554.58s] English:** And then this whole post-ChatGPT boom  
**Translation:** 

**[10558.32s] English:** is going to be a big thing.  
**Translation:** 

**[10558.64s] English:** Putting more resources into that.  
**Translation:** 

**[10560.00s] English:** which i think is a very good area for doing research this is also resulting in much better  
**Translation:** 

**[10564.64s] English:** more accurate more realistic simulators being built uh closing the sim to real gap in the  
**Translation:** Vocabulary: simulators: 模拟器

**[10569.70s] English:** robotic space but you know you mentioned a lot of excitement in the robotics space and a lot  
**Translation:** 

**[10575.84s] English:** of investment the downside of that which happens in hype cycles i personally believe most robotics  
**Translation:** Vocabulary: downside: 负面方面

**[10582.22s] English:** people believe that the it's not robotics is not going to be solved at at the time scale  
**Translation:** 

**[10589.32s] English:** as being kind of implicit or explicitly promised and so what happens when there's all these  
**Translation:** Vocabulary: explicitly: 明确地

**[10595.62s] English:** robotic companies that spring up and then they don't have a product that works then there's going  
**Translation:** 

**[10602.24s] English:** to be this kind of crash of excitement which is nerve-wracking there's hopefully something else  
**Translation:** 

**[10607.50s] English:** will come in and keep swooping in so that the the continued development of some of these ideas  
**Translation:** 

**[10613.48s] English:** keeps going it's also related to the continual learning issue essentially where the real world  
**Translation:** Vocabulary: continual: 持续; swooping: 盘旋

**[10618.60s] English:** is so complacent  
**Translation:** 

**[10619.32s] English:** complex where with lms yeah you don't need to really have something learn for the user because  
**Translation:** Vocabulary: complacent: 自满

**[10625.68s] English:** there are a lot of things everyone has to do everyone maybe wants to i don't fix their  
**Translation:** 

**[10630.96s] English:** grammar in their email or code or something like that it's more constrained so you can kind of  
**Translation:** Vocabulary: constrained: 限制较多

**[10635.98s] English:** prepare the model for that but preparing the robot for the real world that's harder i mean you have  
**Translation:** 

**[10640.98s] English:** the foundation models the robotic foundation models but you can learn certain things like  
**Translation:** 

**[10645.34s] English:** grasping things but then again i think every everyone's house is different you know like  
**Translation:** 

**[10650.26s] English:** it's so different and that is i think where the robot would have to learn on the job essentially  
**Translation:** Vocabulary: grasping: 抓取

**[10655.32s] English:** and i think that i guess is the the bottleneck right now like how to you know customizing it  
**Translation:** 

**[10660.60s] English:** on the fly essentially i do i don't think i can possibly understate the importance of the thing  
**Translation:** Vocabulary: bottleneck: 瓶颈; understate: 低估

**[10667.30s] English:** that doesn't get talked about almost at all by robotics folks or anyone is safety all the  
**Translation:** 

**[10674.10s] English:** interesting complexities  
**Translation:** Vocabulary: complexities: 复杂性

**[10675.18s] English:** we talk about learning all the failure modes and failure cases everything we've been talking  
**Translation:** 

**[10678.78s] English:** about lm sometimes  
**Translation:** 

**[10680.00s] English:** fails in its interesting ways all of that is fun and games in the llm space in the robotic space  
**Translation:** 

**[10687.00s] English:** in people's homes across millions of minutes billions of interactions you really are almost  
**Translation:** 

**[10695.56s] English:** allowed to fail never when you have embodied systems that are put out there in the real world  
**Translation:** 

**[10702.68s] English:** you just have to solve so many problems you never thought you'd have to solve when you're  
**Translation:** Vocabulary: embodied: 体现

**[10709.68s] English:** just thinking about the general robot learning problem i'm so bearish on in-home learned robots  
**Translation:** 

**[10717.18s] English:** for consumer purchase i'm very bullish on self-driving cars and i'm very bullish for  
**Translation:** Vocabulary: bullish: 乐观

**[10721.46s] English:** robotic automation e.g like amazon distribution where amazon has built whole new distribution  
**Translation:** 

**[10726.82s] English:** centers designed for robots first rather than humans there's a lot of excitement in ai circles  
**Translation:** Vocabulary: automation: 自动化

**[10731.56s] English:** about ai enabling automation and like mass scale manufacturing and i do think that the path to  
**Translation:** 

**[10737.84s] English:** robots doing that is more  
**Translation:** 

**[10739.68s] English:** reasonable where it's like a thing that is designed and optimized to do a repetitive task  
**Translation:** 

**[10744.36s] English:** that a human could conceivably do but doesn't want to and then i'm so but it's also going to  
**Translation:** Vocabulary: conceivably: 可以想象; optimized: 优化; repetitive: 重复

**[10751.60s] English:** take a lot longer than people probably predict i think that the leap from ai singularity to  
**Translation:** 

**[10758.34s] English:** we can now scale up mass manufacturing in the u.s because we have a massive ai advantage is one that  
**Translation:** 

**[10764.14s] English:** is troubled by a lot of political and other challenges  
**Translation:** 

**[10769.68s] English:** let's talk about timelines uh specifically timelines to agi or asi is it fair like as a  
**Translation:** Vocabulary: timelines: 时间线

**[10781.26s] English:** starting point to say that nobody really agrees on the definitions of agi and asi i kind of think  
**Translation:** 

**[10786.88s] English:** there's a lot of disagreement but among i've been getting pushback where a lot of people kind of  
**Translation:** 

**[10792.02s] English:** say the same thing which is like a a thing that could reproduce most digital economic work so  
**Translation:** 

**[10798.06s] English:** like the remote remote workers i'm not sure if that's the right word i'm not sure if that's the  
**Translation:** 

**[10799.68s] English:** right word i'm not sure if that's the right word i'm not sure if that's the right word  
**Translation:** 

**[10800.00s] English:** reasonable example and i think open ai's definition is somewhat um related to that which is like an ai  
**Translation:** 

**[10806.50s] English:** that can do a lot of economic like a certain number of economically valuable tasks which i  
**Translation:** 

**[10811.12s] English:** don't really love as a definition but i think it could be a grounding point because um language  
**Translation:** Vocabulary: economically: 经济上

**[10816.84s] English:** models today are immensely powerful are not this remote worker drop-in and there are things that  
**Translation:** 

**[10823.00s] English:** you could think of that are could be done by an ai that are way harder than remote work which are  
**Translation:** Vocabulary: immensely: 极其

**[10827.70s] English:** like solving a finding an unexpected scientific discovery that you couldn't even pause it which  
**Translation:** 

**[10833.38s] English:** would be an example of something that somebody says it's like an artificial super intelligence  
**Translation:** 

**[10836.84s] English:** problem or like taking in all medical records and finding linkages across certain illnesses that  
**Translation:** 

**[10846.04s] English:** people didn't know or figuring out that some common drug can treat some niche cancer like  
**Translation:** Vocabulary: linkages: 关联; niche: 专科

**[10850.56s] English:** they would say that that is like a super intelligence thing so these are kind of natural  
**Translation:** 

**[10854.24s] English:** tiers my problem with it is that it  
**Translation:** Vocabulary: tiers: 等级

**[10856.90s] English:** you  
**Translation:** 

**[10857.70s] English:** becomes deeply entwined with like the quest for meaning of ai and this religious aspects to it  
**Translation:** Vocabulary: entwined: 纠缠

**[10862.50s] English:** so there's kind of different there's different paths you can take it and i don't even know if  
**Translation:** 

**[10867.42s] English:** the remote work is a good definition because what exactly is that it's like perfect tool use  
**Translation:** 

**[10873.54s] English:** i actually i mean i like i don't know if you like the originally titled ai 27 report they focus more  
**Translation:** 

**[10881.16s] English:** on code and research taste so the the target there is the superhuman coder so they have several  
**Translation:** 

**[10887.70s] English:** several milestone systems superhuman coders superhuman ai researcher then super intelligent ai  
**Translation:** 

**[10894.10s] English:** researcher and then the full asi artificial super intelligence but the after you develop the super  
**Translation:** 

**[10900.90s] English:** human coder everything else falls quickly there the task is to have a fully autonomous like  
**Translation:** 

**[10909.70s] English:** automate coding so any kind of coding you need to do in order to perform research is fully automated  
**Translation:** Vocabulary: automate: 自动化; automated: 已自动化; autonomous: 自主

**[10917.70s] English:** and from there humans would  
**Translation:** 

**[10920.00s] English:** be doing AI research together with that system, and they will quickly be able to develop a system  
**Translation:** 

**[10925.88s] English:** that actually can do the research for you. That's the idea. And then initially their prediction was  
**Translation:** 

**[10932.18s] English:** 2027, 2028. Now they've pushed it back by three to four years to 2031 mean prediction. Probably  
**Translation:** 

**[10940.90s] English:** my prediction is even beyond 2031, but at least you can in a concrete way think about how difficult  
**Translation:** 

**[10947.76s] English:** it is to fully automate programming. Yeah, I disagree with some of their presumptions and  
**Translation:** 

**[10953.86s] English:** dynamics on how it would play out. But I think they did good work in the scenario defining  
**Translation:** 

**[10960.44s] English:** milestones that are concrete and to tell a useful story, which is why the reach for this AI 2027  
**Translation:** Vocabulary: milestones: 里程碑

**[10965.20s] English:** document well transcended Silicon Valley is because they told a good story and they did a lot  
**Translation:** 

**[10971.10s] English:** of rigorous work to do this. I think the camp that I fall into is that AI is so-called jagged,  
**Translation:** Vocabulary: jagged: 参差不齐; rigorous: 严谨; transcended: 超越

**[10977.30s] English:** which is a good thing. I think that's a good thing. I think that's a good thing. I think that's a good  
**Translation:** 

**[10977.74s] English:** thing. Which will be excellent at some things and really bad at some things. I think that  
**Translation:** 

**[10981.14s] English:** when they're close to this automated software engineer, what it will be good at is that  
**Translation:** 

**[10987.10s] English:** traditional ML systems and front end, the model is excellent at, but the distributed ML,  
**Translation:** 

**[10992.18s] English:** the models are actually really quite bad at because there's so little training data on doing  
**Translation:** 

**[10995.94s] English:** large scale distributed learning and things. And this is something that we already see. And I think  
**Translation:** 

**[10999.98s] English:** this is just getting amplified. And then it's kind of messier in these trade-offs. And then there's  
**Translation:** 

**[11004.60s] English:** how do you think AI research works and so on.  
**Translation:** Vocabulary: amplified: 放大

**[11007.74s] English:** So you think basically superhuman coder is almost unachievable, meaning like because of the jagged  
**Translation:** 

**[11013.74s] English:** nature of the thing, you're just always going to have gaps in capabilities.  
**Translation:** Vocabulary: unachievable: 无法实现

**[11018.62s] English:** I think it's assigning completeness to something where the models are kind of superhuman at some  
**Translation:** 

**[11023.32s] English:** types of code. And I think that will continue and people are creative. So they'll utilize this like  
**Translation:** Vocabulary: assigning: 分配; completeness: 完整性

**[11028.12s] English:** incredible abilities and like to fill in the weaknesses of the models and move really fast.  
**Translation:** 

**[11033.48s] English:** It'll always kind of be this. I've received for a long time, this dance between  
**Translation:** 

**[11037.04s] English:** the humans are enabling this thing that the model can't do.  
**Translation:** 

**[11040.00s] English:** and the best the best ai researchers the ones that can enable this superpower and i think this  
**Translation:** Vocabulary: superpower: 超能力

**[11044.74s] English:** aligns like to what we already see i think like cloud code for building a website you can stand  
**Translation:** 

**[11049.38s] English:** up a beautiful website in a few hours or do data analysis and i don't think it's going to keep  
**Translation:** Vocabulary: aligns: 与...对齐

**[11053.60s] English:** getting better at these things it'll pick up some new code skills and stuff that'll get along the  
**Translation:** 

**[11058.42s] English:** way and kind of linking to what's happening in in big tech is like this ai 2027 report is like  
**Translation:** 

**[11066.02s] English:** it leans into the singularity idea where i think research is messy and social and largely in the  
**Translation:** 

**[11072.04s] English:** data in ways that ai models can't process but like what we do have today is really powerful and these  
**Translation:** 

**[11077.96s] English:** tech companies are all collectively buying into this with tens of billions of dollars of investment  
**Translation:** 

**[11083.06s] English:** so like we are going to get some much better version of chat gpt a much better version of  
**Translation:** 

**[11088.50s] English:** cloud code than we already have i think that it's just like hard to predict where that is going but  
**Translation:** 

**[11093.60s] English:** the like bright  
**Translation:** 

**[11095.76s] English:** clear  
**Translation:** 

**[11096.00s] English:** clarity of that future is why some of the most powerful people in the world are putting so much  
**Translation:** 

**[11099.86s] English:** money into this and i think it's just kind of small differences between like we don't actually  
**Translation:** 

**[11105.58s] English:** know what a better version of chat gpt is but also like can it automate ai research i would say  
**Translation:** Vocabulary: automate: 自动化

**[11111.42s] English:** probably not at least in this time frame like big tech is going to spend 100 billion dollars  
**Translation:** 

**[11116.86s] English:** much faster than we get a automated ai researcher that enables a ai research singularity so you  
**Translation:** Vocabulary: automated: 自动化

**[11123.00s] English:** your prediction would be what like  
**Translation:** 

**[11125.12s] English:** you  
**Translation:** 

**[11126.00s] English:** spin the wheel  
**Translation:** 

**[11127.00s] English:** if this is even a useful milestone for more than ten years out  
**Translation:** 

**[11131.00s] English:** I would say less than that on the software side  
**Translation:** 

**[11134.50s] English:** but i think longer than that on the things like research  
**Translation:** 

**[11137.64s] English:** just like for fun try to imagine a world where all software writing is fully  
**Translation:** 

**[11144.02s] English:** automated  
**Translation:** 

**[11145.34s] English:** can you imagine that world  
**Translation:** 

**[11146.78s] English:** by the end of this year the amount of software that will be automated will be so high  
**Translation:** 

**[11151.52s] English:** but it's like  
**Translation:** 

**[11152.32s] English:** it'll be the things of like you're trying to train a model with rl and you need to have  
**Translation:** 

**[11155.12s] English:** have multiple bunches of GPUs communicating with each other, that'll still be hard.  
**Translation:** 

**[11160.00s] English:** but i think it'll be much easier one of the ways to think about this so the full automation of  
**Translation:** Vocabulary: automation: 全自动化

**[11164.58s] English:** programming is just think of like lines of useful code written the fraction of that to the number  
**Translation:** 

**[11173.04s] English:** of humans in the loop so presumably there'll be for a long time humans in the loop of software  
**Translation:** Vocabulary: presumably: 大概

**[11178.54s] English:** writing is just be fewer and fewer relative to the amount of code written right and the the sc  
**Translation:** 

**[11184.88s] English:** superhuman coder i think the the presumption there is it goes to zero the number of humans in the  
**Translation:** 

**[11190.22s] English:** loop what does that world look like when the number of humans in the loop is in the hundreds  
**Translation:** 

**[11196.52s] English:** not in the hundreds of thousands i think software engineering will be driven more to system design  
**Translation:** 

**[11202.68s] English:** and goals of outcomes where i do think software is largely going to be come on i think this has  
**Translation:** 

**[11208.54s] English:** been happening over the last few weeks where people have gone from a month ago of like oh  
**Translation:** 

**[11213.06s] English:** yeah agents are kind of slop which is a  
**Translation:** 

**[11214.88s] English:** famous carpenter quote to like the what is a little bit of a meme of like the industrialization  
**Translation:** Vocabulary: carpenter: 木匠

**[11221.56s] English:** of software when anyone can just create software at their fingerprints like i do think we are  
**Translation:** 

**[11226.20s] English:** closer to that side of things and it takes direction and like understanding how the systems  
**Translation:** Vocabulary: fingerprints: 指纹

**[11231.60s] English:** work to extract that best from the language models and i think it's hard to like accept  
**Translation:** 

**[11235.66s] English:** the gravity of how much is going to change with software development and how many more people can  
**Translation:** Vocabulary: gravity: 重要性

**[11240.64s] English:** do things without ever looking at it i think what's interesting is to think about whether  
**Translation:** 

**[11244.30s] English:** these systems are going to be able to do things without ever looking at it i think what's  
**Translation:** 

**[11244.86s] English:** interesting is to think about whether these systems will be um independent like completely  
**Translation:** 

**[11247.14s] English:** independent in the sense that well i have no doubt that aladams will kind of at some point  
**Translation:** 

**[11251.94s] English:** solve coding in a sense like calculators solve calculating right so at some point humans develop  
**Translation:** 

**[11257.46s] English:** the tool that you know you never need a human to calculate that number you just type it in and  
**Translation:** Vocabulary: calculators: 计算器

**[11262.58s] English:** it's an algorithm you you can do it in a in that sense and i i think that's the same probably for  
**Translation:** 

**[11268.26s] English:** coding but the question is so i think what will happen is yeah you will just say build that  
**Translation:** Vocabulary: algorithm: 算法

**[11272.82s] English:** website it will make a very good website and it's going to be a very good website and it's going to  
**Translation:** 

**[11274.86s] English:** you maybe refine it but will it do things independently where so  
**Translation:** Vocabulary: independently: 独立地; refine: 精炼

**[11280.00s] English:** will you be still having humans asking the ai to do something like will there be a person say  
**Translation:** 

**[11286.86s] English:** build that website or will there be ai that just builds websites or something or whatever i think  
**Translation:** 

**[11292.40s] English:** using talking about building websites is the too simple it's just like there's the the problem  
**Translation:** 

**[11298.72s] English:** with websites and the problem with the web you know html and all that kind of stuff it's very  
**Translation:** 

**[11303.06s] English:** resilient to just slop it will show you slop as good as showing slop i would rather like think of  
**Translation:** 

**[11310.88s] English:** like safety critical systems like uh asking ai to end to end generate something that manages  
**Translation:** Vocabulary: resilient: 坚韧不拔

**[11318.88s] English:** logistics or manages cars a fleet of cars all that kind of stuff so end to end generates that  
**Translation:** 

**[11325.28s] English:** for you i think a more intermediate example is take something like slack or microsoft word i think  
**Translation:** 

**[11330.30s] English:** if the organizations allow it ai  
**Translation:** 

**[11333.04s] English:** could very easily implement features end to end and do a fairly good job for like things that you  
**Translation:** 

**[11339.08s] English:** want to try you want to add the new like tab and slack that you want to use and i think ai will be  
**Translation:** 

**[11344.84s] English:** able to do that pretty well actually that's a really great example how far away are we from that  
**Translation:** 

**[11348.88s] English:** like this year see i don't i don't know i don't know i don't know how bad production code bases  
**Translation:** 

**[11356.86s] English:** are but i think that within like on the order of low years a lot of people are going to be pushed  
**Translation:** 

**[11362.40s] English:** to be more  
**Translation:** 

**[11363.02s] English:** of like a designer and product manager where you have multiple of these agents that can try things  
**Translation:** 

**[11367.76s] English:** for you and they might take one to two days to implement a feature or attempt to fix a bug and  
**Translation:** 

**[11373.32s] English:** you have these dashboards which i think slack is actually a good dashboard where your agents will  
**Translation:** Vocabulary: dashboard: 监控面板; dashboards: 监控面板

**[11376.96s] English:** talk to you and you'll then give feedback but things like like i make a website it's like you  
**Translation:** 

**[11383.50s] English:** want to make a logo that's passable like i think these like cohesive design things and this style  
**Translation:** Vocabulary: cohesive: 协调一致

**[11388.92s] English:** is going to be very hard for models and deciding on what to add  
**Translation:** 

**[11393.02s] English:** at the next time i just okay so i hang out with a lot of programmers and some of them are  
**Translation:** Vocabulary: programmers: 程序员

**[11398.10s] English:** a little bit  
**Translation:** 

**[11400.00s] English:** on the skeptical side in general that's just vibe wise they're like that i just think there's a lot  
**Translation:** Vocabulary: skeptical: 怀疑的

**[11406.80s] English:** of complexity involved in adding features to complex systems like if you look at the browser  
**Translation:** 

**[11411.60s] English:** chrome if i wanted to add a feature if i wanted to have tabs as a as opposed to up top i want them on  
**Translation:** 

**[11419.92s] English:** the left side interface right yeah i think we're not is not a next year thing one of the cloud  
**Translation:** 

**[11426.62s] English:** releases this year one of their tests was we give it a piece of software and leave claude to run to  
**Translation:** Vocabulary: interface: 界面

**[11431.66s] English:** recreate it entirely and it can only almost rebuild scrap like slack from scratch just given the  
**Translation:** 

**[11437.38s] English:** parameters of the software and left in a sandbox environment scratch part i like almost better so  
**Translation:** Vocabulary: recreate: 从头创建; sandbox: 测试环境; scrap: 废料

**[11444.54s] English:** it might be that the smaller newer companies are advantaged and they're like we don't have to have  
**Translation:** 

**[11449.32s] English:** the bloat and complexity and therefore this future exists and i think this gets to the point that you  
**Translation:** Vocabulary: bloat: 臃肿; complexity: 复杂性

**[11454.88s] English:** mentioned that some people are  
**Translation:** 

**[11456.60s] English:** uh you talk to us skeptical and i think that's not because the lm can't do xyz it's because  
**Translation:** 

**[11463.00s] English:** people don't want it to do it this way some of that could be a skill issue on the human side  
**Translation:** 

**[11467.16s] English:** unfortunately we have to be honest with ourselves and some of that could be an  
**Translation:** 

**[11471.66s] English:** under specification issue so programming like you're like you're just assuming this is like  
**Translation:** 

**[11479.32s] English:** in in relationships and friendships communication type issue you're assuming the lm somehow is  
**Translation:** Vocabulary: specification: 规范说明

**[11484.86s] English:** supposed to read your mind i think this  
**Translation:** 

**[11486.58s] English:** where spec driven design is really important like you just using natural language specify like what  
**Translation:** 

**[11491.96s] English:** you want i think that's like if you talk to people at the labs they use these in their  
**Translation:** 

**[11495.70s] English:** training and production code like claude code is built with claude code and they all use these  
**Translation:** 

**[11500.82s] English:** things extensively and dario talks about how much of claude's code oh and it's like these people are  
**Translation:** 

**[11507.18s] English:** slightly ahead in terms of the capabilities they have and they probably spend on inference they  
**Translation:** Vocabulary: inference: 推断

**[11513.98s] English:** could spend 10 to 100 plus x as much as we're spending  
**Translation:** 

**[11516.58s] English:** like we're on a lowly 100 or 200 month plan like they threw  
**Translation:** 

**[11520.00s] English:** let it rip and i think that that like with the pace of progress that we have it seems like  
**Translation:** 

**[11526.64s] English:** like where a year ago we didn't have cloud code and we didn't really have reasoning models and  
**Translation:** 

**[11531.72s] English:** it's like the difference between sitting here today and what we can do with these models and  
**Translation:** 

**[11535.64s] English:** it seems like there's a lot of like there's a lot of low-hanging fruit to improve them the failure  
**Translation:** 

**[11540.60s] English:** modes are pretty dumb it's like claude you tried to use the cli command i don't have installed 14  
**Translation:** 

**[11546.98s] English:** times and then i sent you the command to run it's like that thing from a modeling perspective  
**Translation:** 

**[11551.68s] English:** is pretty fixable so i i agree with you i've been uh becoming more and more bullish in general  
**Translation:** 

**[11558.70s] English:** speaking to what you're articulating i think it is a human skill issue so anthropic is leading  
**Translation:** Vocabulary: articulating: 表达; bullish: 乐观

**[11566.06s] English:** the way in or other companies in understanding how to best use the models for programming  
**Translation:** 

**[11572.94s] English:** therefore they're effectively using them i think there's a lot of programmers and  
**Translation:** 

**[11576.70s] English:** uh  
**Translation:** 

**[11576.96s] English:** outskirts they're like they don't i mean there's not a really good guide on how to use them people  
**Translation:** Vocabulary: outskirts: 郊区

**[11583.16s] English:** trying to figure it out exactly it might be very expensive like it might be that the entry point  
**Translation:** 

**[11587.44s] English:** for that is two thousand dollars a month which is only tech companies and rich people just like  
**Translation:** 

**[11591.86s] English:** like that could be it but it might be worth it i mean if if the final result is is a working  
**Translation:** 

**[11597.40s] English:** software system well that'd be worth it but by the way it's funny how we converge from the  
**Translation:** Vocabulary: converge: 趋于一致

**[11601.58s] English:** discussion of timeline to agi to have something more pragmatic and useful is there anything  
**Translation:** 

**[11606.76s] English:** that's going to be worth it i mean i think it's going to be worth it i mean i think it's going to  
**Translation:** Vocabulary: pragmatic: 实用的

**[11606.94s] English:** concrete and interesting and useful and profound to be said about timeline to agi and asi are these  
**Translation:** 

**[11614.14s] English:** discussions a bit too detached from the day-to-day there's interesting bets so there's a lot of  
**Translation:** Vocabulary: detached: 脱离实际; profound: 深刻

**[11620.80s] English:** people trying to do reinforcement learning with verifiable rewards but in real scientific domains  
**Translation:** 

**[11625.60s] English:** where there's startups that are spending like they have hundreds of millions of dollars of  
**Translation:** Vocabulary: reinforcement: 强化; startups: 初创企业; verifiable: 可验证的

**[11628.54s] English:** funding and they have wet labs where they're having language models propose hypotheses that  
**Translation:** 

**[11633.30s] English:** are tested in the real world and i i would say that i think they're very early  
**Translation:** Vocabulary: hypotheses: 假设

**[11636.94s] English:** or they're early but with the pace of progress it's like yeah  
**Translation:** 

**[11640.00s] English:** Maybe they're early by six months and they make it because they were there first, or maybe they're early by eight years and you don't really know.  
**Translation:** 

**[11646.78s] English:** So I think that that type of moonshot to branch this momentum into other sciences is like, okay, that would be very transformative if like alpha fold moments happen in all sorts of other scientific domains by like a startup solving this.  
**Translation:** 

**[11664.96s] English:** I think there are startups, I think maybe Harmonic is one where they're going all in on language models plus lean for math.  
**Translation:** Vocabulary: alpha: 领先成果; harmonic: 谐波科技; moonshot: 大胆尝试

**[11671.28s] English:** I think you had another podcast guest where you talked about this recently.  
**Translation:** 

**[11674.34s] English:** And it's like, we don't know exactly what's going to fall out of spending $100 million on that model.  
**Translation:** 

**[11681.06s] English:** And most of them will fail, but a couple of them might be big breakthroughs that are very different than chat GPT or cloud code type software experiences.  
**Translation:** 

**[11691.36s] English:** Like a tool that's only good for a PhD mathematician.  
**Translation:** Vocabulary: breakthroughs: 重大突破; mathematician: 数学家

**[11694.96s] English:** But makes them a hundred X effective.  
**Translation:** 

**[11697.66s] English:** Like, okay, I agree.  
**Translation:** 

**[11699.16s] English:** I think this will happen in a lot of domains, especially also like domains that have a lot of, you know, resources like finance and legal and pharmaceutical companies.  
**Translation:** 

**[11710.62s] English:** But then again, is it really AGI again, because we are now specializing it again.  
**Translation:** Vocabulary: pharmaceutical: 制药

**[11714.40s] English:** And then again, is it really that much different from back in the day how we had specialized algorithms?  
**Translation:** 

**[11719.46s] English:** I think it's just the same thing, more way more sophisticated.  
**Translation:** Vocabulary: sophisticated: 复杂高级

**[11723.78s] English:** But yeah.  
**Translation:** 

**[11724.96s] English:** I don't know, is there a threshold when we call it AGI, I guess, I think the, the real cool thing is here that we have like the foundation models that we can specialize.  
**Translation:** Vocabulary: specialize: 专门化; threshold: 门槛

**[11731.84s] English:** I think that that's like the breakthrough at some point right now, I think we are not there yet because well, first it's too expensive, but also, you know, like chat GPT doesn't just give away that chat GPT to customize it.  
**Translation:** 

**[11742.84s] English:** I think once that's going to be true in some way, and I think I can imagine this as a business model that chat GPT says at some point, like, Hey, you know, bank of America for a hundred million, we will do your customer service.  
**Translation:** 

**[11754.70s] English:** You know, custom model or something like that.  
**Translation:** 

**[11756.02s] English:** And I think that will be the huge economic value add.  
**Translation:** 

**[11760.00s] English:** The other thing, though, is also companies, I mean, right now, what is the differentiating  
**Translation:** 

**[11765.88s] English:** factor?  
**Translation:** Vocabulary: differentiating: 区分因素

**[11766.46s] English:** I mean, if everyone uses the same LLM, if everyone uses ChatGPD, they will all do the  
**Translation:** 

**[11770.94s] English:** same thing again.  
**Translation:** 

**[11771.86s] English:** I mean, then, well, everyone is moving in lockstep, but usually companies, they want  
**Translation:** 

**[11776.94s] English:** to have a competitive advantage.  
**Translation:** Vocabulary: lockstep: 齐步走

**[11778.34s] English:** And I think there's no way around using some of their private data and experimenting and  
**Translation:** 

**[11783.04s] English:** maybe specializing.  
**Translation:** Vocabulary: experimenting: 实验

**[11784.62s] English:** It's going to be interesting, yeah.  
**Translation:** 

**[11786.00s] English:** But sitting in the pace of progress, it does just feel like things are coming.  
**Translation:** 

**[11790.20s] English:** I don't think the AGI and ASI thresholds are particularly useful.  
**Translation:** 

**[11795.86s] English:** I think, I guess, the real question, and this takes us to the remote worker thing, is when  
**Translation:** Vocabulary: thresholds: 门槛

**[11801.26s] English:** are we going to see a big, obvious leap in economic impact?  
**Translation:** 

**[11807.86s] English:** Because currently, there's not been an obvious leap in economic impact of LLM models, for  
**Translation:** 

**[11813.82s] English:** example.  
**Translation:** 

**[11814.16s] English:** And that's, you know, aside from AGI or ASI or all that kind of stuff, there's a real  
**Translation:** 

**[11820.70s] English:** question of, like, when are we going to see a GDP, like, jump?  
**Translation:** 

**[11826.28s] English:** Yeah, it's like, what is the GDP made up of?  
**Translation:** 

**[11828.52s] English:** Like, a lot of it is, like, financial services.  
**Translation:** 

**[11830.88s] English:** So, like, I don't know what this is.  
**Translation:** 

**[11833.68s] English:** It's just hard for me to think about the GDP bump.  
**Translation:** 

**[11837.16s] English:** But, like, I'd say that software development becomes valuable in a different way when you  
**Translation:** 

**[11843.20s] English:** no longer have to look at the data.  
**Translation:** 

**[11844.12s] English:** You don't have to look at the code anymore.  
**Translation:** 

**[11845.68s] English:** So, when it is, like, cloud will make you a small business, which is essentially cloud  
**Translation:** 

**[11850.84s] English:** can set up your website, your bank account, your email, and your whatever else.  
**Translation:** 

**[11854.42s] English:** And, like, you just have to express, like, what you're trying to put into the world.  
**Translation:** 

**[11859.04s] English:** Like, that's not just an enterprise market, but it is a hard, like, I don't know how you  
**Translation:** 

**[11864.16s] English:** get people to try doing that.  
**Translation:** 

**[11865.62s] English:** I guess if ChatGPT can do it, like, people are trying ChatGPT.  
**Translation:** 

**[11868.74s] English:** I think it boils down to the scientific question of how hard is tool use to solve?  
**Translation:** 

**[11874.12s] English:** Because a lot of the stuff you're applying, the remote work stuff is tool use.  
**Translation:** 

**[11879.68s] English:** It's a...  
**Translation:** 

**[11880.00s] English:** Like how computer use,  
**Translation:** 

**[11881.52s] English:** like how you have an LLM that goes out there,  
**Translation:** 

**[11885.02s] English:** this agentic system and does something in the world and only screws up 1% of  
**Translation:** 

**[11890.88s] English:** the time.  
**Translation:** 

**[11891.78s] English:** Computer use is a good example of what labs care about.  
**Translation:** 

**[11894.86s] English:** And we haven't seen a lot of progress on,  
**Translation:** 

**[11896.28s] English:** we saw multiple demos and 2025 of like,  
**Translation:** Vocabulary: demos: 演示

**[11899.94s] English:** Claude can use your computer or open AI had Kua and they all suck.  
**Translation:** 

**[11904.64s] English:** So like they're also investing money in this.  
**Translation:** 

**[11907.44s] English:** And I think that will be a good example where that's actually,  
**Translation:** 

**[11909.82s] English:** something where it just seems pretty like taking over the whole screen  
**Translation:** 

**[11914.92s] English:** seems a lot harder than having an API that they can call on the backend.  
**Translation:** 

**[11919.56s] English:** And some of that is you have to then set up a different environment for the  
**Translation:** 

**[11922.26s] English:** model to work in.  
**Translation:** 

**[11923.14s] English:** Like they're not working on your Mac book.  
**Translation:** 

**[11925.18s] English:** They are individually interfacing with Google and Amazon and Slack,  
**Translation:** 

**[11930.10s] English:** and they handle all of these things in a very different way than humans do.  
**Translation:** Vocabulary: individually: 单独; interfacing: 对接

**[11933.18s] English:** So some of those might be structural blockers.  
**Translation:** 

**[11936.06s] English:** Also like specification wise,  
**Translation:** Vocabulary: specification: 技术规范

**[11937.44s] English:** I think the problem is also for,  
**Translation:** 

**[11939.82s] English:** you know,  
**Translation:** 

**[11940.38s] English:** arbitrary tasks while you still have to specify what you want your LLM to do.  
**Translation:** 

**[11944.26s] English:** And how do you do that in a,  
**Translation:** Vocabulary: arbitrary: 随意的

**[11945.46s] English:** what is the environment?  
**Translation:** 

**[11947.74s] English:** How do you specify,  
**Translation:** 

**[11948.72s] English:** you can say what the end goal is,  
**Translation:** 

**[11950.06s] English:** but if it can't solve the end goal with LLMs,  
**Translation:** 

**[11953.98s] English:** if you ask it for text,  
**Translation:** 

**[11955.00s] English:** you can always clarify,  
**Translation:** 

**[11956.42s] English:** do sub steps.  
**Translation:** 

**[11957.36s] English:** What is,  
**Translation:** 

**[11958.00s] English:** how do you put that information into a system that let's say books,  
**Translation:** 

**[11961.52s] English:** a travel trip for you,  
**Translation:** 

**[11962.38s] English:** you can say,  
**Translation:** 

**[11962.74s] English:** well,  
**Translation:** 

**[11962.92s] English:** you screwed up my credit card information,  
**Translation:** 

**[11964.46s] English:** but even to get it to that point,  
**Translation:** 

**[11966.82s] English:** like how do you like as a user,  
**Translation:** 

**[11969.82s] English:** guide the model before like it can even attempt that.  
**Translation:** 

**[11973.90s] English:** I think the interface is really hard.  
**Translation:** 

**[11975.94s] English:** Yeah.  
**Translation:** Vocabulary: interface: 用户界面

**[11976.14s] English:** It has to learn a lot about you specifically and about this goes to continue to continue learning about the general mistakes that are made throughout and then mistakes that are made through you.  
**Translation:** 

**[11988.28s] English:** All the AI interfaces are getting set up to ask humans for input.  
**Translation:** Vocabulary: interfaces: 人机接口

**[11992.48s] English:** I think cloud code,  
**Translation:** 

**[11993.16s] English:** we talk about a lot.  
**Translation:** 

**[11993.98s] English:** It asks feedback on questions.  
**Translation:** 

**[11995.52s] English:** If it doesn't have enough specification on your plan or your desired,  
**Translation:** 

**[11998.58s] English:** it starts to ask questions.  
**Translation:** 

**[11999.78s] English:** Would you?  
**Translation:** 

**[12000.00s] English:** rather um we talked about memory which saves across chats which it's first implementation  
**Translation:** 

**[12006.96s] English:** is kind of odd where it'd be like it'll mention my dog's name or something like in a chat i'm like  
**Translation:** Vocabulary: implementation: 实施方式

**[12012.18s] English:** you didn't need to be subtle about this like i don't care but the like things that are emerging  
**Translation:** 

**[12016.38s] English:** our chat gpt has the pulse feature which is like um a curated couple paragraphs with links to  
**Translation:** 

**[12023.44s] English:** something to look at or to talk about and people talk about how the language models are going to  
**Translation:** 

**[12027.26s] English:** ask you questions which i think is a very it's probably going to work the language model is like  
**Translation:** 

**[12033.60s] English:** it knows you had a doctor appointment or something it's like hey how are you feeling after that which  
**Translation:** 

**[12037.94s] English:** is like um again goes into the territory of humans are very susceptible to this and there's a lot of  
**Translation:** Vocabulary: susceptible: 易受影响的

**[12043.46s] English:** social change to come but also like they're experimenting with having the models engage  
**Translation:** 

**[12048.44s] English:** some people really like this pulse feature which is it processes your chats and automatically  
**Translation:** Vocabulary: experimenting: 尝试

**[12052.94s] English:** searches for information and puts it in the chat gpt app  
**Translation:** 

**[12056.28s] English:** so there's a lot of things coming i used that feature before and i always feel bad because  
**Translation:** 

**[12062.00s] English:** it does that every day and i rarely check it out it's like how much money like i mean  
**Translation:** 

**[12067.08s] English:** compute is burned on something i don't even look at you know where it's like  
**Translation:** 

**[12071.18s] English:** it's kind of there's also a lot of idle compute in the world so don't feel too bad  
**Translation:** 

**[12074.74s] English:** okay do you think uh new ideas might be needed is it possible that the path to agi  
**Translation:** 

**[12082.60s] English:** whatever that is however we define that to solve computer use more  
**Translation:** 

**[12086.28s] English:** more generally to solve biology and chemistry and physics sort of the dario definition of agi or  
**Translation:** 

**[12095.42s] English:** powerful yeah do you think it's possible that totally new ideas are needed non-llm non-rl  
**Translation:** 

**[12102.36s] English:** ideas what might they look like this is we're not going into philosophy land a little bit  
**Translation:** 

**[12109.76s] English:** for something like a singularity to happen i would say yes and the new ideas could be  
**Translation:** 

**[12116.28s] English:** or training algorithms which is like fundamental deep learning  
**Translation:** 

**[12120.00s] English:** things but they're in that nature pretty hard to predict and i but i think we won't get very far  
**Translation:** 

**[12126.50s] English:** even without those advances like we might get this software solution but it might stop at software  
**Translation:** 

**[12132.66s] English:** and not do computer use without more innovation so i think that it's like a lot of progress will  
**Translation:** 

**[12137.68s] English:** be coming but in if you're going to zoom out like there are still ideas in the next 30 years that  
**Translation:** 

**[12142.94s] English:** are going to look like that was a major like scientific innovation that enabled the next  
**Translation:** 

**[12148.88s] English:** chapter of this and i don't know if it comes in one year or in 15 years yeah i wonder if the  
**Translation:** 

**[12153.78s] English:** bitter lesson holds true for the next 100 years what that looks like if scaling laws are fundamental  
**Translation:** 

**[12159.26s] English:** and deep learning i think the bitter lesson will always apply which is compute will become more  
**Translation:** 

**[12164.62s] English:** abundant but even within abundant compute the ones that have a steeper scaling law slope or  
**Translation:** 

**[12172.06s] English:** a better offset like this is a 2d plot of performance and compute and like even if  
**Translation:** 

**[12177.14s] English:** there's more compute available the ones that  
**Translation:** 

**[12178.86s] English:** get 100x out of it will win it might be something like literally compute clusters orbiting earth  
**Translation:** Vocabulary: clusters: 计算集群; orbiting: 绕地球运行

**[12186.00s] English:** with solar panels the problem with that is heat dissipation so you get all the radiation from the  
**Translation:** 

**[12192.88s] English:** sun and you don't have any air to dissipate heat but there is a lot of space to put clusters there's  
**Translation:** Vocabulary: dissipate: 散发; dissipation: 散发

**[12197.68s] English:** a lot of solar energy there and you could figure out the heat dissipation but there is a lot of  
**Translation:** 

**[12201.96s] English:** energy and there probably could be engineering will to solve the heat problem so there could be  
**Translation:** 

**[12206.76s] English:** is it possible and we should be able to do that in the future i think it's a good idea to do that  
**Translation:** 

**[12208.86s] English:** i should say that it definitely is possible how likely it is uh is the question that we're  
**Translation:** 

**[12213.98s] English:** basically going to be plateauing this year not in terms of the system capabilities but what  
**Translation:** 

**[12220.58s] English:** the system capabilities actually mean for human civilization so on the coding front really nice  
**Translation:** Vocabulary: plateauing: 停滞不前

**[12227.56s] English:** websites will be built uh very nice autocomplete very nice uh way to understand code bases and  
**Translation:** 

**[12237.96s] English:** maybe help the  
**Translation:** Vocabulary: autocomplete: 自动完成

**[12238.86s] English:** but  
**Translation:** 

**[12240.00s] English:** really just a very nice helper on the coding front it can help research mathematicians do some math  
**Translation:** Vocabulary: mathematicians: 数学家

**[12246.38s] English:** it can help you with shopping it can help you it can help it's a nice helper it's clippy on  
**Translation:** 

**[12252.32s] English:** steroids uh what else it may be a good education tool and all that kind of stuff but computer use  
**Translation:** Vocabulary: steroids: 增强版

**[12261.44s] English:** turns out extremely difficult to solve so i'm trying to be i'm trying to frame the cynical  
**Translation:** 

**[12267.52s] English:** case in all these domains where it kind of there's not a really huge economic impact  
**Translation:** Vocabulary: cynical: 怀疑论的

**[12273.02s] English:** we realize how costly it is to train these systems at every level both the pre-training  
**Translation:** 

**[12278.38s] English:** on the inference how costly the inference is the reasoning all of that uh like is that possible  
**Translation:** 

**[12285.66s] English:** and how likely is that do you think when you look at the models there's so much obvious things to  
**Translation:** 

**[12290.60s] English:** improve and it takes a long time to train these models and to do this art and that it'll take us  
**Translation:** 

**[12297.52s] English:** ideas that we have multiple years to actually saturate in terms of whatever benchmark or  
**Translation:** 

**[12303.36s] English:** performance we are searching for it might serve very narrow niches like the average  
**Translation:** Vocabulary: benchmark: 衡量标准; niches: 细分市场

**[12308.68s] English:** chat gpt 800 million user might not get a lot of benefit out of this but it is going to serve  
**Translation:** 

**[12314.08s] English:** different populations by getting better at different things well i get i think what  
**Translation:** 

**[12319.32s] English:** everybody's chasing now is the is a general system that's useful to everybody so okay so  
**Translation:** 

**[12325.56s] English:** if that's not that can plateau  
**Translation:** Vocabulary: plateau: 平台期

**[12327.52s] English:** right i think that dream is actually kind of dying as you talked about the specialized models where  
**Translation:** 

**[12332.92s] English:** it's like and multimodal is often like video generation is a totally different thing that  
**Translation:** Vocabulary: multimodal: 多模态的

**[12339.18s] English:** dream is kind of dying is a big statement because i don't know if it's dying i don't know if every  
**Translation:** 

**[12344.30s] English:** i don't if you ask the actual frontier lab people they i mean they're still chasing it right i do  
**Translation:** Vocabulary: frontier: 前沿

**[12348.66s] English:** think they are still like rushing to get the next model out which will be much better than the  
**Translation:** 

**[12353.70s] English:** much is a relative term but will be better than the previous one  
**Translation:** 

**[12357.52s] English:** and i i can't see them slowing down  
**Translation:** 

**[12360.00s] English:** just think the gains will be made or felt more through not only scaling the model but now fine  
**Translation:** 

**[12368.08s] English:** so i feel like there's a lot of tech debt it's like well let's just put the better model in there  
**Translation:** 

**[12372.68s] English:** and better model and better model and now people are okay let's also at the same time improve  
**Translation:** 

**[12378.48s] English:** everything around it too like you know like the engineering of the context and inference scaling  
**Translation:** 

**[12383.38s] English:** and i the big labs will still keep doing that and now also the smaller labs will catch up to that  
**Translation:** Vocabulary: inference: 推断

**[12388.70s] English:** because now it's just like they are hiring more there will be more people llms it's kind of like  
**Translation:** 

**[12393.26s] English:** you know like a circle they also make them more productive and it's just it's like amplify i think  
**Translation:** 

**[12398.92s] English:** what we can expect is amplification but not like a change of like a paradigm change i don't think  
**Translation:** 

**[12404.72s] English:** that is true but everything will be just amplified and amplified and amplified and i can see that  
**Translation:** Vocabulary: amplification: 放大; amplified: 被放大

**[12409.94s] English:** continuing for a long time you know yeah i guess my statement with the dream is dying depends on  
**Translation:** 

**[12415.24s] English:** exactly what you think it's going to be doing like cod code is  
**Translation:** 

**[12418.64s] English:** a dream  
**Translation:** 

**[12418.68s] English:** a general model that can do a lot of things but it's not like necessarily like it depends a lot  
**Translation:** 

**[12425.92s] English:** on integrations and other things like i bet cod code can do a fairly good job of doing your email  
**Translation:** 

**[12430.00s] English:** and the hardest part is figuring out how to give the information to it and how to get it to be able  
**Translation:** Vocabulary: integrations: 集成

**[12434.62s] English:** to send your emails and stuff like this but that's just kind of like i think it goes back to like  
**Translation:** 

**[12439.72s] English:** what is the one model to rule everything ethos which is just like a thing in the cloud that  
**Translation:** Vocabulary: ethos: 理念

**[12446.02s] English:** handles your entire digital life and  
**Translation:** 

**[12448.62s] English:** is way smarter than everybody it's like it's operating in a so it's an interesting leap of  
**Translation:** 

**[12456.16s] English:** faith to go from cod code becomes that which is like in some ways is there's some avenues for that  
**Translation:** 

**[12464.40s] English:** but i do think that like the rhetoric of the industry is a little bit different i think the  
**Translation:** Vocabulary: rhetoric: 言辞

**[12470.04s] English:** immediate also thing we will feel next as a normal person using adams as well will probably be  
**Translation:** 

**[12475.20s] English:** related to something like also trivial like making figures a  
**Translation:** 

**[12478.62s] English:** little bit more complicated and i think that's something that's going to be a little bit more  
**Translation:** 

**[12480.00s] English:** at making figures is it because we are getting served the cheap models with very less like less  
**Translation:** 

**[12486.36s] English:** inference compute than behind the scenes maybe some like there are some cranks we can already  
**Translation:** 

**[12491.58s] English:** get better figures but if you ask today i don't draw a flow chart of xyz it's most of the time  
**Translation:** Vocabulary: cranks: 怪人

**[12497.88s] English:** terrible and it is kind of like a very simple task for a human i think it's almost easier sometimes  
**Translation:** 

**[12502.92s] English:** to draw something than to write something yeah the multimodal understanding does feel like something  
**Translation:** Vocabulary: multimodal: 多模态的

**[12507.64s] English:** that is odd that it's not better solved i think we're not saying one actually obvious thing that  
**Translation:** 

**[12513.64s] English:** we're not actually realizing that's a gigantic thing that's hard to measure which is making all  
**Translation:** Vocabulary: gigantic: 巨大的

**[12518.98s] English:** of human knowledge accessible to the entire world like we i don't i one of the things i think  
**Translation:** 

**[12526.00s] English:** it's hard to articulate but there's just a huge difference between google search  
**Translation:** Vocabulary: articulate: 表达清楚

**[12531.38s] English:** and an llm like i feel like i can basically ask an llm anything  
**Translation:** 

**[12537.46s] English:** anything  
**Translation:** 

**[12537.62s] English:** anything  
**Translation:** 

**[12537.64s] English:** and get an answer and less it's doing less and less and less hallucination and that means  
**Translation:** Vocabulary: hallucination: 幻觉

**[12545.22s] English:** understanding my own life figuring out a career trajectory figuring out how to solve the problems  
**Translation:** 

**[12551.64s] English:** all around me uh learn about anything through human history that like i feel like nobody's  
**Translation:** Vocabulary: trajectory: 职业路径

**[12559.50s] English:** really talking about that because they just immediately take it for granted that it's just  
**Translation:** 

**[12565.26s] English:** this is awesome that's why everybody's using it  
**Translation:** 

**[12567.62s] English:** it's because you get answers for stuff and like the impact of that across time like think about  
**Translation:** 

**[12573.88s] English:** this is not just in the united states it's all across the world like kids throughout the world  
**Translation:** 

**[12580.02s] English:** being able to learn these ideas like the impact that has across time is probably that's where the  
**Translation:** 

**[12587.84s] English:** real like talking about gdp it won't be like a leap it'll be that's how we get to mars that's  
**Translation:** 

**[12594.02s] English:** how we build these things that's how we have a million new open ai  
**Translation:** 

**[12597.60s] English:** all the kind of innovation that happens  
**Translation:** 

**[12600.00s] English:** us from there and that's just this quiet force that permeates everything right human knowledge  
**Translation:** 

**[12605.80s] English:** i do agree with you and in a sense uh you make it makes knowledge more accessible but  
**Translation:** Vocabulary: permeates: 渗透

**[12611.84s] English:** um it also i think depends on what the topic is for something like math um in a sense you can ask  
**Translation:** 

**[12619.14s] English:** it questions it answers but if you want to learn a topic from scratch uh i think that again like  
**Translation:** 

**[12626.04s] English:** we talked about this earlier i think the sweet spot is i mean there are really good math textbooks  
**Translation:** 

**[12630.94s] English:** where someone laid it out linearly and that is like a let's say proven strategy to learn this  
**Translation:** 

**[12635.92s] English:** topic and it does make sense if you start from zero to ramp up to get like a like a information  
**Translation:** 

**[12642.20s] English:** dense text to soak it up but then you use the llm to make infinite exercises like you you have  
**Translation:** 

**[12648.20s] English:** problems in a certain area and i have questions something's uncertain or like you are uncertain  
**Translation:** 

**[12653.20s] English:** about certain things you ask it to generate  
**Translation:** 

**[12655.90s] English:** eternity  
**Translation:** 

**[12656.04s] English:** example problems you solve them and you have questions and then maybe you need you need more  
**Translation:** 

**[12660.56s] English:** background knowledge and you ask it to to generate that and i think but then the it won't give you  
**Translation:** 

**[12666.76s] English:** anything let's say that is not in the the textbook it's just packaging it differently if that makes  
**Translation:** 

**[12672.90s] English:** sense but then there are things i feel like where it also adds value in a more i mean timely sense  
**Translation:** 

**[12680.02s] English:** where there is no good alternative besides a human doing it on the fly for example if you  
**Translation:** 

**[12685.24s] English:** i don't like let's say you're planning to go to disneyland and you try to figure out which tickets  
**Translation:** 

**[12689.70s] English:** to buy for which park when well there is no textbook on that there is no information dense  
**Translation:** Vocabulary: disneyland: 迪斯尼乐园

**[12695.88s] English:** resource and that there's only the sparse internet and then there is a lot of value in the llm you  
**Translation:** 

**[12701.06s] English:** just ask it it has you have the constraints i'm traveling these and these days i want to go there  
**Translation:** Vocabulary: constraints: 限制; sparse: 稀少

**[12705.24s] English:** and there please figure out what i need when and from where what what it costs and  
**Translation:** 

**[12710.00s] English:** stuff like that and it is very customized on the fly uh package and then this is like  
**Translation:** 

**[12716.78s] English:** one of the thousand examples and exercise personalized  
**Translation:** 

**[12720.00s] English:** personalization is essentially like pulling information from the sparse internet the  
**Translation:** 

**[12725.08s] English:** non-information dense thing where there is no better version that exists it just doesn't exist  
**Translation:** 

**[12730.44s] English:** you make it from scratch almost and if it does exist it's full of uh speaking of disney world  
**Translation:** 

**[12735.68s] English:** like full of what would you call it ad slop like you just it's impossible uh here you go  
**Translation:** 

**[12742.50s] English:** any city in the world what are the top 10 things to do lm is just way better to ask than anything  
**Translation:** 

**[12749.54s] English:** for now that's because they're massively subsidized and they're going to be paid for by  
**Translation:** 

**[12754.06s] English:** ads it's coming oh i hope they're i mean i'm hoping there's a very clear indication what's  
**Translation:** Vocabulary: massively: 大规模地

**[12764.18s] English:** an ad and what's not in that context i did a little you know that's something i mentioned  
**Translation:** 

**[12767.80s] English:** a few years ago it's like uh i don't know if you're looking for a new running shoe mom is  
**Translation:** 

**[12773.90s] English:** this a coincidence that nike maybe comes up first maybe maybe not and but i think there are clear  
**Translation:** 

**[12779.54s] English:** laws around this you have to be clear about that but i think that's what everyone fears it's like  
**Translation:** Vocabulary: coincidence: 偶然性

**[12783.78s] English:** the subtle um you know subtle message in there or something like that but it also brings us to  
**Translation:** 

**[12789.66s] English:** the topic of i guess ads uh where i think this was the thing hope may i try to launch in 2025  
**Translation:** 

**[12795.56s] English:** and uh just to because i think it's still not uh making money in that other way right now so that  
**Translation:** 

**[12802.32s] English:** like having really like ad spots in there and then the thing though is they couldn't because well  
**Translation:** 

**[12809.54s] English:** ads and people would just flock to the other products and it also is just like crazy how  
**Translation:** 

**[12815.34s] English:** yeah like they're one upping each other spending so much money to just get the users i think so  
**Translation:** 

**[12822.12s] English:** like some instagram ads i don't use instagram but i understand the appeal of paying a platform  
**Translation:** 

**[12829.56s] English:** to find users who will genuinely like your product and that is the best case of things  
**Translation:** 

**[12835.06s] English:** like instagram ads but there are also plenty of cases where advertising is very  
**Translation:** 

**[12839.54s] English:** awful for  
**Translation:** 

**[12840.00s] English:** incentives and i think that a world where the power of ai can integrate with that positive  
**Translation:** 

**[12845.86s] English:** view of like i am a person and i have a small business and i want to make the best i don't  
**Translation:** Vocabulary: incentives: 激励措施; integrate: 整合

**[12851.74s] English:** know damn steak knives in the world and i want to sell them to somebody who needs them and if like  
**Translation:** 

**[12857.02s] English:** if ai can make that sort of advertising thing work even better that's very good for the world  
**Translation:** 

**[12861.54s] English:** especially with like digital infrastructure because that's how like the modern web has  
**Translation:** 

**[12866.74s] English:** been built but that's not to say like addicting feeds so that you can show people more content  
**Translation:** Vocabulary: addicting: 令人上瘾的

**[12873.92s] English:** is a good thing so it's like i think that's even what opening i would say is they want to find a  
**Translation:** 

**[12878.76s] English:** way that can make the monetization upside of ads while still giving their users agency and i'm i  
**Translation:** Vocabulary: monetization: 盈利模式; upside: 好处

**[12885.56s] English:** personally would think that google is probably going to be better at figuring out how to do this  
**Translation:** 

**[12889.52s] English:** because they have they already have ad supply and they figure out how to turn this demand in their  
**Translation:** 

**[12895.80s] English:** gemini app  
**Translation:** 

**[12896.54s] English:** into useful ads then they can turn it on and somebody will figure i don't know if i think  
**Translation:** Vocabulary: gemini: 双子座

**[12902.96s] English:** it's this year but there will be experiments with it i do think what holds companies back  
**Translation:** 

**[12908.12s] English:** right now is really just that the competition is not doing it it's more like more like a  
**Translation:** 

**[12912.70s] English:** reputation thing it's just like i think people are just afraid right now like ruining or like  
**Translation:** 

**[12917.74s] English:** losing the reputation losing users because it is it would make headlines if someone launched  
**Translation:** 

**[12922.22s] English:** these ads unless they were great but the first ads won't be great because it's a hard problem  
**Translation:** 

**[12926.52s] English:** that we don't know how to solve yeah i think also the first version of that will likely be something  
**Translation:** 

**[12930.82s] English:** like on x like the timeline where you have like a promoted post sometimes in between it will be  
**Translation:** 

**[12935.72s] English:** something like that where it will say like promoted or something like small and then there  
**Translation:** 

**[12939.26s] English:** will be an image or something i think right now the problem is who makes the first move if we go  
**Translation:** 

**[12943.34s] English:** 10 years out the proposition for ads is that you will make so much money on ads by having so many  
**Translation:** 

**[12949.48s] English:** users that you can use this to funnel better r&d and make better models which is why like youtube  
**Translation:** 

**[12955.24s] English:** is dominating the  
**Translation:** Vocabulary: dominating: 占据主导; funnel: 引导流量

**[12956.52s] English:** market for any like netflix is scared of you  
**Translation:** 

**[12960.00s] English:** like they have the ad like they make i don't i pay 28 a month for premium they make at least  
**Translation:** Vocabulary: premium: 高级会员

**[12965.44s] English:** 28 a month off of me and many other people and they're just like creating such a dominant  
**Translation:** 

**[12971.38s] English:** position in video so i think that's the proposition which is that ads can make you  
**Translation:** 

**[12976.20s] English:** have a sustained advantage in what you're spending per user but there's so much money  
**Translation:** 

**[12981.90s] English:** in it right now that it's like like somebody starting that flywheel is scary because it's  
**Translation:** Vocabulary: flywheel: 飞轮效应

**[12987.04s] English:** a long-term bet uh do you think there'll be some like crazy big moves this year business wise  
**Translation:** 

**[12994.04s] English:** like somebody like google or apple acquiring anthropic or something like this dario will  
**Translation:** 

**[13000.62s] English:** never sell but we are starting to see some types of consolidation with like grok for 20 billion  
**Translation:** 

**[13006.02s] English:** dollars and um scale ai for almost 30 billion and countless other deals like this that they're  
**Translation:** Vocabulary: consolidation: 合并

**[13013.04s] English:** structured in a way that is actually detrimental to the silicon valley  
**Translation:** 

**[13017.02s] English:** ecosystem which is this sort of licensing deal where not everybody gets brought along rather  
**Translation:** 

**[13022.42s] English:** than a full acquisition that benefits the rank and file employee by getting their stock vested  
**Translation:** 

**[13027.22s] English:** like that's a big issue for silicon valley culture to address because the startup ecosystem is  
**Translation:** Vocabulary: vested: 已归属的权益

**[13031.96s] English:** the lifeblood where if you get a if you join a startup even if it's not that successful your  
**Translation:** 

**[13038.14s] English:** startup very well might get acquired on a cheap premium of it and you'll get paid out for this  
**Translation:** Vocabulary: lifeblood: 生命线

**[13043.80s] English:** equity and these licensing deals are essentially taking the top talent  
**Translation:** 

**[13047.02s] English:** a lot of the times i think grok the deal for grok to nvidia is rumored to be better to the  
**Translation:** 

**[13052.06s] English:** employees but it is still this antitrust avoiding thing but i think that this trend of consolidation  
**Translation:** 

**[13058.60s] English:** will continue i've been me and many smart people i respect have been expecting consolidation to  
**Translation:** Vocabulary: antitrust: 反垄断

**[13064.20s] English:** have happened sooner but it seems like some of these things are starting to turn which  
**Translation:** 

**[13069.64s] English:** but at the same time you have companies raising ridiculous amounts of money for  
**Translation:** 

**[13073.76s] English:** reasons that you don't like i'm like i don't  
**Translation:** 

**[13077.02s] English:** know why you're taking that money so it's  
**Translation:** 

**[13080.00s] English:** maybe like mixed this year but some consolidation pressure is starting what kind of surprising  
**Translation:** 

**[13085.58s] English:** consolidation do you think we'll see so you say it's an anthropic is a never i mean grok is a  
**Translation:** 

**[13090.52s] English:** big one grok with a q by the way yeah there's just a lot of startups and there's a very high  
**Translation:** 

**[13095.86s] English:** premium on ai startups so there's a lot of like there could be a lot of stuff 10 billion range  
**Translation:** Vocabulary: premium: 高需求; startups: 初创公司

**[13100.36s] English:** acquisitions which is a really big acquisition for a startup that was maybe founded a year like  
**Translation:** 

**[13105.50s] English:** a year ago i think manis ai from this company that's based in singapore that meta founded was  
**Translation:** 

**[13110.60s] English:** founded eight months ago and then had a two billion dollar exit and i think that there will  
**Translation:** 

**[13114.60s] English:** be some other big like many billion dollar acquisitions like perplex yeah people rumored  
**Translation:** Vocabulary: acquisitions: 收购

**[13121.30s] English:** them to apple i think there's a lot of pressure and liquidity in ai there's pressure on big  
**Translation:** 

**[13127.76s] English:** companies to have outcomes and i would guess that a big acquisition gives people leeway to then tell  
**Translation:** Vocabulary: leeway: 余地; liquidity: 流动性

**[13134.52s] English:** the next chapter but  
**Translation:** 

**[13135.50s] English:** story i mean yeah there's a i guess cursor we've been talking about code and somebody acquires  
**Translation:** Vocabulary: acquires: 获得

**[13140.88s] English:** cursor they're in such a good position by having so much user data yeah and we talked about  
**Translation:** 

**[13146.50s] English:** continual learning and stuff they had one of the most interesting like two sentences in a blog post  
**Translation:** Vocabulary: continual: 连续的

**[13150.40s] English:** which is that they had their new composer model which was a fine tune of one of these large  
**Translation:** 

**[13155.34s] English:** mixture of expert models from china you can know that by asking gossip or because the model  
**Translation:** 

**[13160.90s] English:** sometimes responds in chinese which none of the american models do and they had a blog  
**Translation:** 

**[13165.50s] English:** post where they're like we're updating the model weights every 90 minutes based on real world  
**Translation:** 

**[13169.62s] English:** feedback from people using it which is like the closest thing to real world rl happening on a  
**Translation:** 

**[13174.86s] English:** model and it's just like in one of their blog posts which is super cool and by the way i should  
**Translation:** 

**[13178.86s] English:** say i use composer a lot because one of the benefits it has is it's fast i need to try it  
**Translation:** 

**[13183.94s] English:** because everybody says this and there'll be some ipos potentially you think anthropic open ai  
**Translation:** 

**[13189.30s] English:** xai they can all raise so much money so easily that they don't feel a need to like so a lot of  
**Translation:** 

**[13195.50s] English:** people don't feel like they're going to be able to do it as long as fundraising is easy they're  
**Translation:** Vocabulary: fundraising: 筹款

**[13199.62s] English:** not going to ipo because public markets apply pressure  
**Translation:** 

**[13200.00s] English:** I think we're seeing in China that the ecosystem is a little different with both Minimax and Z.AI applying for filing IPO paperwork, which will be interesting to see how the Chinese market reacts.  
**Translation:** Vocabulary: minimax: 最小最大

**[13211.20s] English:** I actually would guess that it's going to be similarly hype-y to the U.S. so long as all this is going and not based on the realities that they're both losing a ton of money.  
**Translation:** 

**[13221.26s] English:** I wish more of the American gigantic AI startups were public because it would be very interesting to see how they're spending their money and have more insight.  
**Translation:** Vocabulary: gigantic: 巨大的; startups: 初创公司

**[13228.28s] English:** And also just to give people access to investing in these because I think that they're the companies of the era and the tradition is now for so many of the big startups in the U.S. to not go public.  
**Translation:** 

**[13243.38s] English:** It's like we're still rating for Stripe and the IPO, but Databricks definitely didn't.  
**Translation:** Vocabulary: databricks: 数据湖公司

**[13247.22s] English:** They raised like a Series G or something.  
**Translation:** 

**[13250.62s] English:** And I just feel like it's a kind of a weird equilibrium for the market where it's like, I would like to see these companies go public.  
**Translation:** Vocabulary: equilibrium: 平衡状态

**[13258.28s] English:** And evolve in that way that a company can.  
**Translation:** 

**[13261.36s] English:** You think 10 years from now, some of the frontier model companies are still around?  
**Translation:** Vocabulary: frontier: 前沿

**[13266.70s] English:** Anthropic, OpenAI?  
**Translation:** 

**[13268.00s] English:** I definitely don't see it to be a winner-takes-all unless there truly is.  
**Translation:** 

**[13272.86s] English:** So algorithmic secret that one of them finds, like let's just flywheel.  
**Translation:** 

**[13276.72s] English:** Because the development path is so similar for all of them.  
**Translation:** Vocabulary: algorithmic: 算法; flywheel: 飞轮

**[13279.92s] English:** Google and OpenAI have like all the same products and then like Anthropic's more focused.  
**Translation:** 

**[13284.48s] English:** But when you talk to people, it sounds like they're solving a lot of the same problems.  
**Translation:** 

**[13288.28s] English:** So I think, and there's offerings that'll spread out.  
**Translation:** 

**[13291.34s] English:** There's a lot of, it's a very big cake that's being made that people are going to take money out of.  
**Translation:** 

**[13296.38s] English:** I don't want to trivialize it, but so OpenAI and Anthropic are primarily LLM service providers.  
**Translation:** 

**[13304.44s] English:** And some of the other companies like Google and XAI, linked to X, does other stuff too.  
**Translation:** Vocabulary: trivialize: 轻描淡写

**[13311.90s] English:** And so it's very possible if AI becomes more commodified, that the companies that are just providing,  
**Translation:** 

**[13318.28s] English:** LLM, will die.  
**Translation:** Vocabulary: commodified: 商品化

**[13320.00s] English:** I think they will the advantage they have they have a lot of users and I think they will just pivot I think then if they figure out it's like anthropic I think pivoted I don't think they originally plan to work on code but it happened that they found okay this is like a nice niche and now we are comfortable in this niche and we push on this niche and I can see the same thing once maybe let's say hypothetically speaking I'm not sure it will be true but let's say Google takes all the market share of the general chatbot maybe open I will be then  
**Translation:** 

**[13349.10s] English:** focused on some other topic like the they have too many users to go away and foreseeable future I think I think Google is always ready to say hold my beer with AI mode I think that the question is if the companies can support the valuations I think I'd see the AI companies being looked at in some ways like AWS Azure and GCP are all competing in the same space and all very successful businesses there's a chance that the API market is so unprofitable that  
**Translation:** Vocabulary: foreseeable: 可预见的; hypothetically: 假设性; niche: 细分市场; pivoted: 转向; unprofitable: 亏损的; valuations: 估值

**[13379.10s] English:** they go up and down the stack to products and hardware they have so much cash that they can build power plants and build data centers which is a durable advantage now but there's also just a reasonable outcome that these APIs are so valuable and so flexible for developers that they become the likes of like something like AWS but AWS and Azure are also going to have these APIs so there's some like that's a like five or six people competing in the API market is hard so maybe like that's why they get squeezed out  
**Translation:** 

**[13406.50s] English:** you mentioned RIP Lama  
**Translation:** Vocabulary: durable: 持久的; squeezed: 被挤压

**[13409.10s] English:** is there a path to winning for meta  
**Translation:** 

**[13411.38s] English:** I think nobody knows they're moving a lot so they're signing licensing deals with Black Forest Labs which is an image generation or mid journey or client maintenance so I think in some ways it's on the product and like consumer facing AI front it's too early to tell I think they have some people that are excellent and very motivated being close to Zuckerberg so I think that there's still a story to unfold  
**Translation:** Vocabulary: zuckerberg: 扎克伯格

**[13439.10s] English:** there  
**Translation:** 

**[13440.00s] English:** llama is a bit different where llama was the most focused expression of the organization and i don't  
**Translation:** Vocabulary: llama: 羊驼

**[13447.56s] English:** see llama being supported to that extent i think it was a very successful brand for them so they  
**Translation:** 

**[13453.30s] English:** still might do some part of participation in the open open ecosystem or continue the llama brand  
**Translation:** 

**[13458.40s] English:** into a different surface because people know what llama is you think there's a llama five  
**Translation:** 

**[13462.10s] English:** not an open weight one it's interesting i think also just to recap a bit i think i mean  
**Translation:** 

**[13469.40s] English:** llama was the i would say pioneering open weight model and then llama one two three a lot of love  
**Translation:** 

**[13475.34s] English:** but i think then i think what happened just hypothesizing or speculating i think the um  
**Translation:** Vocabulary: hypothesizing: 猜测; pioneering: 开创性; speculating: 猜测

**[13481.66s] English:** leaders at meta like the upper uh executives they i think they got really excited about llama because  
**Translation:** 

**[13487.54s] English:** they saw how popular it was in the community and then i think the problem was trying to let's say  
**Translation:** Vocabulary: executives: 高层管理人员

**[13493.18s] English:** monetize the open not monetize the open source but like kind of use the open source to make a  
**Translation:** 

**[13497.92s] English:** bigger splash  
**Translation:** Vocabulary: monetize: 商业化

**[13498.90s] English:** in a sense like to kind of force it almost it felt forced like developing these very big llama  
**Translation:** 

**[13504.16s] English:** four models to have like the best like to be on the top of the benchmarks but i don't think the  
**Translation:** Vocabulary: benchmarks: 评价标准

**[13509.90s] English:** goal of llama models is to be on top of the benchmarks beating let's say chachapiti or  
**Translation:** 

**[13514.18s] English:** other models i think the goal was to have a model that people can use trust uh modify understand  
**Translation:** Vocabulary: chachapiti: 参考模型

**[13520.18s] English:** that includes having smaller models they don't have to be the best models and what happened was  
**Translation:** 

**[13525.00s] English:** just these models were of course like the benchmarks  
**Translation:** 

**[13528.90s] English:** suggested they were better than they were by because i think they had like  
**Translation:** 

**[13531.22s] English:** specific models trained on preferences that they perform well on the benchmarks it's kind of like  
**Translation:** 

**[13536.46s] English:** this overfitting thing to kind of force it to be the best but then at the same time  
**Translation:** 

**[13539.98s] English:** well they didn't do the small models that people could use and i think that no one could run these  
**Translation:** Vocabulary: overfitting: 过拟合

**[13545.06s] English:** big models then and then it was kind of like a weird thing and i think it's just because people  
**Translation:** 

**[13549.62s] English:** got too excited about headlines pushing the frontier i think and too much like on the  
**Translation:** Vocabulary: frontier: 边界

**[13555.52s] English:** benchmarking side yeah yeah i think it imploded under  
**Translation:** 

**[13558.90s] English:** political  
**Translation:** Vocabulary: benchmarking: 衡量标准; imploded: 瓦解

**[13560.00s] English:** internal political fighting and misaligned incentives. So the researchers want to build  
**Translation:** 

**[13564.92s] English:** the best models, but there's a layer of organization and manager that is trying to  
**Translation:** Vocabulary: incentives: 激励机制; misaligned: 不一致

**[13569.58s] English:** demonstrate that they do these things. And then there's a lot of pieces and rumors where how  
**Translation:** 

**[13575.34s] English:** some horrible technical decision was made and how that comes in. And it just seems like  
**Translation:** 

**[13580.48s] English:** it kind of got too bad where it all just crashed out.  
**Translation:** 

**[13584.28s] English:** We should also give huge props to Mark Zuckerberg. I think it comes from Mark, actually.  
**Translation:** Vocabulary: props: 表扬; zuckerberg: 扎克伯格

**[13591.86s] English:** Mark Zuckerberg, from the top of the leadership, saying open source is important.  
**Translation:** 

**[13596.24s] English:** I think the fact that that exists means there could be a Lama 5 where they learn the lessons  
**Translation:** 

**[13602.44s] English:** from the benchmarking and say, we're going to be GPT-OSS and provide a really awesome  
**Translation:** 

**[13608.68s] English:** library of open source.  
**Translation:** 

**[13611.16s] English:** What people say is that there's a debate between  
**Translation:** 

**[13614.28s] English:** Mark and Alexander Wang, who is very bright, but much more against open source.  
**Translation:** 

**[13619.98s] English:** And to the extent that he has a lot of influence over the AI org, it seems much less likely.  
**Translation:** 

**[13624.38s] English:** Because it seems like Mark brought him in for a fresh leadership aid in directing AI.  
**Translation:** 

**[13630.76s] English:** And if the open or closed is no longer the defining nature of the model, I don't expect  
**Translation:** 

**[13635.32s] English:** that to be a defining argument between Mark and Alex. They're both very bright.  
**Translation:** 

**[13640.40s] English:** But I have a hard time understanding all of it.  
**Translation:** 

**[13644.28s] English:** Because Mark wrote this piece in July of 2024, maybe, which was probably the best blog  
**Translation:** 

**[13652.00s] English:** post at the time, saying the case for open source AI.  
**Translation:** 

**[13654.82s] English:** And then July 2025 came around, and it was like, we're re-evaluating our relationship  
**Translation:** 

**[13659.76s] English:** with open source.  
**Translation:** 

**[13660.96s] English:** So it's just kind of like...  
**Translation:** 

**[13662.74s] English:** But I think also the problem, not the problem, but I think, well, we may have been a bit also  
**Translation:** 

**[13668.02s] English:** too harsh, I think, and that caused some of that.  
**Translation:** 

**[13670.32s] English:** Because I think, I mean, we as open source developers or the open source community,  
**Translation:** 

**[13674.28s] English:** as I think, even though the model was maybe not what everyone hoped for, it got a lot  
**Translation:** 

**[13679.46s] English:** of backlash.  
**Translation:** 

**[13680.00s] English:** i think that was a bit unfortunate because i can see that as a company now they were hoping for  
**Translation:** Vocabulary: backlash: 逆反反应

**[13685.52s] English:** positive headlines and uh instead of just getting no headlines or not these positive headlines  
**Translation:** 

**[13691.92s] English:** in in turn they got negative headlines and then all it kind of reflected bad on the company  
**Translation:** 

**[13696.80s] English:** and i think that is also something like where you it's maybe a spite reaction almost like okay  
**Translation:** 

**[13701.76s] English:** we have no we we try to do something nice we try to give give you something cool like an open  
**Translation:** 

**[13706.96s] English:** source model and now you are like you know kind of like be negative about us even like like for  
**Translation:** 

**[13713.20s] English:** the company so in that sense it looks like well maybe then we'll change our mind i guess i don't  
**Translation:** 

**[13718.16s] English:** know yeah that's that's where the uh the dynamics of discourse on x can lead us as a community  
**Translation:** 

**[13726.96s] English:** astray because sometimes it feels random people pick the thing they like they don't like and you  
**Translation:** Vocabulary: astray: 偏离; discourse: 讨论

**[13732.88s] English:** can see the same thing with grok uh for one and grok codes  
**Translation:** 

**[13736.96s] English:** fast one i don't think vibe wise people um love it publicly but a lot of people use it  
**Translation:** 

**[13749.44s] English:** so if you look to reddit and x they don't really give it praise from the programming community but  
**Translation:** 

**[13755.60s] English:** like they use it and the same thing with probably the llama i don't understand i don't understand  
**Translation:** Vocabulary: llama: 羊驼

**[13760.64s] English:** the dynamics of either positive hype or negative hype i don't understand it i mean the story of  
**Translation:** 

**[13766.32s] English:** one of the stories  
**Translation:** 

**[13766.96s] English:** of 2025 is the us feeling the gap of llama which is like all the rise of these chinese open weight  
**Translation:** 

**[13773.20s] English:** models to the point where i was like that was the single issue i've spent a lot of energy on  
**Translation:** 

**[13776.88s] English:** in the last five months is like trying to do policy work to get the us to invest in this  
**Translation:** 

**[13781.92s] English:** tell me the story of adam adam project is it started as me calling it the american deep  
**Translation:** 

**[13786.80s] English:** sea project which doesn't really work for dc audiences but it's the story of like what is  
**Translation:** 

**[13791.84s] English:** the most impactful thing i could do with my career which is that it's chinese open weight model  
**Translation:** 

**[13796.96s] English:** and it's like it's a lot of power and there's a lot of demand  
**Translation:** 

**[13800.00s] English:** end for building on these open models, especially in enterprises in the U.S. that are very cagey  
**Translation:** Vocabulary: cagey: 精明的; enterprises: 企业

**[13804.90s] English:** about these Chinese models. Going to perplexity, the Atom Project, American truly open models,  
**Translation:** 

**[13810.82s] English:** is a U.S.-based initiative to build and host high-quality, genuinely open-weight AI models  
**Translation:** Vocabulary: perplexity: 困惑程度

**[13815.76s] English:** and supporting infrastructure explicitly aimed at competing with and catching up to China's rapidly  
**Translation:** 

**[13822.20s] English:** advancing open-source AI ecosystem. I think the one-sentence summary would be that, or two  
**Translation:** Vocabulary: advancing: 快速发展; explicitly: 明确地

**[13828.72s] English:** sentences. One is a proposition that open models are going to be an engine for AI research because  
**Translation:** 

**[13833.98s] English:** that is what people start with. Therefore, it's important to own them. And the second one is,  
**Translation:** 

**[13839.06s] English:** therefore, the U.S. should be building the best models so that the best research happens in the  
**Translation:** 

**[13845.06s] English:** U.S. and the U.S. companies take the value from being the home of where AI research is happening.  
**Translation:** 

**[13852.24s] English:** And without more investment in open models, we have all the plots on the website where it's like,  
**Translation:** 

**[13856.40s] English:** Quen, Quen, Quen, Quen. And it's all...  
**Translation:** 

**[13858.72s] English:** These models that are excellent from these Chinese companies that are  
**Translation:** 

**[13862.74s] English:** cultivating influence in the U.S., in China, and internationally. And I think  
**Translation:** Vocabulary: cultivating: 培养

**[13867.52s] English:** the U.S. is spending way more on AI and the ability to create open models that are half  
**Translation:** 

**[13873.16s] English:** a generation or a generation beyond what the cutting edge of a closed labs is costs orders  
**Translation:** 

**[13878.08s] English:** of like $100 million, which is a lot of money, but not a lot of the money to these companies.  
**Translation:** 

**[13882.70s] English:** So therefore, we need a centralizing force of people who want to do this. And I think  
**Translation:** 

**[13888.72s] English:** we got signed engagement from people pretty much across the full stack, whether it's policy.  
**Translation:** 

**[13894.04s] English:** So there has been support from the administration?  
**Translation:** 

**[13896.66s] English:** I don't think anyone in the, like, technically in government has  
**Translation:** 

**[13899.64s] English:** signed it publicly. But I know that people that have worked in AI policy, both in Biden and Trump  
**Translation:** 

**[13906.32s] English:** administration, are very supportive of trying to promote open source models in the U.S. I think,  
**Translation:** 

**[13911.66s] English:** for example, AI2 got a grant from the NSF for $100 million over four years, which is like  
**Translation:** 

**[13917.60s] English:** the biggest...  
**Translation:** 

**[13918.72s] English:** Yes, grant.  
**Translation:** 

**[13920.00s] English:** nsf has ever awarded and it's for ai2 to attempt to this and i think it's a starting point but the  
**Translation:** 

**[13925.74s] English:** best thing happens when there are multiple organizations building models because they  
**Translation:** 

**[13929.34s] English:** can cross-pollinate ideas and kind of build this ecosystem like i don't think if it just works if  
**Translation:** 

**[13934.10s] English:** it's just llama releasing models to the world because then you can see llama can go away the  
**Translation:** Vocabulary: llama: 羊驼模型

**[13938.86s] English:** same thing applies for ai2 where it's like i can't be the only one building models and i think that's  
**Translation:** 

**[13944.30s] English:** like that it becomes a lot of time spent on talking to people whether they're in policy  
**Translation:** 

**[13951.68s] English:** i know nvidia is very excited about this i think jensen wong has been specifically talking about  
**Translation:** 

**[13956.74s] English:** the urgency for this and they've changed they've done a lot more in 2025 where the nematron models  
**Translation:** Vocabulary: nematron: 神经网络; urgency: 紧迫性

**[13962.00s] English:** are more of a focus they've started releasing some data along with nvidia's open models and  
**Translation:** 

**[13968.12s] English:** like very few companies do this especially of nvidia's size so like there is there is signs  
**Translation:** 

**[13973.22s] English:** of progress and they're  
**Translation:** 

**[13974.24s] English:** you  
**Translation:** 

**[13974.28s] English:** we hear about reflection ai where they say their two billion dollar fundraise is dedicated to  
**Translation:** 

**[13979.46s] English:** building u.s open models and i feel like their announcement tweet is like it reads like a blog  
**Translation:** Vocabulary: fundraise: 募集资金

**[13983.92s] English:** post out right and i think that that cultural tide is starting to turn i think in in july was  
**Translation:** 

**[13990.54s] English:** when we had like four or five deep sea caliber chinese open weight models and zero from the u.s  
**Translation:** Vocabulary: caliber: 水平

**[13997.52s] English:** and that's that's the moment where i was released this and i was like oh i guess i have to spend  
**Translation:** 

**[14001.44s] English:** energy on this because nobody else is going to do it so  
**Translation:** 

**[14004.22s] English:** it takes a lot of it takes a lot of people contributing together and i don't say that  
**Translation:** 

**[14007.36s] English:** like the atom project isn't like the thing that's helping to move the ecosystem but it's people like  
**Translation:** 

**[14012.48s] English:** me doing this sort of thing to get the word out uh do you like the the 2025 america's ai action  
**Translation:** 

**[14018.94s] English:** plan that includes open source stuff the white house ai action plan includes a dedicated section  
**Translation:** 

**[14024.30s] English:** titled encourage open source and open with ai defining such models and arguing they have unique  
**Translation:** 

**[14030.52s] English:** value for innovation and startups yeah i mean like the  
**Translation:** Vocabulary: startups: 初创企业

**[14033.56s] English:** ai action plan is a plan but largely i think it's like maybe the most coherent  
**Translation:** 

**[14040.00s] English:** policy document that has come out of the administration and i hope that it largely  
**Translation:** 

**[14044.60s] English:** succeeds and i know people that have worked on the action plan and the challenge is taking policy and  
**Translation:** 

**[14050.26s] English:** making it real and i have no idea how to do this as an ai researcher but like like largely a lot  
**Translation:** 

**[14055.30s] English:** of things from that were very real and there's a huge build out of ai in the country and it's like  
**Translation:** 

**[14060.38s] English:** there are a lot of issues that people are hearing about from water use to whatever and like we  
**Translation:** 

**[14065.22s] English:** should be able to build things in this country but also we need to not ruin places in our country  
**Translation:** 

**[14070.52s] English:** in the process of building it and it's a worthwhile to spend energy on i think that's a role that the  
**Translation:** 

**[14076.22s] English:** federal government plays it's like they set the agenda and with ai setting the agenda that open  
**Translation:** 

**[14080.92s] English:** wait should be a first consideration is like that's a large part of what they can do and then  
**Translation:** 

**[14087.62s] English:** people think about it also for education and talent for these companies it's i think very  
**Translation:** 

**[14092.86s] English:** important because otherwise you know if they're only  
**Translation:** 

**[14095.20s] English:** closed um models how do you get the next generation of people contributing at some point because  
**Translation:** 

**[14101.84s] English:** otherwise you will at some point only be able to learn after you joined a company but then at that  
**Translation:** 

**[14108.78s] English:** point like how do you hire talented people how do you identify talented people and i think open  
**Translation:** 

**[14113.86s] English:** source is that's even for a lot of things but also even just for educating the population and  
**Translation:** 

**[14119.86s] English:** training the next generation of researchers it's the way or the only way the way that i could have  
**Translation:** 

**[14124.90s] English:** gotten  
**Translation:** 

**[14125.18s] English:** this to more go more viral is was to tell a story of chinese ai integrating with an  
**Translation:** 

**[14130.18s] English:** authoritarian state and being asi and taking over the world and therefore we need our own american  
**Translation:** Vocabulary: authoritarian: 专制; integrating: 融合; viral: 病毒式

**[14134.80s] English:** models but it's very intentional for why i talk about innovation and science in the u.s because i  
**Translation:** 

**[14140.08s] English:** think it's both more realistic as an outcome but just like it's like it's a world that is  
**Translation:** Vocabulary: intentional: 故意的

**[14145.66s] English:** i would like to manifest i would say though also even like let's say uh any open weight model i do  
**Translation:** 

**[14152.34s] English:** think is a valuable model yeah  
**Translation:** Vocabulary: manifest: 显现

**[14155.18s] English:** my argument is that we should be in a leading position but i think that it's  
**Translation:** 

**[14160.00s] English:** worth saying it so simply because there are still voices in the ai ecosystem that say we should  
**Translation:** 

**[14165.70s] English:** consider banning releasing open models due to the safety risks and i think it's worth adding that  
**Translation:** 

**[14170.90s] English:** i think effectively that's impossible without making the u.s like it have its own great  
**Translation:** 

**[14176.36s] English:** firewall which is also known to not work that well because the cost for training these models  
**Translation:** 

**[14182.68s] English:** whether it's one to a hundred million dollars is attainable to a huge amount of people in the world  
**Translation:** Vocabulary: attainable: 可获得的; firewall: 防火墙

**[14189.28s] English:** that want to have influence so these models will be getting trained all over the world and these  
**Translation:** 

**[14194.08s] English:** we want the models especially when like i mean there are safety concerns but we want these  
**Translation:** 

**[14200.20s] English:** information and tools to flow freely across the world and into the u.s so that we people can use  
**Translation:** 

**[14205.64s] English:** them and learn from them and we like stopping that would be such a restructuring of our internet that  
**Translation:** Vocabulary: restructuring: 重新构建

**[14210.36s] English:** it seems impossible do you think maybe in that case the big open weight models from china are  
**Translation:** 

**[14215.40s] English:** actually a good thing in a sense like for the u.s companies because maybe  
**Translation:** 

**[14219.26s] English:** the u.s companies you mentioned earlier they are usually one generation behind in terms of what  
**Translation:** 

**[14223.84s] English:** they release open source versus what they are using for example gpt os s might not be the  
**Translation:** 

**[14229.14s] English:** cutting edge model gemma 3 might not be but they do that because they know this is safe to release  
**Translation:** 

**[14233.98s] English:** but then when they see these companies see for example there is deep seek version 3.2 which is  
**Translation:** Vocabulary: gemma: 宝石模型

**[14239.04s] English:** really awesome and it gets used and there is no backlash there is no security risk that could  
**Translation:** 

**[14244.98s] English:** then again encourage them to release better models maybe that that in a sense is a very  
**Translation:** Vocabulary: backlash: 逆反心理

**[14249.26s] English:** positive thing a hundred percent these chinese companies have set things into motion that i think  
**Translation:** 

**[14253.42s] English:** would potentially not have happened if they were not all releasing models so i think it was like  
**Translation:** 

**[14259.00s] English:** i'm almost sure that those discussions have been had by leadership is there a possible future where  
**Translation:** 

**[14267.16s] English:** the dominant models ai models in the world are all open source depends on the trajectory of  
**Translation:** Vocabulary: trajectory: 发展趋势

**[14272.24s] English:** progress that you predict if you think saturation and progress is even coming within a few years  
**Translation:** 

**[14277.22s] English:** so essentially within the time of the u.s government and the u.s government and the  
**Translation:** 

**[14279.26s] English:** u.s government and the u.s government and the financial support  
**Translation:** 

**[14280.00s] English:** is still very good, then open models will be so optimized and so much cheaper to run that they  
**Translation:** Vocabulary: optimized: 优化

**[14285.30s] English:** will win out. Essentially, this goes back to open source ideas where so many more people will be  
**Translation:** 

**[14290.38s] English:** putting money into optimizing this serving of these open weight common architectures that they  
**Translation:** 

**[14296.12s] English:** will become standards. And then you could have chips dedicated to them and it'll be way cheaper  
**Translation:** 

**[14300.94s] English:** than the offerings from these closed companies that are custom. We should say that AI27 report  
**Translation:** 

**[14307.64s] English:** kind of predicts one of the things it does from a narrative perspective is that there'll be a lot  
**Translation:** 

**[14312.36s] English:** of centralization. As the AI system gets smarter and smarter, the national security concerns will  
**Translation:** 

**[14318.20s] English:** come to be and you'll centralize the labs and you'll become super secretive and there'll be  
**Translation:** 

**[14323.46s] English:** this whole race from a military perspective between China and the United States. And so  
**Translation:** 

**[14329.84s] English:** all of this fun conversations we're having about LLMs, the generals, the soldiers will come into  
**Translation:** 

**[14336.78s] English:** the room and be like,  
**Translation:** 

**[14337.64s] English:** all right, we're now in the Manhattan Project stage of this whole thing.  
**Translation:** 

**[14342.94s] English:** I think 2025, 6, 7, 27, I don't think something like that is even remotely possible. I mean,  
**Translation:** Vocabulary: remotely: 遥远地

**[14349.04s] English:** you can make the same argument for computers, right? You can say, okay, computers are capable  
**Translation:** 

**[14353.78s] English:** and we don't want the general public to get them or chips, even AI chips. But you see how  
**Translation:** 

**[14359.06s] English:** Huawei makes chips now, it took a few years. And I don't think there is a way you can contain  
**Translation:** 

**[14367.64s] English:** something like that, like knowledge like that. I think in this day and age, it is impossible.  
**Translation:** 

**[14373.72s] English:** Like the internet, I don't think this is a possibility.  
**Translation:** 

**[14377.84s] English:** On the Manhattan Project thing, one of my funny things making out of them is I think that like  
**Translation:** 

**[14381.40s] English:** a Manhattan Project-like thing for open models would actually be pretty reasonable because it  
**Translation:** 

**[14385.58s] English:** wouldn't cost that much. But I think that that will come. It seems like culturally the companies  
**Translation:** Vocabulary: culturally: 文化上

**[14390.12s] English:** are changing. But I agree with Sebastian on all of the stuff that you just said. It's just like,  
**Translation:** 

**[14394.14s] English:** I don't see it happening, nor,  
**Translation:** Vocabulary: sebastian: 赛巴斯蒂安

**[14397.64s] English:** being helpful yeah I mean the the  
**Translation:** 

**[14400.00s] English:** The motivating force behind the Manhattan Project  
**Translation:** 

**[14401.70s] English:** is there was a civilizational risk.  
**Translation:** 

**[14404.36s] English:** It's harder to motivate that for open source models.  
**Translation:** Vocabulary: civilizational: 文明的

**[14408.00s] English:** There's not civilizational risk.  
**Translation:** 

**[14410.54s] English:** You think on the hardware side,  
**Translation:** 

**[14412.98s] English:** we mentioned NVIDIA a bunch of times.  
**Translation:** 

**[14414.92s] English:** Do you think Jensen and NVIDIA are going to keep winning?  
**Translation:** 

**[14418.70s] English:** I think they have the downside  
**Translation:** 

**[14419.60s] English:** that they have to iterate a lot and manufacture a lot.  
**Translation:** Vocabulary: downside: 缺点; manufacture: 生产

**[14422.68s] English:** And I think they probably, what they're doing,  
**Translation:** 

**[14426.80s] English:** they do innovate.  
**Translation:** Vocabulary: innovate: 创新

**[14427.98s] English:** But I think there's always the chance  
**Translation:** 

**[14431.70s] English:** that there is something  
**Translation:** 

**[14432.58s] English:** who does something fundamentally different,  
**Translation:** 

**[14434.60s] English:** who gets very lucky and then does something.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[14437.74s] English:** But the problem is, I think, adoption.  
**Translation:** 

**[14439.94s] English:** You know, like the mode of NVIDIA  
**Translation:** 

**[14441.88s] English:** is probably not just the GPU.  
**Translation:** 

**[14443.90s] English:** It's more like the CUDA ecosystem.  
**Translation:** 

**[14445.50s] English:** And that has evolved over so many, I think, two decades.  
**Translation:** 

**[14448.26s] English:** I think, I mean, even back when I was a grad student,  
**Translation:** 

**[14450.24s] English:** I was in a lab where we did biophysical simulations,  
**Translation:** 

**[14453.60s] English:** molecular dynamics, and we had a Tesla GPU.  
**Translation:** Vocabulary: biophysical: 生物物理的

**[14456.32s] English:** Back then, just for the computation,  
**Translation:** 

**[14457.72s] English:** it was...  
**Translation:** Vocabulary: computation: 计算

**[14457.98s] English:** I mean, 15 years ago now.  
**Translation:** 

**[14460.56s] English:** And it just, they built this up for a long time.  
**Translation:** 

**[14463.34s] English:** And that's like, that's the mode, I think.  
**Translation:** 

**[14465.10s] English:** It's not the chip itself,  
**Translation:** 

**[14467.32s] English:** although they have now the money  
**Translation:** 

**[14469.28s] English:** to iterate and build and scale.  
**Translation:** 

**[14471.40s] English:** But then it's really on the compatibility.  
**Translation:** 

**[14474.34s] English:** It's like, well, if you're at that scale as a company,  
**Translation:** Vocabulary: compatibility: 兼容性

**[14476.72s] English:** why would you go with something risky  
**Translation:** 

**[14478.22s] English:** where it's only a few chips that they can make per year?  
**Translation:** 

**[14481.24s] English:** You go with the big one.  
**Translation:** 

**[14482.48s] English:** But then I do think with LLMs now,  
**Translation:** 

**[14485.64s] English:** also, it will be easier to design  
**Translation:** 

**[14487.18s] English:** something like CUDA.  
**Translation:** 

**[14489.16s] English:** You know, like the next...  
**Translation:** 

**[14489.80s] English:** So it took 15 years because it's hard.  
**Translation:** 

**[14491.82s] English:** But then now we have LLMs,  
**Translation:** 

**[14493.62s] English:** we can maybe replicate CUDA.  
**Translation:** 

**[14495.62s] English:** And I wonder if there will be a separation  
**Translation:** 

**[14497.90s] English:** of the training and the inference compute  
**Translation:** Vocabulary: inference: 推理

**[14500.46s] English:** as we kind of stabilize a bit more  
**Translation:** 

**[14502.92s] English:** and more and more computers needed for inference.  
**Translation:** Vocabulary: stabilize: 趋于稳定

**[14506.86s] English:** That's supposed to be the point of the Grok acquisition.  
**Translation:** 

**[14510.10s] English:** And that's why part of what Vera Rubin is,  
**Translation:** Vocabulary: rubin: 鲁宾

**[14512.54s] English:** where they have a new chip with no high bandwidth memory,  
**Translation:** 

**[14515.20s] English:** which is one of the...  
**Translation:** Vocabulary: bandwidth: 数据带宽

**[14515.98s] English:** Or very little,  
**Translation:** 

**[14516.66s] English:** which is one of the most expensive pieces.  
**Translation:** 

**[14519.24s] English:** It's designed...  
**Translation:** 

**[14520.00s] English:** for pre-fill which is the part of inference where you essentially do a lot of matrix multiplications  
**Translation:** Vocabulary: matrix: 矩阵; multiplications: 乘法

**[14526.18s] English:** and then you only need the memory when you're doing this autoregressive generation you have  
**Translation:** 

**[14530.10s] English:** the kv cache swaps so they have this new gpu that's designed for that specific use case and  
**Translation:** Vocabulary: autoregressive: 自回归; cache: 缓存; swaps: 交换

**[14535.76s] English:** then the cost of ownership for per flop or whatever is actually way lower but i i think that  
**Translation:** 

**[14542.20s] English:** nvidia's fate lies in the diffusion of ai still their biggest clients are still these hyperscale  
**Translation:** Vocabulary: diffusion: 扩散; hyperscale: 超大规模

**[14547.98s] English:** companies whether it's like google obviously can make tpus amazon is making tranium microsoft will  
**Translation:** 

**[14555.06s] English:** try to do its own things and like so long as the pace of ai progress is high nvidia's platform is  
**Translation:** 

**[14561.82s] English:** the most flexible and people will want that but if there's stagnation then creating bespoke chips  
**Translation:** 

**[14568.02s] English:** there's more time to do it it's interesting that uh nvidia is quite active in trying to develop  
**Translation:** Vocabulary: bespoke: 定制; stagnation: 停滞

**[14574.38s] English:** all kinds of different products they tried to create areas  
**Translation:** 

**[14577.96s] English:** of commercial value that will use a lot of gpus but they keep innovating and there's like  
**Translation:** Vocabulary: innovating: 不断创新

**[14584.06s] English:** they're doing a lot of incredible research so everyone says the company is super oriented  
**Translation:** 

**[14588.70s] English:** around jensen and how operationally plugged in he is and it sounds so unlike many other big  
**Translation:** Vocabulary: operationally: 运作上; oriented: 导向的

**[14595.02s] English:** companies that i've heard about and so long as that's the culture i think that i will expect  
**Translation:** 

**[14599.64s] English:** them to keep progress happening and it's like he's still in the steve jobs era of apple so long  
**Translation:** 

**[14605.58s] English:** as that is how it operates i'm pretty  
**Translation:** 

**[14607.96s] English:** optimistic for their situation because it's like it is their top order problem and i don't know if  
**Translation:** 

**[14615.28s] English:** making these chips for the whole ecosystem is the top goal of all these other companies they will do  
**Translation:** 

**[14620.36s] English:** a good job but it might not be as good of a job since you mentioned jensen i've been um reading a  
**Translation:** 

**[14627.12s] English:** lot about history and about singular figures in history what do you guys think about the single  
**Translation:** 

**[14631.52s] English:** man woman view of history how important are individuals for steering the direction of history  
**Translation:** Vocabulary: steering: 引导

**[14637.96s] English:** in the tech sector so you know what's  
**Translation:** 

**[14640.00s] English:** nvidia without jensen you mentioned steve jobs what's apple without steve jobs what's xai  
**Translation:** 

**[14646.16s] English:** without elon or deep mind without demis people make things earlier and faster where scientifically  
**Translation:** 

**[14656.08s] English:** many great scientists credit to being in the right place at the right time and still making  
**Translation:** Vocabulary: scientifically: 科学地

**[14661.30s] English:** the innovation where eventually someone else will still have the idea so i think that in that way  
**Translation:** 

**[14667.88s] English:** jensen is helping manifest this gpu revolution much faster and much more focused than without  
**Translation:** Vocabulary: manifest: 显现

**[14675.94s] English:** having a person there it would do and this is making the whole ai build out faster but i do  
**Translation:** 

**[14681.38s] English:** still think that eventually like something like chat gpt would have happened and a build out like  
**Translation:** 

**[14686.44s] English:** this would have happened but it probably would not have been as fast or like as like i think  
**Translation:** 

**[14692.20s] English:** that's the sort of flavor that is applied people these individual people are people who are placing  
**Translation:** 

**[14697.44s] English:** bets on the gpu revolution and i think that's the sort of flavor that is applied people these  
**Translation:** 

**[14697.86s] English:** something some get lucky some don't but if you don't have these people at the helm it will be  
**Translation:** 

**[14701.70s] English:** more diffused it's almost like investing in a etf versus individual stocks individual stocks  
**Translation:** 

**[14708.26s] English:** might go up might go down more heavily than an etf which is more balanced it will eventually  
**Translation:** Vocabulary: diffused: 分散的

**[14712.66s] English:** go up over time we'll get there but it's just like you know the focus i think is the thing  
**Translation:** 

**[14718.66s] English:** passion and focus isn't there a real case to be made that without jensen there's not a  
**Translation:** 

**[14722.50s] English:** uh reinvigoration of the the deep learning revolution it could have been 20 years later  
**Translation:** 

**[14728.26s] English:** is the thing that i would say yeah yeah 20 or like another ai went like a deep learning winter could  
**Translation:** Vocabulary: reinvigoration: 重新振兴

**[14732.74s] English:** have come yeah if gpus weren't around that could change history completely because you could think  
**Translation:** 

**[14738.02s] English:** of all the other technologies that that could have come in the meantime and the focus of human  
**Translation:** Vocabulary: meantime: 其间

**[14743.30s] English:** civilization could the silicon valley would be captured by different hype but i do think it is  
**Translation:** 

**[14748.90s] English:** uh i mean there's certainly an aspect where it was all planned  
**Translation:** 

**[14752.50s] English:** the gpu trajectory but on the other hand it's also a lot of lucky coincidences for example  
**Translation:** 

**[14757.86s] English:** or good intuition like the investment into  
**Translation:** Vocabulary: coincidences: 巧合; intuition: 直觉; trajectory: 轨迹

**[14760.00s] English:** this let's say biophysical simulations or like i mean i think it started with video games and then  
**Translation:** 

**[14765.04s] English:** it just happened to be good at linear algebra because video games require a lot of linear  
**Translation:** Vocabulary: algebra: 线性代数; biophysical: 生物物理

**[14769.44s] English:** algebra and then you have the biophysical um simulations and then but still i don't think  
**Translation:** 

**[14774.40s] English:** the plan the master plan was ai i think there was just it happened to be alex krashevsky so someone  
**Translation:** 

**[14781.36s] English:** took these gpus and like hey let's try to train a neural network on that and happened to work really  
**Translation:** 

**[14785.76s] English:** well and i think it only happened because you could purchase those gpus gaming would have  
**Translation:** Vocabulary: neural: 神经网络

**[14790.96s] English:** created a demand for faster processors if nvidia had gone out of business in the early days  
**Translation:** 

**[14796.80s] English:** that's what i would think like i think that the gpus would have been different for the alex but  
**Translation:** Vocabulary: processors: 处理器

**[14803.44s] English:** i think like gpus would still exist at the time of alex net and at the time of the transformer  
**Translation:** 

**[14808.88s] English:** it was just hard to know if it would be one company as successful or multiple smaller companies with  
**Translation:** 

**[14814.56s] English:** worse gpus  
**Translation:** 

**[14815.76s] English:** chips but i don't think that's like a 100 year delay it might be a decade delay  
**Translation:** 

**[14821.36s] English:** well it could be one two three four five decade delay i mean i just can't see intel or amd doing  
**Translation:** 

**[14828.00s] English:** what nvidia i don't think it would be a company that exists i think it would be a different  
**Translation:** 

**[14832.56s] English:** company it would rise like silicon graphics or something so yeah some company that has died  
**Translation:** 

**[14837.76s] English:** would have done it but it does like just look looking at it it seems like these singular  
**Translation:** 

**[14843.44s] English:** figures these leaders have a huge  
**Translation:** 

**[14845.76s] English:** impact on the trajectory of the world obviously incredible teams behind them  
**Translation:** 

**[14851.36s] English:** but you know having that kind of very singular almost dogmatic focus  
**Translation:** 

**[14858.32s] English:** is necessary to make progress yeah i mean even with uh gpt it wouldn't exist if there wasn't a  
**Translation:** Vocabulary: dogmatic: 教条的

**[14863.92s] English:** person elia who pushed for this scaling right i mean yeah dario was also deeply involved in that  
**Translation:** 

**[14870.08s] English:** you read some of the histories of openai it almost seems wild thinking about how early these people  
**Translation:** 

**[14875.76s] English:** to hook up 10,000 GPUs and take all of OpenAI's compute and train one model.  
**Translation:** 

**[14880.00s] English:** there's a lot of people there that didn't want to do that which is an insane thing to believe  
**Translation:** 

**[14884.34s] English:** that to believe scaling before scaling has any indication that it's going to materialize again  
**Translation:** 

**[14891.12s] English:** singular figures speaking of which 100 years from now this is presumably post singularity whatever  
**Translation:** Vocabulary: materialize: 显现; presumably: 大概

**[14899.40s] English:** singularity is when historians look back at our time now what technological breakthroughs would  
**Translation:** 

**[14907.04s] English:** they really emphasize as the breakthroughs that led to the singularity so so far we have touring  
**Translation:** 

**[14913.90s] English:** to today 80 years i think it would still be computing like the umbrella term computing just  
**Translation:** 

**[14920.62s] English:** i don't necessarily think it's even like 100 years 200 years from now it would be ai it would  
**Translation:** Vocabulary: computing: 计算领域

**[14926.24s] English:** could be still well be computers you know just we are now taking better advantage of computers but  
**Translation:** 

**[14931.70s] English:** like the fact of computing it's basically moore's law kind of discussion you're not  
**Translation:** 

**[14936.72s] English:** even  
**Translation:** 

**[14937.02s] English:** Even the details of CUDA and GPUs won't even be remembered.  
**Translation:** 

**[14940.78s] English:** And it won't be all this software turmoil.  
**Translation:** 

**[14944.24s] English:** It'll be just obviously compute.  
**Translation:** Vocabulary: turmoil: 混乱

**[14947.06s] English:** I generally agree, but it's like, is the connectivity of the internet and compute able to be merged?  
**Translation:** 

**[14955.06s] English:** Or is it both of them?  
**Translation:** 

**[14957.78s] English:** I think the internet will probably be related to, yeah, I mean, communication.  
**Translation:** 

**[14961.86s] English:** It could be a phone, internet, satellite, that stuff.  
**Translation:** 

**[14964.90s] English:** But where, yeah, and compute is more like the scaling aspect of it.  
**Translation:** 

**[14969.22s] English:** It's possible that the internet is completely forgotten.  
**Translation:** 

**[14971.62s] English:** The internet is wrapped into the phone networks, like communication networks.  
**Translation:** 

**[14978.50s] English:** This is just another manifestation of that.  
**Translation:** Vocabulary: manifestation: 表现形式

**[14981.24s] English:** And the real breakthrough comes from just the increased compute, as the Moore's Law broadly defined.  
**Translation:** 

**[14986.56s] English:** Well, I think that connection of people is very fundamental to it.  
**Translation:** 

**[14990.36s] English:** So it's like, you can talk to anybody.  
**Translation:** 

**[14993.26s] English:** You want to find the best person.  
**Translation:** 

**[14994.90s] English:** You want to find the best person in the world for something.  
**Translation:** 

**[14995.90s] English:** They are somewhere in the world.  
**Translation:** 

**[14997.14s] English:** And being able to have that flow of information.  
**Translation:** 

**[15000.00s] English:** The AIs will also rely on this.  
**Translation:** 

**[15002.56s] English:** I think I've been fixating on the, like,  
**Translation:** 

**[15004.66s] English:** when I said the dream was dead  
**Translation:** 

**[15006.20s] English:** about the one central model.  
**Translation:** 

**[15007.52s] English:** And the thing that is evolving is, like,  
**Translation:** Vocabulary: evolving: 演变

**[15009.20s] English:** people have many agents for different tasks.  
**Translation:** 

**[15011.96s] English:** People already start doing this  
**Translation:** 

**[15013.04s] English:** with different clods for different tasks.  
**Translation:** 

**[15015.10s] English:** And it's described as many AGIs in the data center  
**Translation:** Vocabulary: clods: 土块

**[15018.10s] English:** where each one manages and they talk to each other.  
**Translation:** 

**[15020.72s] English:** And, like, that is so reliant on networking  
**Translation:** 

**[15023.76s] English:** and free flow of information on top of compute.  
**Translation:** 

**[15026.88s] English:** But, like, networking, especially with GPUs,  
**Translation:** 

**[15030.46s] English:** is such a part of scaling up compute.  
**Translation:** 

**[15033.36s] English:** Like, the GPUs and the data centers  
**Translation:** 

**[15034.84s] English:** need to talk to each other.  
**Translation:** 

**[15036.54s] English:** Anything about neural networks will be remembered?  
**Translation:** Vocabulary: neural: 神经网络

**[15039.92s] English:** Like, do you think there's something very specific  
**Translation:** 

**[15042.46s] English:** and singular to the fact that it's neural networks  
**Translation:** 

**[15044.48s] English:** that's seen as a breakthrough, like a genius,  
**Translation:** 

**[15046.80s] English:** that you're basically replicating in a very crude way  
**Translation:** 

**[15049.62s] English:** the human mind, the structure of the human brain,  
**Translation:** 

**[15053.28s] English:** the human mind?  
**Translation:** 

**[15054.22s] English:** I think with all the human mind,  
**Translation:** 

**[15056.56s] English:** we probably wouldn't have neural networks  
**Translation:** 

**[15058.86s] English:** because it just wasn't inspiration for that.  
**Translation:** 

**[15061.70s] English:** But at the other end, I think it's just so different.  
**Translation:** 

**[15065.26s] English:** I mean, it's digital versus, you know, biological  
**Translation:** 

**[15067.34s] English:** that I do think it will probably be more, like,  
**Translation:** 

**[15070.30s] English:** grouped as an algorithm.  
**Translation:** 

**[15071.82s] English:** That's massively paralyzable  
**Translation:** Vocabulary: algorithm: 算法; massively: 大规模地; paralyzable: 可瘫痪的

**[15073.16s] English:** on this particular kind of compute.  
**Translation:** 

**[15075.50s] English:** Could have well been, like, genetic computing,  
**Translation:** 

**[15077.60s] English:** like genetic algorithms just as paralyzed.  
**Translation:** 

**[15080.10s] English:** I think it just happens that this is more efficient,  
**Translation:** Vocabulary: paralyzed: 四肢无力

**[15082.28s] English:** works better, you know?  
**Translation:** 

**[15083.26s] English:** And it very well could be that the LLM,  
**Translation:** 

**[15085.08s] English:** you know, the neural networks,  
**Translation:** 

**[15086.28s] English:** the way we architect them now  
**Translation:** 

**[15088.84s] English:** is just a small component of the system  
**Translation:** 

**[15092.58s] English:** that leads to singularity.  
**Translation:** 

**[15093.84s] English:** The thing is, if you think of it 100 years,  
**Translation:** 

**[15095.68s] English:** like, society, I think, can be changed more  
**Translation:** 

**[15098.92s] English:** with more compute and intelligence  
**Translation:** 

**[15100.64s] English:** because of autonomy.  
**Translation:** Vocabulary: autonomy: 自主性

**[15101.98s] English:** But it's like looking at this,  
**Translation:** 

**[15104.50s] English:** like, what are the things from the Industrial Revolution  
**Translation:** 

**[15106.40s] English:** that we remember?  
**Translation:** 

**[15107.08s] English:** We remember, like, the engine  
**Translation:** 

**[15108.14s] English:** is probably the equivalent of the computer in this.  
**Translation:** 

**[15111.72s] English:** But there's a lot of other, like,  
**Translation:** 

**[15113.38s] English:** physical transformations that people are aware of.  
**Translation:** 

**[15115.98s] English:** Like, all the cotton gin and all these things that...  
**Translation:** Vocabulary: transformations: 变化

**[15120.00s] English:** these machines that are still known air conditioning refrigerators like  
**Translation:** 

**[15125.76s] English:** some of these things from ai will still be known like the word transformer could still very well  
**Translation:** 

**[15131.36s] English:** be known i would guess that deep learning is definitely still learn known but the transformer  
**Translation:** 

**[15135.60s] English:** might be evolved away from in 100 years of with asi ai researchers everywhere but i think deep  
**Translation:** 

**[15144.00s] English:** learning is likely to be a term that is remembered and i wonder what the air conditioning and the  
**Translation:** 

**[15150.08s] English:** refrigeration of the future is that ai brings is there uh if we travel forward 100 years from now  
**Translation:** Vocabulary: refrigeration: 制冷技术

**[15157.28s] English:** we transport there right now what do you think is different how do you think the world looks  
**Translation:** 

**[15161.36s] English:** different first of all you think there's humans you think there's robots everywhere walking around  
**Translation:** 

**[15166.40s] English:** i do think specialized robots for sure for certain tasks humanoid form um that i'm maybe half humanoid  
**Translation:** 

**[15173.36s] English:** we'll see  
**Translation:** Vocabulary: humanoid: 类人形

**[15174.00s] English:** i think for certain things yes uh there will be humanoid robots because it's just  
**Translation:** 

**[15178.32s] English:** amenable for the environment but like for certain tasks it might make sense what's harder to imagine  
**Translation:** Vocabulary: amenable: 易于接受的

**[15184.16s] English:** is how we interact with the devices and what humans do with devices will i mean i'm pretty  
**Translation:** 

**[15190.24s] English:** sure will probably not be the cell phone will probably not be the laptop will it be you know  
**Translation:** 

**[15195.28s] English:** implants i mean it has to be brain computer interfaces right yeah i mean 100 years from  
**Translation:** 

**[15199.28s] English:** now it has to like given the progress we're seeing now there has to be  
**Translation:** Vocabulary: interfaces: 接口

**[15204.00s] English:** unless there's legitimately complete alteration of how we interact with reality on the other  
**Translation:** 

**[15213.36s] English:** hand if you think of cars cars are older than 100 years right and it's still the same interface it's  
**Translation:** Vocabulary: alteration: 彻底改变; interface: 界面; legitimately: 正当地

**[15218.24s] English:** not we haven't replaced cars with something else we just made the cars better but it's still  
**Translation:** 

**[15223.44s] English:** steering wheel it's still wheels you know i think we'll still carry around a physical brick of  
**Translation:** Vocabulary: steering: 方向盘

**[15227.76s] English:** compute because people want some ability to have a private like you might not engage with it as much  
**Translation:** 

**[15234.00s] English:** phone but having something where you could have private information that is yours as  
**Translation:** 

**[15237.36s] English:** an interface between the rest of the internet  
**Translation:** 

**[15240.00s] English:** I think it's something that people will still exist.  
**Translation:** 

**[15242.70s] English:** It might not look like an iPhone and it might be used a lot less,  
**Translation:** 

**[15245.16s] English:** but I still expect to have people carry things around.  
**Translation:** 

**[15248.56s] English:** Why do you think the smartphone is the embodiment of private?  
**Translation:** 

**[15252.86s] English:** There's a camera on it.  
**Translation:** Vocabulary: embodiment: 具体体现

**[15255.24s] English:** Private for you,  
**Translation:** 

**[15256.20s] English:** like encrypted messages,  
**Translation:** Vocabulary: encrypted: 加密的

**[15258.04s] English:** encrypted photos.  
**Translation:** 

**[15259.08s] English:** You know what your life is like.  
**Translation:** 

**[15261.96s] English:** I guess this is a question on whether how optimistic on brain machine  
**Translation:** 

**[15265.10s] English:** interfaces you are,  
**Translation:** Vocabulary: optimistic: 乐观

**[15266.46s] English:** if there's all of that just going to be stored in the cloud and you're  
**Translation:** 

**[15269.90s] English:** whole calendar.  
**Translation:** 

**[15272.74s] English:** It's hard to think about processing all the information that we can  
**Translation:** 

**[15276.18s] English:** process visually through brain machine interfaces,  
**Translation:** 

**[15280.22s] English:** presenting something like a calendar or something to you.  
**Translation:** 

**[15283.50s] English:** Like it's hard to just think about knowing without looking,  
**Translation:** 

**[15287.48s] English:** you know,  
**Translation:** 

**[15287.76s] English:** your email inbox,  
**Translation:** 

**[15288.80s] English:** like you signal to a computer and then you just know your email inbox.  
**Translation:** 

**[15292.72s] English:** Like,  
**Translation:** 

**[15292.86s] English:** what does that like?  
**Translation:** 

**[15293.58s] English:** Is that something that the human brain can handle being piped into it?  
**Translation:** 

**[15297.76s] English:** Non-visually like,  
**Translation:** 

**[15299.90s] English:** I don't know exactly how those transformations happen because humans aren't  
**Translation:** Vocabulary: transformations: 变化

**[15303.96s] English:** changing in a hundred years.  
**Translation:** 

**[15305.58s] English:** I think agency and community are things that people actually want local  
**Translation:** 

**[15309.52s] English:** community.  
**Translation:** 

**[15310.10s] English:** So people you are close to being able to do things with them and being able  
**Translation:** 

**[15314.90s] English:** to ascribe mean,  
**Translation:** 

**[15316.94s] English:** like describe meaning to your life and to be able to do things.  
**Translation:** Vocabulary: ascribe: 归因

**[15320.34s] English:** I think that that is maybe if not in a hundred years,  
**Translation:** 

**[15323.64s] English:** I don't think that human biology is changing away from those on a timescale  
**Translation:** Vocabulary: timescale: 时间尺度

**[15328.94s] English:** that.  
**Translation:** 

**[15329.24s] English:** We can discuss.  
**Translation:** 

**[15330.98s] English:** And I think that like UBI does not solve agency.  
**Translation:** 

**[15335.34s] English:** I do expect mass wealth and I hope that it is spread so that the average  
**Translation:** 

**[15340.68s] English:** life does look very different in a hundred years,  
**Translation:** 

**[15343.48s] English:** but that's still a lot to happen in a hundred years.  
**Translation:** 

**[15345.90s] English:** If you think about countries that are early in their development process to  
**Translation:** 

**[15349.88s] English:** getting access to computing and internet,  
**Translation:** 

**[15352.58s] English:** like to build all the infrastructure and to have policy that shares one  
**Translation:** 

**[15359.22s] English:** nation's wealth.  
**Translation:** 

**[15359.90s] English:** Yeah.  
**Translation:** 

**[15360.00s] English:** with another is it's i think it's an optimistic view to see all that happening in 100 years while  
**Translation:** 

**[15366.10s] English:** they still being well they are still independent entities and not just like absorbed into some  
**Translation:** 

**[15370.98s] English:** international order by force but there could be just better more elaborate more effective  
**Translation:** 

**[15376.64s] English:** social support systems that help alleviate some levels of basic suffering from the world  
**Translation:** 

**[15384.26s] English:** you know the transformation of society where a lot of jobs are lost in the short term  
**Translation:** Vocabulary: alleviate: 减轻

**[15388.38s] English:** i think we have to really remember that each individual job that's lost  
**Translation:** 

**[15392.68s] English:** is a human being who's suffering that's like a when jobs are lost it scales a real tragedy  
**Translation:** 

**[15400.22s] English:** you can make all kinds of arguments about economics or it's it's all going to be okay it's  
**Translation:** 

**[15406.42s] English:** it's good for the gdp there's going to be new jobs created fundamentally the individual level  
**Translation:** Vocabulary: fundamentally: 从根本上

**[15412.94s] English:** for that human being that's that's real suffering that's a real personal sort of  
**Translation:** 

**[15418.20s] English:** tragedy  
**Translation:** 

**[15418.38s] English:** and we have to not forget that as the technologies are being developed and also my my hope for all  
**Translation:** 

**[15425.62s] English:** the ai slop we're seeing is that there will be a greater and greater premium for the the  
**Translation:** Vocabulary: premium: 附加价值

**[15432.66s] English:** fundamental aspects of the human experience that are like in person the things that we all  
**Translation:** 

**[15438.50s] English:** like seeing each other talking together in person the next few years are definitely going to be  
**Translation:** 

**[15444.58s] English:** increased value on physical goods and events  
**Translation:** 

**[15448.20s] English:** and even more pressure on slop so it'll be so they'll keep the slop is only starting the next  
**Translation:** 

**[15455.44s] English:** few years will be more and more diverse versions of slop it would be drowning in slop so i'm hoping  
**Translation:** 

**[15460.78s] English:** that we society drowns in slop enough to snap out of it and be like we can't like none like it just  
**Translation:** 

**[15467.44s] English:** doesn't matter we all can't deal with it and then like the physical has such a higher premium on it  
**Translation:** 

**[15473.50s] English:** even like uh classic examples i honestly think this is true and i think we'll get  
**Translation:** 

**[15478.20s] English:** tired of it we are already kind of tired  
**Translation:** 

**[15480.00s] English:** of it same with i mean even art i don't think art will go away i mean you have paintings physical  
**Translation:** 

**[15485.66s] English:** paintings there's more value not just monetary value but just more value appreciation for  
**Translation:** 

**[15491.52s] English:** something that is the actual painting than a photocopy of that painting it could be a perfect  
**Translation:** Vocabulary: photocopy: 复印件

**[15495.68s] English:** digital reprint of that but there is something when you go to a museum and you look at that art  
**Translation:** 

**[15500.08s] English:** and you see that real thing and you think about okay a human i don't it's like a craft you have  
**Translation:** 

**[15504.72s] English:** an appreciation for that and i think the same is true for writing for talking for any type of  
**Translation:** 

**[15510.20s] English:** experience where it will be i do unfortunately think it will be like a comment like it will be  
**Translation:** 

**[15516.64s] English:** like a fork where well some things will be automated like you know there are not as many  
**Translation:** 

**[15521.30s] English:** paintings as they used to be 200 years ago there are more more photographs more photocopies but  
**Translation:** Vocabulary: automated: 自动化; photocopies: 复印件

**[15527.16s] English:** at the same time it won't go away there will be a you know value in that i think that the difference  
**Translation:** 

**[15532.96s] English:** will just be a bit you know  
**Translation:** 

**[15534.56s] English:** you know  
**Translation:** 

**[15534.72s] English:** what's the proportion of that but personally i i have a hard time reading things where i  
**Translation:** 

**[15540.40s] English:** obviously see it's um obviously ai generated i'm like sorry it might be really good information  
**Translation:** 

**[15545.84s] English:** there but i have like a certain nah not for me i think eventually they'll fool you and it'll be on  
**Translation:** 

**[15551.54s] English:** platforms that give ways of verifying or building trust so you will trust that lex is not ai  
**Translation:** 

**[15558.48s] English:** generated having been here so then you have trust in this channel but it's harder for new people  
**Translation:** Vocabulary: verifying: 验证

**[15563.82s] English:** that don't have  
**Translation:** 

**[15564.56s] English:** that trust well that will get interesting because i think fundamentally i think there's a solvable  
**Translation:** Vocabulary: fundamentally: 从根本上; solvable: 可解决的

**[15569.84s] English:** problem by having you know trust in certain outlets that they won't do it but it's all going  
**Translation:** 

**[15575.84s] English:** to be kind of trust based there will be some systems to authorize okay this is real this is  
**Translation:** 

**[15579.76s] English:** not real there will be some telltale science where you can obviously tell this is ai generated and  
**Translation:** 

**[15585.04s] English:** this is not but they won't i mean some will be so good that it's hard to tell and then you have  
**Translation:** Vocabulary: telltale: 明显的迹象

**[15589.52s] English:** to trust and um well that that will get interesting and a bit problematic but i think it's going to be  
**Translation:** 

**[15594.40s] English:** the extreme case of this is to watermark all human content so all photos that we take on our own  
**Translation:** 

**[15600.00s] English:** have some watermark until they are edited  
**Translation:** 

**[15602.16s] English:** or something like this and software  
**Translation:** 

**[15604.10s] English:** can manage communications with the  
**Translation:** 

**[15606.14s] English:** device manufacturer  
**Translation:** 

**[15607.90s] English:** to maintain human editing  
**Translation:** 

**[15610.12s] English:** which is the opposite of the  
**Translation:** 

**[15612.10s] English:** discussion to try to watermark AI  
**Translation:** 

**[15614.14s] English:** images and then  
**Translation:** Vocabulary: watermark: 水印

**[15615.68s] English:** you can make a Google image that has a  
**Translation:** 

**[15618.14s] English:** watermark and use a different Google tool to remove  
**Translation:** 

**[15620.24s] English:** the watermark. Yeah, it's going to be  
**Translation:** 

**[15621.86s] English:** a dumb race.  
**Translation:** 

**[15624.26s] English:** We've been mostly focusing on the positive  
**Translation:** 

**[15626.30s] English:** aspects of AI.  
**Translation:** 

**[15627.24s] English:** I mean, there's also  
**Translation:** 

**[15628.50s] English:** all the capabilities we've been talking about can be  
**Translation:** 

**[15631.34s] English:** used to destabilize human civilization  
**Translation:** 

**[15633.10s] English:** with even just  
**Translation:** Vocabulary: destabilize: 破坏稳定

**[15634.74s] English:** relatively dumb AI  
**Translation:** 

**[15636.72s] English:** applied at scale  
**Translation:** 

**[15638.56s] English:** and then further and further super intelligent  
**Translation:** 

**[15641.38s] English:** AI systems. Of course  
**Translation:** 

**[15643.30s] English:** there's the sort of doomer take  
**Translation:** 

**[15645.08s] English:** that's important to consider  
**Translation:** 

**[15647.28s] English:** a little bit as we  
**Translation:** 

**[15649.22s] English:** develop these technologies.  
**Translation:** 

**[15650.80s] English:** What gives you hope about the future of human  
**Translation:** 

**[15653.30s] English:** civilization? Everything we've been talking  
**Translation:** 

**[15655.34s] English:** about.  
**Translation:** 

**[15657.24s] English:** Are we going to be okay?  
**Translation:** 

**[15658.94s] English:** I think we will. I'm definitely  
**Translation:** 

**[15661.28s] English:** a worrier both about AI  
**Translation:** 

**[15663.42s] English:** and non-AI things but  
**Translation:** 

**[15665.30s] English:** humans do  
**Translation:** 

**[15667.48s] English:** tend to find a way. I think that's  
**Translation:** 

**[15669.58s] English:** what humans are built for  
**Translation:** 

**[15671.30s] English:** is to have community and find a way  
**Translation:** 

**[15673.34s] English:** to figure out problems and that's what has gotten  
**Translation:** 

**[15675.40s] English:** us to this point.  
**Translation:** 

**[15677.20s] English:** I think that the AI  
**Translation:** 

**[15679.46s] English:** opportunity in related  
**Translation:** 

**[15681.18s] English:** technologies is really big  
**Translation:** 

**[15683.22s] English:** and I think that there's big  
**Translation:** 

**[15685.22s] English:** social and political problems  
**Translation:** 

**[15687.12s] English:** to deal with.  
**Translation:** 

**[15687.24s] English:** To help  
**Translation:** 

**[15688.44s] English:** everybody understand that and I think  
**Translation:** 

**[15691.00s] English:** that's what we're staring at a lot of right now.  
**Translation:** 

**[15693.04s] English:** The world is a scary place and AI  
**Translation:** 

**[15695.14s] English:** is a very uncertain thing  
**Translation:** 

**[15696.58s] English:** and it takes a lot of work that is  
**Translation:** 

**[15698.88s] English:** not necessarily building  
**Translation:** 

**[15701.02s] English:** things. It's like telling people  
**Translation:** 

**[15703.10s] English:** and understanding people that  
**Translation:** 

**[15704.90s] English:** the people building AI are historically not  
**Translation:** 

**[15707.20s] English:** motivated or wanting  
**Translation:** Vocabulary: historically: 历史上

**[15709.12s] English:** to do but  
**Translation:** 

**[15710.30s] English:** it is something that is probably doable  
**Translation:** Vocabulary: doable: 可实现的

**[15713.28s] English:** and just will take longer than  
**Translation:** 

**[15715.14s] English:** people want. We have to go through  
**Translation:** 

**[15717.12s] English:** that long period of  
**Translation:** 

**[15718.66s] English:** hard  
**Translation:** 

**[15720.00s] English:** distraught ai discussions if we want to have the lasting benefits yeah through that process i'm  
**Translation:** 

**[15726.32s] English:** especially excited that we get a chance uh to better understand ourselves also at the individual  
**Translation:** Vocabulary: distraught: 心神不安

**[15733.28s] English:** level as humans and at the civilization level answer some of the big mysteries like what is  
**Translation:** 

**[15739.60s] English:** this whole like consciousness thing going on here seems to be truly special like there's a real  
**Translation:** 

**[15745.76s] English:** miracle in our mind and ai puts a mirror to ourselves and get to answer some of the big  
**Translation:** 

**[15751.76s] English:** questions about like what what is this whole thing going on here well one thing about that  
**Translation:** 

**[15756.72s] English:** is also what i do think uh makes us very different from ai and why i don't worry about ai taking over  
**Translation:** 

**[15763.60s] English:** is like you said consciousness we humans we decide what we want to do ai in its current  
**Translation:** 

**[15769.52s] English:** implementation i can't see it changing you have to tell it what to do and so you have still the  
**Translation:** 

**[15775.60s] English:** agency you have to you know the the human being that has the same the same the same the same thing  
**Translation:** Vocabulary: implementation: 执行

**[15775.76s] English:** agency it doesn't take the agency from you because you have to you just it becomes a tool you can  
**Translation:** 

**[15780.88s] English:** think of it as a tool you tell it what to do it will be more automatic than other previous tools  
**Translation:** 

**[15786.74s] English:** it's certainly more powerful than a hammer it can figure things out but it's still you in in in  
**Translation:** 

**[15792.66s] English:** charge right so the ai is not in charge you're in charge you tell the ai what to do and it's doing  
**Translation:** 

**[15796.82s] English:** it for you so in the post-singularity post-apocalyptic war between humans and machines  
**Translation:** 

**[15802.70s] English:** you're saying humans are worth fighting for 100 i mean this is the movie terminator they  
**Translation:** Vocabulary: terminator: 终结者

**[15811.50s] English:** made in the 80s essentially and i do think well the only thing i can see going wrong is of course  
**Translation:** 

**[15818.26s] English:** if things are explicitly programmed to do the thing that is harmful basically i think actually  
**Translation:** Vocabulary: explicitly: 明确地

**[15824.06s] English:** in that in a terminator type of setup i think humans win i think we're too clever  
**Translation:** 

**[15830.28s] English:** uh  
**Translation:** Vocabulary: setup: 设置

**[15832.70s] English:** it's hard to explain how we figure it out but we do and uh we'll probably be using local llms  
**Translation:** 

**[15840.00s] English:** open-source LLMs to help fight the machines.  
**Translation:** 

**[15844.28s] English:** I apologize for the ridiculousness.  
**Translation:** 

**[15846.82s] English:** Like I said, Nathan already knows  
**Translation:** Vocabulary: ridiculousness: 荒谬性

**[15848.72s] English:** I've been a big fan of his for a long time.  
**Translation:** 

**[15851.42s] English:** I've been a big fan of yours, Sebastian, for a long time.  
**Translation:** Vocabulary: sebastian: 赛巴斯蒂安

**[15854.04s] English:** So it's an honor to finally meet you.  
**Translation:** 

**[15856.32s] English:** Thank you for everything you put out into the world.  
**Translation:** 

**[15858.24s] English:** Thank you for the excellent books you're writing.  
**Translation:** 

**[15860.04s] English:** Thank you for teaching us.  
**Translation:** 

**[15862.92s] English:** And thank you for talking today.  
**Translation:** 

**[15865.16s] English:** This was fun.  
**Translation:** 

**[15865.72s] English:** Thank you for inviting us here  
**Translation:** 

**[15867.86s] English:** and having this human connection.  
**Translation:** 

**[15870.00s] English:** This was an extremely valuable human connection.  
**Translation:** 

**[15873.48s] English:** Thanks for listening to this conversation  
**Translation:** 

**[15875.18s] English:** with Sebastian Raschke and Nathan Lambert.  
**Translation:** 

**[15878.28s] English:** To support this podcast,  
**Translation:** Vocabulary: lambert: 拉姆伯特; nathan: 内森

**[15879.60s] English:** please check out our sponsors in the description  
**Translation:** 

**[15881.34s] English:** where you can also find links to contact me,  
**Translation:** Vocabulary: sponsors: 赞助商

**[15884.08s] English:** ask questions, give feedback, and so on.  
**Translation:** 

**[15887.40s] English:** And now, let me leave you with some words  
**Translation:** 

**[15889.62s] English:** from Albert Einstein.  
**Translation:** 

**[15892.04s] English:** It is not that I'm so smart,  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[15894.02s] English:** but I stay with the questions much longer.  
**Translation:** 

**[15899.12s] English:** Thank you for listening.  
**Translation:** 

**[15900.00s] English:** And hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
