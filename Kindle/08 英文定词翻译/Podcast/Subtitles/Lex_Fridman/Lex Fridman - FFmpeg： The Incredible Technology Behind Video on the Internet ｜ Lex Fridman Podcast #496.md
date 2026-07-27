# Podcast vocabulary notes
Source file: Lex Fridman - FFmpeg： The Incredible Technology Behind Video on the Internet ｜ Lex Fridman Podcast #496.opus

**[0.00s] English:** The important is, is your code good?  
**Translation:** 

**[2.64s] English:** We care about excellent code.  
**Translation:** 

**[4.68s] English:** We don't care who you are.  
**Translation:** 

**[6.04s] English:** Like maybe you're a dog.  
**Translation:** 

**[7.24s] English:** I don't care, right?  
**Translation:** 

**[8.44s] English:** I don't care where you come from.  
**Translation:** 

**[9.92s] English:** I need to look at your code.  
**Translation:** 

**[11.72s] English:** Oh yeah, but I'm engineer at this very large company  
**Translation:** 

**[14.20s] English:** in Italy, in Germany, in the US.  
**Translation:** 

**[16.88s] English:** We don't care.  
**Translation:** 

**[18.48s] English:** We care about the quality of your code  
**Translation:** 

**[20.44s] English:** because this is what defines our community.  
**Translation:** 

**[23.54s] English:** And which means that we have a lot of people  
**Translation:** 

**[25.24s] English:** who contribute who are some very different backgrounds  
**Translation:** 

**[27.70s] English:** and very introverts, sure.  
**Translation:** 

**[30.42s] English:** But that's okay, right?  
**Translation:** Vocabulary: introverts: 内向的人

**[31.72s] English:** FFmpeg is probably one of the biggest CPU users in the world.  
**Translation:** 

**[35.00s] English:** Everything we've just said in the past couple of minutes,  
**Translation:** 

**[38.12s] English:** every sentence is someone's lifetime's work.  
**Translation:** 

**[40.20s] English:** There are books about every sentence.  
**Translation:** 

**[41.84s] English:** So the level of complexity in many cases is inordinate.  
**Translation:** 

**[45.78s] English:** FFmpeg has 100,000 lines of assembly for all the codecs.  
**Translation:** Vocabulary: complexity: 复杂性; inordinate: 过度的

**[50.64s] English:** And just this one has 240,000.  
**Translation:** 

**[53.36s] English:** Every cycle matters.  
**Translation:** 

**[55.82s] English:** We are talking about probably  
**Translation:** 

**[57.08s] English:** three, four, five, six, seven, eight, nine, ten, ten.  
**Translation:** 

**[57.68s] English:** Three billion devices which are going to decode video nonstop  
**Translation:** 

**[61.78s] English:** because, for example, 30% of the video from Netflix  
**Translation:** 

**[64.48s] English:** are now in everyone, 50% of YouTube.  
**Translation:** 

**[67.94s] English:** This is what peak video codecs should look like.  
**Translation:** 

**[71.32s] English:** 79.9% assembly, 90.6% C, and 0.5% other.  
**Translation:** 

**[78.82s] English:** And what's incredible is with those tweets,  
**Translation:** Vocabulary: tweets: 微博

**[81.24s] English:** which is factual, people get crazy.  
**Translation:** 

**[85.56s] English:** For the last two years, they go crazy.  
**Translation:** 

**[86.74s] English:** No.  
**Translation:** 

**[86.98s] English:** Intrinsics is fine.  
**Translation:** Vocabulary: intrinsics: 内在特性

**[88.02s] English:** The compiler.  
**Translation:** 

**[88.64s] English:** You can optimize your compiler.  
**Translation:** Vocabulary: optimize: 优化

**[90.34s] English:** Auto vectorization is your fault.  
**Translation:** 

**[92.38s] English:** You don't understand.  
**Translation:** Vocabulary: vectorization: 向量优化

**[93.34s] English:** And we've tried that forever, right?  
**Translation:** 

**[95.50s] English:** For two years and two years later,  
**Translation:** 

**[97.10s] English:** showing hundreds of examples of handwritten assembly.  
**Translation:** 

**[101.30s] English:** No, no, no.  
**Translation:** 

**[101.84s] English:** You're doing it wrong.  
**Translation:** 

**[102.54s] English:** The compiler can do this.  
**Translation:** 

**[103.68s] English:** The intelligence agencies tried to like,  
**Translation:** 

**[106.42s] English:** say, can you put a backdoor in VLC?  
**Translation:** Vocabulary: backdoor: 后门

**[108.52s] English:** Yes.  
**Translation:** 

**[109.06s] English:** Two of them.  
**Translation:** 

**[110.12s] English:** What do you say?  
**Translation:** 

**[111.50s] English:** No.  
**Translation:** 

**[112.24s] English:** I was a lot less polite.  
**Translation:** 

**[114.62s] English:** Basically saying, hell no.  
**Translation:** 

**[115.98s] English:** No.  
**Translation:** 

**[116.04s] English:** Like, if we had to compromise our software,  
**Translation:** 

**[118.46s] English:** we would shut it down.  
**Translation:** 

**[119.50s] English:** This is clear.  
**Translation:** 

**[120.00s] English:** Any tweets carrying your regret?  
**Translation:** 

**[123.92s] English:** Any tweets I regret?  
**Translation:** 

**[125.54s] English:** Or is it like that?  
**Translation:** 

**[126.46s] English:** How does the French song go?  
**Translation:** 

**[128.10s] English:** Regret nothing?  
**Translation:** 

**[128.88s] English:** Don't regret anything.  
**Translation:** 

**[131.06s] English:** No, it's because regrets are a tax on your mind.  
**Translation:** 

**[136.50s] English:** The following is a conversation all about FFmpeg and VLC  
**Translation:** 

**[140.72s] English:** with Jean-Baptiste Kempf and Karen Cunha.  
**Translation:** 

**[145.74s] English:** FFmpeg is an open source software system  
**Translation:** 

**[148.46s] English:** that is the invisible backbone behind YouTube,  
**Translation:** 

**[152.52s] English:** Netflix, Chrome, VLC, Discord,  
**Translation:** Vocabulary: backbone: 支撑体系

**[154.54s] English:** and basically every platform that touches video or audio on the Internet.  
**Translation:** 

**[161.34s] English:** It can decode, encode, transcode, stream, and play  
**Translation:** Vocabulary: encode: 编码; transcode: 转码

**[165.78s] English:** almost any video or audio format ever created.  
**Translation:** 

**[170.36s] English:** To me, it is one of the most incredible software systems ever developed.  
**Translation:** 

**[175.12s] English:** And it's all done by volunteers.  
**Translation:** 

**[179.18s] English:** VLC is also a legendary piece of software.  
**Translation:** 

**[182.84s] English:** It is an open source media player  
**Translation:** 

**[184.40s] English:** that plays basically anything you throw at it.  
**Translation:** 

**[187.74s] English:** Any format, any platform, no ads, no tracking.  
**Translation:** 

**[191.44s] English:** It has been downloaded over 6 billion times.  
**Translation:** 

**[194.90s] English:** And again, for me, it has been one of my favorite pieces of software ever.  
**Translation:** 

**[200.18s] English:** With the most legendary logo,  
**Translation:** 

**[201.94s] English:** which I, of course, had to honor in this conversation  
**Translation:** 

**[204.50s] English:** by wearing the VLC trademark.  
**Translation:** Vocabulary: trademark: 注册商标

**[208.46s] English:** The traffic cone hat the whole time.  
**Translation:** 

**[211.58s] English:** So again, above all else,  
**Translation:** 

**[213.64s] English:** thank you to the incredible volunteer engineers  
**Translation:** 

**[215.70s] English:** who put their heart and soul into this code  
**Translation:** 

**[218.16s] English:** that has been used and loved by billions of people.  
**Translation:** 

**[222.26s] English:** Thank you.  
**Translation:** 

**[223.72s] English:** And about the two great engineers and human beings  
**Translation:** 

**[226.88s] English:** I'm talking to in this episode,  
**Translation:** 

**[229.98s] English:** Jean-Baptiste is the president of VideoLan  
**Translation:** 

**[233.14s] English:** and is a key figure behind VLC and FFmpeg.  
**Translation:** 

**[238.08s] English:** Karen,  
**Translation:** 

**[238.46s] English:** is a long-time coach  
**Translation:** 

**[240.00s] English:** engineer, FFmpeg contributor, and the man behind the now infamous FFmpeg account on Twitter,  
**Translation:** 

**[247.42s] English:** X, that I recommend everybody follow for the memes and for the unapologetic celebration of  
**Translation:** Vocabulary: contributor: 贡献者; infamous: 臭名昭著的; unapologetic: 毫不道歉的

**[254.82s] English:** open source and great low-level software engineering. Let me also say that it's inspiring  
**Translation:** 

**[262.06s] English:** and humbling that so much of modern civilization rests on software built by people who are not  
**Translation:** Vocabulary: humbling: 令人谦卑

**[268.82s] English:** chasing fame or money, but are obsessed with the craft of engineering. We live in a world where  
**Translation:** 

**[275.86s] English:** billions of people consume video every day without ever thinking about the invisible machinery  
**Translation:** Vocabulary: machinery: 机械设备

**[280.50s] English:** underneath it. But that machinery matters. Open source infrastructure matters. It is one of the  
**Translation:** 

**[287.44s] English:** great examples of human beings quietly collaborating across borders to build something useful, durable,  
**Translation:** Vocabulary: collaborating: 合作; durable: 耐用

**[293.56s] English:** and elegant for the rest of us.  
**Translation:** 

**[297.54s] English:** And so, this conversation...  
**Translation:** 

**[298.82s] English:** is not just about codecs and media pipelines. It is also about the deeper spirit of engineering  
**Translation:** 

**[306.14s] English:** and generosity that makes projects like FFmpeg possible. Again, I can never say it enough.  
**Translation:** Vocabulary: generosity: 慷慨; pipelines: 管道

**[314.60s] English:** Thank you.  
**Translation:** 

**[316.70s] English:** This is the Lex Friedman Podcast. To support it, please check out our sponsors in the description  
**Translation:** Vocabulary: friedman: 弗里德曼; sponsors: 赞助商

**[321.76s] English:** where you can also find links to contact me, ask questions, give feedback, and so on. And  
**Translation:** 

**[327.54s] English:** I'll see you next time.  
**Translation:** 

**[328.82s] English:** Now, dear friends, here's Jean-Baptiste Kempf and Kieran Cunha.  
**Translation:** 

**[335.58s] English:** So, the legend goes, VLC can open everything. What's the weirdest thing that you know that it can  
**Translation:** Vocabulary: weirdest: 最奇怪的东西

**[341.66s] English:** open?  
**Translation:** 

**[342.74s] English:** You know, there is a ton of people who are using VLC to record VHS videos, right? Like,  
**Translation:** 

**[347.98s] English:** it's just like you plug it with a capture card and you can basically record VHS video.  
**Translation:** 

**[352.26s] English:** Well, how does that work?  
**Translation:** 

**[353.40s] English:** Basically, it's, you know, those type of capture cards where you can put a peritel in,  
**Translation:** 

**[357.58s] English:** or RGN.  
**Translation:** 

**[358.82s] English:** And you put that.  
**Translation:** 

**[360.00s] English:** And actually, VLC can play those type of cards.  
**Translation:** 

**[362.18s] English:** And there is a module which allows to control directly those VCR camcorders.  
**Translation:** 

**[367.82s] English:** We support DVD audios lately, right?  
**Translation:** Vocabulary: camcorders: 录像机; module: 模块

**[369.66s] English:** We spent the summer working on DVD audio support.  
**Translation:** 

**[373.48s] English:** And, like, there is no one making any DVD audio support.  
**Translation:** 

**[377.12s] English:** There is a custom encryption schemes.  
**Translation:** 

**[378.98s] English:** What about Lucasfilm?  
**Translation:** Vocabulary: encryption: 加密

**[380.06s] English:** Oh, yeah.  
**Translation:** 

**[380.40s] English:** And there is, of course, all the weird codecs, game codecs supported by FFmpeg.  
**Translation:** 

**[385.36s] English:** The one Star Wars video game, the first 10-second opening sequence,  
**Translation:** 

**[388.48s] English:** someone has gone and implemented that and made sure that's a bit exact  
**Translation:** 

**[391.40s] English:** on one disc that existed at one time of one little sequence in the game.  
**Translation:** 

**[396.40s] English:** And then, funnily, at one Videoland conference,  
**Translation:** Vocabulary: videoland: 视频乐园

**[400.02s] English:** we made a competition to make the weirdest and most horrible file ever  
**Translation:** 

**[403.82s] English:** and see if VLC could play it.  
**Translation:** 

**[406.20s] English:** What did it end up being?  
**Translation:** 

**[407.26s] English:** What's the file?  
**Translation:** 

**[408.02s] English:** It was an MKV file made by Derek,  
**Translation:** 

**[412.14s] English:** which each of the frames was changing resolution, aspect ratio, rotation,  
**Translation:** Vocabulary: derek: 制作人

**[417.58s] English:** and everything.  
**Translation:** 

**[418.60s] English:** It was, like, did it work?  
**Translation:** 

**[420.12s] English:** Yes.  
**Translation:** 

**[421.12s] English:** And there was another one where the whole video was actually animated subtitles,  
**Translation:** 

**[426.80s] English:** right, SSA, right?  
**Translation:** 

**[428.12s] English:** Yeah, I remember that, yeah.  
**Translation:** 

**[429.44s] English:** So each frame was a black frame, but on top of that,  
**Translation:** 

**[433.64s] English:** there was a subtitle that was animated for each frame.  
**Translation:** Vocabulary: subtitle: 字幕

**[436.68s] English:** There was a file that's a valid zip and a valid MP3 at the same time  
**Translation:** 

**[439.52s] English:** or something like that.  
**Translation:** 

**[440.56s] English:** So, yeah, we'd made a competition of stupid files.  
**Translation:** 

**[443.70s] English:** And it worked.  
**Translation:** 

**[444.84s] English:** It opened all of the stupid files.  
**Translation:** 

**[447.00s] English:** Yes.  
**Translation:** 

**[447.16s] English:** By the way.  
**Translation:** 

**[448.48s] English:** For people who are not familiar, I am wearing a hat.  
**Translation:** 

**[451.72s] English:** Would it be fair to say this is the best, worst logo of all time, the cone?  
**Translation:** 

**[456.72s] English:** Yeah, by far, right?  
**Translation:** 

**[457.92s] English:** The logo of VLC is so iconic, right?  
**Translation:** 

**[460.52s] English:** Like, we are a team with a small number of people, and the icon is known everywhere.  
**Translation:** 

**[465.64s] English:** I go to middle of nowhere in India or in China, people know the cone, right?  
**Translation:** 

**[469.64s] English:** And 25% of the website traffic that comes to our main website is cone player, right?  
**Translation:** 

**[476.64s] English:** So, so many people don't know VLC, right?  
**Translation:** 

**[478.40s] English:** They know the cone player.  
**Translation:** 

**[479.50s] English:** That's the thing.  
**Translation:** 

**[480.00s] English:** Google Force, Cone Player.  
**Translation:** 

**[481.70s] English:** Yeah, they go on Google and they put Cone Player and they download VLC, right?  
**Translation:** 

**[485.38s] English:** So that's iconic.  
**Translation:** 

**[486.70s] English:** And once we tried to change it as a joke, right?  
**Translation:** 

**[489.02s] English:** We said it was going to be a type of caterpillar construction.  
**Translation:** Vocabulary: caterpillar: 蚯蚓式坦克

**[495.32s] English:** And we said that during April 1st.  
**Translation:** 

**[497.48s] English:** And we had around 10,000 emails saying, no, don't change the logo and so on, right?  
**Translation:** 

**[501.80s] English:** So it's so iconic, right?  
**Translation:** 

**[503.94s] English:** It's so distinctive, right?  
**Translation:** 

**[504.98s] English:** If you want to do a video player, you're going to put a play button on the TV, right?  
**Translation:** 

**[508.60s] English:** And that's YouTube.  
**Translation:** 

**[509.30s] English:** YouTube logo, right?  
**Translation:** 

**[510.64s] English:** It's an original.  
**Translation:** 

**[512.18s] English:** This one is orange, right?  
**Translation:** 

**[513.74s] English:** It's very bright.  
**Translation:** 

**[515.02s] English:** And it's weird.  
**Translation:** 

**[517.18s] English:** And it's ridiculous.  
**Translation:** 

**[517.96s] English:** And it's absurd.  
**Translation:** 

**[518.72s] English:** And it's hilarious.  
**Translation:** 

**[519.46s] English:** It becomes meme and meme becomes culture.  
**Translation:** 

**[521.66s] English:** And you keep it.  
**Translation:** 

**[522.50s] English:** And you know about it.  
**Translation:** 

**[523.46s] English:** And you know that in 20 years, like you still have going to have the cones and remember,  
**Translation:** 

**[528.16s] English:** oh, yeah, that was a video player.  
**Translation:** 

**[529.42s] English:** Yeah.  
**Translation:** 

**[529.74s] English:** And we'll talk about, you know, the mission of FFmpeg being a kind of the archival aspect of it.  
**Translation:** 

**[536.10s] English:** So you can think about a thousand years from now, we'll have all these videos.  
**Translation:** Vocabulary: archival: 档案保存

**[539.12s] English:** They've...  
**Translation:** 

**[539.28s] English:** Only VLC can open.  
**Translation:** 

**[541.02s] English:** Human civilization has already destroyed itself multiple times.  
**Translation:** 

**[545.30s] English:** And the only thing that will remain is this, like, you know, the cockroaches will be crawling around.  
**Translation:** Vocabulary: cockroaches: 蟑螂; crawling: 爬行

**[550.00s] English:** It'll be the VLC logo with some of the archival footage that VLC can open.  
**Translation:** 

**[554.96s] English:** And the aliens will show up and they'll press play and they'll get to see all this.  
**Translation:** 

**[558.50s] English:** Well, we really hope so, right?  
**Translation:** 

**[559.46s] English:** But there is also so many memes where people say, well, I'm sure I can put a pancake inside my DVD drive and VLC will play it.  
**Translation:** 

**[565.42s] English:** Can they?  
**Translation:** 

**[566.20s] English:** No, we tried.  
**Translation:** 

**[566.78s] English:** It doesn't.  
**Translation:** 

**[568.08s] English:** But we actually have a video.  
**Translation:** 

**[569.28s] English:** If us trying that didn't work.  
**Translation:** 

**[571.46s] English:** A codec for physical reality.  
**Translation:** 

**[573.02s] English:** I don't know what that would even look like.  
**Translation:** 

**[574.04s] English:** There was a guy who did that, right?  
**Translation:** 

**[575.38s] English:** He printed a small cone, right?  
**Translation:** 

**[577.92s] English:** Like the ones we distribute as goodies.  
**Translation:** Vocabulary: goodies: 小礼物

**[580.28s] English:** And inside he puts an RFID chip, which was his way of playing a movie, right?  
**Translation:** 

**[586.52s] English:** And so he puts this on the RFID player.  
**Translation:** 

**[589.06s] English:** And when he put that, it was playing like the last Star Wars and so on.  
**Translation:** 

**[592.04s] English:** So instead of having like DVD boxes, he had like VLC cones all around and he plugged that.  
**Translation:** 

**[597.42s] English:** And that was like physical objects.  
**Translation:** 

**[599.28s] English:** So.  
**Translation:** 

**[600.00s] English:** the thing that we're talking about is everything around video codecs video encoding video decoding  
**Translation:** 

**[605.70s] English:** video streaming video player client that i'm wearing on my head the entire ecosystem enabling  
**Translation:** 

**[611.72s] English:** free media we'll talk about ffmpeg we'll talk about video land vlc and all the other incredible  
**Translation:** 

**[618.26s] English:** video technology uh that is used probably by billions of people so jb you're the lead developer  
**Translation:** 

**[626.96s] English:** behind the legendary vlc player kieran amongst many other things your lead developer behind the  
**Translation:** 

**[633.00s] English:** legendary ffmpeg handle on twitter and both of you have spicy opinions i would say so today i want to  
**Translation:** Vocabulary: kieran: 凯利安

**[641.24s] English:** talk about ffmpeg and vlc uh for context for people who are not aware and i'm sure basically  
**Translation:** 

**[649.74s] English:** everybody listening to this have used these two technologies probably regularly without  
**Translation:** 

**[656.80s] English:** nothing  
**Translation:** 

**[656.96s] English:** knowing it so ffmpeg underlies basically most video on the internet including youtube netflix  
**Translation:** 

**[663.12s] English:** chrome firefox of course vlc and countless other video platforms it is estimated that over 90 percent  
**Translation:** 

**[670.66s] English:** of video processing workflows online and offline involve ffmpeg vlc has been downloaded at least  
**Translation:** Vocabulary: workflows: 工作流程

**[677.82s] English:** 6.5 billion times but likely that number because it's impossible to really count the number  
**Translation:** 

**[685.58s] English:** uh is much higher than the number of videos that are being downloaded on ffmpeg  
**Translation:** 

**[686.96s] English:** it's much higher than that virtually any operating system supports virtually any media format  
**Translation:** 

**[693.92s] English:** the limitation being it can't open pancakes so uh can we just lay out some of the basics  
**Translation:** Vocabulary: pancakes: 煎饼

**[701.80s] English:** so to help people understand what's involved in all of this so when we press play on a video  
**Translation:** 

**[709.06s] English:** player like vlc what happens what how does it go from the the file or the stream to the pixels on  
**Translation:** Vocabulary: pixels: 像素

**[716.58s] English:** the screen and what happens when you press play on a video player like vlc what happens when you  
**Translation:** 

**[716.96s] English:** press play on one file when you press play on a video player like vlc what happens when you  
**Translation:** 

**[717.74s] English:** press play on one file when you press play on one file into an audio és the higher the plastic  
**Translation:** 

**[719.60s] English:** happens when you press play on a video player like vlc what happens when you press play on a video  
**Translation:** 

**[721.56s] English:** player like vlc there's an area provided at the bottom of the video player that provides you  
**Translation:** 

**[722.72s] English:** a very wide the position of the правильно speaking the filter for the sound from the  
**Translation:** 

**[723.62s] English:** audio loader working what are the big stages  
**Translation:** 

**[724.22s] English:** audience  
**Translation:** 

**[735.06s] English:** I want you to understand that at some point you'll get a screen infected with micro-computer  
**Translation:** 

**[736.20s] English:** devices that have happened to the touch screen which is leading you off all of your  
**Translation:** 

**[738.74s] English:** live video player apnesis one added something called v ELM  
**Translation:** 

**[740.66s] English:** on it unfortunately absolutely no sound in the camera  
**Translation:** 

**[742.32s] English:** side and it can't be structured  
**Translation:** 

**[744.46s] English:** they're you can't be set in its subsidiary  
**Translation:** Vocabulary: subsidiary: 子公司

**[720.00s] English:** to be aware of? So there are several stages, right? The first stage is to get from an address,  
**Translation:** 

**[726.12s] English:** right, which is the type of URL to give you a byte of streams, right? So this would be,  
**Translation:** 

**[732.28s] English:** for example, HTTP, file, DVD, right? You give the pass to the media and give you a stream of data.  
**Translation:** 

**[739.40s] English:** The stream needs to be cut up by what's known as the container, the demultiplexer or demux.  
**Translation:** Vocabulary: demultiplexer: 解复用器

**[744.44s] English:** We'll try and keep the jargon light throughout this, but it needs to go and start demarcating  
**Translation:** 

**[749.10s] English:** video and audio frames. So it just gets data from the operating system blocks at a time and  
**Translation:** Vocabulary: demarcating: 划分边界; jargon: 行话

**[753.04s] English:** needs to start cutting these frames up into compressed data. It then needs to start doing  
**Translation:** 

**[758.56s] English:** simple parsing of the video frames, mainly to figure out whether that codec is GPU decodable  
**Translation:** Vocabulary: compressed: 压缩; decodable: 可解码; parsing: 解析

**[764.98s] English:** or needs to fall back to software. We're very sort of used to assuming the GPU will play all  
**Translation:** 

**[771.10s] English:** of these things. There'll be hardware acceleration. I think it's up to 45% of files are not GPU  
**Translation:** Vocabulary: acceleration: 硬件加速

**[775.82s] English:** decodable. So these need to be probed. They need to be detected.  
**Translation:** 

**[779.10s] English:** There can be variants of a given codec, some of which are decodable on the GPU.  
**Translation:** Vocabulary: detected: 被发现

**[784.10s] English:** Different vendors of GPU might have different capabilities. So those need to be detected.  
**Translation:** 

**[788.94s] English:** So if it's GPU capable, you pass it through to the GPU black box.  
**Translation:** 

**[793.08s] English:** So now if there's a software fallback, that means in the beginning is to first do  
**Translation:** 

**[798.28s] English:** de-entropy coding. So removing the mathematical coding of the bitstream. So this uses  
**Translation:** Vocabulary: bitstream: 比特流; fallback: 后备方案; mathematical: 数学的

**[802.80s] English:** capabilities such as Hoffman coding or arithmetic coding to actually decompress the mathematical  
**Translation:** 

**[809.10s] English:** layer of the bitstream. We then need to start reading the syntax elements for intra-prediction.  
**Translation:** Vocabulary: arithmetic: 算术编码

**[814.24s] English:** So intra-prediction are like still images of the video, so your iframes. So this works  
**Translation:** 

**[820.60s] English:** and operates in the spatial domain. So you do your intra-prediction in the spatial domain,  
**Translation:** Vocabulary: spatial: 空间的

**[824.98s] English:** you have a residual because your prediction isn't quite matching that of reality. So you've  
**Translation:** 

**[829.10s] English:** made a prediction, but then there's a little bit left, and that's what's known as the residual.  
**Translation:** Vocabulary: residual: 剩余误差

**[833.88s] English:** This is stored in the frequency domain, and these are quantized to decompound their space.  
**Translation:** 

**[839.10s] English:** We then need to do  
**Translation:** Vocabulary: decompound: 分解; quantized: 量化

**[840.00s] English:** the inverse transform to bring them back to the spatial domain and apply these residuals so a lot  
**Translation:** 

**[846.42s] English:** of the process of the decoding is this thing is compressed yes yes and you have to predict the  
**Translation:** Vocabulary: inverse: 逆变换; residuals: 残差

**[852.26s] English:** highest quality thing that's supposed to go there iframe is the best representation you have spatially  
**Translation:** 

**[858.50s] English:** yes and then you and then there's a lot of temporal compression that can happen depending  
**Translation:** Vocabulary: compression: 压缩; spatially: 空间上; temporal: 时间上

**[863.26s] English:** on the codec and then you're predicting you're predicting what the reality that was captured in  
**Translation:** 

**[868.60s] English:** the straws form yeah because what people don't realize is that the compression on video and audio  
**Translation:** 

**[874.52s] English:** is 100 times right like people don't realize how compressed we we do right for audio you move  
**Translation:** 

**[882.10s] English:** you compress by when you go from normal audio to mp3 you compress by 10 times right when you move  
**Translation:** Vocabulary: compress: 压缩; compressed: 已压缩

**[888.16s] English:** to video you need 100 times 200 times right so you need to remove all the details but that you  
**Translation:** 

**[895.06s] English:** don't care about because all the compressions that we do and that's very important  
**Translation:** Vocabulary: compressions: 压缩

**[898.60s] English:** people forget about that is to be viewed by humans right so all the codecs either for audio mimic  
**Translation:** 

**[905.26s] English:** basically how your ear works right and and a lot of things about like the the the response on the  
**Translation:** 

**[910.66s] English:** ear and same for for your eyes right and and so for example on video we don't work on rgb right  
**Translation:** 

**[917.14s] English:** everyone expects to work in rgb we don't right we move to yuv which is basically one is luminance  
**Translation:** Vocabulary: luminance: 亮度

**[924.16s] English:** brightness and the other are colors and this matches your eyes where inside your eyes you're  
**Translation:** 

**[928.60s] English:** you have the cones and the buttons right with some of them look on brightness and more on the other  
**Translation:** 

**[932.92s] English:** on colors right so we need to compress a lot and so we need to degrade but in order to degrade we  
**Translation:** 

**[939.46s] English:** need to match the human perception and this is why it's so difficult and then we need to use the  
**Translation:** Vocabulary: degrade: 降低质量

**[944.56s] English:** maximum power mathematical power uh very complex technologies uh we move to the frequency domain  
**Translation:** 

**[950.56s] English:** as kieran said we do a ton of the quantizing and in order to get the best compression but it still  
**Translation:** Vocabulary: mathematical: 数学运算; quantizing: 量化

**[958.60s] English:** you're trying to compress in  
**Translation:** 

**[960.00s] English:** order to maximize the highest quality thing for human perception. That is correct. And that is  
**Translation:** Vocabulary: maximize: 最大化

**[966.14s] English:** correct. And this is very important, right? Compression is not like a zip, right? A zip,  
**Translation:** 

**[970.62s] English:** you have data in, you get data out, right? And you try with all the zip compression to arrive with  
**Translation:** 

**[976.60s] English:** the limit. Here, we are degrading the signal, right? And so we need to degrade both the audio  
**Translation:** 

**[982.42s] English:** and the video signal in the best way possible. And we can do that, but it involves first a lot  
**Translation:** Vocabulary: degrading: 降低质量

**[988.98s] English:** of theoretical knowledge about how it works, the eye works, but a lot of mathematical change,  
**Translation:** 

**[995.44s] English:** a lot of mathematical tricks, right? For example, when you move to RGB and you go to YUV, for  
**Translation:** 

**[1001.38s] English:** example, what we do very often is that we scale down the resolution of the color compared to the  
**Translation:** 

**[1007.08s] English:** brightness. And most of the time, and just this without compression, it divides the size by two,  
**Translation:** Vocabulary: compression: 压缩

**[1013.54s] English:** but most people don't see it, right? And so on and so on, right? And then,  
**Translation:** 

**[1019.14s] English:** you go to very complex mathematical change. So of course, Fourier transform, which de facto are  
**Translation:** Vocabulary: facto: 实际上; fourier: 傅里叶变换

**[1025.52s] English:** not Fourier transform, they are like discrete continuous transform, but that's the same idea.  
**Translation:** 

**[1030.12s] English:** So frequency domain, we split the video by blocks, right? So that's why when it's wrongly  
**Translation:** Vocabulary: discrete: 离散的

**[1036.10s] English:** decoded, you see those blocks and badly encoded, you see those blocks and so on to arrive to  
**Translation:** 

**[1041.40s] English:** compression states that are insanely high, right? And each generation of the codec is like 30% less.  
**Translation:** Vocabulary: encoded: 编码后的

**[1048.98s] English:** For the same quality, right? And this requires amount of power, of computational power that are  
**Translation:** 

**[1055.26s] English:** huge.  
**Translation:** Vocabulary: computational: 计算的

**[1055.90s] English:** No, but you should elaborate. It's 30% better, but an order of magnitude, perhaps even two orders  
**Translation:** 

**[1061.94s] English:** of magnitude, more compression power. That's the big difference.  
**Translation:** Vocabulary: elaborate: 详细说明

**[1065.64s] English:** What do you mean by compression power?  
**Translation:** 

**[1067.04s] English:** Sorry, CPU power to achieve that level of compression.  
**Translation:** 

**[1069.38s] English:** Oh, yeah. So you have to be able to leverage the CPU and sometimes GPU, like you mentioned.  
**Translation:** 

**[1073.60s] English:** And then we should mention that a lot of this programming is done,  
**Translation:** Vocabulary: leverage: 充分利用

**[1078.98s] English:** at the lowest.  
**Translation:** 

**[1080.00s] English:** possible stack whether it's c and of course as as the legendary twitter handle um re-emphasizes  
**Translation:** 

**[1087.92s] English:** over and over a lot of assembly so what happens is globally is that you have an address right  
**Translation:** 

**[1092.54s] English:** which gives you uh with the operating system a stream of bytes a stream of data right and this  
**Translation:** Vocabulary: bytes: 字节; globally: 全球地

**[1097.40s] English:** is the first step and the second step arise with demuxing where you're going to separate audio  
**Translation:** 

**[1101.96s] English:** video subtitle in type of different tracks and then on each of those tracks you're going to  
**Translation:** Vocabulary: demuxing: 解多路; subtitle: 字幕

**[1107.00s] English:** decompress and decode them either audio with an audio codec video to video codec and subtitle to  
**Translation:** 

**[1112.68s] English:** subtitle codec and once you've decompressed those type of things you have raw images raw  
**Translation:** Vocabulary: decompress: 解压; decompressed: 已解压

**[1118.68s] English:** and then you're going to talk to with your graphic card in your screen and display that and same for  
**Translation:** 

**[1123.34s] English:** the audio you're going to talk to your audio card which then is going to go in analog to to your  
**Translation:** Vocabulary: analog: 模拟的

**[1129.12s] English:** audio speakers and everything we've just said in the past couple of minutes every sentence is  
**Translation:** 

**[1134.52s] English:** someone's lifetime's work there are books about every sentence  
**Translation:** 

**[1136.98s] English:** so the level of complexity in many cases is inordinate you know it's it's every sentence  
**Translation:** 

**[1143.18s] English:** has thousands of people working on this in in industry as a whole books written about it so  
**Translation:** Vocabulary: complexity: 复杂性; inordinate: 过度的

**[1150.84s] English:** there's a lot of detail there's a lot of subtleties there's a lot of both  
**Translation:** 

**[1155.12s] English:** academic and practical realities um both of which matter uh we mentioned codecs but i don't think  
**Translation:** Vocabulary: subtleties: 细微差别

**[1162.46s] English:** you mentioned containers so what what's the actual  
**Translation:** 

**[1166.72s] English:** container  
**Translation:** 

**[1166.96s] English:** for some of the stuff we're talking about so people are familiar with mp4 uh mov mkv so anyway  
**Translation:** 

**[1176.46s] English:** what what are containers versus uh the thing that goes inside so the container is what we call also  
**Translation:** 

**[1182.78s] English:** the muxer right when i said demuxing it means decontinizing right so actually if you look  
**Translation:** 

**[1188.30s] English:** mux multiplexer and demultiplexer right mux and demux are those and same codec is actually coder  
**Translation:** Vocabulary: demultiplexer: 解复用器; multiplexer: 复用器

**[1196.52s] English:** decoder right um and um so  
**Translation:** 

**[1200.00s] English:** So containers are this collection of multiple tracks, right?  
**Translation:** 

**[1204.02s] English:** So it's what normal people call the file format,  
**Translation:** 

**[1207.24s] English:** but it's a bit more subtle than that.  
**Translation:** 

**[1210.36s] English:** But the most known one, of course, is MP4.  
**Translation:** 

**[1212.92s] English:** But when I started, it was AVI, right?  
**Translation:** 

**[1215.62s] English:** AVI was the video format from Microsoft.  
**Translation:** 

**[1219.18s] English:** And MOV, M-O-V, which became MP4, was a format from Apple.  
**Translation:** 

**[1224.06s] English:** In the open source community,  
**Translation:** 

**[1225.34s] English:** one of the persons that is still active on Videoland  
**Translation:** Vocabulary: videoland: 视频乐园

**[1227.64s] English:** is called Steve Lom and started this Matroska format,  
**Translation:** 

**[1231.48s] English:** which is a bit more complex and more feature-proof.  
**Translation:** Vocabulary: matroska: 矩阵块

**[1235.86s] English:** And there are so many others.  
**Translation:** 

**[1238.56s] English:** So, I mean, it's a pretty common thing,  
**Translation:** 

**[1240.58s] English:** and maybe it'll even happen in this conversation,  
**Translation:** 

**[1243.18s] English:** that people confuse container and the codec, right?  
**Translation:** 

**[1246.82s] English:** So they confuse MP4 and H.264, for example.  
**Translation:** 

**[1249.98s] English:** Is that a horrible violation?  
**Translation:** 

**[1251.56s] English:** No, it's not.  
**Translation:** 

**[1252.24s] English:** Because technically, the name of H.264 is MPEG-4,  
**Translation:** 

**[1257.64s] English:** part 10, because MPEG-4 is actually a meta-specification,  
**Translation:** 

**[1262.40s] English:** which has several things in it, right?  
**Translation:** 

**[1265.10s] English:** There is the part 2, so there is like audio codecs, right?  
**Translation:** 

**[1269.30s] English:** AAC, the factor is MP4 audio, something.  
**Translation:** 

**[1272.38s] English:** There is actually several video codecs, right,  
**Translation:** 

**[1274.80s] English:** inside the MPEG-4 specification.  
**Translation:** Vocabulary: specification: 规范

**[1277.04s] English:** One of them is MPEG-4 part 10, called also AVC,  
**Translation:** 

**[1280.92s] English:** called also H.264, right?  
**Translation:** 

**[1283.46s] English:** So it's completely the fault of the industry to make things,  
**Translation:** 

**[1287.64s] English:** difficult to understand.  
**Translation:** 

**[1289.02s] English:** So that's very difficult, so that people then don't understand  
**Translation:** 

**[1292.60s] English:** why sometimes you talk about MPEG-4 part 10,  
**Translation:** 

**[1295.32s] English:** where you mean H.264, and why it's not MP4.  
**Translation:** 

**[1298.32s] English:** So you can technically shove in all kinds of different codecs  
**Translation:** Vocabulary: shove: 硬塞

**[1301.74s] English:** inside containers, and horribly so.  
**Translation:** 

**[1304.40s] English:** But broadly speaking, though, MP4 is understood to generally be  
**Translation:** Vocabulary: horribly: 极其糟糕地

**[1309.08s] English:** H.264 plus AAC audio.  
**Translation:** 

**[1311.46s] English:** 99% of the time, that's that and that.  
**Translation:** 

**[1314.80s] English:** The rest are de minimis, the small effects, you know,  
**Translation:** 

**[1317.22s] English:** edge effects, really, compared to that.  
**Translation:** 

**[1318.80s] English:** So it's not the end.  
**Translation:** 

**[1320.00s] English:** of the world that there are people who do get annoyed by that but also in reality something  
**Translation:** 

**[1324.60s] English:** like vlc just to point out the file may say dot mp4 but it may be something completely different  
**Translation:** 

**[1330.26s] English:** and that's one of the challenges both ffmpeg and vlc have is the real world is a completely  
**Translation:** 

**[1334.82s] English:** different place to a three-letter file format and this is very important to say right like  
**Translation:** 

**[1339.34s] English:** for example in vlc and ffmpeg we discard the file format right we we look into the file to  
**Translation:** 

**[1346.36s] English:** understand what's in it because so many people like they say oh it's a video it should must be  
**Translation:** 

**[1351.52s] English:** mp4 but technically it's an mov or maybe it's a mkv right so we analyze in real time everything  
**Translation:** 

**[1358.84s] English:** that we have and we don't trust uh the the format so what information does the fact that  
**Translation:** 

**[1364.46s] English:** is dot mp4 give you it helps right it gives you a hint right just like oh it's finished by dot mp4  
**Translation:** 

**[1370.78s] English:** i will start first by opening probing it with the mp4  
**Translation:** 

**[1376.18s] English:** format  
**Translation:** 

**[1376.36s] English:** container demuxer to see well it should be that but i don't trust it and if i'm lost i say okay  
**Translation:** 

**[1381.98s] English:** maybe i'm going to try it so it bumps the priority of the module so how do you get to  
**Translation:** 

**[1388.16s] English:** just to take a bit of a tangent there you know the dumb thing is if you try the mp4 but it turns  
**Translation:** 

**[1395.68s] English:** out it's a different codec than you would have expected uh most players just break there yes  
**Translation:** Vocabulary: tangent: 旁枝逸出

**[1401.96s] English:** yes so how do you not break there's just a philosophically  
**Translation:** 

**[1405.60s] English:** i'm sure you've heard of it but it's a different codec than you would have expected  
**Translation:** Vocabulary: philosophically: 从哲学角度

**[1406.34s] English:** sure there's a bunch of stumbling blocks along the way where you it's easy to just break and  
**Translation:** 

**[1411.52s] English:** stop freak out that's it how does vlc not this is why vlc is popular um but the reason is because  
**Translation:** Vocabulary: stumbling: 绊脚石

**[1418.30s] English:** actually vlc was is just a client of a streaming solution called video land from from from very  
**Translation:** 

**[1426.24s] English:** long time ago from the late 90s and when you're playing video which are on udp right in network  
**Translation:** 

**[1432.96s] English:** they might be damaged right so you don't trust your inputs and this is the reason why vlc is so popular  
**Translation:** 

**[1436.34s] English:** it's very important into the security is that you don't trust your inputs so  
**Translation:** 

**[1440.00s] English:** everything in VLC is prepared to work with broken files.  
**Translation:** 

**[1446.26s] English:** And it's a philosophical idea from the beginning,  
**Translation:** Vocabulary: philosophical: 哲学理念

**[1449.94s] English:** and everything is engineered into that.  
**Translation:** 

**[1452.66s] English:** And it's a culture, right?  
**Translation:** 

**[1454.02s] English:** And so, for example,  
**Translation:** 

**[1455.54s] English:** and VLC became very popular on that  
**Translation:** 

**[1457.28s] English:** because a long time ago when people were pirating content,  
**Translation:** 

**[1460.48s] English:** which they do a lot less today.  
**Translation:** Vocabulary: pirating: 非法复制

**[1463.36s] English:** And none of us ever have.  
**Translation:** 

**[1464.68s] English:** No, of course not.  
**Translation:** 

**[1466.52s] English:** The metadata to place on files like AVI  
**Translation:** 

**[1469.04s] English:** is at the end of the file, right?  
**Translation:** Vocabulary: metadata: 文件信息

**[1472.22s] English:** And when you're downloading, you don't have that, right?  
**Translation:** 

**[1474.52s] English:** So VLC was just like, hey, this file is broken,  
**Translation:** 

**[1477.14s] English:** but I'm still going to try to interpret it.  
**Translation:** 

**[1479.38s] English:** And this was very useful.  
**Translation:** Vocabulary: interpret: 解释

**[1481.30s] English:** We hinted at the awesomeness of the various different stages.  
**Translation:** 

**[1485.34s] English:** We hinted at the awesomeness of codecs,  
**Translation:** Vocabulary: awesomeness: 惊人的特性

**[1487.64s] English:** the depth and the richness and the complexity  
**Translation:** 

**[1489.52s] English:** of everything involved there.  
**Translation:** Vocabulary: complexity: 复杂性

**[1491.40s] English:** Let's try to define what is a video codec?  
**Translation:** 

**[1495.70s] English:** What's involved there?  
**Translation:** 

**[1496.76s] English:** What does it mean to compress something?  
**Translation:** 

**[1498.24s] English:** You already started to hint at it,  
**Translation:** Vocabulary: compress: 压缩

**[1499.68s] English:** but can we elaborate a little bit more?  
**Translation:** 

**[1501.84s] English:** So there's a huge amount of redundancy in any video,  
**Translation:** Vocabulary: elaborate: 详细说明; redundancy: 重复内容

**[1505.08s] English:** both spatial and temporal.  
**Translation:** 

**[1507.04s] English:** And the point of any video codec  
**Translation:** Vocabulary: spatial: 空间; temporal: 时间

**[1508.68s] English:** is to remove this redundant data,  
**Translation:** 

**[1510.92s] English:** use mathematical properties  
**Translation:** Vocabulary: mathematical: 数学的; redundant: 多余的

**[1512.04s] English:** as part of this reduction process.  
**Translation:** 

**[1514.38s] English:** So more often than not,  
**Translation:** 

**[1515.56s] English:** using several orders of magnitude more compute to compress  
**Translation:** 

**[1518.40s] English:** because that's more costly versus,  
**Translation:** 

**[1520.84s] English:** both costly both financially and in CPU resources,  
**Translation:** 

**[1523.66s] English:** versus the decompression.  
**Translation:** Vocabulary: decompression: 解压缩; financially: 经济上

**[1525.10s] English:** So it's asymmetric in that respect.  
**Translation:** 

**[1527.42s] English:** Often the case is,  
**Translation:** Vocabulary: asymmetric: 不对称

**[1528.22s] English:** because compression is done once,  
**Translation:** 

**[1529.84s] English:** but there could be lots of viewers of another file.  
**Translation:** 

**[1533.16s] English:** So to take that information and compress it by 100x, 200x,  
**Translation:** 

**[1537.78s] English:** removing redundant information  
**Translation:** 

**[1540.00s] English:** and using mathematical properties to make that small,  
**Translation:** 

**[1542.18s] English:** but also have properties such as error resilience.  
**Translation:** Vocabulary: resilience: 抗干扰性

**[1545.10s] English:** So as JB suggested, VLC in the beginning was used to play  
**Translation:** 

**[1549.72s] English:** UDP network feeds and UDP network feeds lose packets.  
**Translation:** 

**[1553.42s] English:** And so some of the design goals of a codec is also to be recoverable.  
**Translation:** 

**[1557.66s] English:** Mm-hmm.  
**Translation:** 

**[1557.82s] English:** You need to actually be able to join the stream.  
**Translation:** 

**[1560.00s] English:** It's not necessarily a file.  
**Translation:** 

**[1561.22s] English:** You need to join, get on the decoding process, and start decoding.  
**Translation:** 

**[1566.18s] English:** And to give a more image to people who are not familiar, right?  
**Translation:** 

**[1571.46s] English:** Like when you're going to see any type of movie, right?  
**Translation:** 

**[1574.24s] English:** You're going to see the camera is going to pan, right?  
**Translation:** 

**[1576.90s] English:** And travel.  
**Translation:** 

**[1578.04s] English:** And you realize that, for example, all the background is the same for like a minute, right?  
**Translation:** 

**[1583.24s] English:** Or 30 seconds, right?  
**Translation:** 

**[1584.44s] English:** So you can reuse the cloud that you see on the background.  
**Translation:** Vocabulary: reuse: 重复使用

**[1588.22s] English:** You can reuse that from a frame to another, right?  
**Translation:** 

**[1591.02s] English:** And so it gets the more memory you have, the more power, the more comparisons you can make, right?  
**Translation:** 

**[1598.66s] English:** And so the more compressed you can be.  
**Translation:** 

**[1600.86s] English:** And most of the modern codecs are basically doing that.  
**Translation:** Vocabulary: compressed: 压缩

**[1604.70s] English:** So just to make it even more explicit.  
**Translation:** 

**[1607.34s] English:** So what is video?  
**Translation:** Vocabulary: explicit: 明确的

**[1608.84s] English:** Video is a bunch of pixels off an RGB.  
**Translation:** 

**[1613.38s] English:** You have three values.  
**Translation:** Vocabulary: pixels: 像素

**[1616.02s] English:** And you have a grid of pixels.  
**Translation:** 

**[1617.76s] English:** And you have...  
**Translation:** 

**[1618.22s] English:** Let's say 24, 30, or 60 frames a second.  
**Translation:** 

**[1623.98s] English:** And you just have all these pixels repeating and showing different stuff 30 times a second.  
**Translation:** 

**[1630.22s] English:** And so the question, the philosophical, the technical question is,  
**Translation:** 

**[1634.62s] English:** how can I compress all of that, store all of that at 100x?  
**Translation:** Vocabulary: compress: 压缩; philosophical: 哲学的

**[1640.68s] English:** Or 1000x, right?  
**Translation:** 

**[1642.08s] English:** 1000x.  
**Translation:** 

**[1642.72s] English:** The target is 1000x, right?  
**Translation:** 

**[1644.26s] English:** And the goal is, when you say redundancy,  
**Translation:** Vocabulary: redundancy: 多余

**[1647.76s] English:** what is redundant, meaning stuff at best that humans wouldn't notice if it was missing?  
**Translation:** 

**[1655.40s] English:** So, for example, you have a picture of a cloud, right?  
**Translation:** 

**[1658.36s] English:** And from the next frame, they're still going to be the same cloud.  
**Translation:** 

**[1661.14s] English:** So it's redundant.  
**Translation:** Vocabulary: redundant: 多余

**[1661.86s] English:** You could just put it once and not do it, right?  
**Translation:** 

**[1664.24s] English:** Or you have a black background behind me, for example.  
**Translation:** 

**[1667.48s] English:** The black is the same on the whole picture, right?  
**Translation:** 

**[1669.30s] English:** So you can say, well, you know, in this picture, take the pixels that you have on the top left.  
**Translation:** 

**[1674.08s] English:** And the one on the top right, I'm not going to give the value.  
**Translation:** 

**[1676.84s] English:** I'm just going to tell you.  
**Translation:** 

**[1677.94s] English:** It's the same at the top left.  
**Translation:** 

**[1679.42s] English:** And then you can.  
**Translation:** 

**[1680.00s] English:** say for frame one reuse something from the previous frame or the previous previous frame and so on and  
**Translation:** 

**[1686.52s] English:** so on right so you could basically it's unlimited but then it's limited in terms of memory or in  
**Translation:** 

**[1693.92s] English:** terms of compute power because for example if you need to compare pixels on 200 frames in the past  
**Translation:** 

**[1700.14s] English:** on 4k resolutions it's a huge amount of compute and then when you're showing it you have to do  
**Translation:** Vocabulary: resolutions: 分辨率

**[1708.14s] English:** the decompress of all of that so is it the codec the has the encoding and the decoding is that  
**Translation:** 

**[1715.54s] English:** there's a coupled process that you're developing exactly right and those are two different um  
**Translation:** Vocabulary: decompress: 解压; encoding: 编码

**[1720.66s] English:** trade-offs right are you going to compress more uh but then it might be more difficult to to to  
**Translation:** 

**[1726.86s] English:** decode um are you going to come to make it a codec that is more complex to encode and easier  
**Translation:** Vocabulary: encode: 编码

**[1732.80s] English:** to decode are you going to make a codec that is easier to encode because you need to be fast  
**Translation:** 

**[1737.06s] English:** but then the  
**Translation:** 

**[1738.14s] English:** client side the player is going to spend more time that's why you have so many different type  
**Translation:** 

**[1742.90s] English:** of codecs is that it's not always easy and to make it even more complex modern codecs like av1 av2  
**Translation:** 

**[1750.18s] English:** or vvc are actually not codecs they are a collection of tools right there are multiple tools  
**Translation:** 

**[1755.82s] English:** multiple codecs in the same codec to depending on the image get the more compression so just to  
**Translation:** Vocabulary: compression: 压缩

**[1762.34s] English:** elaborate codecs like av1 vvc have a much wide have a wide audience it could be a screen share  
**Translation:** 

**[1770.30s] English:** content it could be video it could be animation all of these require different coding tools  
**Translation:** Vocabulary: elaborate: 复杂

**[1776.88s] English:** so what happens these days is a collection of tools are put in and called av1 and called av2  
**Translation:** 

**[1783.48s] English:** called vvc to allow for different use cases so you may be on zoom and sharing your powerpoint  
**Translation:** Vocabulary: powerpoint: 演示文稿

**[1789.78s] English:** and then you need to show the audience a video  
**Translation:** 

**[1791.58s] English:** that  
**Translation:** 

**[1792.34s] English:** needs to start changing its tool set depending on the content to compress in a different way  
**Translation:** 

**[1800.00s] English:** Like you said, there's a bunch of incredible engineers behind each part of that,  
**Translation:** Vocabulary: compress: 压缩

**[1803.64s] English:** each part of the tools that make up AV1, for example.  
**Translation:** 

**[1805.74s] English:** Sure.  
**Translation:** 

**[1806.44s] English:** So we've kind of danced around it.  
**Translation:** 

**[1808.94s] English:** We talked about VLC, the logo, the hat.  
**Translation:** 

**[1812.88s] English:** Let's talk about FFmpeg.  
**Translation:** 

**[1814.50s] English:** What is FFmpeg exactly?  
**Translation:** 

**[1817.48s] English:** FFmpeg is basically the low-level libraries for codec,  
**Translation:** 

**[1824.90s] English:** so compressions and decompression, muxes and demuxes and filters.  
**Translation:** Vocabulary: compressions: 压缩; decompression: 解压

**[1829.48s] English:** The core is this, and then you have several tools  
**Translation:** 

**[1832.96s] English:** which allow you to create a type of pipeline to process any type of video files.  
**Translation:** Vocabulary: pipeline: 数据管道

**[1838.22s] English:** And it's used as a library absolutely inside everything,  
**Translation:** 

**[1842.48s] English:** from VLC to Chrome to your smart TVs to basically any video that you see online.  
**Translation:** 

**[1848.34s] English:** You usually use FFmpeg.  
**Translation:** 

**[1850.68s] English:** And FFmpeg in it has all those type of tools  
**Translation:** 

**[1854.32s] English:** and sometimes depends on other libraries like x264, LibView,  
**Translation:** 

**[1859.48s] English:** DPX and others, right?  
**Translation:** 

**[1860.98s] English:** So it's really now the de facto tool to process images.  
**Translation:** 

**[1866.00s] English:** From a philosophical level, I think it's incredible that your home videos,  
**Translation:** Vocabulary: facto: 实际上; philosophical: 哲学的

**[1870.92s] English:** your grandmother's home videos and trillion-dollar corporations  
**Translation:** 

**[1874.50s] English:** effectively are on a level playing field using the same technology stack.  
**Translation:** 

**[1880.52s] English:** It wouldn't be a surprise.  
**Translation:** 

**[1882.60s] English:** These big companies just have 3,000-line FFmpeg commands.  
**Translation:** 

**[1887.20s] English:** There are some that use the API,  
**Translation:** 

**[1888.76s] English:** but there are some that just have long command lines.  
**Translation:** 

**[1891.88s] English:** So, yeah, there's a bunch of tools, like literally command line tool,  
**Translation:** 

**[1895.54s] English:** FFmpeg, of course, FFprobe.  
**Translation:** 

**[1898.32s] English:** There's libraries, LibAV Codec, LibAV Format, LibAV Filter.  
**Translation:** 

**[1903.44s] English:** But the FFmpeg on the command line is like legendary  
**Translation:** 

**[1908.48s] English:** because you can cut, there's so many parameters,  
**Translation:** 

**[1912.00s] English:** you can customize everything to help.  
**Translation:** 

**[1913.44s] English:** It's a language. It's an actual language.  
**Translation:** 

**[1915.12s] English:** It's an actual, yeah, you could think of it as a programming language.  
**Translation:** 

**[1917.84s] English:** Yeah, of course, I'm sure.  
**Translation:** 

**[1918.76s] English:** Because, so most of...  
**Translation:** 

**[1920.00s] English:** people they're going to take ffmpeg file in file out and specify the format right but you can we've  
**Translation:** 

**[1925.92s] English:** seen thousands of characters and we've seen also like people like doing um programming um uh  
**Translation:** 

**[1933.08s] English:** generation of common lines to to to make ffmpeg there is a ton of people who are using ai to  
**Translation:** 

**[1938.34s] English:** generate common lines for ffmpeg because you have no idea what it is but you can specify so many  
**Translation:** 

**[1942.96s] English:** filters right uh on common line right so um ffmpeg is this collection of toolbox for multimedia  
**Translation:** 

**[1949.98s] English:** processing that everyone everyone uses and everyone that is watching your videos are also  
**Translation:** Vocabulary: multimedia: 多种媒体; toolbox: 工具箱

**[1956.82s] English:** using right you you're on youtube well it's ffmpeg on on the client side well your server side on the  
**Translation:** 

**[1962.98s] English:** server side the client side is probably chrome well you're using ffmpeg also and and you're  
**Translation:** 

**[1967.78s] English:** using obs to record well it's ffmpeg right you're using a ton of important like big box  
**Translation:** 

**[1972.78s] English:** properties and you're using ffmpeg to record well it's ffmpeg right you're using a ton of  
**Translation:** 

**[1972.94s] English:** boxes well it's very possible that inside some part of ffmpeg is running i mean there's like so  
**Translation:** 

**[1978.98s] English:** many just to give people an idea like i use ffmpeg a lot on everything just trivial stuff like  
**Translation:** 

**[1985.12s] English:** take a video add an intro video and an outro video and fade one into the other like uh what  
**Translation:** 

**[1993.48s] English:** is it called dip to black like where it dips and then shows the next video and does the same thing  
**Translation:** Vocabulary: intro: 开场视频

**[1999.50s] English:** with audio uh there's like a cross dissolve of  
**Translation:** 

**[2002.76s] English:** the audio it's a quiet it quiets the audio and makes it loud again and then there's a bunch of  
**Translation:** 

**[2007.98s] English:** stuff like uh showing the captions on screen card like baking the captions in you can customize the  
**Translation:** 

**[2015.50s] English:** font you can do all kinds of layering of audio and video there's a million things and of course  
**Translation:** Vocabulary: captions: 字幕; layering: 叠加

**[2022.56s] English:** all of that works like magically with basically any codec like anything you can shove in on the  
**Translation:** 

**[2031.52s] English:** audio and the video side it works it works it works it works it works it works it works it works it  
**Translation:** Vocabulary: shove: 强行插入

**[2032.76s] English:** but it's like if you if you look at for example you can do things that you would do with adobe after effects  
**Translation:** 

**[2040.00s] English:** come online on ffmpeg right it's it's very interesting because for example for for for  
**Translation:** 

**[2045.00s] English:** images there is not such tool there is a few tools but not with the breadth of ffmpeg so image magic  
**Translation:** 

**[2051.44s] English:** has a similar kind of yes but you will not do some filters complex filters you don't have the  
**Translation:** 

**[2057.42s] English:** equivalent of photoshop in come online right but you for video you have ffmpeg in come online yeah  
**Translation:** 

**[2062.86s] English:** it's incredible i mean it's like it's an example of a thing when a bunch of great people get  
**Translation:** 

**[2067.62s] English:** together and they get a vision and they stick by that vision for many years which is incredible  
**Translation:** 

**[2073.52s] English:** and the vision behind and the same for vlc and ffmpeg is that we make every everything that is  
**Translation:** 

**[2080.66s] English:** very complex easy to use for the normal people for everyone right our goal is to make something  
**Translation:** 

**[2087.06s] English:** that is insanely complex technically and make it easy to use right and and people they use vlc they  
**Translation:** 

**[2093.24s] English:** drop a file they don't realize how complex the file is but they play it  
**Translation:** 

**[2097.62s] English:** or people put any type of thing inside ffmpeg with complex filters and it just works like  
**Translation:** 

**[2103.08s] English:** magically right and people and this is our mission right make very complex things we wouldn't be here  
**Translation:** 

**[2109.02s] English:** and you wouldn't be here if this required you know a traditional television studio setup  
**Translation:** Vocabulary: setup: 设备配置

**[2115.24s] English:** it's tools like ffmpeg that democratize this the the podcast and streaming revolution the youtube  
**Translation:** 

**[2121.04s] English:** revolution was caused you know ffmpeg was a big player in that because it democratized this  
**Translation:** Vocabulary: democratize: 使大众化; democratized: 使大众化

**[2127.62s] English:** it was once in the in the 90s for example you needed equipment that cost hundreds of thousands  
**Translation:** 

**[2133.50s] English:** of dollars to do compression it was the size of a car and now everybody has that at almost an exact  
**Translation:** Vocabulary: compression: 压缩

**[2139.66s] English:** level playing field and that's something that's so remarkable it gave voice to a lot of people  
**Translation:** 

**[2144.18s] English:** and we just to clarify we say you you wouldn't be here not the human but the podcast  
**Translation:** 

**[2148.96s] English:** vlc did not have anything to do on the biological level  
**Translation:** 

**[2154.54s] English:** creating me as a human you realize  
**Translation:** 

**[2157.62s] English:** so everything moved from text to  
**Translation:** 

**[2160.00s] English:** images and images to video right look look at social networks video is everywhere it's the most  
**Translation:** 

**[2165.74s] English:** powerful um medium there is right and and when you see shorts and and in reels and in tiktok right  
**Translation:** 

**[2172.84s] English:** it's amazingly powerful to to to give video is amazing for that right but the complexity is  
**Translation:** Vocabulary: complexity: 复杂性; reels: 短视频

**[2179.42s] English:** important it's what people don't realize i mean this is really it gave power to the individual  
**Translation:** 

**[2186.58s] English:** all across the world it's real freedom and i think i can't believe it but we still haven't  
**Translation:** 

**[2191.48s] English:** mentioned the actual obvious thing for people who are not familiar which it's open source and  
**Translation:** 

**[2198.24s] English:** there's a open source community of users and developers behind it so it's really it's a  
**Translation:** 

**[2205.00s] English:** movement so like we'll talk a bunch in a bunch of different ways about the community behind it but  
**Translation:** 

**[2209.80s] English:** uh can you speak to the open source element so when we say what is ffmpeg it's an open source  
**Translation:** 

**[2216.58s] English:** project yeah so ffmpeg vlc x264 video and everything we do is fully open source and for  
**Translation:** 

**[2223.30s] English:** the people who don't understand how open source is my usual analogy is about a chocolate cheesecake  
**Translation:** Vocabulary: cheesecake: 蛋糕例子

**[2227.80s] English:** right um usually for you when you want to buy your cheesecake you go to a bakery they give you the  
**Translation:** 

**[2232.84s] English:** cheesecake um the other one way of having a cheesecake is have your grandma give you a  
**Translation:** 

**[2237.50s] English:** recipe of how to make that when we do open source we give you the chocolate cake and we give you  
**Translation:** 

**[2243.28s] English:** the recipe to actually remake the same cake  
**Translation:** Vocabulary: remake: 重新制作

**[2246.58s] English:** but at the same time tell you how to build the oven and also how you're allowed to modify the  
**Translation:** 

**[2252.94s] English:** recipe and resell it to someone else yeah and this is because software is just a very long recipe of  
**Translation:** Vocabulary: resell: 重新销售

**[2258.88s] English:** small instruction computers are not very clever they go very very fast so a normal program has  
**Translation:** 

**[2265.12s] English:** tens of billions of instruction instead of the tens when you have your chocolate recipe so  
**Translation:** 

**[2270.64s] English:** a lot of the software industry was about selling software like where you just have like the final  
**Translation:** 

**[2276.58s] English:** step and that's what we have here in open source we make we give you everything  
**Translation:** 

**[2280.00s] English:** And that managed to get a lot of people to work together, right?  
**Translation:** 

**[2284.52s] English:** Because then you decide that you're going to make the best program,  
**Translation:** 

**[2287.72s] English:** the best recipe for video, and you create communities.  
**Translation:** 

**[2291.42s] English:** In FFmpeg, since the beginning of FFmpeg,  
**Translation:** 

**[2294.42s] English:** probably 2,000 to 3,000 people have contributed from the beginning, right?  
**Translation:** 

**[2299.50s] English:** And then it's exactly like the Linux kernel, right?  
**Translation:** 

**[2301.82s] English:** The Linux kernel has probably 10,000 people contributing everywhere.  
**Translation:** 

**[2305.52s] English:** And they get together, well, mostly online, right?  
**Translation:** Vocabulary: kernel: 内核

**[2309.42s] English:** So they virtually get together to create the best tool for something.  
**Translation:** 

**[2314.48s] English:** And on FFmpeg and VLC, it's just like, well, this codec doesn't work.  
**Translation:** 

**[2320.20s] English:** So I'm going to work on the codec,  
**Translation:** 

**[2321.92s] English:** and I'm going to add the support for this file inside FFmpeg  
**Translation:** 

**[2325.50s] English:** so it will be beneficial to everyone.  
**Translation:** 

**[2328.06s] English:** Because again, we work for the greater good.  
**Translation:** 

**[2329.98s] English:** We work for everyone.  
**Translation:** 

**[2331.92s] English:** And that is what open source is.  
**Translation:** 

**[2334.12s] English:** And we should mention, depending on the licensing,  
**Translation:** 

**[2337.66s] English:** you could probably build it.  
**Translation:** 

**[2339.58s] English:** You could build a billion-dollar, maybe even a trillion-dollar company  
**Translation:** 

**[2343.16s] English:** around this as a wrapper.  
**Translation:** 

**[2347.20s] English:** Well, yes, people do.  
**Translation:** 

**[2349.00s] English:** People do, right?  
**Translation:** 

**[2349.84s] English:** There was a lot of problems with mostly cloud providers  
**Translation:** 

**[2354.22s] English:** who are basically running some open source tools in the cloud  
**Translation:** 

**[2358.90s] English:** and just give you the API to access to that.  
**Translation:** 

**[2362.34s] English:** And there was a lot of databases like Mongo or Elastic  
**Translation:** Vocabulary: databases: 数据库; elastic: 弹性; mongo: MongoDB

**[2367.44s] English:** who changed their license in order to avoid...  
**Translation:** 

**[2369.42s] English:** to avoid those type of scenarios.  
**Translation:** Vocabulary: scenarios: 情景

**[2371.54s] English:** This is a question we get a lot in FFmpeg is,  
**Translation:** 

**[2374.00s] English:** why don't you do that?  
**Translation:** 

**[2375.70s] English:** And you can't.  
**Translation:** 

**[2376.42s] English:** We have thousands of contributors,  
**Translation:** Vocabulary: contributors: 贡献者

**[2377.84s] English:** some of whom aren't even alive anymore.  
**Translation:** 

**[2380.38s] English:** You would need all of their agreement to do that.  
**Translation:** 

**[2382.86s] English:** And JB will go maybe a bit later and talk about  
**Translation:** 

**[2384.88s] English:** how challenging that process was in VLC to do the relicensing.  
**Translation:** Vocabulary: relicensing: 重新授权

**[2389.24s] English:** The license is a social contract in terms of Rousseau,  
**Translation:** 

**[2393.18s] English:** de facto, of the community.  
**Translation:** Vocabulary: facto: 实际上; rousseau: 卢梭

**[2395.28s] English:** The community does not agree on much,  
**Translation:** 

**[2398.78s] English:** besides the license,  
**Translation:** 

**[2399.42s] English:** people...  
**Translation:** 

**[2400.00s] English:** People go around, discuss around because of the license.  
**Translation:** 

**[2404.64s] English:** And that also allows those license forks, right?  
**Translation:** 

**[2406.88s] English:** Sometimes the community splits, but it's possible because of the license then to merge back.  
**Translation:** 

**[2412.10s] English:** And we've seen that so many times, right?  
**Translation:** 

**[2414.04s] English:** GCC and EGCC in the past.  
**Translation:** 

**[2417.92s] English:** We have seen, for example, all the web browsers, right?  
**Translation:** 

**[2420.24s] English:** They started as KHML, which becomes WebKit, and then which becomes Blink, right?  
**Translation:** Vocabulary: browsers: 浏览器

**[2424.78s] English:** So, open source license is like the core of the community.  
**Translation:** 

**[2430.82s] English:** And people are coming from all around the world, very different type of religion, political borders.  
**Translation:** 

**[2439.72s] English:** They work in the same way on a project to solve a specific problem.  
**Translation:** 

**[2445.44s] English:** And the specific problem we're working on is to make multimedia easy for everyone.  
**Translation:** Vocabulary: multimedia: 多种媒体

**[2450.16s] English:** Looking it up on Proplexity here, looking at the different open source licenses.  
**Translation:** 

**[2453.64s] English:** Most major open source licenses fall into two buckets.  
**Translation:** 

**[2458.22s] English:** Permissive, very few conditions, and copy left.  
**Translation:** 

**[2461.56s] English:** Share alike requirements for derivatives.  
**Translation:** Vocabulary: derivatives: 派生作品; permissive: 宽松的

**[2464.02s] English:** Below is a brief practical summary of the main ones you'll see in the wild.  
**Translation:** 

**[2468.52s] English:** MIT license, BSD, ISC, Apache, GNU GPL, GNU AGPL.  
**Translation:** 

**[2479.96s] English:** Where's LGPL?  
**Translation:** 

**[2480.72s] English:** Yeah, LGPL.  
**Translation:** 

**[2483.64s] English:** There's the Mozilla public license.  
**Translation:** 

**[2486.02s] English:** There's Eclipse public license.  
**Translation:** Vocabulary: eclipse: 日食

**[2487.78s] English:** It goes on.  
**Translation:** 

**[2488.74s] English:** There's a lot of variety.  
**Translation:** 

**[2489.98s] English:** I mean, I think the really popular ones is MIT, GPL, LGPL.  
**Translation:** 

**[2494.80s] English:** And BSD.  
**Translation:** 

**[2495.54s] English:** And BSD, Apache, sometimes you'll see.  
**Translation:** 

**[2498.18s] English:** Apache as well.  
**Translation:** Vocabulary: apache: Apache软件

**[2498.88s] English:** On license, that's an option.  
**Translation:** 

**[2500.44s] English:** Attempts to dedicate code to the public domain with a fallback permissive license.  
**Translation:** Vocabulary: fallback: 备用方案

**[2503.84s] English:** There are many licenses for many different things.  
**Translation:** 

**[2506.68s] English:** What people don't understand is that public domain is something that doesn't exist worldwide, right?  
**Translation:** 

**[2511.26s] English:** So, it's all the...  
**Translation:** 

**[2513.64s] English:** The open source licensing use the copyright law, right?  
**Translation:** 

**[2517.48s] English:** The international copyright law in order to give...  
**Translation:** 

**[2520.00s] English:** rights on how you use the software or how you modify it's de facto a copyright license contract  
**Translation:** Vocabulary: facto: 实际上

**[2527.04s] English:** that you give to the end user or to the developer and so you have like the first one which are  
**Translation:** 

**[2532.18s] English:** basically very permissive mit bsd you give the code and basically you do whatever you want right  
**Translation:** 

**[2537.98s] English:** you take it you want you modify you do what you want um and this is popular for uh javascript  
**Translation:** 

**[2545.82s] English:** and the type of bsd operating system so some of them one of the parameters is whether they  
**Translation:** 

**[2552.02s] English:** require attribution meaning if you use the code you have to say yes so in those type of permissive  
**Translation:** 

**[2557.96s] English:** license some you need to say if you use it which is called attribution and some you don't and then  
**Translation:** Vocabulary: attribution: 出处说明

**[2562.92s] English:** there is a the other part of license which are copy left where you need to give back to the  
**Translation:** 

**[2569.30s] English:** community your modifications and with different string attached um some weak uh copy left  
**Translation:** Vocabulary: modifications: 修改

**[2575.64s] English:** license and then you need to give back to the community your modifications and with different  
**Translation:** 

**[2575.80s] English:** license like um the mozilla public license to some which are a bit stronger uh like gpl or even  
**Translation:** 

**[2582.44s] English:** very strong like a gpl so all of those are different um type of licensing that depends on  
**Translation:** 

**[2588.80s] English:** what your goal are and how you want to structure your community which is why i spoke about social  
**Translation:** 

**[2593.16s] English:** contract because this is very important to understand ffmpeg and vlc are mostly gpl or  
**Translation:** 

**[2600.56s] English:** lgpl the linux kernel is gpl but android is  
**Translation:** Vocabulary: kernel: 内核

**[2605.62s] English:** apache uh a ton of uh javascript framework that are using mostly mit um all the bsd kernels open  
**Translation:** 

**[2614.46s] English:** bsd netbsd are of course bsd um and and so the it's philosophical change on how you want people  
**Translation:** Vocabulary: kernels: 内核; philosophical: 哲学的

**[2622.36s] English:** to contribute back basically so there's uh i think you talked about that uh you've moved at  
**Translation:** 

**[2629.90s] English:** one point from gpl to lgpl on certain parts of the project what what can you describe the  
**Translation:** 

**[2635.62s] English:** difference between the two and what does it take to move to i guess a more permissive  
**Translation:** 

**[2640.00s] English:** So that direction is more permissive.  
**Translation:** Vocabulary: permissive: 宽容的

**[2642.06s] English:** LGPL is more permissive than GPL.  
**Translation:** 

**[2643.92s] English:** Yeah.  
**Translation:** 

**[2644.20s] English:** So you have to realize that you can always go from more permissive to less permissive, right?  
**Translation:** 

**[2650.84s] English:** Because, of course, those licenses are basically statements.  
**Translation:** 

**[2654.98s] English:** So if you restrict, you can always restrict more, right?  
**Translation:** 

**[2657.76s] English:** So in a GPL project, you can take MIT code, but you cannot do the opposite, right?  
**Translation:** Vocabulary: cannot: 不能

**[2663.42s] English:** Because there are more constraints to match.  
**Translation:** 

**[2665.28s] English:** In fact, I changed the core of libVLC, which is the engine of VLC, from GPL to LGPL.  
**Translation:** Vocabulary: constraints: 限制条件

**[2677.72s] English:** And there were two reasons to do that.  
**Translation:** 

**[2680.02s] English:** The first one is that so people can use the VLC engine, libVLC, into third-party applications.  
**Translation:** 

**[2686.32s] English:** So a lot of applications which are playing video on your phone or on your tablet are actually VLC engine in it, which is calling FFmpeg in it.  
**Translation:** 

**[2694.42s] English:** Yeah.  
**Translation:** 

**[2695.28s] English:** So that was one of the ways to create one of the companies I created, which is doing consulting and integration of those types of applications where you integrate VLC into third-party solutions, like inside game engines or stuff like that.  
**Translation:** 

**[2710.48s] English:** With GPL, you couldn't do that because that means you needed to open source everything.  
**Translation:** 

**[2714.38s] English:** And those are for a lot of commercial companies who don't want that.  
**Translation:** 

**[2717.96s] English:** So you can create a company with LGPL.  
**Translation:** 

**[2720.76s] English:** You can create a company around it.  
**Translation:** 

**[2722.34s] English:** You can do a commercial thing.  
**Translation:** 

**[2723.34s] English:** You don't have to open source it.  
**Translation:** 

**[2724.34s] English:** So that's a big, big.  
**Translation:** 

**[2725.34s] English:** So you could play video in your game.  
**Translation:** 

**[2727.18s] English:** Yes.  
**Translation:** 

**[2727.60s] English:** The problem is I'm a game developer and I want to play some videos and I don't want to be forced to open source the entire game just to play those videos.  
**Translation:** 

**[2735.88s] English:** So that's where the consulting business, the libVLC LGPL, allows you to do that.  
**Translation:** 

**[2741.14s] English:** The LGPL, the library GPL, as it used to be known, allows you to do that.  
**Translation:** 

**[2744.72s] English:** And FFmpeg is exactly the same.  
**Translation:** 

**[2748.08s] English:** LGPL forces you to give back what you change on this component, this library, which is why it's library GPL.  
**Translation:** 

**[2755.28s] English:** And so you can use FFmpeg as LGPL into any type of application.  
**Translation:** 

**[2760.00s] English:** even non-open source, but you need to give back the modification you did on FFmpeg, same  
**Translation:** 

**[2765.18s] English:** on libvlc.  
**Translation:** Vocabulary: modification: 修改

**[2766.18s] English:** Is it limiting from an open source perspective to go GPL?  
**Translation:** 

**[2770.68s] English:** Because if your library, if your code is GPL, it means you're basically discouraging companies  
**Translation:** Vocabulary: discouraging: 阻碍合作

**[2780.78s] English:** from building a business around it, right?  
**Translation:** 

**[2782.84s] English:** Is that fair to say?  
**Translation:** 

**[2783.84s] English:** Yes.  
**Translation:** 

**[2784.84s] English:** It depends on the company, but the company whose business model requires the application  
**Translation:** 

**[2789.52s] English:** to be closed source, yes, it's limited.  
**Translation:** 

**[2792.00s] English:** So that's why, for example, I moved to LGPL.  
**Translation:** 

**[2793.94s] English:** The second reason is a bit more obscure, is that the terms of condition of the app store,  
**Translation:** 

**[2800.96s] English:** the Apple app store for iOS makes it very complex to have GPL application on it, while  
**Translation:** Vocabulary: obscure: 不明显

**[2806.70s] English:** it's easier to have LGPL applications on it.  
**Translation:** 

**[2809.46s] English:** So VLC on Windows and on Mac and on Linux is GPL, the core is LGPL, but on iOS, the  
**Translation:** 

**[2817.78s] English:** iPhone version and the Apple TV version, it's GPL.  
**Translation:** 

**[2819.50s] English:** And the iPhone version is a type of different license called the MPL.  
**Translation:** 

**[2824.02s] English:** And yes, I went and changed the license and it was a long story.  
**Translation:** 

**[2828.00s] English:** Yeah.  
**Translation:** 

**[2829.00s] English:** So I think basically to change the license, you have to contact all the contributors.  
**Translation:** 

**[2832.74s] English:** Yes.  
**Translation:** Vocabulary: contributors: 贡献者

**[2833.74s] English:** It's very important to understand that open source projects are what we call in the US  
**Translation:** 

**[2838.68s] English:** copyright law, joint work, or in civil law, collective works or collaborative works, is  
**Translation:** Vocabulary: collaborative: 合作创作

**[2845.98s] English:** that you work all together in terms of the same goal.  
**Translation:** 

**[2849.02s] English:** And then it creates one software, which is one release.  
**Translation:** 

**[2852.52s] English:** But the copyright is kept by all the individuals.  
**Translation:** 

**[2856.42s] English:** Some open source projects don't do that, they force copyright assignment, but this is not  
**Translation:** 

**[2859.78s] English:** what we do with communities.  
**Translation:** 

**[2861.70s] English:** So everyone has basically copyright on what they changed.  
**Translation:** 

**[2865.94s] English:** And this copyright stays even if at the end your contribution was deleted because the  
**Translation:** 

**[2871.52s] English:** new contribution was based on your previous one, right?  
**Translation:** 

**[2874.58s] English:** So if you want to properly relicense, you need to find all the contributors.  
**Translation:** 

**[2878.26s] English:** Yeah.  
**Translation:** Vocabulary: relicense: 重新授权

**[2878.34s] English:** Yeah.  
**Translation:** 

**[2878.40s] English:** Yeah.  
**Translation:** 

**[2878.42s] English:** Yeah.  
**Translation:** 

**[2878.46s] English:** Yeah.  
**Translation:** 

**[2878.48s] English:** Yeah.  
**Translation:** 

**[2878.50s] English:** Yeah.  
**Translation:** 

**[2878.52s] English:** Yeah.  
**Translation:** 

**[2878.56s] English:** Yeah.  
**Translation:** 

**[2878.58s] English:** Yeah.  
**Translation:** 

**[2878.62s] English:** Yeah.  
**Translation:** 

**[2878.64s] English:** Yeah.  
**Translation:** 

**[2878.68s] English:** Yeah.  
**Translation:** 

**[2878.72s] English:** Yeah.  
**Translation:** 

**[2878.74s] English:** Yeah.  
**Translation:** 

**[2878.80s] English:** Yeah.  
**Translation:** 

**[2878.88s] English:** Yeah.  
**Translation:** 

**[2879.02s] English:** Yeah.  
**Translation:** 

**[2879.12s] English:** Yeah.  
**Translation:** 

**[2879.62s] English:** Yeah.  
**Translation:** 

**[2879.76s] English:** Yeah.  
**Translation:** 

**[2879.78s] English:** Yeah.  
**Translation:** 

**[2880.00s] English:** contact more than 350 people and sometimes well they are just an email right so it's you need to  
**Translation:** 

**[2886.18s] English:** actually track down i actually like travel to some place to go somewhere that i was like sorry  
**Translation:** 

**[2891.78s] English:** that i found online to see how to go to their job and say well you licensed that can you do you want  
**Translation:** 

**[2898.84s] English:** to change from gpl to lgpl most of the times they don't even care they wanted to help vlt but also  
**Translation:** 

**[2904.16s] English:** it brought me to very complex situation i arrived to the work of a person who was a factory worker  
**Translation:** 

**[2910.04s] English:** and i said well i need to you to sign that because it was his son who died who actually  
**Translation:** 

**[2918.74s] English:** wrote the code right so i had to explain all those type of open source meaning and no i was  
**Translation:** 

**[2924.68s] English:** not a company trying to rip out the two lines or five lines that that guy did but was useful and  
**Translation:** 

**[2930.32s] English:** the whole community agreed on that and he had no idea i was a  
**Translation:** 

**[2934.14s] English:** factory worker this and i was a lot younger right like it was 14 years ago and like like i was  
**Translation:** 

**[2941.36s] English:** almost in tears right it's we very difficult right we are talking about life of people and he  
**Translation:** 

**[2945.40s] English:** explaining and we went to talk about the photo of this guy right so it's important to do it right  
**Translation:** 

**[2951.68s] English:** and to do it correctly um but yes that means tracking down everything because every contribution  
**Translation:** 

**[2957.34s] English:** works there are some projects who don't respect that and we do relicensing a bit like aggressively  
**Translation:** 

**[2963.14s] English:** but as a  
**Translation:** Vocabulary: aggressively: 猛烈地; relicensing: 重新授权

**[2964.14s] English:** said it destroyed the heart of the community because it's we only agree on this on this  
**Translation:** 

**[2969.10s] English:** license so that's important i would emphasize the community is such a wide-ranging group of people  
**Translation:** 

**[2975.06s] English:** there's people in the syrian war zone with electricity part-time there's there's all  
**Translation:** 

**[2982.80s] English:** people from all walks of life rich poor young old um so it's quite remarkable to get you know a  
**Translation:** Vocabulary: syrian: 叙利亚人

**[2991.20s] English:** group of people aligned on something and that's an achievement in itself yeah it's incredible and  
**Translation:** 

**[2996.94s] English:** a lot of them are introverts so you  
**Translation:** Vocabulary: aligned: 齐心协力; introverts: 内向人士

**[3000.00s] English:** Coming to find them and getting them and getting them to answer an email might be quite difficult.  
**Translation:** 

**[3005.40s] English:** Most of us are introverts, right?  
**Translation:** 

**[3007.08s] English:** You need to be more precise.  
**Translation:** 

**[3008.64s] English:** You are extremely introverts, extremely, extremely introverts and introverts, right?  
**Translation:** 

**[3012.64s] English:** It's just like a whole spectrum of different people.  
**Translation:** 

**[3015.28s] English:** It doesn't matter.  
**Translation:** 

**[3016.62s] English:** The important is, is your code good?  
**Translation:** 

**[3019.34s] English:** Is your code great?  
**Translation:** 

**[3020.68s] English:** Is your technology great?  
**Translation:** 

**[3021.82s] English:** We care about excellent code.  
**Translation:** 

**[3023.84s] English:** We don't care who you are.  
**Translation:** 

**[3025.46s] English:** Sorry, it's just like we have no idea to check.  
**Translation:** 

**[3027.78s] English:** We cannot check, right?  
**Translation:** 

**[3028.90s] English:** Like maybe you're a dog.  
**Translation:** 

**[3030.62s] English:** I don't care, right?  
**Translation:** 

**[3031.86s] English:** I don't care where you come from.  
**Translation:** 

**[3033.36s] English:** I need to look at your code.  
**Translation:** 

**[3035.02s] English:** And this is important because people don't understand that.  
**Translation:** 

**[3037.90s] English:** And they come to the community and send them some patches and they get rejected.  
**Translation:** 

**[3042.34s] English:** And they don't like that because, I mean, you're just like, sorry, it's not up to our standards.  
**Translation:** 

**[3047.50s] English:** Oh, yeah, but I'm an engineer at this very large company in Italy, in Germany, in the US.  
**Translation:** 

**[3052.78s] English:** We don't care.  
**Translation:** 

**[3053.90s] English:** We care about the quality of your code because this is what defines our community.  
**Translation:** 

**[3058.90s] English:** And which means that we have a lot of people who contribute who are some very different backgrounds and very introverts.  
**Translation:** 

**[3065.88s] English:** Sure, but that's okay, right?  
**Translation:** 

**[3067.62s] English:** So one of the legends of the community is, of course, Linus Torvalds, who created Linux and is a longtime maintainer of the Linux kernel.  
**Translation:** Vocabulary: kernel: 内核; longtime: 长期; maintainer: 维护者

**[3079.06s] English:** As the legend goes, he can be pretty harsh on this meritocratic process of reviewing the code and saying it's not good enough.  
**Translation:** 

**[3085.38s] English:** Can you just speak to the legend of Linus Torvalds?  
**Translation:** Vocabulary: meritocratic: 功绩至上的

**[3088.90s] English:** Well, Linus is one of a kind, right?  
**Translation:** 

**[3092.64s] English:** And I would even go and say that what he did on Git is more interesting than what he did on the Linux kernel.  
**Translation:** 

**[3099.56s] English:** He's very harsh, but what people don't see is usually when he's harsh, too, it's people who are maintainers of part of the kernel, right?  
**Translation:** 

**[3108.04s] English:** So they know him, right?  
**Translation:** Vocabulary: maintainers: 代码维护者

**[3109.50s] English:** So he's not very harsh like that to everyone.  
**Translation:** 

**[3112.02s] English:** The thing is, what he created in his room is basically powering every server online, right?  
**Translation:** 

**[3118.42s] English:** Even.  
**Translation:** 

**[3118.90s] English:** At Microsoft Cloud.  
**Translation:** 

**[3120.56s] English:** Yeah.  
**Translation:** 

**[3120.00s] English:** called Azure. I'm quite sure 70-80% of the servers are running Linux. All your Android phones are  
**Translation:** 

**[3126.34s] English:** running Linux. What he did with the power of a boot source, sure, is amazing. And yes, the quality  
**Translation:** 

**[3135.20s] English:** of the Linux kernel is very high. And yes, it's difficult. But we cannot compromise on that. We  
**Translation:** Vocabulary: cannot: 不能

**[3142.56s] English:** cannot compromise on quality. Because in the end, and you have to understand that, the core community  
**Translation:** 

**[3148.70s] English:** of VLC is five people. The core community of FFmpeg is 10 to 15. And we are the ones who are  
**Translation:** 

**[3156.14s] English:** going to maintain your code, right? Because 1,000 contributors in the timeline and just 10 things,  
**Translation:** 

**[3161.74s] English:** 1% chance that someone comes and stays. 1%. So you will have change of job, change of wife,  
**Translation:** Vocabulary: contributors: 贡献者

**[3169.52s] English:** you have children, you have accident in life, you're going to change jobs, whatever. You're  
**Translation:** 

**[3173.66s] English:** not going to come back. It's most likely. So we are the ones going to  
**Translation:** 

**[3178.64s] English:** maintain your code.  
**Translation:** 

**[3178.70s] English:** It needs to be maintainable. It needs to be excellent. And yes, sometimes that means that  
**Translation:** Vocabulary: maintainable: 易于维护的

**[3186.62s] English:** you need to rework your work because it was good, but it's not excellent. And we need excellence  
**Translation:** 

**[3190.96s] English:** because we have very few to maintain something that is critical for the whole.  
**Translation:** 

**[3195.80s] English:** But we should also mention that there's some spiciness, some harshness to the language  
**Translation:** 

**[3200.06s] English:** that's sometimes used when you're keeping this high bar of excellence.  
**Translation:** Vocabulary: harshness: 辛辣性; spiciness: 尖锐性

**[3205.80s] English:** Is there something to say to that?  
**Translation:** 

**[3207.12s] English:** It's true, right?  
**Translation:** 

**[3208.70s] English:** It's also the fact that, for example, what we're doing is low level. It's extremely technical.  
**Translation:** 

**[3213.66s] English:** You get into this community. The tone gets very like a type of, it's a subculture, right? So people  
**Translation:** Vocabulary: subculture: 亚文化

**[3221.52s] English:** who arrive from the external are basically not known to the subculture. Most of those people  
**Translation:** 

**[3227.42s] English:** around FFmpeg and VLC, we do VideoLand Dev Days, VDD every year. They are so fun in real life and  
**Translation:** 

**[3234.20s] English:** they love it. But it's true that you're online and sometimes like the tone, you don't know how to do it.  
**Translation:** 

**[3238.68s] English:** You don't realize how it is.  
**Translation:** 

**[3240.00s] English:** But that's okay.  
**Translation:** 

**[3241.16s] English:** It's a culture.  
**Translation:** 

**[3241.90s] English:** I mean, you get this in the gaming culture.  
**Translation:** 

**[3243.80s] English:** There's pretty harsh and tense the way people communicate.  
**Translation:** 

**[3247.36s] English:** And everyone understands that the way you show love and respect just looks different in different communities.  
**Translation:** 

**[3253.12s] English:** Sometimes people, it depends.  
**Translation:** 

**[3255.44s] English:** If it's a book club, usually people are going to be much sweeter.  
**Translation:** 

**[3258.62s] English:** If it's an open source project that's very high stakes and used by millions of people.  
**Translation:** 

**[3264.66s] English:** But it's very not often insults that you see, for example, in the gaming, right?  
**Translation:** 

**[3269.38s] English:** And so Linus' tone is a bit unusual, even for the open source community.  
**Translation:** 

**[3273.82s] English:** It's more like, it's more harsh on the result saying, no, this is not good.  
**Translation:** 

**[3277.50s] English:** This is crap.  
**Translation:** 

**[3278.30s] English:** Those type of things that you will see.  
**Translation:** 

**[3280.34s] English:** Try not to make it about the person, make it about the code.  
**Translation:** 

**[3282.64s] English:** Yes.  
**Translation:** 

**[3283.14s] English:** It's very matter of fact.  
**Translation:** 

**[3284.58s] English:** And I think you've got to look at it in terms of, you know, the famous FFmpeg is developed almost entirely by volunteers.  
**Translation:** 

**[3290.02s] English:** And that's true.  
**Translation:** 

**[3290.78s] English:** And you've got to imagine someone's on a hard day's work at their day job.  
**Translation:** 

**[3294.26s] English:** They come home.  
**Translation:** 

**[3296.34s] English:** You know, terseness might be a thing, you know.  
**Translation:** 

**[3298.22s] English:** And that's not.  
**Translation:** Vocabulary: terseness: 言简意赅

**[3299.38s] English:** That's not something to take personally.  
**Translation:** 

**[3301.82s] English:** You're tired, you're busy, but you still care about this open source stuff.  
**Translation:** 

**[3305.62s] English:** But you may not be able to explain and handhold someone on every subtle detail.  
**Translation:** 

**[3310.28s] English:** And also, you have to realize that most people don't speak English as a native language.  
**Translation:** Vocabulary: handhold: 扶持

**[3317.00s] English:** And this is especially for open source projects like FFmpeg and VLC, which are mostly sent out of Europe.  
**Translation:** 

**[3323.62s] English:** Sometimes, like, people who are from the U.S.  
**Translation:** 

**[3327.88s] English:** or just like...  
**Translation:** 

**[3329.38s] English:** are very not happy about the tone.  
**Translation:** 

**[3331.48s] English:** But most of the time, it's also like they don't know better, right?  
**Translation:** 

**[3334.36s] English:** It's difficult.  
**Translation:** 

**[3334.96s] English:** The language is English is a difficult language.  
**Translation:** 

**[3337.00s] English:** There is so many subtleties and tone and so on that you don't have, right?  
**Translation:** Vocabulary: subtleties: 细微差别

**[3340.48s] English:** So often, it's also difficult in those type of community about like different cultures and languages.  
**Translation:** 

**[3346.32s] English:** So as the legend goes, JB, you repeatedly turned down millions of dollars to keep VLC open source free for everyone without ads.  
**Translation:** 

**[3359.38s] English:** So as the legend goes, JB, you repeatedly turned down millions of dollars to keep VLC open source free for everyone without ads.  
**Translation:** 

**[3360.00s] English:** So take me through the reasoning behind that decision of leaving millions of dollars on the table.  
**Translation:** 

**[3366.44s] English:** Yeah, that's like almost a meme, right, on Reddit?  
**Translation:** 

**[3369.24s] English:** There literally is a meme on Reddit.  
**Translation:** 

**[3371.64s] English:** 9gog and, yeah, yeah, I see there's you looking like a wizard in the VLC hat on Reddit.  
**Translation:** 

**[3380.30s] English:** This is JB, the creator of VLC Media Player.  
**Translation:** 

**[3383.72s] English:** He refused tens of millions of dollars in order to keep VLC hats free.  
**Translation:** 

**[3387.76s] English:** Thanks, Jean-Baptiste Kampf.  
**Translation:** 

**[3391.48s] English:** You can even summon him on Reddit.  
**Translation:** 

**[3393.62s] English:** Yeah, and usually, if you see, right, it's usually like people tag me, right, and then there is me.  
**Translation:** Vocabulary: summon: 召唤

**[3398.66s] English:** And then I say, good morning, I got 24k upvotes, which is great, right?  
**Translation:** 

**[3402.38s] English:** My karma on Reddit is amazing, at least on that account.  
**Translation:** Vocabulary: karma: 积分

**[3406.84s] English:** So the question needs to be answered first.  
**Translation:** 

**[3410.48s] English:** What is the story about VLC, right?  
**Translation:** 

**[3414.16s] English:** Because, yes, this is true.  
**Translation:** 

**[3415.74s] English:** I refuse dozens of millions.  
**Translation:** 

**[3417.88s] English:** Millions of dollars.  
**Translation:** 

**[3419.04s] English:** Yes, several times.  
**Translation:** 

**[3420.12s] English:** Yes, I could be a multimillionaire and be somewhere on the beach.  
**Translation:** 

**[3423.62s] English:** But I did not do it because I thought it was not moral and it was not the right thing to do.  
**Translation:** Vocabulary: multimillionaire: 亿万富翁

**[3429.64s] English:** And this is very important for myself is to be like I work for the greater good.  
**Translation:** 

**[3435.40s] English:** I work for people and I don't want it's not just by myself.  
**Translation:** 

**[3439.42s] English:** But the reason is also because I did not feel that I'm completely legitimate to do that.  
**Translation:** 

**[3444.72s] English:** And let me explain you why.  
**Translation:** 

**[3446.36s] English:** VLC story is a very weird.  
**Translation:** 

**[3447.76s] English:** Weird story.  
**Translation:** 

**[3449.08s] English:** In France, we have university and we have a type of top colleges and those top of excellency schools are engineering school, business schools and basically lawyers and medical.  
**Translation:** 

**[3462.84s] English:** Right.  
**Translation:** 

**[3463.06s] English:** But they're outside of university.  
**Translation:** 

**[3464.88s] English:** And in order to enter those, you spend two years working like crazy mass physics to enter those best engineering school.  
**Translation:** 

**[3472.86s] English:** One of the school is called the Ecole Centrale Paris.  
**Translation:** 

**[3475.48s] English:** It has changed name since, but it was called the Ecole Centrale.  
**Translation:** Vocabulary: ecole: 中学

**[3477.76s] English:** Ecole Centrale Paris and because it was.  
**Translation:** 

**[3480.00s] English:** central they had to move it because it was too small after the world war ii and and they moved  
**Translation:** 

**[3485.04s] English:** it they wanted to move it to the central of france in a place called clermont ferrand and the alumni  
**Translation:** 

**[3490.32s] English:** decided that this was not okay right it is a the school that eiffel right the one who did the eiffel  
**Translation:** Vocabulary: alumni: 校友; clermont: 克勒蒙; eiffel: 埃菲尔; ferrand: 费朗

**[3496.48s] English:** tower attended to right so they said no no we are amazing great school we cannot do that and so they  
**Translation:** 

**[3501.40s] English:** bought a piece of land south of paris uh very near paris um and it was a campus managed by a non-profit  
**Translation:** Vocabulary: cannot: 不能

**[3509.34s] English:** of the alumnis okay because of that everything on the campus was managed by students the university  
**Translation:** 

**[3516.48s] English:** did nothing right so uh radio tv uh supermarket uh library um defining who was going into which  
**Translation:** 

**[3525.38s] English:** rooms um everything was managed by that's amazing that's an amazing experiment that it all didn't go  
**Translation:** 

**[3532.48s] English:** to hell quickly it somehow flourished it worked great and i learned so much in my life  
**Translation:** Vocabulary: flourished: 蓬勃发展

**[3539.34s] English:** doing those side activities right because you're you're 22 and you need to run your campus else you  
**Translation:** 

**[3543.98s] English:** don't have electricity right so you care about that right but anyway in the 80s and they did  
**Translation:** 

**[3549.60s] English:** a full experiment of deploying a network mostly sponsored by ibm and 3com which was a token ring  
**Translation:** 

**[3556.34s] English:** network so token ring is something that probably almost no one knows about anymore it's a networking  
**Translation:** Vocabulary: deploying: 部署; token: 令牌

**[3563.66s] English:** technology where you don't have routers right everyone is linked um it's like  
**Translation:** 

**[3569.34s] English:** really a ring and when you want to send a message you talk to your neighbor who's going to put the  
**Translation:** Vocabulary: routers: 路由器

**[3573.90s] English:** message to the next one who's going to put the things to the next one in terms of ring the issue  
**Translation:** 

**[3579.48s] English:** with token ring is of course is that it's very slow because every computer on the network needs  
**Translation:** 

**[3584.94s] English:** to open the message see if it's okay is it for me no it's not and then send it back like a token  
**Translation:** 

**[3590.58s] English:** which is traveling around the ring in the 80s you're doing some telnet and sending mails as  
**Translation:** 

**[3597.48s] English:** university that's okay right  
**Translation:** 

**[3599.34s] English:** but starts  
**Translation:** 

**[3600.00s] English:** the 90s and the 90s um and start video games and when you have high latency video games basically  
**Translation:** 

**[3606.50s] English:** you die right so in 1994 1995 around doom and nukem coming around they want a faster network  
**Translation:** Vocabulary: latency: 网络延迟

**[3613.06s] English:** so the students go and see the university and say you know what we want a faster network we need to  
**Translation:** 

**[3618.60s] English:** work you should also play video games um and the university tells them that basically oh i'm sorry  
**Translation:** 

**[3625.12s] English:** we cannot help you because you understand the campus is not ours you manage it so do something  
**Translation:** 

**[3632.04s] English:** and you should see some basically partners of the university and basically go away and they go  
**Translation:** Vocabulary: cannot: 不能

**[3638.64s] English:** and they actually go and see um the the the cio of uh buig which is a large uh french company  
**Translation:** 

**[3645.24s] English:** and who's doing some tvs in france and he says well you know what the future of video is satellite  
**Translation:** 

**[3651.84s] English:** well today we know it's not but at least it was a good idea  
**Translation:** 

**[3655.12s] English:** in 1995 the first of satellite dish and he says that instead of having like one satellite dish  
**Translation:** 

**[3661.38s] English:** and a big decoder for each of the students which are 1500 what about you build like you put an  
**Translation:** 

**[3668.90s] English:** enormous dish and only one decoder and you send the video directly  
**Translation:** 

**[3673.38s] English:** on the network and that required a very fast network today it's obvious but at the time was  
**Translation:** 

**[3680.00s] English:** like the first to do video streaming so they built this project which was called network to  
**Translation:** 

**[3685.06s] English:** tell you what the future of video streaming is and they built this project which was called  
**Translation:** 

**[3685.10s] English:** to tell you what the future of video streaming is and they built this project which was called  
**Translation:** 

**[3685.12s] English:** 2000 of course we're in the 90s right everything is futuristic is called 2000 2000 yeah and so they  
**Translation:** 

**[3692.66s] English:** do the network 2000 project it's completely hacked it crashes after 45 seconds that's okay the demo  
**Translation:** Vocabulary: futuristic: 未来主义; hacked: 被黑客攻击

**[3698.90s] English:** is 40 seconds it's leaks memory that's okay they put 64 megabytes of ram instead of the 8 or 16 you  
**Translation:** 

**[3704.96s] English:** have and the demo should have stopped there and that was a network 2000 project by the students  
**Translation:** Vocabulary: megabytes: 兆字节

**[3709.54s] English:** what was the format of the video that they had to work with mpeg-2 because satellite is mpeg-2  
**Translation:** 

**[3714.10s] English:** ts for translation and it's a network 2000 project and it's completely hacked it crashes after 45  
**Translation:** 

**[3715.10s] English:** seconds but you've been able to reach a second network that's called mpeg-2 so far i'll show you  
**Translation:** 

**[3720.00s] English:** The project should have stopped there.  
**Translation:** 

**[3721.50s] English:** Everyone was happy.  
**Translation:** 

**[3722.50s] English:** They had like amazing ATM network at 155 megabits per second.  
**Translation:** 

**[3727.82s] English:** They had probably one of the best networks in Europe at that time.  
**Translation:** 

**[3731.12s] English:** And they stopped the project.  
**Translation:** 

**[3732.20s] English:** Six months or a year later, two students arrive and say, well, you know what?  
**Translation:** 

**[3736.62s] English:** Maybe other people care about video streamed on a local network.  
**Translation:** Vocabulary: streamed: 直播

**[3740.22s] English:** And they create the VideoLan project, VideoLan.  
**Translation:** 

**[3744.14s] English:** And one of them is called Christophe Mathieu.  
**Translation:** 

**[3746.50s] English:** That is a good friend of both Kieran and me.  
**Translation:** 

**[3748.64s] English:** And they start the project.  
**Translation:** 

**[3750.62s] English:** It's not even open source yet.  
**Translation:** 

**[3752.86s] English:** And they spend around three years to get the school to agree to make it open source.  
**Translation:** 

**[3758.12s] English:** Because the university wanted to get, because of the IP and copyright of the students,  
**Translation:** 

**[3763.34s] English:** wanted to basically monetize these MPEG-2 decoders.  
**Translation:** Vocabulary: decoders: 解码器; monetize: 变现

**[3767.12s] English:** Just to be clear, so what's the main application streaming on a local network?  
**Translation:** 

**[3770.88s] English:** It was streaming on a local network.  
**Translation:** 

**[3772.52s] English:** By the way, that's just like to state the obvious.  
**Translation:** 

**[3774.68s] English:** This is before YouTube.  
**Translation:** 

**[3775.90s] English:** This is before...  
**Translation:** 

**[3776.64s] English:** This is 10 years before YouTube.  
**Translation:** 

**[3777.54s] English:** You have a Pentium 6.  
**Translation:** 

**[3778.78s] English:** You have a Pentium 60 or 75, right?  
**Translation:** 

**[3780.76s] English:** The main machine was 4886DX at 33 megahertz, right?  
**Translation:** 

**[3784.54s] English:** Bear in mind, television was the main form of video at the time.  
**Translation:** 

**[3788.18s] English:** You could get new channels.  
**Translation:** 

**[3789.22s] English:** In the 90s, having even one new channel when you grew up with four channels,  
**Translation:** 

**[3793.04s] English:** having a fifth or a sixth was a big deal.  
**Translation:** 

**[3795.16s] English:** And so having this satellite service with, you know, dozens, even hundreds of channels was so groundbreaking.  
**Translation:** Vocabulary: groundbreaking: 划时代

**[3801.90s] English:** Especially because this is a university where you had a ton of different nationalities, right?  
**Translation:** 

**[3806.00s] English:** So there was a ton of people who wanted...  
**Translation:** 

**[3808.64s] English:** So in the end, they had like several dishes on different type of satellite, right?  
**Translation:** 

**[3812.18s] English:** Because, for example, a lot of people were coming from the Maghreb or the Middle East.  
**Translation:** Vocabulary: maghreb: 北非地区

**[3816.14s] English:** And so they went to different type of satellites.  
**Translation:** 

**[3820.78s] English:** Anyway, the solution worked great.  
**Translation:** 

**[3823.40s] English:** And they started the VideoLand project.  
**Translation:** 

**[3825.64s] English:** The VideoLand project has several and some are completely crazy solutions.  
**Translation:** 

**[3830.02s] English:** Like one, how to create multicast on a unicast network.  
**Translation:** 

**[3834.38s] English:** But let's not come to that.  
**Translation:** Vocabulary: multicast: 组播

**[3835.74s] English:** It's too complex.  
**Translation:** 

**[3837.30s] English:** But VideoLand client...  
**Translation:** 

**[3838.64s] English:** The client part is...  
**Translation:** 

**[3840.00s] English:** became vlc actually they basically strong-armed the the university to force it to open source  
**Translation:** 

**[3846.96s] English:** because university did not understand that and in 2001 it's still early but basically yes the  
**Translation:** 

**[3852.48s] English:** university agreed early 2001 to make it open source i joined the project in 2003 because  
**Translation:** 

**[3858.56s] English:** that's when i joined the university so the first thing is i'm not the one who created vlc because  
**Translation:** 

**[3864.48s] English:** actually no one did right just kind of naturally emerged from the video land project and we should  
**Translation:** 

**[3869.12s] English:** mention that like again you you said it just but to make it clear video land as what it became was  
**Translation:** 

**[3876.80s] English:** at the time is a set of technologies around video the vlc what you called the client that's the  
**Translation:** 

**[3883.04s] English:** thing that most normies uh that is correct and think of like as the thing which is like the thing  
**Translation:** 

**[3890.32s] English:** that pops up when you click on video and you play it so i arrive in 2003 and then i will create the  
**Translation:** 

**[3897.28s] English:** open source um  
**Translation:** 

**[3899.12s] English:** non-profit organization called video land and i took everything out of the university to create it  
**Translation:** 

**[3904.24s] English:** in a non-profit project and some six sustainable it's yes it's true that i spent more time than  
**Translation:** 

**[3910.00s] English:** anyone on vlc and video land that is sure um but it's a continuity of a previous project video land  
**Translation:** Vocabulary: continuity: 连续性

**[3917.12s] English:** the student project which is a community of the network 2000 project which is a continuity of that  
**Translation:** 

**[3922.16s] English:** inside i'm sure there's moments along the way there you were thinking like what is the future  
**Translation:** 

**[3929.12s] English:** of vlc so i think this is a part of the project and i'll tell you what it is um i think that one  
**Translation:** 

**[3934.00s] English:** aspect that i had an issue with was that we couldn't create such a beauty and i think it  
**Translation:** 

**[3938.24s] English:** was the project itself was the reason it ran so well so i think that one aspect has been  
**Translation:** 

**[3941.52s] English:** changed and i think that part of the reason i was able to use vlc or video land is because  
**Translation:** 

**[3946.16s] English:** i think that was the thing that i was able to be able to use with vlc um and that was part of the  
**Translation:** 

**[3949.92s] English:** reason that vlc was built into video land but the second one the second one i had to experiment with  
**Translation:** 

**[3953.12s] English:** i was able to process that and that was kind of the answer to the question of how can i give people  
**Translation:** 

**[3957.12s] English:** better ideas of how to do a better video land project i have to solve all the problems and i'm still  
**Translation:** 

**[3959.02s] English:** My, my, my.  
**Translation:** 

**[3960.00s] English:** life and my time. And I made that to grow from a few hundreds of thousands of users, millions of  
**Translation:** 

**[3966.90s] English:** users to what we have now, which is probably billions of versions of VLC around the world  
**Translation:** 

**[3972.70s] English:** and used everywhere. So that's a bit the story of VLC. There is a ton of very funny stories around  
**Translation:** 

**[3979.82s] English:** that. Many people from around the world working on it, like you said, in Syria or middle of nowhere  
**Translation:** 

**[3986.32s] English:** in India. But along the way, I got several offers which were either to bundle toolbars, right? You  
**Translation:** Vocabulary: bundle: 捆绑软件; toolbars: 工具栏

**[3994.36s] English:** remember those horrible toolbars, which are basically spyware or changing your web browser  
**Translation:** 

**[4000.08s] English:** or your search engine or even like advertisement inside VLC. And I didn't like that, right?  
**Translation:** 

**[4007.42s] English:** And people don't understand that I'm not against money, right? I'm very happy to make money.  
**Translation:** 

**[4013.30s] English:** I created several startups and one.  
**Translation:** Vocabulary: startups: 创业公司

**[4015.82s] English:** I hope that is going to work very well. It's the fact that I believe that you need to win money  
**Translation:** 

**[4022.32s] English:** ethically. There is the right way of doing that. And doing sneaky advertisement or stealing data  
**Translation:** Vocabulary: ethically: 合乎道德地

**[4028.26s] English:** is not the correct way, right? For example, if Netflix arrived at some point and say, well,  
**Translation:** 

**[4032.92s] English:** we want to put Netflix inside VLC, probably the story would have been different, right? But they  
**Translation:** 

**[4037.56s] English:** didn't. The only people who came to us were shady ads company. And if I do that, right, I would have  
**Translation:** 

**[4044.00s] English:** a ton of money, right? And then  
**Translation:** Vocabulary: shady: 可疑的

**[4045.82s] English:** three years later, the project is gone, right? Someone forks it and something else happens.  
**Translation:** 

**[4051.76s] English:** So it's not even necessarily ads or any of that. It's the shadiness of the dishonesty of the...  
**Translation:** Vocabulary: dishonesty: 不诚实; shadiness: 可疑

**[4057.24s] English:** So you had a good radar, you had a good threshold of like, no, this compromises the spirit of what  
**Translation:** 

**[4064.32s] English:** this is supposed to represent.  
**Translation:** Vocabulary: compromises: 损害; threshold: 门槛

**[4065.84s] English:** But also it's for me, right? I'm like very selfishly, I need to go to bed at night and be  
**Translation:** 

**[4071.68s] English:** happy about what I've done, right? Maybe it's my upbringing.  
**Translation:** Vocabulary: upbringing: 教育背景

**[4075.82s] English:** Maybe it's my parents' fault or whatever, right? But I believe there is...  
**Translation:** 

**[4080.00s] English:** right and wrong right and this was the right decision at the time it still is i want to be  
**Translation:** 

**[4086.40s] English:** proud of what i've been doing and like if i had sold out i would have betrayed so many other  
**Translation:** 

**[4093.20s] English:** people working yeah well i should say me and uh mostly internet thank you for that decision  
**Translation:** Vocabulary: betrayed: 背叛

**[4099.52s] English:** it's inspiring uh for others uh i think that um that are pushing open source movement forward  
**Translation:** 

**[4107.28s] English:** that it's okay to do these kinds of huge sacrifices if you believe it's right and i  
**Translation:** 

**[4114.34s] English:** think in that case it was right and it was the reason that vlc became as successful as it was  
**Translation:** 

**[4118.14s] English:** because it it's an embodiment it's a symbol of like you know freedom and what the open source  
**Translation:** Vocabulary: embodiment: 体现

**[4125.00s] English:** community can create yeah and be a service for so many people around the world and this is important  
**Translation:** 

**[4130.08s] English:** we should emphasize in the 2000s it was really normal to download a program and it secretly  
**Translation:** 

**[4134.62s] English:** installed some spyware yeah it was it was very  
**Translation:** 

**[4137.28s] English:** in very faint text or in the license text box that nobody reads that at the bottom oh i will  
**Translation:** 

**[4143.46s] English:** be installing this toolbar and changing all these things and it was it was very common to have to  
**Translation:** 

**[4147.64s] English:** you know you install a program to do something at the time of any sort to put yourself in the  
**Translation:** 

**[4152.32s] English:** mind of a developer at that time i think it's very easy to everybody listening to this it's  
**Translation:** 

**[4158.34s] English:** very easy at that time to convince yourself to take a few thousand dollars a few thousand dollars  
**Translation:** 

**[4165.04s] English:** to do it to to say  
**Translation:** 

**[4167.16s] English:** yeah  
**Translation:** 

**[4167.28s] English:** to much more money takes guts and takes vision the last offer i had was obscene  
**Translation:** 

**[4177.16s] English:** and they say yeah but imagine with all that money you could build something new open source right  
**Translation:** Vocabulary: obscene: 荒谬的

**[4183.54s] English:** it was like the mind trick was it was difficult but for me it was just like no this doesn't work  
**Translation:** 

**[4190.30s] English:** like that or this is not the right thing so i don't do it and again right it's not that i don't  
**Translation:** 

**[4196.12s] English:** like money or  
**Translation:** 

**[4197.16s] English:** or whatever it's just like it wasn't right  
**Translation:** 

**[4200.72s] English:** Well, once again, thank you from me and from the rest of the Internet.  
**Translation:** 

**[4204.84s] English:** Let me talk a little bit more about the open source movement,  
**Translation:** 

**[4207.88s] English:** about the fact that, as you say, over and over and over and over,  
**Translation:** 

**[4211.74s] English:** FFMPEG and many open source projects are built by volunteers.  
**Translation:** 

**[4217.60s] English:** So there's a bit of drama recently, Karen, on the interwebs, on Twitter.  
**Translation:** 

**[4224.10s] English:** You have a spicy style on Twitter that I think articulates  
**Translation:** Vocabulary: articulates: 表达; interwebs: 互联网

**[4229.56s] English:** and celebrates all the incredible developers and development  
**Translation:** 

**[4233.12s] English:** and the code, especially assembly, that's involved in building some of these codecs  
**Translation:** 

**[4239.38s] English:** and building some of this incredible technology.  
**Translation:** 

**[4241.60s] English:** But that brings us to a bit of a debacle that happened.  
**Translation:** Vocabulary: debacle: 灾难性失败

**[4245.26s] English:** Tell me the full saga of what happened with the Google security engineers.  
**Translation:** 

**[4250.18s] English:** Just to be clear, Google are one of the biggest supporters of open source out there.  
**Translation:** 

**[4254.12s] English:** They have been for a long time.  
**Translation:** 

**[4255.74s] English:** It's just, I think, some things kind of went a bit overboard this time.  
**Translation:** Vocabulary: overboard: 太过分了

**[4260.18s] English:** So FFMPEG itself, and this is not like a secret, it's on the homepage,  
**Translation:** 

**[4264.40s] English:** it processes untrusted data.  
**Translation:** Vocabulary: untrusted: 不可信

**[4267.86s] English:** There can be security issues when you pass untrusted data.  
**Translation:** 

**[4270.42s] English:** That's very normal.  
**Translation:** 

**[4271.48s] English:** But recently what changed was Google started using AI to create security reports  
**Translation:** 

**[4275.60s] English:** on an open source project, FFMPEG.  
**Translation:** 

**[4279.04s] English:** Volunteers had to deal with that.  
**Translation:** 

**[4281.14s] English:** They provided very limited funding,  
**Translation:** 

**[4282.92s] English:** and they even went to the media first announcing how good their AI was  
**Translation:** 

**[4286.70s] English:** before the issues could be fixed.  
**Translation:** 

**[4289.54s] English:** And this is in the public forum.  
**Translation:** 

**[4291.48s] English:** Yeah.  
**Translation:** 

**[4291.92s] English:** So reporting an issue, using AI to find an issue in the code,  
**Translation:** 

**[4295.70s] English:** which is a security vulnerability,  
**Translation:** Vocabulary: vulnerability: 安全漏洞

**[4297.90s] English:** and then reporting that publicly before you're able to fix it.  
**Translation:** 

**[4300.48s] English:** Yeah.  
**Translation:** 

**[4300.90s] English:** It's announcing how good their AI is.  
**Translation:** 

**[4303.06s] English:** They provided a standard 90-day industry deadline  
**Translation:** 

**[4308.74s] English:** without really understanding the nature of volunteer-driven development.  
**Translation:** 

**[4312.92s] English:** In addition, this vulnerability was on an obscure 1990s game codec.  
**Translation:** Vocabulary: obscure: 冷门

**[4320.00s] English:** the way and let's look at it from their standpoint to begin with let's um you know  
**Translation:** 

**[4324.82s] English:** yeah can you steal me on their case yeah sure they have substantial resources working on the  
**Translation:** Vocabulary: standpoint: 立场

**[4329.18s] English:** security of open source projects that you know are ubiquitous and they've used you know a lot  
**Translation:** 

**[4335.16s] English:** of compute to do that and very expensive and very capable security researchers um to do that and  
**Translation:** Vocabulary: ubiquitous: 无处不在

**[4340.78s] English:** that's their viewpoint is they are contributing by doing that but i think that's where  
**Translation:** 

**[4346.18s] English:** their opinions differ um it opened up a lot of interesting fishes i would say um  
**Translation:** 

**[4354.98s] English:** it does seem that there's a portion of the security community that um look at themselves  
**Translation:** 

**[4361.68s] English:** a bit like building architects that never have to go to site you know going to site is something  
**Translation:** 

**[4366.48s] English:** that is a little bit beneath them the actual day-to-day construction they're there to do  
**Translation:** 

**[4370.66s] English:** security things and it's someone else's problem the security industry also kind of has  
**Translation:** 

**[4376.08s] English:** a very aggressive tone towards things the language they use is extremely aggressive  
**Translation:** 

**[4381.84s] English:** they use very strong language like you will get popped and to Joe Public get popped you know it  
**Translation:** 

**[4388.12s] English:** means something quite bad for them it means to get hacked the way I would look at it personally  
**Translation:** 

**[4392.86s] English:** is a little bit like the padlock on your home not everyone that padlock on your home or you know  
**Translation:** Vocabulary: hacked: 被黑客攻击; padlock: 门锁

**[4400.40s] English:** the lock on your home is there to to protect against the capabilities of of what it's there  
**Translation:** 

**[4407.56s] English:** to protect it's not there to protect nuclear secrets it's not there to protect Fort Knox and  
**Translation:** 

**[4412.62s] English:** it could be looked at that they're using AI at a level of scale to go and pick those locks and  
**Translation:** 

**[4419.24s] English:** then say hey your locks your locks not secure you need to deal with this whereas actually they're  
**Translation:** 

**[4424.44s] English:** the ones with resources to be able to fix this but that seems to not be  
**Translation:** 

**[4430.38s] English:** something either they'll contribute to in terms of patches or in terms of financially and if the  
**Translation:** Vocabulary: financially: 经济上

**[4435.40s] English:** scale of AI is kind of the issue that the the bug reports are very wordy  
**Translation:** 

**[4440.00s] English:** They're very, very, it's almost a denial of service  
**Translation:** Vocabulary: wordy: 啰嗦

**[4442.84s] English:** by AI-generated bug reports on very niche codecs.  
**Translation:** 

**[4447.78s] English:** And the other issue the security community has  
**Translation:** Vocabulary: niche: 细分市场

**[4449.88s] English:** is everything is marked high priority.  
**Translation:** 

**[4452.10s] English:** You're going to, you know,  
**Translation:** 

**[4453.16s] English:** this is the most important thing in the world,  
**Translation:** 

**[4454.58s] English:** and you need to deal with this.  
**Translation:** 

**[4455.66s] English:** High, high, high, vulnerable, scary, scary, scary  
**Translation:** 

**[4457.58s] English:** on a game codec used on one disk in 1993.  
**Translation:** 

**[4463.32s] English:** Yeah.  
**Translation:** 

**[4464.08s] English:** And that's where the dichotomy lies.  
**Translation:** Vocabulary: dichotomy: 对立面

**[4466.60s] English:** Going around telling everyone that their padlocks  
**Translation:** 

**[4469.46s] English:** are not safe, well, that's a hobby project of somebody.  
**Translation:** 

**[4473.30s] English:** The safety of that codec is consummate  
**Translation:** 

**[4475.86s] English:** to what that person thinks.  
**Translation:** Vocabulary: consummate: 完美的

**[4477.62s] English:** It's their hobby.  
**Translation:** 

**[4478.22s] English:** It's good that they're security analyzing it,  
**Translation:** 

**[4479.88s] English:** but it doesn't need a big, scary warning.  
**Translation:** 

**[4481.96s] English:** This is a critical vulnerability.  
**Translation:** 

**[4484.34s] English:** You may recently also see that there was another  
**Translation:** 

**[4488.30s] English:** quote-unquote vulnerability.  
**Translation:** Vocabulary: vulnerability: 安全漏洞

**[4489.96s] English:** It wasn't a Google in this case,  
**Translation:** 

**[4491.36s] English:** but a filter could overflow and have an integer overflow,  
**Translation:** Vocabulary: integer: 整数; overflow: 溢出

**[4496.46s] English:** and one of your pixels could be the wrong color.  
**Translation:** 

**[4499.46s] English:** And this was marked high, 7.5 severity in red.  
**Translation:** Vocabulary: pixels: 像素; severity: 严重程度

**[4505.58s] English:** And at some point, the security industry needs to realize  
**Translation:** 

**[4508.22s] English:** you can't keep crying wolf like this,  
**Translation:** 

**[4510.02s] English:** because this just leads to people, you know,  
**Translation:** 

**[4511.68s] English:** the equivalent thereof of putting password stickers on their PC.  
**Translation:** Vocabulary: thereof: 其中的

**[4515.60s] English:** You know, you can't just keep crying wolf every day.  
**Translation:** 

**[4517.62s] English:** And I appreciate, you know, that's their modus operandi  
**Translation:** Vocabulary: operandi: 惯用法

**[4520.94s] English:** is to create as much scared and fear.  
**Translation:** 

**[4524.30s] English:** But from the Google standpoint, at the end of the day, they need  
**Translation:** Vocabulary: standpoint: 立场

**[4529.34s] English:** to contribute either financially or with patches.  
**Translation:** 

**[4532.52s] English:** Google uses FFmpeg, and a scale probably you or I  
**Translation:** 

**[4535.88s] English:** couldn't even contemplate, millions of CPU cores.  
**Translation:** 

**[4540.32s] English:** And yes, they contribute in areas mostly regarding their own products.  
**Translation:** Vocabulary: contemplate: 考虑

**[4544.28s] English:** So VP9, AV1, but in a wider sense, there's a disproportionate  
**Translation:** 

**[4552.02s] English:** level of contribution.  
**Translation:** Vocabulary: disproportionate: 不相称

**[4552.86s] English:** Yes, they fund students.  
**Translation:** 

**[4554.14s] English:** Yes, they fund Summer of Code.  
**Translation:** 

**[4557.30s] English:** And I think, so Alex Strange is a,  
**Translation:** 

**[4559.34s] English:** former FFmpeg,  
**Translation:** 

**[4560.00s] English:** fake developer. I think posting in a personal capacity. So he posted about security engineers  
**Translation:** 

**[4565.92s] English:** on Hacker News. His post reads, the problem with security reports in general is security people  
**Translation:** Vocabulary: hacker: 黑客

**[4572.74s] English:** are rampant self-promoters. Linus once called them something worse. Imagine you're a humble  
**Translation:** 

**[4581.02s] English:** volunteer open source developer. If a security researcher finds a bug in your code, they're  
**Translation:** 

**[4588.34s] English:** going to make up a cute name for it, start a website with a logo. Google is going to give  
**Translation:** 

**[4594.30s] English:** them a million dollar bounty. They're going to go to DEF CON and get a prize. And I assume  
**Translation:** Vocabulary: bounty: 奖金

**[4600.18s] English:** some kind of secret security people orgy where everyone is dressed like they're in the matrix.  
**Translation:** 

**[4607.58s] English:** Nobody's going to do any of this for you when you fix it.  
**Translation:** Vocabulary: matrix: 仿真世界

**[4614.34s] English:** Basically commenting on the sort of the incentives.  
**Translation:** 

**[4617.24s] English:** For the different people involved, they're misaligned.  
**Translation:** Vocabulary: commenting: 评论; incentives: 激励; misaligned: 不一致

**[4621.72s] English:** The problem here is a disproportion of means on discovery compared to patching it, right?  
**Translation:** 

**[4630.20s] English:** And this is the biggest issue, right? And after that debacle, Google did some changes.  
**Translation:** Vocabulary: debacle: 灾难; disproportion: 失衡; patching: 打补丁

**[4635.26s] English:** They are now starting to send patches, which is...  
**Translation:** 

**[4637.22s] English:** And they also now have reward tools for fixing issues. So it has changed a bit because of that  
**Translation:** 

**[4643.16s] English:** debacle. So it's good, right? But we've seen, and we talk about Google,  
**Translation:** 

**[4647.24s] English:** but we have seen like some other large companies saying, oh, you need to fix this bug because it's  
**Translation:** 

**[4652.60s] English:** critical in our product. Can you explain the XZ fiasco? The FFmpeg tweet reads,  
**Translation:** 

**[4659.80s] English:** the XZ fiasco has shown how a dependence on unpaid volunteers can cause major problems.  
**Translation:** Vocabulary: fiasco: 灾难性失败

**[4666.86s] English:** Trillion dollar corporations expect free and urgent support from volunteers. Microsoft teams posted  
**Translation:** 

**[4674.82s] English:** on a bug tracker full of...  
**Translation:** Vocabulary: trillion: 万亿

**[4677.24s] English:** ...volunteers that their issue is hype.  
**Translation:** 

**[4680.00s] English:** priority. After politely requesting a support contract from Microsoft for long-term maintenance,  
**Translation:** 

**[4686.28s] English:** they offered a one-time payment of a few thousand dollars instead. This is unacceptable. We didn't  
**Translation:** 

**[4692.24s] English:** make it up. This is what Microsoft teams actually did. And then you give the image and the details  
**Translation:** Vocabulary: unacceptable: 无法接受

**[4698.58s] English:** and all that kind of stuff, showing that these trillion dollar companies are not giving much  
**Translation:** 

**[4703.14s] English:** money, not giving much support. They think an open source project is a traditional vendor that  
**Translation:** 

**[4707.76s] English:** they have an SLA. They think a public bug tracker is actually a third-party vendor's  
**Translation:** 

**[4713.84s] English:** Jira where you can do all of these things. It's not. It's there to report bugs. I think the thing  
**Translation:** 

**[4719.32s] English:** that made this particularly heinous was the name dropping of Microsoft, the name dropping that this  
**Translation:** 

**[4724.60s] English:** is a visible product. If this was just a general bug report, I think that would have made it a lot  
**Translation:** Vocabulary: heinous: 罪大恶极

**[4730.76s] English:** better. Yeah, so they literally said like, this is a big deal because a lot of people are using it  
**Translation:** 

**[4736.64s] English:** in Microsoft.  
**Translation:** 

**[4737.76s] English:** I wonder what happens psychologically. So I think what happens in these companies,  
**Translation:** 

**[4742.60s] English:** maybe you can correct me, is they, you're right, they just think of FFmpeg as like a vendor  
**Translation:** Vocabulary: psychologically: 心理上

**[4749.40s] English:** that Microsoft surely is paying a huge amount of money to. They kind of assume that in their  
**Translation:** 

**[4757.02s] English:** interaction and nobody anywhere on the stack is going like, wait a minute, shouldn't we be giving  
**Translation:** 

**[4763.14s] English:** millions of dollars to FFmpeg? And this is a very big problem in  
**Translation:** 

**[4766.98s] English:** large companies.  
**Translation:** 

**[4767.92s] English:** Like we're talking about some companies, but it's the same everywhere, right? A lot of those  
**Translation:** 

**[4773.08s] English:** companies, like when we talked to that person, right, he was just like a manager on one project  
**Translation:** 

**[4779.42s] English:** in Microsoft Teams, right? He had like never really discussed with open source community. He  
**Translation:** 

**[4785.00s] English:** had no idea, right? It was like, and, but the problem is that usually there is what we call  
**Translation:** 

**[4791.06s] English:** OSPOS, right? Open source program offices in those type of companies. And they are the ones who are  
**Translation:** 

**[4796.44s] English:** supposed to discuss with open source. And they are the ones who are supposed to discuss with open  
**Translation:** 

**[4797.72s] English:** source. And they are the ones who are supposed to discuss with open source.  
**Translation:** 

**[4797.76s] English:** And I think that that is the whole point of having open source vendors.  
**Translation:** 

**[4800.00s] English:** open source communities but like they often don't explain that correctly internally right and here  
**Translation:** 

**[4806.24s] English:** is just like we are not your supplier if you want me to be a supplier i'm very happy right i will  
**Translation:** Vocabulary: internally: 内部; supplier: 供应商

**[4813.12s] English:** send you a contract and slas like i created five companies who are doing that around open source  
**Translation:** 

**[4818.48s] English:** projects so that's okay we should say that some some of the spicy tweets that karen you're behind  
**Translation:** Vocabulary: tweets: 推特

**[4824.24s] English:** and some of the debacle produce results positive results donations have increased substantially  
**Translation:** 

**[4832.32s] English:** they're still not enough to cover even a single full-time developer but  
**Translation:** Vocabulary: debacle: 灾难性失败

**[4836.48s] English:** on both a you know awareness level and a technical level there's substantially more technical  
**Translation:** 

**[4842.48s] English:** awareness and sort of awareness of the importance of ffmpeg as a result as a result of x and and  
**Translation:** 

**[4848.56s] English:** what's happened i can say you know it it solved its purpose people realize the level of the  
**Translation:** 

**[4854.16s] English:** level of the level of the level of the level of the level of the level of the level of the level of  
**Translation:** 

**[4854.22s] English:** importance ffmpeg has and on video it's the same right like for example a very simple example for  
**Translation:** 

**[4861.32s] English:** more than a year we couldn't update vlc on android because of a bug on the play store on android play  
**Translation:** 

**[4868.92s] English:** store right the only way we got someone to answer was to put a very spicy as you say um tweet saying  
**Translation:** 

**[4877.92s] English:** that we were going to stop distributing vlc for android right and we have around 100 million  
**Translation:** 

**[4884.14s] English:** people using that um and now then someone from android actually came and discussed to us right  
**Translation:** 

**[4891.34s] English:** um we had the same issue with with microsoft or like saying that we were going to stop distributing  
**Translation:** 

**[4897.98s] English:** vlc on the windows store and unfortunately we are so small that the only very strong power we have  
**Translation:** 

**[4906.22s] English:** to solve those issues is blaming on social network because it's nobles and now they listen to us but  
**Translation:** 

**[4913.66s] English:** so  
**Translation:** 

**[4914.06s] English:** large companies often have difficulty talking to us like for example vlc  
**Translation:** 

**[4920.00s] English:** is probably one of the top 10 software used on windows i am not part of microsoft isv  
**Translation:** 

**[4928.08s] English:** programs right i don't have a point of contact at microsoft right well i'm sure any other software  
**Translation:** 

**[4934.54s] English:** adobe spotify has a point of contact i don't have that right so raising awareness works it's  
**Translation:** 

**[4942.68s] English:** sometimes very spicy a lot of drama well x and twitter are okay for that but it's efficient  
**Translation:** 

**[4949.08s] English:** uh so everybody listening to this should go uh follow ffmpeg on twitter on x follow video land  
**Translation:** 

**[4959.32s] English:** on twitter on x uh go donate donate to ffmpeg thank you lex over the years several years you've  
**Translation:** 

**[4967.88s] English:** been a supporter of you know ffmpeg and video land on x you know giving us shout outs appreciating  
**Translation:** 

**[4974.30s] English:** you know what we do ffmpeg for life and for example like um team sweden  
**Translation:** 

**[4979.06s] English:** carmark and a few others like very high level people have raised also the awareness on on our  
**Translation:** 

**[4985.78s] English:** x accounts and that helped a lot also carpathy yeah i mean also you know outside of the fact  
**Translation:** 

**[4994.06s] English:** that so many people use it it's so impactful on the world it's also a great representation of a  
**Translation:** 

**[4999.12s] English:** great open source project like the value of assembly and c and making sure that like you take  
**Translation:** 

**[5009.06s] English:** real world systems it's not just that we'll talk about assembly later i'm sure that's its whole  
**Translation:** 

**[5013.64s] English:** topic in itself but it's also celebrating people like andreas reinhart who do maintenance it's i  
**Translation:** 

**[5020.50s] English:** believe unpaid i believe as a volunteer he's doing massive refactorings uh andreas reinhart and anton  
**Translation:** 

**[5026.56s] English:** kern of rewriting ffmpeg.c with threading celebrating those guys celebrating the untold  
**Translation:** Vocabulary: andreas: 安德烈; anton: 安东; refactorings: 重构; reinhart: 雷哈特; rewriting: 重写; threading: 线程

**[5032.72s] English:** labor that's gone into this that actually doesn't change anything from the user standpoint the files  
**Translation:** 

**[5039.06s] English:** don't change anything it's just that it's it's it's it's it's it's it's it's it's it's it's it's it's it's  
**Translation:** Vocabulary: standpoint: 用户视角

**[5040.00s] English:** wow, the airplane has been rebuilt whilst it's in the air.  
**Translation:** 

**[5043.58s] English:** Christian Garcia said,  
**Translation:** 

**[5044.50s] English:** as a teenager running this account,  
**Translation:** 

**[5046.26s] English:** referring to the FFmpeg account,  
**Translation:** 

**[5048.08s] English:** and you responded,  
**Translation:** 

**[5048.92s] English:** teenagers have written more assembly in FFmpeg  
**Translation:** 

**[5052.38s] English:** than Google engineers,  
**Translation:** 

**[5054.40s] English:** but also just pointing out  
**Translation:** 

**[5056.72s] English:** that there's a lot of incredible contributors  
**Translation:** 

**[5058.34s] English:** who are teenagers.  
**Translation:** Vocabulary: contributors: 贡献者

**[5059.70s] English:** Like JB said,  
**Translation:** 

**[5061.08s] English:** we don't care who you are,  
**Translation:** 

**[5062.22s] English:** where you're from,  
**Translation:** 

**[5063.16s] English:** what you do.  
**Translation:** 

**[5064.70s] English:** Teenagers have written thousands of lines of assembly  
**Translation:** 

**[5068.24s] English:** over the years.  
**Translation:** 

**[5070.66s] English:** Give a shout out back in the days to Daniel Kang.  
**Translation:** 

**[5073.78s] English:** So also highlighting the work of people like Rukai Peng,  
**Translation:** Vocabulary: highlighting: 突出显示

**[5076.18s] English:** this is a 16-year-old,  
**Translation:** 

**[5077.30s] English:** some of his first contributions to FFmpeg,  
**Translation:** 

**[5080.64s] English:** actually doing and putting some of these  
**Translation:** 

**[5082.54s] English:** quote-unquote security researchers to shame  
**Translation:** 

**[5084.44s] English:** by actually finding issues and fixing them  
**Translation:** 

**[5087.48s] English:** and being 16.  
**Translation:** 

**[5089.56s] English:** There's no barriers.  
**Translation:** 

**[5090.32s] English:** There's no barriers to you have to study at college  
**Translation:** Vocabulary: barriers: 障碍

**[5092.74s] English:** under this person and understand these.  
**Translation:** 

**[5094.62s] English:** If you can learn C,  
**Translation:** 

**[5096.44s] English:** and let's be honest,  
**Translation:** 

**[5097.14s] English:** it's from the K&R book,  
**Translation:** 

**[5099.42s] English:** learn C,  
**Translation:** 

**[5100.84s] English:** you can learn assembly.  
**Translation:** 

**[5101.78s] English:** We'll talk about that maybe a bit later.  
**Translation:** 

**[5103.72s] English:** You can contribute to world-class technologies.  
**Translation:** 

**[5106.42s] English:** In VLC,  
**Translation:** 

**[5107.88s] English:** one of the oldest contributors is called Felix.  
**Translation:** Vocabulary: felix: 菲利克斯

**[5111.18s] English:** He's the one doing everything on Mac and iOS.  
**Translation:** 

**[5113.84s] English:** He's starting working on VLC.  
**Translation:** 

**[5115.42s] English:** He was 16.  
**Translation:** 

**[5116.78s] English:** We had a guy called Edward Wong,  
**Translation:** 

**[5119.52s] English:** who used to be a Google Summer of Code student  
**Translation:** 

**[5121.94s] English:** who stayed for three years around VideoLan.  
**Translation:** 

**[5124.90s] English:** He was 14, right?  
**Translation:** 

**[5126.72s] English:** And part of Google Summer of Code  
**Translation:** 

**[5129.08s] English:** and Google Coding,  
**Translation:** 

**[5130.00s] English:** which were programs where basically we have students  
**Translation:** 

**[5132.90s] English:** or high school.  
**Translation:** 

**[5134.22s] English:** We wrote a ton of assembly for x264  
**Translation:** 

**[5137.02s] English:** and for VLC and for FFmpeg, right?  
**Translation:** 

**[5139.58s] English:** So everyone can contribute.  
**Translation:** 

**[5141.52s] English:** And he also did a good job  
**Translation:** 

**[5142.32s] English:** because he didn't play the alarmist CVE heist,  
**Translation:** Vocabulary: heist: 抢劫

**[5146.14s] English:** create a CVE,  
**Translation:** 

**[5147.30s] English:** which is like a public exposure of security  
**Translation:** 

**[5150.44s] English:** and do these big, scary, red 7.5 priority.  
**Translation:** 

**[5155.50s] English:** He just fixed an issue in Git after three days  
**Translation:** 

**[5157.86s] English:** and just fixed it.  
**Translation:** 

**[5159.08s] English:** He didn't need to,  
**Translation:** 

**[5160.10s] English:** he was good, he was great.  
**Translation:** 

**[5161.22s] English:** We had all these players  
**Translation:** 

**[5162.54s] English:** and he was a good man.  
**Translation:** 

**[5163.88s] English:** And it was just the first thing  
**Translation:** 

**[5165.96s] English:** that made me look at Google  
**Translation:** 

**[5166.92s] English:** and like, oh my God,  
**Translation:** 

**[5167.68s] English:** I'm in this game.  
**Translation:** 

**[5168.48s] English:** It was really easy working on IT.  
**Translation:** 

**[5169.82s] English:** I was like, oh, I am going to do this.  
**Translation:** 

**[5171.12s] English:** I think it's going to be great.  
**Translation:** 

**[5172.34s] English:** I think it's going to be a big success.  
**Translation:** 

**[5173.82s] English:** Now it's been a really hard process  
**Translation:** 

**[5175.34s] English:** in my life.  
**Translation:** 

**[5176.14s] English:** I think I got really bad at it.  
**Translation:** 

**[5177.08s] English:** I think I am going to go places  
**Translation:** 

**[5177.56s] English:** that I should go.  
**Translation:** 

**[5180.90s] English:** I know I figured it out,  
**Translation:** 

**[5182.32s] English:** but I am going to go to the end.  
**Translation:** 

**[5183.92s] English:** I don't think it's going to work,  
**Translation:** 

**[5184.88s] English:** but I've been working for so long  
**Translation:** 

**[5186.52s] English:** and I'm going to try.  
**Translation:** 

**[5188.18s] English:** It's going to be somewhat of an issue,  
**Translation:** 

**[5160.00s] English:** go and play a big security drama about it and i think i posted you know the kids are all right  
**Translation:** 

**[5164.58s] English:** whereas there's there's there's you know there is a i'm not saying all security people do this but  
**Translation:** 

**[5169.76s] English:** there is a portion of the security community as alex said that likes to hype themselves up by  
**Translation:** 

**[5174.52s] English:** creating drama they would have happily raised this is a high priority cve 8.0 or whatever on a  
**Translation:** 

**[5181.38s] English:** on an issue that actually was in git it wasn't even in a release it was in development and three  
**Translation:** 

**[5186.24s] English:** days later was fixed well i just want to put a little bit of love out there even to the bigger  
**Translation:** 

**[5191.78s] English:** community uh much love and respect to google engineers like you said they're uh uh some of  
**Translation:** 

**[5200.04s] English:** the the best software engineers in the world they do contribute a lot even on the security front  
**Translation:** 

**[5204.32s] English:** and also you know i'm a big fan of theo much love to theo he was part of this  
**Translation:** 

**[5209.48s] English:** debacle and drama a little bit i think when you just zoom out  
**Translation:** Vocabulary: debacle: 灾难性失败

**[5213.76s] English:** on the grand rs  
**Translation:** 

**[5216.24s] English:** arc of human history the drama contributed positively to everybody involved donations went  
**Translation:** 

**[5221.30s] English:** up it brought more attention to the topic allowed uh everybody to bicker in a way that ultimately  
**Translation:** 

**[5228.66s] English:** got them to figure out whatever fan peg is all about so the way the way we looked at this is  
**Translation:** Vocabulary: bicker: 争吵

**[5233.46s] English:** like it's a rap battle at the end of the day nobody did it we say stuff we say stuff yeah  
**Translation:** 

**[5239.26s] English:** but we can we can leave it on the x is a perfect place for you know international rap battle  
**Translation:** 

**[5243.74s] English:** you say stuff i say stuff about your mama but  
**Translation:** 

**[5246.24s] English:** doesn't mean you know i have an actual personal issue with her yeah and that's what it looks like  
**Translation:** 

**[5250.74s] English:** the theo situation you know jb can maybe expand went a little bit too far and there was a little  
**Translation:** 

**[5254.78s] English:** but you know it's just a bit of fun it's just a bit of rap battle it's a bit it's wwe you know  
**Translation:** 

**[5260.82s] English:** everyone's having a bit of fun on x it doesn't need to be taken seriously you know the teenagers  
**Translation:** 

**[5265.98s] English:** thing you know that so that that guy was a google employee say hey you know there are other ways to  
**Translation:** 

**[5270.64s] English:** run an open source business you know go and just have a bit of fun you know that's what the point  
**Translation:** 

**[5276.24s] English:** and furthermore if you can teach people about the ways of  
**Translation:** 

**[5280.00s] English:** open source projects, assembly, et cetera, by doing that, I think there's a lot to be offered  
**Translation:** 

**[5283.88s] English:** here. It's not dunking on people for dunking sake. It's showing actually the story that I  
**Translation:** Vocabulary: cetera: 等等; dunking: 羞辱

**[5288.74s] English:** think X learned is these are not big corporate open source projects. This is not Kubernetes  
**Translation:** 

**[5292.62s] English:** where there's, you know, hundreds, maybe thousands of people paid to develop this stuff. These are  
**Translation:** Vocabulary: kubernetes: 容器编排系统

**[5297.32s] English:** just people in their basements in their spare time. And if you can address that topic in a fun  
**Translation:** 

**[5301.98s] English:** and entertaining way, I think that that that's the good thing. And that's, that's the value of X  
**Translation:** Vocabulary: basements: 地下室

**[5307.34s] English:** and in the reach we have. And to be honest, right, like, even on Google, Google is  
**Translation:** 

**[5312.72s] English:** one entity, but so many different people, right? And some, and there is a ton of Google engineer  
**Translation:** 

**[5319.48s] English:** we work with all the time. And even like Google from YouTube to Chrome, to Chrome media, to the  
**Translation:** 

**[5327.34s] English:** rest of Google, those are very different type of entities. But what we do is efficient. And for  
**Translation:** 

**[5332.96s] English:** example, for Theo, right, it went a bit too far. I had him, like, I call him,  
**Translation:** 

**[5337.34s] English:** everyone down, I had him on the phone, we say, okay, like, this goes too far, and so on. But in  
**Translation:** 

**[5342.86s] English:** the end, yeah, it's a hard battle, but it's positive for the project. It's like the awareness  
**Translation:** 

**[5348.20s] English:** we have on open source. And I mean, true open source from communities, right? Not is increased  
**Translation:** 

**[5355.22s] English:** dramatically in the last two years. And this is useful.  
**Translation:** 

**[5359.08s] English:** What do you think motivates all the incredible contributors that we've been talking about? Like,  
**Translation:** Vocabulary: contributors: 贡献者; dramatically: 大幅度地; motivates: 激励

**[5363.82s] English:** what's the engine? It's so interesting to see. Like you said, they're sitting  
**Translation:** 

**[5367.32s] English:** in the basement, what's the driver? What's the engine there?  
**Translation:** 

**[5369.44s] English:** There are many drivers. But weirdly, the main one is that what we do in multimedia plays videos,  
**Translation:** 

**[5376.90s] English:** and video is cool, right? And, and, for example, we have so many people in the community who arrive  
**Translation:** Vocabulary: multimedia: 多种媒体

**[5383.56s] English:** because they loved watching anime, right? And this is like the advice when people ask me,  
**Translation:** 

**[5389.68s] English:** what should I work on in open source? How do I start? And my question, my answer is always the  
**Translation:** Vocabulary: anime: 动画

**[5393.96s] English:** same. Work on something you love. I,  
**Translation:** 

**[5397.32s] English:** I'm working on VLC because I love movies, right?  
**Translation:** 

**[5400.00s] English:** And I love watching the same movies over and over, even if my wife hates me when I do that, right?  
**Translation:** 

**[5405.40s] English:** But because it's interesting, right?  
**Translation:** 

**[5407.12s] English:** Because it's a topic that you like, right?  
**Translation:** 

**[5409.52s] English:** That's the first thing where people come to, usually, to VLC and FFmpeg.  
**Translation:** 

**[5413.94s] English:** The second thing is that, technically, because we search for excellence, this is the best school ever, right?  
**Translation:** 

**[5421.98s] English:** This is the best school ever of programming.  
**Translation:** 

**[5424.74s] English:** If you're good in C, in FFmpeg, if you know how to write assembly, I assure you, you're going to be one of the best programmers ever, even if you're working on writing TypeScript, because this is the most amazing thing to do.  
**Translation:** 

**[5438.96s] English:** And you will, like, have to get reviews by some of the most seasoned programmers ever who are going to look at every part of your code and tell you why it's not great.  
**Translation:** Vocabulary: programmers: 程序员

**[5449.40s] English:** It's like we are the best teachers that you've ever had in programming, right?  
**Translation:** 

**[5452.78s] English:** Andrew, Kelly started Zig.  
**Translation:** 

**[5454.32s] English:** He was an FFmpeg.  
**Translation:** 

**[5454.74s] English:** He was an FFmpeg developer and started Zig after his FFmpeg school.  
**Translation:** 

**[5458.56s] English:** I mean, it's the place to learn so many aspects of programming in the real world, in a thing used by billions of people.  
**Translation:** 

**[5466.42s] English:** You have nowhere to hide.  
**Translation:** 

**[5467.98s] English:** You have to be open and honest about your flaws and how you can learn and be better.  
**Translation:** 

**[5472.68s] English:** And what is also interesting in multimedia is that you have 16 milliseconds to display a frame.  
**Translation:** 

**[5479.20s] English:** It's not like a game engine where you can basically slow down and wait a frame.  
**Translation:** 

**[5483.58s] English:** Like, so it's you need to be good, right?  
**Translation:** 

**[5485.90s] English:** There is no choice else.  
**Translation:** 

**[5486.80s] English:** You don't have your video in and because of how codecs, if you miss a frame, you're going to destroy the look of the video, right?  
**Translation:** 

**[5493.34s] English:** So you need to be good.  
**Translation:** 

**[5495.32s] English:** You need to be perfect to have the right thing.  
**Translation:** 

**[5498.00s] English:** But also is that it's not just pure programming in the mathematical fence, right?  
**Translation:** 

**[5503.54s] English:** A lot of people don't understand.  
**Translation:** Vocabulary: mathematical: 数学的

**[5505.36s] English:** But in order to program correctly on the open source multimedia community, you need to understand how  
**Translation:** 

**[5512.68s] English:** computer works and and when you write assembly, you need to understand about CPU pipelining, right?  
**Translation:** Vocabulary: multimedia: 多媒体; pipelining: 流水线

**[5519.50s] English:** You need to understand.  
**Translation:** 

**[5520.00s] English:** how SIMD works, how the ALU works, right?  
**Translation:** 

**[5523.10s] English:** You need to understand how IO works, right?  
**Translation:** 

**[5525.84s] English:** And this is what I think that is missing  
**Translation:** 

**[5528.46s] English:** to a lot of engineers and software engineers today  
**Translation:** 

**[5530.76s] English:** is understanding what we call computer architecture.  
**Translation:** 

**[5534.74s] English:** And seriously, some of the debate is like,  
**Translation:** 

**[5537.18s] English:** should we use this assembly call or this one?  
**Translation:** 

**[5539.48s] English:** And people say, well, no, it's going to be  
**Translation:** 

**[5541.56s] English:** like three cycle on this type of CPU and this one  
**Translation:** 

**[5544.62s] English:** and has massive impact on the output, right?  
**Translation:** 

**[5547.56s] English:** We should expand.  
**Translation:** 

**[5548.16s] English:** And FFmpeg is probably one of the biggest CPU users  
**Translation:** 

**[5550.92s] English:** in the world.  
**Translation:** 

**[5551.56s] English:** It's probably running, as we speak,  
**Translation:** 

**[5555.32s] English:** easily a hundred, order of magnitude, a hundred million,  
**Translation:** 

**[5557.96s] English:** maybe even a billion CPUs as we speak.  
**Translation:** 

**[5560.46s] English:** So every instruction matters.  
**Translation:** 

**[5563.26s] English:** There's not, the impact, at least in terms of CPU,  
**Translation:** 

**[5567.94s] English:** is massive for everything that we do.  
**Translation:** 

**[5571.22s] English:** So first you come because it's an interesting subject,  
**Translation:** 

**[5574.04s] English:** then you stay because it's excellent.  
**Translation:** 

**[5575.98s] English:** And in the end, you're very proud  
**Translation:** 

**[5578.16s] English:** of it because it's on the end of everyone.  
**Translation:** 

**[5581.84s] English:** Like so many people like, oh, I'm working  
**Translation:** 

**[5584.76s] English:** for whatever consulting company  
**Translation:** 

**[5587.12s] English:** and I'm doing some portal to download invoices  
**Translation:** 

**[5592.08s] English:** for your PG&E.  
**Translation:** Vocabulary: invoices: 账单

**[5593.64s] English:** Wow, great.  
**Translation:** 

**[5594.66s] English:** Like so many jobs are like that.  
**Translation:** 

**[5596.96s] English:** You're not going to tell that to your grandma.  
**Translation:** 

**[5599.62s] English:** But if you go to see your grandma and say,  
**Translation:** 

**[5601.28s] English:** I do this so that you can play video on your laptop,  
**Translation:** 

**[5604.04s] English:** they understand.  
**Translation:** 

**[5604.72s] English:** And this is very important, right?  
**Translation:** 

**[5606.32s] English:** Because you're working on VLC, FFmpeg,  
**Translation:** 

**[5608.16s] English:** X264, it's in the end of hundreds of millions of people  
**Translation:** 

**[5611.98s] English:** and you have an impact.  
**Translation:** 

**[5613.76s] English:** And so you can be proud of yourself.  
**Translation:** 

**[5615.94s] English:** And so I think that in addition to doing a great resume,  
**Translation:** 

**[5619.46s] English:** all those things are why people contribute.  
**Translation:** 

**[5622.00s] English:** Yeah, those are side effects.  
**Translation:** 

**[5623.20s] English:** My favorite quote on this topic is John Collinson.  
**Translation:** 

**[5625.50s] English:** He said, the world is a museum of passion projects.  
**Translation:** Vocabulary: collinson: 科尔林森

**[5628.46s] English:** You know, everything out there is a passion project  
**Translation:** 

**[5630.96s] English:** and open source multimedia and open source in general,  
**Translation:** 

**[5634.34s] English:** you can just do that so much faster.  
**Translation:** 

**[5636.60s] English:** There's such a faster network.  
**Translation:** 

**[5637.90s] English:** In fact, you know, I can open.  
**Translation:** 

**[5640.00s] English:** in a cafe and that can be my passion project but i have to get building code i have to build a  
**Translation:** 

**[5643.54s] English:** building i have to find a find a location i have to do all the you know all sorts of things well  
**Translation:** 

**[5648.24s] English:** in the software world that passion project can be can move quickly it can be amplified  
**Translation:** Vocabulary: amplified: 放大

**[5653.34s] English:** by the network effect and that amplification can be more than the the sum of the sum of the parts  
**Translation:** 

**[5659.78s] English:** you know you can be you can find people interested in extremely obscure things and have a network  
**Translation:** Vocabulary: amplification: 放大效应

**[5667.54s] English:** effect and make something that is truly amazing and uh on that topic of passion projects uh tim  
**Translation:** 

**[5674.52s] English:** sweeney actually said in a reply to a tweet that was uh complimenting jb he said quote many things  
**Translation:** Vocabulary: complimenting: 称赞

**[5683.00s] English:** in the world only happen because an awesome person decides to do it this is the case with vlc and that  
**Translation:** 

**[5689.66s] English:** speaks to something interesting to me that does seem that a small number of people sometimes one  
**Translation:** 

**[5694.38s] English:** person can create  
**Translation:** 

**[5697.54s] English:** something incredible in the software world like you said this over and over and over i think  
**Translation:** 

**[5702.94s] English:** javascript is an incredible thing created by by uh initially a single person some of the  
**Translation:** 

**[5707.90s] English:** programming languages like python and c and java like this one person has this vision has the design  
**Translation:** 

**[5714.54s] English:** and brings it sometimes over a weekend is the initial spark yes linus built git in two weeks  
**Translation:** 

**[5721.50s] English:** wow yeah it changed the world kit i mean it really changed the world linus passion for hey  
**Translation:** 

**[5726.74s] English:** uploading the  
**Translation:** 

**[5727.54s] English:** starboard to an ftp like deal with it but for me it's not just in software right and i believe in  
**Translation:** Vocabulary: uploading: 上传

**[5734.02s] English:** in individuals that are going to change the world right and it's with a good as you said vision  
**Translation:** 

**[5739.54s] English:** right i want to do that um it is useful it will be useful and whether it's going to like build  
**Translation:** 

**[5745.78s] English:** train or cars or rockets or something like i believe people who believe in themselves and  
**Translation:** 

**[5751.86s] English:** have a vision can have a huge impact for humanity let's say actually  
**Translation:** 

**[5757.54s] English:** you already have a vision level  
**Translation:** 

**[5786.42s] English:** before we zoom back in we'll just keep  
**Translation:** 

**[5787.42s] English:** go  
**Translation:** 

**[5760.00s] English:** going up and down the stack so uh you know we've been talking back and forth vlc and ffmpeg  
**Translation:** 

**[5766.04s] English:** karen you said that ffmpeg and videoland vlc coexist and there's no central point of importance  
**Translation:** 

**[5774.34s] English:** it's a kind of what you call the binary star system yeah uh they succeed because of each other  
**Translation:** Vocabulary: binary: 双星系统; coexist: 共存; videoland: 视频陆

**[5780.66s] English:** can you explain the difference how they interact what is the are they competitors i don't i don't  
**Translation:** 

**[5786.74s] English:** think they're competitors i think i think the simple answer is the short answer before i go  
**Translation:** 

**[5791.04s] English:** into detail is vlc is to ffmpeg as android is to linux so they depend on each other but they  
**Translation:** 

**[5797.96s] English:** coexist because of each other so they are a binary star system is the analogy i used  
**Translation:** 

**[5802.28s] English:** by the way i feel horrible that i just recently learned that alpha centauri  
**Translation:** 

**[5807.48s] English:** the closest star system to us is a triple star system and and when you start doing the physics  
**Translation:** Vocabulary: alpha: 阿尔法; centauri: 半人马; triple: 三重的

**[5812.02s] English:** it's a nightmare right yeah but but like hence the three-body problem but anyway  
**Translation:** 

**[5816.74s] English:** so a lot of ffmpeg pipelines involve the x264 project which is a videoland project i would put  
**Translation:** Vocabulary: pipelines: 工作流程

**[5824.34s] English:** a finger in the air that's say 80 plus percent of those pipelines are dependent on a videoland  
**Translation:** 

**[5829.24s] English:** project vlc obviously we've discussed a videoland project uses ffmpeg gives it reach exposure to  
**Translation:** 

**[5837.52s] English:** weird files uh historically used some donation money to fund ffmpeg fmpeg development and we'll  
**Translation:** 

**[5843.78s] English:** talk a bit maybe about some of the reverse engineering later  
**Translation:** Vocabulary: donation: 捐赠; historically: 历史上

**[5846.74s] English:** so it's a binary star system they work and feed off each other many of the developers are shared  
**Translation:** 

**[5851.54s] English:** there's no central location it's a virtuous cycle working together and we should mention that x264  
**Translation:** Vocabulary: virtuous: 互利循环

**[5858.46s] English:** is the encoder for h264 video standard so h264 is the standard yes x264 is the implementation  
**Translation:** 

**[5866.88s] English:** open source implementation of the standards that's used by basically everybody for everything  
**Translation:** Vocabulary: implementation: 实现方式

**[5871.58s] English:** yeah so that is the main driver of this when you think of an mp4 file  
**Translation:** 

**[5876.74s] English:** it has h264 codec in it if it if it  
**Translation:** 

**[5880.00s] English:** If it came from a software environment, like a data center or somewhere, the chances are it was created with x264.  
**Translation:** 

**[5885.94s] English:** And that's under the flag of VideoLan.  
**Translation:** 

**[5889.30s] English:** That's a VideoLan project.  
**Translation:** 

**[5890.48s] English:** So in the VideoLan graphic, it sits in the VideoLan world.  
**Translation:** 

**[5893.64s] English:** And VideoLan has a bunch of stuff in it.  
**Translation:** 

**[5896.84s] English:** Go to the VideoLan website, there's a bunch of icons.  
**Translation:** 

**[5901.32s] English:** Like, if you look, there are so many libraries, right?  
**Translation:** 

**[5903.54s] English:** LibDVDCSS, LibDVDNav, LibDVDPSI, LibVLC, of course, VLC Unity, LibBluway.  
**Translation:** 

**[5917.94s] English:** Yeah.  
**Translation:** 

**[5918.78s] English:** And there is so many more, right?  
**Translation:** 

**[5920.36s] English:** Like, lately, the David project that we might talk about is the last project from VideoLan.  
**Translation:** 

**[5926.40s] English:** It's everywhere, right?  
**Translation:** 

**[5927.86s] English:** And we have a LibSpatialAudio lately that we announced.  
**Translation:** 

**[5931.36s] English:** CheckISM.  
**Translation:** 

**[5932.66s] English:** CheckISM.  
**Translation:** 

**[5933.44s] English:** CheckISM.  
**Translation:** 

**[5933.50s] English:** CheckISM.  
**Translation:** 

**[5933.52s] English:** CheckISM.  
**Translation:** 

**[5933.54s] English:** It's like an insane project, but amazing.  
**Translation:** 

**[5937.26s] English:** So, and x264 is one of those VideoLan projects.  
**Translation:** 

**[5940.86s] English:** And my opinion, for example, is that x264 was the most amazing encoder ever designed.  
**Translation:** 

**[5948.76s] English:** And this helped the adoption of FFmpeg.  
**Translation:** 

**[5951.60s] English:** A lot of people and large companies went through FFmpeg because they wanted to use x264.  
**Translation:** 

**[5957.30s] English:** And x264 increased the popularity on FFmpeg.  
**Translation:** 

**[5960.24s] English:** But also, VLC had its properties.  
**Translation:** 

**[5963.24s] English:** Popularity, because it's played so many files that were done by FFmpeg, right?  
**Translation:** 

**[5967.02s] English:** So, it's many projects that are interweaved and work together.  
**Translation:** 

**[5972.72s] English:** Yeah.  
**Translation:** Vocabulary: interweaved: 错综复杂的

**[5972.94s] English:** Unfortunately, there's a thing on X where VLC is mentioned and there's people.  
**Translation:** 

**[5977.38s] English:** A quick reminder that it's FFmpeg inside doing the actual work.  
**Translation:** 

**[5980.40s] English:** And that's, like I said, it's not, that's not the case.  
**Translation:** 

**[5984.56s] English:** We work together.  
**Translation:** 

**[5986.42s] English:** And to give you an idea, right?  
**Translation:** 

**[5987.76s] English:** When I compiled VLC for Windows, I compiled around 16 million lines of code.  
**Translation:** Vocabulary: compiled: 编译了

**[5992.96s] English:** Right?  
**Translation:** 

**[5993.82s] English:** One million of those are inside the VLC repository.  
**Translation:** Vocabulary: repository: 代码仓库

**[5997.64s] English:** And FFmpeg in total is probably two.  
**Translation:** 

**[6000.00s] English:** around two right but so it means that so many dependencies are outside and if you also look at  
**Translation:** 

**[6005.64s] English:** ffmpeg per se ffmpeg also is integrating third-party libraries like x264 butlib opus  
**Translation:** 

**[6012.08s] English:** and so many others right so we all depend on each other uh yeah that's why i was uh hoping to do  
**Translation:** Vocabulary: integrating: 整合

**[6017.74s] English:** this episode as we are doing they just uh kind of joins ffmpeg and vlc because it's really it's  
**Translation:** 

**[6024.24s] English:** really two two of the same like i said binary star system and we're all just orbiting it  
**Translation:** Vocabulary: binary: 双星系统; orbiting: 围绕

**[6029.42s] English:** uh can we give a shout out to some of the people along the way we didn't really quite talk about  
**Translation:** 

**[6035.06s] English:** the history of ffmpeg so uh maybe can you tell me about fabrice can you tell me about  
**Translation:** 

**[6042.20s] English:** michael nidermeyer can you tell me about some of the key figures here about the eras of fmpeg  
**Translation:** 

**[6047.92s] English:** because there's key eras and key people that made this possible uh fabrice ballard as you mentioned  
**Translation:** Vocabulary: ballard: 巴拉德

**[6055.52s] English:** creating the concept and then probably in the 2000s era i would call it the  
**Translation:** 

**[6059.42s] English:** era era's tool of fmpeg is that the 2000s era was michael nidermeyer so key things he got done  
**Translation:** Vocabulary: nidermeyer: 尼德迈耶

**[6067.14s] English:** was exhaustive support for divx and xvid at the time and all sorts of weird variants of what's  
**Translation:** 

**[6073.20s] English:** known as mpeg4 part 2 so this predates the mpeg4 part 10 that we used to so this was  
**Translation:** Vocabulary: exhaustive: 详尽; predates: 早于

**[6079.42s] English:** 2000s era video codecs where there were flavor after flavor of weird weird decoders  
**Translation:** 

**[6085.76s] English:** at the time in the 2000s you needed a new player to play the game and you needed a new player to  
**Translation:** Vocabulary: decoders: 解码器

**[6089.42s] English:** play every different type of file format so there was windows media player to play windows  
**Translation:** 

**[6093.38s] English:** media formats there was real player to play real media formats and those were the other the other  
**Translation:** 

**[6098.60s] English:** key thing in ffmpeg at the time were native decoders for those i actually do remember being  
**Translation:** 

**[6103.10s] English:** a teenager i must have been figuring out there was this one player that could play  
**Translation:** 

**[6108.60s] English:** could decode these files without having separate bloated players because at the time when you  
**Translation:** 

**[6114.18s] English:** downloaded real player there was a ton of other stuff in there a ton of ads a ton of other things  
**Translation:** Vocabulary: bloated: 体积大

**[6119.42s] English:** and so that was a huge hit for me and i'm looking forward to their release so that's that for now  
**Translation:** 

**[6124.66s] English:** i put a link to the logo in the description and i'll see you all in the future with the sari  
**Translation:** 

**[6129.10s] English:** if you enjoyed this video make sure you like it and hit the subscribe button and hit the bell for  
**Translation:** 

**[6132.44s] English:** all the latest updates we have from youtube i'm gregory peter and i hope you guys enjoyed the  
**Translation:** Vocabulary: subscribe: 订阅

**[6139.06s] English:** video and i'll see you in the next video peace out yall  
**Translation:** 

**[6120.00s] English:** that was fast led to that and then i think 2008 was a 2008 onwards  
**Translation:** Vocabulary: onwards: 往后

**[6126.16s] English:** was a big change because that's when h.264 got its maturity and i think something hopefully  
**Translation:** 

**[6134.80s] English:** we'll talk about a bit more this was the beginning of high definition video so h.264 was the key  
**Translation:** Vocabulary: maturity: 成熟

**[6140.80s] English:** decoder of that so i'd call that the late 2000 and 2010s and that's when the big reverse engineers  
**Translation:** 

**[6146.60s] English:** came along and really did astonishing work the beginning was a single player that could play  
**Translation:** Vocabulary: astonishing: 令人惊讶的

**[6152.84s] English:** xvid divx windows media and real player was already in a massive achievement in itself  
**Translation:** 

**[6158.54s] English:** without codec packs without weird stuff you had to download that had weird ads and weird spyware  
**Translation:** 

**[6163.58s] English:** vlc 1.0 was out on those times 2000 2009 2010 yeah and this is like where it exploded  
**Translation:** 

**[6172.38s] English:** yeah without codec packs it just works across all these  
**Translation:** Vocabulary: exploded: 迅速流行

**[6176.46s] English:** different platforms and it's just like it's like it's like it's like it's like it's like  
**Translation:** 

**[6176.58s] English:** it's like it's like it's like it's like it's like it's like it's like it's like it's like it's like  
**Translation:** 

**[6176.60s] English:** the fact so it's just like all the codec packs are ffmpeg inside vlc plus we have other modules  
**Translation:** 

**[6182.78s] English:** for all the type of at the time that wasn't is there were weird in the 2000s there were weird  
**Translation:** 

**[6187.62s] English:** codec packs with dlls coming from this place with spyware with you know what it wasn't reliable  
**Translation:** 

**[6193.88s] English:** you didn't know and having a single player that was open source or single playback module  
**Translation:** Vocabulary: module: 模块; playback: 播放

**[6198.36s] English:** slash player that could do this that was open source but i think the thing to emphasize is  
**Translation:** 

**[6203.24s] English:** this task in the 2000s that michael did was was  
**Translation:** 

**[6206.58s] English:** really the number of edge cases are poor beyond comprehension in terms of you could have a  
**Translation:** 

**[6213.54s] English:** chinese cctv system that did one weird variant of mpeg-4 part two was known as mpeg-4 asp and  
**Translation:** Vocabulary: comprehension: 理解能力

**[6220.42s] English:** that was a weird variant and you had to fix that without breaking everybody else  
**Translation:** 

**[6223.92s] English:** times a million so that's uh so you said that that's where a lot of the reverse engineering  
**Translation:** 

**[6228.62s] English:** was happening it started it started in the 2000s with the windows media stuff because  
**Translation:** 

**[6232.52s] English:** that was proprietary it started with the real media so with benjamin larson  
**Translation:** Vocabulary: proprietary: 专有技术

**[6236.58s] English:** kosciuszko that era those were the key that was the key  
**Translation:** 

**[6240.00s] English:** groundwork and then in in the 2010s was kind of the poor mahal kostya era building doing doing  
**Translation:** Vocabulary: groundwork: 基础工作; mahal: 玛哈勒

**[6247.60s] English:** some of the most difficult codecs jb maybe can talk about go to meeting four and go to meeting  
**Translation:** 

**[6252.26s] English:** five and what these are what's the good so so so like let's talk about this amazing ukrainian guy  
**Translation:** 

**[6260.26s] English:** called kostya who was at a time living in germany and who was in love with sweden right  
**Translation:** 

**[6268.54s] English:** and the guy was the most he's like like like a lot of the people in the community are very clever  
**Translation:** 

**[6277.12s] English:** he's one of those who are like borderline geniuses right he was able to reverse engineering extremely  
**Translation:** 

**[6283.86s] English:** complex codecs um and he does that and we do a bit of engineers with kieran but clearly not at  
**Translation:** Vocabulary: borderline: 边缘的; geniuses: 天才

**[6290.20s] English:** this level no no um he reverse engineered binary blobs which are 20 megabytes yeah so just for  
**Translation:** 

**[6297.04s] English:** reference uh  
**Translation:** Vocabulary: binary: 二进制; blobs: 数据块; megabytes: 兆字节

**[6298.54s] English:** one megabyte binary blob to reverse engineers probably order of magnitude a month of work and  
**Translation:** 

**[6303.64s] English:** this guy is doing 20 30 megabyte blobs maybe we'll talk about that in a minute about the  
**Translation:** Vocabulary: megabyte: 兆字节

**[6308.30s] English:** subtleties of how you do that but this guy is doing it for very difficult and very obscure codecs  
**Translation:** 

**[6312.92s] English:** and and did that for fun right and yeah and um so go to meeting uh was a big problem with vlc  
**Translation:** Vocabulary: obscure: 冷门; subtleties: 细微之处

**[6319.70s] English:** because that's what like the number half number one uh feature request for a long time so i put  
**Translation:** 

**[6325.00s] English:** a bounty and the guy at some point said okay jb  
**Translation:** Vocabulary: bounty: 悬赏

**[6328.54s] English:** i'm going to do it and in a matter of two months and then he explained how he did it he was just  
**Translation:** 

**[6334.12s] English:** like oh i looked at the code like this looked like a dct that i used to see on wmv and so on  
**Translation:** 

**[6340.10s] English:** he did that and the funniest part is that the code is written is a ton of jokes and there is  
**Translation:** 

**[6347.84s] English:** there is a ton of jb right my name and and kemp and kemp and kostia jokes inside the code the code  
**Translation:** 

**[6355.42s] English:** is beautiful right so one of these uh i'm going to do it in a matter of two months and then he  
**Translation:** 

**[6358.54s] English:** i want to comment is uh  
**Translation:** 

**[6360.00s] English:** I've gotten a chance to speak to some of the developers,  
**Translation:** 

**[6362.76s] English:** some of the assembly language level people,  
**Translation:** 

**[6366.14s] English:** and they all always make everything sound like it's kind of easy.  
**Translation:** 

**[6370.10s] English:** There's a kind of humility  
**Translation:** Vocabulary: humility: 谦逊

**[6371.92s] English:** because maybe just the level of what's required to do this stuff  
**Translation:** 

**[6378.24s] English:** is so high that everything else seems easy,  
**Translation:** 

**[6380.72s] English:** I guess is the lesson to take away from that.  
**Translation:** 

**[6383.48s] English:** So in the community,  
**Translation:** 

**[6384.46s] English:** like some of the most impressive people  
**Translation:** 

**[6386.60s] English:** are the ones doing reverse engineering  
**Translation:** 

**[6387.98s] English:** and the other ones doing the assembly folks, right?  
**Translation:** 

**[6391.58s] English:** And both of those type of people are amazing.  
**Translation:** 

**[6397.30s] English:** x264, for example, became amazing  
**Translation:** 

**[6399.06s] English:** because of a guy called Lorraine Merritt,  
**Translation:** Vocabulary: lorraine: 洛林; merritt: 梅里特

**[6402.16s] English:** who was from the University of Washington, I think.  
**Translation:** 

**[6404.60s] English:** At the time, yeah.  
**Translation:** 

**[6405.28s] English:** And who made everything great and fast  
**Translation:** 

**[6409.52s] English:** doing a ton of assembly.  
**Translation:** 

**[6412.04s] English:** Yeah, so this is like the golden era, I guess,  
**Translation:** 

**[6416.22s] English:** where so many things got done.  
**Translation:** 

**[6417.54s] English:** Yeah, if you look at Colt,  
**Translation:** 

**[6417.96s] English:** for example, he looked at the world as a binary specification.  
**Translation:** Vocabulary: binary: 二进制; specification: 规范

**[6421.10s] English:** He didn't need documentation or anything.  
**Translation:** 

**[6423.46s] English:** It's, I have a binary and I can figure all of this out.  
**Translation:** 

**[6426.18s] English:** And he regularly used the phrase binary specification.  
**Translation:** 

**[6429.66s] English:** I know it's not a problem.  
**Translation:** 

**[6430.72s] English:** And he went and he would go away and he would come back  
**Translation:** 

**[6432.50s] English:** and he would do interesting stuff.  
**Translation:** 

**[6435.16s] English:** Can you actually speak to the details  
**Translation:** 

**[6437.12s] English:** or any add color and texture  
**Translation:** 

**[6439.14s] English:** to what it takes to reverse engineer a blob?  
**Translation:** 

**[6442.06s] English:** Yeah, so let's look at GoToMeeting, for example,  
**Translation:** 

**[6444.18s] English:** is a good one because I record a meeting.  
**Translation:** 

**[6447.96s] English:** So on GoToMeeting, for example,  
**Translation:** 

**[6450.04s] English:** how do I play it back without needing this GoToMeeting player?  
**Translation:** 

**[6454.30s] English:** They may not even be a player.  
**Translation:** 

**[6455.98s] English:** I may need to send a recording of a meeting to someone  
**Translation:** 

**[6458.30s] English:** that doesn't have a player or whatever.  
**Translation:** 

**[6460.62s] English:** So first of all, there's a ton of other stuff there.  
**Translation:** 

**[6463.42s] English:** There's an actual video conferencing client.  
**Translation:** Vocabulary: conferencing: 会议通话

**[6465.26s] English:** You need to go and find, it may be easy,  
**Translation:** 

**[6467.08s] English:** it may not be easy to find the actual module  
**Translation:** Vocabulary: module: 模块

**[6468.92s] English:** doing the decompression.  
**Translation:** 

**[6471.60s] English:** You need a way to actually dump the YUV data from the module.  
**Translation:** Vocabulary: decompression: 减压解压

**[6475.52s] English:** So often it involves opening in a distance,  
**Translation:** 

**[6477.10s] English:** it involves opening in a disassembler,  
**Translation:** Vocabulary: disassembler: 反汇编器

**[6478.48s] English:** trying to guess where the hook.  
**Translation:** 

**[6480.00s] English:** are to incorporate that module and run that module natively to decode a sample file so figure out  
**Translation:** Vocabulary: incorporate: 合并; natively: 本地

**[6487.44s] English:** where this module is doing the decoding process and and find a way to hook in and output the raw  
**Translation:** 

**[6494.10s] English:** YUV data because you will need that as a point of comparison for when you actually do the reverse  
**Translation:** 

**[6499.28s] English:** engineering because you'll need to be bit exact or in some cases close to bit exact and then you  
**Translation:** 

**[6505.48s] English:** open up your disassembler use a lot of intuition to go and figure out you know where the dct is  
**Translation:** Vocabulary: intuition: 直觉

**[6511.64s] English:** where's entropy coding there is a kind of not a rule book but there's always a pattern of some  
**Translation:** 

**[6517.34s] English:** sort um for example go to meeting you know it will be a lot of screen codec tools there's also  
**Translation:** Vocabulary: entropy: 混乱程度

**[6523.30s] English:** different variants so often i think there's what's go to meeting four five two three four i think two  
**Translation:** 

**[6527.98s] English:** three four yeah so as you mentioned here going to perplexity go to meeting uses its own proprietary  
**Translation:** Vocabulary: perplexity: 困惑; proprietary: 专有

**[6533.10s] English:** codec for older recorded sessions  
**Translation:** 

**[6535.32s] English:** historically stored in wmv files that require a special decoder to play properly on windows  
**Translation:** Vocabulary: historically: 历史上

**[6541.58s] English:** without this decoder installed windows media player and some editors cannot decode the video  
**Translation:** 

**[6548.14s] English:** track so you may only hear audio or see a black screen boy do i remember that but this is reverse  
**Translation:** Vocabulary: cannot: 不能

**[6555.16s] English:** engineering that this is key right because the go to meeting is something that not many people  
**Translation:** 

**[6560.38s] English:** know anymore right well you know about zoom and and teams and so on but like now let's fast forward  
**Translation:** 

**[6565.20s] English:** to the go to meeting part two of the go to meeting part two of the go to meeting part two of the  
**Translation:** 

**[6565.32s] English:** 10 years 15 years and like this is a go to meeting.exe for windows 32 bits right which is  
**Translation:** 

**[6571.84s] English:** like oh yeah but i'm on android i'm on an ipad i'm somewhere else right how are you going to do that  
**Translation:** 

**[6576.96s] English:** i'm going to be on risk 5 on arm those are blocked but there are tons of files we need to  
**Translation:** 

**[6582.30s] English:** support for the future and this is why those type of work are  
**Translation:** 

**[6586.38s] English:** exceptionally useful for humanity i just have to say though that reverse engineering process  
**Translation:** Vocabulary: exceptionally: 特别地

**[6594.24s] English:** is mind-blowing  
**Translation:** 

**[6595.32s] English:** it's crazy it's like it's a kind of like you know  
**Translation:** 

**[6600.00s] English:** know I've been reading a lot in the interview archaeologists I mean you you  
**Translation:** 

**[6604.20s] English:** just have so little signal yes yes you know over time you get so much  
**Translation:** Vocabulary: archaeologists: 考古学家

**[6609.06s] English:** experience you understand the structure of the original code so you can kind of  
**Translation:** 

**[6612.18s] English:** start inferring basics yeah but you're like I would like it was like an  
**Translation:** Vocabulary: inferring: 推断

**[6617.68s] English:** archaeologist with a little brush trying to reconstruct the entire human so he  
**Translation:** 

**[6622.20s] English:** is too humble but Karen has done some reversing of Cineform yeah at the time  
**Translation:** Vocabulary: archaeologist: 考古学家; reconstruct: 重建; reversing: 反转

**[6626.38s] English:** Cineform nice yeah at the time before actually led to the open sourcing of  
**Translation:** 

**[6630.64s] English:** that work so in parallel to doing the binary side you obviously have samples  
**Translation:** 

**[6635.38s] English:** in many cases you don't have many samples so you have to figure out what  
**Translation:** 

**[6640.00s] English:** all the different flavors are and you may have a Cineform for example is  
**Translation:** Vocabulary: cineform: 电影格式

**[6643.46s] English:** actually a collection of different approaches and toolkits within that  
**Translation:** 

**[6646.90s] English:** codec because often it it grows naturally and and the hard part is  
**Translation:** Vocabulary: toolkits: 工具包

**[6650.68s] English:** finding the sample that gets you kind of somewhere to start without having to  
**Translation:** 

**[6655.66s] English:** implement  
**Translation:** 

**[6656.00s] English:** 10  
**Translation:** 

**[6656.36s] English:** , 10 different other things so start there I think thankfully at the time I  
**Translation:** 

**[6660.68s] English:** found a sample by pure chance I had a lot of flat blocks it was animation so  
**Translation:** 

**[6664.52s] English:** that really helped a lot because it wasn't using particularly complex coding  
**Translation:** 

**[6668.78s] English:** tools Etc and you could kind of get somewhere and then and then build up and  
**Translation:** 

**[6672.20s] English:** build up until you figure hey here's a few bits here I miss this I miss this  
**Translation:** 

**[6675.74s] English:** this if branch that it does and go oh so when we say samples you mean sample  
**Translation:** 

**[6679.40s] English:** videos and then and then you're tracking trying to infer like what is this codec  
**Translation:** 

**[6684.56s] English:** doing yes by observing  
**Translation:** 

**[6685.98s] English:** observing the sample and then looking at what at the at the machine the machine  
**Translation:** 

**[6691.38s] English:** code saying I have this bite is six take this branch and then a different sample  
**Translation:** 

**[6696.30s] English:** oh it's nuts man and and so you see this is not then you go to things like go to  
**Translation:** 

**[6702.12s] English:** me it's like mine was easy right imagine yeah right two order of magnitude of more  
**Translation:** 

**[6708.60s] English:** complexity a guy alone somewhere in Germany doing that yeah and for a long time you work  
**Translation:** 

**[6715.60s] English:** you're in a black box because a decoder for a long time because there is so many steps from the  
**Translation:** 

**[6720.00s] English:** entropy decoding the intra prediction the motion prediction the idct and so on for a long time you  
**Translation:** Vocabulary: entropy: 熵解码; intra: 内插预测

**[6726.24s] English:** don't see anything right so you're debugging purely in memory debugging guesswork and you  
**Translation:** 

**[6730.96s] English:** may have the buffer that the coefficients are stored in completely wrong and so you may be  
**Translation:** Vocabulary: buffer: 缓冲区; coefficients: 系数; guesswork: 猜测

**[6735.28s] English:** going down a complete rabbit hole thinking it's this and then oh damn that's not that's  
**Translation:** 

**[6739.84s] English:** that's something else and and you're doing that on binaries that are tens of megabytes  
**Translation:** Vocabulary: binaries: 二进制文件; megabytes: 兆字节

**[6744.64s] English:** millions of instructions right so you're stepping through the debugger like one by one you know  
**Translation:** 

**[6750.64s] English:** instruction by instruction going hey this instruction changes this this does this  
**Translation:** 

**[6754.36s] English:** pausing the program on the cpu level on the cpu level watching what's going on trying to figure  
**Translation:** 

**[6758.96s] English:** out sometimes you need to like be in a vm so yes you can pause the vm yeah pause the vm dump the  
**Translation:** 

**[6764.10s] English:** memory because it could some of the codecs could have encryption there could be um like a drm on  
**Translation:** 

**[6768.90s] English:** there so you need to dump the memory from a virtual machine like when i join they call central paris  
**Translation:** Vocabulary: encryption: 加密

**[6774.42s] English:** to take a look at the codecs and i'm like oh my god what's going on here what's going on here  
**Translation:** 

**[6774.62s] English:** 2003 john lesh johansson basically broke the dvd specification and created dcss  
**Translation:** Vocabulary: johansson: 约翰松; specification: 规范

**[6780.56s] English:** showed us how he was breaking a drm which was mp4 fair play from apple what he did on his  
**Translation:** 

**[6787.98s] English:** laptop and i was young i was 21 was just like mind-blowing because he was basically debugging  
**Translation:** 

**[6793.00s] English:** windows inside a type of vm with like wow it's incredible it's mind-blowing and inspiring does  
**Translation:** 

**[6801.18s] English:** it get like from your experience and from what you've seen in the community does it get  
**Translation:** 

**[6804.60s] English:** discouraging does it get people help you people send you samples people are keen  
**Translation:** 

**[6808.94s] English:** sometimes you don't have access to an encoder so this is even more difficult because you just  
**Translation:** Vocabulary: discouraging: 令人灰心

**[6814.44s] English:** you just ask and you have to ask for samples i remember video land used to tweet for samples  
**Translation:** 

**[6819.76s] English:** at one stage hey i need this obscure sample and for a long time i was oh i need this codec and i  
**Translation:** Vocabulary: obscure: 冷门的

**[6824.24s] English:** need this codec and and if you were really lucky you would find like if you were if you were unlucky  
**Translation:** 

**[6828.74s] English:** you'd get like one or two you'd get nothing or you get one or two and then they would sometimes  
**Translation:** 

**[6832.38s] English:** you'd find a gold mine like yeah my company has a home codec and i need this codec and i need this  
**Translation:** 

**[6834.60s] English:** codec and they'll give you like an thousands of these files because we depended on it for some  
**Translation:** 

**[6836.90s] English:** reason and so those are those are kind of the best  
**Translation:** 

**[6840.00s] English:** Because then they can test bit exactness across the huge range of coding tools.  
**Translation:** Vocabulary: exactness: 精确性

**[6846.02s] English:** Can you explain bit exactness?  
**Translation:** 

**[6847.80s] English:** Bit exactness.  
**Translation:** 

**[6849.00s] English:** So most but not all video codecs, certainly from about the 2000s onwards, have a bit exact definition.  
**Translation:** 

**[6857.54s] English:** So every implementation must produce exactly the same bits, bit for bits, in exactly the same data that comes out of a decoder.  
**Translation:** Vocabulary: implementation: 实现; onwards: 以后

**[6866.58s] English:** For like a large number of samples?  
**Translation:** 

**[6868.70s] English:** For a given sample.  
**Translation:** 

**[6869.46s] English:** So Lex's implementation, JB's implementation, and my implementation of H.264 must match bit exactly.  
**Translation:** 

**[6875.76s] English:** That wasn't the case in the 90s of MPEG-2.  
**Translation:** 

**[6878.22s] English:** Probably, fair to say, one of the biggest mistakes the video industry made.  
**Translation:** 

**[6883.08s] English:** And I think people who were in the room in 92, most of both of us were in diapers, I suspect, have acknowledged.  
**Translation:** 

**[6889.68s] English:** I would give a shout out to Yuri Reznik.  
**Translation:** 

**[6892.88s] English:** He's acknowledged that was one of the big mistakes of the era.  
**Translation:** 

**[6895.64s] English:** And you're saying the encoders needed to be able to run tests.  
**Translation:** 

**[6899.02s] English:** And then the bit exactness.  
**Translation:** Vocabulary: encoders: 编码器

**[6902.54s] English:** I mean, that's a nice thing to guarantee.  
**Translation:** 

**[6904.60s] English:** Like, there's a parallel sort of development here on the way the web browser works, which is, you know, takes HTML and displays it.  
**Translation:** 

**[6912.76s] English:** And there's no bit exactness there across the different engines.  
**Translation:** 

**[6915.90s] English:** I would point out, actually, FFmpeg is unique in the sense that it has been a win-it-takes-all scenario.  
**Translation:** 

**[6922.70s] English:** Browsers is a good analogy because it has to parse a lot of different content and render it in a particular way, like a decoder.  
**Translation:** 

**[6929.02s] English:** But there still are multiple browser engines.  
**Translation:** Vocabulary: browsers: 浏览器; parse: 解析; render: 渲染

**[6930.94s] English:** There's Firefox's one.  
**Translation:** 

**[6931.98s] English:** There's Chrome's one.  
**Translation:** 

**[6932.76s] English:** There's a few Japanese ones that are pretty decent.  
**Translation:** 

**[6935.16s] English:** That's not been the case in multimedia in general across a wide range of codecs.  
**Translation:** Vocabulary: multimedia: 多种媒体

**[6940.38s] English:** FFmpeg is kind of one-it-all, I suppose, in a sense, because of the fact that you can get every new codec added is actually worth more than the value of that codec itself because it makes the whole thing better.  
**Translation:** 

**[6952.34s] English:** Man, this is really cool.  
**Translation:** 

**[6954.22s] English:** Going to Perplexity, Yuri Reznik is a multimedia and signal processing researcher.  
**Translation:** 

**[6957.94s] English:** Got his Ph.D. in computer science.  
**Translation:** Vocabulary: perplexity: 困惑程度

**[6960.00s] English:** from Kyiv University  
**Translation:** 

**[6961.04s] English:** with over 150 papers  
**Translation:** 

**[6962.90s] English:** and more than 80  
**Translation:** 

**[6963.78s] English:** granted U.S. patents,  
**Translation:** 

**[6965.80s] English:** contributor to major  
**Translation:** 

**[6967.08s] English:** multimedia standards  
**Translation:** 

**[6967.98s] English:** including issue 64,  
**Translation:** 

**[6970.12s] English:** MPEG-4,  
**Translation:** 

**[6971.12s] English:** AVC,  
**Translation:** 

**[6971.96s] English:** H.265,  
**Translation:** 

**[6973.92s] English:** MPEG-4 ALS,  
**Translation:** 

**[6976.02s] English:** G.718.  
**Translation:** 

**[6977.24s] English:** G.718 is telco stuff.  
**Translation:** 

**[6978.80s] English:** And so he was more  
**Translation:** 

**[6980.24s] English:** connected to companies.  
**Translation:** 

**[6981.24s] English:** Real audio,  
**Translation:** 

**[6982.02s] English:** real video, right?  
**Translation:** 

**[6982.84s] English:** That was very important  
**Translation:** 

**[6984.82s] English:** at that time.  
**Translation:** 

**[6985.40s] English:** Zencoder,  
**Translation:** Vocabulary: zencoder: 编码器

**[6985.86s] English:** Brightcove,  
**Translation:** 

**[6986.50s] English:** Context.  
**Translation:** 

**[6987.40s] English:** Man,  
**Translation:** 

**[6988.10s] English:** I need to hang out  
**Translation:** 

**[6988.82s] English:** with Yuri.  
**Translation:** 

**[6989.30s] English:** He's legit.  
**Translation:** Vocabulary: legit: 正经的

**[6990.58s] English:** And he's like  
**Translation:** 

**[6991.34s] English:** one of the most  
**Translation:** 

**[6992.00s] English:** nice person ever,  
**Translation:** 

**[6993.98s] English:** right?  
**Translation:** 

**[6994.78s] English:** Like,  
**Translation:** 

**[6995.60s] English:** for example,  
**Translation:** 

**[6996.08s] English:** for my startup  
**Translation:** 

**[6997.78s] English:** that I'm doing right now  
**Translation:** 

**[6999.34s] English:** called Kyber,  
**Translation:** 

**[7000.02s] English:** right?  
**Translation:** 

**[7000.20s] English:** I met Yuri  
**Translation:** 

**[7000.74s] English:** because I met him  
**Translation:** 

**[7001.92s] English:** every year  
**Translation:** 

**[7002.44s] English:** at the Mile High  
**Translation:** 

**[7003.20s] English:** video conference  
**Translation:** 

**[7004.38s] English:** which is in Denver.  
**Translation:** Vocabulary: denver: Denver市

**[7006.28s] English:** And he gave me  
**Translation:** 

**[7007.58s] English:** like so much  
**Translation:** 

**[7008.16s] English:** good ideas  
**Translation:** 

**[7009.82s] English:** and good things.  
**Translation:** 

**[7010.84s] English:** He's like  
**Translation:** 

**[7011.22s] English:** really amazing person.  
**Translation:** 

**[7012.58s] English:** He tells us  
**Translation:** 

**[7013.18s] English:** how,  
**Translation:** 

**[7013.56s] English:** you know,  
**Translation:** 

**[7014.92s] English:** how great it is  
**Translation:** 

**[7015.58s] English:** to be,  
**Translation:** 

**[7016.10s] English:** you know,  
**Translation:** 

**[7016.30s] English:** even know us.  
**Translation:** 

**[7017.02s] English:** And,  
**Translation:** 

**[7017.16s] English:** you know,  
**Translation:** 

**[7017.86s] English:** you look at that  
**Translation:** 

**[7018.44s] English:** and I think  
**Translation:** 

**[7019.18s] English:** it's,  
**Translation:** 

**[7019.42s] English:** I think,  
**Translation:** 

**[7019.64s] English:** I think,  
**Translation:** 

**[7020.00s] English:** I think it's the other  
**Translation:** 

**[7020.32s] English:** way around, Yuri.  
**Translation:** 

**[7021.64s] English:** That reminds me  
**Translation:** 

**[7022.56s] English:** of a thing  
**Translation:** 

**[7022.96s] English:** that you mentioned  
**Translation:** 

**[7024.02s] English:** to me about  
**Translation:** 

**[7024.66s] English:** FFmpeg testing  
**Translation:** 

**[7025.44s] English:** and like the  
**Translation:** 

**[7026.22s] English:** insanely vigorous  
**Translation:** 

**[7027.30s] English:** process that's used  
**Translation:** Vocabulary: vigorous: 精力充沛

**[7028.56s] English:** to test everything  
**Translation:** 

**[7030.10s] English:** that's incorporated  
**Translation:** 

**[7030.82s] English:** into FFmpeg.  
**Translation:** 

**[7033.00s] English:** Can you take me  
**Translation:** 

**[7033.64s] English:** through the testing  
**Translation:** 

**[7034.16s] English:** process?  
**Translation:** 

**[7034.86s] English:** Yeah,  
**Translation:** 

**[7035.04s] English:** so FFmpeg  
**Translation:** 

**[7035.78s] English:** has a system  
**Translation:** 

**[7036.34s] English:** called FFmpeg  
**Translation:** 

**[7037.38s] English:** automated testing  
**Translation:** 

**[7038.18s] English:** environment.  
**Translation:** Vocabulary: automated: 自动化测试环境

**[7039.04s] English:** Because FFmpeg  
**Translation:** 

**[7040.04s] English:** runs on so many  
**Translation:** 

**[7041.38s] English:** different OSs  
**Translation:** 

**[7042.16s] English:** and can be compiled  
**Translation:** Vocabulary: compiled: 编译过的

**[7042.88s] English:** with so many  
**Translation:** 

**[7043.42s] English:** different compilers,  
**Translation:** Vocabulary: compilers: 编译器

**[7044.68s] English:** there's been a crazy  
**Translation:** 

**[7046.56s] English:** number of configurations.  
**Translation:** Vocabulary: configurations: 配置方式

**[7048.14s] English:** So,  
**Translation:** 

**[7048.38s] English:** you can see the  
**Translation:** 

**[7050.00s] English:** absurd combination  
**Translation:** 

**[7051.36s] English:** of compiler variants,  
**Translation:** 

**[7054.78s] English:** operating system variants,  
**Translation:** 

**[7056.46s] English:** instruction sets.  
**Translation:** 

**[7058.06s] English:** You can see  
**Translation:** 

**[7058.44s] English:** at the top,  
**Translation:** 

**[7058.84s] English:** macOS has tons  
**Translation:** 

**[7059.78s] English:** of different variants  
**Translation:** 

**[7060.50s] English:** because it has iOS,  
**Translation:** 

**[7061.66s] English:** it has tvOS.  
**Translation:** 

**[7062.62s] English:** I'm looking at a page,  
**Translation:** 

**[7063.60s] English:** fate.ffmpeg.org,  
**Translation:** 

**[7067.00s] English:** 81 minutes ago,  
**Translation:** 

**[7068.56s] English:** 76 minutes ago,  
**Translation:** 

**[7070.24s] English:** looking at the  
**Translation:** 

**[7071.12s] English:** different architectures,  
**Translation:** 

**[7072.08s] English:** the operating systems,  
**Translation:** 

**[7073.00s] English:** the different compilers,  
**Translation:** 

**[7074.04s] English:** Apple,  
**Translation:** 

**[7074.46s] English:** Clang,  
**Translation:** Vocabulary: clang: 金属撞击声

**[7075.64s] English:** version,  
**Translation:** 

**[7077.22s] English:** combinations,  
**Translation:** 

**[7078.28s] English:** the combination  
**Translation:** 

**[7079.06s] English:** is insane.  
**Translation:** 

**[7080.00s] English:** These are all run by volunteers, so these are all volunteer systems.  
**Translation:** 

**[7083.20s] English:** The ones at the top, for example, the Macs I host in my office, for example,  
**Translation:** 

**[7087.74s] English:** host all sorts of different stuff.  
**Translation:** 

**[7089.24s] English:** Other people host other things.  
**Translation:** 

**[7091.38s] English:** So it's really there to make sure,  
**Translation:** 

**[7093.72s] English:** because FFmpeg does quite complex C code, for example,  
**Translation:** 

**[7097.00s] English:** you do have miscompilations.  
**Translation:** 

**[7098.68s] English:** So the compiler will sometimes compile C code incorrectly, for example.  
**Translation:** Vocabulary: miscompilations: 错误编译

**[7103.58s] English:** This happens once in a while.  
**Translation:** 

**[7105.40s] English:** There's a log of all the compilations.  
**Translation:** Vocabulary: compilations: 编译记录

**[7108.26s] English:** Yeah, log of all the compilations, all the tests.  
**Translation:** 

**[7110.64s] English:** I think one of the other ones will show all the tests passing.  
**Translation:** 

**[7112.90s] English:** If you click, you can see all the tests back, all tests successful.  
**Translation:** 

**[7117.64s] English:** And logs tests, yeah.  
**Translation:** 

**[7119.26s] English:** So you see all those tests are passing of all the different codecs,  
**Translation:** 

**[7124.30s] English:** all the different filter transformations.  
**Translation:** 

**[7127.52s] English:** The level of scale is quite crazy.  
**Translation:** 

**[7130.18s] English:** On all the combinations, it's not just a matrix at this point.  
**Translation:** Vocabulary: matrix: 矩阵

**[7133.16s] English:** It's like a pivot table of different combinations.  
**Translation:** 

**[7135.94s] English:** That's nuts.  
**Translation:** 

**[7136.88s] English:** And it's a key part.  
**Translation:** 

**[7138.08s] English:** It's a key part of what we do,  
**Translation:** 

**[7138.62s] English:** because you may be able to test something locally,  
**Translation:** 

**[7142.18s] English:** you make a change,  
**Translation:** 

**[7142.98s] English:** but actually that breaks GCC version 11 on Mac or something like that,  
**Translation:** 

**[7148.62s] English:** and you're able to then fix that.  
**Translation:** 

**[7150.40s] English:** We also have miscompilation.  
**Translation:** 

**[7151.92s] English:** So the C code, sometimes the compiler can have a bug in it  
**Translation:** Vocabulary: miscompilation: 编译错误

**[7154.36s] English:** where it creates the wrong output.  
**Translation:** 

**[7156.24s] English:** And that can have quite a big effect sometimes on a video  
**Translation:** 

**[7159.26s] English:** because of the way frames have dependencies.  
**Translation:** 

**[7162.18s] English:** Even a small change in the output can cascade to actually quite big glitches.  
**Translation:** Vocabulary: glitches: 错误

**[7168.08s] English:** You see PowerPC, you see RISC, you see ARM.  
**Translation:** 

**[7170.84s] English:** There was PowerPC, there was RISC, there was weird stuff in the past, like DEC Alpha.  
**Translation:** Vocabulary: alpha: DEC Alpha

**[7175.00s] English:** You see Visual Studio, different versions of Chrome,  
**Translation:** 

**[7178.20s] English:** Intel Compiler, Apple Clang, you name it.  
**Translation:** 

**[7180.84s] English:** What are some of the pain points?  
**Translation:** 

**[7183.00s] English:** Like maybe do you have emotional triggers,  
**Translation:** 

**[7187.00s] English:** maybe nightmares about a particular operating system,  
**Translation:** 

**[7190.70s] English:** a particular container, codec, combination?  
**Translation:** Vocabulary: nightmares: 噩梦

**[7193.46s] English:** For me, it's really easy because I have a day job, my company builds.  
**Translation:** 

**[7198.08s] English:** At the company I started builds,  
**Translation:** 

**[7200.00s] English:** equipment for broadcasting sports matches between TV stadiums and studios, for example.  
**Translation:** 

**[7205.22s] English:** We have to work with 10-bit video, and 10-bit video has a set of challenges that  
**Translation:** 

**[7210.52s] English:** you can't process 10-bit data natively on a CPU. So that means you have to stick it in 16 bits.  
**Translation:** 

**[7218.92s] English:** So that means you have six wasted bits. So there's different packing formats to actually  
**Translation:** Vocabulary: natively: 本机处理

**[7223.30s] English:** pack the data more efficiently, because when you send that over a network, you lose, because you  
**Translation:** 

**[7228.26s] English:** need to save that 40%. For example, on PCI Express, you may only have bus bandwidth to do  
**Translation:** Vocabulary: bandwidth: 带宽; efficiently: 高效地

**[7233.28s] English:** that. And so I think internally we have about... Some are industry ones, and some are internal to  
**Translation:** 

**[7238.76s] English:** our own hardware that we build. We have, I think, a 5x5 or 6x6 matrix of every single format to  
**Translation:** Vocabulary: internally: 内部地

**[7246.20s] English:** every single other format conversion. In fact, one of them I sent you, and they're all written  
**Translation:** 

**[7250.80s] English:** in handwritten assembly, and they all support different CPU generations. So this is really  
**Translation:** Vocabulary: handwritten: 手工编写

**[7257.98s] English:** traumatic.  
**Translation:** 

**[7258.26s] English:** Handling all these different combinations, times a million.  
**Translation:** Vocabulary: traumatic: 创伤性的

**[7262.30s] English:** By the way, the company you're talking about is Open Broadcast Systems.  
**Translation:** 

**[7264.88s] English:** No relation to the free OBS streaming service.  
**Translation:** 

**[7267.52s] English:** Yeah, yeah.  
**Translation:** 

**[7268.38s] English:** But JB and I have started companies, broadly speaking, around the FFmpeg VLC ethos. So that's  
**Translation:** Vocabulary: ethos: 精神内涵

**[7274.88s] English:** really low-level work. So in most companies, this wouldn't be written in assembly. It would be  
**Translation:** 

**[7280.60s] English:** accepted that C is fast. As you can see from that, C is not fast.  
**Translation:** 

**[7286.60s] English:** So here it says 60...  
**Translation:** 

**[7288.26s] English:** 62 times faster than C.  
**Translation:** 

**[7290.94s] English:** Yeah. So it's taking those... The ethos of doing low-level programming, real-time programming,  
**Translation:** 

**[7298.62s] English:** and using that for commercial applications. And JB and I have started companies around that,  
**Translation:** 

**[7303.84s] English:** in many cases hiring developers from the open-source community,  
**Translation:** 

**[7306.38s] English:** to use that ethos. And so that's a great example of some of the things we're doing.  
**Translation:** 

**[7314.60s] English:** In most companies, it would be, I'll write this in C, and it's fast, and we're done. But actually,  
**Translation:** 

**[7318.28s] English:** you can get a lot better.  
**Translation:** 

**[7319.86s] English:** Formula...  
**Translation:** 

**[7329.02s] English:** .  
**Translation:** 

**[7320.00s] English:** me like some of the headaches we have is around some os that are difficult to support right because  
**Translation:** 

**[7327.88s] English:** if you look at vlc and thanks to fate and ffmpeg we run on the last version of vlc runs on windows  
**Translation:** 

**[7337.68s] English:** xp and still run there and runs on windows 11 we work on mac os 10.7 to the latest mac os whatever  
**Translation:** 

**[7348.26s] English:** it is right 26 we work on ios since ios 9 where we are actually ios 26 right we support  
**Translation:** 

**[7356.28s] English:** we support many types of linux's bsd solaris the last version still runs on os2 right like  
**Translation:** 

**[7365.34s] English:** there is maybe 10 users of os2 in the world and one of them is maintaining vlc then you realize  
**Translation:** 

**[7371.12s] English:** that this very small team around vlc and using ffmpeg codecs and and all the other ones support  
**Translation:** 

**[7377.28s] English:** more  
**Translation:** 

**[7378.24s] English:** os's than microsoft or google or apple and they have infinite amount of uh of power and resources  
**Translation:** 

**[7386.78s] English:** but for example the worst is ios um for in order to build on ios 9 we need to do some very clever  
**Translation:** 

**[7395.70s] English:** mixing of several version of the xcode ide and sdk from apple from several version and do a type  
**Translation:** 

**[7403.78s] English:** of frankenstein version of that so that we can still support ios  
**Translation:** Vocabulary: frankenstein: 拼凑版

**[7408.12s] English:** 9  
**Translation:** 

**[7408.24s] English:** which is not supported at all by the the compiler of uh of uh apple in order to still run on arm 32  
**Translation:** 

**[7417.20s] English:** on ios 9 and you've seen on fate that it was still supporting ios 9 right so so um my headaches are  
**Translation:** 

**[7424.24s] English:** mostly related to the the support of so many os's and it's important because like we receive so many  
**Translation:** 

**[7431.04s] English:** people saying hey thank you i still have my ipad 2 to watch movies and it still works on ios 9 right  
**Translation:** 

**[7438.08s] English:** so it can't just you can't do it right so like you know and for those of us who can learn to use it  
**Translation:** 

**[7440.32s] English:** um we'd like to encourage you just to make sure that you're doing something reasonable and easy  
**Translation:** 

**[7445.10s] English:** and it's also an impact of like we're you know i'm a json and i'm a json  
**Translation:** 

**[7452.92s] English:** i'm not a json to you know i'm not an json kind of like i'm i'm not an from a big beaks  
**Translation:** 

**[7455.52s] English:** or something so like if you don't care about what you're doing it's not gonna be helpful in any way  
**Translation:** 

**[7457.64s] English:** so if you don't care about what you're doing it's not gonna be helpful in any way  
**Translation:** 

**[7458.88s] English:** so i think i hope we've made it clear that we didn't need any of this stuff at all so i think  
**Translation:** 

**[7463.92s] English:** today we're doing the most important thing which is it's going to be about the  
**Translation:** 

**[7440.00s] English:** Like not forcing people to buy new hardware when it works fine.  
**Translation:** 

**[7443.24s] English:** If you optimize it correctly, which brings us to what we were saying about assembly,  
**Translation:** 

**[7448.30s] English:** it's also fighting the fact that you need to buy something new nonstop  
**Translation:** Vocabulary: optimize: 优化

**[7453.00s] English:** while you could optimize more, which is a lost art.  
**Translation:** 

**[7458.24s] English:** You got to tell me about this lost art or the carriers of the flame of assembly.  
**Translation:** 

**[7467.04s] English:** What is assembly? Why is it beautiful? Why is it challenging? How does it work?  
**Translation:** 

**[7474.32s] English:** So when you write assembly code, you write this using the instructions  
**Translation:** 

**[7478.04s] English:** the actual processor is using directly.  
**Translation:** 

**[7480.74s] English:** So most of the time you would write in a language.  
**Translation:** Vocabulary: processor: 处理器

**[7483.18s] English:** Let's take C as a good example.  
**Translation:** 

**[7484.70s] English:** The compiler would use that to create assembly language  
**Translation:** 

**[7488.98s] English:** and machine code instructions for you based off your C code.  
**Translation:** 

**[7493.14s] English:** And there's a specific flavor of assembly that we use in FFmpeg.  
**Translation:** 

**[7496.70s] English:** That's called SIMD, SIMD, single instruction multiple data.  
**Translation:** 

**[7501.28s] English:** So this means, for example, say I want to add five to a number in scalar assembly.  
**Translation:** Vocabulary: scalar: 标量运算

**[7508.64s] English:** So this is what's known as you work on an individual element.  
**Translation:** 

**[7511.16s] English:** So I want to have a number of number 10 and I want to add five.  
**Translation:** 

**[7513.96s] English:** I use the add instruction and I add five to 10 and I get 15.  
**Translation:** 

**[7519.24s] English:** With SIMD, I can have a whole vector of 16 different numbers that could all be different.  
**Translation:** 

**[7524.36s] English:** If I want to add five to that, I can.  
**Translation:** 

**[7526.70s] English:** I can run one instruction and that one instruction sums all 16 elements.  
**Translation:** 

**[7534.44s] English:** And that, as you can imagine, lends itself very well to video.  
**Translation:** 

**[7537.36s] English:** Video is a pixel grid, so I can perform operations on multiple pixels at the same time.  
**Translation:** Vocabulary: pixel: 像素; pixels: 像素

**[7545.48s] English:** The key thing that we do differently in FFmpeg is we don't use any abstractions  
**Translation:** 

**[7549.52s] English:** or any major abstractions on top of that.  
**Translation:** Vocabulary: abstractions: 抽象层

**[7551.44s] English:** So there's a part of the world that uses what's known as intrinsics.  
**Translation:** 

**[7555.28s] English:** So these are C functions.  
**Translation:** Vocabulary: intrinsics: 内在特性

**[7556.30s] English:** That behave very similarly, but not quite the same.  
**Translation:** 

**[7560.00s] English:** writing assembly by hand so the registers that data is stored in on the cpu the compiler allocates  
**Translation:** Vocabulary: allocates: 分配

**[7568.56s] English:** those for you and so the key thing to understand was when we write simd is we have a 10x and not  
**Translation:** 

**[7575.52s] English:** percentage 10x to 50x speed improvement that that function is 62x that's nuts on the ffmpeg account  
**Translation:** 

**[7583.92s] English:** as you know posts and tweets a lot about that to try and say hey we're doing this stuff you are a  
**Translation:** 

**[7589.76s] English:** person who sees the beauty in assembly but it's also extremely useful for these kinds of  
**Translation:** Vocabulary: tweets: 发推特

**[7594.16s] English:** applications to actually significantly outperform even c which is crazy it is necessary yes right  
**Translation:** 

**[7602.16s] English:** because like one of the projects um that we need to talk about is called david right so  
**Translation:** 

**[7608.00s] English:** david is a decoder for the format uh that was done by aliens for open media  
**Translation:** 

**[7614.96s] English:** which is a video decoder called av1 so if people don't know  
**Translation:** 

**[7619.76s] English:** we've been talking about h.264 av1 is another hugely popular standard and codec that is  
**Translation:** 

**[7628.72s] English:** increasingly taking over uh the internet and when this format was launched uh many people said  
**Translation:** 

**[7635.92s] English:** especially even from the alliance from open media right which is google netflix amazon mozilla i say  
**Translation:** 

**[7641.92s] English:** well this format is so complex it must be done in hardware to do decoding right and well i arrived uh  
**Translation:** 

**[7649.76s] English:** with a few other people uh mostly um ronald uh henrik and martin who said we need to have an  
**Translation:** 

**[7656.56s] English:** extremely good software decoder uh because it's going to take time to have hardware and so  
**Translation:** Vocabulary: henrik: 亨里克

**[7662.48s] English:** we wrote this project which is beyond insane um we are talking about 30 000 lines of c  
**Translation:** 

**[7671.44s] English:** but 240 000 lines of handwritten assembly right hand written assembly two hundred  
**Translation:** Vocabulary: handwritten: 手工编写

**[7679.76s] English:** forty  
**Translation:** 

**[7680.00s] English:** 40,000 lines.  
**Translation:** 

**[7682.10s] English:** That's incredible.  
**Translation:** 

**[7683.40s] English:** I mean, some of the stuff we're talking about is probably the biggest assembly code bases.  
**Translation:** 

**[7689.84s] English:** To give you an idea, and Kieran can correct me, but I think the FFmpeg has 100,000 lines of assembly for all the codecs.  
**Translation:** 

**[7697.14s] English:** All codecs.  
**Translation:** 

**[7697.72s] English:** And just this one has 240,000.  
**Translation:** 

**[7700.84s] English:** It's a VideoLand project, of course.  
**Translation:** 

**[7702.78s] English:** And it is optimized at the maximum because the motto when we're starting the project is every cycle matters, right?  
**Translation:** 

**[7713.92s] English:** Every cycle matters because David is used in VLC and in some software AV1 playback stacks.  
**Translation:** Vocabulary: optimized: 优化; playback: 回放

**[7720.64s] English:** We are talking about probably 3 billion devices which are going to decode video nonstop.  
**Translation:** 

**[7726.76s] English:** Because, for example, 30% of the video from Netflix are now in AV1.  
**Translation:** 

**[7730.82s] English:** 50% of YouTube.  
**Translation:** 

**[7732.78s] English:** And you often don't have a hardware decoder because not many devices have a hardware decoder.  
**Translation:** 

**[7739.02s] English:** And with David, we realized that with one or two cores, you were able to decode 720p correctly.  
**Translation:** 

**[7744.96s] English:** So, it is literally incredible.  
**Translation:** 

**[7749.44s] English:** That's David. Look at that.  
**Translation:** 

**[7750.42s] English:** Yeah, so this is another spicy tweet from you.  
**Translation:** 

**[7754.60s] English:** This is what peak video codecs should look like.  
**Translation:** 

**[7758.12s] English:** 79.9% assembly.  
**Translation:** 

**[7760.48s] English:** 19.6% C.  
**Translation:** 

**[7762.50s] English:** And...  
**Translation:** 

**[7762.78s] English:** And 0.5% other.  
**Translation:** 

**[7765.60s] English:** And what's incredible is with those tweets, which is factual, people get crazy.  
**Translation:** Vocabulary: tweets: 微博

**[7772.32s] English:** They are unhappy, right?  
**Translation:** 

**[7773.52s] English:** They say, for the last two years, they go crazy.  
**Translation:** 

**[7775.24s] English:** No, intrinsics is fine.  
**Translation:** 

**[7776.44s] English:** The compiler is...  
**Translation:** Vocabulary: intrinsics: 内在特性

**[7777.28s] English:** Oh, there you go.  
**Translation:** 

**[7777.78s] English:** You can optimize your compiler, auto vectorization.  
**Translation:** Vocabulary: optimize: 优化; vectorization: 向量化的过程

**[7780.72s] English:** It's your fault.  
**Translation:** 

**[7781.54s] English:** You don't understand.  
**Translation:** 

**[7782.46s] English:** And we've tried that forever, right?  
**Translation:** 

**[7784.64s] English:** For two years and two years later, showing hundreds of examples of handwritten assembly.  
**Translation:** 

**[7790.44s] English:** No, no, no.  
**Translation:** 

**[7791.00s] English:** You're doing it wrong.  
**Translation:** 

**[7791.66s] English:** The compiler can do this.  
**Translation:** 

**[7792.74s] English:** So, we should actually just articulate a little clearer.  
**Translation:** Vocabulary: articulate: 表达清晰

**[7795.50s] English:** So, the intuition there from the software engineering folks, when you have code like...  
**Translation:** 

**[7799.40s] English:** Okay, let's just...  
**Translation:** Vocabulary: intuition: 直觉

**[7800.08s] English:** Okay.  
**Translation:** 

**[7801.08s] English:** Okay.  
**Translation:** 

**[7803.08s] English:** Okay.  
**Translation:** 

**[7804.08s] English:** Okay.  
**Translation:** 

**[7805.08s] English:** Okay.  
**Translation:** 

**[7806.08s] English:** Okay.  
**Translation:** 

**[7807.08s] English:** Okay.  
**Translation:** 

**[7808.08s] English:** Okay.  
**Translation:** 

**[7809.08s] English:** Okay.  
**Translation:** 

**[7810.08s] English:** Okay.  
**Translation:** 

**[7811.08s] English:** Okay.  
**Translation:** 

**[7812.08s] English:** Okay.  
**Translation:** 

**[7813.08s] English:** Okay.  
**Translation:** 

**[7814.08s] English:** Okay.  
**Translation:** 

**[7815.08s] English:** Okay.  
**Translation:** 

**[7816.08s] English:** Okay.  
**Translation:** 

**[7817.08s] English:** Okay.  
**Translation:** 

**[7818.08s] English:** Okay.  
**Translation:** 

**[7819.08s] English:** Okay.  
**Translation:** 

**[7820.08s] English:** Okay.  
**Translation:** 

**[7821.08s] English:** Okay.  
**Translation:** 

**[7822.08s] English:** Okay.  
**Translation:** 

**[7800.00s] English:** an example c plus plus there's a compiler that's doing a lot of the optimization yes and the  
**Translation:** 

**[7806.88s] English:** presumption is if you have a good enough compiler if you continue to improve the compiler you're  
**Translation:** Vocabulary: optimization: 优化

**[7811.36s] English:** going to generate code yeah they can perform like optimal performance you cannot possibly beat it  
**Translation:** 

**[7818.40s] English:** and you're consistently challenging that thought that if my orders of magnitude by orders of  
**Translation:** Vocabulary: cannot: 不可能; optimal: 最佳

**[7822.80s] English:** magnitude handcrafted assembly can outperform c the two things that they tell us is yeah but  
**Translation:** 

**[7829.92s] English:** modern compilers have auto vectorization right because simd that we're doing is vectorization  
**Translation:** Vocabulary: compilers: 编译器; handcrafted: 手工制作

**[7835.44s] English:** and like it's not even close right it's not even close right it's not like five percent ten percent  
**Translation:** 

**[7841.28s] English:** slower it's multiple times slower so can we i don't know if you can say something philosophically  
**Translation:** Vocabulary: philosophically: 哲学地

**[7845.84s] English:** because there's a lot of there's a lot of great software engineers great engineers great machine  
**Translation:** 

**[7850.88s] English:** learning people karpathy will listen to this and say what's the intuition he's supposed to get from  
**Translation:** Vocabulary: karpathy: 卡普雷

**[7855.84s] English:** this what are we supposed to he learned assembly because of the tweets by the way i just he's  
**Translation:** 

**[7859.92s] English:** he's like oh i think this is like let me figure out and you know the way he documents his work and  
**Translation:** 

**[7864.88s] English:** so philosophically what's important to realize is that we passed the time where hardware was going  
**Translation:** 

**[7872.00s] English:** so much faster right we at the end of the more low we have limitation for uh for ai for memory  
**Translation:** 

**[7878.40s] English:** you need to go down in the stack and optimize more to get more power from what you have  
**Translation:** 

**[7884.00s] English:** because our requests for power cpu power gpu power are  
**Translation:** 

**[7889.52s] English:** exploding while the hardware is not exploding in speed right so you what people do is that they  
**Translation:** 

**[7897.12s] English:** add more calls right but that's basically like at some point you can have 250 calls right so what we  
**Translation:** Vocabulary: exploding: 爆炸性

**[7903.36s] English:** do is to take every inch of the machine not just that not just that we abuse the machine we go and  
**Translation:** 

**[7909.92s] English:** use we use the machine in ways that the the creator didn't expect sometimes we use an  
**Translation:** 

**[7915.12s] English:** instruction that's completely unrelated to what we do we use a cryptography instruction  
**Translation:** 

**[7919.52s] English:** video  
**Translation:** Vocabulary: cryptography: 密码学

**[7920.00s] English:** to do nothing related and one of the other things that we do for example in david which is a bit  
**Translation:** 

**[7925.72s] English:** crazy is that we don't use the function calling convention from the operating system we should  
**Translation:** 

**[7933.68s] English:** explain that that is extremely complex but basically usually when you do move from one  
**Translation:** 

**[7938.38s] English:** function in code to another there is a way to save the registry the state of the cpu to enter  
**Translation:** Vocabulary: registry: 寄存器状态

**[7944.86s] English:** another function and this is like standard it's a bit complex i would i would simplify this a bit  
**Translation:** 

**[7950.22s] English:** so so david does things to abuse the calling convention you could define the calling convention  
**Translation:** Vocabulary: simplify: 简化

**[7955.52s] English:** as i've written a function and i want to call another function how is the data shared between  
**Translation:** 

**[7961.44s] English:** the functions because there's a convention what's known as a calling convention and what david does  
**Translation:** 

**[7966.70s] English:** for optimal reasons is create its own calling convention sometimes so if i want to call  
**Translation:** 

**[7973.04s] English:** lex friedman's library we got  
**Translation:** Vocabulary: optimal: 最佳的

**[7974.76s] English:** you  
**Translation:** 

**[7974.86s] English:** got to agree on a convention so that i can share data with you in the assembly language space and  
**Translation:** 

**[7980.58s] English:** one of the challenges in assembly is every operating well not every operating system but  
**Translation:** 

**[7984.14s] English:** there are at least four that i can think of on x86 linux 32-bit windows 32-bit windows 64 linux 64  
**Translation:** 

**[7990.96s] English:** they all have their own calling conventions and so one of the amazing things lauren merritt did  
**Translation:** 

**[7996.16s] English:** who we talked about before was create a very lightweight abstraction layer so you could write  
**Translation:** Vocabulary: abstraction: 抽象层; conventions: 调用约定; lightweight: 轻量级

**[7999.92s] English:** your assembly code once and it handled all the calling convention stuff for you  
**Translation:** 

**[8004.86s] English:** which is always a problem because you had to manage four different variants but david takes  
**Translation:** 

**[8010.20s] English:** this even further for speed reasons it does its own calling convention um within itself  
**Translation:** 

**[8015.92s] English:** to bypass the kind of rules the rules of the rules of sort of functions and say okay actually i'm  
**Translation:** Vocabulary: bypass: 绕过

**[8021.76s] English:** going to call a function this way because i know it's within my library does there have to be special  
**Translation:** 

**[8026.28s] English:** to every single operating system well if it's custom no but the the challenge is in general  
**Translation:** 

**[8032.24s] English:** yes and in terms of in terms of each of the functions that are in the library and the  
**Translation:** 

**[8034.86s] English:** instruction set so the thing to also emphasize is we do this on every instruction set so every  
**Translation:** 

**[8039.54s] English:** instruction  
**Translation:** 

**[8040.00s] English:** has its own handwritten assembly which is even more crazy and that that that has um that matrix  
**Translation:** Vocabulary: handwritten: 手写; matrix: 矩阵

**[8045.84s] English:** has got bigger in recent years because of risk 5 because of arm 64 because of the new sve there's  
**Translation:** 

**[8052.44s] English:** sme x86 has avx 512 avx so we do runtime processor detection we see what the machine ffmpeg is  
**Translation:** Vocabulary: detection: 检测; processor: 处理器; runtime: 运行时

**[8061.40s] English:** running on or david's running on is capable of because you could be on a laptop from 2008 where  
**Translation:** 

**[8066.52s] English:** this isn't there runtime detection we set function pointers accordingly and then from then on off you  
**Translation:** Vocabulary: accordingly: 相应地

**[8073.60s] English:** go or you could be on a machine with risk 5 yes and in all that we don't even respect the calling  
**Translation:** 

**[8079.80s] English:** convention of the operating system in order to be faster because we know that we are going to be  
**Translation:** 

**[8084.86s] English:** called from within our binary so we can share data without saving all the registry in the common way  
**Translation:** 

**[8090.30s] English:** because that can lead to loading and saving registry on the l1 and l2 cpu and  
**Translation:** Vocabulary: binary: 二进制; registry: 注册表

**[8096.50s] English:** gets us faster so that's why i said that understanding cpu architecture computer  
**Translation:** 

**[8103.36s] English:** architecture is key and this is also why it's handwritten i don't know anyone i've never heard  
**Translation:** 

**[8108.22s] English:** any other project than david doing that this is what kiran calls he calls it an art right it is  
**Translation:** 

**[8113.92s] English:** an art i think i think in in a mass world there isn't something on billions of devices i know  
**Translation:** 

**[8118.52s] English:** there are some specialist industries i know in high frequency trading they take this really  
**Translation:** 

**[8122.32s] English:** seriously where they're receiving feeds from a market and they need to react within  
**Translation:** 

**[8126.50s] English:** x number of microseconds and so the instructions matter but that's not a mass you know a mass  
**Translation:** 

**[8131.74s] English:** produced thing that's on a billion devices that's hyper specialized running on hyper specialized  
**Translation:** Vocabulary: hyper: 过度; microseconds: 微秒

**[8135.42s] English:** hardware we're running on all hardware from sorry to linger on it but like that's a really  
**Translation:** 

**[8142.30s] English:** counterintuitive almost like revolutionary idea here that there's a huge amount of value to  
**Translation:** Vocabulary: counterintuitive: 逆常理的

**[8149.60s] English:** assembly like what are we supposed to take away from that like what you know there's a bunch of  
**Translation:** 

**[8153.78s] English:** people listening to this they're basically like  
**Translation:** 

**[8156.50s] English:** sorry from myself included you know i program  
**Translation:** 

**[8160.00s] English:** for many, many years in C, C++,  
**Translation:** 

**[8162.28s] English:** going up the standards of C++,  
**Translation:** 

**[8164.30s] English:** fell in love with C++, even the Meta program and so on,  
**Translation:** 

**[8166.66s] English:** and then transitioned more and more  
**Translation:** 

**[8168.16s] English:** because of machine learning about 15 years ago to Python.  
**Translation:** Vocabulary: transitioned: 转变

**[8172.08s] English:** And so, like, for me in this Python world,  
**Translation:** 

**[8175.04s] English:** JavaScript world, now vibe coding  
**Translation:** 

**[8178.46s] English:** where I'm just using natural language,  
**Translation:** 

**[8180.08s] English:** sitting in my jacuzzi, drinking a drink,  
**Translation:** Vocabulary: jacuzzi: 泡澡盆

**[8182.28s] English:** and just talking to the computer,  
**Translation:** 

**[8184.44s] English:** like, record stops.  
**Translation:** 

**[8187.06s] English:** Why is the value to go back  
**Translation:** 

**[8189.46s] English:** all the way down to the low level?  
**Translation:** 

**[8191.50s] English:** Because you can get more power per dollar invested, right?  
**Translation:** 

**[8196.46s] English:** And sometimes it's going to be a problem  
**Translation:** 

**[8199.16s] English:** that is limited by your hardware.  
**Translation:** 

**[8201.40s] English:** A good analogy is what you see in quantization in LLMs, right?  
**Translation:** Vocabulary: quantization: 量化过程

**[8206.86s] English:** And people are doing, oh, I'm going to do that in FP8  
**Translation:** 

**[8209.50s] English:** or FP4 or some crazy things like Microsoft Fear  
**Translation:** 

**[8213.72s] English:** who did it in 1.5  
**Translation:** 

**[8215.42s] English:** because you're constrained  
**Translation:** Vocabulary: constrained: 受到限制

**[8216.94s] English:** by memory, because you're constrained  
**Translation:** 

**[8218.72s] English:** by the machine you can run,  
**Translation:** 

**[8220.50s] English:** because at some point we are doing real time.  
**Translation:** 

**[8223.60s] English:** And I believe this is going to happen  
**Translation:** 

**[8225.24s] English:** on AI inference also,  
**Translation:** 

**[8227.00s] English:** is that at some point you need to get faster  
**Translation:** Vocabulary: inference: 推理

**[8229.34s] English:** and you cannot always get harder,  
**Translation:** 

**[8231.30s] English:** more powerful hardware, right?  
**Translation:** Vocabulary: cannot: 不能

**[8233.28s] English:** So you need to analyze code  
**Translation:** 

**[8235.86s] English:** and see where, like,  
**Translation:** 

**[8237.50s] English:** where is the mission critical?  
**Translation:** 

**[8239.10s] English:** Where is the things that are called non-stops?  
**Translation:** 

**[8241.68s] English:** And, for example, David is a good example.  
**Translation:** 

**[8244.08s] English:** It's going to be run billions  
**Translation:** 

**[8246.50s] English:** of hours per day.  
**Translation:** 

**[8248.54s] English:** That makes sense.  
**Translation:** 

**[8249.88s] English:** It doesn't make sense to be on the glue  
**Translation:** 

**[8252.00s] English:** of FFmpeg CLI.  
**Translation:** 

**[8254.26s] English:** It makes sense over there.  
**Translation:** 

**[8255.58s] English:** Yeah, this has to do,  
**Translation:** 

**[8256.54s] English:** also we'll talk about it more,  
**Translation:** 

**[8257.76s] English:** but your new F, your new company Kyber  
**Translation:** 

**[8260.56s] English:** is doing that kind of thing  
**Translation:** 

**[8263.08s] English:** for ultra low latency.  
**Translation:** Vocabulary: latency: 延迟; ultra: 超乎寻常的

**[8264.82s] English:** So the slogan being every millisecond counts.  
**Translation:** 

**[8267.48s] English:** And when you're actually  
**Translation:** Vocabulary: millisecond: 毫秒

**[8268.18s] English:** extremely highly constrained  
**Translation:** 

**[8270.58s] English:** in some dimension.  
**Translation:** Vocabulary: dimension: 维度

**[8273.14s] English:** We are also arriving at a point  
**Translation:** 

**[8274.74s] English:** where we've done everything  
**Translation:** 

**[8277.20s] English:** So many great things,  
**Translation:** 

**[8278.60s] English:** but the hardware is getting  
**Translation:** 

**[8280.00s] English:** back to us right because cost is increasing because we need more power and so you're limited  
**Translation:** 

**[8285.60s] English:** by either your cpu your ram or your networking and you need to optimize and this is where  
**Translation:** Vocabulary: optimize: 优化

**[8293.04s] English:** value is going to be especially because like doing ai is going to help do the programming of like  
**Translation:** 

**[8299.52s] English:** business right and so the core thing that you will not be able to vibe code are optimization  
**Translation:** 

**[8307.60s] English:** for the all the way out to be as fast as possible i'd love to talk to you about who and how  
**Translation:** 

**[8314.48s] English:** should learn assembly but first i think we need a bathroom break  
**Translation:** 

**[8318.80s] English:** quick 10 second thank you to our sponsors check them out in the description it really is the best  
**Translation:** 

**[8323.44s] English:** way to support this podcast go to alexfriedman.com sponsors and now back to the episode all right and  
**Translation:** Vocabulary: sponsors: 赞助商

**[8331.84s] English:** we're back there's this uh nice repo with the assembly lessons first of all do you  
**Translation:** 

**[8337.52s] English:** think you're going to be able to do a lot of things in the next couple of weeks or do you  
**Translation:** 

**[8337.56s] English:** think you're going to be able to do a lot of things in the next couple of weeks or do you  
**Translation:** 

**[8337.58s] English:** think you're going to be able to do a lot of things in the next couple of weeks or do you think you're  
**Translation:** 

**[8337.60s] English:** think you're going to be able to do a lot of things in the next couple of weeks or do you think developers should learn how to program an assembly and how would you go about learning it what is this asm dash lessons so i personally wasn't happy with the way assembly is taught in books and online because it's very grammar focused and you don't in general learn a language from learning the grammar and the structure you learn a language by asking someone what their name is and you start from there and you go and solve real problems  
**Translation:** 

**[8367.58s] English:** you don't you don't learn sentence structure this is the interrogative and the adverb and all the assembly books seem to be doing like going through every instruction even ones that aren't really relevant explaining what they all do and how they actually doesn't really change much so and the other problem that we have in our community is assembly is taught sort of hand to hand like person to person like blacksmithing one by one that's the only logical sort of analogy and that doesn't really scale online it doesn't um the other thing so  
**Translation:** Vocabulary: blacksmithing: 手工锻造; interrogative: 疑问词

**[8397.56s] English:** this this this this i started  
**Translation:** 

**[8400.00s] English:** a set of assembly lessons in the in the way it's done in ffmpeg which is a little bit different to  
**Translation:** 

**[8404.68s] English:** the way assembly in general for i'm trying to think the other good big use case of assembly  
**Translation:** 

**[8411.16s] English:** is in embedded devices in really really low power cheap devices and that's completely different to  
**Translation:** 

**[8416.10s] English:** what we're doing here i think it would be good if you could highlight the requirements which are  
**Translation:** 

**[8419.84s] English:** quite simple it's high school mathematics and c and actually not even c really really it's pointers  
**Translation:** 

**[8425.02s] English:** to emphasize yes we've talked about how brilliant this stuff is but high schoolers like daniel kang  
**Translation:** 

**[8430.74s] English:** have written um assembly in ffmpeg i think there's been contributions because of these lessons  
**Translation:** Vocabulary: schoolers: 中学生

**[8436.80s] English:** so it's really about trying to get this dying art to continue because we've shown it's possible  
**Translation:** 

**[8444.02s] English:** with david to produce something amazing there's still a lot of codecs in ffmpeg that are only  
**Translation:** 

**[8448.84s] English:** maybe partially assembly um assembly optimized and so it really it really starts with basic  
**Translation:** 

**[8455.02s] English:** and continues explains a lot of the jargon a lot of the syntax it doesn't really try and explain to  
**Translation:** Vocabulary: jargon: 行话; optimized: 优化; syntax: 语法

**[8460.76s] English:** you you know interrupt handlers and interrupt instructions and all of these different jump  
**Translation:** 

**[8465.78s] English:** targets it actually makes this really vector focused and uh describes all kinds of registers  
**Translation:** 

**[8470.92s] English:** general purpose registers vector registers uh really nice examples this is cool it's a classic  
**Translation:** 

**[8479.02s] English:** classic example of ffmpeg but um some of this assembly language is is really beautiful and i  
**Translation:** 

**[8484.28s] English:** think it's beautiful and i think it's beautiful and i think it's beautiful and i think it's beautiful  
**Translation:** 

**[8485.02s] English:** because it's kind of like flying a spitfire it's really aviation at its purest but also pushing  
**Translation:** Vocabulary: spitfire: 喷火战斗机

**[8491.76s] English:** the aircraft beyond what the designer thought was possible so we're abusing for example sometimes  
**Translation:** 

**[8497.74s] English:** cryptography instructions to do certain things and there's a level of beauty and art where  
**Translation:** Vocabulary: cryptography: 加密技术

**[8503.02s] English:** it's really you and the processor there's there's there's nothing in between it's you and the the  
**Translation:** 

**[8509.96s] English:** joystick of the cockpit and you move that joystick and it's physically collected to the earlier ones  
**Translation:** Vocabulary: cockpit: 驾驶舱; joystick: 操纵杆; processor: 处理器

**[8514.14s] English:** and you can push that plane beyond what it can normally do and there's a level of  
**Translation:** 

**[8520.00s] English:** yeah beauty and amazingness to go that but i don't think the sort of person by person assembly  
**Translation:** Vocabulary: amazingness: 惊奇之处

**[8527.24s] English:** that someone taught me and i've taught multiple people is gonna work long run because of the  
**Translation:** 

**[8534.36s] English:** particular flavor and the way that we do it it's literally uh no i should i was gonna say  
**Translation:** 

**[8540.16s] English:** wizards handing it down i realized i look like a wizard wearing this hat but you're basically  
**Translation:** 

**[8544.96s] English:** just like the sages the wise sages handing down the craft can i ask about llms like can they help  
**Translation:** 

**[8552.04s] English:** they had more of an understanding than i expected but they are still i've asked it questions and it  
**Translation:** 

**[8557.68s] English:** still goes and starts hallucinating not hallucinating but making modifications and then i  
**Translation:** Vocabulary: modifications: 修改

**[8563.18s] English:** go is it bit exact no fix it and then it just goes and does the same thing and it's going it there  
**Translation:** 

**[8569.12s] English:** isn't the corpus of information like stack overflow to work on there is not enough data to train on  
**Translation:** Vocabulary: overflow: 溢出问题

**[8574.94s] English:** um and this is the biggest issue um i started my career actually doing some uh assembly for  
**Translation:** 

**[8582.70s] English:** titanium right so the titanium is a dead um processor type right which was done by intel  
**Translation:** Vocabulary: titanium: 钛金属

**[8588.00s] English:** a long time ago when they wanted to do 64 bits uh well they lost and then we got amd who did it  
**Translation:** 

**[8594.58s] English:** amd 64 which became x64 but titanium was extremely interesting in the sense that  
**Translation:** 

**[8601.56s] English:** those were processors who had a ton of computing  
**Translation:** 

**[8604.94s] English:** power to do floats fmas which is similar to what we need now for for llms right and you could pack  
**Translation:** Vocabulary: computing: 计算; processors: 处理器

**[8613.04s] English:** three operations per line that could be loaded so basically you had an output of basically six  
**Translation:** 

**[8619.74s] English:** billion of operation per second but the bus um the memory bus only allowed 1.5 right so your cpu was  
**Translation:** 

**[8629.24s] English:** four times faster so you had to do crazy things to to pack things in memory reuse the  
**Translation:** 

**[8634.94s] English:** cpu was registered and those type of semantics no language could do that right so um  
**Translation:** Vocabulary: reuse: 重复使用; semantics: 语义

**[8640.00s] English:** like i i have the italian programming uh book because intel did amazing books but that's  
**Translation:** 

**[8647.06s] English:** exactly what kieran says if you don't know what you're you're going to do it's impossible to read  
**Translation:** Vocabulary: kieran: 凯利安

**[8653.14s] English:** right it's a ton of jargon and so on while those lessons are amazing because they are targeted to  
**Translation:** 

**[8659.60s] English:** a real problem and you can do it yourself people have people have their patches and i studied your  
**Translation:** Vocabulary: jargon: 行话

**[8664.32s] English:** lessons and here's my first changes that's amazing and part of that in the lessons is a framework  
**Translation:** 

**[8670.48s] English:** called x86 inc written by lauren when we was working on x264 and it allows you to do more  
**Translation:** 

**[8678.10s] English:** things about that to create a type of like not caring too much about different calling convention  
**Translation:** 

**[8683.80s] English:** and we had a lot of students who gave code to x264 using uh that a long time ago right so  
**Translation:** 

**[8692.16s] English:** it's really doable and  
**Translation:** 

**[8694.16s] English:** i  
**Translation:** Vocabulary: doable: 可行的

**[8694.30s] English:** believe it's um necessarily to understand uh assembly language even if you don't do it much  
**Translation:** 

**[8701.90s] English:** to understand what's going on inside your computer and that will make you a better programmer  
**Translation:** 

**[8707.02s] English:** and i assure you that because doing that you will understand some of the  
**Translation:** 

**[8710.78s] English:** architecture of the memory inside your your computer right understanding register at one  
**Translation:** 

**[8715.90s] English:** l203 rams ssds disk and so on which are very important because then you have a good program  
**Translation:** 

**[8724.14s] English:** programming culture that will make you a better programmer uh what do you think about the rust  
**Translation:** Vocabulary: programmer: 程序员

**[8728.62s] English:** programming language because that's a bit of a meme we have very different opinions with kieran i think  
**Translation:** 

**[8733.66s] English:** it's valuable what they're doing in terms of memory safety as a concept can you achieve this some of  
**Translation:** 

**[8739.98s] English:** the speed up that assembly achieves not assembly by hand no i think that's a given c potentially  
**Translation:** 

**[8745.82s] English:** but i see it very it has a very big esperanto vibe about it it's like we're gonna solve this and  
**Translation:** Vocabulary: esperanto: 人造语言

**[8752.46s] English:** we're doing this in a particular way  
**Translation:** 

**[8754.46s] English:** meaning it's a bit too utopian so there's a lot of focus on the  
**Translation:** Vocabulary: utopian: 空想的

**[8757.58s] English:** self-importance rather than solving real-world problems  
**Translation:** 

**[8760.00s] English:** problems it reminds me of the Sinclair C5 Sir Clive Sinclair of Sinclair Computers built a car  
**Translation:** 

**[8765.80s] English:** and he said oh everyone will be traveling around in in one of these electric cars and it was um  
**Translation:** 

**[8772.18s] English:** Frost reminds me of that where I think the community doesn't the community doesn't quite  
**Translation:** 

**[8777.40s] English:** understand that in order to get people to move you have to build something that's as good as  
**Translation:** 

**[8782.44s] English:** if not better than what you have now um yes people are doing Rust rewrites but if they're  
**Translation:** Vocabulary: rewrites: 重写代码

**[8788.52s] English:** if they only if they only do 85 90 percent of the feature set of what what we need like things  
**Translation:** 

**[8795.24s] English:** like core utils that last one percent takes 99 percent of the time um to use Elon's famous quote  
**Translation:** 

**[8801.50s] English:** prototypes are easy like this kind of stuff is easy but this to get a real electric car you have  
**Translation:** 

**[8805.88s] English:** to make a car as good as if not better than what we have now and Rust isn't in that stage yet I  
**Translation:** Vocabulary: prototypes: 样品

**[8811.08s] English:** think we I don't think anyone would object to seeing Rust code in FFmpeg but it needs to work  
**Translation:** 

**[8817.70s] English:** as well and support it and I think that's a big part of it and I think that's a big part of it  
**Translation:** 

**[8818.52s] English:** and I think that's a big part of it and I think that's a big part of it and I think that's a big part  
**Translation:** 

**[8818.56s] English:** of it and I think that's a big part of it and I think that's a big part of it and I think it's  
**Translation:** 

**[8819.52s] English:** important to support the same unit testing as everything else it needs to be flawless it can't  
**Translation:** 

**[8822.64s] English:** just randomly break they can't just randomly break ABI when they want to it needs to it needs to have  
**Translation:** Vocabulary: flawless: 完美无缺

**[8828.16s] English:** I think more I think you know it still has only one compiler implementation yes so it's got to be  
**Translation:** 

**[8834.74s] English:** as good as if not better and saying hey here's my utopia of memory safety isn't enough even though  
**Translation:** Vocabulary: implementation: 实现; utopia: 乌托邦

**[8841.00s] English:** we probably all agree that that's the goal so um I've done a ton of Rust in the two major  
**Translation:** 

**[8848.52s] English:** I had was adding Rust modules inside VLC.  
**Translation:** 

**[8852.30s] English:** One of the reasons VLC got popular  
**Translation:** 

**[8854.68s] English:** and which was one of the main architecture decision  
**Translation:** 

**[8857.62s] English:** is that VLC is a very small core and a ton of modules, right?  
**Translation:** 

**[8861.28s] English:** And so you can write modules in C++, in Objective-C  
**Translation:** 

**[8867.24s] English:** and anything that is basically interoperable with C.  
**Translation:** 

**[8870.40s] English:** And so we did some Rust modules.  
**Translation:** Vocabulary: interoperable: 可以互操作的

**[8874.04s] English:** And so I have experience on that and I wrote some of it.  
**Translation:** 

**[8877.08s] English:** And also like my new startup called Kyber is an open-  
**Translation:** 

**[8880.00s] English:** source project mainly done in rust um what rust is extremely good in in the sense that um  
**Translation:** 

**[8888.58s] English:** it's a better c++ that cares about memory and allows you to do things about memory ownership  
**Translation:** 

**[8895.26s] English:** that no one else can do so far however it's great when you start a new project from scratch and you  
**Translation:** 

**[8903.16s] English:** do everything in rust but it's very not good when you interrupt with the existing part and  
**Translation:** 

**[8909.82s] English:** some part of the rust community believe that they need to rewrite everything and everything will be  
**Translation:** 

**[8914.54s] English:** better with rust and and the answer is like no like i'm almost always and all my years of being  
**Translation:** 

**[8922.40s] English:** engineer manager city of startup and so on don't rewrite right is that that's the that's the  
**Translation:** 

**[8929.48s] English:** initial instinct for a lot of people when they show up to a code base  
**Translation:** Vocabulary: instinct: 初始反应

**[8932.78s] English:** probably before llms is like probably because they don't understand the the the wisdom of the  
**Translation:** 

**[8940.90s] English:** way things have been done in the past to say well we need to rewrite it hence why there's a thousand  
**Translation:** 

**[8945.12s] English:** javascript frameworks but the reason is the following and this is very important to understand  
**Translation:** 

**[8950.60s] English:** it is an order of magnitude easier to write code than read code yeah and you see that also with  
**Translation:** 

**[8957.86s] English:** llm they can wipe code that analyzing is a lot more  
**Translation:** 

**[8962.76s] English:** difficult and so when you arrive and when you arrive to a very complex piece of code right you  
**Translation:** 

**[8969.46s] English:** you don't understand it right um because it's so much more effort to understand the code from  
**Translation:** 

**[8974.92s] English:** someone else because you don't have the thought process um and often i joke about um some some  
**Translation:** 

**[8981.50s] English:** languages mostly uh pearl for example um which has very complex syntax and imagine i am at my  
**Translation:** 

**[8988.54s] English:** maximum intellectual efficiency in programming right  
**Translation:** Vocabulary: syntax: 语法规则

**[8992.76s] English:** and i write the best code ever i will not be able to understanding myself six months later right  
**Translation:** 

**[8998.52s] English:** because reading code  
**Translation:** 

**[9000.00s] English:** is more difficult. So, very often you arrive, you don't understand all the wisdom, all the  
**Translation:** 

**[9005.44s] English:** business logic, the reasons that were done that is maybe not documented. And you say, well, I'm  
**Translation:** 

**[9010.48s] English:** going to rewrite it. And the thing is, no, you don't, right? Because that's, as Kiran said,  
**Translation:** 

**[9015.56s] English:** right, I'm going to rewrite core utils in Rust. And then, of course, you arrive very quickly at  
**Translation:** 

**[9020.20s] English:** 80%, then 90%, takes a bit more time, and then you got the last ones, right? On the other side,  
**Translation:** 

**[9028.38s] English:** so for new projects, it's great. Everything related to parsing files, networking, because of  
**Translation:** Vocabulary: parsing: 解析

**[9035.18s] English:** the memory checker, memory checker, it's amazing and there is nothing else. To answer a bit  
**Translation:** 

**[9040.96s] English:** differently for us, imagine I take a piece of software like David or x264, right, which has a  
**Translation:** 

**[9049.70s] English:** ton of runtime in assembly, right? I rewrite the C part in Rust, right? So, it's more secure. Yes,  
**Translation:** 

**[9056.86s] English:** but then you arrive into the...  
**Translation:** 

**[9058.38s] English:** assembly and you can jump anywhere in the memory because we are doing handwritten assembly. So,  
**Translation:** 

**[9064.08s] English:** even if I rewrite the C part in Rust for security reason, you break all the security when you  
**Translation:** Vocabulary: handwritten: 手工编写

**[9072.78s] English:** write handwritten assembly because we can jump anywhere. So, in my opinion, we need to do  
**Translation:** 

**[9078.28s] English:** something that is secure assembly, right? So, which is compile time, check the assembly, which  
**Translation:** 

**[9085.24s] English:** is similar to the check assembly project that we're doing.  
**Translation:** 

**[9088.38s] English:** Yeah.  
**Translation:** 

**[9089.20s] English:** on David and x264 with Video LAN, is to start instrumenting your assembly at compile time to  
**Translation:** 

**[9097.24s] English:** check that it's not jumping anywhere in the memory. Because else you might rewrite a part of C in Rust,  
**Translation:** 

**[9102.96s] English:** but if you want to have the same performances, you're going to have inline assembly, and so you  
**Translation:** 

**[9106.44s] English:** destroy your whole security model. So, that's a bit what I think about Rust.  
**Translation:** Vocabulary: inline: 嵌入式

**[9111.34s] English:** I just want to... I would say on a personal level, I am so in awe about assembly. I actually  
**Translation:** 

**[9116.38s] English:** . . .  
**Translation:** 

**[9117.38s] English:** once in a while it never gets old the speed  
**Translation:** 

**[9120.00s] English:** improvements to show 62x uh there are months on a personal level i run our internal test suite at  
**Translation:** 

**[9127.46s] English:** work and just see i'm still in awe of the gains we have there's a source of joy and happiness  
**Translation:** 

**[9132.44s] English:** programming for different reasons but i think one of the greatest happinesses is in the optimization  
**Translation:** Vocabulary: happinesses: 幸福感; optimization: 优化

**[9140.02s] English:** of code and it sounds like you're like at the cutting edge of that that was cool in the community  
**Translation:** 

**[9146.46s] English:** i want to speak about two people who are wizards of assembly right the two of them are actually  
**Translation:** 

**[9153.98s] English:** working uh living in north of europe uh sweden in finland and um henrik gramner knows so much  
**Translation:** 

**[9164.46s] English:** about intel x86 assembly that when we ask questions at intel about things they tell  
**Translation:** 

**[9172.18s] English:** like why are you asking us intel you have henrik henrik knows better  
**Translation:** 

**[9176.46s] English:** he knows all the cycles of almost all the simd instruction by all the cpu generation oh yes this  
**Translation:** Vocabulary: henrik: 亨里克

**[9184.82s] English:** is a p4 this is a nehalem this is a core 2 etc that person is like the best person on assembly  
**Translation:** 

**[9191.40s] English:** in the world and he's the nicest person that you've seen like you're very he arrived you don't  
**Translation:** 

**[9199.34s] English:** see he's amazing and the other one is is called martin martin stossio and he's the  
**Translation:** 

**[9206.46s] English:** best person in the world and he's doing mostly the same on arm right so neon right and iphones and  
**Translation:** 

**[9211.92s] English:** android and so on and he codes in assembly on his phone editing it with the crappy uh uh keyboard  
**Translation:** 

**[9223.66s] English:** like virtual keyboard you have while watching his kids play in the playground right like like  
**Translation:** Vocabulary: crappy: 糟糕的键盘

**[9229.58s] English:** this is just like wizard level so those two people are like yes  
**Translation:** 

**[9236.46s] English:** apart when you're programming assembly at that high level  
**Translation:** 

**[9240.00s] English:** a part of that is knowing the architecture  
**Translation:** 

**[9242.10s] English:** that you're programming on.  
**Translation:** 

**[9243.02s] English:** On ARM in particular, yes.  
**Translation:** 

**[9244.82s] English:** ARM in particular.  
**Translation:** 

**[9246.60s] English:** But these are complicated architectures, right?  
**Translation:** 

**[9249.28s] English:** Yeah, but ARM in some ways is more...  
**Translation:** 

**[9252.34s] English:** x86 with out-of-order execution is not so bad.  
**Translation:** 

**[9255.42s] English:** ARM, you really need to understand  
**Translation:** 

**[9256.76s] English:** all the different generations of ARM processor  
**Translation:** 

**[9259.16s] English:** because they're all different.  
**Translation:** 

**[9260.24s] English:** There's A72, et cetera, et cetera.  
**Translation:** 

**[9263.12s] English:** And there's the Apple variant.  
**Translation:** 

**[9264.34s] English:** There's this variant.  
**Translation:** 

**[9264.94s] English:** And you need to write code that works efficiently on all of them.  
**Translation:** Vocabulary: efficiently: 高效地

**[9268.28s] English:** x86, well, broadly speaking, you have Intel AMD,  
**Translation:** 

**[9271.10s] English:** you have sub-variants,  
**Translation:** 

**[9272.10s] English:** but generally speaking,  
**Translation:** 

**[9274.60s] English:** there's something fast that's going to remain fast  
**Translation:** 

**[9277.78s] English:** on all of the variants,  
**Translation:** 

**[9279.14s] English:** whereas in ARM, it's a completely much more complicated ballgame.  
**Translation:** Vocabulary: ballgame: 复杂局面

**[9283.14s] English:** We're taking a nonlinear journey through history here,  
**Translation:** 

**[9286.42s] English:** but we're talking about Michael Niedermeyer.  
**Translation:** 

**[9290.34s] English:** I wanted to ask about this.  
**Translation:** 

**[9294.00s] English:** For a time, there was a split in FFmpeg  
**Translation:** 

**[9298.04s] English:** and...  
**Translation:** 

**[9298.28s] English:** LibAV.  
**Translation:** 

**[9300.48s] English:** Yes.  
**Translation:** 

**[9300.98s] English:** So in open-source projects,  
**Translation:** 

**[9304.46s] English:** sometimes you disagree, right?  
**Translation:** 

**[9310.14s] English:** That's such a nice way of putting it, yeah.  
**Translation:** 

**[9312.28s] English:** And the good thing is because of the license,  
**Translation:** 

**[9314.38s] English:** you're allowed to basically do your own, right?  
**Translation:** 

**[9317.62s] English:** And this is normal,  
**Translation:** 

**[9319.16s] English:** and this has happened all the time, right?  
**Translation:** 

**[9321.10s] English:** At the point, there was GCC at the time of GCC2 and EGCS,  
**Translation:** 

**[9326.64s] English:** which became then...  
**Translation:** 

**[9328.28s] English:** GCC3, right?  
**Translation:** 

**[9329.38s] English:** There is what we told KHTML with WebKit, with Blink.  
**Translation:** 

**[9333.64s] English:** It is a sane process.  
**Translation:** 

**[9335.76s] English:** And also, like, when I want to do a new feature today in VLC,  
**Translation:** 

**[9339.14s] English:** I fork, I do my thing on my own,  
**Translation:** 

**[9341.00s] English:** and then I merge back to the community.  
**Translation:** 

**[9343.12s] English:** So there was a split in the open-source community on FFmpeg,  
**Translation:** 

**[9346.06s] English:** which become LibAV and FFmpeg.  
**Translation:** 

**[9348.24s] English:** And after a few years, well, the community merged back  
**Translation:** 

**[9351.02s] English:** and people moved on.  
**Translation:** 

**[9352.32s] English:** It's a bit drama that is normal in open-source community,  
**Translation:** 

**[9357.76s] English:** but folks are even...  
**Translation:** 

**[9360.00s] English:** important because they change the status quo of a community. Not talking about FFmpeg and eBV here,  
**Translation:** 

**[9368.88s] English:** but the GCC fork made GCC a ton better because some people wanted to change the architecture  
**Translation:** 

**[9376.16s] English:** fundamentally to make it faster. And of course, it's always a question of people and so on,  
**Translation:** 

**[9381.92s] English:** but in the end, you realize that FFmpeg today is better than it was before the fork.  
**Translation:** Vocabulary: fundamentally: 从根本上

**[9388.24s] English:** And now, well, we're back all together, right? And I spend a lot of time in the community.  
**Translation:** 

**[9397.60s] English:** It's not often, to be honest, very well explained because a ton of the reasons are not very public,  
**Translation:** 

**[9405.68s] English:** but I think that's normal and that's good. Yeah. I mean, you're making it sound really  
**Translation:** 

**[9411.20s] English:** nice, but there's pretty heated battles inside open-source projects. I mean,  
**Translation:** 

**[9415.04s] English:** it is a very passionate community and you're kind of an  
**Translation:** 

**[9418.16s] English:** open-source community and you're kind of an open-source community and you're kind of an  
**Translation:** 

**[9418.22s] English:** open-source community and you're kind of an open-source community and you're kind of an  
**Translation:** 

**[9418.24s] English:** open-source community and you're kind of an open-source community and you're kind of an  
**Translation:** 

**[9418.26s] English:** open-source community and you're kind of an open-source community and you're kind of an  
**Translation:** 

**[9418.30s] English:** distributed way have to define the direction of things.  
**Translation:** 

**[9421.58s] English:** distributed way have to define the direction of things.  
**Translation:** 

**[9421.62s] English:** distributed way have to define the direction of things. So here, looking at perplexity,  
**Translation:** Vocabulary: perplexity: 困惑程度

**[9424.10s] English:** So here, looking at perplexity,  
**Translation:** 

**[9424.14s] English:** So here, looking at perplexity, FFmpeg and LibAV split in 2011,  
**Translation:** 

**[9427.10s] English:** FFmpeg and LibAV split in 2011,  
**Translation:** 

**[9427.14s] English:** FFmpeg and LibAV split in 2011, mainly over project governance,  
**Translation:** Vocabulary: governance: 管理方式

**[9428.50s] English:** mainly over project governance,  
**Translation:** 

**[9428.54s] English:** mainly over project governance, leadership style and development  
**Translation:** 

**[9429.82s] English:** leadership style and development  
**Translation:** 

**[9429.86s] English:** leadership style and development processes not because of a fundamental  
**Translation:** 

**[9431.50s] English:** processes not because of a fundamental  
**Translation:** 

**[9431.52s] English:** processes not because of a fundamental technical disagreement.  
**Translation:** 

**[9433.66s] English:** technical disagreement.  
**Translation:** 

**[9433.68s] English:** ffmpeg effectively absorbed libav's work while libav withered their most distributions and  
**Translation:** 

**[9440.08s] English:** developers moved back to ffmpeg yeah that was a that was a weird that was from a user's perspective  
**Translation:** 

**[9445.28s] English:** that was a weird experience because you know i'm a linux user so you know whether it's a bantu and  
**Translation:** 

**[9450.64s] English:** so on all of a sudden i think for for for a little bit bantu i feel like am i remembering correctly  
**Translation:** 

**[9457.44s] English:** switched to libav 12 14 something like that yeah something like that and then they switched back  
**Translation:** Vocabulary: bantu: 班图人

**[9462.00s] English:** to ffmpeg i was like what is happening so on the sort of you you get to feel the ripple effects  
**Translation:** 

**[9469.60s] English:** of the different internal debates that are happening to be fair on apple when you type gcc  
**Translation:** Vocabulary: ripple: 波纹效应

**[9475.20s] English:** you get c lang like they did something like that as well so yeah so to me  
**Translation:** 

**[9480.00s] English:** It's like the fork was like heated drama,  
**Translation:** 

**[9484.16s] English:** but most of the development from Libby was merged back into FFmpeg, right?  
**Translation:** 

**[9488.80s] English:** So de facto, FFmpeg got a superset around Libby.  
**Translation:** Vocabulary: facto: 实际上; libby: 利比

**[9492.78s] English:** And so that gave the user, because in the end,  
**Translation:** 

**[9495.34s] English:** we worked for the users, a larger set of features  
**Translation:** 

**[9498.62s] English:** and a ton of things that were discussed.  
**Translation:** 

**[9502.58s] English:** For example, the debate on reviews and on how we push  
**Translation:** 

**[9506.00s] English:** are something that now is completely settled in FFmpeg  
**Translation:** 

**[9509.50s] English:** and is following mostly what everyone in the community agrees, right?  
**Translation:** 

**[9515.06s] English:** So de facto, everyone who was active on Libby came back  
**Translation:** 

**[9519.58s] English:** and worked on FFmpeg because the disagreements were fixed.  
**Translation:** Vocabulary: disagreements: 分歧

**[9524.50s] English:** And in the end, FFmpeg is stronger than it was before, right?  
**Translation:** 

**[9528.94s] English:** And I know people love drama, but...  
**Translation:** 

**[9532.12s] English:** Well, my main concern, I understand,  
**Translation:** 

**[9535.44s] English:** and I think looking at the long history,  
**Translation:** 

**[9539.00s] English:** it's all...  
**Translation:** 

**[9539.50s] English:** It's all for the good.  
**Translation:** 

**[9541.88s] English:** But I am concerned because there's so few humans  
**Translation:** 

**[9545.48s] English:** that are critical to the success of open source projects  
**Translation:** 

**[9549.46s] English:** that I have seen it be a psychological toll on folks  
**Translation:** 

**[9555.06s] English:** and sometimes leads to burnout.  
**Translation:** 

**[9558.34s] English:** So you have these incredible people  
**Translation:** 

**[9559.72s] English:** that are at the core of open source projects.  
**Translation:** 

**[9562.48s] English:** There is a moment that happens  
**Translation:** 

**[9563.92s] English:** because what is the motivation of doing it?  
**Translation:** 

**[9566.16s] English:** Ultimately, it's because you're passionate about it  
**Translation:** 

**[9568.02s] English:** and it makes you happy.  
**Translation:** 

**[9568.90s] English:** And at a certain point, you wake up and it's like,  
**Translation:** 

**[9571.10s] English:** this has been a bit too much heat from the drama.  
**Translation:** 

**[9574.84s] English:** So at the project level,  
**Translation:** 

**[9577.46s] English:** the project continues and often flourishes.  
**Translation:** Vocabulary: flourishes: 蓬勃发展

**[9579.94s] English:** But sometimes there's these individual humans  
**Translation:** 

**[9582.28s] English:** that are just like, I've had enough.  
**Translation:** 

**[9585.20s] English:** Yeah, but it's not just about folks, right?  
**Translation:** 

**[9586.88s] English:** So it's very...  
**Translation:** 

**[9588.24s] English:** What you are referring to  
**Translation:** 

**[9591.16s] English:** is one of the most challenging  
**Translation:** 

**[9593.40s] English:** and most interesting part of open source today  
**Translation:** 

**[9596.06s] English:** is maintainers' burden.  
**Translation:** Vocabulary: maintainers: 维护者

**[9598.90s] English:** Burnout, right?  
**Translation:** 

**[9599.74s] English:** Mm-hmm.  
**Translation:** Vocabulary: burnout: 职业倦怠

**[9600.00s] English:** And AI is a problem because of that.  
**Translation:** 

**[9603.46s] English:** And Daniel Steinberg, which is the maintainer of Curl, who's probably one of the best promoters of open source in the world.  
**Translation:** Vocabulary: maintainer: 维护者; promoters: 推广者

**[9612.42s] English:** He's, by the way, a member of the European Open Source Academy with me.  
**Translation:** 

**[9616.00s] English:** So I'm very, like, humble to be on the same community as him, right?  
**Translation:** 

**[9619.22s] English:** He's against what he called AI slop, right?  
**Translation:** 

**[9621.78s] English:** Because it gives a ton of fake reports or bad reports, bad patches.  
**Translation:** 

**[9628.46s] English:** And then a lot of maintainers have a lot of burden to maintain the software.  
**Translation:** 

**[9634.38s] English:** And this is straining the mind of open source developers much more than folks.  
**Translation:** Vocabulary: straining: 耗费脑力

**[9642.74s] English:** And for example, the XZ fiasco was because there was one guy maintaining it.  
**Translation:** 

**[9647.94s] English:** And he got basically hammered by two attackers who were asking him questions nonstop at weird times at night to block him.  
**Translation:** Vocabulary: fiasco: 灾难; hammered: 打击

**[9655.58s] English:** And at some point, he got fed up and said, OK, I can't do that.  
**Translation:** 

**[9658.46s] English:** And gave the commit access to the attackant.  
**Translation:** Vocabulary: attackant: 攻击者

**[9662.10s] English:** So burnout in open source community is something that exists.  
**Translation:** 

**[9667.20s] English:** But mostly it's about maintaining things, right?  
**Translation:** 

**[9671.42s] English:** No, for sure.  
**Translation:** 

**[9672.06s] English:** I wonder how we would help that because those people are so important.  
**Translation:** 

**[9675.90s] English:** The human beings are so important.  
**Translation:** 

**[9677.54s] English:** The core of these projects.  
**Translation:** 

**[9679.02s] English:** So, for example, now I am maintaining a ton of multimedia and non-multimedia library as maintainer because the maintainers got fed up, right?  
**Translation:** 

**[9688.62s] English:** Some on Videoland, some outside of Videoland, because it's sometimes you need a tough skin, right?  
**Translation:** Vocabulary: multimedia: 多媒体; videoland: 视频之地

**[9696.32s] English:** Because you get like, it's not really attacks, but, oh, this is not working.  
**Translation:** 

**[9700.42s] English:** This is not working.  
**Translation:** 

**[9701.16s] English:** And you feel it personally.  
**Translation:** 

**[9702.70s] English:** And this is also why resources or the Google fiasco is, was a problem, right?  
**Translation:** 

**[9709.24s] English:** They don't realize that in the end you have, you know, it's like the same graph where you see like everything and it's just like one random open source project that is made.  
**Translation:** 

**[9718.10s] English:** He's maintaining the whole thing.  
**Translation:** 

**[9720.00s] English:** internet you see the one right yeah this is the meme i mean it applies to a lot of projects but  
**Translation:** 

**[9725.94s] English:** this is the all modern digital multimedia infrastructure and then that thing at the  
**Translation:** 

**[9731.38s] English:** very bottom that everything relies on is ffmpeg it's true and then there's usually you know a  
**Translation:** 

**[9737.62s] English:** handful of folks that are maintaining that and ffmpeg or vlc right you have a community of 10  
**Translation:** 

**[9743.24s] English:** 15 core developers are not the worst open source project exe which is even in more installations  
**Translation:** 

**[9749.82s] English:** is one person right there is one guy libxml is yeah libxml right there was a big stop no one is  
**Translation:** 

**[9756.38s] English:** maintaining libxml anymore which is like past the only library that is able to pass xml everywhere  
**Translation:** 

**[9761.26s] English:** all the crazy edge cases of xml under ridiculous circumstances and they get attacked by security  
**Translation:** 

**[9767.04s] English:** researchers because there's one other crazy edge case that they haven't thought of yeah but  
**Translation:** 

**[9771.84s] English:** the body of knowledge to actually resolve that is massive there is one guy maintaining all the  
**Translation:** 

**[9778.16s] English:** time zones for everyone who  
**Translation:** 

**[9779.82s] English:** is in the middle of i think was it nebraska or south dakota like the mental health of the open  
**Translation:** 

**[9786.92s] English:** source maintainers is something that large corporations don't care or don't see right  
**Translation:** 

**[9792.30s] English:** it's just like oh yeah i'm just doing an open source uh report and so on some of it is financial  
**Translation:** Vocabulary: maintainers: 维护者

**[9797.80s] English:** but some of it and people should definitely support open source financially all across the  
**Translation:** 

**[9803.72s] English:** board but some of it is also like spiritual on a basic human level there's something that happens  
**Translation:** Vocabulary: financially: 经济上

**[9809.82s] English:** like with this image of a ffmpeg and so much of the internet depending on it where people almost  
**Translation:** 

**[9815.10s] English:** like talk down to the folks who are carrying these projects forward and maintaining the security  
**Translation:** 

**[9821.40s] English:** community they certainly did that was one of that was one of the things i think that argument came  
**Translation:** 

**[9825.56s] English:** out is there was there was a portion of the security communities like no these guys write  
**Translation:** 

**[9830.66s] English:** crap code they need to fix their crap code i'm like no no no this is a guy's hobby project  
**Translation:** 

**[9834.98s] English:** you've you've have a security bot that's gone and found some ai generated stuff  
**Translation:** 

**[9839.82s] English:** that  
**Translation:** 

**[9840.00s] English:** guy didn't write crap code it's just an edge case to the 99.99999 percentile he didn't think about  
**Translation:** Vocabulary: percentile: 百分位数

**[9847.44s] English:** because it's his hobby project decoding star wars games i get the hobby project aspect of it it's  
**Translation:** 

**[9853.20s] English:** it's just hard work and it's it's beautiful and there's like the right approach there's to  
**Translation:** 

**[9857.36s] English:** celebrate people for doing incredible incredible work it's just incredible that humans step up  
**Translation:** 

**[9864.48s] English:** sure not getting really paid at first or maybe ever and then they're doing it out  
**Translation:** 

**[9869.68s] English:** of the love of it and we need to like human civilization runs on people like that we need  
**Translation:** 

**[9874.88s] English:** to celebrate them to give you an idea i received death threats on video land right and um you  
**Translation:** 

**[9880.32s] English:** mentioned that to me like what was what is behind that so that must be what 2009 2010 right um  
**Translation:** 

**[9888.00s] English:** apple is moving from power pc to core duos um that's probably in 2006 and  
**Translation:** 

**[9894.24s] English:** by the way this was this was in 2009-2010 there was a time where they were basically you know  
**Translation:** 

**[9894.48s] English:** 2009 or 2010 i decided that we are not going to do new versions of vlc for power pc at that time like  
**Translation:** 

**[9903.12s] English:** vlc we were close to the number one dot zero release we were four of us right like just like  
**Translation:** 

**[9909.20s] English:** no this is not possible so i received a death threat with some powder in it right it remember  
**Translation:** 

**[9914.72s] English:** there was some anthrax threats at that time right um and it was because i had taken the decision to  
**Translation:** 

**[9922.96s] English:** not maintain the power pc port anymore and of course it wasn't anthrax of course it was some  
**Translation:** Vocabulary: anthrax: 炭疽病

**[9928.56s] English:** type of floor and so on but i received that as a with the later of like uh your piece of  
**Translation:** 

**[9935.44s] English:** you should die uh power pc forever and so on and was 2009 or 2010 right i was i was  
**Translation:** 

**[9943.60s] English:** i was young i was just like why what did i do right they can break your spirit it's like why  
**Translation:** 

**[9949.76s] English:** my mother freaked out right we had to go see the police  
**Translation:** 

**[9952.96s] English:** and so on and now like i i'm going to say that i'm quite happy that  
**Translation:** 

**[9957.20s] English:** this happened at that time it it forged me a lot  
**Translation:** 

**[9960.00s] English:** right i am i i can see i can take a lot of uh of hate on me i'm i'm okay with it right it sucks  
**Translation:** 

**[9968.04s] English:** that that's part of reality because all the people that love vlc all the people that love ffmpeg  
**Translation:** 

**[9973.24s] English:** like me you know i i legitimately 100 probably thousands of times in my life had a smile on my  
**Translation:** 

**[9983.08s] English:** face because ffmpeg made me happy period and how many times did i get a chance to say that  
**Translation:** Vocabulary: legitimately: 真正地

**[9988.86s] English:** zero until i realized there's a twitter account and every once in a while i'm like messaging it  
**Translation:** 

**[9995.28s] English:** one of the things i like on the reddit meme about me which i don't like this meme for a lot of  
**Translation:** 

**[10000.06s] English:** reasons but and someone says oh jb is on is on reddit which i am right and i say and say hello  
**Translation:** 

**[10005.70s] English:** right and then i got so many people who say oh thank you for vlc and like i take pictures and  
**Translation:** 

**[10010.96s] English:** then i shared that to to to the signal to irc uh yes we use irc on on i saw  
**Translation:** 

**[10018.54s] English:** you  
**Translation:** 

**[10018.86s] English:** as a quick tangent you mentioned irc is like slack for old people so you still use irc of course yeah  
**Translation:** 

**[10024.06s] English:** i have it on my phone as well of course every day works fine wow it works fine you have to power  
**Translation:** Vocabulary: tangent: 旁白

**[10029.42s] English:** with the crank no but there's no there's no there's no tracking there's nothing like it's uh  
**Translation:** 

**[10036.14s] English:** the biggest issue to be honest right compared to slack is that it  
**Translation:** Vocabulary: crank: 曲柄

**[10039.42s] English:** doesn't have threads that's annoying it doesn't have emojis for reaction sometimes  
**Translation:** 

**[10045.42s] English:** yes v3 but no one does it and you cannot edit your messages  
**Translation:** Vocabulary: cannot: 不能

**[10048.86s] English:** right and the rest it works perfectly fine how do you communicate without emojis  
**Translation:** 

**[10053.58s] English:** well that's that's why i said it's for old people old people and we do we do emojis with like you  
**Translation:** 

**[10059.02s] English:** know the columns and yeah exactly so anyway you're communicating irc what were you even talking about  
**Translation:** 

**[10066.70s] English:** yeah we were talking about death threats and but having people thanking you and sometimes  
**Translation:** 

**[10071.58s] English:** they got people who send me a message and oh thank you for vlc and i always answer because i want to  
**Translation:** 

**[10078.86s] English:** to to validate  
**Translation:** Vocabulary: validate: 确认有效

**[10080.00s] English:** It's the fact that you need to thank  
**Translation:** 

**[10081.40s] English:** the open source community.  
**Translation:** 

**[10083.56s] English:** Yeah, please, everybody listening to this,  
**Translation:** 

**[10086.10s] English:** celebrate  
**Translation:** 

**[10086.58s] English:** FFmpegs, celebrate  
**Translation:** 

**[10089.78s] English:** VLC, celebrate all the incredible  
**Translation:** 

**[10091.88s] English:** open source projects,  
**Translation:** 

**[10094.00s] English:** Linux, everything. There's so many.  
**Translation:** 

**[10096.30s] English:** There's so many. And you know what?  
**Translation:** 

**[10098.00s] English:** I mean, even outside of open source,  
**Translation:** 

**[10100.34s] English:** just celebrate companies  
**Translation:** 

**[10101.72s] English:** that create software  
**Translation:** 

**[10103.76s] English:** that you use a lot  
**Translation:** 

**[10105.84s] English:** and love. Celebrate human endeavor.  
**Translation:** Vocabulary: endeavor: 努力

**[10108.00s] English:** Celebrate the human effort to not just  
**Translation:** 

**[10110.00s] English:** build something that's okay.  
**Translation:** 

**[10111.62s] English:** Build something that is damn good.  
**Translation:** 

**[10114.26s] English:** Yeah, this is important, right? Because  
**Translation:** 

**[10115.62s] English:** as we said, we work for  
**Translation:** 

**[10117.60s] English:** technology. We do something  
**Translation:** 

**[10120.10s] English:** very complex for  
**Translation:** 

**[10121.36s] English:** the normal people.  
**Translation:** 

**[10124.30s] English:** We want our excellence  
**Translation:** 

**[10126.30s] English:** in tech to be useful for  
**Translation:** 

**[10127.92s] English:** everyone. And this is why  
**Translation:** 

**[10129.66s] English:** we work. This is why  
**Translation:** 

**[10132.14s] English:** I wake up in the morning. It's because I want  
**Translation:** 

**[10133.88s] English:** people to use our stuff  
**Translation:** 

**[10135.20s] English:** because it's making everyone's life easier.  
**Translation:** 

**[10138.04s] English:** I want to solve our problems.  
**Translation:** 

**[10139.32s] English:** Work on something interesting.  
**Translation:** 

**[10141.00s] English:** Work on some interesting technical challenges.  
**Translation:** 

**[10143.04s] English:** We're engineers. We love to build things.  
**Translation:** 

**[10144.76s] English:** When I was young, very early, I knew I wanted  
**Translation:** 

**[10147.02s] English:** to be an engineer. I wanted to  
**Translation:** 

**[10148.96s] English:** do cars, right? Maybe at some point, I will  
**Translation:** 

**[10150.98s] English:** go back to cars, right?  
**Translation:** 

**[10153.54s] English:** We want to  
**Translation:** 

**[10155.12s] English:** build things that are cool and useful.  
**Translation:** 

**[10157.42s] English:** And they need to be challenging, right?  
**Translation:** 

**[10159.20s] English:** Because you want your brain to turn on.  
**Translation:** 

**[10161.42s] English:** When did the two of you first  
**Translation:** 

**[10162.66s] English:** fall in love with programming, with  
**Translation:** 

**[10164.64s] English:** building, with engineering?  
**Translation:** 

**[10166.66s] English:** When is the first time you programmed, Kieran?  
**Translation:** 

**[10168.58s] English:** Microsoft QBasic.  
**Translation:** 

**[10170.66s] English:** I was on Windows 3.1 and Windows  
**Translation:** 

**[10172.74s] English:** 95, Microsoft QBasic.  
**Translation:** 

**[10174.80s] English:** Wow. What did you build?  
**Translation:** 

**[10176.48s] English:** Like a multiplication.  
**Translation:** Vocabulary: multiplication: 乘法

**[10178.30s] English:** Just counting loops, like 10, 20, 30, 40.  
**Translation:** 

**[10180.78s] English:** Nice. Then I thought I could do  
**Translation:** 

**[10182.48s] English:** everything after that. I jumped from doing  
**Translation:** 

**[10184.48s] English:** that to, I want to create a  
**Translation:** 

**[10186.36s] English:** soccer, no, a football, soccer video game.  
**Translation:** 

**[10188.32s] English:** And I drew everything out.  
**Translation:** 

**[10190.28s] English:** I didn't quite grasp that actually  
**Translation:** 

**[10192.76s] English:** I didn't grasp that actually it's a massive piece of work to  
**Translation:** 

**[10196.38s] English:** jump from basic and drawing some pictures  
**Translation:** 

**[10198.34s] English:** to a video game, but there we go.  
**Translation:** 

**[10200.00s] English:** I think I did also Basics and then Turbo Pascal when I was, yeah, end of elementary school.  
**Translation:** 

**[10211.30s] English:** But mostly the first time I actually did some serious programming was the first year of, you call that middle school when you're 11?  
**Translation:** Vocabulary: pascal: 帕斯卡; turbo: turbo

**[10221.92s] English:** I lived in Italy for a year in Florence and it was an amazing year.  
**Translation:** 

**[10228.12s] English:** And, like, the math teacher told us to work in a programming language called Logo, where you had a turtle that was designing things on the screen and you would turn left and right.  
**Translation:** Vocabulary: florence: 佛罗伦萨

**[10240.22s] English:** And in the end, we used that to do very complex programming because, of course, you could do things.  
**Translation:** 

**[10245.76s] English:** And this changed, like, as I knew I wanted to do things with computers and program.  
**Translation:** 

**[10251.34s] English:** I don't think we quite talked about x264 properly.  
**Translation:** 

**[10255.00s] English:** We talked about David.  
**Translation:** 

**[10255.84s] English:** Can we return?  
**Translation:** 

**[10257.52s] English:** Sure.  
**Translation:** 

**[10257.66s] English:** Let's backtrack a little bit to x264, this thing that powers basically all of the video on the Internet.  
**Translation:** 

**[10264.44s] English:** So can you tell me the story of x264?  
**Translation:** Vocabulary: backtrack: 回顾

**[10269.44s] English:** And, Kieran, you're actually a contributor to x264.  
**Translation:** 

**[10272.20s] English:** So x264 is a video encoder for the H.264 video standard.  
**Translation:** Vocabulary: contributor: 贡献者

**[10277.42s] English:** It dominates Internet video, but also other areas such as Blu-ray discs.  
**Translation:** 

**[10281.18s] English:** And Blu-ray discs are interesting because the people that make them really want the highest quality.  
**Translation:** Vocabulary: dominates: 占据主导

**[10285.66s] English:** And there's some really cool high-end films.  
**Translation:** 

**[10287.66s] English:** They've been encoded broadcasting and all sorts of other areas.  
**Translation:** Vocabulary: broadcasting: 广播; encoded: 编码

**[10291.28s] English:** x264 was a big step change because it kind of happened at the right time as well.  
**Translation:** 

**[10296.84s] English:** A lot of the development took place when HD video was coming out.  
**Translation:** 

**[10300.90s] English:** Intel Core 2 and Nihil MCPUs were getting fast.  
**Translation:** 

**[10303.60s] English:** You could do real-time video.  
**Translation:** 

**[10305.20s] English:** But the most important thing was a key sort of focus on visual metrics.  
**Translation:** 

**[10312.92s] English:** So industry and academia for 20 years before was obsessed with.  
**Translation:** Vocabulary: academia: 学术界

**[10317.66s] English:** Mathematical metrics.  
**Translation:** 

**[10320.00s] English:** known as peak signal to noise ratio so mean squared error logarithm of mean squared error  
**Translation:** Vocabulary: logarithm: 对数; mathematical: 数学的

**[10324.28s] English:** and that led to tons of issues because mean squared error um leads to blurring because you  
**Translation:** 

**[10329.30s] English:** actually want to you want to minimize you want to add a little bit of error to everything  
**Translation:** Vocabulary: blurring: 模糊

**[10332.20s] English:** to reduce the mean squared error as opposed to having a big error and that led to loads and  
**Translation:** 

**[10336.06s] English:** loads of blurring so but hobbyists bucked that trend it was for their own personal videos mostly  
**Translation:** Vocabulary: bucked: 违背

**[10340.76s] English:** anime so there were two there were two things they did differently and there's a big iterative  
**Translation:** 

**[10345.54s] English:** feedback loop with the community they did some stuff differently um two two big things  
**Translation:** Vocabulary: anime: 动画; iterative: 迭代

**[10351.34s] English:** psychovisual rate distortion so using block energy trying to compensate for human perception when  
**Translation:** 

**[10357.46s] English:** making decisions so the psychovisual distortion that's the critical yeah thing that's the thing  
**Translation:** Vocabulary: compensate: 补偿; distortion: 失真; psychovisual: 心理视觉

**[10364.06s] English:** i mean it's kind of revolutionary like that we can like rethink don't don't make it like this  
**Translation:** 

**[10371.98s] English:** kind of theoretic thing of compression make it all  
**Translation:** Vocabulary: compression: 压缩; theoretic: 理论

**[10375.52s] English:** about being pleasing visually to the eye yeah yeah so compressing in a way that loses the least  
**Translation:** 

**[10381.42s] English:** amount of information for the stuff that matters for us humans yes exactly as opposed to what  
**Translation:** Vocabulary: compressing: 压缩

**[10386.42s] English:** industry some parts of industry are still obsessed by this which is mathematical numbers that don't  
**Translation:** 

**[10391.42s] English:** look um good in reality and then adaptive quantization was the other big one where  
**Translation:** Vocabulary: adaptive: 自适应; quantization: 量化

**[10395.70s] English:** it was biasing bits against um complex areas and redistributing them to less complex areas  
**Translation:** 

**[10403.02s] English:** like grass grass has some  
**Translation:** Vocabulary: redistributing: 重新分配

**[10405.52s] English:** high frequencies but it's kind of it's less complex overall compared to more complicated  
**Translation:** 

**[10409.98s] English:** things and this came around by um park joy so park joy was really the canonical sample that was  
**Translation:** Vocabulary: canonical: 典范样本

**[10416.18s] English:** it's the running around in the park yeah so this guy was really the um  
**Translation:** 

**[10420.86s] English:** so this this was created by swedish television in um the beginning of hd and it was done on film  
**Translation:** Vocabulary: swedish: 瑞典的

**[10428.24s] English:** and it was no expense spared in terms of production quality and it was given away for free this was  
**Translation:** 

**[10433.70s] English:** really and this is the  
**Translation:** 

**[10435.52s] English:** sample really that sorts the men from the boys in terms of it has so many challenges with the  
**Translation:** 

**[10440.00s] English:** trees with the water with the grass with the motion with the i don't think there's there's  
**Translation:** 

**[10445.80s] English:** still been any any public test sequence as good as that these days so for people who are just  
**Translation:** 

**[10452.48s] English:** listening we're looking at a bunch of humans running along a river as you have the reflection  
**Translation:** 

**[10459.12s] English:** a lot of really high information textures everywhere the leaves and the lighting playing  
**Translation:** 

**[10465.46s] English:** on the leaves and all of this you could show clearly that encoders with high psnr will blur  
**Translation:** Vocabulary: encoders: 编码器

**[10471.20s] English:** everything will blur everything and you could see actually i could turn on psychovisual stuff i could  
**Translation:** 

**[10474.96s] English:** turn off adaptive quantization and it would just look so much better but your your metrics and  
**Translation:** 

**[10480.40s] English:** these metrics are at the time what at the time were considered so holy yeah these are the holy  
**Translation:** 

**[10484.70s] English:** metrics that are untouchable psnr is uh the most important thing uh can you speak to how do you  
**Translation:** 

**[10490.44s] English:** measure psychovisual stuff like how do you turn how pleasing  
**Translation:** 

**[10495.18s] English:** you can you speak to how do you measure psychovisual stuff like how do you turn  
**Translation:** Vocabulary: psychovisual: 心理视觉

**[10495.44s] English:** a compression is for a human eye into a number is that even possible that's what that's what  
**Translation:** 

**[10500.62s] English:** netflix have been trying to do with vmath they said they've used a machine learning model  
**Translation:** 

**[10504.28s] English:** that's a more recent thing but back in when x86 was being developed that's by eye it was by eye  
**Translation:** 

**[10510.82s] English:** it was developers on their laptops so it's not like even with big companies with professional  
**Translation:** 

**[10515.40s] English:** screens or anything it's and that was actually one of the goals which was i don't the developers  
**Translation:** 

**[10520.22s] English:** at the time lauren merit in particular is i don't want to test this on a 30 000 screen it's i want  
**Translation:** 

**[10525.24s] English:** this to be a machine learning model and i don't want to test this on a 30 000 screen it's i want  
**Translation:** 

**[10525.42s] English:** this to be a machine learning model and i don't want to test this on a 30 000 screen it's i want  
**Translation:** 

**[10525.44s] English:** look good on someone's laptop at home yeah brilliant and there is another sample which is  
**Translation:** 

**[10530.68s] English:** um a sample that is a planet earth killer sample that i absolutely love and you were going to see  
**Translation:** 

**[10538.60s] English:** why right um it's a ton of birds right flying and the more it goes the more there are birds  
**Translation:** 

**[10548.36s] English:** and at the end right it's almost like you have millions of birds it's the most complex thing  
**Translation:** 

**[10555.22s] English:** ever to encode right and well you're watching it on youtube and you see how bad  
**Translation:** 

**[10560.00s] English:** the youtube encoding is actually right um and this is like phenomenal to to optimize and get  
**Translation:** Vocabulary: encode: 编码; encoding: 编码; optimize: 优化; phenomenal: 非凡的

**[10567.92s] English:** um perfect quality in a constant bitrate um there was a lot of optimization mostly by lauren also  
**Translation:** 

**[10575.02s] English:** on anime right for a long time anime was very badly encoded because there was a ton of bending  
**Translation:** Vocabulary: anime: 动画; encoded: 编码; optimization: 优化

**[10581.44s] English:** right and you see those um those issue and there was a ton of things um so x264 is like and today  
**Translation:** 

**[10589.70s] English:** it's still the reference to any encoder new encoder av1 av2 vvc hvc everyone compares to  
**Translation:** 

**[10597.12s] English:** x264 one of my favorite films um cinema paradiso i know the engineer who created the blu-ray and  
**Translation:** 

**[10603.68s] English:** he showed me the comparisons of x264 versus others and uh that's completely different and i think  
**Translation:** Vocabulary: paradiso: 天堂影院

**[10609.84s] English:** a bunch a bunch of guys in the blu-ray world started using x264 um i think the big one was  
**Translation:** 

**[10614.86s] English:** chris henderson from warner brothers he did the whole french box set with that's a quite like a  
**Translation:** Vocabulary: henderson: 亨德森

**[10619.22s] English:** thing  
**Translation:** 

**[10619.70s] English:** a person on the street actually watches and wants to look good and so they kind of took a risk in  
**Translation:** 

**[10623.92s] English:** their jobs doing that because they're in a big company that big company can buy whatever they  
**Translation:** 

**[10627.72s] English:** want and they said no no i want to use this free and open source thing so that things look good for  
**Translation:** 

**[10632.76s] English:** my customers and build the best and to this day i personally still try and avoid watching the most  
**Translation:** 

**[10639.62s] English:** cinematic films on streaming services and buy the physical discs because they look they look good  
**Translation:** Vocabulary: cinematic: 电影般的

**[10645.36s] English:** without even having to buy an expensive tv i think that's the key thing and x264  
**Translation:** 

**[10649.70s] English:** is yet another example of open source project it was started by laurent emar when he was at the  
**Translation:** 

**[10654.68s] English:** ecole centrale paris where vlc was born and then you got a generation of people like lauren like  
**Translation:** 

**[10660.04s] English:** jason like mons like uh so many henrik and henrik and this is anton and this is where the assembly  
**Translation:** Vocabulary: anton: 安东; ecole: 学校; henrik: 亨里克; jason: 杰森; lauren: 劳伦

**[10669.16s] English:** thing that we use now on ffm peg david and so on was born right so x264 is like amazing project  
**Translation:** 

**[10674.80s] English:** with people who were really all over the world and i think most of them never met each other  
**Translation:** 

**[10679.70s] English:** but  
**Translation:** 

**[10680.00s] English:** But all of them, according to Kieran, or a large percentage, love anime.  
**Translation:** 

**[10685.30s] English:** There's several things I've never got into, and one of them is anime.  
**Translation:** 

**[10688.52s] English:** I watch anime so much, especially at the time.  
**Translation:** 

**[10694.28s] English:** Like, at the time, it was like a lot of anime content doesn't exist commercially, right?  
**Translation:** 

**[10701.10s] English:** We are before Crunchyroll, right?  
**Translation:** Vocabulary: anime: 动画; crunchyroll: Crunchy卷

**[10702.62s] English:** So what happens is usually people who love anime, who take some things, some DVDs in Japan, and rip them because there is no commercial offering.  
**Translation:** 

**[10713.12s] English:** And some of the people who are what we call fan subbers are basically translating themselves to make subtitles, right?  
**Translation:** Vocabulary: subtitles: 字幕

**[10720.16s] English:** And at that time, you download completely illegally.  
**Translation:** 

**[10723.36s] English:** It was the only way to do that, right?  
**Translation:** 

**[10725.24s] English:** And so all of that was handcrafted, and it fits the open source community, right?  
**Translation:** 

**[10730.44s] English:** Because they needed tools to encode, to do.  
**Translation:** Vocabulary: encode: 编码; handcrafted: 手工制作

**[10732.62s] English:** One of the most amazing open source projects for subtitles is called AEG Sub, and it's a subtitle.  
**Translation:** 

**[10740.88s] English:** It's done for anime, for South Asian and Japanese languages.  
**Translation:** Vocabulary: subtitle: 字幕

**[10746.98s] English:** There are weird textures in anime that I don't think you get in real life content.  
**Translation:** 

**[10752.12s] English:** I think that was a key one, which was optimizing these weird textures that you get, because anime is not done in a normal fashion.  
**Translation:** Vocabulary: optimizing: 优化

**[10757.52s] English:** Yeah, the way you produce it is not, you mostly produce it like on screens, right?  
**Translation:** 

**[10762.58s] English:** Yeah.  
**Translation:** 

**[10762.60s] English:** Since a bit of time.  
**Translation:** 

**[10763.88s] English:** And you have all those gradients, right, in colors, because they are very easy to produce digitally, very complex to produce in real life.  
**Translation:** Vocabulary: digitally: 电子地; gradients: 渐变

**[10772.86s] English:** And the subtitles also are very complex, because you need to have often the Japanese, and then you need to have the diacritics, right?  
**Translation:** 

**[10781.16s] English:** What we call the Uribe, right?  
**Translation:** Vocabulary: diacritics: 标音符号

**[10782.64s] English:** Which is the Hiragana and the Katakana for the kanji.  
**Translation:** 

**[10785.64s] English:** And then, because of course, so that you have the official subtitling, but you also need the English subtitles or the French subtitles.  
**Translation:** Vocabulary: hiragana: 平假名; kanji: 漢字; katakana: 片假名; subtitling: 字幕

**[10792.56s] English:** Because you want to learn that, right?  
**Translation:** 

**[10794.78s] English:** And there is so many things crazy on subtitles.  
**Translation:** 

**[10797.90s] English:** And we had like crazy samples on subtitles.  
**Translation:** 

**[10800.00s] English:** titles that we've seen all around so um this is an important part of the culture but also because  
**Translation:** 

**[10807.38s] English:** there was no official offering there was no way of doing that uh can you speak to the difference  
**Translation:** 

**[10813.08s] English:** in h264 and av1 and then x264 and david this is this big step can you help people understand  
**Translation:** 

**[10821.78s] English:** are some of the streaming sites moving more towards that direction of av1 let's be honest  
**Translation:** 

**[10827.58s] English:** all of those codecs since mpeg2 video are the same concepts the same concept about inverse  
**Translation:** Vocabulary: inverse: 相反的

**[10838.12s] English:** transform about intra prediction motion composite entropy coding all of them however each generation  
**Translation:** 

**[10845.64s] English:** gives you a bump between 25 and 50 percent more compression for the same quality  
**Translation:** Vocabulary: composite: 合成; compression: 压缩; entropy: 熵; intra: 内间

**[10853.72s] English:** um and so you had the mpeg2 you had the  
**Translation:** 

**[10857.58s] English:** devics area you have h264 which was like changing right h264 improved so much and then  
**Translation:** 

**[10865.22s] English:** you had more right you had hevc um you had vp9 at the same time of hevc vp9 is a bit similar to  
**Translation:** 

**[10873.54s] English:** hevc in terms of quality compression but it's royalty free because in multimedia there is ton  
**Translation:** Vocabulary: multimedia: 多种媒体

**[10879.72s] English:** of patents and the licensing after h264 became out of hand right and could cost hundreds of  
**Translation:** 

**[10886.42s] English:** millions of dollars per year  
**Translation:** 

**[10887.58s] English:** so it made no sense so google did this vp9 and the alliance for open media did this new codec called  
**Translation:** 

**[10894.24s] English:** av1 um so you can imagine that av1 saves between 40 and 60 percent less bandwidth than h264 for  
**Translation:** Vocabulary: bandwidth: 带宽

**[10905.40s] English:** for the same quality visual quality at a given bit rate at a given bit rate right so that's really  
**Translation:** 

**[10911.34s] English:** like you increase the quality either you you set the bit rate and you increase the quality or you  
**Translation:** 

**[10917.58s] English:** increase your bit rate but because now you move from  
**Translation:** 

**[10920.00s] English:** from SD to HD, and HD to 4K, and 4K to 4K HDR,  
**Translation:** 

**[10925.48s] English:** like, you're increasing the size by, like, two, factor two, three, four, right?  
**Translation:** 

**[10930.62s] English:** So you need to have better compression to keep it in terms of something that is manageable.  
**Translation:** 

**[10936.88s] English:** It's more coding tools, more bigger blocks,  
**Translation:** 

**[10940.08s] English:** lots more sub-partitions in each block, it's just exponentially more complex.  
**Translation:** Vocabulary: exponentially: 成倍地

**[10943.46s] English:** It's more complex because the encoder needs to search more possibilities, right?  
**Translation:** 

**[10949.16s] English:** So, for example, one of the things that is easy to understand  
**Translation:** 

**[10952.68s] English:** is to predict a block, a color block to another, you have directions, right?  
**Translation:** 

**[10958.54s] English:** So you can go left, right, bottom, up, and then in terms of, like, the other quadrants, right?  
**Translation:** Vocabulary: quadrants: 四个象限

**[10965.42s] English:** What I call north, east, northwest, and so on, right?  
**Translation:** 

**[10968.66s] English:** But that's eight directions.  
**Translation:** 

**[10970.04s] English:** Then you can do more direction.  
**Translation:** 

**[10971.26s] English:** You can do 16, or 69, or 128, right?  
**Translation:** 

**[10974.92s] English:** You can, and every time your encoder is going to spend more time to see,  
**Translation:** 

**[10979.16s] English:** well, this block is exactly this one, and those type of tools that you can bring,  
**Translation:** 

**[10984.90s] English:** and the encoder needs to check which of the tools are going to compress you better.  
**Translation:** 

**[10990.00s] English:** And so I guess that AV1 encoding is two order of magnitudes more than H.264  
**Translation:** Vocabulary: compress: 压缩; encoding: 编码; magnitudes: 数量级

**[10997.12s] English:** in terms of CPU cycle, right?  
**Translation:** 

**[10999.56s] English:** Order of magnitudes, right?  
**Translation:** 

**[11001.44s] English:** And as we discussed, CPUs are not getting faster.  
**Translation:** 

**[11003.84s] English:** You're just throwing more cores at the problem.  
**Translation:** 

**[11005.58s] English:** But also, it's the fact that you encode once,  
**Translation:** 

**[11008.18s] English:** and you have hundreds of cores.  
**Translation:** Vocabulary: encode: 编码

**[11009.16s] English:** You have millions of users, right?  
**Translation:** 

**[11010.74s] English:** So, for example, YouTube, a very good example.  
**Translation:** 

**[11013.38s] English:** YouTube encodes almost everything in H.264,  
**Translation:** 

**[11016.26s] English:** but the popular video gets re-encoded in AV1  
**Translation:** 

**[11019.74s] English:** because it costs more, of course, to encode,  
**Translation:** 

**[11023.40s] English:** but you encode once, and you send that to millions, right?  
**Translation:** 

**[11026.08s] English:** So it's a trade-off between encoding time and complexity  
**Translation:** 

**[11029.96s] English:** and CPU usage on the server side and on the client side  
**Translation:** 

**[11034.22s] English:** because at the end, if you're distributing a video  
**Translation:** 

**[11037.42s] English:** to hundreds of thousands of people,  
**Translation:** 

**[11039.16s] English:** and the size is...  
**Translation:** 

**[11040.00s] English:** half of the other then it's better it's better for your battery is better for your modem  
**Translation:** 

**[11045.18s] English:** etc etc so we can lay out let's say the top five codec container combos would be asia 64  
**Translation:** 

**[11055.40s] English:** inside mp4 containers av1 inside mp4 webm containers pro res for non-linear editing  
**Translation:** Vocabulary: combos: 组合

**[11066.26s] English:** inside mov containers so for people who don't know i guess pro res is apple's codec for editing  
**Translation:** 

**[11074.30s] English:** originally for final cut pro and it's designed to be fast to decode fast to seek because an editor  
**Translation:** 

**[11079.90s] English:** will need to move very quickly so it's a different use case to the distribution element there's no  
**Translation:** 

**[11085.70s] English:** or very minimal uh temporal compression there's none there's none in progress so you can cut so  
**Translation:** Vocabulary: compression: 压缩; temporal: 时间

**[11091.24s] English:** you can do cuts this is what we call intra only codecs right so i'm  
**Translation:** 

**[11096.26s] English:** going to explain quickly what is ipb frames yes um so iframes often keyframes but  
**Translation:** Vocabulary: intra: 内部编码; keyframes: 关键帧

**[11105.22s] English:** is complete frames it's like an image it's a jpeg right you have you can start you see everything  
**Translation:** 

**[11111.72s] English:** right um and then you the next image can be a p frame which is a predicted frame so you take  
**Translation:** 

**[11119.96s] English:** some part of the previous image saying well i need the block 5 and 7 and 42  
**Translation:** 

**[11124.90s] English:** and you  
**Translation:** 

**[11126.26s] English:** you replace it and then you just give the extra information right but that means that in order to  
**Translation:** 

**[11131.04s] English:** decode this p frame you need to have access to previous i frame right and then of course you  
**Translation:** 

**[11136.66s] English:** have more complex one which are b frames which are b predicted um frames which can be depend on  
**Translation:** 

**[11143.98s] English:** different type of frames some in the past some in the future um and so pro res is an intra only  
**Translation:** 

**[11152.12s] English:** codec for the people who can see this is a very good one right so i  
**Translation:** 

**[11156.26s] English:** think iframes are complete frames um uh p frame basic  
**Translation:** 

**[11160.00s] English:** uh depend only on iframe and b frames can depend on in front and this uh gop group of pictures  
**Translation:** 

**[11166.96s] English:** i think the default for actually ffmpeg for issue 64 is uh like 250 frames something like this yes  
**Translation:** 

**[11179.36s] English:** and to me it's just it's like magic like you can predict that you can have a complete frame every  
**Translation:** 

**[11185.96s] English:** several seconds that means several seconds and then you could still you could have this chain  
**Translation:** 

**[11191.54s] English:** of predictions you make and the fact that you can the fact that somebody like me can can use  
**Translation:** 

**[11197.26s] English:** ffmpeg to compress something and not notice that the result still plays back smoothly  
**Translation:** Vocabulary: compress: 压缩

**[11202.12s] English:** it's like magic you can even have and we use that in terms on kyber is what we call intra refresh  
**Translation:** 

**[11210.00s] English:** where basically it's there is no iframe you have no if you have one at the beginning  
**Translation:** 

**[11215.94s] English:** and you never send an iframe how does that work what is it you build up an iframe gradually  
**Translation:** 

**[11220.78s] English:** across as the stream continues so you refresh certain parts of the image but so you never  
**Translation:** 

**[11226.36s] English:** have an iframe like this is intra refresh that we use right but for me for me the the biggest  
**Translation:** 

**[11231.90s] English:** mind blown when i started was the b frames yeah b frames means be predicted frames can depend  
**Translation:** Vocabulary: intra: 内部

**[11239.12s] English:** on frames that are coming in the future that means that in order to decode  
**Translation:** 

**[11245.54s] English:** these  
**Translation:** 

**[11245.94s] English:** b frame you need to wait for the next frame that is dependent but for that decode that one  
**Translation:** 

**[11253.28s] English:** so that you can decode the b frame right so the the way you decode the frame the decoding order  
**Translation:** 

**[11259.88s] English:** is not the same as the display order right that means the encoder needs to be very clever and  
**Translation:** 

**[11266.40s] English:** decide that well you know i'm going to depend on things like in the future so this is like  
**Translation:** 

**[11271.40s] English:** mind-blowing yeah the fact it works so smoothly every day is  
**Translation:** 

**[11275.62s] English:** is  
**Translation:** 

**[11275.94s] English:** kind of miraculous in some ways it works so you can have a stream that works  
**Translation:** 

**[11280.00s] English:** across the world on their decoder versus one in the US versus one here  
**Translation:** Vocabulary: miraculous: 奇迹般

**[11284.90s] English:** of different manufacturers, and they produce bit for bit exactly the same material.  
**Translation:** 

**[11290.26s] English:** That's quite remarkable, and do quite complex things,  
**Translation:** 

**[11292.90s] English:** and getting more and more complex, and still be bit exact.  
**Translation:** 

**[11296.46s] English:** There's a lot of work that goes into that.  
**Translation:** 

**[11298.36s] English:** There's a lot of knobs you can control in this whole process.  
**Translation:** 

**[11301.02s] English:** There's a lot of really fascinating parameters that I've gotten to know more and more  
**Translation:** Vocabulary: knobs: 旋钮

**[11304.68s] English:** over the years that FFmpeg gives you complete access to.  
**Translation:** 

**[11308.46s] English:** Maybe you can speak to some of those.  
**Translation:** 

**[11309.64s] English:** First of all, obviously, we can lower the resolution.  
**Translation:** 

**[11312.50s] English:** We can lower the frame rate.  
**Translation:** 

**[11313.90s] English:** We can use different kinds of codecs, as we mentioned, from H.264 to AV1.  
**Translation:** 

**[11319.30s] English:** There's ways to tune the tradeoff between bit rate and quality, as we've spoken to.  
**Translation:** Vocabulary: tradeoff: 权衡

**[11325.54s] English:** You could do constant bit rate.  
**Translation:** 

**[11327.12s] English:** You can do constant quality, say, RFCQ, QP.  
**Translation:** 

**[11330.94s] English:** You can do the longer or shorter group of pictures, GOP, that we mentioned.  
**Translation:** 

**[11337.16s] English:** I mean, all that kind of stuff.  
**Translation:** 

**[11338.40s] English:** It's crazy.  
**Translation:** 

**[11339.00s] English:** The number of bit frames.  
**Translation:** 

**[11340.72s] English:** Yeah.  
**Translation:** 

**[11341.04s] English:** What is crazy is that a ton of people's job is to optimize those parameters.  
**Translation:** Vocabulary: optimize: 优化

**[11349.10s] English:** A ton of people that you see at YouTube, at Netflix, at Meta, and so on,  
**Translation:** 

**[11353.48s] English:** they're not writing codecs.  
**Translation:** 

**[11354.68s] English:** They're just finding the right parameters for the file they have, for the format they have.  
**Translation:** 

**[11361.90s] English:** Because something that is for a movie, or something that is user-generated content from your phone,  
**Translation:** 

**[11367.74s] English:** or a screen recording.  
**Translation:** 

**[11369.00s] English:** Or something that you're going to video edit.  
**Translation:** 

**[11371.30s] English:** You don't want the same things.  
**Translation:** 

**[11373.66s] English:** And there are thousands of people whose job is just to optimize all that.  
**Translation:** 

**[11378.12s] English:** Yeah, they're wizards.  
**Translation:** 

**[11379.68s] English:** Hats off to them.  
**Translation:** 

**[11382.18s] English:** YouTube, to deliver all the streaming sites, actually.  
**Translation:** 

**[11385.46s] English:** To deliver at scale.  
**Translation:** 

**[11387.14s] English:** And YouTube is really magical, because it's not just doing what Netflix does, which is one-way broadcasting type thing.  
**Translation:** 

**[11395.92s] English:** It also has to upload videos.  
**Translation:** Vocabulary: broadcasting: 单向传播

**[11400.00s] English:** from all the places so they're also doing encoding at scale for videos they're going to be watched by  
**Translation:** 

**[11405.66s] English:** like five people and it still has to deliver them like at a moment's notice no no delay nothing  
**Translation:** Vocabulary: encoding: 编码

**[11412.68s] English:** no late i mean very minimal latency and and also serve it in all different resolutions  
**Translation:** 

**[11420.14s] English:** like youtube is basically the web version of vlc well actually it's funny because like  
**Translation:** Vocabulary: latency: 延迟; resolutions: 分辨率

**[11427.56s] English:** google video which was something they did before they acquired youtube was actually using the vlc  
**Translation:** 

**[11435.06s] English:** plugin so that you could run vlc inside the web browser using the activix plugin and so it worked  
**Translation:** 

**[11442.50s] English:** in internet explorer and you were actually running vlc inside your browser which is funny because  
**Translation:** 

**[11450.48s] English:** today we have the opposite where we have vlc web assembly where we compile all vlc and ffmpeg to  
**Translation:** Vocabulary: explorer: 浏览器

**[11456.06s] English:** to run vlc  
**Translation:** 

**[11457.50s] English:** in type of inside the javascript virtual machine um with web assembly okay there's this legendary  
**Translation:** 

**[11466.06s] English:** story that you pointed me to that uh it was discovered uh via wikileaks release of all  
**Translation:** 

**[11473.98s] English:** seven documents the cia was using a modified version of vlc uh to basically try and trick  
**Translation:** 

**[11480.14s] English:** people what to steal their data yes exactly so can you explain what the heck happened what  
**Translation:** 

**[11487.50s] English:** so so this was a surprise right um because at some point wikileaks uh mentioned some documents  
**Translation:** 

**[11492.86s] English:** there were a few ones with uh something related to blu-rays and vlc but the the most interesting  
**Translation:** 

**[11498.06s] English:** one was the cia vault 7 which if i understand correctly um was the cia had like a custom version  
**Translation:** Vocabulary: vault: 金库

**[11506.14s] English:** of vlc uh where they had a specific plugin yeah exactly this is like we had to write a press  
**Translation:** 

**[11512.54s] English:** release on that uh video land wrote a press release saying the only safe source for getting  
**Translation:** 

**[11517.34s] English:** vlc media player is the official video  
**Translation:** 

**[11520.00s] English:** on that website i mean i suppose that's a security vulnerability for basically any piece of open  
**Translation:** Vocabulary: vulnerability: 安全漏洞

**[11526.70s] English:** source software somebody can trick you to download in a fake website or targeted advertisement right  
**Translation:** 

**[11533.98s] English:** that was a targeted advertisement to watch a specific file you need to watch with this custom  
**Translation:** 

**[11539.92s] English:** version of vlc and it was the normal binaries of vlc except they added one dll i think it was  
**Translation:** 

**[11545.60s] English:** ps api.dll which was basically reading your your document folder encrypting that and sell sending  
**Translation:** Vocabulary: binaries: 可执行文件; encrypting: 加密

**[11554.86s] English:** that and the thing is this is very clever to be honest because once you're watching a movie right  
**Translation:** 

**[11560.38s] English:** you're going to do that for two hours and you're not going to touch your computer and sometimes  
**Translation:** 

**[11564.56s] English:** it's normal because it's hd that your your fans are going up and say and there is ton of tpu usage  
**Translation:** 

**[11570.28s] English:** because you're using vlc right that's normal but the thing is what you don't see is that actually a  
**Translation:** 

**[11575.18s] English:** a  
**Translation:** 

**[11575.48s] English:** a  
**Translation:** 

**[11575.58s] English:** A powered version of vlc that is used by cia um we had exactly the same problem  
**Translation:** 

**[11582.10s] English:** with chinese hackers that were targeting indian people and that got vlc banned from india until  
**Translation:** Vocabulary: hackers: 黑客

**[11590.66s] English:** i had to to fight in courts in india the indian government to unban vlc they didn't use vlc they  
**Translation:** 

**[11598.24s] English:** took just one dll because we signed the dll correctly and they used that dll to do a  
**Translation:** 

**[11605.46s] English:** another program uh so you had a vlc.exe and was calling lip vlc but it was calling it into a fake  
**Translation:** 

**[11612.54s] English:** one and they used that to target um there is not much we can do actually to to to block those type  
**Translation:** 

**[11618.84s] English:** of hacks yeah i think people should for all open source software for all software in general people  
**Translation:** 

**[11624.78s] English:** should pay attention where they download the thing yes because that means that they were not downloading  
**Translation:** Vocabulary: hacks: 漏洞

**[11629.04s] English:** it from our website do the search engines help you no they don't just to clarify because you can you  
**Translation:** 

**[11634.92s] English:** know to prevent  
**Translation:** 

**[11635.34s] English:** threats from people manipulating  
**Translation:** 

**[11637.96s] English:** SEO to get up there on the link.  
**Translation:** 

**[11640.00s] English:** Absolutely not, right?  
**Translation:** 

**[11641.54s] English:** We have a big issue for like more than 10 years is that there is a fake version of VLC in Germany that was reported for now for 12 years.  
**Translation:** 

**[11652.02s] English:** And Google basically decides to not, they know what's in it, but the binary is too big for their virus analyzer to analyze it.  
**Translation:** 

**[11660.52s] English:** And so, well, if you're in Germany, you can go to a website that is a fake version of VLC with a custom installer.  
**Translation:** Vocabulary: analyzer: 病毒分析器; binary: 可执行文件; installer: 安装程序

**[11667.20s] English:** And it's very popular in Germany because their website is in German and Google mentioned that before VideoLan.  
**Translation:** 

**[11673.80s] English:** And the weirdest thing is that it doesn't do anything on your machine for three weeks because that's how they do the detection.  
**Translation:** Vocabulary: detection: 检测; weirdest: 最奇怪的事

**[11681.34s] English:** And after three weeks, there is a small program that is a service that's installed at the same time that wakes up after three weeks and starts downloading spyware and adware.  
**Translation:** 

**[11689.38s] English:** And Google knows about it.  
**Translation:** 

**[11690.68s] English:** They've decided not to do anything.  
**Translation:** 

**[11692.20s] English:** The guys use dark SEO in Germany to do that.  
**Translation:** 

**[11696.64s] English:** Add some.  
**Translation:** 

**[11697.20s] English:** And this is very damaging, right?  
**Translation:** 

**[11701.68s] English:** Because one of the things that they are downloading is actually something that is replacing your ads inside your machine, right?  
**Translation:** 

**[11708.24s] English:** It's actually quite surprisingly effective.  
**Translation:** 

**[11711.72s] English:** Whoever is doing it with Twitter and X with X, I'll get emails about your X account has been hacked.  
**Translation:** 

**[11719.22s] English:** And however they phrase it, it gets me to like at least click on the email not to follow the thing.  
**Translation:** Vocabulary: hacked: 被盗号

**[11726.46s] English:** And then you're like.  
**Translation:** 

**[11727.24s] English:** Man, whatever they're doing with the psychology to try to trick you, they're quite good.  
**Translation:** 

**[11732.44s] English:** There is a security version of VLC, right?  
**Translation:** 

**[11734.88s] English:** You received an email saying, hey, there is a security version.  
**Translation:** 

**[11737.70s] English:** He updates on VLC.  
**Translation:** 

**[11738.82s] English:** Think about updating right now because it can hack your computer.  
**Translation:** 

**[11741.92s] English:** You come, it's a website that looks decent and and you download it's a new version of VLC.  
**Translation:** 

**[11747.14s] English:** Great.  
**Translation:** 

**[11747.60s] English:** You don't know a month later you're hacked.  
**Translation:** 

**[11749.34s] English:** You have no idea you're part of a botnet.  
**Translation:** 

**[11750.88s] English:** Yeah.  
**Translation:** 

**[11752.00s] English:** So make, make sure wherever you're downloading stuff, it's legitimate.  
**Translation:** 

**[11756.32s] English:** I'm part of a botnet.  
**Translation:** 

**[11756.88s] English:** I'm part of the botnet.  
**Translation:** 

**[11758.20s] English:** Uh, speaking of which, so, uh.  
**Translation:** 

**[11760.00s] English:** You've mentioned that VLC sandboxing is something you're working on,  
**Translation:** Vocabulary: sandboxing: 沙盒技术

**[11764.82s] English:** and it's actually something quite challenging.  
**Translation:** 

**[11766.84s] English:** Why is it important? Why is it hard?  
**Translation:** 

**[11769.00s] English:** So VLC is a core with around 500 plugins, right?  
**Translation:** 

**[11774.44s] English:** One of them is FFmpeg, but we support so many other formats.  
**Translation:** 

**[11778.58s] English:** We support new protocols.  
**Translation:** 

**[11781.22s] English:** We support new filters.  
**Translation:** 

**[11782.74s] English:** We support weird architectures.  
**Translation:** 

**[11784.28s] English:** And in this release of VLC, you have modules that are going to call your drivers, right?  
**Translation:** 

**[11791.46s] English:** Mostly the hardware decoders, which are going to call your Intel, your NVIDIA, your IMD driver.  
**Translation:** 

**[11799.76s] English:** And all calling FFmpeg, right?  
**Translation:** Vocabulary: decoders: 解码器

**[11803.28s] English:** And there might be a security issue.  
**Translation:** 

**[11804.98s] English:** There might be a security issue in the shader.  
**Translation:** Vocabulary: shader: 着色器

**[11807.52s] English:** There might be a security issue in VLC, in FFmpeg, that is going to basically crash.  
**Translation:** 

**[11812.74s] English:** The issue is that you're running...  
**Translation:** 

**[11814.28s] English:** In VLC, like every other program, like Adobe, right?  
**Translation:** 

**[11818.22s] English:** You're running it on your machine, and it has access to all your documents, right?  
**Translation:** 

**[11823.40s] English:** So the idea is to be sure that you do a sandbox so that we can protect from ourselves.  
**Translation:** 

**[11830.26s] English:** Because inside the VLC process is running some code that is not even ours.  
**Translation:** Vocabulary: sandbox: 隔离环境

**[11834.82s] English:** Either it's open source for other projects that we integrate in VLC,  
**Translation:** 

**[11838.14s] English:** or it's your GPU driver or something that is provided by someone else inside.  
**Translation:** Vocabulary: integrate: 整合

**[11843.88s] English:** And so when...  
**Translation:** 

**[11844.28s] English:** When we crash, we want to not allow people to do bad things, right?  
**Translation:** 

**[11849.18s] English:** Because one of the common way of hacking people is to crash a program, very often done with a web browser,  
**Translation:** 

**[11855.24s] English:** very often done with PDF files, less often with multimedia, but that could happen.  
**Translation:** Vocabulary: hacking: 黑客攻击; multimedia: 多媒体

**[11859.80s] English:** And when you crash, you launch something on the machine of the person.  
**Translation:** 

**[11864.38s] English:** Could be a ransomware, could be a botnet, right?  
**Translation:** Vocabulary: ransomware: 勒索软件

**[11866.82s] English:** So security of desktop application is important.  
**Translation:** 

**[11870.32s] English:** On mobile, it's a bit different because most of the mobile applications are running  
**Translation:** 

**[11874.08s] English:** on inside their own sandbox, but for VLC, we could run it inside one sandbox.  
**Translation:** 

**[11880.00s] English:** But the problem is that we need access to so many things that it's basically we would have all the permissions, right?  
**Translation:** 

**[11888.78s] English:** And so if you have a sandbox and you put some holes everywhere, it defeats the purpose, right?  
**Translation:** 

**[11894.28s] English:** So what we are trying to do and we're actually doing is splitting VLC into several processings.  
**Translation:** Vocabulary: processings: 处理单元

**[11900.48s] English:** One is decoding, one is demuxing, one is filters.  
**Translation:** 

**[11904.06s] English:** And all of them run into their own sandbox so that the whole VLC, a part of VLC crash, like Chrome crashes on some tab, right?  
**Translation:** Vocabulary: demuxing: 解复用

**[11915.58s] English:** It crashes, but it did not crash the whole program.  
**Translation:** 

**[11919.06s] English:** And this is what we're trying to do.  
**Translation:** 

**[11920.56s] English:** And it's difficult because it's a sandbox that needs to sustain gigabits per second of mem copies.  
**Translation:** 

**[11927.58s] English:** Now, it's not a website which is five megabytes or 10 megabytes.  
**Translation:** Vocabulary: gigabits: 吉比特; megabytes: 兆字节

**[11930.34s] English:** We're talking about hundreds of megabits per second.  
**Translation:** 

**[11932.58s] English:** So this is why.  
**Translation:** 

**[11934.06s] English:** It is quite challenging.  
**Translation:** 

**[11935.38s] English:** And this is a research topic that we we are working on in order to have multimedia player that is secure.  
**Translation:** 

**[11943.38s] English:** This is all the kind of stuff you have to think about when millions of people are using.  
**Translation:** 

**[11946.82s] English:** You mentioned something somewhere where like all the different features of VLC,  
**Translation:** 

**[11952.58s] English:** when you have that many people using it, somebody will use every single feature and they will tell you about it.  
**Translation:** 

**[11960.18s] English:** Best feature in VLC is called the puzzle filter, right?  
**Translation:** 

**[11964.26s] English:** So you click the puzzle filter and it transforms your video into a jigsaw puzzle, right?  
**Translation:** 

**[11970.58s] English:** And you can click and move the pieces, right?  
**Translation:** Vocabulary: jigsaw: 拼图; transforms: 转换

**[11973.78s] English:** Yeah.  
**Translation:** 

**[11974.38s] English:** It's very, very useful when you're watching a French movie, right?  
**Translation:** 

**[11977.38s] English:** You're bored and because it's like like very long things or a love triangle, right?  
**Translation:** 

**[11982.90s] English:** We've seen that so many times, right?  
**Translation:** 

**[11984.38s] English:** But but you need to watch it because someone, your wife or told you to do that or your boyfriend told you to do that.  
**Translation:** 

**[11991.38s] English:** So you're doing that, right?  
**Translation:** 

**[11992.38s] English:** Yeah.  
**Translation:** 

**[11994.26s] English:** And you move the pieces around.  
**Translation:** 

**[11995.50s] English:** It's absolutely useless, right?  
**Translation:** 

**[11998.06s] English:** Like, who cares about that?  
**Translation:** 

**[11999.78s] English:** For.  
**Translation:** 

**[12000.00s] English:** It was done by a math teacher in high school in South of France to teach his students about  
**Translation:** 

**[12006.62s] English:** Bezier curves, which is something that everyone should know about, right?  
**Translation:** 

**[12009.96s] English:** It's very useful.  
**Translation:** 

**[12011.38s] English:** But the code was clean.  
**Translation:** 

**[12012.84s] English:** So it got in VLC.  
**Translation:** 

**[12013.84s] English:** It was merged in 2010.  
**Translation:** 

**[12015.98s] English:** Five years later, I received an email saying, hello, JB, I have a problem with VLC.  
**Translation:** 

**[12020.70s] English:** The puzzle is too simple.  
**Translation:** 

**[12022.74s] English:** And I was just like, what?  
**Translation:** 

**[12024.62s] English:** And yes, the puzzle was in the UI maximized by 16 by 16, right?  
**Translation:** 

**[12029.62s] English:** Only 256 pieces.  
**Translation:** Vocabulary: maximized: 最大化

**[12032.24s] English:** And he says, I'm sorry, but in a movie, I love puzzles.  
**Translation:** 

**[12035.68s] English:** This is too simple, right?  
**Translation:** 

**[12037.02s] English:** So there is a commit of me.  
**Translation:** 

**[12038.10s] English:** You can check it online, which is JB changing that the dimensions are 256 by 256.  
**Translation:** Vocabulary: dimensions: 尺寸

**[12045.04s] English:** But my point is, so many use features are used by a few people, right?  
**Translation:** 

**[12051.56s] English:** There is a way to watch VLC movies in common line without any UI, right?  
**Translation:** 

**[12057.76s] English:** I saw that you can do ASCII.  
**Translation:** 

**[12059.62s] English:** ASCII art.  
**Translation:** 

**[12061.04s] English:** Is it useful?  
**Translation:** 

**[12061.88s] English:** Very useful.  
**Translation:** 

**[12062.98s] English:** Imagine you're debugging a multicast network, right?  
**Translation:** 

**[12067.08s] English:** You have thousands, very complex networking stack, right?  
**Translation:** Vocabulary: multicast: 组播

**[12071.84s] English:** You can SSH to all of the routers and put VLC on it with no UI.  
**Translation:** 

**[12076.94s] English:** And you're going to see whether it's black or it's not black, right?  
**Translation:** Vocabulary: routers: 路由器

**[12079.34s] English:** So you see if it's all green or not all green, right?  
**Translation:** 

**[12082.08s] English:** So you can see.  
**Translation:** 

**[12084.04s] English:** People don't realize there is so many things in VLC that are useful.  
**Translation:** 

**[12089.28s] English:** Right?  
**Translation:** 

**[12089.44s] English:** Right.  
**Translation:** 

**[12089.52s] English:** Right.  
**Translation:** 

**[12089.58s] English:** Right.  
**Translation:** 

**[12089.62s] English:** And they have users.  
**Translation:** 

**[12093.30s] English:** Because once you have hundreds of millions of users, you have people who use every feature.  
**Translation:** 

**[12099.72s] English:** I would love to sort of zoom in and talk a little bit more about the distinction between kind of downloading a file and watching it offline versus streaming.  
**Translation:** 

**[12111.50s] English:** So the complexities, the challenges of streaming.  
**Translation:** 

**[12114.58s] English:** Is there something we could say about what it takes to stream?  
**Translation:** Vocabulary: complexities: 复杂性

**[12119.80s] English:** Inside DFL?  
**Translation:** 

**[12119.98s] English:** резult  
**Translation:** 

**[12120.10s] English:** In DFL?  
**Translation:** 

**[12120.54s] English:** In DFL?  
**Translation:** 

**[12120.88s] English:** In DFL?  
**Translation:** 

**[12121.18s] English:** In DFL?  
**Translation:** 

**[12121.52s] English:** In DFL?  
**Translation:** 

**[12121.58s] English:** In DFL?  
**Translation:** 

**[12121.82s] English:** In DFL?  
**Translation:** 

**[12121.92s] English:** In DFL?  
**Translation:** 

**[12122.20s] English:** in IDFL?  
**Translation:** 

**[12122.38s] English:** auto  
**Translation:** 

**[12123.02s] English:** changes  
**Translation:** 

**[12123.14s] English:** its  
**Translation:** 

**[12123.28s] English:** in DFL?  
**Translation:** 

**[12123.52s] English:** order  
**Translation:** 

**[12130.94s] English:** speed  
**Translation:** 

**[12131.48s] English:** speed  
**Translation:** 

**[12134.72s] English:** more  
**Translation:** 

**[12135.12s] English:** in DFL?  
**Translation:** 

**[12135.70s] English:** in case  
**Translation:** 

**[12137.22s] English:** you  
**Translation:** 

**[12137.80s] English:** can  
**Translation:** 

**[12138.14s] English:** continue  
**Translation:** 

**[12138.44s] English:** check  
**Translation:** 

**[12143.80s] English:** Don't talk bad about me!  
**Translation:** 

**[12146.66s] English:** I still  
**Translation:** 

**[12148.40s] English:** sit  
**Translation:** 

**[12148.64s] English:** have  
**Translation:** 

**[12148.94s] English:** I still  
**Translation:** 

**[12149.10s] English:** need  
**Translation:** 

**[12149.42s] English:** spit  
**Translation:** 

**[12149.52s] English:** olon  
**Translation:** 

**[12120.00s] English:** because we've been talking about codecs and i think a lot of that implies encoding and decoding  
**Translation:** Vocabulary: encoding: 编码

**[12128.00s] English:** uh without the having to communicate over the network sure sure so can you can you elaborate  
**Translation:** 

**[12134.00s] English:** like what's required to do over network stuff yeah but it is less complex than it seems compared to  
**Translation:** Vocabulary: elaborate: 详细说明

**[12139.60s] English:** everything that we've talked about um especially because the most complex thing is not about  
**Translation:** 

**[12145.68s] English:** streaming in terms of um uh streaming services but it was was what was done to  
**Translation:** 

**[12152.40s] English:** actually broadcast through satellites um because in in most of the modern uh  
**Translation:** 

**[12158.64s] English:** broadcasting services you can pause and you can go on but when you're sending live streaming whether  
**Translation:** Vocabulary: broadcasting: 广播

**[12164.24s] English:** it's broadcast or live for streaming services which are live this is much more difficult  
**Translation:** 

**[12169.28s] English:** because you need to encode in real time you when you go on a satellite you have a specific size  
**Translation:** Vocabulary: encode: 编码

**[12175.44s] English:** of the network that you are using to broadcast to the network that you are using to broadcast to  
**Translation:** 

**[12175.68s] English:** the link right you cannot have a burst of bandwidth even for a second right because you don't have the  
**Translation:** Vocabulary: bandwidth: 带宽; cannot: 不能

**[12181.76s] English:** space for that in your your total file however there is different types of challenges which are  
**Translation:** 

**[12187.92s] English:** interesting challenges but i think they are less complex than the one we've seen with um  
**Translation:** 

**[12193.28s] English:** late 90s and early 2000s about broadcasting and streaming so satellite they're different  
**Translation:** 

**[12198.16s] English:** they're control systems challenges whereas whereas some are more mathematical i think  
**Translation:** Vocabulary: mathematical: 数学相关的

**[12202.08s] English:** there's a difference in the streaming world what you have is called what we call adaptive  
**Translation:** 

**[12206.00s] English:** streaming because the difficulty and it's not really a video problem it's mostly a cdn problem  
**Translation:** Vocabulary: adaptive: 自适应

**[12211.36s] English:** is that you might have too many people watching the same thing at the same time and it's a congestion  
**Translation:** 

**[12216.16s] English:** of the network right so your player has difficulty downloading things fast enough to play them  
**Translation:** Vocabulary: congestion: 网络拥堵

**[12222.88s] English:** so what happens is that locally the player is going to read a lower resolution of it  
**Translation:** 

**[12232.08s] English:** but there are some very clever algorithms to do that but most of it is quite basics to be honest  
**Translation:** 

**[12240.00s] English:** on the buffering side is pretty basic yeah you you start you download a segment what we call a  
**Translation:** 

**[12246.20s] English:** segment and then you you time right and if you if it takes more than 50 percent of the time to  
**Translation:** Vocabulary: buffering: 缓冲

**[12251.36s] English:** download the segment you go down to right and the difficulty is more about when do you go up in  
**Translation:** 

**[12257.38s] English:** bandwidth in quality but this is not very complex to do when you encode you're going to encode seven  
**Translation:** 

**[12263.28s] English:** resolutions right and and you're going to give the bitrate the difficulty is to have your encoder  
**Translation:** 

**[12268.80s] English:** gives the same bitrate but it's not as strict as it used to be so probably youtube has to figure  
**Translation:** Vocabulary: resolutions: 分辨率

**[12276.12s] English:** out how the human psychology side of that like how pissed off do you get when it's like very low bit  
**Translation:** 

**[12285.10s] English:** rate and uh how long should it wait before it increases the bitrate even though the connection  
**Translation:** Vocabulary: pissed: 生气

**[12292.24s] English:** is better because maybe the changes in the bitrate is what like affects you psychologically  
**Translation:** 

**[12298.80s] English:** i think actually the interesting one is the audio that's true that you can kind of notice when they  
**Translation:** Vocabulary: psychologically: 心理上

**[12303.18s] English:** move from um full fat aac to the um there are compressed versions of aac that use spectral  
**Translation:** 

**[12310.00s] English:** band replication you can kind of see it goes a bit tinny and that up and down is very jarring  
**Translation:** Vocabulary: compressed: 压缩; spectral: 频谱; tinny: 刺耳

**[12314.64s] English:** the video side is a lot smoother and there's less notice it's really the audio you can you can  
**Translation:** 

**[12319.62s] English:** definitely you can definitely feel it from when it's moved you from a different audio profile to  
**Translation:** 

**[12323.46s] English:** one or the other i don't know we're surprisingly tolerant at skipping audio glitches i i don't know  
**Translation:** 

**[12328.80s] English:** i'm surprised people i know who are not video engineers how tolerant they are how tolerant  
**Translation:** Vocabulary: glitches: 错误; skipping: 跳过; tolerant: 宽容

**[12333.82s] English:** they are to watching sports at 30 fps for example whereas it should really be 60 the world is a lot  
**Translation:** 

**[12340.24s] English:** more tolerant to that but audio people are very there's it's an immediate feedback mechanism of  
**Translation:** 

**[12344.64s] English:** if you hear a glitch you realize it directly yeah i get to fully realize that i suppose one of the  
**Translation:** 

**[12350.22s] English:** things i'm afraid of when i listen to audio more and more that i get to notice every single tiny  
**Translation:** Vocabulary: glitch: 故障

**[12354.92s] English:** detail and that you can over obsess when uh people are not able to hear it and i'm not able to hear  
**Translation:** 

**[12358.80s] English:** people people in general  
**Translation:** 

**[12360.00s] English:** are able to kind of kind of blur their consumption they can they can look past certain imperfections  
**Translation:** 

**[12368.16s] English:** but then when you combine like um an event that is for example a sport event that is probably going  
**Translation:** 

**[12375.52s] English:** through satellite or somewhere else and goes to a central place for encoding and then you need to  
**Translation:** 

**[12381.76s] English:** encode this older resolution in real time you don't have time for qa you need to push that to  
**Translation:** Vocabulary: encode: 编码; encoding: 编码

**[12387.36s] English:** cdns you need to add probably drm or protection you need to have that over a ton of different  
**Translation:** 

**[12394.88s] English:** devices then yes it is complex um but and also like you in the web browser or in very much  
**Translation:** 

**[12403.84s] English:** different devices that you use for tv where you had like a defined set of box or cable box that  
**Translation:** 

**[12410.64s] English:** that you know where you control end to end um so it's a challenge but it's less i think the  
**Translation:** 

**[12416.16s] English:** networking part  
**Translation:** 

**[12417.36s] English:** while you agree to have 10 20 seconds of latency i don't think this is very difficult speaking of  
**Translation:** Vocabulary: latency: 延迟

**[12425.60s] English:** networking and latency so your new effort as we mentioned is kyber which is aimed at ultra low  
**Translation:** 

**[12435.12s] English:** latency as you say every millisecond counts and uh you're applying that to remote control  
**Translation:** Vocabulary: millisecond: 毫秒; ultra: 超凡

**[12441.76s] English:** machines like robots drones computers can you tell me about it sure um if you start  
**Translation:** 

**[12447.36s] English:** from where we used to be right you used to use fmpeg to encode files right and then we used fmpeg  
**Translation:** Vocabulary: drones: 无人驾驶飞行器

**[12453.92s] English:** and vlc to encode in streaming services right and then you need to go lower and lower and the  
**Translation:** 

**[12462.02s] English:** question was where up to where we can can we go and this question is very important because there  
**Translation:** 

**[12468.16s] English:** are many use cases where you need to be fast and it's when you have feedback interaction right we  
**Translation:** 

**[12475.12s] English:** are not just listening to something you're actually controlling it right because and that's a big  
**Translation:** 

**[12480.00s] English:** difference that compared to what we've done so far is that I need video to have a feedback on  
**Translation:** 

**[12486.56s] English:** something that is happening live, whether it's a drone flying, whether it's controlling a humanoid  
**Translation:** Vocabulary: drone: 无人机; humanoid: 类人机器人

**[12492.96s] English:** robot from distance, whether it's controlling a hover, whether it's playing a video game in the  
**Translation:** 

**[12498.88s] English:** cloud gaming, because this is what I did on a previous job, right? I was CTO of a cloud gaming  
**Translation:** 

**[12505.04s] English:** startup. And this is a very interesting topic because you push to the limit the network. You  
**Translation:** 

**[12512.70s] English:** need to care not about the quality like we've done on video and we've talked about with X264.  
**Translation:** 

**[12519.60s] English:** You care about latency because a millisecond is meaningful when you're controlling a car,  
**Translation:** 

**[12528.34s] English:** right? Well, you've seen, you've used Waymos, right? When Waymos don't work, and that happens  
**Translation:** 

**[12534.18s] English:** even if one...  
**Translation:** 

**[12535.04s] English:** 1% of the time, there is someone that is basically remote controlling that. And this is exactly the  
**Translation:** 

**[12541.60s] English:** stuff that we're building. It's really an SDK platform to do end-to-end control of machines.  
**Translation:** 

**[12550.00s] English:** So, this comes up quite a lot in a lot of different contexts in robotics. So, obviously,  
**Translation:** 

**[12555.12s] English:** teleoperation, teleop is becoming more and more important, including for training  
**Translation:** 

**[12563.20s] English:** robots via machine learning.  
**Translation:** Vocabulary: teleoperation: 远程操作

**[12565.04s] English:** Yes. And what we do is a bit different from everyone else, is that we take only one socket,  
**Translation:** 

**[12571.52s] English:** one connection, which is a quick protocol based on UDP, which is interesting because it's done for  
**Translation:** Vocabulary: socket: 接口

**[12578.24s] English:** low latency. It doesn't have two of the, what we call the TCP end-of-line problem and the  
**Translation:** 

**[12582.32s] English:** HTTP end-of-line problem. It's sifted by default, but on the same wire, we send multiple streams,  
**Translation:** Vocabulary: latency: 低延迟; sifted: 过滤

**[12588.32s] English:** like multiple strikes. We send audio, we send video, but we also send the commands, right?  
**Translation:** 

**[12592.64s] English:** Mouse, keyboard, gamepad, and so on. And we do that while maintaining coherence, right?  
**Translation:** Vocabulary: coherence: 连贯性

**[12600.00s] English:** synchronization because what people don't realize is that all the clocks actually drift and when  
**Translation:** 

**[12607.26s] English:** you're controlling a robot a robot is going to have like two cameras five cameras ten cameras  
**Translation:** Vocabulary: drift: 偏差; synchronization: 同步

**[12611.98s] English:** a ton of captors gps and so on and if you want to train correctly your robotic ai model you need to  
**Translation:** 

**[12618.24s] English:** have all those that are in sync and currents and what we've done and it's all the stuff that we  
**Translation:** Vocabulary: captors: 传感器

**[12624.12s] English:** learn on vlc in broadcast in real time and mpeg ts that currents know well is that we account for  
**Translation:** 

**[12630.94s] English:** clock drifting and so when i record a kyber stream a robot i am sure that it's going to be predictive  
**Translation:** Vocabulary: drifting: 时钟漂移; predictive: 具有预测性

**[12638.98s] English:** in the way you play it back and so when you're going to do recording and training of your ai  
**Translation:** 

**[12644.86s] English:** model you need to be sure that every time you retrain based on the data the data is going to  
**Translation:** 

**[12650.38s] English:** stay coherent and clocks actually drift  
**Translation:** 

**[12653.64s] English:** you need to be sure that every time you retrain based on the data the data is going to stay  
**Translation:** Vocabulary: coherent: 条理清晰

**[12654.10s] English:** coherent and clocks actually drift like the existing solution works with one camera once  
**Translation:** 

**[12657.22s] English:** you're going to a five or say it's more complex so you want to make sure that the visual snapshot  
**Translation:** Vocabulary: snapshot: 快照

**[12665.54s] English:** perfectly matches the time it actually happened exactly and also if you're going to control right  
**Translation:** 

**[12670.66s] English:** i do something on robot i need to be sure that it is actually happening at that precise time right  
**Translation:** 

**[12676.34s] English:** and so we have on the the server which would be a robot a time of like  
**Translation:** 

**[12680.82s] English:** re-time stamping mechanism accounting for clock drift for that  
**Translation:** Vocabulary: stamping: 时间戳

**[12684.10s] English:** right so that's one of the use case um of kyber to to control robots um i also think like remote  
**Translation:** 

**[12691.46s] English:** drones remote whether it's defense or non-defense remote cars remote submarines there is many places  
**Translation:** Vocabulary: drones: 遥控无人机; submarines: 遥控潜艇

**[12699.06s] English:** industry or remote surgery where the experts cannot go everywhere the machine is because  
**Translation:** 

**[12706.74s] English:** either dangerous or it's too costly right so you you allow people to have machines next to you right  
**Translation:** 

**[12714.10s] English:** so you you allow people to have machines next to you right so you you allow people to have machines next to you right  
**Translation:** 

**[12714.42s] English:** the goal of kyber is to make distance disappear because it's either projection of skills or  
**Translation:** Vocabulary: projection: 投影

**[12720.00s] English:** projection of power right so imagine we are all like you've seen the meta reban and everyone else  
**Translation:** 

**[12726.46s] English:** right you need to stream there right because you're not going to run anything over there right  
**Translation:** 

**[12730.38s] English:** so you need gpu power that's on the cloud on the phone to stream that and so all of these use cases  
**Translation:** 

**[12735.62s] English:** needs to be not about extremely low latency but real-time latency for video and so that means you  
**Translation:** Vocabulary: latency: 延迟

**[12742.74s] English:** need we're toying with the encoders so that the encoders encode a frame in four milliseconds and  
**Translation:** 

**[12749.28s] English:** and kiran with his company also goes under those type of lights of latency because you need to  
**Translation:** Vocabulary: encode: 编码; encoders: 编码器; milliseconds: 毫秒

**[12757.12s] English:** optimize at max the local latency right because it's decoder the encoder and so on because this  
**Translation:** 

**[12768.32s] English:** time is going to be added to your networking time so and it's not just about low latency it's also  
**Translation:** Vocabulary: optimize: 优化

**[12774.62s] English:** about like reliability we do clever things like  
**Translation:** 

**[12778.76s] English:** you  
**Translation:** 

**[12779.28s] English:** forward error correction right so for other correction is you over transmit a bit of data  
**Translation:** 

**[12784.78s] English:** right a few percent um and while over transmit you allow to lose some packets because all of that is  
**Translation:** Vocabulary: transmit: 发送

**[12792.48s] English:** very difficult over a internet network where you're going to do things very far away and  
**Translation:** 

**[12799.48s] English:** if you check that all packets are delivered you add a ton of latency if you don't want latency  
**Translation:** 

**[12805.20s] English:** what we do is that we over transmit some data that you don't want to transmit  
**Translation:** 

**[12809.28s] English:** you can retrans reconstruct on the client side when there is um things that are broken right so  
**Translation:** Vocabulary: reconstruct: 重新构建

**[12815.20s] English:** um and we um if you a few days weeks ago we are uh doing the demo around uh las vegas for the ces  
**Translation:** 

**[12822.32s] English:** about we had a rover that is fully 3 printed it's very simple it's a carroright a small car with a  
**Translation:** Vocabulary: carroright: 小汽车; rover: 火星车

**[12829.60s] English:** telescopic arm and it was actually controlled from france right and the the video uh was uh with a  
**Translation:** 

**[12836.32s] English:** webcam and a very small server rated small small piece  
**Translation:** Vocabulary: telescopic: 伸缩臂

**[12840.00s] English:** PCB but basically running and send that to someone that is on the other side of the planet  
**Translation:** 

**[12844.62s] English:** and so there is so many use cases you can also think about having AI who are going to control  
**Translation:** 

**[12851.50s] English:** many drones and so on and the technically we need to be amazing in video we need to be amazing at  
**Translation:** 

**[12857.84s] English:** networking we need to care about any milliseconds in networking in encoding time in decoding time  
**Translation:** Vocabulary: drones: 无人机; encoding: 编码

**[12863.76s] English:** and also you need to integrate very low level so sync everything together well but how like what  
**Translation:** 

**[12869.80s] English:** kind of latency can you get to like why when you say milliseconds what what's the goal so my goal  
**Translation:** Vocabulary: integrate: 整合; latency: 延迟; milliseconds: 毫秒

**[12875.54s] English:** is four milliseconds glass to glass latency um what's glass to glass so it's easy right you have  
**Translation:** 

**[12881.22s] English:** a computer which is running a program right probably a video game and this one is actually  
**Translation:** 

**[12886.06s] English:** running right it could be it's an example of a robot right and you have the replicate that is  
**Translation:** 

**[12892.54s] English:** done through the network and you want if you take a 1000 hertz camera you can  
**Translation:** Vocabulary: hertz: 频率

**[12899.50s] English:** take a 1000 hertz camera and you can take a 1000 hertz camera and you can take a 1000 hertz camera  
**Translation:** 

**[12899.78s] English:** and you can take a picture and you want that to be at four milliseconds four milliseconds means 240  
**Translation:** 

**[12904.44s] English:** hertz right yeah it's not um so far we we achieve um seven milliseconds from a windows to windows or  
**Translation:** 

**[12913.34s] English:** window to mac um and if you look in the timing most there is around 3.5 milliseconds inside the  
**Translation:** 

**[12921.50s] English:** nvidia uh hardware encoder and around two milliseconds on the intel decoder right so  
**Translation:** 

**[12928.06s] English:** like the encoder has to be at 4 milliseconds and if you look in the timing most there is around  
**Translation:** 

**[12929.78s] English:** 3.5 milliseconds and if you look in the timing most there is around 3.5 milliseconds and if you look  
**Translation:** 

**[12929.84s] English:** plus the decoder is already six milliseconds right so in order to go down we need either to have  
**Translation:** 

**[12934.80s] English:** some other type of codecs um or some better encoder that are faster uh but four milliseconds  
**Translation:** 

**[12942.92s] English:** is would be the graal that's pretty nuts i love it though i don't think anyone's ever achieved that  
**Translation:** Vocabulary: graal: 理想解

**[12948.46s] English:** right that's fast you can achieve that with custom hardware with sdi with professional hardware but  
**Translation:** 

**[12955.90s] English:** i want that to work over the internet i want that  
**Translation:** 

**[12959.78s] English:** the  
**Translation:** 

**[12960.00s] English:** to work with any robots where you're going to have a small jetson nano in it or or n150 right  
**Translation:** Vocabulary: jetson: 杰森系列

**[12966.18s] English:** i want that because there is going to be millions of robots or drones are just rolling robots or  
**Translation:** 

**[12973.16s] English:** flying robots or swimming robots right it's just you a machine that you control and in order either  
**Translation:** 

**[12980.10s] English:** you need to teleoperate them or when everything will be fully autonomous you need to tele observe  
**Translation:** 

**[12987.06s] English:** them right you need to check what's happening yeah and in my view in the future like all those  
**Translation:** Vocabulary: autonomous: 自主

**[12992.96s] English:** remote cars will be tele observer observed by an ai model which is just going to say well  
**Translation:** 

**[12999.02s] English:** everything is going good and when it's not good say hey there is a problem and then you have an  
**Translation:** 

**[13003.64s] English:** operator right and this is going to be about safety right when you have your humanoid taking  
**Translation:** 

**[13007.86s] English:** care of your grandma or my grandma i want to be sure that everything goes well and i'm not in  
**Translation:** Vocabulary: humanoid: 类人形机器人

**[13012.88s] English:** those type of horrible scenarios where the robot is dangerous or when i'm  
**Translation:** 

**[13017.06s] English:** driving i want like the car to to stop when it should stop and if needed someone takes care of  
**Translation:** Vocabulary: scenarios: 情景

**[13023.66s] English:** that right and so there is so many cases scenarios about real time and so the goal of kyber is to make  
**Translation:** 

**[13030.54s] English:** real-time control of machine distance disappear it's it's incredible and some of the same  
**Translation:** 

**[13037.50s] English:** technologies some of the same ideas we've been talking about is is connected to what you're  
**Translation:** 

**[13041.86s] English:** and for for me it's amazingly challenging right because i would say that on video i'm doing a  
**Translation:** 

**[13047.54s] English:** but networking i have so much more to learn right it's uh um about like congestion protocols  
**Translation:** 

**[13053.70s] English:** bit rate adaptation in real time um but it's it's quite funny and and so i created this project and  
**Translation:** Vocabulary: adaptation: 适应性; congestion: 拥塞

**[13060.82s] English:** and we we have fundraised in the us of course but it's open source right this is important  
**Translation:** 

**[13065.78s] English:** right like we've not said that right but everything on kyber is open source how do you make money  
**Translation:** Vocabulary: fundraised: 募集资金

**[13071.30s] English:** it's a dual license commercial and agpl right you remember what you said about about uh  
**Translation:** 

**[13077.06s] English:** licenses. Basically, if you want  
**Translation:** 

**[13080.00s] English:** to use kyber in your product you must have your full product open source if you want to use this  
**Translation:** 

**[13085.50s] English:** amazing technology but not open source you pay the commercial license right so the small people or  
**Translation:** 

**[13091.48s] English:** the the the hobbyist and the the very small guys who want to do that they can use the technology  
**Translation:** 

**[13096.86s] English:** they build something that is open source and cool and if you're a large company you're going to have  
**Translation:** 

**[13101.36s] English:** the support all the ip the right modification and so on so um yeah it's really cool and and  
**Translation:** 

**[13108.64s] English:** and also i'm building robots and i love that right like yeah like the the rover we have is  
**Translation:** Vocabulary: modification: 修改; rover: 火星车

**[13113.74s] English:** 3d printed um we are finishing a demo where it's an actual wing right like a type of drone wings  
**Translation:** 

**[13119.84s] English:** that is also fully 3d printed um we are trying to do a sailboat that is uh 3d printed uh and and  
**Translation:** Vocabulary: drone: 无人驾驶飞行器; sailboat: 帆船

**[13128.40s] English:** and we'll work on some humanoids of course they are not going to be very good robots right it's  
**Translation:** 

**[13133.08s] English:** not our job but we're here for everyone to make robots cool uh you're talking to the right  
**Translation:** Vocabulary: humanoids: 类人机器人

**[13138.62s] English:** guy i love robots there's a bunch of them upstairs uh and teleop is going to be really  
**Translation:** 

**[13143.66s] English:** really important especially as the number of robots kills across the world so 100 let's talk  
**Translation:** 

**[13148.24s] English:** about the future of um multimedia ffmpeg vlc but some of the codecs we didn't really mention av2  
**Translation:** 

**[13156.96s] English:** so can we just lay out what is av2 what is the hope for it what is h265 h266 so av1 is this codec  
**Translation:** 

**[13167.76s] English:** that he's done  
**Translation:** 

**[13168.60s] English:** by the aliens for open media right where there is uh google netflix amazon apple uh video land  
**Translation:** 

**[13175.48s] English:** where we try to make a royalty free very good codec right and now it's being deployed but  
**Translation:** 

**[13180.98s] English:** actually the codec was finished in 2018 but a codec takes years to be used in wide scenarios  
**Translation:** Vocabulary: deployed: 部署; scenarios: 应用场景

**[13190.74s] English:** right so av2 is the next generation of this codec it's 30 better right so if you keep  
**Translation:** 

**[13198.58s] English:** the same uh quality  
**Translation:** 

**[13200.00s] English:** you got 30% bandwidth reduction compared to AV1.  
**Translation:** 

**[13203.24s] English:** What's the connection with the David and AV2?  
**Translation:** Vocabulary: bandwidth: 带宽

**[13206.56s] English:** We are going to do a David 2, right?  
**Translation:** 

**[13208.86s] English:** That I call DeVid, because De is 2 in French.  
**Translation:** 

**[13213.04s] English:** Ah, well done.  
**Translation:** 

**[13213.84s] English:** And you have to know that David is an actual,  
**Translation:** 

**[13216.14s] English:** what we call a recursive acronym, right?  
**Translation:** 

**[13218.32s] English:** Because it means D, David, is an AV1 decoder, right?  
**Translation:** Vocabulary: recursive: 递归的

**[13223.24s] English:** Oh, nice, nice.  
**Translation:** 

**[13224.92s] English:** I didn't even think of that.  
**Translation:** 

**[13226.26s] English:** And people should know that David is spelled with a 1.  
**Translation:** 

**[13229.52s] English:** Yes.  
**Translation:** 

**[13230.14s] English:** And so DeVid 2.  
**Translation:** 

**[13232.36s] English:** It's going to be spelled with a 2.  
**Translation:** 

**[13233.62s] English:** It's going to be DeAV2D.  
**Translation:** 

**[13236.30s] English:** Sorry, I don't know how you pronounce that.  
**Translation:** 

**[13238.42s] English:** And again, we did a demo at the CES of VLC  
**Translation:** 

**[13242.38s] English:** running the first demo of AV2.  
**Translation:** 

**[13244.42s] English:** So can you clarify to me the specification of AV2  
**Translation:** 

**[13249.16s] English:** and then the encoding and the decoding?  
**Translation:** Vocabulary: encoding: 编码; specification: 规范

**[13252.52s] English:** Sure.  
**Translation:** 

**[13253.18s] English:** So the specification is like the document  
**Translation:** 

**[13256.84s] English:** who explains how the codec is supposed to work, right?  
**Translation:** 

**[13259.88s] English:** Yes.  
**Translation:** 

**[13260.00s] English:** And that's really AV2.  
**Translation:** 

**[13262.00s] English:** That is AV2, like H.264.  
**Translation:** 

**[13264.04s] English:** Yeah.  
**Translation:** 

**[13264.94s] English:** Then you have an encoder.  
**Translation:** 

**[13266.98s] English:** The current encoder is called AVM  
**Translation:** 

**[13269.22s] English:** and there will probably be other encoders,  
**Translation:** Vocabulary: encoders: 编码器

**[13271.88s] English:** probably one called SVT-AV2.  
**Translation:** 

**[13274.10s] English:** And those are the encoder.  
**Translation:** 

**[13275.36s] English:** The same way X.264 is an encoder to H.264.  
**Translation:** 

**[13278.82s] English:** The same way that X.265 is an encoder for the H.265 codec.  
**Translation:** 

**[13284.82s] English:** And the decoders for AV1 is David.  
**Translation:** 

**[13290.00s] English:** The decoder for AV2 is David2.  
**Translation:** Vocabulary: decoders: 解码器

**[13293.26s] English:** The decoder for H.264 is FF.H.264 inside FFmpeg.  
**Translation:** 

**[13300.46s] English:** The decoder for HEVC is FF.HEVC inside FFmpeg.  
**Translation:** 

**[13306.36s] English:** And there is a next generation codec from the MPEG world  
**Translation:** 

**[13311.48s] English:** after H.264, H.265.  
**Translation:** 

**[13313.76s] English:** There is one that is called H.266, also known as VVC.  
**Translation:** 

**[13319.26s] English:** So H.EVC.  
**Translation:** 

**[13320.00s] English:** VVC is H.265.  
**Translation:** 

**[13322.78s] English:** VVC is H.266.  
**Translation:** 

**[13326.42s] English:** Why is H.266 super sexy so much better?  
**Translation:** 

**[13329.86s] English:** So the question often we have is why are they two names?  
**Translation:** 

**[13333.70s] English:** Because most of the time it is a conjunct work from the ISO world and the ITU, which is the International Telecommunication Union.  
**Translation:** 

**[13344.32s] English:** These are these two regulatory bodies.  
**Translation:** Vocabulary: conjunct: 联合; telecommunication: 电信

**[13346.08s] English:** One is a private entity and one is the United Nations.  
**Translation:** 

**[13348.70s] English:** Which one is the private?  
**Translation:** 

**[13349.68s] English:** ISO is private.  
**Translation:** 

**[13350.54s] English:** In theory, H.264 is MPEG-4 part 10 H.264 slash AVC.  
**Translation:** 

**[13361.76s] English:** And this is the full name.  
**Translation:** 

**[13363.86s] English:** Nice.  
**Translation:** 

**[13364.32s] English:** So it's the concatenation of the ISO name and the ITU name.  
**Translation:** 

**[13368.00s] English:** Yeah.  
**Translation:** Vocabulary: concatenation: 连接

**[13368.44s] English:** Even though they work together.  
**Translation:** 

**[13369.98s] English:** This is politics, historical.  
**Translation:** 

**[13372.88s] English:** And for HEVC, it's MPEG-H H.265 HEVC.  
**Translation:** 

**[13378.66s] English:** Got it.  
**Translation:** 

**[13379.08s] English:** And there is...  
**Translation:** 

**[13379.66s] English:** There is H.266, which is also named VVC.  
**Translation:** 

**[13382.90s] English:** Is there a high-level thing to say about the improvement?  
**Translation:** 

**[13385.54s] English:** 30% each generation is the best summary.  
**Translation:** 

**[13389.14s] English:** This is true both for the AV products and the H.264, 5, 6.  
**Translation:** 

**[13394.98s] English:** So the professionals who are listening to us are going to kill us because they say, no, it's 35%, 25%.  
**Translation:** 

**[13400.64s] English:** It's 50, it's 50, it's blah, blah, blah.  
**Translation:** 

**[13401.58s] English:** But globally, you need to know that HEVC is 30% better than H.264.  
**Translation:** Vocabulary: globally: 全世界

**[13407.66s] English:** H.263 is 30% better than H.264.  
**Translation:** 

**[13409.66s] English:** H.265.  
**Translation:** 

**[13410.06s] English:** Because there are so many cases and so many scenarios.  
**Translation:** 

**[13412.76s] English:** For example, there are cases, especially for screen recording, where the gains are humongous.  
**Translation:** Vocabulary: humongous: 巨大; scenarios: 情况

**[13420.20s] English:** Because you arrive, you have the right tool that is done for that.  
**Translation:** 

**[13423.38s] English:** And so for a specific video, a new generation is going to give you 70% gain or 80% gain.  
**Translation:** 

**[13430.64s] English:** But there used to be a ton more codecs.  
**Translation:** 

**[13432.92s] English:** But now the two main codecs for transmission are the H.264, H.265, H.266.  
**Translation:** 

**[13438.44s] English:** And the other is AV1.  
**Translation:** 

**[13440.00s] English:** And I guess the major difference would be the cost of encoding.  
**Translation:** Vocabulary: encoding: 编码

**[13444.78s] English:** Yes, and the royalty of the patents.  
**Translation:** 

**[13447.94s] English:** And this is the reason why you see the AV version of Codex is because they try to be as royalty-free, which means no cost for the patents as much as possible.  
**Translation:** Vocabulary: codex: 法典

**[13459.50s] English:** Because what you need to know, and we've not talked about that so far, is that multimedia is what we call a patent minefield.  
**Translation:** 

**[13466.82s] English:** There are two places where you have the most patents.  
**Translation:** Vocabulary: minefield: 专利雷区

**[13470.72s] English:** It's everything related to 3G, 4G, 5G, RF, and multimedia, because it's very mathematical and you can get great gains and so on.  
**Translation:** 

**[13480.86s] English:** So Google and Meta and Netflix wanted something where it was royalty-free.  
**Translation:** Vocabulary: mathematical: 数学相关的; multimedia: 多媒体的

**[13486.78s] English:** There are people who say that they have patents outside, but they are fringe patents, right?  
**Translation:** 

**[13490.70s] English:** So it's mostly true that it's patent-free.  
**Translation:** Vocabulary: fringe: 边缘专利

**[13493.36s] English:** We should extend patent checking was done.  
**Translation:** 

**[13496.82s] English:** As part of the standardization process in AV1, AV2, whereas patents are not even discussed in the MPEG world.  
**Translation:** Vocabulary: patent: 专利; standardization: 标准化

**[13506.40s] English:** Patents are off-topic completely.  
**Translation:** 

**[13508.36s] English:** Can you educate me at the patents side?  
**Translation:** 

**[13510.50s] English:** So usually, so MPEG does a format, right?  
**Translation:** 

**[13513.04s] English:** And then there is, everyone comes around and say, well, I have all those patents or formats.  
**Translation:** 

**[13518.38s] English:** And they do usually a union called, what's called MPEG LA, MPEG Licensing Association.  
**Translation:** 

**[13525.50s] English:** And you put all those.  
**Translation:** 

**[13526.82s] English:** You put all your patents in, and then you ask everyone who's using this format to pay for it.  
**Translation:** 

**[13531.64s] English:** Wait, can you elaborate?  
**Translation:** Vocabulary: elaborate: 详细说明

**[13532.82s] English:** What does it mean to have a patent of a codec?  
**Translation:** 

**[13534.44s] English:** Why is there many patents?  
**Translation:** 

**[13537.56s] English:** Imagine I'm doing something where I'm going to, instead of doing blocks, which are square, I'm going to do rectangles, right?  
**Translation:** 

**[13544.10s] English:** Oh, so every idea.  
**Translation:** Vocabulary: rectangles: 长方形

**[13545.58s] English:** Yes.  
**Translation:** 

**[13545.92s] English:** Somebody patents it.  
**Translation:** 

**[13547.12s] English:** Yes.  
**Translation:** 

**[13549.46s] English:** Oh, man.  
**Translation:** 

**[13551.04s] English:** Yes.  
**Translation:** 

**[13551.84s] English:** Oh, man.  
**Translation:** 

**[13553.34s] English:** People and how many lawyers are there?  
**Translation:** 

**[13556.82s] English:** I mean, it pays for a lot of lawyers, right?  
**Translation:** 

**[13558.04s] English:** The biggest issue is not the following, right?  
**Translation:** 

**[13560.00s] English:** Because at the time of H.264, the patents were, let's call it, like, sane.  
**Translation:** 

**[13564.64s] English:** But there was so much money in that, that for HEVC, there were a ton of things that were pushed inside the specification, which are not useful in 99.9% of the time, but just one could add a patent on it.  
**Translation:** 

**[13582.20s] English:** And so it became that for HEVC licensing, there was MPEG-LA plus another patent pool called HEVC Advance, plus, I think, was Nokia was outside of the patent pool.  
**Translation:** Vocabulary: specification: 规范

**[13594.54s] English:** Yeah, a few of them are outside and some other one.  
**Translation:** 

**[13596.88s] English:** And so it was impossible to license, right?  
**Translation:** 

**[13599.00s] English:** And I think that several months ago, HP decided that they were going to remove support from HEVC in their Windows laptops because the cost was increasing of those patents.  
**Translation:** 

**[13610.90s] English:** And it arrived at a point where, and there was uncapped pad.  
**Translation:** 

**[13616.32s] English:** And so for YouTube or Netflix, we could talk about hundreds of millions of dollars of licensing for patents per year.  
**Translation:** 

**[13624.88s] English:** And they said, you know what, at 100 million per year, you know, I could create my own codec.  
**Translation:** 

**[13630.18s] English:** And this is what they did.  
**Translation:** 

**[13631.04s] English:** And so that's why we have the Open Media Alliance, Alliance for Open Media, where we are part of, that is, that created AV1 and creates AV2.  
**Translation:** 

**[13639.54s] English:** We create also audio codecs.  
**Translation:** 

**[13643.16s] English:** But, yes, so the main difference would be that.  
**Translation:** 

**[13646.26s] English:** And because you need to work around the patents or go do some things that are not patented, a lot of things are different, right?  
**Translation:** 

**[13653.98s] English:** The basic things that were done in MPEG-2 30 years ago are, of course, out of patents.  
**Translation:** 

**[13659.98s] English:** But so, for example, there is things like Golden Frame, S-Frame or different type of…  
**Translation:** 

**[13666.82s] English:** These are all patented ideas.  
**Translation:** 

**[13668.24s] English:** Yeah, no, I can't believe it.  
**Translation:** 

**[13669.44s] English:** It's not butter.  
**Translation:** 

**[13670.06s] English:** I can't believe it's not a B-Frame.  
**Translation:** 

**[13672.46s] English:** I mean, it's kind of what it is.  
**Translation:** 

**[13674.02s] English:** In some ways, it's like a…  
**Translation:** 

**[13675.38s] English:** Oh, so it's a different variant of a B-Frame.  
**Translation:** 

**[13677.40s] English:** Yeah, that's to try and sidestep.  
**Translation:** 

**[13679.66s] English:** I think…  
**Translation:** Vocabulary: sidestep: 绕开

**[13680.00s] English:** And so you need to have double creativity, right? Creativity in terms of being more efficient, but creativity of being sure that you don't infringe existing patents. And so, for example, VVC has all the patents of HEVC plus new ones, right? That's why AV2 tries to be as royalty-free as possible.  
**Translation:** 

**[13700.78s] English:** To what degree does FFmpeg and VLC have to think about this kind of stuff?  
**Translation:** 

**[13703.96s] English:** We don't. And one of the reasons why VLC was in France is that France rejects software patents.  
**Translation:** 

**[13711.18s] English:** So most of those patents are illegal in France.  
**Translation:** 

**[13715.30s] English:** Because I once made the calculus that if I had to pay all the licensing fee for VLC, I needed to pay more than 200 euros per user, right?  
**Translation:** 

**[13727.30s] English:** The same in dollars.  
**Translation:** Vocabulary: calculus: 计算

**[13728.68s] English:** But most of those patents are invalid in Europe because those are called VLCs.  
**Translation:** 

**[13733.96s] English:** It's basically mathematical patents or idea patents, and they are not valid in Europe.  
**Translation:** Vocabulary: mathematical: 数学的

**[13739.78s] English:** Let me just at a high level, just out of curiosity.  
**Translation:** 

**[13743.52s] English:** So the meme online and the interwebs on X and Twitter and so on.  
**Translation:** Vocabulary: interwebs: 互联网

**[13748.38s] English:** And my own friends in Europe, the sense is that Europe is not friendly to entrepreneurship.  
**Translation:** 

**[13757.34s] English:** They over-regulate, there's too much bureaucracy and so on.  
**Translation:** Vocabulary: bureaucracy: 官僚主义; entrepreneurship: 创业

**[13761.88s] English:** Is there anything positive?  
**Translation:** 

**[13763.96s] English:** Positive to say, is there hope for entrepreneurship in the future of Europe?  
**Translation:** 

**[13767.86s] English:** Is Europe over from a tech perspective?  
**Translation:** 

**[13772.00s] English:** Just look at the two of us, right?  
**Translation:** 

**[13773.36s] English:** It's notable that there's two people from the European continent on this podcast talking about video.  
**Translation:** 

**[13779.68s] English:** It's fair to say the community has waited heavily.  
**Translation:** 

**[13782.32s] English:** What you probably don't see yet is that there is a new generation of entrepreneurs in Europe and mostly in France.  
**Translation:** 

**[13791.98s] English:** UK has done it since a long time.  
**Translation:** Vocabulary: entrepreneurs: 企业家

**[13793.84s] English:** Because it's been a long time.  
**Translation:** 

**[13793.96s] English:** Because, well, it's more Anglo-Saxon type of business, look at business.  
**Translation:** 

**[13800.00s] English:** but especially like what happened in france and of course sometimes a bit overdone with everything  
**Translation:** 

**[13805.44s] English:** called french tech but today most of the people who come on the market wants to create a startups  
**Translation:** Vocabulary: overdone: 过度炒作; startups: 初创企业

**[13811.76s] English:** 15 years ago it wasn't the case everyone wanted to work on big companies because when you failed  
**Translation:** 

**[13818.00s] English:** in in france for example 20 years ago 15 years ago and you destroy your company which is normal  
**Translation:** 

**[13824.72s] English:** for startup right you you were not allowed to create a new company right there was a lot of  
**Translation:** 

**[13829.04s] English:** stigma this team is gone um there is so many things happening on ai in france and so on right  
**Translation:** 

**[13835.68s] English:** so there is sure over regulations i i know that right but it has some good things also i mean  
**Translation:** 

**[13846.08s] English:** is there some paralyzing aspects you know if i look at the case of somebody i've uh  
**Translation:** Vocabulary: paralyzing: 使人瘫痪的

**[13851.68s] English:** become close with paul durov you know he was uh uh blamed directly by the french government  
**Translation:** 

**[13859.92s] English:** for the kind of things his quote platform was hosting i could see the same kind of stuff  
**Translation:** 

**[13867.36s] English:** basically just as an example vlc being blamed for the kind of videos that people are watching right  
**Translation:** 

**[13874.00s] English:** right like we had we like we we had issues like we like i mean is that that's the pressure that  
**Translation:** 

**[13880.40s] English:** people worry about because if you have to think about that kind of stuff when you're kind of  
**Translation:** 

**[13884.72s] English:** just obsessed about well you don't think about it and that's that's okay right  
**Translation:** 

**[13889.04s] English:** like but what if they come in when if they show up and there is no office fiddleland doesn't have  
**Translation:** 

**[13893.36s] English:** office i mean this is what happened with paula they arrested him right so arrested him for  
**Translation:** Vocabulary: fiddleland: 虚构之地

**[13897.52s] English:** particular videos or or a particular content that's being shared on the platform sure i don't  
**Translation:** 

**[13902.40s] English:** have any platform everything is on the client side yeah but they're they can still arrest you  
**Translation:** 

**[13907.28s] English:** on what ground i'm not sharing anything i'm not the content doesn't go through my my stuff for  
**Translation:** 

**[13912.08s] English:** sure but it's still lawyer fees that's the problem yes that's correct it's paperwork so they actually  
**Translation:** 

**[13919.04s] English:** have to do it and they're not going to be able to do it because they're not going to be able to do it  
**Translation:** 

**[13920.00s] English:** you would win easily because you're on the right side but the thing is there is a degree to which  
**Translation:** 

**[13930.06s] English:** they suffocate you with paperwork that's that's the downside of bureaucracy through paperwork  
**Translation:** 

**[13934.22s] English:** through process yes you know it's the kafka you have to to realize that one of the good  
**Translation:** Vocabulary: bureaucracy: 官僚主义; downside: 缺点; kafka: 卡夫卡; suffocate: 窒息

**[13939.82s] English:** things for example um in france or most of europe is that the the answering to a court order does  
**Translation:** 

**[13948.70s] English:** not make you bankrupt right it's not like in the u.s where it can actually bankrupt you right  
**Translation:** 

**[13953.70s] English:** there is the way the law system work is that like i i receive lawyers letters every week right  
**Translation:** 

**[13963.14s] English:** and i can tell you that the cost of lawyer fees for video land is less than ten thousand dollars  
**Translation:** 

**[13970.66s] English:** per year right right so that's not really scary i mean similar with paul the intelligence agencies  
**Translation:** 

**[13976.04s] English:** tried to like say can you put it back  
**Translation:** 

**[13978.54s] English:** do it  
**Translation:** 

**[13978.70s] English:** yes two of them what do you say no i was a lot less polite i see you uh yeah yeah you're  
**Translation:** 

**[13987.78s] English:** basically saying hell no like if we had to compromise our software we would shut it down  
**Translation:** 

**[13992.74s] English:** this is clear and what's the definition of compromise like allowing a government to do a  
**Translation:** 

**[13998.62s] English:** backdoor there is no code that gets into vlc that we don't control and the way we compile vlc you  
**Translation:** 

**[14005.58s] English:** would call me completely paranoid like  
**Translation:** Vocabulary: backdoor: 后门; paranoid: 多疑

**[14008.70s] English:** we compile on boxes that are offline where we start by compiling the compiler we do everything  
**Translation:** 

**[14015.94s] English:** offline on on places that have never been connected to the internet uh we the way we do  
**Translation:** Vocabulary: compiling: 编译

**[14022.20s] English:** signing there is double signature um especially because for example we've seen and we believe it's  
**Translation:** 

**[14028.90s] English:** a it's a governmental agency that is not from uh the western world to try to push a fake binary  
**Translation:** Vocabulary: binary: 二元对立; governmental: 政府机构

**[14035.08s] English:** into our own servers and that scared us a lot  
**Translation:** 

**[14038.70s] English:** and video land  
**Translation:** 

**[14040.00s] English:** is open source how can you kill it like i moved to where right i moved to malta i moved to uh  
**Translation:** 

**[14047.04s] English:** i don't know cayman islands and i changed the domain name and i i start again right like  
**Translation:** Vocabulary: cayman: 开曼群岛; malta: 马耳他

**[14054.24s] English:** vlc is a tool um it's a tool that is going to help people doing things uh we are not a platform  
**Translation:** 

**[14061.92s] English:** um and for patents well i'm sorry but most of the patents like you shouldn't be able to patent math  
**Translation:** Vocabulary: patent: 专利

**[14069.52s] English:** and matrixes like this is wrong does vlc ever like censor the kind of videos it can play and  
**Translation:** 

**[14076.56s] English:** not based on the content of the video no never we never do that because like a vlc is completely  
**Translation:** Vocabulary: censor: 审查

**[14084.88s] English:** offline doesn't talk to any server so we don't know anything that you're using the software for  
**Translation:** 

**[14089.68s] English:** so again there's no government that can say you know like the french government come in and say  
**Translation:** 

**[14095.76s] English:** we don't want uh i think anime is destructive to  
**Translation:** 

**[14099.52s] English:** society we don't want any anime not a lot of people no they cannot they cannot do that and  
**Translation:** Vocabulary: anime: 动画; cannot: 不能

**[14104.24s] English:** also what they tried is to say hey i want to know if that person watched that type of video  
**Translation:** 

**[14109.36s] English:** and the answer is like no idea so no on that too so for surveillance no no no because the  
**Translation:** 

**[14115.28s] English:** only infrastructure we have is a downloading infrastructure there is no telemetry in vlc  
**Translation:** 

**[14120.16s] English:** right it would be difficult because of the international nature it would be difficult  
**Translation:** Vocabulary: telemetry: 遥测系统

**[14124.56s] English:** for you to incorporate that code because there would be someone in the uk and someone in germany  
**Translation:** 

**[14129.52s] English:** in the us as part of video and who'd be able to see that it would be extremely difficult the only  
**Translation:** Vocabulary: incorporate: 吸收

**[14133.76s] English:** thing that we can do which happened is like we had the issue we had the case with some police  
**Translation:** 

**[14138.48s] English:** in the us who said we have a murder case right and the file is destructed or doesn't play in  
**Translation:** Vocabulary: destructed: 损毁的文件

**[14144.40s] English:** that version of vlc could you help us right we never have access to the video it's like  
**Translation:** 

**[14148.40s] English:** a normal support right oh it's really about playing the file yes and like i remember in  
**Translation:** 

**[14153.36s] English:** the middle of the afghan war right i received an email from someone in the army right i had  
**Translation:** 

**[14159.52s] English:** don't remember  
**Translation:** Vocabulary: afghan: 阿富汗的

**[14160.00s] English:** the grades right it was just like we have a big issue with the latest version of vlc  
**Translation:** 

**[14164.96s] English:** because it doesn't play correctly the file on an rtsp server that we have where there is all the  
**Translation:** 

**[14171.76s] English:** the movies and he says vlc is very important for the moral on the troop on the ground right  
**Translation:** 

**[14176.48s] English:** because at night i think it might be boring right so they have a collection of videos to watch  
**Translation:** 

**[14180.40s] English:** or movies over there right and and of course i did an update and i broke some support of rtsp  
**Translation:** 

**[14186.80s] English:** right so i gave them another version just for them right because it was important and because  
**Translation:** 

**[14192.16s] English:** vlc is completely open source i think it is allowed on the u.s army laptops right because the  
**Translation:** 

**[14198.48s] English:** i guess someone in in the in the u.s military actually looked at it and say well okay this is  
**Translation:** 

**[14204.40s] English:** okay right and the way we document how we process that was okay right so the only way we we work  
**Translation:** 

**[14209.52s] English:** with authorities is to help them uh doing support that's amazing that's really that's amazing story  
**Translation:** 

**[14215.92s] English:** yeah we don't  
**Translation:** 

**[14216.80s] English:** see anything happening on how people use vlc and this is strong do you feel the stress of this  
**Translation:** 

**[14223.20s] English:** so first of all millions of people using it second of all the military using it maybe sometimes  
**Translation:** 

**[14229.60s] English:** pressure from governments is that does that that's a that's a small team right yeah how big is vlc  
**Translation:** 

**[14237.68s] English:** country like the core contribute how many six eight but and and everything legally is only me  
**Translation:** 

**[14246.40s] English:** everything  
**Translation:** 

**[14246.80s] English:** that is legal is only me you're not stressed about this i used to stress about that a lot  
**Translation:** 

**[14252.00s] English:** yeah but the thing is we're doing what we can for everyone for the greater good we we work  
**Translation:** 

**[14259.04s] English:** that we make some extremely complex technology easy for everyone we're a tool and every tool  
**Translation:** 

**[14265.84s] English:** is going to be used for great things and for bad things right you cannot blame a tool i think  
**Translation:** 

**[14272.24s] English:** and and this is like very important for us  
**Translation:** 

**[14275.20s] English:** um i used to be a lot in a lot of stress i'm not anymore right  
**Translation:** 

**[14281.92s] English:** you  
**Translation:** 

**[14280.00s] English:** what's the secret to your son i mean over and over in the chats i've had with you uh in the  
**Translation:** 

**[14287.96s] English:** conversation today about every even tense topic you're very zen what's the uh what's the source  
**Translation:** 

**[14292.90s] English:** of zen i have a way of um thinking about what is the worst case scenario always right and the  
**Translation:** 

**[14302.74s] English:** answer is at the end if i take like like a chess player right in the end am i dead yes or no  
**Translation:** 

**[14309.52s] English:** right and and i do that non-stop right and that's also how i do my my startups right is that i'm  
**Translation:** Vocabulary: startups: 创业项目

**[14317.22s] English:** here to get something right what is the worst case it goes bankrupt that's life a company lives a  
**Translation:** 

**[14323.26s] English:** company dies that's okay right like and so my moral way is always like am i dying in the end  
**Translation:** 

**[14329.24s] English:** am i hurting someone if i'm the answer is no then too bad right like oh some lawyers are not going  
**Translation:** 

**[14335.90s] English:** to be unhappy what are they going to do take all the money off video landings  
**Translation:** 

**[14339.52s] English:** wow they're going to have 50 grand amazing right what are they going to do is that the  
**Translation:** 

**[14344.76s] English:** cuts the source code is out there it's not stoppable also because what we do is good  
**Translation:** Vocabulary: stoppable: 可停止的

**[14350.38s] English:** and it's done for everyone that's beautiful uh karen you you said that there's an active  
**Translation:** 

**[14357.60s] English:** archiving uh preservation community i think that's super fascinating you wrote that  
**Translation:** Vocabulary: archiving: 归档

**[14362.80s] English:** they're stretching budget but they see the extreme importance of ffmpeg as a rosetta stone  
**Translation:** 

**[14369.52s] English:** media can be played a thousand years from now i mean that's a beautiful way to see ffmpeg vlc  
**Translation:** Vocabulary: rosetta: 石碑对照

**[14376.46s] English:** as a tool for preserving visual knowledge yes it's one of the coolest communities um in open  
**Translation:** 

**[14384.88s] English:** source multimedia mainly led by someone called dave rice i'll give him a shout out i think from  
**Translation:** Vocabulary: multimedia: 多种媒体

**[14389.28s] English:** um city university of new york is the archiving community they've done so much stuff that they  
**Translation:** 

**[14394.90s] English:** value that they value open source one because yes they lack budgets but two they see the  
**Translation:** 

**[14399.52s] English:** fact that  
**Translation:** 

**[14400.00s] English:** but archiving video is important for the world,  
**Translation:** 

**[14404.92s] English:** but being able to play that is a big problem.  
**Translation:** 

**[14407.96s] English:** Famously in the UK, there was something called the New Doomsday Book,  
**Translation:** Vocabulary: doomsday: 世界末日

**[14411.72s] English:** and they archived lots of stuff on BBC microcomputers.  
**Translation:** 

**[14415.18s] English:** Within 10 to 15 years, no one had the right software to play that.  
**Translation:** Vocabulary: archived: 归档; microcomputers: 微型计算机

**[14419.00s] English:** I think it was 20 years or something like that,  
**Translation:** 

**[14420.92s] English:** and someone had to go and reverse engineer this,  
**Translation:** 

**[14422.72s] English:** and that was for 20 years. Imagine that in 1,000 years.  
**Translation:** 

**[14426.40s] English:** I think one of the great things about FFmpeg is it's written in C,  
**Translation:** 

**[14429.58s] English:** and C is the closest to mathematics you're probably going to get,  
**Translation:** 

**[14433.44s] English:** the closest to logic.  
**Translation:** 

**[14434.52s] English:** Do you think in 1,000 years we'll still have C compilers?  
**Translation:** 

**[14437.12s] English:** Yes, we have languages that exist that haven't changed too much.  
**Translation:** Vocabulary: compilers: 编译器

**[14440.54s] English:** We have mathematical notation that exists.  
**Translation:** 

**[14443.90s] English:** It will be like Latin. C will be like Latin.  
**Translation:** Vocabulary: mathematical: 数学的

**[14445.54s] English:** It will be a thing that you learn from the past,  
**Translation:** 

**[14448.32s] English:** but it will still be usable in certain contexts.  
**Translation:** Vocabulary: usable: 可用的

**[14451.16s] English:** The archiving community are really great, practically.  
**Translation:** 

**[14453.90s] English:** They, again, limited funds.  
**Translation:** 

**[14455.92s] English:** They funded the development of the FFv1 codec,  
**Translation:** 

**[14458.46s] English:** so that's a lossless codec.  
**Translation:** Vocabulary: lossless: 无损的

**[14459.58s] English:** The archiving community is really scared  
**Translation:** 

**[14462.50s] English:** about the act of compression losing things.  
**Translation:** Vocabulary: compression: 压缩

**[14464.90s] English:** They have a fair point in this.  
**Translation:** 

**[14468.00s] English:** If they compress too hard, it could change the view of the material.  
**Translation:** Vocabulary: compress: 压缩

**[14473.12s] English:** There could be something slightly different here and there,  
**Translation:** 

**[14475.32s] English:** so they're really concerned about things need to be not just compressed well,  
**Translation:** Vocabulary: compressed: 压缩

**[14479.20s] English:** but lossless and be fast.  
**Translation:** 

**[14481.24s] English:** They worked with FFmpeg to develop a whole new codec  
**Translation:** 

**[14484.66s] English:** designed for fast software-based encoding.  
**Translation:** 

**[14487.64s] English:** They're really concerned about resilience  
**Translation:** Vocabulary: encoding: 编码; resilience: 韧性

**[14489.58s] English:** so if they're storing on tapes or other hard disks,  
**Translation:** 

**[14494.08s] English:** I lose some bits, I need to recover quickly,  
**Translation:** 

**[14496.12s] English:** I can't lose a whole GOP because I've lost a bit,  
**Translation:** 

**[14499.12s] English:** something like that.  
**Translation:** 

**[14501.20s] English:** So they're a really great bunch of people.  
**Translation:** 

**[14502.28s] English:** They funded GPU encoding in FFmpeg to make FFv1 encode faster.  
**Translation:** Vocabulary: encode: 编码

**[14507.00s] English:** And it's really about preserving the world's multimedia heritage  
**Translation:** 

**[14512.16s] English:** in a way that's usable.  
**Translation:** Vocabulary: multimedia: 多种媒体

**[14514.16s] English:** And there's a lot of great teams and a lot of archival groups across the world  
**Translation:** 

**[14519.50s] English:** that have chosen FFmpeg.  
**Translation:** Vocabulary: archival: 档案馆

**[14520.00s] English:** ffmpeg and ffv1 as their archiving solution and they can really provide us also super specialist  
**Translation:** 

**[14527.16s] English:** advice they can explain ah in the 1950s colorimetry was done like this on this certain type of  
**Translation:** Vocabulary: archiving: 存档; colorimetry: 色彩测量

**[14534.26s] English:** tape and so there is a this special case that you need to handle and you'll never get this  
**Translation:** 

**[14539.98s] English:** anywhere else you see they know things on video like we don't yes like every time i talk to  
**Translation:** 

**[14546.00s] English:** was it dave rice or the people from the british uh british film film it's just like every time i  
**Translation:** 

**[14551.46s] English:** just learn something new and i've been doing video for 20 years they they have especially on  
**Translation:** 

**[14556.66s] English:** colorimetry and colors storage these other things i mean they have a deep deep appreciation of the  
**Translation:** 

**[14563.56s] English:** content itself of the video itself and like especially when you're thinking lossless  
**Translation:** 

**[14568.38s] English:** they're terrified of losing something essential about the thing and in so doing they're deeply  
**Translation:** 

**[14575.24s] English:** understanding  
**Translation:** 

**[14576.00s] English:** the thing that is to be preserved which you sometimes might not be thinking about when you're  
**Translation:** 

**[14580.56s] English:** obsessing about the actual technology of the encoding and so on and when you enter the habit  
**Translation:** 

**[14585.44s] English:** hole of film scanners right so you take those those things to make to digital life it's like  
**Translation:** 

**[14592.88s] English:** a huge topic that like would take another five hours of podcast just on that film and there's  
**Translation:** Vocabulary: scanners: 扫描仪

**[14599.34s] English:** a lot of film that needs to be archived film is degrading it's maybe not stored in the right  
**Translation:** 

**[14603.08s] English:** environment the other thing is they can what they also do is  
**Translation:** Vocabulary: archived: 已归档; degrading: 退化

**[14605.90s] English:** you can you can you can you can you can you can you can you can you can you can you can  
**Translation:** 

**[14605.98s] English:** because it's open source they give this away their workflows to countries who can't afford to  
**Translation:** Vocabulary: workflows: 工作流程

**[14610.66s] English:** have archiving institutions where archiving is done by volunteers it's done by other things  
**Translation:** 

**[14615.38s] English:** they go and teach you know in india they teach children to do to do ffmpeg commands they're  
**Translation:** 

**[14620.82s] English:** really great they're really uh they're really the model community the model ethos of what we're  
**Translation:** 

**[14625.96s] English:** trying to achieve that they are such a great bunch of people so interested in participating  
**Translation:** Vocabulary: ethos: 行为准则

**[14631.84s] English:** and being part of something much bigger because they realize the work they're doing  
**Translation:** 

**[14635.98s] English:** in a thousand years is going to tell a lot you know in a thousand years  
**Translation:** 

**[14640.00s] English:** years we may be drowning in ai slop this stuff needs to be important and you know archived well  
**Translation:** 

**[14645.20s] English:** what was the what was life like yeah it feels like capturing the 20th century in the 21st century is  
**Translation:** 

**[14650.84s] English:** essential because it feels like a transition point where we went from scarcity of data to  
**Translation:** 

**[14658.50s] English:** slop oceans of slop and that transition point is good to archive people don't realize we are losing  
**Translation:** Vocabulary: scarcity: 匮乏

**[14667.12s] English:** today a ton of films there is a ton of things from the 30s from the 40s and the 50s that where  
**Translation:** 

**[14675.28s] English:** there is no value and tape 70s and 80s there's tape and there's not enough tape heads in the  
**Translation:** 

**[14681.02s] English:** world to read all the types of readers so they have to decide what they want to archive and  
**Translation:** 

**[14684.86s] English:** throw away the rest of the tapes there's huge moral hazard i guess for want of a better phrase  
**Translation:** 

**[14690.00s] English:** around this topic because this is a digital record of human history and they have to make decisions  
**Translation:** 

**[14697.12s] English:** and there's digital stewardship i suppose for one to have i made that phrase up that's not a real  
**Translation:** Vocabulary: stewardship: 数字保管

**[14701.12s] English:** phrase um to make sure the world can have this information in something that's playable by  
**Translation:** 

**[14706.88s] English:** everybody not playable on some device that doesn't exist anymore and then there's like  
**Translation:** 

**[14713.98s] English:** realistically speaking there's a needle in a haystack where there's a lot of value in  
**Translation:** 

**[14718.88s] English:** in archiving all that footage and then over time finding the gems that we don't know are there  
**Translation:** Vocabulary: archiving: 归档; haystack: haystack

**[14725.02s] English:** hey there was something in that corner  
**Translation:** 

**[14727.12s] English:** that we just did yeah and now that would have been compressed away because some little thing  
**Translation:** Vocabulary: compressed: 压缩

**[14731.60s] English:** oh wow there's something there and that's they've made sure that it's lost us they can prove  
**Translation:** 

**[14736.56s] English:** mathematically that it's lossless they can run different trade-offs for if there's bit  
**Translation:** Vocabulary: lossless: 无损的; mathematically: 数学上

**[14741.84s] English:** for they lose a bit a single bit flips i can make sure that i only lose a portion of a given frame  
**Translation:** 

**[14747.36s] English:** we can do error they can do error recovery on previous frames they could do all sorts  
**Translation:** 

**[14750.96s] English:** of different things do you think uh vlc and ffmpeg will be here 100 years from now  
**Translation:** 

**[14757.12s] English:** fmpeg yes yep we'll see  
**Translation:** 

**[14760.00s] English:** Maybe.  
**Translation:** 

**[14761.04s] English:** What's the future of, where is FFmpeg going?  
**Translation:** 

**[14765.02s] English:** Where is VLC going?  
**Translation:** 

**[14766.36s] English:** Like in the next, if you think about like five years, 10 years, 20 years.  
**Translation:** 

**[14770.54s] English:** Five years, 10 years is easy.  
**Translation:** 

**[14772.06s] English:** The question is after that, right?  
**Translation:** 

**[14775.12s] English:** The question is, do we arrive at something called holograms, right?  
**Translation:** 

**[14779.38s] English:** Yeah, so will VLC and FFmpeg expand to whatever multimedia?  
**Translation:** Vocabulary: holograms: 全息图; multimedia: 多媒体

**[14786.80s] English:** Multimedia might become, sorry for the pothead expansion of topic,  
**Translation:** 

**[14792.20s] English:** but if you look at something like Neuralink with brain-computer interfaces,  
**Translation:** Vocabulary: interfaces: 接口

**[14798.48s] English:** it's very possible that we start to consume what multimedia means  
**Translation:** 

**[14802.40s] English:** is whatever codec, whatever data that our brain wants to consume  
**Translation:** 

**[14808.40s] English:** through the brain-computer interfaces.  
**Translation:** 

**[14810.44s] English:** That's one.  
**Translation:** 

**[14811.22s] English:** And virtual reality, of course.  
**Translation:** 

**[14812.70s] English:** You will have VLC for Neuralink.  
**Translation:** 

**[14815.30s] English:** And you'll have FFmpeg-R.  
**Translation:** 

**[14816.88s] English:** Input format, human brain.  
**Translation:** 

**[14818.62s] English:** There's going to be codecs for the brain, yes.  
**Translation:** 

**[14821.20s] English:** Sure, 100%.  
**Translation:** 

**[14821.88s] English:** Of course.  
**Translation:** 

**[14823.88s] English:** I mean, today there is like, there are new codecs for, for example,  
**Translation:** 

**[14828.24s] English:** what we call point cloud, right?  
**Translation:** 

**[14830.00s] English:** Or volumetric videos, right?  
**Translation:** Vocabulary: volumetric: 体域的

**[14831.74s] English:** There is a ton of research on what we call RGBD, right?  
**Translation:** 

**[14834.84s] English:** So codecs for depth that is useful for robotics and for 3D things.  
**Translation:** 

**[14839.22s] English:** There is a ton of codecs for compression of 3D elements.  
**Translation:** 

**[14842.64s] English:** Compression for astronomy.  
**Translation:** Vocabulary: astronomy: 天文学; compression: 压缩

**[14843.90s] English:** For example, on VLC, we also have already a VR.  
**Translation:** 

**[14846.80s] English:** An XR version of VLC.  
**Translation:** 

**[14848.58s] English:** And also on Kyber, right?  
**Translation:** 

**[14850.06s] English:** We talk about Kyber.  
**Translation:** 

**[14850.92s] English:** On Kyber, we also like do streaming of XR content  
**Translation:** 

**[14853.60s] English:** for the glasses who cannot have enough power  
**Translation:** Vocabulary: cannot: 不能

**[14857.18s] English:** or inside the Apple Vision or the Quest.  
**Translation:** 

**[14859.90s] English:** So we already work on streaming 3D, XR, interactive, low latency.  
**Translation:** Vocabulary: interactive: 交互性; latency: 延迟

**[14866.90s] English:** There is something called volumetric video, point cloud videos.  
**Translation:** 

**[14870.40s] English:** So it's not stopping.  
**Translation:** 

**[14872.02s] English:** And yes, at some point, we'll manage 3D data inside VLC and FFmpeg,  
**Translation:** 

**[14876.74s] English:** right?  
**Translation:** 

**[14876.80s] English:** It's obvious.  
**Translation:** 

**[14878.04s] English:** So that's where it is moving, like the community.  
**Translation:** 

**[14880.00s] English:** it is open not everyone in the community sees that but like as kiran and i we are we are  
**Translation:** 

**[14886.22s] English:** entrepreneurs we know where it's going we see that right so i suppose that there is a tension  
**Translation:** Vocabulary: entrepreneurs: 企业家

**[14891.78s] English:** probably inside of a fan pack it's like hey listen folks we're really good at doing video and audio  
**Translation:** 

**[14899.24s] English:** so like why expand like let's do the thing we're really good at doing in order to answer that  
**Translation:** 

**[14905.92s] English:** question we need to answer the definition of what is multimedia yeah and multimedia is a digital  
**Translation:** 

**[14915.08s] English:** representation of several streams for the human senses and we will do that right so imagine there  
**Translation:** 

**[14925.72s] English:** is now a way to not have a mic but have a outdoor sensor and a diffuser of others it will get into  
**Translation:** 

**[14933.72s] English:** so you're demox  
**Translation:** Vocabulary: diffuser: 扩散器; sensor: 传感器

**[14935.08s] English:** yes  
**Translation:** 

**[14935.80s] English:** yes of course your demoxer has a new track type that is basically others right and you already  
**Translation:** 

**[14941.98s] English:** have touch it's like audio you'll have a left and right nose track you have a left and right audio  
**Translation:** 

**[14946.24s] English:** pair it's easy yes of course the stereo smell so in vlc for example we already have a plugin for  
**Translation:** Vocabulary: stereo: 立体声

**[14952.96s] English:** aptic it's mostly for what we call 4d cinemas right you know those ones on hydraulic i don't  
**Translation:** 

**[14958.96s] English:** know how you say that hydraulic arms and where everything is moving like you have uh in theme  
**Translation:** Vocabulary: hydraulic: 液压系统

**[14964.90s] English:** parks right  
**Translation:** 

**[14965.80s] English:** and there is a data feed synchronized which is basically transporting this information is there  
**Translation:** Vocabulary: synchronized: 同步; transporting: 传输

**[14972.46s] English:** yet a standard there are many standards right um you make me so happy and so of course like we have  
**Translation:** 

**[14980.74s] English:** a plug-in which is not in the normal version of vlc that is basically transporting those type of  
**Translation:** 

**[14986.08s] English:** movements which is physical movements which is haptic movements right it is a human sense so it  
**Translation:** 

**[14992.98s] English:** will get in that's such an exciting future  
**Translation:** Vocabulary: haptic: 触觉反馈

**[14995.80s] English:** was it I mean it's a small community of developers  
**Translation:** 

**[15000.00s] English:** pull that off like if you're a contributor to ffmpeg or vlc it feels stressful like it's just  
**Translation:** Vocabulary: contributor: 贡献者

**[15007.24s] English:** looking at twitter it's like it's a huge amount of work to make it work on all these different  
**Translation:** 

**[15015.26s] English:** operating systems an incredible effort no see it in the other direction we are not the contributors  
**Translation:** Vocabulary: contributors: 贡献者

**[15021.76s] English:** we are the maintainers right so we maintain for everyone meaning that for example every year  
**Translation:** 

**[15029.98s] English:** there is around 150 people who contribute to vlc and maybe 300 on ffmpeg right our goal as a small  
**Translation:** Vocabulary: maintainers: 维护者

**[15038.00s] English:** team is to get all the contribution in so if there is more usage there will be more contributions  
**Translation:** 

**[15044.94s] English:** and those people will do the right module the new formats and so on we care about the architecture  
**Translation:** Vocabulary: module: 模块

**[15051.40s] English:** of vlc the architecture of ffmpeg right now we're doing things in vlc which is a special audio right  
**Translation:** 

**[15058.26s] English:** we did the demo not not long ago  
**Translation:** 

**[15059.98s] English:** there was changes needed on the architecture and we did the first special audio module  
**Translation:** 

**[15066.76s] English:** when it's going to add the second one it's going to be easy or the third one is going to be easy  
**Translation:** 

**[15070.36s] English:** right our goal ends is going to be the same for orders or haptic right we need to work the  
**Translation:** 

**[15076.00s] English:** architecture so that's modules can be added to add future capabilities so yes we are going we  
**Translation:** 

**[15083.12s] English:** are multimedia frameworks so that's not just audio and video it's everything that is timed and  
**Translation:** 

**[15089.98s] English:** ийн фич 來  
**Translation:** Vocabulary: multimedia: 多种媒体

**[15090.62s] English:** represent  
**Translation:** 

**[15091.30s] English:** it's  
**Translation:** 

**[15092.26s] English:** what you can give your users  
**Translation:** 

**[15107.38s] English:** a  
**Translation:** 

**[15117.90s] English:** very  
**Translation:** 

**[15118.46s] English:** good  
**Translation:** 

**[15119.40s] English:** product  
**Translation:** 

**[15119.84s] English:** a  
**Translation:** 

**[15119.98s] English:** Thank you.  
**Translation:** 

**[15120.00s] English:** via brain computer interfaces or for robots with haptic by experience what happens is always the  
**Translation:** Vocabulary: haptic: 触觉反馈; interfaces: 接口

**[15127.54s] English:** same right you start it's a new topic there is like five different standards because everyone  
**Translation:** 

**[15133.00s] English:** starts to do this the hype goes down because every time the hype goes down then people start to say  
**Translation:** 

**[15138.60s] English:** well you know what we need to do a standard people because two or three companies usually not the  
**Translation:** 

**[15143.48s] English:** leader but the two or three followers do a standard and then we implement the standard and  
**Translation:** 

**[15149.16s] English:** and then it's the end of the curves it starts to be more pepper and then the leader is kind of  
**Translation:** 

**[15153.88s] English:** pressured into it because it is better to do a standard example 3d audio right yeah six or seven  
**Translation:** 

**[15159.70s] English:** years ago it was everything about 3d you go you had the cardboard on android yeah you had two  
**Translation:** 

**[15164.26s] English:** two audio formats they're all dead right and now it's coming back with actual use cases and we  
**Translation:** Vocabulary: cardboard: 纸板

**[15170.58s] English:** learn from the mistakes of the past standard so it will be the same everywhere and not try to avoid  
**Translation:** 

**[15178.02s] English:** closed  
**Translation:** 

**[15179.16s] English:** i saw somewhere you you didn't have too many nice things to say about dolby  
**Translation:** 

**[15182.86s] English:** no i don't what is uh can you educate uh me on why where they went what would they do bad  
**Translation:** Vocabulary: dolby: 杜比

**[15191.16s] English:** that made you mad it used to be an amazing company doing tons of great things with amazing engineers  
**Translation:** 

**[15200.12s] English:** they define what sound was and now it's mostly like lawyers and licensing things oh so they're  
**Translation:** 

**[15207.62s] English:** yeah they're closed  
**Translation:** 

**[15209.16s] English:** they're closing stuff off they're trying it's just like they don't innovate as much as they did and so on it's a bit like i'm sorry to say right like hp race  
**Translation:** Vocabulary: innovate: 创新

**[15216.32s] English:** oh since we talked about twitter a bunch in a bunch of different contexts do you have a do a favorite  
**Translation:** 

**[15225.06s] English:** your and least favorite most embarrassing tweet i need a video land off the fan page twitters  
**Translation:** Vocabulary: twitters: 微博

**[15232.38s] English:** the two my two favorites are talk is cheap send patches i think that that embodies a lot of the  
**Translation:** 

**[15239.16s] English:** stuff doesn't get as  
**Translation:** Vocabulary: embodies: 体现

**[15240.00s] English:** we've talked about stuff doesn't get built unless someone does it it doesn't just appear from the  
**Translation:** 

**[15244.32s] English:** ether uh the other one that i like is um ffmpeg nothing is beyond our reach i think that comes  
**Translation:** 

**[15250.96s] English:** from a u.s military satellite patch where i think they invented some kind of um monitoring system  
**Translation:** 

**[15257.12s] English:** they could see the whole world and this was released wasn't there something where ffmpeg  
**Translation:** 

**[15260.56s] English:** was running on a hover on mars yeah so ffmpeg is used by the mars rover uh the mars 2020  
**Translation:** 

**[15266.16s] English:** rover to compress uh pictures and they really wanted um they wrote a paper about it and they  
**Translation:** Vocabulary: compress: 压缩; rover: 探测车

**[15271.76s] English:** really wanted to use as much commercial off-the-shelf technology as possible  
**Translation:** 

**[15274.88s] English:** ffmpeg runs on mars so we are we are a multi-planetary open source library nice  
**Translation:** 

**[15281.60s] English:** very often we've seen tweets for people using vlt in weird places a lot of the people doing  
**Translation:** 

**[15290.88s] English:** formula ones are in all the paddocks they use vlc to play the live feed we've seen  
**Translation:** Vocabulary: paddocks: 赛车场地; tweets: 推特帖子

**[15296.16s] English:** uh the european space agency we've seen space six like monitoring the the launches with with vlc and  
**Translation:** 

**[15302.88s] English:** like this like fills you with joy right i've seen a particle accelerator oh yeah yeah we had one of  
**Translation:** Vocabulary: accelerator: 加速器; particle: 粒子

**[15309.68s] English:** the most amazing thing that i went for was to go to the cern at the lhc because they were using vlc  
**Translation:** 

**[15317.52s] English:** to monitor all the captors on the ring because the ring is 27 kilometers and so they had some analog  
**Translation:** Vocabulary: analog: 模拟; captors: 探测器

**[15326.16s] English:** cameras and they were using some of the capture cards to go to analog to vlc so vlc could stream  
**Translation:** 

**[15332.56s] English:** on their multicast network for the whole cern to access to that and like i visited that in 2010  
**Translation:** Vocabulary: multicast: 组播

**[15340.08s] English:** with laurent and and and like we fixed their issue in an hour or something like that right because  
**Translation:** 

**[15346.88s] English:** with some parameters uh maybe not well documented at that time and he said okay for the whole day  
**Translation:** 

**[15352.88s] English:** what do you want to do and we visited everything like things were  
**Translation:** 

**[15356.16s] English:** always anti-matter and and and colliders and so  
**Translation:** Vocabulary: colliders: 对撞机

**[15360.00s] English:** And that was like one of the most amazing day of my,  
**Translation:** 

**[15363.90s] English:** my physique background.  
**Translation:** Vocabulary: physique: 体格

**[15366.16s] English:** Yeah.  
**Translation:** 

**[15366.72s] English:** It's used like everywhere.  
**Translation:** 

**[15368.42s] English:** Uh,  
**Translation:** 

**[15368.92s] English:** any,  
**Translation:** 

**[15369.50s] English:** any tweets,  
**Translation:** 

**[15370.58s] English:** uh,  
**Translation:** 

**[15371.10s] English:** carrying your regret?  
**Translation:** 

**[15372.92s] English:** No tweets or regret.  
**Translation:** 

**[15374.24s] English:** Or is it like that?  
**Translation:** 

**[15375.46s] English:** Well,  
**Translation:** 

**[15375.56s] English:** how's the French song go?  
**Translation:** 

**[15377.10s] English:** Regret nothing.  
**Translation:** 

**[15379.00s] English:** Yes.  
**Translation:** 

**[15379.42s] English:** That's very important for me,  
**Translation:** 

**[15380.90s] English:** right?  
**Translation:** 

**[15381.66s] English:** Don't regret anything.  
**Translation:** 

**[15384.10s] English:** No,  
**Translation:** 

**[15384.26s] English:** it's because regrets are a tax on your mind,  
**Translation:** 

**[15387.70s] English:** right?  
**Translation:** 

**[15387.90s] English:** So learn from your mistakes,  
**Translation:** 

**[15389.48s] English:** but don't regret because you've done it.  
**Translation:** 

**[15392.90s] English:** So except if you have a time machine to go back in time,  
**Translation:** 

**[15396.60s] English:** don't regret,  
**Translation:** 

**[15398.10s] English:** right?  
**Translation:** 

**[15398.28s] English:** It's going to just tax your brain.  
**Translation:** 

**[15400.22s] English:** Learn from your mistake.  
**Translation:** 

**[15401.36s] English:** Sure.  
**Translation:** 

**[15401.70s] English:** Don't regret.  
**Translation:** 

**[15403.48s] English:** It's like,  
**Translation:** 

**[15404.12s] English:** it reminds me,  
**Translation:** 

**[15404.98s] English:** it's beautiful.  
**Translation:** 

**[15405.54s] English:** It's a tax on your brain.  
**Translation:** 

**[15406.64s] English:** It reminds me of the Johnny Depp quote I saw where he was saying,  
**Translation:** 

**[15410.70s] English:** hate,  
**Translation:** Vocabulary: johnny: 强尼·德普

**[15411.10s] English:** you know,  
**Translation:** 

**[15411.42s] English:** I don't hate.  
**Translation:** 

**[15412.66s] English:** That's hate is a very expensive emotion.  
**Translation:** 

**[15415.88s] English:** Are you comparing me to Johnny Depp?  
**Translation:** 

**[15418.06s] English:** Because that would be your first one.  
**Translation:** 

**[15419.64s] English:** Well,  
**Translation:** 

**[15420.76s] English:** gentlemen,  
**Translation:** 

**[15421.58s] English:** like I said,  
**Translation:** 

**[15422.50s] English:** I'm internally grateful for the software that the two of you and the bigger  
**Translation:** 

**[15428.24s] English:** community have been part of building with FFMPEG and VLC and everything else.  
**Translation:** Vocabulary: internally: 内心地

**[15432.68s] English:** I'm eternally grateful for the spicy tweets.  
**Translation:** 

**[15436.00s] English:** Never stop.  
**Translation:** Vocabulary: eternally: 永恒地

**[15437.42s] English:** And I'm grateful that you would talk with me today and give me this sexy hat.  
**Translation:** 

**[15444.40s] English:** I feel like a wizard.  
**Translation:** 

**[15445.98s] English:** I feel special.  
**Translation:** 

**[15448.16s] English:** And I feel special.  
**Translation:** 

**[15449.22s] English:** I get a chance to talk and celebrate the piece of software that brought me so much joy over the years.  
**Translation:** 

**[15453.40s] English:** So thank you for everything.  
**Translation:** 

**[15454.86s] English:** And thank you for talking today.  
**Translation:** 

**[15456.22s] English:** Thank you for having me.  
**Translation:** 

**[15456.88s] English:** Thank you so much.  
**Translation:** 

**[15458.38s] English:** Thanks for listening to this conversation with John Baptiste Kempf and Kieran Cunha.  
**Translation:** 

**[15463.12s] English:** To support this podcast,  
**Translation:** 

**[15464.20s] English:** please check out our sponsors in the description where you can also find links to contact me,  
**Translation:** Vocabulary: sponsors: 赞助商

**[15469.00s] English:** ask questions,  
**Translation:** 

**[15469.98s] English:** give feedback and so on.  
**Translation:** 

**[15471.68s] English:** And now let me leave you with some words from the legendary Linus Torvalds.  
**Translation:** 

**[15477.20s] English:** Most good programmers do programs.  
**Translation:** Vocabulary: programmers: 程序员

**[15479.22s] English:** Okay, me.  
**Translation:** 

**[15480.00s] English:** not because they expect to get paid or get adulation by the public,  
**Translation:** Vocabulary: adulation: 赞美

**[15484.86s] English:** but because it is fun to program.  
**Translation:** 

**[15488.40s] English:** Thank you for listening, and I hope to see you next time.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
