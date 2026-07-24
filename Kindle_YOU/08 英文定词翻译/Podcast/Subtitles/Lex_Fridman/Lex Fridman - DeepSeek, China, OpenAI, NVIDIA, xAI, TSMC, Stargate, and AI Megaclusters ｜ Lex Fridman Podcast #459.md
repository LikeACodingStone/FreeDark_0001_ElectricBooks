# Podcast vocabulary notes
Source file: Lex Fridman - DeepSeek, China, OpenAI, NVIDIA, xAI, TSMC, Stargate, and AI Megaclusters ｜ Lex Fridman Podcast #459.opus

**[0.00s] English:** The following is a conversation with Dylan Patel and Nathan Lampert.  
**Translation:** 

**[4.64s] English:** Dylan runs SemiAnalysis, a well-respected research and analysis company that specializes in semiconductors, GPUs, CPUs, and AI hardware in general.  
**Translation:** 

**[16.98s] English:** Nathan is a research scientist at the Allen Institute for AI and is the author of the amazing blog on AI called Interconnects.  
**Translation:** 

**[26.48s] English:** They are both highly respected, read, and listened to by the experts, researchers, and engineers in the field of AI.  
**Translation:** Vocabulary: interconnects: 连接网络

**[34.82s] English:** And personally, I'm just a fan of the two of them.  
**Translation:** 

**[37.90s] English:** So I used the deep-seek moment that shook the AI world a bit as an opportunity to sit down with them and lay it all out.  
**Translation:** 

**[47.64s] English:** From deep-seek OpenAI, Google, XAI, Meta, Anthropic, to NVIDIA and TSMC, and to US, China, Taiwan.  
**Translation:** 

**[56.48s] English:** They are both highly respected, read, and listened to by the experts, researchers, and engineers in the field of AI.  
**Translation:** Vocabulary: taiwan: 台湾

**[60.78s] English:** This conversation is a deep dive into many critical aspects of the AI industry.  
**Translation:** 

**[67.44s] English:** While it does get super technical, we try to make sure that it's still accessible to folks outside of the AI field by defining terms, stating important concepts explicitly, spelling out acronyms, and, in general, always moving across the several layers of abstraction and levels of detail.  
**Translation:** Vocabulary: abstraction: 抽象; acronyms: 缩写; explicitly: 明确地

**[86.48s] English:** There is a lot of hype in the media about what AI is and isn't.  
**Translation:** 

**[91.94s] English:** The purpose of this podcast, in part, is to cut through the hype, through the bullshit, and the low-resolution analysis, and to discuss in detail how stuff works and what the implications are.  
**Translation:** Vocabulary: bullshit: 胡说八道

**[106.08s] English:** Let me also, if I may, comment on the new OpenAI 03 Mini reasoning model, the release of which we were anticipating during the conversation.  
**Translation:** 

**[115.42s] English:** And it did increase.  
**Translation:** Vocabulary: anticipating: 预期

**[116.48s] English:** It did come out right after.  
**Translation:** 

**[117.56s] English:** Its capabilities and cost.  
**Translation:** 

**[120.00s] English:** are on par with our expectations, as we stated.  
**Translation:** 

**[124.72s] English:** OpenAI O3 Mini is indeed a great model.  
**Translation:** 

**[127.86s] English:** But it should be stated that DeepSeek R1 has similar performance on benchmarks,  
**Translation:** 

**[132.68s] English:** is still cheaper, and it reveals its chain-of-thought reasoning, which O3 Mini does not.  
**Translation:** Vocabulary: benchmarks: 测试基准

**[139.44s] English:** It only shows a summary of the reasoning.  
**Translation:** 

**[142.86s] English:** Plus, R1 is open weight, and O3 Mini is not.  
**Translation:** 

**[147.68s] English:** By the way, I got a chance to play with O3 Mini.  
**Translation:** 

**[152.66s] English:** And anecdotal vibe-check-wise, I felt that O3 Mini, specifically O3 Mini High, is better than R1.  
**Translation:** Vocabulary: anecdotal: 轶事的

**[161.68s] English:** Still, for me personally, I find that ClaudeSana 3.5 is the best model for programming,  
**Translation:** 

**[167.56s] English:** except for tricky cases where I will use O1 Pro to brainstorm.  
**Translation:** 

**[171.92s] English:** Either way, many more better AI models will come, including reasoning models,  
**Translation:** 

**[177.02s] English:** both from OpenAI.  
**Translation:** 

**[177.68s] English:** American and Chinese companies.  
**Translation:** 

**[180.12s] English:** They will continue to shift the cost curve.  
**Translation:** 

**[183.44s] English:** But the, quote, DeepSeek moment is indeed real.  
**Translation:** 

**[187.72s] English:** I think it will still be remembered five years from now as a pivotal event in tech history,  
**Translation:** Vocabulary: pivotal: 关键的

**[193.06s] English:** due in part to the geopolitical implications, but for other reasons, too,  
**Translation:** 

**[198.30s] English:** as we discuss in detail from many perspectives in this conversation.  
**Translation:** Vocabulary: geopolitical: 地缘政治; perspectives: 视角

**[202.12s] English:** This is the Lex Friedman Podcast.  
**Translation:** 

**[203.94s] English:** To support it, please check out our sponsors in the description.  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[207.68s] English:** And now, dear friends, here's Dylan Patel and Nathan Lambert.  
**Translation:** 

**[213.32s] English:** A lot of people are curious to understand China's DeepSeek AI models.  
**Translation:** 

**[217.48s] English:** So let's lay it out.  
**Translation:** 

**[218.96s] English:** Nathan, can you describe what DeepSeek V3 and DeepSeek R1 are, how they work, how they're trained?  
**Translation:** 

**[225.54s] English:** Let's look at the big picture, and then we'll zoom in on the details.  
**Translation:** 

**[228.96s] English:** Yeah, so DeepSeek V3 is a new mixture of experts, transformer language model from DeepSeek,  
**Translation:** 

**[236.78s] English:** who is based in China.  
**Translation:** 

**[238.92s] English:** They have some...  
**Translation:** 

**[240.00s] English:** new specifics in the model that we'll get into largely this is a open weight model and it's a  
**Translation:** 

**[247.12s] English:** instruction model like what you would use in chat gpt they also release what is called the base  
**Translation:** 

**[252.80s] English:** model which is before these techniques of post-training most people use instruction  
**Translation:** 

**[257.58s] English:** models today and those are what's served in all sorts of applications this was released on i  
**Translation:** 

**[263.28s] English:** believe december 26th or that week and then weeks later on january 20th deep seek released deep seek  
**Translation:** 

**[272.30s] English:** r1 which is a reasoning model which really accelerated a lot of this discussion this  
**Translation:** Vocabulary: accelerated: 加速

**[278.84s] English:** reasoning model it has a lot of overlapping training steps to deep seek v3 and it's confusing  
**Translation:** 

**[284.28s] English:** that you have a base model called v3 that you do something to to get a chat model and then you do  
**Translation:** Vocabulary: overlapping: 重叠

**[290.86s] English:** some different things to get a reasoning model  
**Translation:** 

**[293.14s] English:** i think a lot of the ai industry is going through this challenge of communications right now where  
**Translation:** 

**[297.60s] English:** open ai makes fun of their own naming schemes they have gpt 40 they have open ai 01 and there's a lot  
**Translation:** 

**[305.26s] English:** of types of models so we're going to break down what each of them are there's a lot of technical  
**Translation:** 

**[309.68s] English:** specifics on training and go from high level to specific and kind of go through each of them  
**Translation:** 

**[314.68s] English:** there's so many places we can go here but maybe let's go to open weights first what does it mean  
**Translation:** 

**[319.78s] English:** for a model to be open weights and what are the different flavors of open source in general  
**Translation:** 

**[323.14s] English:** yeah so this discussion has been going on for a long time in ai it became more important since  
**Translation:** 

**[328.64s] English:** chat gpt or more focal since chat gpt at the end of 2022 open weights is the accepted term for  
**Translation:** 

**[334.84s] English:** when model weights of a language model are available on the internet for people to download  
**Translation:** 

**[340.04s] English:** those weights can have different licenses which is the effectively the terms by which you can  
**Translation:** 

**[345.52s] English:** use the model there are licenses that come from history and open source software there are licenses  
**Translation:** 

**[350.46s] English:** that are designed by companies specifically  
**Translation:** 

**[353.14s] English:** um all of llama deep seek quen mistral these popular names in  
**Translation:** Vocabulary: llama: 羊驼

**[360.00s] English:** open weight models have some of their own licenses it's complicated because not all the same models  
**Translation:** 

**[365.12s] English:** have the same terms the big debate is on what makes a model open weight it's like why are we  
**Translation:** 

**[372.82s] English:** saying this term it's kind of a mouthful it sounds close to open source but it's not the same there's  
**Translation:** 

**[377.88s] English:** still a lot of debate on the definition and soul of open source ai open source software has a rich  
**Translation:** 

**[383.64s] English:** history on freedom to modify freedom to take on your own freedom from any restrictions on how you  
**Translation:** 

**[389.38s] English:** would use the software and what that means for ai is still being defined so uh for what i do i work  
**Translation:** 

**[397.84s] English:** at the allen institute for ai we're a non-profit we want to make ai open for everybody and we try  
**Translation:** 

**[403.28s] English:** to lead on what we think is truly open source there's not full agreement in the community  
**Translation:** 

**[407.22s] English:** but for us that means releasing the training data releasing the training code and then also having  
**Translation:** 

**[412.58s] English:** open weights like this and we'll get into the details of the models and again and again as we  
**Translation:** 

**[418.88s] English:** try to get  
**Translation:** 

**[419.32s] English:** you  
**Translation:** 

**[419.36s] English:** you  
**Translation:** 

**[419.38s] English:** to get deeper into how the models will train we're trained we will say things like the data  
**Translation:** 

**[424.32s] English:** processing data filtering data quality is the number one determinant of the model quality and  
**Translation:** 

**[429.68s] English:** then a lot of the training code is the determinant on how long it takes to train and how fast your  
**Translation:** Vocabulary: determinant: 决定因素

**[434.88s] English:** experimentation is so without fully open source models where you have access to this data it is  
**Translation:** 

**[441.80s] English:** hard to know or it's harder to replicate so we'll get into cost numbers for deepseek v3 on mostly gpu  
**Translation:** Vocabulary: experimentation: 实验

**[448.64s] English:** hours and  
**Translation:** 

**[449.36s] English:** how much you could  
**Translation:** 

**[450.54s] English:** pay to rent those yourselves but without the data the replication cost is going to be far far higher and same goes for the code we should also say that this is probably one of the more open models out of the frontier models it's like.  
**Translation:** 

**[465.12s] English:** In this full spectrum where probably the fullest open source like you said open code open data open weights this is not open code this is probably not open data.  
**Translation:** Vocabulary: frontier: 最前沿; yourselves: 你们自己

**[478.62s] English:** And  
**Translation:** 

**[480.00s] English:** And this is open weights and the licensing is MIT license or it's I mean, there's some nuance in the different models, but it's towards the free in terms of the open source movement.  
**Translation:** Vocabulary: nuance: 细微差别

**[491.72s] English:** These are the kind of the good guys.  
**Translation:** 

**[493.26s] English:** Yeah, DeepSeek is doing fantastic work for disseminating understanding of AI.  
**Translation:** Vocabulary: disseminating: 传播

**[498.50s] English:** Their papers are extremely detailed in what they do.  
**Translation:** 

**[502.30s] English:** And for other teams around the world, they're very actionable in terms of improving your own training techniques.  
**Translation:** 

**[510.52s] English:** And we'll talk about licenses more.  
**Translation:** 

**[513.50s] English:** The DeepSeek R1 model has a very permissive license.  
**Translation:** Vocabulary: permissive: 宽容的

**[517.04s] English:** It's called the MIT license.  
**Translation:** 

**[518.32s] English:** That effectively means there's no downstream restrictions on commercial use.  
**Translation:** 

**[522.06s] English:** There's no use case restrictions.  
**Translation:** 

**[524.04s] English:** You can use the outputs from the models to create synthetic data.  
**Translation:** Vocabulary: synthetic: 合成的

**[527.58s] English:** And this is all fantastic.  
**Translation:** 

**[529.78s] English:** I think the closest peer is something like LAMA, where you have the weights and you have a technical report.  
**Translation:** 

**[535.70s] English:** And the technical report is very good for LAMA.  
**Translation:** 

**[538.64s] English:** One of the most read PDFs of the year.  
**Translation:** 

**[540.00s] English:** Last year is the LAMA 3 paper.  
**Translation:** 

**[542.22s] English:** But in some ways, it's slightly less actionable.  
**Translation:** 

**[544.56s] English:** It has less details on the training specifics and less plots and so on.  
**Translation:** 

**[549.46s] English:** And the LAMA 3 license is more restrictive than MIT.  
**Translation:** 

**[553.08s] English:** And then between the DeepSeek custom license and the LAMA license, we can get into this whole rabbit hole.  
**Translation:** 

**[557.56s] English:** I think we'll make sure we want to go down the license rabbit hole before we do specifics.  
**Translation:** 

**[561.46s] English:** Yeah.  
**Translation:** 

**[562.06s] English:** And I mean, so it should be stated that one of the implications of DeepSeek, it puts pressure on LAMA and everybody else on OpenAI.  
**Translation:** 

**[568.84s] English:** To push towards open source.  
**Translation:** 

**[572.04s] English:** And that's the other side of open source that you mentioned is how much is published in detail about it.  
**Translation:** 

**[577.38s] English:** So how open are you with the sort of the insights behind the code?  
**Translation:** 

**[582.78s] English:** So like, how good is the technical reports?  
**Translation:** 

**[585.62s] English:** Are they hand wavy or is there actual details in there?  
**Translation:** 

**[588.88s] English:** And that's one of the things that DeepSeek did well is they published a lot of the details.  
**Translation:** 

**[592.54s] English:** Yeah, especially in the DeepSeek V3, which is their pre-training paper.  
**Translation:** 

**[595.84s] English:** They were very clear that they are doing.  
**Translation:** 

**[598.84s] English:** So they're very clear that you can do a lot more with  
**Translation:** 

**[627.42s] English:** a traditional software.  
**Translation:** 

**[628.14s] English:** A lot of the time, they don't kind of say, you know, like, hey, you can do all these different things with, like, an open source document.  
**Translation:** 

**[628.38s] English:** So they're very clear that they're handling it very well.  
**Translation:** 

**[628.76s] English:** And then, of course, they're doing a lot of other things.  
**Translation:** 

**[600.00s] English:** technical stack that go at many different levels. For example, to get highly efficient training,  
**Translation:** 

**[606.24s] English:** they're making modifications at or below the CUDA layer for NVIDIA chips. I have never worked  
**Translation:** 

**[612.84s] English:** there myself, and there are a few people in the world that do that very well, and some of them  
**Translation:** Vocabulary: modifications: 修改

**[616.72s] English:** are at DeepSeq. And these types of people are at DeepSeq and leading American frontier labs,  
**Translation:** 

**[623.28s] English:** but there are not many places. To help people understand the other  
**Translation:** Vocabulary: frontier: 前沿

**[627.02s] English:** implication of open weights, there's a topic we return to often here. So there's a fear that  
**Translation:** 

**[636.98s] English:** China, the nation, might have interest in stealing American data, violating privacy of American  
**Translation:** Vocabulary: implication: 暗示; violating: 侵犯

**[644.54s] English:** citizens. What can we say about open weights to help us understand what the weights are able to do  
**Translation:** 

**[651.50s] English:** in terms of stealing people's data? Yeah, so these weights that you can  
**Translation:** 

**[656.40s] English:** download from Hugging.com.  
**Translation:** 

**[657.02s] English:** or other platforms are very big matrices of numbers. You can download them to a computer  
**Translation:** Vocabulary: matrices: 数值矩阵

**[662.98s] English:** in your own house that has no internet, and you can run this model, and you're totally in control  
**Translation:** 

**[667.08s] English:** of your data. That is something that is different than how a lot of language model usage is actually  
**Translation:** 

**[673.48s] English:** done today, which is mostly through APIs, where you send your prompt to GPUs run by certain  
**Translation:** 

**[678.72s] English:** companies. And these companies will have different distributions and policies on how your data is  
**Translation:** 

**[682.92s] English:** stored, if it is used to train future models, where it is stored, if it is encrypted, and so on.  
**Translation:** 

**[687.02s] English:** So the open weights are, you have your fate of data in your own hands, and that is something that is  
**Translation:** Vocabulary: encrypted: 加密存储

**[694.24s] English:** deeply connected to the soul of open source. So it's not the model that steals your data,  
**Translation:** 

**[699.34s] English:** it's Clover's hosting the model, which could be China, if you're using the DeepSeek app,  
**Translation:** 

**[704.34s] English:** or it could be Perplexity. You're trusting them with your data, or OpenAI, you're trusting them  
**Translation:** 

**[710.64s] English:** with your data. And some of these are American companies, some of these are Chinese companies,  
**Translation:** Vocabulary: perplexity: 困惑

**[713.84s] English:** but the model itself is not doing the stealing.  
**Translation:** 

**[717.02s] English:** It's the host. All right.  
**Translation:** 

**[720.00s] English:** So back to the basics. What's the difference between DeepSeq v3 and DeepSeq R1? Can we try to  
**Translation:** 

**[727.80s] English:** lay out the confusion potential? Yes. So for one, I have very understanding of many people being  
**Translation:** 

**[734.92s] English:** confused by these two model names. So I would say the best way to think about this is that  
**Translation:** 

**[739.58s] English:** when training a language model, you have what is called pre-training, which is when you're  
**Translation:** 

**[743.06s] English:** predicting the large amounts of mostly internet text. You're trying to predict the next token.  
**Translation:** 

**[748.50s] English:** And what to know about these new DeepSeq models is that they do this internet large-scale  
**Translation:** Vocabulary: token: 标记

**[754.84s] English:** pre-training once to get what is called DeepSeq v3 base. This is a base model. It's just going  
**Translation:** 

**[760.90s] English:** to finish your sentences for you. It's going to be harder to work with than ChatGPT. And then  
**Translation:** 

**[766.30s] English:** what DeepSeq did is they've done two different post-training regimes to make the models have  
**Translation:** 

**[772.82s] English:** specific desirable behaviors. So what is the more normal model in terms of  
**Translation:** Vocabulary: desirable: 令人满意的

**[777.94s] English:** the language model?  
**Translation:** 

**[778.50s] English:** The last few years of AI, an instruct model, a chat model, a quote-unquote aligned model,  
**Translation:** Vocabulary: aligned: 对齐; instruct: 指令

**[783.10s] English:** a helpful model, there are many ways to describe this, is more standard post-training. So this is  
**Translation:** 

**[788.72s] English:** things like instruction tuning, reinforced learning from human feedback. We'll get into  
**Translation:** Vocabulary: reinforced: 强化

**[792.38s] English:** some of these words. And this is what they did to create the DeepSeq v3 model. This was the first  
**Translation:** 

**[798.34s] English:** model to be released, and it is very high-performance. It's competitive with GPT-4,  
**Translation:** 

**[805.16s] English:** LAMA-405b, so on.  
**Translation:** 

**[807.06s] English:** And then when this release was happening, we don't know their exact timeline, or soon after,  
**Translation:** 

**[813.12s] English:** they were finishing the training of a different training process from the same  
**Translation:** 

**[817.36s] English:** next token prediction base model that I talked about, which is when this new reasoning training  
**Translation:** 

**[823.02s] English:** that people have heard about comes in, in order to create the model that is called DeepSeq R1.  
**Translation:** 

**[828.42s] English:** The R through this conversation is good for grounding for reasoning,  
**Translation:** 

**[831.26s] English:** and the name is also similar to OpenAI's O1, which is the other reasoning model that people  
**Translation:** 

**[835.76s] English:** have heard about.  
**Translation:** 

**[837.06s] English:** And we'll have to break down the training for R1.  
**Translation:** 

**[840.00s] English:** on in more detail because for one, we have a paper detailing it, but also it is a far newer  
**Translation:** 

**[845.62s] English:** set of techniques for the AI community. So it's a much more rapidly evolving area of research.  
**Translation:** 

**[852.04s] English:** Maybe we should also say the big two categories of training of pre-training and post-training,  
**Translation:** Vocabulary: evolving: 发展中的

**[858.44s] English:** these umbrella terms that people use. So what is pre-training and what is post-training and  
**Translation:** 

**[864.78s] English:** what are the different flavors of things underneath post-training umbrella?  
**Translation:** 

**[867.54s] English:** Yeah. So pre-training, I'm using some of the same words to really get the message across is  
**Translation:** 

**[871.92s] English:** you're doing what is called autoregressive prediction to predict the next token in a  
**Translation:** Vocabulary: autoregressive: 自回归; token: 标记

**[875.94s] English:** series of documents. This is done over standard practices, trillions of tokens. So this is a ton  
**Translation:** 

**[883.00s] English:** of data that is mostly scraped from the web. And some of DeepSeek's earlier papers, they talk about  
**Translation:** Vocabulary: scraped: 从网上抓取; trillions: 万亿

**[889.76s] English:** their training data being distilled for math. I shouldn't use this word yet, but taken from  
**Translation:** 

**[895.22s] English:** Common Crawl. And that's a  
**Translation:** Vocabulary: distilled: 提炼

**[897.52s] English:** public access that anyone listening to this could go download data from the Common Crawl website.  
**Translation:** 

**[902.06s] English:** This is a crawler that is maintained publicly. Yes, other tech companies eventually shift to  
**Translation:** 

**[906.74s] English:** their own crawler and DeepSeek likely has done this as well as most frontier labs do.  
**Translation:** 

**[911.30s] English:** But this sort of data is something that people can get started with. And you're just predicting  
**Translation:** Vocabulary: frontier: 前沿技术

**[915.68s] English:** text in a series of documents. This can be scaled to be very efficient. And there's a lot of numbers  
**Translation:** 

**[924.50s] English:** that are thrown around in AI training, like how many floating point,  
**Translation:** 

**[927.52s] English:** operations or flops are used. And then you can also look at how many hours of these GPUs  
**Translation:** 

**[933.18s] English:** that are used. And it's largely one loss function taken to a very large amount of  
**Translation:** Vocabulary: flops: 运算次数

**[941.42s] English:** compute usage. You just set up really efficient systems. And then at the end of that, you have  
**Translation:** 

**[946.58s] English:** this base model. And pre-training is where there is a lot more of complexity in terms of how the  
**Translation:** Vocabulary: complexity: 复杂性

**[953.70s] English:** process is emerging or evolving. And there's a lot more complexity in terms of how the process is  
**Translation:** 

**[957.52s] English:** emerging. And there's a lot more complexity in terms of how the different types of training  
**Translation:** 

**[958.54s] English:** losses that you will use.  
**Translation:** 

**[960.00s] English:** I think this is a lot of techniques grounded in the natural language processing literature.  
**Translation:** 

**[965.72s] English:** The oldest technique, which is still used today, is something called instruction tuning or also known as supervised fine tuning.  
**Translation:** 

**[972.16s] English:** These acronyms will be IFT or SFT.  
**Translation:** Vocabulary: acronyms: 缩写; supervised: 监督

**[975.72s] English:** People really go back and forth throughout them, and I will probably do the same, which is where you add this formatting to the model where it knows to take a question that is like, explain the history of the Roman Empire to me.  
**Translation:** 

**[989.50s] English:** And or something, a sort of question you'll see on Reddit or Stack Overflow, and then the model will respond in a information dense but presentable manner.  
**Translation:** Vocabulary: formatting: 格式化; overflow: 溢出; presentable: 可展示的

**[998.82s] English:** The core of that formatting is in this instruction tuning phase.  
**Translation:** 

**[1001.78s] English:** And then there's two other categories of loss functions that are being used today.  
**Translation:** 

**[1007.22s] English:** One I will classify as preference fine tuning.  
**Translation:** 

**[1010.00s] English:** Preference fine tuning is a generalized term for what came out of reinforcement learning from human feedback, which is RLHF.  
**Translation:** Vocabulary: classify: 分类; generalized: 泛化; reinforcement: 强化

**[1017.36s] English:** This reinforcement learning.  
**Translation:** 

**[1019.50s] English:** From human feedback is credited as the technique that helped chat GPT breakthrough.  
**Translation:** 

**[1025.94s] English:** It is a technique to make the responses that are nicely formatted, like these Reddit answers, more in tune with what a human would like to read.  
**Translation:** 

**[1034.26s] English:** This is done by collecting pairwise preferences from actual humans out in the world to start.  
**Translation:** Vocabulary: formatted: 排版整齐; pairwise: 成对地

**[1039.52s] English:** And now AIs are also labeling this data and we'll get into those tradeoffs.  
**Translation:** 

**[1043.56s] English:** And you have this kind of contrastive loss function between a good answer and a bad answer.  
**Translation:** Vocabulary: labeling: 标注; tradeoffs: 权衡

**[1048.62s] English:** And the model.  
**Translation:** 

**[1049.38s] English:** Learns to pick up these trends.  
**Translation:** 

**[1051.08s] English:** There's different implementation ways you have things called reward models.  
**Translation:** 

**[1055.06s] English:** You could have direct alignment algorithms.  
**Translation:** Vocabulary: alignment: 对齐; implementation: 实施

**[1056.90s] English:** There's a lot of really specific things you can do, but all of this is about fine tuning to human preferences.  
**Translation:** 

**[1062.74s] English:** And the final stage is much newer and will link to what is done in our one.  
**Translation:** 

**[1068.00s] English:** And these reasoning models is, I think, open AIs name for this.  
**Translation:** 

**[1072.16s] English:** They had this new API in the fall, which they called the reinforcement fine tuning API.  
**Translation:** 

**[1077.36s] English:** This is the idea that you use the techniques.  
**Translation:** 

**[1079.38s] English:** Of reinforcement.  
**Translation:** 

**[1080.00s] English:** learning, which is a whole framework of AI. There's a deep literature here to summarize.  
**Translation:** 

**[1085.46s] English:** It's often known as trial and error learning or the subfield of AI where you're trying to  
**Translation:** 

**[1090.58s] English:** make sequential decisions in a certain potentially noisy environment. There's a lot of ways we could  
**Translation:** 

**[1096.98s] English:** go down that, but fine-tuning language models where they can generate an answer and then you  
**Translation:** Vocabulary: sequential: 顺序的

**[1102.46s] English:** check to see if the answer matches the true solution. For math or code, you have an exactly  
**Translation:** 

**[1108.18s] English:** correct answer for math. You can have unit tests for code. And what we're doing is we are checking  
**Translation:** 

**[1113.00s] English:** the language models work and we're giving it multiple opportunities on the same questions  
**Translation:** 

**[1116.92s] English:** to see if it is right. And if you keep doing this, the models can learn to improve in verifiable  
**Translation:** Vocabulary: verifiable: 可验证的

**[1121.66s] English:** domains to a great extent. It works really well. It's a newer technique in the academic literature.  
**Translation:** 

**[1127.42s] English:** It's been used at frontier labs in the U.S. that don't share every detail for multiple years. So  
**Translation:** Vocabulary: frontier: 前沿

**[1133.38s] English:** this is the idea of using reinforcement learning with language models, and it has  
**Translation:** 

**[1138.00s] English:** been used in the U.S. for multiple years. So this is the idea of using reinforcement learning with  
**Translation:** Vocabulary: reinforcement: 强化

**[1138.16s] English:** language models. And we should say that there's a lot of exciting stuff going on on the,  
**Translation:** 

**[1144.32s] English:** again, across the stack, but the post-training probably this year, there's going to be a lot  
**Translation:** 

**[1148.70s] English:** of interesting developments in the post-training. We'll talk about it. I almost forgot to talk  
**Translation:** 

**[1153.38s] English:** about the difference between DeepSeq v3 and R1 on the user experience side. So  
**Translation:** 

**[1158.28s] English:** forget the technical stuff, forget all that. Just people that don't know anything about AI,  
**Translation:** 

**[1163.50s] English:** they show up. Like, what's the actual experience? What's the use case for each one when they  
**Translation:** 

**[1167.98s] English:** actually like type and talk to it what is each good at and that kind of thing so let's start with  
**Translation:** 

**[1172.56s] English:** deep seek v3 again it's what more people would have tried something like it you ask it a question  
**Translation:** 

**[1176.98s] English:** it'll start generating tokens very fast and those tokens will look like a very human legible answer  
**Translation:** 

**[1183.94s] English:** it'll be some sort of markdown list it might have formatting to help you draw to the core details in  
**Translation:** Vocabulary: formatting: 排版; markdown: 标记语言

**[1191.18s] English:** the answer and it'll generate tens to hundreds of tokens a token is normally a word for common  
**Translation:** 

**[1198.24s] English:** words or a subword part  
**Translation:** Vocabulary: token: 一个词或子词单元

**[1200.00s] English:** in a longer word. And it'll look like a very high quality Reddit or Stack Overflow answer.  
**Translation:** 

**[1206.92s] English:** These models are really getting good at doing these across a wide variety of domains. Even  
**Translation:** Vocabulary: overflow: 溢出

**[1212.48s] English:** things that if you're an expert, things that are close to the fringe of knowledge, they will still  
**Translation:** 

**[1217.68s] English:** be fairly good at. Cutting edge AI topics that I do research on, these models are capable for  
**Translation:** Vocabulary: fringe: 边缘领域

**[1224.92s] English:** study aid, and they're regularly updated. Where this changes is with the DeepSeq R1,  
**Translation:** 

**[1231.46s] English:** what is called these reasoning models, is when you see tokens coming from these models to start,  
**Translation:** 

**[1236.36s] English:** it will be a large chain of thought process. We'll get back to chain of thought in a second,  
**Translation:** 

**[1242.50s] English:** which looks like a lot of tokens where the model is explaining the problem. The model will often  
**Translation:** 

**[1247.66s] English:** break down the problem and be like, okay, they asked me for this. Let's break down the problem.  
**Translation:** 

**[1251.96s] English:** I'm going to need to do this. And you'll see all of this generated,  
**Translation:** 

**[1254.92s] English:** from the model. It'll come very fast in most user experiences. These APIs are very fast. So you'll  
**Translation:** 

**[1259.64s] English:** see a lot of tokens, a lot of words show up really fast. It'll keep flowing on the screen. And this  
**Translation:** 

**[1264.14s] English:** is all the reasoning process. And then eventually the model will change its tone in R1, and it'll  
**Translation:** 

**[1269.40s] English:** write the answer where it summarizes its reasoning process and writes a similar answer to the first  
**Translation:** Vocabulary: summarizes: 总结

**[1275.30s] English:** types of model. But in DeepSeq's case, which is part of why this was so popular, even outside  
**Translation:** 

**[1281.92s] English:** the AI community, is that you can see how the language model,  
**Translation:** 

**[1284.92s] English:** is breaking down problems. And then you get this answer on a technical side. They train the model  
**Translation:** 

**[1290.46s] English:** to do this specifically where they have a section, which is reasoning, and then it generates a  
**Translation:** 

**[1294.30s] English:** special token, which is probably hidden from the user most of the time, which says, okay,  
**Translation:** 

**[1297.60s] English:** I'm starting the answer. So the model is trained to do this two-stage process on its own.  
**Translation:** 

**[1302.82s] English:** If you use a similar model in, say, OpenAI, OpenAI's user interface is trying to summarize  
**Translation:** 

**[1308.54s] English:** this process for you nicely by kind of showing the sections that the model is doing. And it'll  
**Translation:** Vocabulary: interface: 用户界面; summarize: 总结

**[1314.92s] English:** kind of click through. It'll say, breaking down the problem, making X calculation.  
**Translation:** 

**[1320.00s] English:** cleaning the result, and then the answer will come for something like OpenAI.  
**Translation:** 

**[1323.82s] English:** Maybe it's useful here to go through an example of a DeepSeek R1 reasoning.  
**Translation:** 

**[1329.04s] English:** Yeah, so if you're looking at the screen here, what you'll see is a screenshot of the DeepSeek  
**Translation:** 

**[1334.42s] English:** chat app, and at the top is thought for 157 seconds with the drop-down arrow. Underneath  
**Translation:** 

**[1341.10s] English:** that, if we were in an app that we were running, the drop-down arrow would have the reasoning.  
**Translation:** 

**[1344.38s] English:** So in this case, the specific question, which I'm philosophically slash pothead inclined,  
**Translation:** 

**[1351.46s] English:** so this is asking DeepSeek R1 for one truly novel insight about humans, and it reveals  
**Translation:** Vocabulary: inclined: 倾向; philosophically: 哲学地; pothead: 烟 pot

**[1360.30s] English:** the reasoning, and basically the truly novel aspect is what's pushing the reasoning to  
**Translation:** 

**[1366.74s] English:** constantly sort of the model asking itself, is this truly novel? So it's actually challenging  
**Translation:** 

**[1370.88s] English:** itself to be more novel, more counterintuitive.  
**Translation:** 

**[1374.38s] English:** Uh, more, uh, less cringe, I suppose. So some of the reasoning says, uh, this is just  
**Translation:** Vocabulary: counterintuitive: 违反直觉; cringe: 尴尬

**[1380.42s] English:** snapshots. Alternatively, humans have a unique meta-emotion where they feel emotions about  
**Translation:** 

**[1385.08s] English:** their own emotions, e.g. feeling guilty about being angry. This recursive emotional layering  
**Translation:** Vocabulary: alternatively: 替代地; layering: 层叠; recursive: 递归; snapshots: 快照

**[1389.46s] English:** creates complex motivational drives that don't exist in other animals. The insight is that  
**Translation:** 

**[1394.02s] English:** human emotions are nested, so it's like, it's reasoning through how humans feel emotions,  
**Translation:** Vocabulary: motivational: 动机的

**[1399.56s] English:** it's reasoning about meta-emotions.  
**Translation:** 

**[1401.12s] English:** It's going to have pages and pages of this. It's almost too much to actually read,  
**Translation:** 

**[1404.38s] English:** but it's nice to skim as it's coming.  
**Translation:** 

**[1406.30s] English:** It's a stream of, it's a James Joyce-like stream of consciousness, and then it goes,  
**Translation:** 

**[1410.52s] English:** wait, the user wants something that's not seen anywhere else, let me dig deeper. And consider  
**Translation:** 

**[1417.32s] English:** the human ability to hold contradictory beliefs simultaneously. Cognitive dissonance is known,  
**Translation:** Vocabulary: cognitive: 认知; contradictory: 矛盾

**[1421.74s] English:** but perhaps the function is to allow flexible adaptation, so on and so forth. I mean,  
**Translation:** 

**[1427.66s] English:** that really captures the public imagination that, holy shit, this isn't, uh,  
**Translation:** Vocabulary: adaptation: 适应性

**[1434.38s] English:** I mean, intelligence slash almost like, like an inkling of sense.  
**Translation:** 

**[1440.00s] English:** because you're thinking through, you're self-reflecting, you're deliberating.  
**Translation:** Vocabulary: deliberating: 深思熟虑

**[1444.56s] English:** And the final result of that, after 157 seconds, is humans instinctively convert selfish desires into cooperative systems  
**Translation:** 

**[1453.60s] English:** by collectively pretending abstract rules, money, laws, rights are real.  
**Translation:** Vocabulary: cooperative: 合作; instinctively: 本能地

**[1458.48s] English:** These shared hallucinations act as, quote, games, where competition is secretly redirected to benefit the group,  
**Translation:** 

**[1465.10s] English:** turning conflict into society's fuel.  
**Translation:** Vocabulary: hallucinations: 集体幻觉

**[1467.52s] English:** Pretty profound. I mean, you know.  
**Translation:** 

**[1471.70s] English:** This is a potential digression, but a lot of people have found that these reasoning models can sometimes produce much more eloquent text.  
**Translation:** Vocabulary: digression: 离题; eloquent: 文雅; profound: 深奥

**[1480.40s] English:** That is a at least interesting example, I think, depending on how open-minded you are,  
**Translation:** 

**[1484.96s] English:** you find language models interesting or not, and there's a spectrum there.  
**Translation:** 

**[1488.22s] English:** Well, I mean, some of the, we'll talk about different benchmarks and so on, but some is just a vibe.  
**Translation:** 

**[1492.82s] English:** Like that in itself is a, let's say, quote, fire tweet.  
**Translation:** Vocabulary: benchmarks: 参考标准

**[1497.52s] English:** Yeah.  
**Translation:** 

**[1498.06s] English:** If I'm trying to produce something, something where people are like, oh, shit.  
**Translation:** 

**[1503.32s] English:** Okay, so that's a chance I will probably return to it more.  
**Translation:** 

**[1507.60s] English:** How were they able to achieve such low cost on the training and the inference?  
**Translation:** Vocabulary: inference: 推理

**[1513.40s] English:** Maybe you could talk the training first.  
**Translation:** 

**[1515.60s] English:** Yeah, so there's two main techniques that they implemented that are probably the majority of their efficiency.  
**Translation:** 

**[1522.60s] English:** And then there's a lot of implementation details that maybe we'll gloss over or get into later.  
**Translation:** 

**[1527.52s] English:** That sort of contribute to it.  
**Translation:** Vocabulary: gloss: 略过; implementation: 实施细节

**[1528.64s] English:** But those two main things are one is they went to a mixture of experts model, which we'll define in a second.  
**Translation:** 

**[1535.76s] English:** And then the other thing is that they invented this new technique called MLA latent attention.  
**Translation:** 

**[1540.56s] English:** Both of these are big deals.  
**Translation:** 

**[1542.10s] English:** Mixture of experts is something that's been in the literature for a handful of years.  
**Translation:** 

**[1546.24s] English:** And OpenAI with GPT-4 was the first one to productize a mixture of experts model.  
**Translation:** 

**[1551.58s] English:** And what this means is when you look at the common models around that most people have been able to,  
**Translation:** Vocabulary: productize: 商品化

**[1557.52s] English:** to interact with that are open, right?  
**Translation:** 

**[1559.64s] English:** Think.  
**Translation:** 

**[1560.00s] English:** LAMA. LAMA is a dense model, i.e. every single parameter or neuron is activated as you're going  
**Translation:** 

**[1567.30s] English:** through the model for every single token you generate, right? Now, with a mixture of experts  
**Translation:** Vocabulary: neuron: 神经元; parameter: 参数; token: 标记

**[1572.10s] English:** model, you don't do that, right? How does the human actually work, right? It's like, oh, well,  
**Translation:** 

**[1576.48s] English:** my visual cortex is active when I'm thinking about, you know, vision tasks and like, you know,  
**Translation:** Vocabulary: cortex: 皮层

**[1580.62s] English:** other things, right? My amygdala is when I'm scared, right? These different aspects of your  
**Translation:** 

**[1585.18s] English:** brain are focused on different things. A mixture of experts model attempts to approximate this to  
**Translation:** Vocabulary: amygdala: 杏仁体; approximate: 近似

**[1589.68s] English:** some extent. It's nowhere close to what a brain architecture is, but different portions of the  
**Translation:** 

**[1594.12s] English:** model activate, right? You'll have a set number of experts in the model and a set number that  
**Translation:** Vocabulary: portions: 部分

**[1599.46s] English:** are activated each time. And this dramatically reduces both your training and inference costs  
**Translation:** 

**[1603.72s] English:** because now you're, you know, if you think about the parameter count as the sort of  
**Translation:** Vocabulary: dramatically: 大幅度地

**[1608.64s] English:** total embedding space for all of this knowledge that you're compressing down during training,  
**Translation:** 

**[1614.28s] English:** when you're embedding this data in, instead of having to activate every single parameter every  
**Translation:** Vocabulary: compressing: 压缩; embedding: 嵌入

**[1619.34s] English:** single time, you're going to have to activate every single parameter every single time.  
**Translation:** 

**[1619.68s] English:** You're training or running inference. Now you can just activate a subset and the model will learn  
**Translation:** 

**[1624.72s] English:** which expert to route to for different tasks. And so this is a humongous innovation in terms of,  
**Translation:** 

**[1630.98s] English:** hey, I can continue to grow the total embedding space of parameters. And so DeepSeek's model is,  
**Translation:** Vocabulary: humongous: 巨大

**[1635.52s] English:** you know, 600 something billion parameters, right? Relative to LAMA 405b, it's 405 billion  
**Translation:** 

**[1640.68s] English:** parameters, right? Relative to LAMA 70b, it's 70 billion parameters, right? So this model  
**Translation:** 

**[1644.92s] English:** technically has more embedding space for information, right? To compress all of the  
**Translation:** 

**[1649.20s] English:** world's knowledge that's on the internet down. But at the same time, it is only activating  
**Translation:** Vocabulary: compress: 压缩

**[1654.04s] English:** around 37 billion of the parameters. So only 37 billion of these parameters actually need to be  
**Translation:** 

**[1659.32s] English:** computed every single time you're training data or inferencing data out of it. And so versus,  
**Translation:** Vocabulary: computed: 计算; inferencing: 推理

**[1665.16s] English:** versus again, a LAMA model, 70 billion parameters must be activated, or 405 billion parameters must  
**Translation:** 

**[1669.76s] English:** be activated. So you've dramatically reduced your compute cost when you're doing training  
**Translation:** 

**[1673.50s] English:** and inference with this mixture of experts architecture. So we break down where it actually  
**Translation:** 

**[1678.80s] English:** applies.  
**Translation:** Vocabulary: inference: 推断

**[1679.20s] English:** And go into  
**Translation:** 

**[1680.00s] English:** the transformer is that useful let's go let's go into the transformer is a thing that is talked  
**Translation:** 

**[1685.66s] English:** about a lot and we will not cover every detail uh essentially the transformer is built on repeated  
**Translation:** 

**[1692.28s] English:** blocks of this attention mechanism and then a traditional dense fully connected multi-layer  
**Translation:** 

**[1698.48s] English:** perception whatever word you want to use for your normal neural network and you alternate these  
**Translation:** 

**[1702.62s] English:** blocks there's other details and where mixture of experts is applied is that this dense model  
**Translation:** 

**[1707.66s] English:** the dense model holds most of the weights if you count them in a transformer model so you can get  
**Translation:** 

**[1714.70s] English:** really big gains from those mixture of experts on parameter efficiency at training and inference  
**Translation:** Vocabulary: parameter: 参数

**[1719.08s] English:** because you get this efficiency by not activating all of these parameters we should also say that a  
**Translation:** 

**[1725.56s] English:** transformer is a giant neural network yeah and then there's for 15 years now there's what's  
**Translation:** Vocabulary: neural: 神经网络

**[1732.48s] English:** called the deep learning revolution networks gotten larger and larger in a certain point  
**Translation:** 

**[1737.66s] English:** scaling laws appeared where people realized this is a scaling law shirt by the way representing  
**Translation:** 

**[1743.34s] English:** scaling laws where it became more and more formalized that bigger is better across multiple  
**Translation:** 

**[1750.38s] English:** dimensions of what bigger means so uh and but these are all sort of neural networks we're talking  
**Translation:** Vocabulary: dimensions: 维度

**[1755.62s] English:** about and we're talking about different architectures of how construct to construct  
**Translation:** 

**[1759.58s] English:** these neural networks such that the training and the inference on them is super efficient yeah  
**Translation:** 

**[1764.42s] English:** every different type of model has a different scaling law for it  
**Translation:** 

**[1767.66s] English:** which is effectively for how much compute you put in the architecture will get to different levels  
**Translation:** 

**[1774.32s] English:** of performance at test tasks and mixture of experts is one of the ones at training time even if you  
**Translation:** 

**[1779.72s] English:** don't consider the inference benefits which are also big at training time your efficiency with  
**Translation:** 

**[1784.24s] English:** your gpus is dramatically improved by using this architecture if it is well implemented  
**Translation:** 

**[1788.32s] English:** so you can get effectively the same performance model and evaluation scores with numbers like 30  
**Translation:** Vocabulary: dramatically: 显著地

**[1796.46s] English:** less compute i think that's the difference between the two so that's the difference between the two  
**Translation:** 

**[1797.66s] English:** there's going to be a wide variation depending on your implement  
**Translation:** 

**[1800.00s] English:** details and stuff. But it is just important to realize that this type of technical innovation  
**Translation:** 

**[1805.20s] English:** is something that gives huge gains. And I expect most companies that are serving their models to  
**Translation:** 

**[1811.42s] English:** move to this mixture of experts implementation. Historically, the reason why not everyone might  
**Translation:** 

**[1816.46s] English:** do it is because it's an implementation complexity, especially when doing these big models.  
**Translation:** Vocabulary: complexity: 复杂性; historically: 历史上; implementation: 实施

**[1821.18s] English:** So this is one of the things that DeepSeek gets credit for is they do this extremely well.  
**Translation:** 

**[1825.68s] English:** They do mixture of experts extremely well. This architecture for what is called DeepSeek MOE,  
**Translation:** 

**[1831.44s] English:** MOE is the shortened version of mixture of experts, is multiple papers old. This part of  
**Translation:** 

**[1837.02s] English:** their training infrastructure is not new to these models alone. And same goes for what Dylan mentioned  
**Translation:** 

**[1842.90s] English:** with multi-headlight inattention. It's all about reducing memory usage during inference and same  
**Translation:** 

**[1849.00s] English:** things during training by using some fancy low-rank approximation math. If you get into the details  
**Translation:** Vocabulary: approximation: 近似; inference: 推理

**[1854.74s] English:** with this,  
**Translation:** 

**[1855.68s] English:** latent attention, it's one of those things I look at. It's like, okay, they're doing really  
**Translation:** 

**[1860.34s] English:** complex implementations because there's other parts of language models, such as  
**Translation:** 

**[1864.44s] English:** embeddings that are used to extend the context length. The common one that DeepSeek used is  
**Translation:** Vocabulary: embeddings: 嵌入表示; implementations: 实现方式

**[1869.28s] English:** rotary positional embeddings, which is called ROPE. And if you want to use ROPE with a normal MOE,  
**Translation:** 

**[1875.34s] English:** it's kind of a sequential thing. You take two of the attention matrices and you rotate them  
**Translation:** Vocabulary: matrices: 矩阵; positional: 位置; rotary: 旋转; rotate: 转动; sequential: 顺序

**[1880.26s] English:** by a complex value rotation, which is a matrix multiplication. With DeepSeek's  
**Translation:** 

**[1885.68s] English:** MLA, with this new attention architecture, they need to do some clever things because they're not  
**Translation:** Vocabulary: matrix: 矩阵; multiplication: 乘法

**[1890.50s] English:** set up the same and it just makes the implementation complexity much higher. So they're managing all of  
**Translation:** 

**[1895.20s] English:** these things. And these are probably the sort of things that OpenAI, these closed labs are doing.  
**Translation:** 

**[1900.38s] English:** We don't know if they're doing the exact same techniques, but they actually shared them with  
**Translation:** 

**[1903.64s] English:** the world, which is really nice to feel like this is the cutting edge of efficient language model  
**Translation:** 

**[1908.50s] English:** training. And some of this requires low-level engineering. It's a giant mess and trickery.  
**Translation:** 

**[1915.68s] English:** So as I understand, that went below CUDA. So they go super low programming.  
**Translation:** Vocabulary: trickery: 欺诈手段

**[1920.00s] English:** gpus effectively nvidia builds this library called nickel right uh in which you know when you're  
**Translation:** 

**[1926.46s] English:** training a model you have all these communications between every single layer of the model and you  
**Translation:** Vocabulary: nickel: 镍币库

**[1931.02s] English:** may have over 100 layers what does nickel stand for it's nccl nvidia communications collectives  
**Translation:** 

**[1936.08s] English:** library nice um and so damn when when you're training a model right you're gonna have all  
**Translation:** 

**[1943.84s] English:** these all reduces and all gathers right uh between each layer between the uh multi-layer  
**Translation:** 

**[1949.00s] English:** perceptron or feed forward network and the attention mechanism you'll have you'll have  
**Translation:** Vocabulary: perceptron: 感知机

**[1952.52s] English:** basically the model synchronized right um or you'll have all the you'll have all reducer and  
**Translation:** 

**[1957.24s] English:** all gather um and and this is a communication between all the gpus in the network whether  
**Translation:** Vocabulary: synchronized: 同步

**[1961.40s] English:** whether it's in training or inference so nvidia has a standard library this is one of the reasons  
**Translation:** 

**[1965.64s] English:** why it's really difficult to use anyone else's hardware uh for training is because no one's  
**Translation:** 

**[1970.70s] English:** really built a standard communications library um and nvidia has done this at a sort of a higher  
**Translation:** 

**[1975.30s] English:** level right a deep seek because they have certain limitations around  
**Translation:** 

**[1978.94s] English:** the  
**Translation:** 

**[1979.00s] English:** gpus that they have access to the interconnects are limited to some extent um by the restrictions  
**Translation:** Vocabulary: interconnects: 互联网络

**[1984.68s] English:** of the gpus that were shipped into china legally not the ones that are smuggled but legally shipped  
**Translation:** 

**[1988.92s] English:** in uh that they used to train this model they had to figure out how to get efficiencies right and  
**Translation:** Vocabulary: efficiencies: 效率

**[1995.32s] English:** one of those things is that instead of just calling the nvidia library nickel right they  
**Translation:** 

**[2000.66s] English:** instead created their they scheduled their own communications uh which which the lab some of the  
**Translation:** 

**[2009.00s] English:** labs that they used to train the nvidia library nickel right they scheduled their own communications  
**Translation:** 

**[2011.00s] English:** uh which which the lab some of the labs that they used to train the nvidia library nickel right they  
**Translation:** 

**[2011.88s] English:** didn't they didn't talk about the implementation details this is some of what they did probably  
**Translation:** 

**[2015.24s] English:** not as well as maybe not as well as deep seek because deep seek you know necessity is the  
**Translation:** Vocabulary: implementation: 实施方案; necessity: 必要性

**[2019.64s] English:** mother of innovation and they had to do this whereas uh in the case you know open ai has  
**Translation:** 

**[2025.50s] English:** people that do this sort of stuff anthropic etc uh but you know deep seek certainly did it publicly  
**Translation:** 

**[2030.34s] English:** and they may have done it even better because they were gimped on a certain aspect of the chips that  
**Translation:** 

**[2034.74s] English:** they have access to and so they scheduled communication between the gpus and the nvidia  
**Translation:** 

**[2039.00s] English:** library nickel right they scheduled their own communications uh they scheduled their own  
**Translation:** 

**[2040.00s] English:** by scheduling specific SMs.  
**Translation:** 

**[2042.58s] English:** SMs you could think of as like the core on a GPU, right?  
**Translation:** 

**[2046.22s] English:** So there's hundreds of cores  
**Translation:** 

**[2047.84s] English:** or there's a bit over a hundred cores SMs on a GPU  
**Translation:** 

**[2051.36s] English:** and they were specifically scheduling,  
**Translation:** 

**[2053.24s] English:** hey, which ones are running the model?  
**Translation:** 

**[2054.54s] English:** Which ones are doing all reduce?  
**Translation:** 

**[2055.84s] English:** Which one are doing all gather, right?  
**Translation:** 

**[2057.38s] English:** And they would flip back and forth between them  
**Translation:** 

**[2059.06s] English:** and this requires extremely low level programming.  
**Translation:** 

**[2062.18s] English:** This is what Nickel does automatically  
**Translation:** 

**[2063.48s] English:** or other NVIDIA libraries handle this automatically usually.  
**Translation:** 

**[2066.58s] English:** Yeah, exactly.  
**Translation:** 

**[2067.10s] English:** And so technically they're using, you know, PTX,  
**Translation:** 

**[2070.08s] English:** which is like sort of like,  
**Translation:** 

**[2071.38s] English:** you could think of it as like an assembly type language.  
**Translation:** 

**[2073.70s] English:** It's not exactly that or instruction set, right?  
**Translation:** 

**[2075.82s] English:** Like coding directly to assembly or instruction set.  
**Translation:** 

**[2078.18s] English:** It's not exactly that,  
**Translation:** 

**[2079.44s] English:** but that's still part of technically CUDA,  
**Translation:** 

**[2082.04s] English:** but it's like, do I want to write in Python,  
**Translation:** 

**[2084.16s] English:** you know, PyTorch equivalent and call NVIDIA libraries?  
**Translation:** 

**[2087.04s] English:** Do I want to go down to the C level, right?  
**Translation:** 

**[2089.04s] English:** Or, you know, encode even lower level  
**Translation:** 

**[2090.60s] English:** or do I want to go all the way down  
**Translation:** Vocabulary: encode: 编码

**[2091.54s] English:** to the assembly or ISO level?  
**Translation:** 

**[2093.18s] English:** And there are cases where you go all the way down there  
**Translation:** 

**[2095.80s] English:** at the very big labs,  
**Translation:** 

**[2097.14s] English:** but most companies just do not do that, right?  
**Translation:** 

**[2099.62s] English:** Because it's a waste of time  
**Translation:** 

**[2100.76s] English:** and the efficiency gains you get are not worth it.  
**Translation:** 

**[2103.74s] English:** But DeepSeq's implementation is so complex, right?  
**Translation:** 

**[2106.84s] English:** Especially with their mixture of experts, right?  
**Translation:** 

**[2109.24s] English:** People have done mixture of experts,  
**Translation:** 

**[2110.76s] English:** but they're generally eight, 16 experts, right?  
**Translation:** 

**[2113.36s] English:** And they activate too.  
**Translation:** 

**[2114.40s] English:** So, you know, one of the words that we like to use  
**Translation:** 

**[2117.00s] English:** is like sparsity factor, right?  
**Translation:** 

**[2118.66s] English:** Or usage, right?  
**Translation:** Vocabulary: sparsity: 稀疏程度

**[2119.44s] English:** So you might have four, you know,  
**Translation:** 

**[2121.50s] English:** one fourth of your model activate, right?  
**Translation:** 

**[2123.70s] English:** And that's what Mistral's, Mistral model, right?  
**Translation:** 

**[2127.24s] English:** Their model that really catapulted them to like,  
**Translation:** Vocabulary: catapulted: 推动

**[2129.92s] English:** oh my God, they're really, really good.  
**Translation:** 

**[2132.24s] English:** OpenAI has also had models that are MOE  
**Translation:** 

**[2134.16s] English:** and so have all the other labs that are major closed.  
**Translation:** 

**[2137.94s] English:** But what DeepSeq did that maybe only the leading labs  
**Translation:** 

**[2140.72s] English:** have only just started recently doing  
**Translation:** 

**[2142.20s] English:** is have such a high sparsity factor, right?  
**Translation:** 

**[2144.24s] English:** It's not one fourth of the model, right?  
**Translation:** 

**[2146.00s] English:** Two out of eight experts activating  
**Translation:** 

**[2147.58s] English:** every time you go through the model,  
**Translation:** 

**[2149.24s] English:** it's eight out of 256.  
**Translation:** 

**[2151.20s] English:** And there's different implementations  
**Translation:** 

**[2152.94s] English:** for mixture of experts where you can have  
**Translation:** Vocabulary: implementations: 实现方式

**[2155.08s] English:** some of these experts that are,  
**Translation:** 

**[2157.00s] English:** you know, they're not going to be able to do that.  
**Translation:** 

**[2157.10s] English:** Always activated, which this just looks like.  
**Translation:** 

**[2160.00s] English:** a small neural network and then all the tokens go through that and then they also go through some  
**Translation:** Vocabulary: neural: 神经网络

**[2166.08s] English:** that are selected by this routing mechanism and one of the innovations in deep seek's architecture  
**Translation:** 

**[2172.96s] English:** is that they change the routing mechanism in mixture of expert models there's something called  
**Translation:** Vocabulary: innovations: 创新; routing: 路由机制

**[2177.36s] English:** an auxiliary loss which effectively means during training you want to make sure that all of these  
**Translation:** 

**[2182.72s] English:** experts are used across the tasks that the model sees why there can be failures and mixture of  
**Translation:** 

**[2188.32s] English:** experts is that when you're doing this training the one objective is token prediction accuracy  
**Translation:** 

**[2195.52s] English:** and if you just let turning go with a mixture of expert model on your own it can be that the model  
**Translation:** Vocabulary: token: 令牌

**[2201.60s] English:** learns to only use a subset of the experts and in the moe literature there's something called  
**Translation:** 

**[2207.20s] English:** the auxiliary loss which helps balance them but if you think about the loss functions of  
**Translation:** 

**[2213.04s] English:** deep learning this even connects to the bitter lesson is that you want to have the minimum  
**Translation:** 

**[2218.32s] English:** inductive bias in your model to let the model learn maximally and this auxiliary loss this  
**Translation:** Vocabulary: inductive: 归纳; maximally: 最大化

**[2223.20s] English:** balancing across experts could be seen as intention with the prediction accuracy of the tokens  
**Translation:** 

**[2229.28s] English:** so we don't know the exact extent that the deep seek moe change which is instead of doing an  
**Translation:** Vocabulary: balancing: 平衡

**[2234.40s] English:** auxiliary loss they have an extra parameter in their routing which after the batches they update  
**Translation:** 

**[2239.44s] English:** this parameter to make sure that the next batches all have a similar use of experts and this type of  
**Translation:** Vocabulary: parameter: 参数

**[2244.96s] English:** change can be big it can be small but they add up over time  
**Translation:** 

**[2248.32s] English:** and this is the sort of thing that just points to them innovating and i'm sure  
**Translation:** Vocabulary: innovating: 创新

**[2252.00s] English:** all the labs that are training big moes are looking at this sort of things which is  
**Translation:** 

**[2255.68s] English:** getting away from the auxiliary loss some of them might already use it but you just keep  
**Translation:** 

**[2259.12s] English:** you keep accumulating gains and we'll talk about the philosophy of training and how you organize  
**Translation:** 

**[2264.00s] English:** these organizations and a lot of it is just compounding small improvements over time in  
**Translation:** Vocabulary: accumulating: 累积; compounding: 复利

**[2268.96s] English:** your data in your architecture and your post training and how they integrate with each other  
**Translation:** 

**[2273.92s] English:** deepseek does the same thing and some of them are shared or a lot we have to take them on face to  
**Translation:** Vocabulary: integrate: 融合

**[2278.32s] English:** face value that they share their most  
**Translation:** 

**[2280.00s] English:** important details. I mean, the architecture and the weights are out there. So we're seeing what  
**Translation:** 

**[2282.94s] English:** they're doing. And it adds up. Going back to sort of the like efficiency and complexity point,  
**Translation:** 

**[2288.18s] English:** right? It's 32 versus four, right? For like mixed draw and other MOE models that have been publicly  
**Translation:** 

**[2293.56s] English:** released. So this ratio is extremely high. And sort of what Nathan was getting at there was  
**Translation:** 

**[2298.12s] English:** when you have such a different level of sparsity, you can't just have every GPU have the entire  
**Translation:** 

**[2304.90s] English:** model, right? The model is too big. There's too much complexity there. So you have to split up  
**Translation:** 

**[2308.44s] English:** the model with different types of parallelism, right? And so you might have different experts  
**Translation:** Vocabulary: complexity: 复杂性

**[2312.80s] English:** on different GPU nodes. But now what happens when this set of data that you get, hey, all of it  
**Translation:** 

**[2319.10s] English:** looks like this one way and all of it should route to one part of my model, right? So when all of it  
**Translation:** 

**[2325.44s] English:** routes to one part of the model, then you can have this overloading of a certain set of the GPU  
**Translation:** 

**[2332.70s] English:** resources or a certain set of the GPUs. And then the rest of the training network sits,  
**Translation:** Vocabulary: overloading: 超载

**[2338.32s] English:** I have to do this. I have to do this. I have to do this. I have to do this. I have to do this.  
**Translation:** 

**[2338.42s] English:** Because all of the tokens are just routing to that. So this is the biggest complexity. One of  
**Translation:** Vocabulary: routing: 路由

**[2341.88s] English:** the biggest complexities with running a very sparse mixture of experts model, i.e. this 32  
**Translation:** 

**[2348.28s] English:** ratio versus this four ratio, is that you end up with so many of the experts just sitting there  
**Translation:** Vocabulary: complexities: 复杂性; sparse: 稀疏的

**[2353.66s] English:** idle. So how do I load balance between them? How do I schedule the communications between them?  
**Translation:** 

**[2358.30s] English:** This is a lot of the extremely low level detailed work that they figured out in the public first,  
**Translation:** 

**[2364.98s] English:** and potentially like second or third in the world, and maybe even,  
**Translation:** 

**[2368.44s] English:** first in some cases. What lesson do you, in the direction of the bitter lesson, do you take from  
**Translation:** 

**[2374.52s] English:** all of this? Where is this going to be the direction where a lot of the gain is going to be,  
**Translation:** 

**[2379.18s] English:** which is this kind of low level optimization? Or is this a short term thing where the biggest  
**Translation:** Vocabulary: optimization: 优化

**[2385.34s] English:** gains will be more on the algorithmic high level side of like post-training? Is this like a short  
**Translation:** 

**[2391.66s] English:** term leap because they figured out like a hack because constraints, necessities, the mother of  
**Translation:** Vocabulary: algorithmic: 算法; constraints: 限制; necessities: 必要性

**[2397.66s] English:** invention? Or is there, is there  
**Translation:** 

**[2400.00s] English:** still a lot of gains i think we should summarize what the bitter lesson actually is about is that  
**Translation:** 

**[2404.26s] English:** the bitter lesson essentially if you paraphrase it is that the types of training that will win  
**Translation:** 

**[2410.74s] English:** out in deep learning as we go are those methods that are which are scalable in learning in search  
**Translation:** Vocabulary: paraphrase: 改写; scalable: 可扩展

**[2417.28s] English:** is what it calls out and this scale word gets a lot of attention in this the interpretation that  
**Translation:** 

**[2426.04s] English:** i use is effectively to avoid adding in the human priors to your learning process and if you read  
**Translation:** 

**[2434.10s] English:** the original essay this is what it talks about is how researchers will try to come up with what  
**Translation:** 

**[2439.58s] English:** clever solutions to their specific problem that might get them small gains in the short term  
**Translation:** 

**[2445.70s] English:** while simply enabling these deep learning systems to work efficiently and for these bigger problems  
**Translation:** 

**[2451.82s] English:** in the long term might be more likely to scale and continue to  
**Translation:** Vocabulary: efficiently: 高效地

**[2456.04s] English:** drive success and therefore we were talking about relatively small implementation changes  
**Translation:** 

**[2462.24s] English:** to the mixture of experts model and therefore it's like okay like we will need a few more years to  
**Translation:** Vocabulary: implementation: 实施方案

**[2468.56s] English:** know if one of these are actually really crucial to the bitter lesson but the bitter lesson is  
**Translation:** 

**[2473.32s] English:** really this long-term arc of how simplicity can often win and there's a lot of sayings in the  
**Translation:** Vocabulary: simplicity: 简单性

**[2478.70s] English:** industry like the models just want to learn you have to give them the simple lost landscape where  
**Translation:** 

**[2483.74s] English:** you put compute through the model and and they  
**Translation:** 

**[2486.02s] English:** will learn and getting barriers out of the way that that's where the power something like nickel  
**Translation:** 

**[2491.32s] English:** comes in where standardized code that can be used by a lot of people to create sort of simple  
**Translation:** Vocabulary: barriers: 障碍; nickel: 镍; standardized: 标准化

**[2497.62s] English:** innovations that can scale which is why the hacks that i imagine that the code base for deep seek is  
**Translation:** 

**[2504.02s] English:** probably a giant mess i'm sure they have deep seek definitely has code bases that are extremely  
**Translation:** Vocabulary: hacks: 权宜之计; innovations: 创新

**[2508.60s] English:** messy where they're testing these new ideas multi-headlight and attention probably start  
**Translation:** 

**[2513.20s] English:** could start in something like a jupiter notebook or somebody tries  
**Translation:** Vocabulary: jupiter: 示例

**[2516.02s] English:** something on a few gpus and that is really messy  
**Translation:** 

**[2520.00s] English:** But the stuff that trains the DeepSeq V3 and DeepSeq R1, those libraries, if you were to present them to us, I would guess are extremely high quality code.  
**Translation:** 

**[2530.30s] English:** High quality readable code.  
**Translation:** 

**[2531.72s] English:** I think there is one aspect to note, though, right, is that there is the general ability for that to transfer across different types of runs, right?  
**Translation:** 

**[2541.34s] English:** You may make really, really high quality code for one specific model architecture at one size.  
**Translation:** 

**[2547.20s] English:** And then that is not transferable to, hey, when I make this architecture tweak, everything's broken again, right?  
**Translation:** Vocabulary: transferable: 可移植的; tweak: 调整

**[2553.42s] English:** Like that's something that could be, you know, with their specific low level coding of like scheduling SMs is specific to this model architecture and size, right?  
**Translation:** 

**[2563.50s] English:** And whereas like NVIDIA's collectives library is more like, hey, it'll work for anything, right?  
**Translation:** 

**[2568.86s] English:** You want to do an all reduce?  
**Translation:** 

**[2569.96s] English:** Great.  
**Translation:** 

**[2570.28s] English:** I don't care what your model architecture is.  
**Translation:** 

**[2571.80s] English:** It'll work.  
**Translation:** 

**[2572.50s] English:** And you're giving up a lot of performance when you do that in many cases.  
**Translation:** 

**[2576.32s] English:** But it's worthwhile.  
**Translation:** 

**[2577.20s] English:** It's worthwhile for them to do this specific optimization for this specific run, given the constraints that they have regarding compute.  
**Translation:** 

**[2583.80s] English:** I wonder how stressful it is to like, you know, these frontier models, like initiate training, like to have the code to push the button that like you're now spending a large amount of money and time to train this.  
**Translation:** Vocabulary: constraints: 计算限制; frontier: 前沿模型; initiate: 启动训练; optimization: 优化

**[2600.96s] English:** Like there must, I mean, there must be a lot of innovation on the debugging stage of like making sure there's no.  
**Translation:** 

**[2607.20s] English:** There's no issues that you're monitoring and visualizing every aspect of the training, all that kind of stuff.  
**Translation:** Vocabulary: visualizing: 可视化

**[2612.90s] English:** When people are training, they have all these various dashboards, but like the most simple one is your loss, right?  
**Translation:** 

**[2618.32s] English:** And it continues to go down.  
**Translation:** Vocabulary: dashboards: 仪表盘

**[2620.16s] English:** But in reality, especially with more complicated stuff like MOE, the biggest problem with it or FP8 training, which is another innovation, you know, going to a lower precision number format, i.e. less accurate, is that you end up with loss spikes, right?  
**Translation:** 

**[2632.32s] English:** And no one knows why the loss spike happened.  
**Translation:** Vocabulary: spike: 突增; spikes: 突增

**[2634.90s] English:** Some of them you do.  
**Translation:** 

**[2635.84s] English:** Some of them you do.  
**Translation:** 

**[2636.46s] English:** Some of them are bad.  
**Translation:** 

**[2637.20s] English:** I give AI2's example of what blue.  
**Translation:** 

**[2640.00s] English:** up our earlier models is a subreddit called  
**Translation:** 

**[2641.96s] English:** Microwave Gang. We love to shout  
**Translation:** Vocabulary: microwave: 微波炉; subreddit: 子版块

**[2643.84s] English:** about this out. It's a real thing. You can pull  
**Translation:** 

**[2645.94s] English:** up Microwave Gang. Essentially, it's a  
**Translation:** 

**[2647.86s] English:** subreddit where everybody makes posts that  
**Translation:** 

**[2649.86s] English:** are just the letter M, so it's like,  
**Translation:** 

**[2651.26s] English:** so there's extremely long sequences  
**Translation:** 

**[2654.10s] English:** of the letter M, and then the comments  
**Translation:** 

**[2656.02s] English:** are like, beep, beep, because it's in the microwave ends.  
**Translation:** 

**[2658.02s] English:** But if you pass this into a model that's trained to  
**Translation:** 

**[2659.92s] English:** be a normal producing text, it's extremely  
**Translation:** 

**[2662.14s] English:** high loss, because normally  
**Translation:** 

**[2663.82s] English:** you see an M. You don't predict M's  
**Translation:** 

**[2665.96s] English:** for a long time. So this is  
**Translation:** 

**[2667.82s] English:** something that caused the loss spikes for us.  
**Translation:** 

**[2670.00s] English:** But when you have much, like, this is old,  
**Translation:** 

**[2671.94s] English:** this is not recent, and when you  
**Translation:** 

**[2673.96s] English:** have more mature data systems, that's not the thing  
**Translation:** 

**[2676.00s] English:** that causes the loss spike. And what Dylan is saying  
**Translation:** 

**[2677.90s] English:** is true, but it's like,  
**Translation:** Vocabulary: dylan: 迪伦

**[2679.62s] English:** it's levels to this sort of idea.  
**Translation:** 

**[2681.90s] English:** With regards to the stress, right?  
**Translation:** 

**[2683.80s] English:** These people are like, you know, you'll go out to  
**Translation:** 

**[2685.90s] English:** dinner with a friend that works at one of these labs,  
**Translation:** 

**[2688.46s] English:** and they'll just be  
**Translation:** 

**[2689.64s] English:** looking at their phone every 10 minutes,  
**Translation:** 

**[2691.88s] English:** and they're not, like, you know, it's one thing if they're  
**Translation:** 

**[2693.72s] English:** texting, but they're just like,  
**Translation:** 

**[2695.12s] English:** is the loss provoking?  
**Translation:** 

**[2698.00s] English:** Tokens per second, loss  
**Translation:** Vocabulary: provoking: 引起不满的

**[2699.76s] English:** not blown up. They're just  
**Translation:** 

**[2701.46s] English:** watching this. And the heart rate goes  
**Translation:** 

**[2703.74s] English:** up if there's a spike. And some  
**Translation:** 

**[2705.86s] English:** level of spikes is normal, right? It'll  
**Translation:** 

**[2707.38s] English:** recover and be back. Sometimes, a lot of the  
**Translation:** 

**[2709.66s] English:** old strategy was like, you just stop the run,  
**Translation:** 

**[2711.94s] English:** restart from the old version, and then  
**Translation:** 

**[2713.80s] English:** change the data mix, and then it keeps going.  
**Translation:** 

**[2716.14s] English:** There are even different types of spikes.  
**Translation:** 

**[2718.12s] English:** So Dirk Greneveld  
**Translation:** 

**[2719.50s] English:** has a theory that's like fast spikes  
**Translation:** 

**[2721.72s] English:** and slow spikes, where there are  
**Translation:** 

**[2723.42s] English:** sometimes where you're looking at the loss and there are other parameters,  
**Translation:** 

**[2725.88s] English:** you can see it start to creep up  
**Translation:** Vocabulary: creep: 缓慢增加

**[2727.18s] English:** and then blow up, and that's really hard to  
**Translation:** 

**[2729.56s] English:** recover from, so you have to go back much further.  
**Translation:** 

**[2731.44s] English:** So you have the stressful period where it's, like, flat  
**Translation:** 

**[2733.32s] English:** or it might start going up, and you're like, what do I do?  
**Translation:** 

**[2735.42s] English:** Whereas there are also loss spikes that are, it looks good,  
**Translation:** 

**[2737.66s] English:** and then there's one spiky data point,  
**Translation:** Vocabulary: spiky: 尖刺的

**[2739.52s] English:** and what you can do is you just skip those.  
**Translation:** 

**[2741.12s] English:** You see that there's a spike, you're like, okay,  
**Translation:** 

**[2743.20s] English:** I can ignore this data, don't update the model,  
**Translation:** 

**[2745.20s] English:** and do the next one, and it'll recover quickly.  
**Translation:** 

**[2747.28s] English:** But these, like,  
**Translation:** 

**[2748.60s] English:** trickier implementations, as you get more  
**Translation:** Vocabulary: implementations: 实施方案; trickier: 更复杂的

**[2751.22s] English:** complex in your architecture  
**Translation:** 

**[2752.78s] English:** and you scale up to more GPUs,  
**Translation:** 

**[2754.90s] English:** you have more potential for your  
**Translation:** 

**[2757.00s] English:** loss blowing up. So it's like, there's...  
**Translation:** 

**[2759.18s] English:** And there's a...  
**Translation:** 

**[2760.00s] English:** The whole idea of grokking also comes in, right? It's like, just because it slowed down from improving and lost doesn't mean it's not learning, because all of a sudden it could be like this, and it could just spike down and loss again, because it learned, truly learned something, right? And it took some time for it to learn that. It's not like a gradual process, right? And that's what humans are like, that's what models are like. So it's really a stressful task, as you mentioned.  
**Translation:** Vocabulary: grokking: 理解透彻; spike: 突增

**[2781.10s] English:** And the whole time the dollar count is going up.  
**Translation:** 

**[2784.02s] English:** Every company has failed runs. You need failed runs to push the envelope on your infrastructure. So a lot of news cycles are made of X company had Y failed run. Every company that's trying to push the frontier of AI has these. So yes, it's noteworthy because it's a lot of money and it can be week to month setback, but it is part of the process.  
**Translation:** Vocabulary: frontier: 技术边界; noteworthy: 值得留意

**[2805.02s] English:** But how do you get, if you're deep seek, how do you get to a place where, holy shit, there's a successful combination of hyperparameters?  
**Translation:** 

**[2812.48s] English:** A lot of small failed runs.  
**Translation:** Vocabulary: hyperparameters: 超参数

**[2814.48s] English:** So rapid iteration through failed runs.  
**Translation:** 

**[2819.10s] English:** And successful ones.  
**Translation:** Vocabulary: iteration: 迭代

**[2820.74s] English:** And then you build a sum of intuition like this, this mixture of expert works, and then this implementation of MLA works.  
**Translation:** 

**[2828.72s] English:** Key hyperparameters like learning rate and regularization and things like this. And you find the regime that works for your code base.  
**Translation:** Vocabulary: implementation: 实现; intuition: 直觉

**[2837.36s] English:** Talking to people at Frontier Labs, there's a story that you can tell where training language models is kind of a path.  
**Translation:** 

**[2844.02s] English:** That you need to follow.  
**Translation:** 

**[2844.90s] English:** So you need to unlock the ability to train a certain type of model or a certain scale.  
**Translation:** 

**[2849.64s] English:** And then your code base and your internal know-how of which hyperparameters work for it is kind of known.  
**Translation:** 

**[2853.94s] English:** And you look at the deep seek papers and models, they've scaled up, they've added complexity, and it's just continuing to build the capabilities that they have.  
**Translation:** 

**[2862.20s] English:** There's the concept of a YOLO run.  
**Translation:** Vocabulary: complexity: 复杂性

**[2864.76s] English:** So YOLO, you only live once.  
**Translation:** 

**[2867.06s] English:** And what it is, is like, you know, there's all this experimentation you do at the small scale, right?  
**Translation:** Vocabulary: experimentation: 小规模尝试

**[2872.90s] English:** Research ablations.  
**Translation:** 

**[2874.02s] English:** Right?  
**Translation:** Vocabulary: ablations: 切除手术

**[2874.16s] English:** Like you have your Jupyter notebook where you're experimenting with MLA on like three GPUs or whatever.  
**Translation:** 

**[2878.96s] English:** And you're doing all this.  
**Translation:** Vocabulary: experimenting: 尝试

**[2880.00s] English:** these different uh things like hey do i do four expert four active experts 128 experts do i arrange  
**Translation:** 

**[2885.36s] English:** the experts this way you know all these different uh model architecture things you're testing at a  
**Translation:** 

**[2889.60s] English:** very small scale right couple researchers few gpus tens of gpus hundreds of gpus whatever it is  
**Translation:** 

**[2894.94s] English:** and then all of a sudden you're like okay guys no more no more fucking around right uh no more  
**Translation:** 

**[2899.22s] English:** screwing around everyone take all the resources we have let's pick what we think will work and  
**Translation:** 

**[2904.72s] English:** just go for it right yolo and this is where that sort of stress comes in is like well i know it  
**Translation:** Vocabulary: screwing: 胡闹

**[2909.70s] English:** works here but some things that work here don't work here and some things that work here don't  
**Translation:** 

**[2914.12s] English:** work down here right in terms of scale right so it's it's it's really truly a yolo run and and  
**Translation:** 

**[2920.22s] English:** sort of like there's this like like discussion of like certain researchers just have like this  
**Translation:** 

**[2924.44s] English:** methodical nature like they can find the whole search space and like figure out all the ablations  
**Translation:** 

**[2928.34s] English:** of different research and really see what is best and there's certain researchers who just kind of  
**Translation:** 

**[2932.86s] English:** like you know have that innate gut instinct of like this is the yolo run like you know looking  
**Translation:** Vocabulary: instinct: 直觉

**[2938.10s] English:** at the data this is it  
**Translation:** 

**[2939.70s] English:** this is why you want to work in post-training because the gpu cost for training is lower so  
**Translation:** 

**[2943.76s] English:** you can make a higher percentage of your training runs yolo runs yeah for now yeah for now for now  
**Translation:** 

**[2949.04s] English:** so some of this is fundamentally luck still luck is skill right in many cases yeah i mean it looks  
**Translation:** Vocabulary: fundamentally: 本质上

**[2957.52s] English:** lucky right when you're but the hill to climb if you're on one of these labs you have an evaluation  
**Translation:** 

**[2962.72s] English:** you're not crushing there's a repeated playbook of how you improve things there are localized  
**Translation:** Vocabulary: playbook: 操作手册

**[2967.34s] English:** improvements which might be data improvements and these add up to the data improvements and  
**Translation:** 

**[2969.70s] English:** these add up into the whole model just being much better and when you zoom in really close it can be  
**Translation:** 

**[2973.88s] English:** really obvious that this model is just really bad at this thing and we can fix it and you just add  
**Translation:** 

**[2978.94s] English:** these up so some of it feels like luck but on the ground especially with these new reasoning models  
**Translation:** 

**[2984.08s] English:** we're talking to it's just so many ways that we can poke around and normally it's that some of  
**Translation:** 

**[2990.06s] English:** them give big improvements the search space is near infinite right and and yet the amount of  
**Translation:** 

**[2994.18s] English:** compute and time you have is is very low and you're you're you have to hit release schedule  
**Translation:** 

**[2999.70s] English:** you have  
**Translation:** 

**[3000.00s] English:** have to not get blown past by everyone otherwise you know what happened with deep seek you know  
**Translation:** 

**[3005.18s] English:** crushing meta and mistral and coherent all these guys they moved too slow right they they maybe  
**Translation:** Vocabulary: coherent: 条理清晰

**[3009.66s] English:** were too methodical i don't know they didn't hit the yolo run whatever the reason was maybe they  
**Translation:** 

**[3013.36s] English:** weren't as skilled uh whatever what you know you can call it luck if you want but at the end of  
**Translation:** 

**[3017.38s] English:** the day it's skill so 2025 is the year of the yolo run it seems like all the labs are like going in  
**Translation:** 

**[3024.74s] English:** i i think it's even more impressive what opening i did in 2022 right at the time no one believed in  
**Translation:** 

**[3031.18s] English:** mixture of experts models right at google uh who had all the researchers uh opening i had such  
**Translation:** 

**[3036.64s] English:** little compute and they devoted all of their compute for many months right all of it 100  
**Translation:** 

**[3041.92s] English:** for many months to gpt4 with a brand new architecture with no belief that hey let me  
**Translation:** 

**[3048.32s] English:** spend a couple hundred million dollars which is all of the money i have on this model right that  
**Translation:** 

**[3052.90s] English:** is truly yolo yeah right  
**Translation:** 

**[3054.74s] English:** now now you know people are like all these like training run failures that are in the media right  
**Translation:** 

**[3059.92s] English:** it's like okay great but like actually a lot a huge chunk of my gps are doing inference i still  
**Translation:** 

**[3064.44s] English:** have a bunch doing research constantly and yes my biggest cluster is training but like on this  
**Translation:** Vocabulary: cluster: 训练集群; inference: 推理

**[3069.20s] English:** yolo run but like that yolo run is much less risky than like what opening i did in 2022 or  
**Translation:** 

**[3075.12s] English:** maybe what deep seek did now or you know like sort of like hey we're just gonna throw everything at  
**Translation:** 

**[3079.22s] English:** it the big winners throughout human history are the ones who are willing to do yolo at some point  
**Translation:** 

**[3084.72s] English:** okay uh what do we understand about the hardware it's been trained on deep seek deep seek is very  
**Translation:** 

**[3092.44s] English:** interesting at least a second to take us to zoom out out of who they are first of all right  
**Translation:** 

**[3095.68s] English:** high flyer is a hedge fund that has historically done quantitative trading in china as well as  
**Translation:** Vocabulary: historically: 历史上; quantitative: 量化

**[3101.68s] English:** elsewhere and they have always had a significant number of gpus right in the past a lot of these  
**Translation:** 

**[3106.40s] English:** high frequency trading algorithmic quant traders used fpgas uh but it shifted to gpus definitely  
**Translation:** Vocabulary: algorithmic: 算法; quant: 量化

**[3112.12s] English:** and there's both right but gpus especially and  
**Translation:** 

**[3114.72s] English:** deep and high flyer which is the hedge fund that owns deep seek  
**Translation:** 

**[3117.34s] English:** and everyone who works for deep seek is part of high fly  
**Translation:** 

**[3120.00s] English:** to some extent, right? Same parent company, same owner, same CEO. They had all these resources  
**Translation:** 

**[3126.46s] English:** and infrastructure for trading. And then they devoted a humongous portion of them to training  
**Translation:** 

**[3132.74s] English:** models, both language models and otherwise, right? Because these techniques were heavily AI  
**Translation:** Vocabulary: humongous: 巨大

**[3138.74s] English:** influenced. More recently, people have realized, hey, trading with... Even when you go back to  
**Translation:** 

**[3146.92s] English:** Renaissance and all these quantitative firms, natural language processing is the key to  
**Translation:** Vocabulary: renaissance: 文艺复兴

**[3151.50s] English:** trading really fast, right? Understanding a press release and making the right trade, right?  
**Translation:** 

**[3156.16s] English:** And so DeepSeek has always been really good at this. And even as far back as 2021,  
**Translation:** 

**[3161.20s] English:** they have press releases and papers saying like, hey, we're the first company in China with an  
**Translation:** 

**[3166.42s] English:** A100 cluster this large, those 10,000 A100 GPUs, right? This is in 2021. Now, this wasn't all for  
**Translation:** 

**[3172.68s] English:** training large language models. This was mostly for training models for  
**Translation:** 

**[3176.84s] English:** their quantitative aspects, their quantitative trading, as well as a lot of that was natural  
**Translation:** 

**[3181.10s] English:** language processing, to be clear, right? And so this is the sort of history, right?  
**Translation:** 

**[3184.98s] English:** So verifiable fact is that in 2021, they built the largest cluster, at least they claim it was  
**Translation:** Vocabulary: cluster: 计算集群; verifiable: 可验证的

**[3189.82s] English:** the largest cluster in China, 10,000 GPUs. Before expert controls started.  
**Translation:** 

**[3194.34s] English:** Yeah.  
**Translation:** 

**[3194.84s] English:** It's like they've had a huge cluster before any conversation of expert controls.  
**Translation:** 

**[3198.22s] English:** So then you step it forward to like, what have they done over the last four years since then,  
**Translation:** 

**[3202.52s] English:** right? Obviously, they've continued to operate the hedge fund, probably make tons of money,  
**Translation:** 

**[3206.54s] English:** right? And the other thing is that they've leaned more and more and more into AI. The CEO,  
**Translation:** 

**[3211.56s] English:** Liang Qingfeng, Liang...  
**Translation:** 

**[3213.48s] English:** You're not putting me in spot on this. We discussed this before.  
**Translation:** Vocabulary: qingfeng: 清风

**[3216.22s] English:** Liang Qingfeng, right? The CEO, he owns maybe a little bit more than half the company,  
**Translation:** 

**[3221.84s] English:** allegedly, right? Is an extremely like Elon Jensen kind of figure where he's just like  
**Translation:** Vocabulary: allegedly: 据说; liang: 梁

**[3227.92s] English:** involved in everything, right? And so over that time period, he's gotten really in-depth into AI.  
**Translation:** 

**[3234.00s] English:** He actually has a bit of a like a...  
**Translation:** 

**[3236.54s] English:** I see some of the statements, a bit of an IAC vibe almost, right?  
**Translation:** 

**[3239.64s] English:** Total...  
**Translation:** 

**[3240.00s] English:** AGI vibes. They're like, we need to do this. We need to make a new ecosystem of open AI. We need  
**Translation:** 

**[3246.88s] English:** China to lead on this sort of ecosystem because historically the Western countries have led on  
**Translation:** Vocabulary: vibes: 感觉

**[3251.80s] English:** software ecosystems. And he straight up acknowledges in order to do this, we need to do  
**Translation:** 

**[3257.92s] English:** something different. DeepSeek is his way of doing this. Some of the translated interviews with him  
**Translation:** 

**[3262.82s] English:** are fantastic. So he has done interviews?  
**Translation:** 

**[3264.36s] English:** Yeah.  
**Translation:** 

**[3264.76s] English:** You think he would do a Western interview or no? Or is there controls on the channel?  
**Translation:** 

**[3268.26s] English:** Hasn't been one yet, but I would try it.  
**Translation:** 

**[3271.52s] English:** I just got a Chinese translator. So it was great. This is all push. So fascinating figure,  
**Translation:** 

**[3277.42s] English:** engineer, pushing full on into AI, leveraging the success from the high frequency trading.  
**Translation:** Vocabulary: leveraging: 利用; translator: 翻译机

**[3284.10s] English:** Very direct quotes. We will not switch to closed source when asked about this stuff.  
**Translation:** 

**[3289.56s] English:** Very long-term motivated in how the ecosystem of AI should work. And I think from a Chinese  
**Translation:** 

**[3298.08s] English:** perspective...  
**Translation:** 

**[3298.26s] English:** He wants a Chinese company to build this vision.  
**Translation:** 

**[3303.08s] English:** And so this is sort of like the quote-unquote visionary behind the company, right? This hedge  
**Translation:** 

**[3307.38s] English:** fund still exists, right? This quantitative firm. And so DeepSeek is the sort of...  
**Translation:** Vocabulary: quantitative: 量化; visionary: 有远见的人

**[3313.14s] English:** Slowly he got turned to this full view of AI, everything about this, right? But at some point,  
**Translation:** 

**[3318.44s] English:** it slowly maneuvered and he made DeepSeek. And DeepSeek has done multiple models since then.  
**Translation:** Vocabulary: maneuvered: 调整方向

**[3323.20s] English:** They've acquired more and more GPUs. They share infrastructure with the fund,  
**Translation:** 

**[3327.20s] English:** right?  
**Translation:** 

**[3328.26s] English:** And so there is no exact number of public GPU resources that they have, but besides this 10,000  
**Translation:** 

**[3335.40s] English:** GPUs that they bought in 2021, right? And they were fantastically profitable, right? And then  
**Translation:** Vocabulary: fantastically: 极其; profitable: 盈利的

**[3340.42s] English:** this paper claims they did only 2,000 H800 GPUs, which are a restricted GPU that was previously  
**Translation:** 

**[3346.50s] English:** allowed in China, but no longer allowed. And there's a new version, but it's basically NVIDIA's  
**Translation:** 

**[3350.58s] English:** H100 for China, right? And there's some restrictions on it specifically around the  
**Translation:** 

**[3355.04s] English:** communications sort of speed, the interconnect speed.  
**Translation:** Vocabulary: interconnect: 互联速度

**[3358.24s] English:** Right? Which is why they had to do this crazy  
**Translation:** 

**[3360.00s] English:** SM scheduling stuff. So going back to that, this is obviously not true in terms of their total GPU  
**Translation:** 

**[3367.82s] English:** count. Obvious available GPUs, but for this training run, you think 2000 is the correct  
**Translation:** 

**[3373.30s] English:** number or no? So this is where it takes a significant amount of zoning in. What do you  
**Translation:** 

**[3380.40s] English:** call your training run? Do you count all of the research and ablations that you ran, picking all  
**Translation:** 

**[3386.02s] English:** this stuff? Because yes, you can do a YOLO run, but at some level you have to do the test at the  
**Translation:** Vocabulary: ablations: 删减测试

**[3389.88s] English:** small scale. And then you have to do some tests at medium scale before you go to a large scale.  
**Translation:** 

**[3393.78s] English:** Accepted practice is that for any given model that is a notable advancement, you're going to  
**Translation:** Vocabulary: advancement: 进步

**[3398.56s] English:** do two to four X compute of the full training run in experiments alone. So a lot of this compute  
**Translation:** 

**[3404.28s] English:** that's being scaled up is probably used in large part at this time for research. Yeah. And research  
**Translation:** 

**[3409.74s] English:** begets the new ideas that let you get huge efficiency. Research gets you O1. Research  
**Translation:** 

**[3415.30s] English:** gets you break.  
**Translation:** Vocabulary: begets: 产生

**[3416.02s] English:** So some of the pricing strategy that we'll discuss has the research baked into the price.  
**Translation:** 

**[3422.66s] English:** So the numbers that DeepSeek specifically said publicly, right, are just the 10,000 GPUs in 2021  
**Translation:** 

**[3427.58s] English:** and then 2000 GPUs for only the pre-training for V3. They did not discuss cost on R1. They did not  
**Translation:** 

**[3434.68s] English:** discuss cost on all the other RL, right, for the instruct model that they made, right? They only  
**Translation:** Vocabulary: instruct: 指导模型

**[3440.24s] English:** discussed the pre-training for the base model and they did not discuss anything on research and  
**Translation:** 

**[3444.42s] English:** ablations. And they do not discuss cost on R1. And they do not discuss cost on R2. And they do not  
**Translation:** 

**[3445.30s] English:** talk about any of the resources that are shared in terms of, hey, the fund is using all these GPUs,  
**Translation:** 

**[3450.60s] English:** right? And we know that they're very profitable and that 10,000 GPUs in 2021. So some of the  
**Translation:** 

**[3458.88s] English:** research that we've found is that we actually believe they have closer to 50,000 GPUs.  
**Translation:** 

**[3463.68s] English:** We as Semi Analysis, so we should say that you're sort of one of the world experts in figuring out  
**Translation:** 

**[3469.68s] English:** what everybody's doing in terms of the semiconductor, in terms of cluster build-outs, in terms of  
**Translation:** 

**[3473.90s] English:** like who is doing what.  
**Translation:** Vocabulary: cluster: 计算集群; semiconductor: 半导体

**[3475.32s] English:** In terms of training runs. So yeah, so that's the we. Okay, go ahead.  
**Translation:** 

**[3479.56s] English:** Yeah, sorry.  
**Translation:** 

**[3480.00s] English:** we believe they actually have something closer to 50,000 gpus right now this is this is split  
**Translation:** 

**[3484.92s] English:** across many tasks right again the fund um research and ablations for ballpark how much would open ai  
**Translation:** Vocabulary: ballpark: 大致范围

**[3490.72s] English:** or anthropic had i think the clearest example we have because meta is also open they talk about  
**Translation:** 

**[3495.86s] English:** like order of 60k to 100k h100 equivalent gpus in their training clusters right so so like llama  
**Translation:** Vocabulary: clusters: 训练集群; llama: 羊驼模型

**[3502.44s] English:** three they said they trained on 16,000 h100s right but the company of meta last year publicly  
**Translation:** 

**[3507.72s] English:** disclosed they bought like 400 something thousand gpus yeah right so so of course tiny percentage on  
**Translation:** 

**[3512.58s] English:** the training again like most of it is like serving me the best instagram reels right um or whatever  
**Translation:** 

**[3516.88s] English:** right i mean we could get into a cost of like what is the cost of ownership for a 2,000 gpu cluster  
**Translation:** Vocabulary: reels: 短视频

**[3522.42s] English:** 10,000 like there's just different sizes of companies that can afford these things and deep  
**Translation:** 

**[3526.98s] English:** seek is reasonably big their compute allocation compared is one of the top few in the world it's  
**Translation:** Vocabulary: allocation: 分配; reasonably: 相当

**[3535.32s] English:** not open ai anthropic etc but they have a lot of  
**Translation:** 

**[3537.72s] English:** can you general actually just zoom out and also talk about the the hopper architecture the  
**Translation:** 

**[3541.86s] English:** nvidia hopper gpu architecture and the difference between h100 and h800 like you mentioned the  
**Translation:** 

**[3548.86s] English:** interconnects yeah so there's you know ampere was the a100 and then h100 hopper right people  
**Translation:** Vocabulary: ampere: 安培; interconnects: 互联

**[3553.76s] English:** use them synonymously in the u.s because really there's just h100 and now there's h200 right but  
**Translation:** 

**[3558.70s] English:** same thing uh mostly in china they've had two there have been different salvos of export  
**Translation:** Vocabulary: salvos: 一连串攻击; synonymously: 同义地

**[3563.72s] English:** restrictions so initially the u.s government limited on a two-factor scale  
**Translation:** 

**[3567.72s] English:** right which is chip interconnect versus uh flops right so any chip that had interconnects above a  
**Translation:** Vocabulary: flops: 运算次数; interconnect: 连接芯片

**[3573.14s] English:** certain level and flops above a certain floating point operations above a certain level was  
**Translation:** 

**[3577.68s] English:** restricted uh later the government realized that this was a flaw in the restriction and they cut  
**Translation:** Vocabulary: restriction: 限制

**[3583.02s] English:** it down to just floating point operations and so um h800 had high flops low communication  
**Translation:** 

**[3590.86s] English:** exactly so the h800 was the same performance as h100 on flops right but it didn't have it just  
**Translation:** 

**[3597.72s] English:** the interconnect bandwidth cut deep seek knew how  
**Translation:** 

**[3600.00s] English:** to utilize this you know hey even though we're cut back on the interconnect we can do all this  
**Translation:** Vocabulary: bandwidth: 带宽

**[3604.92s] English:** fancy stuff to figure out how to use the gpu fully anyways right and and so that was back in october  
**Translation:** 

**[3611.40s] English:** 2022 but uh later in 2023 end of 2023 implemented in 2024 the u.s government banned the h800 right  
**Translation:** 

**[3619.62s] English:** and so by the way this h800 cluster these 2000 gpus was not even purchased in 2024 right it's  
**Translation:** 

**[3624.92s] English:** purchased in late 2023 um and they're just getting the model out now right because it takes a lot of  
**Translation:** Vocabulary: cluster: 计算集群

**[3629.82s] English:** research etc um h800 was banned and now there's a new chip called the h20 uh the h20 is uh cut back  
**Translation:** 

**[3636.96s] English:** on only flops but the interconnect bandwidth is the same and in fact in some ways it's better than  
**Translation:** 

**[3641.90s] English:** the h100 because it has better memory bandwidth and memory capacity so there are you know nvidia  
**Translation:** 

**[3646.66s] English:** is working within the constraints of what the government says and then get builds the best  
**Translation:** Vocabulary: constraints: 限制

**[3650.98s] English:** possible gpu for china can we take this actual tangent and we'll return back to the hardware  
**Translation:** 

**[3655.32s] English:** is the the philosophy the the motivation  
**Translation:** 

**[3658.54s] English:** the case  
**Translation:** 

**[3659.82s] English:** for expert controls what is it uh daria just published a blog post about expert controls  
**Translation:** 

**[3665.00s] English:** the case he makes is that if ai becomes super powerful and he says by 2026 we'll have agi or  
**Translation:** 

**[3672.60s] English:** super powerful ai and that's going to give a significant whoever builds that will have a  
**Translation:** 

**[3677.02s] English:** significant military advantage and so because the united states is a democracy and as he says china  
**Translation:** 

**[3684.84s] English:** is uh authoritarian or has authoritarian elements  
**Translation:** 

**[3688.92s] English:** you want to have a super powerful ai and that's going to give a significant military advantage  
**Translation:** 

**[3689.80s] English:** you want a unipolar world where the super powerful military because of the ai is one that's a  
**Translation:** Vocabulary: unipolar: 单极世界

**[3696.52s] English:** democracy it's a much more complicated world geopolitically when you have two superpowers  
**Translation:** 

**[3702.42s] English:** with super powerful ai and one is authoritarian so that's the case he makes and so we want to  
**Translation:** Vocabulary: authoritarian: 独裁统治; geopolitically: 地缘政治; superpowers: 超级大国

**[3708.78s] English:** uh the united states wants to use expert controls to slow down to make sure that china can't do  
**Translation:** 

**[3716.16s] English:** these gigantic uh training runs  
**Translation:** Vocabulary: gigantic: 巨大的

**[3719.80s] English:** that they know how to do  
**Translation:** 

**[3726.28s] English:** so  
**Translation:** 

**[3730.98s] English:** you  
**Translation:** 

**[3745.06s] English:** you  
**Translation:** 

**[3746.82s] English:** you  
**Translation:** 

**[3748.92s] English:** you  
**Translation:** 

**[3749.00s] English:** you  
**Translation:** 

**[3749.42s] English:** you  
**Translation:** 

**[3749.62s] English:** you  
**Translation:** 

**[3749.68s] English:** you  
**Translation:** 

**[3749.70s] English:** you  
**Translation:** 

**[3749.74s] English:** you  
**Translation:** 

**[3749.76s] English:** you  
**Translation:** 

**[3720.00s] English:** be presumably required to build AGI. This is very abstract. I think this can be the goal of how some  
**Translation:** Vocabulary: presumably: 大概

**[3726.80s] English:** people describe export controls is this super powerful AI. And you touched on the training run  
**Translation:** 

**[3733.04s] English:** idea. There's not many worlds where China cannot train AI models. Export controls are kneecapping  
**Translation:** 

**[3741.66s] English:** the amount of compute or the density of compute that China can have. And if you think about the  
**Translation:** 

**[3747.90s] English:** AI ecosystem right now, as all of these AI companies, revenue numbers are up and to the  
**Translation:** Vocabulary: density: 计算密度

**[3752.34s] English:** right. Their AI usage is just continuing to grow. More GPUs are going to inference. A large part of  
**Translation:** 

**[3757.84s] English:** export controls, if they work, is just that the amount of AI that can be run in China is going  
**Translation:** Vocabulary: inference: 推断

**[3764.38s] English:** to be much lower. So on the training side, DeepSeek v3 is a great example, which you have a very  
**Translation:** 

**[3768.88s] English:** focused team that can still get to the frontier of AI. On this, 2,000 GPUs is not that hard to get,  
**Translation:** Vocabulary: frontier: 最前沿

**[3774.64s] English:** all considering in the world. They're still going to  
**Translation:** 

**[3777.84s] English:** have to be able to get to the frontier of AI. They're still going to have to be able to get to  
**Translation:** 

**[3777.88s] English:** the frontier of AI. They're still going to have to be able to get to the frontier of AI. They're still  
**Translation:** 

**[3777.90s] English:** going to have those GPUs. They're still going to be able to train models. But if there's going to be  
**Translation:** 

**[3780.82s] English:** a huge market for AI, if you have strong export controls and you want to have 100,000 GPUs just  
**Translation:** 

**[3785.46s] English:** serving the equivalent of chat GPT clusters, with good export controls, it also just makes it so  
**Translation:** Vocabulary: clusters: 计算集群

**[3790.12s] English:** that AI can be used much less. And I think that is a much easier goal to achieve than trying to  
**Translation:** 

**[3798.48s] English:** debate on what AGI is. And if you have these extremely intelligent, autonomous AIs and data  
**Translation:** Vocabulary: autonomous: 自主

**[3803.92s] English:** centers, those are the things that could be running in these GPU clusters.  
**Translation:** 

**[3807.68s] English:** To some extent, training a model does effectively nothing, right?  
**Translation:** 

**[3813.08s] English:** The thing that Dario is sort of speaking to is the implementation of that model,  
**Translation:** 

**[3820.26s] English:** once trained, to then create huge economic growth, huge increases in military capabilities,  
**Translation:** Vocabulary: implementation: 实施

**[3826.32s] English:** huge increases in productivity of people, betterment of lives, whatever you want to direct  
**Translation:** 

**[3831.38s] English:** super powerful AI towards, you can't. But that requires significant amounts of compute, right?  
**Translation:** 

**[3836.86s] English:** And so the U.S.  
**Translation:** 

**[3837.62s] English:** government has effectively said...  
**Translation:** 

**[3840.00s] English:** And forever, right?  
**Translation:** 

**[3841.44s] English:** Like training will always be a portion of the total compute.  
**Translation:** 

**[3845.02s] English:** You know, we mentioned Meta's 400,000 GPUs, only 16,000 made Lama, right?  
**Translation:** 

**[3849.10s] English:** So the percentage that Meta is dedicating to inference, now this might be for recommendation  
**Translation:** 

**[3853.68s] English:** systems that are trying to hack our mind into spending more time and watching more ads,  
**Translation:** 

**[3857.38s] English:** or if it's for a super powerful AI that's doing productive things, it doesn't matter  
**Translation:** 

**[3862.06s] English:** about the exact use that our economic system decides.  
**Translation:** 

**[3865.14s] English:** It's that that can be delivered in whatever way we want.  
**Translation:** 

**[3868.26s] English:** Whereas with China, right?  
**Translation:** 

**[3870.24s] English:** You know, you're, you know, expert restrictions, great.  
**Translation:** 

**[3872.60s] English:** You're never going to be able to cut everything off, right?  
**Translation:** 

**[3874.84s] English:** And that's, that's like, I think that's quite well understood by the US government is that  
**Translation:** 

**[3878.52s] English:** you can't cut everything off, you know, they'll make their own chips and they're trying to  
**Translation:** 

**[3882.86s] English:** make their own chips.  
**Translation:** 

**[3883.44s] English:** They'll be worse than ours.  
**Translation:** 

**[3884.18s] English:** But, you know, this is the whole point is to just keep a gap, right?  
**Translation:** 

**[3887.24s] English:** And therefore, at some point as the AI, you know, in a world where two, 3% economic growth,  
**Translation:** 

**[3891.76s] English:** this is really dumb, by the way, right?  
**Translation:** 

**[3893.44s] English:** To cut off, you know, high tech and not make money off of it.  
**Translation:** 

**[3896.64s] English:** But in a world where super.  
**Translation:** 

**[3898.26s] English:** Powerful AI comes about and then starts creating significant changes in society, which is what  
**Translation:** 

**[3903.12s] English:** all the AI leaders and big tech companies believe, I think super powerful AI is going  
**Translation:** 

**[3906.84s] English:** to change society massively.  
**Translation:** 

**[3908.52s] English:** And therefore, this compounding effect of the difference in compute is really important.  
**Translation:** Vocabulary: compounding: 累积效应; massively: 大规模地

**[3912.58s] English:** There's some sci-fi out there where like AI is, is like measured in the power of in like  
**Translation:** 

**[3917.92s] English:** how much power is delivered to compute, right?  
**Translation:** 

**[3919.58s] English:** Or how much is being, you know, that's sort of a way of thinking about what's the economic  
**Translation:** 

**[3923.36s] English:** output is just how much power you directing towards that AI.  
**Translation:** 

**[3926.46s] English:** Should we talk about reasoning models with this?  
**Translation:** 

**[3928.26s] English:** As a way that this might be actionable as something that people can actually see.  
**Translation:** 

**[3932.02s] English:** So the reasoning models that are coming out with R1 and O1, they're designed to use more compute.  
**Translation:** 

**[3937.38s] English:** There's a lot of buzzy words in the AI community about this test time, compute, inference, time,  
**Translation:** Vocabulary: buzzy: 热门; inference: 推理

**[3942.72s] English:** compute, whatever.  
**Translation:** 

**[3944.22s] English:** But Dylan has good research on this.  
**Translation:** Vocabulary: dylan: Dylan

**[3946.02s] English:** You can get to the specific numbers on the ratio of when you train a model, you can look at things  
**Translation:** 

**[3949.58s] English:** about the amount of compute used at training and amount of compute used at inference.  
**Translation:** 

**[3953.22s] English:** These reasoning models are making inference way more important to doing complex tasks.  
**Translation:** 

**[3957.36s] English:** In the fall, in December,  
**Translation:** 

**[3960.00s] English:** their open ai announced this o3 model there's another thing in ai when things move fast we get  
**Translation:** 

**[3964.40s] English:** both announcements and releases announcements are essentially blog posts where you pat yourself on  
**Translation:** 

**[3968.46s] English:** the back and you say you did things and releases are on the models out there the papers out there  
**Translation:** 

**[3972.24s] English:** etc so open ai has announced o3 and we can check if o3 mini is out as of recording potentially  
**Translation:** 

**[3978.24s] English:** but that doesn't really change the point which is that the breakthrough result was something  
**Translation:** 

**[3982.96s] English:** called arc agi task which is the abstract reasoning corpus a task for artificial general  
**Translation:** 

**[3988.48s] English:** intelligence um francois chalet is the guy who's been it's a multi-year old paper it's a brilliant  
**Translation:** 

**[3994.98s] English:** benchmark and the number for open ai o3 to solve this was that it used some sort of number of  
**Translation:** Vocabulary: benchmark: 衡量标准

**[4001.78s] English:** samples in the api the api has like thinking effort and number of samples they used a thousand  
**Translation:** 

**[4006.84s] English:** samples to solve this task and it comes out to be like five to twenty dollars per question which  
**Translation:** 

**[4013.50s] English:** you're you're putting in effectively a math puzzle and then it takes orders of dollars to answer one  
**Translation:** 

**[4018.12s] English:** question  
**Translation:** 

**[4018.48s] English:** and this is a lot of compute if those are going to take off in the u.s open ai needs a ton of gpus  
**Translation:** 

**[4023.66s] English:** on inference to capture this they have this open ai chat gpt pro subscription which is two hundred  
**Translation:** Vocabulary: subscription: 订阅

**[4028.70s] English:** dollars a month which sam said they're losing money on which means that people are burning a  
**Translation:** 

**[4032.56s] English:** lot of gpus on inference and i've signed up with it i've played with it i don't think i'm a power  
**Translation:** 

**[4036.92s] English:** user but i i use it and it's like that is the thing that a chinese company with mediumly strong  
**Translation:** 

**[4043.72s] English:** expert controls there will always be loopholes might not be able to do it all and if that  
**Translation:** Vocabulary: loopholes: 漏洞

**[4047.94s] English:** that's the thing that a chinese company with mediumly strong expert controls there will always  
**Translation:** 

**[4048.12s] English:** be loopholes might not be able to do it all and if that the main result for o3 is also a spectacular  
**Translation:** 

**[4051.22s] English:** coding performance and if that feeds back into ai companies being able to experiment better so  
**Translation:** 

**[4057.78s] English:** presumably the idea is for an agi a much larger fraction of the compute would be used for this  
**Translation:** Vocabulary: presumably: 大概

**[4064.28s] English:** test time compute for the reasoning for the agi goes into a room and thinks about how to  
**Translation:** 

**[4068.96s] English:** take over the world and that you know come back in 2.7 hours this is what it's going to take a lot  
**Translation:** 

**[4076.12s] English:** of computers this is what people are like  
**Translation:** 

**[4078.12s] English:** c.e.o. or leaders of opening  
**Translation:** 

**[4080.00s] English:** AI and anthropic talk about is autonomous AI models, which is you give them a task and they  
**Translation:** 

**[4084.46s] English:** work on it in the background. My personal definition of AGI is much simpler. I think  
**Translation:** Vocabulary: autonomous: 自主

**[4090.68s] English:** language models are a form of AGI and all this super powerful stuff is a next step that's great  
**Translation:** 

**[4095.52s] English:** if we get these tools, but a language model has so much value in so many domains that it's a  
**Translation:** 

**[4099.86s] English:** general intelligence to me. But this next step of agentic things where they're independent and  
**Translation:** 

**[4104.90s] English:** they can do tasks that aren't in the training data is what the few year outlook that these AI  
**Translation:** 

**[4111.02s] English:** companies are driving for. I think the terminology here that Dario uses is super powerful AI. So I  
**Translation:** 

**[4118.16s] English:** agree with you on the AGI. I think we already have something like that's exceptionally impressive  
**Translation:** Vocabulary: exceptionally: 特别; terminology: 术语

**[4122.32s] English:** that Alan Turing would for sure say is AGI, but he's referring more to something once in possession  
**Translation:** 

**[4128.66s] English:** of, then you would have a significant military and geopolitical advantage over other nations.  
**Translation:** Vocabulary: geopolitical: 地缘政治; turing: 图灵

**[4134.34s] English:** So it's not...  
**Translation:** 

**[4134.90s] English:** It's not just like you can ask it how to cook an omelet.  
**Translation:** 

**[4138.38s] English:** And he has a much more positive view in his essay, Machines of Love and Grace. I've read into this.  
**Translation:** 

**[4143.10s] English:** I don't have enough background in physical sciences to gauge exactly how competent I am.  
**Translation:** Vocabulary: competent: 有能力的; gauge: 评估

**[4147.42s] English:** If AI can revolutionize biology, I'm safe saying that AI is going to accelerate the  
**Translation:** 

**[4154.32s] English:** progress of any computational science. So we're doing a depth first search here  
**Translation:** Vocabulary: accelerate: 加速; computational: 计算; revolutionize: 革命化

**[4157.78s] English:** on topics, taking tangent of a tangent. So let's continue on that depth first search.  
**Translation:** 

**[4162.62s] English:** You said that you're both feeling the AGI. So what's your timeline? Dario's 2026 for the super  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[4173.22s] English:** powerful AI that's basically agentic to a degree where it's a real security threat,  
**Translation:** 

**[4181.30s] English:** that level of AGI. What's your timeline?  
**Translation:** 

**[4184.70s] English:** I don't like to attribute specific abilities because predicting specific abilities and when  
**Translation:** 

**[4188.94s] English:** is very hard. I think mostly if you're going to say that I'm feeling the AGI,  
**Translation:** Vocabulary: attribute: 归因

**[4192.78s] English:** is that I expect continued rapid surprising progress over the next few years.  
**Translation:** 

**[4197.08s] English:** So something like R1 is less.  
**Translation:** 

**[4200.00s] English:** surprising to me from deep seek because i expect there to be new paradigms where substantial  
**Translation:** 

**[4204.26s] English:** progress can be made i think deep seek r1 is so unsettling because we're kind of on this path with  
**Translation:** Vocabulary: paradigms: 基本模式; unsettling: 不安

**[4209.44s] English:** with chat gpt it's like it's getting better it's getting better it's getting better and then we  
**Translation:** 

**[4212.60s] English:** have a new direction for for changing the models and we took one step like this and we like took  
**Translation:** 

**[4216.92s] English:** a step up so it looks like a really fast slope and then we're going to just take more steps  
**Translation:** 

**[4220.80s] English:** so like this is really unsettling when you have these big steps and i expect that to keep happening  
**Translation:** 

**[4225.76s] English:** i see i've tried opening i operator i've tried claude computer use they're not there yet i  
**Translation:** 

**[4232.36s] English:** understand the idea but it's just so hard to predict what is the breakthrough that will make  
**Translation:** 

**[4236.90s] English:** something like that work and i think it's more likely that we have breakthroughs that work and  
**Translation:** 

**[4241.24s] English:** things that we don't know what they're going to do so like everyone wants agents dario has very  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[4245.44s] English:** eloquent way of describing this and i just think that it's like there's going to be more than that  
**Translation:** 

**[4251.20s] English:** so i could just expect these things to come i'm gonna have to try to pin you down to a date  
**Translation:** Vocabulary: eloquent: 口才好

**[4255.74s] English:** on the agi timeline uh like the nuclear weapon moment so moment where on the geopolitical stage  
**Translation:** 

**[4265.22s] English:** there's a real like you know because we're talking about export controls  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[4270.84s] English:** when do you think just even to throw out a date when do you think that would be like for me it's  
**Translation:** 

**[4276.72s] English:** probably after 2030 so i'm not as what i would say so define that right because to me it kind  
**Translation:** 

**[4282.88s] English:** of almost has already happened right you look at elections in india  
**Translation:** 

**[4285.74s] English:** and pakistan people get ai voice calls and think they're talking to the politician right the ai  
**Translation:** 

**[4291.50s] English:** diffusion rules which was enacted in the last couple weeks of the biden admin and looks like  
**Translation:** 

**[4295.04s] English:** the trump admin will keep and potentially even strengthen limit cloud computing and gpu sales  
**Translation:** Vocabulary: admin: 行政部门; computing: 计算; diffusion: 扩散; enacted: 制定

**[4301.06s] English:** to countries that are not even related to china it's like this is portugal and all these like  
**Translation:** 

**[4305.84s] English:** normal company countries are on the you need approval from the u.s list like yeah portugal  
**Translation:** 

**[4310.44s] English:** and like you know like like all these countries that are allies right singapore right like they  
**Translation:** 

**[4314.76s] English:** they freaking have  
**Translation:** Vocabulary: freaking: damn

**[4315.74s] English:** 35s and we don't let them buy gpus like this is this to me is already to this  
**Translation:** 

**[4320.00s] English:** scale of like you know well that just means that uh the u.s military is really nervous about this  
**Translation:** 

**[4326.16s] English:** new technology that doesn't mean the technology is already there so like they might be just very  
**Translation:** 

**[4331.76s] English:** cautious about this thing that they don't quite understand but that's a really good point sort of  
**Translation:** 

**[4336.16s] English:** the the robocalls swarms of semi-intelligent bots could be a weapon could be doing a lot of social  
**Translation:** 

**[4344.84s] English:** engineering i mean there's tons of talk about you know from the 2016 elections like cambridge  
**Translation:** Vocabulary: robocalls: 自动电话外呼

**[4348.98s] English:** analytica and all this stuff russian influence i mean every country in the world is pushing stuff  
**Translation:** 

**[4353.86s] English:** onto the internet and has narratives they want right like that's every every like technically  
**Translation:** 

**[4357.86s] English:** competent whether it's russia china u.s israel etc right you know people are pushing viewpoints  
**Translation:** 

**[4363.02s] English:** onto the internet en masse and language models crash the cost of like very intelligent sounding  
**Translation:** Vocabulary: viewpoints: 观点

**[4368.34s] English:** language there's some research that shows that the distribution is actually a limiting factor  
**Translation:** 

**[4372.76s] English:** so language models haven't yet made misinformation particularly like  
**Translation:** Vocabulary: misinformation: 错误信息

**[4378.74s] English:** you  
**Translation:** 

**[4378.98s] English:** change the equation there the internet is still ongoing i think there's a blog ai snake oil and  
**Translation:** Vocabulary: equation: 方程式

**[4383.88s] English:** some of my friends at princeton that write on this stuff so there is research it's like it's  
**Translation:** 

**[4387.32s] English:** a default that everyone assumes and i would have thought the same thing is that misinformation  
**Translation:** 

**[4391.28s] English:** doesn't get far worse with language models i think in terms of internet posts and things that people  
**Translation:** 

**[4396.86s] English:** have been measuring it hasn't been a exponential increase or something extremely measurable and  
**Translation:** Vocabulary: exponential: 指数的; measurable: 可测量的

**[4401.44s] English:** things you're talking about with like voice calls and stuff like that it could be in modalities that  
**Translation:** 

**[4405.90s] English:** are harder to measure so it's it's something that it's too soon to tell in terms of i think  
**Translation:** Vocabulary: modalities: 沟通方式

**[4411.64s] English:** that's like political instability via the web is very it's it's monitored by a lot of researchers  
**Translation:** 

**[4418.32s] English:** to see what's happening i think that you're asking about like the agi thing i might if i  
**Translation:** 

**[4425.34s] English:** ever make me give a year i'm gonna be like okay i have ai ceo saying this they've been saying two  
**Translation:** 

**[4429.14s] English:** years for a while i think that they're people like dario at anthropic the ceo had thought  
**Translation:** 

**[4435.88s] English:** about this so deeply. I need to take their words seriously, but also  
**Translation:** 

**[4440.00s] English:** also understand that they have different incentives. So I would be like, add a few  
**Translation:** Vocabulary: incentives: 动机

**[4444.46s] English:** years to that, which is how you get something similar to 2030 or a little after 2030.  
**Translation:** 

**[4448.46s] English:** I think to some extent, we have capabilities that hit a certain point where any one person could say,  
**Translation:** 

**[4453.82s] English:** oh, okay, if I can leverage those capabilities for X amount of time, this is AGI, right? Call it 27,  
**Translation:** 

**[4459.42s] English:** 28. But then the cost of actually operating that capability is so, so extreme that no one can  
**Translation:** 

**[4466.62s] English:** actually deploy it at scale and mass to actually completely revolutionize the economy on a snap  
**Translation:** 

**[4472.74s] English:** of a finger. So I don't think it will be like a snap of the finger moment. It's a physical constraint.  
**Translation:** Vocabulary: constraint: 物理限制; deploy: 部署; revolutionize: 彻底变革

**[4476.62s] English:** Rather, it'll be a, oh, the capabilities are here, but I can't deploy it everywhere, right?  
**Translation:** 

**[4481.30s] English:** And so one simple example going back sort of to 2023 was when Bing with GPT-4 came out and  
**Translation:** 

**[4488.96s] English:** everyone was freaking out about search, right? Perplexity came out. If you did the cost on like,  
**Translation:** 

**[4493.16s] English:** hey, implementing GPT-3 into every Google search, it was like, oh, okay,  
**Translation:** Vocabulary: freaking: 恐慌; implementing: 实施; perplexity: 困惑

**[4496.50s] English:** this is a really good idea. But if you did the cost on like, hey, implementing GPT-3 into every  
**Translation:** 

**[4496.60s] English:** Google search, it was like, oh, okay, this is a really good idea. But if you did the cost on like,  
**Translation:** 

**[4496.62s] English:** this is just like physically impossible to implement, right? And as we step forward to  
**Translation:** 

**[4500.56s] English:** like going back to the test time compute thing, right? A query for, you know, you ask ChatGPT a  
**Translation:** 

**[4505.80s] English:** question, it costs cents, right? For their most capable model of chat, right? To get a query back  
**Translation:** 

**[4511.92s] English:** to solve an Arc AGI problem though, cost five to 20 bucks, right? And this is a-  
**Translation:** 

**[4518.52s] English:** It's only going up from there.  
**Translation:** 

**[4519.68s] English:** This is a thousand, 10,000 X factor difference in cost to respond to a query versus do a task.  
**Translation:** 

**[4525.96s] English:** And the task-  
**Translation:** 

**[4526.60s] English:** The task of Arc AGI, it's not like it's like, it's simple to some extent, you know, but it's  
**Translation:** 

**[4532.24s] English:** also like, what are the tasks that we want? Okay, AGI, quote unquote, what we have today can do Arc  
**Translation:** 

**[4536.88s] English:** AGI. Three years from now, it can do much more complicated problems, but the cost is going to  
**Translation:** 

**[4541.26s] English:** be measured in thousands and thousands and hundreds of thousands of dollars of GPU time.  
**Translation:** 

**[4546.02s] English:** And there just won't be enough power, GPUs, infrastructure to operate this and therefore  
**Translation:** 

**[4550.10s] English:** shift everything in the world on the snap of the finger. But at that moment, who gets to  
**Translation:** 

**[4554.68s] English:** control and point out the problem? And who gets to control and point out the problem?  
**Translation:** 

**[4556.58s] English:** Who gets to control and point the AGI at a task? And so this was in Dario.  
**Translation:** 

**[4560.00s] English:** post that he's like, hey, China can effectively and more quickly than us point their AGI at  
**Translation:** 

**[4565.74s] English:** military tasks, right? And they have been in many ways faster at adopting certain new technologies  
**Translation:** 

**[4570.74s] English:** into their military, right? Especially with regards to drones, right? The US maybe has a  
**Translation:** Vocabulary: drones: 无人机

**[4576.40s] English:** longstanding, you know, large air sort of, you know, fighter jet type of thing, bombers. But  
**Translation:** 

**[4581.72s] English:** when it comes to asymmetric arms, such as drones, they've completely leapfrogged the US and the West.  
**Translation:** Vocabulary: asymmetric: 不对称; leapfrogged: 超越; longstanding: 长期的

**[4587.90s] English:** And the fear that Dario is sort of pointing out there, I think, is that, yeah, great,  
**Translation:** 

**[4593.10s] English:** we'll have AGI in the commercial sector. The US military won't be able to implement it super fast.  
**Translation:** 

**[4598.40s] English:** Chinese military could, and they could direct all their resources to implementing it in the  
**Translation:** 

**[4602.30s] English:** military and therefore solving, you know, military logistics or solving some other aspect of like  
**Translation:** 

**[4607.74s] English:** disinformation for targeted certain set of people so they can flip a country's politics or something  
**Translation:** 

**[4612.62s] English:** like that, that is actually like catastrophic versus, you know, the US just wants to, you know,  
**Translation:** Vocabulary: catastrophic: 灾难性的

**[4617.60s] English:** because of the pandemic.  
**Translation:** 

**[4617.88s] English:** It'll be more capitalistically allocated just towards whatever is the highest return on  
**Translation:** Vocabulary: allocated: 分配; pandemic: 流行病

**[4621.14s] English:** income, which might be like building, you know, factories better or whatever.  
**Translation:** 

**[4624.42s] English:** So everything I've seen, people's intuition seems to fail on robotics. So you have this kind of  
**Translation:** Vocabulary: intuition: 直觉

**[4630.86s] English:** general optimism. I've seen this on self-driving cars. People think it's much easier problem than  
**Translation:** 

**[4635.76s] English:** it is. Similar with drones. Here, I understand it a little bit less, but I've just seen the  
**Translation:** Vocabulary: optimism: 乐观主义

**[4642.30s] English:** reality of the war in Ukraine and the usage of drones on both sides. And it seems,  
**Translation:** 

**[4647.88s] English:** I guess, that humans still far outperform any fully autonomous systems. AI is an assistant,  
**Translation:** Vocabulary: autonomous: 自主的

**[4656.64s] English:** but humans drive. FPV drones where the humans control most of it just far, far, far outperforms  
**Translation:** 

**[4662.58s] English:** AI systems. So I think it's not obvious to me that we're going to have swarms of autonomous robots  
**Translation:** 

**[4668.46s] English:** anytime soon in the military context. Maybe the fastest I can imagine is 2030, which is why I said  
**Translation:** 

**[4675.66s] English:** 2030 for the super powerful AI. I don't know. I don't know. I don't know. I don't know. I don't  
**Translation:** Vocabulary: anytime: 任何时间

**[4677.58s] English:** know. I don't know. I don't know. I don't know. Whenever you have large scale,  
**Translation:** 

**[4680.00s] English:** swarms of robots doing military actions that's when the world just starts to look different  
**Translation:** 

**[4686.00s] English:** to me so that's the thing i'm really worried about but there could be cyber war  
**Translation:** 

**[4690.94s] English:** cyber war type of technologies that uh from social engineering to actually just  
**Translation:** 

**[4696.54s] English:** swarms of robots that find attack vectors in our code bases and shut down power grids that kind of  
**Translation:** 

**[4703.28s] English:** stuff and it could be one of those things like on any given weekend or something power goes out  
**Translation:** 

**[4709.80s] English:** nobody knows why and the world changes forever just power going out for two days in all of the  
**Translation:** 

**[4716.58s] English:** united states that will lead to murder to chaos but going back to expert controls do you see that  
**Translation:** 

**[4725.88s] English:** as a useful way to uh control the balance of power geopolitically in the context of ai  
**Translation:** 

**[4735.50s] English:** and i think going going back to my viewpoint is if you believe we're in this sort of  
**Translation:** 

**[4739.80s] English:** uh stage of economic growth and change that we've been in for the last 20 years the export controls  
**Translation:** 

**[4746.00s] English:** are absolutely guaranteeing that china will win long term right if you do not believe ai is going  
**Translation:** Vocabulary: guaranteeing: 确保

**[4752.60s] English:** to make significant changes to society in the next 10 years or five years right five five year  
**Translation:** 

**[4758.46s] English:** timelines are sort of what the more executives and such of ai companies and even big tech companies  
**Translation:** Vocabulary: executives: 高层管理者; timelines: 时间线

**[4763.18s] English:** believe but even 10-year timelines you know it's reasonable but once you get to hey these these  
**Translation:** 

**[4769.30s] English:** timelines are going to be a big deal and i think that's going to be a big deal and i think that's  
**Translation:** 

**[4769.78s] English:** are uh below that time period then the only way to sort of like create a sizable advantage or  
**Translation:** 

**[4778.32s] English:** disadvantage for america versus china is if you constrain compute because  
**Translation:** Vocabulary: constrain: 限制; sizable: 可观的

**[4783.88s] English:** talent is not really something that's constraining right china arguably has more talent right more  
**Translation:** 

**[4789.66s] English:** stem graduates more programmers the u.s can draw upon the world's people which it does there's tons  
**Translation:** Vocabulary: arguably: 或许; constraining: 限制; programmers: 程序员

**[4794.76s] English:** of you know foreigners in the ai industry so many of these ai teams are all people  
**Translation:** 

**[4799.78s] English:** that are  
**Translation:** 

**[4800.00s] English:** a U.S. passport. Yeah, I mean, many of them are Chinese people who are moving to America,  
**Translation:** 

**[4806.12s] English:** right? And that's great. That's exactly what we want, right? But that talent is one aspect,  
**Translation:** 

**[4811.68s] English:** but I don't think that's one that is a measurable advantage for the U.S. or not.  
**Translation:** 

**[4814.76s] English:** It truly is just whether or not compute, right? Now, even on the compute side, when we look at  
**Translation:** Vocabulary: measurable: 可衡量的

**[4820.72s] English:** chips versus data centers, right? China has the unprecedented ability to build ridiculous sums  
**Translation:** 

**[4826.84s] English:** of power, clockwork, right? They're always building more and more power. They've got  
**Translation:** Vocabulary: clockwork: 机械装置; unprecedented: 前所未有的

**[4832.30s] English:** steel mills that individually are the size of the entire U.S. industry, right? And they've  
**Translation:** 

**[4838.08s] English:** got aluminum mills that consume gigawatts and gigawatts of power, right? And when we talk  
**Translation:** Vocabulary: aluminum: 铝; gigawatts: gig瓦; individually: 单独地

**[4842.64s] English:** about what's the biggest data center, right? OpenAI made this huge thing about Stargate,  
**Translation:** 

**[4846.90s] English:** their announcement there. That's like once it's fully built out in a few years, it'll be two  
**Translation:** Vocabulary: stargate: 星际之门

**[4851.94s] English:** gigawatts, right? Of power, right? And this is still smaller than the largest, you know,  
**Translation:** 

**[4856.84s] English:** industrial facilities in China, right? China, if they wanted to build the largest data center in  
**Translation:** 

**[4861.02s] English:** the world, if they had access to the chips, could. So it's not just, it's just a question of when,  
**Translation:** 

**[4866.78s] English:** not if, right? So their industrial capacity far exceeds the United States?  
**Translation:** 

**[4870.46s] English:** Exactly. To manufacture stuff. So long-term, they're going to be manufacturing chips there.  
**Translation:** 

**[4878.52s] English:** Chips are a little bit more specialized. I'm specifically referring to the data centers,  
**Translation:** Vocabulary: manufacture: 生产

**[4882.10s] English:** right? Chips, fabs take huge amounts of power. Don't get me wrong. That's not necessarily the  
**Translation:** 

**[4886.52s] English:** gating factor there. The gating factor on how fast people can build the largest clusters today  
**Translation:** Vocabulary: clusters: 大规模计算集群

**[4891.36s] English:** in the US is power, right? It is whether it's, now it could be power generation,  
**Translation:** 

**[4896.18s] English:** power transmission, substations, and, you know, all these sorts of transformers and all these  
**Translation:** Vocabulary: substations: 变电站

**[4901.20s] English:** things, building the data center. These are all constraints on the US industry's ability to build  
**Translation:** 

**[4906.92s] English:** larger and larger training systems, as well as deploying more and more inference compute.  
**Translation:** Vocabulary: constraints: 限制; deploying: 部署; inference: 推理

**[4911.68s] English:** I think we need to make the point clear on why the time is now for people that don't,  
**Translation:** 

**[4916.52s] English:** think about this, because essentially with export controls, you're making it so China cannot  
**Translation:** Vocabulary: cannot: 不能

**[4920.00s] English:** make or get cutting edge chips. And the idea is that if you time this wrong, China is pouring  
**Translation:** 

**[4926.98s] English:** a ton of money into their chip production. And if you time it wrong, they are going to have more  
**Translation:** 

**[4930.98s] English:** capacity for production, more capacity for energy and figure out how to make the chips and have more  
**Translation:** 

**[4935.92s] English:** capacity than the rest of the world to make the chips because everybody can buy. They're going  
**Translation:** 

**[4939.88s] English:** to sell their Chinese chips to everybody. They might subsidize them. And therefore, if AI takes  
**Translation:** 

**[4944.76s] English:** a long time to become differentiated, we've kneecapped the financial performance of American  
**Translation:** Vocabulary: kneecapped: 削弱; subsidize: 补贴

**[4948.90s] English:** companies. NVIDIA can sell less. TSMC cannot sell to China. So therefore, we have less demand  
**Translation:** 

**[4956.10s] English:** to therefore keep driving the production cycle. So that's the assumption behind the timing being  
**Translation:** Vocabulary: assumption: 假设

**[4962.90s] English:** less than 10 years or five years to above, right? China will win because of these restrictions  
**Translation:** 

**[4968.28s] English:** long term unless AI does something in the short term, which I believe AI will do,  
**Translation:** 

**[4973.44s] English:** make massive changes to society in the medium short term, right?  
**Translation:** 

**[4977.72s] English:** And so that's the big...  
**Translation:** 

**[4978.90s] English:** Unlocker there. And even today, right? If Xi Jinping decided to get, quote unquote,  
**Translation:** 

**[4984.98s] English:** scale-pilled, right? I.e. decide that scaling laws are what matters, right? Just like the US  
**Translation:** Vocabulary: unlocker: 解锁器; unquote: 反引号

**[4991.52s] English:** executives like Satya Nadella and Mark Zuckerberg and Sundar and all these US executives of the  
**Translation:** 

**[4997.52s] English:** biggest, most powerful tech companies have decided they're scale-pilled and they're building  
**Translation:** Vocabulary: executives: 高管; zuckerberg: 扎克伯格

**[5001.62s] English:** multi-gigawatt data centers, right? Whether it's in Texas or Louisiana or Wisconsin,  
**Translation:** 

**[5005.72s] English:** wherever it is, they're building these massive things.  
**Translation:** Vocabulary: texas: 德克萨斯州

**[5008.90s] English:** That cost as much as their entire budget for spending on data centers globally in one spot,  
**Translation:** 

**[5014.48s] English:** right? This is what they've committed to for next year, year after, et cetera. And so they're so  
**Translation:** Vocabulary: globally: 全世界

**[5019.90s] English:** convinced that this is the way, that this is what they're doing. But if China decided to,  
**Translation:** 

**[5025.08s] English:** they could do it faster than us. But this is where the restrictions come in.  
**Translation:** 

**[5028.94s] English:** It is not clear that China as a whole has decided from the highest levels that this is a priority.  
**Translation:** 

**[5034.18s] English:** The US sort of has, right? You see Trump talking about deep seek and,  
**Translation:** 

**[5038.90s] English:** uh, Stargate within the same.  
**Translation:** 

**[5040.00s] English:** week, right? And the Biden admin as well had a lot of discussions about AI and such. It's clear  
**Translation:** Vocabulary: admin: 行政部门

**[5045.44s] English:** that they think about it. Only just last week did DeepSeek meet the second in command of China,  
**Translation:** 

**[5051.82s] English:** right? They have not even met the top, right? They haven't met Xi. Xi hasn't sat down. And they only  
**Translation:** 

**[5057.18s] English:** just released a subsidy of a trillion RMB, roughly $160 billion, which is closer to the spending of  
**Translation:** 

**[5065.38s] English:** Microsoft and Meta and Google combined, right, for this year. So it's like they're realizing it  
**Translation:** 

**[5071.42s] English:** just now, but that's where the export restrictions come in and say, hey, you can't ship the most  
**Translation:** 

**[5077.30s] English:** powerful US chips to China. You can ship a cut down version. You can't ship the most powerful  
**Translation:** 

**[5083.66s] English:** chips to all these countries who we know are just going to rent it to China. You have to limit the  
**Translation:** 

**[5088.08s] English:** numbers, right? And the tools. And same with manufacturing tools, all these different  
**Translation:** 

**[5093.16s] English:** aspects. But it all stems from AI.  
**Translation:** 

**[5095.10s] English:** And then what downstream can slow them down in AI? And so the entire semiconductor restrictions,  
**Translation:** 

**[5100.62s] English:** you read them, they are very clear. It's about AI and military civil fusion of technology,  
**Translation:** 

**[5105.90s] English:** right? It's very clear. And then from there, it goes, oh, well, we're banning them from buying  
**Translation:** 

**[5109.76s] English:** lithography tools and etch tools and deposition tools. And oh, this random subsystem from a  
**Translation:** 

**[5115.60s] English:** random company that's tiny, right? Why are we banning this? Because all of it, the US government  
**Translation:** Vocabulary: deposition: 沉积; lithography: 光刻

**[5120.38s] English:** has decided is critical to AI systems. I think the fulcrum point is,  
**Translation:** 

**[5125.10s] English:** the transition from 7 nanometer to 5 nanometer chips, where I think it was Huawei that had the  
**Translation:** Vocabulary: fulcrum: 支点; nanometer: 纳米

**[5130.26s] English:** 7 nanometer chip a few years ago, which caused another political brouhaha, almost like this  
**Translation:** 

**[5136.10s] English:** moment. And then it's the ASML deep UV, what is that? Extreme ultraviolet lithography.  
**Translation:** Vocabulary: brouhaha: 轩然大波; ultraviolet: 紫外线

**[5143.40s] English:** To set context on the chips, right, what Nathan's referring to is in 2020,  
**Translation:** 

**[5147.12s] English:** Huawei released their Ascend 910 chip, which was an AI chip, first one on 7 nanometer before Google  
**Translation:** Vocabulary: ascend: 上升

**[5153.72s] English:** did, before NVIDIA did.  
**Translation:** 

**[5155.10s] English:** And they submitted it to the MLPerf benchmark, which is sort of a industry standard for machine  
**Translation:** Vocabulary: benchmark: 衡量标准

**[5160.00s] English:** learning performance benchmark um and and it did quite well and it was the best chip at the  
**Translation:** 

**[5164.58s] English:** submission right this was this was a huge deal um the trump admin of course banned um it was 2019  
**Translation:** Vocabulary: admin: 行政部门

**[5171.20s] English:** right banned the huawei from getting seven nanometer chips from tsmc and so then they had  
**Translation:** 

**[5176.06s] English:** to switch to move using internal domestically produced chips which was a multi-year setback  
**Translation:** Vocabulary: domestically: 国内

**[5180.04s] English:** many companies have done seven nanometer chips and the question is like we don't know how much  
**Translation:** 

**[5184.28s] English:** huawei was subsidizing production of that chip like intel has made seven nanometer chips that  
**Translation:** Vocabulary: subsidizing: 补贴生产

**[5189.30s] English:** are not profitable and things like this so this is how it all feeds back into the economic engine  
**Translation:** 

**[5194.68s] English:** of export controls well so you're saying that for now xi jinping has not felt the agi but it feels  
**Translation:** 

**[5201.66s] English:** like the deep seek moment yeah might like there might be meetings going on now where he's going  
**Translation:** 

**[5208.24s] English:** to start wearing the same t-shirt and things are going to escalate i mean like like this he may  
**Translation:** 

**[5213.88s] English:** have woken up last week right lian fang met the vice chairman vice the second command guy um  
**Translation:** 

**[5219.28s] English:** and they had a meeting and then the day the next day they announced the ai subsidies which are a  
**Translation:** Vocabulary: subsidies: 补助

**[5223.74s] English:** trillion rmb right so it's possible that this deep seek moment is truly the beginning of a cold war  
**Translation:** 

**[5229.76s] English:** that's what a lot of people are worried about people in ai have been worried that this is  
**Translation:** 

**[5234.54s] English:** going towards a cold war or already is but there's it's not deep seeks fault but there's something  
**Translation:** 

**[5239.10s] English:** a bunch of factors came together where history works explosion i mean it all has to do with  
**Translation:** 

**[5244.02s] English:** nvidia stock going down probably but it it's just some like mass  
**Translation:** 

**[5249.28s] English:** that happened that eventually led to xi jinping having meetings and waking up to this idea  
**Translation:** 

**[5254.56s] English:** and the u.s government realized in october 7th 2022 before chat gpt released that that restriction  
**Translation:** 

**[5261.38s] English:** october 7th which dropped and shocked everyone and it was very clearly aimed at ai everyone was like  
**Translation:** Vocabulary: restriction: 限制

**[5266.42s] English:** what the heck are you doing stable diffusion was out then but not yeah but not chad gp so it's like  
**Translation:** 

**[5271.66s] English:** starting to be rumblings like of what gen ai can do to society but it was very clear i think to at  
**Translation:** Vocabulary: diffusion: 扩散; rumblings: 不安

**[5277.46s] English:** least like national security council's  
**Translation:** 

**[5279.28s] English:** law and  
**Translation:** 

**[5280.00s] English:** And those sort of folks that this was where the world is headed, this Cold War that's happening.  
**Translation:** 

**[5285.10s] English:** So is there any concerns that the export controls push China to take military action on Taiwan?  
**Translation:** Vocabulary: taiwan: 台湾

**[5295.22s] English:** This is the big risk, right?  
**Translation:** 

**[5297.00s] English:** The further you push China away from having access to cutting edge American and global technologies, the more likely they are to say, well, because I can't access it, I might as well, like no one should access it, right?  
**Translation:** 

**[5308.44s] English:** And there's a few like interesting aspects of that, right?  
**Translation:** 

**[5311.64s] English:** Like, you know, China has a urban rural divide like no other.  
**Translation:** 

**[5316.74s] English:** They have a male female birth ratio like no other to the point where, you know, if you look in most of China, it's like the ratio is not that bad.  
**Translation:** 

**[5323.48s] English:** But when you look at single dudes in rural China, it's like a 30 to 1 ratio.  
**Translation:** 

**[5327.44s] English:** And those are disenfranchised dudes, right?  
**Translation:** 

**[5329.38s] English:** Like, quote unquote, like the U.S. has an incel problem like China does, too.  
**Translation:** Vocabulary: disenfranchised: 失去投票权

**[5333.66s] English:** It's just they're placated in some way or cut, crushed down.  
**Translation:** 

**[5336.32s] English:** What do you do with these people?  
**Translation:** Vocabulary: placated: 安抚

**[5337.72s] English:** And at the same time, you're not allowed to access the most important technology.  
**Translation:** 

**[5341.56s] English:** At least the U.S. thinks so.  
**Translation:** 

**[5342.90s] English:** China is maybe starting to think this is the most important technology by starting to dump subsidies in it, right?  
**Translation:** 

**[5347.30s] English:** They thought EVs and renewables were the most important technology.  
**Translation:** Vocabulary: renewables: 可再生能源; subsidies: 补贴

**[5349.88s] English:** They dominate that now, right?  
**Translation:** 

**[5351.34s] English:** Now they're starting to they started thinking about that about semiconductors in, you know, the late 2010s and early 2020s.  
**Translation:** Vocabulary: dominate: 占据主导; semiconductors: 半导体

**[5357.60s] English:** And now they've been dumping money and they're catching up rapidly.  
**Translation:** 

**[5360.88s] English:** And they're going to do the same with AI, right?  
**Translation:** 

**[5362.64s] English:** Because they're very talented, right?  
**Translation:** 

**[5364.20s] English:** So the question is, like, what?  
**Translation:** 

**[5367.72s] English:** When when does when when does when does this hit a breaking point?  
**Translation:** 

**[5371.02s] English:** Right. And if China sees this as, hey, they can continue if they if not having access and starting a true hot war, right, taking over Taiwan or trying to subvert its democracy in some way or blockading it hurts the rest of the world far more than it hurts them.  
**Translation:** Vocabulary: blockading: 封锁; subvert: 颠覆

**[5388.00s] English:** This is something they could potentially do.  
**Translation:** 

**[5389.90s] English:** Right. And and so is this pushing them towards that potentially?  
**Translation:** 

**[5393.84s] English:** Right. I'm not quite a geopolitical person, but, you know, it's.  
**Translation:** 

**[5397.72s] English:** It's obvious that the world regime of.  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[5400.00s] English:** peace and like trade is like super awesome for economics uh but but at some point it could break  
**Translation:** 

**[5406.58s] English:** right i think we should comment that the like why chinese economy would be hurt by that is that  
**Translation:** 

**[5410.90s] English:** they're export heavy i think the united states buys so much like if that goes away like that's  
**Translation:** 

**[5415.86s] English:** how their economy well also also they just like would not be able to import raw materials from  
**Translation:** 

**[5420.22s] English:** like all over the world right the u.s would just shut down the trade in malacca and like you know  
**Translation:** 

**[5424.62s] English:** at the same time the u.s entire like you could argue almost all the gdp growth in america since  
**Translation:** 

**[5429.88s] English:** you know the 70s has been either population growth or tech right um because you know your  
**Translation:** 

**[5437.08s] English:** your life today is not that much better than someone from the 80s outside of tech right you  
**Translation:** 

**[5441.68s] English:** still you know you know cars they all have semiconductors in them everywhere fridges  
**Translation:** 

**[5445.36s] English:** semiconductors everywhere there's these funny stories about how russians were taking apart  
**Translation:** 

**[5448.90s] English:** laundry machines because they had certain like texas instrument chips that they could then  
**Translation:** 

**[5452.78s] English:** repurpose and put into like their  
**Translation:** Vocabulary: repurpose: 重新利用

**[5454.60s] English:** their anti-missile missile things right like their s400 or whatever you would know more about  
**Translation:** 

**[5459.88s] English:** this but uh there's all sorts of like everything about semiconductors is so integral to every part  
**Translation:** Vocabulary: integral: 必不可少的

**[5465.16s] English:** of our lives so can you explain the role of tsmc in the story of semiconductors and  
**Translation:** 

**[5471.54s] English:** maybe also how the united states can break the reliance on tsmc i don't think it's necessarily  
**Translation:** 

**[5478.56s] English:** breaking the reliance i think it's uh getting tsmc to you know build in the u.s um but so  
**Translation:** 

**[5484.50s] English:** so  
**Translation:** 

**[5484.58s] English:** so taking a step back right tsmc produces most of the world's chips right especially on the  
**Translation:** 

**[5491.38s] English:** foundry side um you know there's a lot of companies that build their own chips uh samsung intel um you  
**Translation:** Vocabulary: foundry: 晶圆厂

**[5497.88s] English:** know st micro texas instruments you know analog devices all these kinds of companies build their  
**Translation:** 

**[5502.80s] English:** own chips and xp but more and more of these companies are outsourcing to tsmc and have been  
**Translation:** Vocabulary: analog: 模拟; outsourcing: 外包

**[5508.08s] English:** for multiple decades can you explain the the supply chain there and where most of tsmc is  
**Translation:** 

**[5513.50s] English:** in terms of manufacturing  
**Translation:** 

**[5514.48s] English:** sure so historically supply chain was companies would build their own chips they would you know  
**Translation:** 

**[5519.86s] English:** be  
**Translation:** Vocabulary: historically: 历史上

**[5520.00s] English:** company started, they'd build their own chips, and then they'd design the chip and build the  
**Translation:** 

**[5524.40s] English:** ship and sell it. Over time, this became really difficult because the cost of building a fab  
**Translation:** 

**[5529.84s] English:** continues to compound every single generation. Of course, figuring out the technology for it  
**Translation:** 

**[5534.26s] English:** is incredibly difficult regardless, but just the dollars and cents that are required,  
**Translation:** 

**[5538.90s] English:** ignoring, saying, hey, yes, I have all the technical capability, which it's really hard  
**Translation:** 

**[5542.40s] English:** to get that by the way, right? Intel's failing, Samsung's failing, et cetera.  
**Translation:** Vocabulary: capability: 能力

**[5544.92s] English:** But if you look at just the dollars to spend to build that next generation fab,  
**Translation:** 

**[5550.02s] English:** it keeps growing, right? More's law is halving the cost of chips every two years.  
**Translation:** 

**[5554.22s] English:** There's a separate law that's doubling the cost of fabs every handful of years.  
**Translation:** 

**[5558.18s] English:** And so you look at a leading edge fab that is going to be profitable today that's building  
**Translation:** Vocabulary: profitable: 有利可图的

**[5562.42s] English:** three nanometer chips or two nanometer chips in the future, that's going to cost north of $30,  
**Translation:** 

**[5567.14s] English:** $40 billion, right? And that's just for a token amount. That's like the base building block,  
**Translation:** Vocabulary: nanometer: 纳米; token: 象征性

**[5572.62s] English:** you probably need to build multiple, right? And so,  
**Translation:** 

**[5574.92s] English:** when you look at the industry over the last, if I go back 20, 30 years ago,  
**Translation:** 

**[5579.70s] English:** there were 20, 30 companies that could build the most advanced chips, and then they would design  
**Translation:** 

**[5583.58s] English:** them themselves and sell them, right? So companies like AMD would build their own chips. Intel,  
**Translation:** 

**[5587.80s] English:** of course, still builds their own chips, they're very famous for it, but IBM would build their  
**Translation:** 

**[5590.18s] English:** own chips. And you could keep going down the list, all these companies built their own chips.  
**Translation:** 

**[5594.60s] English:** Slowly, they kept falling like flies, and that's because of what TSMC did, right?  
**Translation:** 

**[5598.92s] English:** They created the foundry business model, which is, I'm not going to design any chips.  
**Translation:** 

**[5602.70s] English:** I'm just going to contract manufacturer chips,  
**Translation:** 

**[5604.92s] English:** or else other people. And one of their early customers is NVIDIA, right? NVIDIA  
**Translation:** 

**[5609.12s] English:** is the only semiconductor company that's worth, that's doing more than a billion dollars of  
**Translation:** 

**[5615.30s] English:** revenue, that was started in the era of foundry, right? Every other company started before then,  
**Translation:** Vocabulary: foundry: 代工工厂; semiconductor: 半导体

**[5620.48s] English:** and at some point had fabs, which is actually incredible, right? Like AMD, and Intel,  
**Translation:** 

**[5625.88s] English:** and Broadcom. It's like everyone had fabs at some point, or some companies like Broadcom,  
**Translation:** Vocabulary: broadcom: 博通

**[5631.80s] English:** it was like a merger, amalgamation of various companies that rolled up.  
**Translation:** 

**[5634.92s] English:** But even today, Broadcom has fabs, right? They build iPhone RF radio chips, sort of  
**Translation:** Vocabulary: amalgamation: 合并

**[5640.00s] English:** in colorado for for you know for apple right like there's there all these companies had fabs and for  
**Translation:** 

**[5645.30s] English:** most of the fabs they threw them away or sold them off or they got rolled into something else  
**Translation:** 

**[5648.94s] English:** and now everyone relies on tsmc right including intel their latest pc chip uses tsmc chips right  
**Translation:** 

**[5656.04s] English:** it also uses some intel chips but it uses tsmc process can you explain why the foundry model is  
**Translation:** 

**[5660.90s] English:** so successful for these companies why why are they going with economies of scale scale yeah so i mean  
**Translation:** 

**[5667.36s] English:** like like i mentioned right the cost of building a fab is so high the rnd is so difficult um and  
**Translation:** 

**[5672.86s] English:** uh when you look at like these like companies that had their own vertical stack there was an  
**Translation:** 

**[5677.50s] English:** antiquated process of like okay like i'm so hyper customized to each specific chip right but as we've  
**Translation:** Vocabulary: antiquated: 过时的; hyper: 过度的; vertical: 垂直的

**[5683.14s] English:** gone through the history of sort of like the last 50 years of of electronics and semiconductors  
**Translation:** 

**[5687.12s] English:** a you need more and more specialization right because moore's law has died um denard scaling  
**Translation:** Vocabulary: semiconductors: 半导体

**[5692.08s] English:** has died i.e chips are not getting better just for free right you know from manufacturing you have to  
**Translation:** 

**[5697.00s] English:** make  
**Translation:** 

**[5697.20s] English:** real architectural innovations right google is not just running on intel cpus for web serving  
**Translation:** 

**[5701.84s] English:** they have a youtube chip they have tpus they have pixel chips they have a wide diversity of chips  
**Translation:** Vocabulary: architectural: 建筑风格; innovations: 创新; pixel: 像素

**[5706.70s] English:** that uh you know generate all the economic value of google right running right you know it's running  
**Translation:** 

**[5711.50s] English:** all the services and stuff and so and this is just google and you could go across any company  
**Translation:** 

**[5715.02s] English:** in the industry and it's like this right cars contain 5 000 chips you know 200 different  
**Translation:** 

**[5720.00s] English:** varieties of them right all these random things a tesla door handle has two chips right like it's  
**Translation:** 

**[5723.96s] English:** like ridiculous um and it's a cool door handle right it's like you know you don't think it's  
**Translation:** 

**[5726.84s] English:** you don't think about it but it's like has two really chipped like like penny like chips in there  
**Translation:** 

**[5731.10s] English:** right anyway so so as you have more diversity of chips as you have more specialization required  
**Translation:** 

**[5736.06s] English:** and the cost of fabs continues to grow you need someone who is laser focused on building the best  
**Translation:** 

**[5741.90s] English:** process technology and making it as flexible as possible i think you could say it's simple  
**Translation:** 

**[5746.70s] English:** which is the cost for fab goes up and if you are a small player that makes a few types of chips  
**Translation:** 

**[5752.78s] English:** you're not going to have the demand to pay back the cost of the fab  
**Translation:** 

**[5756.84s] English:** NVIDIA can have many different customers.  
**Translation:** 

**[5760.00s] English:** create all this demand into one place and then they're the only person that makes enough money  
**Translation:** 

**[5764.46s] English:** building chips to buy the next to build the next fab so this is kind of why they the company slowly  
**Translation:** 

**[5770.66s] English:** get killed because they have the they have 10 years ago a chip that is profitable and is good  
**Translation:** 

**[5776.24s] English:** enough but the cost to build the next one goes up they may try to do this fail because they don't  
**Translation:** Vocabulary: profitable: 有利可图的

**[5781.04s] English:** have the money to make it work and then they don't have any chips or they build it and it's too  
**Translation:** 

**[5784.28s] English:** expensive and they just have or they run you know there's more failure points right you know you  
**Translation:** 

**[5788.88s] English:** could have one little process related to like some sort of like uh chemical etch or some sort of  
**Translation:** 

**[5794.06s] English:** like plasma etch or you know some little process that screws up you didn't engineer it right and  
**Translation:** Vocabulary: plasma: 等离子蚀刻

**[5799.10s] English:** now the whole company falls apart you can't make chips right and so super super powerful companies  
**Translation:** 

**[5803.42s] English:** like intel they had like the weathering storm to like hey they still exist today even though  
**Translation:** 

**[5807.76s] English:** they really screwed up their manufacturing six seven years ago but in the case of like amd  
**Translation:** 

**[5811.90s] English:** they almost went bankrupt they had to sell their fabs to mubadala uh uae right um and and like that  
**Translation:** Vocabulary: bankrupt: 破产; mubadala: 穆巴达拉

**[5818.36s] English:** became a separate industry and they had to sell their fabs to mubadala uh uae right um and and like that became a separate  
**Translation:** 

**[5818.86s] English:** company called global foundries which is a foundry firm um and and then amd was able to then  
**Translation:** Vocabulary: foundries: 晶圆厂; foundry: 代工厂

**[5823.24s] English:** focus on like on the return back up was like hey let's focus on making chiplets and a bunch of  
**Translation:** 

**[5828.04s] English:** different chips for different markets um and focusing on specific workloads rather than you  
**Translation:** Vocabulary: chiplets: 小芯片; workloads: 工作负载

**[5832.66s] English:** know all of the these different things and so you get more diversity of chips you have more companies  
**Translation:** 

**[5836.70s] English:** than ever designing chips but you have fewer companies than ever manufacturing them right and  
**Translation:** 

**[5841.66s] English:** this is this is where tsmc comes in is they've they've just been the best right they are so good  
**Translation:** 

**[5847.06s] English:** at it right they're customer focused  
**Translation:** 

**[5848.86s] English:** they make it easy for you to fabricate your chips they take all of that complexity and like  
**Translation:** 

**[5852.64s] English:** kind of try and abstract a lot of it away from you um they make good money they don't make insane  
**Translation:** Vocabulary: complexity: 复杂性; fabricate: 伪造

**[5856.94s] English:** money but they make good money um and and they're able to aggregate all this demand and continue to  
**Translation:** 

**[5862.26s] English:** build the next fab the next fab the next fab so why is taiwan so special for tsmc why is it  
**Translation:** Vocabulary: aggregate: 聚合; taiwan: 台湾

**[5867.38s] English:** happening there can it be replicated inside the united states yeah so there's there's aspects of  
**Translation:** 

**[5873.12s] English:** it that i would say yes and aspects that i'd say no right um tsmc is way ahead because it's  
**Translation:** 

**[5878.86s] English:** uh for  
**Translation:** 

**[5880.00s] English:** former, you know, executive Morris Chang of Texas Instruments, wasn't promoted to CEO. And he's like,  
**Translation:** Vocabulary: chang: 前董事长

**[5885.36s] English:** screw this, I'm gonna go make a my own chip company, right. And he went to Taiwan and made  
**Translation:** 

**[5888.72s] English:** TSMC, right. And there's, there's a whole lot more story there. So he could have been Texas  
**Translation:** Vocabulary: texas: 得州

**[5892.98s] English:** Instruments could have been the, you know, could have been TSMC, but Texas semiconductor  
**Translation:** 

**[5896.52s] English:** manufacturing, right, instead of, you know, Texas Instruments, right. But, but, you know,  
**Translation:** 

**[5900.24s] English:** so there is that whole story there, sitting here in Texas. I mean, and that sounds like a human  
**Translation:** 

**[5904.84s] English:** story, like it didn't get promoted, just the brilliance of Morris Chang, you know, which I  
**Translation:** Vocabulary: brilliance: 卓越智慧

**[5908.82s] English:** wouldn't underplay. But there's also like a different level of like, how, how this works,  
**Translation:** 

**[5913.54s] English:** right. So in Taiwan, the, you know, like the number top percent of graduates of students that  
**Translation:** Vocabulary: underplay: 低估

**[5921.30s] English:** go to the best school, which is NTU, the top percent of those all go work to TSMC, right.  
**Translation:** 

**[5925.80s] English:** And guess what their pay is, their starting pay is like $80,000, $70,000, right, which is like,  
**Translation:** 

**[5931.94s] English:** that's like starting pay for like a good graduate in the US, right? Not the top,  
**Translation:** 

**[5935.34s] English:** the top graduates are making hundreds of thousands of dollars at the Google,  
**Translation:** 

**[5938.82s] English:** and the Amazons, and now I guess the open AIs of the world, right. So there is, there is a large  
**Translation:** 

**[5944.22s] English:** dichotomy of like, what is the top 1% of the society doing? And where are they headed because  
**Translation:** Vocabulary: amazons: 女战士; dichotomy: 对立面

**[5948.38s] English:** of economic reasons, right? Intel never paid that crazy good, right? And it didn't make sense to  
**Translation:** 

**[5952.98s] English:** them, right? That's, that's one aspect, right? Where's the best going? Second is the work ethic,  
**Translation:** 

**[5957.14s] English:** right? Like, you know, we like to work, you know, you work a lot, we work a lot. But at the end of  
**Translation:** 

**[5962.16s] English:** the day, when there's a, you know, when, when, what is the time and amount of work that you're  
**Translation:** 

**[5967.20s] English:** doing? And what does a fab require, right?  
**Translation:** 

**[5969.08s] English:** Fabs are not work from home jobs, they are you go into the fab and grueling work, right?  
**Translation:** Vocabulary: grueling: 艰苦的

**[5974.10s] English:** There's, there's, hey, if there is any amount of vibration, right, an earthquake happens,  
**Translation:** 

**[5979.62s] English:** vibrates the machines, they're all, you know, they're either broken, you've, you've scrapped  
**Translation:** Vocabulary: scrapped: 报废; vibrates: 震动; vibration: 振动

**[5983.72s] English:** some of your production. And then in many cases, they're like not calibrated properly. So, so when  
**Translation:** 

**[5988.22s] English:** TSMC, when there's an earthquake, right, recently, there's been an earthquake, TSMC doesn't call  
**Translation:** Vocabulary: calibrated: 校准正确

**[5992.50s] English:** their employees, they just, they just go to the fab. And like, they just show up the parking lot  
**Translation:** 

**[5997.28s] English:** gets slammed, and people just go into the fab and  
**Translation:** 

**[6000.00s] English:** fix it right like it's like an arm it's like ants right like it's like you know a hive of ants  
**Translation:** 

**[6004.06s] English:** doesn't get told by the queen what to do the ants just know it's like one person just specializes  
**Translation:** 

**[6010.06s] English:** on these one task and it's like you're going to take this one tool and you're the best person in  
**Translation:** 

**[6014.04s] English:** the world and this is what you're going to do for your whole life is this one task in the fab which  
**Translation:** 

**[6017.36s] English:** is like some special chemistry plus nano manufacturing on one line of tools that  
**Translation:** 

**[6021.94s] English:** continues to get iterated and yeah it's just like it's like specific plasma edge for removing  
**Translation:** Vocabulary: plasma: 等离子体

**[6026.90s] English:** silicon dioxide right that's all you focus on your whole career and it's like such a specialized  
**Translation:** 

**[6030.88s] English:** thing and and so it's not like the task are transferable ai today is awesome because like  
**Translation:** 

**[6035.72s] English:** people can pick it up like that uh semiconductor manufacturing is is very antiquated and difficult  
**Translation:** 

**[6040.68s] English:** none of the materials are online for people to read easily and learn right the papers are very  
**Translation:** Vocabulary: antiquated: 过时的; semiconductor: 半导体

**[6045.62s] English:** dense and like it takes it takes a lot of experience to learn and so it makes the barrier  
**Translation:** 

**[6050.60s] English:** to entry much higher too so so when you talk about hey you have all these people that are  
**Translation:** 

**[6054.98s] English:** super specialized they will work  
**Translation:** 

**[6056.90s] English:** you know 80 hours a week in a factory right in a fab uh and if anything goes wrong they'll go  
**Translation:** 

**[6063.06s] English:** show up in the middle of the night because some earthquake their wife was like there was an  
**Translation:** 

**[6066.30s] English:** earthquake he's like great i'm gonna go to the fab it's like would you would you like as an  
**Translation:** 

**[6071.08s] English:** american do that right it's like these sorts of things are like what you know i guess are the  
**Translation:** 

**[6075.08s] English:** exemplifying like why tsmc is so amazing now can you replicate it in the u.s uh let's not ignore  
**Translation:** Vocabulary: exemplifying: 举例子

**[6080.74s] English:** intel was the leader in manufacturing for over 20 years they brought every technology to market  
**Translation:** 

**[6086.28s] English:** first  
**Translation:** 

**[6086.90s] English:** besides euv strained silicon high k metal gates finfet um you know the list goes on and on and on  
**Translation:** 

**[6093.14s] English:** of technologies that intel brought to market first made the most money from um and and and  
**Translation:** Vocabulary: strained: 拉伸

**[6098.50s] English:** manufactured at scale first best highest profit margins right so we shouldn't ignore that intel  
**Translation:** 

**[6104.14s] English:** can't do this right it's that the culture uh has broken right um you've invested in the wrong  
**Translation:** 

**[6109.74s] English:** things they said no to the iphone they they had all these different things regarding like you  
**Translation:** 

**[6114.26s] English:** know mismanagement of the fabs mismanagement of designs  
**Translation:** Vocabulary: mismanagement: 管理不善

**[6116.90s] English:** this lock-up right and at the same time old  
**Translation:** 

**[6120.00s] English:** these brilliant people right these like 50 000 phds uh you know or masters that have been working  
**Translation:** 

**[6125.00s] English:** on specific chemical or physical processes or nano manufacturing processes for decades in oregon  
**Translation:** 

**[6130.80s] English:** they're still there they're still producing amazing work it's just like getting it to the  
**Translation:** 

**[6134.20s] English:** last mile of production at high yield where you can design where you can manufacture dozens and  
**Translation:** 

**[6138.96s] English:** hundreds of different kinds of chips you know and and it's good customer experience has broken right  
**Translation:** Vocabulary: manufacture: 生产

**[6144.18s] English:** you know it's that customer experience it's like the like part of it is like people will say intel  
**Translation:** 

**[6147.94s] English:** is too pompous in the 2000s 2010s right they just thought they were better than everyone the tool  
**Translation:** Vocabulary: pompous: 自大的

**[6152.24s] English:** guys were like oh i don't think that this is mature enough they're like you just don't know  
**Translation:** 

**[6155.48s] English:** we know right this sort of stuff would happen um and so can the u.s bring it to the uh can the u.s  
**Translation:** 

**[6161.90s] English:** bring leading-edge semiconductor manufacturing to the u.s emphatically yes right and we are right  
**Translation:** 

**[6166.28s] English:** it's happening like arizona is getting better and better as time goes on tsmc has built you know  
**Translation:** Vocabulary: emphatically: 坚定地; semiconductor: 半导体

**[6172.06s] English:** roughly 20 percent of their capacity for five nanometer in the u.s right um now this is nowhere  
**Translation:** 

**[6177.92s] English:** near enough right uh you know 20 of capacity in the u.s is like nothing right um and furthermore  
**Translation:** 

**[6183.60s] English:** this is still dependent on taiwan existing right all there's sort of important way to separate it  
**Translation:** 

**[6188.16s] English:** out there's rnd and there's high volume manufacturing there are there effectively  
**Translation:** Vocabulary: taiwan: 台湾

**[6193.18s] English:** there are three places in the world that are doing leading edge rnd there's since you taiwan  
**Translation:** 

**[6198.32s] English:** there's hillsborough oregon and there is pyong uh pyong pyong yang uh south korea right these  
**Translation:** 

**[6204.52s] English:** three places are doing the leading edge rnd for the rest of the world's  
**Translation:** 

**[6207.92s] English:** leading edge semiconductors right um now manufacturing can be distributed more globally  
**Translation:** Vocabulary: globally: 全球范围内; semiconductors: 半导体

**[6213.44s] English:** right um and this is sort of where this dichotomy exists of like who's actually modifying the  
**Translation:** 

**[6219.68s] English:** process who's actually developing the next generation one who's improving them is since  
**Translation:** Vocabulary: dichotomy: 对立面; modifying: 修改

**[6224.40s] English:** you is hillsborough is pyongyang right it is not the rest of these uh you know fabs like arizona  
**Translation:** 

**[6230.14s] English:** right arizona is a paperweight if if since you disappeared off the face of the planet um you  
**Translation:** Vocabulary: arizona: 典范; paperweight: 废纸夹; pyongyang: 平壤

**[6235.16s] English:** know within within a year a couple years  
**Translation:** 

**[6237.92s] English:** arizona would stop producing too right  
**Translation:** 

**[6240.00s] English:** It's actually pretty critical.  
**Translation:** 

**[6241.92s] English:** One of the things I like to say is if I had a few missiles, I know exactly where I could  
**Translation:** Vocabulary: missiles: 导弹

**[6246.06s] English:** cause the most economic damage, right?  
**Translation:** 

**[6247.52s] English:** It's not targeting the White House, right?  
**Translation:** 

**[6248.96s] English:** It's the R&D centers.  
**Translation:** 

**[6250.22s] English:** It's the R&D centers for TSMC, Intel, Samsung, and then some of the memory guys, Micron and  
**Translation:** Vocabulary: micron: 微米

**[6254.68s] English:** Hynix.  
**Translation:** 

**[6255.08s] English:** Because they define the future evolution of these semiconductors and everything's moving  
**Translation:** 

**[6258.46s] English:** so rapidly that it really is fundamentally about R&D.  
**Translation:** 

**[6263.86s] English:** And it is all about TSMC, huh?  
**Translation:** Vocabulary: fundamentally: 从根本上

**[6267.18s] English:** And so TSMC, you cannot purchase a vehicle without TSMC chips, right?  
**Translation:** 

**[6272.74s] English:** You cannot purchase a fridge without TSMC chips.  
**Translation:** Vocabulary: cannot: 不能

**[6275.76s] English:** I think one of the few things you can purchase, ironically, is a Texas Instruments graphing  
**Translation:** 

**[6282.58s] English:** calculator, right?  
**Translation:** Vocabulary: graphing: 图形绘制; ironically: 讽刺的是

**[6283.46s] English:** Because they actually manufacture in Texas.  
**Translation:** 

**[6284.88s] English:** But outside of that, a laptop, a phone, servers, GPUs, none of this stuff can exist.  
**Translation:** Vocabulary: manufacture: 生产; texas: 得克萨斯

**[6291.06s] English:** And this is without TSMC.  
**Translation:** 

**[6292.84s] English:** And in many cases, it's not even like the leading edge, you know, sexy five nanometer  
**Translation:** Vocabulary: nanometer: 纳米

**[6296.12s] English:** chip, three nanometer chip.  
**Translation:** 

**[6297.18s] English:** Two nanometer chip.  
**Translation:** 

**[6298.10s] English:** Oftentimes, it's just like some stupid power IC that's like converting from like, you know,  
**Translation:** 

**[6302.60s] English:** some voltage to another, right?  
**Translation:** Vocabulary: converting: 转换; oftentimes: 经常; voltage: 电压

**[6303.74s] English:** And it's made at TSMC, right?  
**Translation:** 

**[6304.76s] English:** This is what China is investing in as well.  
**Translation:** 

**[6306.54s] English:** It's like they can build out this long tail fab where the techniques are much more known.  
**Translation:** 

**[6310.36s] English:** You don't have to figure out these problems with EUV.  
**Translation:** 

**[6312.62s] English:** They're investing in this.  
**Translation:** 

**[6314.10s] English:** And then they have large supply for things like the car door handles and the random stuff.  
**Translation:** 

**[6320.08s] English:** And that trickles down into this whole economic discussion as well, which is they have far  
**Translation:** 

**[6325.72s] English:** more than we do.  
**Translation:** Vocabulary: trickles: 渗透

**[6326.40s] English:** And having supply for things like this is crucial to normal life.  
**Translation:** 

**[6329.46s] English:** So they're starting to invest in high volume manufacturer, but they're not doing R&D.  
**Translation:** 

**[6334.90s] English:** So they do R&D on their own.  
**Translation:** 

**[6336.62s] English:** They're just way behind, right?  
**Translation:** 

**[6337.94s] English:** So I would say like in 2015, China had a five-year plan where they defined by 2025 and 2020 certain  
**Translation:** 

**[6346.50s] English:** goals, including like 80% domestic production of semiconductors.  
**Translation:** Vocabulary: semiconductors: 半导体

**[6350.14s] English:** They're not going to hit that, right?  
**Translation:** 

**[6351.62s] English:** To be clear.  
**Translation:** 

**[6352.36s] English:** But they are in certain areas really, really close, right?  
**Translation:** 

**[6355.42s] English:** Like BYD.  
**Translation:** 

**[6356.40s] English:** BYD is probably going to be the first company in the world to not have to.  
**Translation:** 

**[6360.00s] English:** use tsmc for making because they have their own fabs right uh for making chips now they still  
**Translation:** 

**[6365.02s] English:** have to buy some chips from foreign uh for example like around like self-driving adas capabilities  
**Translation:** 

**[6370.62s] English:** because those are really high end but at least like you know like an internal combustion engine  
**Translation:** 

**[6374.86s] English:** has 40 chips and an ev you know just just for like controlling like flow rates and all these  
**Translation:** 

**[6378.66s] English:** things and evs are even more complicated so all these different power ics and battery management  
**Translation:** 

**[6383.16s] English:** controllers and all these things they're they're insourcing right um and this is this is something  
**Translation:** 

**[6388.12s] English:** that like china has been doing since 2015 now as far as like the trailing edge they're getting so  
**Translation:** Vocabulary: insourcing: 内部采购; trailing: 落后

**[6393.66s] English:** much capacity there as far as the leading edge right ie this five nanometer and so on so forth  
**Translation:** 

**[6398.62s] English:** right where gpus they are still behind and this is the u.s restrictions are trying to stop them  
**Translation:** 

**[6404.18s] English:** in the ladder but you know all that's happened you know is yes they've slowed down their five  
**Translation:** 

**[6408.50s] English:** nanometer three nanometer etc but they've accelerated their hey 45 nanometer 90 nanometer  
**Translation:** Vocabulary: accelerated: 加快

**[6413.94s] English:** power ic or analog ic or you know random chip in my keyboard right  
**Translation:** 

**[6418.12s] English:** that kind of stuff so so there is an angle of like the u.s's actions have been so from these  
**Translation:** Vocabulary: analog: 模拟芯片

**[6424.02s] English:** export you know from the angle of the expert controls have been so inflammatory at slowing  
**Translation:** 

**[6429.28s] English:** down china's progress on the leading edge that they've turned around and have accelerated their  
**Translation:** Vocabulary: inflammatory: 激进的

**[6433.72s] English:** progress elsewhere because they know that this is so important right if the u.s is going to lock  
**Translation:** 

**[6437.56s] English:** them out here or if they lock us out here as well uh in the trailing edge and so going back can the  
**Translation:** 

**[6442.08s] English:** u.s build it here um yes but it's going to take a ton of money i truly think like to  
**Translation:** 

**[6448.12s] English:** to revolutionize and completely in-source semiconductors would take a decade and a  
**Translation:** Vocabulary: revolutionize: 彻底改变

**[6452.28s] English:** trillion dollars is some of it also culture like you said extreme competence extreme work ethic  
**Translation:** 

**[6457.80s] English:** in taiwan i think if you have the demand and the money is on the line the american companies figure  
**Translation:** Vocabulary: competence: 卓越能力; trillion: 万亿

**[6462.80s] English:** it out it's going to take handholding with the government but i i think that the culture helps  
**Translation:** 

**[6467.14s] English:** tsmc breakthrough and it's easier for them you get tsmc has some like 90 000 employees right  
**Translation:** Vocabulary: handholding: 扶持

**[6472.52s] English:** it's not actually that insane amount um the arizona fab has 3 000 from taiwan  
**Translation:** 

**[6478.12s] English:** and and these people like their wives were like  
**Translation:** Vocabulary: arizona: 亚利桑那; taiwan: 台湾

**[6480.00s] English:** Like, yeah, we're not going to have kids unless you sign up for the Arizona fab.  
**Translation:** 

**[6483.18s] English:** We go to Arizona and we have our kids there.  
**Translation:** 

**[6484.82s] English:** There's also a Japan fab where the same thing happened, right?  
**Translation:** 

**[6486.94s] English:** And so these wives drove these dudes to go to Japan or America to have the kids there.  
**Translation:** 

**[6493.10s] English:** And it's an element of culture.  
**Translation:** 

**[6494.64s] English:** Yeah, sure.  
**Translation:** 

**[6495.42s] English:** Taiwan works that hard.  
**Translation:** 

**[6496.68s] English:** But also the US has done it in the past.  
**Translation:** 

**[6498.90s] English:** They could do it now, right?  
**Translation:** 

**[6500.78s] English:** We can just import, I say import, the best people in the world if we want to.  
**Translation:** 

**[6505.50s] English:** That's where the immigration conversation is a tricky one.  
**Translation:** 

**[6508.54s] English:** And there's been a lot of debate over that.  
**Translation:** 

**[6509.78s] English:** But yeah, it seems absurdly controversial to import the best people in the world.  
**Translation:** 

**[6514.46s] English:** I don't understand why it's controversial.  
**Translation:** Vocabulary: absurdly: 荒谬地

**[6516.24s] English:** That's one of the ways of winning.  
**Translation:** 

**[6518.24s] English:** I'm sure we agree with you.  
**Translation:** 

**[6519.58s] English:** And even if you can't import those people, I still think you could do a lot to manufacture  
**Translation:** 

**[6523.78s] English:** most of them in the US if the money's there, right?  
**Translation:** Vocabulary: manufacture: 生产

**[6526.38s] English:** And so it's just way more expensive.  
**Translation:** 

**[6528.02s] English:** It's not profitable for a long time.  
**Translation:** Vocabulary: profitable: 有利可图

**[6529.82s] English:** And that's the context of the CHIPS Act is only like $50 billion relative to some of  
**Translation:** 

**[6535.14s] English:** the renewable initiatives that were passed in the Inflation Reduction Act and the infrastructure  
**Translation:** Vocabulary: initiatives: 政策措施

**[6539.76s] English:** Act.  
**Translation:** 

**[6539.78s] English:** Which total in the hundreds of billions of dollars, right?  
**Translation:** 

**[6543.06s] English:** And so the amount of money that the US is spending on the semiconductor industry is  
**Translation:** 

**[6546.66s] English:** nothing, right?  
**Translation:** 

**[6548.20s] English:** Whereas all these other countries have structural advantages in terms of work ethic and amount  
**Translation:** 

**[6553.28s] English:** of work and things like that, but also a number of STEM graduates, the percentile of their  
**Translation:** Vocabulary: percentile: 百分位

**[6557.96s] English:** best going to that, right?  
**Translation:** 

**[6559.78s] English:** But they also have differences in terms of like, hey, there's just tax benefits in the  
**Translation:** 

**[6565.30s] English:** law and have been in the law for 20 years, right?  
**Translation:** 

**[6567.42s] English:** And then some countries have massive.  
**Translation:** 

**[6569.70s] English:** Subsidies, right?  
**Translation:** 

**[6570.72s] English:** China has something like $200 billion of semiconductor subsidies a year.  
**Translation:** Vocabulary: semiconductor: 半导体; subsidies: 补贴

**[6575.36s] English:** We're talking about $50 billion in the US over like six, right?  
**Translation:** 

**[6578.78s] English:** So the girth or difference in like the subsidy amounts is also huge, right?  
**Translation:** Vocabulary: girth: 差距

**[6583.68s] English:** And so I think, you know, Trump has been talking about tariffing Taiwan recently.  
**Translation:** 

**[6588.76s] English:** You know, that's sort of like one of these things that's like, oh, okay, well, like,  
**Translation:** Vocabulary: tariffing: 加征关税

**[6592.82s] English:** you know, maybe he doesn't want to subsidize the semiconductor industry.  
**Translation:** 

**[6596.02s] English:** Obviously, tariffing Taiwan is going to cost a lot of things to go get much more expensive.  
**Translation:** Vocabulary: subsidize: 补贴

**[6599.68s] English:** And so.  
**Translation:** 

**[6600.00s] English:** but does it change the equation for tsmc building more fabs in the u.s that's what he's sort of  
**Translation:** Vocabulary: equation: 方程式

**[6604.00s] English:** positing right so can you lay out the so we laid out the importance by the way it's incredible how  
**Translation:** 

**[6610.76s] English:** much you know about so much we told you dylan knows all this stuff yeah so okay you laid out  
**Translation:** 

**[6618.72s] English:** why tsmc is really important if we look out into the future 10 20 years out u.s china relationship  
**Translation:** 

**[6627.28s] English:** seems like it can go to a dark place of cold war escalated cold war even hot war  
**Translation:** Vocabulary: escalated: 升级

**[6636.50s] English:** or to a good place of uh anything from frenemies to cooperation to working together so in this game  
**Translation:** 

**[6646.54s] English:** theory complicated game uh what are the different trajectories what should u.s be doing like what  
**Translation:** Vocabulary: frenemies: 敌友关系; trajectories: 发展路径

**[6653.30s] English:** do you see as the different possible trajectories of u.s china relations as uh  
**Translation:** 

**[6657.28s] English:** both leaders start to feel the agi more and more and see the importance of chips and the importance  
**Translation:** 

**[6663.08s] English:** of ai i mean ultimately the export controls are pointing towards a separate future economy i think  
**Translation:** 

**[6670.40s] English:** the u.s has made it clear to chinese leaders that we intend to control this technology at whatever  
**Translation:** 

**[6678.02s] English:** cost to global economic inter like integration so that it's hard to unwind that like the the  
**Translation:** 

**[6685.80s] English:** card has been played  
**Translation:** Vocabulary: inter: 国际间

**[6687.28s] English:** at some point you know there was there was a convergence right uh but but over at least the  
**Translation:** 

**[6697.94s] English:** last decade it's been branching further and further out right like u.s companies can't enter  
**Translation:** Vocabulary: convergence: 交汇

**[6702.04s] English:** china chinese companies can't enter the u.s the u.s is saying hey china you can't get access to  
**Translation:** 

**[6708.04s] English:** our technologies in certain areas and china's rebuttaling with the same thing around like you  
**Translation:** Vocabulary: rebuttaling: 反驳

**[6713.22s] English:** know they've done some sort of specific materials and you know gallium and things like that and  
**Translation:** 

**[6717.28s] English:** that they've tried to limit the u.s on um one of the  
**Translation:** 

**[6720.00s] English:** There's a U.S. drone company that's not allowed to buy batteries, and they have, like, military customers.  
**Translation:** 

**[6724.22s] English:** And this drone company just tells the military customers, like, hey, just get it from Amazon because I can't actually physically get them, right?  
**Translation:** Vocabulary: drone: 无人驾驶飞机

**[6730.04s] English:** Like, there's all these things that are happening that point to further and further divergence.  
**Translation:** 

**[6734.04s] English:** I have zero idea, and I would love if we could all hold hands and sing Kumbaya, but, like, I have zero idea how that could possibly happen.  
**Translation:** Vocabulary: divergence: 分歧

**[6740.86s] English:** Is the divergence good or bad for avoiding war?  
**Translation:** 

**[6745.28s] English:** Is it possible that the divergence in terms of manufacturer chips, of training AI systems is actually good for avoiding military conflict?  
**Translation:** 

**[6755.34s] English:** It's an objective fact that the world has been the most peaceful it has ever been when there are global hegemons, right, or regional hegemons, right, in historical context, right?  
**Translation:** 

**[6765.24s] English:** The Mediterranean was the most peaceful ever when the Romans were there, right?  
**Translation:** Vocabulary: hegemons: 霸主

**[6768.52s] English:** China had very peaceful and warring times, and the peaceful times were when dynasties had a lockhold over not just themselves but all their tributaries around.  
**Translation:** 

**[6775.28s] English:** And, likewise, the most peaceful time in human history has been when the U.S. was the global hegemon, right, the last, you know, decades.  
**Translation:** Vocabulary: dynasties: 王朝; hegemon: 霸主; likewise: 同样; lockhold: 控制; tributaries: 藩属

**[6784.12s] English:** Now, we've sort of seen things start to slide, right, with Russia-Ukraine, with what's going on in the Middle East and, you know, Taiwan risk.  
**Translation:** 

**[6790.64s] English:** All these different things are starting to bubble up, still objectively extremely peaceful.  
**Translation:** Vocabulary: objectively: 客观上; taiwan: 台湾

**[6794.50s] English:** Now, what happens when it's not one global hegemon but it's two, obviously, and, you know, China will be, you know, competitive or even overtake the U.S. like it's possible, right?  
**Translation:** 

**[6803.98s] English:** And so this...  
**Translation:** Vocabulary: overtake: 超越

**[6805.28s] English:** This change in global hegemony, it's...  
**Translation:** 

**[6807.96s] English:** I don't think it ever happens, like, super peacefully, right?  
**Translation:** Vocabulary: hegemony: 霸权; peacefully: 和平地

**[6809.94s] English:** When empires fall, right, which is a possible trajectory for America, they don't fall gracefully, right?  
**Translation:** 

**[6815.64s] English:** Like, they don't just slide out of irrelevance.  
**Translation:** Vocabulary: irrelevance: 无关紧要; trajectory: 轨迹路径

**[6817.96s] English:** Usually, there's a lot of shaking.  
**Translation:** 

**[6820.24s] English:** And so, you know, what the U.S. is trying to do is maintain its top position.  
**Translation:** 

**[6825.06s] English:** And what China is trying to do is become the top position, right?  
**Translation:** 

**[6827.70s] English:** And, obviously, there's butting of heads here in the most simple terms.  
**Translation:** 

**[6832.78s] English:** And that could take shape in all kinds of ways.  
**Translation:** 

**[6835.28s] English:** Including proxy wars.  
**Translation:** Vocabulary: proxy: 代理战争

**[6837.82s] English:** And that will...  
**Translation:** 

**[6838.48s] English:** It seems like it's already happening.  
**Translation:** 

**[6839.82s] English:** Like, I...  
**Translation:** 

**[6840.00s] English:** As much as I want there to be centuries of prolonged peace, it looks like further instability internationally is ahead.  
**Translation:** 

**[6848.66s] English:** And the U.S.'s sort of current task is like, hey, if we control AI, if we're the leader in AI, and AI significantly accelerates progress, then we can maintain the global hegemony position.  
**Translation:** 

**[6861.36s] English:** I hope that works.  
**Translation:** Vocabulary: accelerates: 加速

**[6862.40s] English:** And as an American, kind of like, okay, I guess that's going to lead to peace for us.  
**Translation:** 

**[6867.54s] English:** Now, obviously, other people around the world get affected negatively.  
**Translation:** Vocabulary: negatively: 负面地

**[6872.90s] English:** Obviously, the Chinese people are not going to be in as advantageous of a position if that happens.  
**Translation:** 

**[6878.00s] English:** But this is sort of the reality of what's being done and the actions that are being carried out.  
**Translation:** Vocabulary: advantageous: 有利的

**[6884.28s] English:** So can we go back to the specific detail of the different hardware?  
**Translation:** 

**[6887.62s] English:** There's this nice graphic in the export controls of which GPUs are allowed to be exported.  
**Translation:** Vocabulary: exported: 出口的

**[6897.54s] English:** Can you kind of explain the difference?  
**Translation:** 

**[6900.28s] English:** Is there, from a technical perspective, are the H20s promising?  
**Translation:** 

**[6908.02s] English:** Yeah, so this goes, and I think we'd have to like, we need to dive really deep into the reasoning aspect and what's going on there.  
**Translation:** 

**[6914.62s] English:** But the H20, you know, the U.S. has gone through multiple iterations of the export controls, right?  
**Translation:** Vocabulary: iterations: 多次修订

**[6920.34s] English:** This H800 was at one point allowed back in 23, but then it got canceled.  
**Translation:** 

**[6924.78s] English:** And by then, you know, DeepSeek had already built their cluster.  
**Translation:** Vocabulary: cluster: 计算集群

**[6927.54s] English:** They claimed 2K.  
**Translation:** 

**[6928.76s] English:** I think they actually have like many more, like something like 10K of those.  
**Translation:** 

**[6931.80s] English:** And now this H20 is the legally allowed chip, right?  
**Translation:** 

**[6934.48s] English:** NVIDIA shipped a million of these last year to China, right?  
**Translation:** 

**[6937.22s] English:** For context, it was like four or five million GPUs, right?  
**Translation:** 

**[6939.76s] English:** So the percentage of GPUs that were this China-specific H20 is quite high, right?  
**Translation:** 

**[6945.52s] English:** You know, roughly 20%, 25%, right?  
**Translation:** 

**[6947.92s] English:** 20% or so.  
**Translation:** 

**[6948.86s] English:** And so this H20 has been neutered in one way, but it's actually upgraded in other ways, right?  
**Translation:** 

**[6955.12s] English:** And, you know, you could think of chips along three.  
**Translation:** Vocabulary: neutered: 阉割; upgraded: 升级

**[6957.58s] English:** Axis for AI, right?  
**Translation:** 

**[6959.60s] English:** You know, ignore.  
**Translation:** 

**[6960.00s] English:** Ignoring software stack and like exact architecture, just raw specifications. There's floating point operations, right? Flops. There is memory bandwidth, i.e. in memory capacity, right? IO, right? Memory. And then there is interconnect, right? Chip to chip interconnections. All three of these are incredibly important for making AI systems, right? Because AI systems involve a lot of compute.  
**Translation:** 

**[6983.00s] English:** They involve a lot of moving memory around, whether it be to memory or to other chips, right?  
**Translation:** Vocabulary: bandwidth: 内存带宽; flops: 浮点运算; interconnect: 芯片间连接; interconnections: 芯片间连接

**[6988.00s] English:** And so these three vectors, the US initially had two of these vectors controlled and one of them not controlled, which was flops and interconnect bandwidth were initially controlled.  
**Translation:** 

**[6997.82s] English:** And then they said, no, no, no, no.  
**Translation:** 

**[6999.10s] English:** We're going to remove the interconnect bandwidth and just make it a very simple only flops.  
**Translation:** 

**[7002.48s] English:** But now NVIDIA can now make a chip that has, okay, it's cut down on flops.  
**Translation:** 

**[7006.98s] English:** It's like one third that of the H100, right?  
**Translation:** 

**[7010.54s] English:** On spec sheet paper performance for flops, you know, in real world, it's closer to like half or maybe even like 60% of it, right?  
**Translation:** 

**[7019.54s] English:** But then on the other two vectors, it's just as good for interconnect bandwidth.  
**Translation:** 

**[7023.34s] English:** And then for memory bandwidth and memory capacity, the H20 has more memory bandwidth and more memory capacity than the H100, right?  
**Translation:** 

**[7030.68s] English:** Now, recently, you know, we at our research, we cut NVIDIA's production for H20 for this year down drastically.  
**Translation:** 

**[7037.94s] English:** They were going to make another 2 million of those this year.  
**Translation:** Vocabulary: drastically: 大幅地

**[7040.54s] English:** But they just canceled all the orders a couple of weeks ago.  
**Translation:** 

**[7043.50s] English:** In our view, that's because we think that they think they're going to get restricted, right?  
**Translation:** 

**[7047.50s] English:** Because why would they cancel all these orders for H20?  
**Translation:** 

**[7050.70s] English:** Because they shipped a million of them last year.  
**Translation:** 

**[7052.40s] English:** They had orders in for a couple million this year and just gone, right?  
**Translation:** 

**[7055.46s] English:** For H20, B20, right?  
**Translation:** 

**[7056.68s] English:** A successor to H20.  
**Translation:** 

**[7058.08s] English:** And now they're all gone.  
**Translation:** 

**[7059.12s] English:** Now, why would they do this, right?  
**Translation:** 

**[7061.14s] English:** I think it's very clear, right?  
**Translation:** 

**[7063.12s] English:** The H20 is actually better for certain tasks.  
**Translation:** 

**[7066.36s] English:** And that certain task is reasoning, right?  
**Translation:** 

**[7069.50s] English:** Okay, reasoning is incredibly, like, different than, you know, when you look at the different regimes of models, right?  
**Translation:** 

**[7076.26s] English:** Pre-training is all about flops, right?  
**Translation:** 

**[7079.16s] English:** It's all about flops.  
**Translation:** 

**[7080.00s] English:** There's things you do like mixture of experts that we talked about to trade off interconnect or to trade off, you know, other aspects and lower the flops and rely more on interconnect and memory.  
**Translation:** 

**[7090.26s] English:** But at the end of the day, it's flops is everything. Right. We talk about models in terms of like how many flops they are. Right.  
**Translation:** 

**[7096.64s] English:** So like, you know, we talk about, oh, GPT-4 is 2E25. Right. 2 to the 25th, you know, 25 zeros. Right. Flop. Right. Floating point operations for training.  
**Translation:** 

**[7108.72s] English:** For training. Right. And we're talking about the restrictions for the 2E24, right. The U.S. has an executive order that Trump recently unsigned, but which was, hey, 1E26, once you hit that number of floating point operations, you must notify the government and you must share your results with us. Right.  
**Translation:** 

**[7125.52s] English:** Like there's a level of model where the U.S. government must be told. Right. And that's 1E26. And so as we move forward, this is this is an incredibly like important flop is the vector that the government has cared about historically.  
**Translation:** Vocabulary: historically: 历史上

**[7137.02s] English:** But the other two vectors are.  
**Translation:** 

**[7138.72s] English:** Arguably just as important. Right. And especially when we come to this new paradigm, which the world is only just learning about over the last six months. Right. Reasoning.  
**Translation:** Vocabulary: arguably: 或许; paradigm: 范式

**[7147.44s] English:** And do we understand firmly which of the three dimensions is best for reasoning? So interconnect, the flops don't matter as much. Is it memory?  
**Translation:** 

**[7157.34s] English:** Memory. Right. Yeah. Excellent. We're going to get into technical stuff real fast.  
**Translation:** Vocabulary: dimensions: 维度; flops: 浮点; interconnect: 互联

**[7161.42s] English:** There's a there's two articles in this one that I could show maybe graphics that might be interesting for you to pull up.  
**Translation:** 

**[7166.60s] English:** For the listeners, we're looking at the second.  
**Translation:** Vocabulary: listeners: 听众

**[7168.72s] English:** Section of oh one inference architectures tokenomics.  
**Translation:** 

**[7173.22s] English:** You want to explain KV cache before we talk about this?  
**Translation:** Vocabulary: cache: 缓存; inference: 推理; tokenomics: 代经济

**[7175.14s] English:** I think like it's better to.  
**Translation:** 

**[7176.10s] English:** Okay. Yeah, we should get it.  
**Translation:** 

**[7177.24s] English:** We need to go through a lot of specific technical things as transformers to make this easier for people because it's it's incredibly important because this changes how models work.  
**Translation:** 

**[7186.30s] English:** But I think I think resetting.  
**Translation:** 

**[7187.86s] English:** Right. Why is why is memory so important?  
**Translation:** 

**[7191.22s] English:** It's because so far we've talked about parameter counts.  
**Translation:** Vocabulary: parameter: 参数

**[7193.50s] English:** Right. And mixture of experts.  
**Translation:** 

**[7194.94s] English:** You can change how many active parameters versus total parameters to embed more data.  
**Translation:** Vocabulary: embed: 嵌入

**[7198.50s] English:** I have less flops, but.  
**Translation:** 

**[7200.00s] English:** But more important, you know, another aspect of, you know, what's part of this humongous revolution in the last handful of years is the transformer.  
**Translation:** Vocabulary: humongous: 巨大

**[7206.86s] English:** Right. And the attention mechanism, attention mechanism is that the model understands the relationships between all the words in its context.  
**Translation:** 

**[7214.18s] English:** Right. And that is that is separate from the parameters themselves.  
**Translation:** 

**[7218.12s] English:** Right. And that is that is something that you must calculate.  
**Translation:** 

**[7221.58s] English:** Right. How each token, right, each word in the context length is relatively connected to each other.  
**Translation:** Vocabulary: token: 标记

**[7228.74s] English:** Right. And I think I think, Nathan, you can explain KV cache better.  
**Translation:** 

**[7231.74s] English:** KV cache is one of the optimizations.  
**Translation:** Vocabulary: optimizations: 优化措施

**[7233.08s] English:** Yeah. So the attention operator has three core things.  
**Translation:** 

**[7237.16s] English:** It's queries, keys and values.  
**Translation:** 

**[7239.70s] English:** QKV is the thing that goes into this.  
**Translation:** 

**[7242.66s] English:** You'll look at the equation.  
**Translation:** Vocabulary: equation: 方程式

**[7244.04s] English:** You see that these matrices are multiplied together.  
**Translation:** 

**[7246.62s] English:** These words, query, key and value come from information retrieval backgrounds where the query is the thing you're trying to get the values for.  
**Translation:** Vocabulary: matrices: 矩阵; multiplied: 相乘; retrieval: 检索

**[7253.78s] English:** And you access the keys and values is reweighting.  
**Translation:** 

**[7256.32s] English:** My background's not in information retrieval.  
**Translation:** Vocabulary: reweighting: 重新加权

**[7258.08s] English:** Right.  
**Translation:** 

**[7258.74s] English:** And things like this, it's just fun to have backlinks.  
**Translation:** Vocabulary: backlinks: 反向链接

**[7261.56s] English:** And what effectively happens is that when you're doing these matrix multiplications, you're having matrices that are of the size of the context length.  
**Translation:** 

**[7269.82s] English:** So the number of tokens that you put into the model and the KV cache is effectively some form of compressed representation of all the previous tokens in the model.  
**Translation:** Vocabulary: compressed: 压缩; matrix: 矩阵; multiplications: 乘法

**[7279.46s] English:** So when you're doing this, we talk about autoregressive models.  
**Translation:** 

**[7282.40s] English:** You predict one token at a time.  
**Translation:** Vocabulary: autoregressive: 自回归的

**[7284.20s] English:** You start with whatever your prompt was.  
**Translation:** 

**[7286.36s] English:** You ask a question.  
**Translation:** 

**[7287.46s] English:** Who was the president?  
**Translation:** 

**[7288.40s] English:** Who was the president in 1825?  
**Translation:** 

**[7289.92s] English:** The model then is going to generate its first token.  
**Translation:** 

**[7292.24s] English:** For each of these tokens, you're doing the same attention operator where you're multiplying these query key value matrices.  
**Translation:** Vocabulary: multiplying: 相乘

**[7300.32s] English:** But the math is very nice so that when you're doing this repeatedly, this KV cache, this key value operation, you can keep appending the new values to it.  
**Translation:** 

**[7311.24s] English:** So you keep track of what your previous values you're inferring over in this autoregressive chain.  
**Translation:** Vocabulary: appending: 追加; cache: 缓存; inferring: 推断

**[7316.40s] English:** You keep it in memory the whole time.  
**Translation:** 

**[7318.40s] English:** And this is a really good way to do it.  
**Translation:** 

**[7320.00s] English:** a crucial thing to manage when serving inference at scale. There are far bigger experts in this,  
**Translation:** 

**[7326.18s] English:** and there are so many levels of detail that you can go into. Essentially, one of the key  
**Translation:** Vocabulary: inference: 推断

**[7331.84s] English:** drawbacks of the attention operator and the transformer is that there is a form of quadratic  
**Translation:** 

**[7337.90s] English:** memory cost in proportion to the context length. So as you put in longer questions, the memory used  
**Translation:** Vocabulary: drawbacks: 缺点; quadratic: 平方的

**[7345.26s] English:** in order to make that computation is going up in the form of a quadratic. You'll hear about a lot  
**Translation:** 

**[7350.46s] English:** of other language model architectures that are like subquadratic or linear attention forms,  
**Translation:** Vocabulary: computation: 计算; subquadratic: 亚二次的

**[7356.68s] English:** which is like state-space models. We don't need to go down all these now. And then there's  
**Translation:** 

**[7361.30s] English:** innovations on attention to make this memory usage and the ability to attend over long contexts  
**Translation:** Vocabulary: innovations: 创新

**[7367.50s] English:** much more accurate and high performance. And those innovations are going to help you with,  
**Translation:** 

**[7372.22s] English:** I mean, you're highly memory constrained. They help with memory constraint,  
**Translation:** Vocabulary: constrained: 内存受限; constraint: 限制

**[7375.18s] English:** and they're going to help you with memory constraints.  
**Translation:** 

**[7375.26s] English:** So if you put in a book into, I think, Gemini is the model that has the longest context length  
**Translation:** Vocabulary: constraints: 限制; gemini: 吉米尼

**[7380.48s] English:** that people are using. Gemini is known for 1 million and now 2 million context length.  
**Translation:** 

**[7384.18s] English:** You put a whole book into Gemini, and sometimes it'll draw facts out of it. It's not perfect.  
**Translation:** 

**[7390.12s] English:** They're getting better. So there's two things. One, to be able to serve this on the memory level.  
**Translation:** 

**[7395.58s] English:** Google has magic with their TPU stack where they can serve really long contexts. And then there's  
**Translation:** 

**[7400.02s] English:** also many decisions along the way to actually make long context performance work. This implies  
**Translation:** 

**[7404.58s] English:** data.  
**Translation:** 

**[7405.26s] English:** There's subtle changes to these computations in attention, and it changes the architecture.  
**Translation:** 

**[7411.20s] English:** But serving long context is extremely memory constrained, especially when you're making a  
**Translation:** Vocabulary: computations: 计算

**[7416.30s] English:** lot of predictions. I actually don't know why input and output tokens are more expensive,  
**Translation:** 

**[7421.14s] English:** but I think essentially output tokens, you have to do more computation because you have to sample  
**Translation:** 

**[7425.10s] English:** from the model.  
**Translation:** 

**[7425.96s] English:** I can explain that. So today, if you use a model, like you look at an API, OpenAI charges  
**Translation:** 

**[7432.38s] English:** certain price per million tokens, right?  
**Translation:** 

**[7434.56s] English:** And that price for input and output tokens is different, right? And the reason is, is that  
**Translation:** 

**[7440.00s] English:** there is, you know, when you're inputting a query into the model, right? Let's say you have  
**Translation:** 

**[7444.66s] English:** a book, right? That book, you must now calculate the entire KV cache for, right? This key value  
**Translation:** Vocabulary: cache: 缓存

**[7449.58s] English:** cache. And so when you do that, that is a parallel operation. All of the tokens can be processed at  
**Translation:** 

**[7455.18s] English:** one time. And therefore you can dramatically reduce how much you're spending, right?  
**Translation:** Vocabulary: dramatically: 大幅度地; processed: 处理

**[7459.04s] English:** The flop requirements for generating a token and an input token are identical, right? If I input  
**Translation:** 

**[7464.76s] English:** one token or if I generate one token, it's completely identical. I have to go through  
**Translation:** Vocabulary: token: 令牌

**[7467.88s] English:** the model, right? But the difference is that I can do that input, i.e. the pre-fill, i.e. the  
**Translation:** 

**[7473.24s] English:** prompt simultaneously in a batch nature, right? And therefore it is all flop.  
**Translation:** 

**[7478.80s] English:** I think the pricing model mostly they use is for input tokens is about one fourth the price of the  
**Translation:** 

**[7483.82s] English:** output tokens.  
**Translation:** 

**[7484.24s] English:** Correct. But then output tokens, the reason why it's so expensive is because I can't do it in  
**Translation:** 

**[7488.26s] English:** parallel, right? It's auto-regressive. Every time I generate a token, I must not only take the  
**Translation:** 

**[7493.22s] English:** entire, I must not only read the whole entire model into memory, right? And activate it, right?  
**Translation:** 

**[7497.88s] English:** Go calculate it to generate the next token. I also have to read the entire KV cache and I generate a  
**Translation:** 

**[7502.36s] English:** token and I append that KV, that one token I generated and it's KV cache. And then I do it  
**Translation:** 

**[7506.92s] English:** again, right? And so therefore this is a non-parallel operation. And this is one where you  
**Translation:** Vocabulary: append: 附加

**[7512.90s] English:** have to, you know, in the case of pre-fill or prompt, you pull the whole model in and you  
**Translation:** 

**[7517.50s] English:** calculate 20,000 tokens at once, right? So these are features that APIs are shipping,  
**Translation:** 

**[7522.18s] English:** which is like prompt caching, pre-filling, because you can drive prices down and you can make APIs  
**Translation:** 

**[7527.86s] English:** much faster. If you know you're going to keep, if you run a business and you're going to keep  
**Translation:** Vocabulary: caching: 缓存

**[7530.96s] English:** passing the same initial content to Cloud's API, you can load that in to the Anthropic API and  
**Translation:** 

**[7537.32s] English:** always keep it there. But it's very different than we're kind of leading to the reasoning models,  
**Translation:** 

**[7541.48s] English:** which we talked, we showed this example earlier and read some of this kind of mumbling stuff.  
**Translation:** 

**[7546.66s] English:** And what happens is that the output context length is so much higher. And I mean, I learned a lot  
**Translation:** Vocabulary: mumbling: 含糊说话

**[7552.46s] English:** about this from Dylan's work, which is essentially as the output length gets higher, you're using  
**Translation:** 

**[7556.50s] English:** this, you're writing this quadrangle.  
**Translation:** Vocabulary: quadrangle: 四方形

**[7557.86s] English:** It's quadratic in terms of memory used. And then  
**Translation:** 

**[7560.00s] English:** And the GPUs that we have, effectively, you're going to run out of memory, and they're all  
**Translation:** Vocabulary: quadratic: 平方的

**[7565.36s] English:** trying to serve multiple requests at once.  
**Translation:** 

**[7567.26s] English:** So they're doing this batch processing where not all of the prompts are exactly the same,  
**Translation:** 

**[7570.54s] English:** really complex handling.  
**Translation:** 

**[7572.02s] English:** And then as context links gets longer, there's this, I think you'd call it critical batch  
**Translation:** 

**[7576.30s] English:** size, where your ability to serve more users, so how much you can parallelize your inference  
**Translation:** 

**[7583.30s] English:** plummets because of this long context.  
**Translation:** Vocabulary: inference: 推理; plummets: 急剧下降

**[7585.56s] English:** So your memory usage is going way up with these reasoning models, and you still have  
**Translation:** 

**[7589.76s] English:** a lot of users.  
**Translation:** 

**[7590.76s] English:** So effectively, the cost to serve multiplies by a ton.  
**Translation:** 

**[7595.04s] English:** And we're looking at a plot when the x-axis is sequence length.  
**Translation:** Vocabulary: multiplies: 增加很多倍

**[7599.86s] English:** I.e., how many tokens are being generated slash prompt, right?  
**Translation:** 

**[7603.36s] English:** So if I put in a book, that's a million tokens, right?  
**Translation:** 

**[7605.70s] English:** But if I put in the sky is blue, then that's like six tokens or whatever.  
**Translation:** 

**[7609.48s] English:** We should say that what we're calling reasoning and chain of thought is extending this sequence  
**Translation:** 

**[7615.24s] English:** length.  
**Translation:** 

**[7615.52s] English:** It's mostly output tokens.  
**Translation:** 

**[7616.56s] English:** So before, you know, three months ago, whenever O1 launched.  
**Translation:** 

**[7619.22s] English:** All of the use cases for long context length were like, let me put a ton of documents in  
**Translation:** 

**[7623.74s] English:** and then get an answer out, right?  
**Translation:** 

**[7625.48s] English:** And it's a single, you know, pre-fill, compute a lot in parallel, and then output a little  
**Translation:** 

**[7630.80s] English:** bit.  
**Translation:** 

**[7631.26s] English:** Now, with reasoning and agents, this is a very different idea, right?  
**Translation:** 

**[7635.06s] English:** Now, instead, I might only have like, hey, do this task, or I might have all these documents.  
**Translation:** 

**[7639.20s] English:** But at the end of the day, the model is not just like producing a little bit, right?  
**Translation:** 

**[7642.66s] English:** It's producing tons of information.  
**Translation:** 

**[7644.88s] English:** This chain of thought just continues to go and go and go and go.  
**Translation:** 

**[7648.02s] English:** And so the sequence.  
**Translation:** 

**[7649.22s] English:** Sequence length is effectively that, you know, if it's generated 10,000 tokens, it's 10,000  
**Translation:** 

**[7653.82s] English:** sequence length, right?  
**Translation:** 

**[7654.96s] English:** Or, and plus whatever you inputted in the prompt.  
**Translation:** Vocabulary: inputted: 输入的

**[7657.38s] English:** And so what this chart is showing, and it's a logarithmic chart, right, is, you know,  
**Translation:** 

**[7661.82s] English:** as you go from 1K to 4K or 4K to 16K, the memory requirements grow so fast for your  
**Translation:** Vocabulary: logarithmic: 对数的

**[7669.56s] English:** KV cache that you end up not being able to run a certain number of, you know, your sequence  
**Translation:** 

**[7675.96s] English:** length is capped or the number of users.  
**Translation:** Vocabulary: cache: 缓存

**[7677.52s] English:** Let's say the model.  
**Translation:** 

**[7678.48s] English:** So this is.  
**Translation:** 

**[7679.22s] English:** Showing for a four.  
**Translation:** 

**[7680.00s] English:** 5b model and batch size 64 llama 3145d yeah and batch size is crucial to essentially they just  
**Translation:** Vocabulary: llama: 羊驼

**[7687.34s] English:** like you want to have higher batch size to parallelize parallel your throughput 64 different  
**Translation:** 

**[7692.10s] English:** users at once right yeah and therefore your serving costs are lower right because the server  
**Translation:** Vocabulary: throughput: 处理速度

**[7695.52s] English:** costs the same right this is eight h100s roughly two dollars an hour per gpu that's sixteen dollars  
**Translation:** 

**[7700.68s] English:** an hour right that is that is like somewhat of a fixed cost you can do things to make it lower of  
**Translation:** 

**[7704.94s] English:** course but like it's like sixteen dollars an hour now how many users can you serve how many tokens  
**Translation:** 

**[7709.08s] English:** can you generate and then you divide the two and that's your cost right um and so with reasoning  
**Translation:** 

**[7713.70s] English:** models this is this is where a lot of the complexity comes about and why memory is so  
**Translation:** 

**[7718.08s] English:** important because if you have limited amounts of memory then you can't serve so many users if you  
**Translation:** Vocabulary: complexity: 复杂性

**[7723.16s] English:** have limited amounts of memory your serving speeds get lower right and so your costs get a lot lot  
**Translation:** 

**[7728.00s] English:** worse um because all of a sudden if i was used to hey on the sixteen dollar an hour server i'm  
**Translation:** 

**[7733.08s] English:** serving llama 405b or if i'm serving you know deep seek v3 um and it's all chat style  
**Translation:** 

**[7738.86s] English:** applications and i'm serving you know deep seek v3 um and it's all chat style applications  
**Translation:** 

**[7739.06s] English:** i.e we're just chatting the sequence lengths are a thousand a few thousand right uh you know when  
**Translation:** 

**[7744.56s] English:** you use the language model it's a few thousand context length most times sometimes you're  
**Translation:** 

**[7747.14s] English:** dropping a big document but then you process it you get your answer you throw it away right you  
**Translation:** 

**[7750.98s] English:** move on to the next thing right whereas with reasoning i'm now generating tens of thousands  
**Translation:** 

**[7755.72s] English:** of tokens in in sequence right and so this this memory this kv cache has to stay resonant and you  
**Translation:** 

**[7761.58s] English:** have to keep loading it you have to keep it keep it in memory constantly and now this butts out  
**Translation:** Vocabulary: resonant: 谐振的

**[7766.22s] English:** other users right if there's now a reasoning task right if there's now a reasoning task  
**Translation:** 

**[7769.06s] English:** and the model is capable of reasoning then all of a sudden i it that memory pressure means that i  
**Translation:** 

**[7774.58s] English:** can't serve as many users simultaneously let's go into deep seek again so we're in the post deep  
**Translation:** 

**[7779.80s] English:** seek r1 time i think and what we're there's two sides to this market watching how hard it is to  
**Translation:** 

**[7786.14s] English:** serve it on one side we're going to talk about deep seek themselves they now have a chat app  
**Translation:** 

**[7790.20s] English:** that got to number one on the app store disclaimer number one on the app store is measured by  
**Translation:** 

**[7794.54s] English:** velocity so it's not necessarily saying that more people have the deep seek app than chat gpt  
**Translation:** 

**[7798.84s] English:** app but it is  
**Translation:** 

**[7800.00s] English:** Still remarkable, Claude has never hit the number one in the app store, even though everyone in San Francisco is like, oh, my God, you got to use Claude, don't use strategy BT. So DeepSeek hit this. They also launched an API product recently where you can ping their API and get these super long responses for R1 out.  
**Translation:** 

**[7814.10s] English:** At the same time as these are out, we'll get to what's happened to them. Because the model weights for DeepSeek R1 are openly available and the license is very friendly, the MIT license is commercially available, all of these midsize companies and big companies are trying to be first to serve R1 to their users.  
**Translation:** Vocabulary: commercially: 商业上; midsize: 中型的

**[7833.48s] English:** We were trying to evaluate R1 because we have really similar research going on. We released the model and we're trying to compare to it. And out of all the companies that are, quote unquote, serving R1.  
**Translation:** 

**[7844.10s] English:** And they're doing it at prices that are way higher than the DeepSeek API. Most of them barely work and the throughput is really low.  
**Translation:** Vocabulary: evaluate: 评估; throughput: 吞吐量; unquote: 反引号

**[7851.06s] English:** To give context, right? Everyone, one of the parts of like freaking this out was like trying to reach the capabilities. The other aspect is they did it so cheap, right? And the so cheap, we kind of talked about on the training side, why it was so cheap.  
**Translation:** 

**[7861.86s] English:** Let's talk about why it's so cheap on the inference. It works well and it's cheap. Why is R1 so damn cheap?  
**Translation:** Vocabulary: freaking: 极度; inference: 推断

**[7868.32s] English:** So I think there's a couple of factors here, right? One is that they do have model architecture innovation.  
**Translation:** 

**[7874.10s] English:** Right. This MLA, this new attention that they've done is different than the attention from attention is all you need to transform our attention. Right. Now, others have already innovated. There's a lot of work like MQA, GQA, local, global, all these different innovations that like try to bend the curve. Right. It's still quadratic, but the constant is now smaller. Right.  
**Translation:** Vocabulary: innovated: 创新; innovations: 创新; quadratic: 二次的

**[7893.74s] English:** Related to our previous discussion, this multi-head latent attention can save about 80 to 90 percent in memory from the attention mechanism, which helps especially along context.  
**Translation:** 

**[7904.10s] English:** Related to our previous discussion, this multi-head latent attention can save about 80 to 90 percent in memory from the attention mechanism, which helps especially along context.  
**Translation:** 

**[7904.60s] English:** It's 80 to 90 percent versus the original, but then versus what people are actually doing. It's still an innovation.  
**Translation:** 

**[7909.60s] English:** This 80 to 90 percent doesn't say that the whole model is 80 to 90 percent cheaper just as one part of it.  
**Translation:** 

**[7914.72s] English:** Well, and not just that, right? Like other people have implemented techniques like local, global, sliding window and GQA, MQA.  
**Translation:** 

**[7920.00s] English:** But anyways, DeepSeq has their attention mechanism as a true architectural innovation.  
**Translation:** Vocabulary: architectural: 建筑性的

**[7925.04s] English:** They did tons of experimentation.  
**Translation:** 

**[7926.92s] English:** And this dramatically reduces the memory pressure.  
**Translation:** Vocabulary: dramatically: 显著地; experimentation: 实验

**[7929.96s] English:** It's still there, right?  
**Translation:** 

**[7930.84s] English:** It's still attention.  
**Translation:** 

**[7932.10s] English:** It's still quadratic.  
**Translation:** 

**[7933.04s] English:** It's just dramatically reduced it relative to prior forms.  
**Translation:** 

**[7936.04s] English:** Yeah, right.  
**Translation:** 

**[7936.32s] English:** That's the memory pressure.  
**Translation:** 

**[7937.74s] English:** I should say, in case people don't know, R1 is 27 times cheaper than O1.  
**Translation:** 

**[7945.26s] English:** We think that OpenAI had a large margin built in.  
**Translation:** 

**[7948.24s] English:** Okay.  
**Translation:** 

**[7948.86s] English:** There's multiple factors.  
**Translation:** 

**[7950.00s] English:** We should break down the factors, I think.  
**Translation:** 

**[7951.46s] English:** It's $2 per million token output for R1 and $60 per million token output for O1.  
**Translation:** Vocabulary: token: 令牌

**[7960.76s] English:** Yeah, let's look at this.  
**Translation:** 

**[7963.14s] English:** So I think this is very important, right?  
**Translation:** 

**[7965.18s] English:** OpenAI is that drastic gap between DeepSeq and pricing.  
**Translation:** 

**[7970.94s] English:** But DeepSeq is offering the same model, because they open-weighted it, to everyone else for a very similar, much lower price than what others are able to serve it for.  
**Translation:** Vocabulary: drastic: 巨大

**[7979.58s] English:** Right?  
**Translation:** 

**[7979.72s] English:** Right.  
**Translation:** 

**[7979.98s] English:** So there's two factors here, right?  
**Translation:** 

**[7981.60s] English:** Their model is cheaper, right?  
**Translation:** 

**[7983.52s] English:** It is 27 times cheaper.  
**Translation:** 

**[7985.18s] English:** I don't remember the number exactly off the top of my head.  
**Translation:** 

**[7986.84s] English:** So we're looking at a graphic that's showing different places serving V3, DeepSeq V3, which is similar to DeepSeq R1.  
**Translation:** 

**[7997.92s] English:** And there's a vast difference in…  
**Translation:** 

**[8000.68s] English:** In serving costs, right?  
**Translation:** 

**[8001.74s] English:** In serving costs.  
**Translation:** 

**[8002.58s] English:** And what explains that difference?  
**Translation:** 

**[8003.84s] English:** And so part of it is OpenAI has a fantastic margin, right?  
**Translation:** 

**[8007.24s] English:** They're serving.  
**Translation:** 

**[8008.08s] English:** When they're doing inference, their gross margins are…  
**Translation:** Vocabulary: inference: 推断

**[8009.98s] English:** North of 75%, right?  
**Translation:** 

**[8011.46s] English:** So that's a 4 to 5x factor right there of the cost difference, is that OpenAI is just making crazy amounts of money, because they're the only one with the capability.  
**Translation:** Vocabulary: capability: 能力

**[8020.12s] English:** Do they need that money?  
**Translation:** 

**[8021.18s] English:** Are they using it for R&D?  
**Translation:** 

**[8022.42s] English:** They're losing money, obviously, as a company, because they spend so much on training, right?  
**Translation:** 

**[8026.04s] English:** So the inference itself is a very high margin, but it doesn't recoup the cost of everything else they're doing.  
**Translation:** Vocabulary: recoup: 弥补损失

**[8030.42s] English:** Okay.  
**Translation:** 

**[8030.98s] English:** So yes, they need that money, because the revenue and margins pay for continuing to build the next thing, right?  
**Translation:** 

**[8036.54s] English:** As long as I'm raising more money.  
**Translation:** 

**[8037.80s] English:** So the suggestion is that DeepSeq is really…  
**Translation:** 

**[8039.98s] English:** Okay.  
**Translation:** 

**[8040.22s] English:** So the suggestion is that DeepSeq is really…  
**Translation:** 

**[8040.00s] English:** bleeding out money. Well, so here's one thing, right? We'll get to this in a second, but like  
**Translation:** 

**[8044.24s] English:** DeepSeek doesn't have any capacity to actually serve the model. They stopped signups.  
**Translation:** 

**[8049.00s] English:** The ability to use it is like non-existent now, right? For most people, because so many people  
**Translation:** 

**[8053.88s] English:** are trying to use it, they just don't have the GPUs to serve it, right? OpenAI has hundreds of  
**Translation:** 

**[8058.02s] English:** thousands of GPUs between them and Microsoft to serve their models. DeepSeek has a factor of  
**Translation:** 

**[8062.96s] English:** much lower, right? Even if you believe our research, which is 50,000 GPUs, and a portion  
**Translation:** 

**[8067.70s] English:** of those are for research, a portion of those are for the hedge fund, right? They still have  
**Translation:** 

**[8070.88s] English:** nowhere close to the GPU volumes and capacity to serve the model, right? At scale. So it is cheaper.  
**Translation:** 

**[8078.04s] English:** A part of that is OpenAI making a ton of money. Is DeepSeek making money on their API? Unknown.  
**Translation:** 

**[8083.50s] English:** I don't actually think so. And part of that is this chart, right? Look at all the other providers,  
**Translation:** 

**[8088.20s] English:** right? Together AI, Fireworks AI are very high-end companies, right? XMeta, Together AI is  
**Translation:** 

**[8093.36s] English:** TreeDAO and the inventor of Flash Attention, right? Which is a huge efficiency technology.  
**Translation:** Vocabulary: inventor: 发明者

**[8097.86s] English:** Right? They're very efficient, good companies. And I do know those companies make money,  
**Translation:** 

**[8102.58s] English:** right? Not tons of money on inference, but they make money. And so they're serving at like a five  
**Translation:** 

**[8106.50s] English:** to seven X difference in cost, right? And so now when you equate, okay, OpenAI is making tons of  
**Translation:** 

**[8112.48s] English:** money, that's like a five X difference. And the companies that are trying to make money for this  
**Translation:** Vocabulary: equate: 换算

**[8115.94s] English:** model is like a five X difference. There is still a gap, right? There's still a gap. And that is  
**Translation:** 

**[8119.62s] English:** just DeepSeek being really freaking good, right? The model architecture, MLA, the way they did  
**Translation:** Vocabulary: freaking: 极其

**[8124.10s] English:** the MOE, all these things, there is like legitimate, just efficiency difference.  
**Translation:** 

**[8127.86s] English:** All their low-level libraries that we talked about in training, some of them probably translate to  
**Translation:** 

**[8131.74s] English:** inference and those weren't released. So we may go a bit into conspiracy  
**Translation:** 

**[8135.56s] English:** line, but is it possible the Chinese government is subsidizing DeepSeek?  
**Translation:** Vocabulary: inference: 推断; subsidizing: 补贴

**[8140.48s] English:** I actually don't think they are. I think when you look at the Chinese labs, there's Huawei has a  
**Translation:** 

**[8147.04s] English:** lab, Moonshot AI, there's a couple other labs out there that are really close with the government.  
**Translation:** Vocabulary: moonshot: 雄心勃勃的项目

**[8151.90s] English:** And then there's labs like Alibaba and DeepSeek, which are not close with the government.  
**Translation:** 

**[8156.02s] English:** Mm-hmm.  
**Translation:** 

**[8156.66s] English:** Mm-hmm.  
**Translation:** 

**[8156.98s] English:** Mm-hmm.  
**Translation:** 

**[8157.00s] English:** Mm-hmm.  
**Translation:** 

**[8157.06s] English:** Mm-hmm.  
**Translation:** 

**[8157.16s] English:** Mm-hmm.  
**Translation:** 

**[8157.22s] English:** Mm-hmm.  
**Translation:** 

**[8157.24s] English:** Mm-hmm.  
**Translation:** 

**[8157.30s] English:** Mm-hmm.  
**Translation:** 

**[8157.34s] English:** Mm-hmm.  
**Translation:** 

**[8157.40s] English:** Mm-hmm.  
**Translation:** 

**[8157.42s] English:** Mm-hmm.  
**Translation:** 

**[8157.44s] English:** Mm-hmm.  
**Translation:** 

**[8157.46s] English:** Mm-hmm.  
**Translation:** 

**[8157.70s] English:** Mm-hmm.  
**Translation:** 

**[8157.72s] English:** Mm-hmm.  
**Translation:** 

**[8157.74s] English:** Mm-hmm.  
**Translation:** 

**[8157.76s] English:** Mm-hmm.  
**Translation:** 

**[8157.80s] English:** Mm-hmm.  
**Translation:** 

**[8157.84s] English:** Mm-hmm.  
**Translation:** 

**[8157.86s] English:** Mm-hmm.  
**Translation:** 

**[8157.90s] English:** Mm-hmm.  
**Translation:** 

**[8157.92s] English:** Mm-hmm.  
**Translation:** 

**[8157.94s] English:** Mm-hmm.  
**Translation:** 

**[8157.96s] English:** Mm-hmm.  
**Translation:** 

**[8157.98s] English:** Mm-hmm.  
**Translation:** 

**[8158.00s] English:** Mm-hmm.  
**Translation:** 

**[8158.02s] English:** Mm-hmm.  
**Translation:** 

**[8158.04s] English:** Mm-hmm.  
**Translation:** 

**[8158.06s] English:** Mm-hmm.  
**Translation:** 

**[8158.08s] English:** Mm-hmm.  
**Translation:** 

**[8158.10s] English:** Mm-hmm.  
**Translation:** 

**[8158.12s] English:** Mm-hmm.  
**Translation:** 

**[8160.00s] English:** reverent figure who's quite different, who has very different viewpoints based on the  
**Translation:** 

**[8165.56s] English:** Chinese interviews that are translated than what the CCP might necessarily want.  
**Translation:** Vocabulary: reverent: 尊敬的; viewpoints: 观点

**[8169.92s] English:** Now, to be clear, does he have a loss leader because he can fund it through his hedge fund?  
**Translation:** 

**[8173.76s] English:** Yeah, sure.  
**Translation:** 

**[8174.38s] English:** So the hedge fund might be subsidizing it.  
**Translation:** 

**[8176.56s] English:** Yes. I mean, they absolutely did, right? Because DeepSeek has not raised much money. They're now  
**Translation:** 

**[8179.86s] English:** trying to raise around in China, but they have not raised money historically. It's all just been  
**Translation:** 

**[8184.60s] English:** funded by the hedge fund. And he owns like over half the company, like 50, 60% of the company  
**Translation:** Vocabulary: historically: 历史上

**[8188.54s] English:** is owned by him.  
**Translation:** 

**[8189.18s] English:** Some of the interviews, there's discussion on how like doing this as a recruiting tool. You see  
**Translation:** Vocabulary: recruiting: 招聘

**[8192.86s] English:** this at the American companies too. It's like having GPUs, recruiting tool, being at the cutting  
**Translation:** 

**[8197.90s] English:** edge of AI, recruiting tool.  
**Translation:** 

**[8199.72s] English:** Open sourcing.  
**Translation:** 

**[8200.30s] English:** Open sourcing, recruiting tool.  
**Translation:** Vocabulary: sourcing: 采购

**[8201.80s] English:** So much talent. They were so far behind and they got so much talent because they just open source  
**Translation:** 

**[8205.48s] English:** stuff.  
**Translation:** 

**[8206.34s] English:** More conspiracy thoughts. Is it possible since they're a hedge fund that they timed everything  
**Translation:** 

**[8212.26s] English:** with this release and the pricing and they shorted NVIDIA stock and stockpile?  
**Translation:** 

**[8219.18s] English:** It's like a block of USA ad companies and released it with Stargate, like just perfect timing to be  
**Translation:** 

**[8226.34s] English:** able to make money.  
**Translation:** Vocabulary: stargate: 星际之门

**[8227.98s] English:** Like they released it on inauguration day. They know the international, what is on the  
**Translation:** 

**[8232.92s] English:** international calendar, but I mean, I don't expect them to. If you listen to their motivations for  
**Translation:** Vocabulary: inauguration: 就职日; motivations: 动机

**[8237.46s] English:** AI, it's like.  
**Translation:** 

**[8238.54s] English:** No, if you release, they released V3 on like December 26th. Like who releases the date?  
**Translation:** 

**[8243.36s] English:** No one looks right. They released the papers before this, right? The V3 paper and the R1 paper.  
**Translation:** 

**[8248.48s] English:** So people,  
**Translation:** 

**[8249.10s] English:** have been looking at it and be like wow um and then they just released the r1 model i think  
**Translation:** 

**[8253.48s] English:** they're just shipping as fast as they can and like who cares about christmas who cares about  
**Translation:** Vocabulary: christmas: 圣诞节

**[8257.10s] English:** you know get it out before chinese new year right obviously which just happened um i don't think  
**Translation:** 

**[8261.10s] English:** they actually were like timing the market or trying to make the biggest splash possible i  
**Translation:** 

**[8265.22s] English:** think they're just like shipping i think that's one of their big advantages i we know that a lot  
**Translation:** 

**[8269.72s] English:** of the american companies are very invested in safety and that is the central culture of a place  
**Translation:** 

**[8275.06s] English:** like anthropic and i think anthropic sounds like a wonderful place to work but if safe  
**Translation:** 

**[8280.00s] English:** safety is your number one goal, it takes way longer to get artifacts out. That's why Anthropic  
**Translation:** Vocabulary: artifacts: 文物

**[8285.18s] English:** is not open sourcing things. That's their claims. But there's reviews internally. Anthropic  
**Translation:** 

**[8290.62s] English:** mentions things to international governments. There's been news of how Anthropic has done  
**Translation:** Vocabulary: internally: 内部地

**[8295.58s] English:** pre-release testing with the UK AI Safety Institute. All of these things add inertia  
**Translation:** 

**[8299.82s] English:** to the process of getting things out. And we're on this trend line where the progress is very high.  
**Translation:** Vocabulary: inertia: 阻力

**[8304.56s] English:** So if you reduce the time from when your model is done training, you run evals, it's good.  
**Translation:** 

**[8308.98s] English:** You want to get it out as soon as possible to maximize the perceived quality of your outputs.  
**Translation:** Vocabulary: maximize: 最大化

**[8315.52s] English:** DeepSeat does this so well. Dario explicitly said Claude 3.5 Sonnet was trained nine months or  
**Translation:** 

**[8321.26s] English:** nine to 10 months ago. And I think it took them another handful of months to release it. So it's  
**Translation:** Vocabulary: explicitly: 明确地

**[8326.64s] English:** like there is a significant gap here. And especially with reasoning models, the word in the  
**Translation:** 

**[8332.60s] English:** San Francisco street is that Anthropic has a better model than O3. And they won't release it.  
**Translation:** 

**[8337.88s] English:** Why? Because...  
**Translation:** 

**[8338.98s] English:** Chains of thought are scary, right? And they are legitimately scary, right? If you look at R1,  
**Translation:** Vocabulary: legitimately: 确实地

**[8343.58s] English:** it flips back and forth between Chinese and English. Sometimes it's gibberish. And then  
**Translation:** 

**[8347.56s] English:** the right answer comes out, right? And like for you and I, it's like, great.  
**Translation:** Vocabulary: gibberish: 乱说

**[8351.20s] English:** Great. I mean, like people are infatuated with you. You're telling me this is a high value thing  
**Translation:** 

**[8355.80s] English:** and it works and it's doing this. It's amazing. I mean, you talked about that sort of like chain  
**Translation:** Vocabulary: infatuated: 狂热喜爱

**[8361.22s] English:** of thought for that philosophical thing, which is not something they trained it to be philosophically  
**Translation:** 

**[8364.88s] English:** good. It's just sort of an artifact of the chain of thought training it did. But like,  
**Translation:** Vocabulary: artifact: 产物; philosophical: 哲学的; philosophically: 从哲学角度看

**[8368.86s] English:** that's...  
**Translation:** 

**[8368.96s] English:** That's super important in that, like, can I inspect your mind and what you're thinking right  
**Translation:** 

**[8374.04s] English:** now? No. And so I don't know if you're lying to my face. And chain of thought models are that way,  
**Translation:** 

**[8378.74s] English:** right? Like this is a true quote unquote risk between a chat application where, hey, I asked  
**Translation:** Vocabulary: unquote: 引号

**[8383.98s] English:** the model to say bad words or whatever, or how to make anthrax. And it tells me that's unsafe,  
**Translation:** 

**[8389.50s] English:** sure. But that's something I can get out relatively easily. What if I tell the AI to do a task and  
**Translation:** Vocabulary: anthrax: 炭疽病

**[8395.12s] English:** then it does the task all of a sudden randomly in a way that I don't want it, right? And now that  
**Translation:** 

**[8398.94s] English:** has like much more...  
**Translation:** 

**[8400.00s] English:** task versus like response is very different right so the bar for safety is much higher  
**Translation:** 

**[8403.94s] English:** at least this is anthropics case right like for deep seek they're like ship right yeah so i mean  
**Translation:** Vocabulary: anthropics: 人类智能

**[8409.78s] English:** the bar for safety is probably lowered a bit because of deep seek i mean there's parallels  
**Translation:** 

**[8414.60s] English:** here to the space race the reason the soviets probably put a man in space first is because  
**Translation:** 

**[8420.54s] English:** their approach to safety was uh the bar for safety was lower and they they killed that dog right and  
**Translation:** 

**[8427.64s] English:** all these things right so it's like a less risk averse uh than the than the u.s space program  
**Translation:** Vocabulary: averse: 规避风险

**[8433.34s] English:** and there's parallels here but you know there's probably going to be downward pressure on that  
**Translation:** 

**[8438.34s] English:** safety bar for the u.s companies right this is something that dario talks about is like that's  
**Translation:** 

**[8443.14s] English:** the situation that dario wants to avoid is dario talks to about the difference between race to the  
**Translation:** 

**[8449.18s] English:** bottom and race to the top and the race to the top is where there's a very high standard on safety  
**Translation:** 

**[8453.24s] English:** there's a very high standard on your model forms and certain about crucial evaluations and  
**Translation:** 

**[8457.64s] English:** when certain companies are really good to it they will converge this is the idea and  
**Translation:** Vocabulary: converge: 汇聚; evaluations: 评估

**[8461.86s] English:** ultimately ai is not confined to one nationality or to one like set of morals for what it should  
**Translation:** 

**[8471.24s] English:** mean and there's a lot of arguments on like should we stop open sourcing models and if the u.s stops  
**Translation:** Vocabulary: confined: 局限于; sourcing: 采购

**[8477.58s] English:** it's pretty clear i mean it's way easier to see now at deep seek that a different international  
**Translation:** 

**[8482.74s] English:** body will be the one that builds it they we talk about the cost of training deep seek as this  
**Translation:** 

**[8487.64s] English:** shocking five million dollar number think about how many entities in the world can afford a hundred  
**Translation:** 

**[8491.76s] English:** times that to have the best open source model that people use in the world and it's like it's  
**Translation:** 

**[8498.24s] English:** a scary reality which is that these open models are probably going to keep coming for the time  
**Translation:** 

**[8503.18s] English:** being whether or not we want to stop them and it is like stopping them might make it even worse and  
**Translation:** 

**[8508.50s] English:** harder to prepare but it just means that the preparation and understanding what ai can do  
**Translation:** 

**[8513.00s] English:** is just so much more important that's why i'm here the  
**Translation:** 

**[8517.64s] English:** end of the day but it's like budding that thing  
**Translation:** 

**[8520.00s] English:** into people especially not in ai is that like this is coming there are some structural things  
**Translation:** 

**[8525.44s] English:** in a global interconnected world that you have to accept yeah you mentioned uh you sent me something  
**Translation:** 

**[8532.00s] English:** that zuck mark zuckerberg mentioned on the earnings call he said that i think in light of  
**Translation:** Vocabulary: interconnected: 相互连接

**[8536.96s] English:** some of the recent news the new competitor deep seek from china i think it's one of the things  
**Translation:** 

**[8541.60s] English:** that we're talking about is there's going to be an open source standard globally and i think for  
**Translation:** Vocabulary: globally: 全世界

**[8546.16s] English:** our kind of national advantage it's important that it's an american standard  
**Translation:** 

**[8550.32s] English:** so we take that seriously we want to build the ai system that people around the world are using  
**Translation:** 

**[8555.20s] English:** and i think that if anything some of the recent news has only strengthened our conviction  
**Translation:** 

**[8559.68s] English:** that this is the right thing to be focused on so yeah open sourcing yeah mark zuckerberg is not  
**Translation:** 

**[8564.16s] English:** new to having american values and how he presents his company's trajectory i think their products  
**Translation:** 

**[8570.88s] English:** have long since been banned in china and i i respect the saying it directly and and there's  
**Translation:** Vocabulary: trajectory: 发展路径

**[8575.60s] English:** an interesting  
**Translation:** 

**[8576.16s] English:** aspect of just because it's open weights or open source doesn't mean it can't be subverted right  
**Translation:** Vocabulary: subverted: 被篡改

**[8582.08s] English:** there have been many open source software bugs that have been like uh you know for example there  
**Translation:** 

**[8586.96s] English:** was a linux bug that was found after like 10 years which was clearly a back door uh because somebody  
**Translation:** 

**[8592.16s] English:** was like why is this taking uh you know half a second to the recent one right like there's why  
**Translation:** 

**[8596.08s] English:** is this taking half a second to load and it was like oh crap there's a back door here that's why  
**Translation:** 

**[8600.00s] English:** right and it's like this is very much possible with ai models right um today you know the the  
**Translation:** 

**[8606.16s] English:** alignment of these models is very clear right like i'm not gonna say you know bad words i'm not gonna  
**Translation:** Vocabulary: alignment: 对齐

**[8612.08s] English:** teach you how to make anthrax i'm not gonna talk about tiananmen square uh i'm not gonna you know  
**Translation:** 

**[8616.40s] English:** you know things like i'm gonna say taiwan is part of you know is is just in eastern province right  
**Translation:** Vocabulary: taiwan: 台湾; tiananmen: 天安门广场

**[8621.52s] English:** like you know all these things are like depending on who you are what you align what you know whether  
**Translation:** 

**[8626.32s] English:** you know even like xai is aligned a certain way right you know there they might be it's not aligned  
**Translation:** Vocabulary: align: 对齐; aligned: 对齐的

**[8631.60s] English:** in the like woke sense it's not aligned in the like pro china sense but there is certain things  
**Translation:** 

**[8635.60s] English:** that are imbued within the model now when you release this publicly in an instruct model  
**Translation:** Vocabulary: imbued: 蕴含; instruct: 指导

**[8639.52s] English:** that's open  
**Translation:** 

**[8640.00s] English:** and weights this can then proliferate right but as these systems get more and more capable  
**Translation:** Vocabulary: proliferate: 迅速增加

**[8644.58s] English:** what you can embed deep down in the model is not as clear right um and so they're asked that is  
**Translation:** 

**[8650.90s] English:** like one of the big fears is like if a an american model or a chinese model is the top model right  
**Translation:** Vocabulary: embed: 植入

**[8656.50s] English:** you're going to embed things that are unclear and it can be unintentional too right like british  
**Translation:** 

**[8660.66s] English:** english is dead because american llms won right and the internet is american and therefore like  
**Translation:** Vocabulary: unintentional: 无意的

**[8665.82s] English:** color is spelled the way americans spell it right and this is just strong words right now  
**Translation:** 

**[8670.04s] English:** this is just like this is just the factual nature of the llms the right way to carve with each we  
**Translation:** 

**[8674.84s] English:** the english is the hottest programming language and that english is defined by a bunch of companies  
**Translation:** 

**[8679.36s] English:** that primarily are in san francisco the right way to spell optimization is with a z just in case  
**Translation:** Vocabulary: optimization: 优化

**[8685.68s] English:** it's an i think it's an s in british english it is taking it as something silly right like  
**Translation:** 

**[8691.90s] English:** something as silly as the spelling like which british and english you know brits and and  
**Translation:** Vocabulary: brits: 英国人

**[8695.70s] English:** and and and and and and and and and and and and and and and and and and and and and and and and  
**Translation:** 

**[8695.80s] English:** and americans will like laugh about probably right i don't think we care that much uh but like  
**Translation:** 

**[8700.32s] English:** you know some people will but like this can this can boil down into like very  
**Translation:** 

**[8704.14s] English:** very important topics like hey you know so you know subverting people right uh you know chat  
**Translation:** Vocabulary: subverting: 颠覆

**[8710.76s] English:** bots right character ai has shown that they can like you know talk to kids and or adults and like  
**Translation:** 

**[8716.60s] English:** it will like you people feel a certain way right and that's unintentional alignment but like what  
**Translation:** 

**[8722.00s] English:** happens when there's intentional alignment deep down on the open source standard it's a  
**Translation:** 

**[8725.68s] English:** backdoor today for like linux right that we discover or some encryption system right china  
**Translation:** Vocabulary: backdoor: 后门; encryption: 加密; intentional: 故意的

**[8730.70s] English:** uses different encryption than nist defines the us nist because there's clearly at least they think  
**Translation:** 

**[8735.10s] English:** there's backdoors in it right um what happens when the models are backdoors not just to computer  
**Translation:** Vocabulary: backdoors: 后门

**[8740.52s] English:** systems but to our minds yeah they're cultural black doors the thing that amplifies the relevance  
**Translation:** 

**[8746.44s] English:** of culture with language models is that we are used to this mode of interacting with people in  
**Translation:** Vocabulary: amplifies: 增强; relevance: 相关性

**[8753.56s] English:** back and forth conversation and we have  
**Translation:** 

**[8755.68s] English:** now have a super, a very powerful computer system that slots into  
**Translation:** 

**[8760.00s] English:** a social context they were used to which makes people very we don't know the extent that which  
**Translation:** 

**[8767.00s] English:** people can be impacted by that so there there could be this is one this is an actual concern  
**Translation:** 

**[8773.06s] English:** with a chinese company that is providing open weights models is that there could be some secret  
**Translation:** 

**[8780.00s] English:** chinese government sort of requirement for these models to have a certain kind of backdoor to have  
**Translation:** 

**[8786.90s] English:** some kind of thing i don't necessarily think it'll be a backdoor right because once it's open  
**Translation:** 

**[8790.96s] English:** weights it doesn't like phone home it's more about like if it recognizes a certain system  
**Translation:** 

**[8795.86s] English:** it could like if now now it could be a backdoor in the sense of like hey if you're building a  
**Translation:** 

**[8800.18s] English:** software uh you know something in software all of a sudden it's a software agent oh program this  
**Translation:** 

**[8805.34s] English:** backdoor that only we know about or it could be like subvert the mind to think that like xyz  
**Translation:** 

**[8810.12s] English:** opinion is the correct one anthropic has research on this where they show that if you put different  
**Translation:** Vocabulary: subvert: 颠覆

**[8815.36s] English:** phrases certain phrases in  
**Translation:** 

**[8816.84s] English:** at pre-training you can then elicit different behavior when you're actually using the model  
**Translation:** Vocabulary: elicit: 引出

**[8821.96s] English:** because they've like poisoned the pre-training data i don't think like as of now i don't think  
**Translation:** 

**[8827.22s] English:** anybody in a production system is trying to do anything like this i think it's mostly  
**Translation:** Vocabulary: poisoned: 污染数据

**[8831.86s] English:** anthropic is doing very direct work and mostly just subtle things we don't know what these  
**Translation:** 

**[8837.90s] English:** models are going to how they are going to generate tokens what information they're  
**Translation:** 

**[8842.26s] English:** going to represent and what the complex representations they have are well one of  
**Translation:** 

**[8846.56s] English:** the  
**Translation:** 

**[8846.84s] English:** we're talking about anthropic which is generally just is permeated with like good humans trying to  
**Translation:** 

**[8853.40s] English:** do good in the world i i don't we just don't know of any labs this would be done in the military  
**Translation:** Vocabulary: permeated: 充满

**[8859.68s] English:** context that are explicitly trained to okay how can we the the front door looks like a happy nl  
**Translation:** 

**[8869.34s] English:** lm but underneath it's a thing that will over time do the maximum amount of damage to the  
**Translation:** 

**[8876.84s] English:** weapons to our quote unquote enemies there there's this very good quote from  
**Translation:** 

**[8880.00s] English:** emaltment who you know he can be a hype beast sometime but one of the things he said and i  
**Translation:** 

**[8884.64s] English:** think i agree is that superhuman persuasion will happen before superhuman intelligence yeah right  
**Translation:** 

**[8890.20s] English:** and if that's the case then these things before before we get this agi asi stuff we can embed  
**Translation:** Vocabulary: embed: 植入; persuasion: 说服

**[8896.08s] English:** superhuman persuasion towards our ideal or whatever the ideal of the model maker is right and again  
**Translation:** 

**[8901.44s] English:** like today i truly don't believe deep seek has done this right like but it is a sign of like  
**Translation:** 

**[8906.02s] English:** what could happen so one of the dystopian worlds is uh described by brave new world so we could  
**Translation:** 

**[8911.98s] English:** just be stuck scrolling instagram looking at cute puppies or worse and then talking to bots that are  
**Translation:** Vocabulary: dystopian: 乌托邦反面; scrolling: 滑动浏览

**[8919.52s] English:** giving us a narrative and we completely get lost in that world that's controlled by somebody else  
**Translation:** 

**[8924.28s] English:** but versus thinking independently and that's that's that's a major concern as we rely more  
**Translation:** 

**[8930.00s] English:** and more on these kinds of systems i mean we've already seen this with recommendation systems  
**Translation:** 

**[8933.86s] English:** yeah recommendation systems hack the  
**Translation:** 

**[8935.88s] English:** the  
**Translation:** 

**[8936.02s] English:** dopamine induced reward circuit but the brain is a lot more complicated and what other  
**Translation:** 

**[8940.14s] English:** sort of circuits quote-unquote feedback loops in your brain can you hack slash  
**Translation:** 

**[8943.78s] English:** subvert in ways like recommendation systems are purely just trying to do you know increase time  
**Translation:** Vocabulary: circuits: 电路; subvert: 颠覆

**[8949.86s] English:** and ads and etc but there's so many more goals that can be achieved through these complicated  
**Translation:** 

**[8955.00s] English:** models there's no reason in some number of years that you can't train a language model to maximize  
**Translation:** 

**[8960.22s] English:** time spent on a chat app like right now they are trained i mean is that not what character i  
**Translation:** 

**[8965.84s] English:** a i has done their time per session is like two hours yeah character i'm probably very likely could  
**Translation:** 

**[8971.24s] English:** be optimizing this where it's like the the way that this data is collected is naive or it's like  
**Translation:** 

**[8975.18s] English:** you're presented a few options and you choose them but there's that's not the only way that  
**Translation:** Vocabulary: naive: 幼稚; optimizing: 优化

**[8979.30s] English:** these models are going to be trained it's naive stuff like talk to an anime girl but like it can  
**Translation:** 

**[8982.92s] English:** be like yeah this is a risk right like it's it's a bit of a cliche thing to say but i've uh over  
**Translation:** Vocabulary: anime: 动画; cliche: 陈词滥调

**[8989.86s] English:** the past year had a few stretches of time where i didn't use social media or the internet at all  
**Translation:** 

**[8995.84s] English:** and just read books and was out in nature and it like it clearly has a  
**Translation:** 

**[9000.00s] English:** an effect on the mind where like it changed like i feel like i'm returning of course i was  
**Translation:** 

**[9005.84s] English:** raised before the internet really took off but i'm returning to someone  
**Translation:** 

**[9010.12s] English:** i know where you're going i mean you can see it physiologically like i take three days if i'm  
**Translation:** 

**[9015.96s] English:** like backpacking or something and you you're you're literal like you're breaking down addiction  
**Translation:** Vocabulary: backpacking: 徒步旅行; physiologically: 生理上

**[9021.78s] English:** cycles i feel like i'm more in control of my mind there feels like a sovereignty of intelligence  
**Translation:** 

**[9028.02s] English:** that's happening when i'm disconnected from the internet i think um the more i use the internet  
**Translation:** 

**[9033.58s] English:** and social media the more other people are controlling my mind there's definitely a feeling  
**Translation:** 

**[9037.64s] English:** and then in the future that would be not other people but algorithms or other people presented  
**Translation:** 

**[9043.30s] English:** to me via algorithms there i mean there are already tons of ai bots on the internet and  
**Translation:** 

**[9048.42s] English:** every so right now it's not frequent but every so often i have replied to one and they're instantly  
**Translation:** 

**[9052.96s] English:** replied i'm like crap i was a bot and that is just going to become more common like they're  
**Translation:** 

**[9057.94s] English:** going to be more common and i'm going to be more common and i'm going to be more common  
**Translation:** 

**[9058.00s] English:** gonna get good one of the hilarious things about technology over its history is that the uh illicit  
**Translation:** 

**[9063.88s] English:** adult entertainment industry has always adopted technologies first right whether it was like video  
**Translation:** Vocabulary: illicit: 非法的

**[9069.10s] English:** streaming yeah um to like where you know the there's now the like sort of like independent  
**Translation:** 

**[9073.96s] English:** adult illicit content creators uh who have their you know subscription pages and there they actually  
**Translation:** 

**[9079.32s] English:** heavily utilize uh you know generative ai has already been like diffusion models and all that  
**Translation:** 

**[9083.04s] English:** is huge there but now these like these these subscription-based individual creators do use  
**Translation:** Vocabulary: diffusion: 扩散模型; generative: 生成式

**[9088.16s] English:** bots to approximate themselves and chat with their you know people pay a lot for it and people pay a  
**Translation:** 

**[9093.70s] English:** lot right it's a lot of times it's them but a lot of there are agencies that do this for these  
**Translation:** Vocabulary: approximate: 近似

**[9098.04s] English:** creators and do it like on a like mass scale so the largest creators are like able to talk to  
**Translation:** 

**[9104.18s] English:** hundreds or thousands of like people at a time because of these bots and so it's it's already  
**Translation:** 

**[9110.18s] English:** being used there obviously you know like video streaming  
**Translation:** 

**[9113.04s] English:** and and other technologies have gone there first it's going to come to the rest of society too  
**Translation:** 

**[9117.04s] English:** there's a general concern that models  
**Translation:** 

**[9120.00s] English:** get censored by the companies that deploy them so one case when we've seen that and maybe censorship  
**Translation:** Vocabulary: censored: 被删改; censorship: 审查制度; deploy: 部署

**[9126.78s] English:** is one word alignment maybe via rlhf or some other way is another word so that we saw that  
**Translation:** 

**[9135.52s] English:** with black nazi image generation with uh gemini uh as you mentioned we also see that uh with  
**Translation:** Vocabulary: alignment: 对齐方式; gemini: 金星

**[9143.64s] English:** chinese models refusing to answer what happened in uh june 4th 1989 at tiananmen square so how  
**Translation:** 

**[9151.68s] English:** can this be avoided and maybe can you just in general talk about how this happens and how can  
**Translation:** Vocabulary: tiananmen: 天安门广场

**[9157.82s] English:** it be avoided you give multiple examples um there's probably a few things to keep in mind here  
**Translation:** 

**[9166.04s] English:** one is the kind of tiananmen square factual knowledge like did think like how does that  
**Translation:** 

**[9172.30s] English:** get embedded into the model  
**Translation:** 

**[9173.64s] English:** two is the gemini what you called the black nazi incident which is when gemini as a system  
**Translation:** 

**[9181.30s] English:** had this extra thing put into it that dramatically changed the behavior  
**Translation:** 

**[9184.90s] English:** and then three is what most people would call general alignment rlhf post-training  
**Translation:** Vocabulary: dramatically: 大幅度地

**[9190.60s] English:** each of these have very different scopes and how they are applied in order to do if you're just  
**Translation:** 

**[9196.90s] English:** look at the model weights in order to audit specific facts is extremely hard because you  
**Translation:** 

**[9203.06s] English:** have to chrome  
**Translation:** 

**[9203.62s] English:** through the pre-training data and look at all this and then that's terabytes of files and look  
**Translation:** Vocabulary: terabytes: 千兆字节

**[9209.76s] English:** for very specific words or hints of the words so i guess one way to say is that you can insert  
**Translation:** 

**[9215.06s] English:** censorship or alignment at various stages in the pipeline and what you refer to now is at the very  
**Translation:** Vocabulary: insert: 插入; pipeline: 管道

**[9220.46s] English:** beginning of the data so if you want to get rid of facts in a model you have to do it at every  
**Translation:** 

**[9225.82s] English:** stage you have to do it at the pre-training so most people think that pre-training is where  
**Translation:** 

**[9229.52s] English:** most of the knowledge is put into the model and then you can  
**Translation:** 

**[9233.62s] English:** and move that in different ways whether through post-training or whether through systems  
**Translation:** 

**[9237.88s] English:** afterwards this is where the whole like  
**Translation:** 

**[9240.00s] English:** models comes from right like gpt will not tell you how to make anthrax but if you try really  
**Translation:** Vocabulary: anthrax: 炭疽病菌

**[9245.10s] English:** really hard you can eventually get to tell you about anthrax because they didn't filter it from  
**Translation:** 

**[9249.66s] English:** the pre-training data set right but by the way removing facts has such a ominous dark feel to it  
**Translation:** Vocabulary: ominous: 不祥的

**[9258.12s] English:** almost think it's practically impossible because you effectively have to remove them from the  
**Translation:** 

**[9261.76s] English:** internet you're you're taking on a what did did they remove the the thing from the subreddits  
**Translation:** Vocabulary: subreddits: 细分论坛

**[9268.44s] English:** the mmmm it gets filtered out right so that's quality filters which are small language models  
**Translation:** 

**[9273.74s] English:** that look at a document and tell you like how good is this text is it close to a wikipedia  
**Translation:** 

**[9278.34s] English:** article which is a good thing that we want language models to be able to imitate so couldn't  
**Translation:** 

**[9282.94s] English:** you do a small language model that filters out mentions of tiananmen square in the data yes but  
**Translation:** Vocabulary: tiananmen: 天安门

**[9287.66s] English:** is it going to catch um wordplay or encoded language i mean people have been meaning on  
**Translation:** 

**[9292.72s] English:** like games and other stuff how to like say things that don't say tiananmen square um but or  
**Translation:** Vocabulary: encoded: 编码; wordplay: 文字游戏

**[9298.36s] English:** like  
**Translation:** 

**[9298.42s] English:** yeah so there's always like different ways to do it there's hey the internet as a whole does tend  
**Translation:** 

**[9303.62s] English:** to just have a slight left bias right because it's always been richer more affluent uh younger  
**Translation:** 

**[9310.04s] English:** people on the internet relative to the rest of the population so there is already inherently a  
**Translation:** 

**[9315.00s] English:** slight left bias right on the internet and so how do you filter things that are this complicated  
**Translation:** 

**[9319.62s] English:** right is it like and and some of these can be like you know factual non-factual but like tiananmen  
**Translation:** 

**[9324.50s] English:** square is obviously the example of a factual but it gets a lot harder when you're talking about  
**Translation:** 

**[9327.92s] English:** aligning to a ideal right um which is yeah and so grok for example right elon's tried really hard  
**Translation:** Vocabulary: aligning: 对齐

**[9335.46s] English:** to make the model not be super pc and woke but the best way to do pre-training is to throw the  
**Translation:** 

**[9341.76s] English:** whole freaking internet at it right and then later figure out but then at the end of the day  
**Translation:** Vocabulary: freaking: 该死的

**[9345.10s] English:** the model at its core now still has some of these ideals right you still ingested reddit slash r  
**Translation:** 

**[9350.08s] English:** slash politics which is probably the largest political discussion board on the world that's  
**Translation:** Vocabulary: ingested: 吸收

**[9353.54s] English:** freely available to scrape and guess what that's left-leaning right um and so um  
**Translation:** 

**[9357.92s] English:** you know there are some aspects like  
**Translation:** Vocabulary: scrape: 抓取

**[9360.00s] English:** that that you just can't censor unless you try really really really really really hard  
**Translation:** 

**[9364.62s] English:** so the base model will always have some tds trauma derangement syndrome because it's trained so much  
**Translation:** Vocabulary: censor: 审查; trauma: 创伤

**[9371.20s] English:** it'll have the ability to express it but what if there's a there's a wide representation in the  
**Translation:** 

**[9377.78s] English:** data this is what happens it's like a lot of modern what is called post-training it's a series  
**Translation:** 

**[9382.74s] English:** of techniques to get the model on rails of a really specific behavior uh and i mean it's it's  
**Translation:** 

**[9388.84s] English:** like you can you also have the ingested data of like twitter or like reddit slash r slash the  
**Translation:** 

**[9393.54s] English:** donald which is like also super pro trump right and then you have like fascist subreddits or like  
**Translation:** 

**[9397.64s] English:** you have communist subreddits so you the model in pre-training ingests everything it has no world  
**Translation:** Vocabulary: fascist: 法西斯; ingests: 摄入; subreddits: 版块

**[9402.50s] English:** view now it does have like some some skew because more of the text is skewed a certain way uh which  
**Translation:** 

**[9408.46s] English:** is general like slight left like but also like you know somewhat like you know intellectual  
**Translation:** Vocabulary: skewed: 偏向

**[9414.22s] English:** somewhat like you know it's just like the general internet is a certain way and then and then as as  
**Translation:** 

**[9418.72s] English:** as  
**Translation:** 

**[9418.84s] English:** as Nathan's about to describe eloquently, right?  
**Translation:** 

**[9420.76s] English:** Like you can elicit certain things out.  
**Translation:** Vocabulary: elicit: 引出; eloquently: 流畅地

**[9422.70s] English:** And there's a lot of history here.  
**Translation:** 

**[9423.84s] English:** So we can go through multiple examples  
**Translation:** 

**[9425.24s] English:** and what happened.  
**Translation:** 

**[9426.20s] English:** Lama2 was a launch that the phrase  
**Translation:** 

**[9429.36s] English:** like too much RLHF or like too much safety  
**Translation:** 

**[9431.44s] English:** was a lot, it's just,  
**Translation:** 

**[9434.14s] English:** that was the whole narrative  
**Translation:** 

**[9435.20s] English:** after Lama2's chat models released.  
**Translation:** 

**[9437.64s] English:** And the examples are sorts of things  
**Translation:** 

**[9440.32s] English:** like you would ask Lama2 chat,  
**Translation:** 

**[9441.96s] English:** how do you kill a Python process?  
**Translation:** 

**[9443.26s] English:** And it would say, I can't talk about killing  
**Translation:** 

**[9445.76s] English:** because that's a bad thing.  
**Translation:** 

**[9446.90s] English:** And anyone that is trying to design an AI model  
**Translation:** 

**[9450.20s] English:** will probably agree that that's just like,  
**Translation:** 

**[9451.92s] English:** eh, model, you messed up a bit on the training there.  
**Translation:** 

**[9454.58s] English:** I don't think they meant to do this,  
**Translation:** 

**[9455.74s] English:** but this was in the model weight.  
**Translation:** 

**[9456.92s] English:** So this is not, it didn't necessarily be,  
**Translation:** 

**[9459.56s] English:** there's things called system prompts,  
**Translation:** 

**[9461.14s] English:** which are when you're querying a model,  
**Translation:** 

**[9464.50s] English:** it's a piece of text that is shown to the model,  
**Translation:** Vocabulary: querying: 提问

**[9467.04s] English:** but not to the user.  
**Translation:** 

**[9468.14s] English:** So a fun example is your system prompt  
**Translation:** 

**[9471.38s] English:** could be talk like a pirate.  
**Translation:** 

**[9472.28s] English:** So no matter what the user says to the model,  
**Translation:** 

**[9474.82s] English:** it'll respond like a pirate.  
**Translation:** 

**[9476.28s] English:** In practice,  
**Translation:** 

**[9476.70s] English:** what they are is you are a helpful assistant.  
**Translation:** 

**[9480.00s] English:** you should break down problems. If you don't know about something, don't tell them your date cut off  
**Translation:** 

**[9484.68s] English:** is this, today's date is this. It's a lot of really useful context for how can you answer  
**Translation:** 

**[9488.66s] English:** a question well. And Anthropic publishes their system. Yes, which I think is great. And there's  
**Translation:** 

**[9492.94s] English:** a lot of research that goes into this. And one of your previous guests, Amanda Askell, is probably  
**Translation:** 

**[9497.98s] English:** the most knowledgeable person, at least in the combination of execution and sharing. She's the  
**Translation:** 

**[9503.00s] English:** person that should talk about system prompts and character of models. Yeah, and people should read  
**Translation:** 

**[9507.20s] English:** these system prompts because you're trying to nudge sometimes through extreme politeness  
**Translation:** Vocabulary: nudge: 暗示; politeness: 礼貌

**[9514.72s] English:** the model to be a certain way. And you could use this for bad things. We've done tests, which is  
**Translation:** 

**[9519.88s] English:** what if I tell the model to be a dumb model? Which evaluation scores go down? And it's like,  
**Translation:** 

**[9526.50s] English:** we'll have this behavior where it could sometimes say, oh, I'm supposed to be dumb. And sometimes  
**Translation:** 

**[9530.28s] English:** it doesn't affect math abilities as much, but something like if you're trying, it's just the  
**Translation:** 

**[9536.02s] English:** quality of a human judgment.  
**Translation:** 

**[9537.20s] English:** Let's go back to post-training, specifically RLHF around LAMA2. It was too much safety  
**Translation:** 

**[9544.44s] English:** prioritization was baked into the model weights. This makes you refuse things in a really annoying  
**Translation:** 

**[9549.38s] English:** way for users. It's not great. It caused a lot of awareness to be attached to RLHF that it makes  
**Translation:** Vocabulary: prioritization: 优先级设定

**[9557.20s] English:** the models dumb. And it stigmatized the word. It did in AI culture. And as the techniques have  
**Translation:** 

**[9562.86s] English:** evolved, that's no longer the case where all of these labs have very fine-grained control.  
**Translation:** Vocabulary: stigmatized: 污名化

**[9567.20s] English:** What they get out of the models through techniques like RLHF.  
**Translation:** 

**[9570.02s] English:** Although different labs are definitely different levels. On one end of the spectrum is Google.  
**Translation:** 

**[9576.64s] English:** And then maybe OpenAI does less and Anthropic does less. And then on the other end of the  
**Translation:** 

**[9581.36s] English:** spectrum is XAI. But they all have different forms of RLHF trying to make them a certain way.  
**Translation:** 

**[9587.36s] English:** And the important thing to say is that no matter how you want the model to behave,  
**Translation:** 

**[9593.60s] English:** these RLHF and preference tuning techniques also improve performance.  
**Translation:** 

**[9597.20s] English:** And things like math evals and code evals, there is  
**Translation:** 

**[9600.00s] English:** something innate to these, what is called contrastive loss functions. We could start to  
**Translation:** 

**[9604.46s] English:** get into RL here. We don't really need to, but RLHF also boosts performance on anything from a  
**Translation:** 

**[9609.26s] English:** chat task to a math problem to a code problem. So it is becoming a much more useful tool to these  
**Translation:** 

**[9615.32s] English:** labs. So this kind of takes us through the arc of, we've talked about pre-training, hard to get rid  
**Translation:** 

**[9619.40s] English:** of things. We've talked about post-training and how post-training, you can mess it up. It's a  
**Translation:** 

**[9624.14s] English:** complex, multifaceted optimization with 10 to 100 person teams converging on one artifact. It's  
**Translation:** 

**[9630.34s] English:** really easy to not do it perfectly. And then there's the third case, which is what we talked  
**Translation:** Vocabulary: artifact: 产物; converging: 汇聚; multifaceted: 多面的; optimization: 优化

**[9634.30s] English:** about Gemini. The thing that was about Gemini is this was a served product where Google has their  
**Translation:** 

**[9640.08s] English:** internal model weights. They've done all these processes that we talked about. And in the served  
**Translation:** Vocabulary: gemini: 双子座

**[9643.80s] English:** product, what came out after this was that they had a prompt that they were rewriting user queries  
**Translation:** 

**[9648.26s] English:** to boost diversity or something. And this just made it, the outputs were just blatantly wrong.  
**Translation:** Vocabulary: blatantly: 明显地; rewriting: 重写

**[9653.86s] English:** It was a...  
**Translation:** 

**[9654.14s] English:** Some sort of organizational failure that had this prompt in that position.  
**Translation:** 

**[9658.46s] English:** And I think Google executives probably have owned this. I didn't pay that attention,  
**Translation:** 

**[9662.46s] English:** that detail, but it was just a mess up in execution that led to this ridiculous thing.  
**Translation:** 

**[9666.74s] English:** But at the system level, the model weights might have been fine.  
**Translation:** 

**[9669.86s] English:** So at the very end of the pipeline, there was a rewriting.  
**Translation:** Vocabulary: pipeline: 处理流程

**[9672.82s] English:** To something like a system prompt. It was like the system prompt or what is called in industry  
**Translation:** 

**[9678.24s] English:** is like you rewrite prompts. So especially for image models, if you're using DALI or chat GPT,  
**Translation:** 

**[9684.14s] English:** you can generate you an image. You'll say, draw me a beautiful car. With these leading image  
**Translation:** 

**[9689.86s] English:** models, they benefit from highly descriptive prompts. So what would happen is if you do that  
**Translation:** Vocabulary: descriptive: 描述详细的

**[9695.52s] English:** on chat GPT, a language model behind the scenes will rewrite the prompt, say, make this more  
**Translation:** 

**[9700.14s] English:** descriptive. And then that is passed to the image model. So prompt rewriting is something that is  
**Translation:** 

**[9704.44s] English:** used at multiple levels of industry. And it's used effectively for image models. And the Gemini  
**Translation:** 

**[9708.94s] English:** example is just a failed execution. Big philosophical question here.  
**Translation:** Vocabulary: philosophical: 哲学的

**[9714.14s] English:** With RLHF, to generalize, where is human?  
**Translation:** 

**[9720.00s] English:** input, human in the loop, human data most useful at the current stage?  
**Translation:** Vocabulary: generalize: 泛化

**[9726.60s] English:** For the past few years, the highest cost human data has been in these preferences,  
**Translation:** 

**[9732.36s] English:** which is comparing, I would say, highest cost and highest total usage. So a lot of money has  
**Translation:** 

**[9738.10s] English:** gone to these pairwise comparisons where you have two model outputs and a human is  
**Translation:** 

**[9742.04s] English:** comparing between the two of them. In earlier years, there was a lot of this instruction  
**Translation:** Vocabulary: pairwise: 一一比较

**[9747.16s] English:** tuning data. So creating highly specific examples to something like a Reddit question to a domain  
**Translation:** 

**[9753.48s] English:** that you care about. Language models used to struggle on math and code. So you would pay  
**Translation:** 

**[9757.52s] English:** experts in math and code to come up with questions and write detailed answers that  
**Translation:** 

**[9761.26s] English:** were used to train the models. Now it is the case that there are many model options that  
**Translation:** 

**[9767.32s] English:** are way better than humans at writing detailed and eloquent answers for things like model and  
**Translation:** 

**[9772.60s] English:** code. So they talked about this with the Lama 3 release where they switched to use  
**Translation:** 

**[9777.14s] English:** Lama 3, 4, or 5B to write their answers for math and code. But they, in their paper,  
**Translation:** 

**[9783.26s] English:** talk about how they use extensive human preference data, which is something that  
**Translation:** 

**[9787.12s] English:** they haven't gotten AIs to replace. There are other techniques in industry like constitutional  
**Translation:** 

**[9790.78s] English:** AI where you use human data for preferences and AI for preferences. And I expect the AI  
**Translation:** 

**[9795.34s] English:** part to scale faster than the human part. But among the research that we have access to  
**Translation:** 

**[9800.44s] English:** is that humans are in this kind of preference loop.  
**Translation:** 

**[9804.42s] English:** So for as reasoning becomes,  
**Translation:** 

**[9807.14s] English:** bigger and bigger and bigger, as we said, where's the role of humans in that?  
**Translation:** 

**[9810.96s] English:** It's even less prevalent. So it's the remarkable thing about these reasoning results,  
**Translation:** 

**[9816.64s] English:** and especially the DeepSeek R1 paper, is this result that they call DeepSeek R1-0,  
**Translation:** Vocabulary: prevalent: 普遍的

**[9821.58s] English:** which is they took one of these pre-trained models. They took DeepSeek V3 base,  
**Translation:** 

**[9825.32s] English:** and then they do this reinforcement learning optimization on verifiable questions or  
**Translation:** Vocabulary: optimization: 优化; reinforcement: 强化; verifiable: 可验证的

**[9830.00s] English:** verifiable rewards for a lot of questions and a lot of training. And these reasoning behaviors  
**Translation:** 

**[9835.44s] English:** emerge naturally. So these things,  
**Translation:** 

**[9837.14s] English:** like wait, let me see, wait, let me check this.  
**Translation:** 

**[9840.00s] English:** that might be a mistake. And they emerge from only having questions and answers. And when you're  
**Translation:** 

**[9845.74s] English:** using the model, the part that you look at is the completion. So in this case, all of that just  
**Translation:** 

**[9850.88s] English:** emerges from this large-scale RL training. And that model, which the weights are available,  
**Translation:** 

**[9856.58s] English:** has no human preferences added into the post-training. The DeepSeek R1 full model has  
**Translation:** 

**[9863.32s] English:** some of this human preference tuning, this RLHF, after the reasoning stage. But the very remarkable  
**Translation:** 

**[9868.76s] English:** thing is that you can get these reasoning behaviors, and it's very unlikely that there's  
**Translation:** 

**[9873.28s] English:** humans writing out reasoning chains. It's very unlikely that they somehow hacked OpenAI and they  
**Translation:** Vocabulary: hacked: 破解入侵

**[9877.72s] English:** got access to OpenAI 01's reasoning chains. It's something about the pre-trained language models  
**Translation:** 

**[9883.62s] English:** and this RL training, where you reward the model for getting the question right.  
**Translation:** 

**[9888.06s] English:** And therefore, it's trying multiple solutions, and it emerges this chain of thought.  
**Translation:** 

**[9892.98s] English:** This might be a good place to mention the eloquent and the insightful tweet  
**Translation:** Vocabulary: eloquent: 口才好

**[9898.74s] English:** of the great and the powerful Andrzej Karpathy. I think he had a bunch of thoughts, but one of them,  
**Translation:** 

**[9904.80s] English:** last thought, not sure if this is obvious. You know something profound is coming when you're  
**Translation:** Vocabulary: profound: 深奥

**[9909.24s] English:** saying it's not sure if it's obvious. There are two major types of learning in both children and  
**Translation:** 

**[9914.36s] English:** in deep learning. There's one, imitation learning, watch and repeat, i.e. pre-training, supervised,  
**Translation:** Vocabulary: imitation: 模仿; supervised: 监督

**[9920.34s] English:** fine-tuning. And two, trial and error learning, reinforcement learning. My favorite simple example  
**Translation:** 

**[9926.60s] English:** is AlphaGo. One is AlphaGo. AlphaGo is a training tool for learning. AlphaGo is a training tool for  
**Translation:** 

**[9928.72s] English:** learning by imitating expert players. Two is reinforcement learning to win the game.  
**Translation:** 

**[9933.58s] English:** Almost every single shocking result of deep learning and the source of all magic is always  
**Translation:** Vocabulary: imitating: 模仿

**[9939.62s] English:** two. Two is significantly more powerful. Two is what surprises you. Two is when the paddle learns  
**Translation:** 

**[9946.78s] English:** to hit the ball behind the blocks and break out. Two is when AlphaGo beats even Lee Sedol.  
**Translation:** 

**[9952.18s] English:** And two is the aha moment when the deep seek or oh one, et cetera,  
**Translation:** 

**[9958.72s] English:** that it works well to  
**Translation:** Vocabulary: cetera: 等等

**[9960.00s] English:** re-evaluate your assumptions, backtrack, try something else, etc. It's the solving strategies  
**Translation:** 

**[9966.04s] English:** you see this model use in its chain of thought. It's how it goes back and forth thinking to itself.  
**Translation:** Vocabulary: assumptions: 前提; backtrack: 回溯

**[9973.38s] English:** These thoughts are emergent, three exclamation points, and this is actually seriously incredible,  
**Translation:** 

**[9979.94s] English:** impressive, and new, and is publicly available and documented. The model could never learn this with  
**Translation:** Vocabulary: emergent: 涌现; exclamation: 感叹

**[9986.28s] English:** imitation because the cognition of the model and the cognition of the human labeler is different.  
**Translation:** 

**[9993.10s] English:** The human would never know to correctly annotate these kinds of solving strategies  
**Translation:** Vocabulary: annotate: 标注; cognition: 认知

**[9996.62s] English:** and what they should even look like. They have to be discovered during reinforcement learning  
**Translation:** 

**[10002.06s] English:** as empirically and statistically useful towards the final outcome. Anyway, the alpha zero sort of  
**Translation:** Vocabulary: alpha: 阿尔法; empirically: 根据经验; reinforcement: 强化学习

**[10007.08s] English:** metaphor analogy here. Can you speak to that, the magic of the chain of thought that he's referring  
**Translation:** 

**[10013.30s] English:** to? I think it's good to recap AlphaGo and  
**Translation:** Vocabulary: metaphor: 比喻

**[10016.02s] English:** AlphaZero.  
**Translation:** 

**[10016.28s] English:** Because it plays nicely with these analogies between imitation learning and learning from  
**Translation:** Vocabulary: analogies: 类比

**[10020.00s] English:** scratch. So AlphaGo, the beginning of the process was learning from humans where they started the  
**Translation:** 

**[10026.18s] English:** first, this is the first expert level Go player or chess player in DeepMind's series of models  
**Translation:** 

**[10031.60s] English:** where they had some human data. And then why it is called AlphaZero is that there was zero human  
**Translation:** 

**[10036.96s] English:** data in the loop. And that change to AlphaZero made a model that was dramatically more powerful  
**Translation:** Vocabulary: dramatically: 大幅度地

**[10042.24s] English:** for DeepMind. So this remove of the human prior, the  
**Translation:** 

**[10046.02s] English:** human inductive bias makes the final system far more powerful. This we mentioned bitter lesson  
**Translation:** Vocabulary: inductive: 归纳的

**[10051.14s] English:** hours ago, and this is all aligned with this. And then there's been a lot of discussion in  
**Translation:** 

**[10058.80s] English:** language models. This is not new. This goes back to the whole Q star rumors, which if you piece  
**Translation:** Vocabulary: aligned: 一致

**[10065.06s] English:** together the pieces is probably the start of open AI figuring out it's all one stuff. When last year  
**Translation:** 

**[10070.42s] English:** in November, the Q star rumors came out. There's a lot of intellectual,  
**Translation:** 

**[10076.02s] English:** drive to know when is something like this going to happen with language models?  
**Translation:** 

**[10080.00s] English:** because we know these models are so powerful and we know it has been so successful in the past.  
**Translation:** 

**[10084.92s] English:** And it is a reasonable analogy that this new type of reinforced learning training for reasoning  
**Translation:** 

**[10091.18s] English:** models is when the door is open to this. We don't yet have the equivalent of turn 37,  
**Translation:** Vocabulary: reinforced: 加强的

**[10097.76s] English:** which is the famous turn where the DeepMind's AI plan go stumped Lee Sedol completely. We don't  
**Translation:** 

**[10104.42s] English:** have something that's that level of focal point, but that doesn't mean that the approach to  
**Translation:** Vocabulary: stumped: 难倒

**[10108.46s] English:** technology is different and the impact of the general training. It's still incredibly new.  
**Translation:** 

**[10112.52s] English:** What do you think that point would be? What would be move 37 for chain of thought, for reasoning?  
**Translation:** 

**[10117.42s] English:** Scientific discovery. When you use this sort of reasoning problem in it,  
**Translation:** 

**[10121.48s] English:** just something we fully don't expect. I think it's actually probably simpler than that. It's  
**Translation:** 

**[10125.98s] English:** probably something related to computer user robotics rather than science discovery. Because  
**Translation:** 

**[10131.90s] English:** the important aspect here is models take so much data to learn, they're not sample  
**Translation:** 

**[10138.46s] English:** efficient. They take the entire web, over 10 trillion tokens to train on. This would take  
**Translation:** 

**[10145.74s] English:** a human thousands of years to read. And humans know most of the stuff, a lot of the stuff models  
**Translation:** Vocabulary: trillion: 万亿

**[10153.60s] English:** know better than it. Humans are way, way, way more sample efficient. That is because of the  
**Translation:** 

**[10157.98s] English:** self-play. How does a baby learn what its body is? As it sticks its foot in its mouth and it says,  
**Translation:** 

**[10164.04s] English:** oh, this is my body. It sticks its hand in its mouth and it calibrates,  
**Translation:** 

**[10168.46s] English:** its touch on its fingers with the most sensitive touch thing on its tongue. This is how babies  
**Translation:** Vocabulary: calibrates: 校准

**[10172.80s] English:** learn. And it's just self-play over and over and over and over again. And now we have something  
**Translation:** 

**[10178.80s] English:** that is similar to that with these verifiable proofs, whether it's a unit test in code or  
**Translation:** Vocabulary: verifiable: 可验证的

**[10185.92s] English:** mathematical verifiable task, generate many traces of reasoning. And keep branching them out,  
**Translation:** 

**[10193.22s] English:** keep branching them out. And then check at the end, hey, which one actually has the right answer?  
**Translation:** Vocabulary: mathematical: 数学的

**[10196.52s] English:** Most of them are wrong. Great. These are the few that are right.  
**Translation:** 

**[10198.46s] English:** Maybe we use some sort of reward model.  
**Translation:** 

**[10200.00s] English:** outside of this to select even the best one to preference as well but now you've started to get  
**Translation:** 

**[10204.54s] English:** better and better at these benchmarks and so you've seen over the last six months a skyrocketing  
**Translation:** Vocabulary: benchmarks: 评估标准; skyrocketing: 急剧上升

**[10209.12s] English:** in a lot of different benchmarks right all math and code benchmarks were pretty much solved except  
**Translation:** 

**[10213.86s] English:** for frontier math which is designed to be almost questions that aren't practical to most people  
**Translation:** Vocabulary: frontier: 前沿

**[10218.94s] English:** because they're like they're exam level open math problem type things so it's like on the math  
**Translation:** 

**[10226.22s] English:** problems that are somewhat reasonable which is like somewhat complicated word problems or coding  
**Translation:** 

**[10230.22s] English:** problems it's just what dylan is saying so the thing here is that these are only with verifiable  
**Translation:** 

**[10236.10s] English:** tasks we earlier showed an example of the you know the really interesting like what happens  
**Translation:** 

**[10240.42s] English:** when chain of thought is to a non-verifiable thing it's just like a human you know chatting  
**Translation:** 

**[10244.26s] English:** right with the you know thinking about what's novel for humans right a unique thought but this  
**Translation:** 

**[10248.94s] English:** task and form of training only works when it's infinite when it's verifiable and from here the  
**Translation:** 

**[10254.40s] English:** thought is okay we can continue  
**Translation:** 

**[10256.20s] English:** to scale this current training method by increasing the number of verifiable tasks  
**Translation:** 

**[10260.36s] English:** in math and coding coding probably has a lot more to go math has a lot less to go in terms of what  
**Translation:** 

**[10266.58s] English:** are verifiable things can i create a solver that then i generate trajectories toward or traces  
**Translation:** 

**[10271.50s] English:** towards reasoning traces towards and then prune the ones that don't work and keep the ones that  
**Translation:** Vocabulary: prune: 剪枝; solver: 求解器; trajectories: 轨迹

**[10275.30s] English:** do work well those are going to be solved pretty quickly but even if you've solved math you have not  
**Translation:** 

**[10279.66s] English:** actually created intelligence right and so this is where i think the like aha moment  
**Translation:** 

**[10285.32s] English:** of  
**Translation:** 

**[10286.20s] English:** computer user robotics will come in because now you have a sandbox or a playground that is  
**Translation:** Vocabulary: sandbox: 试验环境

**[10291.96s] English:** infinitely verifiable right did you you know messing around on the internet there are so many  
**Translation:** 

**[10297.34s] English:** actions that you can do that are verifiable it'll start off with like log into a website create an  
**Translation:** Vocabulary: infinitely: 无穷地

**[10301.36s] English:** account click a button here blah blah blah but it'll then get to the point where it's hey go do  
**Translation:** 

**[10306.18s] English:** a task on tasker or whatever these other all these various task websites hey go get hundreds of likes  
**Translation:** 

**[10310.96s] English:** right um and and it's going to fail it's going to spawn hundreds of accounts it's going to fail on  
**Translation:** 

**[10315.00s] English:** most of them but this one got to a thousand great now you've reached the verifiable thing  
**Translation:** Vocabulary: spawn: 滋生; verifiable: 可验证的

**[10318.62s] English:** and you just keep iterating  
**Translation:** 

**[10320.00s] English:** this loop over and over and that's when and same with robotics right that's where you know where  
**Translation:** 

**[10324.10s] English:** you have an infinite playground of tasks like hey did i put the ball in the bucket all the way to  
**Translation:** 

**[10328.18s] English:** like oh did i like build a car right like you know there's a whole trajectory to speed run or you  
**Translation:** Vocabulary: trajectory: 轨迹

**[10333.42s] English:** know what models can do but at some point i truly think that like you know we'll spawn models and  
**Translation:** 

**[10339.52s] English:** initially all the training will be in sandboxes but then at some point you know the language model  
**Translation:** Vocabulary: sandboxes: 隔离环境

**[10343.24s] English:** pre-training is going to be dwarfed by what is this reinforcement learning you know you'll  
**Translation:** 

**[10347.94s] English:** pre-train a multimodal model that can see that can read that can write you know blah blah blah  
**Translation:** Vocabulary: multimodal: 多模态; reinforcement: 强化学习

**[10351.92s] English:** whatever vision audio etc but then you'll have it play in a sandbox infinitely and figure out  
**Translation:** 

**[10358.82s] English:** figure out math figure out code figure out navigating the web figure out operating a robot  
**Translation:** Vocabulary: navigating: 浏览网页

**[10362.58s] English:** arm right and then it'll learn so much and the aha moment i think will be when this is available  
**Translation:** 

**[10368.46s] English:** to then create something that's not good right like oh cool part of it was like figuring out  
**Translation:** 

**[10372.48s] English:** how to use the web now all of a sudden it's figured out really well how to just get hundreds  
**Translation:** 

**[10377.36s] English:** of thousands of files and then it's like oh cool i'm going to do this now i'm going to do this now  
**Translation:** 

**[10377.92s] English:** that are real and real engagement on twitter because all of a sudden this is one of the  
**Translation:** 

**[10381.30s] English:** things that are verifiable and maybe not just engagement but make money yes i've become i mean  
**Translation:** 

**[10387.22s] English:** that could be the thing where almost fully automated it makes you know 10 million dollars  
**Translation:** 

**[10393.28s] English:** by being an influencer selling a product creating the product like  
**Translation:** Vocabulary: automated: 自动化; influencer: 意见领袖

**[10396.54s] English:** and and i i'm not referring to like a hype product but an actual product  
**Translation:** 

**[10401.68s] English:** like holy shit this thing created a business it's running it it's the face of the business  
**Translation:** 

**[10407.92s] English:** that kind of thing maybe or maybe uh number one song like it creates the whole infrastructure  
**Translation:** 

**[10413.28s] English:** required to create the song to be the influencer that represents that song that kind of thing  
**Translation:** 

**[10417.98s] English:** and makes a lot of that could be the move i mean this our culture respects money in that kind of  
**Translation:** 

**[10424.00s] English:** way and it's and it's verifiable right the bank account can't lie exactly there's surprising  
**Translation:** 

**[10430.84s] English:** evidence that once you set up the ways of collecting the verifiable domain that this can work  
**Translation:** 

**[10435.66s] English:** there's a been a lot of research  
**Translation:** Vocabulary: verifiable: 可验证的

**[10437.92s] English:** before this r1 on math  
**Translation:** 

**[10440.00s] English:** problems and they approach math with language models just by increasing the number of samples  
**Translation:** 

**[10444.70s] English:** so you can just try again and again and again and you look at the amount of times that the language  
**Translation:** 

**[10449.54s] English:** models get it right and what we see is that even very bad models get it right sometimes and the  
**Translation:** 

**[10456.14s] English:** whole idea behind reinforcement learning is that you can learn from very sparse rewards so it it  
**Translation:** 

**[10462.08s] English:** doesn't the space of language and the space of tokens whether you're generating language or  
**Translation:** Vocabulary: sparse: 稀疏的

**[10466.06s] English:** tasks for a robot is so big that you might say that it's like i mean each the tokenizer for a  
**Translation:** 

**[10471.74s] English:** language model can be like 200 000 things so at each each step it can sample from that big of a  
**Translation:** Vocabulary: tokenizer: 分词器

**[10475.54s] English:** space so if it can generate a bit of a signal that it can climb onto that's the what the whole field  
**Translation:** 

**[10481.78s] English:** of rl is around is learning from sparse rewards and the same thing has played out in math where  
**Translation:** 

**[10487.12s] English:** it's like very weak models that sometimes generate answers where you see research already that  
**Translation:** 

**[10491.42s] English:** you can boost their math scores you can do this sort of rl training  
**Translation:** 

**[10494.78s] English:** for  
**Translation:** 

**[10495.70s] English:** for math it might not be as effective but if you take a 1 billion parameter model so something 600  
**Translation:** 

**[10500.62s] English:** times smaller than deep seek you can boost its grade school math scores very directly with a  
**Translation:** 

**[10505.94s] English:** small amount of this training so it's not to say that this is coming soon setting up the  
**Translation:** 

**[10510.96s] English:** verification domains is extremely hard and there's a lot of nuance in this but there are some basic  
**Translation:** 

**[10516.72s] English:** things that we have seen before where it's like it's at least expectable that there's a domain  
**Translation:** Vocabulary: nuance: 细微差别; verification: 验证

**[10521.92s] English:** and there's a chance that this works all right so we have fun things happening in real  
**Translation:** 

**[10525.60s] English:** time  
**Translation:** 

**[10525.70s] English:** this is a good opportunity to talk about other reasoning models 0103 just now open ai as perhaps  
**Translation:** 

**[10534.76s] English:** expected released 03 mini what are we expecting from the different flavors can you just lay out  
**Translation:** 

**[10542.10s] English:** the different flavors of the old models and from gemini the reasoning model something i would say  
**Translation:** 

**[10548.04s] English:** about these reasoning models is we talked a lot about reasoning training on math and code and what  
**Translation:** Vocabulary: gemini: 金星外理模型

**[10553.18s] English:** is done is that you have the base model we've talked about a lot of the reasoning training  
**Translation:** 

**[10555.70s] English:** so for example you look at the internet and you can do a lot on the internet you do this large scale  
**Translation:** 

**[10559.86s] English:** reasoning training with reinforcement learning  
**Translation:** 

**[10560.00s] English:** And then what the DeepSeq paper detailed in this R1 paper, which for me is one of the big open questions on how do you do this, is that they did reasoning heavy, but very standard post-training techniques after the large scale reasoning RL.  
**Translation:** Vocabulary: reinforcement: 强化

**[10575.22s] English:** So they did the same things with a form of instruction tuning through rejection sampling, which is essentially heavily filtered instruction tuning with some reward models.  
**Translation:** 

**[10583.96s] English:** And then they did this RLHF, but they made it math heavy.  
**Translation:** 

**[10587.14s] English:** So some of this transfer, we looked at this philosophical example early on.  
**Translation:** 

**[10593.38s] English:** One of the big open questions is how much does this transfer?  
**Translation:** Vocabulary: philosophical: 哲学的

**[10596.90s] English:** If we bring in domains after the reasoning training, are all the models going to become eloquent writers by reasoning?  
**Translation:** 

**[10603.52s] English:** Is this philosophy stuff going to be open?  
**Translation:** Vocabulary: eloquent: 口才好

**[10605.06s] English:** We don't know in the research of how much this will transfer.  
**Translation:** 

**[10607.72s] English:** There's other things about how we can make soft verifiers and things like this.  
**Translation:** Vocabulary: verifiers: 验证器

**[10611.18s] English:** But there is more training after reasoning, which makes it easier to use these reasoning models.  
**Translation:** 

**[10616.48s] English:** And that's what we're using right now.  
**Translation:** 

**[10617.84s] English:** So if we're going to talk about with 3Mini and O1, these have gone through these extra techniques that are designed for human preferences after being trained to elicit reasoning.  
**Translation:** 

**[10626.82s] English:** I think one of the things that people are ignoring is Google's Gemini flash thinking is both cheaper than R1 and better.  
**Translation:** Vocabulary: elicit: 引发

**[10635.58s] English:** And they released it in the beginning of December.  
**Translation:** 

**[10637.48s] English:** And nobody's talking about it.  
**Translation:** 

**[10638.36s] English:** No one cares.  
**Translation:** 

**[10638.76s] English:** It has a different flavor to it.  
**Translation:** 

**[10640.28s] English:** Its behavior is less expressive than something like O1.  
**Translation:** 

**[10642.86s] English:** It has fewer tracks than it is on.  
**Translation:** Vocabulary: expressive: 表达力强的

**[10645.34s] English:** Quinn released a model.  
**Translation:** 

**[10646.48s] English:** Last fall, QWQ, which was their preview reasoning model.  
**Translation:** Vocabulary: quinn: Quinn

**[10651.12s] English:** And in DeepSeek had R1 Lite last fall, where these models kind of felt like they're on rails, where they really, really only can do math and code.  
**Translation:** 

**[10658.44s] English:** And O1 is it can answer anything.  
**Translation:** 

**[10660.94s] English:** It might not be perfect for some tasks, but it's flexible.  
**Translation:** 

**[10664.48s] English:** It has some richness to it.  
**Translation:** 

**[10666.78s] English:** And this is kind of the art of like how cook like as a model, a little bit undercooked.  
**Translation:** 

**[10671.82s] English:** It's like it's good to get a model out the door, but it's hard to gauge.  
**Translation:** Vocabulary: gauge: 衡量; undercooked: 半生的

**[10675.86s] English:** And it takes a lot of taste to be like, is this a full fledged model?  
**Translation:** 

**[10680.00s] English:** can i use this for everything they're probably more similar for math and code my quick read is  
**Translation:** 

**[10684.98s] English:** that gemini flash is like not trained the same way as 01 but taking an existing training stack  
**Translation:** 

**[10693.10s] English:** adding reasoning to it so taking a more normal training stack and adding reasoning to it  
**Translation:** Vocabulary: gemini: 双子座模型

**[10697.06s] English:** and i'm sure they're gonna have more i mean they've done quick releases on gemini flash the  
**Translation:** 

**[10701.80s] English:** reasoning and this is the second version from the holidays it's evolving fast and  
**Translation:** 

**[10707.56s] English:** it takes longer to make this training stack where you're doing this large scale ask the  
**Translation:** 

**[10712.24s] English:** same question from uh earlier uh the one about the the human nature yeah what was the human  
**Translation:** 

**[10718.96s] English:** nature one uh the way i can ramble why i can ramble about this so much is that we've been  
**Translation:** 

**[10724.68s] English:** working on this at ai2 before 01 was fully available to everyone and before r1 which is  
**Translation:** Vocabulary: ramble: 啰嗦

**[10730.44s] English:** essentially using this rl training for fine tuning we use this in our like tulu series of models  
**Translation:** 

**[10735.58s] English:** and you can  
**Translation:** 

**[10737.40s] English:** you can  
**Translation:** 

**[10737.50s] English:** you can  
**Translation:** 

**[10737.54s] English:** the same behaviors where you say like wait and so and so much on but it's so late in the training  
**Translation:** 

**[10742.82s] English:** process that this kind of reasoning expression is much lighter so you can there's there's  
**Translation:** 

**[10747.48s] English:** essentially a gradation and just how much of this rl training you put into it determines how the  
**Translation:** 

**[10751.80s] English:** output looks so uh we're now using gemini 2.0 flash thinking experimental 121 it summarized  
**Translation:** Vocabulary: gradation: 等级划分; summarized: 总结

**[10761.58s] English:** the problem as humans self-domesticated apes perspective okay all right so wait is this  
**Translation:** 

**[10769.86s] English:** reviewing the the reasoning here's why this is a novel okay uh oh yeah and click to expand okay  
**Translation:** 

**[10776.66s] English:** analyze the request novel is the keyword like see how it just looks a little different it looks like  
**Translation:** 

**[10783.36s] English:** a normal output yeah it's i mean in some sense it's better structured it makes more sense and  
**Translation:** Vocabulary: keyword: 关键字

**[10790.42s] English:** in it  
**Translation:** 

**[10791.52s] English:** well  
**Translation:** 

**[10791.56s] English:** when it latched onto human and then it went into organisms and oh wow apex predator focus on  
**Translation:** 

**[10798.28s] English:** domestication  
**Translation:** Vocabulary: domestication: 驯化; latched: 附着; predator: 捕食者

**[10800.00s] English:** Apply domestication to humans.  
**Translation:** 

**[10801.98s] English:** Explore the idea of self-domestication.  
**Translation:** 

**[10804.70s] English:** Not good.  
**Translation:** 

**[10806.08s] English:** Not good.  
**Translation:** 

**[10806.80s] English:** Where is this going?  
**Translation:** 

**[10808.90s] English:** Refine and articulate the insight.  
**Translation:** Vocabulary: articulate: 表达清晰; refine: 精炼

**[10810.62s] English:** Greater facial expressiveness and communication ability.  
**Translation:** 

**[10813.92s] English:** Yes.  
**Translation:** Vocabulary: facial: 面部

**[10815.12s] English:** Plasticity and adaptability.  
**Translation:** 

**[10816.60s] English:** Yes.  
**Translation:** Vocabulary: adaptability: 适应性

**[10817.04s] English:** Dependence on social groups.  
**Translation:** 

**[10818.50s] English:** Yes.  
**Translation:** 

**[10819.02s] English:** All right.  
**Translation:** 

**[10820.30s] English:** And self-critique and refine further.  
**Translation:** 

**[10823.40s] English:** Wow.  
**Translation:** 

**[10824.54s] English:** Is this truly novel?  
**Translation:** 

**[10826.06s] English:** Is it well-supported?  
**Translation:** 

**[10828.30s] English:** So on.  
**Translation:** 

**[10829.46s] English:** And so forth.  
**Translation:** 

**[10830.74s] English:** And the insight is getting at is humans are not just social animals,  
**Translation:** 

**[10834.50s] English:** but profoundly self-domesticated apes.  
**Translation:** 

**[10837.36s] English:** And this self-domestication is the key to understanding our unique cognitive  
**Translation:** Vocabulary: cognitive: 认知; profoundly: 深刻地

**[10841.66s] English:** and social abilities.  
**Translation:** 

**[10843.26s] English:** Self-domesticated apes.  
**Translation:** 

**[10845.70s] English:** I prefer the deep seek response.  
**Translation:** 

**[10848.66s] English:** I mean, it's novel.  
**Translation:** 

**[10851.56s] English:** The insight is novel.  
**Translation:** 

**[10853.44s] English:** I mean, that's like a good book title.  
**Translation:** 

**[10855.62s] English:** Self-domesticated apes.  
**Translation:** 

**[10857.94s] English:** There could be a case made for that.  
**Translation:** 

**[10859.32s] English:** I mean.  
**Translation:** 

**[10859.46s] English:** Yeah, it's cool.  
**Translation:** 

**[10860.06s] English:** And it's revealing the reasoning.  
**Translation:** 

**[10862.26s] English:** It's magical.  
**Translation:** 

**[10863.70s] English:** It's magical.  
**Translation:** 

**[10865.04s] English:** Like, this is really powerful.  
**Translation:** 

**[10867.82s] English:** Hello, everyone.  
**Translation:** 

**[10869.60s] English:** This is Lex with a quick intermission recorded after the podcast.  
**Translation:** Vocabulary: intermission: 休息时段

**[10874.74s] English:** Since we reviewed responses from Deep Seeker 1 and Gemini Flash 2.0 thinking during this  
**Translation:** 

**[10880.26s] English:** conversation, I thought at this moment, it would be nice to insert myself quickly doing  
**Translation:** Vocabulary: gemini: 双子座; insert: 插入

**[10886.08s] English:** the same for OpenAI 01 Pro and 03 Me.  
**Translation:** 

**[10889.46s] English:** Mini with the same prompt, the prompt being, give one truly novel insight about humans.  
**Translation:** 

**[10897.74s] English:** And I thought I would, in general, give my vibe check and vibe based anecdotal report on my own  
**Translation:** 

**[10907.46s] English:** experiences with the new 03 Mini model, now that I got a chance to spend many hours with it in  
**Translation:** Vocabulary: anecdotal: 零星经验

**[10913.10s] English:** different kinds of contexts and applications.  
**Translation:** 

**[10915.50s] English:** So I would probably categorize this question as, let's say, a very simple one.  
**Translation:** Vocabulary: categorize: 分类

**[10919.30s] English:** Let's say, open.  
**Translation:** 

**[10920.00s] English:** ended philosophical question. And in particular, the emphasis on novelty, I think is a nice way to  
**Translation:** Vocabulary: philosophical: 哲学的

**[10926.62s] English:** test one of the capabilities of the model, which is come up with something that makes you pause  
**Translation:** 

**[10932.96s] English:** and almost surprise you with its brilliance. So that said, my general review after running  
**Translation:** Vocabulary: brilliance: 卓越智慧

**[10940.00s] English:** each of the models on this question a bunch of times is that O1 Pro consistently gave brilliant  
**Translation:** 

**[10946.84s] English:** answers. Ones that gave me pause and made me think, both cutting in its insight and just  
**Translation:** 

**[10954.48s] English:** really nicely phrased with wit, with clarity, with nuance, over and over consistently generating the  
**Translation:** 

**[10961.86s] English:** best answers. After that is R1, which is less consistent, but again, delivered brilliance.  
**Translation:** Vocabulary: nuance: 细微差别

**[10968.80s] English:** Gemini Flash 2.0 Thinking was third. And last was O3 Mini, actually. It  
**Translation:** 

**[10976.44s] English:** often gave me pause and made me think, both cutting in its insight and just really nicely phrased.  
**Translation:** 

**[10976.82s] English:** It often gave quite a generic answer, at least to my particular sensibilities. That said,  
**Translation:** 

**[10981.88s] English:** in a bunch of other applications that I tested for brainstorming purposes, it actually worked  
**Translation:** Vocabulary: brainstorming: 头脑风暴; sensibilities: 感受

**[10988.58s] English:** extremely well and often outperformed R1. But on this open-ended philosophical question,  
**Translation:** 

**[10995.38s] English:** it did consistently worse. Now, another important element for each of these models is how the  
**Translation:** 

**[11001.26s] English:** reasoning is presented. DeepSeek R1 shows the full chain of thought tokens,  
**Translation:** 

**[11006.16s] English:** which I personally just love. For these open-ended philosophical questions, it's really,  
**Translation:** 

**[11011.82s] English:** really interesting to see the model think through it. But really, also, just stepping back,  
**Translation:** 

**[11017.08s] English:** me as a person who appreciates intelligence and reasoning and reflection,  
**Translation:** 

**[11022.16s] English:** reading these kind of chain of thought raw tokens of R1, there's something genuinely beautiful  
**Translation:** 

**[11027.70s] English:** about observing the path of deliberation in an intelligence system. I think we don't always  
**Translation:** Vocabulary: deliberation: 深思熟虑

**[11035.24s] English:** have that explicitly laid out for us humans. So to see it  
**Translation:** 

**[11040.00s] English:** in another intelligence system, the non-linearity of it, akin to Ulysses Finnegan's Wake by James  
**Translation:** Vocabulary: explicitly: 明确地; ulysses: 尤利西斯

**[11047.18s] English:** Joyce. It's just beautiful to watch. Anyway, as we discussed in the episode, DeepSeek R1 talked  
**Translation:** 

**[11053.90s] English:** about humans being able to convert selfish desires into cooperative systems by collectively pretending  
**Translation:** Vocabulary: cooperative: 合作的

**[11058.94s] English:** abstract rules like money, laws, and rights are real, and these shared hallucinations act as  
**Translation:** 

**[11064.98s] English:** games, where competition is secretly redirected to benefit the group, turning conflict into  
**Translation:** Vocabulary: hallucinations: 集体幻觉

**[11070.90s] English:** society's fuel. Gemini 2.0 Flash Thinking said, humans are not just social animals, but self-domesticated  
**Translation:** 

**[11078.16s] English:** apes, and this self-domestication is the key to understanding our unique cognitive and social  
**Translation:** Vocabulary: cognitive: 认知; gemini: 天蝎座

**[11083.62s] English:** abilities. Now, it's important to say that the chain of thought there was really interesting.  
**Translation:** 

**[11089.08s] English:** It was looking through the entire evolution of life on Earth, considering apex predators,  
**Translation:** Vocabulary: predators: 顶级捕食者

**[11094.98s] English:** and considering how, from that, we ended up to where we are. I think that domestication by  
**Translation:** 

**[11102.44s] English:** choice is a really interesting angle. Again, it's one of those things when somebody presents a  
**Translation:** 

**[11107.94s] English:** different angle on a seemingly obvious thing, it just makes me smile. And the same with DeepSeek  
**Translation:** 

**[11112.94s] English:** R1, that these hallucinations of money, laws, and rights, and us collectively pretending like it's  
**Translation:** 

**[11120.72s] English:** real, and we play games with them that look like competition when secretly,  
**Translation:** 

**[11124.98s] English:** we're just cooperating with each other. And that is the fuel of progress. Beautifully put.  
**Translation:** Vocabulary: cooperating: 互相配合

**[11131.02s] English:** Now, OpenAI 01 Pro consistently, over and over, delivered bangers. I can go through many of them,  
**Translation:** 

**[11137.24s] English:** but the first one was, humans are the only species that turns raw materials into symbolic resources,  
**Translation:** Vocabulary: symbolic: 符号化的

**[11142.94s] English:** then uses those symbols to reorganize the very materials they came from,  
**Translation:** 

**[11147.38s] English:** creating a closed feedback loop between meaning and matter. Here, I just ran it again.  
**Translation:** Vocabulary: reorganize: 重新组织

**[11154.98s] English:** Banger after banger, I'm telling you, humans are unique among known species in that they  
**Translation:** 

**[11159.68s] English:** simultaneously  
**Translation:** 

**[11160.00s] English:** Rewrite two layers of reality, the external world and their own private mental landscapes, and then merge these two rewritten layers into a continuous personal narrative that feels objectively true.  
**Translation:** 

**[11175.08s] English:** Feels true.  
**Translation:** Vocabulary: objectively: 客观地; rewritten: 重写

**[11177.28s] English:** This is poetry.  
**Translation:** 

**[11179.28s] English:** Okay.  
**Translation:** 

**[11179.86s] English:** And then O3 Mini High for me was smart, fast, actually, and kind of generic.  
**Translation:** 

**[11188.56s] English:** Never quite got there for me.  
**Translation:** 

**[11191.00s] English:** So here's the first one I got from O3 Mini.  
**Translation:** 

**[11218.56s] English:** Now, it almost sneaks up to something approximating cutting insight with narrative plasticity in quotes.  
**Translation:** Vocabulary: approximating: 接近

**[11227.08s] English:** But then it goes back to the sort of the generic.  
**Translation:** 

**[11229.98s] English:** I don't know.  
**Translation:** 

**[11230.64s] English:** All of these models are incredible for different reasons.  
**Translation:** 

**[11233.48s] English:** There's a lot of concerns, as we discussed in this episode, but there's a lot of reasons to be excited as well.  
**Translation:** 

**[11241.20s] English:** And I've probably spoken for too long.  
**Translation:** 

**[11243.56s] English:** I am severely sleep deprived.  
**Translation:** 

**[11247.40s] English:** Borderline delirious.  
**Translation:** 

**[11248.56s] English:** So hopefully some of this made sense.  
**Translation:** Vocabulary: borderline: 边缘的; delirious: 谵妄的

**[11251.66s] English:** And now, dear friends, back to the episode.  
**Translation:** 

**[11256.22s] English:** I think when you, you know, to Nathan's point, when you look at like the reasoning models, to me, even when I used R1 versus O1, there was like that sort of rough edges around the corner feeling.  
**Translation:** 

**[11270.72s] English:** Right.  
**Translation:** 

**[11271.18s] English:** And flash thinking, you know, earlier, I didn't use this version, but the one from December, and it definitely had that rough edges around the corner feeling.  
**Translation:** 

**[11278.38s] English:** Right.  
**Translation:** 

**[11278.56s] English:** Where it's just not flesh.  
**Translation:** 

**[11280.00s] English:** out in any as many ways right um sure they added math and coding capabilities via these verifiers  
**Translation:** 

**[11285.68s] English:** and rl but you know they it feels like they lost something in certain areas and o1 is worse  
**Translation:** Vocabulary: verifiers: 验证器

**[11291.08s] English:** performing than chat in many areas as well to be clear um not by a lot not by a lot though right  
**Translation:** 

**[11296.80s] English:** and it's like some like r1 definitely felt to me like it was worse than v3 in certain areas like  
**Translation:** 

**[11302.08s] English:** doing this rl expressed and learned a lot but then it weakened in other areas and so i think that's  
**Translation:** 

**[11308.34s] English:** one of the big differences between these models and the and and what o1 offers and then open ai  
**Translation:** Vocabulary: weakened: 变弱

**[11314.56s] English:** has o1 pro and what they did with o3 which is like also very unique is that they stacked search on  
**Translation:** 

**[11321.14s] English:** top of chain of thought right um and so chain of thought is one thing where it's able it's one  
**Translation:** 

**[11325.66s] English:** chain it backtracks goes back and forth but how they served solved the arc agi challenge was not  
**Translation:** 

**[11331.20s] English:** just the chain of thought it was also sampling many times i.e running them in parallel and then  
**Translation:** Vocabulary: backtracks: 倒退思考

**[11337.40s] English:** selecting is  
**Translation:** 

**[11338.26s] English:** right  
**Translation:** 

**[11338.32s] English:** running in parallel actually search because i i don't know if we have the full information on  
**Translation:** 

**[11342.26s] English:** how o1 pro works so like i'm not i don't have enough information to confidently say that it  
**Translation:** 

**[11346.60s] English:** is search it is parallel samples yeah and then it selects something and we don't know what the  
**Translation:** 

**[11351.10s] English:** selection function is the reason why we're debating is because since o1 was announced  
**Translation:** 

**[11356.06s] English:** there's been a lot of interest in techniques called monte carlo research which is where you  
**Translation:** 

**[11359.50s] English:** will break down the chain of thought into intermediate steps we haven't defined chain  
**Translation:** 

**[11363.64s] English:** of thought chain of thought is from a paper from years ago where you introduce the  
**Translation:** 

**[11368.24s] English:** idea to ask a language model that at the time was much less easy to use you would say let's verify  
**Translation:** Vocabulary: verify: 验证

**[11373.68s] English:** step by step and it would induce the model to do this bulleted list of steps chain of thought is now  
**Translation:** 

**[11379.68s] English:** almost a default in models where if you ask it a math question you don't need to tell it to think  
**Translation:** Vocabulary: bulleted: 列表项

**[11383.20s] English:** step by step and the idea with monte carlo tree search is that you would take an intermediate  
**Translation:** 

**[11388.72s] English:** point in that train do some sort of expansion spend more compute and then just select the right  
**Translation:** 

**[11393.20s] English:** one that's like a very complex form of search that has been used in things like mu zero and i'll be  
**Translation:** 

**[11398.16s] English:** talking about alpha zero potentially i know mu zero does  
**Translation:** Vocabulary: alpha: 阿尔法

**[11400.00s] English:** us another form of search is just asking five different people and then taking the majority  
**Translation:** 

**[11404.82s] English:** answer yes right there's a variety of like you know it could be complicated it could be simple  
**Translation:** 

**[11409.32s] English:** we don't know what it is just that they are they are not just issuing one chain of thought in  
**Translation:** 

**[11414.28s] English:** sequence they're launching many in parallel and in the arc agi they launched a thousand in parallel  
**Translation:** 

**[11420.32s] English:** for their uh the one that like really shocked everyone that beat the benchmark was they want  
**Translation:** 

**[11424.64s] English:** they would launch a thousand in parallel and then they would get the right answer like 80 percent of  
**Translation:** Vocabulary: benchmark: 标准

**[11428.48s] English:** the time or 70 percent of the time 90 maybe even uh whereas if they just launched one it was like  
**Translation:** 

**[11432.68s] English:** 30 percent there are many extensions to this i would say the simplest one is that our language  
**Translation:** Vocabulary: extensions: 扩展

**[11438.20s] English:** models to date have been designed to give the right answer the highest percentage of the time  
**Translation:** 

**[11443.16s] English:** in one response and we are now opening the door to different ways of running inference on our models  
**Translation:** Vocabulary: inference: 推断

**[11449.12s] English:** in which we need to reevaluate many parts of the training process which normally opens the door to  
**Translation:** 

**[11455.30s] English:** more progress but we don't know if open ai changed a lot  
**Translation:** Vocabulary: reevaluate: 重新评估

**[11458.32s] English:** or if just sampling more and multiple choice is what they're doing or if it's something more  
**Translation:** 

**[11462.44s] English:** complex but they change the training and they know that the inference mode is going to be different  
**Translation:** 

**[11467.24s] English:** so we're talking about 01 pro 200 a month and they're losing money so the thing that we're  
**Translation:** 

**[11475.96s] English:** referring to this fascinating exploration of the test time compute space is that actually possible  
**Translation:** 

**[11483.82s] English:** do we have enough compute for that does the financials make sense  
**Translation:** 

**[11488.32s] English:** the fantastic thing is in in there it's in the uh thing that i just pulled up earlier but uh the  
**Translation:** Vocabulary: financials: 财务状况

**[11493.96s] English:** cost for uh gpt3 has plummeted if you scroll up uh just a few images i think the important thing  
**Translation:** 

**[11501.06s] English:** about like hey is cost a limiting factor here right like my my view is that like we'll have  
**Translation:** Vocabulary: plummeted: 急剧下降; scroll: 滚动

**[11506.32s] English:** like really awesome intelligence before we have like agi before we have it permeate throughout  
**Translation:** 

**[11511.30s] English:** the economy um and this is sort of why that reason is right gpt3 was trained in what 2020 2021  
**Translation:** 

**[11516.36s] English:** um and  
**Translation:** 

**[11518.32s] English:** the cost for running inference on  
**Translation:** 

**[11520.00s] English:** was $60, $70 per million tokens, right?  
**Translation:** 

**[11524.14s] English:** Which is the cost per intelligence was ridiculous.  
**Translation:** 

**[11526.96s] English:** Now, as we scaled forward two years,  
**Translation:** 

**[11528.88s] English:** we've had a 1200x reduction in cost  
**Translation:** 

**[11531.80s] English:** to achieve the same level of intelligence as GPT-3.  
**Translation:** 

**[11534.76s] English:** So here on the x-axis is time over just a couple of years.  
**Translation:** 

**[11539.78s] English:** And on the y-axis is log scale dollars  
**Translation:** 

**[11543.66s] English:** to run inference on a million tokens.  
**Translation:** 

**[11547.36s] English:** And so you have just a down,  
**Translation:** 

**[11550.94s] English:** like a linear decline on log scale  
**Translation:** 

**[11553.86s] English:** from GPT-3 through 3.5 to LAMA.  
**Translation:** 

**[11557.44s] English:** It's like 5 cents or something like that now, right?  
**Translation:** 

**[11559.54s] English:** Which is versus $60, 1200x.  
**Translation:** 

**[11562.96s] English:** That's not the exact numbers, but it's 1200x.  
**Translation:** 

**[11565.06s] English:** I remember that number.  
**Translation:** 

**[11566.48s] English:** Is the humongous cost per intelligence, right?  
**Translation:** 

**[11570.16s] English:** Now, the freak out over DeepSeek is,  
**Translation:** 

**[11572.06s] English:** oh my God, they made it so cheap.  
**Translation:** 

**[11573.70s] English:** It's like, actually, if you look at this trend line,  
**Translation:** 

**[11575.90s] English:** they're not below the trend line.  
**Translation:** 

**[11577.18s] English:** First of all, and at least for GPT-3, right?  
**Translation:** 

**[11579.60s] English:** They are the first to hit it, right?  
**Translation:** 

**[11580.96s] English:** Which is a big deal.  
**Translation:** 

**[11582.28s] English:** But they're not below the trend line as far as GPT-3.  
**Translation:** 

**[11584.86s] English:** Now we have GPT-4.  
**Translation:** 

**[11586.02s] English:** What's going to happen with these reasoning capabilities, right?  
**Translation:** 

**[11588.34s] English:** It's a mix of architectural innovations.  
**Translation:** 

**[11590.42s] English:** It's a mix of better data.  
**Translation:** Vocabulary: architectural: 建筑相关的; innovations: 创新

**[11592.24s] English:** And it's going to be better training techniques  
**Translation:** 

**[11593.80s] English:** and all of these different better inference systems,  
**Translation:** Vocabulary: inference: 推断

**[11596.00s] English:** better hardware, right?  
**Translation:** 

**[11597.26s] English:** Going from each generation of GPU to new generations or ASICs.  
**Translation:** 

**[11602.32s] English:** Everything is going to take this cost curve  
**Translation:** 

**[11604.68s] English:** down and down and down and down.  
**Translation:** 

**[11606.22s] English:** And then Canada,  
**Translation:** 

**[11607.18s] English:** can I just spawn a thousand different LLMs  
**Translation:** Vocabulary: spawn: 繁殖

**[11610.66s] English:** to create a task and then pick from one of them  
**Translation:** 

**[11613.08s] English:** or whatever search technique I want,  
**Translation:** 

**[11615.34s] English:** a tree, Monte Carlo tree search.  
**Translation:** 

**[11617.02s] English:** Maybe it gets that complicated.  
**Translation:** Vocabulary: carlo: 卡洛; monte: 蒙特

**[11618.86s] English:** Maybe it doesn't because it's too complicated  
**Translation:** 

**[11620.28s] English:** to actually scale.  
**Translation:** 

**[11621.24s] English:** Like, who knows?  
**Translation:** 

**[11622.08s] English:** Bitter lesson, right?  
**Translation:** 

**[11623.38s] English:** The question is, I think, when, not if.  
**Translation:** 

**[11627.96s] English:** Because the rate of progress is so fast, right?  
**Translation:** 

**[11631.64s] English:** Nine months ago, Dario was saying,  
**Translation:** 

**[11633.64s] English:** or Dario said nine months ago,  
**Translation:** 

**[11635.22s] English:** the cost to train an inference was this.  
**Translation:** 

**[11637.18s] English:** Right?  
**Translation:** 

**[11637.80s] English:** And now we're much better than this, right?  
**Translation:** 

**[11640.00s] English:** and DeepSeek is much better than this. And that cost curve for GPT-4, which was also roughly $60  
**Translation:** 

**[11645.20s] English:** per million tokens when it launched, has already fallen to $2 or so, right? And we're going to get  
**Translation:** 

**[11651.80s] English:** it down to cents, probably, for GPT-4 quality. And then that's the base for the reasoning models  
**Translation:** 

**[11659.00s] English:** like O1 that we have today, and O1 Pro is spawning multiple, right? And O3 and so on and so forth.  
**Translation:** 

**[11664.60s] English:** These search techniques, too expensive today, but they will get cheaper. And that's what's  
**Translation:** 

**[11668.94s] English:** going to unlock the intelligence, right? So it'll get cheaper and cheaper and cheaper.  
**Translation:** 

**[11673.98s] English:** The big DeepSeek R1 release freaked everybody out because of the cheaper.  
**Translation:** 

**[11679.80s] English:** One of the manifestations of that is NVIDIA stock plummeted. Can you explain what happened?  
**Translation:** 

**[11686.10s] English:** I mean, and also just explain this moment and whether, you know, if NVIDIA is going to keep  
**Translation:** Vocabulary: manifestations: 表现; plummeted: 暴跌

**[11691.66s] English:** winning. We're both NVIDIA bulls here, I would say. And in some ways, the market response is  
**Translation:** 

**[11698.60s] English:** reasonable.  
**Translation:** 

**[11698.94s] English:** Most of the market, like NVIDIA's biggest customers in the US are major tech companies,  
**Translation:** 

**[11704.82s] English:** and they're spending a ton on AI. And if a simple interpretation of DeepSeek is you can get really  
**Translation:** 

**[11710.58s] English:** good models without spending as much on AI. So in that capacity, it's like, oh, maybe these big tech  
**Translation:** 

**[11715.90s] English:** companies won't need to spend as much on AI and go down. The actual thing that happened, it's much  
**Translation:** 

**[11719.94s] English:** more complex where there's social factors, where there's the rising in the app store, the social  
**Translation:** 

**[11724.82s] English:** contagion that is happening. And then I think a lot of some of it is just like, I'm not,  
**Translation:** Vocabulary: contagion: 传染

**[11728.94s] English:** I don't trade, I don't know anything about financial markets, but it builds up over the  
**Translation:** 

**[11731.76s] English:** weekend or the social pressure, where it's like, if it was during the week, and there was multiple  
**Translation:** 

**[11735.66s] English:** days of trading when this was really becoming, but it comes on the weekend, and then everybody  
**Translation:** 

**[11739.58s] English:** wants to sell. And that is a social contagion. I think I think and like, there are a lot of  
**Translation:** 

**[11744.92s] English:** false narratives, which is like, hey, these guys are spending billions on models, right? And they're  
**Translation:** 

**[11749.24s] English:** not spending billions on models, no one spent more than a billion dollars on a model that's  
**Translation:** 

**[11753.56s] English:** released publicly, right? GPT-4 was a couple hundred million. And then, you know, they've  
**Translation:** 

**[11758.60s] English:** reduced the cost with for a  
**Translation:** 

**[11760.00s] English:** for turbo for all right um but billion dollar model runs are coming right um this concludes  
**Translation:** 

**[11765.76s] English:** pre-training and post-training right and then the other number is like hey deep seek didn't include  
**Translation:** Vocabulary: turbo: 涡轮增压

**[11769.06s] English:** everything right they didn't include you know a lot of the cost goes to research and all this sort  
**Translation:** 

**[11772.28s] English:** of stuff a lot of the cost goes to inference a lot of cost goes to post-training none of these  
**Translation:** Vocabulary: inference: 推断

**[11775.94s] English:** things were factored research salaries right like all these things are like counted in the billions  
**Translation:** 

**[11780.40s] English:** of dollars that open ai is spending but they weren't counted in the you know hey six million  
**Translation:** Vocabulary: factored: 考虑进去; salaries: 工资

**[11784.54s] English:** five million dollars that deep seek spent right so but so there's a bit of misunderstanding of  
**Translation:** 

**[11788.40s] English:** what these numbers are um and then there's also an element of nvidia has just been a straight line  
**Translation:** 

**[11794.00s] English:** up right and and there's been so many different narratives that have been trying to push down  
**Translation:** 

**[11798.94s] English:** nvidia not i don't say push down nvidia stock everyone is looking for a reason to sell or to  
**Translation:** 

**[11803.28s] English:** be worried right um you know it was it was blackwell delays right their gpu was you know  
**Translation:** 

**[11808.26s] English:** there's a lot of report every two weeks there's a new report about their gpus being delayed um  
**Translation:** Vocabulary: blackwell: 布莱克威尔

**[11811.96s] English:** there's um there's the whole thing about scaling laws ending right it's so it's so ironic right  
**Translation:** 

**[11817.80s] English:** it lasted a month  
**Translation:** 

**[11818.40s] English:** it was it was just it was just like literally just hey models aren't getting better right  
**Translation:** 

**[11823.70s] English:** they're just not getting better there's no reason to spend more pre-training scaling is dead  
**Translation:** 

**[11827.48s] English:** and then it's like oh one oh three right r1 r1 right and now it's like wait models are getting  
**Translation:** 

**[11833.56s] English:** too they're progressing too fast slow down the progress stop spending on gpus right but you know  
**Translation:** Vocabulary: progressing: 快速发展

**[11838.84s] English:** the funniest thing i think that like comes out of this is javon's paradox is true right aws pricing  
**Translation:** 

**[11845.08s] English:** for h100s has gone up over the last couple weeks right since  
**Translation:** 

**[11848.40s] English:** since since since a little bit after christmas since v3 was launched aws h100 pricing has gone  
**Translation:** 

**[11853.94s] English:** up h200s are like almost out of stock everywhere because it you know h200 has more memory and  
**Translation:** Vocabulary: christmas: 圣诞节

**[11859.58s] English:** therefore r1 like you know wants that chip over h100 right we were trying to get gpus on a short  
**Translation:** 

**[11864.42s] English:** notice this week for a demo and it wasn't that easy we were trying to get just like 16 or 32  
**Translation:** 

**[11868.20s] English:** h100s for demo and it was not very easy so for people who don't know javon's paradox is uh  
**Translation:** 

**[11874.46s] English:** when uh you know the efficiency goes up  
**Translation:** 

**[11878.40s] English:** how magically conor  
**Translation:** 

**[11880.00s] English:** intuitively the total resource consumption goes up as well right and semiconductors is you know  
**Translation:** Vocabulary: intuitively: 直觉上; semiconductors: 半导体

**[11884.74s] English:** we're at 50 years of moore's law every two years half the cost double the transistors just like  
**Translation:** 

**[11890.18s] English:** clockwork and it's slowed down obviously but like the semiconductor industry has gone up the whole  
**Translation:** Vocabulary: clockwork: 机械装置; semiconductor: 半导体; transistors: 晶体管

**[11894.64s] English:** time right it's been wavy right there's obviously cycles and stuff and i don't expect ai to be any  
**Translation:** 

**[11898.96s] English:** different right there's going to be ebbs and flows but this is an ai it's just playing out  
**Translation:** 

**[11903.34s] English:** at an insane time scale right it was 2x every two years this is 1200x in like three years right so  
**Translation:** 

**[11909.98s] English:** it's like the scale of improvement that is like hard to get wrap your head around yeah i was  
**Translation:** 

**[11915.18s] English:** confused because i to me nvidia stock on that should have gone up but maybe it went down because  
**Translation:** 

**[11921.50s] English:** there's kind of suspicion of foul play on the side of china or something like this but if you just  
**Translation:** 

**[11926.40s] English:** look purely at the actual principles of play here like it's obvious yeah the javon's paradox that  
**Translation:** 

**[11933.02s] English:** ai makes or the higher the derivative of ai progress is especially you should because nvidia  
**Translation:** 

**[11939.28s] English:** is in the best place  
**Translation:** 

**[11939.96s] English:** the higher the derivative is the sooner the market's going to be bigger and expanding and  
**Translation:** Vocabulary: derivative: 导数

**[11943.94s] English:** nvidia is the only one that does everything reliably right now because it's not like an  
**Translation:** 

**[11948.36s] English:** nvidia competitor arose it's it's another company that's using nvidia who historically has been a  
**Translation:** Vocabulary: historically: 历史上; reliably: 可靠地

**[11955.82s] English:** large nvidia customer yeah and has press releases about them cheering about being china's biggest  
**Translation:** 

**[11961.52s] English:** nvidia customer right like yeah i mean it made obviously they've quieted down but like i think  
**Translation:** 

**[11967.08s] English:** that's like another element of is that they don't want to say how many gpus do they have  
**Translation:** 

**[11969.96s] English:** yeah because hey they yes they have h800s yes they have h20s they also have some h100s right which  
**Translation:** 

**[11976.98s] English:** can you speak to that to the smuggling what's the scale of smuggling that's feasible for a nation  
**Translation:** 

**[11983.34s] English:** state to do for companies is it possible to i think i think there's a few angles of smuggling  
**Translation:** 

**[11989.28s] English:** here right one is bite dance arguably is the largest smuggler of gpus for china right china's  
**Translation:** 

**[11994.58s] English:** not supposed to have gpus bite dance has like over 500 000 gpus why because they're all rented from  
**Translation:** Vocabulary: arguably: 可以说; smuggler: 走私者

**[11999.96s] English:** people and they're oiled and all kind of stuff but those countries are still pretty far away  
**Translation:** 

**[12002.50s] English:** and so it's hard to see how much of a difference it makes so i think it's possible to make an  
**Translation:** 

**[12019.00s] English:** improvement because the more you get more sales you're just going to get more business in the  
**Translation:** 

**[12023.42s] English:** future but i think it's possible to make a difference because there's still a lot of  
**Translation:** 

**[12027.86s] English:** competition going on right now i think the other thing that's of interest i think the one that's  
**Translation:** 

**[12029.82s] English:** really interesting is the way that theirler is designed and developed is that it's not all the other  
**Translation:** Vocabulary: theirler: 他们的产品

**[12029.90s] English:** technology is being sold it's just not being sold the technology the only technology that's being game and  
**Translation:** 

**[12000.00s] English:** companies around the world they rent from oracle they rent from google they rent from all these  
**Translation:** 

**[12004.46s] English:** mass and and a bunch of smaller cloud companies too right all the neo clouds right of the world  
**Translation:** 

**[12008.26s] English:** they rent so so many gps they also buy a bunch right and and they do this for mostly like what  
**Translation:** 

**[12013.74s] English:** meta does right serving tiktok right serving next best discussion to be clear that's today the view  
**Translation:** 

**[12020.60s] English:** use right and it's a valid use right hack the dopamine circuit right um now that's that's  
**Translation:** Vocabulary: dopamine: 多巴胺

**[12026.74s] English:** theoretically now very much restricted with the ai diffusion rules which happened in the last week  
**Translation:** 

**[12031.30s] English:** of the biden admin and uh trump admin looks like they're going to keep them which limits like  
**Translation:** Vocabulary: admin: 行政; theoretically: 理论上

**[12036.52s] English:** allies even like singapore um which singapore is like 20 percent of nvidia's 20 20 30 percent of  
**Translation:** 

**[12041.88s] English:** nvidia's revenue but uh singapore's had a memorandum on not building data centers for like 15 years  
**Translation:** Vocabulary: memorandum: 备忘录

**[12046.86s] English:** because they don't have enough power so where are they going i mean i'm not claiming they're all  
**Translation:** 

**[12051.92s] English:** going to china right but a portion are you know many are going to malaysia um including microsoft  
**Translation:** Vocabulary: malaysia: 马来西亚

**[12056.18s] English:** and oracle  
**Translation:** 

**[12056.62s] English:** have big data centers in malaysia like you know all they're going all over southeast asia probably  
**Translation:** 

**[12060.56s] English:** india as well right like there's stuff routing but like the diffusion rules are very de facto like  
**Translation:** 

**[12065.70s] English:** you can only buy this many gpus from this country and it's and you can only rent a cluster this  
**Translation:** Vocabulary: cluster: 计算集群; facto: 事实上; routing: 路由

**[12070.64s] English:** large to companies that are chinese right like they're very explicit on trying to stop smuggling  
**Translation:** 

**[12075.56s] English:** right and a big chunk of it was hey let's let's you know random company by 16 servers  
**Translation:** Vocabulary: explicit: 明确; smuggling: 走私

**[12080.06s] English:** ship them to uh to china right um there's actually i saw a photo from someone uh  
**Translation:** 

**[12086.62s] English:** in the semiconductor industry is an isn't who leads like a a team for like networking chips  
**Translation:** Vocabulary: semiconductor: 半导体

**[12092.00s] English:** uh that competes with nvidia and he sent a photo of a guy checking into a first class united flight  
**Translation:** 

**[12097.50s] English:** from san francisco to shanghai or shenzhen with a super micro box that was this big which can only  
**Translation:** Vocabulary: competes: 竞争; shanghai: 上海; shenzhen: 深圳

**[12104.70s] English:** contain gpus right and he was booking first class because think about it three to five k for your  
**Translation:** 

**[12109.70s] English:** first class ticket server cost you know 240 000 in the us 250 000 you sell it for 300 000 in china  
**Translation:** 

**[12116.62s] English:** you just got a free first class ticket and a lot more money  
**Translation:** 

**[12120.00s] English:** So it's like, you know, and that's like small scale smuggling. Most of the large scale smuggling is like companies in Singapore and Malaysia, like routing them around or renting GPUs completely legally.  
**Translation:** 

**[12129.92s] English:** I want to jump in. How much is the scale? I think there's been some number, like some people that are higher level economics understanding say that as you go from 1 billion of smuggling to 10 billion, it's like you're hiding certain levels of economic activity. And that's the most reasonable thing to me is that there's going to be some level where it's so obvious that it's easier to find this economic activity.  
**Translation:** 

**[12149.20s] English:** And yeah, so my belief is that last year, roughly, so NVIDIA made a million H20s, which are legally allowed to be shipped to China, which we talked about is better for reasoning, right? Inference, at least, not maybe not training, but reasoning inference, and inference generally, then they also had, you know, a couple hundred thousand, we think like 200 to 300,000 GPUs were routed to China from, you know, Singapore, Malaysia, US, wherever companies spawn up by 16 GPUs, 64 GPUs, whatever.  
**Translation:** Vocabulary: inference: 推断; routed: 路由; spawn: 滋生

**[12179.20s] English:** And Huawei is known for having spent up a massive network of like, companies to get the materials they need after they were banned in like 2018. So it's not like otherworldly. But I agree, right? Nathan's point is like, hey, you can't smuggle up $10 billion of GPUs. And then the third sort of source, which is just now banned, and you know, which wasn't considered smuggling, but is China is renting like, is I believe from our research, right? Oracle's biggest GPU customer is ByteDance, right? And for Google, I think it's their second biggest customer.  
**Translation:** 

**[12209.20s] English:** Right. And so like, and you go down the list of clouds, and especially these smaller cloud companies that aren't like the hyperscalers, right? Think beyond Core, even Lambda, even there's a whole sea, there's 60 different new cloud companies serving NVIDIA GPUs. I think ByteDance is renting a lot of these, right? All over, right? And so these companies are renting GPUs to Chinese companies. And that's completely, that was completely legal, up until the diffusion rules, which happened just a few weeks ago. And even now, you can rent GPU clusters that are less than 2000 GPUs, or you can buy GPUs,  
**Translation:** Vocabulary: clusters: GPU集群; diffusion: 扩散; hyperscalers: 超大规模; lambda: Lambda函数; smuggle: 走私; smuggling: 走私

**[12239.20s] English:** and  
**Translation:** 

**[12240.00s] English:** ship them wherever you want if you're if they're less than 1500 gpus right so it's like there are  
**Translation:** 

**[12244.32s] English:** still like some ways to smuggle but yeah it's not you know as the numbers grow right uh you know  
**Translation:** 

**[12249.84s] English:** 100 something billion dollars of revenue for nvidia last year 200 something billion this year  
**Translation:** 

**[12253.80s] English:** right and if next year are you know it could it could nearly double again or more than double  
**Translation:** 

**[12258.98s] English:** right based on like what we see with data center footprints like being built out all across the  
**Translation:** Vocabulary: footprints: 数据中心规模

**[12263.02s] English:** u.s and the rest of the world it's going to be really hard for china to keep up with these rules  
**Translation:** 

**[12267.60s] English:** right yes there will always be smuggling um and deep seek level models of gpd4 level models  
**Translation:** 

**[12272.98s] English:** uh oh one level models capable to train on what china can get even the next year above that but  
**Translation:** 

**[12278.30s] English:** if we speed run a couple more you know jumps right you know to billion dollar models 10 billion  
**Translation:** 

**[12284.34s] English:** dollar models then it becomes you know hey there is a compute disadvantage for china for training  
**Translation:** 

**[12288.66s] English:** models and serving them and and the serving part is really critical right deep seek cannot serve  
**Translation:** Vocabulary: cannot: 不能

**[12293.26s] English:** their model today right it's it's completely out of inventory uh it's already started  
**Translation:** 

**[12297.52s] English:** for the next year right so it's going to be really hard for china to keep up with these  
**Translation:** 

**[12297.58s] English:** falling in the app store actually downloads because you download it you try and sign up  
**Translation:** 

**[12301.52s] English:** they say we're not taking registrations because they have no capacity right you open it up you  
**Translation:** Vocabulary: registrations: 注册

**[12304.78s] English:** get like less than five tokens per second if you even get your request approved right because  
**Translation:** 

**[12308.78s] English:** there's just no capacity because they just don't have enough gpus to serve the model even though  
**Translation:** 

**[12312.94s] English:** it's incredibly efficient it would be fascinating to watch the smuggling because i mean there's drug  
**Translation:** 

**[12317.98s] English:** smuggling right that's a that's a market there's weapons smuggling and gpus will surpass that at  
**Translation:** Vocabulary: surpass: 超越

**[12325.44s] English:** their highest value per kilogram  
**Translation:** 

**[12327.50s] English:** probably by far um i have another question for you don't do track uh model api access  
**Translation:** 

**[12335.66s] English:** internationally how how easy is it for chinese companies to use hosted model apis from the u.s  
**Translation:** 

**[12341.32s] English:** yeah i mean that's incredibly easy right like open ai publicly stated deep seek uses their api  
**Translation:** 

**[12346.46s] English:** and as they say they have evidence right and this is this is another element of the training regime  
**Translation:** 

**[12350.66s] English:** is people at open ai have claimed that it's a distilled model i.e you're taking open ai's model  
**Translation:** Vocabulary: distilled: 提炼模型

**[12356.12s] English:** you're generating a lot of output you're generating a lot of output you're generating a lot of output  
**Translation:** 

**[12357.50s] English:** and then you're training on the output in their model  
**Translation:** 

**[12360.00s] English:** And even if that's the case, what they did is still amazing, by the way, what DeepSeq did efficiency-wise.  
**Translation:** 

**[12364.44s] English:** Distillation is standard practice in industry, whether or not—if you're at a closed lab where you care about terms of service and IP closely, you distill from your own models.  
**Translation:** Vocabulary: distill: 提纯; distillation: 提纯过程

**[12372.12s] English:** If you are a researcher and you're not building any products, you distill from the opening eye models.  
**Translation:** 

**[12376.54s] English:** This is a good opportunity.  
**Translation:** 

**[12377.72s] English:** Can you explain big-picture distillation as a process?  
**Translation:** 

**[12381.80s] English:** What is distillation?  
**Translation:** 

**[12383.00s] English:** What's the process of distillation?  
**Translation:** 

**[12383.78s] English:** We've talked a lot about training language models.  
**Translation:** 

**[12386.14s] English:** They are trained on text.  
**Translation:** 

**[12387.22s] English:** In post-training, you're trying to train on very high-quality text that you want the model to match the features of, or if you're using RL, you're letting the model find its own thing.  
**Translation:** 

**[12396.06s] English:** But for supervised fine-tuning, for preference data, you need to have some completions what the model is trying to learn to imitate.  
**Translation:** 

**[12402.96s] English:** And what you do there is instead of a human data or instead of the model you're currently training, you take completions from a different, normally more powerful model.  
**Translation:** Vocabulary: completions: 补充内容; supervised: 监督

**[12412.68s] English:** I think there's rumors that these big models that people are waiting for.  
**Translation:** 

**[12417.22s] English:** These GPT-5s of the world, the CLAWD-3 opuses of the world, are used internally to do this distillation process at OpenAI.  
**Translation:** Vocabulary: internally: 内部; opuses: 作品

**[12424.50s] English:** There's also public examples, right?  
**Translation:** 

**[12426.06s] English:** Like Meta explicitly stated, not necessarily distilling, but they used 405B as a reward model for 70B in their LAMA 3.2 and 3.3.  
**Translation:** Vocabulary: explicitly: 明确地

**[12435.10s] English:** This is all the same topic.  
**Translation:** 

**[12436.70s] English:** So is this ethical?  
**Translation:** 

**[12439.66s] English:** Is this legal?  
**Translation:** 

**[12440.36s] English:** Why is that Financial Times article headline, say, OpenAI says that?  
**Translation:** 

**[12446.70s] English:** There's evidence that China's deep-seek used its model to train competitor.  
**Translation:** 

**[12451.54s] English:** This is a long, at least in the academic side and research side, it's a long history because you're trying to interpret OpenAI's rule.  
**Translation:** Vocabulary: interpret: 解释

**[12457.94s] English:** OpenAI's terms of service say that you cannot build a competitor with outputs from their model.  
**Translation:** 

**[12463.26s] English:** Terms of service are different than a license, which are essentially a contract between organizations.  
**Translation:** 

**[12467.94s] English:** So if you have a terms of service on OpenAI's account, if I violate it, OpenAI can cancel my account.  
**Translation:** 

**[12472.98s] English:** This is very different than a license that says how you could use a downstream artifact.  
**Translation:** Vocabulary: artifact: 下游产物

**[12476.70s] English:** So a lot of it hinges on a word that is very unclear in the AI space.  
**Translation:** 

**[12480.00s] English:** which is what is a competitor.  
**Translation:** Vocabulary: hinges: 取决于

**[12481.60s] English:** And then the ethical aspect of it is like,  
**Translation:** 

**[12484.52s] English:** why is it unethical for me to train on your model  
**Translation:** Vocabulary: unethical: 不合伦理

**[12487.04s] English:** when you can train on the internet's text?  
**Translation:** 

**[12489.14s] English:** Yeah.  
**Translation:** 

**[12489.52s] English:** Right?  
**Translation:** 

**[12489.98s] English:** So there's a bit of a hypocrisy  
**Translation:** Vocabulary: hypocrisy: 虚伪

**[12491.70s] English:** because sort of OpenAI  
**Translation:** 

**[12494.02s] English:** and potentially most of the companies  
**Translation:** 

**[12496.86s] English:** trained on the internet's text without permission.  
**Translation:** 

**[12500.20s] English:** There's also a clear loophole,  
**Translation:** Vocabulary: loophole: 漏洞

**[12501.44s] English:** which is that I generate data from OpenAI  
**Translation:** 

**[12504.74s] English:** and then I upload it somewhere  
**Translation:** 

**[12506.72s] English:** and then somebody else trains on it  
**Translation:** 

**[12508.38s] English:** and the link has been broken.  
**Translation:** 

**[12510.00s] English:** Like they're not under the same terms of service contract.  
**Translation:** 

**[12513.10s] English:** This is why...  
**Translation:** 

**[12513.76s] English:** There's a lot of hip hop.  
**Translation:** 

**[12514.80s] English:** There's a lot of like to be discovered details  
**Translation:** 

**[12517.24s] English:** that don't make a lot of sense.  
**Translation:** 

**[12518.52s] English:** This is why a lot of models today,  
**Translation:** 

**[12520.54s] English:** even if they train on zero OpenAI data,  
**Translation:** 

**[12522.92s] English:** you ask the model who trained you,  
**Translation:** 

**[12524.82s] English:** it'll say, I am Chad GPT trained by OpenAI  
**Translation:** 

**[12527.10s] English:** because there's so much copy paste  
**Translation:** 

**[12529.28s] English:** of like OpenAI outputs from that on the internet  
**Translation:** 

**[12532.02s] English:** that you just weren't able to filter it out.  
**Translation:** 

**[12533.76s] English:** And there was nothing in the URL  
**Translation:** 

**[12535.38s] English:** where they implemented like,  
**Translation:** 

**[12537.04s] English:** hey, like, or post-training or SFT,  
**Translation:** 

**[12539.04s] English:** whatever that says,  
**Translation:** 

**[12539.84s] English:** hey,  
**Translation:** 

**[12540.00s] English:** I'm actually a model by Allen Institute  
**Translation:** 

**[12542.52s] English:** instead of OpenAI.  
**Translation:** 

**[12543.70s] English:** We have to do this if we serve a demo.  
**Translation:** 

**[12545.60s] English:** We do research and we use OpenAI APIs  
**Translation:** 

**[12548.08s] English:** because it's useful  
**Translation:** 

**[12548.80s] English:** and we want to understand post-training  
**Translation:** 

**[12550.28s] English:** and like our research models,  
**Translation:** 

**[12552.08s] English:** they will say they're written by OpenAI  
**Translation:** 

**[12553.56s] English:** unless we put in the system prop  
**Translation:** 

**[12555.22s] English:** that we talked about that like,  
**Translation:** 

**[12556.34s] English:** I am Tulu.  
**Translation:** 

**[12557.04s] English:** I am a language model trained  
**Translation:** 

**[12558.20s] English:** by the Allen Institute for AI.  
**Translation:** 

**[12559.92s] English:** And if you ask more people around industry,  
**Translation:** 

**[12562.48s] English:** especially with post-training,  
**Translation:** 

**[12563.64s] English:** it's a very doable task  
**Translation:** 

**[12565.28s] English:** to make the model say who it is  
**Translation:** Vocabulary: doable: 可实现的

**[12567.54s] English:** or to suppress the OpenAI thing.  
**Translation:** 

**[12569.30s] English:** So in some levels,  
**Translation:** Vocabulary: suppress: 压制

**[12570.98s] English:** it might be that DeepSeq didn't care  
**Translation:** 

**[12572.82s] English:** that it was saying that it was by OpenAI.  
**Translation:** 

**[12574.72s] English:** Like if you're going to upload model weights,  
**Translation:** 

**[12576.54s] English:** it doesn't really matter  
**Translation:** 

**[12577.22s] English:** because anyone that's serving it in an application  
**Translation:** 

**[12579.46s] English:** and cares a lot about serving  
**Translation:** 

**[12581.22s] English:** is going to,  
**Translation:** 

**[12582.44s] English:** when serving it,  
**Translation:** 

**[12583.48s] English:** if they're using it for a specific task,  
**Translation:** 

**[12585.24s] English:** they're going to tailor it to that.  
**Translation:** 

**[12586.26s] English:** And it doesn't matter  
**Translation:** 

**[12586.84s] English:** that it's saying it's ChatGPT.  
**Translation:** 

**[12588.94s] English:** Oh, I guess one of the ways to do that  
**Translation:** 

**[12590.86s] English:** is like a system prompt or something like that.  
**Translation:** 

**[12592.66s] English:** Like if you're serving it to say that you're...  
**Translation:** 

**[12595.08s] English:** That's what we do.  
**Translation:** 

**[12596.08s] English:** Like if we host the demo,  
**Translation:** 

**[12596.92s] English:** you say you are Tulu 3,  
**Translation:** 

**[12599.30s] English:** a language model...  
**Translation:** 

**[12600.00s] English:** model trained by the allen institute for ai we also are benefited from open ai data because it's  
**Translation:** Vocabulary: benefited: 受益

**[12605.26s] English:** a great research tool i mean do you think there's any any truth and value to the the claim open  
**Translation:** 

**[12612.46s] English:** ai's claim that there's evidence that china's deep seek used this model to train i think  
**Translation:** 

**[12616.56s] English:** everyone has benefited regardless because the data is on the internet um and therefore it's in  
**Translation:** 

**[12622.90s] English:** your portraying now right there are like subreddits where people share the best chat gpt outputs and  
**Translation:** Vocabulary: portraying: 展示; subreddits: 讨论版

**[12627.52s] English:** those are those are in your i think that they're trying to ship the narrative like they're trying  
**Translation:** 

**[12632.50s] English:** to protect themselves and we saw this years ago when bite dance was actually banned from some  
**Translation:** 

**[12637.04s] English:** open ai apis for training on outputs there's other ai startups that most people if you're in the like  
**Translation:** 

**[12643.10s] English:** ai culture were like they just told us they trained on open ai outputs and they never got  
**Translation:** Vocabulary: startups: 初创公司

**[12647.74s] English:** banned like that's how they bootstrapped their early models so it's much easier to get off the  
**Translation:** 

**[12652.42s] English:** ground using this than to set up human pipelines and build a strong model so there's a long history  
**Translation:** Vocabulary: bootstrapped: 自我提升; pipelines: 数据管道

**[12657.50s] English:** here and a lot of the communications are seem like narrative actually like the over the last  
**Translation:** 

**[12662.04s] English:** couple days we've seen a lot of people distill deep seeks model into llama model because the  
**Translation:** Vocabulary: distill: 提炼; llama: 羊驼

**[12667.32s] English:** deep seek models are kind of complicated to run inference on because they're mixture of experts  
**Translation:** 

**[12671.18s] English:** and they're you know 600 plus billion parameters and all this and people distilled them into the  
**Translation:** Vocabulary: distilled: 提炼; inference: 推断

**[12675.62s] English:** llama models and then because the llama models are so easy to serve and everyone's built the  
**Translation:** 

**[12679.28s] English:** pipelines and tooling for inference with the llama models right because it's the open standard  
**Translation:** 

**[12683.18s] English:** uh so you know we've seen it we've seen a sort of roundabout right like is it is it  
**Translation:** 

**[12687.50s] English:** bad is it illegal maybe it's illegal whatever i don't know about that but like it could break  
**Translation:** 

**[12691.52s] English:** contracts i don't think it's illegal like in any legal like no one's going to jail for this  
**Translation:** 

**[12695.54s] English:** i i think like fundamentally i think it's ethical or i hope it's ethical because like the moment  
**Translation:** Vocabulary: fundamentally: 从根本上

**[12701.48s] English:** becomes we ban that kind of thing it's going to make everybody much worse off and i also actually  
**Translation:** 

**[12709.46s] English:** it's it's this is difficult but i think you should be allowed to train on the internet I  
**Translation:** 

**[12715.34s] English:** know a lot of authors and creators are very sensitive  
**Translation:** 

**[12717.50s] English:** about it that's that's a difficult question but  
**Translation:** 

**[12720.00s] English:** The moment you're not allowed to train on the internet.  
**Translation:** 

**[12723.22s] English:** I agree.  
**Translation:** 

**[12723.80s] English:** I have a schizo take on how you can solve this because it already works.  
**Translation:** 

**[12727.18s] English:** I have a reasonable take on it.  
**Translation:** Vocabulary: schizo: 精神分裂的

**[12728.92s] English:** All right.  
**Translation:** 

**[12729.90s] English:** So, you know, Japan has a law which you're allowed to train on any training data and  
**Translation:** 

**[12735.80s] English:** copyrights don't apply if you want to train a model.  
**Translation:** 

**[12737.84s] English:** A. B. Japan has nine gigawatts of curtailed nuclear power.  
**Translation:** Vocabulary: copyrights: 著作权; curtailed: 削减; gigawatts: 吉瓦

**[12743.04s] English:** C. Japan is allowed under the AI diffusion rule to import as many GPUs as they'd like.  
**Translation:** 

**[12748.32s] English:** Like, so all we have to do, we have a market here to make.  
**Translation:** Vocabulary: diffusion: 扩散

**[12751.08s] English:** We build massive data centers.  
**Translation:** 

**[12752.74s] English:** We rent them to the labs.  
**Translation:** 

**[12754.30s] English:** And then we train models in a legally permissible way.  
**Translation:** 

**[12757.14s] English:** And there's no ifs, ands, or buts.  
**Translation:** Vocabulary: permissible: 允许的

**[12758.72s] English:** And now the models have no, like, potential copyright lawsuit from New York Times or anything  
**Translation:** 

**[12763.92s] English:** like that.  
**Translation:** 

**[12764.34s] English:** No, no.  
**Translation:** 

**[12764.56s] English:** It's just, like, completely legal.  
**Translation:** 

**[12765.84s] English:** No, so, so, so.  
**Translation:** 

**[12767.78s] English:** The early copyright lawsuits have fallen in the favor of AI training.  
**Translation:** Vocabulary: lawsuits: 诉讼

**[12771.62s] English:** I would say that the long tail of use is going to go in the side of AI, which is if you do  
**Translation:** 

**[12778.02s] English:** this.  
**Translation:** 

**[12778.32s] English:** If you scrape trillions of data, you're not looking at the trillions of tokens of data.  
**Translation:** 

**[12782.18s] English:** You're not looking and saying, this one New York Times article is so important to me.  
**Translation:** Vocabulary: scrape: 抓取; trillions: 万亿

**[12786.82s] English:** But if you're doing a audio generation for music or image generation, and you say, make  
**Translation:** 

**[12791.04s] English:** it in the style of X person, that's a reasonable case where you could figure out what is their  
**Translation:** 

**[12795.78s] English:** profit margin on inference.  
**Translation:** 

**[12798.20s] English:** I don't know if it's going to be the 50-50 of YouTube creator program or something, but  
**Translation:** Vocabulary: inference: 推断

**[12802.46s] English:** I would opt into that program as a writer.  
**Translation:** 

**[12804.94s] English:** Like, please, like, like that.  
**Translation:** 

**[12806.96s] English:** It's just, it's.  
**Translation:** 

**[12808.32s] English:** It's going to be a rough journey, but there will be some solutions like that that make  
**Translation:** 

**[12812.26s] English:** sense.  
**Translation:** 

**[12812.66s] English:** But there's a long tail where it's just on the internet.  
**Translation:** 

**[12815.94s] English:** I think one of the other aspects of that Financial Times article implied, and so that leads to  
**Translation:** 

**[12821.98s] English:** a more general question.  
**Translation:** 

**[12822.96s] English:** Do you think there's, how difficult is spying, espionage, and stealing of actual secret code  
**Translation:** 

**[12831.20s] English:** and data from inside companies?  
**Translation:** Vocabulary: espionage: 间谍活动

**[12833.76s] English:** How much of that is being attempted?  
**Translation:** 

**[12835.24s] English:** Code and data is hard, but ideas is easy.  
**Translation:** 

**[12837.42s] English:** Silicon Valley.  
**Translation:** 

**[12838.32s] English:** Silicon Valley operates on the.  
**Translation:** 

**[12840.00s] English:** the way that top employees get bought out by other companies for a pay raise and a large reason why  
**Translation:** 

**[12846.16s] English:** these companies do this is to bring ideas with them and there are there's no i mean in california  
**Translation:** Vocabulary: california: 加利福尼亚

**[12851.36s] English:** there's rules like certain like non-competes or whatever are illegal in california and whether  
**Translation:** 

**[12856.24s] English:** or not there's ndas and things that is how a lot of it process happens recently there was somebody  
**Translation:** 

**[12861.44s] English:** from gemini who helped make this one million contacts length and everyone is saying the next  
**Translation:** 

**[12866.80s] English:** llama who i mean he went to the meta team is gonna have one million contacts length and that's kind  
**Translation:** Vocabulary: gemini: 双子座; llama: llama

**[12872.48s] English:** of how the world works you know as far as like industrial espionage and things that has been  
**Translation:** 

**[12877.76s] English:** greatly successful in the past right um you know the americans did the brits  
**Translation:** Vocabulary: brits: 英国人

**[12882.24s] English:** uh the chinese have done it to the americans right and you know so on and so forth it's just  
**Translation:** 

**[12886.16s] English:** it is a fact of life um and so like to argue industrial espionage can be stopped is probably  
**Translation:** 

**[12893.20s] English:** unlikely you can make it difficult but even then like there's all these stories about like  
**Translation:** 

**[12896.80s] English:** hey f35 and f22 have already been like sort of like given to china in terms of design plans  
**Translation:** 

**[12901.44s] English:** and stuff um code and stuff like between you know i say companies not nation states is probably very  
**Translation:** 

**[12907.36s] English:** difficult um but ideas are discussed a lot right whether it be a house party in san francisco  
**Translation:** 

**[12913.60s] English:** or a company changing employees or you know or the you know the always the like mythical honey  
**Translation:** 

**[12919.44s] English:** pot that always gets talked about right like someone gets honey potted right uh because  
**Translation:** Vocabulary: mythical: 神话般的

**[12923.20s] English:** everyone working on ai is a single dude who's in their 20s and 30s  
**Translation:** 

**[12926.80s] English:** not everyone but like a insane amount of insane percentages um so there's always like all these  
**Translation:** Vocabulary: percentages: 百分比

**[12932.24s] English:** like you know and and obviously so honey potter is like a spy a female spy approaches you and like  
**Translation:** 

**[12938.56s] English:** yeah yeah or or male right you know it's san francisco right but um as a single dude i will  
**Translation:** 

**[12944.80s] English:** say in his late 20s right is like we are very easily corrupted right like you know like not not  
**Translation:** 

**[12950.16s] English:** corrupted myself but you know like we are we are right everybody else not me yeah i'm too oblivious  
**Translation:** Vocabulary: corrupted: 堕落; oblivious: 无知

**[12956.80s] English:** i'm safe from one espionage access  
**Translation:** 

**[12960.00s] English:** Yeah, you have to make sure to close all security vulnerabilities. So you, Dylan, collect a lot of information about each of the megaclusters for each of the major AI companies. Can you talk about the buildouts for each one that stand out?  
**Translation:** Vocabulary: buildouts: 建设方案; espionage: 间谍活动; megaclusters: 超集群; vulnerabilities: 漏洞

**[12977.60s] English:** Yeah. So I think the thing that's like really important about these megacluster buildouts is they're completely unprecedented in scale, right? US, you know, sort of like data center power consumption has been slowly on the rise and it's gone up to 2, 3% even through the cloud computing revolution, right? Data center consumption as a percentage of total US. And that's been over decades, right? Of data centers, etc. It's been climbing, climbing slowly. But now 2 to 3%. Now, by the end of this decade, it's like even under like, you know, when I say like,  
**Translation:** 

**[13007.60s] English:** like 10 a lot of people that are traditionally uh by like 2028 2030 people traditionally non  
**Translation:** Vocabulary: computing: 计算; megacluster: 超大型集群; unprecedented: 前所未见

**[13013.38s] English:** a uh traditional data center people like that's nuts but then like people who are in like ai who  
**Translation:** 

**[13018.98s] English:** have like really looked at this at like the anthropics and open ais are like that's not  
**Translation:** Vocabulary: anthropics: 人类中心主义

**[13022.16s] English:** enough and i'm like okay but like you know this is this is both through uh globally distributed  
**Translation:** 

**[13028.36s] English:** uh and or distributed throughout the u.s as well as like centralized clusters right the the  
**Translation:** Vocabulary: clusters: 聚集; globally: 全球地

**[13032.74s] English:** distributed throughout the u.s is is exciting and it's the bulk of it right like hey you know  
**Translation:** 

**[13037.30s] English:** uh open ai or uh you know say meta is adding a gigawatt right um but most of it is distributed  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[13044.22s] English:** through the u.s for inference and all these other things right so maybe we should lay out what a  
**Translation:** 

**[13048.64s] English:** what a cluster is so uh you know does this include aws maybe it's it's good to talk about the  
**Translation:** Vocabulary: cluster: 聚类; inference: 推断

**[13055.20s] English:** different kinds of clusters and what you mean by mega clusters and what's the gpu and what's  
**Translation:** 

**[13059.36s] English:** the computer and what yeah not that far back but yeah so like what do we mean by the clusters  
**Translation:** 

**[13065.02s] English:** no man i thought i was about to do the apple ad right  
**Translation:** 

**[13067.30s] English:** what's a computer so so traditionally data centers and data center tasks have been a  
**Translation:** 

**[13074.56s] English:** distributed systems problem that is uh capable of being spread very far and widely right  
**Translation:** 

**[13080.00s] English:** I.e., I send a request to Google, it gets routed to a data center somewhat close to me, it does whatever search ranking recommendation, sends a result back, right?  
**Translation:** Vocabulary: routed: 路由

**[13090.64s] English:** The nature of the task is changing rapidly in that there's two tasks that people are really focused on now, right?  
**Translation:** 

**[13096.60s] English:** It's not database access, it's not serve me the right page, serve me the right ad.  
**Translation:** 

**[13100.26s] English:** It's now, A, inference.  
**Translation:** 

**[13102.86s] English:** And inference is dramatically different from traditional distributed systems, but it looks a lot more similar.  
**Translation:** Vocabulary: dramatically: 显著地

**[13106.80s] English:** And then there's training, right?  
**Translation:** 

**[13109.10s] English:** The inference side is still like, hey, I'm going to put thousands of GPUs and blocks all around these data centers, I'm going to run models on them, user submits a request, gets kicked off, or hey, my service, they submit a request to my service, right?  
**Translation:** 

**[13124.28s] English:** They're on Word, and they're like, oh, yeah, help me copilot, and it kicks it off, or I'm on my Windows, copilot, whatever, Apple Intelligence, whatever it is, it gets kicked off to a data center, right?  
**Translation:** 

**[13131.92s] English:** And that data center does some work and sends it back, that's inference, that is going to be the bulk of compute, but then...  
**Translation:** Vocabulary: copilot: 副驾助手

**[13139.10s] English:** And that's like, there's thousands of data centers that we're tracking with satellites and all these other things, and those are the bulk of what's being built, but the scale of...  
**Translation:** 

**[13148.22s] English:** And so that's what's really reshaping, and that's what's getting millions of GPUs, but the scale of the largest cluster is also really important, right?  
**Translation:** Vocabulary: reshaping: 重塑格局

**[13156.82s] English:** When we look back at history, right, or through the age of AI, right, it was a really big deal when they did AlexNet on, I think, two GPUs or four GPUs, I don't remember.  
**Translation:** 

**[13169.10s] English:** It was a really big deal.  
**Translation:** 

**[13170.06s] English:** It's a big deal because you used GPUs.  
**Translation:** 

**[13171.76s] English:** It's a big deal, they used GPUs, and they used multiple, right?  
**Translation:** 

**[13174.66s] English:** But then over time, its scale has just been compounding, right?  
**Translation:** 

**[13178.24s] English:** And so when you skip forward to GPT-3, then GPT-4, GPT-4, 20,000 A100 GPUs, unprecedented run, right, in terms of the size and the cost, right?  
**Translation:** Vocabulary: compounding: 累积; unprecedented: 前所未有的

**[13188.18s] English:** A couple hundred million dollars on a YOLO, right, a YOLO run for GPT-4, and it yielded this magical improvement that was perfectly in line with what was experimented and just a log scale, right?  
**Translation:** 

**[13198.78s] English:** Oh, yeah.  
**Translation:** 

**[13199.10s] English:** They have that plot.  
**Translation:** 

**[13200.00s] English:** from the paper the technical report the scaling laws were perfect right but that's not a crazy  
**Translation:** 

**[13205.20s] English:** number right 20 000 a100s uh roughly each gpu is consuming 400 watts uh and then when you add in  
**Translation:** 

**[13211.52s] English:** the whole server right everything um it's like 15 to 20 megawatts of power right uh you know  
**Translation:** Vocabulary: megawatts: 兆瓦; watts: 瓦

**[13217.58s] English:** you know maybe you could look up what the power of consumption of a human person is because the  
**Translation:** 

**[13221.84s] English:** numbers are gonna get silly but like that 15 to 20 megawatts was standard data center size it was  
**Translation:** 

**[13226.36s] English:** just unprecedented that was all gpus running one tap it was a toaster the toaster is like it's a  
**Translation:** 

**[13232.14s] English:** good example similar power consumption to an a100 right h100 comes around they increase the power  
**Translation:** 

**[13237.44s] English:** from like 400 to 700 watts and that's just per gpu and then there's all the associated stuff  
**Translation:** 

**[13241.38s] English:** around it so once you count all that it's roughly like 1200 to 1400 watts for everything networking  
**Translation:** 

**[13246.84s] English:** cpus memory blah blah blah so we should also say so what's required you said power so a lot of  
**Translation:** 

**[13253.96s] English:** power is required a lot of heat is generated  
**Translation:** 

**[13256.36s] English:** cooling is required and uh because there's a lot of gpus that have to be or cpus or whatever they  
**Translation:** 

**[13263.90s] English:** have to be connected so there's a lot of networking yeah yeah so i think yeah sorry for uh skipping  
**Translation:** Vocabulary: skipping: 跳过

**[13268.92s] English:** past that and then the data center itself is like complicated right but these are still  
**Translation:** 

**[13273.04s] English:** standardized data centers for gpd4 scale right now we step forward to sort of what is the scale  
**Translation:** 

**[13279.28s] English:** of clusters that people built last year right and it ranges widely right it ranges from like  
**Translation:** 

**[13285.22s] English:** hey these are standard  
**Translation:** Vocabulary: clusters: 聚类

**[13286.30s] English:** gpus memory blah blah blah and then it ranges from like hey these are standard  
**Translation:** 

**[13286.34s] English:** data centers and we're just using multiple of them and connecting them together really  
**Translation:** 

**[13289.80s] English:** with a ton of fiber between them a lot of networking etc that's what open ai and microsoft  
**Translation:** 

**[13293.90s] English:** did in arizona right and so they have a you know 100 000 gpus right meta similar thing they took  
**Translation:** Vocabulary: arizona: 亚利桑那州

**[13298.68s] English:** their standard existing data center design um and it looks like an h and they connected multiple  
**Translation:** 

**[13302.96s] English:** of them together um and you know they got to they first did 16 000 gpus uh 24 000 gpus total  
**Translation:** 

**[13309.12s] English:** only 16 of them thousand of them were running on the training run because gpus are very unreliable  
**Translation:** 

**[13313.16s] English:** so they need to have spares to like swap in and out all the way to like now  
**Translation:** Vocabulary: unreliable: 不可靠

**[13316.28s] English:** hundred thousand gpus that they're training on llama 4 on currently right like a hundred  
**Translation:** 

**[13320.00s] English:** 128,000 or so, right? This is, you know, think about 100,000 GPUs with roughly 1400 watts a  
**Translation:** Vocabulary: llama: 羊驼模型

**[13327.70s] English:** piece. That's, that's, that's 140 megawatts, 150 megawatts, right? For 128,000, right? So you're  
**Translation:** 

**[13333.26s] English:** talking about, you've jumped from 15 to 20 megawatts to 10x, you know, almost 10x that  
**Translation:** 

**[13337.88s] English:** number, 9x that number to 150 megawatts in, in two years, right? From 2022 to 2024, right? And  
**Translation:** 

**[13344.76s] English:** some people like Elon, he admittedly, right? And he says himself got into the game a little bit  
**Translation:** Vocabulary: admittedly: 坦白地说; megawatts: 兆瓦

**[13349.80s] English:** late for pre-training large language models, right? XAI was started later, right? But then  
**Translation:** 

**[13353.92s] English:** he, he bet heaven and hell to get his data center up and get the largest cluster in the world,  
**Translation:** Vocabulary: cluster: 计算集群

**[13358.38s] English:** right? Which is 200,000 GPUs. And, and, and he did that. He bought a factory in Memphis.  
**Translation:** 

**[13363.98s] English:** He, he's upgrading the substation, but at the same time, he's got a bunch of mobile power  
**Translation:** Vocabulary: memphis: Memphis市; substation: 变电站; upgrading: 升级

**[13368.00s] English:** generation, a bunch of single cycle combine. He tapped the natural gas line that's right next to  
**Translation:** 

**[13372.84s] English:** the factory. And it's just pulling a ton of gas, burning gas. He's generating all this power.  
**Translation:** 

**[13377.40s] English:** He's in a factory in an old appliance factory.  
**Translation:** 

**[13379.80s] English:** That's shut down and moved to China long ago, right? Like, you know, and, and, and he's  
**Translation:** 

**[13383.30s] English:** got 200,000 GPUs in it. And now what's the next scale, right? Like all the hyperscalers have done  
**Translation:** 

**[13388.36s] English:** this. Now the next scale is, is, is something that's even bigger, right? And so, you know,  
**Translation:** Vocabulary: hyperscalers: 超大规模云服务商

**[13392.24s] English:** Elon, just to stick on the topic, he's, he's building his own natural gas plant, like a proper  
**Translation:** 

**[13396.78s] English:** one right next door. He's, he's deploying tons of Tesla mega pack batteries to make the power more  
**Translation:** Vocabulary: deploying: 部署

**[13402.72s] English:** smooth and all sorts of other things. He's got like industrial chillers to cool the water down  
**Translation:** 

**[13407.62s] English:** because he's water cooling the chips.  
**Translation:** Vocabulary: chillers: 冷水机

**[13409.80s] English:** So all these crazy things to get the clusters bigger and bigger. But when you look at like,  
**Translation:** 

**[13414.90s] English:** say what OpenAI did with Stargate, that's that in Arizona, in, in Abilene, Texas, right? What  
**Translation:** Vocabulary: abilene: 阿比林; arizona: 亚利桑那; clusters: 聚类; stargate: 星门; texas: 得克萨斯

**[13422.44s] English:** they've announced at least, right? It's not built, right? Elon says they don't have the money. You  
**Translation:** 

**[13425.60s] English:** know, there's some debates about this. But at full scale, at least the first section is like,  
**Translation:** 

**[13430.94s] English:** definitely money's accounted for, but there's multiple sections. But full scale, that data  
**Translation:** 

**[13434.40s] English:** center is going to be 2.2 gigawatts, right? 2,200 megawatts of power in. And roughly,  
**Translation:** Vocabulary: gigawatts: 吉瓦

**[13439.80s] English:** like,  
**Translation:** 

**[13440.00s] English:** 1.8 gigawatts or 1800 megawatt uh yeah 1800 megawatts of power delivered to chips right  
**Translation:** Vocabulary: megawatt: 兆瓦

**[13447.30s] English:** now this is an absurd scale 2.2 gigawatts is like more than most cities right you know to be clear  
**Translation:** 

**[13452.96s] English:** um and delivered to a single cluster that's connected to do training right um to train  
**Translation:** 

**[13459.14s] English:** these models to do both the pre-training the post-training all of this stuff right  
**Translation:** 

**[13462.12s] English:** this is insane what is a nuclear power plant again everyone is doing this right everyone is doing  
**Translation:** 

**[13467.42s] English:** meta meta in louisiana right they're building two natural gas plants massive ones uh and they're  
**Translation:** 

**[13473.90s] English:** and then they're building this massive data center um amazon has like plans for this scale uh google  
**Translation:** 

**[13479.70s] English:** has plans for this scale uh xai has plans for this scale right like all of these the guys that  
**Translation:** 

**[13485.72s] English:** are racing the companies that are racing are racing hard and they're doing multi-gigawatt  
**Translation:** 

**[13490.28s] English:** data centers right um to to build this out because they they think that yeah if i if i now have you  
**Translation:** 

**[13497.42s] English:** see pre-training scaling is going to continue but to some extent but then also all this post-training  
**Translation:** 

**[13501.16s] English:** stuff where you have an rl sandbox for computer use or whatever right like you know this is where  
**Translation:** 

**[13505.30s] English:** they're going to and all these fearful about viable domains where they just keep learning  
**Translation:** Vocabulary: sandbox: 试验环境

**[13508.26s] English:** and learning and learning self-play whatever whatever it is makes the ai so much more capable  
**Translation:** 

**[13512.48s] English:** because the line does go up right uh as you throw more compute you get more performance the shirt is  
**Translation:** 

**[13517.42s] English:** about scaling laws um you know to some extent it is diminishing returns right you 10x the compute  
**Translation:** 

**[13522.16s] English:** you don't get 10x better model right you get a diminishing returns but also you get efficiency  
**Translation:** Vocabulary: diminishing: 递减的

**[13526.56s] English:** improvements so you better you better you better you better you better you better you better you  
**Translation:** 

**[13527.42s] English:** the curve right um and these scale of data centers are doing you know reeking you know a lot of like  
**Translation:** Vocabulary: reeking: 臭味熏天

**[13533.36s] English:** havoc on the network right and you know nathan was mentioning there's amazon has tried to buy  
**Translation:** 

**[13538.32s] English:** this nuclear power plant uh talon um and if you look at talon stock it's just like skyrocketing  
**Translation:** Vocabulary: havoc: 混乱; skyrocketing: 飙升; talon: 塔伦

**[13543.12s] English:** and um you know like they're building a massive multi-gigawatt data center there and you know  
**Translation:** 

**[13547.18s] English:** you just go down the list there's so many ramifications interesting thing is like certain  
**Translation:** Vocabulary: ramifications: 影响

**[13551.16s] English:** regions of the u.s transmitting power cost more than actually generating it right because the  
**Translation:** 

**[13557.42s] English:** grid is so slow to build and the demand for power  
**Translation:** Vocabulary: transmitting: 传输

**[13560.00s] English:** and the ability to build power and like, re ramping on a natural gas plant, or even a coal  
**Translation:** 

**[13563.84s] English:** plant is like easy enough to do, but like, transmitting the power is really hard. So in  
**Translation:** 

**[13567.40s] English:** some parts of the US, like in Virginia, it costs more to transmit power than it costs to generate  
**Translation:** 

**[13572.30s] English:** it, which is like, you know, there's there's all sorts of like second order effects that are insane  
**Translation:** Vocabulary: transmit: 传输

**[13576.02s] English:** here. Can the power grid support this kind of growth? You know, Trump's executive orders,  
**Translation:** 

**[13580.36s] English:** there's there's a Biden executive order before the end of the year, but then Trump had some  
**Translation:** 

**[13583.66s] English:** more executive orders, which hopefully reduce the regulations to where yes, things can be built.  
**Translation:** 

**[13590.00s] English:** Um, but yeah, this is a big, big challenge, right? Is building enough power fast enough?  
**Translation:** 

**[13594.00s] English:** Are you going to basically have a nuclear power plant next to a data center for each one of these?  
**Translation:** 

**[13598.52s] English:** So so the fun thing here is this is too slow. To build the power plant to build a power plant or  
**Translation:** 

**[13604.54s] English:** to re configure an existing power plant is too slow. And so therefore, you must use natural data  
**Translation:** 

**[13611.06s] English:** center power consumption is flat, right? You know, I mean, like, it's like, it's why nuclear is also  
**Translation:** Vocabulary: configure: 配置

**[13614.74s] English:** good for it. Like long term nuclear is a very natural fit. But yeah, it's short, you can't  
**Translation:** 

**[13619.98s] English:** do solar or anything in the short term. Like that is data center powers like this, right? Like  
**Translation:** 

**[13624.14s] English:** you're telling me, you know, I'm gonna buy 10s of billions of dollars of GPUs and idle them because  
**Translation:** 

**[13629.64s] English:** the power is not being generated, like power is cheap, right? Like if you look at the cost of a  
**Translation:** 

**[13632.76s] English:** cluster, less than 20% of it is power, right? Most of it is the capital costs and depreciation of the  
**Translation:** 

**[13638.64s] English:** GPUs, right? And so it's like, well, screw it. I'll just like, you know, I'll just build natural  
**Translation:** Vocabulary: cluster: 计算集群; depreciation: 折旧

**[13642.78s] English:** gas plants. This is what meta is doing in Louisiana. This is what open AI is doing in Texas  
**Translation:** 

**[13646.76s] English:** and like all these different places. They may not be doing it directly,  
**Translation:** Vocabulary: texas: 德克萨斯州

**[13649.98s] English:** but they are partnered with someone. And so there is a couple hopes, right? Like one is,  
**Translation:** 

**[13655.22s] English:** you know, Elon, what he's doing in Memphis is like, you know, to the extreme, they're not just  
**Translation:** Vocabulary: memphis: 孟菲斯

**[13658.58s] English:** using dual combine cycle gas, which is like super efficient. He's also just using single cycle and  
**Translation:** 

**[13663.60s] English:** like mobile generators and stuff, which is less efficient. But he's, you know, there's also like  
**Translation:** 

**[13668.52s] English:** the flip side, which is like, solar power generation is like this and wind is another  
**Translation:** 

**[13672.62s] English:** like, like this different correlate, you know, different. So if you stack both of those,  
**Translation:** Vocabulary: correlate: 相关性

**[13676.28s] English:** plus you get a big chunk of batteries, plus you have a little bit of gas,  
**Translation:** 

**[13679.98s] English:** Uh huh.  
**Translation:** 

**[13680.00s] English:** it is possible to run it more green it's just the time scales for that is slow right so people are  
**Translation:** 

**[13685.22s] English:** trying but you know meta basically said whatever don't care about my sustainability pledge or  
**Translation:** Vocabulary: pledge: 承诺

**[13692.00s] English:** they'll buy like a power it's called a ppa power purchasing agreement where there'll be a massive  
**Translation:** 

**[13695.96s] English:** wind farm or solar farm like wherever and then they'll just pretend like those electrons are  
**Translation:** Vocabulary: purchasing: 购买

**[13700.04s] English:** being consumed by the data center but in reality they're paying for the power here and selling it  
**Translation:** 

**[13703.66s] English:** to the grid and they're buying power here um and then another thing is like microsoft quit on some  
**Translation:** 

**[13708.56s] English:** of their sustainability pledges right elon uh he what he did with memphis is objectively somewhat  
**Translation:** 

**[13713.54s] English:** dirty but he's also doing it in an area where there's like a bigger natural gas plant right  
**Translation:** Vocabulary: objectively: 客观上; pledges: 承诺

**[13717.74s] English:** next door and like a sewer next or not a sewer but like a wastewater treatment and a garbage dump  
**Translation:** 

**[13722.04s] English:** nearby right and and he's he's obviously made the world a lot more clean than that one data center  
**Translation:** Vocabulary: wastewater: 废水

**[13726.50s] English:** is gonna do right so i think like it's fine uh to some extent and maybe agi solves you know global  
**Translation:** 

**[13732.28s] English:** warming and stuff right whatever it is um you know this is this is sort of the attitude that  
**Translation:** 

**[13736.48s] English:** people at the labs have right which is like yeah  
**Translation:** 

**[13738.56s] English:** we'll just use gas right because the race is that important and if we lose you know that's way worse  
**Translation:** 

**[13743.06s] English:** right i should say that uh i got a chance to visit um the memphis data center and it's uh  
**Translation:** 

**[13749.44s] English:** kind of incredible i mean i visited with elon just the teams and the rate of innovation there's  
**Translation:** 

**[13757.68s] English:** insane there's uh my sense is that you know nobody's ever done anything of this scale  
**Translation:** 

**[13762.68s] English:** and nobody has certainly ever done anything of this scale at the rate that xai is doing  
**Translation:** 

**[13768.56s] English:** so they're like figuring out i mean and so i was sitting in on all these meetings where they're  
**Translation:** 

**[13774.02s] English:** brainstorming it's like it's insane it's exciting because they're like they're trying to figure out  
**Translation:** Vocabulary: brainstorming: 头脑风暴

**[13779.42s] English:** what the bottlenecks are how to remove the bottlenecks how to make sure that you know  
**Translation:** 

**[13783.24s] English:** there's just so many really cool things about putting together a data center because you know  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[13789.66s] English:** everything has to work it's uh the the people that do like the sysadmin you know the machine  
**Translation:** 

**[13795.80s] English:** learning all that is the exciting thing so on but really  
**Translation:** Vocabulary: sysadmin: 系统管理员

**[13798.56s] English:** the people that run everything are the  
**Translation:** 

**[13800.00s] English:** the folks that know like the low level uh software and hardware that runs everything  
**Translation:** 

**[13806.42s] English:** the networking all of that and so you have to like make sure you have procedures that test  
**Translation:** 

**[13811.58s] English:** everything i think they're using ethernet i don't know how they're doing the networking but  
**Translation:** Vocabulary: ethernet: 以太网

**[13815.18s] English:** they're using nvidia spectrum x ethernet um there's actually like i think yeah the unsung  
**Translation:** 

**[13820.00s] English:** heroes are the cooling and electrical systems which are just like glossed over yeah um but i  
**Translation:** Vocabulary: glossed: 略过

**[13825.34s] English:** think like like one story that maybe is like exemplifies how insane this stuff is is uh when  
**Translation:** 

**[13831.20s] English:** you're training right um you're always doing you're you're you're running through the model  
**Translation:** Vocabulary: exemplifies: 举例说明

**[13835.48s] English:** a bunch right in the most simplistic terms running through the model a bunch and then you're uh  
**Translation:** 

**[13840.02s] English:** you're going to exchange everything and synchronize the weights right so you'll do you'll do a step  
**Translation:** Vocabulary: simplistic: 简单化; synchronize: 同步

**[13844.04s] English:** this is like a step in model training right and every step your loss goes down hopefully and it  
**Translation:** 

**[13847.56s] English:** doesn't always but um in the simplest terms you'll be computing a lot and then you'll exchange  
**Translation:** Vocabulary: computing: 计算

**[13851.66s] English:** right the interesting thing is gpu power is most of it networking power is some  
**Translation:** 

**[13855.34s] English:** but it's a lot less but so while you're computing your power for your gpus is here but then when  
**Translation:** 

**[13859.68s] English:** you're exchanging weights uh if you're not able to overlap communications and compute perfectly  
**Translation:** 

**[13863.90s] English:** there may be a time period where your gpus are just idle and you're exchanging weights and you're like  
**Translation:** 

**[13868.48s] English:** hey the model's updating so you're exchanging the gradients you do the model update and then you you  
**Translation:** 

**[13872.58s] English:** start training again so the power goes right and it's super spiky and so funnily enough right like  
**Translation:** Vocabulary: gradients: 梯度; spiky: 尖峰的

**[13878.60s] English:** this when you talk about the scale of data center power right you can blow stuff up so easy um and  
**Translation:** 

**[13885.00s] English:** so  
**Translation:** 

**[13885.12s] English:** meta actually has accidentally opened upstream something to code in pi torch where they added  
**Translation:** 

**[13890.88s] English:** an operator and i kid you not whoever made this like i want to hug the guy because it says  
**Translation:** 

**[13894.80s] English:** says pi torch uh it's like pi torch dot power plant no blow up equal zero or equal one and  
**Translation:** 

**[13900.70s] English:** what it does what it does is amazing right either you know one year when you're exchanging the  
**Translation:** 

**[13905.98s] English:** weights the gpu will just compute fake numbers so the power doesn't spike too much and so then  
**Translation:** 

**[13910.26s] English:** the power plants don't blow up because the transient spikes like screw stuff up well that  
**Translation:** Vocabulary: spike: 峰值; spikes: 峰值; transient: 瞬态

**[13914.46s] English:** makes sense i mean  
**Translation:** 

**[13915.12s] English:** you have to do that kind of thing you have to make sure they're not idle yeah an elon solution  
**Translation:** 

**[13920.00s] English:** was like let me throw a bunch of tesla mega packs and a few other things right like everyone has  
**Translation:** 

**[13923.70s] English:** different solutions but like metas at least was publicly and openly known which is just like  
**Translation:** 

**[13927.96s] English:** set this operator and what this operator does is it just makes the gpus compute nothing  
**Translation:** 

**[13932.30s] English:** so that the power doesn't spike but that just tells you how much power you're working with i  
**Translation:** 

**[13937.10s] English:** mean it's insane it's insane people should just go to google like scale like what does x watts do  
**Translation:** 

**[13943.14s] English:** and go through all the scales from one watt to a kilowatt to a megawatt and you look and stare at  
**Translation:** Vocabulary: kilowatt: 千瓦; megawatt: 兆瓦; watts: 瓦

**[13948.46s] English:** that and you're how high on the list a gigawatt is and it's mind-blowing can you say something  
**Translation:** 

**[13954.66s] English:** about the cooling so i i know elon's using liquid cooling i believe in in all cases uh that's a new  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[13962.84s] English:** thing right most of them don't use liquid cooling is there something interesting to say about the  
**Translation:** 

**[13966.42s] English:** cooling yeah yeah so air cooling has been the de facto standard uh throw a bunch of metal heat  
**Translation:** Vocabulary: facto: 实际上

**[13971.12s] English:** heat pipes etc and fans right and like that's cooled that's been enough to cool it um people  
**Translation:** 

**[13976.60s] English:** have been dabbling in water cooling google  
**Translation:** Vocabulary: dabbling: 业余尝试

**[13978.46s] English:** tpus are water cooled right um so they've been doing that for a few years uh but uh with gpus no  
**Translation:** 

**[13985.18s] English:** one's ever done and no one's ever done the scale of water cooling that elon just did right uh um  
**Translation:** 

**[13989.60s] English:** now next generation nvidia is uh for the for the like highest end gpu it is mandatory water  
**Translation:** 

**[13994.80s] English:** cooling you have to water cool it but elon did it on this current generation uh and that required  
**Translation:** 

**[13999.54s] English:** a lot of stuff right if you look at like some of the satellite photos and stuff of of uh the  
**Translation:** 

**[14004.16s] English:** memphis facility there's all these external water chillers that are sitting basically it looks like  
**Translation:** Vocabulary: chillers: 冷却塔

**[14008.46s] English:** it looks like a semi-truck pod thing uh what's it called the container uh but really those are  
**Translation:** 

**[14012.68s] English:** water chillers and he has like 90 of those water chillers just sitting outside 90 different  
**Translation:** 

**[14016.56s] English:** containers right with water you know like chill the water bring it back to the data center and  
**Translation:** 

**[14021.00s] English:** then you distribute it to all the chips pull all the heat out and then send it back right and this  
**Translation:** Vocabulary: chill: 冷却

**[14024.96s] English:** is both a uh way to cool the chips but also an efficiency thing all right and going back to that  
**Translation:** 

**[14030.52s] English:** like sort of three vector thing right there is um there is you know memory bandwidth flops and  
**Translation:** Vocabulary: bandwidth: 内存带宽; flops: 浮点运算

**[14038.46s] English:** things like that and i think that's one of the things that's really great about this it's  
**Translation:** 

**[14043.24s] English:** not a big deal it's about the functionality of it i don't think it's maybe a big deal for solvents  
**Translation:** Vocabulary: functionality: 功能; solvents: 溶剂

**[14047.90s] English:** it's really it's really something that we have to work with to really know how to use it in a way  
**Translation:** 

**[14051.72s] English:** that i think makes it much easier to do a lot of stuff and i could help with that as well but  
**Translation:** 

**[14056.12s] English:** it's really just one of the things that i've realized that you know people have asked me is  
**Translation:** 

**[14061.00s] English:** you know with the the idea of the modding and the use of instant memory and i don't think it has  
**Translation:** 

**[14040.00s] English:** speed interconnects right and so this is this is also like a reason why you're going to go  
**Translation:** 

**[14045.24s] English:** water cooling is because you can just put the chips right next to each other and therefore get  
**Translation:** Vocabulary: interconnects: 连接

**[14049.16s] English:** higher uh speed connectivity i gotta ask you so in uh one of your recent posts there's a section  
**Translation:** 

**[14059.18s] English:** called cluster measuring contest so uh there's another word there but i won't say it you know  
**Translation:** Vocabulary: cluster: 聚类

**[14064.64s] English:** uh what who's who's who's got the biggest now and who's gonna have the today individual largest  
**Translation:** 

**[14072.80s] English:** is elon right um elon's cluster elon's cluster in memphis 200 000 gpus right um meta has like  
**Translation:** Vocabulary: memphis: Memphis 市

**[14081.02s] English:** 128 000 opening has 100 000 now now to be clear other companies have more gpus than elon they  
**Translation:** 

**[14086.24s] English:** just don't have them in one place right and for training you want them tightly connected there's  
**Translation:** 

**[14090.72s] English:** some techniques that people are researching or and working on that lets you train  
**Translation:** 

**[14094.64s] English:** across multiple regions but for the most part you want them all in like one area right so you  
**Translation:** 

**[14099.78s] English:** can connect them highly with high speed networking um and so you know elon today has 200 000 gp h100s  
**Translation:** 

**[14106.14s] English:** and h 100 000 h100s 100 000 h200s right um meta open ai uh you know and and and amazon all have  
**Translation:** 

**[14114.44s] English:** on the scale of 100 000 a little bit less um but next this year right this year people are building  
**Translation:** 

**[14119.42s] English:** much more right anthropic and amazon are building a cluster of 400 000 tranium 2 which is amazon  
**Translation:** 

**[14124.38s] English:** specifically  
**Translation:** 

**[14124.64s] English:** trying to get away from nvidia right um you know uh meta and and and open ai have scales for  
**Translation:** 

**[14132.70s] English:** hundreds of thousands but by next year you'll have like 500 000 to 700 000 gpu clusters and  
**Translation:** 

**[14138.18s] English:** and note those gpus are much higher power consumption than existing ones right hopper  
**Translation:** Vocabulary: clusters: 计算节点群

**[14142.16s] English:** 700 watts blackwell goes to 1200 watts right so so the power per chip is growing and the number  
**Translation:** 

**[14148.38s] English:** of chips is growing right nuts yeah you think you think elon said he'll get to a million you  
**Translation:** Vocabulary: watts: 瓦特

**[14154.14s] English:** think that's  
**Translation:** 

**[14154.38s] English:** actually feasible um i mean i i don't doubt elon right uh the filings that  
**Translation:** Vocabulary: feasible: 可行的

**[14160.00s] English:** he has for like you know the power plant and the tesla battery packs it's clear he has some crazy  
**Translation:** 

**[14164.12s] English:** plans for memphis um like permits and stuff is open record right um but it's not quite clear  
**Translation:** 

**[14169.70s] English:** that you know what what and what the time scales are um i just never doubt elon right you know  
**Translation:** 

**[14175.12s] English:** that's he's gonna surprise us so what's the idea with these clusters if you have a million gpus  
**Translation:** 

**[14179.04s] English:** what percentage in uh let's say two three years is used for uh training and what percent pre-training  
**Translation:** 

**[14187.76s] English:** what percent is used for like for the actual computation clusters make no sense for inference  
**Translation:** Vocabulary: computation: 计算; inference: 推断

**[14193.30s] English:** right you could route inference there and just not train um but most of the inference capacity  
**Translation:** 

**[14198.62s] English:** is being you know hey i've got a 30 megawatt data center here i've got 50 megawatts here i've got  
**Translation:** Vocabulary: megawatt: 兆瓦; megawatts: 兆瓦

**[14202.80s] English:** 100 here whatever i'll just throw inference in all of those because the mega clusters right  
**Translation:** 

**[14207.84s] English:** multi-gigawatt data centers i want to train there because that's where all of my gpus are co-located  
**Translation:** 

**[14212.68s] English:** where i can put them at a super high networking speed connected together right because that's  
**Translation:** 

**[14217.10s] English:** what you need for training  
**Translation:** 

**[14217.76s] English:** now with pre-training this is the old scale right you could you would increase parameters you'd  
**Translation:** 

**[14222.30s] English:** increase data model gets better uh that doesn't that doesn't apply anymore because there's not  
**Translation:** 

**[14227.36s] English:** much more data in the pre-training side right uh yes there's video and audio and image that has  
**Translation:** 

**[14232.08s] English:** not been fully taken advantage of so there's a lot more scaling but a lot of people like like  
**Translation:** 

**[14236.08s] English:** have have transcript taken transcripts of youtube videos and that gets you a lot of the data doesn't  
**Translation:** 

**[14240.30s] English:** get you all the learning value out of the video and image data but you know there's there's still  
**Translation:** Vocabulary: transcript: 书面记录; transcripts: 书面记录

**[14244.18s] English:** scaling to be done on pre-training uh but this post-training world  
**Translation:** 

**[14247.58s] English:** you know there's still scaling to be done on pre-training but this post-training world  
**Translation:** 

**[14247.74s] English:** is where all the flops are going to be spent right the model is going to play with itself  
**Translation:** 

**[14251.14s] English:** it's going to self-play it's going to do verifiable tasks it's going to do computer  
**Translation:** Vocabulary: flops: 运算次数; verifiable: 可验证的

**[14254.06s] English:** use in sandboxes it might even do like simulated robotics things right like all of these things  
**Translation:** 

**[14259.72s] English:** are going to be environments where compute is spent in quote-unquote post-training but i think  
**Translation:** Vocabulary: environments: 环境; sandboxes: 沙箱; simulated: 模拟

**[14265.34s] English:** i think it's going to be good we're going to we're going to drop the post from post-training  
**Translation:** 

**[14268.34s] English:** yeah it's going to be pre-training and it's going to be training i think at some point um because  
**Translation:** 

**[14274.14s] English:** because for the like bulk of like the last few years um pre-training has dwarfed post-training  
**Translation:** 

**[14280.00s] English:** But with these verifiable methods, especially ones that scale really, you know, potentially  
**Translation:** 

**[14284.62s] English:** infinitely, like computer use and robotics, not just math and coding, right, where you  
**Translation:** 

**[14288.16s] English:** can verify what's happening, those infinitely verifiable tasks, it seems you can spend as  
**Translation:** Vocabulary: infinitely: 无穷地; verify: 验证

**[14292.30s] English:** much compute as you want on them.  
**Translation:** 

**[14293.68s] English:** Especially at the context length increase, because at the end of pre-training is when  
**Translation:** 

**[14296.78s] English:** you increase the context length for these models.  
**Translation:** 

**[14299.16s] English:** And we've talked earlier in the conversation about how the context length, when you have  
**Translation:** 

**[14303.40s] English:** a long input, is much easier to manage than output.  
**Translation:** 

**[14305.74s] English:** And a lot of these post-training and reasoning techniques rely on a ton of sampling, and  
**Translation:** 

**[14310.70s] English:** it's becoming increasingly long context.  
**Translation:** 

**[14313.10s] English:** So it's just like, effectively, your compute efficiency goes down.  
**Translation:** 

**[14317.04s] English:** I don't think flops is the standard for how you measure it, but with RL, and you have  
**Translation:** 

**[14322.54s] English:** to do all these things where you move your weights around in a different way than at  
**Translation:** 

**[14326.66s] English:** pre-training and just generation, it's going to become less efficient, and flops is going  
**Translation:** 

**[14332.22s] English:** to be less of a useful term.  
**Translation:** 

**[14333.50s] English:** And then as the infrastructure gets better, it's probably going to go down.  
**Translation:** 

**[14335.74s] English:** It's going to go back to flops.  
**Translation:** 

**[14337.12s] English:** So all of the things we've been talking about is most likely going to be NVIDIA, right?  
**Translation:** 

**[14341.90s] English:** Is there any competitors?  
**Translation:** 

**[14343.44s] English:** Google, I kind of ignored them.  
**Translation:** 

**[14346.32s] English:** What's the story with TPU?  
**Translation:** 

**[14350.56s] English:** TPU is awesome, right?  
**Translation:** 

**[14352.14s] English:** It's great.  
**Translation:** 

**[14353.14s] English:** Google is, they're a bit more tepid on building data centers for some reason.  
**Translation:** 

**[14357.44s] English:** They're building big data centers, don't get me wrong.  
**Translation:** Vocabulary: tepid: 态度温和

**[14359.36s] English:** And they actually have the biggest cluster.  
**Translation:** 

**[14361.28s] English:** I was talking about NVIDIA clusters.  
**Translation:** Vocabulary: cluster: 聚集; clusters: 聚集

**[14363.08s] English:** They actually have the biggest cluster, period.  
**Translation:** 

**[14365.74s] English:** But the way they do it is very interesting, right?  
**Translation:** 

**[14368.60s] English:** They have two sort of data center super regions, right?  
**Translation:** 

**[14372.36s] English:** In that the data center isn't physically, all of the GPUs aren't physically on one site,  
**Translation:** 

**[14376.14s] English:** but they're like 30 miles from each other.  
**Translation:** 

**[14377.64s] English:** They're not GPUs, TPUs, right?  
**Translation:** 

**[14378.94s] English:** They have, in Iowa and Nebraska, they have four data centers that are just right next  
**Translation:** 

**[14383.32s] English:** to each other.  
**Translation:** Vocabulary: nebraska: 内布拉斯加州

**[14384.30s] English:** Why doesn't Google flex its cluster size?  
**Translation:** 

**[14388.14s] English:** Go to multi-data center training.  
**Translation:** 

**[14389.70s] English:** There's good images in there, so I'll show you what I mean.  
**Translation:** 

**[14391.54s] English:** It's just semi-analysis multi-data center.  
**Translation:** 

**[14394.86s] English:** So this is like...  
**Translation:** 

**[14395.74s] English:** So this is an image of what a standard Google data center looks like.  
**Translation:** 

**[14398.88s] English:** By the way, their data centers look...  
**Translation:** 

**[14400.00s] English:** different than anyone else's data centers. What are we looking at here? So these are, yeah, so if  
**Translation:** 

**[14404.02s] English:** you see this image, right, in the center there are these big rectangular boxes, right? Those are where  
**Translation:** 

**[14408.92s] English:** the actual chips are kept. And then if you scroll down a little bit further, you can see there's  
**Translation:** Vocabulary: rectangular: 长方形的; scroll: 滚动

**[14414.90s] English:** like these water pipes, there's these chiller cooling towers in the top, and a bunch of like  
**Translation:** 

**[14419.18s] English:** diesel generators. The diesel generators are backup power. The data center itself is like, look,  
**Translation:** Vocabulary: chiller: 制冷塔; diesel: 柴油; generators: 发电机组

**[14424.72s] English:** physically smaller than the water chillers, right? So the chips are actually easier to like keep  
**Translation:** 

**[14429.06s] English:** together, but then like cooling all the water for the water cooling is very difficult, right? So  
**Translation:** Vocabulary: chillers: 冷水机

**[14433.32s] English:** Google has like a very advanced infrastructure that no one else has for the TPU. And what they  
**Translation:** 

**[14438.72s] English:** do is they've like stamped these data center, they've stamped a bunch of these data centers out  
**Translation:** 

**[14442.08s] English:** in a few regions, right? So if you go a little bit further down, this is a Microsoft, this is  
**Translation:** 

**[14447.88s] English:** in Arizona, this is where GPT-5 quote-unquote will be trained, you know. If it doesn't exist already.  
**Translation:** Vocabulary: arizona: 亚利桑那州

**[14454.36s] English:** Yeah, if it doesn't exist already. But each of these data centers, right, I've shown a couple  
**Translation:** 

**[14458.32s] English:** images of them.  
**Translation:** 

**[14459.06s] English:** They're like really closely co-located in the same region, right? Nebraska, Iowa. And then they  
**Translation:** 

**[14463.26s] English:** also have a similar one in Ohio complex, right? And so these data centers are really close to each  
**Translation:** 

**[14468.74s] English:** other. And what they've done is they've connected them super high bandwidth with fiber. And so these  
**Translation:** 

**[14473.82s] English:** are just a bunch of data centers. And the point here is that Google has a very advanced infrastructure,  
**Translation:** Vocabulary: bandwidth: 带宽

**[14479.28s] English:** very tightly connected in a small region. So Elon will always have the biggest cluster  
**Translation:** 

**[14483.50s] English:** fully connected, right? Because it's all in one building, right? And he's completely right on that,  
**Translation:** Vocabulary: cluster: 聚类

**[14488.10s] English:** right?  
**Translation:** 

**[14489.06s] English:** Has the biggest cluster, but you have to spread over three sites and by a significant margin,  
**Translation:** 

**[14493.82s] English:** we have to go across multiple sites.  
**Translation:** 

**[14495.46s] English:** Why doesn't Google compete with NVIDIA? Why don't they sell TPUs?  
**Translation:** 

**[14501.40s] English:** I think there's a couple problems with it. It's like one, TPU has been a form of allowing search  
**Translation:** 

**[14509.24s] English:** to be really freaking cheap and build models for that, right? And so like a big chunk of the search  
**Translation:** Vocabulary: freaking: 极其

**[14515.14s] English:** GPU purchases or TPU purchases are a big chunk of Google's purchase.  
**Translation:** 

**[14519.06s] English:** Here's this.  
**Translation:** 

**[14520.00s] English:** usage, all of it is for internal workloads, right? Whether it be search, now Gemini, right? YouTube,  
**Translation:** 

**[14526.14s] English:** all these different applications that they have, you know, ads. These are where all their TPUs are  
**Translation:** Vocabulary: gemini: 双子座; workloads: 工作负载

**[14531.54s] English:** being spent and that's what they're hyper-focused on, right? And so there's certain like aspects of  
**Translation:** 

**[14536.28s] English:** the architecture that are optimized for their use case that are not optimized elsewhere, right?  
**Translation:** 

**[14540.88s] English:** One simple one is like they've open sourced the Gemma model and they called it Gemma 7B, right?  
**Translation:** 

**[14545.94s] English:** But then it's actually 8 billion parameters because the vocabulary is so large  
**Translation:** Vocabulary: gemma: 吉玛模型

**[14549.52s] English:** and the reason they made the vocabulary so large is because TPUs like matrix multiply unit is  
**Translation:** 

**[14554.76s] English:** massive because that's what they've like sort of optimized for. And so they decided, oh, well,  
**Translation:** Vocabulary: matrix: 矩阵; multiply: 乘法; optimized: 优化

**[14558.78s] English:** I'll just make the vocabulary large too, even though it makes no sense to do so on such a small  
**Translation:** 

**[14562.30s] English:** model because that fits on their hardware. So Gemma doesn't run as efficiently on a GPU as a  
**Translation:** Vocabulary: efficiently: 运行高效

**[14566.82s] English:** Lama does, right? But vice versa, Lama doesn't run as efficiently on a TPU as a Gemma does,  
**Translation:** 

**[14572.14s] English:** right? And it's so like, there's like certain like aspects of like hardware software co-design.  
**Translation:** Vocabulary: versa: 相反

**[14575.72s] English:** So all their search models are their ranking and recommendation models, all these different  
**Translation:** 

**[14579.50s] English:** models that are AI, but not like Gen AI, right? Have been hyper optimized with TPUs forever.  
**Translation:** 

**[14584.98s] English:** The software stack is super optimized, but all of this software stack has not been released  
**Translation:** 

**[14589.54s] English:** publicly at all, right? Very small portions of it. Jackson XLA have been, but like the experience  
**Translation:** Vocabulary: portions: 部分

**[14595.36s] English:** when you're inside of Google and you're training on TPUs as a researcher, you don't need to know  
**Translation:** 

**[14599.14s] English:** anything about the hardware in many cases, right? Like it's like pretty beautiful, but as soon as  
**Translation:** 

**[14603.42s] English:** you step outside, they'll go, they'll go. A lot of them go back. They leave Google and then they go  
**Translation:** 

**[14608.08s] English:** back. Yeah. Yeah. They're like,  
**Translation:** 

**[14609.50s] English:** they leave and they start a company because they have all these amazing research ideas and they're  
**Translation:** 

**[14612.64s] English:** like, wait, infrastructure is hard. Software is hard. And this is on GPUs. Or if they try to use  
**Translation:** 

**[14617.26s] English:** TPUs, same thing, because they don't have access to all this code. And so it's like, how do you  
**Translation:** 

**[14621.06s] English:** convince a company whose golden goose is search where they're making hundreds of billions of  
**Translation:** Vocabulary: goose: 金蛋鸡

**[14624.70s] English:** dollars from to start selling GPU or TPUs, which they used to only buy a couple billion of, you  
**Translation:** 

**[14630.74s] English:** know, I think in 2023, they bought like a couple billion and now they're buying like 10 billion to  
**Translation:** 

**[14636.96s] English:** $15 billion worth. But how do you convince them that they could,  
**Translation:** 

**[14639.50s] English:** they should just  
**Translation:** 

**[14640.00s] English:** buy like twice as many and figure out how to sell them and make 30 billion dollars like who cares  
**Translation:** 

**[14643.72s] English:** about making 30 billion dollars won't that 30 billion exceed actually the search profit  
**Translation:** 

**[14649.36s] English:** eventually oh i mean like you're always going to make more money on services than than always  
**Translation:** 

**[14655.02s] English:** i mean like yeah like you know like to be clear like today people are spending a lot more on  
**Translation:** 

**[14659.18s] English:** hardware than they are the services right because the hardware front runs the service spend but like  
**Translation:** 

**[14665.76s] English:** you're investing if if there's no revenue for ai stuff or not enough revenue then obviously like  
**Translation:** 

**[14670.24s] English:** it's going to blow up right you know uh people won't continue to spend on gpus forever um and  
**Translation:** 

**[14674.56s] English:** nvidia is trying to move up the stack with like software that they're trying to sell and license  
**Translation:** 

**[14677.84s] English:** and stuff right but google has never had that like dna of like this is a product we should sell  
**Translation:** 

**[14683.26s] English:** right they don't act the google cloud does it is which is a separate organization from the tpu team  
**Translation:** 

**[14687.86s] English:** which is a separate organization from the deep mind team which is a separate organization from  
**Translation:** 

**[14690.80s] English:** the search team right there's a lot of bureaucracy wait google cloud is a separate team than the tpu  
**Translation:** Vocabulary: bureaucracy: 官僚主义

**[14694.92s] English:** team  
**Translation:** 

**[14695.36s] English:** technically tpu in sits under infrastructure which sits under google cloud but like google  
**Translation:** 

**[14700.98s] English:** cloud like for like renting stuff and tpu architecture are very different goals right  
**Translation:** 

**[14707.32s] English:** in hardware um and software like all of this right like the jacks xla teams do not serve google's  
**Translation:** 

**[14712.62s] English:** customers externally whereas nvidia's various cuda teams for like things like nickel serve  
**Translation:** 

**[14717.14s] English:** external customers right um the internal teams like jackson xla and stuff they more so serve  
**Translation:** Vocabulary: externally: 外部; nickel: 镍

**[14722.70s] English:** deep mind and search right and so their customers  
**Translation:** 

**[14725.36s] English:** they're not building a product for them do you understand why aws keeps winning  
**Translation:** 

**[14729.28s] English:** uh versus azure for cloud uh versus google cloud yeah there's google cloud is tiny isn't it relative  
**Translation:** 

**[14737.08s] English:** to the google cloud is third yeah yeah um microsoft is the second biggest but amazon is the biggest  
**Translation:** 

**[14742.20s] English:** right yeah um and and microsoft uh deceptively sort of includes like microsoft office 365 and  
**Translation:** 

**[14747.32s] English:** things like that like some of these enterprise-wide licenses so in reality the gulf is even larger  
**Translation:** Vocabulary: deceptively: 误导地

**[14751.78s] English:** microsoft is still second though right um amazon is way bigger why because they're not building a product for them  
**Translation:** 

**[14755.36s] English:** because using aws is better and easier and in many cases it's cheaper and it's first  
**Translation:** 

**[14760.00s] English:** lose first yeah but there's a lot of things that are first that well it's easier it's harder to  
**Translation:** 

**[14764.56s] English:** switch than it is to aws because there's big fees for switching to aws generates over 80 percent of  
**Translation:** 

**[14771.00s] English:** amazon's profit i think over 90 percent that's insane the distribution centers are just like  
**Translation:** 

**[14775.18s] English:** one day we'll decide to make money from this but they haven't yet right like they make tiny  
**Translation:** 

**[14779.62s] English:** little profit from you know one day of amazon prime will triple in price you would think they  
**Translation:** 

**[14783.30s] English:** would improve aws uh interface because it's like horrible it's like clunky but everybody is  
**Translation:** Vocabulary: clunky: 笨拙; interface: 界面; triple: 三倍

**[14790.58s] English:** yeah you one would think i think actually google's interface is sometimes nice but it's also like  
**Translation:** 

**[14796.66s] English:** they don't care about anyone besides their top customers exactly like their customer service  
**Translation:** 

**[14800.14s] English:** sucks and like they have a lot less like i mean all these companies they optimize for the big  
**Translation:** 

**[14804.42s] English:** customers yeah it's supposed to be for business amazon has always optimized for the small customer  
**Translation:** Vocabulary: optimize: 优化; optimized: 已经优化

**[14809.02s] English:** too though right like obviously they optimize a lot for the big customer but like when they started  
**Translation:** 

**[14812.66s] English:** they just  
**Translation:** 

**[14813.24s] English:** they just  
**Translation:** 

**[14813.28s] English:** they just  
**Translation:** 

**[14813.30s] English:** would go to like random bay area things and give out credits right and then they like or just put  
**Translation:** 

**[14817.78s] English:** in your credit card and use us right like back in the early days so they've always the business has  
**Translation:** 

**[14821.72s] English:** grown with them right in virgin so like why does amazon like why snowflake all over amazon because  
**Translation:** 

**[14826.38s] English:** snowflake in the beginning when amazon didn't care about them was still using amazon right and then  
**Translation:** Vocabulary: snowflake: 雪花公司; virgin: 处女地

**[14830.30s] English:** of course one day snowflake and amazon has a super huge partnership but like this is the case like  
**Translation:** 

**[14834.48s] English:** amazon's user experience and quality is better also a lot of the silicon they've engineered  
**Translation:** 

**[14838.78s] English:** makes them have a lower cost structure and traditional cloud storage cpu networking  
**Translation:** 

**[14842.90s] English:** that kind of stuff uh then um in databases right like you know i think like four of amazon's top  
**Translation:** Vocabulary: databases: 数据库

**[14849.94s] English:** five revenue products uh margin products are like gross profit products are all database related  
**Translation:** 

**[14854.96s] English:** products like redshift and like all these things right like um so so amazon has a very like good  
**Translation:** Vocabulary: redshift: 红移服务

**[14861.42s] English:** silicon to a user experience like entire pipeline with aws i think google they're in for their silicon  
**Translation:** 

**[14867.44s] English:** teams yeah they have awesome silicon internally tpu the youtube chip um you know some of these  
**Translation:** Vocabulary: internally: 内部; pipeline: 流程

**[14872.30s] English:** other chips that they have they have a lot of silicon internally they have a lot of silicon  
**Translation:** 

**[14872.88s] English:** they've made and the problem is they're not serving external customers or serving internal  
**Translation:** 

**[14877.48s] English:** customers right it's i mean nvidia's entire culture is  
**Translation:** 

**[14880.00s] English:** designed from the bottom up to do this there's this recent book the nvidia way by take him  
**Translation:** 

**[14884.12s] English:** that details this and they're how they look for future opportunities and ready their cuda software  
**Translation:** 

**[14891.06s] English:** libraries to make it so that new applications of high performance computing can very rapidly be  
**Translation:** Vocabulary: computing: 高性能计算

**[14896.86s] English:** evolved on cuda and nvidia chips and that is entirely different than google as a services  
**Translation:** 

**[14902.90s] English:** business yeah i mean nvidia it should be said as a truly special company like i mean they  
**Translation:** 

**[14908.90s] English:** the whole the culture of everything they're really optimized for that kind of thing  
**Translation:** 

**[14912.56s] English:** speaking of which is there somebody that can even challenge nvidia hardware wise intel amd  
**Translation:** 

**[14918.76s] English:** i i really don't think so we went through a like a very long process uh yeah working with amd on  
**Translation:** 

**[14926.22s] English:** training on their gpus inference and stuff and they're they're decent their hardware is better  
**Translation:** Vocabulary: inference: 推断

**[14930.24s] English:** in many ways than in nvidia's uh the problem is their software is really bad and i think  
**Translation:** 

**[14934.66s] English:** they're they're getting better right they're getting better faster but they're just the gulf  
**Translation:** 

**[14937.98s] English:** is so large  
**Translation:** 

**[14938.72s] English:** um and like they don't spend enough resources on or haven't historically right maybe they're  
**Translation:** Vocabulary: historically: 历史上

**[14944.04s] English:** changing their tune now but you know for for for multiple months we were submitting those bugs  
**Translation:** 

**[14948.76s] English:** right like us semi-analysis right like what the fuck like why are we submitting those bugs  
**Translation:** Vocabulary: submitting: 提交

**[14953.32s] English:** right because they only and they only cared about their like biggest customers and so they'd ship  
**Translation:** 

**[14957.94s] English:** them a private image blah blah blah and it's like okay but like i am just using pytorch and i want  
**Translation:** 

**[14963.50s] English:** to use the publicly available libraries and like you don't care about that right so they're they're  
**Translation:** 

**[14967.42s] English:** getting better um but they're they're getting better and they're getting better and they're  
**Translation:** 

**[14968.72s] English:** getting better and they're getting better and they're getting better and they're getting better  
**Translation:** 

**[14968.78s] English:** but like i think amd is not possible intel is obviously in dire straits right now  
**Translation:** 

**[14972.26s] English:** um and needs to be saved somehow uh very important for national security for american  
**Translation:** 

**[14977.52s] English:** you know can you explain the obviously so what why are they in dire straits going back to earlier  
**Translation:** 

**[14982.52s] English:** only three companies can r&d right taiwan since you uh samsung uh pyongyang and then intel  
**Translation:** 

**[14989.84s] English:** hillsborough samsung's doing horribly intel's doing horribly we could be in a world where  
**Translation:** Vocabulary: horribly: 糟糕地; taiwan: 台湾

**[14994.18s] English:** there's only one company that can do r&d and that one company already manufactures most of chips  
**Translation:** 

**[14997.84s] English:** they've been gaining market share and they're not going to be able to do that so i think it's  
**Translation:** Vocabulary: manufactures: 生产芯片

**[14998.72s] English:** they're not going to be able to do that so i think it's going to be harder anyways but like  
**Translation:** 

**[14999.52s] English:** that  
**Translation:** 

**[15000.00s] English:** That's a critical thing, right?  
**Translation:** 

**[15001.46s] English:** So what happens to Taiwan means the rest of the world's semiconductor industry, and therefore tech, relies on Taiwan, right?  
**Translation:** 

**[15006.98s] English:** And that's obviously precarious.  
**Translation:** 

**[15008.90s] English:** As far as, like, Intel, they've been slowly, steadily declining.  
**Translation:** Vocabulary: declining: 下降; precarious: 不稳固

**[15013.00s] English:** They were on top of servers and PCs, but now Apple's done the M1, and NVIDIA's releasing a PC chip, and Qualcomm's releasing a PC chip.  
**Translation:** 

**[15021.14s] English:** And in servers, hyperscalers are all making their own ARM-based server chips, and Intel has no AI silicon-like wins, right?  
**Translation:** Vocabulary: hyperscalers: 超大规模云服务商

**[15029.08s] English:** They have very small wins.  
**Translation:** 

**[15031.04s] English:** And they never got into mobile because they said no to the iPhone.  
**Translation:** 

**[15034.06s] English:** And, like, all these things have compounded, and they've lost their process technology leadership, right?  
**Translation:** 

**[15037.80s] English:** They were ahead for 20 years, and now they're behind by at least a couple years, right?  
**Translation:** Vocabulary: compounded: 累积加剧

**[15041.24s] English:** And they're trying to catch back up, and we'll see if, like, their 18A, 14A strategy works out, where they try and leapfrog TSMC.  
**Translation:** 

**[15048.16s] English:** But, like, and Intel's just, like, losing tons of money anyways, right?  
**Translation:** Vocabulary: leapfrog: 超越

**[15051.66s] English:** And they just fired their CEO, even though their CEO was the only person who understood the company well, right?  
**Translation:** 

**[15056.48s] English:** We'll see.  
**Translation:** 

**[15057.04s] English:** He was not the best, but he was pretty good.  
**Translation:** 

**[15059.08s] English:** He was good, relatively.  
**Translation:** 

**[15060.56s] English:** Technical guy.  
**Translation:** 

**[15061.44s] English:** Where does Intel make most of its money?  
**Translation:** 

**[15063.08s] English:** The CPUs, though, right?  
**Translation:** 

**[15064.06s] English:** PCs and data center CPUs, yeah.  
**Translation:** 

**[15065.52s] English:** But data center CPUs are all going cloud, and Amazon, Microsoft, Google are making ARM-based CPUs.  
**Translation:** 

**[15071.46s] English:** And then PC side, AMD's gained market share.  
**Translation:** 

**[15075.02s] English:** NVIDIA's launching a chip.  
**Translation:** 

**[15076.08s] English:** That's not going to be a success, right?  
**Translation:** 

**[15077.30s] English:** MediaTek, Qualcomm have relaunched chips.  
**Translation:** 

**[15079.24s] English:** Apple's doing well, right?  
**Translation:** Vocabulary: qualcomm: 高通; relaunched: 重新推出

**[15080.58s] English:** Like, they could get squeezed a little bit in PC, although PC generally, I imagine, will just stick Intel mostly for Windows side.  
**Translation:** 

**[15086.96s] English:** Let's talk about the broad AI race.  
**Translation:** Vocabulary: squeezed: 受到挤压

**[15089.08s] English:** Who do you think wins?  
**Translation:** 

**[15090.86s] English:** We talked about Google.  
**Translation:** 

**[15091.86s] English:** The default leader has been Google because of their infrastructure advantage.  
**Translation:** 

**[15097.58s] English:** Well, like, in the news, OpenAI is the leader.  
**Translation:** 

**[15100.86s] English:** They're the leading in the narrative.  
**Translation:** 

**[15102.50s] English:** They have the best model.  
**Translation:** 

**[15103.08s] English:** They have the best model that people can use, and they're experts.  
**Translation:** 

**[15106.82s] English:** And they have the most AI revenue.  
**Translation:** 

**[15108.56s] English:** Yeah.  
**Translation:** 

**[15109.32s] English:** OpenAI is winning.  
**Translation:** 

**[15111.04s] English:** So, who's making money on AI right now?  
**Translation:** 

**[15113.66s] English:** Is anyone making money?  
**Translation:** 

**[15114.98s] English:** So, accounting profit-wise, Microsoft is making money, but they're spending a lot of capital.  
**Translation:** 

**[15119.06s] English:** They're spending a lot of capital on graphics, right?  
**Translation:** 

**[15119.74s] English:** You know, and they're spending a lot of capital on graphics.  
**Translation:** 

**[15120.00s] English:** gets depreciated over years uh meta is making tons of money but with recommendation systems  
**Translation:** Vocabulary: depreciated: 资产折旧

**[15125.14s] English:** which is ai but not with llama right llama is losing money for sure right um i think  
**Translation:** 

**[15130.64s] English:** anthropic and open ai are obviously not making money because otherwise they wouldn't be raising  
**Translation:** Vocabulary: llama: 羊驼

**[15134.22s] English:** money right they have to raise money to build more right um although theoretically they are  
**Translation:** 

**[15139.14s] English:** making money right like you know you spent a few hundred million dollars on gpd4 and it's doing  
**Translation:** Vocabulary: theoretically: 理论上

**[15143.44s] English:** billions in revenue so like obviously it's like making money although they had to continue to  
**Translation:** 

**[15147.20s] English:** research to get the compute efficiency wins right and and move down the curve uh to like you know  
**Translation:** 

**[15152.02s] English:** that 12 get that 1200x that has been achieved for gpt3 you know maybe we're only at like a uh you  
**Translation:** 

**[15157.46s] English:** know a couple hundred x now but you know with gpd4 turbo and 4o and there will be another one  
**Translation:** Vocabulary: turbo: 加速版

**[15161.42s] English:** probably cheaper than gpd4o even that comes out at some point and that research costs a lot a lot  
**Translation:** 

**[15167.12s] English:** of money yep exactly that's the thing that i guess is not talked about with the cost  
**Translation:** 

**[15171.68s] English:** the p that uh when you're referring to the cost of the model it's not just the training  
**Translation:** 

**[15176.74s] English:** it's not just the cost of the model it's not just the cost of the model it's not just the  
**Translation:** 

**[15177.20s] English:** or the test runs it's the actual research the the manpower yeah to do things like reasoning  
**Translation:** 

**[15183.10s] English:** right now that that exists they're going to scale it they're going to do a lot of research so i think  
**Translation:** Vocabulary: manpower: 人力

**[15186.24s] English:** i think the you know people focus on the payback question but it's really easy to like just be  
**Translation:** 

**[15191.42s] English:** like well like you know gdp is humans and industrial capital right and if you can make  
**Translation:** Vocabulary: payback: 回报

**[15196.64s] English:** intelligence cheap then you can grow a lot right that's the sort of dumb dumb way to explain it  
**Translation:** 

**[15202.00s] English:** but that's sort of what basically the investment thesis is um i think only nvidia is actually  
**Translation:** 

**[15206.86s] English:** making money right so i think that's the sort of dumb way to explain it but that's sort of what  
**Translation:** 

**[15207.18s] English:** and other hardware vendors um the hyperscalers are all on paper making money uh but in reality  
**Translation:** Vocabulary: hyperscalers: 超大规模服务商

**[15213.30s] English:** they're like spending a lot more on purchasing the gpus which you don't know if they're still  
**Translation:** 

**[15217.32s] English:** going to make this much money on each gpu in two years right um you don't know if um you know all  
**Translation:** Vocabulary: purchasing: 购买

**[15223.78s] English:** of a sudden open ai goes kapoof and now microsoft has like hundreds of thousands of gpus they were  
**Translation:** 

**[15228.74s] English:** renting to open ai that are that they paid for themselves with their you know investment in them  
**Translation:** 

**[15233.20s] English:** um you know that that no longer have a customer right like this is always a possibility  
**Translation:** 

**[15237.18s] English:** i don't believe that right um i think you know opening  
**Translation:** 

**[15240.00s] English:** will keep raising money i think others will keep raising money um because the investments the the  
**Translation:** 

**[15244.36s] English:** returns from it are going to be eventually huge once we have agi so do you think multiple companies  
**Translation:** 

**[15249.28s] English:** will get let's assume i don't think it's winner take all okay so it's not uh let's not call it  
**Translation:** 

**[15255.54s] English:** agi whatever it's like a single day it's a gradual thing super powerful ai but it's it's a gradually  
**Translation:** 

**[15262.16s] English:** increasing set of features that are useful and uh rapidly increasing rapidly rapidly increasing set  
**Translation:** 

**[15268.84s] English:** of features uh so you're saying a lot of companies will be it just seems absurd that  
**Translation:** 

**[15276.04s] English:** all of these companies are building gigantic data centers there are companies that will benefit from  
**Translation:** 

**[15282.34s] English:** ai but not because they train the best model like meta has so many avenues to benefit from ai and  
**Translation:** Vocabulary: gigantic: 巨大的

**[15287.64s] English:** all of their services people are there people spend time on meta's platforms and it's a way  
**Translation:** 

**[15292.04s] English:** to make more money per user per hour yeah it seems like google x  
**Translation:** 

**[15297.80s] English:** slash  
**Translation:** 

**[15298.82s] English:** xai slash tesla important to say and then meta will benefit not directly from the ai like the  
**Translation:** 

**[15305.10s] English:** llms but from the intelligence like the additional boost of intelligence to the products they already  
**Translation:** 

**[15312.68s] English:** sell so whether that's the recommendation system or for elon who's been talking about optimus the  
**Translation:** 

**[15318.00s] English:** robot potentially the intelligence of the robot and then you have personalized robots in the home  
**Translation:** 

**[15324.68s] English:** that kind of thing he thinks it's a 10 10 plus trillion dollar  
**Translation:** Vocabulary: trillion: 万亿

**[15328.82s] English:** business which at some point maybe i don't not soon but who knows what robotics let's do let's do a  
**Translation:** 

**[15336.60s] English:** tam analysis right eight billion humans and let's get eight billion robots right and let's let's pay  
**Translation:** 

**[15342.16s] English:** them the average salary and yeah there we go 10 trillion more than 10 trillion yeah i mean you  
**Translation:** 

**[15347.44s] English:** know if if if there's robots everywhere why does it have to be just eight eight eight billion robots  
**Translation:** 

**[15352.70s] English:** yeah of course of course i'm gonna get i'm gonna have like one robot you're gonna have like 20  
**Translation:** 

**[15356.92s] English:** yeah i mean i see you're gonna have like 20 robots you're gonna have like 20 robots you're gonna have  
**Translation:** 

**[15358.82s] English:** use case for that so yeah  
**Translation:** 

**[15360.00s] English:** Yeah. So I guess the benefit would be in the products they sell, which is why OpenAI is in a trickier position because they...  
**Translation:** Vocabulary: trickier: 更棘手

**[15366.50s] English:** All of the value of OpenAI right now as a brand is in ChatGPT.  
**Translation:** 

**[15369.82s] English:** And there is actually not that... For most users, there's not that much of a reason that they need OpenAI to be spending billions and billions of dollars on the next best model when they could just license Lama5 and Furby way cheaper.  
**Translation:** 

**[15383.10s] English:** So that's kind of like... ChatGPT is an extremely valuable entity to them.  
**Translation:** 

**[15387.82s] English:** But they could make more money just off that.  
**Translation:** 

**[15391.26s] English:** The chat application is clearly like does not have tons of room to continue, right?  
**Translation:** 

**[15395.24s] English:** Like the standard chat, right? Where you're just using it for random questions and stuff, right?  
**Translation:** 

**[15399.08s] English:** The cost continues to collapse. V3 is the latest one, biggest.  
**Translation:** 

**[15403.34s] English:** But it's going to get supported by ads, right?  
**Translation:** 

**[15405.10s] English:** Like, you know, Lama... Meta already serves 405B, probably loses the money.  
**Translation:** 

**[15409.24s] English:** But at some point, you know, they're going to get... The models are going to get so cheap that they can just serve them for free with ads supported, right?  
**Translation:** 

**[15416.12s] English:** And that's what Google is going to be able to do.  
**Translation:** 

**[15417.52s] English:** And that's obviously they've got a bigger reach, right?  
**Translation:** 

**[15419.48s] English:** So chat is not going to be the only use case.  
**Translation:** 

**[15421.76s] English:** It's like these reasoning, code, agents, computer use.  
**Translation:** 

**[15425.68s] English:** All this stuff is where OpenAI has to actually go to make money in the future.  
**Translation:** 

**[15429.06s] English:** Otherwise, they're kaputs.  
**Translation:** 

**[15430.38s] English:** But X, Google, and Meta have these other products.  
**Translation:** 

**[15435.18s] English:** So isn't it likely that OpenAI and Anthropic disappear eventually?  
**Translation:** 

**[15442.18s] English:** Unless they're so good at models, which they are.  
**Translation:** 

**[15444.30s] English:** But it's such a cutting edge.  
**Translation:** 

**[15445.34s] English:** It depends on where you think AI came from.  
**Translation:** 

**[15447.52s] English:** Where the capabilities are going.  
**Translation:** 

**[15448.50s] English:** You have to keep winning.  
**Translation:** 

**[15449.90s] English:** Yes.  
**Translation:** 

**[15450.48s] English:** You have to keep winning.  
**Translation:** 

**[15451.72s] English:** As you climb, even if the AI capabilities are going super rapidly, awesome, into the direction of AGI,  
**Translation:** 

**[15458.74s] English:** like, there's still a boost for X in terms of data.  
**Translation:** 

**[15463.24s] English:** Google, in terms of data.  
**Translation:** 

**[15464.72s] English:** Meta, in terms of data.  
**Translation:** 

**[15466.00s] English:** In terms of other products and the money.  
**Translation:** 

**[15467.86s] English:** And, like, there's just huge amounts of money.  
**Translation:** 

**[15470.06s] English:** The whole idea is human data is kind of tapped out.  
**Translation:** 

**[15472.50s] English:** We don't care.  
**Translation:** 

**[15472.94s] English:** We all care about self-play, verifiable tasks.  
**Translation:** Vocabulary: verifiable: 可验证的

**[15475.60s] English:** Yes, the self-play sandbox.  
**Translation:** 

**[15476.16s] English:** Think about AWS.  
**Translation:** Vocabulary: sandbox: 测试环境

**[15477.00s] English:** Which is an awesome thing.  
**Translation:** 

**[15477.52s] English:** I think AWS does not make a lot of money.  
**Translation:** 

**[15480.00s] English:** each individual machine and the same can be said for the most powerful ai platform which is even  
**Translation:** 

**[15486.24s] English:** though the calls to the api are so cheap there's still a lot of money to be made by owning that  
**Translation:** 

**[15491.20s] English:** platform and there's a lot of discussions as it's the next compute layer you you have to believe  
**Translation:** 

**[15496.56s] English:** that and you know there's a lot of discussions that tokens and tokenomics and llm apis are the  
**Translation:** Vocabulary: tokenomics: 代币经济

**[15501.48s] English:** next compute layer or the next paradigm for the economy kind of like energy and oil was but there's  
**Translation:** 

**[15506.34s] English:** also like you have to sort of believe that apis and chat are not where ai is stuck right it is  
**Translation:** Vocabulary: paradigm: 范式

**[15513.00s] English:** actually just tasks and agents and robotics and computer use and those are the areas where all  
**Translation:** 

**[15518.22s] English:** the value will be delivered not api not chat application right is it possible you have i mean  
**Translation:** 

**[15524.70s] English:** it all just becomes a commodity and you have uh the the very thin wrapper like perplexity  
**Translation:** 

**[15532.14s] English:** just joking uh there are a lot of wrappers making  
**Translation:** Vocabulary: commodity: 商品; wrappers: 包装

**[15536.30s] English:** it  
**Translation:** 

**[15536.34s] English:** a lot of money yeah so but but do you think it's possible that people would just even forget what  
**Translation:** 

**[15540.98s] English:** open ai and the tropic is and just because the there'll be wrappers around the api and it just  
**Translation:** 

**[15545.84s] English:** dynamically if model progress is not rapid yeah it's it's becoming a commodity right deep seek v3  
**Translation:** Vocabulary: dynamically: 动态地

**[15550.94s] English:** shows this but also the gpt3 chart earlier chart showed this right llama 3b is 1200x cheaper than  
**Translation:** 

**[15557.36s] English:** gpt3 any gpt3 like anyone whose business model was gpt3 level capabilities is dead anyone whose  
**Translation:** Vocabulary: llama: llama 模型

**[15563.22s] English:** business model is gpt4 level capabilities is dead it's dead it's dead it's dead it's dead it's dead  
**Translation:** 

**[15566.30s] English:** it is a common saying that the best businesses being made now are ones that are predicated on  
**Translation:** Vocabulary: predicated: 基于

**[15570.86s] English:** models getting better right which would be like wrappers thing that is riding the wave of the  
**Translation:** 

**[15576.38s] English:** models the short term the company that could make the most money is the one that figures out what  
**Translation:** 

**[15581.26s] English:** advertising targeting method works for language model generations we have the meta ads which are  
**Translation:** 

**[15586.80s] English:** hyper targeted in feed not within specific pieces of content and we have search ads that are used  
**Translation:** Vocabulary: hyper: 过度的

**[15592.34s] English:** by google and amazon has been rising a lot on search but within a piece with within  
**Translation:** 

**[15596.26s] English:** a return from chat gpt it is not clear how you get a  
**Translation:** 

**[15600.00s] English:** high-quality placed ad within the output.  
**Translation:** 

**[15603.12s] English:** And if you can do that with model costs coming down,  
**Translation:** 

**[15606.24s] English:** you can just get super high revenue.  
**Translation:** 

**[15609.42s] English:** Like that revenue is totally untapped  
**Translation:** Vocabulary: untapped: 未开发

**[15610.88s] English:** and it's not clear technically how it is done.  
**Translation:** 

**[15612.74s] English:** Yeah, that is, I mean,  
**Translation:** 

**[15614.52s] English:** sort of the AdSense innovation that Google did.  
**Translation:** 

**[15618.30s] English:** The one day you'll have in GPT output an ad  
**Translation:** 

**[15621.92s] English:** and that's going to make like billions.  
**Translation:** 

**[15624.42s] English:** And it could be very subtle.  
**Translation:** 

**[15625.72s] English:** It could be in conversation.  
**Translation:** 

**[15627.06s] English:** We have voice mode now.  
**Translation:** 

**[15628.06s] English:** It could be some way of making it  
**Translation:** 

**[15630.16s] English:** so the voice introduces certain things.  
**Translation:** 

**[15632.58s] English:** It's much harder to measure  
**Translation:** 

**[15633.52s] English:** and it takes imagination, but yeah.  
**Translation:** 

**[15635.92s] English:** And it wouldn't come off shady  
**Translation:** 

**[15639.02s] English:** so that you would receive public blowback,  
**Translation:** Vocabulary: blowback: 负面反应; shady: 可疑

**[15641.64s] English:** that kind of thing.  
**Translation:** 

**[15642.20s] English:** So you have to do it loud enough  
**Translation:** 

**[15643.42s] English:** to where it's clear it's an ad  
**Translation:** 

**[15644.58s] English:** and balance all of that.  
**Translation:** 

**[15646.42s] English:** So that's the open question they're trying to solve.  
**Translation:** 

**[15649.02s] English:** Anthropic and open AI, they need to.  
**Translation:** 

**[15651.42s] English:** They might not say that they care about that at all.  
**Translation:** 

**[15653.36s] English:** They don't care about it right now.  
**Translation:** 

**[15654.60s] English:** I think it's places like Perplexity  
**Translation:** 

**[15656.78s] English:** are experimenting on that more.  
**Translation:** Vocabulary: experimenting: 尝试; perplexity: 困惑

**[15658.06s] English:** Yeah, oh, interesting.  
**Translation:** 

**[15660.00s] English:** Yeah, for sure.  
**Translation:** 

**[15661.12s] English:** Like Perplexity, Google, Meta care about this.  
**Translation:** 

**[15664.00s] English:** I think open AI and Anthropic  
**Translation:** 

**[15665.74s] English:** are purely laser focused on-  
**Translation:** 

**[15668.04s] English:** AGI.  
**Translation:** 

**[15668.48s] English:** Yeah, agents and AGI.  
**Translation:** 

**[15670.54s] English:** And if I build AGI, I can make tons of money, right?  
**Translation:** 

**[15674.48s] English:** Or I can pay for everything, right?  
**Translation:** 

**[15675.94s] English:** And this is, it's just predicated  
**Translation:** 

**[15678.82s] English:** like back on the like export control thing, right?  
**Translation:** 

**[15680.60s] English:** If you think AGI is five, 10 years away or less, right?  
**Translation:** 

**[15683.60s] English:** These labs think it's two, three years away.  
**Translation:** 

**[15686.06s] English:** Obviously you're, you're, you're,  
**Translation:** 

**[15687.56s] English:** your actions are, you know,  
**Translation:** 

**[15689.66s] English:** if you assume they're rational actors,  
**Translation:** 

**[15690.98s] English:** which they are mostly,  
**Translation:** 

**[15693.32s] English:** you're, what you do in a two year AGI  
**Translation:** 

**[15695.62s] English:** versus five year versus 10 years,  
**Translation:** 

**[15697.18s] English:** very, very, very different, right?  
**Translation:** 

**[15699.90s] English:** Do you think agents are promising?  
**Translation:** 

**[15702.32s] English:** We'll have to talk about this.  
**Translation:** 

**[15703.54s] English:** This was, this is like the excitement of the year  
**Translation:** 

**[15708.04s] English:** that agents are gonna,  
**Translation:** 

**[15709.22s] English:** this is the generic hype term  
**Translation:** 

**[15713.20s] English:** that a lot of business folks are using.  
**Translation:** 

**[15714.88s] English:** AI agents are gonna revolutionize everything.  
**Translation:** 

**[15717.32s] English:** Okay, so mostly the term agent is obviously  
**Translation:** Vocabulary: revolutionize: 彻底改变

**[15720.00s] English:** overblown. We've talked a lot about reinforcement learning as a way to train for verifiable  
**Translation:** 

**[15724.54s] English:** outcomes. Agents should mean something that is open-ended and is solving a task independently  
**Translation:** Vocabulary: independently: 独立地; reinforcement: 强化; verifiable: 可验证地

**[15729.84s] English:** on its own and able to adapt to uncertainty. There's a lot of term agent applied to things  
**Translation:** 

**[15734.84s] English:** like Apple intelligence, which we still don't have after the last WWDC, which is orchestrating  
**Translation:** Vocabulary: orchestrating: 协调运作

**[15740.74s] English:** between apps. And that type of tool use thing is something that language models can do really well.  
**Translation:** 

**[15745.68s] English:** Apple intelligence, I suspect, will come eventually. It's a closed domain. It's your  
**Translation:** 

**[15750.76s] English:** messages app integrating with your photos, with AI in the background. That will work. That has  
**Translation:** 

**[15755.84s] English:** been described as an agent by a lot of software companies to get into the narrative. The question  
**Translation:** Vocabulary: integrating: 整合

**[15761.44s] English:** is, what ways can we get language models to generalize to new domains and solve their own  
**Translation:** 

**[15769.10s] English:** problems in real time? Maybe some tiny amount of training when they are doing this with fine-tuning  
**Translation:** Vocabulary: generalize: 泛化

**[15774.30s] English:** themselves or in context.  
**Translation:** 

**[15775.68s] English:** Learning, which is the idea of storing information in a prompt, and you can use learning algorithms  
**Translation:** 

**[15780.34s] English:** to update that. And whether or not you believe that that is going to actually generalize to things  
**Translation:** 

**[15786.28s] English:** like me saying, book my trip to go to Austin in two days, I have XYZ constraints and actually  
**Translation:** 

**[15794.88s] English:** trusting it. I think there's an HCI problem, coming back for information.  
**Translation:** 

**[15799.56s] English:** Well, what's your prediction there? Because my gut says we're very far away from that.  
**Translation:** 

**[15804.62s] English:** I think open AI...  
**Translation:** 

**[15805.68s] English:** Open AI's statement, I don't know if you've seen the five levels, right? Where it's chat is level  
**Translation:** 

**[15810.52s] English:** one, reasoning is level two, and then agents is level three. And I think there's a couple more  
**Translation:** 

**[15815.32s] English:** levels, but it's important to note, right? We were in chat for a couple of years, right? We just  
**Translation:** 

**[15820.56s] English:** theoretically got to reasoning. We'll be here for a year or two, right? And then agents. But at the  
**Translation:** 

**[15825.60s] English:** same time, people can try and approximate capabilities of the next level. But the agents  
**Translation:** Vocabulary: approximate: 近似; theoretically: 理论上

**[15831.56s] English:** are doing things autonomously, doing things for minutes at a time, hours at a time,  
**Translation:** 

**[15835.68s] English:** et cetera, right? Reasoning is doing things for...  
**Translation:** Vocabulary: autonomously: 独立自主

**[15840.00s] English:** tens of seconds at a time. Right. And then coming back with an output that I still need to verify  
**Translation:** 

**[15843.76s] English:** and use and try to check out. Right. So, and the biggest problem is of course, like it's the same  
**Translation:** Vocabulary: verify: 验证

**[15849.84s] English:** thing with manufacturing, right? Like there's the whole six Sigma thing, right? Like, you know,  
**Translation:** 

**[15853.08s] English:** how many nines do you get? And then you compound the nines onto each other. And it's like, if you  
**Translation:** Vocabulary: sigma: 六西格玛

**[15856.78s] English:** multiply, you know, by the number of steps that are six Sigma, you get to you know, a yield,  
**Translation:** 

**[15862.98s] English:** a yield or something. Right. So like in semiconductor manufacturing, tens of thousands  
**Translation:** Vocabulary: multiply: 增加; semiconductor: 半导体

**[15866.10s] English:** of steps, nine, nine, nine, nine, nine, nine, nine is not enough. Right. Cause you multiply  
**Translation:** 

**[15870.60s] English:** that by that many times, you actually end up with like 60% yield or zero or zero. And this is the  
**Translation:** 

**[15876.90s] English:** same thing with agents, right? Like chaining tasks together each time, LLMs, even the best LLMs in  
**Translation:** 

**[15883.32s] English:** particularly pretty good benchmarks don't get a hundred percent, right? They get a little bit  
**Translation:** Vocabulary: benchmarks: 评估标准

**[15888.80s] English:** below that because there's a lot of noise. And so how do you get to enough nines, right? This is the  
**Translation:** 

**[15894.88s] English:** same thing with self-driving.  
**Translation:** 

**[15896.10s] English:** We don't, we can't have self-driving because without it being like super geo-fenced, like  
**Translation:** 

**[15899.88s] English:** Google, like Google's right. And even then they have a bunch of tele operators to make sure it  
**Translation:** 

**[15903.28s] English:** doesn't get stuck. Right. But you can't do that because it doesn't have enough nines.  
**Translation:** 

**[15906.94s] English:** And self-driving has quite a lot of structure because roads have rules. It's well-defined,  
**Translation:** 

**[15913.94s] English:** there's regulation. When you're talking about computer use for the open web, for example,  
**Translation:** 

**[15919.76s] English:** or the open operating system, like there's no, it's a mess. So like the possibility,  
**Translation:** 

**[15926.10s] English:** I'm always skeptical of any system that is tasked with interacting with the human world,  
**Translation:** 

**[15934.80s] English:** with the open, messy human world.  
**Translation:** Vocabulary: skeptical: 怀疑的

**[15936.36s] English:** That's the thing. If we can't get intelligence, that's enough to solve the human world on its  
**Translation:** 

**[15940.74s] English:** own. We can create infrastructure, like the human operators for Waymo over many years that enable  
**Translation:** 

**[15946.70s] English:** certain workflows.  
**Translation:** 

**[15947.64s] English:** There is a company, I don't remember it, but it is, but that's literally their pitches. Yeah. We're  
**Translation:** 

**[15951.46s] English:** just going to be the human operator when agents fail and you just call us and we fix it.  
**Translation:** 

**[15954.88s] English:** Yeah.  
**Translation:** 

**[15956.10s] English:** I call it, it's hilarious. There's going to be teleoperation markets when we get human robots.  
**Translation:** 

**[15960.00s] English:** is there's going to be somebody around the world that's happy to fix the fact that it can't finish  
**Translation:** Vocabulary: teleoperation: 远程操作

**[15964.90s] English:** loading my dishwasher when i'm unhappy with it but that's just going to be part of the tesla  
**Translation:** 

**[15969.26s] English:** service package i'm just imagining like an ai agent talking to another ai agent one company  
**Translation:** Vocabulary: dishwasher: 洗碗机

**[15976.08s] English:** has an agent that specializes in helping other ai agents but if you can make things that are  
**Translation:** 

**[15981.98s] English:** good at one step you can yeah you can stack them together so that's why i'm like if it takes a long  
**Translation:** 

**[15987.36s] English:** time we're going to build infrastructure that enables it you see the operator launch they have  
**Translation:** 

**[15991.82s] English:** partnerships with certain websites with doordash with open table with things like this those  
**Translation:** Vocabulary: doordash: 送餐服务; partnerships: 合作关系

**[15997.46s] English:** partnerships are going to let them climb really fast their model is going to get really good at  
**Translation:** 

**[16000.94s] English:** those things it's going to proof of concept that might be a network effect where more companies  
**Translation:** 

**[16005.42s] English:** want to make it easier for ai some companies will be like no let's put blockers in place  
**Translation:** 

**[16010.78s] English:** yeah and this is the story of the internet we've seen we see it now with training data for language  
**Translation:** 

**[16015.26s] English:** models where companies are like no you have to pay  
**Translation:** 

**[16017.36s] English:** like business working it out that said i think like airlines have a very and hotels have high  
**Translation:** 

**[16024.84s] English:** incentive to make their site work really well and they usually don't like if you look at how many  
**Translation:** 

**[16030.78s] English:** clicks it takes to order a airplane ticket it's insane i don't you actually can't call an american  
**Translation:** Vocabulary: incentive: 激励

**[16036.12s] English:** airlines agent anymore they they don't have a phone number it's i mean it's it's it's horrible  
**Translation:** 

**[16041.72s] English:** on many on the interface front and and all to imagine that agents will be able to deal with  
**Translation:** Vocabulary: interface: 界面

**[16046.48s] English:** that website  
**Translation:** 

**[16047.36s] English:** when i as a human struggle like i have an existential crisis every time i try to book  
**Translation:** 

**[16052.24s] English:** an airplane ticket that i i don't i think it's going to be extremely difficult to build an ai  
**Translation:** 

**[16058.36s] English:** ai agent that's robust but think about like united has accepted the starlink term which is they have  
**Translation:** Vocabulary: robust: 强壮稳定; starlink: 星链

**[16063.94s] English:** to provide starlink for free and the users are going to love it what if one airline is like  
**Translation:** 

**[16068.50s] English:** we're going to take a year and we're going to make our website have white text that works  
**Translation:** 

**[16072.92s] English:** perfectly for the ais every time anyone asks about an ai flight  
**Translation:** 

**[16077.36s] English:** they buy whatever airline it is or like  
**Translation:** 

**[16080.00s] English:** just like here's an api and it's only exposed to ai agents and if anyone queries it the price is 10  
**Translation:** 

**[16085.38s] English:** higher and and for any flight but we'll let you see any of our flights and you can just book any  
**Translation:** 

**[16090.02s] English:** of them here you go agent man then it's like oh and i made 10 higher price awesome yeah and like  
**Translation:** 

**[16094.94s] English:** am i willing to say that for like hey book me a flight to see lex right and it's like yeah whatever  
**Translation:** 

**[16098.62s] English:** yeah yeah i think i think you know computers and real world and the open world are really really  
**Translation:** 

**[16105.00s] English:** messy um but if you start defining the problem and narrow regions people are going to be able  
**Translation:** 

**[16111.00s] English:** to create very very productive things um and and ratchet down cost massively right like now crazy  
**Translation:** 

**[16118.54s] English:** things like you know robotics in the home you know those are going to be a lot harder to do  
**Translation:** Vocabulary: massively: 大幅度地

**[16123.44s] English:** just like self-driving right because there's just a billion different failure modes right but but  
**Translation:** 

**[16128.74s] English:** like agents that can like navigate a certain set of websites and do certain sets of tasks  
**Translation:** Vocabulary: navigate: 浏览

**[16133.62s] English:** or like look at  
**Translation:** 

**[16135.00s] English:** you know look at your you know take a photo of your grocery uh your fridge and or like upload  
**Translation:** Vocabulary: grocery: 杂货

**[16139.04s] English:** your recipes and then like it figures out what to order from you know uh amazon slash whole foods  
**Translation:** 

**[16143.94s] English:** food delivery like that's then that's going to be like pretty quick and easy to do i think so it's  
**Translation:** 

**[16147.72s] English:** going to be be a whole range of like business outcomes and it's going to be tons of tons of  
**Translation:** 

**[16151.80s] English:** sort of optimism around people can just figure out ways to make money to be clear these sandboxes  
**Translation:** Vocabulary: optimism: 乐观; sandboxes: 试验空间

**[16155.72s] English:** already exist in research there are people who have built clones of all the most popular websites  
**Translation:** 

**[16160.28s] English:** of google amazon blah blah blah to make it so that there's  
**Translation:** 

**[16164.28s] English:** i mean  
**Translation:** 

**[16164.98s] English:** openai probably has them internally to train these things it's the same as deepmind's robotics team  
**Translation:** Vocabulary: internally: 内部地

**[16169.06s] English:** for years has had clusters for robotics where you like you interact with robots fully remotely they  
**Translation:** 

**[16174.58s] English:** just have a lab in london and you send tasks to it arrange the blocks and you do this research  
**Translation:** Vocabulary: clusters: 机器人集群; remotely: 远程

**[16179.62s] English:** obviously there's techs there that fix stuff but we've turned these cranks of automation before  
**Translation:** 

**[16186.26s] English:** you go from sandbox to progress and then you add one more domain at a time  
**Translation:** Vocabulary: automation: 自动化; cranks: 旋钮; sandbox: 沙盒

**[16190.98s] English:** and generalize i think in the history of nlp and language processing  
**Translation:** 

**[16194.98s] English:** instruction tuning and tasks per language model used to be like one language model did one task  
**Translation:** Vocabulary: generalize: 泛化

**[16200.00s] English:** And then in the instruction tuning literature, there's this point where you start adding more and more tasks together, where it just starts to generalize to every task.  
**Translation:** 

**[16207.34s] English:** And we don't know where on this curve we are.  
**Translation:** 

**[16208.96s] English:** I think for reasoning with this RL and verifiable domains, we're early, but we don't know where the point is where you just start training on enough domains and poof, like more domains just start working and you've crossed the generalization barrier.  
**Translation:** 

**[16222.08s] English:** Well, what do you think about the programming context?  
**Translation:** Vocabulary: generalization: 泛化; verifiable: 可验证

**[16225.82s] English:** So software engineering.  
**Translation:** 

**[16227.06s] English:** That's where I personally and I know a lot of people interact with AI the most.  
**Translation:** 

**[16234.58s] English:** There's a lot of fear and angst too from current CS students, but there's also, that's where, that is the area where probably the most AI revenue and productivity gains have come, right?  
**Translation:** 

**[16244.32s] English:** Whether it be co-pilots or cursor or what have you, right?  
**Translation:** Vocabulary: angst: 焦虑

**[16248.24s] English:** This is, or just standard chat GPT, right?  
**Translation:** 

**[16250.40s] English:** Like a lot of, I know very few programmers who don't have chat GPT and actually many of them have the $200 tier because that's what.  
**Translation:** 

**[16257.06s] English:** It's so good for, right?  
**Translation:** 

**[16259.04s] English:** I think that in that world, we already see it like SweBench.  
**Translation:** 

**[16264.02s] English:** And if you've looked at the benchmark made by some Stanford students, I wouldn't say it's like really hard, but I wouldn't say it's easy either.  
**Translation:** 

**[16270.26s] English:** I think like it takes someone who's been through at least, you know, a few years of CS or a couple of years of programming to do SweBench well.  
**Translation:** Vocabulary: benchmark: 参考标准

**[16276.88s] English:** And the models went from 4% to 60% in like a year, right?  
**Translation:** 

**[16281.86s] English:** And where are they going to go to next year?  
**Translation:** 

**[16283.80s] English:** You know, it's going to be higher.  
**Translation:** 

**[16284.94s] English:** It probably won't be 100% because again, that 9%.  
**Translation:** 

**[16287.06s] English:** This is like really hard to do, but we're going to get to some point where that's, and then we're going to need harder software engineering benchmarks and so on and so forth.  
**Translation:** 

**[16293.98s] English:** But the way that like people think of it now is it can do code completion easy.  
**Translation:** Vocabulary: benchmarks: 衡量标准

**[16298.92s] English:** It can do some function generation and I have to review it.  
**Translation:** 

**[16301.40s] English:** Great.  
**Translation:** 

**[16301.92s] English:** But really the like software engineering agents, I think can be done faster, sooner than any other agent because it is a verifiable domain.  
**Translation:** 

**[16310.06s] English:** You can always like unit test or compile.  
**Translation:** 

**[16313.04s] English:** And there's many different regions of like.  
**Translation:** 

**[16317.06s] English:** It can inspect the whole code base at once, which no, no engineer.  
**Translation:** 

**[16320.00s] English:** really can only the architects can really think about this stuff the really senior guys and they  
**Translation:** 

**[16324.00s] English:** can define stuff and then the agent can execute on it so i think i think software engineering costs  
**Translation:** 

**[16328.48s] English:** are going to plummet like crazy and and one interesting aspect of that is when software  
**Translation:** 

**[16332.92s] English:** engineering costs are really low you get very different markets right so in the u.s you have  
**Translation:** Vocabulary: plummet: 急剧下降

**[16337.54s] English:** all these platform sas companies right salesforce and so on and so forth right in in china no one  
**Translation:** 

**[16343.80s] English:** uses platform sas everyone just builds their own stack because software engineering is much  
**Translation:** Vocabulary: salesforce: 销售力士

**[16349.90s] English:** cheaper in china and partially because like people stem number of stem graduates etc uh so  
**Translation:** 

**[16354.86s] English:** stem so it's generally just cheaper to do um and so at the same time code for l like code lms have  
**Translation:** 

**[16361.30s] English:** been adopted much less in china because the cost of an engineer there is much lower but like what  
**Translation:** 

**[16365.74s] English:** happens when every company can just invent their own business logic like really cheaply and quickly  
**Translation:** 

**[16369.60s] English:** you stop using platform sas you start building custom tailored solutions you change them really  
**Translation:** 

**[16374.34s] English:** quickly now all of a sudden your business is a little bit more efficient too potentially because  
**Translation:** Vocabulary: tailored: 量身定制

**[16377.56s] English:** you're not dealing with the hell that is like some  
**Translation:** 

**[16379.76s] English:** you're not dealing with the hell that is like some  
**Translation:** 

**[16379.88s] English:** you're not dealing with the hell that is like some  
**Translation:** 

**[16379.90s] English:** platform sas company stuff not working perfectly and having to adjust workflows or random business  
**Translation:** 

**[16385.08s] English:** automation cases that aren't necessarily ai required it's just logic that needs to be built  
**Translation:** 

**[16389.26s] English:** that no one has built right all of these things can go happen faster and so i think software and  
**Translation:** Vocabulary: automation: 自动化

**[16393.22s] English:** then and then the other domain is like industrial chemical mechanical engineers suck at coding  
**Translation:** 

**[16397.72s] English:** right uh just generally and like their tools like semiconductor engineers their tools are 20 years  
**Translation:** 

**[16401.98s] English:** old all the tools run on xp including asml lithography tools run on windows xp right it's  
**Translation:** 

**[16409.88s] English:** all the tools run on xp including asml lithography tools run on windows xp right it's  
**Translation:** Vocabulary: lithography: 光刻技术

**[16411.56s] English:** just like guys you guys can move 20 years forward with all the data you have and gathered and do a  
**Translation:** 

**[16416.14s] English:** lot better it's just you need the engineering skills for software engineering to be delivered  
**Translation:** 

**[16420.46s] English:** to the actual domain expert engineers so i think i think that's the area where i'm like super duper  
**Translation:** 

**[16424.66s] English:** bullish of of generally ai creating value the big picture is that i don't think it's going to be a  
**Translation:** Vocabulary: bullish: 看涨

**[16430.24s] English:** clip it's like we talked to anything a really good example of how growth changes is when meta  
**Translation:** 

**[16437.94s] English:** added stories so snapchat was on an  
**Translation:** 

**[16439.76s] English:** I expect.  
**Translation:** 

**[16440.00s] English:** exponential they added stories it flatlined software engineers then up into the right  
**Translation:** Vocabulary: exponential: 指数增长; flatlined: 停滞不前

**[16445.00s] English:** ai is going to come in it's probably just going to be flat it's like it's a lot like everyone's  
**Translation:** 

**[16449.10s] English:** going to lose their job it's hard because the supply corrects more slowly so the amount of  
**Translation:** 

**[16454.20s] English:** students is still growing and that'll correct on a multi-year like a year delay but the amount of  
**Translation:** 

**[16460.02s] English:** jobs will just turn and then maybe in 20 40 years it'll be well down but in the few years there'll  
**Translation:** 

**[16467.24s] English:** never going to be the snap moment where it's like software engineers aren't useful i think also the  
**Translation:** 

**[16471.12s] English:** nature of what it means to be a programmer and what kind of jobs programmers do changes because i  
**Translation:** Vocabulary: programmer: 程序员; programmers: 程序员

**[16476.00s] English:** think there needs to be a human in the loop of everything you've talked about there's a really  
**Translation:** 

**[16482.38s] English:** important human in that picture of like correcting the code like fixing larger than the context  
**Translation:** 

**[16490.50s] English:** length yep and debugging also like debugging by sort of reading the code understanding  
**Translation:** 

**[16497.18s] English:** understanding  
**Translation:** 

**[16497.22s] English:** the steering the system like no no you missed the point adding more to the prompt kind of like  
**Translation:** 

**[16502.82s] English:** yes adding the human designing the perfect google button google's famous for having people design  
**Translation:** Vocabulary: steering: 操控

**[16508.96s] English:** buttons that are so perfect and it's like how like how is ai going to do that like it's like  
**Translation:** 

**[16513.78s] English:** they could give you all the ideas perfect i mean that's the thing you can call it taste humans have  
**Translation:** 

**[16520.36s] English:** one thing humans can do is figure out what other humans enjoy better than ai systems that's where  
**Translation:** 

**[16525.98s] English:** the preference you  
**Translation:** 

**[16527.16s] English:** loading that in but ultimately humans are the greatest preference generate that's where the  
**Translation:** 

**[16531.80s] English:** preference comes from and humans are actually very good at reading or like judging between two things  
**Translation:** 

**[16536.68s] English:** versus this is this goes back to the core of what rlhf and preference tuning is is that it's hard  
**Translation:** 

**[16541.12s] English:** to generate a good answer for a lot of problems but it's easy to see which one is better and that's  
**Translation:** 

**[16545.32s] English:** how we're using a humans for ai now is judging which one is better and that's what software  
**Translation:** 

**[16549.64s] English:** engineering could look like it's the pr review here's a few options what are the like here's  
**Translation:** 

**[16555.10s] English:** some potential pros and cons  
**Translation:** 

**[16557.16s] English:** and they're going to be judgment judges  
**Translation:** 

**[16560.00s] English:** think the thing i would very much recommend is people start programmers start using ai  
**Translation:** 

**[16565.04s] English:** and embracing that role of the supervisor of the ai system and like partner the ai system  
**Translation:** Vocabulary: embracing: 接纳; supervisor: 监督者

**[16570.96s] English:** versus writing from scratch or not learning coding at all and just generating stuff because i think  
**Translation:** 

**[16577.22s] English:** there actually has to be a pretty high level of expertise as a programmer to be able to manage  
**Translation:** 

**[16581.64s] English:** increasingly intelligent systems i think it's i think it's that and then becoming a domain expert  
**Translation:** 

**[16586.36s] English:** in something sure yeah right because you like seriously if you go look at aerospace or  
**Translation:** Vocabulary: aerospace: 航空航天

**[16590.66s] English:** semiconductors or chemical engineering everyone is using really crappy platforms really old software  
**Translation:** 

**[16595.88s] English:** like the job of the data sciences is like is like a joke right in many cases um in many cases it's  
**Translation:** Vocabulary: crappy: 糟糕的; semiconductors: 半导体

**[16602.00s] English:** very real but it's like bring what the forefront of human capabilities are to your domain and like  
**Translation:** 

**[16607.16s] English:** even if the forefront is like from the ai your domain you're like at the forefront right so it's  
**Translation:** Vocabulary: forefront: 前沿

**[16611.20s] English:** like it's like you have to be at the forefront of something and then leverage the the like rising  
**Translation:** 

**[16615.74s] English:** tide that is the forefront of something and then leverage the the like rising tide that is the  
**Translation:** Vocabulary: leverage: 利用

**[16616.34s] English:** ai for everything else oh yeah there's so many low-hanging fruit everywhere in terms of where  
**Translation:** 

**[16622.56s] English:** software can like help automate a thing or digitize a thing in in a legal system i mean that's why  
**Translation:** Vocabulary: automate: 自动化; digitize: 数字化

**[16629.28s] English:** doge is exciting you have i mean i got to uh hang out with a bunch of the doge folks and they  
**Translation:** 

**[16636.40s] English:** i mean government is like so old school it it's like begging for the modernization of software of  
**Translation:** Vocabulary: modernization: 现代化

**[16645.74s] English:** organizing and and and and and and and and and and and and and and and and and and and and and  
**Translation:** 

**[16646.32s] English:** the data all this kind of stuff i mean in that case is by design because bureaucracy create  
**Translation:** Vocabulary: bureaucracy: 官僚体系

**[16651.84s] English:** protects centers of power and so on but software breaks down those barriers uh so it hurts  
**Translation:** 

**[16660.46s] English:** those that are holding on to power but ultimately benefits humanity so uh there's a bunch of domains  
**Translation:** Vocabulary: barriers: 障碍

**[16667.32s] English:** of that kind one thing we uh didn't fully finish talking about is open source so first of all  
**Translation:** 

**[16675.50s] English:** congrats you released a new model yeah this is tulu  
**Translation:** Vocabulary: congrats: 恭喜

**[16680.00s] English:** I'll explain what a Tulu is.  
**Translation:** 

**[16681.52s] English:** A Tulu is a hybrid camel when you breed a Dromedary with a Bacchian camel.  
**Translation:** Vocabulary: bacchian: 贝卡尼; dromedary: 单峰驼

**[16686.38s] English:** Back in the early days after ChatGPT, there was a big wave of models coming out like Alpaca,  
**Translation:** 

**[16691.38s] English:** Vicuna, et cetera, that were all named after various mammalian species.  
**Translation:** Vocabulary: alpaca: 羊驼; mammalian: 哺乳动物; vicuna: 羊驼

**[16695.52s] English:** So Tulu, the brand is multiple years old, which comes from that.  
**Translation:** 

**[16700.10s] English:** And we've been playing at the frontiers of post-training with open source code.  
**Translation:** Vocabulary: frontiers: 前沿

**[16705.32s] English:** And this first part of this release was in the fall where we've built on LLAMA's open  
**Translation:** 

**[16712.48s] English:** models, open weight models, and then we add in our fully open code, our fully open data.  
**Translation:** 

**[16717.82s] English:** There's a popular benchmark that is Chatbot Arena, and that's generally the metric by  
**Translation:** 

**[16722.44s] English:** which how these chat models are evaluated.  
**Translation:** Vocabulary: benchmark: 衡量标准; evaluated: 评估

**[16724.94s] English:** And it's humans compare random models from different organizations.  
**Translation:** 

**[16728.68s] English:** And if you looked at the leaderboard in November or December, among the top 60 models from  
**Translation:** Vocabulary: leaderboard: 排行榜

**[16733.70s] English:** 10s to 20s of organizations, there was a lot of chatbot arena.  
**Translation:** 

**[16735.32s] English:** None of them had open code or data for just post-training.  
**Translation:** 

**[16738.56s] English:** Among that, even fewer or none have pre-training data and code available.  
**Translation:** 

**[16742.06s] English:** But post-training is much more accessible at this time.  
**Translation:** 

**[16744.42s] English:** It's still pretty cheap and you can do it.  
**Translation:** 

**[16746.32s] English:** And the thing is, how high can we push this number where people have access to all the  
**Translation:** 

**[16750.32s] English:** code and data?  
**Translation:** 

**[16751.36s] English:** So that's kind of the motivation of the project.  
**Translation:** 

**[16752.88s] English:** We draw on lessons from LLAMA.  
**Translation:** 

**[16754.40s] English:** NVIDIA had a Nemotron model where the recipe for their post-training was fairly open with  
**Translation:** Vocabulary: nemotron: 聂摩汀模型

**[16759.32s] English:** some data and a paper.  
**Translation:** 

**[16761.46s] English:** And it's putting all these together to try to create a recipe that people can  
**Translation:** 

**[16764.74s] English:** fine-tune models like GPT-4 to their domain.  
**Translation:** 

**[16767.86s] English:** So to be clear, in the case of TULU, maybe you can talk about ALMA too, but in the case  
**Translation:** 

**[16772.94s] English:** of TULU, you're taking LLAMA 3, 4, 5B.  
**Translation:** 

**[16778.92s] English:** TULU has been a series of recipes for post-training.  
**Translation:** 

**[16781.44s] English:** So we've done multiple models over years.  
**Translation:** 

**[16783.56s] English:** And so you're open sourcing everything.  
**Translation:** Vocabulary: sourcing: 采购

**[16786.68s] English:** Yeah.  
**Translation:** 

**[16786.96s] English:** If you start with an open weight-based model, the whole model technically is an open source  
**Translation:** 

**[16791.48s] English:** because you don't know what LLAMA put into it.  
**Translation:** 

**[16793.56s] English:** Which is why we have this.  
**Translation:** 

**[16794.78s] English:** It's a separate thing that we'll get to.  
**Translation:** 

**[16795.92s] English:** But it's just getting parts of the pipeline where people can zoom in and customize.  
**Translation:** Vocabulary: pipeline: 管道

**[16800.00s] English:** eyes i know i hear from startups and businesses they're like okay like i can take this post  
**Translation:** 

**[16803.60s] English:** training and try to apply it to my domain we talk about verifiers a lot we use this idea which is  
**Translation:** Vocabulary: startups: 初创企业; verifiers: 验证者

**[16808.96s] English:** reinforcement learning with verifiable domain rewards rlvr kind of similar to rlhf and we  
**Translation:** 

**[16816.72s] English:** applied it to map and the model today which is like we applied it to the llama 405b base model  
**Translation:** Vocabulary: llama: 羊驼; reinforcement: 强化; verifiable: 可验证

**[16822.80s] English:** from last year and we have our other stuff we have our instruction tuning  
**Translation:** 

**[16826.76s] English:** and or preference tuning but the math thing is interesting which is like it's easier to improve  
**Translation:** 

**[16832.88s] English:** this math benchmark there's a benchmark m-a-t-h math all capitals tough name when the benchmark  
**Translation:** 

**[16838.98s] English:** is name is the area that you're evaluating we're researchers we're not we're not brands  
**Translation:** Vocabulary: evaluating: 评估

**[16843.28s] English:** brand strategists and this is something that the deep seek paper talked about as well as like at  
**Translation:** 

**[16848.62s] English:** this bigger model it's easier to elicit powerful capabilities with this rl training and then they  
**Translation:** Vocabulary: elicit: 诱发; strategists: 策略师

**[16853.80s] English:** distill it down from that big model to the small model and  
**Translation:** 

**[16856.76s] English:** this model we released today we saw the same thing as we're at ai2 we don't have a ton of  
**Translation:** Vocabulary: distill: 提炼

**[16861.86s] English:** compute we can't train 405b models all the time so we just did a few runs and they tend to work  
**Translation:** 

**[16866.70s] English:** and it's like it just shows that there's a lot of room for people to play in these things and that  
**Translation:** 

**[16872.58s] English:** and they crushed llama's actual release right like the they're way better than it yeah so our  
**Translation:** 

**[16877.38s] English:** valve numbers i mean we have extra months in this but our valve numbers are like much better than  
**Translation:** Vocabulary: valve: 阀门

**[16881.46s] English:** the llama instruct model that they released and then you also said better than deep seek v3  
**Translation:** 

**[16886.76s] English:** on our eval benchmark the most deep seek v3 is really similar we have a safety benchmark to  
**Translation:** Vocabulary: benchmark: 评估基准; instruct: 指导

**[16892.56s] English:** understand if it will say harmful things and things like that and that's what draws down most  
**Translation:** 

**[16896.54s] English:** of the way it's still it's like an amalgamation of multiple benchmarks or what do you mean yeah  
**Translation:** Vocabulary: amalgamation: 混合体; benchmarks: 参考标准

**[16900.32s] English:** so we have a 10 value this is like this is standard practice in post-training is you choose  
**Translation:** 

**[16903.96s] English:** your evaluations you care about in academics and smaller labs you'll have fewer evaluations  
**Translation:** Vocabulary: evaluations: 评估

**[16908.66s] English:** in companies you'll have a really one domain that you really care about in frontier labs you'll have  
**Translation:** 

**[16913.22s] English:** 10s to 20s to maybe even like 100 evaluations of specific things  
**Translation:** Vocabulary: frontier: 前沿领域

**[16916.76s] English:** so we choose a representative suite of things that look like chat  
**Translation:** 

**[16920.00s] English:** precise instruction following which is like respond only in emojis like does the model  
**Translation:** 

**[16924.20s] English:** follow weird things like that yeah math code and you create a suite like this so safety would be  
**Translation:** 

**[16928.90s] English:** one of 10 in that type of suite where you have like what is the broader community of ai care  
**Translation:** 

**[16933.96s] English:** about and for example in comparison to deep seek it would be something like our average eval for  
**Translation:** 

**[16938.86s] English:** our model would be um 80 including safety and similar without and deep seek would be like 79  
**Translation:** 

**[16944.72s] English:** percent average score without safety and their safety score would bring it down like oh so you  
**Translation:** 

**[16952.22s] English:** beat them even ignoring safety yeah so this is something that internally it's like i don't want  
**Translation:** Vocabulary: internally: 内部地

**[16957.10s] English:** to win only by like how you shape the eval benchmark so if there's something that's like  
**Translation:** 

**[16960.62s] English:** people may or may not care about safety in their model safety can come downstream safety can be  
**Translation:** 

**[16965.04s] English:** when you host the model for an api like safety is addressed in a spectrum of locations in a  
**Translation:** 

**[16969.86s] English:** application so it's like if you want to say that you have the best recipe you can't just gate it  
**Translation:** 

**[16973.62s] English:** on these things that some people don't know about you can't just say that you have the best recipe  
**Translation:** 

**[16974.70s] English:** people might not want and and this is because it's like the time of progress we benefit if we  
**Translation:** 

**[16981.74s] English:** can release a model later we have more time to learn new techniques like this rl technique we  
**Translation:** 

**[16986.28s] English:** had started this in the fall it's now really popular reasoning models the next thing to do  
**Translation:** 

**[16990.74s] English:** for open source post training is to scale up verifiers to scale up data to replicate some  
**Translation:** 

**[16995.78s] English:** of deep seek's results and it's awesome that we have a paper to draw on and it makes it a lot  
**Translation:** Vocabulary: verifiers: 验证者

**[16999.62s] English:** easier and that's the type of things that is going on among  
**Translation:** 

**[17004.54s] English:** you  
**Translation:** 

**[17004.70s] English:** academic and closed frontier research in ai since you're pushing open source what do you think is  
**Translation:** 

**[17010.34s] English:** the future of it you think deep seek actually changes things since it's open source or open  
**Translation:** 

**[17015.74s] English:** weight or is pushing the open source movement into the open direction this goes very back to  
**Translation:** 

**[17020.02s] English:** license discussion so deep seek r1 with a friendly license is a major reset so it's like the first  
**Translation:** 

**[17024.80s] English:** time that we've had a really clear frontier model that is open weights and with a commercially  
**Translation:** 

**[17030.06s] English:** friendly license with no restrictions on downstream use cases synthetic data distillation whatever  
**Translation:** Vocabulary: commercially: 商业上; distillation: 提炼; synthetic: 合成

**[17034.70s] English:** this has never been the case at all in the history of ai in the last few years since chachi bt there have  
**Translation:** 

**[17039.86s] English:** been  
**Translation:** 

**[17040.00s] English:** models that are off the frontier or models with weird licenses that you can't really use them  
**Translation:** 

**[17043.98s] English:** so is isn't meta's license like pretty much permissible except for five companies  
**Translation:** Vocabulary: frontier: 边界; permissible: 允许的

**[17048.42s] English:** um and there's also so this goes to like what open source ai is which is there's also use case  
**Translation:** 

**[17054.18s] English:** restrictions in the llama license which says you can't use it for specific things so if you come  
**Translation:** Vocabulary: llama: 羊驼模型

**[17058.24s] English:** from an open source software background you would say that that is not an open source license what  
**Translation:** 

**[17062.40s] English:** kind of things are those though like are they like it's i at this point i can't pull them off  
**Translation:** 

**[17067.08s] English:** but it'll be like competitor it used to be military use was one and they removed that  
**Translation:** 

**[17071.64s] English:** for scale it'll be like like c-sam like child abuse material or like that's the type of thing  
**Translation:** 

**[17078.46s] English:** that is forbidden there but that's enough from an open source background to say it's not open  
**Translation:** 

**[17082.68s] English:** source license and also the llama license has this horrible thing where you have to name your model  
**Translation:** 

**[17087.78s] English:** llama if you touch it to the llama model so it's like the branding thing so if a company uses llama  
**Translation:** 

**[17093.48s] English:** technically the license says that they should say built with llama at the bottom of their  
**Translation:** 

**[17096.84s] English:** application  
**Translation:** 

**[17097.08s] English:** and from like a marketing perspective that just that just hurts like i can i could suck it up as  
**Translation:** 

**[17101.42s] English:** a researcher i'm like oh it's fine like it says llama dash on all of our on all of our materials  
**Translation:** 

**[17106.12s] English:** for this release but this is why we need truly open models which is uh we don't know deep seek  
**Translation:** 

**[17111.06s] English:** r1's data so you're saying i can't make a you know cheap copy of llama and pretend it's mine  
**Translation:** 

**[17115.92s] English:** but i can do this with the chinese model yeah hell yeah that's that's what i'm saying and yeah  
**Translation:** 

**[17121.56s] English:** and that's why it's like we want this whole open language models thing the olmo thing is  
**Translation:** 

**[17126.84s] English:** to try to keep the model where everything is open with the data as close to the frontier as  
**Translation:** 

**[17131.56s] English:** possible so we're compute constrained we're personnel constrained we're we rely on getting  
**Translation:** 

**[17136.26s] English:** insights from people like john shulman tells us to do rl on outputs like we can make these big  
**Translation:** Vocabulary: constrained: 资源有限

**[17141.12s] English:** jumps but it just takes a long time to push the frontier of open source and fundamentally i would  
**Translation:** 

**[17146.88s] English:** say that that's because open source ai does not have the same feedback loops as open source  
**Translation:** Vocabulary: fundamentally: 从根本上

**[17151.44s] English:** software we talked about open source software for security also it's just because you build something  
**Translation:** 

**[17156.84s] English:** you can reuse it if you go into a new company there's so many benefits  
**Translation:** Vocabulary: reuse: 重复利用

**[17160.00s] English:** But if you open source a language model, you have you have this data sitting around, you have this training code. It's not like that easy for someone to come and build on and improve because you need to spend a lot on compute. You need to have expertise. So until there are feedback loops of open source AI, it seems like mostly an ideological mission.  
**Translation:** 

**[17177.90s] English:** Like people like Mark Zuckerberg, which is like America needs this. And I agree with him. But in the time where the motivation ideologically is high, we need to capitalize and build this ecosystem around what benefits do you get from seeing the language model data.  
**Translation:** Vocabulary: capitalize: 利用收益; ideological: 意识形态的; ideologically: 从意识形态角度

**[17193.14s] English:** And there's not a lot about that. We're going to try to launch a demo soon where you can look at an OMO model and a query and see what pre-training data is similar to it, which is like legally risky and complicated.  
**Translation:** 

**[17204.34s] English:** But it's like, what does it mean to see the data?  
**Translation:** 

**[17207.38s] English:** That the AI was trained on? It's hard to parse. It's terabytes of files. It's like, I don't know what I'm going to find in there.  
**Translation:** 

**[17214.10s] English:** But that's what that's what we need to do as an ecosystem. If people want open source AI to be financially useful.  
**Translation:** Vocabulary: financially: 经济效益; parse: 解析; terabytes: 太字节

**[17221.08s] English:** We didn't really talk about Stargate. I would love to get your opinion on like what the new administration, the Trump administration, everything that's doing that's being done in from the America side and supporting AI infrastructure and the efforts of the different AI companies.  
**Translation:** 

**[17236.00s] English:** What do you think about Stargate?  
**Translation:** Vocabulary: stargate: 星际之门

**[17237.40s] English:** What are we supposed to think about Stargate? And does Sam have the money?  
**Translation:** 

**[17243.30s] English:** Yeah, so I think Stargate is a opaque thing. It definitely doesn't have $500 billion. Doesn't even have $100 billion, right?  
**Translation:** 

**[17250.66s] English:** So what they announced is this $500 billion number, Larry Ellison, Sam Altman, and Trump said it.  
**Translation:** 

**[17257.00s] English:** They thanked Trump and Trump did do some executive actions that like do significantly improve the ability for this to be built faster.  
**Translation:** Vocabulary: altman: 萨姆·阿尔特曼; ellison: 拉里·埃利森

**[17267.38s] English:** You know, one of the executive actions he did is on federal land, you can just basically build data centers in power, you know, like pretty much like that.  
**Translation:** 

**[17274.32s] English:** And then the permitting process is basically gone or you file after the fact.  
**Translation:** Vocabulary: permitting: 许可程序

**[17277.90s] English:** So like one of the again, like I said,  
**Translation:** 

**[17280.00s] English:** schizotake earlier another schizotake if you've ever been to the presidio in san francisco  
**Translation:** Vocabulary: presidio: 军事要塞

**[17283.88s] English:** beautiful area you could build a power plant and a data center there if you wanted to  
**Translation:** 

**[17288.04s] English:** because it is federal land it used to be a military base but you know obviously this  
**Translation:** 

**[17293.02s] English:** would like piss people off you know it's a good bit anyways trump has made it much easier to do  
**Translation:** 

**[17299.32s] English:** this right generally texas has the only unregulated grid in the in the nation as well let's go texas  
**Translation:** Vocabulary: texas: 德克萨斯; unregulated: 不受监管

**[17304.92s] English:** and so you know therefore like ercot enables people to build faster as well in addition the  
**Translation:** 

**[17310.64s] English:** federal regulations are coming down um and so stargate is predicated this is why that whole  
**Translation:** Vocabulary: predicated: 基于

**[17316.20s] English:** show happened now how they came up with a 500 billion dollar number is beyond me how they came  
**Translation:** 

**[17321.28s] English:** up with a hundred billion dollar number makes sense to some extent right and um there's actually  
**Translation:** 

**[17326.58s] English:** a good table in here that i would like to show um in the in that stargate piece that i had um  
**Translation:** 

**[17332.30s] English:** it's  
**Translation:** 

**[17334.90s] English:** it's the it's the most recent one yeah so so anyways stargate um you know it's it's basically  
**Translation:** 

**[17340.22s] English:** right like there is uh it's it's a table about cost um there you passed it already it's that one  
**Translation:** 

**[17347.40s] English:** so this table is kind of explaining what happens right so stargate is in abilene texas the first  
**Translation:** 

**[17354.48s] English:** hundred billion dollars of it uh that site is 2.2 gigawatts of power in about 1.8 gigawatts of power  
**Translation:** Vocabulary: abilene: 阿比林; gigawatts: 吉瓦

**[17360.84s] English:** uh consumed right um per gpu they they have like roughly uh oracle is already building the first  
**Translation:** 

**[17368.50s] English:** part of uh this before stargate came about to clear they've been building it for a year they  
**Translation:** Vocabulary: stargate: 星门

**[17372.82s] English:** tried to rent it to elon in fact right um but elon was like it's too slow i need it faster so  
**Translation:** 

**[17377.52s] English:** then he went and did his memphis thing um and so opening i was able to get it uh with this like  
**Translation:** Vocabulary: memphis: 孟菲斯

**[17382.34s] English:** weird joint venture called stargate uh they initially signed a deal with just oracle for  
**Translation:** 

**[17386.20s] English:** the first section of this cluster right this first section of this cluster right is  
**Translation:** Vocabulary: cluster: 集群

**[17390.84s] English:** roughly um five billion dollars to six billion dollars of server spend right and then there's  
**Translation:** 

**[17397.32s] English:** another billion or so of data center spend but  
**Translation:** 

**[17400.00s] English:** And then likewise, like if you fill out that entire 1.8 gigawatts with the next two generations of NVIDIA's chips, GB200, GB300, VR200, and you fill it out completely, that ends up being roughly $50 billion server cost, right?  
**Translation:** 

**[17415.54s] English:** Plus there's data center cost, plus maintenance cost, plus operation cost, plus all these things.  
**Translation:** Vocabulary: likewise: 同样地

**[17421.08s] English:** And that's where OpenAI gets to their $100 billion announcement that they had, right?  
**Translation:** 

**[17425.40s] English:** Because they talked about $100 billion is phase one.  
**Translation:** 

**[17427.92s] English:** That's this Abilene, Texas data center, right?  
**Translation:** 

**[17430.22s] English:** $100 billion of total cost of ownership, quote unquote, right?  
**Translation:** Vocabulary: unquote: 引用结束

**[17433.32s] English:** So it's not CapEx.  
**Translation:** 

**[17434.40s] English:** It's not investment.  
**Translation:** 

**[17435.22s] English:** It's $100 billion of total cost of ownership.  
**Translation:** 

**[17438.40s] English:** And then there will be future phases.  
**Translation:** 

**[17440.74s] English:** They're looking at other sites that are even bigger than this 2.2 gigawatts, by the way, in Texas and elsewhere.  
**Translation:** 

**[17446.50s] English:** And so they're not completely ignoring that.  
**Translation:** Vocabulary: texas: 德克萨斯州

**[17449.22s] English:** But there is the number of $100 billion that they say is for phase one, which I do think will happen.  
**Translation:** 

**[17455.50s] English:** They don't even have the money for that.  
**Translation:** 

**[17457.28s] English:** Furthermore, it's not $100 billion.  
**Translation:** 

**[17458.40s] English:** It's $50 billion of spend, right?  
**Translation:** 

**[17460.16s] English:** And then like $50 billion of operational cost, power, et cetera, rental pricing, et cetera.  
**Translation:** 

**[17466.70s] English:** Because OpenAI is renting the GPUs from the Stargate joint venture, right?  
**Translation:** 

**[17471.60s] English:** What money do they actually have, right?  
**Translation:** 

**[17473.64s] English:** SoftBank is going to invest.  
**Translation:** 

**[17475.16s] English:** Oracle is going to invest.  
**Translation:** 

**[17475.90s] English:** OpenAI is going to invest.  
**Translation:** 

**[17476.82s] English:** OpenAI is on the line for $19 billion.  
**Translation:** 

**[17478.66s] English:** Everyone knows that they've only got $6 billion in their last round and $4 billion in debt.  
**Translation:** 

**[17482.92s] English:** But there is news of...  
**Translation:** 

**[17485.40s] English:** Like SoftBank maybe investing $25 billion into OpenAI, right?  
**Translation:** 

**[17489.12s] English:** So that's part of it, right?  
**Translation:** 

**[17490.78s] English:** So $19 billion can come from there.  
**Translation:** 

**[17492.44s] English:** So OpenAI does not have the money at all, right?  
**Translation:** 

**[17494.28s] English:** To be clear.  
**Translation:** 

**[17495.66s] English:** Inc. is not dried on anything.  
**Translation:** 

**[17497.26s] English:** OpenAI has $0 for this $50 billion, right?  
**Translation:** 

**[17499.82s] English:** In which they're legally obligated to put $19 billion of CapEx into the joint venture.  
**Translation:** 

**[17503.70s] English:** And then the rest they're going to pay via renting the GPUs from the joint venture.  
**Translation:** Vocabulary: obligated: 法律责任

**[17506.80s] English:** And then there's Oracle.  
**Translation:** 

**[17509.90s] English:** Oracle has a lot of money.  
**Translation:** 

**[17511.70s] English:** They're building the first section completely.  
**Translation:** 

**[17513.38s] English:** They were spending for it themselves, right?  
**Translation:** 

**[17514.78s] English:** This $6 billion.  
**Translation:** 

**[17515.34s] English:** $10 billion of CapEx.  
**Translation:** 

**[17516.34s] English:** $10 billion of TCO.  
**Translation:** 

**[17518.80s] English:** But they...  
**Translation:** 

**[17519.56s] English:** And they were going to...  
**Translation:** 

**[17520.00s] English:** to do that first section they're paying for that right um as far as the rest of the section i don't  
**Translation:** 

**[17523.90s] English:** know how much larry wants to spend right at any point he could pull out right like this is again  
**Translation:** 

**[17528.10s] English:** it's like completely voluntary so at any point there's no signed ink on this right but he  
**Translation:** Vocabulary: voluntary: 自愿的

**[17532.36s] English:** potentially could contribute tens of billions of dollars right to be clear he's got the money  
**Translation:** 

**[17535.44s] English:** oracle's got the money um and then there's like mgx which is the south the uae fund which technically  
**Translation:** 

**[17540.90s] English:** has 1.5 trillion dollars for investing in ai but again like i don't know how real that money is  
**Translation:** 

**[17546.92s] English:** and like whereas there is no ink signed for this softbank does not have 25 billion dollars of cash  
**Translation:** Vocabulary: trillion: 万亿

**[17552.80s] English:** they have to sell down their stake in arm uh which is you know the leader in cpus and they they ipo'd  
**Translation:** 

**[17558.20s] English:** it this is obviously what they've always wanted to do they just didn't know where they'd redeploy  
**Translation:** 

**[17560.92s] English:** the capital selling down the stake in arm makes a ton of sense so they can sell that down and  
**Translation:** 

**[17565.72s] English:** invest in in this if they want to and invest in open air if they want to um as far as like money  
**Translation:** 

**[17570.38s] English:** secured the first hundred thousand gb200 cluster is like can fund be funded everything else after  
**Translation:** 

**[17576.90s] English:** that up in the air is up in the air money's coming i believe the money will come i personally do just  
**Translation:** Vocabulary: cluster: 计算集群

**[17582.36s] English:** it's a belief okay it's a belief that they are going to release better models and be able to  
**Translation:** 

**[17586.26s] English:** raise more yeah right but like the actual reality is is that elon's right there is the money does  
**Translation:** 

**[17591.38s] English:** not exist right what does the u.s government have to do with anything what does trump have to do  
**Translation:** 

**[17595.82s] English:** with everything he's just a hype man trump is he's reducing the regulation so they can build it  
**Translation:** 

**[17600.04s] English:** faster right um and he's allowing them to do it right you know because any investment of this  
**Translation:** 

**[17605.14s] English:** side is going to involve like antitrust stuff right  
**Translation:** Vocabulary: antitrust: 反垄断

**[17606.90s] English:** like so obviously he's gonna he's gonna allow them to do it he's gonna enable the regulations  
**Translation:** 

**[17610.90s] English:** to actually allow it to be built uh i don't believe there's any u.s government dollars being spent on  
**Translation:** 

**[17616.02s] English:** this though yeah so i i think he's also just creating a general vibe that this is regulation  
**Translation:** 

**[17621.58s] English:** will go down and this is the era of building so if you're a builder you want to create stuff you  
**Translation:** 

**[17628.00s] English:** want to launch stuff this is the time to do it and so like we've had this 1.8 gigawatt data center in  
**Translation:** 

**[17632.60s] English:** our data for over a year now and we've been like sort of sending it to all of our clients including  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[17636.38s] English:** many of these  
**Translation:** 

**[17636.90s] English:** companies that are building the multi-gigawatts but that is like  
**Translation:** 

**[17640.00s] English:** at a level that's not quite maybe executives like seeing 500 billion dollars 100 billion dollars and  
**Translation:** 

**[17644.64s] English:** then everyone's asking them like so it could spur like another like an even faster arms race right  
**Translation:** Vocabulary: executives: 高管

**[17650.04s] English:** because there's already an arms race but like this this like 100 billion 500 billion dollar number  
**Translation:** 

**[17654.12s] English:** trump talking about it on tv like it could spur the arm race to be even faster um and more  
**Translation:** 

**[17659.24s] English:** investors to flood in and etc etc so i think i think you're right is that uh in that uh sense  
**Translation:** 

**[17664.10s] English:** that open eye uh or sort of trump is sort of like championing people are going to build more and his  
**Translation:** Vocabulary: championing: 提倡

**[17668.68s] English:** actions are going to let people build more what are you uh what are you excited about  
**Translation:** 

**[17672.80s] English:** about these uh several years that are upcoming in terms of cluster buildouts in terms of  
**Translation:** Vocabulary: buildouts: 建设; upcoming: 即将来临的

**[17681.16s] English:** breakthroughs in ai like the best possible future you can imagine in the next couple years  
**Translation:** 

**[17686.90s] English:** two three four years what does that look like just it could be very specific technical things  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[17692.16s] English:** like breakthroughs on post post training or it could be just size big  
**Translation:** 

**[17698.24s] English:** you  
**Translation:** 

**[17698.68s] English:** yeah i mean it's impressive clusters i really i really enjoy tracking supply chain and like  
**Translation:** 

**[17704.42s] English:** who's involved in what yeah i really do it's really fun to see like the numbers the cost  
**Translation:** Vocabulary: clusters: 聚类

**[17708.46s] English:** who's building what capacity helping them figure out how much capacity they should build winning  
**Translation:** 

**[17712.18s] English:** deals strategic stuff that's really cool i think technologically uh there's a lot around the  
**Translation:** Vocabulary: technologically: 技术上

**[17717.24s] English:** networking side that really excites me uh with optics and electro electronics right like kind  
**Translation:** 

**[17722.68s] English:** of getting closer and closer whether it be co-package optics or some sort of like forms  
**Translation:** Vocabulary: electro: 电子; excites: 激发; optics: 光学

**[17726.64s] English:** of new forms of switching this is  
**Translation:** 

**[17728.68s] English:** internal to a cluster yeah um also multi-data center training right like there's uh people  
**Translation:** Vocabulary: cluster: 集群

**[17734.64s] English:** are putting so much fiber between these data centers and lighting it up with so many different  
**Translation:** 

**[17738.64s] English:** you know with so much bandwidth that there's a lot of interesting stuff happening on that end  
**Translation:** Vocabulary: bandwidth: 带宽

**[17742.32s] English:** right telecom has been really boring since 5g and now it's like really exciting again um  
**Translation:** 

**[17747.10s] English:** can you educate me a little bit about the speed of things so the speed of memory versus the speed  
**Translation:** 

**[17752.54s] English:** of interconnect versus the speed of fiber between data centers are these like orders of magnitude  
**Translation:** 

**[17757.42s] English:** different is there a difference between the speed of memory versus the speed of data centers  
**Translation:** Vocabulary: interconnect: 互联网络

**[17758.66s] English:** can we at some point  
**Translation:** 

**[17760.00s] English:** point converge towards the place where it all just feels like one computer uh no i don't think  
**Translation:** Vocabulary: converge: 汇聚

**[17764.92s] English:** that's possible all right um it's gonna it's only gonna get harder to program not easier okay um  
**Translation:** 

**[17769.50s] English:** it's only gonna get more difficult and complicated and more layers right uh the the general image  
**Translation:** 

**[17774.20s] English:** that people like to have is like this hierarchy of memory so on chip is really close localized  
**Translation:** 

**[17778.90s] English:** within the chip right you know there you have registers right and those are shared between  
**Translation:** Vocabulary: hierarchy: 层次结构

**[17782.20s] English:** some compute elements and then you'll have caches which are shared between more compute elements  
**Translation:** 

**[17785.90s] English:** then you have like memory right like hbm or dram like ddr memory or whatever it is and that's  
**Translation:** Vocabulary: caches: 缓存

**[17790.64s] English:** shared between the whole chip um and then you can have you know pools of memory that are shared  
**Translation:** 

**[17795.18s] English:** between many chips right um and then storage and it keep you keep zoning out right the access latency  
**Translation:** Vocabulary: latency: 访问延迟

**[17800.50s] English:** across data centers across within the data center within a chip is different so like you're obviously  
**Translation:** 

**[17804.88s] English:** always you're always going to have different um programming paradigms for this it's not going to  
**Translation:** Vocabulary: paradigms: 编程范式

**[17810.36s] English:** be easy programming this stuff is going to be hard maybe i can help right um you know with programming  
**Translation:** 

**[17815.02s] English:** this but the the  
**Translation:** 

**[17815.90s] English:** the way to think about it is that like there is  
**Translation:** 

**[17820.30s] English:** there there's sort of like the more elements you add to a task you you don't gain you don't get  
**Translation:** 

**[17829.72s] English:** strong scaling right if i double the number of chips i don't get two exit performance right this  
**Translation:** 

**[17832.98s] English:** is just like a reality of computing uh because there's inefficiencies um and there's a lot of  
**Translation:** Vocabulary: computing: 计算; inefficiencies: 低效性

**[17837.76s] English:** interesting work being done to make it not you know uh to make it more linear whether it's making  
**Translation:** 

**[17842.64s] English:** the chips more networked together more tightly or uh you know cool  
**Translation:** Vocabulary: networked: 互相连接

**[17845.88s] English:** programming models or cool algorithmic things that you can do on the model side  
**Translation:** 

**[17849.96s] English:** right deep seek did some of these really cool innovations because they were limited on  
**Translation:** Vocabulary: algorithmic: 算法相关的; innovations: 创新

**[17853.18s] English:** interconnect but they still needed to parallelize right like all sorts of you know all everyone's  
**Translation:** 

**[17856.80s] English:** always doing stuff google's got a bunch of work and everyone's got a bunch of work about this  
**Translation:** 

**[17859.70s] English:** um that stuff is super exciting on the model and workload and innovation side right hardware  
**Translation:** 

**[17865.36s] English:** solid state transformers are interesting right for the power side there's all sorts of stuff on  
**Translation:** 

**[17869.90s] English:** batteries and there's all sorts of stuff on you know i think i think when you look at if you look  
**Translation:** 

**[17874.48s] English:** at every layer of the compute stack you're going to see a lot of things that are going to be  
**Translation:** 

**[17875.88s] English:** right whether it goes from lithography and etch all the way to like fabrication to like optic  
**Translation:** 

**[17880.00s] English:** to networking to power to transformers to cooling to you know a networking and you just go on up  
**Translation:** Vocabulary: fabrication: 制造; lithography: 光刻; optic: 光学

**[17886.00s] English:** and up and up and up the stack you know even air conditioners for data centers are like innovating  
**Translation:** 

**[17889.58s] English:** right like it's like there's like copper cables are innovating right like you wouldn't think it  
**Translation:** Vocabulary: innovating: 创新

**[17893.58s] English:** but copper cables like are there's some innovations happening there with like the density of how you  
**Translation:** 

**[17897.84s] English:** can pack them and like it's like all of these layers of the stack all the way up to the models  
**Translation:** Vocabulary: density: 密度

**[17901.64s] English:** human progress is at a pace that's never been seen before i'm just imagining you sitting back  
**Translation:** 

**[17906.22s] English:** in a layer somewhere with screens everywhere just monitoring the supply chain where all these  
**Translation:** 

**[17910.52s] English:** clusters like all the information you're gathering i mean you there's a big team there's a big team  
**Translation:** 

**[17915.28s] English:** i mean you're you you do quite incredible work uh with semi-analysis i mean just  
**Translation:** Vocabulary: clusters: 聚类

**[17921.62s] English:** keeping your finger on the pulse of human civilization in the digital world it's pretty  
**Translation:** 

**[17929.40s] English:** cool like just to watch feel that yeah thank you i guess uh feel feel all of us like doing shit  
**Translation:** 

**[17935.72s] English:** okay  
**Translation:** 

**[17936.22s] English:** epic shit feel the agi feel the i mean from meme to like reality um what nathan is there like  
**Translation:** 

**[17943.64s] English:** breakthroughs that you're like looking forward to potentially i had a while to think about this  
**Translation:** 

**[17948.34s] English:** while listening to dellon's beautiful response he didn't listen to me i knew no i knew this was  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[17953.22s] English:** coming and it's like realistically training models is very fun because there's so much low-hanging  
**Translation:** 

**[17958.78s] English:** fruit and the thing that makes my job entertaining i train models i write analysis about what's  
**Translation:** 

**[17965.04s] English:** happening with models  
**Translation:** 

**[17965.72s] English:** and it's fun because there is obviously so much more progress to be had and the real motivation  
**Translation:** 

**[17972.22s] English:** why i do this somewhere where i can share things is that there's just i don't trust people that  
**Translation:** 

**[17977.56s] English:** are like trust me bro we're gonna make ai good it's like we're the ones that it's like we're  
**Translation:** 

**[17981.30s] English:** gonna do it and you can trust us and we're just gonna have all the ai and it's just like i would  
**Translation:** 

**[17985.96s] English:** like a future where more people have a say in what ai is and can understand it and that's it's a  
**Translation:** 

**[17993.02s] English:** little bit less fun that it's not a like positive thing i feel like this is just a bit more fun and  
**Translation:** 

**[17995.72s] English:** all really fun like training models is fun and bringing people in is fun but it's really  
**Translation:** 

**[18000.00s] English:** AI, if it is going to be the most powerful technology of my lifetime, it's like we need to have a lot of people involved in making that and making it open helps with that as accessible as possible, as open as possible.  
**Translation:** 

**[18013.94s] English:** Yeah.  
**Translation:** 

**[18014.28s] English:** In my read of the last few years is that more openness would help the AI ecosystem in terms of having more people understand what's going on, rather than researchers from non-AI fields to governments to everything.  
**Translation:** 

**[18025.32s] English:** It doesn't mean that openness will always be the answer.  
**Translation:** 

**[18027.72s] English:** I think then I will reassess of like, what is the biggest problem facing AI and tack on a different angle to the wild ride that we're on.  
**Translation:** 

**[18036.28s] English:** And for me, just from even the user experience, anytime you have the, like Apathy said, the aha moments, like the magic, like seeing the reasoning, the chain of thought.  
**Translation:** Vocabulary: anytime: 任何时候

**[18050.24s] English:** It's like, there's something really just fundamentally beautiful about that.  
**Translation:** 

**[18054.30s] English:** It's putting a mirror to ourselves and seeing like, oh, shit.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[18057.72s] English:** It is solving intelligence as the cliche, like goal of these companies is, and you get to understand why we humans are special.  
**Translation:** 

**[18066.82s] English:** The intelligence within us is special.  
**Translation:** Vocabulary: cliche: 陈词滥调

**[18069.18s] English:** And for now, also why we are special in terms of we seem to be conscious and the AI systems for now aren't.  
**Translation:** 

**[18076.44s] English:** And we get to solve, we get to explore that mystery.  
**Translation:** 

**[18079.88s] English:** So that's, it's just really cool to get to explore these questions that I don't think, I would have never imagined.  
**Translation:** 

**[18087.72s] English:** It would be even possible back when, so just watching with excitement, deep blue, big Kasparov, like I wouldn't have ever thought this kind of AI would be possible in my lifetime.  
**Translation:** Vocabulary: kasparov: 卡斯帕罗夫

**[18101.20s] English:** It's like, this is really feels like AI.  
**Translation:** 

**[18103.40s] English:** It's incredible.  
**Translation:** 

**[18104.36s] English:** I started with AI of learning to fly a silly quad rotor.  
**Translation:** 

**[18108.60s] English:** It's like learn to fly.  
**Translation:** Vocabulary: rotor: 旋翼

**[18109.60s] English:** And it just like, it learned to fly up.  
**Translation:** 

**[18111.82s] English:** It would hit the ceiling and stop and catch it.  
**Translation:** 

**[18113.62s] English:** It's like, okay, that is like really stupid compared to what's going on now.  
**Translation:** 

**[18117.18s] English:** And now you could.  
**Translation:** 

**[18117.72s] English:** Probably with natural language.  
**Translation:** 

**[18120.00s] English:** it to learn to fly and is going to generate the control algorithm required to do that probably  
**Translation:** Vocabulary: algorithm: 控制算法

**[18124.96s] English:** there's low level blockers like we had to do some weird stuff for that but you can you you  
**Translation:** 

**[18129.20s] English:** definitely back to our robotics conversation yeah when you have to interact an actual physical world  
**Translation:** 

**[18133.28s] English:** that's hard what gives you hope about the future of human civilization looking into the next  
**Translation:** 

**[18140.56s] English:** 10 years 100 years thousand years how long do you think we'll make it  
**Translation:** 

**[18144.32s] English:** do you think we've got a thousand years humans will definitely be around in a thousand years i  
**Translation:** 

**[18150.48s] English:** think there's there's ways that very bad things could happen there will be way fewer humans but  
**Translation:** 

**[18155.20s] English:** humans are very good at surviving there's been a lot of things that that is true i don't think  
**Translation:** 

**[18161.24s] English:** they're necessarily we're good at long-term credit assignment of risk but when the risk becomes  
**Translation:** 

**[18166.56s] English:** immediate we tend to figure things out and oh yeah for that reason i'm like there's physical  
**Translation:** 

**[18172.54s] English:** constraints to things like  
**Translation:** Vocabulary: constraints: 限制

**[18174.32s] English:** agi hyper like recursive improvement to kill us all type stuff i'm for the physical reasons and  
**Translation:** 

**[18181.22s] English:** for how humans have figured things out before i'm not too worried about it ai takeover there are  
**Translation:** Vocabulary: hyper: 过度; recursive: 递归; takeover: 接管

**[18185.88s] English:** other international things that are worrying but there's just fundamental human goodness and trying  
**Translation:** 

**[18192.98s] English:** to amplify that and like we're on a tenuous time and i mean if you look at humanity as it as a whole  
**Translation:** Vocabulary: tenuous: 脆弱

**[18200.40s] English:** there's been times where things go backwards there's times when things don't have to be  
**Translation:** 

**[18204.30s] English:** at all and we're on a what should be very positive trajectory right now yeah there seems to be  
**Translation:** Vocabulary: backwards: 倒退; trajectory: 轨迹

**[18209.60s] English:** progress but just like with with power uh there's like spikes of human suffering and we want to try  
**Translation:** 

**[18216.40s] English:** to minimize the amount of spikes generally humanity is going to suffer a lot less right i'm very  
**Translation:** Vocabulary: spikes: 高峰

**[18221.94s] English:** optimistic about that um i do worry of like techno fascism type stuff arising as uh ai becomes more  
**Translation:** 

**[18229.94s] English:** and more prevalent and powerful and those who control it can do more and more uh maybe it's  
**Translation:** Vocabulary: fascism: 法西斯主义; optimistic: 乐观; prevalent: 盛行

**[18234.30s] English:** maybe it doesn't kill us all uh but at some point every very powerful human is going to want to  
**Translation:** 

**[18239.64s] English:** brain  
**Translation:** 

**[18240.00s] English:** computer interface so that they can interact with the AGI and all of its advantages in many more  
**Translation:** 

**[18244.68s] English:** way and merge its mind with, you know, sort of like, and its capabilities or that person's  
**Translation:** Vocabulary: interface: 人机接口

**[18248.80s] English:** capabilities, uh, can leverage those much better than anyone else. And therefore be, you know,  
**Translation:** 

**[18253.28s] English:** it won't be one person rule them all, but it will be, uh, you know, the thing I worry about is it'll  
**Translation:** Vocabulary: leverage: 利用

**[18257.40s] English:** be like few people, you know, you know, hundreds, thousands, tens of thousands, maybe millions of  
**Translation:** 

**[18261.90s] English:** people rule whoever's left. Right. Um, and the economy around it. Right. And I think it'll,  
**Translation:** 

**[18267.94s] English:** that's like the thing that's probably more worrisome is like human machine amalgamations.  
**Translation:** 

**[18273.78s] English:** This enables an individual human to have more impact on the world. And that impact can be both  
**Translation:** Vocabulary: amalgamations: 人机融合; worrisome: 令人担忧

**[18278.20s] English:** positive and negative, right? Uh, generally humans have positive impacts on the world,  
**Translation:** 

**[18282.54s] English:** at least societally. Uh, but it's possible for individual humans to have such negative impacts  
**Translation:** Vocabulary: societally: 社会上

**[18287.30s] English:** and AGI, at least as I think the labs define it, which is not a runaway sentient thing,  
**Translation:** 

**[18293.36s] English:** but rather just something that can do a lot of tasks really efficiently. Um,  
**Translation:** Vocabulary: efficiently: 高效地; sentient: 有感知的

**[18297.94s] English:** amplifies the capabilities of someone causing extreme damage. Uh, but, but for the most part,  
**Translation:** 

**[18303.12s] English:** I think it'll be used for, you know, profit seeking motives, which will then reduce,  
**Translation:** Vocabulary: amplifies: 增强

**[18307.24s] English:** which will increase the abundance and supply of things and therefore reduce suffering. Right.  
**Translation:** 

**[18311.50s] English:** Yeah. That's the goal. Scrolling on a timeline, just drawing a stasis.  
**Translation:** Vocabulary: scrolling: 滚动; stasis: 停滞

**[18318.28s] English:** Scrolling holds the status quo of the world. That is a positive outcome, right? Like it's like,  
**Translation:** 

**[18322.78s] English:** if I have food tubes and I'm scrolling and I'm happy, that's a positive outcome.  
**Translation:** 

**[18327.94s] English:** Yeah. While expanding out into the cosmos. Uh, well, this is a fun time to be alive  
**Translation:** 

**[18334.68s] English:** and thank you for pushing the forefront of what is possible in humans. And thank you for talking  
**Translation:** Vocabulary: cosmos: 宇宙; forefront: 前沿

**[18340.50s] English:** today. This was fun. Thanks for having us. Thanks for having us. Thanks for listening  
**Translation:** 

**[18344.60s] English:** to this conversation with Dylan Patel and Nathan Lambert. To support this podcast,  
**Translation:** 

**[18349.36s] English:** please check out our sponsors in the description. And now let me leave you some words from Richard  
**Translation:** 

**[18355.76s] English:** Feynman.  
**Translation:** Vocabulary: sponsors: 赞助商

**[18357.94s] English:** Successful technology, reality.  
**Translation:** 

**[18360.00s] English:** must take precedence over public relations, for nature cannot be fooled.  
**Translation:** 

**[18366.14s] English:** Thank you for listening, and I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
