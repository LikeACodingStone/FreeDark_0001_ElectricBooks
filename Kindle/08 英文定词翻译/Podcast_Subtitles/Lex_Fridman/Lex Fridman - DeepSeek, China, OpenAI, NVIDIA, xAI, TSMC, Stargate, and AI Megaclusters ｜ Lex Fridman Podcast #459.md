# Podcast vocabulary notes
Source file: Lex Fridman - DeepSeek, China, OpenAI, NVIDIA, xAI, TSMC, Stargate, and AI Megaclusters ｜ Lex Fridman Podcast #459.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Dylan Patel and Nathan Lampert.  
**Translation:** 

**[4.64s] English:** Dylan runs SemiAnalysis, a well-respected research and analysis company that specializes in semiconductors, GPUs, CPUs, and AI hardware in general.  
**Translation:** 

**[16.98s] English:** Nathan is a research scientist at the Allen Institute for AI and is the author of the amazing blog on AI called InterConnects.  
**Translation:** 

**[26.48s] English:** They are both highly respected, read, and listened to by the experts, researchers, and engineers in the field of AI.  
**Translation:** Vocabulary: respected: 受尊敬的

**[34.82s] English:** And personally, I'm just a fan of the two of them.  
**Translation:** 

**[37.90s] English:** So, I used the deep-seek moment that shook the AI world a bit as an opportunity to sit down with them and lay it all out.  
**Translation:** 

**[47.64s] English:** From DeepSeek, OpenAI, Google, XAI, Meta, Anthropic, to NVIDIA and TSMC, and to the U.S., China, and Taiwan.  
**Translation:** 

**[56.48s] English:** They are both highly respected, read, and listened to by the experts, researchers, and engineers in the field of AI.  
**Translation:** Vocabulary: taiwan: 台湾

**[60.78s] English:** This conversation is a deep dive into many critical aspects of the AI industry.  
**Translation:** 

**[67.44s] English:** While it does get super technical, we try to make sure that it's still accessible to folks outside of the AI field by defining terms, stating important concepts explicitly, spelling out acronyms, and, in general, always moving across different layers of abstraction and levels of detail.  
**Translation:** Vocabulary: abstraction: 抽象; acronyms: 缩写; explicitly: 明确地

**[86.48s] English:** There is a lot of hype in the media about what AI is and isn't.  
**Translation:** 

**[91.94s] English:** The purpose of this podcast, in part, is to cut through the hype, the bullshit, and low-resolution analysis, and to discuss in detail how stuff works and what the implications are.  
**Translation:** Vocabulary: bullshit: 胡说八道; implications: 影响

**[106.08s] English:** Let me also, if I may, comment on the new OpenAI 03 Mini reasoning model, the release of which we were anticipating during the conversation.  
**Translation:** 

**[115.42s] English:** And it did increase.  
**Translation:** Vocabulary: anticipating: 预期

**[116.48s] English:** It did come out right after.  
**Translation:** 

**[117.56s] English:** Its capabilities and cost.  
**Translation:** Vocabulary: capabilities: 能力

**[120.00s] English:** Are on par with our expectations, as we stated.  
**Translation:** 

**[124.72s] English:** OpenAI O3 Mini is indeed a great model.  
**Translation:** 

**[127.86s] English:** But it should be stated that DeepSeek R1 has similar performance on benchmarks.  
**Translation:** 

**[132.68s] English:** Is still cheaper, and it reveals its chain-of-thought reasoning, which O3 Mini does not.  
**Translation:** Vocabulary: benchmarks: 测试基准

**[139.44s] English:** It only shows a summary of the reasoning.  
**Translation:** 

**[142.86s] English:** Plus, R1 is open weight, and the O3 Mini is not.  
**Translation:** 

**[147.68s] English:** By the way, I got a chance to play with the O3 Mini.  
**Translation:** 

**[152.66s] English:** And, in an anecdotal vibe-check, I felt that O3 Mini, specifically O3 Mini High, is better than R1.  
**Translation:** Vocabulary: anecdotal: 轶事的

**[161.68s] English:** Still, for me personally, I find that ClaudeSana 3.5 is the best model for programming.  
**Translation:** 

**[167.56s] English:** Except for tricky cases, where I will use O1 Pro to brainstorm.  
**Translation:** Vocabulary: tricky: 棘手的

**[171.92s] English:** Either way, many better AI models will come, including reasoning models.  
**Translation:** 

**[177.02s] English:** Both from OpenAI.  
**Translation:** 

**[177.68s] English:** American and Chinese companies.  
**Translation:** 

**[180.12s] English:** They will continue to shift the cost curve.  
**Translation:** 

**[183.44s] English:** But the "DeepSeek" moment is indeed real.  
**Translation:** 

**[187.72s] English:** I think it will still be remembered five years from now as a pivotal event in tech history.  
**Translation:** Vocabulary: pivotal: 关键的

**[193.06s] English:** Due, in part, to the geopolitical implications, but for other reasons as well, too.  
**Translation:** 

**[198.30s] English:** As we discuss in detail, from many perspectives, in this conversation.  
**Translation:** Vocabulary: geopolitical: 地缘政治的; implications: 影响; perspectives: 视角

**[202.12s] English:** This is the Lex Friedman Podcast.  
**Translation:** 

**[203.94s] English:** To support it, please check out our sponsors in the description.  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[207.68s] English:** And now, dear friends: here's Dylan Patel and Nathan Lambert.  
**Translation:** 

**[213.32s] English:** A lot of people are curious to understand China's DeepSeek AI models.  
**Translation:** 

**[217.48s] English:** So, let's lay it out.  
**Translation:** 

**[218.96s] English:** Nathan, can you describe what DeepSeek V3 and DeepSeek R1 are, how they work, and how they're trained?  
**Translation:** 

**[225.54s] English:** Let's look at the big picture, and then we'll zoom in on the details.  
**Translation:** 

**[228.96s] English:** Yeah, so DeepSeek V3 is a new mixture of experts, transformer language model from DeepSeek.  
**Translation:** Vocabulary: mixture: 混合体

**[236.78s] English:** Who is based in China?  
**Translation:** 

**[238.92s] English:** They have some....  
**Translation:** 

**[240.00s] English:** New specifics in the model that we'll get into: largely, this is an open-weight model, and it's a  
**Translation:** 

**[247.12s] English:** Instructions, similar to what you would use for ChatGPT, they also release what is called the base.  
**Translation:** 

**[252.80s] English:** Model which is before these techniques of post-training, most people use instruction.  
**Translation:** 

**[257.58s] English:** Models today, and those are what's served in all sorts of applications. This was released on I.  
**Translation:** 

**[263.28s] English:** Believe, December 26th or that week, and then a few weeks later, on January 20th, DeepSeek released DeepSeek.  
**Translation:** 

**[272.30s] English:** R1, which is a reasoning model, really accelerated a lot of this discussion. This  
**Translation:** 

**[278.84s] English:** Reasoning: The model has a lot of overlapping training steps with DeepSeek V3, and it's confusing.  
**Translation:** 

**[284.28s] English:** That you have a base model called V3, that you do something to get a chat model, and then you do  
**Translation:** Vocabulary: overlapping: 重叠的

**[290.86s] English:** Some Different Things to Get a Reasoning Model.  
**Translation:** 

**[293.14s] English:** I think a lot of the AI industry is going through this challenge of communications right now where  
**Translation:** 

**[297.60s] English:** Open AI makes fun of their own naming schemes; they have GPT-4, they have "OpenAI 0.1," and there are a lot.  
**Translation:** 

**[305.26s] English:** Of different types of models, so we're going to break down what each of them are. There's a lot of technical  
**Translation:** Vocabulary: schemes: 命名方案

**[309.68s] English:** Specifics on training, and go from high-level to specific, kind of going through each one.  
**Translation:** 

**[314.68s] English:** There are so many places we can go here, but maybe let's go to open weights first. What does that mean?  
**Translation:** 

**[319.78s] English:** For a model to be open, what are the different flavors of open-source in general?  
**Translation:** 

**[323.14s] English:** Yeah, so this discussion has been going on for a long time in AI; it became more important since  
**Translation:** Vocabulary: flavors: 不同版本

**[328.64s] English:** Chat GPT or More Focal Since Chat GPT at the end of 2022, "open weights" is the accepted term for.  
**Translation:** 

**[334.84s] English:** When model weights of a language model are available on the Internet for people to download,  
**Translation:** 

**[340.04s] English:** Those weights can have different licenses, which is effectively the terms by which you can.  
**Translation:** 

**[345.52s] English:** Use the model, there are licenses that come from history and open-source software; there are licenses.  
**Translation:** 

**[350.46s] English:** That are designed by companies specifically,  
**Translation:** 

**[353.14s] English:** Um, all of Llama, DeepSeek, Quen, Mistral—these popular names in  
**Translation:** Vocabulary: mistral: 盛行的

**[360.00s] English:** Open-weight models have some of their own licenses, it's complicated because not all the same models.  
**Translation:** 

**[365.12s] English:** Have the same terms? The big debate is on what makes a model open, weight it's like why are we  
**Translation:** 

**[372.82s] English:** Saying "this term" is kind of a mouthful; it sounds close to open source, but it's not the same. There's  
**Translation:** 

**[377.88s] English:** Still, there is a lot of debate on the definition and soul of open-source AI. Open-source software has a rich  
**Translation:** 

**[383.64s] English:** History on freedom to modify, freedom to take ownership of your own work, freedom from any restrictions on how you use it.  
**Translation:** 

**[389.38s] English:** Would use the software, and what that means for AI is still being defined. So, for what I do, I work...  
**Translation:** 

**[397.84s] English:** At the Allen Institute for AI, we're a nonprofit. We want to make AI open for everybody, and we try.  
**Translation:** 

**[403.28s] English:** To lead on what we think is truly open source, there's not full agreement in the community.  
**Translation:** Vocabulary: nonprofit: 非盈利机构

**[407.22s] English:** But for us, that means releasing the training data, releasing the training code, and then also having  
**Translation:** 

**[412.58s] English:** Open weights like this, and we'll get into the details of the models. And again, and again, as we  
**Translation:** 

**[418.88s] English:** Try to get  
**Translation:** 

**[419.32s] English:** You.  
**Translation:** 

**[419.36s] English:** You.  
**Translation:** 

**[419.38s] English:** To get deeper into how the models will train, we'll say things like the data.  
**Translation:** 

**[424.32s] English:** Processing and filtering data for quality is the number one determinant of model quality, and  
**Translation:** 

**[429.68s] English:** Then, a lot of the training code is the determinant on how long it takes to train and how fast your model converges.  
**Translation:** Vocabulary: converges: 收敛; determinant: 决定因素; filtering: 过滤

**[434.88s] English:** Experimentation is so limited without fully open-source models, where you have access to this data.  
**Translation:** 

**[441.80s] English:** It's hard to know, or it's harder to replicate. So, we'll get into the cost numbers for DeepSeek V3, mostly GPU-based.  
**Translation:** 

**[448.64s] English:** Hours and  
**Translation:** 

**[449.36s] English:** How much could you?  
**Translation:** 

**[450.54s] English:** Pay to rent those yourselves, but without the data, the replication cost is going to be far, far higher. And the same goes for the code; we should also say that this is probably one of the more open models out of the frontier models, it's like.  
**Translation:** 

**[465.12s] English:** In this full spectrum, where probably the fullest open source (like you said, "open code, open data, open weights"), this is not open code, and this is probably not open data.  
**Translation:** Vocabulary: frontier: 最前沿; yourselves: 你们自己

**[478.62s] English:** And  
**Translation:** 

**[480.00s] English:** And this is open-source weight sharing, and the licensing is MIT license—or, to be more precise, there's some nuance in the different models, but it's generally toward the free side in terms of the open-source movement.  
**Translation:** Vocabulary: nuance: 细微差别

**[491.72s] English:** These are the kinds of good guys.  
**Translation:** 

**[493.26s] English:** Yeah, DeepSeek is doing fantastic work for disseminating understanding of AI.  
**Translation:** Vocabulary: disseminating: 传播

**[498.50s] English:** Their papers are extremely detailed in what they do.  
**Translation:** 

**[502.30s] English:** And for other teams around the world, they are very actionable in terms of improving your own training techniques.  
**Translation:** 

**[510.52s] English:** And we'll talk about licenses more.  
**Translation:** 

**[513.50s] English:** The DeepSeek R1 model has a very permissive license.  
**Translation:** Vocabulary: permissive: 宽容的

**[517.04s] English:** It's called the MIT license.  
**Translation:** 

**[518.32s] English:** That effectively means there are no downstream restrictions on commercial use.  
**Translation:** Vocabulary: downstream: 下游的

**[522.06s] English:** There are no use case restrictions.  
**Translation:** 

**[524.04s] English:** You can use the outputs from the models to create synthetic data.  
**Translation:** Vocabulary: outputs: 输出; synthetic: 合成

**[527.58s] English:** And this is all fantastic!  
**Translation:** 

**[529.78s] English:** I think the closest peer is something like LAMA, where you have the weights and a technical report.  
**Translation:** 

**[535.70s] English:** And the technical report is very good for LAMA.  
**Translation:** 

**[538.64s] English:** One of the most-read PDFs of the year.  
**Translation:** 

**[540.00s] English:** Last year was the LAMA 3 paper.  
**Translation:** 

**[542.22s] English:** But, in some ways, it's slightly less actionable.  
**Translation:** 

**[544.56s] English:** It has less detail on the training specifics and fewer plots, and so on.  
**Translation:** 

**[549.46s] English:** And the LAMA 3 license is more restrictive than MIT.  
**Translation:** 

**[553.08s] English:** And then, between the DeepSeek custom license and the LAMA license, we can get into this whole rabbit hole.  
**Translation:** 

**[557.56s] English:** I think we'll make sure we want to go down the licensing rabbit hole before we get into specifics.  
**Translation:** 

**[561.46s] English:** Yeah.  
**Translation:** 

**[562.06s] English:** And I mean, so it should be stated that one of the implications of DeepSeek is that it puts pressure on LAMA and everybody else at OpenAI.  
**Translation:** Vocabulary: implications: 含义

**[568.84s] English:** To push toward open source.  
**Translation:** 

**[572.04s] English:** And that's the other side of open source that you mentioned: how much is published in detail about it.  
**Translation:** 

**[577.38s] English:** So, how open are you about the insights behind the code?  
**Translation:** 

**[582.78s] English:** So, how good are the technical reports?  
**Translation:** 

**[585.62s] English:** Are they hand-wavy, or is there actual details in there?  
**Translation:** 

**[588.88s] English:** And that's one of the things that DeepSeek did well: they published a lot of the details.  
**Translation:** 

**[592.54s] English:** Yeah, especially in the DeepSeek V3, which is their pre-training paper.  
**Translation:** 

**[595.84s] English:** They were very clear about what they are doing.  
**Translation:** 

**[598.84s] English:** So, they're very clear that you can do a lot more with.  
**Translation:** 

**[600.00s] English:** Technical stack that goes at many different levels. For example, to get highly efficient training,  
**Translation:** 

**[606.24s] English:** They're making modifications at or below the CUDA layer for NVIDIA chips. I have never worked  
**Translation:** 

**[612.84s] English:** There, myself, and there are a few people in the world who do that very well, and some of them,  
**Translation:** Vocabulary: modifications: 修改

**[616.72s] English:** Are they at DeepSeq? And these types of people are at DeepSeq and leading American frontier labs.  
**Translation:** 

**[623.28s] English:** But there aren't many places. To help people understand the other,  
**Translation:** Vocabulary: frontier: 前沿

**[627.02s] English:** The implication of open weights is a topic we return to often here. So there's a fear that  
**Translation:** 

**[627.42s] English:** A traditional software.  
**Translation:** Vocabulary: implication: 暗示

**[628.14s] English:** A lot of the time, they don't kind of say, you know, like, "hey, you can do all these different things with, like, an open-source document.  
**Translation:** 

**[628.38s] English:** So, they're very clear that they're handling it very well.  
**Translation:** 

**[628.76s] English:** And then, of course, they are doing a lot of other things.  
**Translation:** 

**[636.98s] English:** China, the nation, might have an interest in stealing American data, violating the privacy of Americans.  
**Translation:** Vocabulary: violating: 侵犯

**[644.54s] English:** Citizens, what can we say about open weights to help us understand what they are able to do?  
**Translation:** 

**[651.50s] English:** In terms of stealing people's data? Yeah, so these weights that you can  
**Translation:** 

**[656.40s] English:** Download from Hugging.com.  
**Translation:** 

**[657.02s] English:** Or, on other platforms, are very big matrices of numbers. You can download them to a computer.  
**Translation:** Vocabulary: hugging: 拥抱; matrices: 矩阵

**[662.98s] English:** In your own house that has no internet, you can run this model, and you're totally in control.  
**Translation:** 

**[667.08s] English:** Of your data. That is something that is different from how a lot of language model usage is actually.  
**Translation:** 

**[673.48s] English:** Done today, which is mostly through APIs, where you send your prompt to GPUs run by certain companies.  
**Translation:** 

**[678.72s] English:** Companies, and these companies will have different distributions and policies on how your data is.  
**Translation:** Vocabulary: distributions: 数据分布; prompt: 提示

**[682.92s] English:** Stored, if it is used to train future models, where it is stored, if it is encrypted, and so on.  
**Translation:** 

**[687.02s] English:** So, the open weights are: you have your fate of data in your own hands, and that is something that is  
**Translation:** Vocabulary: encrypted: 加密了

**[694.24s] English:** Deeply connected to the soul of open source, so it's not the model that steals your data.  
**Translation:** 

**[699.34s] English:** It's Clover's hosting the model, which could be China, if you're using the DeepSeek app.  
**Translation:** 

**[704.34s] English:** Or it could be Perplexity. You're trusting them with your data, or OpenAI—you're trusting them.  
**Translation:** 

**[710.64s] English:** With your data. And some of these are American companies, some are Chinese companies.  
**Translation:** Vocabulary: perplexity: 困惑

**[713.84s] English:** But the model itself is not doing the stealing.  
**Translation:** 

**[717.02s] English:** It's the host. All right.  
**Translation:** 

**[720.00s] English:** So, back to the basics. What's the difference between DeepSeq v3 and DeepSeq R1? Can we try to...  
**Translation:** 

**[727.80s] English:** Lay out the confusion potential? Yes. So, for one, I have a very good understanding of many people being  
**Translation:** 

**[734.92s] English:** Confused by these two model names, so I would say the best way to think about this is that:  
**Translation:** 

**[739.58s] English:** When training a language model, you have what is called pre-training, which is when you're  
**Translation:** 

**[743.06s] English:** Predicting large amounts of mostly Internet text. You're trying to predict the next token.  
**Translation:** 

**[748.50s] English:** And what to know about these new DeepSeq models is that they do this on a large scale over the Internet.  
**Translation:** Vocabulary: token: 标记

**[754.84s] English:** Pre-training once to get what is called DeepSeq v3 Base. This is a base model; it's just going...  
**Translation:** 

**[760.90s] English:** To finish your sentences for you, it's going to be harder to work with than ChatGPT. And then,...  
**Translation:** 

**[766.30s] English:** What DeepSeq did is that they've done two different post-training regimes to make the models have  
**Translation:** 

**[772.82s] English:** Specific desirable behaviors. So, what is the more normal model in terms of?  
**Translation:** Vocabulary: desirable: 值得期望的; regimes: 训练制度

**[777.94s] English:** The language model?  
**Translation:** 

**[778.50s] English:** The last few years of AI have included an instruction model, a chat model, and what's often referred to as a "quote-unquote" aligned model.  
**Translation:** Vocabulary: aligned: 对齐的

**[783.10s] English:** A helpful model can be described in many ways, but it is more standard to refer to it as post-training. So, this is  
**Translation:** 

**[788.72s] English:** Things like instruction tuning and reinforcement learning from human feedback. We'll get into  
**Translation:** Vocabulary: reinforcement: 强化

**[792.38s] English:** Some of these words, and this is what they did to create the DeepSeq v3 model. This was the first.  
**Translation:** 

**[798.34s] English:** Model to be released, and it is very high-performance. It's competitive with GPT-4.  
**Translation:** 

**[805.16s] English:** LAMA-405b, and so on.  
**Translation:** 

**[807.06s] English:** And then, when this release was happening, we don't know their exact timeline, or soon after.  
**Translation:** 

**[813.12s] English:** They were finishing the training of a different training process from the same.  
**Translation:** 

**[817.36s] English:** Next, the token prediction base model that I talked about, which is when this new reasoning training begins.  
**Translation:** 

**[823.02s] English:** That people have heard about comes in, in order to create the model that is called DeepSeq R1.  
**Translation:** 

**[828.42s] English:** The R through this conversation is good for grounding for reasoning.  
**Translation:** 

**[831.26s] English:** And the name is also similar to OpenAI's O1, which is the other reasoning model that people  
**Translation:** 

**[835.76s] English:** I have heard about it.  
**Translation:** 

**[837.06s] English:** And we'll have to break down the training for R1.  
**Translation:** 

**[840.00s] English:** On in more detail because, for one, we have a paper detailing it, but also it is far newer.  
**Translation:** 

**[845.62s] English:** A set of techniques for the AI community. So, it's a much more rapidly evolving area of research.  
**Translation:** 

**[852.04s] English:** Maybe we should also say the big two categories: pre-training and post-training.  
**Translation:** Vocabulary: evolving: 不断发展的

**[858.44s] English:** These umbrella terms that people use. So, what is pre-training, and what is post-training?  
**Translation:** 

**[864.78s] English:** What are the different flavors of things under the post-training umbrella?  
**Translation:** Vocabulary: flavors: 种类

**[867.54s] English:** Yeah. So, pre-training, I'm using some of the same words to really get the message across.  
**Translation:** 

**[871.92s] English:** You're doing what is called autoregressive prediction to predict the next token in a  
**Translation:** Vocabulary: autoregressive: 自回归; token: 标记

**[875.94s] English:** A series of documents. This is done according to standard practices, involving trillions of tokens. So, this is a lot.  
**Translation:** 

**[883.00s] English:** Of data that is mostly scraped from the web. And some of DeepSeek's earlier papers they talk about  
**Translation:** Vocabulary: scraped: 从网上抓取; trillions: 万亿

**[889.76s] English:** Their training data being distilled for math. I shouldn't use this word yet, but taken from.  
**Translation:** 

**[895.22s] English:** Common Crawl. And that's a  
**Translation:** Vocabulary: distilled: 提炼

**[897.52s] English:** Public access allows anyone listening to this to go download data from the Common Crawl website.  
**Translation:** 

**[902.06s] English:** This is a crawler that is maintained publicly. Yes, other tech companies eventually shift to.  
**Translation:** Vocabulary: crawler: 网络爬虫

**[906.74s] English:** Their own crawler, and DeepSeek, likely have done this as well as most Frontier Labs do.  
**Translation:** 

**[911.30s] English:** But this sort of data is something that people can get started with, and you're just predicting.  
**Translation:** Vocabulary: frontier: 前沿技术

**[915.68s] English:** Text in a series of documents. This can be scaled to be very efficient, and there are a lot of numbers.  
**Translation:** 

**[924.50s] English:** That are thrown around in AI training, like how many floating-point,  
**Translation:** 

**[927.52s] English:** Operations or flops are used, and then you can also look at how many hours of these GPUs.  
**Translation:** 

**[933.18s] English:** That are used, and it's largely one loss function taken to a very large amount.  
**Translation:** Vocabulary: flops: 运算次数

**[941.42s] English:** Compute usage: You just set up really efficient systems. And then at the end of that, you have  
**Translation:** 

**[946.58s] English:** This base model, and pre-training is where there is a lot more complexity in terms of how the  
**Translation:** Vocabulary: complexity: 复杂性; compute: 计算

**[953.70s] English:** The process is emerging or evolving, and there's a lot more complexity in terms of how the process is.  
**Translation:** 

**[957.52s] English:** Emerging, and there's a lot more complexity in terms of how the different types of training work.  
**Translation:** Vocabulary: evolving: 发展中的

**[958.54s] English:** Losses that you will use.  
**Translation:** 

**[960.00s] English:** I think this is a lot of techniques grounded in the natural language processing literature.  
**Translation:** 

**[965.72s] English:** The oldest technique, which is still used today, is something called instruction tuning, or also known as supervised fine-tuning.  
**Translation:** 

**[972.16s] English:** These acronyms will be IFT or SFT.  
**Translation:** Vocabulary: acronyms: 缩写; supervised: 监督

**[975.72s] English:** People really go back and forth throughout them, and I will probably do the same, which is why you should add this formatting to the model so that it knows to take a question like, "Explain the history of the Roman Empire" to me.  
**Translation:** 

**[989.50s] English:** And, or something like a question you'll see on Reddit or Stack Overflow, and then the model will respond in an information-dense but presentable manner.  
**Translation:** Vocabulary: formatting: 格式; overflow: 溢出; presentable: 可展示的

**[998.82s] English:** The core of that formatting is in this instruction-tuning phase.  
**Translation:** 

**[1001.78s] English:** And then there are two other categories of loss functions that are being used today.  
**Translation:** 

**[1007.22s] English:** One I will classify as preference tuning.  
**Translation:** 

**[1010.00s] English:** Preference Fine-Tuning is a generalized term for what came out of Reinforcement Learning from Human Feedback, which is RLHF.  
**Translation:** Vocabulary: classify: 分类; generalized: 泛化; reinforcement: 强化

**[1017.36s] English:** This is reinforcement learning.  
**Translation:** 

**[1019.50s] English:** From Human Feedback is credited as the technique that helped ChatGPT breakthrough.  
**Translation:** 

**[1025.94s] English:** It is a technique to make the responses that are nicely formatted, like these Reddit answers, more in tune with what a human would like to read.  
**Translation:** 

**[1034.26s] English:** This is done by collecting pairwise preferences from actual humans out in the world, to start.  
**Translation:** Vocabulary: formatted: 排版整齐; nicely: 良好地; pairwise: 成对地

**[1039.52s] English:** And now, AI systems are also labeling this data, and we'll get into those tradeoffs.  
**Translation:** 

**[1043.56s] English:** And you have this kind of contrastive loss function between a good answer and a bad answer.  
**Translation:** Vocabulary: labeling: 标注; tradeoffs: 权衡

**[1048.62s] English:** And the model.  
**Translation:** 

**[1049.38s] English:** Learns to pick up these trends.  
**Translation:** 

**[1051.08s] English:** There are different implementation ways, and you have things called reward models.  
**Translation:** 

**[1055.06s] English:** You could have direct alignment algorithms.  
**Translation:** Vocabulary: alignment: 对齐; implementation: 实施

**[1056.90s] English:** There are a lot of really specific things you can do, but all of this is about fine-tuning to human preferences.  
**Translation:** 

**[1062.74s] English:** And the final stage is much newer and will link to what we do in ours.  
**Translation:** 

**[1068.00s] English:** And these reasoning models is, I think, OpenAI's name for this.  
**Translation:** 

**[1072.16s] English:** They had this new API in the fall, which they called the Reinforcement Fine Tuning API.  
**Translation:** 

**[1077.36s] English:** This is the idea that you use the techniques.  
**Translation:** 

**[1079.38s] English:** Of reinforcement.  
**Translation:** 

**[1080.00s] English:** Learning, which is a whole framework of AI, has a deep literature to summarize.  
**Translation:** 

**[1085.46s] English:** It's often known as trial-and-error learning, or the subfield of AI where you're trying to  
**Translation:** 

**[1090.58s] English:** Make sequential decisions in a certain, potentially noisy environment. There are lots of ways we could  
**Translation:** 

**[1096.98s] English:** Go down that, but fine-tuning language models where they can generate an answer, and then you  
**Translation:** Vocabulary: sequential: 顺序的

**[1102.46s] English:** Check to see if the answer matches the true solution. For math or code, you have an exactly.  
**Translation:** 

**[1108.18s] English:** Correct answer for math. You can have unit tests for code. And what we're doing is we are checking...  
**Translation:** 

**[1113.00s] English:** The language models work, and we're giving it multiple opportunities on the same questions.  
**Translation:** 

**[1116.92s] English:** To see if it is right, and if you keep doing this, the models can learn to improve in a verifiable manner.  
**Translation:** Vocabulary: verifiable: 可验证的

**[1121.66s] English:** Domains to a great extent. It works really well. It's a newer technique in the academic literature.  
**Translation:** 

**[1127.42s] English:** It's been used at Frontier Labs in the U.S., which don't share every detail, for multiple years. So,  
**Translation:** Vocabulary: frontier: 前沿领域

**[1133.38s] English:** This is the idea of using reinforcement learning with language models, and it has  
**Translation:** 

**[1138.00s] English:** Been used in the U.S. for multiple years, so this is the idea of using reinforcement learning with  
**Translation:** Vocabulary: reinforcement: 强化

**[1138.16s] English:** Language models. And we should say that there's a lot of exciting stuff going on in the,  
**Translation:** 

**[1144.32s] English:** Again, across the stack, but the post-training—probably this year, there's going to be a lot.  
**Translation:** 

**[1148.70s] English:** Of interesting developments in the post-training, we'll talk about it. I almost forgot to mention that.  
**Translation:** 

**[1153.38s] English:** About the difference between DeepSeq v3 and R1 on the user experience side, so  
**Translation:** 

**[1158.28s] English:** Forget the technical stuff; forget all that. Just think about people who don't know anything about AI.  
**Translation:** 

**[1163.50s] English:** They show up. Like, what's the actual experience? What's the use case for each one when they do?  
**Translation:** 

**[1167.98s] English:** Actually, like typing and talking to it, what is each good at, and that kind of thing. So, let's start with...  
**Translation:** 

**[1172.56s] English:** DeepSeek V3: Again, it's what more people would have tried something like it. You ask it a question.  
**Translation:** 

**[1176.98s] English:** It'll start generating tokens very fast, and those tokens will look like a very human, legible answer.  
**Translation:** 

**[1183.94s] English:** It will be some sort of markdown list, which might have formatting to help you draw out the core details.  
**Translation:** Vocabulary: formatting: 格式; markdown: 标记语言

**[1191.18s] English:** The answer will generate tens to hundreds of tokens, and a token is normally a word for common usage.  
**Translation:** 

**[1198.24s] English:** Words or a subword part.  
**Translation:** Vocabulary: subword: 子词; token: 令牌

**[1200.00s] English:** In a longer word, and it will look like a very high-quality Reddit or Stack Overflow answer.  
**Translation:** 

**[1206.92s] English:** These models are really getting good at doing this across a wide variety of domains. Even  
**Translation:** Vocabulary: overflow: 溢出

**[1212.48s] English:** Things that, if you're an expert, or things that are close to the fringe of knowledge, they will still  
**Translation:** 

**[1217.68s] English:** I am fairly good at. Cutting-edge AI topics that I do research on; these models are capable of.  
**Translation:** Vocabulary: fringe: 边缘领域

**[1224.92s] English:** Study aids are regularly updated. Where this changes with the DeepSeq R1,  
**Translation:** 

**[1231.46s] English:** What is called these reasoning models is when you see tokens coming from these models to start.  
**Translation:** 

**[1236.36s] English:** It will be a large chain of thought process. We'll get back to chain of thought in a second.  
**Translation:** 

**[1242.50s] English:** Which looks like a lot of tokens, where the model is explaining the problem. The model will often  
**Translation:** 

**[1247.66s] English:** Break down the problem and be like, "Okay, they asked me for this. Let's break it down.  
**Translation:** 

**[1251.96s] English:** I'm going to need to do this, and you'll see all of this generated.  
**Translation:** 

**[1254.92s] English:** From the model, it'll come very fast in most user experiences. These APIs are very fast, so you'll  
**Translation:** 

**[1259.64s] English:** See a lot of tokens, a lot of words show up really fast. It'll keep flowing on the screen, and this...  
**Translation:** 

**[1264.14s] English:** Is all the reasoning process. And then, eventually, the model will change its tone in R1, and it'll  
**Translation:** 

**[1269.40s] English:** Write the answer, summarizing the reasoning process, and provide a similar response to the first.  
**Translation:** 

**[1275.30s] English:** Types of models. But in DeepSeq's case, which is part of why this was so popular, even outside,  
**Translation:** 

**[1281.92s] English:** The AI community can see how the language model,  
**Translation:** 

**[1284.92s] English:** Is breaking down problems, and then you get this answer on the technical side. They train the model.  
**Translation:** 

**[1290.46s] English:** To do this specifically, where they have a section which is reasoning, and then it generates a  
**Translation:** Vocabulary: generates: 产生

**[1294.30s] English:** Special token, which is probably hidden from the user most of the time, which says, "okay,  
**Translation:** 

**[1297.60s] English:** I'm starting the answer. So, the model is trained to do this two-stage process on its own.  
**Translation:** Vocabulary: token: 标记

**[1302.82s] English:** If you use a similar model, say, in OpenAI, OpenAI's user interface is trying to summarize,  
**Translation:** 

**[1308.54s] English:** This process for you nicely by kind of showing the sections that the model is doing, and it'll.  
**Translation:** Vocabulary: interface: 用户界面; nicely: 良好地; summarize: 总结

**[1314.92s] English:** Kind of click through. It'll say, "Breaking down the problem, making X calculation.  
**Translation:** 

**[1320.00s] English:** Cleaning the result, and then the answer will come, something like OpenAI.  
**Translation:** 

**[1323.82s] English:** Maybe it's useful here to go through an example of a DeepSeek R1 reasoning.  
**Translation:** 

**[1329.04s] English:** Yeah, so if you're looking at the screen here, what you'll see is a screenshot of the DeepSeek.  
**Translation:** 

**[1334.42s] English:** Chat app, and at the top is "Thought" for 157 seconds with the drop-down arrow. underneath,  
**Translation:** 

**[1341.10s] English:** That, if we were in an app that we were running, the drop-down arrow would have the reasoning.  
**Translation:** Vocabulary: underneath: 在...下方

**[1344.38s] English:** So, in this case, the specific question, which I'm philosophically/slash pothead-inclined,  
**Translation:** 

**[1351.46s] English:** So, this is asking DeepSeek R1 for one truly novel insight about humans, and it reveals,  
**Translation:** Vocabulary: philosophically: 从哲学角度

**[1360.30s] English:** The reasoning, and basically the truly novel aspect is what's pushing the reasoning to:  
**Translation:** 

**[1366.74s] English:** Constantly, the model asks itself, "Is this truly novel?" So it's actually challenging.  
**Translation:** 

**[1370.88s] English:** Itself to be more novel and more counterintuitive.  
**Translation:** 

**[1374.38s] English:** Uh, more, uh, less cringe, I suppose. So, some of the reasoning goes like this: uh, this is just  
**Translation:** Vocabulary: counterintuitive: 违反直觉的; cringe: 尴尬

**[1380.42s] English:** Snapshots. Alternatively, humans have a unique meta-emotion where they feel emotions about...  
**Translation:** 

**[1385.08s] English:** Their own emotions, such as feeling guilty about being angry, can lead to recursive emotional layering.  
**Translation:** Vocabulary: alternatively: 或者; layering: 叠加; recursive: 递归; snapshots: 快照

**[1389.46s] English:** Creates complex motivational drives that don't exist in other animals. The insight is that.  
**Translation:** 

**[1394.02s] English:** Human emotions are nested, so it's like reasoning through how humans feel emotions.  
**Translation:** Vocabulary: motivational: 激励的; nested: 嵌套的

**[1399.56s] English:** It's reasoning about meta-emotions.  
**Translation:** 

**[1401.12s] English:** It's going to have pages and pages of this. It's almost too much to actually read.  
**Translation:** 

**[1404.38s] English:** But it's nice to skim as it's coming.  
**Translation:** 

**[1406.30s] English:** It's a stream of consciousness, like that found in James Joyce's works, and then it goes,  
**Translation:** 

**[1410.52s] English:** Wait, the user wants something that's not seen anywhere else. Let me dig deeper, and consider.  
**Translation:** 

**[1417.32s] English:** The human ability to hold contradictory beliefs simultaneously. Cognitive dissonance is known,  
**Translation:** Vocabulary: cognitive: 认知; contradictory: 矛盾

**[1421.74s] English:** But perhaps the function is to allow flexible adaptation, so on and so forth. I mean,  
**Translation:** 

**[1427.66s] English:** That really captures the public imagination: "Holy shit, this isn't,  
**Translation:** Vocabulary: adaptation: 适应; flexible: 灵活

**[1434.38s] English:** I mean, intelligence—slash—an almost like inkling of sense.  
**Translation:** 

**[1440.00s] English:** Because you're thinking through it, you're self-reflecting, you're deliberating.  
**Translation:** Vocabulary: deliberating: 仔细考虑

**[1444.56s] English:** And the final result of that, after 157 seconds, is that humans instinctively convert selfish desires into cooperative systems.  
**Translation:** 

**[1453.60s] English:** By collectively pretending that abstract rules, money, laws, and rights are real.  
**Translation:** Vocabulary: convert: 转变; cooperative: 合作的; desires: 欲望; instinctively: 本能地

**[1458.48s] English:** These shared hallucinations act as "games," where competition is secretly redirected to benefit the group.  
**Translation:** 

**[1465.10s] English:** Turning conflict into society's fuel.  
**Translation:** Vocabulary: hallucinations: 集体幻觉

**[1467.52s] English:** Pretty profound. I mean, you know.  
**Translation:** 

**[1471.70s] English:** This is a potential digression, but a lot of people have found that these reasoning models can sometimes produce much more eloquent text.  
**Translation:** Vocabulary: digression: 离题; eloquent: 文雅; profound: 深奥

**[1480.40s] English:** That is at least an interesting example, I think, depending on how open-minded you are.  
**Translation:** 

**[1484.96s] English:** You find language models interesting, or not, and there's a spectrum there.  
**Translation:** 

**[1488.22s] English:** Well, I mean, some of it, we'll talk about different benchmarks and so on, but some is just a vibe.  
**Translation:** 

**[1492.82s] English:** Like that, in itself, is a let's say, "quote," fire tweet.  
**Translation:** Vocabulary: benchmarks: 参考标准

**[1497.52s] English:** Yeah.  
**Translation:** 

**[1498.06s] English:** If I'm trying to produce something, something where people are like, "Oh, shit.  
**Translation:** 

**[1503.32s] English:** Okay, so that's a chance I'll probably return to it more.  
**Translation:** 

**[1507.60s] English:** How were they able to achieve such low costs for both training and inference?  
**Translation:** Vocabulary: inference: 推断

**[1513.40s] English:** Maybe you could start with the training first.  
**Translation:** 

**[1515.60s] English:** Yeah, so there are two main techniques that they implemented, which are probably the majority of their efficiency.  
**Translation:** Vocabulary: implemented: 执行

**[1522.60s] English:** And then there are a lot of implementation details that maybe we'll gloss over or get into later.  
**Translation:** 

**[1527.52s] English:** That sort of contributes to it.  
**Translation:** 

**[1528.64s] English:** But those two main things are: one, they went to a mixture of experts model, which we'll define in a second.  
**Translation:** 

**[1535.76s] English:** And then, another thing is that they invented a new technique called MLA latent attention.  
**Translation:** Vocabulary: mixture: 混合模型

**[1540.56s] English:** Both of these are big deals.  
**Translation:** 

**[1542.10s] English:** A mixture of experts has been in the literature for a handful of years.  
**Translation:** 

**[1546.24s] English:** And OpenAI, with GPT-4, was the first one to productize a mixture-of-experts model.  
**Translation:** 

**[1551.58s] English:** And what this means is, when you look at the common models around that most people have been able to,  
**Translation:** Vocabulary: productize: 商品化

**[1557.52s] English:** To interact with those that are open, right?  
**Translation:** 

**[1559.64s] English:** Think.  
**Translation:** 

**[1560.00s] English:** LAMA. LAMA is a dense model, i.e., every single parameter or neuron is activated as you're going.  
**Translation:** 

**[1567.30s] English:** Through the model for every single token you generate, right? Now, with a mixture of experts,...  
**Translation:** Vocabulary: neuron: 神经元; parameter: 参数; token: 标记

**[1572.10s] English:** Model, you don't do that, right? How does a human actually work, right? It's like, oh, well,  
**Translation:** 

**[1576.48s] English:** My visual cortex is active when I'm thinking about, you know, vision tasks, and like, you know,  
**Translation:** Vocabulary: cortex: 皮层

**[1580.62s] English:** Other things, right? My amygdala is when I'm scared, right? These different aspects of yours, right?  
**Translation:** 

**[1585.18s] English:** Brains are focused on different things. A mixture of experts model attempts to approximate this.  
**Translation:** Vocabulary: amygdala: 杏仁体; approximate: 近似

**[1589.68s] English:** Some extent. It's nowhere close to what a brain architecture is, but different portions of the  
**Translation:** 

**[1594.12s] English:** Model activate, right? You'll have a set number of experts in the model, and a set number that  
**Translation:** Vocabulary: portions: 部分

**[1599.46s] English:** Are activated each time, and this dramatically reduces both your training and inference costs.  
**Translation:** 

**[1603.72s] English:** Because now you're, you know, if you think about the parameter count as the sort of  
**Translation:** Vocabulary: dramatically: 大幅度地

**[1608.64s] English:** Total embedding space for all of this knowledge that you're compressing down during training,  
**Translation:** 

**[1614.28s] English:** When you're embedding this data in, instead of having to activate every single parameter every  
**Translation:** Vocabulary: compressing: 压缩; embedding: 嵌入

**[1619.34s] English:** Single time, you're going to have to activate every single parameter every single time.  
**Translation:** 

**[1619.68s] English:** You're training or running inference. Now, you can just activate a subset, and the model will learn.  
**Translation:** Vocabulary: inference: 推理

**[1624.72s] English:** Which expert to route to for different tasks. And so this is a humongous innovation in terms of,  
**Translation:** 

**[1630.98s] English:** Hey, I can continue to grow the total embedding space of parameters. And so, DeepSeek's model is,  
**Translation:** Vocabulary: humongous: 巨大的

**[1635.52s] English:** You know, 600-something billion parameters, right? Relative to LAMA 405B, it's 405 billion.  
**Translation:** 

**[1640.68s] English:** Parameters, right? Relative to LAMA 70B, it's 70 billion parameters, right? So this model,...  
**Translation:** 

**[1644.92s] English:** Technically, it has more embedding space for information, right? To compress all of the  
**Translation:** 

**[1649.20s] English:** World's knowledge that's on the Internet down. But at the same time, it is only activating.  
**Translation:** Vocabulary: compress: 压缩; technically: 从技术上说

**[1654.04s] English:** Around 37 billion of the parameters. So, only 37 billion of these parameters actually need to be.  
**Translation:** 

**[1659.32s] English:** Computed every single time you're training or inference data is used out of it. And so, versus,  
**Translation:** Vocabulary: computed: 计算

**[1665.16s] English:** Versus again, a LAMA model, 70 billion parameters must be activated, or 405 billion parameters must.  
**Translation:** 

**[1669.76s] English:** Be activated. So, you've dramatically reduced your compute cost when you're doing training.  
**Translation:** Vocabulary: compute: 计算

**[1673.50s] English:** And inference with this mixture-of-experts architecture. So, we break down where it actually  
**Translation:** 

**[1678.80s] English:** Applies.  
**Translation:** 

**[1679.20s] English:** And go into.  
**Translation:** 

**[1680.00s] English:** The transformer is useful, let's go into it. The transformer is a thing that is talked about.  
**Translation:** 

**[1685.66s] English:** About a lot, and we will not cover every detail. Uh, essentially, the transformer is built on repeated  
**Translation:** 

**[1692.28s] English:** Blocks of this attention mechanism, and then a traditional dense, fully connected, multi-layer.  
**Translation:** 

**[1698.48s] English:** Perception: Whatever word you want to use, for your normal neural network, and you alternate these.  
**Translation:** 

**[1702.62s] English:** Blocks: There are other details, and where a mixture of experts is applied is that this dense model.  
**Translation:** Vocabulary: alternate: 交替; mixture: 混合; neural: 神经; perception: 感知

**[1707.66s] English:** The dense model holds most of the weights, if you count them in a transformer model, so you can get.  
**Translation:** 

**[1714.70s] English:** Really big gains from those mixtures of experts on parameter efficiency at training and inference.  
**Translation:** Vocabulary: inference: 推理; mixtures: 混合; parameter: 参数

**[1719.08s] English:** Because you get this efficiency by not activating all of these parameters, we should also say that a  
**Translation:** 

**[1725.56s] English:** Transformer is a giant neural network, yeah, and then there's been something for 15 years now.  
**Translation:** 

**[1732.48s] English:** Called the deep learning revolution, networks have gotten larger and larger, but in a certain point.  
**Translation:** 

**[1737.66s] English:** Scaling laws appeared where people realized this is a scaling law, by the way, representing...  
**Translation:** 

**[1743.34s] English:** Scaling Laws, where it became more and more formalized that "bigger is better" across multiple domains.  
**Translation:** 

**[1750.38s] English:** Dimensions of what "bigger" means, so, uh, and but these are all sorts of neural networks we're talking about.  
**Translation:** Vocabulary: dimensions: 维度

**[1755.62s] English:** About it, and we're talking about different architectures of how to construct.  
**Translation:** 

**[1759.58s] English:** These neural networks are designed such that both the training and the inference on them are super efficient, yeah.  
**Translation:** 

**[1764.42s] English:** Every different type of model has a different scaling law for it.  
**Translation:** 

**[1767.66s] English:** Which is effectively how much compute you put into the architecture will get you to different levels.  
**Translation:** Vocabulary: compute: 计算能力

**[1774.32s] English:** Of performance at test tasks and a mixture of experts is one of the things at training time, even if you  
**Translation:** 

**[1779.72s] English:** Don't consider the inference benefits, which are also significant at training time, your efficiency with.  
**Translation:** 

**[1784.24s] English:** Your GPUs are dramatically improved by using this architecture, if it is well implemented.  
**Translation:** 

**[1788.32s] English:** So, you can get effectively the same performance model and evaluation scores with numbers like 30.  
**Translation:** Vocabulary: dramatically: 显著地; evaluation: 评估; implemented: 实现

**[1796.46s] English:** Less compute, I think that's the difference between the two, so that's the difference between the two.  
**Translation:** 

**[1797.66s] English:** There's going to be a wide variation depending on your implement.  
**Translation:** Vocabulary: implement: 实施方案; variation: 变化程度

**[1800.00s] English:** Details and stuff, but it is just important to realize that this type of technical innovation  
**Translation:** 

**[1805.20s] English:** Is something that gives huge gains. And I expect most companies that are serving their models to  
**Translation:** 

**[1811.42s] English:** Move to this mixture of experts implementation. Historically, the reason why not everyone might  
**Translation:** 

**[1816.46s] English:** It is because of implementation complexity, especially when dealing with these big models.  
**Translation:** Vocabulary: complexity: 复杂性; historically: 历史上; implementation: 实施; mixture: 混合体

**[1821.18s] English:** So, this is one of the things that DeepSeek gets credit for; they do this extremely well.  
**Translation:** 

**[1825.68s] English:** They do a mixture of experts extremely well. This architecture, for what is called DeepSeek MOE,  
**Translation:** 

**[1831.44s] English:** MOE is the shortened version of Mixture of Experts; it's been around for multiple papers. This part of  
**Translation:** 

**[1837.02s] English:** Their training infrastructure is not new to these models alone. And the same goes for what Dylan mentioned.  
**Translation:** 

**[1842.90s] English:** With multi-headlight inattention, it's all about reducing memory usage during inference, and same.  
**Translation:** 

**[1849.00s] English:** Things during training can be handled by using some fancy low-rank approximation math. If you get into the details,...  
**Translation:** Vocabulary: approximation: 近似; inattention: 不注意; inference: 推理

**[1854.74s] English:** With this,  
**Translation:** 

**[1855.68s] English:** Latent attention—it's one of those things I look at. It's like, okay, they're doing really  
**Translation:** 

**[1860.34s] English:** Complex implementations because there are other parts of language models, such as  
**Translation:** 

**[1864.44s] English:** Embeddings that are used to extend the context length. The common one that DeepSeek used is  
**Translation:** Vocabulary: embeddings: 嵌入表示; implementations: 实现方式

**[1869.28s] English:** Rotary positional embeddings, which is called ROPE, and if you want to use ROPE with a normal MoE,  
**Translation:** 

**[1875.34s] English:** It's kind of a sequential thing. You take two of the attention matrices and you rotate them.  
**Translation:** Vocabulary: matrices: 矩阵; positional: 位置; rotary: 旋转; rotate: 转动; sequential: 顺序

**[1880.26s] English:** By a complex value rotation, which is a matrix multiplication. With DeepSeek's  
**Translation:** 

**[1885.68s] English:** MLA, with this new attention architecture, they need to do some clever things because they're not  
**Translation:** Vocabulary: matrix: 矩阵; multiplication: 乘法

**[1890.50s] English:** Set up the same, and it just makes the implementation complexity much higher. So they're managing all of  
**Translation:** 

**[1895.20s] English:** These things, and these are probably the sorts of things that OpenAI and these closed labs are doing.  
**Translation:** 

**[1900.38s] English:** We don't know if they're doing the exact same techniques, but they actually shared them with us.  
**Translation:** 

**[1903.64s] English:** The world, which is really nice to feel, is at the cutting edge of efficient language models.  
**Translation:** 

**[1908.50s] English:** Training. And some of this requires low-level engineering. It's a giant mess, and there's a lot of trickery involved.  
**Translation:** 

**[1915.68s] English:** So, as I understand, that went below CUDA. So they go super-low-level programming.  
**Translation:** Vocabulary: trickery: 诡计

**[1920.00s] English:** GPUs effectively, NVIDIA builds this library called Nickel, right? In which you know, when you're  
**Translation:** 

**[1926.46s] English:** Training a model, you have all these communications between every single layer of the model, and you  
**Translation:** Vocabulary: nickel: 镍

**[1931.02s] English:** May have over 100 layers. What does "NCCL" stand for? It's Nvidia Communications Collectives.  
**Translation:** 

**[1936.08s] English:** Library, nice. Um, and so damn, when you're training a model, right, you're gonna have all  
**Translation:** 

**[1943.84s] English:** These all reduce and gather, right? Between each layer, between the multi-layer.  
**Translation:** 

**[1949.00s] English:** Perceptron or feed-forward network, and the attention mechanism—you'll have.  
**Translation:** Vocabulary: perceptron: 感知机

**[1952.52s] English:** Basically, the model synchronized correctly, or you'll have all the reducers and  
**Translation:** 

**[1957.24s] English:** All gather, um, and this is a communication between all the GPUs in the network, whether  
**Translation:** Vocabulary: reducers: 减少器; synchronized: 同步

**[1961.40s] English:** Whether it's in training or inference, NVIDIA has a standard library, and this is one of the reasons.  
**Translation:** 

**[1965.64s] English:** Why it's really difficult to use anyone else's hardware for training is because no one's  
**Translation:** Vocabulary: inference: 推断

**[1970.70s] English:** Really, they've built a standard communications library, and NVIDIA has done this at a somewhat higher level.  
**Translation:** 

**[1975.30s] English:** Level, right? A deep seek is because they have certain limitations around.  
**Translation:** 

**[1978.94s] English:** The  
**Translation:** 

**[1979.00s] English:** GPUs that they have access to the interconnects are limited to some extent, um, by the restrictions.  
**Translation:** Vocabulary: interconnects: 互联接口

**[1984.68s] English:** Of the GPUs that were shipped into China legally, not the ones that are smuggled but legally shipped.  
**Translation:** 

**[1988.92s] English:** In that, they had to figure out how to get efficiencies right when training this model.  
**Translation:** Vocabulary: efficiencies: 效率; smuggled: 走私

**[1995.32s] English:** One of those things is that, instead of just calling the NVIDIA library "nickel," they  
**Translation:** 

**[2000.66s] English:** Instead, they created their own communications schedule, which the lab did not participate in.  
**Translation:** 

**[2009.00s] English:** Labs that they used to train the NVIDIA library, Nickle, right? They scheduled their own communications.  
**Translation:** 

**[2011.00s] English:** Uh, which labs did they use to train the NVIDIA library Nickel? Right? They  
**Translation:** Vocabulary: nickel: 镍

**[2011.88s] English:** Didn't they avoid talking about the implementation details? This is some of what they did, probably.  
**Translation:** 

**[2015.24s] English:** Not as well as, maybe not as well as DeepSeek, because DeepSeek—you know, necessity is the  
**Translation:** Vocabulary: implementation: 实施方案; necessity: 必要性

**[2019.64s] English:** Mother of Innovation, and they had to do this, whereas, in the case of OpenAI, they have...  
**Translation:** 

**[2025.50s] English:** People that do this sort of stuff, like Anthropic, etc., but you know, DeepSeek certainly did it publicly.  
**Translation:** 

**[2030.34s] English:** And they may have done it even better because they were gimped on a certain aspect of the chips that.  
**Translation:** 

**[2034.74s] English:** They have access to, and so they scheduled communication between the GPUs and NVIDIA.  
**Translation:** 

**[2039.00s] English:** Library, nickel, right? They scheduled their own communications, uh, they scheduled their own.  
**Translation:** 

**[2040.00s] English:** By scheduling specific SMs.  
**Translation:** Vocabulary: scheduling: 安排

**[2042.58s] English:** SMSs can be thought of as like the core on a GPU, right?  
**Translation:** 

**[2046.22s] English:** So, there are hundreds of cores.  
**Translation:** 

**[2047.84s] English:** Or there are a bit over a hundred cores (SMs) on a GPU.  
**Translation:** 

**[2051.36s] English:** And they were specifically scheduling,  
**Translation:** 

**[2053.24s] English:** Hey, which ones are running the model?  
**Translation:** 

**[2054.54s] English:** Which ones are doing allreduce?  
**Translation:** Vocabulary: allreduce: 全部减少

**[2055.84s] English:** Which one is doing an all-gather, right?  
**Translation:** 

**[2057.38s] English:** And they would flip back and forth between them.  
**Translation:** 

**[2059.06s] English:** And this requires extremely low-level programming.  
**Translation:** 

**[2062.18s] English:** This is what Nickel does automatically.  
**Translation:** 

**[2063.48s] English:** Or, other NVIDIA libraries handle this automatically, usually.  
**Translation:** 

**[2066.58s] English:** Yeah, exactly.  
**Translation:** 

**[2067.10s] English:** And so, technically, they're using, you know, PTX.  
**Translation:** 

**[2070.08s] English:** Which is kind of like,  
**Translation:** Vocabulary: technically: 实际上

**[2071.38s] English:** You could think of it as like an assembly-type language.  
**Translation:** 

**[2073.70s] English:** It's not exactly that instruction set, right?  
**Translation:** 

**[2075.82s] English:** Like coding directly to assembly or instruction set.  
**Translation:** 

**[2078.18s] English:** It's not exactly that.  
**Translation:** 

**[2079.44s] English:** But that's still part of technically CUDA.  
**Translation:** 

**[2082.04s] English:** But it's like, do I want to write in Python?  
**Translation:** 

**[2084.16s] English:** You know, is there a way to use PyTorch equivalents and call NVIDIA libraries?  
**Translation:** 

**[2087.04s] English:** Do I want to go down to the C-level, right?  
**Translation:** 

**[2089.04s] English:** Or, you know, encode even lower-level  
**Translation:** 

**[2090.60s] English:** Or do I want to go all the way down?  
**Translation:** Vocabulary: encode: 编码

**[2091.54s] English:** To the assembly or ISO level?  
**Translation:** 

**[2093.18s] English:** And there are cases where you go all the way down there.  
**Translation:** 

**[2095.80s] English:** At the very big labs,  
**Translation:** 

**[2097.14s] English:** But most companies just don't do that, right?  
**Translation:** 

**[2099.62s] English:** Because it's a waste of time.  
**Translation:** 

**[2100.76s] English:** And the efficiency gains you get are not worth it.  
**Translation:** 

**[2103.74s] English:** But DeepSeq's implementation is so complex, right?  
**Translation:** 

**[2106.84s] English:** Especially with their mix of experts, right?  
**Translation:** Vocabulary: implementation: 实施方案

**[2109.24s] English:** People have done a mixture of experts.  
**Translation:** 

**[2110.76s] English:** But they're generally eight to sixteen experts, right?  
**Translation:** Vocabulary: mixture: 混合

**[2113.36s] English:** And they activate, too.  
**Translation:** 

**[2114.40s] English:** So, you know, one of the words that we like to use.  
**Translation:** 

**[2117.00s] English:** Is it like the sparsity factor, right?  
**Translation:** 

**[2118.66s] English:** Or usage, right?  
**Translation:** Vocabulary: sparsity: 稀疏程度

**[2119.44s] English:** So, you might have four, you know,  
**Translation:** 

**[2121.50s] English:** One-fourth of your model activated, right?  
**Translation:** 

**[2123.70s] English:** And that's what Mistral's model, right?  
**Translation:** 

**[2127.24s] English:** Their model that really catapulted them to, like,  
**Translation:** Vocabulary: catapulted: 推动

**[2129.92s] English:** Oh my God, they're really, really good.  
**Translation:** 

**[2132.24s] English:** OpenAI has also had models that are MOE.  
**Translation:** 

**[2134.16s] English:** And so have all the other major labs.  
**Translation:** 

**[2137.94s] English:** But what DeepSeq did that, perhaps, may have been limited to only the leading labs.  
**Translation:** 

**[2140.72s] English:** Have only just started recently doing.  
**Translation:** 

**[2142.20s] English:** Is it really has such a high sparsity factor, right?  
**Translation:** 

**[2144.24s] English:** It's not one-fourth of the model, right?  
**Translation:** 

**[2146.00s] English:** Two out of eight experts activated.  
**Translation:** 

**[2147.58s] English:** Every time you go through the model,  
**Translation:** 

**[2149.24s] English:** It's 8 out of 256.  
**Translation:** 

**[2151.20s] English:** And there are different implementations.  
**Translation:** 

**[2152.94s] English:** For a mixture of experts, where you can have  
**Translation:** Vocabulary: implementations: 实施方案

**[2155.08s] English:** Some of these experts that are,  
**Translation:** 

**[2157.00s] English:** You know, they're not going to be able to do that.  
**Translation:** 

**[2157.10s] English:** Always activated; which is just looks like.  
**Translation:** 

**[2160.00s] English:** A small neural network, and then all the tokens go through that, and then they also go through some.  
**Translation:** Vocabulary: neural: 神经网络

**[2166.08s] English:** That are selected by this routing mechanism, and one of the innovations in DeepSeek's architecture.  
**Translation:** 

**[2172.96s] English:** Is that they change the routing mechanism in a mixture-of-expert models, there's something called  
**Translation:** Vocabulary: innovations: 创新; routing: 路由机制

**[2177.36s] English:** An auxiliary loss, which effectively means during training you want to make sure that all of these  
**Translation:** 

**[2182.72s] English:** Experts are used across the tasks that the model sees, why there can be failures and a mixture of results.  
**Translation:** 

**[2188.32s] English:** Experts say that when you're doing this training, the one objective is token prediction accuracy.  
**Translation:** 

**[2195.52s] English:** And if you just let turning go with a mixture of an expert model and your own, it can be that the model...  
**Translation:** Vocabulary: mixture: 混合; token: 标记

**[2201.60s] English:** Learns to only use a subset of the experts, and in the Mixture of Experts (MoE) literature, there's something called  
**Translation:** 

**[2207.20s] English:** The auxiliary loss, which helps balance them, but if you think about the loss functions of  
**Translation:** 

**[2213.04s] English:** Deep learning: this even connects to the "bitter lesson" is that you want to have the minimum.  
**Translation:** 

**[2218.32s] English:** Inductive bias in your model to let it learn maximally, and this auxiliary loss:  
**Translation:** Vocabulary: inductive: 归纳; maximally: 最大化地

**[2223.20s] English:** Balancing across experts could be seen as an intention to improve the prediction accuracy of the tokens.  
**Translation:** 

**[2229.28s] English:** So, we don't know the exact extent that the DeepSeek MOE change is, which is instead of doing an  
**Translation:** Vocabulary: balancing: 平衡

**[2234.40s] English:** Auxiliary loss has an extra parameter in its routing, which they update after the batches.  
**Translation:** 

**[2239.44s] English:** This parameter to make sure that the next batches all have a similar use of experts and this type of.  
**Translation:** Vocabulary: parameter: 参数

**[2244.96s] English:** Change can be big, it can be small, but they add up over time.  
**Translation:** 

**[2248.32s] English:** And this is the sort of thing that just points to them innovating, and I'm sure.  
**Translation:** Vocabulary: innovating: 创新

**[2252.00s] English:** All the labs that are training Big Moes are looking at these sorts of things, which is  
**Translation:** 

**[2255.68s] English:** Getting away from the auxiliary loss, some of them might already use it, but you just keep.  
**Translation:** 

**[2259.12s] English:** You keep accumulating gains, and we'll talk about the philosophy of training and how you organize.  
**Translation:** 

**[2264.00s] English:** These organizations, and a lot of it is just compounding small improvements over time.  
**Translation:** Vocabulary: accumulating: 累积; compounding: 复利增长

**[2268.96s] English:** Your data in your architecture, and your post-training processes and how they integrate with each other.  
**Translation:** 

**[2273.92s] English:** DeepSeek does the same thing, and some of them are shared—or a lot—we have to take them on face to face.  
**Translation:** Vocabulary: integrate: 融合

**[2278.32s] English:** Face value that they share their most.  
**Translation:** 

**[2280.00s] English:** Important details. I mean, the architecture and the weights are out there. So we're seeing what  
**Translation:** 

**[2282.94s] English:** They're doing it, and it adds up. Going back to the efficiency and complexity point,  
**Translation:** 

**[2288.18s] English:** Right? It's 32 versus four, right? For example, in mixed-draw and other MOE models that have been publicly.  
**Translation:** Vocabulary: complexity: 复杂性

**[2293.56s] English:** Released, so this ratio is extremely high. And, sort of, what Nathan was getting at there was,...  
**Translation:** 

**[2298.12s] English:** When you have such a different level of sparsity, you can't just have every GPU have the entire dataset.  
**Translation:** Vocabulary: dataset: 数据集; sparsity: 稀疏性

**[2304.90s] English:** Model, right? The model is too big. There's too much complexity there. So, you have to split it up.  
**Translation:** 

**[2308.44s] English:** The model with different types of parallelism, right? And so you might have different experts.  
**Translation:** 

**[2312.80s] English:** On different GPU nodes. But now, what happens when you get this set of data—hey, all of it?  
**Translation:** 

**[2319.10s] English:** It looks like this one way, and all of it should route to one part of my model, right? So when all of it...  
**Translation:** 

**[2325.44s] English:** Routes to one part of the model, then you can have this overloading of a certain set of the GPU.  
**Translation:** 

**[2332.70s] English:** Resources, or a certain set of GPUs, and then the rest of the training network sits.  
**Translation:** Vocabulary: overloading: 超载; routes: 路由

**[2338.32s] English:** I have to do this. I have to do this. I have to do this. I have to do this. I have to do this.  
**Translation:** 

**[2338.42s] English:** Because all of the tokens are just routing to that. So, this is the biggest complexity. One of  
**Translation:** Vocabulary: routing: 路由

**[2341.88s] English:** The biggest complexities with running a very sparse mixture of experts model, i.e., this 32, involve...  
**Translation:** 

**[2348.28s] English:** Ratio versus this 4:1 ratio, is that you end up with so many of the experts just sitting there.  
**Translation:** Vocabulary: complexities: 复杂性; mixture: 混合模型; sparse: 稀疏的

**[2353.66s] English:** Idle. So, how do I load balance between them? How do I schedule the communications between them?  
**Translation:** 

**[2358.30s] English:** This is a lot of the extremely low-level detailed work that they figured out in the public first.  
**Translation:** 

**[2364.98s] English:** And potentially, second or third in the world, and maybe even,  
**Translation:** 

**[2368.44s] English:** First, in some cases, what lesson do you draw from the bitter lesson?  
**Translation:** 

**[2374.52s] English:** All of this? Where is this going to be the direction where a lot of the gain is going to be?  
**Translation:** 

**[2379.18s] English:** Which is this kind of low-level optimization? Or is this a short-term thing where the biggest  
**Translation:** Vocabulary: optimization: 优化

**[2385.34s] English:** Gains will be more on the algorithmic, high-level side of things, like post-training? Is this like a short?  
**Translation:** 

**[2391.66s] English:** Term leap because they figured out a hack, because constraints are often the mother of necessity.  
**Translation:** Vocabulary: algorithmic: 算法相关的; constraints: 限制; necessity: 必要性

**[2397.66s] English:** Invention? Or is there, is there?  
**Translation:** 

**[2400.00s] English:** Still, there are a lot of gains. I think we should summarize what "The Bitter Lesson" is actually about, is that:  
**Translation:** 

**[2404.26s] English:** The bitter lesson, essentially, if you paraphrase it, is that the types of training that will win,...  
**Translation:** 

**[2410.74s] English:** Out in deep learning, as we go, are those methods that are scalable in learning and search.  
**Translation:** Vocabulary: paraphrase: 改写; scalable: 可扩展的

**[2417.28s] English:** Is what it calls out, and this "scale" word gets a lot of attention in this interpretation that.  
**Translation:** 

**[2426.04s] English:** I use it effectively to avoid adding in the human priors to your learning process, and if you read  
**Translation:** Vocabulary: interpretation: 解释; priors: 先验知识

**[2434.10s] English:** The original essay is about how researchers will try to come up with what  
**Translation:** 

**[2439.58s] English:** Clever solutions to their specific problem that might get them small gains in the short term.  
**Translation:** 

**[2445.70s] English:** While simply enabling these deep learning systems to work efficiently and for these bigger problems,...  
**Translation:** 

**[2451.82s] English:** In the long term, it might be more likely to scale and continue to.  
**Translation:** Vocabulary: efficiently: 高效率地

**[2456.04s] English:** Drive success, and therefore, we were talking about relatively small implementation changes.  
**Translation:** 

**[2462.24s] English:** To the mixture of experts model, and therefore it's like okay, we will need a few more years to.  
**Translation:** Vocabulary: implementation: 实施方案; mixture: 混合模型

**[2468.56s] English:** Know if one of these is actually really crucial to the bitter lesson, but the bitter lesson is...  
**Translation:** 

**[2473.32s] English:** Really, this long-term arc of how simplicity can often win, and there are a lot of sayings in the  
**Translation:** Vocabulary: crucial: 至关重要的; simplicity: 简洁

**[2478.70s] English:** Industry, like the models, just want to learn; you have to give them the simple loss landscape where.  
**Translation:** 

**[2483.74s] English:** You put compute through the model, and then they  
**Translation:** Vocabulary: compute: 计算

**[2486.02s] English:** We'll learn and get barriers out of the way—that's where the power lies, something like nickel.  
**Translation:** 

**[2491.32s] English:** Comes in, where standardized code that can be used by a lot of people to create sort of simple...  
**Translation:** Vocabulary: barriers: 障碍; nickel: 镍; standardized: 标准化

**[2497.62s] English:** Innovations that can scale, which is why the hacks that I imagine are behind the code base for DeepSeek are...  
**Translation:** 

**[2504.02s] English:** Probably a giant mess. I'm sure they have deep-seek, definitely has codebases that are extremely.  
**Translation:** Vocabulary: codebases: 代码库; hacks: 修补; innovations: 创新

**[2508.60s] English:** Messy, where they're testing these new ideas, like multi-headlights and attention, probably start.  
**Translation:** 

**[2513.20s] English:** Could start in something like a Jupiter notebook, or somebody tries.  
**Translation:** Vocabulary: jupiter: 巨无霸笔记本

**[2516.02s] English:** Something on a few GPUs, and that is really messy.  
**Translation:** 

**[2520.00s] English:** But the stuff that trains the DeepSeq V3 and DeepSeq R1; those libraries, if you were to present them to us, I would guess are extremely high-quality code.  
**Translation:** 

**[2530.30s] English:** High-quality, readable code.  
**Translation:** 

**[2531.72s] English:** I think there is one aspect to note, though: that there is a general ability for that to transfer across different types of runs, right?  
**Translation:** 

**[2541.34s] English:** You may make really, really high-quality code for one specific model architecture at one size.  
**Translation:** 

**[2547.20s] English:** And then that is not transferable to: hey, when I make this architecture tweak, everything's broken again, right?  
**Translation:** Vocabulary: transferable: 可移植的; tweak: 调整

**[2553.42s] English:** Like, that's something that could be, you know, with their specific low-level coding of like scheduling SMs, which is specific to this model's architecture and size, right?  
**Translation:** 

**[2563.50s] English:** And whereas, like NVIDIA's collective communications library, is more like, "hey, it'll work for anything," right?  
**Translation:** 

**[2568.86s] English:** You want to do an all-reduce?  
**Translation:** 

**[2569.96s] English:** Great.  
**Translation:** 

**[2570.28s] English:** I don't care what your model architecture is.  
**Translation:** 

**[2571.80s] English:** It'll work.  
**Translation:** 

**[2572.50s] English:** And you're giving up a lot of performance when you do that, in many cases.  
**Translation:** 

**[2576.32s] English:** But it's worthwhile.  
**Translation:** 

**[2577.20s] English:** It's worthwhile for them to do this specific optimization for this specific run, given the constraints they have regarding compute.  
**Translation:** 

**[2583.80s] English:** I wonder how stressful it is to, like, you know, deal with these frontier models—initiating training, having the code to push the button—that now requires a large amount of money and time to train this.  
**Translation:** Vocabulary: compute: 计算; constraints: 限制; frontier: 前沿; initiating: 启动; optimization: 优化

**[2600.96s] English:** Like, there must be a lot of innovation on the debugging stage of making sure there's no bugs.  
**Translation:** 

**[2607.20s] English:** There's no issue; you're monitoring and visualizing every aspect of the training, and all that kind of stuff.  
**Translation:** Vocabulary: visualizing: 可视化

**[2612.90s] English:** When people are training, they have all these various dashboards, but the most simple one is your loss, right?  
**Translation:** 

**[2618.32s] English:** And it continues to go down.  
**Translation:** Vocabulary: dashboards: 仪表盘

**[2620.16s] English:** But, in reality, especially with more complicated stuff like MOE, the biggest problem with it—or FP8 training, which is another innovation, going to a lower precision number format (i.e., less accurate)—is that you end up with loss spikes, right?  
**Translation:** 

**[2632.32s] English:** And no one knows why the loss spike happened.  
**Translation:** Vocabulary: spike: 突增; spikes: 突增

**[2634.90s] English:** Some of them, you do.  
**Translation:** 

**[2635.84s] English:** Some of them, you do.  
**Translation:** 

**[2636.46s] English:** Some of them are bad.  
**Translation:** 

**[2637.20s] English:** I give AI2's example of what blue.  
**Translation:** 

**[2640.00s] English:** Up our earlier models is a subreddit called:  
**Translation:** 

**[2641.96s] English:** Microwave Gang. We love to shout.  
**Translation:** Vocabulary: microwave: 微波炉; subreddit: 子版块

**[2643.84s] English:** About this out. It's a real thing. You can pull.  
**Translation:** 

**[2645.94s] English:** Up, Microwave Gang. Essentially, it's a  
**Translation:** 

**[2647.86s] English:** Subreddit where everyone makes posts that  
**Translation:** 

**[2649.86s] English:** Are just the letter M's, so it's like,  
**Translation:** 

**[2651.26s] English:** So, there are extremely long sequences.  
**Translation:** 

**[2654.10s] English:** Of the letter M, and then the comments.  
**Translation:** 

**[2656.02s] English:** Are like, "beep, beep," because it's in the microwave, ends.  
**Translation:** 

**[2658.02s] English:** But if you pass this into a model that's trained to  
**Translation:** 

**[2659.92s] English:** Be a normal-producing text, it's extremely  
**Translation:** 

**[2662.14s] English:** High loss, because normally,  
**Translation:** 

**[2663.82s] English:** You see an M. You don't predict M's.  
**Translation:** 

**[2665.96s] English:** For a long time. So, this is  
**Translation:** 

**[2667.82s] English:** Something that caused the loss spikes for us.  
**Translation:** 

**[2670.00s] English:** But when you have a lot, like, this is old,  
**Translation:** 

**[2671.94s] English:** This is not recent, and when you  
**Translation:** 

**[2673.96s] English:** Have more mature data systems? That's not the thing.  
**Translation:** Vocabulary: mature: 成熟的

**[2676.00s] English:** That causes the loss spike. And what Dylan is saying,...  
**Translation:** 

**[2677.90s] English:** It is true, but it's like,  
**Translation:** 

**[2679.62s] English:** It's all about these sorts of ideas.  
**Translation:** 

**[2681.90s] English:** With regard to the stress, right?  
**Translation:** 

**[2683.80s] English:** These people are like: you know, you'll go out to  
**Translation:** 

**[2685.90s] English:** Dinner with a friend who works at one of these labs,  
**Translation:** 

**[2688.46s] English:** And they'll just be.  
**Translation:** 

**[2689.64s] English:** Looking at their phone every 10 minutes,  
**Translation:** 

**[2691.88s] English:** And they're not, like, you know, it's one thing if they're  
**Translation:** 

**[2693.72s] English:** Texting, but they're just like,  
**Translation:** 

**[2695.12s] English:** Is the loss provoking?  
**Translation:** 

**[2698.00s] English:** Tokens Per Second, Loss.  
**Translation:** Vocabulary: provoking: 激起争议的

**[2699.76s] English:** Not blown up. They're just  
**Translation:** 

**[2701.46s] English:** Watching this, and the heart rate goes.  
**Translation:** 

**[2703.74s] English:** Up if there's a spike, and some.  
**Translation:** 

**[2705.86s] English:** The level of spikes is normal, right? It'll  
**Translation:** 

**[2707.38s] English:** Recover and be back. Sometimes, a lot of the  
**Translation:** 

**[2709.66s] English:** The old strategy was like: you just stop the run.  
**Translation:** 

**[2711.94s] English:** Restart from the old version, and then.  
**Translation:** 

**[2713.80s] English:** Change the data mix, and then it keeps going.  
**Translation:** 

**[2716.14s] English:** There are even different types of spikes.  
**Translation:** 

**[2718.12s] English:** So, Dirk Greneveld.  
**Translation:** Vocabulary: spikes: 尖刺

**[2719.50s] English:** Has a theory that's like fast spikes.  
**Translation:** 

**[2721.72s] English:** And slow spikes, where there are  
**Translation:** 

**[2723.42s] English:** Sometimes, when you're looking at the loss and there are other parameters,  
**Translation:** 

**[2725.88s] English:** You can see it start to creep up.  
**Translation:** Vocabulary: creep: 缓慢增加

**[2727.18s] English:** And then it blows up, and that's really hard to.  
**Translation:** 

**[2729.56s] English:** Recover from something, so you have to go back much further.  
**Translation:** 

**[2731.44s] English:** So, you have the stressful period where it's, like, flat.  
**Translation:** 

**[2733.32s] English:** Or it might start going up, and you're like, "What do I do?  
**Translation:** 

**[2735.42s] English:** Whereas there are also loss spikes that are, it looks good.  
**Translation:** 

**[2737.66s] English:** And then there's one spiky data point.  
**Translation:** Vocabulary: spiky: 有尖刺的

**[2739.52s] English:** And what you can do is just skip those.  
**Translation:** 

**[2741.12s] English:** You see that there's a spike; you're like, "Okay,  
**Translation:** Vocabulary: spike: 突增

**[2743.20s] English:** I can ignore this data; don't update the model.  
**Translation:** 

**[2745.20s] English:** And do the next one, and it will recover quickly.  
**Translation:** 

**[2747.28s] English:** But these, like,  
**Translation:** 

**[2748.60s] English:** Trickier implementations, as you get more.  
**Translation:** Vocabulary: implementations: 实施方案; trickier: 更棘手的

**[2751.22s] English:** Complex in your architecture.  
**Translation:** 

**[2752.78s] English:** And you scale up to more GPUs.  
**Translation:** 

**[2754.90s] English:** You have more potential for your  
**Translation:** 

**[2757.00s] English:** Loss blowing up. So it's like, there's...  
**Translation:** 

**[2759.18s] English:** And there's a...  
**Translation:** 

**[2760.00s] English:** The whole idea of grokking also comes in, right? It's like, just because it slowed down from improving and lost doesn't mean it's not learning, because all of a sudden it could be like this, and it could just spike down and loss again, because it learned—truly learned something, right? And it took some time for it to learn that. It's not like a gradual process, right? And that's what humans are like; that's what models are like. So it's really a stressful task, as you mentioned.  
**Translation:** Vocabulary: gradual: 逐渐的; grokking: 理解透彻

**[2781.10s] English:** And the whole time, the dollar count is going up.  
**Translation:** 

**[2784.02s] English:** Every company has failed runs. You need failed runs to push the envelope on your infrastructure. So a lot of news cycles are made of X company had Y failed run. Every company that's trying to push the frontier of AI has these. So yes, it's noteworthy because it's a lot of money and it can be a week-to-month setback, but it is part of the process.  
**Translation:** Vocabulary: frontier: 技术边界; noteworthy: 值得留意; setback: 挫折

**[2805.02s] English:** But how do you get to a place where, if you're deep in the search, holy shit, there's a successful combination of hyperparameters?  
**Translation:** 

**[2812.48s] English:** A lot of small, failed runs.  
**Translation:** Vocabulary: hyperparameters: 超参数

**[2814.48s] English:** So rapid iteration through failed runs.  
**Translation:** 

**[2819.10s] English:** And successful ones.  
**Translation:** Vocabulary: iteration: 循环迭代

**[2820.74s] English:** And then you build a sum of intuition like this: this mixture of expert work, and then this implementation of MLA work.  
**Translation:** 

**[2828.72s] English:** Key hyperparameters, such as learning rate and regularization, and other related settings, are found through experimentation to work best for your specific code base.  
**Translation:** Vocabulary: experimentation: 实验; implementation: 实现; intuition: 直觉; mixture: 混合

**[2837.36s] English:** Talking to people at Frontier Labs, there's a story that you can tell where training language models is kind of a journey.  
**Translation:** 

**[2844.02s] English:** That you need to follow.  
**Translation:** 

**[2844.90s] English:** So, you need to unlock the ability to train a certain type of model or a certain scale.  
**Translation:** 

**[2849.64s] English:** And then, your codebase and your internal know-how of which hyperparameters work for it is kind of known.  
**Translation:** Vocabulary: codebase: 代码库; unlock: 解锁

**[2853.94s] English:** And you look at the deep-seek papers and models; they've scaled up, added complexity, and it's just continuing to build the capabilities they have.  
**Translation:** 

**[2862.20s] English:** There's the concept of a YOLO run.  
**Translation:** Vocabulary: capabilities: 能力; complexity: 复杂性

**[2864.76s] English:** So, YOLO: you only live once.  
**Translation:** 

**[2867.06s] English:** And what it is, is like, you know, there's all this experimentation you do at the small scale, right?  
**Translation:** 

**[2872.90s] English:** Research ablations.  
**Translation:** 

**[2874.02s] English:** Right?  
**Translation:** Vocabulary: ablations: 切除试验

**[2874.16s] English:** Like, you have your Jupyter notebook where you're experimenting with MLA on, like, three GPUs or whatever.  
**Translation:** 

**[2878.96s] English:** And you're doing all this.  
**Translation:** Vocabulary: experimenting: 实验; jupyter: 笔记本

**[2880.00s] English:** These different things, like, hey, do I do four expert, four active experts, 128 experts? Do I arrange?  
**Translation:** 

**[2885.36s] English:** The experts test all these different model architectures, you know, in this way.  
**Translation:** 

**[2889.60s] English:** Very small-scale, right? A couple of researchers, a few GPUs, tens of GPUs, hundreds of GPUs—whatever it is.  
**Translation:** 

**[2894.94s] English:** And then all of a sudden, you're like, "Okay, guys, no more fucking around, right? Uh, no more.  
**Translation:** 

**[2899.22s] English:** Screwing around, everyone! Let's take all the resources we have and pick what we think will work.  
**Translation:** 

**[2904.72s] English:** Just go for it, right? YOLO, and this is where that sort of stress comes in: "Is like, well, I know it.  
**Translation:** Vocabulary: screwing: 胡闹

**[2909.70s] English:** Works here, but some things that work here don't work there, and some things that work here don't.  
**Translation:** 

**[2914.12s] English:** Work down here, right? In terms of scale, it's really truly a YOLO run, and...  
**Translation:** 

**[2920.22s] English:** Sort of like, there's this kind of discussion where certain researchers just have this.  
**Translation:** 

**[2924.44s] English:** Methodical nature, like they can find the entire search space and figure out all the ablations.  
**Translation:** 

**[2928.34s] English:** Of different research, and really see what is best; there are certain researchers who just kind of  
**Translation:** 

**[2932.86s] English:** Like, you know, you have that innate gut instinct, like, "This is the YOLO run," like you know, looking...  
**Translation:** Vocabulary: innate: 天生的; instinct: 直觉

**[2938.10s] English:** At the data, this is it.  
**Translation:** 

**[2939.70s] English:** This is why you want to work in post-training, because the GPU cost for training is lower, so  
**Translation:** 

**[2943.76s] English:** You can make a higher percentage of your training runs YOLO runs, yeah. For now, for now, for now.  
**Translation:** 

**[2949.04s] English:** So, some of this is fundamentally luck. Still, luck is a mix of skill, right? In many cases, yeah. I mean, it looks  
**Translation:** Vocabulary: fundamentally: 本质上

**[2957.52s] English:** Lucky, right? When you're at the hill to climb, if you're in one of these labs, you have an evaluation.  
**Translation:** 

**[2962.72s] English:** You're not crushing; there's a repeated playbook of how you improve things, and there are localized versions of it.  
**Translation:** Vocabulary: evaluation: 评估; playbook: 操作手册

**[2967.34s] English:** Improvements which might be data improvements, and these add up to the data improvements and...  
**Translation:** 

**[2969.70s] English:** These add up into the whole model, just being much better, and when you zoom in really close, it can be  
**Translation:** 

**[2973.88s] English:** Really obvious that this model is just really bad at this thing, and we can fix it. You just add  
**Translation:** 

**[2978.94s] English:** These ups and downs feel like luck, but on the ground, especially with these new reasoning models,  
**Translation:** 

**[2984.08s] English:** We're talking; it's just so many ways that we can poke around, and normally it's that some of  
**Translation:** 

**[2990.06s] English:** They give big improvements, the search space is nearly infinite, right, and yet the amount of  
**Translation:** Vocabulary: infinite: 无穷的

**[2994.18s] English:** Compute and time you have is very low, and you're going to have to hit the release schedule.  
**Translation:** 

**[2999.70s] English:** You have  
**Translation:** Vocabulary: compute: 计算

**[3000.00s] English:** Have to not get blown past by everyone, otherwise, you know, what happened with DeepSeek, you know.  
**Translation:** 

**[3005.18s] English:** Crushing Meta and Mistral, and Coherent — all these guys; they moved too slow, right? They maybe...  
**Translation:** Vocabulary: coherent: 条理清晰; mistral: 软件名

**[3009.66s] English:** Were too methodical. I don't know; they didn't hit the YOLO run, whatever the reason was, maybe they...  
**Translation:** 

**[3013.36s] English:** Weren't as skilled, uh, whatever — you know, you can call it luck if you want, but at the end of  
**Translation:** Vocabulary: skilled: 熟练的

**[3017.38s] English:** The day it's skills so far, 2025 is the year of the YOLO run. It seems like all the labs are going in.  
**Translation:** 

**[3024.74s] English:** I think it's even more impressive what I did in 2022, right at the time when no one believed in it.  
**Translation:** 

**[3031.18s] English:** Mixture of experts models, right? At Google, who had all the researchers. I had such.  
**Translation:** 

**[3036.64s] English:** Little compute, and they devoted all of their compute for many months—right, all of it, 100%.  
**Translation:** Vocabulary: devoted: 专注; mixture: 混合

**[3041.92s] English:** For many months, GPT-4 was developed with a brand new architecture, with no belief that it would work.  
**Translation:** 

**[3048.32s] English:** Spend a couple hundred million dollars, which is all of the money I have on this model, right?  
**Translation:** 

**[3052.90s] English:** Is truly YOLO? Yeah, right.  
**Translation:** 

**[3054.74s] English:** Now, now you know people are like all these training run failures that are in the media, right?  
**Translation:** 

**[3059.92s] English:** It's like, okay, great, but actually, a lot—a huge chunk—of my GPS are doing inference, I still...  
**Translation:** 

**[3064.44s] English:** Have a bunch doing research constantly, and yes, my biggest cluster is training, but like on this.  
**Translation:** Vocabulary: cluster: 聚类; inference: 推断

**[3069.20s] English:** YOLO run, but like that YOLO run is much less risky than what I did in 2022 or  
**Translation:** 

**[3075.12s] English:** Maybe what DeepSeek did now, or you know, sort of like hey, we're just gonna throw everything at it.  
**Translation:** 

**[3079.22s] English:** It's the big winners throughout human history who are willing to do YOLO at some point.  
**Translation:** 

**[3084.72s] English:** Okay, uh, what do we understand about the hardware it's been trained on? DeepSeek is very  
**Translation:** 

**[3092.44s] English:** Interesting; at least a second to take us to zoom out on who they are, first of all, right?  
**Translation:** 

**[3095.68s] English:** High Flyer is a hedge fund that has historically done quantitative trading in China as well as  
**Translation:** Vocabulary: historically: 历史上; quantitative: 定量的

**[3101.68s] English:** Elsewhere, and they have always had a significant number of GPUs. Right in the past, a lot of these.  
**Translation:** 

**[3106.40s] English:** High-frequency trading algorithmic quant traders used FPGAs, but it shifted to GPUs definitely.  
**Translation:** Vocabulary: algorithmic: 算法; quant: 量化; shifted: 转移; traders: 交易者

**[3112.12s] English:** And there's both right, but GPUs, especially, and  
**Translation:** 

**[3114.72s] English:** Deep & High Flyer, which is the hedge fund that owns Deep Seek.  
**Translation:** 

**[3117.34s] English:** And everyone who works for DeepSeek is part of High Fly.  
**Translation:** 

**[3120.00s] English:** To some extent, right? Same parent company, same owner, same CEO. They had all these resources.  
**Translation:** 

**[3126.46s] English:** And infrastructure for trading. And then, they devoted a humongous portion of it to training.  
**Translation:** 

**[3132.74s] English:** Models, both language models and otherwise, right? Because these techniques were heavily AI-driven.  
**Translation:** Vocabulary: devoted: 投入; humongous: 巨大

**[3138.74s] English:** Influenced. More recently, people have realized: "Hey, trading with..." Even when you go back to  
**Translation:** 

**[3146.92s] English:** Renaissance and all these quantitative firms, natural language processing is the key to.  
**Translation:** Vocabulary: renaissance: 文艺复兴

**[3151.50s] English:** Trading really fast, right? Understanding a press release and making the right trade, right?  
**Translation:** 

**[3156.16s] English:** And so, DeepSeek has always been really good at this. And even as far back as 2021,  
**Translation:** 

**[3161.20s] English:** They have press releases and papers saying, like, "Hey, we're the first company in China with an  
**Translation:** 

**[3166.42s] English:** A100 cluster, this large; those 10,000 A100 GPUs, right? This was in 2021. Now, this wasn't all for  
**Translation:** Vocabulary: cluster: 计算集群

**[3172.68s] English:** Training large language models. This was mostly for training models for  
**Translation:** 

**[3176.84s] English:** Their quantitative aspects, their quantitative trading, as well as a lot of that was natural.  
**Translation:** Vocabulary: quantitative: 量化的

**[3181.10s] English:** Language processing, to be clear, right? And so this is the sort of history, right?  
**Translation:** 

**[3184.98s] English:** So, a verifiable fact is that in 2021, they built the largest cluster—at least they claim it was.  
**Translation:** Vocabulary: verifiable: 可验证的

**[3189.82s] English:** The largest cluster in China has 10,000 GPUs. Before expert controls started.  
**Translation:** 

**[3194.34s] English:** Yeah.  
**Translation:** 

**[3194.84s] English:** It's like they've had a huge cluster before any conversation about expert controls.  
**Translation:** 

**[3198.22s] English:** So then you step it forward to, like, what have they done over the last four years since then?  
**Translation:** 

**[3202.52s] English:** Right? Obviously, they've continued to operate the hedge fund and are probably making tons of money.  
**Translation:** 

**[3206.54s] English:** Right? And the other thing is that they've leaned more and more and more into AI. The CEO,  
**Translation:** Vocabulary: leaned: 倾向

**[3211.56s] English:** Liang Qingfeng, Liang,...  
**Translation:** 

**[3213.48s] English:** You're not putting me in a spot on this. We discussed this before.  
**Translation:** Vocabulary: qingfeng: 清风

**[3216.22s] English:** Liang Qingfeng, right? The CEO owns maybe a little bit more than half the company.  
**Translation:** 

**[3221.84s] English:** Allegedly, right? He's kind of like Elon Musk, where he's just really into it.  
**Translation:** 

**[3227.92s] English:** Involved in everything, right? And so, over that time period, he's gotten really in-depth into AI.  
**Translation:** 

**[3234.00s] English:** He actually has a bit of a, like,...  
**Translation:** 

**[3236.54s] English:** I see some of the statements; a bit of an IAC vibe, almost, right?  
**Translation:** 

**[3239.64s] English:** Total...  
**Translation:** 

**[3240.00s] English:** AGI vibes. They're like, "We need to do this. We need to make a new ecosystem of open AI." We need  
**Translation:** 

**[3246.88s] English:** China is set to lead in this type of ecosystem, because historically, Western countries have led on.  
**Translation:** Vocabulary: vibes: 感觉

**[3251.80s] English:** Software ecosystems. And he straight up acknowledges that in order to do this, we need to do  
**Translation:** 

**[3257.92s] English:** Something different. DeepSeek is his way of doing this. Some of the translated interviews with him:  
**Translation:** Vocabulary: ecosystems: 生态系统

**[3262.82s] English:** Are they fantastic? So, has he done any interviews?  
**Translation:** 

**[3264.36s] English:** Yeah.  
**Translation:** 

**[3264.76s] English:** You think he would do a Western-style interview, or is there any control on the channel?  
**Translation:** 

**[3268.26s] English:** Hasn't been one yet, but I would try it.  
**Translation:** 

**[3271.52s] English:** I just got a Chinese translator, so it was great! This is all push; so fascinating!  
**Translation:** 

**[3277.42s] English:** Engineer, pushing full-on into AI, leveraging the success from high-frequency trading.  
**Translation:** Vocabulary: leveraging: 利用; translator: 翻译机

**[3284.10s] English:** Very direct quotes: We will not switch to closed source when asked about this stuff.  
**Translation:** 

**[3289.56s] English:** Very long-term, I'm motivated by how the ecosystem of AI should work. And I think from a Chinese perspective,...  
**Translation:** Vocabulary: motivated: 驱使; quotes: 引语

**[3298.08s] English:** Perspective...  
**Translation:** 

**[3298.26s] English:** He wants a Chinese company to build this vision.  
**Translation:** 

**[3303.08s] English:** And so, this is sort of like the "quote-unquote" visionary behind the company, right? This hedge  
**Translation:** 

**[3307.38s] English:** Fund still exists, right? This quantitative firm. And so, DeepSeek is the sort of...  
**Translation:** Vocabulary: quantitative: 量化; visionary: visionary

**[3313.14s] English:** Slowly, he got fully immersed in the view of AI—everything about it, right? But at some point,  
**Translation:** 

**[3318.44s] English:** It slowly maneuvered, and he made DeepSeek. And DeepSeek has done multiple models since then.  
**Translation:** Vocabulary: immersed: 沉浸; maneuvered: 操控

**[3323.20s] English:** They've acquired more and more GPUs. They share infrastructure with the fund.  
**Translation:** 

**[3327.20s] English:** Right?  
**Translation:** 

**[3328.26s] English:** And so, there is no exact number of public GPU resources that they have, but besides this 10,000.  
**Translation:** 

**[3335.40s] English:** GPUs that they bought in 2021, right? And they were fantastically profitable, right? And then,...  
**Translation:** Vocabulary: fantastically: 极其; profitable: 盈利的

**[3340.42s] English:** This paper claims they did only 2,000 H800 GPUs, which are a restricted GPU that was previously.  
**Translation:** 

**[3346.50s] English:** Allowed in China, but no longer allowed. And there's a new version, but it's basically NVIDIA's.  
**Translation:** 

**[3350.58s] English:** H100 for China, right? And there are some restrictions on it, specifically around the  
**Translation:** 

**[3355.04s] English:** Communication speeds, such as interconnect speed.  
**Translation:** Vocabulary: interconnect: 互联速度

**[3358.24s] English:** Right? Which is why they had to do this crazy.  
**Translation:** 

**[3360.00s] English:** SM scheduling stuff. So, going back to that, this is obviously not true in terms of their total GPU.  
**Translation:** Vocabulary: scheduling: 排程

**[3367.82s] English:** Count. There are obvious available GPUs, but for this training run, you think 2000 is the correct.  
**Translation:** 

**[3373.30s] English:** Number or no? So, this is where it takes a significant amount of zoning in. What do you?  
**Translation:** 

**[3380.40s] English:** Do you call your training run? Do you count all of the research and ablations that you ran, picking all?  
**Translation:** 

**[3386.02s] English:** This stuff? Because, yes, you can do a YOLO run, but at some level, you have to do the test at the  
**Translation:** Vocabulary: ablations: 删减试验

**[3389.88s] English:** Small-scale. And then you have to do some tests at medium scale before you go to a large scale.  
**Translation:** 

**[3393.78s] English:** Accepted practice is that for any given model that is a notable advancement, you're going to  
**Translation:** Vocabulary: advancement: 进步

**[3398.56s] English:** Do two to four times the compute of the full training run in experiments alone. So, a lot of this compute.  
**Translation:** 

**[3404.28s] English:** That's being scaled up is probably used in large part at this time for research. Yeah, and research.  
**Translation:** Vocabulary: compute: 计算; experiments: 实验

**[3409.74s] English:** Begets the new ideas that let you gain huge efficiency. Research gets you O(1). Research.  
**Translation:** 

**[3415.30s] English:** Gets you a break.  
**Translation:** Vocabulary: begets: 产生

**[3416.02s] English:** So, some of the pricing strategies that we'll discuss have the research baked into the price.  
**Translation:** 

**[3422.66s] English:** So, the numbers that DeepSeek specifically said publicly are just the 10,000 GPUs in 2021.  
**Translation:** 

**[3427.58s] English:** And then, 2000 GPUs for only the pre-training for V3. They did not discuss cost for R1. They did not  
**Translation:** 

**[3434.68s] English:** Discuss the costs for all other RL models, right, for the instruction model that they made, right? They only  
**Translation:** 

**[3440.24s] English:** Discussed the pre-training for the base model, and they did not discuss anything on research and  
**Translation:** 

**[3444.42s] English:** Ablations. And they do not discuss cost on R1. And they do not discuss cost on R2. And they do not...  
**Translation:** 

**[3445.30s] English:** Talk about any of the resources that are shared, such as, hey, the fund is using all these GPUs.  
**Translation:** 

**[3450.60s] English:** Right? And we know that they're very profitable, and that 10,000 GPUs were sold in 2021. So some of the  
**Translation:** Vocabulary: profitable: 有利可图的

**[3458.88s] English:** Research that we've found is that we actually believe they have closer to 50,000 GPUs.  
**Translation:** 

**[3463.68s] English:** We, as semi-analysis experts, should say that you're sort of one of the world's experts in figuring out  
**Translation:** 

**[3469.68s] English:** What everybody is doing in terms of the semiconductor, in terms of cluster build-outs, in terms of  
**Translation:** 

**[3473.90s] English:** Like, who is doing what?  
**Translation:** Vocabulary: cluster: 计算集群; semiconductor: 半导体

**[3475.32s] English:** In terms of training runs. So, yeah. That's the one. Okay, go ahead.  
**Translation:** 

**[3479.56s] English:** Yeah, sorry.  
**Translation:** 

**[3480.00s] English:** We believe they actually have something closer to 50,000 GPUs right now. This is split,  
**Translation:** 

**[3484.92s] English:** Across many tasks, right? Again, the fund's um research and ablations suggest how much would OpenAI  
**Translation:** Vocabulary: ablations: 削减试验

**[3490.72s] English:** Or, Anthropic had I think the clearest example we have, because Meta is also open, they talk about  
**Translation:** 

**[3495.86s] English:** Like an order of 60K to 100K H100 equivalent GPUs in their training clusters, right? So, like, LLAMA.  
**Translation:** Vocabulary: clusters: 训练集群

**[3502.44s] English:** Three, they said they trained on 16,000 H100s, right? But the company of Meta last year publicly...  
**Translation:** 

**[3507.72s] English:** Disclosed they bought like 400,000 GPUs, yeah? Right? So, of course, a tiny percentage.  
**Translation:** Vocabulary: disclosed: 公布

**[3512.58s] English:** The training again; like, most of it is about serving me the best Instagram reels, right? Um,...  
**Translation:** 

**[3516.88s] English:** Right; I mean, we could get into a cost of, like, what is the cost of ownership for a 2,000 GPU cluster?  
**Translation:** Vocabulary: reels: 短视频

**[3522.42s] English:** 10,000—like there are just different sizes of companies that can afford these things, and deep...  
**Translation:** 

**[3526.98s] English:** The seek is reasonably big, in terms of their compute allocation, compared to others; it's one of the top few in the world.  
**Translation:** Vocabulary: allocation: 分配; compute: 计算; reasonably: 相当

**[3535.32s] English:** Not open AI, Anthropic, etc., but they have a lot of  
**Translation:** 

**[3537.72s] English:** Can you give a general overview, zoom out a bit, and also talk about the Hopper architecture?  
**Translation:** Vocabulary: hopper: 投料斗

**[3541.86s] English:** NVIDIA Hopper GPU architecture and the difference between H100 and H800, as you mentioned, like:  
**Translation:** 

**[3548.86s] English:** Interconnects, yeah. So, there's you know, Ampere was the A100 and then H100 Hopper, right? People.  
**Translation:** Vocabulary: ampere: 安培; interconnects: 互联

**[3553.76s] English:** Use them synonymously in the U.S., because really, there's just H100, and now there's H200, right?  
**Translation:** 

**[3558.70s] English:** Same thing; uh, mostly in China, they've had two different salvoes of exports.  
**Translation:** Vocabulary: exports: 出口; salvoes: 批次; synonymously: 同义

**[3563.72s] English:** Restrictions were so initial that the U.S. government limited it on a two-factor scale.  
**Translation:** 

**[3567.72s] English:** Right, which is chip interconnect versus FLOPS. So, any chip that had interconnects above a  
**Translation:** Vocabulary: interconnect: 芯片互联

**[3573.14s] English:** Certain level, and flops above a certain floating-point operations above a certain level were  
**Translation:** 

**[3577.68s] English:** Restricted, uh, later the government realized that this was a flaw in the restriction and they cut  
**Translation:** Vocabulary: flops: 失败; restriction: 限制

**[3583.02s] English:** It's all about just floating-point operations, and so the H800 had high flops but low communication.  
**Translation:** 

**[3590.86s] English:** Exactly, so the H800 had the same performance as the H100 on FLOPS, right, but it didn't have it just.  
**Translation:** 

**[3597.72s] English:** The interconnect bandwidth cut, DeepSeek knew how.  
**Translation:** 

**[3600.00s] English:** To utilize this, you know, hey, even though we're cut back on the interconnect, we can still do all this.  
**Translation:** Vocabulary: bandwidth: 带宽; utilize: 利用

**[3604.92s] English:** Fancy stuff to figure out how to use the GPU fully, anyway, and so that was back in October.  
**Translation:** 

**[3611.40s] English:** 2022, but uh, later in 2023, by the end of 2023, implemented in 2024: the U.S. government banned the H-800, right?  
**Translation:** Vocabulary: implemented: 付诸实施

**[3619.62s] English:** And so, by the way, this H800 cluster with these 2000 GPUs was not even purchased in 2024; it's  
**Translation:** 

**[3624.92s] English:** Purchased in late 2023, um, and they're just getting the model out now, right, because it takes a lot of  
**Translation:** Vocabulary: cluster: 计算集群

**[3629.82s] English:** Research, etc. Um, H800 was banned, and now there's a new chip called the H20. Uh, the H20 is uh cut back.  
**Translation:** 

**[3636.96s] English:** On only flops, but the interconnect bandwidth is the same, and in fact, in some ways, it's better than.  
**Translation:** 

**[3641.90s] English:** The H100, because it has better memory bandwidth and memory capacity, so there are you know, Nvidia.  
**Translation:** 

**[3646.66s] English:** Is working within the constraints of what the government says, and then gets the best results possible.  
**Translation:** Vocabulary: constraints: 限制条件

**[3650.98s] English:** Possible GPU for China, can we take this actual tangent and we'll return back to the hardware.  
**Translation:** 

**[3655.32s] English:** Is the philosophy, the motivation?  
**Translation:** 

**[3658.54s] English:** The case  
**Translation:** 

**[3659.82s] English:** For expert controls, what is it? Uh, Daria just published a blog post about expert controls.  
**Translation:** 

**[3665.00s] English:** The case he makes is that if AI becomes super powerful, and he says by 2026 we'll have AGI, or  
**Translation:** 

**[3672.60s] English:** Super powerful AI, and that's going to give a significant advantage to whoever builds it.  
**Translation:** 

**[3677.02s] English:** Significant military advantage, and so, because the United States is a democracy, and as he says, China...  
**Translation:** 

**[3684.84s] English:** Is it authoritarian or has authoritarian elements?  
**Translation:** Vocabulary: authoritarian: 独裁主义的

**[3688.92s] English:** You want to have a super powerful AI, and that's going to give a significant military advantage.  
**Translation:** 

**[3689.80s] English:** You want a unipolar world where the super-powerful military, because of AI, is one that's  
**Translation:** Vocabulary: unipolar: 单极世界

**[3696.52s] English:** Democracy: It's a much more complicated world geopolitically when you have two superpowers.  
**Translation:** 

**[3702.42s] English:** With super-powerful AI, and one is authoritarian, so that's the case he makes. So, we want to  
**Translation:** Vocabulary: geopolitically: 地缘政治上; superpowers: 超级大国

**[3708.78s] English:** Uh, the United States wants to use export controls to slow down and make sure that China can't do  
**Translation:** 

**[3716.16s] English:** These gigantic training runs.  
**Translation:** Vocabulary: export: 出口; gigantic: 巨大的

**[3719.80s] English:** That they know how to do.  
**Translation:** 

**[3720.00s] English:** Be presumably required to build AGI. This is very abstract. I think this can be the goal for how some.  
**Translation:** Vocabulary: presumably: 大概

**[3726.28s] English:** So,  
**Translation:** 

**[3726.80s] English:** People describe export controls as this super-powerful AI, and you touched on the training run.  
**Translation:** 

**[3730.98s] English:** You.  
**Translation:** 

**[3733.04s] English:** Idea: There aren't many worlds where China cannot train AI models. Export controls are kneecapping.  
**Translation:** 

**[3741.66s] English:** The amount of compute, or the density of compute, that China can have. And if you think about the  
**Translation:** 

**[3745.06s] English:** You.  
**Translation:** Vocabulary: compute: 计算; density: 密度

**[3746.82s] English:** You.  
**Translation:** 

**[3747.90s] English:** AI ecosystem, right now, as all of these AI companies' revenue numbers are up and to the  
**Translation:** 

**[3748.92s] English:** You.  
**Translation:** 

**[3749.00s] English:** You.  
**Translation:** 

**[3749.42s] English:** You.  
**Translation:** 

**[3749.62s] English:** You.  
**Translation:** 

**[3749.68s] English:** You.  
**Translation:** 

**[3749.70s] English:** You.  
**Translation:** 

**[3749.74s] English:** You.  
**Translation:** 

**[3749.76s] English:** You.  
**Translation:** 

**[3752.34s] English:** Right. Their AI usage is just continuing to grow. More GPUs are going to be used for inference, and a large part of  
**Translation:** 

**[3757.84s] English:** Export controls, if they work, is just that the amount of AI that can be run in China is going  
**Translation:** Vocabulary: inference: 推断

**[3764.38s] English:** To be much lower. So, on the training side, DeepSeek v3 is a great example, which you have a very  
**Translation:** 

**[3768.88s] English:** A focused team that can still get to the frontier of AI. On this, 2,000 GPUs is not that hard to get.  
**Translation:** Vocabulary: frontier: 最前沿

**[3774.64s] English:** All considering in the world, they're still going to  
**Translation:** 

**[3777.84s] English:** Have to be able to get to the frontier of AI. They're still going to have to be able to get to.  
**Translation:** 

**[3777.88s] English:** The frontier of AI. They're still going to have to be able to get to the frontier of AI. They're still.  
**Translation:** 

**[3777.90s] English:** Going to have those GPUs. They're still going to be able to train models. But if there's going to be  
**Translation:** 

**[3780.82s] English:** A huge market for AI, if you have strong export controls and you want to have 100,000 GPUs, just  
**Translation:** 

**[3785.46s] English:** Serving the equivalent of Chat GPT clusters, with good export controls, it also just makes it so  
**Translation:** Vocabulary: clusters: 计算集群

**[3790.12s] English:** That AI can be used much less. And I think that is a much easier goal to achieve than trying to.  
**Translation:** 

**[3798.48s] English:** Debate on what AGI is. And if you have these extremely intelligent, autonomous AI systems and data,...  
**Translation:** Vocabulary: autonomous: 自主的

**[3803.92s] English:** Centers: Those are the things that could be running in these GPU clusters.  
**Translation:** 

**[3807.68s] English:** To some extent, training a model does effectively nothing, right?  
**Translation:** 

**[3813.08s] English:** The thing that Dario is sort of speaking to is the implementation of that model.  
**Translation:** 

**[3820.26s] English:** Once trained, it can then create huge economic growth and huge increases in military capabilities.  
**Translation:** Vocabulary: capabilities: 能力; implementation: 实施

**[3826.32s] English:** Huge increases in productivity, betterment of lives — whatever you want to direct.  
**Translation:** 

**[3831.38s] English:** Super powerful AI: you can't do that. But that requires significant amounts of compute, right?  
**Translation:** Vocabulary: compute: 计算能力

**[3836.86s] English:** And so, the U.S.,  
**Translation:** 

**[3837.62s] English:** The government has effectively said,...  
**Translation:** 

**[3840.00s] English:** And forever, right?  
**Translation:** 

**[3841.44s] English:** Like, training will always be a portion of the total compute.  
**Translation:** 

**[3845.02s] English:** You know, we mentioned Meta's 400,000 GPUs, only 16,000 were used to make LAMA, right?  
**Translation:** 

**[3849.10s] English:** So, the percentage that Meta is dedicating to inference—now, this might be for recommendations.  
**Translation:** 

**[3853.68s] English:** Systems that are trying to hack our minds into spending more time and watching more ads,  
**Translation:** 

**[3857.38s] English:** Or, if it's for a super-powerful AI that's doing productive things, it doesn't matter.  
**Translation:** 

**[3862.06s] English:** About the exact use that our economic system decides.  
**Translation:** 

**[3865.14s] English:** It's what can be delivered in whatever way we want.  
**Translation:** 

**[3868.26s] English:** Whereas, with China, right?  
**Translation:** 

**[3870.24s] English:** You know, you're an expert on restrictions; great.  
**Translation:** 

**[3872.60s] English:** You're never going to be able to cut everything off, right?  
**Translation:** 

**[3874.84s] English:** And that's, I think, quite well understood by the U.S. government.  
**Translation:** 

**[3878.52s] English:** You can't cut everything off, you know; they'll make their own chips, and they're trying to.  
**Translation:** 

**[3882.86s] English:** Make their own chips.  
**Translation:** 

**[3883.44s] English:** They'll be worse than ours.  
**Translation:** 

**[3884.18s] English:** But, you know, this is the whole point: it's just to keep a gap, right?  
**Translation:** 

**[3887.24s] English:** And therefore, at some point, as the AI, you know, in a world where 2-3% economic growth,  
**Translation:** 

**[3891.76s] English:** This is really dumb, by the way, right?  
**Translation:** 

**[3893.44s] English:** To cut off, you know, high-tech products and not make money off of it.  
**Translation:** 

**[3896.64s] English:** But, in a world where super.  
**Translation:** 

**[3898.26s] English:** Powerful AI comes about and then starts creating significant changes in society, which is what  
**Translation:** 

**[3903.12s] English:** All the AI leaders and big tech companies believe that I think super-powerful AI is going  
**Translation:** 

**[3906.84s] English:** To change society massively.  
**Translation:** 

**[3908.52s] English:** And therefore, this compounding effect of the difference in compute is really important.  
**Translation:** Vocabulary: compounding: 累积效应; massively: 大规模地

**[3912.58s] English:** There's some sci-fi out there where AI is measured in the power of, like  
**Translation:** 

**[3917.92s] English:** How much power is delivered to compute, right?  
**Translation:** Vocabulary: compute: 计算能力

**[3919.58s] English:** Or how much is being spent, you know, that's sort of a way of thinking about what's the economic impact.  
**Translation:** 

**[3923.36s] English:** Output is just how much power you're directing toward that AI.  
**Translation:** 

**[3926.46s] English:** Should we talk about reasoning models with this?  
**Translation:** 

**[3928.26s] English:** As a way that this might be actionable, something that people can actually see.  
**Translation:** 

**[3932.02s] English:** So, the reasoning models that are coming out with R1 and O1 are designed to use more compute.  
**Translation:** 

**[3937.38s] English:** There are a lot of buzzwords in the AI community about this test-time, compute, and inference time.  
**Translation:** Vocabulary: buzzwords: 热门词汇; inference: 推理

**[3942.72s] English:** Compute, whatever.  
**Translation:** 

**[3944.22s] English:** But Dylan has good research on this.  
**Translation:** Vocabulary: dylan: Dylan

**[3946.02s] English:** You can get to the specific numbers on the ratio of when you train a model; you can look at things.  
**Translation:** 

**[3949.58s] English:** About the amount of compute used at training and the amount of compute used at inference.  
**Translation:** 

**[3953.22s] English:** These reasoning models are making inference much more important to doing complex tasks.  
**Translation:** 

**[3957.36s] English:** In the fall, in December,  
**Translation:** 

**[3960.00s] English:** Their OpenAI announced this O3 model. There's another thing in AI when things move fast, we get  
**Translation:** 

**[3964.40s] English:** Both announcements and releases are essentially blog posts where you pat yourself on the back.  
**Translation:** 

**[3968.46s] English:** The back, and you say you did things, and releases are out there in the models and in the papers.  
**Translation:** 

**[3972.24s] English:** Etc., so OpenAI has announced O3, and we can check if O3 Mini is out as of recording, potentially.  
**Translation:** 

**[3978.24s] English:** But that doesn't really change the point, which is that the breakthrough result was something.  
**Translation:** 

**[3982.96s] English:** Called ARC-Agi, which is the Abstract Reasoning Corpus task for artificial general intelligence.  
**Translation:** Vocabulary: corpus: 文本集

**[3988.48s] English:** Intelligence, um, François Chalet is the guy who's been referenced in an older paper—it's a multi-year-old paper—and it's a brilliant one.  
**Translation:** 

**[3994.98s] English:** Benchmark, and the number for OpenAI's O3 to solve this was that it used some sort of [number].  
**Translation:** Vocabulary: benchmark: 标准; referenced: 引用

**[4001.78s] English:** Samples in the API have something like "thinking effort" and the number of samples they used was a thousand.  
**Translation:** 

**[4006.84s] English:** Samples to solve this task, and it comes out to be around five to twenty dollars per question, which  
**Translation:** 

**[4013.50s] English:** You're putting in effectively a math puzzle, and then it takes orders of magnitude in dollars to answer one.  
**Translation:** 

**[4018.12s] English:** Question:  
**Translation:** 

**[4018.48s] English:** And this is a lot of compute if they're going to take off in the U.S.; OpenAI needs a ton of GPUs.  
**Translation:** 

**[4023.66s] English:** On inference, to capture this, they have this Open AI Chat GPT Pro subscription, which is two hundred dollars.  
**Translation:** 

**[4028.70s] English:** Dollars a month, which Sam said they're losing money on, which means that people are burning through money at that rate.  
**Translation:** 

**[4032.56s] English:** Lots of GPUs on inference, and I've signed up with it. I've played with it, but I don't think I'm a power user.  
**Translation:** Vocabulary: inference: 推理

**[4036.92s] English:** User: But I use it, and it's like that is the thing that a Chinese company with mediumly strong.  
**Translation:** 

**[4043.72s] English:** Expert controls: there will always be loopholes; might not be able to do it all, and if that  
**Translation:** Vocabulary: loopholes: 漏洞

**[4047.94s] English:** That's the thing: a Chinese company with moderately strong expertise will always  
**Translation:** 

**[4048.12s] English:** Be aware that there might not be enough information to do it all, and if that's the case, the main result for O3 might also be spectacular.  
**Translation:** Vocabulary: moderately: 中等程度地

**[4051.22s] English:** Coding performance, and if that feeds back into AI companies being able to experiment better, so  
**Translation:** 

**[4057.78s] English:** Presumably, the idea is that for an AGI, a much larger fraction of the compute would be used for this.  
**Translation:** Vocabulary: compute: 计算; presumably: 推测而言

**[4064.28s] English:** Test time: Compute for the reasoning for AGI, it goes into a room and thinks about how to.  
**Translation:** 

**[4068.96s] English:** Take over the world, and that you know, come back in 2.7 hours. This is what it's going to take: a lot.  
**Translation:** 

**[4076.12s] English:** Of computers, this is what people are like.  
**Translation:** 

**[4078.12s] English:** CEO or leaders of opening:  
**Translation:** 

**[4080.00s] English:** AI and Anthropic talk about autonomous AI models, which is that you give them a task and they  
**Translation:** 

**[4084.46s] English:** Work on it in the background. My personal definition of AGI is much simpler. I think.  
**Translation:** Vocabulary: autonomous: 自主的

**[4090.68s] English:** Language models are a form of AGI, and all this super powerful stuff is a next step—that's great!  
**Translation:** 

**[4095.52s] English:** If we get these tools, a language model has such immense value in so many domains that it's a  
**Translation:** Vocabulary: immense: 巨大

**[4099.86s] English:** General intelligence, to me. But this next step of agentic things, where they're independent and  
**Translation:** 

**[4104.90s] English:** They can do tasks that aren't in the training data, which is what the few-year outlook for these AI systems suggests.  
**Translation:** Vocabulary: agentic: 自主的; outlook: 前景

**[4111.02s] English:** Companies are driving for. I think the terminology here, that Dario uses, is "super-powerful AI." So I  
**Translation:** 

**[4118.16s] English:** Agree with you on the AGI. I think we already have something that's exceptionally impressive.  
**Translation:** Vocabulary: exceptionally: 特别地; terminology: 术语

**[4122.32s] English:** That Alan Turing would for sure say is AGI, but he's referring more to something "once in possession.  
**Translation:** 

**[4128.66s] English:** Of course, then you would have a significant military and geopolitical advantage over other nations.  
**Translation:** Vocabulary: geopolitical: 地缘政治的; turing: 图灵

**[4134.34s] English:** So, it's not...  
**Translation:** 

**[4134.90s] English:** It's not just like you can ask it how to cook an omelet.  
**Translation:** 

**[4138.38s] English:** And he has a much more positive view in his essay, "Machines of Love and Grace." I've read it.  
**Translation:** 

**[4143.10s] English:** I don't have enough background in physical sciences to gauge exactly how competent I am.  
**Translation:** Vocabulary: competent: 有能力的; gauge: 评估

**[4147.42s] English:** If AI can revolutionize biology, I'm safe saying that AI is going to accelerate the  
**Translation:** 

**[4154.32s] English:** Progress in any computational science. So, we're doing a depth-first search here.  
**Translation:** Vocabulary: accelerate: 加速; computational: 计算的; revolutionize: 革命性改变

**[4157.78s] English:** On topics, taking tangents of tangents. So, let's continue with depth-first search.  
**Translation:** 

**[4162.62s] English:** You said that you're both feeling the AGI. So, what's your timeline? Dario's 2026 for the super.  
**Translation:** Vocabulary: tangents: 旁枝话题

**[4173.22s] English:** Powerful AI that's basically agentic to a degree where it's a real security threat.  
**Translation:** 

**[4181.30s] English:** That level of AGI. What's your timeline?  
**Translation:** 

**[4184.70s] English:** I don't like to attribute specific abilities because predicting specific abilities and when  
**Translation:** 

**[4188.94s] English:** It is very hard. I think mostly if you're going to say that I'm feeling the AGI,  
**Translation:** Vocabulary: attribute: 归因

**[4192.78s] English:** Is that I expect continued, rapid, and surprising progress over the next few years.  
**Translation:** 

**[4197.08s] English:** So, something like R1 is less.  
**Translation:** 

**[4200.00s] English:** Surprising to me from DeepSeek, because I expect there to be new paradigms where substantial  
**Translation:** 

**[4204.26s] English:** Progress can be made, I think. DeepSeek R1 is so unsettling because we're kind of on this path with...  
**Translation:** Vocabulary: paradigms: 基本模式; unsettling: 令人不安

**[4209.44s] English:** With Chat GPT, it's like it's getting better, better, and better, and then we  
**Translation:** 

**[4212.60s] English:** Have a new direction for changing the models, and we took one step like this. We liked it.  
**Translation:** 

**[4216.92s] English:** A step up, so it looks like a really fast slope, and then we're going to just take more steps.  
**Translation:** 

**[4220.80s] English:** So, like, this is really unsettling when you have these big steps, and I expect that to keep happening.  
**Translation:** 

**[4225.76s] English:** I see. I've tried opening them, but they're not there yet. I've also tried using Claude on my computer, and they're still not available.  
**Translation:** 

**[4232.36s] English:** Understand the idea, but it's just so hard to predict what the breakthrough will make.  
**Translation:** 

**[4236.90s] English:** Something like that works, and I think it's more likely that we have breakthroughs that work.  
**Translation:** 

**[4241.24s] English:** Things that we don't know what they're going to do, so like everyone wants agents; Dario has very.  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[4245.44s] English:** An eloquent way of describing this, and I just think that it's like there's going to be more than that.  
**Translation:** 

**[4251.20s] English:** So, I could just expect these things to come, I'm gonna have to try to pin you down to a date.  
**Translation:** Vocabulary: eloquent: 口才好的

**[4255.74s] English:** On the AGI timeline, much like the nuclear weapon moment—so, the moment where it would have a significant impact on the geopolitical stage—  
**Translation:** 

**[4265.22s] English:** There's a real issue, you know, because we're talking about export controls.  
**Translation:** Vocabulary: export: 出口; geopolitical: 地缘政治的

**[4270.84s] English:** When do you think we should just even throw out a date? When do you think that would be, like, for me? It's  
**Translation:** 

**[4276.72s] English:** Probably after 2030, so I'm not as sure how to define that exactly because to me it kind of...  
**Translation:** 

**[4282.88s] English:** Of almost everything has already happened, right? You look at elections in India.  
**Translation:** 

**[4285.74s] English:** And Pakistanis get AI voice calls and think they're talking to the politician, right? The AI  
**Translation:** Vocabulary: pakistanis: 巴基斯坦人

**[4291.50s] English:** Diffusion rules, which were enacted in the last couple weeks of the Biden administration, look like  
**Translation:** 

**[4295.04s] English:** The Trump administration will keep and potentially even strengthen limits on cloud computing and GPU sales.  
**Translation:** Vocabulary: computing: 计算; diffusion: 扩散; enacted: 制定

**[4301.06s] English:** To countries that are not even related to China, it's like this is Portugal and all these kinds of things.  
**Translation:** 

**[4305.84s] English:** Normal companies in countries on the U.S. list, like Portugal, need approval.  
**Translation:** Vocabulary: portugal: 葡萄牙

**[4310.44s] English:** And, like, you know, like all these countries that are allies, right? Singapore, right? Like they  
**Translation:** 

**[4314.76s] English:** They freaking have.  
**Translation:** Vocabulary: allies: 盟友; freaking: 该死的

**[4315.74s] English:** 35 seconds, and we don't let them buy GPUs like this. Is this to me already too much?  
**Translation:** 

**[4320.00s] English:** Scale of, you know, just means that the U.S. military is really nervous about this.  
**Translation:** 

**[4326.16s] English:** New technology doesn't necessarily mean the technology is already there; so, they might just be working on it.  
**Translation:** 

**[4331.76s] English:** Cautious about this thing that they don't quite understand, but that's a really good point, sort of.  
**Translation:** 

**[4336.16s] English:** The swarm of semi-intelligent bots could be a weapon, doing a lot of social damage.  
**Translation:** 

**[4344.84s] English:** Engineering, I mean, there's tons of talk about you know, from the 2016 elections like Cambridge Analytica.  
**Translation:** 

**[4348.98s] English:** Analytica and all this stuff—Russian influence, I mean—every country in the world is pushing stuff.  
**Translation:** 

**[4353.86s] English:** On the Internet, and they have narratives they want, right? Like that's everything—technically.  
**Translation:** Vocabulary: narratives: 叙述; technically: 从技术上说

**[4357.86s] English:** Competent, whether it's Russia, China, U.S., Israel, etc.—right? You know, people are pushing viewpoints.  
**Translation:** 

**[4363.02s] English:** Onto the Internet en masse, and language models crash the cost of very intelligent-sounding  
**Translation:** Vocabulary: competent: 有能力的; viewpoints: 观点

**[4368.34s] English:** Language: There's some research that shows that the distribution is actually a limiting factor.  
**Translation:** 

**[4372.76s] English:** So, language models haven't yet made misinformation particularly problematic.  
**Translation:** Vocabulary: misinformation: 错误信息

**[4378.74s] English:** You.  
**Translation:** 

**[4378.98s] English:** Change the equation; there, the Internet is still ongoing. I think there's a blog titled "AI Snake Oil," and...  
**Translation:** Vocabulary: equation: 方程式

**[4383.88s] English:** Some of my friends at Princeton who write on this stuff, so there is research; it's like that.  
**Translation:** 

**[4387.32s] English:** A default that everyone assumes, and I would have thought the same thing, is that misinformation.  
**Translation:** 

**[4391.28s] English:** Doesn't get much worse with language models, I think, in terms of internet posts and things that people  
**Translation:** 

**[4396.86s] English:** Have been measuring it; it hasn't been an exponential increase or something extremely measurable, and  
**Translation:** Vocabulary: exponential: 指数的; measurable: 可测量的

**[4401.44s] English:** Things you're talking about, with like voice calls and stuff, could be in modalities that  
**Translation:** 

**[4405.90s] English:** Are harder to measure, so it's something that's too soon to tell, in terms of what I think.  
**Translation:** Vocabulary: modalities: 方式

**[4411.64s] English:** That's like political instability via the web is very much monitored by a lot of researchers.  
**Translation:** 

**[4418.32s] English:** To see what's happening, I think you're asking about the AGI thing; I might.  
**Translation:** 

**[4425.34s] English:** Ever made me give a year? I'm gonna be like, okay, I have an AI CEO saying this; they've been saying "two.  
**Translation:** 

**[4429.14s] English:** Years ago, for a while, I think that people like Dario, the CEO of Anthropic, had thought.  
**Translation:** 

**[4435.88s] English:** About this so deeply. I need to take their words seriously, but also,...  
**Translation:** 

**[4440.00s] English:** Also, understand that they have different incentives. So, I would be like, add a few.  
**Translation:** Vocabulary: incentives: 动机

**[4444.46s] English:** Years from that, which is how you get something similar to 2030 or a little after 2030.  
**Translation:** 

**[4448.46s] English:** I think, to some extent, we have capabilities that hit a certain point where any one person could say,  
**Translation:** Vocabulary: capabilities: 能力

**[4453.82s] English:** Oh, okay. If I can leverage those capabilities for X amount of time, is this AGI, right? Call it 27.  
**Translation:** 

**[4459.42s] English:** But then, the cost of actually operating that capability is so extreme that no one can.  
**Translation:** 

**[4466.62s] English:** Actually, deploying it at scale and mass could completely revolutionize the economy in a snap.  
**Translation:** 

**[4472.74s] English:** Of a finger. So, I don't think it will be like a snap of the finger moment. It's a physical constraint.  
**Translation:** Vocabulary: constraint: 物理限制; deploying: 部署; revolutionize: 彻底改变

**[4476.62s] English:** Rather, it'll be a capability here, but I can't deploy it everywhere, right?  
**Translation:** 

**[4481.30s] English:** And so, as a simple example going back to 2023, was when Bing with GPT-4 came out.  
**Translation:** Vocabulary: capability: 能力; deploy: 部署

**[4488.96s] English:** Everyone was freaking out about search, right? Perplexity came out. If you did the cost analysis,  
**Translation:** 

**[4493.16s] English:** Hey, implementing GPT-3 into every Google search, it was like, oh, okay,...  
**Translation:** Vocabulary: freaking: 恐慌; implementing: 实施; perplexity: 困惑

**[4496.50s] English:** This is a really good idea. But if you did the cost of implementing GPT-3 into every  
**Translation:** 

**[4496.60s] English:** Google Search: It was like, oh, okay, this is a really good idea. But if you did the cost analysis,  
**Translation:** 

**[4496.62s] English:** This is just like physically impossible to implement, right? And as we step forward,  
**Translation:** 

**[4500.56s] English:** Like going back to the test-time computation thing, right? You know, you ask ChatGPT a  
**Translation:** Vocabulary: computation: 计算; implement: 实施

**[4505.80s] English:** Question: It costs cents, right? For their most capable model of chat, right? To get a query back.  
**Translation:** 

**[4511.92s] English:** To solve an Arc AGI problem, though, it costs five to twenty dollars, right? And this is—a  
**Translation:** 

**[4518.52s] English:** It's only going up from there.  
**Translation:** 

**[4519.68s] English:** This is a thousand, 10,000 times the X-factor difference in cost to respond to a query versus do a task.  
**Translation:** 

**[4525.96s] English:** And the task:  
**Translation:** 

**[4526.60s] English:** The task of Arc AGI is not like it's simple, to some extent, you know, but it's  
**Translation:** 

**[4532.24s] English:** Also, like, what are the tasks that we want? Okay, AGI—quote unquote—what we have today can do arc.  
**Translation:** 

**[4536.88s] English:** AGI. Three years from now, it can do much more complicated problems, but the cost is going to...  
**Translation:** 

**[4541.26s] English:** It can be measured in thousands, and thousands, and hundreds of thousands of dollars of GPU time.  
**Translation:** 

**[4546.02s] English:** And there just won't be enough power, GPUs, or infrastructure to operate this, and therefore,...  
**Translation:** 

**[4550.10s] English:** Shift everything in the world on the snap of the finger. But at that moment, who gets to?  
**Translation:** 

**[4554.68s] English:** Control and point out the problem? And who gets to control and point out the problem?  
**Translation:** 

**[4556.58s] English:** Who gets to control and point the AGI at a task? And so, this was discussed in Dario.  
**Translation:** 

**[4560.00s] English:** Post that he's like, "Hey, China can effectively and more quickly than us point their AGI at  
**Translation:** 

**[4565.74s] English:** Military tasks, right? And they have been, in many ways, faster at adopting certain new technologies.  
**Translation:** 

**[4570.74s] English:** Into their military, right? Especially with regards to drones, right? The US may have a  
**Translation:** Vocabulary: drones: 无人机; regards: 涉及

**[4576.40s] English:** Long-standing, you know, large-air sort of you-know-what, like fighter jets and bombers. But  
**Translation:** 

**[4581.72s] English:** When it comes to asymmetric arms, such as drones, they've completely leaped ahead of the US and the West.  
**Translation:** Vocabulary: asymmetric: 不对称; bombers: 轰炸机; leaped: 超越

**[4587.90s] English:** And the fear that Dario is sort of pointing out there, I think, is that, yeah, great,  
**Translation:** 

**[4593.10s] English:** We'll have AGI in the commercial sector. The U.S. military won't be able to implement it super fast.  
**Translation:** Vocabulary: implement: 执行

**[4598.40s] English:** The Chinese military could, and they could direct all their resources to implementing it in the  
**Translation:** 

**[4602.30s] English:** Military, and therefore solving, you know, military logistics, or solving some other aspect of it,  
**Translation:** Vocabulary: implementing: 执行

**[4607.74s] English:** Disinformation for a targeted, certain set of people, so they can flip a country's politics or something.  
**Translation:** 

**[4612.62s] English:** Like that, that is actually catastrophic versus, you know, the U.S. just wants to, you know,  
**Translation:** Vocabulary: catastrophic: 灾难性的; disinformation: 虚假信息

**[4617.60s] English:** Because of the pandemic.  
**Translation:** 

**[4617.88s] English:** It will be more capitalistically allocated just toward whatever has the highest return on.  
**Translation:** Vocabulary: allocated: 分配; capitalistically: 资本地; pandemic: 大流行

**[4621.14s] English:** Income, which might be like building factories or whatever.  
**Translation:** 

**[4624.42s] English:** So, everything I've seen, people's intuition seems to fail when it comes to robotics. So, you have this kind of  
**Translation:** Vocabulary: intuition: 直觉; robotics: 机器人技术

**[4630.86s] English:** General optimism. I've seen this on self-driving cars. People think it's much easier a problem than.  
**Translation:** 

**[4635.76s] English:** It is similar to drones. Here, I understand it a little bit less, but I've just seen the  
**Translation:** Vocabulary: optimism: 积极乐观

**[4642.30s] English:** The reality of the war in Ukraine and the usage of drones on both sides. And it seems,  
**Translation:** 

**[4647.88s] English:** I guess that humans still far outperform any fully autonomous systems. AI is an assistant.  
**Translation:** Vocabulary: autonomous: 自主的

**[4656.64s] English:** But humans drive. FPV drones, where humans control most of it, just far, far, far outperform.  
**Translation:** 

**[4662.58s] English:** AI systems. So, I think it's not obvious to me that we're going to have swarms of autonomous robots.  
**Translation:** Vocabulary: drones: 无人驾驶飞行器; swarms: 群集

**[4668.46s] English:** Anytime soon in the military context. Maybe the fastest I can imagine is 2030, which is why I said.  
**Translation:** 

**[4675.66s] English:** 2030 for the super-powerful AI. I don't know. I don't know. I don't know. I don't know. I don't  
**Translation:** Vocabulary: anytime: 任何时间

**[4677.58s] English:** Know. I don't know. I don't know. I don't know. Whenever you have large-scale,  
**Translation:** 

**[4680.00s] English:** Swarms of robots doing military actions is when the world just starts to look different.  
**Translation:** 

**[4686.00s] English:** To me, so that's the thing I'm really worried about, but there could be a cyber war.  
**Translation:** 

**[4690.94s] English:** Cyber war-type technologies, that range from social engineering to actually just  
**Translation:** 

**[4696.54s] English:** Swarms of robots that find attack vectors in our code bases and shut down power grids—that kind of  
**Translation:** 

**[4703.28s] English:** Stuff, and it could be one of those things—like on any given weekend—or something, the power goes out.  
**Translation:** Vocabulary: vectors: 攻击路径

**[4709.80s] English:** Nobody knows why, and the world changes forever. Just power going out for two days in all of the...  
**Translation:** 

**[4716.58s] English:** United States that will lead to murder, to chaos, but going back to expert controls: do you see that?  
**Translation:** 

**[4725.88s] English:** As a useful way to control the balance of power geopolitically in the context of AI.  
**Translation:** 

**[4735.50s] English:** And I think, going back to my viewpoint, if you believe we're in this sort of  
**Translation:** Vocabulary: geopolitically: geopolitically; viewpoint: 观点

**[4739.80s] English:** Uh, it's been a stage of economic growth and change that we've been in for the last 20 years, and the export controls.  
**Translation:** 

**[4746.00s] English:** Are we absolutely guaranteeing that China will win in the long term? Right? If you don't believe AI is going  
**Translation:** Vocabulary: export: 出口; guaranteeing: 保证

**[4752.60s] English:** To make significant changes to society in the next 10 years or five-year period.  
**Translation:** 

**[4758.46s] English:** Timelines are sort of what more executives and such at AI companies, and even big tech companies, discuss.  
**Translation:** Vocabulary: executives: 高层管理人员; timelines: 时间线

**[4763.18s] English:** Believe, but even 10-year timelines — you know, it's reasonable, but once you get to "hey, these,  
**Translation:** 

**[4769.30s] English:** Timelines are going to be a big deal, and I think that's going to be a big deal, and I think that's.  
**Translation:** 

**[4769.78s] English:** Are they below that time period, then the only way to sort of create a sizable advantage or  
**Translation:** 

**[4778.32s] English:** Disadvantage for America versus China is if you constrain compute, because  
**Translation:** Vocabulary: compute: 计算; constrain: 限制; sizable: 可观的

**[4783.88s] English:** Talent is not really something that's constraining, right? China arguably has more talent, right? More...  
**Translation:** 

**[4789.66s] English:** Stem graduates more programmers, the U.S. can draw upon the world's people, which it does. There's tons.  
**Translation:** Vocabulary: arguably: 或许; constraining: 限制; programmers: 程序员

**[4794.76s] English:** Of course, you know that in the AI industry, so many of these AI teams are all people.  
**Translation:** 

**[4799.78s] English:** That are  
**Translation:** 

**[4800.00s] English:** A U.S. passport. Yeah, I mean, many of them are Chinese people who are moving to America.  
**Translation:** 

**[4806.12s] English:** Right? And that's great. That's exactly what we want, right? But that talent is just one aspect,  
**Translation:** 

**[4811.68s] English:** But I don't think that's one that is a measurable advantage for the U.S., or not.  
**Translation:** 

**[4814.76s] English:** It truly is just a matter of computation, right? Now, even on the computational side, when we look at  
**Translation:** Vocabulary: computation: 计算; computational: 计算相关的; measurable: 可衡量的

**[4820.72s] English:** Chips versus data centers, right? China has the unprecedented ability to build ridiculous sums.  
**Translation:** 

**[4826.84s] English:** Of power, clockwork, right? They're always building more and more power. They've got  
**Translation:** Vocabulary: clockwork: 机械装置; unprecedented: 前所未有的

**[4832.30s] English:** Steel mills that individually are the size of the entire U.S. industry, right? And they have  
**Translation:** 

**[4838.08s] English:** Got aluminum mills that consume gigawatts and gigawatts of power, right? And when we talk,...  
**Translation:** Vocabulary: aluminum: 铝; gigawatts: gig瓦; individually: 单独地

**[4842.64s] English:** About what's the biggest data center, right? OpenAI made this huge thing about Stargate.  
**Translation:** 

**[4846.90s] English:** Their announcement: There. That's like, once it's fully built out in a few years, it'll be two.  
**Translation:** Vocabulary: stargate: 星际之门

**[4851.94s] English:** Gigawatts, right? Of power, right? And this is still smaller than the largest, you know,  
**Translation:** 

**[4856.84s] English:** Industrial facilities in China, right? If China wanted to build the largest data center,  
**Translation:** 

**[4861.02s] English:** The world, if they had access to the chips, could do it. So it's not just a matter of if; it's just a question of when.  
**Translation:** 

**[4866.78s] English:** Not if, right? So their industrial capacity far exceeds that of the United States?  
**Translation:** Vocabulary: exceeds: 超过

**[4870.46s] English:** Exactly. To manufacture stuff. In the long term, they're going to be manufacturing chips there.  
**Translation:** 

**[4878.52s] English:** Chips are a little bit more specialized. I'm specifically referring to data centers.  
**Translation:** Vocabulary: manufacture: 生产

**[4882.10s] English:** Right? Chips andfabs take huge amounts of power. Don't get me wrong. That's not necessarily the  
**Translation:** 

**[4886.52s] English:** Gating factor there. The gating factor on how fast people can build the largest clusters today.  
**Translation:** Vocabulary: andfabs: 晶圆厂; clusters: 计算集群

**[4891.36s] English:** In the U.S., is power generation, right? It is whether it's now.  
**Translation:** 

**[4896.18s] English:** Power transmission, substations, and, you know, all these sorts of transformers and all these  
**Translation:** Vocabulary: substations: 变电站

**[4901.20s] English:** Things, such as building the data center, are all constraints on the U.S. industry's ability to build.  
**Translation:** 

**[4906.92s] English:** Larger and larger training systems, as well as deploying more and more inference compute.  
**Translation:** Vocabulary: compute: 计算; constraints: 限制; deploying: 部署; inference: 推理

**[4911.68s] English:** I think we need to make the point clear on why the time is now for people who don't.  
**Translation:** 

**[4916.52s] English:** Think about this: because essentially, with export controls, you're making it so that China cannot  
**Translation:** 

**[4920.00s] English:** Make or get cutting-edge chips. And the idea is that if you time this wrong, China is pouring  
**Translation:** 

**[4926.98s] English:** A ton of money into their chip production. And if you time it wrong, they are going to have more.  
**Translation:** 

**[4930.98s] English:** Capacity for production, more capacity for energy, and figure out how to make the chips and have more.  
**Translation:** 

**[4935.92s] English:** Capacity than the rest of the world to make the chips, because everybody can buy them.  
**Translation:** 

**[4939.88s] English:** To sell their Chinese chips to everybody. They might subsidize them. And therefore, if AI takes  
**Translation:** 

**[4944.76s] English:** A long time to become differentiated, we've kneecapped the financial performance of American.  
**Translation:** Vocabulary: kneecapped: 削弱; subsidize: 补贴

**[4948.90s] English:** Companies may sell less. NVIDIA can sell less. TSMC cannot sell to China. So, therefore, we have less demand.  
**Translation:** 

**[4956.10s] English:** To therefore keep driving the production cycle, so that's the assumption behind the timing being  
**Translation:** Vocabulary: assumption: 假设; cannot: 不能; timing: 时间

**[4962.90s] English:** Less than 10 years or five years to above, right? China will win because of these restrictions.  
**Translation:** 

**[4968.28s] English:** Long-term, unless AI does something in the short term, which I believe it will do.  
**Translation:** 

**[4973.44s] English:** Make massive changes to society in the medium to short term, right?  
**Translation:** 

**[4977.72s] English:** And so that's the big...  
**Translation:** 

**[4978.90s] English:** Unlocker there. And even today, right? If Xi Jinping decided to get, "quote unquote,  
**Translation:** 

**[4984.98s] English:** Scale-piled, right? I.e., decide that scaling laws are what matters, right? Just like the U.S.,  
**Translation:** Vocabulary: jinping: 习近平; unlocker: 解锁者; unquote: 引用结束

**[4991.52s] English:** Executives like Satya Nadella, Mark Zuckerberg, and Sundar, and all these U.S. executives of the  
**Translation:** 

**[4997.52s] English:** Biggest, most powerful tech companies have decided they're scale-piled and they're building.  
**Translation:** Vocabulary: executives: 高管

**[5001.62s] English:** Multi-gigawatt data centers, right? Whether it's in Texas or Louisiana or Wisconsin,  
**Translation:** 

**[5005.72s] English:** Wherever it is, they're building these massive things.  
**Translation:** Vocabulary: texas: 德克萨斯州

**[5008.90s] English:** That cost as much as their entire budget for spending on data centers globally in one spot.  
**Translation:** 

**[5014.48s] English:** Right? This is what they've committed to for next year, the year after, and so on. And so they're so  
**Translation:** Vocabulary: globally: 全世界地

**[5019.90s] English:** Convinced that this is the way, that this is what they're doing. But if China decided to,...  
**Translation:** 

**[5025.08s] English:** They could do it faster than us, but this is where the restrictions come in.  
**Translation:** 

**[5028.94s] English:** It is not clear that China, as a whole, has decided from the highest levels that this is a priority.  
**Translation:** 

**[5034.18s] English:** The U.S. sort of has, right? You see Trump talking about deep state and,  
**Translation:** 

**[5038.90s] English:** Uh, Stargate within the same.  
**Translation:** 

**[5040.00s] English:** Week, right? And the Biden administration also had a lot of discussions about AI and such. It's clear.  
**Translation:** Vocabulary: stargate: 星际之门

**[5045.44s] English:** That they think about it. Only just last week, DeepSeek met the second-in-command of China.  
**Translation:** 

**[5051.82s] English:** Right? They have not even met the top, right? They haven't met Xi. Xi hasn't sat down, and they only  
**Translation:** 

**[5057.18s] English:** Just released a subsidy of a trillion RMB, roughly $160 billion, which is closer to the spending of  
**Translation:** 

**[5065.38s] English:** Microsoft, Meta, and Google, combined, right, for this year. So it's like they're realizing it.  
**Translation:** Vocabulary: subsidy: 补助; trillion: 万亿

**[5071.42s] English:** Just now, but that's where the export restrictions come in and say, "Hey, you can't ship the most.  
**Translation:** 

**[5077.30s] English:** Powerful U.S. chips to China. You can ship a cut-down version. You can't ship the most powerful.  
**Translation:** Vocabulary: export: 出口

**[5083.66s] English:** Chips to all these countries, who we know are just going to rent it to China. You have to limit the  
**Translation:** 

**[5088.08s] English:** Numbers, right? And the tools. And the same with manufacturing tools—all these different  
**Translation:** 

**[5093.16s] English:** Aspects. But it all stems from AI.  
**Translation:** 

**[5095.10s] English:** And then what can downstream do to slow them down in AI? So, the entire semiconductor restrictions,  
**Translation:** Vocabulary: downstream: 下游; semiconductor: 半导体

**[5100.62s] English:** You read them; they are very clear. It's about AI and military-civil fusion of technology.  
**Translation:** 

**[5105.90s] English:** Right? It's very clear. And then from there, it goes: Oh, well, we're banning them from buying.  
**Translation:** Vocabulary: banning: 禁止; fusion: 融合

**[5109.76s] English:** Lithography tools, etch tools, and deposition tools. And oh, this random subsystem from a  
**Translation:** 

**[5115.60s] English:** Random company, that's tiny, right? Why are we banning this? Because all of it—the U.S. government,...  
**Translation:** Vocabulary: deposition: 沉积; lithography: 光刻

**[5120.38s] English:** Has decided is critical to AI systems. I think the fulcrum point is,  
**Translation:** 

**[5125.10s] English:** The transition from 7-nanometer to 5-nanometer chips, where I think it was Huawei that had  
**Translation:** Vocabulary: fulcrum: 支点; nanometer: 纳米

**[5130.26s] English:** A 7-nanometer chip a few years ago, which caused another political brouhaha, almost like this.  
**Translation:** 

**[5136.10s] English:** Moment. And then it's the ASML deep UV—what is that? Extreme ultraviolet lithography.  
**Translation:** Vocabulary: brouhaha: 喧闹; ultraviolet: 紫外线

**[5143.40s] English:** To set the context on the chips, right, what Nathan's referring to is in 2020,  
**Translation:** 

**[5147.12s] English:** Huawei released their Ascend 910 chip, which was an AI chip and the first one on 7 nanometers, before Google.  
**Translation:** Vocabulary: ascend: 上升; nanometers: 纳米

**[5153.72s] English:** Did they do it before NVIDIA did?  
**Translation:** 

**[5155.10s] English:** And they submitted it to the MLPerf benchmark, which is sort of an industry standard for machine learning performance.  
**Translation:** Vocabulary: benchmark: 行业标准

**[5160.00s] English:** Learning performance benchmark, and it did quite well. It was the best chip at the time.  
**Translation:** 

**[5164.58s] English:** Submission: Right, this was a huge deal. Um, the Trump administration, of course, banned it in 2019.  
**Translation:** 

**[5171.20s] English:** Right, they banned Huawei from getting seven-nanometer chips from TSMC, and so then they had...  
**Translation:** 

**[5176.06s] English:** To switch to moving using internally produced domestic chips, which was a multi-year setback.  
**Translation:** Vocabulary: internally: 内部生产; setback: 挫折

**[5180.04s] English:** Many companies have developed 7-nanometer chips, and the question is: do we know how much?  
**Translation:** 

**[5184.28s] English:** Huawei was subsidizing production of that chip, like Intel has made seven-nanometer chips that.  
**Translation:** Vocabulary: subsidizing: 补贴生产

**[5189.30s] English:** Are not profitable, and things like this. So, this is how it all feeds back into the economic engine.  
**Translation:** 

**[5194.68s] English:** Of export controls, well, so you're saying that for now Xi Jinping has not felt the AGI, but it feels  
**Translation:** Vocabulary: export: 出口; profitable: 有利可图

**[5201.66s] English:** Like the deep-seek moment, yeah. Might be meetings going on now where he's going.  
**Translation:** 

**[5208.24s] English:** To start wearing the same t-shirt, and things are going to escalate. I mean, like, this; he may...  
**Translation:** Vocabulary: escalate: 升级

**[5213.88s] English:** Last week, I woke up and found out that Lian Fang met the vice-chairman, the second-in-command guy.  
**Translation:** 

**[5219.28s] English:** And they had a meeting, and then the very next day they announced the AI subsidies, which are  
**Translation:** Vocabulary: subsidies: 补助

**[5223.74s] English:** Trillion RMB, right? So it's possible that this Deep Sea moment is truly the beginning of a cold war.  
**Translation:** 

**[5229.76s] English:** That's what a lot of people are worried about. People in AI have been worried that this is.  
**Translation:** 

**[5234.54s] English:** Going towards a cold war, or already is—but there's no need to seek fault; there's something else.  
**Translation:** 

**[5239.10s] English:** A bunch of factors came together where history works, an explosion — I mean, it all has to do with.  
**Translation:** 

**[5244.02s] English:** NVIDIA stock going down, probably, but it's just some like mass.  
**Translation:** 

**[5249.28s] English:** That happened, which eventually led to Xi Jinping having meetings and waking up to this idea.  
**Translation:** 

**[5254.56s] English:** And the U.S. government realized on October 7th, 2022, before Chat GPT was released, that this restriction...  
**Translation:** 

**[5261.38s] English:** October 7th, which dropped and shocked everyone, and it was very clearly aimed at AI. Everyone was like,  
**Translation:** Vocabulary: restriction: 限制

**[5266.42s] English:** What the heck are you doing? Stable Diffusion was out then, but not Chad GP, so it's like...  
**Translation:** 

**[5271.66s] English:** Starting to be some rumblings about what Gen AI can do to society, but it was very clear to me that...  
**Translation:** Vocabulary: diffusion: 扩散; rumblings: 不安迹象

**[5277.46s] English:** Least like the National Security Council's  
**Translation:** 

**[5279.28s] English:** Law and  
**Translation:** 

**[5280.00s] English:** And those sorts of folks thought that this was where the world was heading—the Cold War that's happening.  
**Translation:** 

**[5285.10s] English:** So, are there any concerns that export controls might push China to take military action on Taiwan?  
**Translation:** Vocabulary: export: 出口; taiwan: 台湾

**[5295.22s] English:** This is the big risk, right?  
**Translation:** 

**[5297.00s] English:** The further you push China away from having access to cutting-edge American and global technologies, the more likely they are to say, "Well, because I can't access it, I might as well, like, no one should access it," right?  
**Translation:** 

**[5308.44s] English:** And there are a few interesting aspects of that, right?  
**Translation:** 

**[5311.64s] English:** Like, you know, China has an urban-rural divide like no other.  
**Translation:** 

**[5316.74s] English:** They have a male-to-female birth ratio like no other, to the point where, if you look in most of China, it's like the ratio isn't that bad.  
**Translation:** 

**[5323.48s] English:** But when you look at single dudes in rural China, it's a 30-to-1 ratio.  
**Translation:** 

**[5327.44s] English:** And those are disenfranchised dudes, right?  
**Translation:** 

**[5329.38s] English:** Like, "quote unquote," like the U.S. has an incel problem, like China does, too.  
**Translation:** Vocabulary: disenfranchised: 失去投票权

**[5333.66s] English:** It's just that they're placated in some way or crushed down.  
**Translation:** 

**[5336.32s] English:** What do you do with these people?  
**Translation:** Vocabulary: placated: 安抚

**[5337.72s] English:** And at the same time, you're not allowed to access the most important technology.  
**Translation:** 

**[5341.56s] English:** At least the U.S. thinks so.  
**Translation:** 

**[5342.90s] English:** China is maybe starting to think this is the most important technology by starting to dump subsidies into it, right?  
**Translation:** 

**[5347.30s] English:** They thought EVs and renewables were the most important technologies.  
**Translation:** Vocabulary: renewables: 可再生能源; subsidies: 补贴

**[5349.88s] English:** They dominate that now, right?  
**Translation:** 

**[5351.34s] English:** Now they're starting to think about semiconductors in the late 2010s and early 2020s.  
**Translation:** Vocabulary: dominate: 占据主导; semiconductors: 半导体

**[5357.60s] English:** And now, they've been dumping money, and they're catching up rapidly.  
**Translation:** 

**[5360.88s] English:** And they're going to do the same with AI, right?  
**Translation:** Vocabulary: dumping: 倾倒

**[5362.64s] English:** Because they're very talented, right?  
**Translation:** 

**[5364.20s] English:** So the question is: what?  
**Translation:** 

**[5367.72s] English:** When does this hit a breaking point?  
**Translation:** 

**[5371.02s] English:** Right. And if China sees this as, hey, they can continue if they don't have access and start a true hot war — right, taking over Taiwan or trying to subvert its democracy in some way — blocking it hurts the rest of the world far more than it hurts them.  
**Translation:** Vocabulary: subvert: 颠覆; taiwan: 台湾

**[5388.00s] English:** This is something they could potentially do.  
**Translation:** 

**[5389.90s] English:** Right, and so is this pushing them toward that potentially?  
**Translation:** 

**[5393.84s] English:** Right. I'm not quite a geopolitical person, but, you know, it's.  
**Translation:** 

**[5397.72s] English:** It's obvious that the world regime of.  
**Translation:** Vocabulary: geopolitical: 地缘政治的

**[5400.00s] English:** Peace and like trade is super awesome for economics, uh, but at some point, it could break.  
**Translation:** 

**[5406.58s] English:** Right, I think we should comment that the reason why the Chinese economy would be hurt by that is that.  
**Translation:** 

**[5410.90s] English:** They're export-heavy, I think the United States buys so much. Like, if that goes away, that's  
**Translation:** 

**[5415.86s] English:** How their economy would also not be able to import raw materials from  
**Translation:** Vocabulary: import: 进口

**[5420.22s] English:** Like all over the world, the U.S. would just shut down the trade in Malacca, and you know.  
**Translation:** 

**[5424.62s] English:** At the same time, the U.S. has experienced almost all of the GDP growth in America since.  
**Translation:** Vocabulary: malacca: 马六甲

**[5429.88s] English:** You know, the '70s has been either population growth or tech, right? Um, because, you know, your  
**Translation:** 

**[5437.08s] English:** Your life today is not that much better than someone from the 80s, outside of tech, right?  
**Translation:** 

**[5441.68s] English:** Still, you know, you know, cars they all have semiconductors in them everywhere, like fridges.  
**Translation:** 

**[5445.36s] English:** Semiconductors: Everywhere, there are these funny stories about how Russians were taking them apart.  
**Translation:** Vocabulary: semiconductors: 半导体

**[5448.90s] English:** Laundry machines, because they had certain like Texas Instruments chips, that they could then  
**Translation:** 

**[5452.78s] English:** Repurpose and put into like their  
**Translation:** Vocabulary: laundry: 洗衣; repurpose: 重新利用

**[5454.60s] English:** Their anti-missile missiles, like their S-400 or whatever—you would know more about that.  
**Translation:** 

**[5459.88s] English:** This, but uh, there's all sorts of stuff about semiconductors; they're so integral to every part.  
**Translation:** Vocabulary: integral: 必不可少的; missiles: 导弹

**[5465.16s] English:** Of our lives, so can you explain the role of TSMC in the story of semiconductors and?  
**Translation:** 

**[5471.54s] English:** Maybe also how the United States can break its reliance on TSMC; I don't think it's necessarily  
**Translation:** 

**[5478.56s] English:** Breaking the reliance, I think it's about getting TSMC to build in the U.S., but so  
**Translation:** 

**[5484.50s] English:** So,  
**Translation:** 

**[5484.58s] English:** So, taking a step back, TSMC produces most of the world's chips, especially on the  
**Translation:** 

**[5491.38s] English:** Foundry side, um, you know, there are a lot of companies that build their own chips, uh, like Samsung and Intel, um,  
**Translation:** Vocabulary: foundry: 代工厂

**[5497.88s] English:** Know STMicro, Texas Instruments, you know, Analog Devices — all these kinds of companies build their  
**Translation:** 

**[5502.80s] English:** Own chips and XP, but more and more of these companies are outsourcing to TSMC and have been.  
**Translation:** Vocabulary: analog: 模拟; outsourcing: 外包

**[5508.08s] English:** For multiple decades, could you explain the supply chain there and where most of TSMC is?  
**Translation:** 

**[5513.50s] English:** In terms of manufacturing,  
**Translation:** 

**[5514.48s] English:** Sure, so historically, supply chains were such that companies would build their own chips, they would, you know,  
**Translation:** 

**[5519.86s] English:** Be.  
**Translation:** 

**[5520.00s] English:** Company started, they'd build their own chips, and then they'd design and build the  
**Translation:** 

**[5524.40s] English:** Ship and sell it. Over time, this became really difficult because the cost of building a fab increased.  
**Translation:** 

**[5529.84s] English:** Continues to compound every single generation. Of course, figuring out the technology for it,...  
**Translation:** 

**[5534.26s] English:** It is incredibly difficult, regardless, but just the dollars and cents that are required,  
**Translation:** 

**[5538.90s] English:** Ignoring, saying, "Hey, yes, I have all the technical capability," which is really hard.  
**Translation:** 

**[5542.40s] English:** To get that, by the way, right? Intel's failing, Samsung's failing, etc.  
**Translation:** Vocabulary: capability: 能力

**[5544.92s] English:** But if you look at just the dollars to spend to build that next-generation fab,  
**Translation:** 

**[5550.02s] English:** It keeps growing, right? Moore's Law is halving the cost of chips every two years.  
**Translation:** Vocabulary: halving: 减半

**[5554.22s] English:** There's a separate law that's doubling the cost of fabs every few years.  
**Translation:** 

**[5558.18s] English:** And so, you look at a leading-edge fab that is going to be profitable today and that's building  
**Translation:** Vocabulary: doubling: 翻倍; profitable: 盈利的

**[5562.42s] English:** Three-nanometer chips or two-nanometer chips in the future are going to cost north of $30.  
**Translation:** 

**[5567.14s] English:** $40 billion, right? And that's just for a token amount. That's like the base building block.  
**Translation:** Vocabulary: token: 象征性

**[5572.62s] English:** You probably need to build multiple, right? And so,  
**Translation:** 

**[5574.92s] English:** When you look at the industry over the last, if I go back 20, 30 years ago,  
**Translation:** 

**[5579.70s] English:** There were 20, 30 companies that could build the most advanced chips, and then they would design.  
**Translation:** 

**[5583.58s] English:** They would build their own chips and sell them, right? So companies like AMD would build their own chips. Intel,  
**Translation:** 

**[5587.80s] English:** Of course, they still build their own chips; they're very famous for it, but IBM would build their  
**Translation:** 

**[5590.18s] English:** Own chips. And you could keep going down the list; all these companies built their own chips.  
**Translation:** 

**[5594.60s] English:** Slowly, they kept falling like flies, and that's because of what TSMC did, right?  
**Translation:** 

**[5598.92s] English:** They created the foundry business model, which is: I'm not going to design any chips.  
**Translation:** Vocabulary: foundry: 代工工厂

**[5602.70s] English:** I'm just going to contract-manufacture chips.  
**Translation:** 

**[5604.92s] English:** Or else other people. And one of their early customers is NVIDIA, right? NVIDIA.  
**Translation:** 

**[5609.12s] English:** Is the only semiconductor company that's worth doing more than a billion dollars of  
**Translation:** 

**[5615.30s] English:** Revenue, that was started in the era of foundry, right? Every other company started before then.  
**Translation:** 

**[5620.48s] English:** And at some point, they had fabs, which is actually incredible, right? Like AMD and Intel.  
**Translation:** 

**[5625.88s] English:** And Broadcom: it's like everyone had fabs at some point, or some companies, like Broadcom.  
**Translation:** Vocabulary: broadcom: 博通公司

**[5631.80s] English:** It was like a merger or amalgamation of various companies that rolled up.  
**Translation:** 

**[5634.92s] English:** But even today, Broadcom has fabs, right? They build iPhone RF radio chips, sort of.  
**Translation:** Vocabulary: amalgamation: 合并; merger: 合并

**[5640.00s] English:** In Colorado, for you to know, Apple has fabs, and many other companies do too.  
**Translation:** 

**[5645.30s] English:** Most of the fabs, they threw them away, or sold them off, or they got rolled into something else.  
**Translation:** 

**[5648.94s] English:** And now, everyone relies on TSMC, right? Including Intel; their latest PC chip uses TSMC chips, right?  
**Translation:** 

**[5656.04s] English:** It also uses some Intel chips, but it uses TSMC for the process. Can you explain why the foundry model is used?  
**Translation:** 

**[5660.90s] English:** So successful for these companies, why are they going with economies of scale? Yeah, so I mean,  
**Translation:** 

**[5667.36s] English:** Like, like I mentioned, the cost of building a fab is so high, the R&D is so difficult, um,...  
**Translation:** 

**[5672.86s] English:** Uh, when you look at companies that had their own vertical stack, there was an  
**Translation:** 

**[5677.50s] English:** Antiquated process of, like, okay, like I'm so hyper-customized to each specific chip, right? But as we've  
**Translation:** Vocabulary: antiquated: 过时的; vertical: 垂直的

**[5683.14s] English:** Gone through the history of, sort of, like the last 50 years of electronics and semiconductors.  
**Translation:** 

**[5687.12s] English:** You need more and more specialization, right? Because Moore's Law has died, and Denard scaling has stalled.  
**Translation:** Vocabulary: electronics: 电子器件; semiconductors: 半导体; stalled: 停滞

**[5692.08s] English:** Has died. I.e., chips are not getting better; just for free, right? You know, from manufacturing, you have to.  
**Translation:** 

**[5697.00s] English:** Make.  
**Translation:** 

**[5697.20s] English:** Real architectural innovations: Google is not just running on Intel CPUs for web serving.  
**Translation:** 

**[5701.84s] English:** They have a YouTube chip, they have TPUs, they have Pixel chips, and they have a wide diversity of chips.  
**Translation:** Vocabulary: architectural: 建筑学的; innovations: 创新; pixel: 像素

**[5706.70s] English:** That, you know, generates all the economic value of Google, right? It's running, you know.  
**Translation:** 

**[5711.50s] English:** All the services and stuff, and this is just Google; you could go across any company.  
**Translation:** Vocabulary: generates: 产生

**[5715.02s] English:** In the industry, and it's like this: right, cars contain 5,000 chips, you know, 200 different  
**Translation:** 

**[5720.00s] English:** Varieties of them, right? All these random things—a Tesla door handle has two chips, right? Like it's  
**Translation:** 

**[5723.96s] English:** Like, ridiculous. Um, and it's a cool door handle, right? It's like, you know, you don't think it's  
**Translation:** 

**[5726.84s] English:** You don't think about it, but it's like it has two really chipped, like, little chip-like marks in there.  
**Translation:** Vocabulary: chipped: 裂痕

**[5731.10s] English:** Right, anyway, so as you have more diversity of chips, as you have more specialization required.  
**Translation:** 

**[5736.06s] English:** And the cost offabs continues to grow, so you need someone who is laser-focused on building the best.  
**Translation:** 

**[5741.90s] English:** Process technology, and making it as flexible as possible, I think you could say it's simple.  
**Translation:** 

**[5746.70s] English:** Which is the cost for fabrication to go up, and if you are a small player that makes a few types of chips,...  
**Translation:** Vocabulary: fabrication: 制造; flexible: 灵活

**[5752.78s] English:** You're not going to have the demand to pay back the cost of the fab.  
**Translation:** 

**[5756.84s] English:** NVIDIA can have many different customers.  
**Translation:** 

**[5760.00s] English:** Create all this demand into one place, and then they're the only ones who make enough money.  
**Translation:** 

**[5764.46s] English:** Building chips to buy the next one to build the next fab, so this is kind of why the company has been slowly doing it.  
**Translation:** 

**[5770.66s] English:** Get killed because they have the chip that was profitable and good 10 years ago.  
**Translation:** 

**[5776.24s] English:** Enough, but the cost to build the next one goes up. They may try to do this and fail because they don't.  
**Translation:** Vocabulary: profitable: 有利可图的

**[5781.04s] English:** Have the money to make it work, and then they don't have any chips, or they build it and it's too  
**Translation:** 

**[5784.28s] English:** Expensive, and they just have, or they run—you know, there are more failure points, right?  
**Translation:** 

**[5788.88s] English:** Could have one little process related to, like, some sort of chemical etch or something like that.  
**Translation:** 

**[5794.06s] English:** Like plasma etch, or you know, some little process that screws up—didn't engineer it right, and  
**Translation:** Vocabulary: plasma: 等离子; screws: 搞砸了

**[5799.10s] English:** Now, the whole company falls apart; you can't make chips right, and so super-powerful companies.  
**Translation:** 

**[5803.42s] English:** Like Intel, they had "Weathering Storm" to like, hey, they still exist today, even though...  
**Translation:** 

**[5807.76s] English:** They really screwed up their manufacturing six to seven years ago, but in the case of AMD,...  
**Translation:** 

**[5811.90s] English:** They almost went bankrupt; they had to sell their fabs to Mubadala, the UAE, right? And like that.  
**Translation:** Vocabulary: bankrupt: 破产; mubadala: 穆巴达拉

**[5818.36s] English:** Became a separate industry, and they had to sell their fabs to Mubadala, UAE, and so on.  
**Translation:** 

**[5818.86s] English:** Company called Global Foundries, which is a foundry firm, and then AMD was able to then  
**Translation:** Vocabulary: foundries: 晶圆厂; foundry: 代工厂

**[5823.24s] English:** Focus on, like, on the return back up; it was like, "Hey, let's focus on making chiplets and a bunch of  
**Translation:** 

**[5828.04s] English:** Different chips for different markets, um, and focusing on specific workloads rather than you.  
**Translation:** Vocabulary: chiplets: 小芯片; workloads: 工作负载

**[5832.66s] English:** Know all of these different things, and so you get more diversity of chips; you have more companies.  
**Translation:** 

**[5836.70s] English:** Than ever, designing chips, but you have fewer companies than ever manufacturing them, right?  
**Translation:** 

**[5841.66s] English:** This is where TSMC comes in; they've just been the best, right? They are so good.  
**Translation:** 

**[5847.06s] English:** At it right, they're customer-focused.  
**Translation:** 

**[5848.86s] English:** They make it easy for you to fabricate your chips; they take all of that complexity and simplify it.  
**Translation:** 

**[5852.64s] English:** Kind of try and abstract a lot of it away from you, um, they make good money; they don't make insane.  
**Translation:** Vocabulary: complexity: 复杂性; fabricate: 伪造; simplify: 简化

**[5856.94s] English:** Money, but they make good money, um, and they're able to aggregate all this demand and continue to.  
**Translation:** 

**[5862.26s] English:** Build the next fab, the next fab, the next fab. So, why is Taiwan so special for TSMC? Why is it  
**Translation:** Vocabulary: aggregate: 汇集; taiwan: 台湾

**[5867.38s] English:** Happening, there can it be replicated inside the United States? Yeah, so there are aspects of...  
**Translation:** 

**[5873.12s] English:** It's that I would say yes, and aspects that I'd say no; right? Um, TSMC is way ahead because it's  
**Translation:** 

**[5878.86s] English:** Uh, for  
**Translation:** 

**[5880.00s] English:** Former executive Morris Chang of Texas Instruments wasn't promoted to CEO. And he's like,  
**Translation:** Vocabulary: chang: 变化; texas: 德克萨斯州

**[5885.36s] English:** Screw this; I'm gonna go make my own chip company, right? And he went to Taiwan and made  
**Translation:** 

**[5888.72s] English:** TSMC, right. And there's a whole lot more to that story. So he could have been in Texas.  
**Translation:** 

**[5892.98s] English:** Instruments could have been TSMC, or Texas Semiconductor, but we'll keep it open for now.  
**Translation:** 

**[5896.52s] English:** Manufacturing, right? Instead of, you know, Texas Instruments, right? But, but, you know,  
**Translation:** Vocabulary: semiconductor: 半导体

**[5900.24s] English:** So, there's that whole story, sitting here in Texas. I mean, that sounds like a human.  
**Translation:** 

**[5904.84s] English:** Story: Like it didn't get promoted, just the brilliance of Morris Chang, you know, which I  
**Translation:** Vocabulary: brilliance: 卓越

**[5908.82s] English:** Wouldn't underplay. But there's also a different level to how this works.  
**Translation:** 

**[5913.54s] English:** Right. So in Taiwan, the top percent of graduates of students that  
**Translation:** Vocabulary: underplay: 低估

**[5921.30s] English:** Go to the best school, which is NTU; the top percent of those all go to work at TSMC, right.  
**Translation:** 

**[5925.80s] English:** And guess what their pay is: their starting pay is like $80,000, $70,000, right, which is like,  
**Translation:** 

**[5931.94s] English:** That's like starting pay for a good graduate in the US, right? Not the top,  
**Translation:** 

**[5935.34s] English:** The top graduates are making hundreds of thousands of dollars at Google.  
**Translation:** 

**[5938.82s] English:** And the Amazons, and now I guess the open AI systems of the world, right? So there is, there is a large  
**Translation:** 

**[5944.22s] English:** Dichotomy: What is the top 1% of society doing, and where are they headed?  
**Translation:** Vocabulary: amazons: 女战士; dichotomy: 对立面

**[5948.38s] English:** Of economic reasons, right? Intel never paid that crazy good, right? And it didn't make sense to.  
**Translation:** 

**[5952.98s] English:** Them, right? That's one aspect, right? Where's the best going? Second is the work ethic,  
**Translation:** 

**[5957.14s] English:** Right? Like, you know, we like to work a lot, and you work a lot, we work a lot. But at the end of  
**Translation:** 

**[5962.16s] English:** The day, when there's a known time and amount of work that you're  
**Translation:** 

**[5967.20s] English:** Doing what? And what does a Fab require, right?  
**Translation:** 

**[5969.08s] English:** Fabs are not work-from-home jobs; they are where you go into the fab and do grueling work, right?  
**Translation:** Vocabulary: grueling: 艰苦的

**[5974.10s] English:** There's, there's, hey, if there is any amount of vibration at all, right, an earthquake happens.  
**Translation:** 

**[5979.62s] English:** Vibrates the machines; they're all, you know, either broken or scrapped.  
**Translation:** Vocabulary: scrapped: 报废; vibrates: 震动; vibration: 振动

**[5983.72s] English:** Some of your production. And then, in many cases, they're not calibrated properly. So, so when  
**Translation:** 

**[5988.22s] English:** TSMC, when there's an earthquake, right? Recently, there's been an earthquake, and TSMC doesn't call.  
**Translation:** Vocabulary: calibrated: 校准

**[5992.50s] English:** Their employees just go to the fab and show up in the parking lot.  
**Translation:** 

**[5997.28s] English:** Gets slammed, and people just go into the fab and  
**Translation:** Vocabulary: slammed: 受到冲击

**[6000.00s] English:** Fix it right, like it's an arm. It's like a hive of ants, you know?  
**Translation:** 

**[6004.06s] English:** Doesn't get told by the queen what to do; the ants just know. It's like one person just specializing.  
**Translation:** Vocabulary: specializing: 专门化

**[6010.06s] English:** On this one task, and it's like you're going to take this one tool, and you're the best person in  
**Translation:** 

**[6014.04s] English:** The world, and this is what you're going to do for your whole life: is this one task in the Fab?  
**Translation:** 

**[6017.36s] English:** Is like some special chemistry, plus nano-manufacturing on one line of tools that  
**Translation:** 

**[6021.94s] English:** Continues to get iterated, and yeah, it's just like specific plasma edge for removing.  
**Translation:** Vocabulary: plasma: 等离子体

**[6026.90s] English:** Silicon dioxide, right? That's all you focus on for your whole career, and it's like such a specialized field.  
**Translation:** 

**[6030.88s] English:** Thing, and so it's not like the tasks are transferable. AI today is awesome because, like,...  
**Translation:** Vocabulary: silicon: 硅

**[6035.72s] English:** People can pick it up like that, but semiconductor manufacturing is very antiquated and difficult.  
**Translation:** 

**[6040.68s] English:** None of the materials are online for people to read easily, and the papers are very  
**Translation:** Vocabulary: antiquated: 过时的; semiconductor: 半导体

**[6045.62s] English:** Dense, and it takes a lot of experience to learn. So, it makes the barrier.  
**Translation:** 

**[6050.60s] English:** To enter, it's much higher, too. So, when you talk about having all these people that are  
**Translation:** Vocabulary: barrier: 障碍

**[6054.98s] English:** Super-specialized, they will work.  
**Translation:** 

**[6056.90s] English:** You know, 80 hours a week in a factory—right in a fab—and if anything goes wrong, they'll go.  
**Translation:** 

**[6063.06s] English:** Show up in the middle of the night because some earthquake; their wife was like, "There was an  
**Translation:** 

**[6066.30s] English:** Earthquake! He's like, "Great, I'm gonna go to the fab." It's like, would you like to come with?  
**Translation:** 

**[6071.08s] English:** American do that, right? It's like these sorts of things are, I guess, the ones you know.  
**Translation:** 

**[6075.08s] English:** Exemplifying, why TSMC is so amazing, now: can you replicate it in the U.S.? Let's not ignore.  
**Translation:** Vocabulary: exemplifying: 举例子

**[6080.74s] English:** Intel was the leader in manufacturing for over 20 years, and they brought every technology to market.  
**Translation:** 

**[6086.28s] English:** First,  
**Translation:** 

**[6086.90s] English:** Besides EUV, strained silicon, high-k metal gates, FinFETs — you know, the list goes on and on.  
**Translation:** 

**[6093.14s] English:** Of the technologies that Intel brought to market first, the ones that made the most money were those related to, um, and, and, and  
**Translation:** Vocabulary: strained: 拉伸的

**[6098.50s] English:** Manufactured at scale, first, best, and highest profit margins—right? So, we shouldn't ignore that Intel.  
**Translation:** 

**[6104.14s] English:** Can't do this right; it's that the culture has broken, right? You've invested in the wrong...  
**Translation:** Vocabulary: manufactured: 批量生产的; margins: 利润Margins

**[6109.74s] English:** Things they said "no" to the iPhone; they had all these different things, like you  
**Translation:** 

**[6114.26s] English:** Know about the mismanagement of the fabs and designs.  
**Translation:** Vocabulary: mismanagement: 管理不善

**[6116.90s] English:** This lock-up, right, and at the same time, old.  
**Translation:** 

**[6120.00s] English:** These brilliant people, like 50,000 PhDs or masters, have been working...  
**Translation:** 

**[6125.00s] English:** On specific chemical or physical processes or nano-manufacturing processes for decades in Oregon.  
**Translation:** 

**[6130.80s] English:** They're still there, producing amazing work. It's just a matter of getting it to the right place.  
**Translation:** 

**[6134.20s] English:** Last mile of production at high yield, where you can design and manufacture dozens and  
**Translation:** 

**[6138.96s] English:** Hundreds of different kinds of chips, you know, and it's good customer experience has broken down.  
**Translation:** Vocabulary: manufacture: 生产

**[6144.18s] English:** You know, it's all about the customer experience. It's like the part of it where people will say Intel.  
**Translation:** 

**[6147.94s] English:** Is too pompous in the 2000s and 2010s, right? They just thought they were better than everyone. The tool.  
**Translation:** Vocabulary: pompous: 自大的

**[6152.24s] English:** Guys were like, "Oh, I don't think that's mature enough." They're like, "You just don't know.  
**Translation:** 

**[6155.48s] English:** We know, right, that this sort of stuff would happen, and so can the U.S. bring it to the table, can the U.S.?  
**Translation:** Vocabulary: mature: 成熟

**[6161.90s] English:** Bring leading-edge semiconductor manufacturing to the U.S.? Emphatically, yes! Right, and we are.  
**Translation:** 

**[6166.28s] English:** It's happening; Arizona is getting better and better as time goes on. TSMC has built, you know,  
**Translation:** Vocabulary: arizona: 亚利桑那州; emphatically: 坚定地; semiconductor: 半导体

**[6172.06s] English:** Roughly 20 percent of their capacity for five-nanometer production in the U.S. right now is nowhere near full utilization.  
**Translation:** 

**[6177.92s] English:** Near enough, right? You know, 20% of capacity in the U.S. is like nothing, right? And furthermore,  
**Translation:** Vocabulary: utilization: 使用率

**[6183.60s] English:** This is still dependent on Taiwan existing, right? All there's really an important way to separate it.  
**Translation:** 

**[6188.16s] English:** Out, there's RND, and there's high-volume manufacturing. There are there effectively.  
**Translation:** Vocabulary: taiwan: 台湾

**[6193.18s] English:** There are three places in the world that are doing leading-edge R&D. There's Taiwan, and...  
**Translation:** 

**[6198.32s] English:** There's Hillsborough, Oregon, and there is Pyongyang, South Korea, right?  
**Translation:** Vocabulary: hillsborough: Hillsborough; pyongyang: 平壤

**[6204.52s] English:** Three places are doing the leading-edge R&D for the rest of the world's  
**Translation:** 

**[6207.92s] English:** Leading-edge semiconductors, right now, manufacturing can be distributed more globally.  
**Translation:** Vocabulary: globally: 全世界地; semiconductors: 半导体

**[6213.44s] English:** Right, um, and this is sort of where this dichotomy exists: of like who's actually modifying the  
**Translation:** 

**[6219.68s] English:** Process: Who's actually developing the next generation, one who's improving them is... since  
**Translation:** Vocabulary: dichotomy: 对立面; modifying: 修改

**[6224.40s] English:** You are Hillsborough, not Pyongyang, right? It's not like the other fabs, like Arizona.  
**Translation:** 

**[6230.14s] English:** Right, Arizona is a paperweight. If you've disappeared off the face of the planet, um,...  
**Translation:** 

**[6235.16s] English:** Know within a year or a couple of years.  
**Translation:** 

**[6237.92s] English:** Arizona would stop producing too, right?  
**Translation:** 

**[6240.00s] English:** It's actually pretty critical.  
**Translation:** 

**[6241.92s] English:** One of the things I like to say is that if I had a few missiles, I know exactly where I could.  
**Translation:** Vocabulary: missiles: 导弹

**[6246.06s] English:** Cause the most economic damage, right?  
**Translation:** 

**[6247.52s] English:** It's not targeting the White House, right?  
**Translation:** 

**[6248.96s] English:** It's the R&D centers.  
**Translation:** 

**[6250.22s] English:** It's the R&D centers for TSMC, Intel, Samsung, and then some of the memory guys, Micron and  
**Translation:** Vocabulary: micron: 微米

**[6254.68s] English:** Hynix.  
**Translation:** 

**[6255.08s] English:** Because they define the future evolution of these semiconductors, and everything's moving.  
**Translation:** 

**[6258.46s] English:** So, it's happening so rapidly that it really is fundamentally about R&D.  
**Translation:** 

**[6263.86s] English:** And it is all about TSMC, huh?  
**Translation:** Vocabulary: fundamentally: 从根本上

**[6267.18s] English:** And so, TSMC: you cannot purchase a vehicle without TSMC chips, right?  
**Translation:** 

**[6272.74s] English:** You cannot purchase a fridge without TSMC chips.  
**Translation:** 

**[6275.76s] English:** I think one of the few things you can purchase, ironically, is a Texas Instruments graphing calculator.  
**Translation:** 

**[6282.58s] English:** Calculator, right?  
**Translation:** Vocabulary: calculator: 计算器; graphing: 图形绘制; ironically: 讽刺的是

**[6283.46s] English:** Because they actually manufacture in Texas.  
**Translation:** 

**[6284.88s] English:** But outside of that, a laptop, a phone, servers, GPUs—none of this stuff can exist.  
**Translation:** Vocabulary: laptop: 笔记本; manufacture: 制造

**[6291.06s] English:** And this is without TSMC.  
**Translation:** 

**[6292.84s] English:** And in many cases, it's not even like the leading edge, you know, sexy five-nanometer technology.  
**Translation:** 

**[6296.12s] English:** Chip, three-nanometer chip.  
**Translation:** 

**[6297.18s] English:** A two-nanometer chip.  
**Translation:** 

**[6298.10s] English:** Oftentimes, it's just like some stupid power IC that's converting from, you know,  
**Translation:** 

**[6302.60s] English:** Some voltage to another, right?  
**Translation:** Vocabulary: converting: 转换; oftentimes: 经常; voltage: 电压

**[6303.74s] English:** And it's made at TSMC, right?  
**Translation:** 

**[6304.76s] English:** This is what China is investing in, as well.  
**Translation:** 

**[6306.54s] English:** It's like they can build out this long-tail Fab, where the techniques are much more known.  
**Translation:** 

**[6310.36s] English:** You don't have to figure out these problems with EUV.  
**Translation:** 

**[6312.62s] English:** They're investing in this.  
**Translation:** 

**[6314.10s] English:** And then they have a large supply for things like car door handles and random stuff.  
**Translation:** 

**[6320.08s] English:** And that trickles down into this whole economic discussion as well, which is why they have far  
**Translation:** 

**[6325.72s] English:** More than we do.  
**Translation:** Vocabulary: trickles: 渗透

**[6326.40s] English:** And having supplies for things like this is crucial to normal life.  
**Translation:** 

**[6329.46s] English:** So they're starting to invest in high-volume manufacturers, but they're not doing R&D.  
**Translation:** Vocabulary: crucial: 至关重要

**[6334.90s] English:** So, they do R&D on their own.  
**Translation:** 

**[6336.62s] English:** They're just way behind, right?  
**Translation:** 

**[6337.94s] English:** So, I would say that in 2015, China had a five-year plan where they defined goals for 2025 and 2020.  
**Translation:** 

**[6346.50s] English:** Goals, including at least 80% domestic production of semiconductors.  
**Translation:** Vocabulary: semiconductors: 半导体

**[6350.14s] English:** They're not going to hit that, right?  
**Translation:** 

**[6351.62s] English:** To be clear.  
**Translation:** 

**[6352.36s] English:** But they are, in certain areas, really, really close, right?  
**Translation:** 

**[6355.42s] English:** Like BYD.  
**Translation:** 

**[6356.40s] English:** BYD is probably going to be the first company in the world to not have to.  
**Translation:** 

**[6360.00s] English:** Use TSMC for making because they have their ownfabs, right? For making chips now, they still  
**Translation:** Vocabulary: ownfabs: 自有晶圆厂

**[6365.02s] English:** Have to buy some chips from foreign sources, for example, like those with advanced self-driving and ADAS capabilities.  
**Translation:** 

**[6370.62s] English:** Because those are really high-end, but at least like, you know, like an internal combustion engine.  
**Translation:** Vocabulary: capabilities: 功能; combustion: 燃烧

**[6374.86s] English:** Has 40 chips and an EV, you know, just for controlling like flow rates and all these.  
**Translation:** 

**[6378.66s] English:** Things and EVs are even more complicated, so all these different power ICs and battery management systems.  
**Translation:** 

**[6383.16s] English:** Controllers and all these things—they're insourcing, right? And this is something,...  
**Translation:** 

**[6388.12s] English:** That, like China has been doing since 2015, now as far as the trailing edge, they're getting so  
**Translation:** Vocabulary: insourcing: 内部采购; trailing: 后端

**[6393.66s] English:** Much capacity, there as far as the leading edge, right? I.e., this five-nanometer and so on and so forth.  
**Translation:** 

**[6398.62s] English:** Right where GPUs are still behind, and this is where U.S. restrictions are trying to stop them.  
**Translation:** 

**[6404.18s] English:** In the ladder, but you know, all that's happened is, yes, they've slowed down their five.  
**Translation:** 

**[6408.50s] English:** Nanometer, three-nanometer, etc., but they've accelerated to 45-nanometer and 90-nanometer.  
**Translation:** Vocabulary: accelerated: 加速; nanometer: 纳米

**[6413.94s] English:** Power IC, or analog IC, or you know, random chip in my keyboard, right?  
**Translation:** 

**[6418.12s] English:** That kind of stuff, so there is an angle of how the U.S.'s actions have been so... from these.  
**Translation:** Vocabulary: analog: 模拟芯片

**[6424.02s] English:** Export, you know, from the angle of the expert, controls have been so inflammatory as to slow...  
**Translation:** 

**[6429.28s] English:** Down China's progress on the leading edge, that they've turned around and have accelerated their  
**Translation:** Vocabulary: export: 出口; inflammatory: 激进的

**[6433.72s] English:** Progress elsewhere because they know that this is so important, especially if the U.S. is going to lock in these gains.  
**Translation:** 

**[6437.56s] English:** They might let us out here, or if they lock us out here as well, in the trailing edge. Going back... Can the...  
**Translation:** 

**[6442.08s] English:** U.S. built it here, um, yes, but it's going to take a ton of money, I truly think.  
**Translation:** 

**[6448.12s] English:** To revolutionize and completely in-source semiconductors would take a decade and a  
**Translation:** Vocabulary: revolutionize: 彻底改变; semiconductors: 半导体

**[6452.28s] English:** Trillion dollars is some of it, too—culture, like you said: extreme competence and extreme work ethic.  
**Translation:** 

**[6457.80s] English:** In Taiwan, I think if you have the demand and the money is on the line, American companies figure  
**Translation:** 

**[6462.80s] English:** It's going to take handholding with the government, but I think that the culture helps.  
**Translation:** 

**[6467.14s] English:** TSMC's breakthrough and it's easier for them; you get that TSMC has around 90, 000 employees, right?  
**Translation:** Vocabulary: handholding: 扶持

**[6472.52s] English:** It's not actually that insane amount; the Arizona Fab has $3,000 from Taiwan.  
**Translation:** 

**[6478.12s] English:** And these people, like their wives, were like  
**Translation:** Vocabulary: arizona: 亚利桑那; taiwan: 台湾

**[6480.00s] English:** Like, yeah, we're not going to have kids unless you sign up for the Arizona Fab.  
**Translation:** 

**[6483.18s] English:** We go to Arizona, and we have our kids there.  
**Translation:** 

**[6484.82s] English:** There's also a Japan fab where the same thing happened, right?  
**Translation:** 

**[6486.94s] English:** And so, these wives drove their husbands to go to Japan or America to have the kids there.  
**Translation:** 

**[6493.10s] English:** And it's an element of culture.  
**Translation:** 

**[6494.64s] English:** Yeah, sure.  
**Translation:** 

**[6495.42s] English:** Taiwan works that hard.  
**Translation:** 

**[6496.68s] English:** But the U.S. has also done it in the past.  
**Translation:** 

**[6498.90s] English:** They could do it now, right?  
**Translation:** 

**[6500.78s] English:** We can just import, I say, import the best people in the world if we want to.  
**Translation:** Vocabulary: import: 引入

**[6505.50s] English:** That's where the immigration conversation is a tricky one.  
**Translation:** 

**[6508.54s] English:** And there has been a lot of debate over that.  
**Translation:** Vocabulary: tricky: 棘手的

**[6509.78s] English:** But, yeah, it seems absurdly controversial to import the best people in the world.  
**Translation:** 

**[6514.46s] English:** I don't understand why it's controversial.  
**Translation:** Vocabulary: absurdly: 荒谬地

**[6516.24s] English:** That's one of the ways of winning.  
**Translation:** 

**[6518.24s] English:** I'm sure we agree with you.  
**Translation:** 

**[6519.58s] English:** And even if you can't import those people, I still think you could do a lot to manufacture  
**Translation:** 

**[6523.78s] English:** Most of them in the U.S., if the money's there, right?  
**Translation:** Vocabulary: manufacture: 生产

**[6526.38s] English:** And so, it's just way more expensive.  
**Translation:** 

**[6528.02s] English:** It's not profitable for a long time.  
**Translation:** Vocabulary: profitable: 有利可图的

**[6529.82s] English:** And that's the context of the CHIPS Act, which is only about $50 billion relative to some of  
**Translation:** 

**[6535.14s] English:** The renewable initiatives that were passed in the Inflation Reduction Act and the infrastructure  
**Translation:** Vocabulary: inflation: 通货膨胀; initiatives: 举措

**[6539.76s] English:** Act.  
**Translation:** 

**[6539.78s] English:** Which total, in the hundreds of billions of dollars, right?  
**Translation:** 

**[6543.06s] English:** And so, the amount of money that the U.S. is spending on the semiconductor industry is  
**Translation:** 

**[6546.66s] English:** Nothing, right?  
**Translation:** 

**[6548.20s] English:** Whereas all these other countries have structural advantages in terms of work ethic and amount,  
**Translation:** 

**[6553.28s] English:** Of work and things like that, but also a number of STEM graduates, the percentile of their  
**Translation:** Vocabulary: percentile: 百分位

**[6557.96s] English:** Best going to that, right?  
**Translation:** 

**[6559.78s] English:** But they also have differences in terms of, like, hey, there are just tax benefits in the  
**Translation:** 

**[6565.30s] English:** Law and have been in the law for 20 years, right?  
**Translation:** 

**[6567.42s] English:** And then, some countries have massive.  
**Translation:** 

**[6569.70s] English:** Subsidies, right?  
**Translation:** 

**[6570.72s] English:** China has something like $200 billion in semiconductor subsidies per year.  
**Translation:** Vocabulary: semiconductor: 半导体; subsidies: 补贴

**[6575.36s] English:** We're talking about $50 billion in the U.S. over, like, six years, right?  
**Translation:** 

**[6578.78s] English:** So, the girth or difference in, like, the subsidy amounts is also huge, right?  
**Translation:** Vocabulary: girth: 规模; subsidy: 补助

**[6583.68s] English:** And so I think, you know, Trump has been talking about tariffs on Taiwan recently.  
**Translation:** 

**[6588.76s] English:** You know, that's sort of like one of those things that's, oh, okay, well, like,...  
**Translation:** Vocabulary: taiwan: 台湾; tariffs: 关税

**[6592.82s] English:** You know, maybe he doesn't want to subsidize the semiconductor industry.  
**Translation:** 

**[6596.02s] English:** Obviously, tariffing Taiwan is going to cost a lot, making many things much more expensive.  
**Translation:** Vocabulary: subsidize: 补贴; tariffing: 征关税

**[6599.68s] English:** And so.  
**Translation:** 

**[6600.00s] English:** But does it change the equation for TSMC building more fabs in the U.S.? That's what he's sort of wondering.  
**Translation:** Vocabulary: equation: 方程

**[6604.00s] English:** Positing, right? So, can you lay out the importance? By the way, it's incredible how...  
**Translation:** 

**[6610.76s] English:** Much of this, you know, we told you. Dylan knows all this stuff, yeah. So, okay, you've laid it out.  
**Translation:** Vocabulary: positing: 假设

**[6618.72s] English:** Why is TSMC really important if we look out 10 to 20 years into the future, and the U.S.-China relationship?  
**Translation:** 

**[6627.28s] English:** It seems like it could go to a dark place, from a cold war to an escalated cold war, even a hot war.  
**Translation:** Vocabulary: escalated: 升级

**[6636.50s] English:** Or, to a good place—anything from frenemies to cooperation to working together. So, in this game.  
**Translation:** 

**[6646.54s] English:** Theory, complicated game; uh, what are the different trajectories? What should the U.S. be doing? Like, what?  
**Translation:** Vocabulary: frenemies: 敌友; trajectories: 发展路径

**[6653.30s] English:** Do you see any different possible trajectories of U.S.-China relations as, uh,  
**Translation:** 

**[6657.28s] English:** Both leaders start to feel the AGI more and more, and see the importance of chips and the importance  
**Translation:** 

**[6663.08s] English:** Of AI, I mean, ultimately, the export controls are pointing toward a separate future economy, I think.  
**Translation:** 

**[6670.40s] English:** The U.S. has made it clear to Chinese leaders that we intend to control this technology at whatever cost.  
**Translation:** Vocabulary: export: 出口

**[6678.02s] English:** Cost to global economic integration is such that it's hard to unwind that.  
**Translation:** 

**[6685.80s] English:** Card has been played.  
**Translation:** 

**[6687.28s] English:** At some point, you know, there was a convergence, right? But, over at least the  
**Translation:** 

**[6697.94s] English:** In the last decade, it's been branching further and further out; right now, U.S. companies can't enter.  
**Translation:** Vocabulary: convergence: 交汇

**[6702.04s] English:** China's Chinese companies can't enter the U.S.; the U.S. is saying, "Hey, China, you can't get access to  
**Translation:** 

**[6708.04s] English:** Our technologies in certain areas, and China's rebuttal with the same thing around, like you.  
**Translation:** 

**[6713.22s] English:** Know they've done some sort of specific materials, and you know, gallium and things like that.  
**Translation:** 

**[6717.28s] English:** That they've tried to limit the U.S., on one of the  
**Translation:** Vocabulary: gallium: 镓

**[6720.00s] English:** There's a U.S. drone company that's not allowed to buy batteries, and they have, like, military customers.  
**Translation:** 

**[6724.22s] English:** And this drone company just tells military customers, "like, just get it from Amazon because I can't actually physically get them," right?  
**Translation:** Vocabulary: drone: 无人驾驶飞机

**[6730.04s] English:** Like, there are all these things happening that point to further and further divergence.  
**Translation:** 

**[6734.04s] English:** I have zero idea, and I would love if we could all hold hands and sing "Kumbaya," but, like, I have zero idea how that could possibly happen.  
**Translation:** Vocabulary: divergence: 分歧; kumbaya: 团结之歌

**[6740.86s] English:** Is the divergence good or bad for avoiding war?  
**Translation:** 

**[6745.28s] English:** Is it possible that the divergence in terms of manufacturer chips, used in training AI systems, is actually good for avoiding military conflict?  
**Translation:** Vocabulary: manufacturer: 生产商

**[6755.34s] English:** It's an objective fact that the world has been the most peaceful it has ever been when there are global hegemonies, or regional hegemonies, in historical context, right?  
**Translation:** 

**[6765.24s] English:** The Mediterranean was the most peaceful ever when the Romans were there, right?  
**Translation:** Vocabulary: hegemonies: 霸权

**[6768.52s] English:** China had very peaceful and warring times, and the peaceful times were when dynasties had a lockhold over not just themselves, but all their tributaries around.  
**Translation:** 

**[6775.28s] English:** And, likewise, the most peaceful time in human history has been when the U.S. was the global hegemon, right? The last few decades.  
**Translation:** Vocabulary: dynasties: 王朝; hegemon: 霸主; likewise: 同样; lockhold: 控制; tributaries: 朝贡国

**[6784.12s] English:** Now, we've sort of seen things start to slide, right, with Russia-Ukraine, with what's going on in the Middle East, and, you know, Taiwan risk.  
**Translation:** 

**[6790.64s] English:** All these different things are starting to bubble up, still objectively, extremely peaceful.  
**Translation:** Vocabulary: objectively: 客观地; taiwan: 台湾

**[6794.50s] English:** Now, what happens when it's not one global hegemon, but it's two—obviously, and, you know, China will be competitive or even overtake the U.S., like it's possible, right?  
**Translation:** 

**[6803.98s] English:** And so, this...  
**Translation:** Vocabulary: overtake: 超越

**[6805.28s] English:** This change in global hegemony is...  
**Translation:** 

**[6807.96s] English:** I don't think it ever happens super peacefully, right?  
**Translation:** Vocabulary: hegemony: 霸权; peacefully: 和平地

**[6809.94s] English:** When empires fall, right; they don't fall gracefully, right?  
**Translation:** 

**[6815.64s] English:** Like, they don't just slide out of irrelevance.  
**Translation:** Vocabulary: empires: 帝国; irrelevance: 无关性

**[6817.96s] English:** Usually, there is a lot of shaking.  
**Translation:** 

**[6820.24s] English:** And so, you know, what the U.S. is trying to do is maintain its top position.  
**Translation:** 

**[6825.06s] English:** And what China is trying to do is become the top position, right?  
**Translation:** 

**[6827.70s] English:** And, obviously, there's some butting of heads here in the most simple terms.  
**Translation:** 

**[6832.78s] English:** And that could take shape in all kinds of ways.  
**Translation:** 

**[6835.28s] English:** Including proxy wars.  
**Translation:** Vocabulary: proxy: 代理战争

**[6837.82s] English:** And that will...  
**Translation:** 

**[6838.48s] English:** It seems like it's already happening.  
**Translation:** 

**[6839.82s] English:** Like, I....  
**Translation:** 

**[6840.00s] English:** As much as I want there to be centuries of prolonged peace, it looks like further instability internationally is ahead.  
**Translation:** 

**[6848.66s] English:** And the U.S.'s sort-of current task is, like, hey, if we control AI, if we're the leader in AI, and AI significantly accelerates progress, then we can maintain the global hegemony position.  
**Translation:** 

**[6861.36s] English:** I hope that works.  
**Translation:** Vocabulary: accelerates: 加速

**[6862.40s] English:** And, as an American, kind of like, okay, I guess that's going to lead to peace for us.  
**Translation:** 

**[6867.54s] English:** Now, obviously, other people around the world are affected negatively.  
**Translation:** Vocabulary: negatively: 不利地

**[6872.90s] English:** Obviously, the Chinese people are not going to be in as advantageous a position if that happens.  
**Translation:** 

**[6878.00s] English:** But this is, sort of, the reality of what's being done and the actions that are being carried out.  
**Translation:** Vocabulary: advantageous: 有利的

**[6884.28s] English:** So, can we go back to the specific details of the different hardware?  
**Translation:** 

**[6887.62s] English:** There's this nice graphic in the export controls that shows which GPUs are allowed to be exported.  
**Translation:** Vocabulary: export: 出口; exported: 已经出口的

**[6897.54s] English:** Can you kind of explain the difference?  
**Translation:** 

**[6900.28s] English:** Is there, from a technical perspective, are the H20s promising? (Note: The question seems to be missing a verb after "are." A more natural phrasing might be: "Is there, from a technical perspective, anything promising about the H20s?" or "Are the H20s promising from a technical perspective?")  
**Translation:** Vocabulary: phrasing: 表达方式

**[6908.02s] English:** Yeah, so this goes, and I think we'd have to really dive deep into the reasoning aspect and what's going on there.  
**Translation:** 

**[6914.62s] English:** But the H2O: you know, the U.S. has gone through multiple iterations of the export controls, right?  
**Translation:** Vocabulary: iterations: 多次修订

**[6920.34s] English:** This H800 was, at one point, allowed back in 2023, but then it got canceled.  
**Translation:** 

**[6924.78s] English:** And by then, you know, DeepSeek had already built their cluster.  
**Translation:** Vocabulary: cluster: 计算集群

**[6927.54s] English:** They claimed $2K.  
**Translation:** 

**[6928.76s] English:** I think they actually have a lot more—like around 10,000 of those.  
**Translation:** 

**[6931.80s] English:** And now, this H2O is the legally allowed chip, right?  
**Translation:** 

**[6934.48s] English:** NVIDIA shipped a million of these last year to China, right?  
**Translation:** 

**[6937.22s] English:** For context, it was like four or five million GPUs, right?  
**Translation:** 

**[6939.76s] English:** So, the percentage of GPUs that were this China-specific H20 is quite high, right?  
**Translation:** 

**[6945.52s] English:** You know, roughly 20% to 25%, right?  
**Translation:** 

**[6947.92s] English:** 20% or so.  
**Translation:** 

**[6948.86s] English:** And so this H2O has been neutered in one way, but it's actually upgraded in other ways, right?  
**Translation:** 

**[6955.12s] English:** And, you know, you could think of chips along three.  
**Translation:** Vocabulary: neutered: 阉割; upgraded: 升级

**[6957.58s] English:** Axis for AI, right?  
**Translation:** 

**[6959.60s] English:** You know, ignore it.  
**Translation:** 

**[6960.00s] English:** Ignoring the software stack and exact architecture, just focusing on raw specifications: there's floating-point operations (FLOPS), memory bandwidth (i.e., memory capacity), IO, memory, and then interconnect (chip-to-chip connections). All three of these are incredibly important for making AI systems because they involve a lot of compute.  
**Translation:** 

**[6983.00s] English:** They involve a lot of moving memory around, whether it be to memory or to other chips, right?  
**Translation:** Vocabulary: bandwidth: 内存带宽; compute: 计算; interconnect: 片间连接

**[6988.00s] English:** And so these three vectors: the U.S. initially had two of these vectors controlled, and one of them not controlled (which was flops and interconnect bandwidth), and these were initially controlled.  
**Translation:** 

**[6997.82s] English:** And then they said, "No, no, no, no.  
**Translation:** Vocabulary: flops: 运算次数; vectors: 方向

**[6999.10s] English:** We're going to remove the interconnect bandwidth and just make it a very simple, only flops.  
**Translation:** 

**[7002.48s] English:** But now, NVIDIA can make a chip that has cut down on flops.  
**Translation:** 

**[7006.98s] English:** It's like one-third that of the H100, right?  
**Translation:** 

**[7010.54s] English:** On the spec sheet, paper performance for FLOPS is usually much higher. In the real world, it's closer to about half—or maybe even as low as 60%—of that, right?  
**Translation:** 

**[7019.54s] English:** But then, on the other two vectors, it's just as good for interconnect bandwidth.  
**Translation:** 

**[7023.34s] English:** And then, for memory bandwidth and memory capacity, the H20 has more memory bandwidth and more memory capacity than the H100, right?  
**Translation:** 

**[7030.68s] English:** Now, recently, we at our research have cut NVIDIA's production for H20 for this year down drastically.  
**Translation:** 

**[7037.94s] English:** They were going to make another 2 million of those this year.  
**Translation:** Vocabulary: drastically: 大幅地

**[7040.54s] English:** But they just canceled all the orders a couple of weeks ago.  
**Translation:** 

**[7043.50s] English:** In our view, that's because we think that they think they're going to get restricted, right?  
**Translation:** 

**[7047.50s] English:** Because, why would they cancel all these orders for H20?  
**Translation:** 

**[7050.70s] English:** Because they shipped a million of them last year.  
**Translation:** 

**[7052.40s] English:** They had orders in for a couple million this year—and just gone, right?  
**Translation:** 

**[7055.46s] English:** For H2O, B20, right?  
**Translation:** 

**[7056.68s] English:** A successor to H2O.  
**Translation:** 

**[7058.08s] English:** And now, they're all gone.  
**Translation:** 

**[7059.12s] English:** Now, why would they do this, right?  
**Translation:** 

**[7061.14s] English:** I think it's very clear, right?  
**Translation:** 

**[7063.12s] English:** The H20 is actually better for certain tasks.  
**Translation:** 

**[7066.36s] English:** And that certain task is reasoning, right?  
**Translation:** 

**[7069.50s] English:** Okay, reasoning is incredibly different from how you look at the different regimes of models, right?  
**Translation:** 

**[7076.26s] English:** Pre-training is all about FLOPs, right?  
**Translation:** Vocabulary: regimes: 模式体系

**[7079.16s] English:** It's all about flops.  
**Translation:** 

**[7080.00s] English:** There are things you can do, like a mixture of experts that we talked about, to trade off interconnect or to trade off other aspects and lower the FLOPs, and rely more on interconnect and memory.  
**Translation:** Vocabulary: flops: 浮点运算; interconnect: 互联; mixture: 混合

**[7090.26s] English:** But at the end of the day, it's flops that matter. Right. We talk about models in terms of how many flops they are. Right.  
**Translation:** 

**[7096.64s] English:** So, like, you know, we talk about, oh, GPT-4 is 2^25. Right—2 to the 25th, you know, with 25 zeros. Right? Flops—right, floating-point operations for training.  
**Translation:** 

**[7108.72s] English:** For training. Right. And we're talking about the restrictions for the 2E24, right? The U.S. has an executive order that Trump recently unsigned, but which required, hey, at 1E26 floating point operations, you must notify the government and share your results with us. Right.  
**Translation:** 

**[7125.52s] English:** Like, there's a level at which the U.S. government must be told. Right. And that's 1E26. And so, as we move forward, this is an incredibly important vector that the government has cared about historically.  
**Translation:** Vocabulary: historically: 历史上

**[7137.02s] English:** But the other two vectors are.  
**Translation:** 

**[7138.72s] English:** Arguably, just as important. Right. And especially when we come to this new paradigm, which the world is only just learning about over the last six months. Right. Reasoning.  
**Translation:** Vocabulary: arguably: 或许; paradigm: 范式; vectors: 向量

**[7147.44s] English:** And do we understand firmly which of the three dimensions is best for reasoning? So, interconnectedness doesn't matter as much. Is it memory?  
**Translation:** 

**[7157.34s] English:** Memory. Right. Yeah. Excellent. We're going to get into technical stuff really fast.  
**Translation:** Vocabulary: dimensions: 维度; interconnectedness: 关联性

**[7161.42s] English:** There are two articles in this one that I could show, maybe some graphics that might be interesting for you to pull up.  
**Translation:** 

**[7166.60s] English:** For the listeners, we're looking at the second.  
**Translation:** Vocabulary: listeners: 听众

**[7168.72s] English:** Section of OH-One Inference Architectures Tokenomics.  
**Translation:** 

**[7173.22s] English:** You want to explain KV cache before we talk about this?  
**Translation:** Vocabulary: cache: 缓存; inference: 推理; tokenomics: 代经济

**[7175.14s] English:** I think it's better to.  
**Translation:** 

**[7176.10s] English:** Okay. Yeah, we should get that.  
**Translation:** 

**[7177.24s] English:** We need to go through a lot of specific technical things as transformers to make this easier for people because it's incredibly important, because this changes how models work.  
**Translation:** 

**[7186.30s] English:** But I think I think resetting.  
**Translation:** 

**[7187.86s] English:** Right. Why is memory so important?  
**Translation:** 

**[7191.22s] English:** It's because, so far, we've talked about parameter counts.  
**Translation:** Vocabulary: parameter: 参数

**[7193.50s] English:** Right. And a mixture of experts.  
**Translation:** 

**[7194.94s] English:** You can change how many active parameters versus total parameters to embed more data.  
**Translation:** Vocabulary: embed: 嵌入; mixture: 混合

**[7198.50s] English:** I have fewer flops, but.  
**Translation:** 

**[7200.00s] English:** But more importantly, another aspect of what's part of this humongous revolution in the last handful of years is the transformer.  
**Translation:** Vocabulary: flops: 失败; humongous: 巨大的

**[7206.86s] English:** Right. And the attention mechanism is that the model understands the relationships between all the words in its context.  
**Translation:** 

**[7214.18s] English:** Right. And that is separate from the parameters themselves.  
**Translation:** 

**[7218.12s] English:** Right. And that is something that you must calculate.  
**Translation:** 

**[7221.58s] English:** Right. How each token, or word in the context, is relatively connected to each other.  
**Translation:** Vocabulary: token: 词汇

**[7228.74s] English:** Right. And I think you can explain KV cache better, Nathan.  
**Translation:** 

**[7231.74s] English:** KV Cache is one of the optimizations.  
**Translation:** Vocabulary: optimizations: 优化措施

**[7233.08s] English:** Yeah. So the attention operator has three core components.  
**Translation:** 

**[7237.16s] English:** It's queries, keys, and values.  
**Translation:** Vocabulary: queries: 查询

**[7239.70s] English:** QKV is the thing that goes into this.  
**Translation:** 

**[7242.66s] English:** You'll look at the equation.  
**Translation:** Vocabulary: equation: 方程式

**[7244.04s] English:** You see that these matrices are multiplied together.  
**Translation:** 

**[7246.62s] English:** These words, "query," "key," and "value" come from information retrieval backgrounds, where the query is the thing you're trying to get the values for.  
**Translation:** Vocabulary: matrices: 矩阵; multiplied: 相乘; retrieval: 检索

**[7253.78s] English:** And you access the keys and values by reweighting.  
**Translation:** 

**[7256.32s] English:** My background is not in information retrieval.  
**Translation:** Vocabulary: reweighting: 重新加权

**[7258.08s] English:** Right.  
**Translation:** 

**[7258.74s] English:** And things like this, it's just fun to have backlinks.  
**Translation:** Vocabulary: backlinks: 反向链接

**[7261.56s] English:** And what effectively happens is that when you're doing these matrix multiplications, you have matrices that are of the size of the context length.  
**Translation:** 

**[7269.82s] English:** So, the number of tokens that you put into the model and the KV cache is effectively some form of compressed representation of all the previous tokens in the model.  
**Translation:** Vocabulary: cache: 缓存; compressed: 压缩; matrix: 矩阵; multiplications: 乘法

**[7279.46s] English:** So, when you're doing this, we talk about autoregressive models.  
**Translation:** 

**[7282.40s] English:** You predict one token at a time.  
**Translation:** Vocabulary: autoregressive: 自回归的

**[7284.20s] English:** You start with whatever your prompt was.  
**Translation:** 

**[7286.36s] English:** You ask a question.  
**Translation:** Vocabulary: prompt: 提示

**[7287.46s] English:** Who was the president?  
**Translation:** 

**[7288.40s] English:** Who was the president in 1825?  
**Translation:** 

**[7289.92s] English:** The model is then going to generate its first token.  
**Translation:** 

**[7292.24s] English:** For each of these tokens, you're doing the same attention operator, where you're multiplying these query, key, and value matrices.  
**Translation:** Vocabulary: multiplying: 相乘

**[7300.32s] English:** But the math is very nice, so that when you're doing this repeatedly with the KV cache and key-value operations, you can keep appending new values to it.  
**Translation:** 

**[7311.24s] English:** So, you keep track of what your previous values you're inferring over in this autoregressive chain.  
**Translation:** Vocabulary: appending: 追加; inferring: 推断

**[7316.40s] English:** You keep it in mind the whole time.  
**Translation:** 

**[7318.40s] English:** And this is a really good way to do it.  
**Translation:** 

**[7320.00s] English:** A crucial thing to manage when serving inference at scale. There are far bigger experts in this,  
**Translation:** 

**[7326.18s] English:** And there are so many levels of detail that you can go into. Essentially, one of the key  
**Translation:** Vocabulary: crucial: 至关重要的; inference: 推断

**[7331.84s] English:** Drawbacks of the attention operator and the transformer is that there is a form of quadratic.  
**Translation:** 

**[7337.90s] English:** Memory cost is in proportion to the context length. So, as you put in longer questions, the memory used increases.  
**Translation:** Vocabulary: drawbacks: 缺点; quadratic: 平方的

**[7345.26s] English:** In order to make that computation, it is going up in the form of a quadratic. You'll hear about it a lot.  
**Translation:** 

**[7350.46s] English:** Of other language model architectures that are like subquadratic or linear attention forms,  
**Translation:** Vocabulary: computation: 计算; linear: 线性的; subquadratic: 次二次的

**[7356.68s] English:** Which is like state-space models. We don't need to go into all these now. And then there's  
**Translation:** 

**[7361.30s] English:** Innovations on attention mechanisms have made this memory usage and the ability to attend over long contexts possible.  
**Translation:** Vocabulary: innovations: 创新

**[7367.50s] English:** Much more accurate and high-performance. And those innovations are going to help you with,  
**Translation:** 

**[7372.22s] English:** I mean, you're highly memory-constrained. They help with memory constraints.  
**Translation:** Vocabulary: constraints: 限制

**[7375.18s] English:** And they're going to help you with memory constraints.  
**Translation:** 

**[7375.26s] English:** So, if you input a book into it, I think Gemini is the model that has the longest context length.  
**Translation:** Vocabulary: gemini: 双子座模型

**[7380.48s] English:** That people are using, Gemini is known for 1 million and now 2 million context length.  
**Translation:** 

**[7384.18s] English:** You put a whole book into Gemini, and sometimes it'll draw facts out of it. It's not perfect.  
**Translation:** 

**[7390.12s] English:** They're getting better. So, there are two things: one, to be able to serve this from memory.  
**Translation:** 

**[7395.58s] English:** Google has magic with their TPU stack, where they can serve really long contexts. And then there's  
**Translation:** 

**[7400.02s] English:** Also, many decisions along the way are needed to actually make long-context performance work. This implies,...  
**Translation:** 

**[7404.58s] English:** Data.  
**Translation:** Vocabulary: implies: 意味着

**[7405.26s] English:** There are subtle changes to these computations in attention, and it changes the architecture.  
**Translation:** 

**[7411.20s] English:** But serving long contexts is extremely memory-constrained, especially when you're making a  
**Translation:** Vocabulary: computations: 计算; subtle: 微妙

**[7416.30s] English:** Lots of predictions. I actually don't know why input and output tokens are more expensive.  
**Translation:** 

**[7421.14s] English:** But I think, essentially, output tokens require more computation because you have to sample.  
**Translation:** 

**[7425.10s] English:** From the model.  
**Translation:** 

**[7425.96s] English:** I can explain that. So, today, if you use a model, like you look at an API, OpenAI charges:  
**Translation:** 

**[7432.38s] English:** Certainly at a certain price per million tokens, right?  
**Translation:** 

**[7434.56s] English:** And that price for input and output tokens is different, right? And the reason is that  
**Translation:** 

**[7440.00s] English:** There is, you know, when you're inputting a query into the model, right? Let's say you have  
**Translation:** 

**[7444.66s] English:** A book, right? That book, you must now calculate the entire KV cache for, right? This key-value...  
**Translation:** Vocabulary: cache: 缓存

**[7449.58s] English:** Cache. And so when you do that, that is a parallel operation. All of the tokens can be processed at once.  
**Translation:** 

**[7455.18s] English:** One time, and therefore you can dramatically reduce how much you're spending, right?  
**Translation:** Vocabulary: dramatically: 大幅度地

**[7459.04s] English:** The flop requirements for generating a token and an input token are identical, right? If I input  
**Translation:** 

**[7464.76s] English:** One token, or if I generate one token, is completely identical. I have to go through  
**Translation:** Vocabulary: token: 代币

**[7467.88s] English:** The model, right? But the difference is that I can do that input, i.e., the pre-fill, i.e., the  
**Translation:** 

**[7473.24s] English:** Prompt simultaneously in a batch nature, right? And therefore, it is all a flop.  
**Translation:** Vocabulary: prompt: 提示

**[7478.80s] English:** I think the pricing model, mostly they use, is for input tokens about one-fourth the price of the  
**Translation:** 

**[7483.82s] English:** Output tokens.  
**Translation:** 

**[7484.24s] English:** Correct. But then, output tokens: the reason why it's so expensive is because I can't do it in.  
**Translation:** 

**[7488.26s] English:** Parallel, right? It's autoregressive. Every time I generate a token, I must not only take into account the previous tokens.  
**Translation:** Vocabulary: autoregressive: 自回归; parallel: 并行

**[7493.22s] English:** Entirely, I must not only read the entire model into memory, right? And activate it, right?  
**Translation:** 

**[7497.88s] English:** Go calculate it to generate the next token. I also have to read the entire KV cache, and I'll generate a  
**Translation:** 

**[7502.36s] English:** Token and I append that KV pair; that one token I generated, and it's for the KV cache. Then I do it.  
**Translation:** 

**[7506.92s] English:** Again, right? And so, therefore, this is a non-parallel operation. And this is one where you  
**Translation:** Vocabulary: append: 添加

**[7512.90s] English:** Have to, you know, in the case of pre-fill or prompt, you pull the whole model in and you,...  
**Translation:** 

**[7517.50s] English:** Calculate 20,000 tokens at once, right? So, these are features that APIs are shipping.  
**Translation:** 

**[7522.18s] English:** Which is like prompt caching or pre-filling, because you can drive prices down and you can make APIs more efficient.  
**Translation:** 

**[7527.86s] English:** Much faster. If you know you're going to keep running a business and you're going to keep  
**Translation:** Vocabulary: caching: 缓存

**[7530.96s] English:** Passing the same initial content to Cloud's API, you can load it into the Anthropic API and  
**Translation:** 

**[7537.32s] English:** Always keep it there. But it's very different from what we're kind of leading to—the reasoning models.  
**Translation:** 

**[7541.48s] English:** Which we talked about, we showed this example earlier and read some of that kind of mumbling stuff.  
**Translation:** 

**[7546.66s] English:** And what happens is that the output context length is so much higher. And I mean, I learned a lot.  
**Translation:** Vocabulary: mumbling: 含糊说话

**[7552.46s] English:** About this from Dylan's work, which is essentially that as the output length gets higher, you're using  
**Translation:** 

**[7556.50s] English:** This: You're writing this quadrangle.  
**Translation:** Vocabulary: quadrangle: 四方形

**[7557.86s] English:** It's quadratic in terms of memory used. And then,...  
**Translation:** 

**[7560.00s] English:** And the GPUs that we have, effectively, you're going to run out of memory, and they're all  
**Translation:** Vocabulary: quadratic: 平方的

**[7565.36s] English:** Trying to serve multiple requests at once.  
**Translation:** 

**[7567.26s] English:** So, they're doing this batch processing where not all of the prompts aren't exactly the same,  
**Translation:** Vocabulary: prompts: 提示

**[7570.54s] English:** Really complex handling.  
**Translation:** 

**[7572.02s] English:** And then, as context links get longer, there's this—I think you'd call it—a critical batch.  
**Translation:** 

**[7576.30s] English:** Size, where your ability to serve more users, so how much you can parallelize your inference.  
**Translation:** 

**[7583.30s] English:** Plummets because of this long context.  
**Translation:** Vocabulary: inference: 推理; plummets: 急剧下降

**[7585.56s] English:** So, your memory usage is going way up with these reasoning models, and you still have...  
**Translation:** 

**[7589.76s] English:** A lot of users.  
**Translation:** 

**[7590.76s] English:** So, effectively, the cost to serve multiplies by a ton.  
**Translation:** 

**[7595.04s] English:** And we're looking at a plot where the x-axis is sequence length.  
**Translation:** Vocabulary: multiplies: 增加

**[7599.86s] English:** I.e., how many tokens are being generated per prompt, right?  
**Translation:** 

**[7603.36s] English:** So, if I put in a book with a million tokens, right?  
**Translation:** Vocabulary: prompt: 提示

**[7605.70s] English:** But if I put "sky is blue" in, then that's like six tokens or so.  
**Translation:** 

**[7609.48s] English:** We should say that, when we're calling it reasoning and chain of thought, we are extending this sequence.  
**Translation:** 

**[7615.24s] English:** Length.  
**Translation:** 

**[7615.52s] English:** It's mostly output tokens.  
**Translation:** 

**[7616.56s] English:** So, before three months ago, when O1 launched.  
**Translation:** 

**[7619.22s] English:** All of the use cases for long context length were like, let me put a ton of documents in.  
**Translation:** 

**[7623.74s] English:** And then get an answer out, right?  
**Translation:** 

**[7625.48s] English:** And it's a single, you know, pre-fill, compute a lot in parallel, and then output a little.  
**Translation:** Vocabulary: compute: 计算; parallel: 并行

**[7630.80s] English:** Bit.  
**Translation:** 

**[7631.26s] English:** Now, with reasoning and agents, this is a very different idea, right?  
**Translation:** 

**[7635.06s] English:** Now, instead, I might just say, "Hey, do this task," or I might have all these documents.  
**Translation:** 

**[7639.20s] English:** But at the end of the day, the model is not just like producing a little bit, right?  
**Translation:** 

**[7642.66s] English:** It's producing tons of information.  
**Translation:** 

**[7644.88s] English:** This chain of thought just continues to go, and go, and go, and go.  
**Translation:** 

**[7648.02s] English:** And so, the sequence.  
**Translation:** 

**[7649.22s] English:** Sequence length is effectively that. If it's generated from 10,000 tokens, it's 10,000.  
**Translation:** 

**[7653.82s] English:** Sequence length, right?  
**Translation:** 

**[7654.96s] English:** Or, and plus whatever you inputted in the prompt.  
**Translation:** Vocabulary: inputted: 输入的

**[7657.38s] English:** And so, what this chart is showing, and it's a logarithmic chart, is:  
**Translation:** 

**[7661.82s] English:** As you go from 1K to 4K or 4K to 16K, the memory requirements grow so fast for your.  
**Translation:** Vocabulary: logarithmic: 对数的

**[7669.56s] English:** KV Cache: That you end up not being able to run a certain number of, you know, your sequence.  
**Translation:** 

**[7675.96s] English:** Length is capped, or the number of users.  
**Translation:** Vocabulary: cache: 缓存

**[7677.52s] English:** Let's say the model.  
**Translation:** 

**[7678.48s] English:** So, this is.  
**Translation:** 

**[7679.22s] English:** Showing for a four.  
**Translation:** 

**[7680.00s] English:** 5B model and batch size 64, Llama 3:145D. Yeah, and batch size is crucial; essentially, they just  
**Translation:** Vocabulary: crucial: 至关重要; llama: llama

**[7687.34s] English:** Like you want to have a higher batch size to parallelize and increase your throughput, 64 different ways.  
**Translation:** 

**[7692.10s] English:** Users can be served at once, right? Yeah, and therefore, your serving costs are lower, right, because the server...  
**Translation:** Vocabulary: throughput: 处理速度

**[7695.52s] English:** Costs the same, right? This is eight H100s, roughly two dollars an hour per GPU, that's sixteen dollars.  
**Translation:** 

**[7700.68s] English:** An hour—right, that is somewhat of a fixed cost. You can do things to make it lower, though.  
**Translation:** 

**[7704.94s] English:** Course, but like it's like sixteen dollars an hour now. How many users can you serve? How many tokens?  
**Translation:** 

**[7709.08s] English:** Can you generate, and then you divide the two, and that's your cost, right? Um, and so with reasoning.  
**Translation:** 

**[7713.70s] English:** Models, this is where a lot of the complexity comes about, and why memory is so.  
**Translation:** 

**[7718.08s] English:** Important because if you have limited amounts of memory, then you can't serve so many users if you  
**Translation:** Vocabulary: complexity: 复杂性

**[7723.16s] English:** Have limited amounts of memory, your serving speeds get lower, right? And so, your costs get a lot, lot higher.  
**Translation:** 

**[7728.00s] English:** Worse, um, because all of a sudden, if I was used to hey, on the sixteen-dollar-an-hour server, I'm  
**Translation:** 

**[7733.08s] English:** Serving Llama 405B, or if I'm serving, you know, DeepSeek V3, um, and it's all chat-style.  
**Translation:** 

**[7738.86s] English:** Applications, and I'm serving—you know, DeepSeek V3, um, and it's all chat-style applications.  
**Translation:** 

**[7739.06s] English:** I.e., we're just chatting. The sequence lengths are a thousand, a few thousand, right? You know, when...  
**Translation:** 

**[7744.56s] English:** You can use the language model, which has a context length of a few thousand tokens most of the time. Sometimes, however, you might encounter limitations.  
**Translation:** Vocabulary: encounter: 遇到

**[7747.14s] English:** Dropping a big document, but then you process it; you get your answer, you throw it away, right?  
**Translation:** 

**[7750.98s] English:** Move on to the next thing, right? Whereas with reasoning, I'm now generating tens of thousands.  
**Translation:** 

**[7755.72s] English:** Of tokens in the sequence, right? And so, this KV cache has to stay resonant, and you  
**Translation:** 

**[7761.58s] English:** You have to keep loading it; you have to keep it in memory constantly, and now this butts out.  
**Translation:** Vocabulary: cache: 内存缓存; resonant: 同步的

**[7766.22s] English:** Other users, right? If there's now a reasoning task, right?  
**Translation:** 

**[7769.06s] English:** And the model is capable of reasoning, then all of a sudden I it that memory pressure means that I  
**Translation:** 

**[7774.58s] English:** Can't serve as many users simultaneously. Let's go into DeepSeek again. So, we're in the post-deep.  
**Translation:** 

**[7779.80s] English:** Seek R1 time; I think, and what we're seeing are two sides to this market, watching how hard it is to.  
**Translation:** 

**[7786.14s] English:** Serve it on one side; we're going to talk about DeepSeek, which now has a chat app.  
**Translation:** 

**[7790.20s] English:** That got to number one on the App Store. Disclaimer: Number one on the App Store is measured by  
**Translation:** 

**[7794.54s] English:** Velocity, so it's not necessarily saying that more people have the DeepSeek app than ChatGPT.  
**Translation:** 

**[7798.84s] English:** App, but it is  
**Translation:** 

**[7800.00s] English:** Still remarkable, Claude has never hit the number one in the App Store, even though everyone in San Francisco is like, "Oh, my God, you've got to use Claude; don't use Strategy BT." So DeepSeek did hit it. They also launched an API product recently where you can ping their API and get these super long responses for R1 out.  
**Translation:** 

**[7814.10s] English:** At the same time as these are out, we'll get to what's happened to them. Because the model weights for DeepSeek R1 are openly available and the license is very friendly—the MIT license being commercially available—all of these midsize companies and big companies are trying to be first to serve R1 to their users.  
**Translation:** Vocabulary: commercially: 商业化; midsize: 中型的; openly: 公开地

**[7833.48s] English:** We were trying to evaluate R1 because we have really similar research going on. We released the model and we're trying to compare it. And out of all the companies that are, "quote unquote," serving R1.  
**Translation:** 

**[7844.10s] English:** And they're doing it at prices that are way higher than the DeepSeek API. Most of them barely work, and the throughput is really low.  
**Translation:** Vocabulary: evaluate: 评估; throughput: 处理速度; unquote: 反引号

**[7851.06s] English:** To give context, right? Everyone, one of the parts of freaking this out was trying to reach the capabilities. The other aspect is that they did it so cheap, right? And the fact that it was so cheap, we kind of talked about on the training side why it was so cheap.  
**Translation:** 

**[7861.86s] English:** Let's talk about why it's so cheap for inference. It works well, and it's cheap. Why is R1 so damn cheap?  
**Translation:** Vocabulary: capabilities: 能力; freaking: 真他媽的; inference: 推理

**[7868.32s] English:** So, I think there are a couple of factors here, right? One is that they do have model architecture innovation.  
**Translation:** 

**[7874.10s] English:** Right. This new MLA attention is different from the attention mechanism in "Attention Is All You Need." Right. Others have already innovated with work like MQA, GQA, local, global, and all these different innovations try to bend the curve. Right. It's still quadratic, but the constant is now smaller. Right.  
**Translation:** Vocabulary: innovated: 创新; innovations: 创新; quadratic: 二次的

**[7893.74s] English:** Related to our previous discussion, this multi-head latent attention can save about 80 to 90 percent in memory compared to the attention mechanism, which helps especially with context.  
**Translation:** 

**[7904.10s] English:** Related to our previous discussion, this multi-head latent attention can save about 80 to 90 percent in memory compared to the attention mechanism, which helps especially with context.  
**Translation:** 

**[7904.60s] English:** It's 80 to 90 percent versus the original, but then versus what people are actually doing—it's still an innovation.  
**Translation:** 

**[7909.60s] English:** This 80 to 90 percent doesn't say that the whole model is 80 to 90 percent cheaper; just one part of it.  
**Translation:** 

**[7914.72s] English:** Well, and not just that, right? Like, other people have implemented techniques like local, global, sliding window, and GQA, MQA.  
**Translation:** 

**[7920.00s] English:** But, anyway, DeepSeq has their attention mechanism as a true architectural innovation.  
**Translation:** Vocabulary: architectural: 建筑性的; implemented: 实现

**[7925.04s] English:** They did tons of experimentation.  
**Translation:** 

**[7926.92s] English:** And this dramatically reduces the memory pressure.  
**Translation:** Vocabulary: dramatically: 显著地; experimentation: 实验

**[7929.96s] English:** It's still there, right?  
**Translation:** 

**[7930.84s] English:** It's still about attention.  
**Translation:** 

**[7932.10s] English:** It's still quadratic.  
**Translation:** 

**[7933.04s] English:** It's just dramatically reduced it relative to prior forms.  
**Translation:** 

**[7936.04s] English:** Yeah, right.  
**Translation:** 

**[7936.32s] English:** That's the memory pressure.  
**Translation:** 

**[7937.74s] English:** I should say, in case people don't know, that R1 is 27 times cheaper than O1.  
**Translation:** 

**[7945.26s] English:** We think that OpenAI had a large margin built in.  
**Translation:** Vocabulary: margin: 利润空间

**[7948.24s] English:** Okay.  
**Translation:** 

**[7948.86s] English:** There are multiple factors.  
**Translation:** 

**[7950.00s] English:** We should break down the factors, I think.  
**Translation:** 

**[7951.46s] English:** It's $2 per million token output for R1, and $60 per million token output for O1.  
**Translation:** Vocabulary: token: 令牌

**[7960.76s] English:** Yeah, let's look at this.  
**Translation:** 

**[7963.14s] English:** So, I think this is very important, right?  
**Translation:** 

**[7965.18s] English:** OpenAI is that drastic gap between DeepSeq and pricing.  
**Translation:** 

**[7970.94s] English:** But DeepSeq is offering the same model, because they opened it up weighted to everyone else for a very similar, much lower price than what others are able to offer.  
**Translation:** Vocabulary: drastic: 巨大的

**[7979.58s] English:** Right?  
**Translation:** 

**[7979.72s] English:** Right.  
**Translation:** 

**[7979.98s] English:** So there are two factors here, right?  
**Translation:** 

**[7981.60s] English:** Their model is cheaper, right?  
**Translation:** 

**[7983.52s] English:** It is 27 times cheaper.  
**Translation:** 

**[7985.18s] English:** I don't remember the number exactly off the top of my head.  
**Translation:** 

**[7986.84s] English:** So, we're looking at a graphic that's showing different places serving V3, DeepSeq V3, which is similar to DeepSeq R1.  
**Translation:** 

**[7997.92s] English:** And there's a vast difference in...  
**Translation:** 

**[8000.68s] English:** In serving costs, right?  
**Translation:** 

**[8001.74s] English:** In serving costs.  
**Translation:** 

**[8002.58s] English:** And what explains that difference?  
**Translation:** 

**[8003.84s] English:** And so part of it is that OpenAI has a fantastic margin, right?  
**Translation:** 

**[8007.24s] English:** They're serving.  
**Translation:** 

**[8008.08s] English:** When they're doing inference, their gross margins are...  
**Translation:** Vocabulary: inference: 推断; margins: 利润

**[8009.98s] English:** North of 75%? Right?  
**Translation:** 

**[8011.46s] English:** So, that's a 4 to 5x factor right there in the cost difference. Is that OpenAI is just making crazy amounts of money, because they're the only one with the capability.  
**Translation:** Vocabulary: capability: 能力

**[8020.12s] English:** Do they need that money?  
**Translation:** 

**[8021.18s] English:** Are they using it for R&D?  
**Translation:** 

**[8022.42s] English:** They're losing money, obviously, as a company, because they spend so much on training, right?  
**Translation:** 

**[8026.04s] English:** So, the inference itself is a very high-margin, but it doesn't recoup the cost of everything else they're doing.  
**Translation:** Vocabulary: recoup: 弥补损失

**[8030.42s] English:** Okay.  
**Translation:** 

**[8030.98s] English:** So, yes, they need that money because the revenue and margins pay for continuing to build the next thing, right?  
**Translation:** 

**[8036.54s] English:** As long as I'm raising more money.  
**Translation:** 

**[8037.80s] English:** So, the suggestion is that DeepSeq is really...  
**Translation:** 

**[8039.98s] English:** Okay.  
**Translation:** 

**[8040.00s] English:** Bleeding out money. Well, so here's one thing, right? We'll get to this in a second, but like...  
**Translation:** 

**[8040.22s] English:** So, the suggestion is that DeepSeq is really...  
**Translation:** 

**[8044.24s] English:** DeepSeek doesn't have any capacity to actually serve the model. They stopped sign-ups.  
**Translation:** 

**[8049.00s] English:** The ability to use it is like non-existent now, right? For most people, because so many people  
**Translation:** 

**[8053.88s] English:** Are trying to use it, they just don't have the GPUs to serve it, right? OpenAI has hundreds of  
**Translation:** 

**[8058.02s] English:** Thousands of GPUs between them and Microsoft to serve their models. DeepSeek has a factor of  
**Translation:** 

**[8062.96s] English:** Much lower, right? Even if you believe our research, which is 50,000 GPUs, and a portion,...  
**Translation:** 

**[8067.70s] English:** Of those, some are for research, a portion of those are for the hedge fund, right? They still have.  
**Translation:** 

**[8070.88s] English:** Nowhere close to the GPU volumes and capacity to serve the model, right? At scale, so it is cheaper.  
**Translation:** 

**[8078.04s] English:** A part of that is OpenAI making a ton of money. Is DeepSeek making money on their API? Unknown.  
**Translation:** 

**[8083.50s] English:** I don't actually think so. And part of that is this chart, right? Look at all the other providers,  
**Translation:** Vocabulary: providers: 提供者

**[8088.20s] English:** Right? Together AI and Fireworks AI are very high-end companies, right? XMeta, Together AI, is  
**Translation:** 

**[8093.36s] English:** TreeDAO and the inventor of Flash Attention, right? It's a huge efficiency technology.  
**Translation:** Vocabulary: inventor: 发明者

**[8097.86s] English:** Right? They're very efficient and good companies. And I do know that they make money.  
**Translation:** 

**[8102.58s] English:** Right? Not tons of money in inference, but they make money. And so they're serving at about a five.  
**Translation:** Vocabulary: inference: 推断

**[8106.50s] English:** To a seven-X difference in cost, right? And so now, when you equate it, okay, OpenAI is making tons of  
**Translation:** 

**[8112.48s] English:** Money, that's like a 5X difference. And the companies that are trying to make money for this.  
**Translation:** Vocabulary: equate: 换算

**[8115.94s] English:** Model is like a five-X difference. There is still a gap, right? There's still a gap. And that is  
**Translation:** 

**[8119.62s] English:** Just DeepSeek being really freaking good, right? The model architecture, MLA, the way they did it,  
**Translation:** Vocabulary: freaking: 极好的

**[8124.10s] English:** The MOE, all these things, there is a legitimate, just efficiency difference.  
**Translation:** 

**[8127.86s] English:** All their low-level libraries that we talked about in training, some of them probably translate to  
**Translation:** Vocabulary: legitimate: 正当的

**[8131.74s] English:** Inference and those weren't released. So, we may go a bit into conspiracy.  
**Translation:** 

**[8135.56s] English:** But is it possible that the Chinese government is subsidizing DeepSeek?  
**Translation:** Vocabulary: conspiracy: 阴谋论; subsidizing: 补贴

**[8140.48s] English:** I actually don't think they are. I think when you look at the Chinese labs, there's Huawei has a  
**Translation:** 

**[8147.04s] English:** Lab, Moonshot AI, there's a couple of other labs out there that are really close with the government.  
**Translation:** Vocabulary: moonshot: 宏图大计

**[8151.90s] English:** And then there are labs like Alibaba and DeepSeek, which are not closely aligned with the government.  
**Translation:** 

**[8156.02s] English:** Mm-hmm.  
**Translation:** Vocabulary: aligned: 吻合

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

**[8160.00s] English:** Reverent figure, who's quite different and has very different viewpoints, based on the  
**Translation:** 

**[8165.56s] English:** Chinese interviews that are translated may not reflect exactly what the CCP might want.  
**Translation:** Vocabulary: reverent: 尊敬的; viewpoints: 观点

**[8169.92s] English:** Now, to be clear: Does he have a loss leader because he can fund it through his hedge fund?  
**Translation:** 

**[8173.76s] English:** Yeah, sure.  
**Translation:** 

**[8174.38s] English:** So, the hedge fund might be subsidizing it.  
**Translation:** 

**[8176.56s] English:** Yes. I mean, they absolutely did, right? Because DeepSeek has not raised much money. They're now  
**Translation:** 

**[8179.86s] English:** Trying to raise funds in China, but they have not historically raised money. It's all just been  
**Translation:** 

**[8184.60s] English:** Funded by the hedge fund. And he owns about half the company, like 50-60%.  
**Translation:** 

**[8188.54s] English:** Is owned by him.  
**Translation:** 

**[8189.18s] English:** Some of the interviews include discussions on how doing this can be used as a recruiting tool. You see,  
**Translation:** Vocabulary: recruiting: 招聘

**[8192.86s] English:** This is true for American companies too. It's like having GPUs, a recruiting tool, and being at the cutting-edge.  
**Translation:** 

**[8197.90s] English:** Edge of AI, recruiting tool.  
**Translation:** 

**[8199.72s] English:** Open Sourcing.  
**Translation:** 

**[8200.30s] English:** Open-sourcing, recruiting tool.  
**Translation:** Vocabulary: sourcing: 采购

**[8201.80s] English:** So much talent. They were so far behind, and they got so much talent because they just opened source.  
**Translation:** 

**[8205.48s] English:** Stuff.  
**Translation:** 

**[8206.34s] English:** More conspiracy theories. Is it possible that, since they're a hedge fund, they timed everything?  
**Translation:** 

**[8212.26s] English:** With this release and the pricing, they shorted NVIDIA stock and stockpiled?  
**Translation:** Vocabulary: stockpiled: 囤积股票

**[8219.18s] English:** It's like a block of USA ad companies, and they released it with Stargate; like, just perfect timing to be.  
**Translation:** 

**[8226.34s] English:** Able to make money.  
**Translation:** Vocabulary: stargate: 星际之门; timing: 时机

**[8227.98s] English:** Like they released it on Inauguration Day. They know the international community, what is on the  
**Translation:** 

**[8232.92s] English:** International calendar, but I mean, I don't expect them to. If you listen to their motivations for  
**Translation:** Vocabulary: inauguration: 就职; motivations: 动机

**[8237.46s] English:** AI, it's like.  
**Translation:** 

**[8238.54s] English:** No, if you release, they released V3 on December 26th. Like who sets the release date?  
**Translation:** 

**[8243.36s] English:** No one looks right. They released the papers before this, right? The V3 paper and the R1 paper.  
**Translation:** 

**[8248.48s] English:** So, people,  
**Translation:** 

**[8249.10s] English:** I have been looking at it and been like, "Wow," um, and then they just released the R1 model, I think.  
**Translation:** 

**[8253.48s] English:** They're just shipping as fast as they can, and like, who cares about Christmas? Who cares about...  
**Translation:** Vocabulary: christmas: 圣诞节

**[8257.10s] English:** You know, get it out before Chinese New Year, right? Obviously, which just happened. I don't think...  
**Translation:** 

**[8261.10s] English:** They actually were like timing the market or trying to make the biggest splash possible.  
**Translation:** 

**[8265.22s] English:** I think they're just like shipping, and I think that's one of their big advantages. We know that a lot.  
**Translation:** 

**[8269.72s] English:** Of the American companies, many are very invested in safety, and that is the central culture of a place.  
**Translation:** 

**[8275.06s] English:** Like Anthropic, and I think Anthropic sounds like a wonderful place to work, but if Safe...  
**Translation:** 

**[8280.00s] English:** Safety is your number-one goal; it takes way longer to get artifacts out. That's why Anthropic.  
**Translation:** Vocabulary: artifacts: 产物

**[8285.18s] English:** Is not open sourcing things. That's their claim. But there are internal reviews. Anthropic.  
**Translation:** 

**[8290.62s] English:** Mentions things to international governments. There's been news of how Anthropic has done.  
**Translation:** Vocabulary: sourcing: 采购

**[8295.58s] English:** Pre-release testing with the UK AI Safety Institute. All of these things add inertia.  
**Translation:** 

**[8299.82s] English:** To the process of getting things out, and we're on this trend line where the progress is very high.  
**Translation:** Vocabulary: inertia: 阻力

**[8304.56s] English:** So, if you reduce the time from when your model is done training to running evaluations, that's good.  
**Translation:** 

**[8308.98s] English:** You want to get it out as soon as possible to maximize the perceived quality of your outputs.  
**Translation:** Vocabulary: evaluations: 评估; maximize: 最大化; outputs: 输出; perceived: 感知的

**[8315.52s] English:** DeepSeat does this so well. Dario explicitly said that Claude 3.5 Sonnet was trained for nine months or  
**Translation:** 

**[8321.26s] English:** Nine to ten months ago, and I think it took them another handful of months to release it. So it's  
**Translation:** Vocabulary: explicitly: 明确地; sonnet: 十四行诗

**[8326.64s] English:** Like there is a significant gap here, and especially with reasoning models, the word in the  
**Translation:** 

**[8332.60s] English:** San Francisco street: "Anthropic has a better model than O3, and they won't release it.  
**Translation:** 

**[8337.88s] English:** Why? Because...  
**Translation:** 

**[8338.98s] English:** Chains of thought are scary, right? And they are legitimately scary, right? If you look at R1,  
**Translation:** Vocabulary: legitimately: 确实地

**[8343.58s] English:** It flips back and forth between Chinese and English. Sometimes it's gibberish, and then  
**Translation:** 

**[8347.56s] English:** The right answer comes out, right? And for you and me, it's like, great.  
**Translation:** Vocabulary: gibberish: 乱七八糟的言语

**[8351.20s] English:** Great. I mean, like, people are infatuated with you. You're telling me this is a high-value thing.  
**Translation:** 

**[8355.80s] English:** And it works and it's doing this. It's amazing. I mean, you talked about that sort of like a chain.  
**Translation:** Vocabulary: infatuated: 狂热喜爱

**[8361.22s] English:** Of thought for that philosophical thing, which is not something they were trained to be philosophically.  
**Translation:** 

**[8364.88s] English:** Good. It's just sort of an artifact of the chain-of-thought training it did. But, like,  
**Translation:** Vocabulary: artifact: 产物; philosophical: 哲学的; philosophically: 哲学地

**[8368.86s] English:** That's...  
**Translation:** 

**[8368.96s] English:** That's super important. Like, can I inspect your mind and what you're thinking right now?  
**Translation:** Vocabulary: inspect: 检查

**[8374.04s] English:** Now, no. And so I don't know if you're lying to my face. Chain-of-thought models are that way,  
**Translation:** 

**[8378.74s] English:** Right? Like, this is a true "quote-unquote" risk between a chat application where, hey, I asked,...  
**Translation:** 

**[8383.98s] English:** The model should not be used to say bad words or whatever, or how to make anthrax. And it tells me that's unsafe.  
**Translation:** 

**[8389.50s] English:** Sure. But that's something I can get out relatively easily. What if I tell the AI to do a task and...  
**Translation:** Vocabulary: anthrax: 炭疽; unsafe: 不安全

**[8395.12s] English:** Then it does the task all of a sudden randomly in a way that I don't want it, right? And now that...  
**Translation:** 

**[8398.94s] English:** Has like much more...  
**Translation:** 

**[8400.00s] English:** Task versus a like response is very different, right? So, the bar for safety is much higher.  
**Translation:** 

**[8403.94s] English:** At least, this is Anthropic's case, right? Like for DeepSeek, they're like "ship," right? Yeah, so I mean.  
**Translation:** 

**[8409.78s] English:** The bar for safety is probably lowered a bit because of DeepSeek. I mean, there are parallels.  
**Translation:** 

**[8414.60s] English:** Here, to the space race, the reason the Soviets probably put a man in space first is because  
**Translation:** Vocabulary: lowered: 降低

**[8420.54s] English:** Their approach to safety was uh the bar for safety was lower, and they they killed that dog right.  
**Translation:** 

**[8427.64s] English:** All of these things, right? So it's like a less risk-averse approach than the U.S. space program.  
**Translation:** 

**[8433.34s] English:** And there are parallels here, but you know, there's probably going to be downward pressure on that.  
**Translation:** 

**[8438.34s] English:** Safety bar for U.S. companies, right? This is something that Dario talks about: it's like that's  
**Translation:** 

**[8443.14s] English:** The situation that Dario wants to avoid is what Dario talks about—the difference between "race to the  
**Translation:** 

**[8449.18s] English:** Bottom, and race to the top, and the race to the top is where there's a very high standard on safety.  
**Translation:** 

**[8453.24s] English:** There's a very high standard on your model forms, and certain about crucial evaluations and...  
**Translation:** 

**[8457.64s] English:** When certain companies are really good to it, they will converge. This is the idea.  
**Translation:** Vocabulary: converge: 汇聚; crucial: 关键的; evaluations: 评估

**[8461.86s] English:** Ultimately, AI is not confined to one nationality or one set of morals about what it should.  
**Translation:** 

**[8471.24s] English:** Mean, and there are a lot of arguments about whether we should stop open-sourcing models, and if the U.S. stops.  
**Translation:** Vocabulary: confined: 局限于; morals: 道德

**[8477.58s] English:** It's pretty clear, I mean, it's way easier to see now at DeepSeek that a different international...  
**Translation:** 

**[8482.74s] English:** The body will be the one that builds it. They we talk about the cost of training deep learning models as this.  
**Translation:** 

**[8487.64s] English:** Shocking, $5 million! Think about how many entities in the world can afford a hundred.  
**Translation:** 

**[8491.76s] English:** Times, to have the best open-source model that people use in the world, and it's like it's  
**Translation:** 

**[8498.24s] English:** A scary reality is that these open models are probably going to keep coming for the time.  
**Translation:** 

**[8503.18s] English:** Being whether or not we want to stop them, and it is like stopping them might make it even worse.  
**Translation:** 

**[8508.50s] English:** Harder to prepare, but it just means that the preparation and understanding what AI can do.  
**Translation:** 

**[8513.00s] English:** Is just so much more important, that's why I'm here. The  
**Translation:** 

**[8517.64s] English:** At the end of the day, but it's like a budding thing.  
**Translation:** 

**[8520.00s] English:** Into people, especially not in AI, is that like this is coming, there are some structural things.  
**Translation:** Vocabulary: budding: 初露头角

**[8525.44s] English:** In a global, interconnected world, you have to accept, yeah. You mentioned that you sent me something.  
**Translation:** 

**[8532.00s] English:** That Zuck (Mark Zuckerberg) mentioned on the earnings call that he said, "I think, in light of,  
**Translation:** Vocabulary: earnings: 财报; interconnected: 互联互通

**[8536.96s] English:** Some of the recent news is about the new competitor, DeepSeek from China. I think it's one of the things.  
**Translation:** 

**[8541.60s] English:** That we're talking about is that there's going to be an open-source standard globally, and I think for  
**Translation:** Vocabulary: globally: 全世界地

**[8546.16s] English:** Our kind of national advantage is important; it's an American standard.  
**Translation:** 

**[8550.32s] English:** So, we take that seriously. We want to build the AI system that people around the world are using.  
**Translation:** 

**[8555.20s] English:** And I think that, if anything, some of the recent news has only strengthened our conviction.  
**Translation:** 

**[8559.68s] English:** That's the right thing to focus on, so yes, open sourcing. Yeah, Mark Zuckerberg is not.  
**Translation:** Vocabulary: sourcing: 采购; strengthened: 加强

**[8564.16s] English:** New to having American values and how he presents his company's trajectory, I think their products,...  
**Translation:** 

**[8570.88s] English:** Have long since been banned in China, and I respect the saying directly, and there's  
**Translation:** Vocabulary: trajectory: 发展趋势

**[8575.60s] English:** An interesting  
**Translation:** 

**[8576.16s] English:** An aspect of just because it's open, weights, or open source, doesn't mean it can't be subverted, right?  
**Translation:** Vocabulary: subverted: 被颠覆

**[8582.08s] English:** There have been many open-source software bugs that have been, for example, you know.  
**Translation:** 

**[8586.96s] English:** There was a Linux bug that was found after about 10 years, which was clearly a backdoor, because somebody  
**Translation:** Vocabulary: backdoor: 后门

**[8592.16s] English:** Was like, "Why is this taking, you know, half a second? The recent one, right? Like, there's...  
**Translation:** 

**[8596.08s] English:** Is this taking half a second to load? And it was like, oh crap, there's a back door here—that's why.  
**Translation:** 

**[8600.00s] English:** Right, and it's like this is very much possible with AI models, right? Um, today, you know, the  
**Translation:** 

**[8606.16s] English:** The alignment of these models is very clear, right? Like, I'm not gonna say you know bad words, I'm not gonna  
**Translation:** Vocabulary: alignment: 对齐

**[8612.08s] English:** Teach you how to make anthrax? I'm not gonna talk about Tiananmen Square, uh, I'm not gonna, you know.  
**Translation:** 

**[8616.40s] English:** You know, things like I'm gonna say Taiwan is part of, you know, it's just in the eastern province, right?  
**Translation:** Vocabulary: taiwan: 台湾; tiananmen: 天安门广场

**[8621.52s] English:** Like, you know, all these things are kind of depending on who you are, what you align with, and what you know.  
**Translation:** 

**[8626.32s] English:** You know, even like XAI is aligned a certain way, right? You know, there they might be it's not aligned.  
**Translation:** Vocabulary: align: 一致; aligned: 对齐

**[8631.60s] English:** In the "woke" sense, it's not aligned with the pro-China sense, but there are certain things.  
**Translation:** 

**[8635.60s] English:** That are imbued within the model now, when you release this publicly in an instruct model.  
**Translation:** Vocabulary: imbued: 渗透; instruct: 指导

**[8639.52s] English:** That's open.  
**Translation:** 

**[8640.00s] English:** And weights can then proliferate, right? But as these systems get more and more capable,...  
**Translation:** Vocabulary: proliferate: 迅速增加

**[8644.58s] English:** What you can embed deep down in the model is not as clear, right? And so they're asked that is  
**Translation:** 

**[8650.90s] English:** Like one of the big fears is that if an American model or a Chinese model is the top model, right?  
**Translation:** Vocabulary: embed: 植入

**[8656.50s] English:** You're going to embed things that are unclear, and it can be unintentional, too, right? Like British.  
**Translation:** 

**[8660.66s] English:** English is dead because American LLMs won, and the Internet is American, and therefore like.  
**Translation:** Vocabulary: unintentional: 无意的

**[8665.82s] English:** Color is spelled the way Americans spell it, right? And this is just strong words, right now.  
**Translation:** 

**[8670.04s] English:** This is just like the factual nature of LLMs—the right way to carve it with each one.  
**Translation:** 

**[8674.84s] English:** The English is the hottest programming language, and that's defined by a bunch of companies.  
**Translation:** 

**[8679.36s] English:** That primarily are in San Francisco, the right way to spell "optimization" is with a "z," just in case.  
**Translation:** Vocabulary: optimization: 最优化

**[8685.68s] English:** It's an "I," I think. In British English, it is taking it as something silly, right?  
**Translation:** 

**[8691.90s] English:** Something as silly as the spelling, like which British or English, you know, Brits and and  
**Translation:** Vocabulary: brits: 英国人

**[8695.70s] English:** And, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and, and.  
**Translation:** 

**[8695.80s] English:** And Americans will likely like to laugh about it, probably. I don't think we care that much, though. But like,...  
**Translation:** 

**[8700.32s] English:** You know, some people will, but this can boil down to like very  
**Translation:** 

**[8704.14s] English:** Very important topics, like, hey, you know, so you know, subverting people, right? Uh, you know, chat.  
**Translation:** Vocabulary: subverting: 颠覆

**[8710.76s] English:** Bots, right? Character AI has shown that they can, you know, talk to kids and/or adults, and like.  
**Translation:** 

**[8716.60s] English:** It will make you feel a certain way, right? And that's unintentional alignment, but like, what?  
**Translation:** Vocabulary: alignment: 一致

**[8722.00s] English:** Happens when there's intentional alignment deep down on the open-source standard; it's a  
**Translation:** 

**[8725.68s] English:** Backdoor today for Linux, right? That's what we discovered, or some encryption system, right? China.  
**Translation:** Vocabulary: backdoor: 后门; encryption: 加密; intentional: 故意的

**[8730.70s] English:** Uses different encryption than NIST defines for the U.S., because there's clearly at least they think.  
**Translation:** 

**[8735.10s] English:** There's backdoors in it, right? Um, what happens when the models have backdoors, not just to computers?  
**Translation:** Vocabulary: backdoors: 后门

**[8740.52s] English:** Systems, but to our minds, yeah, they're cultural barriers. The thing that amplifies their relevance.  
**Translation:** 

**[8746.44s] English:** Of culture with language models is that we are used to this mode of interacting with people in.  
**Translation:** Vocabulary: amplifies: 增强; barriers: 障碍; interacting: 互动; relevance: 相关性

**[8753.56s] English:** Back and forth, the conversation continued.  
**Translation:** 

**[8755.68s] English:** Now we have a super, very powerful computer system that slots into  
**Translation:** 

**[8760.00s] English:** In a social context they were used to, which makes people very uncertain. We don't know the extent to which.  
**Translation:** 

**[8767.00s] English:** People can be impacted by that, so there could be this as an actual concern.  
**Translation:** 

**[8773.06s] English:** With a Chinese company that is providing open-weight models, there could be some secrets.  
**Translation:** 

**[8780.00s] English:** The Chinese government requires these models to have a certain kind of backdoor.  
**Translation:** 

**[8786.90s] English:** Some kind of thing; I don't necessarily think it'll be a backdoor, right? Because once it's open,...  
**Translation:** 

**[8790.96s] English:** Weights it doesn't like to phone home; it's more about whether it recognizes a certain system.  
**Translation:** 

**[8795.86s] English:** It could, like, if now, now it could be a backdoor in the sense that, hey, if you're building a  
**Translation:** 

**[8800.18s] English:** Software, uh, you know, something in software all of a sudden it's a software agent, oh, program, this.  
**Translation:** 

**[8805.34s] English:** Backdoor that only we know about, or it could be like subvert the mind to think that, like XYZ.  
**Translation:** 

**[8810.12s] English:** Opinion is the correct one, as anthropic has researched this, where they show that if you put different  
**Translation:** Vocabulary: backdoor: 后门; researched: 研究过; subvert: 颠覆

**[8815.36s] English:** Phrases certain phrases in  
**Translation:** 

**[8816.84s] English:** At pre-training, you can then elicit different behavior when you're actually using the model.  
**Translation:** Vocabulary: elicit: 引出

**[8821.96s] English:** Because they've poisoned the pre-training data, I don't think—as of now—I don't think.  
**Translation:** 

**[8827.22s] English:** Anybody in a production system is trying to do anything like this, I think it's mostly  
**Translation:** Vocabulary: poisoned: 污染了

**[8831.86s] English:** Anthropic is doing very direct work and mostly just subtle things; we don't know what these are.  
**Translation:** 

**[8837.90s] English:** Models are going to generate tokens based on what information they're given.  
**Translation:** Vocabulary: subtle: 微妙

**[8842.26s] English:** Going to represent, and what the complex representations they have are: well, one of  
**Translation:** 

**[8846.56s] English:** The  
**Translation:** 

**[8846.84s] English:** We're talking about Anthropic, which is generally just permeated with good humans trying to.  
**Translation:** 

**[8853.40s] English:** Do good in the world; I don't, we just don't know of any labs where this would be done in the military.  
**Translation:** Vocabulary: permeated: 充满

**[8859.68s] English:** Context that are explicitly trained to, okay? How can we make the front door look like a happy NL?  
**Translation:** 

**[8869.34s] English:** I'm but underneath it's a thing that will, over time, do the maximum amount of damage to the  
**Translation:** Vocabulary: underneath: 在下面

**[8876.84s] English:** Weapons to our so-called enemies: there's this very good quote from.  
**Translation:** 

**[8880.00s] English:** Emal mentioned who you know, he can be a hype beast sometimes, but one of the things he said, and I  
**Translation:** 

**[8884.64s] English:** I think I agree: that superhuman persuasion will happen before superhuman intelligence, yeah.  
**Translation:** 

**[8890.20s] English:** And if that's the case, then these things before we get this AGI/ASI stuff, we can embed...  
**Translation:** Vocabulary: embed: 植入; persuasion: 说服力

**[8896.08s] English:** Superhuman persuasion toward our ideal, or whatever the ideal of the model maker is, right? And again,  
**Translation:** 

**[8901.44s] English:** Like today, I truly don't believe DeepSeek has done this right; it is a sign of something, though.  
**Translation:** 

**[8906.02s] English:** What could happen, so one of the dystopian worlds is described by "Brave New World"? So we could  
**Translation:** 

**[8911.98s] English:** Just be stuck scrolling Instagram, looking at cute puppies, or worse, and then talking to bots that are  
**Translation:** 

**[8919.52s] English:** Giving us a narrative, and we completely get lost in that world that's controlled by somebody else.  
**Translation:** 

**[8924.28s] English:** But versus thinking independently, and that's a major concern as we rely more.  
**Translation:** Vocabulary: independently: 独立思考

**[8930.00s] English:** And more on these kinds of systems; I mean, we've already seen this with recommendation systems.  
**Translation:** 

**[8933.86s] English:** Yeah, recommendation systems hack the  
**Translation:** 

**[8935.88s] English:** The  
**Translation:** 

**[8936.02s] English:** Dopamine-induced reward circuit, but the brain is a lot more complicated, and what other factors come into play?  
**Translation:** 

**[8940.14s] English:** Sort of circuits, quote-unquote, feedback loops in your brain—can you hack/slash?  
**Translation:** 

**[8943.78s] English:** Subvert in ways like recommendation systems, which are purely just trying to increase time.  
**Translation:** Vocabulary: circuits: 电路; recommendation: 推荐系统; subvert: 颠覆

**[8949.86s] English:** And ads, and etc., but there are so many more goals that can be achieved through these complicated methods.  
**Translation:** 

**[8955.00s] English:** Models: There's no reason, in some number of years, that you can't train a language model to maximize.  
**Translation:** Vocabulary: maximize: 使最大化

**[8960.22s] English:** Time spent on a chat app, like right now—they are trained, I mean—is that not what characterizes it?  
**Translation:** 

**[8965.84s] English:** A, I have done their time, per session is like two hours, yeah. Character? I'm probably very likely could.  
**Translation:** 

**[8971.24s] English:** Be optimizing this, where it's like the way that this data is collected is naive, or it's like:  
**Translation:** 

**[8975.18s] English:** You're presented with a few options and you choose them, but that's not the only way that.  
**Translation:** Vocabulary: naive: 幼稚; optimizing: 优化

**[8979.30s] English:** These models are going to be trained; it's naive stuff like talking to an anime girl, but like it can  
**Translation:** 

**[8982.92s] English:** Be like, yeah, this is a risk, right? Like, it's kind of a cliché thing to say, but I've uh, over  
**Translation:** Vocabulary: anime: 动画

**[8989.86s] English:** The past year had a few stretches of time where I didn't use social media or the internet at all.  
**Translation:** 

**[8995.84s] English:** And just read books and was out in nature, and it clearly has a  
**Translation:** 

**[9000.00s] English:** An effect on the mind, where it felt like I was changing. Of course, I was.  
**Translation:** 

**[9005.84s] English:** Raised before the Internet really took off, but I'm returning to someone.  
**Translation:** 

**[9010.12s] English:** I know where you're going. I mean, you can see it physiologically; like, I take three days if I'm  
**Translation:** 

**[9015.96s] English:** Like backpacking or something, and you're literally breaking down addiction.  
**Translation:** Vocabulary: addiction: 成瘾; backpacking: 背包旅行; physiologically: 生理上

**[9021.78s] English:** Cycles, I feel like I'm more in control of my mind. There feels like a sovereignty of intelligence.  
**Translation:** 

**[9028.02s] English:** That's happening when I'm disconnected from the Internet, I think. The more I use the internet,...  
**Translation:** Vocabulary: disconnected: 不连接; sovereignty: 主权

**[9033.58s] English:** And on social media, the more other people are controlling my mind, there's definitely a feeling.  
**Translation:** 

**[9037.64s] English:** And then, in the future, that would be either algorithms or other people presented.  
**Translation:** 

**[9043.30s] English:** To me, via algorithms, there: I mean, there are already tons of AI bots on the internet, and  
**Translation:** 

**[9048.42s] English:** Every so right now, it's not frequent, but every so often I have replied to one, and they're instantly.  
**Translation:** Vocabulary: instantly: 立刻

**[9052.96s] English:** Replied: "I'm like crap. I was a bot, and that is just going to become more common. Like they're  
**Translation:** 

**[9057.94s] English:** Going to be more common, and I'm going to be more common.  
**Translation:** 

**[9058.00s] English:** Gonna get a good one: One of the hilarious things about technology over its history is that the illicit  
**Translation:** 

**[9063.88s] English:** The adult entertainment industry has always adopted technologies first, right? Whether it was video,...  
**Translation:** Vocabulary: hilarious: 滑稽; illicit: 非法

**[9069.10s] English:** Streaming, yeah, um, to like where you know, the there's now the like sort of like independent...  
**Translation:** 

**[9073.96s] English:** Adult illicit content creators, who have their own subscription pages, and there they actually  
**Translation:** 

**[9079.32s] English:** Heavily utilizing, you know, generative AI has already been like diffusion models and all that.  
**Translation:** 

**[9083.04s] English:** Is huge there, but now, these subscription-based individual creators do use.  
**Translation:** Vocabulary: diffusion: 扩散模型; generative: 生成; utilizing: 利用

**[9088.16s] English:** Bots to approximate themselves and chat with their users; people pay a lot for it, and people pay a lot for similar services.  
**Translation:** 

**[9093.70s] English:** It's often them, but a lot of agencies do this for these.  
**Translation:** Vocabulary: approximate: 近似

**[9098.04s] English:** Creators and do it like on a large scale, so the largest creators are able to talk to  
**Translation:** 

**[9104.18s] English:** Hundreds or thousands of likes at a time, because of these bots, and so it's already  
**Translation:** 

**[9110.18s] English:** Being used there, obviously, you know, like video streaming.  
**Translation:** 

**[9113.04s] English:** And other technologies have gone there first, so it's going to come to the rest of society too.  
**Translation:** 

**[9117.04s] English:** There's a general concern that models  
**Translation:** 

**[9120.00s] English:** Get censored by the companies that deploy them, so one case when we've seen that, and maybe censorship.  
**Translation:** Vocabulary: censored: 被删改的内容; censorship: 审查制度; deploy: 部署

**[9126.78s] English:** Is one word alignment, perhaps via RLHF or some other way, another word? So that we saw that.  
**Translation:** 

**[9135.52s] English:** With a black Nazi image generation, using Gemini, as you mentioned, we also see that,  
**Translation:** Vocabulary: alignment: 对齐; gemini: Gemini模型

**[9143.64s] English:** Chinese models refusing to answer what happened on June 4th, 1989, at Tiananmen Square. So, how?  
**Translation:** 

**[9151.68s] English:** Can this be avoided, and maybe you could just in general talk about how this happens and how it can be prevented?  
**Translation:** Vocabulary: tiananmen: 天安门广场事件

**[9157.82s] English:** It should be avoided to give multiple examples. There are probably a few things to keep in mind here.  
**Translation:** 

**[9166.04s] English:** One is the kind of Tian'anmen Square factual knowledge, like did you think, like how does that work?  
**Translation:** 

**[9172.30s] English:** Get embedded into the model.  
**Translation:** 

**[9173.64s] English:** Two is the Gemini, what you called the "Black Nazi" incident, which is when Gemini as a system  
**Translation:** 

**[9181.30s] English:** Had this extra thing put into it that dramatically changed the behavior.  
**Translation:** 

**[9184.90s] English:** And then, three is what most people would call general alignment RLHF post-training.  
**Translation:** Vocabulary: dramatically: 大幅度地

**[9190.60s] English:** Each of these has a very different scope and how they are applied. In order to do this, if you're just  
**Translation:** 

**[9196.90s] English:** Look at the model weights in order to audit specific facts is extremely hard because you  
**Translation:** 

**[9203.06s] English:** Have to Chrome.  
**Translation:** 

**[9203.62s] English:** Through the pre-training data, we need to look at all this, and then that's terabytes of files to examine.  
**Translation:** Vocabulary: terabytes: 千兆字节

**[9209.76s] English:** For very specific words or hints of those words, so I guess one way to say it is that you can insert  
**Translation:** 

**[9215.06s] English:** Censorship or alignment at various stages in the pipeline, and what you refer to now is at the very  
**Translation:** Vocabulary: censorship: 审查; insert: 插入; pipeline: 管道

**[9220.46s] English:** Beginning of the data, so if you want to get rid of facts in a model, you have to do it at every  
**Translation:** 

**[9225.82s] English:** Stage, you have to do it at the pre-training. So, most people think that pre-training is where  
**Translation:** 

**[9229.52s] English:** Most of the knowledge is put into the model, and then you can  
**Translation:** 

**[9233.62s] English:** And move that in different ways, whether through post-training or through systems.  
**Translation:** 

**[9237.88s] English:** Afterwards, this is where the whole thing like  
**Translation:** 

**[9240.00s] English:** Models come from the right; GPT will not tell you how to make anthrax, but if you try really hard, it might give you some unintended hints.  
**Translation:** Vocabulary: anthrax: 炭疽; unintended: 无意的

**[9245.10s] English:** Really hard; you can eventually get to tell you about anthrax, because they didn't filter it from.  
**Translation:** 

**[9249.66s] English:** The pre-training data set, right? But by the way, removing facts has such an ominously dark feel to it.  
**Translation:** Vocabulary: ominously: 阴森森地

**[9258.12s] English:** Almost, I think it's practically impossible because you effectively have to remove them from the  
**Translation:** 

**[9261.76s] English:** Internet, you're taking on a lot. Did they remove the thing from the subreddits?  
**Translation:** Vocabulary: subreddits: 小红书板块

**[9268.44s] English:** The Mmm, it gets filtered out, right? So, that's quality filters, which are small language models.  
**Translation:** 

**[9273.74s] English:** That looks at a document and tells you, for example, how good the text is and whether it's close to Wikipedia.  
**Translation:** Vocabulary: filtered: 过滤掉

**[9278.34s] English:** An article, which is a good thing that we want language models to be able to imitate, so couldn't.  
**Translation:** 

**[9282.94s] English:** You could do a small language model that filters out mentions of Tiananmen Square in the data, yes, but  
**Translation:** Vocabulary: imitate: 模仿; tiananmen: 天安门

**[9287.66s] English:** Is it going to catch wordplay or encoded language? I mean, people have been messing on.  
**Translation:** 

**[9292.72s] English:** Like games and other stuff, how to say things that don't say Tiananmen Square, um, but or.  
**Translation:** Vocabulary: encoded: 编码; messing: 胡闹; wordplay: 文字游戏

**[9298.36s] English:** Like  
**Translation:** 

**[9298.42s] English:** Yeah, so there are always different ways to do it. The internet, as a whole, does tend...  
**Translation:** 

**[9303.62s] English:** To just have a slight left bias, right? Because it's always been richer, more affluent, and younger.  
**Translation:** 

**[9310.04s] English:** People on the Internet, relative to the rest of the population, so there is already inherently a  
**Translation:** Vocabulary: affluent: 富裕; slight: 轻微

**[9315.00s] English:** Slight left bias on the Internet, and so, how do you filter things that are this complicated?  
**Translation:** 

**[9319.62s] English:** Right, it's like, and some of these can be, you know, factual or non-factual, but like Tiananmen.  
**Translation:** 

**[9324.50s] English:** Square is obviously the example of a fact, but it gets a lot harder when you're talking about.  
**Translation:** 

**[9327.92s] English:** Aligning to an ideal right, um, which is, yeah. And, for example, Elon has tried really hard.  
**Translation:** Vocabulary: aligning: 对齐

**[9335.46s] English:** To make the model not too PC and woke, but the best way to do pre-training is to throw the  
**Translation:** 

**[9341.76s] English:** The whole freaking Internet was at it, right? And then later, figure out, but then at the end of the day,  
**Translation:** Vocabulary: freaking: 该死的

**[9345.10s] English:** The model, at its core, now still has some of these ideals right. You still ingested Reddit/r,  
**Translation:** 

**[9350.08s] English:** Slash Politics, which is probably the largest political discussion board on the world, that's  
**Translation:** Vocabulary: ingested: 吸收

**[9353.54s] English:** Freely available to scrape, and guess what—that's left-leaning, right? Um, and so, um,...  
**Translation:** 

**[9357.92s] English:** You know, there are some aspects like  
**Translation:** Vocabulary: scrape: 抓取

**[9360.00s] English:** That is something you just can't censor unless you try really, really, really, really hard.  
**Translation:** 

**[9364.62s] English:** So, the base model will always have some TDS (trauma derangement syndrome) because it's trained so much.  
**Translation:** Vocabulary: censor: 审查; trauma: 创伤

**[9371.20s] English:** It will have the ability to express it, but what if there's a wide range of representation in the  
**Translation:** 

**[9377.78s] English:** Data: This is what happens; it's like a lot of modern, what is called "post-training," it's a series.  
**Translation:** 

**[9382.74s] English:** Of techniques to get the model on rails for a really specific behavior, uh, and I mean, it's:  
**Translation:** 

**[9388.84s] English:** Like, you can also have the ingested data from sources like Twitter or like Reddit/r/the.  
**Translation:** 

**[9393.54s] English:** Donald, which is also super pro-Trump, right, and then you have like fascist subreddits, or like  
**Translation:** 

**[9397.64s] English:** You have communist subreddits, so the model during pre-training ingests everything; it has no filter for the real world.  
**Translation:** Vocabulary: fascist: 法西斯; ingests: 摄入; subreddits: 论坛

**[9402.50s] English:** View now, it does have some skew because more of the text is skewed a certain way, uh, which  
**Translation:** 

**[9408.46s] English:** Is it general, like a slight left? But also, like, you know, somewhat intellectual?  
**Translation:** Vocabulary: skewed: 偏斜; slight: 轻微的

**[9414.22s] English:** Somewhat like, you know, it's just like the general Internet is a certain way, and then... and then, [pause]  
**Translation:** 

**[9418.72s] English:** As  
**Translation:** 

**[9418.84s] English:** As Nathan is about to describe eloquently, right?  
**Translation:** 

**[9420.76s] English:** Like you can elicit certain things out.  
**Translation:** Vocabulary: elicit: 引出; eloquently: 流利地

**[9422.70s] English:** And there's a lot of history here.  
**Translation:** 

**[9423.84s] English:** So, we can go through multiple examples.  
**Translation:** 

**[9425.24s] English:** And what happened?  
**Translation:** 

**[9426.20s] English:** Lama2 was a launch that the phrase  
**Translation:** 

**[9429.36s] English:** Like too much RLHF, or like too much safety.  
**Translation:** 

**[9431.44s] English:** There was a lot; it's just,  
**Translation:** 

**[9434.14s] English:** That was the whole narrative.  
**Translation:** 

**[9435.20s] English:** After Lama2's chat models were released.  
**Translation:** 

**[9437.64s] English:** And the examples are sorts of things.  
**Translation:** 

**[9440.32s] English:** Like you would ask Lama2 Chat:  
**Translation:** 

**[9441.96s] English:** How do you kill a Python process?  
**Translation:** 

**[9443.26s] English:** And it would say, "I can't talk about killing.  
**Translation:** 

**[9445.76s] English:** Because that's a bad thing.  
**Translation:** 

**[9446.90s] English:** And anyone trying to design an AI model,  
**Translation:** 

**[9450.20s] English:** Will probably agree that that's just like,  
**Translation:** 

**[9451.92s] English:** EH, model, you messed up a bit on the training there.  
**Translation:** Vocabulary: messed: 搞砸了

**[9454.58s] English:** I don't think they meant to do this.  
**Translation:** 

**[9455.74s] English:** But this was in the model weight.  
**Translation:** 

**[9456.92s] English:** So, this is not necessarily be.  
**Translation:** 

**[9459.56s] English:** There are things called system prompts,  
**Translation:** Vocabulary: prompts: 提示

**[9461.14s] English:** Which are when you're querying a model.  
**Translation:** 

**[9464.50s] English:** It's a piece of text that is shown to the model.  
**Translation:** Vocabulary: querying: 提问

**[9467.04s] English:** But not to the user.  
**Translation:** 

**[9468.14s] English:** So, a fun example is your system prompt.  
**Translation:** Vocabulary: prompt: 提示

**[9471.38s] English:** Could be talk like a pirate.  
**Translation:** 

**[9472.28s] English:** So, no matter what the user says to the model,  
**Translation:** Vocabulary: pirate: 海盗

**[9474.82s] English:** It'll respond like a pirate.  
**Translation:** 

**[9476.28s] English:** In practice,  
**Translation:** 

**[9476.70s] English:** What they are: You are a helpful assistant.  
**Translation:** 

**[9480.00s] English:** You should break down problems. If you don't know about something, don't tell them; cut off.  
**Translation:** 

**[9484.68s] English:** Is this today's date? It's a lot of really useful context for answering.  
**Translation:** 

**[9488.66s] English:** A question, well. And Anthropic publishes their system: yes, which I think is great. And there's  
**Translation:** 

**[9492.94s] English:** A lot of research goes into this. And one of your previous guests, Amanda Askell, is probably  
**Translation:** 

**[9497.98s] English:** The most knowledgeable person, at least in the combination of execution and sharing. She's the  
**Translation:** 

**[9503.00s] English:** Person that should talk about system prompts and model characters. Yeah, and people should read.  
**Translation:** 

**[9507.20s] English:** These system prompts because you're trying to nudge sometimes through extreme politeness.  
**Translation:** Vocabulary: nudge: 暗示; politeness: 礼貌

**[9514.72s] English:** The model to be a certain way, and you could use this for bad things. We've done tests, which is  
**Translation:** 

**[9519.88s] English:** What if I tell the model to be a dumb model? Which evaluation scores go down? And it's like,...  
**Translation:** Vocabulary: evaluation: 评估

**[9526.50s] English:** We'll have this behavior where it could sometimes say, "Oh, I'm supposed to be dumb." And sometimes,...  
**Translation:** 

**[9530.28s] English:** It doesn't affect math abilities as much, but something like, if you're trying, it's just the  
**Translation:** 

**[9536.02s] English:** Quality of human judgment.  
**Translation:** 

**[9537.20s] English:** Let's go back to post-training, specifically RLHF around LAMA2. It was too much safety.  
**Translation:** 

**[9544.44s] English:** Prioritization was baked into the model weights. This makes you refuse things in a really annoying way.  
**Translation:** 

**[9549.38s] English:** A way for users: It's not great; it caused a lot of awareness to be attached to RLHF, making  
**Translation:** Vocabulary: prioritization: 优先级设定

**[9557.20s] English:** The model is dumb, and it stigmatized the word. It did this in AI culture. And as the techniques have  
**Translation:** 

**[9562.86s] English:** Evolved, that's no longer the case where all of these labs have very fine-grained control.  
**Translation:** Vocabulary: evolved: 发展; stigmatized: 污名化

**[9567.20s] English:** What they get out of the models through techniques like RLHF.  
**Translation:** 

**[9570.02s] English:** Although different labs are definitely at different levels, on one end of the spectrum is Google.  
**Translation:** 

**[9576.64s] English:** And then, maybe OpenAI does less and Anthropic does less. And then, on the other end of the  
**Translation:** 

**[9581.36s] English:** The spectrum is XAI, but they all have different forms of RLHF, trying to make them a certain way.  
**Translation:** 

**[9587.36s] English:** And the important thing to say is that, no matter how you want the model to behave,  
**Translation:** 

**[9593.60s] English:** These RLHF and preference tuning techniques also improve performance.  
**Translation:** 

**[9597.20s] English:** And things like math evals and code evals, there is  
**Translation:** 

**[9600.00s] English:** Something innate to these, what is called contrastive loss functions. We could start to  
**Translation:** Vocabulary: innate: 天生的

**[9604.46s] English:** Get into RL here. We don't really need to, but RLHF also boosts performance on anything from a  
**Translation:** 

**[9609.26s] English:** Chat tasks are being transformed into math problems, which are then turned into code problems. So, it is becoming a much more useful tool for these purposes.  
**Translation:** Vocabulary: boosts: 提升

**[9615.32s] English:** Labs. So, this kind of takes us through the arc of: we've talked about pre-training; it's hard to get rid of that.  
**Translation:** 

**[9619.40s] English:** Of things, we've talked about post-training and how, after post-training, you can mess it up. It's  
**Translation:** 

**[9624.14s] English:** Complex, multifaceted optimization with 10 to 100-person teams converging on one artifact. It's  
**Translation:** 

**[9630.34s] English:** Really, it's easy to not do it perfectly. And then there's the third case, which is what we talked about.  
**Translation:** Vocabulary: artifact: 产物; converging: 汇聚; multifaceted: 多面的; optimization: 优化

**[9634.30s] English:** About Gemini. The thing about Gemini is that it's a served product where Google has their  
**Translation:** 

**[9640.08s] English:** Internal model weights. They've done all these processes that we talked about, and in the served.  
**Translation:** Vocabulary: gemini: 双子座产品

**[9643.80s] English:** Product: What came out after this was that they had a prompt they were rewriting user queries.  
**Translation:** 

**[9648.26s] English:** To boost diversity, or something. And this just made it; the outputs were just blatantly wrong.  
**Translation:** Vocabulary: blatantly: 明显地; outputs: 输出; prompt: 提示; queries: 询问; rewriting: 重写

**[9653.86s] English:** It was a....  
**Translation:** 

**[9654.14s] English:** Some sort of organizational failure led to this prompt being in that position.  
**Translation:** 

**[9658.46s] English:** And I think Google executives probably have owned this. I didn't pay that much attention.  
**Translation:** 

**[9662.46s] English:** That detail, but it was just a mess-up in execution that led to this ridiculous thing.  
**Translation:** Vocabulary: execution: 执行; executives: 高管

**[9666.74s] English:** But, at the system level, the model weights might have been fine.  
**Translation:** 

**[9669.86s] English:** So, at the very end of the pipeline, there was a rewrite.  
**Translation:** Vocabulary: pipeline: 处理流程; rewrite: 重写代码

**[9672.82s] English:** To something like a system prompt. It was like the system prompt, or what is called in the industry.  
**Translation:** 

**[9678.24s] English:** It's like rewriting prompts. So, especially for image models, if you're using DALI or ChatGPT,  
**Translation:** Vocabulary: prompts: 提示词

**[9684.14s] English:** You can generate an image for you. You'll say, "Draw me a beautiful car." With these leading instructions.  
**Translation:** 

**[9689.86s] English:** Models, they benefit from highly descriptive prompts. So, what would happen is if you do that.  
**Translation:** Vocabulary: descriptive: 描述详细的

**[9695.52s] English:** On Chat GPT, a language model behind the scenes will rewrite the prompt, saying, "make this more...  
**Translation:** 

**[9700.14s] English:** Descriptive, and then that is passed to the image model. So, prompt rewriting is something that is  
**Translation:** 

**[9704.44s] English:** Used at multiple levels of industry, and it's effectively used for image models. And the Gemini.  
**Translation:** 

**[9708.94s] English:** An example is just a failed execution. Big philosophical question, here.  
**Translation:** 

**[9714.14s] English:** With RLHF, to generalize, where is the human?  
**Translation:** 

**[9720.00s] English:** Input: Human in the loop, is human data most useful at the current stage?  
**Translation:** Vocabulary: generalize: 泛化

**[9726.60s] English:** For the past few years, the highest cost for human data has been in these preferences.  
**Translation:** 

**[9732.36s] English:** Which is comparing, I would say, the highest cost and highest total usage. So, a lot of money has  
**Translation:** 

**[9738.10s] English:** Gone to these pairwise comparisons, where you have two model outputs and a human is  
**Translation:** 

**[9742.04s] English:** Comparing the two of them, in earlier years, there was a lot of this instruction.  
**Translation:** Vocabulary: outputs: 模型结果; pairwise: 两两对比

**[9747.16s] English:** Tuning data. So, creating highly specific examples for something like a Reddit question within a domain.  
**Translation:** 

**[9753.48s] English:** That you care about. Language models used to struggle with math and code. So, you would pay  
**Translation:** 

**[9757.52s] English:** Experts in math and code to come up with questions and write detailed answers that  
**Translation:** 

**[9761.26s] English:** Were used to train the models. Now, it is the case that there are many model options that  
**Translation:** 

**[9767.32s] English:** Are they way better than humans at writing detailed and eloquent answers for things like models?  
**Translation:** 

**[9772.60s] English:** Code. So, they talked about this with the Lama 3 release, where they switched to use.  
**Translation:** Vocabulary: eloquent: 口才好

**[9777.14s] English:** Lama 3, 4, or 5B to write their answers for math and code. But they, in their papers,  
**Translation:** 

**[9783.26s] English:** Talk about how they use extensive human preference data, which is something that  
**Translation:** 

**[9787.12s] English:** They haven't gotten AIs to replace. There are other techniques in industry, like constitutional.  
**Translation:** 

**[9790.78s] English:** AI, where you use human data for preferences and AI for preferences. And I expect the AI  
**Translation:** 

**[9795.34s] English:** Part can scale faster than the human part. But among the research that we have access to,  
**Translation:** 

**[9800.44s] English:** Is that humans are in this kind of preference loop?  
**Translation:** 

**[9804.42s] English:** So, as reasoning becomes,  
**Translation:** 

**[9807.14s] English:** Bigger and bigger and bigger, as we said, where's the role of humans in that?  
**Translation:** 

**[9810.96s] English:** It's even less prevalent. So, it's the remarkable thing about these reasoning results.  
**Translation:** 

**[9816.64s] English:** And especially the DeepSeek R1 paper, is this result that they call DeepSeek R1-0.  
**Translation:** Vocabulary: prevalent: 普遍的

**[9821.58s] English:** Which is that they took one of these pre-trained models, specifically DeepSeek V3 base.  
**Translation:** 

**[9825.32s] English:** And then they do this reinforcement learning optimization on verifiable questions or  
**Translation:** Vocabulary: optimization: 优化; reinforcement: 强化; verifiable: 可验证的

**[9830.00s] English:** Verifiable rewards for a lot of questions and a lot of training. And these reasoning behaviors.  
**Translation:** 

**[9835.44s] English:** emerge naturally. So, these things,  
**Translation:** Vocabulary: rewards: 奖励

**[9837.14s] English:** Like, wait, let me see. Wait, let me check this.  
**Translation:** 

**[9840.00s] English:** That might be a mistake. And they emerge from only having questions and answers. And when you're  
**Translation:** 

**[9845.74s] English:** Using the model, the part that you look at is the completion. So, in this case, all of that just  
**Translation:** 

**[9850.88s] English:** Emerges from this large-scale RL training. And that model, whose weights are available,  
**Translation:** Vocabulary: completion: 完成部分

**[9856.58s] English:** Has no human preferences added into the post-training. The DeepSeek R1 full model has  
**Translation:** 

**[9863.32s] English:** Some of this human preference tuning, also known as RLHF, comes after the reasoning stage. But the very remarkable...  
**Translation:** 

**[9868.76s] English:** The thing is, you can get these reasoning behaviors, and it's very unlikely that there's  
**Translation:** 

**[9873.28s] English:** Humans writing out reasoning chains. It's very unlikely that they somehow hacked OpenAI, and they  
**Translation:** Vocabulary: hacked: 破解

**[9877.72s] English:** Got access to OpenAI 01's reasoning chains. It's something about the pre-trained language models.  
**Translation:** 

**[9883.62s] English:** And in this RL training, where you reward the model for getting the question right.  
**Translation:** 

**[9888.06s] English:** And therefore, it's trying multiple solutions, and this chain of thought emerges.  
**Translation:** 

**[9892.98s] English:** This might be a good place to mention the eloquent and insightful tweet.  
**Translation:** Vocabulary: eloquent: 口才好; emerges: 出现

**[9898.74s] English:** Of the great and powerful Andrzej Karpathy, I think he had a bunch of thoughts, but one of them,  
**Translation:** 

**[9904.80s] English:** Last thought: not sure if this is obvious. You know something profound is coming when you're  
**Translation:** Vocabulary: profound: 深奥的

**[9909.24s] English:** Saying it's not sure if it's obvious, there are two major types of learning in both children and  
**Translation:** 

**[9914.36s] English:** In deep learning, there's one approach called imitation learning: watch and repeat, i.e., pre-training, supervised.  
**Translation:** Vocabulary: imitation: 模仿; supervised: 监督

**[9920.34s] English:** Fine-tuning. And two, trial-and-error learning, reinforcement learning. My favorite simple example:  
**Translation:** 

**[9926.60s] English:** Is AlphaGo one of them? AlphaGo is a training tool for learning.  
**Translation:** Vocabulary: reinforcement: 强化学习

**[9928.72s] English:** Learning by imitating expert players. Two: reinforcement learning to win the game.  
**Translation:** 

**[9933.58s] English:** Almost every single shocking result of deep learning, and the source of all its magic, is always  
**Translation:** Vocabulary: imitating: 模仿

**[9939.62s] English:** Two is significantly more powerful. Two is what surprises you. Two is when the paddle learns.  
**Translation:** 

**[9946.78s] English:** To hit the ball behind the blocks and break out. Two: when AlphaGo beats even Lee Sedol.  
**Translation:** Vocabulary: paddle: 球拍

**[9952.18s] English:** And two is the "aha" moment when the deep seek, or "oh, one," etc.  
**Translation:** 

**[9958.72s] English:** That it works well to  
**Translation:** 

**[9960.00s] English:** Re-evaluate your assumptions, backtrack, try something else, etc. It's the solving strategies.  
**Translation:** 

**[9966.04s] English:** You see, this model uses a chain of thought, which is how it goes back and forth, thinking to itself.  
**Translation:** Vocabulary: assumptions: 前提; backtrack: 回溯

**[9973.38s] English:** These thoughts are emergent! And this is actually, seriously incredible!  
**Translation:** 

**[9979.94s] English:** Impressive, and new, and is publicly available and documented. The model could never learn this on its own.  
**Translation:** Vocabulary: emergent: 涌现的

**[9986.28s] English:** Imitation, because the cognition of the model and the cognition of the human labeler are different.  
**Translation:** 

**[9993.10s] English:** The human would never know how to correctly annotate these kinds of solving strategies.  
**Translation:** Vocabulary: annotate: 标注; cognition: 认知; labeler: 标注员

**[9996.62s] English:** And what they should even look like. They have to be discovered during reinforcement learning.  
**Translation:** 

**[10002.06s] English:** As empirically and statistically useful towards the final outcome, anyway, the α-zero sort of  
**Translation:** Vocabulary: empirically: 根据经验; statistically: 统计数据

**[10007.08s] English:** Metaphor and analogy here. Can you speak to that—the magic of the chain of thought that he's referring to?  
**Translation:** 

**[10013.30s] English:** To, I think it's good to recap AlphaGo and  
**Translation:** Vocabulary: analogy: 类比; metaphor: 比喻

**[10016.02s] English:** AlphaZero.  
**Translation:** 

**[10016.28s] English:** Because it plays nicely with these analogies between imitation learning and learning from.  
**Translation:** Vocabulary: analogies: 类比; imitation: 模仿; nicely: 恰当

**[10020.00s] English:** Scratch. So, AlphaGo: the beginning of the process was learning from humans, where they started the  
**Translation:** 

**[10026.18s] English:** First, this is the first expert-level Go or chess player in DeepMind's series of models.  
**Translation:** 

**[10031.60s] English:** Where they had some human data, and then why it is called AlphaZero is that there was zero human input.  
**Translation:** 

**[10036.96s] English:** Data in the loop, and that change to AlphaZero made a model that was dramatically more powerful.  
**Translation:** Vocabulary: dramatically: 大幅度地

**[10042.24s] English:** For DeepMind, so this removal of the human prior, the  
**Translation:** 

**[10046.02s] English:** Human inductive bias makes the final system far more powerful. This is a bitter lesson we mentioned.  
**Translation:** Vocabulary: inductive: 归纳的

**[10051.14s] English:** Hours ago, and this is all aligned with that. And then there has been a lot of discussion in  
**Translation:** 

**[10058.80s] English:** Language models. This is not new. This goes back to the whole Q* rumors, which, if you piece together,...  
**Translation:** Vocabulary: aligned: 一致

**[10065.06s] English:** Together, the pieces is probably the start of OpenAI figuring out that it's all one system. Last year,...  
**Translation:** 

**[10070.42s] English:** In November, the Q-Star rumors came out. There are a lot of intellectual,  
**Translation:** 

**[10076.02s] English:** Drive to know when something like this is going to happen with language models?  
**Translation:** 

**[10080.00s] English:** Because we know these models are so powerful, and we know it has been so successful in the past.  
**Translation:** 

**[10084.92s] English:** And it is a reasonable analogy that this new type of reinforcement learning training for reasoning.  
**Translation:** 

**[10091.18s] English:** Models is when the door is open to this. We don't yet have the equivalent of Turn 37.  
**Translation:** Vocabulary: reinforcement: 强化

**[10097.76s] English:** Which is the famous turn where DeepMind's AI plan got stumped by Lee Sedol completely? We don't  
**Translation:** 

**[10104.42s] English:** Have something that's that level of focal point, but that doesn't mean that the approach to  
**Translation:** Vocabulary: stumped: 难倒了

**[10108.46s] English:** Technology is different, and the impact of generalized training is still incredibly new.  
**Translation:** 

**[10112.52s] English:** What do you think that point would be? What would be move 37 for the chain of thought, for reasoning?  
**Translation:** Vocabulary: generalized: 泛化的

**[10117.42s] English:** Scientific discovery: When you use this sort of reasoning problem in it,  
**Translation:** 

**[10121.48s] English:** Just something we fully don't expect. I think it's actually probably simpler than that. It's  
**Translation:** 

**[10125.98s] English:** Probably something related to computer-user robotics rather than science discovery. Because  
**Translation:** 

**[10131.90s] English:** The important aspect here is that models take so much data to learn; they're not samples.  
**Translation:** Vocabulary: robotics: 机器人技术

**[10138.46s] English:** Efficient. They take the entire web, over 10 trillion tokens to train on. This would take:  
**Translation:** 

**[10145.74s] English:** A human would take thousands of years to read. And humans know most of the stuff, a lot of the stuff models know.  
**Translation:** Vocabulary: trillion: 万亿

**[10153.60s] English:** Know better than it. Humans are way, way, way more sample-efficient. That is because of the  
**Translation:** 

**[10157.98s] English:** Self-play. How does a baby learn what its body is? As it sticks its foot in its mouth, and it says,...  
**Translation:** Vocabulary: sticks: 用嘴触碰

**[10164.04s] English:** Oh, this is my body. It sticks its hand in its mouth and it calibrates.  
**Translation:** 

**[10168.46s] English:** Its touch on its fingers with the most sensitive touch, much like that on its tongue. This is how babies.  
**Translation:** Vocabulary: calibrates: 校准

**[10172.80s] English:** Learn. And it's just self-play, over and over and over again. And now we have something.  
**Translation:** 

**[10178.80s] English:** That is similar to using these verifiable proofs, whether it's a unit test in code or  
**Translation:** Vocabulary: proofs: 证明; verifiable: 可验证的

**[10185.92s] English:** Mathematical, verifiable tasks generate many traces of reasoning, and keep branching them out.  
**Translation:** 

**[10193.22s] English:** Keep branching them out. And then, at the end, check which one actually has the right answer?  
**Translation:** Vocabulary: mathematical: 数学的; traces: 痕迹

**[10196.52s] English:** Most of them are wrong. Great! These are the few that are right.  
**Translation:** 

**[10198.46s] English:** Maybe we could use some sort of reward model.  
**Translation:** 

**[10200.00s] English:** Outside of this, to select even the best one to prefer as well, but now you've started to get...  
**Translation:** 

**[10204.54s] English:** Better and better at these benchmarks, and so you've seen over the last six months a skyrocketing  
**Translation:** Vocabulary: benchmarks: 评估标准; skyrocketing: 急剧上升

**[10209.12s] English:** In a lot of different benchmarks, right? All math and code benchmarks were pretty much solved, except...  
**Translation:** 

**[10213.86s] English:** For frontier math, which is designed to be almost questions that aren't practical for most people.  
**Translation:** Vocabulary: frontier: 前沿领域

**[10218.94s] English:** Because they're like exam-level open math problems, so it's like on the math  
**Translation:** 

**[10226.22s] English:** Problems that are somewhat reasonable, which is like somewhat complicated word problems or coding.  
**Translation:** 

**[10230.22s] English:** Problems, it's just what Dylan is saying. So, the thing here is that these are only with verifiable  
**Translation:** 

**[10236.10s] English:** Tasks we earlier showed an example of the, you know, the really interesting stuff like what happens.  
**Translation:** Vocabulary: dylan: Dylan

**[10240.42s] English:** When a chain of thought is about a non-verifiable thing, it's just like a human, you know, chatting.  
**Translation:** 

**[10244.26s] English:** Right, with the you know, thinking about what's novel for humans — a unique thought, but this  
**Translation:** 

**[10248.94s] English:** Task and form of training only works when it's infinite, when it's verifiable, and from here the  
**Translation:** 

**[10254.40s] English:** Thought, it's okay we can continue.  
**Translation:** Vocabulary: infinite: 无穷的

**[10256.20s] English:** To scale this current training method by increasing the number of verifiable tasks.  
**Translation:** 

**[10260.36s] English:** In math and coding, coding probably has a lot more room for growth, while math has a lot less.  
**Translation:** Vocabulary: verifiable: 可验证的

**[10266.58s] English:** Are there verifiable things? Can I create a solver that then generates trajectories or traces?  
**Translation:** 

**[10271.50s] English:** Towards reasoning, trace out those that don't work and keep the ones that do.  
**Translation:** Vocabulary: generates: 产生; solver: 求解器; trajectories: 轨迹

**[10275.30s] English:** Do work well; those are going to be solved pretty quickly, but even if you've solved math, you have not  
**Translation:** 

**[10279.66s] English:** Actually, it was created through intelligence, and so I think this is where the "aha" moment occurs.  
**Translation:** 

**[10285.32s] English:** Of  
**Translation:** 

**[10286.20s] English:** Computer users will come in because now you have a sandbox or a playground that is  
**Translation:** Vocabulary: sandbox: 测试环境

**[10291.96s] English:** Infinitely verifiable, right? Did you know that messing around on the internet, there are so many  
**Translation:** 

**[10297.34s] English:** Actions that you can do that are verifiable will start off with things like logging into a website or creating an account.  
**Translation:** Vocabulary: infinitely: 无穷地; messing: 胡闹

**[10301.36s] English:** Account: Click a button here, blah blah blah, but it will then get to the point where it's "hey, go do...  
**Translation:** 

**[10306.18s] English:** A task on Tasker or whatever these other various task websites: hey, go get hundreds of likes!  
**Translation:** 

**[10310.96s] English:** Right, um, and it's going to fail. It's going to spawn hundreds of accounts, and it's going to fail on...  
**Translation:** 

**[10315.00s] English:** Most of them, but this one got to a thousand—great! Now you've reached the verifiable thing.  
**Translation:** Vocabulary: spawn: 产生

**[10318.62s] English:** And you just keep iterating.  
**Translation:** 

**[10320.00s] English:** This loop over and over, and that's when and same with robotics—right? That's where you know where.  
**Translation:** Vocabulary: robotics: 机器人技术

**[10324.10s] English:** You have an infinite playground of tasks, like "Hey, did I put the ball in the bucket?" all the way to  
**Translation:** 

**[10328.18s] English:** Like, oh, did I like build a car? Right, you know, there's a whole trajectory to speed run or you.  
**Translation:** Vocabulary: trajectory: 轨迹

**[10333.42s] English:** Know what models can do, but at some point, I truly think that, like, you know, we'll spawn models and  
**Translation:** 

**[10339.52s] English:** Initially, all the training will be in sandboxes, but then at some point, you know, the language model...  
**Translation:** 

**[10343.24s] English:** Pre-training is going to be dwarfed by what is this reinforcement learning? You know, you'll see.  
**Translation:** 

**[10347.94s] English:** Pre-train a multimodal model that can see, that can read, and that can write, you know, blah blah blah.  
**Translation:** Vocabulary: dwarfed: 相形见绌; multimodal: 多模态; reinforcement: 强化

**[10351.92s] English:** Whatever, vision, audio, etc., but then you'll have it play in a sandbox infinitely and figure out...  
**Translation:** 

**[10358.82s] English:** Figure out math, figure out coding, figure out navigating the web, and figure out operating a robot.  
**Translation:** Vocabulary: navigating: 网络导航

**[10362.58s] English:** Arm it right, and then it'll learn so much. I think the "aha" moment will be when this is available.  
**Translation:** 

**[10368.46s] English:** To then create something that's not good, right? Like, oh, cool, part of it was like figuring out  
**Translation:** 

**[10372.48s] English:** How to use the Web now, all of a sudden, it's figured out really well how to just get hundreds.  
**Translation:** 

**[10377.36s] English:** Of thousands of files, and then it's like, "Oh, cool! I'm going to do this now. I'm going to do this now.  
**Translation:** 

**[10377.92s] English:** That are real and real engagement on Twitter, because all of a sudden, this is one of the  
**Translation:** 

**[10381.30s] English:** Things that are verifiable, and maybe not just engagement but make money, yes, I've become—I mean.  
**Translation:** Vocabulary: verifiable: 可验证的

**[10387.22s] English:** That could be the thing where almost fully automated, it makes you know $10 million.  
**Translation:** 

**[10393.28s] English:** By being an influencer, selling a product, creating the product, like  
**Translation:** Vocabulary: automated: 自动化; influencer: 意见领袖

**[10396.54s] English:** And I'm not referring to a hype product, but an actual product.  
**Translation:** 

**[10401.68s] English:** Like, holy shit! This thing created a business; it's running it, and it's the face of the business.  
**Translation:** 

**[10407.92s] English:** That kind of thing, maybe, or maybe, uh, Number One Song—it creates the whole infrastructure.  
**Translation:** 

**[10413.28s] English:** Required to create the song to be the influencer that represents it, kind of thing.  
**Translation:** 

**[10417.98s] English:** And it makes a lot of sense that could be the move. I mean, this is our culture, which respects money in that kind of way.  
**Translation:** 

**[10424.00s] English:** Way, and it's and it's verifiable, right? The bank account can't lie. Exactly, there's something surprising.  
**Translation:** 

**[10430.84s] English:** Evidence that once you set up the ways of collecting the verifiable data, this can work.  
**Translation:** 

**[10435.66s] English:** There has been a lot of research.  
**Translation:** 

**[10437.92s] English:** Before this R1 on math.  
**Translation:** 

**[10440.00s] English:** Problems, and they approach math with language models just by increasing the number of samples.  
**Translation:** 

**[10444.70s] English:** So, you can just try again and again and again, and you look at the amount of times that the language  
**Translation:** 

**[10449.54s] English:** Models get it right, and what we see is that even very bad models get it right sometimes, and the  
**Translation:** 

**[10456.14s] English:** The whole idea behind reinforcement learning is that you can learn from very sparse rewards, so it is.  
**Translation:** 

**[10462.08s] English:** Doesn't the space of language and the space of tokens, whether you're generating language or...  
**Translation:** Vocabulary: reinforcement: 强化; rewards: 奖励; sparse: 稀疏

**[10466.06s] English:** Tasks for a robot are so big that you might say it's like, I mean, each tokenizer for a  
**Translation:** 

**[10471.74s] English:** A language model can be like 200,000 things, so at each step, it can sample from that big of a pool.  
**Translation:** Vocabulary: tokenizer: 分词器

**[10475.54s] English:** Space; so, if it can generate a bit of a signal that it can climb onto, that's the whole field.  
**Translation:** 

**[10481.78s] English:** Of RL is around learning from sparse rewards, and the same thing has played out in math, where  
**Translation:** 

**[10487.12s] English:** It's like very weak models that sometimes generate answers where you see research already that.  
**Translation:** 

**[10491.42s] English:** You can boost their math scores. You can do this kind of RL training.  
**Translation:** 

**[10494.78s] English:** For  
**Translation:** 

**[10495.70s] English:** For math, it might not be as effective, but if you take a 1-billion-parameter model, so something around 600...  
**Translation:** 

**[10500.62s] English:** Times smaller than deep seek, you can boost its grade-school math scores very directly with a  
**Translation:** 

**[10505.94s] English:** A small amount of this training, so it's not to say that this is coming soon. Setting up the  
**Translation:** 

**[10510.96s] English:** Verification domains is extremely hard, and there's a lot of nuance in this, but there are some basic.  
**Translation:** 

**[10516.72s] English:** Things that we have seen before, where it's at least expectable that there's a domain.  
**Translation:** 

**[10521.92s] English:** And there's a chance that this works, all right? So, we have some fun things happening in real life.  
**Translation:** 

**[10525.60s] English:** Time.  
**Translation:** 

**[10525.70s] English:** This is a good opportunity to talk about other reasoning models, just now OpenAI as perhaps.  
**Translation:** 

**[10534.76s] English:** Expected release: 03 mini. What are we expecting from the different flavors? Can you just lay it out?  
**Translation:** Vocabulary: flavors: 不同版本

**[10542.10s] English:** The different flavors of the old models, and from Gemini, the reasoning model: something I would say.  
**Translation:** 

**[10548.04s] English:** About these reasoning models, we talked a lot about reasoning training on math and code, and what  
**Translation:** Vocabulary: gemini: 双子座模型

**[10553.18s] English:** Is done, you have the base model we've talked about a lot and the reasoning training.  
**Translation:** 

**[10555.70s] English:** So, for example, you look at the Internet, and you can do a lot on the Internet; you do this on a large scale.  
**Translation:** 

**[10559.86s] English:** Reasoning Training with Reinforcement Learning  
**Translation:** 

**[10560.00s] English:** And then, as the DeepSeq paper detailed in this R1 paper, which for me is one of the big open questions on how to do this, is that they did reasoning-heavy, but very standard post-training techniques after the large-scale reasoning RL.  
**Translation:** Vocabulary: reinforcement: 强化

**[10575.22s] English:** So, they did the same thing with a form of instruction tuning through rejection sampling, which is essentially heavily filtered instruction tuning with some reward models.  
**Translation:** 

**[10583.96s] English:** And then they did this RLHF, but they made it math-heavy.  
**Translation:** Vocabulary: filtered: 筛选后的

**[10587.14s] English:** So, some of this transfer, we looked at this philosophical example early on.  
**Translation:** 

**[10593.38s] English:** One of the big open questions is: How much does this transfer?  
**Translation:** Vocabulary: philosophical: 哲学的

**[10596.90s] English:** If we bring in domains after the reasoning training, will all the models become eloquent writers through reasoning?  
**Translation:** 

**[10603.52s] English:** Is this philosophy stuff going to be open?  
**Translation:** Vocabulary: eloquent: 口才好

**[10605.06s] English:** We don't know, in the research, how much this will transfer.  
**Translation:** 

**[10607.72s] English:** There are other things about how we can make soft verifiers and things like that.  
**Translation:** Vocabulary: verifiers: 验证器

**[10611.18s] English:** But there is more training after reasoning, which makes it easier to use these reasoning models.  
**Translation:** 

**[10616.48s] English:** And that's what we're using right now.  
**Translation:** 

**[10617.84s] English:** So, if we're going to talk about Mini 3 and O1, these have gone through these extra techniques that are designed to align with human preferences after being trained to elicit reasoning.  
**Translation:** 

**[10626.82s] English:** I think one of the things that people are ignoring is Google's Gemini, which is both cheaper than R1 and better.  
**Translation:** Vocabulary: align: 使一致; elicit: 引发

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

**[10642.86s] English:** It has fewer tracks than it is supposed to have.  
**Translation:** Vocabulary: expressive: 有表现力的

**[10645.34s] English:** Quinn released a model.  
**Translation:** 

**[10646.48s] English:** Last fall, QWQ, which was their preview reasoning model.  
**Translation:** Vocabulary: quinn: 奎因

**[10651.12s] English:** And in DeepSeek, R1 Lite had last fall, where these models kind of felt like they were on rails, where they could really only do math and code.  
**Translation:** 

**[10658.44s] English:** And O1 is: it can answer anything.  
**Translation:** 

**[10660.94s] English:** It might not be perfect for some tasks, but it's flexible.  
**Translation:** 

**[10664.48s] English:** It has some richness to it.  
**Translation:** Vocabulary: flexible: 有弹性的

**[10666.78s] English:** And this is kind of the art of how to cook it a little bit undercooked.  
**Translation:** 

**[10671.82s] English:** It's like it's good to get a model out the door, but it's hard to gauge.  
**Translation:** Vocabulary: gauge: 测量; undercooked: 半生的

**[10675.86s] English:** And it takes a lot of taste to be like: "Is this a full-fledged model?  
**Translation:** 

**[10680.00s] English:** Can I use this for everything? They're probably more similar for math and code, my quick read is.  
**Translation:** 

**[10684.98s] English:** That Gemini Flash is like not trained the same way as 01, but taking an existing training stack.  
**Translation:** 

**[10693.10s] English:** Adding reasoning to it, so taking a more normal training stack and adding reasoning to it.  
**Translation:** Vocabulary: gemini: 双子座

**[10697.06s] English:** And I'm sure they're gonna have more. I mean, they've done quick releases on Gemini Flash, the...  
**Translation:** 

**[10701.80s] English:** Reasoning: and this is the second version from the holidays; it's evolving fast, and  
**Translation:** Vocabulary: evolving: 快速发展

**[10707.56s] English:** It takes longer to make this training stack where you're doing this large-scale ask the.  
**Translation:** 

**[10712.24s] English:** Same question from earlier: the one about human nature, yeah. What was the human?  
**Translation:** 

**[10718.96s] English:** Nature, one thing I can ramble on about so much is that we've been  
**Translation:** 

**[10724.68s] English:** Working on this at AI2 before 01 was fully available to everyone, and before R1, which is  
**Translation:** Vocabulary: ramble: 长篇大论

**[10730.44s] English:** Essentially, using RL training for fine-tuning, we use this in our TULU series of models.  
**Translation:** 

**[10735.58s] English:** And you can.  
**Translation:** 

**[10737.40s] English:** You can.  
**Translation:** 

**[10737.50s] English:** You can.  
**Translation:** 

**[10737.54s] English:** The same behaviors, where you say, "Wait and so much longer," but it's so late in the training.  
**Translation:** 

**[10742.82s] English:** Process that this kind of reasoning expression is much lighter, so you can there's, there's  
**Translation:** 

**[10747.48s] English:** Essentially, a gradation, and just how much of this RL training you put into it determines how the  
**Translation:** 

**[10751.80s] English:** Output looks so. Uh, we're now using Gemini 2.0 for flash thinking; experimental, version 121. It summarized.  
**Translation:** Vocabulary: gradation: 渐变; summarized: 总结

**[10761.58s] English:** The problem, as humans self-domesticated apes, perspective: okay, all right, so, wait, is this?  
**Translation:** 

**[10769.86s] English:** Reviewing the reasoning, here's why this is a novel: okay, uh, oh, yeah, and click to expand, okay.  
**Translation:** 

**[10776.66s] English:** Analyze the request; "novel" is the keyword, like see how it just looks a little different; it looks like.  
**Translation:** 

**[10783.36s] English:** A normal output, yeah. It's, I mean, in some sense, it's better structured; it makes more sense, and...  
**Translation:** Vocabulary: keyword: 关键字

**[10790.42s] English:** In it.  
**Translation:** 

**[10791.52s] English:** Well,  
**Translation:** 

**[10791.56s] English:** When it latched onto a human, and then it went into organisms—oh, wow! Apex predator focus on.  
**Translation:** 

**[10798.28s] English:** Domestication  
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
**Translation:** Vocabulary: articulate: 表达; refine: 精炼

**[10810.62s] English:** Greater facial expressiveness and communication ability.  
**Translation:** 

**[10813.92s] English:** Yes.  
**Translation:** Vocabulary: facial: 面部的

**[10815.12s] English:** Plasticity and adaptability.  
**Translation:** 

**[10816.60s] English:** Yes.  
**Translation:** Vocabulary: adaptability: 适应性

**[10817.04s] English:** Dependency on social groups.  
**Translation:** 

**[10818.50s] English:** Yes.  
**Translation:** 

**[10819.02s] English:** All right.  
**Translation:** 

**[10820.30s] English:** And self-criticize and refine further.  
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

**[10830.74s] English:** And the insight is getting at is that humans are not just social animals,  
**Translation:** 

**[10834.50s] English:** But profoundly self-domesticated apes.  
**Translation:** 

**[10837.36s] English:** And this self-domestication is the key to understanding our unique cognitive abilities.  
**Translation:** Vocabulary: cognitive: 认知; profoundly: 深刻地

**[10841.66s] English:** And social abilities.  
**Translation:** 

**[10843.26s] English:** Self-Domesticated Apes.  
**Translation:** 

**[10845.70s] English:** I prefer the deep-seek response.  
**Translation:** 

**[10848.66s] English:** I mean, it's novel.  
**Translation:** 

**[10851.56s] English:** The insight is novel.  
**Translation:** 

**[10853.44s] English:** I mean, that's like a good book title.  
**Translation:** 

**[10855.62s] English:** Self-Domesticated Apes.  
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

**[10869.60s] English:** This is Lex with a quick intermission, recorded after the podcast.  
**Translation:** Vocabulary: intermission: 休息时段

**[10874.74s] English:** Since we reviewed responses from Deep Seeker 1 and Gemini Flash 2.0, thinking during this  
**Translation:** 

**[10880.26s] English:** Conversation, I thought at this moment it would be nice to insert myself quickly, doing  
**Translation:** Vocabulary: gemini: 双子座; insert: 插入

**[10886.08s] English:** The same for OpenAI 01 Pro and 03 ME.  
**Translation:** 

**[10889.46s] English:** Mini, with the same prompt: "Give one truly novel insight about humans.  
**Translation:** Vocabulary: prompt: 提示

**[10897.74s] English:** And I thought I would, in general, give my vibe check and vibe-based anecdotal report on my own experience.  
**Translation:** 

**[10907.46s] English:** Experiences with the new 03 Mini model, now that I got a chance to spend many hours with it.  
**Translation:** Vocabulary: anecdotal: 个人经历

**[10913.10s] English:** Different kinds of contexts and applications.  
**Translation:** 

**[10915.50s] English:** So, I would probably categorize this question as, let's say, a very simple one.  
**Translation:** Vocabulary: categorize: 分类

**[10919.30s] English:** Let's say: Open.  
**Translation:** 

**[10920.00s] English:** Ended with a philosophical question. And in particular, the emphasis on novelty is a nice way to  
**Translation:** Vocabulary: novelty: 新奇; philosophical: 哲学的

**[10926.62s] English:** Test one of the model's capabilities, which is to come up with something that makes you pause.  
**Translation:** 

**[10932.96s] English:** And almost surprise you with its brilliance. So, said, my general review after running.  
**Translation:** Vocabulary: brilliance: 卓越; capabilities: 能力

**[10940.00s] English:** Each of the models on this question, a bunch of times, is that O1 Pro consistently gave brilliant.  
**Translation:** 

**[10946.84s] English:** Answers. Ones that gave me pause and made me think, both for their cutting insight and just.  
**Translation:** 

**[10954.48s] English:** Really nicely phrased with wit, with clarity, with nuance, over and over, consistently generating the  
**Translation:** 

**[10961.86s] English:** Best answers. After that is R1, which is less consistent, but again, delivered brilliance.  
**Translation:** Vocabulary: clarity: 清晰; nicely: 巧妙地; nuance: 细微差别; phrased: 表达

**[10968.80s] English:** Gemini Flash 2.0 thinking was third. And last was O3 Mini, actually.  
**Translation:** 

**[10976.44s] English:** Often gave me pause and made me think; both cutting in its insight and just really nicely phrased.  
**Translation:** 

**[10976.82s] English:** It often gave quite a generic answer, at least to my particular sensibilities. That said,  
**Translation:** 

**[10981.88s] English:** In a bunch of other applications that I tested for brainstorming purposes, it actually worked.  
**Translation:** Vocabulary: brainstorming: 头脑风暴; generic: 通用; sensibilities: 感受

**[10988.58s] English:** Extremely well, and often outperformed R1. But on this open-ended philosophical question,  
**Translation:** 

**[10995.38s] English:** It did consistently worse. Now, another important element for each of these models is how the  
**Translation:** 

**[11001.26s] English:** Reasoning is presented. DeepSeek R1 shows the full chain of thought tokens.  
**Translation:** 

**[11006.16s] English:** Which I personally just love. For these open-ended philosophical questions, it's really,  
**Translation:** Vocabulary: philosophical: 哲学的

**[11011.82s] English:** It's really interesting to see the model think through it. But, really, also, just stepping back,  
**Translation:** 

**[11017.08s] English:** As a person who appreciates intelligence, reasoning, and reflection,  
**Translation:** 

**[11022.16s] English:** Reading these kinds of chain-of-thought raw tokens from R1, there's something genuinely beautiful.  
**Translation:** 

**[11027.70s] English:** About observing the path of deliberation in an intelligent system. I think we don't always  
**Translation:** Vocabulary: deliberation: 思考过程; genuinely: 真正地

**[11035.24s] English:** To have that explicitly laid out for us humans, so we can see it.  
**Translation:** 

**[11040.00s] English:** In another intelligence system, the non-linearity of it, akin to Ulysses by James Joyce's Finnegans Wake,  
**Translation:** Vocabulary: explicitly: 明确地; ulysses: 尤利西斯

**[11047.18s] English:** Joyce. It's just beautiful to watch. Anyway, as we discussed in the episode, DeepSeek R1 talked:  
**Translation:** 

**[11053.90s] English:** About humans being able to convert selfish desires into cooperative systems by collectively pretending.  
**Translation:** Vocabulary: convert: 转变; cooperative: 合作的; desires: 欲望

**[11058.94s] English:** Abstract rules like money, laws, and rights are real, and these shared hallucinations act as  
**Translation:** 

**[11064.98s] English:** Games, where competition is secretly redirected to benefit the group, turning conflict into cooperation.  
**Translation:** Vocabulary: hallucinations: 共同幻觉

**[11070.90s] English:** Society's fuel. Gemini 2.0 Flash Thinking said: Humans are not just social animals, but self-domesticated.  
**Translation:** 

**[11078.16s] English:** Apes, and this self-domestication is the key to understanding our unique cognitive and social.  
**Translation:** Vocabulary: cognitive: 认知; gemini: 双子座

**[11083.62s] English:** Abilities. Now, it's important to say that the chain of thought there was really interesting.  
**Translation:** 

**[11089.08s] English:** It was looking through the entire evolution of life on Earth, considering apex predators.  
**Translation:** Vocabulary: predators: 顶级捕食者

**[11094.98s] English:** And considering how, from that, we ended up where we are, I think that domestication by  
**Translation:** 

**[11102.44s] English:** Choice is a really interesting angle. Again, it's one of those things when somebody presents a  
**Translation:** Vocabulary: domestication: 驯化

**[11107.94s] English:** Different angles on seemingly obvious things just make me smile, and the same goes for DeepSeek.  
**Translation:** 

**[11112.94s] English:** R1: That these hallucinations of money, laws, and rights, and us collectively pretending like it's  
**Translation:** 

**[11120.72s] English:** Real, and we play games with them that look like competition when secretly,  
**Translation:** 

**[11124.98s] English:** We're just cooperating with each other, and that is the fuel of progress. Beautifully put.  
**Translation:** Vocabulary: cooperating: 合作

**[11131.02s] English:** Now, OpenAI 01 Pro consistently, over and over, delivered bangers. I can go through many of them.  
**Translation:** 

**[11137.24s] English:** But the first one was: humans are the only species that turn raw materials into symbolic resources.  
**Translation:** Vocabulary: bangers: 精彩的段子; symbolic: 符号化的

**[11142.94s] English:** Then they use those symbols to reorganize the very materials they came from.  
**Translation:** 

**[11147.38s] English:** Creating a closed feedback loop between meaning and matter. Here, I just ran it again.  
**Translation:** Vocabulary: reorganize: 重新组织

**[11154.98s] English:** Bang after bang, I'm telling you, humans are unique among known species in that they  
**Translation:** 

**[11159.68s] English:** Simultaneously,  
**Translation:** 

**[11160.00s] English:** Rewrite two layers of reality—the external world and their own private mental landscapes—and then merge these two rewritten layers into a continuous, personal narrative that feels objectively true.  
**Translation:** 

**[11175.08s] English:** Feels true.  
**Translation:** Vocabulary: objectively: 客观地; rewrite: 重写; rewritten: 被重写

**[11177.28s] English:** This is poetry.  
**Translation:** 

**[11179.28s] English:** Okay.  
**Translation:** 

**[11179.86s] English:** And then, "O3 Mini High" for me was smart, fast, actually, and kind of generic.  
**Translation:** 

**[11188.56s] English:** Never quite got there for me.  
**Translation:** Vocabulary: generic: 普通的

**[11191.00s] English:** So, here's the first one I got from O3 Mini.  
**Translation:** 

**[11218.56s] English:** Now, it almost sneaks up on something approximating cutting insight with narrative plasticity, in quotes.  
**Translation:** Vocabulary: approximating: 接近; quotes: 引号; sneaks: 偷偷靠近

**[11227.08s] English:** But then it goes back to the sort of generic.  
**Translation:** 

**[11229.98s] English:** I don't know.  
**Translation:** 

**[11230.64s] English:** All of these models are incredible for different reasons.  
**Translation:** 

**[11233.48s] English:** There are a lot of concerns, as we discussed in this episode, but there are also a lot of reasons to be excited as well.  
**Translation:** 

**[11241.20s] English:** And I've probably spoken for too long.  
**Translation:** 

**[11243.56s] English:** I am severely sleep-deprived.  
**Translation:** 

**[11247.40s] English:** Borderline delirious.  
**Translation:** 

**[11248.56s] English:** So, hopefully, some of this made sense.  
**Translation:** Vocabulary: borderline: 接近界限的; delirious: 神志不清的

**[11251.66s] English:** And now, dear friends, back to the episode.  
**Translation:** 

**[11256.22s] English:** I think, when you know, to Nathan's point, when you look at the reasoning models—when I used R1 versus O1, there was that sort of "rough edges around the corner" feeling.  
**Translation:** 

**[11270.72s] English:** Right.  
**Translation:** 

**[11271.18s] English:** And in flash thinking, you know, earlier, I didn't use this version but the one from December, and it definitely had that rough edges around the corners feeling.  
**Translation:** 

**[11278.38s] English:** Right.  
**Translation:** 

**[11278.56s] English:** Where it's just not flesh.  
**Translation:** 

**[11280.00s] English:** Out, in any number of ways, right? Um, sure, they added math and coding capabilities via these verifiers.  
**Translation:** 

**[11285.68s] English:** And RL, but you know, they feel like they've lost something in certain areas, and O1 is worse.  
**Translation:** Vocabulary: capabilities: 能力; verifiers: 验证器

**[11291.08s] English:** Performing than chat in many areas, as well to be clear: um, not by a lot, not by a lot, though, right?  
**Translation:** 

**[11296.80s] English:** And it's like, some R1 definitely felt to me like it was worse than V3 in certain areas, like.  
**Translation:** 

**[11302.08s] English:** Doing this, RL expressed and learned a lot, but then it weakened in other areas, and so I think that's  
**Translation:** 

**[11308.34s] English:** One of the big differences between these models and what O1 offers, and then OpenAI.  
**Translation:** Vocabulary: weakened: 变弱

**[11314.56s] English:** Has O1 Pro, and what they did with O3, which is also very unique, is that they stacked search on.  
**Translation:** 

**[11321.14s] English:** Top of the chain of thought, right? Um, and so, chain of thought is one thing where it's able to be.  
**Translation:** Vocabulary: stacked: 叠加

**[11325.66s] English:** Chain it backtracks, goes back and forth, but how they served and solved the arc AGI challenge was not.  
**Translation:** 

**[11331.20s] English:** Just the chain of thought: it was also sampling many times, i.e., running them in parallel, and then...  
**Translation:** Vocabulary: backtracks: 回头; parallel: 并行

**[11337.40s] English:** Selecting is  
**Translation:** 

**[11338.26s] English:** Right.  
**Translation:** Vocabulary: selecting: 挑选

**[11338.32s] English:** Running in parallel, actually search because I don't know if we have the full information on.  
**Translation:** 

**[11342.26s] English:** How O1 Pro works, so, I'm not sure enough to confidently say that it...  
**Translation:** 

**[11346.60s] English:** Is search: It is parallel samples, yeah, and then it selects something, and we don't know what the.  
**Translation:** 

**[11351.10s] English:** Selection function is the reason why we're debating, because since O1 was announced.  
**Translation:** Vocabulary: selects: 挑选

**[11356.06s] English:** There has been a lot of interest in techniques called Monte Carlo simulations, which is where you  
**Translation:** 

**[11359.50s] English:** Will break down the chain of thought into intermediate steps. We haven't defined what the chain is.  
**Translation:** 

**[11363.64s] English:** Of thought, chain of thought is from a paper from years ago where you introduce the  
**Translation:** 

**[11368.24s] English:** Idea: To ask a language model that, at the time, was much less user-friendly, you would say, "Let's verify.  
**Translation:** Vocabulary: verify: 验证

**[11373.68s] English:** Step by step, and it would induce the model to do this. Bulleted list of steps: chain of thought is now.  
**Translation:** 

**[11379.68s] English:** Almost a default in models, where if you ask it a math question, you don't need to tell it to think.  
**Translation:** Vocabulary: bulleted: 项目符号; induce: 引导

**[11383.20s] English:** Step by step, and the idea with Monte Carlo Tree Search is that you would take an intermediate  
**Translation:** 

**[11388.72s] English:** At what point in that train do you start some sort of expansion, spend more compute resources, and then just select the right one?  
**Translation:** Vocabulary: compute: 计算; monte: 蒙特

**[11393.20s] English:** One that's like a very complex form of search, that has been used in things like MuZero, and I'll be  
**Translation:** 

**[11398.16s] English:** Talking about Alpha Zero, potentially, I know MuZero does.  
**Translation:** Vocabulary: alpha: 阿尔法

**[11400.00s] English:** Another form of search is just asking five different people, and then taking the majority.  
**Translation:** 

**[11404.82s] English:** Answer: Yes, there's a variety of things; it could be complicated, or it could be simple.  
**Translation:** 

**[11409.32s] English:** We don't know what it is; just that they are not just issuing a single chain of thought.  
**Translation:** 

**[11414.28s] English:** Sequence: They're launching many in parallel, and in the ARC AGI, they launched a thousand in parallel.  
**Translation:** Vocabulary: parallel: 并行

**[11420.32s] English:** For their one that really shocked everyone by beating the benchmark, they wanted  
**Translation:** 

**[11424.64s] English:** They would launch a thousand simulations in parallel, and then they would get the right answer about 80 percent of the time.  
**Translation:** Vocabulary: benchmark: 标准; simulations: 模拟

**[11428.48s] English:** The time, or 70 percent of the time, 90 percent maybe even more, whereas if they just launched one, it was like  
**Translation:** 

**[11432.68s] English:** 30 percent; there are many extensions to this. I would say the simplest one is that our language.  
**Translation:** Vocabulary: extensions: 扩展

**[11438.20s] English:** Models to date have been designed to give the right answer the highest percentage of the time.  
**Translation:** 

**[11443.16s] English:** In one response, and we are now opening the door to different ways of running inference on our models.  
**Translation:** Vocabulary: inference: 推断

**[11449.12s] English:** In which we need to reevaluate many parts of the training process, which normally opens the door to  
**Translation:** 

**[11455.30s] English:** More progress, but we don't know if Open AI changed a lot.  
**Translation:** Vocabulary: reevaluate: 重新评估

**[11458.32s] English:** Or, if just sampling more and using multiple-choice questions is what they're doing, or if it's something more.  
**Translation:** 

**[11462.44s] English:** Complex, but they change the training, and they know that the inference mode will be different.  
**Translation:** 

**[11467.24s] English:** So, we're talking about $0.10 per day (or $20.00 per month), and they're losing money. So, the thing that we're  
**Translation:** 

**[11475.96s] English:** Referring to this fascinating exploration, is it actually possible to examine the test-time compute space?  
**Translation:** Vocabulary: compute: 计算

**[11483.82s] English:** Do we have enough compute for that? Does the financials make sense?  
**Translation:** 

**[11488.32s] English:** The fantastic thing is, in there, it's in the thing that I just pulled up earlier, but uh,...  
**Translation:** Vocabulary: financials: 财务状况

**[11493.96s] English:** The cost for GPT-3 has plummeted. If you scroll up just a few images, I think the important thing is...  
**Translation:** 

**[11501.06s] English:** About, like, hey, is cost a limiting factor here, right? Like, in my view, we'll have  
**Translation:** Vocabulary: plummeted: 急剧下降; scroll: 滚动查看

**[11506.32s] English:** Like, really awesome intelligence before we have AGI, before we have it permeate throughout.  
**Translation:** 

**[11511.30s] English:** The economy, um, and this is sort of why: GPT-3 was trained in 2020-2021.  
**Translation:** Vocabulary: permeate: 渗透

**[11516.36s] English:** Um, and  
**Translation:** 

**[11518.32s] English:** The cost for running inference on  
**Translation:** 

**[11520.00s] English:** Was it $60, $70 per million tokens, right?  
**Translation:** 

**[11524.14s] English:** Which is the cost per unit of intelligence was ridiculous.  
**Translation:** 

**[11526.96s] English:** Now, as we scaled forward two years,  
**Translation:** 

**[11528.88s] English:** We've had a 1,200x reduction in cost.  
**Translation:** 

**[11531.80s] English:** To achieve the same level of intelligence as GPT-3.  
**Translation:** 

**[11534.76s] English:** So, here on the x-axis is time over just a couple of years.  
**Translation:** 

**[11539.78s] English:** And on the y-axis is a log-scale dollars.  
**Translation:** 

**[11543.66s] English:** To run inference on a million tokens.  
**Translation:** Vocabulary: inference: 推断

**[11547.36s] English:** And so you have just a down,  
**Translation:** 

**[11550.94s] English:** Like a linear decline on a log scale.  
**Translation:** Vocabulary: linear: 直线的

**[11553.86s] English:** From GPT-3 through 3.5 to LAMA.  
**Translation:** 

**[11557.44s] English:** It's like 5 cents, or something like that, now, right?  
**Translation:** 

**[11559.54s] English:** Which is versus $60, 1200x.  
**Translation:** 

**[11562.96s] English:** That's not the exact number, but it's 1,200 times.  
**Translation:** 

**[11565.06s] English:** I remember that number.  
**Translation:** 

**[11566.48s] English:** Is the humongous cost per unit of intelligence, right?  
**Translation:** Vocabulary: humongous: 巨大的

**[11570.16s] English:** Now, the freak-out over DeepSeek is,  
**Translation:** 

**[11572.06s] English:** Oh my God, they made it so cheap.  
**Translation:** 

**[11573.70s] English:** It's like, actually, if you look at this trend line,  
**Translation:** 

**[11575.90s] English:** They're not below the trend line.  
**Translation:** 

**[11577.18s] English:** First of all, and at least for GPT-3, right?  
**Translation:** 

**[11579.60s] English:** They are the first to hit it, right?  
**Translation:** 

**[11580.96s] English:** Which is a big deal.  
**Translation:** 

**[11582.28s] English:** But they're not below the trend line, as far as GPT-3.  
**Translation:** 

**[11584.86s] English:** Now, we have GPT-4.  
**Translation:** 

**[11586.02s] English:** What's going to happen with these reasoning capabilities, right?  
**Translation:** Vocabulary: capabilities: 能力

**[11588.34s] English:** It's a mix of architectural innovations.  
**Translation:** 

**[11590.42s] English:** It's a mix of better data.  
**Translation:** Vocabulary: architectural: 建筑方面的; innovations: 创新

**[11592.24s] English:** And it's going to be better training techniques.  
**Translation:** 

**[11593.80s] English:** And all of these different better inference systems,  
**Translation:** 

**[11596.00s] English:** Better hardware, right?  
**Translation:** 

**[11597.26s] English:** Going from each generation of GPU to new generations or ASICs.  
**Translation:** 

**[11602.32s] English:** Everything is going to take this cost curve.  
**Translation:** 

**[11604.68s] English:** Down, and down, and down, and down.  
**Translation:** 

**[11606.22s] English:** And then, Canada,...  
**Translation:** 

**[11607.18s] English:** Can I just spawn a thousand different LLMs?  
**Translation:** Vocabulary: spawn: 繁殖

**[11610.66s] English:** To create a task, and then pick from one of them.  
**Translation:** 

**[11613.08s] English:** Or whatever search technique I want,  
**Translation:** 

**[11615.34s] English:** A tree, Monte Carlo Tree Search.  
**Translation:** 

**[11617.02s] English:** Maybe it gets that complicated.  
**Translation:** Vocabulary: carlo: 卡尔洛; monte: 蒙特

**[11618.86s] English:** Maybe it doesn't because it's too complicated.  
**Translation:** 

**[11620.28s] English:** To actually scale.  
**Translation:** 

**[11621.24s] English:** Like, who knows?  
**Translation:** 

**[11622.08s] English:** Bitter lesson, right?  
**Translation:** 

**[11623.38s] English:** The question is: I think, when, not if.  
**Translation:** 

**[11627.96s] English:** Because the rate of progress is so fast, right?  
**Translation:** 

**[11631.64s] English:** Nine months ago, Dario was saying,  
**Translation:** 

**[11633.64s] English:** Or Dario said nine months ago,  
**Translation:** 

**[11635.22s] English:** The cost to train an inference was this.  
**Translation:** 

**[11637.18s] English:** Right?  
**Translation:** Vocabulary: inference: 推断

**[11637.80s] English:** And now we're much better than this, right?  
**Translation:** 

**[11640.00s] English:** And DeepSeek is much better than this. And that cost curve for GPT-4, which was also roughly $60.  
**Translation:** 

**[11645.20s] English:** Per million tokens, when it launched, has already fallen to $2 or so, right? And we're going to get  
**Translation:** 

**[11651.80s] English:** It would be down to cents, probably, for GPT-4 quality. And then that's the base for the reasoning models.  
**Translation:** 

**[11659.00s] English:** Like O1 that we have today, and O1 Pro is spawning multiple, right? And O3, and so on and so forth.  
**Translation:** 

**[11664.60s] English:** These search techniques, which are too expensive today, but they will get cheaper. And that's what's  
**Translation:** Vocabulary: spawning: 产生

**[11668.94s] English:** Going to unlock the intelligence, right? So it'll get cheaper and cheaper and cheaper.  
**Translation:** 

**[11673.98s] English:** The big DeepSeek R1 release freaked everybody out because of the cheaper.  
**Translation:** 

**[11679.80s] English:** One of the manifestations of that is that NVIDIA stock plummeted. Can you explain what happened?  
**Translation:** 

**[11686.10s] English:** I mean, and also just explain this moment and whether, you know, if NVIDIA is going to keep  
**Translation:** Vocabulary: manifestations: 表现; plummeted: 暴跌

**[11691.66s] English:** Winning. We're both NVIDIA bulls here, I would say. And in some ways, the market response is...  
**Translation:** 

**[11698.60s] English:** Reasonable.  
**Translation:** 

**[11698.94s] English:** Most of the market, like NVIDIA's biggest customers in the U.S., are major tech companies.  
**Translation:** 

**[11704.82s] English:** And they're spending a ton on AI. And if a simple interpretation of DeepSeek is that you can get really  
**Translation:** Vocabulary: interpretation: 解释

**[11710.58s] English:** Good models without spending as much on AI. So, in that capacity, it's like, oh, maybe these big tech  
**Translation:** 

**[11715.90s] English:** Companies won't need to spend as much on AI and go down. The actual thing that happened is much  
**Translation:** 

**[11719.94s] English:** More complex where there are social factors, where there's a rise in the app store, and the social.  
**Translation:** 

**[11724.82s] English:** Contagion that is happening. And then, I think, a lot of it is just like, I'm not,  
**Translation:** Vocabulary: contagion: 传染

**[11728.94s] English:** I don't trade, and I don't know anything about financial markets, but it builds up over the  
**Translation:** 

**[11731.76s] English:** Weekend or the social pressure, where it's like, if it was during the week, and there were multiple  
**Translation:** 

**[11735.66s] English:** Days of trading when this was really becoming clear, but it comes on the weekend, and then everybody  
**Translation:** 

**[11739.58s] English:** Wants to sell. And that is a social contagion. I think, I think, and like, there are a lot of  
**Translation:** 

**[11744.92s] English:** False narratives, which is like, "Hey, these guys are spending billions on models, right?" And they're  
**Translation:** 

**[11749.24s] English:** Not spending billions on models, no one spent more than a billion dollars on a model that's.  
**Translation:** Vocabulary: narratives: 虚假叙述

**[11753.56s] English:** Released publicly, right? GPT-4 had a couple hundred million parameters. And then, you know, they've  
**Translation:** 

**[11758.60s] English:** Reduced the cost for a  
**Translation:** 

**[11760.00s] English:** For turbo, all right. Um, but billion-dollar model runs are coming right. This concludes.  
**Translation:** 

**[11765.76s] English:** Pre-training and post-training, and then the other number is like, "Hey, DeepSeek didn't include...  
**Translation:** Vocabulary: turbo: 涡轮增压

**[11769.06s] English:** Everything's right; they didn't include, you know, a lot of the costs go to research and all this sort.  
**Translation:** 

**[11772.28s] English:** Of stuff, a lot of the cost goes to inference, a lot of cost goes to post-training, and none of these.  
**Translation:** Vocabulary: inference: 推断

**[11775.94s] English:** Things were factored, research salaries, right—like all these things are counted in the billions.  
**Translation:** 

**[11780.40s] English:** Of the dollars that Open AI is spending, but they weren't counted in the, you know, hey, six million.  
**Translation:** Vocabulary: factored: 考虑进去; salaries: 工资

**[11784.54s] English:** Five million dollars that Deepak spent, right? So, but there's a bit of a misunderstanding of  
**Translation:** 

**[11788.40s] English:** What these numbers are, um, and then there's also an element of NVIDIA that has just been a straight line.  
**Translation:** 

**[11794.00s] English:** Up right, and there have been so many different narratives trying to push down.  
**Translation:** 

**[11798.94s] English:** NVIDIA: Not, I don't say push down NVIDIA stock. Everyone is looking for a reason to sell or to  
**Translation:** 

**[11803.28s] English:** Be worried, right? Um, you know, it was Blackwell's delays, right? Their GPU was, you know,  
**Translation:** 

**[11808.26s] English:** There are lots of reports every two weeks; there's a new report about their GPUs being delayed, um,...  
**Translation:** 

**[11811.96s] English:** There's the whole thing about scaling laws ending, right? It's so ironic, right?  
**Translation:** 

**[11817.80s] English:** It lasted a month.  
**Translation:** 

**[11818.40s] English:** It was just like, literally, "hey, models aren't getting better, right?  
**Translation:** 

**[11823.70s] English:** They're just not getting better. There's no reason to spend more on pre-training; scaling is dead.  
**Translation:** 

**[11827.48s] English:** And then it's like, "Oh, 103," right? R1, R1, right? And now it's like, "Wait, models are getting...  
**Translation:** 

**[11833.56s] English:** Too, they're progressing too fast; slow down the progress. Stop spending on GPUs, right? But you know.  
**Translation:** 

**[11838.84s] English:** The funniest thing I think that comes out of this is Javon's Paradox is true, right? AWS pricing.  
**Translation:** 

**[11845.08s] English:** For H100s have gone up over the last couple of weeks, right?  
**Translation:** 

**[11848.40s] English:** Since a little bit after Christmas, when AWS H100 was launched, the pricing has gone...  
**Translation:** 

**[11853.94s] English:** Up H200s are like almost out of stock everywhere because it you know, H200 has more memory and  
**Translation:** Vocabulary: christmas: 圣诞节

**[11859.58s] English:** Therefore, R1 likes that chip over H100, right? We were trying to get GPUs on a short.  
**Translation:** 

**[11864.42s] English:** Notice this week for a demo, and it wasn't that easy. We were trying to get just like 16 or 32.  
**Translation:** 

**[11868.20s] English:** H100s for demo, and it was not very easy. So, for people who don't know, Javon's Paradox is...  
**Translation:** 

**[11874.46s] English:** When, you know, the efficiency goes up.  
**Translation:** 

**[11878.40s] English:** How magically, Conor.  
**Translation:** 

**[11880.00s] English:** Intuitively, the total resource consumption goes up as well, right? And semiconductors, you know,  
**Translation:** Vocabulary: intuitively: 直觉上; semiconductors: 半导体

**[11884.74s] English:** We're at 50 years of Moore's Law, where every two years, the cost is halved and the number of transistors doubles, just like  
**Translation:** 

**[11890.18s] English:** Clockwork, and it's slowed down obviously, but like the semiconductor industry, it has gone up the whole way.  
**Translation:** Vocabulary: clockwork: 发条机制; halved: 减半; semiconductor: 半导体; transistors: 晶体管

**[11894.64s] English:** Time has been wavy, right? There are obviously cycles and stuff, and I don't expect AI to be any different.  
**Translation:** 

**[11898.96s] English:** Different; right, there's going to be ebbs and flows, but this is an AI; it's just playing out.  
**Translation:** 

**[11903.34s] English:** At an insane timescale, right? It was 2x every two years. This is 1200x in just three years, right? So,  
**Translation:** 

**[11909.98s] English:** It's like the scale of improvement that is hard to get your head around, yeah, I was.  
**Translation:** Vocabulary: timescale: 时间尺度

**[11915.18s] English:** Confused because I thought NVIDIA stock should have gone up, but maybe it went down because  
**Translation:** 

**[11921.50s] English:** There's kind of a suspicion of foul play on the side of China, or something like this, but if you just  
**Translation:** 

**[11926.40s] English:** Look purely at the actual principles of play here. It's obvious, yeah—the Javon's Paradox that.  
**Translation:** 

**[11933.02s] English:** AI makes or the higher the derivative of AI progress is, especially you should be aware that NVIDIA  
**Translation:** Vocabulary: derivative: 导数; paradox: 悖论

**[11939.28s] English:** Is in the best place.  
**Translation:** 

**[11939.96s] English:** The higher the derivative is, the sooner the market's going to be bigger and expanding.  
**Translation:** 

**[11943.94s] English:** NVIDIA is the only one that does everything reliably right now, because it's not like an  
**Translation:** 

**[11948.36s] English:** NVIDIA's competitor has arisen; it's another company that's using NVIDIA technology, who historically has been  
**Translation:** Vocabulary: historically: 历史上; reliably: 可靠地

**[11955.82s] English:** Large NVIDIA customer, yeah, and has press releases about them cheering about being China's biggest.  
**Translation:** 

**[11961.52s] English:** NVIDIA's customer service, like, yeah, I mean, it's obviously quieted down, but I think  
**Translation:** 

**[11967.08s] English:** That's like another element: they don't want to say how many GPUs they have.  
**Translation:** 

**[11969.96s] English:** Yeah, because they do have H800s, yes, they have H20s, and they also have some H100s, right?  
**Translation:** 

**[11976.98s] English:** Can you speak to that? To the smuggling: what's the scale of smuggling that's feasible for a nation?  
**Translation:** 

**[11983.34s] English:** The state could do for companies: is it possible to address the issue of smuggling from a few different angles?  
**Translation:** Vocabulary: feasible: 可行的; smuggling: 走私

**[11989.28s] English:** Here, right, one is Bit Dance, arguably is the largest smuggler of GPUs for China, right? China's  
**Translation:** 

**[11994.58s] English:** Not supposed to have GPUs, but Dance has over 500,000 GPUs. Why? Because they're all rented from...  
**Translation:** Vocabulary: arguably: 可能; smuggler: 走私商

**[11999.96s] English:** People and they're oiled and all kinds of stuff, but those countries are still pretty far away.  
**Translation:** 

**[12000.00s] English:** Companies around the world rent from Oracle, they rent from Google, and they rent from all these others.  
**Translation:** 

**[12002.50s] English:** And so, it's hard to see how much of a difference it makes. So, I think it's possible to make an  
**Translation:** 

**[12004.46s] English:** Mass and a bunch of smaller cloud companies, too—right? All the neo-clouds, right? Of the world.  
**Translation:** 

**[12008.26s] English:** They rent so many GPS devices, they also buy a bunch, and they do this mostly for logistics purposes.  
**Translation:** 

**[12013.74s] English:** Meta does right serving TikTok right, serving the next best discussion. To be clear, that's today's view.  
**Translation:** 

**[12019.00s] English:** Improvement because the more you get, more sales, you're just going to get more business in the  
**Translation:** 

**[12020.60s] English:** Use "right" and it's a valid use of the term to hack the dopamine circuit, right? Um, now that's that's  
**Translation:** Vocabulary: dopamine: 多巴胺

**[12023.42s] English:** Future, but I think it's possible to make a difference because there's still a lot of  
**Translation:** 

**[12026.74s] English:** Theoretically, it is now much more restricted with the AI diffusion rules that happened last week.  
**Translation:** Vocabulary: diffusion: 扩散; theoretically: 理论上

**[12027.86s] English:** Competition is going on right now, I think. The other thing that's of interest, I think, is the one that's  
**Translation:** 

**[12029.82s] English:** Really interesting is the way that their system is designed and developed; it's not all the other  
**Translation:** 

**[12029.90s] English:** Technology is being sold, but it's just not being sold as the technology. The only technology that's really being marketed is  
**Translation:** 

**[12031.30s] English:** Of the Biden administration and Trump administration, it looks like they're going to keep the limits like.  
**Translation:** 

**[12036.52s] English:** Allies, even like Singapore, which is about 20 to 30 percent of Nvidia's business.  
**Translation:** 

**[12041.88s] English:** NVIDIA's revenue, but uh, Singapore's had a memorandum on not building data centers for like 15 years.  
**Translation:** Vocabulary: allies: 盟友; memorandum: 备忘录

**[12046.86s] English:** Because they don't have enough power, so where are they going? I mean, I'm not claiming they're all.  
**Translation:** 

**[12051.92s] English:** Going to China, right? But a portion—你知道很多人的目的地是马来西亚，包括微软。  
**Translation:** 

**[12056.18s] English:** And Oracle.  
**Translation:** 

**[12056.62s] English:** Have big data centers in Malaysia, like you know, all they're going all over Southeast Asia, probably.  
**Translation:** Vocabulary: malaysia: 马来西亚

**[12060.56s] English:** India, as well, right? Like, there's stuff routing, but the diffusion rules are very de facto, like.  
**Translation:** 

**[12065.70s] English:** You can only buy this many GPUs from this country, and it's and you can only rent a cluster this.  
**Translation:** Vocabulary: cluster: 计算集群; routing: 路由

**[12070.64s] English:** Large companies that are Chinese, however, are very explicit about trying to stop smuggling.  
**Translation:** 

**[12075.56s] English:** Right, and a big chunk of it was "hey, let's let's, you know, random company" by 16 servers.  
**Translation:** Vocabulary: explicit: 明确; smuggling: 走私

**[12080.06s] English:** Ship them to China, right? There's actually a photo I saw from someone, uh,...  
**Translation:** 

**[12086.62s] English:** In the semiconductor industry, there isn't anyone who leads like a team for networking chips.  
**Translation:** Vocabulary: semiconductor: 半导体

**[12092.00s] English:** Uh, that competes with NVIDIA, and he sent a photo of a guy checking into a first-class United flight.  
**Translation:** 

**[12097.50s] English:** From San Francisco to Shanghai or Shenzhen, with a Super Micro box that was this big, which can only  
**Translation:** Vocabulary: competes: 竞争; shanghai: 上海; shenzhen: 深圳

**[12104.70s] English:** Contains GPUs, right? And he was booking first class because, think about it, $3-5K for your.  
**Translation:** 

**[12109.70s] English:** First-class ticket server costs you about $240,000 in the US, $250,000. You sell it for $300,000 in China.  
**Translation:** 

**[12116.62s] English:** You just got a free first-class ticket and a lot more money.  
**Translation:** 

**[12120.00s] English:** So it's like, you know, and that's on a small scale. Smuggling on a larger scale is often done by companies in Singapore and Malaysia, who route them around or rent GPUs completely legally.  
**Translation:** 

**[12129.92s] English:** I want to jump in. How much is the scale? I think there's been some number, like some people with higher-level economics understanding say that as you go from 1 billion of smuggling to 10 billion, it's like you're hiding certain levels of economic activity. And that's the most reasonable thing to me: there's going to be some level where it's so obvious that it's easier to find this economic activity.  
**Translation:** 

**[12149.20s] English:** And yeah, so my belief is that last year, roughly, NVIDIA made a million H20s, which are legally allowed to be shipped to China, which we talked about is better for reasoning, right? Inference, at least—not maybe not training, but reasoning and inference—and inference generally. Then they also had, you know, a couple hundred thousand—we think 200 to 300,000 GPUs were routed to China from, you know, Singapore, Malaysia, US, wherever companies spawn up by 16 GPUs, 64 GPUs, whatever.  
**Translation:** Vocabulary: inference: 推断; routed: 转移; spawn: 涌现

**[12179.20s] English:** And Huawei is known for having spent up a massive network of companies to get the materials they need after they were banned in 2018. So it's not like otherworldly. But I agree—right? Nathan's point is, hey, you can't smuggle up $10 billion of GPUs. And then the third sort of source, which is just now banned, and you know, which wasn't considered smuggling, but is China is renting—I believe from our research, right? Oracle's biggest GPU customer is ByteDance, right? And for Google, I think it's their second-biggest customer.  
**Translation:** 

**[12209.20s] English:** Right. And so, like, as you go down the list of clouds, especially these smaller cloud companies that aren't the hyperscalers—think beyond Core, Lambda; even there's a whole sea of 60 different new cloud companies serving NVIDIA GPUs. I think ByteDance is renting a lot of these, right? All over, right? And so these companies are renting GPUs to Chinese companies. And that was completely legal up until the diffusion rules, which happened just a few weeks ago. Even now, you can rent GPU clusters that are less than 2000 GPUs, or you can buy GPUs.  
**Translation:** Vocabulary: clusters: GPU集群; diffusion: 扩散; hyperscalers: 超大规模云服务商; lambda: Lambda函数; otherworldly: 不现实; smuggle: 走私; smuggling: 走私

**[12239.20s] English:** And  
**Translation:** 

**[12240.00s] English:** Ship them wherever you want if they're less than 1,500 GPUs, right? So it's like there are.  
**Translation:** 

**[12244.32s] English:** Still, there are still some ways to smuggle, but yeah, it's not you know as effective as the numbers grow, right?  
**Translation:** 

**[12249.84s] English:** NVIDIA had revenues of around $100 billion last year, and about $200 billion this year.  
**Translation:** Vocabulary: revenues: 收入

**[12253.80s] English:** Right, and if next year, you know, it could nearly double again, or more than double.  
**Translation:** 

**[12258.98s] English:** Right, based on like what we see with data center footprints being built out all across the  
**Translation:** Vocabulary: footprints: 数据中心规模

**[12263.02s] English:** It's going to be really hard for China to keep up with these rules, especially compared to the U.S. and the rest of the world.  
**Translation:** 

**[12267.60s] English:** Right, yes, there will always be smuggling. Um, and deep-seek-level models of GDP4-level models.  
**Translation:** 

**[12272.98s] English:** Uh-oh, one-level models capable of training on what China can get, even for the next year; above that, but  
**Translation:** 

**[12278.30s] English:** If we speed-run a couple more, you know, jumps right to billion-dollar models (10 billion).  
**Translation:** 

**[12284.34s] English:** Dollar models, then it becomes, you know, hey, there is a computational disadvantage for China in training.  
**Translation:** 

**[12288.66s] English:** Models and serving them, and the serving part is really critical. Right? DeepSeek cannot serve.  
**Translation:** 

**[12293.26s] English:** Their model is completely out of inventory, right? It's already started.  
**Translation:** 

**[12297.52s] English:** For the next year, right? So, it's going to be really hard for China to keep up with these.  
**Translation:** 

**[12297.58s] English:** Falling in the App Store actually downloads because, when you download it, you try and sign up.  
**Translation:** 

**[12301.52s] English:** They say we're not taking registrations because they have no capacity. Right? You open it up, you...  
**Translation:** Vocabulary: downloads: 下载; registrations: 注册

**[12304.78s] English:** Get like less than five tokens per second if you even get your request approved, right? Because  
**Translation:** 

**[12308.78s] English:** There's just no capacity because they just don't have enough GPUs to serve the model, even though.  
**Translation:** 

**[12312.94s] English:** It's incredibly efficient. It would be fascinating to watch the smuggling, because I mean, there's drug.  
**Translation:** 

**[12317.98s] English:** Smuggling, right? That's a market. There's weapons smuggling, and GPUs will surpass that at  
**Translation:** Vocabulary: smuggling: 走私; surpass: 超越

**[12325.44s] English:** Their highest value per kilogram.  
**Translation:** 

**[12327.50s] English:** Probably by far, I have another question for you. Don't do track or model API access.  
**Translation:** 

**[12335.66s] English:** Internationally, how easy is it for Chinese companies to use hosted models of APIs from the U.S.?  
**Translation:** 

**[12341.32s] English:** Yeah, I mean, that's incredibly easy, right? Like, Open AI publicly stated that DeepSeek uses their API.  
**Translation:** 

**[12346.46s] English:** And, as they say, they have evidence, right? And this is another element of the training regime.  
**Translation:** 

**[12350.66s] English:** Is it true that people at Open AI have claimed that it's a distilled model, i.e., you're taking Open AI's model...  
**Translation:** Vocabulary: distilled: 提炼的模型

**[12356.12s] English:** You're generating a lot of output. You're generating a lot of output. You're generating a lot of output.  
**Translation:** 

**[12357.50s] English:** And then you're training on the output of their model.  
**Translation:** 

**[12360.00s] English:** And even if that's the case, what they did is still amazing, by the way—what DeepSeq did, efficiency-wise.  
**Translation:** 

**[12364.44s] English:** Distillation is a standard practice in industry. Whether or not you are at a closed lab where you care about terms of service and IP closely, you may distill from your own models.  
**Translation:** Vocabulary: distill: 提炼; distillation: 蒸馏

**[12372.12s] English:** If you are a researcher and you're not building any products, you distill insights from the early-stage models.  
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

**[12396.06s] English:** But for supervised fine-tuning, for preference data, you need to have some completions that the model is trying to learn to imitate.  
**Translation:** 

**[12402.96s] English:** And what you do there is, instead of using human data or the model you're currently training, you take completions from a different, normally more powerful model.  
**Translation:** Vocabulary: completions: 完成句

**[12412.68s] English:** I think there are rumors that these big models people are waiting for.  
**Translation:** 

**[12417.22s] English:** These GPT-5s and CLAWD-3 opuses, which are used internally at OpenAI, are employed for this distillation process.  
**Translation:** Vocabulary: internally: 内部使用; opuses: 专著

**[12424.50s] English:** There are also public examples, right?  
**Translation:** 

**[12426.06s] English:** Like Meta explicitly stated, not necessarily distilling, but they used 405B as a reward model for 70B in their LAMA 3.2 and 3.3.  
**Translation:** Vocabulary: explicitly: 明确地

**[12435.10s] English:** This is all the same topic.  
**Translation:** 

**[12436.70s] English:** So, is this ethical?  
**Translation:** 

**[12439.66s] English:** Is this legal?  
**Translation:** 

**[12440.36s] English:** Why is that Financial Times article headline saying "OpenAI says that"?  
**Translation:** 

**[12446.70s] English:** There's evidence that China's deepfake was used to train a competitor.  
**Translation:** 

**[12451.54s] English:** This is a long history, at least in the academic and research sides, because you're trying to interpret OpenAI's rules.  
**Translation:** Vocabulary: deepfake: 深度合成; interpret: 解释

**[12457.94s] English:** OpenAI's terms of service say that you cannot build a competitor using outputs from their model.  
**Translation:** 

**[12463.26s] English:** Terms of service are different from a license, which are essentially a contract between organizations.  
**Translation:** Vocabulary: outputs: 输出结果

**[12467.94s] English:** So, if you have a terms of service on OpenAI's account, and I violate it, OpenAI can cancel my account.  
**Translation:** 

**[12472.98s] English:** This is very different from a license that says how you could use a downstream artifact.  
**Translation:** Vocabulary: artifact: 下游产品; downstream: 下游的; violate: 违反

**[12476.70s] English:** So, a lot of it hinges on a word that is very unclear in the AI space.  
**Translation:** 

**[12480.00s] English:** Which is what a competitor is.  
**Translation:** Vocabulary: hinges: 取决于

**[12481.60s] English:** And then the ethical aspect of it is like:  
**Translation:** 

**[12484.52s] English:** Why is it unethical for me to train on your model?  
**Translation:** Vocabulary: unethical: 不道德的

**[12487.04s] English:** When can you train on the Internet's text?  
**Translation:** 

**[12489.14s] English:** Yeah.  
**Translation:** 

**[12489.52s] English:** Right?  
**Translation:** 

**[12489.98s] English:** So, there's a bit of a hypocrisy.  
**Translation:** Vocabulary: hypocrisy: 虚伪

**[12491.70s] English:** Because, sort of, OpenAI.  
**Translation:** 

**[12494.02s] English:** And potentially, most of the companies.  
**Translation:** 

**[12496.86s] English:** Trained on the Internet's text without permission.  
**Translation:** 

**[12500.20s] English:** There's also a clear loophole.  
**Translation:** Vocabulary: loophole: 漏洞

**[12501.44s] English:** Which is that I generate data from OpenAI.  
**Translation:** 

**[12504.74s] English:** And then I upload it somewhere.  
**Translation:** 

**[12506.72s] English:** And then somebody else trains on it.  
**Translation:** 

**[12508.38s] English:** And the link has been broken.  
**Translation:** 

**[12510.00s] English:** Like, they're not under the same terms of service contract.  
**Translation:** 

**[12513.10s] English:** This is why....  
**Translation:** 

**[12513.76s] English:** There's a lot of hip-hop.  
**Translation:** 

**[12514.80s] English:** There's a lot of interesting details to be discovered.  
**Translation:** 

**[12517.24s] English:** That doesn't make a lot of sense.  
**Translation:** 

**[12518.52s] English:** This is why a lot of models today,  
**Translation:** 

**[12520.54s] English:** Even if they train on zero OpenAI data,  
**Translation:** 

**[12522.92s] English:** You ask the model who trained you.  
**Translation:** 

**[12524.82s] English:** It will say, "I am Chad GPT, trained by OpenAI.  
**Translation:** 

**[12527.10s] English:** Because there's so much copying and pasting.  
**Translation:** 

**[12529.28s] English:** Of, like, open-source outputs from that on the internet.  
**Translation:** 

**[12532.02s] English:** That you just weren't able to filter it out.  
**Translation:** 

**[12533.76s] English:** And there was nothing in the URL.  
**Translation:** 

**[12535.38s] English:** Where they implemented, like,  
**Translation:** Vocabulary: implemented: 执行了

**[12537.04s] English:** Hey, like, for post-training or SFT.  
**Translation:** 

**[12539.04s] English:** Whatever that says,  
**Translation:** 

**[12539.84s] English:** Hey,  
**Translation:** 

**[12540.00s] English:** I'm actually a model by Allen Institute.  
**Translation:** 

**[12542.52s] English:** Instead of OpenAI.  
**Translation:** 

**[12543.70s] English:** We have to do this if we serve a demo.  
**Translation:** 

**[12545.60s] English:** We do research, and we use OpenAI APIs.  
**Translation:** 

**[12548.08s] English:** Because it's useful.  
**Translation:** 

**[12548.80s] English:** And we want to understand post-training.  
**Translation:** 

**[12550.28s] English:** And, like our research models,  
**Translation:** 

**[12552.08s] English:** They will say they are written by OpenAI.  
**Translation:** 

**[12553.56s] English:** Unless we put in the system property,  
**Translation:** 

**[12555.22s] English:** That we talked about, like,  
**Translation:** 

**[12556.34s] English:** I am Tulu.  
**Translation:** 

**[12557.04s] English:** I am a language model trained.  
**Translation:** 

**[12558.20s] English:** By the Allen Institute for AI.  
**Translation:** 

**[12559.92s] English:** And if you ask more people around the industry,  
**Translation:** 

**[12562.48s] English:** Especially with post-training,  
**Translation:** 

**[12563.64s] English:** It's a very doable task.  
**Translation:** 

**[12565.28s] English:** To make the model say, "Who it is.  
**Translation:** Vocabulary: doable: 可行的

**[12567.54s] English:** Or to suppress the OpenAI thing.  
**Translation:** 

**[12569.30s] English:** So, at some levels,  
**Translation:** Vocabulary: suppress: 压制

**[12570.98s] English:** It might be that DeepSeq didn't care.  
**Translation:** 

**[12572.82s] English:** That it was saying that it was by OpenAI.  
**Translation:** 

**[12574.72s] English:** Like, if you're going to upload model weights,...  
**Translation:** 

**[12576.54s] English:** It doesn't really matter.  
**Translation:** 

**[12577.22s] English:** Because anyone serving it in an application  
**Translation:** 

**[12579.46s] English:** And he cares a lot about serving.  
**Translation:** 

**[12581.22s] English:** Is going to,  
**Translation:** 

**[12582.44s] English:** When serving it,  
**Translation:** 

**[12583.48s] English:** If they're using it for a specific task,  
**Translation:** 

**[12585.24s] English:** They're going to tailor it to that.  
**Translation:** Vocabulary: tailor: 量身定制

**[12586.26s] English:** And it doesn't matter.  
**Translation:** 

**[12586.84s] English:** That's saying it's ChatGPT.  
**Translation:** 

**[12588.94s] English:** Oh, I guess one of the ways to do that is to...  
**Translation:** 

**[12590.86s] English:** It's like a system prompt, or something like that.  
**Translation:** Vocabulary: prompt: 提示

**[12592.66s] English:** Like, if you're serving it, to say that you're...  
**Translation:** 

**[12595.08s] English:** That's what we do.  
**Translation:** 

**[12596.08s] English:** Like, if we host the demo,  
**Translation:** 

**[12596.92s] English:** You say you are Tulu 3.  
**Translation:** 

**[12599.30s] English:** A language model....  
**Translation:** 

**[12600.00s] English:** Model trained by the Allen Institute for AI, we are also benefited from OpenAI data because it's  
**Translation:** Vocabulary: benefited: 受益

**[12605.26s] English:** A great research tool, I mean, do you think there's any truth and value to the claim Open?  
**Translation:** 

**[12612.46s] English:** AI's claim that there's evidence China deeply sought to use this model to train. I think.  
**Translation:** 

**[12616.56s] English:** Everyone has benefited, regardless, because the data is on the Internet, and therefore it's available.  
**Translation:** 

**[12622.90s] English:** Your portrayal now, right? There are like subreddits where people share the best Chat GPT outputs and...  
**Translation:** Vocabulary: outputs: 结果; portrayal: 形象; subreddits: 论坛

**[12627.52s] English:** Those are, I think, in your mind, and they're trying to ship the narrative, like they're trying.  
**Translation:** 

**[12632.50s] English:** To protect themselves, and we saw this years ago when TikTok was actually banned in some countries.  
**Translation:** 

**[12637.04s] English:** Open AI APIs for training on outputs: there are other AI startups that most people, if you're in the like  
**Translation:** 

**[12643.10s] English:** AI culture were like, they just told us they trained on Open AI outputs and they never got  
**Translation:** Vocabulary: startups: 初创公司

**[12647.74s] English:** Banned, like that's how they bootstrapped their early models, so it's much easier to get off the ground.  
**Translation:** 

**[12652.42s] English:** Grounding using this is better than setting up human pipelines and building a strong model, so there's a long history.  
**Translation:** Vocabulary: bootstrapped: 自我提升; pipelines: 信息渠道

**[12657.50s] English:** Here, and a lot of the communications seem like narratives, actually, like the ones over the last.  
**Translation:** 

**[12662.04s] English:** Couple of days we've seen a lot of people distill the DeepSeek model into the Llama model because the  
**Translation:** Vocabulary: distill: 提炼; llama: 羊驼; narratives: 叙述

**[12667.32s] English:** Deep seek models are kind of complicated to run inference on because they're a mixture of experts.  
**Translation:** 

**[12671.18s] English:** And they're, you know, 600-plus billion parameters, and all this, and people distilled them into the  
**Translation:** Vocabulary: distilled: 提炼; inference: 推断; mixture: 混合物

**[12675.62s] English:** Llama models, and then, because the llama models are so easy to serve, and everyone's built the  
**Translation:** 

**[12679.28s] English:** Pipelines and tooling for inference with the Llama models, right? Because it's the open standard.  
**Translation:** 

**[12683.18s] English:** Uh, so you know, we've seen it—we've seen a sort of roundabout, right? Is it...  
**Translation:** 

**[12687.50s] English:** Bad? Is it illegal, maybe it's illegal. Whatever, I don't know about that, but like, it could break.  
**Translation:** 

**[12691.52s] English:** Contracts: I don't think it's illegal; like, no one's going to jail for this.  
**Translation:** 

**[12695.54s] English:** I think, fundamentally, I think it's ethical, or I hope it's ethical, because like the moment  
**Translation:** Vocabulary: fundamentally: 从根本上

**[12701.48s] English:** Becomes, we ban that kind of thing, it's going to make everybody much worse off, and I also actually  
**Translation:** 

**[12709.46s] English:** It's difficult, but I think you should be allowed to train on the Internet, I.  
**Translation:** 

**[12715.34s] English:** Know a lot of authors and creators are very sensitive.  
**Translation:** 

**[12717.50s] English:** About it, that's a difficult question, but  
**Translation:** 

**[12720.00s] English:** The moment you're not allowed to train on the internet.  
**Translation:** 

**[12723.22s] English:** I agree.  
**Translation:** 

**[12723.80s] English:** I have a schizophrenic take on how you can solve this because it already works.  
**Translation:** 

**[12727.18s] English:** I have a reasonable take on it.  
**Translation:** Vocabulary: schizophrenic: 矛盾的

**[12728.92s] English:** All right.  
**Translation:** 

**[12729.90s] English:** So, you know, Japan has a law which allows you to train on any training data, and  
**Translation:** 

**[12735.80s] English:** Copyrights don't apply if you want to train a model.  
**Translation:** 

**[12737.84s] English:** A. B. Japan has nine gigawatts of curtailed nuclear power.  
**Translation:** Vocabulary: copyrights: 版权; curtailed: 削减; gigawatts: 吉瓦

**[12743.04s] English:** C. Japan is allowed under the AI diffusion rule to import as many GPUs as they would like.  
**Translation:** 

**[12748.32s] English:** Like, so all we have to do is make a market here.  
**Translation:** Vocabulary: diffusion: 扩散; import: 进口

**[12751.08s] English:** We build massive data centers.  
**Translation:** 

**[12752.74s] English:** We rent them to the labs.  
**Translation:** 

**[12754.30s] English:** And then we train models in a legally permissible way.  
**Translation:** 

**[12757.14s] English:** And there's no ifs, ands, or buts.  
**Translation:** Vocabulary: permissible: 允许的

**[12758.72s] English:** And now, the models have no potential copyright lawsuit from The New York Times or anything.  
**Translation:** 

**[12763.92s] English:** Like that.  
**Translation:** Vocabulary: lawsuit: 诉讼

**[12764.34s] English:** No, no.  
**Translation:** 

**[12764.56s] English:** It's just, like, completely legal.  
**Translation:** 

**[12765.84s] English:** No, so, so, so.  
**Translation:** 

**[12767.78s] English:** The early copyright lawsuits have fallen in favor of AI training.  
**Translation:** Vocabulary: lawsuits: 诉讼

**[12771.62s] English:** I would say that the long tail of usage is going to favor AI, which is if you do  
**Translation:** 

**[12778.02s] English:** This.  
**Translation:** 

**[12778.32s] English:** If you scrape trillions of data, you're not looking at trillions of tokens of data.  
**Translation:** 

**[12782.18s] English:** You're not looking and saying, "This one New York Times article is so important to me.  
**Translation:** Vocabulary: scrape: 抓取; trillions: 万亿

**[12786.82s] English:** But if you're doing audio generation for music or image generation, and you say, "make  
**Translation:** 

**[12791.04s] English:** It would be in the style of X person, that's a reasonable case where you could figure out what is their  
**Translation:** 

**[12795.78s] English:** Profit margin on inference.  
**Translation:** 

**[12798.20s] English:** I don't know if it's going to be a 50-50 split in the YouTube Creator Program or something, but...  
**Translation:** Vocabulary: margin: 利润 margin 利润率

**[12802.46s] English:** I would opt into that program as a writer.  
**Translation:** 

**[12804.94s] English:** Like, please, like that.  
**Translation:** 

**[12806.96s] English:** It's just, it's.  
**Translation:** 

**[12808.32s] English:** It's going to be a rough journey, but there will be some solutions like that that make.  
**Translation:** 

**[12812.26s] English:** Sense.  
**Translation:** 

**[12812.66s] English:** But there's a long tail where it's just on the Internet.  
**Translation:** 

**[12815.94s] English:** I think one of the other aspects of that Financial Times article implied, and so that leads to...  
**Translation:** 

**[12821.98s] English:** A more general question.  
**Translation:** Vocabulary: implied: 含蓄地表示

**[12822.96s] English:** Do you think there's how difficult it is to carry out spying, espionage, and the stealing of actual secret codes?  
**Translation:** 

**[12831.20s] English:** And data from inside companies?  
**Translation:** Vocabulary: espionage: 间谍活动

**[12833.76s] English:** How much of that is being attempted?  
**Translation:** 

**[12835.24s] English:** Code and data are hard, but ideas are easy.  
**Translation:** 

**[12837.42s] English:** Silicon Valley.  
**Translation:** 

**[12838.32s] English:** Silicon Valley operates on the.  
**Translation:** 

**[12840.00s] English:** The way that top employees get bought out by other companies for a pay raise, and a large reason why.  
**Translation:** 

**[12846.16s] English:** These companies do this by bringing ideas with them, and there's no real reason to doubt that in California.  
**Translation:** Vocabulary: california: 加利福尼亚州

**[12851.36s] English:** There's rules, like certain non-competes or whatever, that are illegal in California, and whether  
**Translation:** 

**[12856.24s] English:** Or, not there's NDAs and things that is how a lot of it processes happen. Recently, there was somebody.  
**Translation:** 

**[12861.44s] English:** From Gemini, who helped make this one million contacts long, and everyone is saying the next...  
**Translation:** 

**[12866.80s] English:** Llama, who I mean, he went to the Meta team, is gonna have one million contacts, and that's kind.  
**Translation:** Vocabulary: gemini: 双子座; llama: 羊驼

**[12872.48s] English:** Of how the world works, you know, as far as industrial espionage and things like that have been.  
**Translation:** 

**[12877.76s] English:** Greatly successful in the past, right? Um, you know, the Americans did it for the Brits.  
**Translation:** Vocabulary: brits: 英国人

**[12882.24s] English:** Uh, the Chinese have done it to the Americans, right? And you know, so on and so forth; it's just...  
**Translation:** 

**[12886.16s] English:** It is a fact of life, um, and so to argue that industrial espionage can be stopped is probably  
**Translation:** 

**[12893.20s] English:** Unlikely, you can make it difficult, but even then, like, there are all these stories about like  
**Translation:** 

**[12896.80s] English:** Hey, F-35 and F-22 have already been, more or less, given to China in terms of design plans.  
**Translation:** 

**[12901.44s] English:** And stuff, um, code and stuff like that—between you know, I say companies, not nation states—is probably very  
**Translation:** 

**[12907.36s] English:** Difficult, um, but ideas are discussed a lot, right? Whether it be a house party in San Francisco.  
**Translation:** 

**[12913.60s] English:** Or, for a company changing employees, or you know, or the always-mythical honey.  
**Translation:** 

**[12919.44s] English:** Pot that always gets talked about, right? Like someone gets honey-potted, right? Uh, because  
**Translation:** 

**[12923.20s] English:** Everyone working on AI is a single dude who's in his 20s and 30s.  
**Translation:** 

**[12926.80s] English:** Not everyone, but like an insane amount of insane percentages, um, so there's always like all these.  
**Translation:** Vocabulary: percentages: 比例极高

**[12932.24s] English:** Like, you know, and obviously, so Honey Potter is like a spy—a female spy approaches you, and like  
**Translation:** 

**[12938.56s] English:** Yeah, yeah, or maybe a guy, right? You know, it's San Francisco, right? But as a single dude, I'll  
**Translation:** Vocabulary: approaches: 靠近

**[12944.80s] English:** Say, in his late 20s, right, is like we are very easily corrupted, right? Like, you know.  
**Translation:** 

**[12950.16s] English:** Corrupted myself, but you know, like, we are — we are, right? Everybody else, not me. Yeah, I'm too oblivious.  
**Translation:** Vocabulary: corrupted: 堕落; oblivious: 无知

**[12956.80s] English:** I'm safe from one espionage access.  
**Translation:** 

**[12960.00s] English:** Yeah, you have to make sure to close all security vulnerabilities. So, you, Dylan, collect a lot of information about each of the megaclusters for each of the major AI companies. Can you talk about the buildouts for each one that stand out?  
**Translation:** Vocabulary: buildouts: 建设方案; espionage: 间谍活动; megaclusters: 超集群; vulnerabilities: 漏洞

**[12977.60s] English:** Yeah. So I think the thing that's really important about these megacluster buildouts is they're completely unprecedented in scale, right? In the U.S., you know, data center power consumption has been slowly on the rise and it's gone up to 2-3% even through the cloud computing revolution, right? Data center consumption as a percentage of total U.S. energy use has been climbing slowly over decades, right? But now at 2-3%, by the end of this decade, it's like—it's going to be even higher, right?  
**Translation:** 

**[13007.60s] English:** Like 10, a lot of people that are traditionally by around 2028-2030, people traditionally non.  
**Translation:** Vocabulary: computing: 计算; megacluster: 大规模集群; unprecedented: 前所未有的

**[13013.38s] English:** A traditional data center, people like that's nuts, but then people who are in AI, who  
**Translation:** 

**[13018.98s] English:** Have you really looked at this at all, like the Anthropic and OpenAI stuff? That's not...  
**Translation:** 

**[13022.16s] English:** Enough, and I'm like, okay, but like, you know, this is both through a globally distributed  
**Translation:** 

**[13028.36s] English:** Uh, and they are either distributed throughout the U.S., as well as like centralized clusters, right?  
**Translation:** Vocabulary: clusters: 集中群; globally: 全球地

**[13032.74s] English:** Distributed throughout the U.S., it's both exciting and makes up the bulk of it, right? Like, hey, you know.  
**Translation:** 

**[13037.30s] English:** Uh, Open AI or, you know, like Meta is adding a gigawatt, right? But most of it is distributed.  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[13044.22s] English:** Through the U.S. for inference, and all these other things. Right? So, maybe we should lay out what a  
**Translation:** 

**[13048.64s] English:** What a cluster is, so, you know, does this include AWS? Maybe it's good to talk about that.  
**Translation:** Vocabulary: cluster: 聚类; inference: 推断

**[13055.20s] English:** Different kinds of clusters, and what you mean by mega-clusters, and what's a GPU, and what's  
**Translation:** 

**[13059.36s] English:** The computer and what, yeah—not that far back—but yeah, so like, what do we mean by the clusters?  
**Translation:** 

**[13065.02s] English:** No, man. I thought I was about to do the Apple ad, right?  
**Translation:** 

**[13067.30s] English:** What's a computer, so traditionally, data centers and data center tasks have been a  
**Translation:** 

**[13074.56s] English:** A distributed systems problem that is capable of being spread very far and widely, right?  
**Translation:** 

**[13080.00s] English:** I.e., I send a request to Google; it gets routed to a data center somewhat close to me, it does whatever search-ranking recommendation, sends a result back, right?  
**Translation:** Vocabulary: recommendation: 建议; routed: 路由

**[13090.64s] English:** The nature of the task is changing rapidly, as there are now two specific tasks that people are really focused on, right?  
**Translation:** 

**[13096.60s] English:** It's not about database access; it's not about serving me the right page or ad.  
**Translation:** 

**[13100.26s] English:** It's now: A, inference.  
**Translation:** 

**[13102.86s] English:** And inference is dramatically different from traditional distributed systems, but it looks a lot more similar.  
**Translation:** Vocabulary: dramatically: 显著地

**[13106.80s] English:** And then there's training, right?  
**Translation:** 

**[13109.10s] English:** The inference side is still like, "Hey, I'm going to put thousands of GPUs and blocks all around these data centers. I'm going to run models on them. User submits a request, gets kicked off— or hey, my service: they submit a request to my service, right?  
**Translation:** Vocabulary: submit: 提交

**[13124.28s] English:** They're on Word, and they're like, "Oh, yeah, help me Copilot," and it kicks it off. Or I'm on my Windows Copilot, or whatever, Apple Intelligence, whatever it is—it gets kicked off to a data center, right?  
**Translation:** 

**[13131.92s] English:** And that data center does some work and sends it back—that's inference—and that is going to be the bulk of the compute, but then...  
**Translation:** Vocabulary: compute: 计算; copilot: 协作者; inference: 推断

**[13139.10s] English:** And that's like, there are thousands of data centers that we're tracking with satellites and all these other things, and those are the bulk of what's being built, but the scale of...  
**Translation:** 

**[13148.22s] English:** And so that's what's really reshaping, and that's what's getting millions of GPUs, but the scale of the largest cluster is also really important, right?  
**Translation:** Vocabulary: cluster: 大规模计算集群; reshaping: 重塑

**[13156.82s] English:** When we look back at history, or through the age of AI, it was a really big deal when they did AlexNet on, I think, two to four GPUs, I don't remember.  
**Translation:** 

**[13169.10s] English:** It was a really big deal.  
**Translation:** 

**[13170.06s] English:** It's a big deal because you used GPUs.  
**Translation:** 

**[13171.76s] English:** It's a big deal; they used GPUs, and they used multiple, right?  
**Translation:** 

**[13174.66s] English:** But then, over time, its scale has just been compounding, right?  
**Translation:** 

**[13178.24s] English:** And so when you skip forward to GPT-3, then GPT-4, with 20,000 A100 GPUs, it was an unprecedented run, right, in terms of both its size and the cost, right?  
**Translation:** Vocabulary: compounding: 累积; unprecedented: 前所未有的

**[13188.18s] English:** A couple hundred million dollars on a YOLO, right? A YOLO run for GPT-4, and it yielded this magical improvement that was perfectly in line with what was experimented with, just a log-scale increase, right?  
**Translation:** 

**[13198.78s] English:** Oh, yeah.  
**Translation:** Vocabulary: experimented: 实验; yielded: 产生

**[13199.10s] English:** They have that plot.  
**Translation:** 

**[13200.00s] English:** From the paper, the technical report, the scaling laws were perfect, right? But that's not a crazy.  
**Translation:** 

**[13205.20s] English:** Number right, 20,000 A100s; uh, roughly, each GPU is consuming 400 watts; uh, and then when you add in,...  
**Translation:** 

**[13211.52s] English:** The whole server, right? Everything—it's like 15 to 20 megawatts of power, right? You know.  
**Translation:** Vocabulary: megawatts: 兆瓦; watts: 瓦

**[13217.58s] English:** You know, maybe you could look up what the power consumption of a human person is, because the  
**Translation:** 

**[13221.84s] English:** Numbers are gonna get silly, but like, 15 to 20 megawatts was standard for a data center size; it was  
**Translation:** 

**[13226.36s] English:** Just unprecedented: that was all GPUs, running one tap. It was a toaster—the toaster is like it's a  
**Translation:** 

**[13232.14s] English:** A good example of similar power consumption to an A100 is the H100; as they increase the power,  
**Translation:** 

**[13237.44s] English:** From about 400 to 700 watts, and that's just per GPU, and then there's all the associated stuff.  
**Translation:** 

**[13241.38s] English:** Around it, so once you count all that, it's roughly like 1,200 to 1,400 watts for everything networking.  
**Translation:** 

**[13246.84s] English:** CPUs, memory: blah, blah, blah. So, we should also say, "What's required?" You said power, so a lot of...  
**Translation:** 

**[13253.96s] English:** Power is required, a lot of heat is generated.  
**Translation:** 

**[13256.36s] English:** Cooling is required, and because there are a lot of GPUs, CPUs, or whatever they are, that need it.  
**Translation:** 

**[13263.90s] English:** Have to be connected, so there's a lot of networking, yeah. Yeah, so I think... Sorry for skipping.  
**Translation:** Vocabulary: skipping: 跳过

**[13268.92s] English:** Past that, and then the data center itself is like complicated, right? But these are still...  
**Translation:** 

**[13273.04s] English:** Standardized data centers for GPD4 scale—right now, we step forward to sort of determine what the scale will be.  
**Translation:** Vocabulary: standardized: 规范化的

**[13279.28s] English:** Of clusters that people built last year, right, and it ranges widely, right? It ranges from like  
**Translation:** 

**[13285.22s] English:** Hey, these are standard.  
**Translation:** Vocabulary: clusters: 聚类

**[13286.30s] English:** GPUs memory, blah, blah, blah, and then it ranges from, like, "hey, these are standard.  
**Translation:** 

**[13286.34s] English:** Data centers, and we're just using multiple of them and connecting them together, really.  
**Translation:** 

**[13289.80s] English:** With a ton of fiber between them, a lot of networking, etc., that's what Open AI and Microsoft are focusing on.  
**Translation:** 

**[13293.90s] English:** Did they do something in Arizona, right? And so they have a you know, 100,000 GPUs, right, like Meta did, and they took...  
**Translation:** Vocabulary: arizona: 亚利桑那州

**[13298.68s] English:** Their standard existing data center design, um, and it looks like an H, and they connected multiple.  
**Translation:** 

**[13302.96s] English:** Of them together, um, and you know, they got to do it with 16,000 GPUs, uh, 24,000 GPUs total.  
**Translation:** 

**[13309.12s] English:** Only 16 of them, out of thousands, were running on the training run because GPUs are very unreliable.  
**Translation:** 

**[13313.16s] English:** So, they need to have spares to like swap in and out, all the way to like now.  
**Translation:** Vocabulary: spares: 备用件; unreliable: 不可靠

**[13316.28s] English:** Hundred thousand GPUs that they're training on LLaMA 4, currently, right? Like a hundred.  
**Translation:** 

**[13320.00s] English:** 128,000 or so, right? This is, you know, like thinking about 100,000 GPUs with roughly 1,400 watts each.  
**Translation:** Vocabulary: watts: 瓦

**[13327.70s] English:** Piece. That's that's 140 megawatts, 150 megawatts, right? For $128,000, right? So you're  
**Translation:** 

**[13333.26s] English:** Talking about, you've jumped from 15 to 20 megawatts to almost 10 times that.  
**Translation:** Vocabulary: megawatts: 兆瓦

**[13337.88s] English:** Number 9x that number to 150 megawatts in two years, right? From 2022 to 2024, right? And  
**Translation:** 

**[13344.76s] English:** Some people like Elon, he admittedly says, right? And he says himself that he got into the game a little bit.  
**Translation:** Vocabulary: admittedly: 坦白地说

**[13349.80s] English:** Late for pre-training large language models, right? XAI was started later, right? But then,...  
**Translation:** 

**[13353.92s] English:** He bet heaven and hell to get his data center up and running and get the largest cluster in the world.  
**Translation:** Vocabulary: cluster: 大规模计算集群

**[13358.38s] English:** Right? Which is 200,000 GPUs. And he did that—he bought a factory in Memphis.  
**Translation:** 

**[13363.98s] English:** He's upgrading the substation, but at the same time, he's got a bunch of mobile power.  
**Translation:** Vocabulary: memphis: 美国田纳西州的港口城市; substation: 变电站; upgrading: 升级

**[13368.00s] English:** Generation: A bunch of single-cycle combines. He tapped the natural gas line that's right next to.  
**Translation:** 

**[13372.84s] English:** The factory is just pulling a ton of gas, burning it. He's generating all this power.  
**Translation:** Vocabulary: tapped: 接通

**[13377.40s] English:** He's in a factory in an old appliance factory.  
**Translation:** 

**[13379.80s] English:** That's shut down and moved to China long ago, right? Like, you know, and he's  
**Translation:** 

**[13383.30s] English:** It has 200,000 GPUs in it. And now, what's the next scale, right? Like, all the hyperscalers have done  
**Translation:** 

**[13388.36s] English:** This. Now, the next scale is something that's even bigger, right? And so, you know,  
**Translation:** Vocabulary: hyperscalers: 超大规模云服务商

**[13392.24s] English:** Elon, just to stick to the topic, he's building his own natural gas plant, like a proper one.  
**Translation:** 

**[13396.78s] English:** One right next door. He's deploying tons of Tesla Mega Pack batteries to make the power more stable.  
**Translation:** Vocabulary: deploying: 部署

**[13402.72s] English:** Smooth and all sorts of other things. He's got industrial chillers to cool the water down.  
**Translation:** 

**[13407.62s] English:** Because he's water-cooling the chips.  
**Translation:** Vocabulary: chillers: 冷水机

**[13409.80s] English:** So, all these crazy things to get the clusters bigger and bigger. But when you look at it,  
**Translation:** 

**[13414.90s] English:** Say what OpenAI did with Stargate—that's in Arizona, in Abilene, Texas, right? What?  
**Translation:** Vocabulary: abilene: 阿比林; arizona: 亚利桑那; clusters: 集群; stargate: 星门; texas: 得克萨斯

**[13422.44s] English:** They've announced it at least, right? It's not built yet, right? Elon says they don't have the money.  
**Translation:** 

**[13425.60s] English:** Know, there's some debates about this. But at full scale, at least the first section is like,  
**Translation:** 

**[13430.94s] English:** Definitely, money is accounted for, but there are multiple sections. But on a full-scale basis, that data...  
**Translation:** 

**[13434.40s] English:** The center is going to be 2.2 gigawatts, right? That's 2,200 megawatts of power. And roughly,  
**Translation:** Vocabulary: gigawatts: 吉瓦; megawatts: 兆瓦

**[13439.80s] English:** Like,  
**Translation:** 

**[13440.00s] English:** 1.8 gigawatts, or 1,800 megawatts, of power delivered to chips, right?  
**Translation:** 

**[13447.30s] English:** Now, this is an absurd scale: 2.2 gigawatts is like more than most cities, right? You know, to be clear.  
**Translation:** 

**[13452.96s] English:** Um, and it was delivered to a single cluster that's connected for training, right? To train,...  
**Translation:** Vocabulary: absurd: 荒谬; cluster: 集群

**[13459.14s] English:** These models need to do both the pre-training and post-training, all of this stuff, right?  
**Translation:** 

**[13462.12s] English:** This is insane. What is a nuclear power plant, again? Everyone is doing this, right? Everyone is doing  
**Translation:** 

**[13467.42s] English:** Meta, meta, in Louisiana, right? They're building two massive natural gas plants, and they're  
**Translation:** 

**[13473.90s] English:** And then they're building this massive data center. Um, Amazon has like plans for this scale, uh, and Google...  
**Translation:** 

**[13479.70s] English:** Has plans for this scale, uh, Xai has plans for this scale, right? Like, all of these guys that...  
**Translation:** 

**[13485.72s] English:** Are racing the companies that are racing hard, and they're doing multi-gigawatt.  
**Translation:** 

**[13490.28s] English:** Data centers, right? Um, to build this out because they think that, yeah, if I now have you.  
**Translation:** 

**[13497.42s] English:** See, pre-training scaling is going to continue, but to some extent, but then also all this post-training.  
**Translation:** 

**[13501.16s] English:** Stuff, where you have an RL sandbox for computer use or whatever, right? Like, you know, this is where.  
**Translation:** 

**[13505.30s] English:** They're going to, and all these are fearful about viable domains where they just keep learning.  
**Translation:** Vocabulary: fearful: 害怕的; sandbox: 测试环境; viable: 可行的

**[13508.26s] English:** And learning, self-play, and whatever it is, makes AI so much more capable.  
**Translation:** 

**[13512.48s] English:** Because the line does go up, right? As you throw more compute, you get more performance. The shirt is.  
**Translation:** Vocabulary: compute: 计算能力

**[13517.42s] English:** About scaling laws, um, you know, to some extent, it is diminishing returns, right? You 10x the compute,...  
**Translation:** 

**[13522.16s] English:** You don't get 10x better model; right? You get diminishing returns, but also you get efficiency.  
**Translation:** Vocabulary: diminishing: 递减的

**[13526.56s] English:** Improvements, so you're better, you're better, you're better, you're better, you're better.  
**Translation:** 

**[13527.42s] English:** The curve, right? Um, and these large-scale data centers are doing you know, wreaking a lot of havoc.  
**Translation:** Vocabulary: havoc: 混乱; wreaking: 造成

**[13533.36s] English:** Havoc on the network, right? And you know, Nathan was mentioning that Amazon has tried to buy...  
**Translation:** 

**[13538.32s] English:** This nuclear power plant, Talon, and if you look at Talon stock, it's just skyrocketing.  
**Translation:** Vocabulary: skyrocketing: 飙升; talon: 塔伦

**[13543.12s] English:** And, um, you know, like they're building a massive multi-gigawatt data center there, and you know,  
**Translation:** 

**[13547.18s] English:** You just go down the list; there are so many ramifications. An interesting thing is that certain  
**Translation:** Vocabulary: ramifications: 影响

**[13551.16s] English:** Regions of the U.S. transmitting power cost more than actually generating it, right? Because the  
**Translation:** 

**[13557.42s] English:** The grid is so slow to build, and the demand for power...  
**Translation:** Vocabulary: transmitting: 传输

**[13560.00s] English:** And the ability to build power and, like, ramping up on a natural gas plant, or even a coal plant.  
**Translation:** 

**[13563.84s] English:** Plants are pretty easy to do, but transmitting the power is really hard. So in  
**Translation:** Vocabulary: ramping: 增加

**[13567.40s] English:** In some parts of the U.S., like in Virginia, it costs more to transmit power than it costs to generate.  
**Translation:** 

**[13572.30s] English:** It, which is like, you know, there are all sorts of second-order effects that are insane.  
**Translation:** Vocabulary: transmit: 传输

**[13576.02s] English:** Here, can the power grid support this kind of growth? You know, Trump's executive orders,  
**Translation:** 

**[13580.36s] English:** There's an Biden executive order before the end of the year, but then Trump had some.  
**Translation:** 

**[13583.66s] English:** More executive orders, which hopefully reduce the regulations to where things can be built again.  
**Translation:** 

**[13590.00s] English:** Um, but yeah, this is a big, big challenge, right? Is building enough power fast enough?  
**Translation:** 

**[13594.00s] English:** Are you going to basically have a nuclear power plant next to a data center for each one of these?  
**Translation:** 

**[13598.52s] English:** So, the fun thing here is that it's too slow to build the power plant. Or  
**Translation:** 

**[13604.54s] English:** To reconfigure an existing power plant is too slow. And so, therefore, you must use natural gas.  
**Translation:** 

**[13611.06s] English:** Center power consumption is flat, right? You know, like, it's why nuclear is also...  
**Translation:** Vocabulary: reconfigure: 重新配置

**[13614.74s] English:** Good for it. Like, long-term nuclear is a very natural fit. But yeah, it's short; you can't.  
**Translation:** 

**[13619.98s] English:** Do solar or anything else in the short term? Like, that is how data center power works, right?  
**Translation:** 

**[13624.14s] English:** You're telling me: I'm going to buy tens of billions of dollars' worth of GPUs and idle them because...  
**Translation:** 

**[13629.64s] English:** The power is not being generated, like power is cheap, right? Like, if you look at the cost of a  
**Translation:** 

**[13632.76s] English:** Cluster: Less than 20% of it is power, right? Most of it is the capital costs and depreciation.  
**Translation:** 

**[13638.64s] English:** GPUs, right? And so it's like, well, screw it. I'll just, you know, I'll just build natural.  
**Translation:** Vocabulary: cluster: 聚类; depreciation: 折旧

**[13642.78s] English:** Gas plants. This is what Meta is doing in Louisiana. This is what OpenAI is doing in Texas.  
**Translation:** 

**[13646.76s] English:** And, like all these different places, they may not be doing it directly.  
**Translation:** Vocabulary: texas: 德克萨斯州

**[13649.98s] English:** But they are partnered with someone. And so there are a few hopes, right? Like one is,  
**Translation:** 

**[13655.22s] English:** You know, Elon, what he's doing in Memphis is like, you know, to the extreme—they're not just  
**Translation:** Vocabulary: memphis: 美国田纳西州最大城市

**[13658.58s] English:** Using dual combined cycle gas, which is like super efficient. He's also just using single cycle, and  
**Translation:** 

**[13663.60s] English:** Like mobile generators and stuff, which is less efficient. But he's, you know, there's also like  
**Translation:** 

**[13668.52s] English:** The flip side is that, while solar power generation works in this way, wind is another option.  
**Translation:** 

**[13672.62s] English:** Like, like this, different correlate, you know, different. So if you stack both of those,  
**Translation:** Vocabulary: correlate: 相关

**[13676.28s] English:** Plus, you get a big chunk of batteries, and plus you have a little bit of gas.  
**Translation:** 

**[13679.98s] English:** Uh-huh.  
**Translation:** 

**[13680.00s] English:** It is possible to run it more "green," but it's just that the time scales for that are slow, right? So, people are  
**Translation:** 

**[13685.22s] English:** Trying, but you know, Meta basically said, "Whatever; don't care about my sustainability pledge," or  
**Translation:** Vocabulary: pledge: 承诺

**[13692.00s] English:** They'll buy power, like a PPA (power purchasing agreement), where there will be a massive  
**Translation:** 

**[13695.96s] English:** Wind farms or solar farms, like wherever, and then they'll just pretend that those electrons are...  
**Translation:** Vocabulary: electrons: 电能; purchasing: 购买

**[13700.04s] English:** Being consumed by the data center, but in reality, they're paying for the power here and selling it.  
**Translation:** 

**[13703.66s] English:** To the grid, and they're buying power here. Um, and then another thing is that Microsoft quit on some.  
**Translation:** 

**[13708.56s] English:** Of their sustainability pledges, right? Elon, uh, what he did with Memphis is objectively somewhat  
**Translation:** 

**[13713.54s] English:** Dirty, but he's also doing it in an area where there's a bigger natural gas plant right?  
**Translation:** Vocabulary: objectively: 客观上; pledges: 承诺

**[13717.74s] English:** Next door, it's more like a sewer—or not exactly a sewer, but like a wastewater treatment plant and a garbage dump.  
**Translation:** 

**[13722.04s] English:** Nearby, right? And he's obviously made the world a lot more clean than that one data center.  
**Translation:** Vocabulary: wastewater: 废水

**[13726.50s] English:** Is going to do right, so I think it's fine to some extent, and maybe AGI solves you know, global.  
**Translation:** 

**[13732.28s] English:** Warming and stuff, right? Whatever it is, um, you know, this is this is sort of the attitude that.  
**Translation:** 

**[13736.48s] English:** People at the labs have a right, which is like, yeah.  
**Translation:** 

**[13738.56s] English:** We'll just use gas, right? Because the race is that important, and if we lose, you know, that's way worse.  
**Translation:** 

**[13743.06s] English:** Right, I should say that I got a chance to visit the Memphis data center, and it's  
**Translation:** 

**[13749.44s] English:** Kind of incredible. I mean, I visited with Elon; just the team and the rate of innovation there's  
**Translation:** Vocabulary: memphis: 孟菲斯

**[13757.68s] English:** Insane, there's. Uh, my sense is that you know, nobody's ever done anything on this scale.  
**Translation:** 

**[13762.68s] English:** And nobody has certainly ever done anything of this scale at the rate that XAI is doing.  
**Translation:** 

**[13768.56s] English:** So, they're figuring it out, and I was sitting in on all these meetings where they're  
**Translation:** 

**[13774.02s] English:** Brainstorming is like it's insane; it's exciting because they're all trying to figure out.  
**Translation:** Vocabulary: brainstorming: 头脑风暴

**[13779.42s] English:** What are the bottlenecks? How can we remove them? How can we make sure?  
**Translation:** 

**[13783.24s] English:** There are just so many really cool things about putting together a data center, because you know.  
**Translation:** Vocabulary: bottlenecks: 瓶颈

**[13789.66s] English:** Everything has to work, it's uh, the people that do, like the sysadmins, you know, the machines.  
**Translation:** 

**[13795.80s] English:** Learning all that is the exciting thing, so on, but really?  
**Translation:** Vocabulary: sysadmins: 系统管理员

**[13798.56s] English:** The people that run everything are the  
**Translation:** 

**[13800.00s] English:** The folks who know about the low-level software and hardware that runs everything,  
**Translation:** 

**[13806.42s] English:** The networking, all of that, and so you have to make sure you have procedures that test.  
**Translation:** 

**[13811.58s] English:** Everything I think they're using Ethernet, I don't know how they're doing the networking, but...  
**Translation:** Vocabulary: ethernet: 以太网

**[13815.18s] English:** They're using NVIDIA Spectrum X Ethernet. Um, there's actually, I think, yeah, the unsung  
**Translation:** 

**[13820.00s] English:** Heroes are the cooling and electrical systems, which are just like glossed-over, yeah, um, but I  
**Translation:** 

**[13825.34s] English:** Think, like, for example, one story that maybe exemplifies how insane this stuff is: uh, when  
**Translation:** 

**[13831.20s] English:** You're training, right? Um, you're always doing—you're, you're, you're running through the model.  
**Translation:** Vocabulary: exemplifies: 作为例子

**[13835.48s] English:** A bunch, right, in the most simplistic terms: running through the model, a bunch, and then you're, uh,...  
**Translation:** 

**[13840.02s] English:** You're going to exchange everything and synchronize the weights, right? So, you'll do it in a step.  
**Translation:** Vocabulary: simplistic: 简单的; synchronize: 同步

**[13844.04s] English:** This is like a step in model training, right? And every step, your loss goes down, hopefully, and it...  
**Translation:** 

**[13847.56s] English:** Doesn't always, but in the simplest terms, you'll be computing a lot and then you'll exchange.  
**Translation:** Vocabulary: computing: 计算

**[13851.66s] English:** The interesting thing is, GPU power is most of it; networking power is some.  
**Translation:** 

**[13855.34s] English:** But it's a lot less, but so while you're computing your power for your GPUs, is here, but then when  
**Translation:** 

**[13859.68s] English:** You're exchanging weights, uh, if you're not able to overlap communications and computation perfectly.  
**Translation:** 

**[13863.90s] English:** There may be a time period where your GPUs are just idle, and you're exchanging weights, and you're like,  
**Translation:** Vocabulary: computation: 计算; overlap: 重叠

**[13868.48s] English:** Hey, the model's updating, so you're exchanging the gradients, you do the model update, and then you...  
**Translation:** 

**[13872.58s] English:** Start training again, so the power goes right, and it's super spiky—and so funny enough, right?  
**Translation:** Vocabulary: gradients: 梯度; spiky: 尖峰的

**[13878.60s] English:** This, when you talk about the scale of data center power, you can blow stuff up so easily, um, and  
**Translation:** 

**[13885.00s] English:** So,  
**Translation:** 

**[13885.12s] English:** Meta actually has accidentally opened an upstream issue regarding some code in PyTorch, where they added  
**Translation:** 

**[13890.88s] English:** An operator, and I kid you not—whenever made this, I want to hug the guy because it says  
**Translation:** Vocabulary: upstream: 上游的

**[13894.80s] English:** Says Pi Torch, uh, it's like Pi Torch dot power plant: no blow-up equals zero or equals one, and  
**Translation:** 

**[13900.70s] English:** What it does is amazing, right? Either, you know, one year when you're exchanging...  
**Translation:** Vocabulary: equals: 等于

**[13905.98s] English:** Weights the GPU will just compute fake numbers so the power doesn't spike too much, and so then,...  
**Translation:** 

**[13910.26s] English:** The power plants don't blow up because transient spikes, like surges, can mess things up, well, that's how it works.  
**Translation:** Vocabulary: compute: 计算; spike: 峰值; spikes: 峰值; surges: 浪涌; transient: 瞬时的

**[13914.46s] English:** Makes sense, I mean.  
**Translation:** 

**[13915.12s] English:** You have to do that kind of thing; you have to make sure they're not idle, yeah—an Elon solution.  
**Translation:** 

**[13920.00s] English:** It was like, let me throw a bunch of Tesla Mega Packs and a few other things, right? Like everyone has.  
**Translation:** 

**[13923.70s] English:** Different solutions, but like Meta's at least was publicly and openly known, which is just like  
**Translation:** Vocabulary: openly: 公开地

**[13927.96s] English:** Set this operator, and what this operator does is just make the GPUs compute nothing.  
**Translation:** 

**[13932.30s] English:** So, that the power doesn't spike, but that just tells you how much power you're working with. I  
**Translation:** 

**[13937.10s] English:** It's insane. It's insane. People should just go to Google and scale. Like, what does X watts do?  
**Translation:** 

**[13943.14s] English:** And go through all the scales, from one watt to a kilowatt to a megawatt, and you look and stare at.  
**Translation:** Vocabulary: kilowatt: 千瓦; megawatt: 兆瓦; watts: 瓦

**[13948.46s] English:** That and you're how high on the list a gigawatt is, and it's mind-blowing. Can you say something?  
**Translation:** 

**[13954.66s] English:** About the cooling: so, I know Elon's using liquid cooling in all cases, I believe. That's a new development.  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[13962.84s] English:** Thing right; most of them don't use liquid cooling. Is there something interesting to say about that?  
**Translation:** 

**[13966.42s] English:** Cooling, yeah, yeah. So, air cooling has been the de facto standard. Uh, throw a bunch of metal heat sinks at it.  
**Translation:** Vocabulary: facto: 实际上

**[13971.12s] English:** Heat pipes, etc., and fans: right. And like that's been enough to cool it, um, people.  
**Translation:** 

**[13976.60s] English:** Have been dabbling in water cooling, Google.  
**Translation:** Vocabulary: dabbling: 尝试

**[13978.46s] English:** TPUs are water-cooled, right? Um, so they've been doing that for a few years, uh, but with GPUs, no.  
**Translation:** 

**[13985.18s] English:** One has never done, and no one has ever done on the scale of water cooling that Elon just did, right? Um,  
**Translation:** 

**[13989.60s] English:** Now, next-generation NVIDIA is, for the highest-end GPU, mandatory with water.  
**Translation:** 

**[13994.80s] English:** Cooling: You have to water-cool it, but Elon did it for this current generation, and that required...  
**Translation:** Vocabulary: mandatory: 必须的

**[13999.54s] English:** A lot of stuff, right? If you look at some of the satellite photos and stuff of the  
**Translation:** 

**[14004.16s] English:** Memphis facility: There's all these external water chillers that are sitting; it looks like  
**Translation:** Vocabulary: chillers: 冷水机组

**[14008.46s] English:** It looks like a semi-truck pod thing, uh, what's it called—the container, uh—but really, those are.  
**Translation:** 

**[14012.68s] English:** Water chillers, and he has about 90 of those water chillers just sitting outside in 90 different locations.  
**Translation:** 

**[14016.56s] English:** Containers, right? With water, you know, like chill the water, bring it back to the data center and...  
**Translation:** 

**[14021.00s] English:** Then, you distribute it to all the chips, pull all the heat out, and then send it back, right?  
**Translation:** Vocabulary: chill: 冷却

**[14024.96s] English:** Is both a way to cool the chips but also an efficiency thing, all right? Going back to that,...  
**Translation:** 

**[14030.52s] English:** Like, sort of a three-vector thing, right? There is, you know, memory bandwidth, flops, and  
**Translation:** Vocabulary: bandwidth: 内存带宽; flops: 浮点运算

**[14038.46s] English:** Things like that, and I think that's one of the things that's really great about this; it's  
**Translation:** 

**[14040.00s] English:** Speed interconnects right, and so this is also like a reason why you're going to go.  
**Translation:** Vocabulary: interconnects: 连接

**[14043.24s] English:** Not a big deal; it's about the functionality of it. I don't think it's maybe a big deal for solvents.  
**Translation:** 

**[14045.24s] English:** Water cooling is because you can just put the chips right next to each other, and therefore get  
**Translation:** Vocabulary: functionality: 功能; solvents: 溶剂

**[14047.90s] English:** It's really something that we have to work with to figure out how to use it in a way.  
**Translation:** 

**[14049.16s] English:** Higher-speed connectivity: I've got to ask you, so in one of your recent posts, there's a section  
**Translation:** Vocabulary: connectivity: 连接性

**[14051.72s] English:** That I think makes it much easier to do a lot of stuff, and I could help with that as well.  
**Translation:** 

**[14056.12s] English:** It's really just one of the things that I've realized that, you know, people have asked me about.  
**Translation:** 

**[14059.18s] English:** Called a cluster-measuring contest, so uh, there's another word there, but I won't say it; you know.  
**Translation:** 

**[14061.00s] English:** You know, with the idea of modding and the use of instant memory, I don't think it has...  
**Translation:** Vocabulary: modding: 修改游戏内容

**[14064.64s] English:** Uh, who's got the biggest now, and who's gonna have the today's largest?  
**Translation:** 

**[14072.80s] English:** Is Elon right? Um, Elon's cluster in Memphis has 200,000 GPUs, right? Um, Meta has like  
**Translation:** Vocabulary: cluster: 计算集群

**[14081.02s] English:** 128,000 openings have 100,000 now. To be clear, other companies have more GPUs than Elon's.  
**Translation:** 

**[14086.24s] English:** Just don't have them in one place, right? And for training, you want them tightly connected, there's  
**Translation:** 

**[14090.72s] English:** Some techniques that people are researching or working on that let you train  
**Translation:** 

**[14094.64s] English:** Across multiple regions, but for the most part, you want them all in one area, right?  
**Translation:** Vocabulary: researching: 研究

**[14099.78s] English:** Can we connect them highly with high-speed networking? Um, and so you know, Elon today has 200,000 GP H100s.  
**Translation:** 

**[14106.14s] English:** And $100,000 (H$100s), $100,000 (H$200s), right? Um, Meta, OpenAI, uh, you know, and Amazon, all have...  
**Translation:** 

**[14114.44s] English:** On the scale of 100,000, a little bit less, um, but next year, right? This year, people are building.  
**Translation:** 

**[14119.42s] English:** Much more right, Anthropic and Amazon are building a cluster of 400,000 Tranium 2s, which is Amazon's  
**Translation:** 

**[14124.38s] English:** Specifically,  
**Translation:** 

**[14124.64s] English:** Trying to get away from NVIDIA, right? Um, you know, Meta and OpenAI have different scales.  
**Translation:** 

**[14132.70s] English:** Hundreds of thousands, but by next year you'll have around 500,000 to 700,000 GPU clusters.  
**Translation:** 

**[14138.18s] English:** And note that those GPUs are much higher in power consumption than existing ones, right, Hopper?  
**Translation:** Vocabulary: clusters: GPU集群; hopper: 霍普金斯

**[14142.16s] English:** 700 watts Blackwell goes to 1,200 watts, right? So, the power per chip is growing, and the number...  
**Translation:** 

**[14148.38s] English:** Of chips is growing, right? Nuts! Yeah, you think, you think Elon said he'll get to a million, you?  
**Translation:** Vocabulary: watts: 瓦

**[14154.14s] English:** I think that's  
**Translation:** 

**[14154.38s] English:** Actually, it's feasible, um, I mean, I don't doubt Elon at all. The filings that...  
**Translation:** Vocabulary: feasible: 可行的

**[14160.00s] English:** He has, for example, the power plant and the Tesla battery packs. It's clear he has some crazy ideas.  
**Translation:** 

**[14164.12s] English:** Plans for Memphis, um, like permits and stuff are open records, right? But it's not quite clear.  
**Translation:** 

**[14169.70s] English:** That you know, what the time scales are, um, I just never doubt Elon, right?  
**Translation:** 

**[14175.12s] English:** That's he's gonna surprise us, so what's the idea with these clusters if you have a million GPUs?  
**Translation:** 

**[14179.04s] English:** What percentage, on average, is used for training over two to three years, and what percent before training?  
**Translation:** 

**[14187.76s] English:** What percentage is used for actual computation? Clusters make no sense for inference.  
**Translation:** Vocabulary: computation: 计算; inference: 推理

**[14193.30s] English:** Right, you could route inference there and just not train it, but most of the inference capacity,  
**Translation:** 

**[14198.62s] English:** Is being, you know, hey, I've got a 30-megawatt data center here, I've got 50 megawatts here, I've got  
**Translation:** Vocabulary: megawatt: 兆瓦; megawatts: 兆瓦

**[14202.80s] English:** 100, here, whatever. I'll just throw inference in all of those because the mega clusters, right?  
**Translation:** 

**[14207.84s] English:** Multi-gigawatt data centers: I want to train there because that's where all of my GPUs are co-located.  
**Translation:** 

**[14212.68s] English:** Where I can put them at a super-high networking speed, connected together, right? Because that's  
**Translation:** 

**[14217.10s] English:** What you need for training:  
**Translation:** 

**[14217.76s] English:** Now, with pre-training, this is the old scale: right? You could increase parameters, you'd  
**Translation:** 

**[14222.30s] English:** Increase data model gets better, but that doesn't apply anymore because there's not.  
**Translation:** 

**[14227.36s] English:** Much more data on the pre-training side, right? Uh, yes, there's video and audio and images that have.  
**Translation:** 

**[14232.08s] English:** Not been fully taken advantage of, so there's a lot more scaling, but a lot of people like it.  
**Translation:** 

**[14236.08s] English:** Have you taken transcripts of YouTube videos, and that gets you a lot of the data, doesn't it?  
**Translation:** 

**[14240.30s] English:** Get you all the learning value out of the video and image data, but you know, there's still  
**Translation:** Vocabulary: transcripts: 文字稿

**[14244.18s] English:** Scaling to be done during pre-training, but this post-training world,...  
**Translation:** 

**[14247.58s] English:** You know, there's still scaling to be done on pre-training, but this post-training world,...  
**Translation:** 

**[14247.74s] English:** Is where all the flops are going to be spent. Right? The model is going to play with itself.  
**Translation:** 

**[14251.14s] English:** It's going to self-play, it's going to do verifiable tasks, and it's going to do computer.  
**Translation:** Vocabulary: flops: 运算次数; verifiable: 可验证的

**[14254.06s] English:** Use in sandboxes, it might even do like simulated robotics things, right? Like all of these things.  
**Translation:** 

**[14259.72s] English:** Are going to be environments where compute is spent in "quote-unquote" post-training, but I think  
**Translation:** Vocabulary: compute: 计算; environments: 环境; robotics: 机器人; sandboxes: 沙箱; simulated: 模拟

**[14265.34s] English:** I think it's going to be good. We're going to drop the post from post-training.  
**Translation:** 

**[14268.34s] English:** Yeah, it's going to be pre-training and it's going to be training, I think, at some point, um,...  
**Translation:** 

**[14274.14s] English:** Because, for the bulk of the last few years, pre-training has dwarfed post-training.  
**Translation:** 

**[14280.00s] English:** But with these verifiable methods, especially ones that scale really well, you know.  
**Translation:** Vocabulary: dwarfed: 超越

**[14284.62s] English:** Infinitely, like computer use and robotics, not just math and coding, right? Where you  
**Translation:** 

**[14288.16s] English:** Can verify what's happening; those infinitely verifiable tasks, it seems you can spend as  
**Translation:** Vocabulary: infinitely: 无穷地; verify: 验证

**[14292.30s] English:** You can use them for as much computing as you want.  
**Translation:** 

**[14293.68s] English:** Especially at the context length increase, because at the end of pre-training is when  
**Translation:** Vocabulary: computing: 计算

**[14296.78s] English:** You can increase the context length for these models.  
**Translation:** 

**[14299.16s] English:** And we've talked earlier in the conversation about how the context length, when you have,  
**Translation:** 

**[14303.40s] English:** A long input is much easier to manage than output.  
**Translation:** 

**[14305.74s] English:** And a lot of these post-training and reasoning techniques rely on a ton of sampling, and  
**Translation:** 

**[14310.70s] English:** It's becoming increasingly long context.  
**Translation:** 

**[14313.10s] English:** So it's just like effectively, your compute efficiency goes down.  
**Translation:** 

**[14317.04s] English:** I don't think "flops" is the standard for how you measure it, but with RL, and you have...  
**Translation:** 

**[14322.54s] English:** To do all these things, where you move your weights around in a different way than at  
**Translation:** 

**[14326.66s] English:** Pre-training and just generation, it's going to become less efficient, and FLOPS is going  
**Translation:** 

**[14332.22s] English:** To be less of a useful term.  
**Translation:** 

**[14333.50s] English:** And then, as the infrastructure gets better, it's probably going to go down.  
**Translation:** 

**[14335.74s] English:** It's going to go back to flops.  
**Translation:** Vocabulary: flops: 失败的作品

**[14337.12s] English:** So, all of the things we've been talking about is most likely going to be NVIDIA, right?  
**Translation:** 

**[14341.90s] English:** Is there any competition?  
**Translation:** 

**[14343.44s] English:** Google, I kind of ignored them.  
**Translation:** 

**[14346.32s] English:** What's the story with TPU?  
**Translation:** 

**[14350.56s] English:** TPU is awesome, right?  
**Translation:** 

**[14352.14s] English:** It's great.  
**Translation:** 

**[14353.14s] English:** Google is a bit more tepid about building data centers for some reason.  
**Translation:** 

**[14357.44s] English:** They're building big data centers, don't get me wrong.  
**Translation:** Vocabulary: tepid: 温和

**[14359.36s] English:** And they actually have the biggest cluster.  
**Translation:** 

**[14361.28s] English:** I was talking about NVIDIA clusters.  
**Translation:** Vocabulary: cluster: 聚集; clusters: 聚集

**[14363.08s] English:** They actually have the biggest cluster, period.  
**Translation:** 

**[14365.74s] English:** But the way they do it is very interesting, right?  
**Translation:** 

**[14368.60s] English:** They have two sorts of data center super regions, right?  
**Translation:** 

**[14372.36s] English:** In that the data center isn't physically located such that all of the GPUs are on one site,  
**Translation:** 

**[14376.14s] English:** But they're about 30 miles from each other.  
**Translation:** 

**[14377.64s] English:** They're not GPUs or TPUs, right?  
**Translation:** 

**[14378.94s] English:** They have, in Iowa and Nebraska, four data centers that are just right next to each other.  
**Translation:** 

**[14383.32s] English:** To each other.  
**Translation:** Vocabulary: nebraska: 内布拉斯加州

**[14384.30s] English:** Why doesn't Google flex its cluster size?  
**Translation:** 

**[14388.14s] English:** Go to multi-data center training.  
**Translation:** 

**[14389.70s] English:** There are good images in there, so I'll show you what I mean.  
**Translation:** 

**[14391.54s] English:** It's just a semi-analysis, multi-data center.  
**Translation:** 

**[14394.86s] English:** So, this is like...  
**Translation:** 

**[14395.74s] English:** So, this is an image of what a standard Google data center looks like.  
**Translation:** 

**[14398.88s] English:** By the way, their data centers look...  
**Translation:** 

**[14400.00s] English:** Different than anyone else's data centers. What are we looking at here? So, these are, yeah, so if  
**Translation:** 

**[14404.02s] English:** You see this image, right? In the center, there are these big rectangular boxes, right? Those are where  
**Translation:** 

**[14408.92s] English:** The actual chips are kept. And then, if you scroll down a little bit further, you can see there's  
**Translation:** Vocabulary: rectangular: 长方形的; scroll: 滚动查看

**[14414.90s] English:** Like these water pipes, there are chiller cooling towers on top, and a bunch of other equipment.  
**Translation:** 

**[14419.18s] English:** Diesel generators. The diesel generators are backup power. The data center itself is like:  
**Translation:** Vocabulary: backup: 备用; chiller: 制冷; diesel: 柴油; generators: 发电机组

**[14424.72s] English:** Physically smaller than the water chillers, right? So the chips are actually easier to keep.  
**Translation:** 

**[14429.06s] English:** Together, but then cooling all the water for the water cooling system is very difficult, right? So,  
**Translation:** Vocabulary: chillers: 冷水机

**[14433.32s] English:** Google has a very advanced infrastructure that no one else has for the TPU, and what they  
**Translation:** 

**[14438.72s] English:** Do they have like stamped these data centers? They've stamped a bunch of these data centers out.  
**Translation:** Vocabulary: stamped: 大规模建设

**[14442.08s] English:** In a few regions, right? So if you go a little bit further down, this is Microsoft, and this is  
**Translation:** 

**[14447.88s] English:** In Arizona, this is where GPT-5 (quote-unquote) will be trained, you know—if it doesn't exist already.  
**Translation:** Vocabulary: arizona: 亚利桑那州

**[14454.36s] English:** Yeah, if it doesn't exist already. But each of these data centers, right—I've shown a couple.  
**Translation:** 

**[14458.32s] English:** Images of them.  
**Translation:** 

**[14459.06s] English:** They're like really closely co-located in the same region, right? Nebraska, Iowa. And then they,...  
**Translation:** 

**[14463.26s] English:** Also, we have a similar one in Ohio, right? And so these data centers are really close to each other.  
**Translation:** 

**[14468.74s] English:** Other. And what they've done is connect them with super-high-bandwidth fiber. And so these  
**Translation:** 

**[14473.82s] English:** Are just a bunch of data centers. And the point here is that Google has a very advanced infrastructure.  
**Translation:** 

**[14479.28s] English:** Very tightly connected in a small region. So, Elon will always have the biggest cluster.  
**Translation:** 

**[14483.50s] English:** Fully connected, right? Because it's all in one building, right? And he's completely right on that.  
**Translation:** Vocabulary: cluster: 聚类

**[14488.10s] English:** Right?  
**Translation:** 

**[14489.06s] English:** Has the biggest cluster, but you have to spread over three sites, and by a significant margin,  
**Translation:** Vocabulary: margin: 差距

**[14493.82s] English:** We have to go across multiple sites.  
**Translation:** 

**[14495.46s] English:** Why doesn't Google compete with NVIDIA? Why don't they sell TPUs?  
**Translation:** 

**[14501.40s] English:** I think there are a couple problems with it. It's like, one, TPU has been a form of allowing search.  
**Translation:** 

**[14509.24s] English:** To be really freaking cheap and build models for that, right? And so, a big chunk of the search...  
**Translation:** Vocabulary: freaking: damn

**[14515.14s] English:** GPU Purchases or TPU Purchases are a big chunk of Google's purchases.  
**Translation:** 

**[14519.06s] English:** Here's this.  
**Translation:** Vocabulary: purchases: 购买

**[14520.00s] English:** Usage: All of it is for internal workloads, right? Whether it be search, like Gemini, right? Or YouTube.  
**Translation:** 

**[14526.14s] English:** All these different applications that they have—你知道，广告就在这些地方。这些都是他们的TPU所在。  
**Translation:** Vocabulary: gemini: 双子座; workloads: 工作负载

**[14531.54s] English:** Being spent, and that's what they're hyper-focused on, right? And so there are certain aspects of  
**Translation:** 

**[14536.28s] English:** The architecture that is optimized for their use case, but not optimized elsewhere, right?  
**Translation:** Vocabulary: optimized: 优化

**[14540.88s] English:** One simple example is that they have open-sourced the Gemma model and called it Gemma 7B, right?  
**Translation:** 

**[14545.94s] English:** But then it's actually 8 billion parameters, because the vocabulary is so large.  
**Translation:** Vocabulary: gemma: 吉玛模型

**[14549.52s] English:** And the reason they made the vocabulary so large is because TPUs, like matrix-multiply units, are involved.  
**Translation:** 

**[14554.76s] English:** Massive, because that's what they've kind of optimized for. And so they decided, oh, well,  
**Translation:** 

**[14558.78s] English:** I'll just make the vocabulary large, too, even though it makes no sense to do so on such a small project.  
**Translation:** 

**[14562.30s] English:** Model, because that fits on their hardware. So, Gemma doesn't run as efficiently on a GPU as a  
**Translation:** Vocabulary: efficiently: 高效地

**[14566.82s] English:** Lama does, right? But vice versa, Lama doesn't run as efficiently on a TPU as a Gemma does.  
**Translation:** 

**[14572.14s] English:** Right? And it's sort of like there are certain aspects of hardware-software co-design.  
**Translation:** Vocabulary: versa: 相反

**[14575.72s] English:** So, all their search models are their ranking and recommendation models, all these different ones.  
**Translation:** 

**[14579.50s] English:** Models that are AI, but not like gen AI, have been hyper-optimized with TPUs for a long time, right?  
**Translation:** Vocabulary: recommendation: 推荐模型

**[14584.98s] English:** The software stack is super-optimized, but not all of this software stack has been released.  
**Translation:** 

**[14589.54s] English:** Publicly, at all, right? Very small portions of it. Jackson XLA have been, but like the experience.  
**Translation:** Vocabulary: portions: 部分

**[14595.36s] English:** When you're inside of Google and you're training on TPUs as a researcher, you don't need to know  
**Translation:** 

**[14599.14s] English:** Anything about the hardware in many cases, right? Like it's pretty beautiful, but as soon as  
**Translation:** 

**[14603.42s] English:** You step outside, they'll go, they'll go. A lot of them go back. They leave Google and then they go.  
**Translation:** 

**[14608.08s] English:** Back. Yeah. Yeah. They're like,  
**Translation:** 

**[14609.50s] English:** They leave and start a company because they have all these amazing research ideas and they're  
**Translation:** 

**[14612.64s] English:** Like, wait, infrastructure is hard. Software is hard. And this is on GPUs—or if they try to use,...  
**Translation:** 

**[14617.26s] English:** TPUs, same thing, because they don't have access to all this code. And so, how do you?  
**Translation:** 

**[14621.06s] English:** Convince a company whose golden goose is search, where they're making hundreds of billions of dollars,  
**Translation:** 

**[14624.70s] English:** Dollars from start selling GPUs or TPUs, which they used to only buy a couple billion of, you  
**Translation:** 

**[14630.74s] English:** Know, I think in 2023, they bought like a couple billion, and now they're buying like ten billion to.  
**Translation:** 

**[14636.96s] English:** $15 billion worth. But how do you convince them that they could?  
**Translation:** 

**[14639.50s] English:** They should just  
**Translation:** 

**[14640.00s] English:** Buy like twice as many and figure out how to sell them and make $30 billion—who cares?  
**Translation:** 

**[14643.72s] English:** About making $30 billion in profits won't that $30 billion exceed actually the search profit?  
**Translation:** Vocabulary: exceed: 超过

**[14649.36s] English:** Eventually, oh, I mean, like, you're always going to make more money on services than always.  
**Translation:** 

**[14655.02s] English:** I mean, like, yeah, like you know, like to be clear, today people are spending a lot more on  
**Translation:** 

**[14659.18s] English:** Hardware is what they are, the services, right? Because the hardware front-ends run the services, but like.  
**Translation:** 

**[14665.76s] English:** You're investing if there's no revenue for AI stuff, or not enough revenue, then obviously, like  
**Translation:** 

**[14670.24s] English:** It's going to blow up, right? You know, uh, people won't continue to spend on GPUs forever, um,...  
**Translation:** 

**[14674.56s] English:** NVIDIA is trying to move up the stack with software that they're trying to sell and license.  
**Translation:** 

**[14677.84s] English:** And, stuff, right? But Google has never had that kind of DNA — like, this is a product we should sell.  
**Translation:** 

**[14683.26s] English:** Right, they don't act; Google Cloud does it, which is a separate organization from the TPU team.  
**Translation:** 

**[14687.86s] English:** Which is a separate organization from the Deep Mind team, which is a separate organization from  
**Translation:** 

**[14690.80s] English:** The search team, however, there's a lot of bureaucracy. Wait—Google Cloud is a separate team from TPU.  
**Translation:** Vocabulary: bureaucracy: 官僚主义

**[14694.92s] English:** Team  
**Translation:** 

**[14695.36s] English:** Technically, TPU sits under infrastructure, which sits under Google Cloud, but like Google.  
**Translation:** Vocabulary: technically: 实际上

**[14700.98s] English:** Cloud, like for like renting stuff, and TPU architecture are very different goals, right?  
**Translation:** 

**[14707.32s] English:** In hardware and software, like all of this — for example, the jacks, XLAs, and Teams — do not serve Google's.  
**Translation:** 

**[14712.62s] English:** Customers externally, whereas NVIDIA's various CUDA teams serve for things like Nickel.  
**Translation:** 

**[14717.14s] English:** External customers, right? Um, the internal teams like Jackson XLA and stuff they more so serve.  
**Translation:** Vocabulary: externally: 外部; nickel: 镍

**[14722.70s] English:** DeepMind and search right, and so their customers.  
**Translation:** 

**[14725.36s] English:** They're not building a product for them, do you understand why AWS keeps winning?  
**Translation:** 

**[14729.28s] English:** Uh, versus Azure for cloud, uh, versus Google Cloud, yeah, there's Google Cloud—isn't it—tiny, relative?  
**Translation:** 

**[14737.08s] English:** To the Google Cloud, it's third, yeah, yeah. Um, Microsoft is the second biggest, but Amazon is the biggest.  
**Translation:** 

**[14742.20s] English:** Right, yeah, um, and Microsoft sort of deceptively includes something like Microsoft Office 365,  
**Translation:** 

**[14747.32s] English:** Things like that, like some of these enterprise-wide licenses, so in reality, the gap is even larger.  
**Translation:** Vocabulary: deceptively: 误导性地

**[14751.78s] English:** Microsoft is still second, though, right? Um, Amazon is way bigger. Why? Because they're not building a product for them.  
**Translation:** 

**[14755.36s] English:** Because using AWS is better and easier, and in many cases it's cheaper, and it's first-class.  
**Translation:** 

**[14760.00s] English:** Lose first, yeah, but there's a lot of things that are first. That's easier; it's also harder.  
**Translation:** 

**[14764.56s] English:** Switching than it is to AWS because there are big fees for switching to AWS, which generate over 80 percent of  
**Translation:** 

**[14771.00s] English:** Amazon's profit, I think, is over 90 percent—that's insane. The distribution centers are just like  
**Translation:** 

**[14775.18s] English:** One day, we'll decide to make money from this, but they haven't done it yet, right? Like, they make tiny...  
**Translation:** 

**[14779.62s] English:** Little profit from, you know, one day of Amazon Prime will triple in price. You would think they,  
**Translation:** 

**[14783.30s] English:** Would improve AWS's interface because it's like horrible; it's like clunky, but everybody is  
**Translation:** Vocabulary: clunky: 笨拙的; interface: 界面; triple: 三倍

**[14790.58s] English:** Yeah, you'd think. I think actually Google's interface is sometimes nice, but it's also like  
**Translation:** 

**[14796.66s] English:** They don't care about anyone besides their top customers, exactly like their customer service.  
**Translation:** 

**[14800.14s] English:** Sucks, and like they have a lot less. I mean, all these companies they optimize for the big...  
**Translation:** 

**[14804.42s] English:** Customers, yeah; it's supposed to be for business. Amazon has always optimized for the small customer.  
**Translation:** Vocabulary: optimize: 使最优化; optimized: 已经最优化

**[14809.02s] English:** Too, though, right? Like, obviously, they optimize a lot for the big customers, but like when they started...  
**Translation:** 

**[14812.66s] English:** They just  
**Translation:** 

**[14813.24s] English:** They just  
**Translation:** 

**[14813.28s] English:** They just  
**Translation:** 

**[14813.30s] English:** Would go to like random Bay Area things and give out credits, right? And then they just put  
**Translation:** 

**[14817.78s] English:** In your credit card, and use us, right? Like back in the early days; so they've always said the business has.  
**Translation:** 

**[14821.72s] English:** Grown with them right in virgin, so, like, why does Amazon like why Snowflake all over Amazon because?  
**Translation:** 

**[14826.38s] English:** Snowflake, in the beginning, when Amazon didn't care about them, was still using Amazon—and then.  
**Translation:** Vocabulary: snowflake: 雪花; virgin: 未开发的

**[14830.30s] English:** Of course, one day Snowflake and Amazon have a super huge partnership, but like, this is the case like  
**Translation:** 

**[14834.48s] English:** Amazon's user experience and quality are better, and they've also engineered a lot of the silicon.  
**Translation:** 

**[14838.78s] English:** Makes them have a lower cost structure and traditional cloud storage, CPU, and networking.  
**Translation:** 

**[14842.90s] English:** That kind of stuff, uh, then, um, in databases, right? Like, you know, I think like four of Amazon's top  
**Translation:** Vocabulary: databases: 数据库

**[14849.94s] English:** Five revenue products, such as margin products, are like gross profit products, and are all database-related.  
**Translation:** 

**[14854.96s] English:** Products like Redshift, and like all these things, right? So Amazon has a very good  
**Translation:** Vocabulary: margin: 利润; redshift: 红移

**[14861.42s] English:** Silicon to a user experience, like an entire pipeline with AWS—I think Google is in for their silicon.  
**Translation:** 

**[14867.44s] English:** Teams, yeah, they have awesome silicon internally, TPU, the YouTube chip, you know, some of these.  
**Translation:** Vocabulary: internally: 内部; pipeline: 流程; silicon: 硅片

**[14872.30s] English:** Other chips that they have have a lot of silicon internally, and they have a lot of silicon.  
**Translation:** 

**[14872.88s] English:** They've made, and the problem is, they're not serving external customers or internal ones.  
**Translation:** 

**[14877.48s] English:** Customers, right? It's, I mean, NVIDIA's entire culture is  
**Translation:** 

**[14880.00s] English:** Designed from the bottom up to do this, there's this recent book, "The Nvidia Way," by Takehim.  
**Translation:** 

**[14884.12s] English:** That details this, and they're how they look for future opportunities and ready their CUDA software.  
**Translation:** 

**[14891.06s] English:** Libraries to make it so that new applications of high-performance computing can very rapidly be  
**Translation:** Vocabulary: computing: 计算

**[14896.86s] English:** Evolved on CUDA and NVIDIA chips, and that is entirely different than Google as a service.  
**Translation:** 

**[14902.90s] English:** Business, yeah, I mean, NVIDIA should be said as a truly special company, like I mean, they  
**Translation:** Vocabulary: evolved: 发展

**[14908.90s] English:** The whole culture is optimized for that kind of thing.  
**Translation:** 

**[14912.56s] English:** Speaking of that, is there anybody that can even challenge NVIDIA's hardware-wise, Intel and AMD?  
**Translation:** Vocabulary: optimized: 优化

**[14918.76s] English:** I really don't think so. We went through a very long process, working with AMD, though.  
**Translation:** 

**[14926.22s] English:** Training on their GPUs, inference, and stuff; and they're decent—their hardware is better.  
**Translation:** Vocabulary: inference: 推断

**[14930.24s] English:** In many ways, NVIDIA's software is really bad, and I think  
**Translation:** 

**[14934.66s] English:** They're getting better, right? They're getting better faster, but there's still a long way to go.  
**Translation:** 

**[14937.98s] English:** It is so large.  
**Translation:** 

**[14938.72s] English:** Um, and like they don't spend enough resources on it, or haven't historically. Maybe they're  
**Translation:** Vocabulary: historically: 历史上

**[14944.04s] English:** Changing their tune now, but you know, for multiple months we were submitting those bugs.  
**Translation:** 

**[14948.76s] English:** Right, like us semi-analysis, right? Like "what the fuck"? Like, why are we submitting those bugs?  
**Translation:** Vocabulary: submitting: 提交

**[14953.32s] English:** Right, because they only cared about their biggest customers and so they'd ship  
**Translation:** 

**[14957.94s] English:** They sent me a private image, blah, blah, blah, and it's like, "Okay, but I am just using PyTorch and I want...  
**Translation:** 

**[14963.50s] English:** To use the publicly available libraries, and like, you don't care about that, right? So they are  
**Translation:** 

**[14967.42s] English:** Getting better, um, but they're getting better and better and they're.  
**Translation:** 

**[14968.72s] English:** Getting better, and they're getting better, and they're getting better, and they're getting better.  
**Translation:** 

**[14968.78s] English:** But, like I think AMD is not possible; Intel is obviously in dire straits right now.  
**Translation:** Vocabulary: straits: 困境

**[14972.26s] English:** Um, and needs to be saved somehow; uh, very important for national security for America.  
**Translation:** 

**[14977.52s] English:** You know, can you explain why they're in such dire straits, going back to earlier?  
**Translation:** 

**[14982.52s] English:** Only three companies can R&D in Taiwan: Samsung, Pyongyang, and Intel.  
**Translation:** 

**[14989.84s] English:** Hillsborough, Samsung's doing horribly, Intel's doing horribly. We could be in a world where...  
**Translation:** Vocabulary: horribly: 糟糕地; pyongyang: 平壤; taiwan: 台湾

**[14994.18s] English:** There's only one company that can do R&D, and that one company already manufactures most of the chips.  
**Translation:** 

**[14997.84s] English:** They've been gaining market share, but they're not going to be able to do that, so I think it's  
**Translation:** Vocabulary: manufactures: 生产芯片

**[14998.72s] English:** They're not going to be able to do that, so I think it's going to be harder anyway, but like  
**Translation:** 

**[14999.52s] English:** That  
**Translation:** 

**[15000.00s] English:** That's a critical thing, right?  
**Translation:** 

**[15001.46s] English:** So, what happens to Taiwan means the rest of the world's semiconductor industry—and, therefore, tech—rely on Taiwan, right?  
**Translation:** 

**[15006.98s] English:** And that's obviously precarious.  
**Translation:** 

**[15008.90s] English:** As far as Intel is concerned, they've been slowly and steadily declining.  
**Translation:** Vocabulary: declining: 下滑; precarious: 不稳固

**[15013.00s] English:** They were on top of servers and PCs, but now Apple's done the M1, and NVIDIA's releasing a PC chip, and Qualcomm's releasing a PC chip.  
**Translation:** 

**[15021.14s] English:** And in servers, hyperscalers are all making their own ARM-based server chips, and Intel has no AI-specific silicon wins, right?  
**Translation:** Vocabulary: hyperscalers: 超大规模云服务商; silicon: 半导体

**[15029.08s] English:** They have very small wins.  
**Translation:** 

**[15031.04s] English:** And they never got into mobile because they said no to the iPhone.  
**Translation:** 

**[15034.06s] English:** And, like, all these things have compounded, and they've lost their process technology leadership, right?  
**Translation:** 

**[15037.80s] English:** They were ahead for 20 years, and now they're behind by at least a couple of years, right?  
**Translation:** Vocabulary: compounded: 累积外溢

**[15041.24s] English:** And they're trying to catch back up, and we'll see if, like, their 18A, 14A strategy works out, where they try and leapfrog TSMC.  
**Translation:** 

**[15048.16s] English:** But, like, Intel's just losing tons of money anyway, right?  
**Translation:** Vocabulary: leapfrog: 超越

**[15051.66s] English:** And they just fired their CEO, even though their CEO was the only person who understood the company well, right?  
**Translation:** 

**[15056.48s] English:** We'll see.  
**Translation:** 

**[15057.04s] English:** He was not the best, but he was pretty good.  
**Translation:** 

**[15059.08s] English:** He was good, relatively.  
**Translation:** 

**[15060.56s] English:** Technical Guy.  
**Translation:** 

**[15061.44s] English:** Where does Intel make most of its money?  
**Translation:** 

**[15063.08s] English:** The CPUs, though, right?  
**Translation:** 

**[15064.06s] English:** PCs and data center CPUs, yeah.  
**Translation:** 

**[15065.52s] English:** But data center CPUs are all going cloud, and Amazon, Microsoft, and Google are making ARM-based CPUs.  
**Translation:** 

**[15071.46s] English:** And then on the PC side, AMD's gained market share.  
**Translation:** 

**[15075.02s] English:** NVIDIA is launching a chip.  
**Translation:** 

**[15076.08s] English:** That's not going to be a success, right?  
**Translation:** 

**[15077.30s] English:** MediaTek and Qualcomm have relaunched their chips.  
**Translation:** 

**[15079.24s] English:** Apple's doing well, right?  
**Translation:** Vocabulary: qualcomm: 高通; relaunched: 重新推出

**[15080.58s] English:** Like, they could get squeezed a little bit in PC, although PC, generally, I imagine, will just stick with Intel mostly for the Windows side.  
**Translation:** 

**[15086.96s] English:** Let's talk about the broad AI race.  
**Translation:** Vocabulary: squeezed: 受到挤压

**[15089.08s] English:** Who do you think wins?  
**Translation:** 

**[15090.86s] English:** We talked about Google.  
**Translation:** 

**[15091.86s] English:** The default leader has been Google, because of their infrastructure advantage.  
**Translation:** 

**[15097.58s] English:** Well, like, in the news, OpenAI is the leader.  
**Translation:** 

**[15100.86s] English:** They're the leaders in the narrative.  
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

**[15114.98s] English:** So, from an accounting profit perspective, Microsoft is making money, but they're spending a lot of capital.  
**Translation:** 

**[15119.06s] English:** They're spending a lot of capital on graphics, right?  
**Translation:** 

**[15119.74s] English:** You know, they're spending a lot of capital on graphics.  
**Translation:** 

**[15120.00s] English:** Gets depreciated over years; uh, Meta is making tons of money, but with recommendation systems.  
**Translation:** Vocabulary: depreciated: 资产折旧; recommendation: 推荐系统

**[15125.14s] English:** Which is AI, but not with llama, right? Llama is losing money for sure, right? Um, I think.  
**Translation:** 

**[15130.64s] English:** Anthropic and Open AI are obviously not making money, because otherwise they wouldn't be raising.  
**Translation:** Vocabulary: llama: 亏损公司

**[15134.22s] English:** Money, right? They have to raise money to build more, right? Although, theoretically, they are  
**Translation:** 

**[15139.14s] English:** Making money, right? Like, you know, you spent a few hundred million dollars on GDP4, and it's doing  
**Translation:** Vocabulary: theoretically: 理论上

**[15143.44s] English:** Billions in revenue, so, obviously, it's making money, although they had to continue to  
**Translation:** 

**[15147.20s] English:** Research to get the compute efficiency wins right, and then move down the curve, like you know.  
**Translation:** Vocabulary: compute: 计算

**[15152.02s] English:** That's 12, get that 1200x increase for GPT-3. You know, maybe we're only at like a fraction of that.  
**Translation:** 

**[15157.46s] English:** Know a couple hundred X now, but you know, with GDP4 Turbo and 4O, and there will be another one.  
**Translation:** Vocabulary: turbo: 加速器

**[15161.42s] English:** Probably cheaper than GDP4O, even when it comes out, and that research costs a lot, a lot.  
**Translation:** 

**[15167.12s] English:** Of money, yep, exactly. That's the thing that I guess isn't talked about when it comes to the cost.  
**Translation:** 

**[15171.68s] English:** The P that uh, when you're referring to the cost of the model, it's not just the training.  
**Translation:** 

**[15176.74s] English:** It's not just the cost of the model; it's not just the cost of the model; it's not just the  
**Translation:** 

**[15177.20s] English:** Or, for the test runs, it's the actual research and the manpower, yeah, to do things like reasoning.  
**Translation:** 

**[15183.10s] English:** Right now, what exists is going to be scaled up, and they're going to do a lot of research. I think  
**Translation:** Vocabulary: manpower: 人力

**[15186.24s] English:** I think the you know, people focus on the payback question, but it's really easy to just be  
**Translation:** 

**[15191.42s] English:** Like, well, GDP is a measure of humans and industrial capital, right? And if you can make  
**Translation:** Vocabulary: payback: 回报

**[15196.64s] English:** Intelligence is cheap, then you can grow a lot, right? That's the sort of dumb-dumb way to explain it.  
**Translation:** 

**[15202.00s] English:** But that's sort of what basically the investment thesis is, I think only Nvidia is actually.  
**Translation:** Vocabulary: thesis: 投资理念

**[15206.86s] English:** Making money, right? So, I think that's the sort of dumb way to explain it, but that's sort of what.  
**Translation:** 

**[15207.18s] English:** And other hardware vendors, um, the hyperscalers are all on paper making money, uh, but in reality,  
**Translation:** Vocabulary: hyperscalers: 超大规模服务商; vendors: 供应商

**[15213.30s] English:** They're like spending a lot more on purchasing the GPUs, which you don't know if they're still  
**Translation:** 

**[15217.32s] English:** Going to make this much money on each GPU in two years, right? Um, you don't know if, you know, all  
**Translation:** 

**[15223.78s] English:** Of a sudden, OpenAI goes "kapoof," and now Microsoft has like hundreds of thousands of GPUs, they were  
**Translation:** 

**[15228.74s] English:** Rental income from Open AI tools that paid for themselves with their initial investment.  
**Translation:** Vocabulary: rental: 租赁

**[15233.20s] English:** Um, you know, that no longer having a customer is always a possibility.  
**Translation:** 

**[15237.18s] English:** I don't believe that, right? Um, I think you know, opening.  
**Translation:** 

**[15240.00s] English:** Will keep raising money, I think others will keep raising money, um, because the investments, the  
**Translation:** 

**[15244.36s] English:** Returns from it are going to be eventually huge once we have AGI. So, do you think multiple companies will enter this space?  
**Translation:** Vocabulary: investments: 投资

**[15249.28s] English:** Let's assume it's not winner-take-all, okay? So, let's not call it that.  
**Translation:** 

**[15255.54s] English:** AGI, however, is like a single day—it's a gradual thing, super powerful AI, but it's a gradual process.  
**Translation:** Vocabulary: gradual: 逐渐的

**[15262.16s] English:** Increasing set of features that are useful and rapidly increasing, rapidly, rapidly increasing set.  
**Translation:** 

**[15268.84s] English:** Of features, uh, so you're saying a lot of companies will be it just seems absurd that.  
**Translation:** Vocabulary: absurd: 荒谬

**[15276.04s] English:** All of these companies are building gigantic data centers. There are companies that will benefit from this.  
**Translation:** 

**[15282.34s] English:** AI, but not because they train the best model like Meta; they have so many avenues to benefit from AI and  
**Translation:** Vocabulary: avenues: 途径; gigantic: 巨大的

**[15287.64s] English:** All of their services, people are there. People spend time on Meta's platforms, and it's a way,...  
**Translation:** 

**[15292.04s] English:** To make more money per user per hour, yeah, it seems like Google X.  
**Translation:** 

**[15297.80s] English:** /  
**Translation:** 

**[15298.82s] English:** It's important to say, and then Meta will not benefit directly from the AI like the  
**Translation:** 

**[15305.10s] English:** LLMs, but from the intelligence, like an additional boost of intelligence, to the products they already have.  
**Translation:** 

**[15312.68s] English:** Sell, so whether that's the recommendation system, or for Elon, who's been talking about Optimus.  
**Translation:** Vocabulary: optimus: 人形机器人; recommendation: 推荐系统

**[15318.00s] English:** Robot: Potentially, the intelligence of the robot, and then you have personalized robots in the home.  
**Translation:** 

**[15324.68s] English:** That kind of thing, he thinks it's a $10+ trillion dollar.  
**Translation:** Vocabulary: trillion: 万亿

**[15328.82s] English:** Business, which at some point, maybe I don't know when, but who knows? Let's do it. Let's do a...  
**Translation:** 

**[15336.60s] English:** Tam analysis: Right, eight billion humans, and let's get eight billion robots right, and let's pay.  
**Translation:** 

**[15342.16s] English:** Them, the average salary, and yeah, there we go: $10 trillion more than $10 trillion. Yeah, I mean you.  
**Translation:** 

**[15347.44s] English:** Know if there are robots everywhere, why does it have to be just eight billion of them?  
**Translation:** 

**[15352.70s] English:** Yeah, of course. Of course I'm gonna get one robot; you're gonna have like 20.  
**Translation:** 

**[15356.92s] English:** Yeah, I mean, I see you're gonna have like 20 robots. You're gonna have like 20 robots. You're gonna have  
**Translation:** 

**[15358.82s] English:** Use case for that, so yeah.  
**Translation:** 

**[15360.00s] English:** Yeah. So, I guess the benefit would be in the products they sell, which is why OpenAI is in a trickier position because they....  
**Translation:** Vocabulary: trickier: 更棘手

**[15366.50s] English:** All of the value of OpenAI, right now, as a brand, is in ChatGPT.  
**Translation:** 

**[15369.82s] English:** And there is actually not that much of a reason for most users that they need OpenAI to be spending billions and billions of dollars on the next best model when they could just license Lama5 and Furby way cheaper.  
**Translation:** 

**[15383.10s] English:** So, that's kind of like... ChatGPT is an extremely valuable entity to them.  
**Translation:** 

**[15387.82s] English:** But they could make more money just off that.  
**Translation:** 

**[15391.26s] English:** The chat application is clearly not designed to have much room to continue, right?  
**Translation:** 

**[15395.24s] English:** Like the standard chat, right? Where you're just using it for random questions and stuff, right?  
**Translation:** 

**[15399.08s] English:** The cost continues to collapse. V3 is the latest one, and it's the biggest.  
**Translation:** 

**[15403.34s] English:** But it's going to be supported by ads, right?  
**Translation:** Vocabulary: collapse: 急剧下降

**[15405.10s] English:** Like, you know, Lama... Meta already serves 405B users, and probably loses money.  
**Translation:** 

**[15409.24s] English:** But at some point, you know, they're going to get so cheap that they can just serve them for free with ads supported, right?  
**Translation:** 

**[15416.12s] English:** And that's what Google is going to be able to do.  
**Translation:** 

**[15417.52s] English:** And that's obviously they've got a bigger reach, right?  
**Translation:** 

**[15419.48s] English:** So, chat is not going to be the only use case.  
**Translation:** 

**[15421.76s] English:** It's like these reasoning, code, agents, and computers use.  
**Translation:** 

**[15425.68s] English:** All this stuff is where OpenAI has to actually go to make money in the future.  
**Translation:** 

**[15429.06s] English:** Otherwise, they're kaput.  
**Translation:** Vocabulary: kaput: 完蛋了

**[15430.38s] English:** But X, Google, and Meta have these other products.  
**Translation:** 

**[15435.18s] English:** So, isn't it likely that OpenAI and Anthropic will eventually disappear?  
**Translation:** 

**[15442.18s] English:** Unless they're so good at modeling, which they are.  
**Translation:** 

**[15444.30s] English:** But it's such a cutting-edge technology.  
**Translation:** 

**[15445.34s] English:** It depends on where you think AI came from.  
**Translation:** 

**[15447.52s] English:** Where the capabilities are going.  
**Translation:** Vocabulary: capabilities: 能力

**[15448.50s] English:** You have to keep winning.  
**Translation:** 

**[15449.90s] English:** Yes.  
**Translation:** 

**[15450.48s] English:** You have to keep winning.  
**Translation:** 

**[15451.72s] English:** As you climb, even if the AI capabilities are going super rapidly—awesome, in the direction of AGI—  
**Translation:** 

**[15458.74s] English:** Like, there's still a boost for X in terms of data.  
**Translation:** 

**[15463.24s] English:** Google, in terms of data.  
**Translation:** 

**[15464.72s] English:** Meta, in terms of data.  
**Translation:** 

**[15466.00s] English:** In terms of other products and the money.  
**Translation:** 

**[15467.86s] English:** And, like, there are just huge amounts of money.  
**Translation:** 

**[15470.06s] English:** The whole idea is that human data is kind of tapped out.  
**Translation:** Vocabulary: tapped: 用尽

**[15472.50s] English:** We don't care.  
**Translation:** 

**[15472.94s] English:** We all care about self-play and verifiable tasks.  
**Translation:** Vocabulary: verifiable: 可验证的

**[15475.60s] English:** Yes, the self-play sandbox.  
**Translation:** 

**[15476.16s] English:** Think about AWS.  
**Translation:** Vocabulary: sandbox: 测试环境

**[15477.00s] English:** Which is an awesome thing.  
**Translation:** 

**[15477.52s] English:** I think AWS doesn't make a lot of money.  
**Translation:** 

**[15480.00s] English:** Each individual machine, and the same can be said for the most powerful AI platform, which is even  
**Translation:** 

**[15486.24s] English:** Though the calls to the API are so cheap, there's still a lot of money to be made by owning that.  
**Translation:** 

**[15491.20s] English:** Platform, and there are lots of discussions as it's the next compute layer; you have to believe,...  
**Translation:** 

**[15496.56s] English:** That, and you know, there are a lot of discussions about tokens, tokenomics, and LLM APIs.  
**Translation:** Vocabulary: compute: 计算; tokenomics: 代经济

**[15501.48s] English:** Next, we might see a compute layer or the next paradigm for the economy, kind of like energy and oil were, but there's  
**Translation:** 

**[15506.34s] English:** Also, you have to sort of believe that APIs and chat are not where AI is stuck; it is  
**Translation:** Vocabulary: paradigm: 模式

**[15513.00s] English:** Actually, just tasks and agents, and robotics, and computer use — and those are the areas where all  
**Translation:** 

**[15518.22s] English:** The value will be delivered, not an API, not a chat application, right? Is it possible? I mean.  
**Translation:** Vocabulary: robotics: 机器人技术

**[15524.70s] English:** It all just becomes a commodity, and you have the very thin wrapper like perplexity.  
**Translation:** 

**[15532.14s] English:** Just joking—uh, there are a lot of wrappers making.  
**Translation:** Vocabulary: commodity: 商品; perplexity: 困惑; wrapper: 包装; wrappers: 包装纸

**[15536.30s] English:** It  
**Translation:** 

**[15536.34s] English:** A lot of money, yeah. So, but do you think it's possible that people would just even forget what?  
**Translation:** 

**[15540.98s] English:** Open AI and the Tropic is, and just because there will be wrappers around the API, and it just  
**Translation:** 

**[15545.84s] English:** Dynamically, if model progress is not rapid, yeah, it's becoming a commodity, right? DeepSeek V3.  
**Translation:** Vocabulary: dynamically: 动态; tropic: 热带

**[15550.94s] English:** Shows this, but also the GPT-3 chart earlier showed this: right, LLaMA 3B is 1200x cheaper than.  
**Translation:** 

**[15557.36s] English:** GPT-3, or anyone whose business model relied on GPT-3-level capabilities, is dead. Anyone whose  
**Translation:** Vocabulary: capabilities: 能力

**[15563.22s] English:** The business model based on GPT-4-level capabilities is dead. It's dead. It's dead. It's dead. It's dead. It's dead.  
**Translation:** 

**[15566.30s] English:** It is a common saying that the best businesses being made now are ones that are predicated on  
**Translation:** Vocabulary: predicated: 基于

**[15570.86s] English:** Models are getting better, right? Which would be like a wrapper thing that is riding the wave of the  
**Translation:** 

**[15576.38s] English:** Models the short-term, the company that could make the most money is the one that figures out what.  
**Translation:** 

**[15581.26s] English:** Advertising targeting methods work for language model generation. We have the Meta Ads, which are  
**Translation:** 

**[15586.80s] English:** Hyper-targeted in the feed, not within specific pieces of content, and we have search ads that are used.  
**Translation:** 

**[15592.34s] English:** By Google and Amazon has been rising a lot on search, but within a piece with within  
**Translation:** 

**[15596.26s] English:** A return from Chat GPT: It is not clear how you get a  
**Translation:** 

**[15600.00s] English:** High-quality ad placed within the output.  
**Translation:** 

**[15603.12s] English:** And if you can do that with model costs coming down,  
**Translation:** 

**[15606.24s] English:** You can just get super-high revenue.  
**Translation:** 

**[15609.42s] English:** Like that, revenue is totally untapped.  
**Translation:** Vocabulary: untapped: 未开发的

**[15610.88s] English:** And it's not clear, technically, how it is done.  
**Translation:** 

**[15612.74s] English:** Yeah, that is what I mean,  
**Translation:** Vocabulary: technically: 技术上

**[15614.52s] English:** Sort of the AdSense innovation that Google did.  
**Translation:** 

**[15618.30s] English:** The one day you'll have in GPT, output an ad.  
**Translation:** 

**[15621.92s] English:** And that's going to make like billions.  
**Translation:** 

**[15624.42s] English:** And it could be very subtle.  
**Translation:** Vocabulary: subtle: 微妙的

**[15625.72s] English:** It could be in a conversation.  
**Translation:** 

**[15627.06s] English:** We have voice mode now.  
**Translation:** 

**[15628.06s] English:** It could be some way of making it.  
**Translation:** 

**[15630.16s] English:** So, the voice introduces certain things.  
**Translation:** 

**[15632.58s] English:** It's much harder to measure.  
**Translation:** 

**[15633.52s] English:** And it takes imagination, but yeah.  
**Translation:** 

**[15635.92s] English:** And it wouldn't come off; shady.  
**Translation:** 

**[15639.02s] English:** So, that you would receive public backlash,  
**Translation:** Vocabulary: backlash: 公众反对; shady: 可疑

**[15641.64s] English:** That kind of thing.  
**Translation:** 

**[15642.20s] English:** So, you have to do it loud enough.  
**Translation:** 

**[15643.42s] English:** To where it's clear that it's an ad.  
**Translation:** 

**[15644.58s] English:** And balance all of that.  
**Translation:** 

**[15646.42s] English:** So, that's the open question they're trying to solve.  
**Translation:** 

**[15649.02s] English:** Anthropic and OpenAI, they need to.  
**Translation:** 

**[15651.42s] English:** They might not say that they care about it at all.  
**Translation:** 

**[15653.36s] English:** They don't care about it right now.  
**Translation:** 

**[15654.60s] English:** I think it's places like Perplexity.  
**Translation:** 

**[15656.78s] English:** We are experimenting with that more.  
**Translation:** Vocabulary: experimenting: 尝试; perplexity: 困惑

**[15658.06s] English:** Yeah, oh, interesting.  
**Translation:** 

**[15660.00s] English:** Yeah, for sure.  
**Translation:** 

**[15661.12s] English:** Like Perplexity, Google, and Meta care about this.  
**Translation:** 

**[15664.00s] English:** I think OpenAI and Anthropic  
**Translation:** 

**[15665.74s] English:** Are they purely laser-focused on?  
**Translation:** 

**[15668.04s] English:** AGI.  
**Translation:** 

**[15668.48s] English:** Yeah, agents and AGI.  
**Translation:** 

**[15670.54s] English:** And if I build AGI, I can make tons of money, right?  
**Translation:** 

**[15674.48s] English:** Or I can pay for everything, right?  
**Translation:** 

**[15675.94s] English:** And this is; it's just predicated,  
**Translation:** Vocabulary: predicated: 基于

**[15678.82s] English:** Like back on the export control thing, right?  
**Translation:** 

**[15680.60s] English:** If you think AGI is five or ten years away—or less—, right?  
**Translation:** 

**[15683.60s] English:** These labs think it's two or three years away.  
**Translation:** 

**[15686.06s] English:** Obviously, you're you're you're.  
**Translation:** 

**[15687.56s] English:** Your actions are, you know,  
**Translation:** 

**[15689.66s] English:** If you assume they are rational actors,  
**Translation:** 

**[15690.98s] English:** Which ones are mostly,  
**Translation:** 

**[15693.32s] English:** You're right; what do you do in a two-year AGI?  
**Translation:** 

**[15695.62s] English:** versus five years versus 10 years,  
**Translation:** 

**[15697.18s] English:** Very, very, very different, right?  
**Translation:** 

**[15699.90s] English:** Do you think agents are promising?  
**Translation:** 

**[15702.32s] English:** We'll have to talk about this.  
**Translation:** 

**[15703.54s] English:** This was, this is like the excitement of the year!  
**Translation:** 

**[15708.04s] English:** That agents are gonna,  
**Translation:** 

**[15709.22s] English:** This is the generic hype term.  
**Translation:** 

**[15713.20s] English:** That's a lot of business folks are using.  
**Translation:** Vocabulary: generic: 通用的

**[15714.88s] English:** AI agents are going to revolutionize everything.  
**Translation:** 

**[15717.32s] English:** Okay, so mostly the term "agent" is obviously  
**Translation:** Vocabulary: revolutionize: 彻底改变

**[15720.00s] English:** Overblown. We've talked a lot about reinforcement learning as a way to train for verifiable.  
**Translation:** 

**[15724.54s] English:** Outcomes should be open-ended and allow agents to solve tasks independently.  
**Translation:** Vocabulary: independently: 自主地; outcomes: 结果; reinforcement: 强化; verifiable: 可验证的

**[15729.84s] English:** On its own and able to adapt to uncertainty, there's a lot of terms applied to things.  
**Translation:** 

**[15734.84s] English:** Like Apple's intelligence, which we still don't have after the last WWDC, which is orchestrating.  
**Translation:** 

**[15740.74s] English:** Between apps, and that type of tool-use thing is something that language models can do really well.  
**Translation:** 

**[15745.68s] English:** Apple intelligence, I suspect, will come eventually. It's a closed domain. It's yours.  
**Translation:** 

**[15750.76s] English:** Messages app integrating with your photos, with AI in the background. That will work. That has  
**Translation:** 

**[15755.84s] English:** Been described as an "agent" by a lot of software companies to get into the narrative, the question...  
**Translation:** Vocabulary: integrating: 整合

**[15761.44s] English:** Is there any way we can get language models to generalize to new domains and solve their own problems?  
**Translation:** 

**[15769.10s] English:** Problems in real time? Maybe a tiny amount of training when they are doing this with fine-tuning.  
**Translation:** Vocabulary: generalize: 泛化

**[15774.30s] English:** They themselves or in context.  
**Translation:** 

**[15775.68s] English:** Learning, which is the idea of storing information in a prompt, and you can use learning algorithms.  
**Translation:** Vocabulary: prompt: 提示

**[15780.34s] English:** To update that, and whether or not you believe that it is going to actually generalize to things,...  
**Translation:** 

**[15786.28s] English:** Like me saying, "Book my trip to go to Austin in two days; I have XYZ constraints," and actually  
**Translation:** 

**[15794.88s] English:** Trusting it. I think there's an HCI problem coming back for information.  
**Translation:** 

**[15799.56s] English:** Well, what's your prediction there? Because my gut says we're very far away from that.  
**Translation:** 

**[15804.62s] English:** I think OpenAI....  
**Translation:** 

**[15805.68s] English:** Open AI's statement: I don't know if you've seen the five levels, right? Where it's chat is level.  
**Translation:** 

**[15810.52s] English:** One, reasoning is level two, and then agents is level three. And I think there are a couple more.  
**Translation:** 

**[15815.32s] English:** Levels, but it's important to note, right? We were in chat for a couple of years, right? We just...  
**Translation:** 

**[15820.56s] English:** Theoretically, we're going to be here for a year or two, right? And then the agents. But at the  
**Translation:** 

**[15825.60s] English:** At the same time, people can try to approximate the capabilities of the next level. But the agents,...  
**Translation:** Vocabulary: approximate: 估算; capabilities: 能力; theoretically: 理论上

**[15831.56s] English:** Are doing things autonomously, doing things for minutes at a time, hours at a time.  
**Translation:** 

**[15835.68s] English:** Et cetera, right? Reasoning is doing things for...  
**Translation:** Vocabulary: autonomously: 独立地

**[15840.00s] English:** Tens of seconds at a time. Right, and then coming back with an output that I still need to verify.  
**Translation:** 

**[15843.76s] English:** And use and try to check out. Right. So, and the biggest problem is, of course, like it's the same.  
**Translation:** Vocabulary: verify: 验证

**[15849.84s] English:** Thing with manufacturing, right? Like, there's the whole Six Sigma thing, right? Like, you know,  
**Translation:** 

**[15853.08s] English:** How many nines do you get? And then you compound the nines onto each other. And it's like, if you  
**Translation:** Vocabulary: sigma: 标准差

**[15856.78s] English:** Multiply by the number of steps that are six sigma, and you get to a yield.  
**Translation:** 

**[15862.98s] English:** A yield or something, right? So, in semiconductor manufacturing, tens of thousands.  
**Translation:** Vocabulary: multiply: 乘以; semiconductor: 半导体

**[15866.10s] English:** Of steps, nine is not enough. Right? Because you multiply.  
**Translation:** 

**[15870.60s] English:** That by that many times, you actually end up with a 60% yield, or zero, or zero. And this is the  
**Translation:** 

**[15876.90s] English:** Same thing with agents, right? Like chaining tasks together each time, LLMs—even the best LLMs—in  
**Translation:** 

**[15883.32s] English:** Particularly, pretty good benchmarks don't get a hundred percent, right? They get a little bit.  
**Translation:** Vocabulary: benchmarks: 衡量标准

**[15888.80s] English:** Below that, because there's a lot of noise. And so, how do you get to enough nines, right? This is the  
**Translation:** 

**[15894.88s] English:** The same thing with self-driving.  
**Translation:** 

**[15896.10s] English:** We don't, we can't have self-driving because without it being like super geo-fenced, like  
**Translation:** 

**[15899.88s] English:** Google, like, Google's right. And even then, they have a bunch of operators to make sure it  
**Translation:** Vocabulary: operators: 操作员

**[15903.28s] English:** Doesn't get stuck. Right. But you can't do that because it doesn't have enough nines.  
**Translation:** 

**[15906.94s] English:** And self-driving has quite a lot of structure because roads have rules. It's well-defined.  
**Translation:** 

**[15913.94s] English:** There's a regulation. When you're talking about computer use for the open web, for example,  
**Translation:** 

**[15919.76s] English:** For the open operating system, like there's no clear structure; it's a mess. So, the possibility,...  
**Translation:** 

**[15926.10s] English:** I'm always skeptical of any system that is tasked with interacting with the human world.  
**Translation:** 

**[15934.80s] English:** With the open, messy human world.  
**Translation:** Vocabulary: interacting: 互动; skeptical: 怀疑

**[15936.36s] English:** That's the thing: if we can't get intelligence, that's enough to solve the human world on its own.  
**Translation:** 

**[15940.74s] English:** Own. We can create infrastructure, like the human operators for Waymo over many years, that enable  
**Translation:** 

**[15946.70s] English:** Certain workflows.  
**Translation:** 

**[15947.64s] English:** There is a company—I don't remember its name—but it is literally their pitch. Yeah. We're  
**Translation:** Vocabulary: workflows: 工作流程

**[15951.46s] English:** Just going to be the human operator when agents fail, and you just call us and we'll fix it.  
**Translation:** 

**[15954.88s] English:** Yeah.  
**Translation:** 

**[15956.10s] English:** I call it hilarious. There will be teleoperation markets when we have human robots.  
**Translation:** 

**[15960.00s] English:** Is there going to be somebody around the world that's happy to fix the fact that it can't finish?  
**Translation:** Vocabulary: hilarious: 滑稽; teleoperation: 远程操作

**[15964.90s] English:** Loading the dishwasher when I'm unhappy with it, but that's just going to be part of the Tesla.  
**Translation:** 

**[15969.26s] English:** Service package. I'm just imagining, like, an AI agent talking to another AI agent—one company.  
**Translation:** Vocabulary: dishwasher: 洗碗机

**[15976.08s] English:** Has an agent that specializes in helping other AI agents, but if you can make things that are  
**Translation:** 

**[15981.98s] English:** Good, at one step you can stack them together, so that's why I'm like, if it takes a long...  
**Translation:** Vocabulary: specializes: 专门从事

**[15987.36s] English:** Time we're going to build infrastructure that enables it; you see, the operator launches, and they have...  
**Translation:** 

**[15991.82s] English:** Partnerships with certain websites, such as Doordash and OpenTable, and things like this or those.  
**Translation:** Vocabulary: doordash: 送餐应用; partnerships: 合作关系

**[15997.46s] English:** Partnerships are going to let them climb really fast. Their model is going to get really good at.  
**Translation:** 

**[16000.94s] English:** Those things will likely prove a concept that might be a network effect, where more companies  
**Translation:** 

**[16005.42s] English:** Want to make it easier for AI? Some companies will be like, "No, let's put blockers in place.  
**Translation:** 

**[16010.78s] English:** Yeah, and this is the story of the Internet. We've seen it now with training data for language models.  
**Translation:** 

**[16015.26s] English:** Models where companies are like, you have to pay:  
**Translation:** 

**[16017.36s] English:** Like business working it out, that said, I think that airlines have a very high  
**Translation:** 

**[16024.84s] English:** Incentive to make their site work really well, and they usually don't like if you look at how many.  
**Translation:** 

**[16030.78s] English:** Clicks it takes to order an airplane ticket—it's insane. I don't; you actually can't call an American  
**Translation:** Vocabulary: incentive: 动力

**[16036.12s] English:** Airlines agents don't have a phone number anymore, and it's really horrible.  
**Translation:** 

**[16041.72s] English:** On many of the interface fronts, it's hard to imagine that agents will be able to deal with everything.  
**Translation:** Vocabulary: interface: 界面

**[16046.48s] English:** That website  
**Translation:** 

**[16047.36s] English:** When I, as a human, struggle like I have an existential crisis every time I try to book,  
**Translation:** Vocabulary: existential: 存在主义的

**[16052.24s] English:** An airplane ticket that I don't think it's going to be extremely difficult to build an AI.  
**Translation:** 

**[16058.36s] English:** AI agent, that's robust, but think about how United has accepted the Starlink terms—which is they have  
**Translation:** Vocabulary: robust: 强壮的; starlink: 星链

**[16063.94s] English:** To provide Starlink for free, and the users are going to love it. What if one airline is like?  
**Translation:** 

**[16068.50s] English:** We're going to take a year and we're going to make our website have white text that works.  
**Translation:** 

**[16072.92s] English:** Perfectly for the AIS every time anyone asks about an AI flight.  
**Translation:** 

**[16077.36s] English:** They buy whatever airline ticket it is, or something like that.  
**Translation:** 

**[16080.00s] English:** Just like, here's an API, and it's only exposed to AI agents. If anyone queries it, the price is $10.  
**Translation:** 

**[16085.38s] English:** Higher, and for any flight, but we'll let you see any of our flights, and you can just book any.  
**Translation:** Vocabulary: queries: 询问

**[16090.02s] English:** Of them, here you go, Agent Man. Then it's like, "Oh, and I made $10 higher than the price." Awesome, yeah, and like  
**Translation:** 

**[16094.94s] English:** Am I willing to say that for, like, "Hey, book me a flight to see Lex"? And it's like, "Yeah, whatever.  
**Translation:** 

**[16098.62s] English:** Yeah, yeah, I think computers and the real world and the open world are really, really  
**Translation:** 

**[16105.00s] English:** Messy, um, but if you start defining the problem and narrowing the regions, people are going to be able  
**Translation:** Vocabulary: narrowing: 缩小范围

**[16111.00s] English:** To create very, very productive things, um, and ratchet down costs massively—right? Like, now, crazy!  
**Translation:** 

**[16118.54s] English:** Things, like you know, robotics in the home—you know, those are going to be a lot harder to do.  
**Translation:** Vocabulary: massively: 大幅度地

**[16123.44s] English:** Just like self-driving, right? Because there are just a billion different failure modes, right? But  
**Translation:** 

**[16128.74s] English:** Like agents that can navigate a certain set of websites and do certain sets of tasks.  
**Translation:** Vocabulary: navigate: 浏览

**[16133.62s] English:** Or, like, look at  
**Translation:** 

**[16135.00s] English:** You know, look at your groceries or your fridge and take a photo of them, or just upload them.  
**Translation:** Vocabulary: groceries: 食品杂货

**[16139.04s] English:** Your recipes, and then it figures out what to order from, you know, Amazon or Whole Foods.  
**Translation:** 

**[16143.94s] English:** Food delivery, like that's then going to be pretty quick and easy to do, I think so. It's  
**Translation:** Vocabulary: recipes: 食谱

**[16147.72s] English:** Going to be a whole range of business outcomes, and it's going to be tons of them.  
**Translation:** 

**[16151.80s] English:** Sort of optimism around people can just figure out ways to make money, to be clear, these sandboxes.  
**Translation:** Vocabulary: optimism: 乐观; outcomes: 结果; sandboxes: 实验区

**[16155.72s] English:** Already, there exist in research people who have built clones of all the most popular websites.  
**Translation:** 

**[16160.28s] English:** Of Google, Amazon, and blah, blah, blah, to make it so that there's  
**Translation:** 

**[16164.28s] English:** I mean  
**Translation:** 

**[16164.98s] English:** OpenAI probably has them internally to train these things, it's the same as DeepMind's Robotics Team.  
**Translation:** Vocabulary: internally: 内部; robotics: 机器人技术

**[16169.06s] English:** For years, there have been clusters for robotics where you can interact with robots fully remotely.  
**Translation:** 

**[16174.58s] English:** Just have a lab in London, and you send tasks to it. Arrange the blocks, and you do this research.  
**Translation:** Vocabulary: clusters: 机器人集群; remotely: 远程地

**[16179.62s] English:** Obviously, there are techs there that fix stuff, but we've turned these cranks of automation before.  
**Translation:** 

**[16186.26s] English:** You go from sandbox to progress, and then you add one more domain at a time.  
**Translation:** Vocabulary: automation: 自动化; cranks: 把手; sandbox: 沙箱环境

**[16190.98s] English:** And generalize, I think, in the history of NLP and language processing.  
**Translation:** 

**[16194.98s] English:** Instruction tuning and tasks per language model used to be like one language model did one task.  
**Translation:** Vocabulary: generalize: 泛化

**[16200.00s] English:** And then, in the instruction tuning literature, there's a point where you start adding more and more tasks together, at which point it just starts to generalize to every task.  
**Translation:** 

**[16207.34s] English:** And we don't know where on this curve we are.  
**Translation:** 

**[16208.96s] English:** I think, for reasoning with this RL and verifiable domains, we're early, but we don't know where the point is where you just start training on enough domains, and poof — like more domains just start working and you've crossed the generalization barrier.  
**Translation:** 

**[16222.08s] English:** Well, what do you think about the programming context?  
**Translation:** Vocabulary: barrier: 门槛; generalization: 泛化; verifiable: 可验证的

**[16225.82s] English:** So, software engineering.  
**Translation:** 

**[16227.06s] English:** That's where I personally, and I know many people, interact with AI the most.  
**Translation:** 

**[16234.58s] English:** There's a lot of fear and angst, too, from current CS students, but there's also an area where the most AI revenue and productivity gains have come—right?  
**Translation:** 

**[16244.32s] English:** Whether it be co-pilots, cursors, or whatever, right?  
**Translation:** Vocabulary: angst: 焦虑; cursors: 光标

**[16248.24s] English:** This is, or just standard Chat GPT, right?  
**Translation:** 

**[16250.40s] English:** Like a lot of people, I know very few programmers who don't have ChatGPT, and actually many of them have the $200 tier because that's what they use.  
**Translation:** 

**[16257.06s] English:** It's so good, right?  
**Translation:** 

**[16259.04s] English:** I think that in that world, we already see it, like SweBench.  
**Translation:** 

**[16264.02s] English:** And if you've looked at the benchmark made by some Stanford students, I wouldn't say it's really hard, but I wouldn't say it's easy either.  
**Translation:** 

**[16270.26s] English:** I think it takes someone who's been through at least a few years of CS or a couple of years of programming to do SweBench well.  
**Translation:** Vocabulary: benchmark: 参考标准; stanford: 斯坦福大学

**[16276.88s] English:** And the models went from 4% to 60% in just a year, right?  
**Translation:** 

**[16281.86s] English:** And where are they going to go next year?  
**Translation:** 

**[16283.80s] English:** You know, it's going to be higher.  
**Translation:** 

**[16284.94s] English:** It probably won't be 100%, because again, that 9%.  
**Translation:** 

**[16287.06s] English:** This is really hard to do, but we're going to get to a point where we'll need harder software engineering benchmarks, and so on.  
**Translation:** 

**[16293.98s] English:** But the way people think of it now is that it can do code completion easily.  
**Translation:** Vocabulary: benchmarks: 衡量标准; completion: 完成

**[16298.92s] English:** It can do some function generation, and I have to review it.  
**Translation:** 

**[16301.40s] English:** Great.  
**Translation:** 

**[16301.92s] English:** But, really, I think that software engineering agents can be developed faster and sooner than any other type of agent because it is a verifiable domain.  
**Translation:** 

**[16310.06s] English:** You can always like, unit test, or compile.  
**Translation:** Vocabulary: compile: 编译; verifiable: 可验证的

**[16313.04s] English:** And there are many different regions, like.  
**Translation:** 

**[16317.06s] English:** It can inspect the entire codebase at once, which no engineer can do.  
**Translation:** Vocabulary: codebase: 代码库; inspect: 检查

**[16320.00s] English:** Really, can only the architects really think about this stuff? The really senior guys, and they...  
**Translation:** 

**[16324.00s] English:** Can define stuff, and then the agent can execute on it. So I think software engineering costs.  
**Translation:** Vocabulary: execute: 执行

**[16328.48s] English:** Are going to plummet like crazy, and one interesting aspect of that is when software  
**Translation:** 

**[16332.92s] English:** Engineering costs are really low, you get very different markets, right? So in the U.S., you have  
**Translation:** Vocabulary: plummet: 急剧下降

**[16337.54s] English:** All these platform SaaS companies, like Salesforce and so on and so forth—right? In China, none...  
**Translation:** 

**[16343.80s] English:** Uses Platform SAS, everyone just builds their own stack because software engineering is much.  
**Translation:** Vocabulary: salesforce: 销售力云

**[16349.90s] English:** Cheaper in China, and partially because there are a lot of STEM graduates, etc., so  
**Translation:** 

**[16354.86s] English:** Stem, so it's generally just cheaper to do. Um, and so at the same time, code L like CodeLMS have.  
**Translation:** 

**[16361.30s] English:** Been adopted much less in China because the cost of an engineer there is much lower, but like what?  
**Translation:** 

**[16365.74s] English:** Happens when every company can just invent their own business logic, like really cheaply and quickly.  
**Translation:** Vocabulary: cheaply: 便宜地

**[16369.60s] English:** You stop using platform SAS, you start building custom-tailored solutions, and you change them really.  
**Translation:** 

**[16374.34s] English:** Quickly, now, all of a sudden, your business is a little bit more efficient, too, potentially because.  
**Translation:** 

**[16377.56s] English:** You're not dealing with the hell that is like some.  
**Translation:** 

**[16379.76s] English:** You're not dealing with the hell that is like some.  
**Translation:** 

**[16379.88s] English:** You're not dealing with the hell that is like some.  
**Translation:** 

**[16379.90s] English:** Platform SAS company stuff is not working perfectly, and we have to adjust workflows or deal with random business issues.  
**Translation:** Vocabulary: workflows: 工作流程

**[16385.08s] English:** Automation cases that aren't necessarily AI-required; it's just logic that needs to be built.  
**Translation:** 

**[16389.26s] English:** That no one has built right, all of these things can go much faster, and so I think software and  
**Translation:** Vocabulary: automation: 自动化

**[16393.22s] English:** Then, and then the other domain is that industrial, chemical, and mechanical engineers often suck at coding.  
**Translation:** 

**[16397.72s] English:** Right, uh, generally, and like their tools—semiconductor engineers' tools are 20 years old.  
**Translation:** 

**[16401.98s] English:** All of the tools run on XP, including ASML lithography tools, which run on Windows XP, right?  
**Translation:** 

**[16409.88s] English:** All the tools run on XP, including ASML lithography tools, which run on Windows XP, right?  
**Translation:** Vocabulary: lithography: 光刻技术

**[16411.56s] English:** Just like guys, you guys can move 20 years forward with all the data you have and gathered, and do a  
**Translation:** 

**[16416.14s] English:** It's a lot better, but you just need the engineering skills for software engineering to be delivered.  
**Translation:** 

**[16420.46s] English:** To the actual domain expert engineers, so I think that's the area where I'm like super duper.  
**Translation:** 

**[16424.66s] English:** Bullish on AI generally, I think it's creating value in the big picture. I don't think it's going to be a  
**Translation:** Vocabulary: bullish: 乐观

**[16430.24s] English:** It's like we talked to anything; a really good example of how growth changes is when Meta.  
**Translation:** 

**[16437.94s] English:** Added stories, so Snapchat was on an  
**Translation:** 

**[16439.76s] English:** I expect.  
**Translation:** 

**[16440.00s] English:** Exponential growth, they added stories, it flatlined, and then software engineers went right.  
**Translation:** Vocabulary: exponential: 指数增长; flatlined: 停滞不前

**[16445.00s] English:** AI is going to come in; it's probably just going to be flat, it's like it's a lot like everyone's.  
**Translation:** 

**[16449.10s] English:** Going to lose their job is hard because the supply corrects more slowly, so the amount of  
**Translation:** 

**[16454.20s] English:** Students are still growing, and that will correct with a multi-year delay — about a one-year lag.  
**Translation:** 

**[16460.02s] English:** Jobs will just turn, and then maybe in 20-40 years, it'll be well down, but in the few years, there'll  
**Translation:** 

**[16467.24s] English:** Never will there be a "snap" moment where it's like software engineers aren't useful. I think also,  
**Translation:** 

**[16471.12s] English:** Nature of what it means to be a programmer and what kinds of jobs programmers do changes, because I  
**Translation:** Vocabulary: programmer: 编程人员; programmers: 编程人员

**[16476.00s] English:** Think there needs to be a human in the loop of everything you've talked about. There's a really  
**Translation:** 

**[16482.38s] English:** Important human in that picture, like correcting the code and fixing something larger than the context.  
**Translation:** 

**[16490.50s] English:** Length, yep, and debugging—also like debugging by sort of reading the code and understanding.  
**Translation:** 

**[16497.18s] English:** Understanding  
**Translation:** 

**[16497.22s] English:** The steering system, like, no, no, you missed the point; adding more to the prompt, kind of like...  
**Translation:** 

**[16502.82s] English:** Yes, adding the human touch in designing the perfect Google button; Google is famous for having people design it.  
**Translation:** Vocabulary: prompt: 提示; steering: 转向

**[16508.96s] English:** Buttons that are so perfect, and it's like, how is AI going to do that? It's like,  
**Translation:** 

**[16513.78s] English:** They could give you all the ideas, perfect—I mean, that's the thing; you can call it taste, humans have.  
**Translation:** 

**[16520.36s] English:** One thing humans can do is figure out what other humans enjoy better than AI systems—that's where.  
**Translation:** 

**[16525.98s] English:** The preference you  
**Translation:** 

**[16527.16s] English:** Loading that in, but ultimately, humans are the greatest preference. Generate that's where the  
**Translation:** 

**[16531.80s] English:** Preference comes from, and humans are actually very good at reading or liking to judge between two things.  
**Translation:** 

**[16536.68s] English:** Versus, this is something that goes back to the core of what RLHF and preference tuning is: it's hard.  
**Translation:** 

**[16541.12s] English:** To generate a good answer for a lot of problems, but it's easy to see which one is better, and that's  
**Translation:** 

**[16545.32s] English:** How we're using humans for AI now is judging which one is better, and that's what the software does.  
**Translation:** 

**[16549.64s] English:** Engineering could look like it's the PR review. Here's a few options: what are the likes?  
**Translation:** 

**[16555.10s] English:** Some potential pros and cons.  
**Translation:** 

**[16557.16s] English:** And they're going to be judgmental judges.  
**Translation:** Vocabulary: judgmental: 爱挑剔的

**[16560.00s] English:** Think the thing I would very much recommend is that people starting programming start using AI.  
**Translation:** 

**[16565.04s] English:** And embracing that role as the supervisor of the AI system and like a partner with the AI system.  
**Translation:** Vocabulary: embracing: 接纳; supervisor: 监督者

**[16570.96s] English:** Versus writing from scratch, or not learning coding at all and just generating stuff because I think.  
**Translation:** 

**[16577.22s] English:** There actually has to be a pretty high level of expertise as a programmer to be able to manage.  
**Translation:** Vocabulary: programmer: 程序员; scratch: 从零开始

**[16581.64s] English:** Increasingly intelligent systems, I think it's that and then becoming a domain expert.  
**Translation:** 

**[16586.36s] English:** In something, sure, yeah, right? Because you like, seriously, if you go look at aerospace or  
**Translation:** Vocabulary: aerospace: 航空航天

**[16590.66s] English:** Semiconductors or chemical engineering—everyone is using really crappy platforms and really old software.  
**Translation:** 

**[16595.88s] English:** Like the job of data science is like a joke, right? In many cases, it's  
**Translation:** Vocabulary: crappy: 糟糕的; semiconductors: 半导体

**[16602.00s] English:** Very real, but it's like bringing what the forefront of human capabilities are to your domain and like  
**Translation:** 

**[16607.16s] English:** Even if the forefront is like from the AI, your domain, you're like at the forefront, right? So it's  
**Translation:** Vocabulary: capabilities: 能力; forefront: 前沿

**[16611.20s] English:** Like, it's like you have to be at the forefront of something and then leverage the rising trend.  
**Translation:** 

**[16615.74s] English:** Tide that is at the forefront of something, and then leverage the like rising tide that is the  
**Translation:** Vocabulary: leverage: 利用

**[16616.34s] English:** AI for Everything Else, oh, yeah, there are so many low-hanging fruits everywhere in terms of where.  
**Translation:** 

**[16622.56s] English:** Software can help automate a thing or digitize a thing in a legal system, I mean that's why.  
**Translation:** Vocabulary: automate: 自动化; digitize: 数字化

**[16629.28s] English:** Doge is exciting. You have, I mean, I got to hang out with a bunch of the Doge folks, and they...  
**Translation:** 

**[16636.40s] English:** I mean, government is like so old-school; it's like begging for the modernization of its software.  
**Translation:** Vocabulary: modernization: 现代化

**[16645.74s] English:** Organizing and...  
**Translation:** 

**[16646.32s] English:** The data, all this kind of stuff—I mean, in that case—is by design because bureaucracy creates it.  
**Translation:** Vocabulary: bureaucracy: 官僚主义

**[16651.84s] English:** Protects centers of power, and so on, but software breaks down those barriers; uh, so it hurts.  
**Translation:** 

**[16660.46s] English:** Those who are holding on to power, but ultimately benefit humanity, so there's a bunch of domains.  
**Translation:** Vocabulary: barriers: 障碍

**[16667.32s] English:** Of that kind, one thing we didn't fully finish talking about is open source. So, first of all,  
**Translation:** 

**[16675.50s] English:** Congrats, you released a new model! Yeah, this is TULU.  
**Translation:** Vocabulary: congrats: 恭喜

**[16680.00s] English:** I'll explain what a Tulu is.  
**Translation:** 

**[16681.52s] English:** A Tulu is a hybrid camel when you breed a Dromedary with a Bactrian camel.  
**Translation:** Vocabulary: bactrian: 双峰驼; dromedary: 单峰驼; hybrid: 杂交

**[16686.38s] English:** Back in the early days after ChatGPT, there was a big wave of models coming out, like Alpaca.  
**Translation:** 

**[16691.38s] English:** Vicuna, et cetera, were all named after various mammalian species.  
**Translation:** Vocabulary: alpaca: 羊驼; cetera: 等等; mammalian: 哺乳动物; vicuna: 羊驼

**[16695.52s] English:** So, Tulu, the brand is multiple years old, which comes from that.  
**Translation:** 

**[16700.10s] English:** And we've been playing at the frontiers of post-training with open-source code.  
**Translation:** Vocabulary: frontiers: 边界地带

**[16705.32s] English:** And this first part of this release was in the fall, where we have built on LLAMA's open.  
**Translation:** 

**[16712.48s] English:** Models, open-weight models, and then we add in our fully open code and fully open data.  
**Translation:** 

**[16717.82s] English:** There's a popular benchmark called Chatbot Arena, and that's generally the metric by which...  
**Translation:** 

**[16722.44s] English:** How are these chat models evaluated?  
**Translation:** Vocabulary: benchmark: 参考标准; chatbot: 聊天机器人; evaluated: 评估; metric: 衡量指标

**[16724.94s] English:** And it's humans comparing random models from different organizations.  
**Translation:** 

**[16728.68s] English:** And if you looked at the leaderboard in November or December, among the top 60 models from:  
**Translation:** Vocabulary: leaderboard: 排行榜

**[16733.70s] English:** In the 10s to 20s, there was a lot of activity in the chatbot arena.  
**Translation:** 

**[16735.32s] English:** None of them had open code or data for just post-training.  
**Translation:** 

**[16738.56s] English:** Among them, even fewer—or none—have pre-training data and code available.  
**Translation:** 

**[16742.06s] English:** But post-training is much more accessible at this time.  
**Translation:** 

**[16744.42s] English:** It's still pretty cheap, and you can do it.  
**Translation:** 

**[16746.32s] English:** And the thing is: How high can we push this number where people have access to all the  
**Translation:** 

**[16750.32s] English:** Code and data?  
**Translation:** 

**[16751.36s] English:** So, that's kind of the motivation for the project.  
**Translation:** 

**[16752.88s] English:** We draw on lessons from LLAMA.  
**Translation:** 

**[16754.40s] English:** NVIDIA had a Nemotron model, where the recipe for their post-training was fairly open with:  
**Translation:** Vocabulary: nemotron: nemotron模型; recipe: 训练后调优方法

**[16759.32s] English:** Some data and a paper.  
**Translation:** 

**[16761.46s] English:** And it's putting all these together to try to create a recipe that people can.  
**Translation:** 

**[16764.74s] English:** Fine-tune models like GPT-4 for their domain.  
**Translation:** 

**[16767.86s] English:** So, to be clear, in the case of TULU, maybe you can talk about ALMA too, but in the case  
**Translation:** 

**[16772.94s] English:** Of TULU, you're taking LLAMA 3, 4, and 5B.  
**Translation:** 

**[16778.92s] English:** Tulu has been a series of recipes for post-training.  
**Translation:** Vocabulary: recipes: 训练方案

**[16781.44s] English:** So, we've done multiple models over the years.  
**Translation:** 

**[16783.56s] English:** And so you're open-sourcing everything.  
**Translation:** 

**[16786.68s] English:** Yeah.  
**Translation:** 

**[16786.96s] English:** If you start with an open-weight-based model, the whole model technically is open source.  
**Translation:** Vocabulary: technically: 实际上

**[16791.48s] English:** Because you don't know what LLAMA put into it.  
**Translation:** 

**[16793.56s] English:** Which is why we have this.  
**Translation:** 

**[16794.78s] English:** It's a separate thing, and we'll get to it.  
**Translation:** 

**[16795.92s] English:** But it's just getting parts of the pipeline where people can zoom in and customize.  
**Translation:** Vocabulary: pipeline: 管道

**[16800.00s] English:** Eyes, I know I hear from startups and businesses that they're like, "Okay, like I can take this post.  
**Translation:** 

**[16803.60s] English:** Training and trying to apply it to my domain, we talk a lot about verifiers, and we use this idea which is  
**Translation:** Vocabulary: startups: 初创企业; verifiers: 验证者

**[16808.96s] English:** Reinforcement learning with verifiable domain rewards (RLVR) is kind of similar to RLHF, and we  
**Translation:** 

**[16816.72s] English:** Applied it to the map and the model today, which is like we applied it to the LLaMA 40B base model.  
**Translation:** Vocabulary: reinforcement: 强化; rewards: 奖励; verifiable: 可验证的

**[16822.80s] English:** From last year, and we have our other stuff—we have our instruction tuning.  
**Translation:** 

**[16826.76s] English:** And/or preference tuning, but the math thing is interesting; it's easier to improve.  
**Translation:** 

**[16832.88s] English:** This math benchmark is called "MATH." It's a tough name to remember when the benchmark is given.  
**Translation:** 

**[16838.98s] English:** Is name is the area that you're evaluating. We're researchers, we're not brands.  
**Translation:** Vocabulary: benchmark: 参考标准; evaluating: 评估

**[16843.28s] English:** Brand strategists, and this is something that the DeepSeek paper also discussed, as well as like at  
**Translation:** 

**[16848.62s] English:** This bigger model is easier to elicit powerful capabilities with this RL training, and then they...  
**Translation:** Vocabulary: capabilities: 能力; elicit: 激发; strategists: 策略师

**[16853.80s] English:** Distill it down from that big model to the small model, and  
**Translation:** 

**[16856.76s] English:** This model, which we released today, we saw the same thing as we are at AI2—we don't have a ton of.  
**Translation:** Vocabulary: distill: 提炼

**[16861.86s] English:** Compute: We can't train 405B models all the time, so we just did a few runs, and they tend to work.  
**Translation:** 

**[16866.70s] English:** And it's like it just shows that there's a lot of room for people to play in these things, and that  
**Translation:** Vocabulary: compute: 计算

**[16872.58s] English:** And they crushed Llama's actual release, right? Like, they're way better than it. Yeah, so our.  
**Translation:** 

**[16877.38s] English:** Valve numbers, I mean, we have extra months in this, but our valve numbers are much better than.  
**Translation:** Vocabulary: valve: 阀门

**[16881.46s] English:** The Llama instruct model that they released, and then you also said it was better than DeepSeek V3.  
**Translation:** 

**[16886.76s] English:** On our eval benchmark, the Most Deep Seek V3 is really similar. We have a safety benchmark to  
**Translation:** Vocabulary: instruct: 指导; llama: 羊驼

**[16892.56s] English:** Understand if it will say harmful things, and that's what draws down most.  
**Translation:** 

**[16896.54s] English:** Of the way, it's still like an amalgamation of multiple benchmarks. Or what do you mean? Yeah.  
**Translation:** Vocabulary: amalgamation: 混合体; benchmarks: 参考标准

**[16900.32s] English:** So, we have a 10-value system. This is like standard practice in post-training; you choose,...  
**Translation:** 

**[16903.96s] English:** Your evaluations, which you care about in academics, and smaller labs will have fewer evaluations.  
**Translation:** Vocabulary: evaluations: 评估

**[16908.66s] English:** In companies, you'll have a really specific domain that you really care about. At Frontier Labs, you'll have  
**Translation:** 

**[16913.22s] English:** 10-20 to maybe even up to 100 evaluations of specific things.  
**Translation:** Vocabulary: frontier: 前沿领域

**[16916.76s] English:** So, we choose a representative suite of things that look like chat.  
**Translation:** 

**[16920.00s] English:** Precise instruction, following which is like responding only in emojis: Does the model?  
**Translation:** 

**[16924.20s] English:** Follow weird things like that, yeah? Math, code, and you create a suite like this, so safety would be...  
**Translation:** 

**[16928.90s] English:** One of 10 in that type of suite, where you have, like, what is the broader community of AI care?  
**Translation:** 

**[16933.96s] English:** About, and for example, in comparison to DeepSeek, it would be something like our average eval for.  
**Translation:** 

**[16938.86s] English:** Our model would be $80, including safety features, and a similar one without those features would be around $79.  
**Translation:** 

**[16944.72s] English:** Percent average score, without safety and their safety score would bring it down. Like, oh, so you  
**Translation:** 

**[16952.22s] English:** Beat them, even ignoring safety, yeah. So, this is something that internally, I don't want.  
**Translation:** Vocabulary: internally: 内部地

**[16957.10s] English:** To win, you need to shape the evaluation benchmark in your favor. If there's something that's like  
**Translation:** 

**[16960.62s] English:** People may or may not care about safety in their models. Safety can come downstream, and safety can be...  
**Translation:** Vocabulary: benchmark: 评价标准; downstream: 后期阶段; evaluation: 评估

**[16965.04s] English:** When you host the model for an API, like safety, it is addressed in a spectrum of locations in a  
**Translation:** 

**[16969.86s] English:** Application: So, it's like if you want to say that you have the best recipe, you can't just keep it to yourself.  
**Translation:** Vocabulary: recipe: 食谱

**[16973.62s] English:** On these things, that some people don't know about, you can't just say that you have the best recipe.  
**Translation:** 

**[16974.70s] English:** People might not want that, and this is because it's like the time of progress; we benefit if we  
**Translation:** 

**[16981.74s] English:** Can we release a model later? We have more time to learn new techniques, like this RL technique.  
**Translation:** 

**[16986.28s] English:** Had started this in the fall; it's now really popular. Reasoning: the next thing to do...  
**Translation:** 

**[16990.74s] English:** For open-source post-training, it is to scale up verifiers to scale up data to replicate some.  
**Translation:** 

**[16995.78s] English:** Of DeepSeek's results, and it's awesome that we have a paper to draw on; it makes it a lot better.  
**Translation:** Vocabulary: verifiers: 验证器

**[16999.62s] English:** Easier, and that's the type of things that are going on among  
**Translation:** 

**[17004.54s] English:** You.  
**Translation:** 

**[17004.70s] English:** Academic and closed-frontier research in AI: Since you're pushing open-source, what do you think is  
**Translation:** 

**[17010.34s] English:** The future of it, you think DeepSeek actually changes things since it's open-source or open.  
**Translation:** 

**[17015.74s] English:** Weight, or is pushing the open-source movement into an open direction? This goes very back to  
**Translation:** 

**[17020.02s] English:** License discussion: So, deep-seek R1 with a friendly license is a major reset, so it's like the first.  
**Translation:** 

**[17024.80s] English:** Time that we've had a really clear frontier model that is open weights and with a commercially  
**Translation:** 

**[17030.06s] English:** Friendly license with no restrictions on downstream use cases, synthetic data, distillation: whatever.  
**Translation:** Vocabulary: commercially: 商业上; distillation: 蒸馏; frontier: 前沿; synthetic: 合成的

**[17034.70s] English:** This has never been the case at all in the history of AI. In the last few years, since Chachi BT, there have  
**Translation:** 

**[17039.86s] English:** Been  
**Translation:** 

**[17040.00s] English:** Models that are off the frontier, or models with weird licenses that you can't really use.  
**Translation:** 

**[17043.98s] English:** So, isn't Meta's license basically permissible except for five companies?  
**Translation:** Vocabulary: permissible: 允许的

**[17048.42s] English:** Um, and there's also, so this goes to what open-source AI is, which is there are also use cases.  
**Translation:** 

**[17054.18s] English:** Restrictions in the Llama License, which says you can't use it for specific things, so if you come  
**Translation:** Vocabulary: llama: 羊驼

**[17058.24s] English:** From an open-source software background, you would say that that is not an open-source license, what?  
**Translation:** 

**[17062.40s] English:** Kind of things are those, though. Like, are they? It's like, I at this point can't pull them off.  
**Translation:** 

**[17067.08s] English:** But it will be like a competitor; it used to be for military use, but they removed that.  
**Translation:** 

**[17071.64s] English:** For scale, it'll be like child abuse material, or like that's the type of thing.  
**Translation:** 

**[17078.46s] English:** That is forbidden there, but that's enough from an open-source background to say it's not open.  
**Translation:** 

**[17082.68s] English:** Source license, and also the Llama license, has this horrible thing where you have to name your model.  
**Translation:** 

**[17087.78s] English:** If you touch it to the llama model, so it's like the branding thing, so if a company uses llama.  
**Translation:** 

**[17093.48s] English:** Technically, the license says that they should say "Built with Llama" at the bottom of their  
**Translation:** Vocabulary: technically: 按技术上说

**[17096.84s] English:** Application:  
**Translation:** 

**[17097.08s] English:** And, from a marketing perspective, that just hurts. Like, I could suck it up, but...  
**Translation:** 

**[17101.42s] English:** A researcher, I'm like, "Oh, it's fine. It says 'llama-dash' on all of our materials.  
**Translation:** 

**[17106.12s] English:** For this release, but this is why we need truly open models, which is, uh, we don't know DeepSeek.  
**Translation:** 

**[17111.06s] English:** R1's data. So, you're saying I can't make a cheap copy of Llama and pretend it's mine?  
**Translation:** 

**[17115.92s] English:** But I can do this with the Chinese model, yeah. Hell yeah, that's what I'm saying, and yeah.  
**Translation:** 

**[17121.56s] English:** And that's why we want this whole open language models thing, the OLMO thing, is  
**Translation:** 

**[17126.84s] English:** To try to keep the model where everything is open, with the data as close to the frontier as possible.  
**Translation:** Vocabulary: frontier: 最前沿

**[17131.56s] English:** Possible, so we're compute-constrained, we're personnel-constrained, and we're relying on getting.  
**Translation:** 

**[17136.26s] English:** Insights from people like John Shulman tell us to do RL on outputs: like we can make these big.  
**Translation:** Vocabulary: outputs: 输出

**[17141.12s] English:** Jumps, but it just takes a long time to push the frontier of open source, and fundamentally, I would...  
**Translation:** 

**[17146.88s] English:** Say that that's because open-source AI does not have the same feedback loops as proprietary software.  
**Translation:** Vocabulary: fundamentally: 本质上; proprietary: 私有的

**[17151.44s] English:** Software we talked about, open-source software for security, is just because you build something.  
**Translation:** 

**[17156.84s] English:** You can reuse it if you go into a new company; there are so many benefits.  
**Translation:** Vocabulary: reuse: 重复使用

**[17160.00s] English:** But if you open-source a language model, you have this data sitting around, and you have this training code. It's not that easy for someone to come in and build on and improve because you need to spend a lot on compute. You need to have expertise. So until there are feedback loops of open-source AI, it seems like mostly an ideological mission.  
**Translation:** 

**[17177.90s] English:** Like people like Mark Zuckerberg, which is like America needs this. And I agree with him. But in the time when the motivation ideologically is high, we need to capitalize and build this ecosystem around what benefits you get from seeing the language model data.  
**Translation:** Vocabulary: capitalize: 利用; compute: 计算; ideological: 意识形态的; ideologically: 从意识形态角度

**[17193.14s] English:** And there's not a lot about that. We're going to try to launch a demo soon where you can look at an OMO model and a query and see what pre-training data is similar to it, which is like legally risky and complicated.  
**Translation:** 

**[17204.34s] English:** But what does it mean to see the data?  
**Translation:** 

**[17207.38s] English:** That the AI was trained on? It's hard to parse. It's terabytes of files. I don't know what I'm going to find in there.  
**Translation:** 

**[17214.10s] English:** But that's what we need to do as an ecosystem. If people want open-source AI to be financially useful.  
**Translation:** Vocabulary: financially: 在经济上; parse: 解析; terabytes: 太字节

**[17221.08s] English:** We didn't really talk about Stargate. I would love to get your opinion on, like, what the new administration (the Trump administration) is doing, especially everything that's being done on the American side and supporting AI infrastructure and the efforts of different AI companies.  
**Translation:** 

**[17236.00s] English:** What do you think about Stargate?  
**Translation:** Vocabulary: stargate: 星际之门

**[17237.40s] English:** What are we supposed to think about Stargate? And do Sam have the money?  
**Translation:** 

**[17243.30s] English:** Yeah, so I think Stargate is an opaque thing. It definitely doesn't have $500 billion. Doesn't even have $100 billion, right?  
**Translation:** Vocabulary: opaque: 不透明的

**[17250.66s] English:** So, what they announced is this $500 billion number, Larry Ellison, Sam Altman, and Trump said it.  
**Translation:** 

**[17257.00s] English:** They thanked Trump, and he did do some executive actions that significantly improved the ability for this to be built faster.  
**Translation:** Vocabulary: altman: 萨姆·阿尔特曼; ellison: 拉里·埃利森

**[17267.38s] English:** You know, one of the executive actions he took is on federal land, where you can basically build data centers with power, you know, kind of like that.  
**Translation:** 

**[17274.32s] English:** And then, the permitting process is basically gone, or you file after the fact.  
**Translation:** Vocabulary: permitting: 审批程序

**[17277.90s] English:** So, like, one of the things again, like I said,  
**Translation:** 

**[17280.00s] English:** Schizo-take: Earlier, another Schizo-take. If you've ever been to the Presidio in San Francisco,...  
**Translation:** Vocabulary: presidio: 旧金山军事基地

**[17283.88s] English:** Beautiful area; you could build a power plant and a data center there if you wanted to.  
**Translation:** 

**[17288.04s] English:** Because it is federal land, it used to be a military base, but you know, obviously, this.  
**Translation:** 

**[17293.02s] English:** Would like to piss people off, you know? It's a good bit, anyways. Trump has made it much easier to do.  
**Translation:** 

**[17299.32s] English:** This is right; generally, Texas has the only unregulated grid in the nation as well. Let's go, Texas!  
**Translation:** Vocabulary: texas: 德克萨斯州; unregulated: 不受监管的

**[17304.92s] English:** And so, you know, ERCOT enables people to build faster, as well. In addition,  
**Translation:** 

**[17310.64s] English:** Federal regulations are coming down, um, and so Stargate is predicated on this, is why that whole  
**Translation:** Vocabulary: predicated: 基于

**[17316.20s] English:** Show me how they came up with a $500 billion dollar number; that's beyond me.  
**Translation:** 

**[17321.28s] English:** Up with a hundred billion-dollar number makes sense to some extent, right? And, um, there's actually  
**Translation:** 

**[17326.58s] English:** A good table in here that I would like to show, um, in the Stargate piece that I had, um,  
**Translation:** 

**[17332.30s] English:** It's  
**Translation:** Vocabulary: stargate: 星门

**[17334.90s] English:** It's the most recent one, yeah. So, anyway, Stargate... You know, it's basically  
**Translation:** 

**[17340.22s] English:** Right, like there is a table about costs. Um, you passed it already; it's that one.  
**Translation:** 

**[17347.40s] English:** So, this table is kind of explaining what happens. Right? Stargate is in Abilene, Texas, the first.  
**Translation:** 

**[17354.48s] English:** Hundred billion dollars of it, uh, that site is 2.2 gigawatts of power, in about 1.8 gigawatts of power.  
**Translation:** Vocabulary: abilene: 美国德克萨斯州的阿比林; gigawatts: 吉瓦

**[17360.84s] English:** Uh, consumed right? Per GPU, they have like roughly, uh, Oracle is already building the first.  
**Translation:** 

**[17368.50s] English:** Part of this, before Stargate came about, to clear, they've been building it for a year they  
**Translation:** 

**[17372.82s] English:** Tried to rent it to Elon, in fact. Right? Um, but Elon was like, "It's too slow; I need it faster.  
**Translation:** 

**[17377.52s] English:** Then he went and did his Memphis thing, um, and so I was able to get it with this like.  
**Translation:** Vocabulary: memphis: 孟菲斯

**[17382.34s] English:** Weird joint venture called Stargate; uh, they initially signed a deal with just Oracle for.  
**Translation:** 

**[17386.20s] English:** The first section of this cluster, right? Is  
**Translation:** Vocabulary: cluster: 聚集; venture: 合作

**[17390.84s] English:** Roughly five billion to six billion dollars of server spend, and then there's  
**Translation:** 

**[17397.32s] English:** Another billion or so of data center spend, but  
**Translation:** 

**[17400.00s] English:** And then, likewise, if you fill out that entire 1.8 gigawatts with the next two generations of NVIDIA's chips—GB200, GB300, VR200—and you fill it out completely, that ends up being roughly $50 billion in server costs, right?  
**Translation:** 

**[17415.54s] English:** Plus there's data center cost, plus maintenance cost, plus operation cost, plus all these things.  
**Translation:** Vocabulary: likewise: 同样地

**[17421.08s] English:** And that's where OpenAI gets to their $100 billion announcement, right?  
**Translation:** 

**[17425.40s] English:** Because they talked about $100 billion in phase one.  
**Translation:** 

**[17427.92s] English:** That's the Abilene, Texas data center, right?  
**Translation:** 

**[17430.22s] English:** $100 billion of total cost of ownership, "quote unquote," right?  
**Translation:** Vocabulary: unquote: 引用结束

**[17433.32s] English:** So, it's not CapEx.  
**Translation:** 

**[17434.40s] English:** It's not an investment.  
**Translation:** 

**[17435.22s] English:** It's a $100 billion total cost of ownership.  
**Translation:** 

**[17438.40s] English:** And then there will be future phases.  
**Translation:** Vocabulary: phases: 阶段

**[17440.74s] English:** They're looking at other sites that are even bigger than this 2.2 gigawatts, by the way, in Texas and elsewhere.  
**Translation:** 

**[17446.50s] English:** And so, they're not completely ignoring that.  
**Translation:** Vocabulary: gigawatts: 吉瓦; texas: 德克萨斯州

**[17449.22s] English:** But there is the $100 billion that they say is for phase one, which I do think will happen.  
**Translation:** 

**[17455.50s] English:** They don't even have the money for that.  
**Translation:** 

**[17457.28s] English:** Furthermore, it's not $100 billion.  
**Translation:** 

**[17458.40s] English:** It's $50 billion of spend, right?  
**Translation:** 

**[17460.16s] English:** And then, like $50 billion in operational costs, power, et cetera, and rental pricing, et cetera.  
**Translation:** 

**[17466.70s] English:** Because OpenAI is renting the GPUs from the Stargate joint venture, right?  
**Translation:** Vocabulary: cetera: 等等; rental: 租赁; stargate: 星门; venture: 合资企业

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

**[17478.66s] English:** Everyone knows that they've only got $6 billion in their last round, and $4 billion in debt.  
**Translation:** 

**[17482.92s] English:** But there is news of....  
**Translation:** 

**[17485.40s] English:** Like SoftBank maybe investing $25 billion into OpenAI, right?  
**Translation:** 

**[17489.12s] English:** So that's part of it, right?  
**Translation:** 

**[17490.78s] English:** So, $19 billion can come from there.  
**Translation:** 

**[17492.44s] English:** So, OpenAI does not have the money at all, right?  
**Translation:** 

**[17494.28s] English:** To be clear.  
**Translation:** 

**[17495.66s] English:** Inc. is not dried on anything.  
**Translation:** 

**[17497.26s] English:** OpenAI has $0 for this $50 billion, right?  
**Translation:** 

**[17499.82s] English:** In which they are legally obligated to put $19 billion of CapEx into the joint venture.  
**Translation:** 

**[17503.70s] English:** And then the rest will be paid via renting the GPUs from the joint venture.  
**Translation:** Vocabulary: obligated: 有法律义务

**[17506.80s] English:** And then there's Oracle.  
**Translation:** 

**[17509.90s] English:** Oracle has a lot of money.  
**Translation:** 

**[17511.70s] English:** They're building the first section completely.  
**Translation:** 

**[17513.38s] English:** They were spending on it themselves, right?  
**Translation:** 

**[17514.78s] English:** This is $6 billion.  
**Translation:** 

**[17515.34s] English:** $10 billion of CapEx.  
**Translation:** 

**[17516.34s] English:** $10 billion of TCO.  
**Translation:** 

**[17518.80s] English:** But they...  
**Translation:** 

**[17519.56s] English:** And they were going to....  
**Translation:** 

**[17520.00s] English:** To do that, first section, they're paying for that, right? Um, as far as the rest of the section, I don't...  
**Translation:** 

**[17523.90s] English:** Know how much Larry wants to spend; right, at any point, he could pull it out, like this is again.  
**Translation:** 

**[17528.10s] English:** It's like completely voluntary, so at any point, there's no signed ink on this, right? But he  
**Translation:** Vocabulary: voluntary: 自愿的

**[17532.36s] English:** Potentially, he could contribute tens of billions of dollars. Right to be clear, he's got the money.  
**Translation:** 

**[17535.44s] English:** Oracle's got the money, um, and then there's MGX, which is the South UAE fund, which technically,...  
**Translation:** 

**[17540.90s] English:** Has $1.5 trillion for investing in AI, but again, I don't know how real that money is.  
**Translation:** 

**[17546.92s] English:** And, like, whereas there is no ink signed for this, SoftBank does not have $25 billion of cash.  
**Translation:** Vocabulary: trillion: 万亿

**[17552.80s] English:** They have to sell down their stake in ARM, uh, which is you know the leader in CPUs, and they IPO'd.  
**Translation:** 

**[17558.20s] English:** It's obvious that this is what they've always wanted to do, but they just didn't know where they'd redeploy.  
**Translation:** Vocabulary: redeploy: 重新部署

**[17560.92s] English:** The capital is selling down its stake in ARM, making a lot of sense so they can sell that down and  
**Translation:** 

**[17565.72s] English:** Invest in this if they want to, and invest in open-air if they want to. As far as money,  
**Translation:** 

**[17570.38s] English:** Secured the first hundred thousand GB200 cluster is like; can the funding be secured, and everything else after?  
**Translation:** 

**[17576.90s] English:** That's up in the air. Money's coming, I believe the money will come, I personally do just  
**Translation:** Vocabulary: cluster: 计算集群

**[17582.36s] English:** It's a belief, okay. It's a belief that they are going to release better models and be able to  
**Translation:** 

**[17586.26s] English:** Raise more, yeah, right? But like, the actual reality is that Elon's right: there is the money, does  
**Translation:** 

**[17591.38s] English:** Not exist, right? What does the U.S. government have to do with anything? What does Trump have to do with it?  
**Translation:** 

**[17595.82s] English:** With everything he's just a hype man, Trump is he's reducing regulations so they can build it.  
**Translation:** 

**[17600.04s] English:** Faster, right? Um, and he's allowing them to do it, right? You know, because any investment of this...  
**Translation:** 

**[17605.14s] English:** Side is going to involve, like, antitrust stuff, right?  
**Translation:** Vocabulary: antitrust: 反垄断

**[17606.90s] English:** Like so, obviously he's going to allow them to do it and enable the regulations.  
**Translation:** 

**[17610.90s] English:** To actually allow it to be built, I don't believe there are any U.S. government dollars being spent on.  
**Translation:** 

**[17616.02s] English:** This, though, yeah, so I think he's also just creating a general vibe that this is regulation.  
**Translation:** 

**[17621.58s] English:** Will go down, and this is the era of building. So, if you're a builder, you want to create stuff you  
**Translation:** 

**[17628.00s] English:** We want to launch stuff; this is the time to do it, and so, like, we've had this 1.8 gigawatt data center in.  
**Translation:** 

**[17632.60s] English:** Our data for over a year now, and we've been sort of sending it to all of our clients, including...  
**Translation:** Vocabulary: gigawatt: 吉瓦

**[17636.38s] English:** Many of these  
**Translation:** 

**[17636.90s] English:** Companies that are building the multi-gigawatt systems, but that is like  
**Translation:** 

**[17640.00s] English:** At a level that's not quite, maybe, executives like seeing $500 billion, $100 billion, and  
**Translation:** 

**[17644.64s] English:** Then, everyone's asking them, like, so it could spur an even faster arms race, right?  
**Translation:** Vocabulary: executives: 高层管理者

**[17650.04s] English:** Because there's already an arms race, but it's like a $100 billion to $500 billion dollar number.  
**Translation:** 

**[17654.12s] English:** Trump was talking about it on TV, like it could spur the arms race to be even faster and more advanced.  
**Translation:** 

**[17659.24s] English:** Investors will flood in, and so I think you're right in that sense.  
**Translation:** 

**[17664.10s] English:** That open-eye thing, or sort of like how Trump is championing that people are going to build more and his  
**Translation:** Vocabulary: championing: 提倡

**[17668.68s] English:** Actions are going to let people build more. What are you, uh, excited about?  
**Translation:** 

**[17672.80s] English:** About these several years that are upcoming, in terms of cluster buildouts,  
**Translation:** Vocabulary: buildouts: 建设; cluster: 集群; upcoming: 即将到来的

**[17681.16s] English:** Breakthroughs in AI, like the best possible future you can imagine, in the next couple of years.  
**Translation:** 

**[17686.90s] English:** Two, three, or four years—what does that look like? Just it could be very specific, technical things.  
**Translation:** Vocabulary: breakthroughs: 重大突破

**[17692.16s] English:** Like breakthroughs on post-training, or it could be just size big.  
**Translation:** 

**[17698.24s] English:** You.  
**Translation:** 

**[17698.68s] English:** Yeah, I mean, it's impressive how the clusters work. I really enjoy tracking supply chains and stuff.  
**Translation:** 

**[17704.42s] English:** Who is involved in what? Yeah, I really do. It's really fun to see the numbers and the costs.  
**Translation:** Vocabulary: clusters: 聚类

**[17708.46s] English:** Who's building what capacity, helping them figure out how much capacity they should build, and winning?  
**Translation:** 

**[17712.18s] English:** Deals with strategic stuff that's really cool, I think. Technologically, there's a lot around the  
**Translation:** Vocabulary: technologically: 技术上

**[17717.24s] English:** Networking, on the side that really excites me, involves optics and electro-electronics, right? Like, you know,  
**Translation:** 

**[17722.68s] English:** Of getting closer and closer, whether it be co-packaged optics or some sort of similar form.  
**Translation:** Vocabulary: excites: 激发兴趣; optics: 光学

**[17726.64s] English:** Of new forms of switching, this is.  
**Translation:** 

**[17728.68s] English:** Internal to a cluster, yeah, um, also multi-data center training, right? Like, there are people  
**Translation:** 

**[17734.64s] English:** Are they putting so much fiber between these data centers and lighting it up with so many different?  
**Translation:** 

**[17738.64s] English:** You know, with so much bandwidth, there's a lot of interesting stuff happening on that end.  
**Translation:** Vocabulary: bandwidth: 带宽; lighting: 点亮

**[17742.32s] English:** Right, Telecom has been really boring since 5G, and now it's like really exciting again. UM  
**Translation:** 

**[17747.10s] English:** Can you educate me a little bit about the speed of things, such as the speed of memory versus the speed of storage?  
**Translation:** 

**[17752.54s] English:** Of interconnect versus the speed of fiber between data centers, are these like orders of magnitude?  
**Translation:** 

**[17757.42s] English:** Is there a difference between the speed of memory versus the speed of data centers?  
**Translation:** Vocabulary: interconnect: 网络连接

**[17758.66s] English:** Can we at some point?  
**Translation:** 

**[17760.00s] English:** Point converges toward the place where it all just feels like one computer. Uh, no, I don't think.  
**Translation:** Vocabulary: converges: 汇聚

**[17764.92s] English:** That's possible, all right. Um, it's gonna get harder to program, not easier, okay? Um,  
**Translation:** 

**[17769.50s] English:** It's only going to get more difficult and complicated, and more layers, right? The general image...  
**Translation:** 

**[17774.20s] English:** That people like to have is a hierarchy of memory, so on-chip is really close and localized.  
**Translation:** 

**[17778.90s] English:** Within the chip, right? You know, there you have registers, right, and those are shared between  
**Translation:** Vocabulary: hierarchy: 层次; registers: 寄存器

**[17782.20s] English:** Some compute elements, and then you'll have caches which are shared between more compute elements.  
**Translation:** 

**[17785.90s] English:** Then, you have things like memory, such as HBM or DRAM, or DDR memory, and that's  
**Translation:** Vocabulary: caches: 缓存; compute: 计算

**[17790.64s] English:** Shared between the whole chip, and then you can have pools of memory that are shared.  
**Translation:** 

**[17795.18s] English:** Between many chips, right? Um, and then storage; it keeps you zoning out, right? The access latency,...  
**Translation:** Vocabulary: latency: 访问延迟

**[17800.50s] English:** Across data centers, across within the data center, within a chip, it's different. So, you're obviously  
**Translation:** 

**[17804.88s] English:** Always, you're always going to have different programming paradigms for this. It's not going to  
**Translation:** Vocabulary: paradigms: 范式

**[17810.36s] English:** Programming this stuff is going to be hard, but maybe I can help, right? Um, you know, with programming.  
**Translation:** 

**[17815.02s] English:** This, but the thing is...  
**Translation:** 

**[17815.90s] English:** The way to think about it is that, like, there is  
**Translation:** 

**[17820.30s] English:** There, there's sort of like the more elements you add to a task; you don't gain anything.  
**Translation:** 

**[17829.72s] English:** Strong scaling: right, if I double the number of chips, I don't get twice the exit performance, right?  
**Translation:** 

**[17832.98s] English:** Is just like a reality of computing, uh, because there are inefficiencies, um, and there's a lot of  
**Translation:** Vocabulary: computing: 计算; inefficiencies: 低效

**[17837.76s] English:** Interesting work is being done to make it more linear, whether it's making  
**Translation:** 

**[17842.64s] English:** The chips are more networked together more tightly, or, you know, cool.  
**Translation:** Vocabulary: linear: 成直线的; networked: 联网的

**[17845.88s] English:** Programming models or cool algorithmic things that you can do on the model side.  
**Translation:** 

**[17849.96s] English:** Right, deep-seek did some really cool innovations because they were limited on.  
**Translation:** Vocabulary: algorithmic: 算法相关的; innovations: 创新

**[17853.18s] English:** Interconnect, but they still needed to parallelize, right? Like, all sorts of people.  
**Translation:** 

**[17856.80s] English:** Always doing stuff, Google's got a bunch of work, and everyone's got a bunch of work about this.  
**Translation:** Vocabulary: interconnect: 互相连接

**[17859.70s] English:** Um, that stuff is super exciting on the model, workload, and innovation side—right? Hardware.  
**Translation:** 

**[17865.36s] English:** Solid-state transformers are interesting, right? For the power side, there's all sorts of stuff on.  
**Translation:** Vocabulary: workload: 工作负载

**[17869.90s] English:** Batteries, and there's all sorts of stuff. I think, I think when you look at it, if you look...  
**Translation:** 

**[17874.48s] English:** At every layer of the compute stack, you're going to see a lot of things that are going to be  
**Translation:** Vocabulary: compute: 计算

**[17875.88s] English:** Right, whether it goes from lithography and etch all the way to fabrication or even to optics.  
**Translation:** 

**[17880.00s] English:** To networking, to power, to transformers, to cooling, and you just go on up.  
**Translation:** Vocabulary: fabrication: 制造; lithography: 光刻; optics: 光学

**[17886.00s] English:** And up, up, and up the stack—you know, even air conditioners for data centers are like innovating.  
**Translation:** 

**[17889.58s] English:** Right, like it's like there's like copper cables are innovating, right, like you wouldn't think it.  
**Translation:** Vocabulary: cables: 电缆; copper: 铜质; innovating: 创新

**[17893.58s] English:** But copper cables, like, there are some innovations happening there with how you  
**Translation:** 

**[17897.84s] English:** Can pack them, and it's like all of these layers of the stack, all the way up to the models.  
**Translation:** 

**[17901.64s] English:** Human progress is at a pace that's never been seen before. I'm just imagining you sitting back.  
**Translation:** 

**[17906.22s] English:** In a layer, somewhere with screens everywhere, just monitoring the supply chain where all these  
**Translation:** 

**[17910.52s] English:** Clusters, like all the information you're gathering—I mean, you've got a big team there's a big team.  
**Translation:** 

**[17915.28s] English:** I mean, you're doing quite incredible work, uh, with semi-analysis. I mean, just  
**Translation:** Vocabulary: clusters: 聚类

**[17921.62s] English:** Keeping your finger on the pulse of human civilization in the digital world is pretty  
**Translation:** 

**[17929.40s] English:** Cool, like just to watch, feels good, yeah. Thank you. I guess. Uh, all of us feel like doing shit.  
**Translation:** 

**[17935.72s] English:** Okay.  
**Translation:** 

**[17936.22s] English:** Epic shit! Feel the AGI—feel the... I mean, from meme to like reality, um, what Nathan is there like?  
**Translation:** 

**[17943.64s] English:** Breakthroughs that you're looking forward to, potentially—I had some time to think about this.  
**Translation:** 

**[17948.34s] English:** While listening to Dellen's beautiful response, he didn't listen to me. I knew, no, I knew this was.  
**Translation:** Vocabulary: breakthroughs: 重大进展

**[17953.22s] English:** Coming along, it's like realistically training models is very fun because there's so much low-hanging fruit.  
**Translation:** 

**[17958.78s] English:** Fruit, and the thing that makes my job entertaining: I train models and write analysis about what's  
**Translation:** Vocabulary: entertaining: 令人愉快的

**[17965.04s] English:** Happening with models.  
**Translation:** 

**[17965.72s] English:** And it's fun because there is obviously so much more progress to be had, and the real motivation.  
**Translation:** 

**[17972.22s] English:** Why I do this somewhere where I can share things is that there's just no trusting people that.  
**Translation:** 

**[17977.56s] English:** Are like, trust me, bro. We're gonna make AI good. It's like, we're the ones.  
**Translation:** 

**[17981.30s] English:** Gonna do it, and you can trust us. We're just gonna have all the AI, and it's just like I'd  
**Translation:** 

**[17985.96s] English:** Like a future where more people have a say in what AI is and can understand it, and that's it.  
**Translation:** 

**[17993.02s] English:** A little bit less fun; that's not a very positive thing. I feel like this is just a bit more fun, and  
**Translation:** 

**[17995.72s] English:** All really fun, like training models is fun, and bringing people in is fun, but it's really  
**Translation:** 

**[18000.00s] English:** AI, if it is going to be the most powerful technology of my lifetime, it's like we need to have a lot of people involved in making that. Making it open helps with that, as accessible and as open as possible.  
**Translation:** 

**[18013.94s] English:** Yeah.  
**Translation:** 

**[18014.28s] English:** In my read of the last few years, it is that more openness would help the AI ecosystem in terms of having more people understand what's going on, rather than researchers from non-AI fields, governments, and everything else.  
**Translation:** 

**[18025.32s] English:** It doesn't mean that openness will always be the answer.  
**Translation:** 

**[18027.72s] English:** I think then I will reassess and determine what the biggest problem facing AI is, and approach it from a different angle in this wild ride we're on.  
**Translation:** 

**[18036.28s] English:** And for me, just from an even better user experience, anytime you have those "aha" moments—like Apathy said—the magic, like seeing the reasoning and the chain of thought.  
**Translation:** Vocabulary: anytime: 任何时候; apathy: 冷漠; reassess: 重新评估

**[18050.24s] English:** It's like there's something really fundamentally beautiful about that.  
**Translation:** 

**[18054.30s] English:** It's putting a mirror to ourselves and seeing, oh, shit.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[18057.72s] English:** It is solving intelligence, as the cliché goes, like the goal of these companies is, and you get to understand why we humans are special.  
**Translation:** 

**[18066.82s] English:** The intelligence within us is special.  
**Translation:** 

**[18069.18s] English:** And for now, that's also why we are special in terms of we seem to be conscious, while the AI systems aren't.  
**Translation:** 

**[18076.44s] English:** And we get to solve that mystery, we get to explore it.  
**Translation:** 

**[18079.88s] English:** So that's just really cool to get to explore these questions that I don't think I would have ever imagined.  
**Translation:** 

**[18087.72s] English:** It would have been even possible back then, so just watching with excitement, deep blue and big Kasparov—like I wouldn't have ever thought this kind of AI would be possible in my lifetime.  
**Translation:** Vocabulary: kasparov: 卡斯帕罗夫

**[18101.20s] English:** It's like, this really feels like AI.  
**Translation:** 

**[18103.40s] English:** It's incredible.  
**Translation:** 

**[18104.36s] English:** I started with AI to learn how to fly a silly quadrotor.  
**Translation:** 

**[18108.60s] English:** It's like learning to fly.  
**Translation:** Vocabulary: quadrotor: 四旋翼无人机

**[18109.60s] English:** And it just learned to fly up.  
**Translation:** 

**[18111.82s] English:** It would hit the ceiling, stop, and catch it.  
**Translation:** Vocabulary: ceiling: 天花板

**[18113.62s] English:** It's like, okay, that is really stupid compared to what's going on now.  
**Translation:** 

**[18117.18s] English:** And now, you could.  
**Translation:** 

**[18117.72s] English:** Probably with natural language processing.  
**Translation:** 

**[18120.00s] English:** It will learn to fly, and it is going to generate the control algorithm required to do that, probably.  
**Translation:** Vocabulary: algorithm: 控制算法

**[18124.96s] English:** There are low-level blockers, like we had to do some weird stuff for that, but you can still proceed.  
**Translation:** 

**[18129.20s] English:** Definitely back to our robotics conversation. Yeah, when you have to interact with an actual physical world.  
**Translation:** Vocabulary: robotics: 机器人技术

**[18133.28s] English:** That's hard. What gives you hope about the future of human civilization, looking into the next?  
**Translation:** 

**[18140.56s] English:** 10 years, 100 years, or a thousand years—how long do you think we'll make it?  
**Translation:** 

**[18144.32s] English:** Do you think we'll have humans around in a thousand years?  
**Translation:** 

**[18150.48s] English:** I think there are ways that very bad things could happen; there will be way fewer humans.  
**Translation:** 

**[18155.20s] English:** Humans are very good at surviving; there's been a lot of things that are true. I don't think...  
**Translation:** 

**[18161.24s] English:** They're not necessarily good at long-term credit assignment of risk, but when the risk becomes  
**Translation:** 

**[18166.56s] English:** Immediate, we tend to figure things out, and oh, yeah, for that reason, I'm like, there's physical.  
**Translation:** 

**[18172.54s] English:** Constraints to things like:  
**Translation:** Vocabulary: constraints: 限制

**[18174.32s] English:** AGI hyper-like recursive improvement to kill us all—type stuff; I’m for the physical reasons, and  
**Translation:** 

**[18181.22s] English:** For how humans have figured things out before, I'm not too worried about an AI takeover. There are  
**Translation:** Vocabulary: recursive: 递归; takeover: 接管

**[18185.88s] English:** Other international things that are worrying, but there's just fundamental human goodness and trying...  
**Translation:** 

**[18192.98s] English:** To amplify that, and like we're on a tenuous time, and I mean, if you look at humanity as a whole,...  
**Translation:** Vocabulary: amplify: 放大; tenuous: 脆弱; worrying: 令人担忧的

**[18200.40s] English:** There have been times where things go backwards, and there are times when things don't have to be.  
**Translation:** 

**[18204.30s] English:** At all, and we're on what should be a very positive trajectory right now. Yeah, there seems to be  
**Translation:** Vocabulary: backwards: 倒退; trajectory: 趋势

**[18209.60s] English:** Progress, but just like with power, there are like spikes of human suffering, and we want to try.  
**Translation:** 

**[18216.40s] English:** To minimize the amount of spikes, generally humanity is going to suffer a lot less, right? I'm very  
**Translation:** Vocabulary: spikes: 剧烈波动

**[18221.94s] English:** Optimistic about that, but I do worry about something like techno-fascism-type stuff arising as AI becomes more prevalent.  
**Translation:** 

**[18229.94s] English:** And more prevalent and powerful, and those who control it can do more and more. Maybe it's  
**Translation:** Vocabulary: optimistic: 乐观; prevalent: 普遍

**[18234.30s] English:** Maybe it doesn't kill us all, uh, but at some point, every very powerful human is going to want to.  
**Translation:** 

**[18239.64s] English:** Brain  
**Translation:** 

**[18240.00s] English:** Computer interface so that they can interact with the AGI and all of its advantages in many more ways.  
**Translation:** 

**[18244.68s] English:** Way and merge its mind with, you know, sort of like, and its capabilities—or that person's.  
**Translation:** Vocabulary: capabilities: 能力; interface: 接口

**[18248.80s] English:** Capabilities, uh, can leverage those much better than anyone else. And therefore be, you know,  
**Translation:** 

**[18253.28s] English:** It won't be one person ruling them all, but it will be — you know — the thing I worry about is it'll  
**Translation:** Vocabulary: leverage: 利用

**[18257.40s] English:** Be like few people, you know, in the thousands, tens of thousands, maybe millions of.  
**Translation:** 

**[18261.90s] English:** People rule whoever's left. Right. And the economy around it. Right. And I think it'll,  
**Translation:** 

**[18267.94s] English:** That's like the thing that's probably more worrying is human-machine amalgamations.  
**Translation:** 

**[18273.78s] English:** This enables an individual human to have more impact on the world. And that impact can be both positive and negative.  
**Translation:** Vocabulary: amalgamations: 人机结合; worrying: 令人担忧的

**[18278.20s] English:** Positive and negative, right? Uh, generally, humans have positive impacts on the world.  
**Translation:** 

**[18282.54s] English:** At least, societally, but it's possible for individual humans to have such negative impacts.  
**Translation:** Vocabulary: societally: 社会上

**[18287.30s] English:** And AGI, at least as I think the labs define it, which is not a runaway sentient thing,  
**Translation:** 

**[18293.36s] English:** But rather, just something that can do a lot of tasks really efficiently. Um,  
**Translation:** Vocabulary: efficiently: 高效地; runaway: 失控的; sentient: 有感知的

**[18297.94s] English:** Amplifies the capabilities of someone, causing extreme damage. But, for the most part,  
**Translation:** 

**[18303.12s] English:** I think it'll be used for, you know, profit-seeking motives, which will then reduce,  
**Translation:** Vocabulary: amplifies: 增强

**[18307.24s] English:** Which will increase the abundance and supply of things, and therefore reduce suffering. Right.  
**Translation:** 

**[18311.50s] English:** Yeah. That's the goal: scrolling on a timeline, just drawing a stasis.  
**Translation:** Vocabulary: scrolling: 滚动; stasis: 静止

**[18318.28s] English:** Scrolling holds the status quo of the world. That is a positive outcome, right? Like, it's like,  
**Translation:** 

**[18322.78s] English:** If I have food tubes and I'm scrolling, and I'm happy, that's a positive outcome.  
**Translation:** 

**[18327.94s] English:** Yeah. While expanding out into the cosmos; it's a fun time to be alive.  
**Translation:** 

**[18334.68s] English:** And thank you for pushing the forefront of what is possible in humans, and thank you for talking.  
**Translation:** Vocabulary: cosmos: 宇宙; forefront: 前沿

**[18340.50s] English:** Today, this was fun. Thanks for having us. Thanks for having us. Thanks for listening.  
**Translation:** 

**[18344.60s] English:** To this conversation with Dylan Patel and Nathan Lambert. To support this podcast,  
**Translation:** 

**[18349.36s] English:** Please check out our sponsors in the description. And now, let me leave you some words from Richard.  
**Translation:** 

**[18355.76s] English:** Feynman.  
**Translation:** Vocabulary: sponsors: 赞助商

**[18357.94s] English:** Successful Technology: Reality.  
**Translation:** 

**[18360.00s] English:** Must take precedence over public relations, for nature cannot be fooled.  
**Translation:** 

**[18366.14s] English:** Thank you for listening, and I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
