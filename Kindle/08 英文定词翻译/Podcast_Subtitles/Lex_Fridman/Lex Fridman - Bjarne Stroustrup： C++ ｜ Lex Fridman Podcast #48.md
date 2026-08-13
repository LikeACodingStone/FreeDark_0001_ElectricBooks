# Podcast vocabulary notes
Source file: Lex Fridman - Bjarne Stroustrup： C++ ｜ Lex Fridman Podcast #48.opus
Improved subtitle: punctuation and vocabulary regenerated from current config.

**[0.00s] English:** The following is a conversation with Bjørn Strølstrøm.  
**Translation:** 

**[3.24s] English:** He is the creator of C++, a programming language that, after 40 years,  
**Translation:** 

**[8.00s] English:** Is still one of the most popular and powerful languages in the world.  
**Translation:** 

**[12.52s] English:** Its focus on fast, stable, robust code underlies many of the biggest systems in the world.  
**Translation:** Vocabulary: robust: 强壮的

**[17.90s] English:** That we have come to rely on as a society.  
**Translation:** 

**[20.84s] English:** If you're watching this on YouTube, for example:  
**Translation:** 

**[23.24s] English:** Many of the critical backend components of YouTube are written in C++.  
**Translation:** 

**[27.16s] English:** The same goes for Google, Facebook, Amazon, Twitter, and most Microsoft applications.  
**Translation:** Vocabulary: backend: 后端

**[33.06s] English:** Adobe applications, most database systems, and most physical systems that operate in the real world,  
**Translation:** 

**[39.40s] English:** Like cars, robots, rockets that launch us into space, and one day will land us on Mars.  
**Translation:** Vocabulary: rockets: 火箭

**[46.62s] English:** C++ also happens to be the language that I use more than any other in my life.  
**Translation:** 

**[52.70s] English:** I've written several hundred thousand lines of C++ source code.  
**Translation:** 

**[56.26s] English:** Of course.  
**Translation:** 

**[57.58s] English:** Lines of source code don't mean much,  
**Translation:** 

**[59.54s] English:** But they do give hints of my personal journey through the world of software.  
**Translation:** 

**[64.44s] English:** I've enjoyed watching the development of C++ as a programming language.  
**Translation:** 

**[68.38s] English:** Leading up to the big update in a standard in 2011,  
**Translation:** 

**[72.50s] English:** And those that followed in 2014, 2017,  
**Translation:** 

**[75.48s] English:** And toward the new C++20 standard, hopefully coming out next year.  
**Translation:** 

**[80.84s] English:** This is the Artificial Intelligence Podcast.  
**Translation:** 

**[83.62s] English:** If you enjoy it, subscribe on YouTube,  
**Translation:** 

**[86.36s] English:** Give it five stars.  
**Translation:** Vocabulary: subscribe: 订阅

**[87.16s] English:** And iTunes,  
**Translation:** 

**[88.00s] English:** Support it on Patreon,  
**Translation:** Vocabulary: patreon: 支持者

**[89.34s] English:** Or simply connect with me on Twitter at @LexFriedman.  
**Translation:** 

**[92.54s] English:** Spelled F-R-I-D-M-A-N.  
**Translation:** 

**[95.02s] English:** And now, here's my conversation with Bjørn Stroustrup.  
**Translation:** 

**[99.90s] English:** What was the first program you've ever written?  
**Translation:** 

**[103.54s] English:** Do you remember?  
**Translation:** 

**[104.86s] English:** It was my second year in university.  
**Translation:** 

**[107.78s] English:** First year of computer science,  
**Translation:** 

**[110.44s] English:** And it was an Alco-60.  
**Translation:** 

**[112.52s] English:** I calculated the shape of a super,  
**Translation:** 

**[117.16s] English:** And then, connect the points.  
**Translation:** 

**[119.60s] English:** So,  
**Translation:** 

**[120.00s] English:** The ones on the perimeter creating star patterns were done with wet ink on paper using a printer.  
**Translation:** Vocabulary: perimeter: 边界

**[131.52s] English:** And that was in college or university; yes, yes, I learned to program my second year in university.  
**Translation:** 

**[138.32s] English:** And what was the first programming language, if I may ask, that you fell in love with?  
**Translation:** 

**[144.96s] English:** I think I'll call 60, and after that, I remember.  
**Translation:** 

**[154.16s] English:** I remember Snowball, but I didn't fall in love with Fortran. I remember Pascal.  
**Translation:** Vocabulary: pascal: 计算机语言; snowball: 猪名

**[161.20s] English:** Didn't fall in luck with that; it all got in the way of me, and then I discovered assembly.  
**Translation:** 

**[167.92s] English:** And that was much more fun, and from there I went to microcode.  
**Translation:** Vocabulary: microcode: 微代码

**[174.96s] English:** You were drawn to the low-level stuff, finding it beautiful. I, on the other hand, went...  
**Translation:** 

**[182.24s] English:** Through a lot of languages, and then I spent significant time in assembler and microcode.  
**Translation:** Vocabulary: assembler: 汇编语言

**[189.44s] English:** That was sort of the first really profitable thing, and I paid for my master's actually.  
**Translation:** 

**[195.36s] English:** And then I discovered Simula, which was absolutely great. Simula was the extension of ELBOL 60.  
**Translation:** 

**[205.36s] English:** Uh, done primarily for simulation, but basically, they invented object-oriented programming and  
**Translation:** 

**[211.28s] English:** Inheritance and runtime polymorphism when they were doing it.  
**Translation:** Vocabulary: inheritance: 继承; polymorphism: 多态; runtime: 运行时

**[217.52s] English:** And that was the language that taught me that you could have the sorts of problems of  
**Translation:** 

**[226.40s] English:** A program grows with the size of the program, rather than with the square of the size of the program.  
**Translation:** 

**[233.36s] English:** That is, you can actually monitor  
**Translation:** 

**[234.96s] English:** Arise very nicely.  
**Translation:** Vocabulary: nicely: 良好地

**[236.20s] English:** And that  
**Translation:** 

**[238.28s] English:** It was a surprise.  
**Translation:** 

**[240.00s] English:** It was also a surprise to me that a stricter type system than Pascal's was helpful, whereas  
**Translation:** 

**[248.80s] English:** Pascal's type system got in my way all the time, so you need a strong type system to organize your code.  
**Translation:** 

**[257.76s] English:** Code well, but it has to be extensible and flexible. Let's get into the details a little bit: what kind?  
**Translation:** 

**[263.68s] English:** If you remember, what kind of type system did Pascal have? What type system was it?  
**Translation:** Vocabulary: extensible: 可扩展的; flexible: 灵活的; pascal: 帕斯卡

**[268.88s] English:** Did the Alcohol 60 have basically Pascal, which was sort of the simplest language that Nicholas Viet could?  
**Translation:** 

**[277.76s] English:** Define that served Nicholas Viet's needs at the time, and it has a sort of highly moral tone.  
**Translation:** 

**[287.68s] English:** To it, that is, if you can say it in Pascal, it's good; and if you can't, it's not so good, whereas  
**Translation:** 

**[297.44s] English:** Similar  
**Translation:** 

**[299.28s] English:** Allowed you basically to build your own type system.  
**Translation:** 

**[302.88s] English:** So, instead of trying to fit yourself into Nicholas Velt's world, Christian Newgau's language,  
**Translation:** 

**[312.16s] English:** Olivia's language allowed you to build your own, so it's sort of close to the original idea.  
**Translation:** 

**[320.24s] English:** Of, of you build a domain-specific language, as a matter of fact, what you build is a set of types.  
**Translation:** 

**[328.88s] English:** And relations among types that allow you to express something that is suitable for an application.  
**Translation:** 

**[336.16s] English:** So, when you say "types" the stuff, you're saying has echoes of object-oriented programming.  
**Translation:** Vocabulary: echoes: 回声

**[342.16s] English:** Yes, they invented it. Every language that uses the word "class" for "type" is a descendant of similar.  
**Translation:** 

**[352.00s] English:** Directly or indirectly, Christian Newgau and Ole Johann Dal were mathematicians.  
**Translation:** Vocabulary: descendant: 后代; mathematicians: 数学家

**[358.88s] English:** Um, and  
**Translation:** 

**[360.00s] English:** And they didn't think in terms of types, but they understood sets and classes of elements.  
**Translation:** 

**[368.64s] English:** And so they called their types "classes.  
**Translation:** 

**[371.74s] English:** And basically, in C++ (as in Simula), classes are user-defined types.  
**Translation:** Vocabulary: simula: 早期面向对象编程语言

**[378.76s] English:** So, can you try the impossible task and give a brief history of programming languages from?  
**Translation:** 

**[385.28s] English:** Your perspective?  
**Translation:** 

**[386.40s] English:** So we started with ALGOL 60, Simula, and Pascal, but that's just the 1960s and 1970s.  
**Translation:** 

**[394.06s] English:** I can try.  
**Translation:** Vocabulary: pascal: 帕斯卡

**[396.72s] English:** The most interesting and major improvement in programming languages was Fortran, the  
**Translation:** 

**[404.38s] English:** First, Fortran.  
**Translation:** 

**[406.08s] English:** Because before that, all code was written for a specific machine, and each specific  
**Translation:** 

**[411.26s] English:** The machine had a language.  
**Translation:** 

**[413.52s] English:** A simple language, or...  
**Translation:** 

**[416.38s] English:** A macro-assembler, or some extension of that idea.  
**Translation:** 

**[420.26s] English:** But you are writing for a specific machine in the language of that machine.  
**Translation:** 

**[427.60s] English:** And Barkas and his team at IBM built a language that would allow you to write what you really meant.  
**Translation:** 

**[437.44s] English:** Wanted.  
**Translation:** 

**[438.44s] English:** That is, you could write it in a language that was natural for people.  
**Translation:** 

**[443.46s] English:** Now, these people happened to be engineers and physicists.  
**Translation:** 

**[446.04s] English:** So, the language that came out was somewhat unusual for the rest of the world.  
**Translation:** Vocabulary: physicists: 物理学家

**[450.80s] English:** But basically, they said "formula translation" because they wanted to have the mathematical  
**Translation:** 

**[455.10s] English:** Formulas translated into the machine.  
**Translation:** Vocabulary: formulas: 公式; mathematical: 数学的

**[458.86s] English:** And as a side effect, they got portability.  
**Translation:** 

**[463.62s] English:** Because now they are writing in the terms that humans used and the way humans think.  
**Translation:** Vocabulary: portability: 便携性

**[470.94s] English:** And then they had a program that translated it into the machine's needs.  
**Translation:** 

**[475.90s] English:** And that was new, and that was great.  
**Translation:** 

**[478.78s] English:** And it's something that...  
**Translation:** 

**[480.00s] English:** To remember: We want to raise the language to the human level, but we don't want to lose the  
**Translation:** 

**[487.32s] English:** Efficiency. And that was the first step toward the human. That was the first step. And of course,  
**Translation:** 

**[495.38s] English:** They were a very particular kind of humans. Business people were different, so they got  
**Translation:** 

**[500.42s] English:** COBOL, and so on, and so forth. And then Simula came out. No, let's not go to Simula just yet. Let's  
**Translation:** 

**[508.56s] English:** Go to Algor. Fortran didn't have, at the time, a precise notion of type.  
**Translation:** Vocabulary: algor: 算法; simula: Simula编程语言

**[518.80s] English:** Not a precise notion of scope, not a set of translation phases—that's what we have today.  
**Translation:** 

**[529.58s] English:** Lexical, syntax, semantics. It was sort of a bit of a model in the early days, but...  
**Translation:** Vocabulary: lexical: 词汇; semantics: 语义; syntax: 句法

**[536.30s] English:** Hey, they had just done the big  
**Translation:** 

**[537.96s] English:** Breakthrough in the history of programming, right? So you can't criticize them for not.  
**Translation:** 

**[543.70s] English:** Having gotten all the technical details right, so we got AlgoR. That was very pretty, and  
**Translation:** 

**[550.16s] English:** Most people in commerce and science considered it useless because it was not flexible enough.  
**Translation:** Vocabulary: flexible: 不灵活

**[557.72s] English:** And it wasn't efficient enough, and et cetera, et cetera. But that was a breakthrough from a  
**Translation:** 

**[564.58s] English:** From a technical point of view, then Simula,  
**Translation:** 

**[567.96s] English:** Simula came along to make that idea more flexible, and you could define your own types. And that's why it was such a significant step in programming language design.  
**Translation:** 

**[575.90s] English:** Where I got very interested was in Christian Nygaard, who is the main idea man behind Simula.  
**Translation:** Vocabulary: nygaard: 尼雅格

**[584.04s] English:** That was the late 1960s.  
**Translation:** 

**[585.24s] English:** This was the late 1960s. Well, I was a visiting professor in Aarhus, and so I learned object-oriented.  
**Translation:** Vocabulary: aarhus: 丹麦城市

**[592.42s] English:** Programming by sitting around, and, well, in theory,  
**Translation:** 

**[597.96s] English:** Discussing with everyone...  
**Translation:** 

**[600.00s] English:** With Christen, but Christen: once you get started and are in full flow, it's  
**Translation:** 

**[607.84s] English:** Very hard to get a word in edgeways when you're just listening, so it was great I.  
**Translation:** Vocabulary: christen: 命名

**[613.00s] English:** Learned it from there not to romanticize the notion, but it seems like a big leap.  
**Translation:** 

**[617.56s] English:** To think about or object-oriented programming, what it's really a leap of.  
**Translation:** 

**[622.96s] English:** Abstraction: It's, yes, and was that as big and beautiful of a leap as it seems.  
**Translation:** 

**[632.20s] English:** From now on, in retrospect, I was obviously in the wrong at the time; it was not.  
**Translation:** Vocabulary: abstraction: 抽象; retrospect: 回顾

**[639.58s] English:** Obvious, and many people have tried to do something like that, but most people  
**Translation:** 

**[645.40s] English:** Didn't come up with something as wonderful as similar lots of people got.  
**Translation:** 

**[651.34s] English:** Their PhDs and made their careers in the field of computer science, and they  
**Translation:** 

**[652.94s] English:** Career is out of forgetting about something similar, or never knowing it for me.  
**Translation:** 

**[659.18s] English:** The key idea was basically that I could get my own types, and that's the idea that goes.  
**Translation:** 

**[665.90s] English:** Further into C++, where I can get better types, more flexible types, and more.  
**Translation:** Vocabulary: flexible: 灵活的

**[672.26s] English:** Efficient types, but it's still the fundamental idea when I want to write a  
**Translation:** 

**[676.22s] English:** Program: I want to write it with my types that are appropriate to my problem and  
**Translation:** 

**[682.64s] English:** You know, it's it's it's it's it's it's it's it's it's it's it's it's  
**Translation:** 

**[682.76s] English:** It's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's.  
**Translation:** 

**[682.92s] English:** It's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's.  
**Translation:** 

**[682.98s] English:** It's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's.  
**Translation:** 

**[683.08s] English:** It's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's.  
**Translation:** 

**[683.10s] English:** It's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's.  
**Translation:** 

**[683.12s] English:** It's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's.  
**Translation:** 

**[683.42s] English:** The constraints that I'm under with hardware, software, environment, etc.  
**Translation:** Vocabulary: constraints: 限制条件

**[689.68s] English:** And that's the key idea.  
**Translation:** 

**[692.76s] English:** People picked up on the class hierarchies, the virtual functions, and the inheritance.  
**Translation:** Vocabulary: hierarchies: 等级体系; inheritance: 继承机制

**[699.68s] English:** And that was only part of it.  
**Translation:** 

**[703.96s] English:** It was an interesting and major part, and still is a major part, in a lot of graphic stuff, but  
**Translation:** 

**[710.60s] English:** It was not the most fundamental.  
**Translation:** 

**[712.48s] English:** It was when you wanted to relate one type to another.  
**Translation:** 

**[718.00s] English:** You don't want them all to be independent.  
**Translation:** 

**[720.00s] English:** The classical example is that you don't actually want to write a city simulation with vehicles where you say, "Well, if it's a bicycle, write the code for turning a bicycle to the left.  
**Translation:** 

**[735.86s] English:** If it's a normal car, turn right the normal car way. If it's a fire engine, turn right the fire engine way. You get these big case statements and bunches of if statements, and such.  
**Translation:** 

**[748.14s] English:** Instead, you tell the base class that that's the vehicle and say, "turn left" the way you want to. And this is actually a real example: they used it to simulate and optimize emergency services for somewhere in Norway back in the 60s.  
**Translation:** Vocabulary: bunches: 成堆; optimize: 优化; simulate: 模拟

**[774.68s] English:** Wow.  
**Translation:** 

**[775.36s] English:** So, this was one of the early examples.  
**Translation:** 

**[778.14s] English:** For why you needed inheritance and you needed runtime polymorphism. Because you wanted to handle this set of vehicles in a manageable way. You can't just rewrite your code each time a new kind of vehicle comes along.  
**Translation:** 

**[799.56s] English:** Yeah, that's a beautiful, powerful idea. And of course, it stretches through your work, UC++, as we'll talk about.  
**Translation:** 

**[807.44s] English:** But.  
**Translation:** 

**[808.14s] English:** I think you've structured it nicely. What other breakthroughs came along in the history of programming languages? If we were to tell the history that way.  
**Translation:** Vocabulary: breakthroughs: 重大进展; nicely: 很好

**[819.48s] English:** Obviously, I'm better at telling the part of the history that is the path I'm on, as opposed to all the other paths.  
**Translation:** 

**[826.70s] English:** Yeah, you skipped the hippie John McCarthy and Lisp—one of my favorite languages.  
**Translation:** Vocabulary: hippie: 嬉皮士; skipped: 跳过

**[832.02s] English:** But Lisp is not one of my favorite languages.  
**Translation:** 

**[836.48s] English:** It's obviously important.  
**Translation:** 

**[838.14s] English:** It's obviously interesting.  
**Translation:** 

**[840.00s] English:** Of people write code in it, and then they rewrite it into C or C++ when they want to go to production.  
**Translation:** Vocabulary: rewrite: 重写代码

**[847.36s] English:** It's in the world I'm at, which are constrained by performance and reliability.  
**Translation:** 

**[857.60s] English:** Issues, deployability, cost of hardware. I don't like things to be too dynamic.  
**Translation:** Vocabulary: constrained: 受限; deployability: 部署性; reliability: 可靠性

**[865.52s] English:** It is really hard to write a piece of code that's perfectly flexible, that you can also deploy.  
**Translation:** 

**[873.92s] English:** On a small computer, and that you can also put in, say, a telephone switch in Bogota. What's the  
**Translation:** Vocabulary: bogota: 波哥大; deploy: 部署; flexible: 灵活

**[881.42s] English:** Chance, if you get an error and find yourself in the debugger, that the telephone switch might be in...  
**Translation:** 

**[887.12s] English:** Bogota, on a late Sunday night, has a programmer around? The chance is zero. And so, a lot of  
**Translation:** 

**[894.92s] English:** Things I think are going to happen. I think it's going to happen. I think it's going to happen.  
**Translation:** 

**[895.50s] English:** I think most people can't afford that flexibility. I'm quite aware that maybe 70-80% of all code  
**Translation:** Vocabulary: flexibility: 灵活性

**[908.60s] English:** Are not under the kind of constraints I'm interested in. But somebody has to do the job.  
**Translation:** 

**[915.78s] English:** I'm doing it because you have to get from these high-level, flexible languages to the hardware.  
**Translation:** Vocabulary: constraints: 限制

**[922.36s] English:** The stuff that lasts for 10, 20,...  
**Translation:** 

**[925.50s] English:** Thirty years is robust and operates under very constrained conditions. Yes, absolutely.  
**Translation:** Vocabulary: robust: 强壮的

**[930.80s] English:** That's right.  
**Translation:** 

**[931.36s] English:** And it's fascinating and beautiful in its own way. C++ is one of my favorite languages.  
**Translation:** 

**[938.28s] English:** And so is Lisp. So, I can embody it too for different reasons as a programmer.  
**Translation:** 

**[947.16s] English:** I understand why Lisp is popular, and I can see the beauty of the ideas. And similarly with other programming languages.  
**Translation:** Vocabulary: embody: 体现; programmer: 程序员

**[954.48s] English:** The small talk is just not as relevant.  
**Translation:** 

**[960.00s] English:** It is not as relevant in my world.  
**Translation:** 

**[965.42s] English:** And by the way, I distinguish between those and the functional languages, where I go to  
**Translation:** 

**[970.34s] English:** Things like ML and Haskell, different kinds of languages.  
**Translation:** Vocabulary: functional: 函数式的; haskell: 哈斯克尔语言

**[976.76s] English:** They have a different kind of beauty, and they're very interesting.  
**Translation:** 

**[980.38s] English:** And I actually try to learn from all the languages I encounter to see what is there that would be useful or interesting.  
**Translation:** Vocabulary: encounter: 遇见

**[988.28s] English:** Make working on the kind of problems I'm interested in, with the kind of constraints.  
**Translation:** 

**[997.20s] English:** That interests me, what can actually be done better, because we can surely do better.  
**Translation:** Vocabulary: constraints: 限制条件

**[1002.94s] English:** Than we do today.  
**Translation:** 

**[1006.92s] English:** You've said that it's good for any professional programmer to know at least five languages.  
**Translation:** 

**[1011.78s] English:** Speaking about a variety of languages that you've taken inspiration from.  
**Translation:** 

**[1017.72s] English:** And you've listed...  
**Translation:** 

**[1018.28s] English:** Yours, as being at least at the time, C++, obviously, Java, Python, Ruby, and JavaScript.  
**Translation:** 

**[1028.62s] English:** Can you, first of all, update that list and modify it?  
**Translation:** 

**[1032.46s] English:** You don't have to be constrained to just five, but can you describe what you picked up as well?  
**Translation:** 

**[1038.90s] English:** From each of these languages, how do you see them as inspirations when you're working?  
**Translation:** Vocabulary: constrained: 限制

**[1044.76s] English:** With C++?  
**Translation:** 

**[1045.76s] English:** This is a very hard question.  
**Translation:** 

**[1048.26s] English:** It's a very difficult question to answer.  
**Translation:** 

**[1050.38s] English:** So, about languages, you should know them.  
**Translation:** 

**[1056.30s] English:** I reckon I knew about 25 or so when I did C++.  
**Translation:** 

**[1061.30s] English:** It was easier in those days because the languages were smaller, and you didn't have to learn  
**Translation:** Vocabulary: reckon: 估计

**[1067.06s] English:** A whole programming environment and such to do it.  
**Translation:** 

**[1070.64s] English:** You could learn the language quite easily.  
**Translation:** 

**[1073.30s] English:** And it's good to learn so many languages.  
**Translation:** 

**[1075.60s] English:** I imagine, just like...  
**Translation:** 

**[1076.60s] English:** Yeah.  
**Translation:** 

**[1077.60s] English:** Yeah.  
**Translation:** 

**[1078.60s] English:** Yeah.  
**Translation:** 

**[1079.60s] English:** Just like with...  
**Translation:** 

**[1080.00s] English:** Natural language for communication, there are different paradigms that emerge; in all of them,  
**Translation:** 

**[1085.42s] English:** Yeah, there are commonalities, and so on. So I picked five out of a hat; you pick five out.  
**Translation:** Vocabulary: paradigms: 范式

**[1092.36s] English:** Of a hat, obviously, the important thing is that the number isn't one that's right; it's like I  
**Translation:** 

**[1099.90s] English:** Don't like; I mean, if you're monolingual, you are likely to think that your own culture is the  
**Translation:** Vocabulary: monolingual: 使用一种语言的

**[1105.34s] English:** Only one person's period, for everybody else's, it's a good learning experience for a foreign language and a foreign  
**Translation:** 

**[1110.54s] English:** Culture is important; it helps you think and be a better person. With programming languages, you  
**Translation:** 

**[1116.98s] English:** Become a better programmer, better designer with the second language now. Once you've got two,  
**Translation:** 

**[1123.90s] English:** The weight of five isn't that long; it's the second one that's most important, and then when I had to  
**Translation:** Vocabulary: programmer: 程序员

**[1132.06s] English:** Pick five, um, I  
**Translation:** 

**[1134.36s] English:** I.  
**Translation:** 

**[1135.34s] English:** Sort of thinking, what kinds of languages are there? Well, there's really low-level stuff, it's  
**Translation:** 

**[1141.86s] English:** Good; it's actually good to know machine code, even still, sorry, even today, um.  
**Translation:** 

**[1148.80s] English:** The C++ optimizers write better machine code than I do, yes, but I don't think I could appreciate them.  
**Translation:** 

**[1157.26s] English:** If I actually didn't understand machine code and machine architecture at least in my position,  
**Translation:** Vocabulary: optimizers: 优化器

**[1164.18s] English:** I have to understand it.  
**Translation:** 

**[1165.34s] English:** A bit of it, because you mess up the cache and you're off in performance by a factor of a hundred.  
**Translation:** Vocabulary: cache: 缓存

**[1172.40s] English:** Right; it shouldn't be that if you are interested in either performance or the size of the computer.  
**Translation:** 

**[1179.58s] English:** You have to deploy, so I would go with something simpler these days, as I used to mention C, but now I prefer going lower-level.  
**Translation:** Vocabulary: deploy: 部署

**[1189.76s] English:** Is not actually what gives you the performance; it is to express your ideas.  
**Translation:** 

**[1195.34s] English:** So cleanly that you can think about it, and the optimizer can understand what you're  
**Translation:** Vocabulary: optimizer: 优化器

**[1200.00s] English:** Up to now, my favorite way of optimizing these days is to throw out the clever bits and see.  
**Translation:** 

**[1207.20s] English:** If it still runs fast, and sometimes it runs even faster, so I need the abstraction mechanisms.  
**Translation:** Vocabulary: abstraction: 抽象机制; optimizing: 优化

**[1214.58s] English:** Or something like C++ to write compact, high-performance code. There was a beautiful  
**Translation:** 

**[1221.50s] English:** Keynote by Jason Turner at the CPPCon a couple of years ago, where he decided he was going to.  
**Translation:** Vocabulary: compact: 紧凑; keynote: 主题演讲

**[1227.96s] English:** Program Pong on Motorola 6800, I think it was. And he says, "Well, this is relevant because it...  
**Translation:** 

**[1240.38s] English:** It looks like a microcontroller. It has specialized hardware. It doesn't have very much memory, and it's  
**Translation:** Vocabulary: microcontroller: 微控制器; motorola: 摩托罗拉

**[1246.52s] English:** Relatively slow. And so he shows, in real time, how he writes Pong, starting with fairly straightforward,  
**Translation:** 

**[1255.98s] English:** Low-level stuff, improving.  
**Translation:** Vocabulary: straightforward: 简单明了

**[1257.96s] English:** It's abstractions. And what he's doing is writing C++, and it translates into  
**Translation:** 

**[1264.66s] English:** 86. Assembler, which you can do with Clang, and you can see it in real time. It's  
**Translation:** Vocabulary: abstractions: 抽象; assembler: 汇编; translates: 翻译

**[1273.70s] English:** The Compiler Explorer, which you can use on the web, and then he wrote a little program.  
**Translation:** 

**[1279.40s] English:** That translated 86 Assembler into Motorola Assembler. And so he types, and you can see.  
**Translation:** Vocabulary: explorer: 浏览器

**[1287.68s] English:** This.  
**Translation:** 

**[1287.96s] English:** In real time, wow.  
**Translation:** 

**[1289.30s] English:** You can see it in real time. And even if you can't read the assembly code, you can just see it. He's  
**Translation:** 

**[1295.24s] English:** Code gets better. The assembler gets smaller. He increases the abstraction level and uses C++11.  
**Translation:** Vocabulary: abstraction: 抽象

**[1304.56s] English:** As it were, it's better. This code gets cleaner. It gets easier to maintain. The code shrinks,  
**Translation:** 

**[1310.34s] English:** And it keeps shrinking. And I could not, in any reasonable amount of time,  
**Translation:** Vocabulary: shrinking: 变小; shrinks: 变小

**[1317.96s] English:** Write that Assembler.  
**Translation:** 

**[1320.00s] English:** As good as the compiler-generated code from really quite nice modern C++.  
**Translation:** 

**[1326.56s] English:** And I'll go as far as to say that the thing that looked like a C  
**Translation:** 

**[1330.64s] English:** It was significantly uglier and larger when it became machine code.  
**Translation:** 

**[1342.24s] English:** So, the abstractions that can be optimized are important.  
**Translation:** 

**[1346.64s] English:** I would love to see that kind of visualization in larger codebases.  
**Translation:** Vocabulary: abstractions: 抽象; codebases: 代码库; optimized: 优化; visualization: 可视化

**[1350.88s] English:** Yeah.  
**Translation:** 

**[1351.20s] English:** That might be beautiful.  
**Translation:** 

**[1352.08s] English:** But, you can't show a larger codebase in a one-hour talk and have it fit on screen.  
**Translation:** 

**[1358.08s] English:** Right. So that's C and C++.  
**Translation:** Vocabulary: codebase: 代码库

**[1360.24s] English:** So, my two languages would be machine code and C++.  
**Translation:** 

**[1363.68s] English:** Right.  
**Translation:** 

**[1364.48s] English:** And then I think you can learn a lot from functional languages, so  
**Translation:** 

**[1370.64s] English:** PIC, Haskell, or ML. I don't care which. I think actually you learn the same lessons.  
**Translation:** Vocabulary: functional: 函数式的; haskell: 哈斯克尔语言

**[1377.20s] English:** Of expressing, especially mathematical notions, really clearly and having a type system that's  
**Translation:** 

**[1386.40s] English:** Really strict. And then you should probably have a language for sort of quickly churning out.  
**Translation:** Vocabulary: churning: 快速生成; mathematical: 数学的; notions: 概念

**[1394.00s] English:** Something. You could pick JavaScript, you could pick Python, you could pick Ruby.  
**Translation:** 

**[1400.24s] English:** What do you make of JavaScript, in general? So, you're talking in the Platonic sense of...  
**Translation:** Vocabulary: platonic: 纯粹的

**[1406.64s] English:** About languages, what they're good at, and their philosophy of design,  
**Translation:** 

**[1411.76s] English:** But there's also a large user base behind each of these languages, and they use it in the way  
**Translation:** 

**[1416.80s] English:** Sometimes, maybe it wasn't really designed for.  
**Translation:** 

**[1419.52s] English:** That's right.  
**Translation:** 

**[1420.16s] English:** JavaScript is used way beyond what it was probably designed for.  
**Translation:** 

**[1424.24s] English:** Let me say it this way: when you build a tool, you do not know how it's going to be used; you try  
**Translation:** 

**[1430.16s] English:** Improve the tool by looking at how it's being used, and when people cut their fingers, try and  
**Translation:** 

**[1436.00s] English:** Stop that.  
**Translation:** 

**[1436.50s] English:** Yeah. I think that's a great point. I think that's a great point. I think that's a great point.  
**Translation:** 

**[1436.64s] English:** I think that's a great point. From happening, but really, you have no control.  
**Translation:** 

**[1440.00s] English:** Control over how something is used.  
**Translation:** 

**[1442.68s] English:** So, I'm very happy and proud of some of the things C++ is being used for, and some of the  
**Translation:** 

**[1447.86s] English:** Things I wish people wouldn't do: Bitcoin mining, being my favorite example, uses as  
**Translation:** 

**[1454.36s] English:** Much like Switzerland, it consumes a similar amount of energy and mostly serves criminals.  
**Translation:** Vocabulary: consumes: 消耗; criminals: 罪犯

**[1461.42s] English:** But back to the languages, I actually think that having JavaScript run in the browser:  
**Translation:** 

**[1468.84s] English:** It was an enabling thing for a lot of things.  
**Translation:** Vocabulary: browser: 浏览器

**[1472.84s] English:** Yes, you could have done it better, but people were trying to do it better and they were.  
**Translation:** 

**[1477.00s] English:** Using sort-of more principled language design approaches, but they just couldn't get it right.  
**Translation:** Vocabulary: approaches: 方法; principled: 基于原则的

**[1485.14s] English:** And the non-professional programmers who write lots of that code just couldn't understand.  
**Translation:** 

**[1491.98s] English:** Them.  
**Translation:** Vocabulary: programmers: 程序员

**[1492.98s] English:** So, it did an amazing job for what it was.  
**Translation:** 

**[1498.82s] English:** It's not the prettiest language, and I don't think it ever will be the prettiest language.  
**Translation:** 

**[1504.18s] English:** But let's not be bigots here.  
**Translation:** 

**[1507.90s] English:** So, what was the origin story of C++?  
**Translation:** Vocabulary: bigots: 狭隘者

**[1512.66s] English:** You basically gave a few perspectives on your inspiration for object-oriented programming.  
**Translation:** 

**[1521.82s] English:** You had a connection with C, and performance efficiency was an important thing you were.  
**Translation:** Vocabulary: perspectives: 观点

**[1526.82s] English:** Drawn to.  
**Translation:** 

**[1528.82s] English:** Efficiency and reliability.  
**Translation:** 

**[1529.82s] English:** Reliability.  
**Translation:** 

**[1530.82s] English:** You have to get both.  
**Translation:** Vocabulary: reliability: 可靠性

**[1533.20s] English:** What's reliability?  
**Translation:** 

**[1534.84s] English:** I really want my telephone calls to get through, and I want the quality of what I am talking about to be good.  
**Translation:** 

**[1542.38s] English:** Coming out at the other end.  
**Translation:** 

**[1544.94s] English:** The other end might be in London, or wherever.  
**Translation:** 

**[1551.14s] English:** And you don't want the system to crash.  
**Translation:** 

**[1553.26s] English:** If you're doing a bank, you mustn't crash.  
**Translation:** 

**[1557.00s] English:** It might be yours....  
**Translation:** 

**[1558.30s] English:** Yeah.  
**Translation:** 

**[1558.82s] English:** It might be your bank.  
**Translation:** 

**[1560.00s] English:** An account that is in trouble has different constraints, like in games; it doesn't matter.  
**Translation:** Vocabulary: constraints: 限制

**[1564.82s] English:** Too much, if there's a crash, nobody dies and nobody gets ruined. But I'm interested in the  
**Translation:** 

**[1571.10s] English:** Combination of performance, partly because of the speed at which things are done, and part of being able  
**Translation:** 

**[1579.58s] English:** To do things that are necessary for the reliability of larger systems, if you spend all your  
**Translation:** 

**[1589.82s] English:** Time interpreting a simple function call, you are not going to have enough time to do proper signaling.  
**Translation:** Vocabulary: interpreting: 解释; signaling: 信号传递

**[1598.34s] English:** Processing to get the telephone calls to sound right. Either that, or you have to have 10 times...  
**Translation:** 

**[1604.88s] English:** As many computers, and you can't afford your phone anymore. It's a ridiculous idea in the modern world.  
**Translation:** 

**[1611.10s] English:** World because we've solved all of those problems. I mean, they keep popping up in different ways.  
**Translation:** 

**[1617.62s] English:** Because we tackle bigger and bigger problems.  
**Translation:** Vocabulary: tackle: 应对

**[1619.82s] English:** Efficiency remains always an important aspect.  
**Translation:** 

**[1622.94s] English:** But you have to think about efficiency, not just as speed, but as an enabler to important things.  
**Translation:** Vocabulary: enabler: 促成因素

**[1630.62s] English:** And one of the things it enables is reliability and dependability. When I press the pedal,  
**Translation:** 

**[1639.92s] English:** The brake pedal of a car is not actually connected directly to anything but a computer.  
**Translation:** Vocabulary: reliability: 可靠性和依赖性

**[1648.06s] English:** Yeah.  
**Translation:** 

**[1648.68s] English:** That computer better not.  
**Translation:** 

**[1649.80s] English:** Work.  
**Translation:** 

**[1650.32s] English:** Let's talk about reliability just a little bit. Modern cars have ECUs and have millions  
**Translation:** 

**[1659.12s] English:** Of lines of code today, this is certainly especially true of autonomous vehicles, where  
**Translation:** 

**[1665.96s] English:** Some of the aspects of the control or driver assistance systems that steer the car, that  
**Translation:** Vocabulary: autonomous: 独立控制的

**[1670.56s] English:** Keep it in the lane, and so on. I talk to regulators and people in the government who are very nervous.  
**Translation:** 

**[1677.84s] English:** About testing the safety.  
**Translation:** Vocabulary: regulators: 监管者

**[1678.92s] English:** Yeah.  
**Translation:** 

**[1679.16s] English:** Yeah.  
**Translation:** 

**[1679.44s] English:** Yeah.  
**Translation:** 

**[1679.50s] English:** Yeah.  
**Translation:** 

**[1679.60s] English:** Yeah.  
**Translation:** 

**[1679.70s] English:** Yeah.  
**Translation:** 

**[1679.74s] English:** Yeah.  
**Translation:** 

**[1679.76s] English:** Yeah.  
**Translation:** 

**[1679.80s] English:** Yeah.  
**Translation:** 

**[1680.00s] English:** These systems of software, ultimately, make decisions that could lead to fatalities.  
**Translation:** 

**[1687.32s] English:** So, how do we test software systems like these?  
**Translation:** 

**[1693.94s] English:** First of all, safety, like performance and like security, is a system's property.  
**Translation:** 

**[1703.92s] English:** People tend to look at one part of a system at a time, and saying something like, "this,  
**Translation:** 

**[1708.70s] English:** Is it secure?  
**Translation:** 

**[1710.82s] English:** That's all right.  
**Translation:** 

**[1711.82s] English:** I don't need to do that.  
**Translation:** 

**[1713.52s] English:** Yeah, that piece of code is secure.  
**Translation:** 

**[1715.70s] English:** I'll buy your operator.  
**Translation:** 

**[1718.72s] English:** If you want reliability, if you want performance, if you want security,  
**Translation:** 

**[1724.80s] English:** You have to look at the whole system.  
**Translation:** Vocabulary: reliability: 可靠性

**[1727.14s] English:** I did not expect you to say that, but that's very true.  
**Translation:** 

**[1729.80s] English:** Yes.  
**Translation:** 

**[1730.80s] English:** I'm dealing with one part of the system, and I want my part to be really good, but I know  
**Translation:** 

**[1735.62s] English:** It's not the whole system.  
**Translation:** 

**[1737.66s] English:** Furthermore,...  
**Translation:** 

**[1738.66s] English:** Yes.  
**Translation:** 

**[1739.66s] English:** Making an individual part perfect may actually not be the best way to get the highest.  
**Translation:** 

**[1747.10s] English:** Degree of reliability and performance, and such.  
**Translation:** 

**[1750.42s] English:** There are people who say that C++ is not type-safe.  
**Translation:** 

**[1754.30s] English:** You can break it.  
**Translation:** 

**[1755.90s] English:** Sure.  
**Translation:** 

**[1756.90s] English:** I can break anything that runs on a computer.  
**Translation:** 

**[1759.94s] English:** I may not go through your type system.  
**Translation:** 

**[1763.56s] English:** If I wanted to break into your computer, I'll probably try SQL injection.  
**Translation:** Vocabulary: injection: 注入攻击

**[1767.78s] English:** It's very true.  
**Translation:** 

**[1769.72s] English:** If you think about safety or even reliability at a system level, especially when a human is involved, ...  
**Translation:** 

**[1775.74s] English:** Being involved, it starts becoming hopeless pretty quickly in terms of proving that something.  
**Translation:** 

**[1786.22s] English:** It is safe to a certain level because there are so many variables, and it's so complex.  
**Translation:** 

**[1791.78s] English:** Yeah.  
**Translation:** 

**[1792.78s] English:** Well, let's get back to something we can talk about and actually make some progress on.  
**Translation:** 

**[1797.78s] English:** Yes.  
**Translation:** 

**[1798.78s] English:** We can look at C++.  
**Translation:** 

**[1800.00s] English:** Programs, and we can try and make sure they crash less often—the way you do.  
**Translation:** 

**[1807.98s] English:** That is largely by simplification. It is not the first step, however, to simplify the.  
**Translation:** Vocabulary: simplification: 简化; simplify: 简化

**[1816.98s] English:** Code has less code, which has code that is less likely to go wrong; it's not by  
**Translation:** 

**[1822.20s] English:** Runtime testing everything; it is not done by big test frameworks that you are using.  
**Translation:** Vocabulary: runtime: 运行时

**[1828.56s] English:** Yes, we do that as well, but the first step is actually to make sure that when you  
**Translation:** 

**[1835.18s] English:** Want to express something, you can express it directly in code rather than  
**Translation:** 

**[1841.32s] English:** Going through endless loops and convolutions in your head before it gets  
**Translation:** 

**[1846.14s] English:** Down the code that if the way you are thinking about a problem is not in the  
**Translation:** Vocabulary: convolutions: 复杂曲折的想法

**[1853.58s] English:** Code: There is a missing piece, that's just in your head.  
**Translation:** 

**[1858.56s] English:** And the code you can see what it does, but it cannot see what you thought about.  
**Translation:** 

**[1864.08s] English:** It's only true unless you have expressed things directly when you express things.  
**Translation:** 

**[1868.80s] English:** Directly, you can maintain it; it's easier to find errors, it's easier to make.  
**Translation:** 

**[1874.10s] English:** Modifications: it's actually easier to test, and lo and behold, it runs faster.  
**Translation:** 

**[1879.80s] English:** And therefore, you can use a smaller number of computers, which means there's  
**Translation:** Vocabulary: behold: 果然; modifications: 修改

**[1886.32s] English:** Less hardware that could possibly break.  
**Translation:** 

**[1888.56s] English:** But, in the domain I'm dealing with, that's the simplification I'm after.  
**Translation:** Vocabulary: simplification: 简化

**[1893.76s] English:** How do you inspire or ensure that all of your songs fit well into the  
**Translation:** 

**[1899.48s] English:** Server: The most important thing here are all the released songs.  
**Translation:** 

**[1903.56s] English:** However, they are my favorite ones. Just check them out! I have it on the  
**Translation:** 

**[1908.24s] English:** Website: This and That, which is on the blog, so those songs are the ones that.  
**Translation:** 

**[1913.46s] English:** Would get out of on the Internet better than any of the other songs, if that's  
**Translation:** 

**[1917.90s] English:** Right.  
**Translation:** 

**[1918.56s] English:** That  
**Translation:** 

**[1920.00s] English:** Einstein's level of simplification has been reached. So, can you do a code review? Can you look at the code?  
**Translation:** 

**[1929.12s] English:** If I gave you the code for the Ford F-150 and said, "Here, is this a mess or is this okay?  
**Translation:** 

**[1938.72s] English:** Is it possible to tell? Is it possible to regulate?  
**Translation:** Vocabulary: regulate: 调控

**[1943.04s] English:** An experienced developer can look at code and see if it smells.  
**Translation:** 

**[1947.84s] English:** I mixed metaphors deliberately. The point is that.  
**Translation:** Vocabulary: metaphors: 比喻

**[1957.76s] English:** It is hard to generate something that is really obviously clean and can be appreciated.  
**Translation:** 

**[1968.96s] English:** But you can usually recognize when you haven't reached that point.  
**Translation:** 

**[1973.84s] English:** And so, I have never looked at.  
**Translation:** 

**[1978.48s] English:** The F-150 code, so I wouldn't know. But I know what I ought to be looking for. I'll be looking.  
**Translation:** 

**[1986.48s] English:** For some tricks that correlate with bugs, and elsewhere. And I have tried to formulate rules.  
**Translation:** 

**[1995.68s] English:** For what good code looks like, and the current version of that is called the C++ Core Guidelines.  
**Translation:** Vocabulary: correlate: 相关; guidelines: 准则

**[2007.52s] English:** One.  
**Translation:** 

**[2007.84s] English:** The thing people should remember is that there's what you can do in a language, and what you should do.  
**Translation:** 

**[2015.52s] English:** In a language, you have lots of things that are necessary in some contexts, but not in others.  
**Translation:** 

**[2022.08s] English:** There are things that exist just because there's 30-year-old code out there, and you can't get rid of them.  
**Translation:** 

**[2027.60s] English:** Of course, but you can't have rules that say, "when you create it, try and follow these rules.  
**Translation:** 

**[2034.64s] English:** This does not create.  
**Translation:** 

**[2037.84s] English:** Good programs, by themselves, are effective.  
**Translation:** 

**[2040.00s] English:** But it limits the damage from mistakes.  
**Translation:** 

**[2043.50s] English:** It limits the possibilities of mistakes.  
**Translation:** 

**[2046.92s] English:** And basically, we are trying to say,  
**Translation:** 

**[2049.18s] English:** What is it that a good programmer does?  
**Translation:** 

**[2051.84s] English:** At the fairly simple level of where you use the language.  
**Translation:** Vocabulary: programmer: 程序员

**[2056.32s] English:** And how do you use it?  
**Translation:** 

**[2057.84s] English:** Now, I can put all the rules for chiseling in marble.  
**Translation:** Vocabulary: chiseling: 在大理石上雕刻

**[2063.50s] English:** It doesn't mean that somebody who follows all of those rules  
**Translation:** 

**[2067.22s] English:** Can do a masterpiece by Michelangelo.  
**Translation:** Vocabulary: masterpiece: 杰作; michelangelo: 米开朗基罗

**[2070.00s] English:** That is, there's something else to writing a good program.  
**Translation:** 

**[2076.54s] English:** Is there anything else that can create an important work of art?  
**Translation:** 

**[2082.04s] English:** That is, there's some kind of inspiration, understanding, or gift.  
**Translation:** 

**[2088.52s] English:** But we can approach the sort of technical,  
**Translation:** 

**[2095.74s] English:** The craftsmanship level of it.  
**Translation:** 

**[2099.30s] English:** The craftsmanship level of it.  
**Translation:** Vocabulary: craftsmanship: 工艺水平

**[2099.98s] English:** The craftsmanship level of it.  
**Translation:** 

**[2100.00s] English:** The famous painters, the famous sculptures.  
**Translation:** Vocabulary: sculptures: 著名雕塑

**[2102.54s] English:** Was, among other things, a superb craftsman.  
**Translation:** 

**[2107.42s] English:** They could express their ideas using their tools very well.  
**Translation:** Vocabulary: craftsman: 手工艺人; superb: 卓越的

**[2114.34s] English:** And so, these days, I think what I'm doing,  
**Translation:** 

**[2118.12s] English:** What a lot of people are doing,  
**Translation:** 

**[2119.46s] English:** We are still trying to figure it out.  
**Translation:** 

**[2120.98s] English:** How it is to use our tools very well.  
**Translation:** 

**[2124.38s] English:** For a really good piece of code,  
**Translation:** 

**[2128.52s] English:** You need a spark.  
**Translation:** 

**[2129.94s] English:** You need a spark of inspiration.  
**Translation:** 

**[2131.10s] English:** And you can't, I think, regulate that.  
**Translation:** Vocabulary: regulate: 控制

**[2133.50s] English:** You cannot say that I'll take a picture only,  
**Translation:** 

**[2138.70s] English:** I'll buy your picture only if you're at least Van Gogh.  
**Translation:** 

**[2144.86s] English:** There are other things you can regulate.  
**Translation:** 

**[2147.40s] English:** But, not the inspiration.  
**Translation:** 

**[2150.14s] English:** I think that's quite beautifully put.  
**Translation:** 

**[2152.88s] English:** It is true that there is,  
**Translation:** 

**[2156.36s] English:** As an experienced programmer,  
**Translation:** 

**[2158.04s] English:** When you see code,  
**Translation:** Vocabulary: programmer: 程序员

**[2159.26s] English:** That's it.  
**Translation:** 

**[2160.00s] English:** Inspired, that's kind of like Michelangelo — you know, when you see his work. And the opposite of that is  
**Translation:** 

**[2170.40s] English:** Code that is messy, code that smells—you know, when you see it, and I'm not sure you can describe it.  
**Translation:** 

**[2176.82s] English:** In words, except vaguely through guidelines and so on, yes, it's easier to recognize ugly than to.  
**Translation:** Vocabulary: guidelines: 准则; vaguely: 模糊地

**[2184.66s] English:** Recognize beauty in code, and for the reason is that sometimes beauty comes from something that's  
**Translation:** 

**[2191.80s] English:** Innovative and unusual; you have to sometimes think reasonably hard to appreciate that.  
**Translation:** Vocabulary: innovative: 新颖的; reasonably: 合理地

**[2198.16s] English:** On the other hand, the messes have things in common, and you can have static checkers.  
**Translation:** 

**[2208.04s] English:** And dynamic checkers that find a large number of the  
**Translation:** Vocabulary: messes: 混乱的事情

**[2214.66s] English:** Most common mistakes you can catch a lot of sloppiness mechanically. I'm a great fan of.  
**Translation:** 

**[2224.10s] English:** Static analysis, in particular, because you can check for not just language rules but for  
**Translation:** Vocabulary: mechanically: 机械地; sloppiness: 粗心

**[2231.06s] English:** The use of language rules, and I think we will see much more static analysis in the coming decade.  
**Translation:** 

**[2238.46s] English:** Can you describe what static analysis is? It involves representing a piece of code.  
**Translation:** 

**[2244.66s] English:** So, that you can write a program that goes over that representation and look for things that are  
**Translation:** 

**[2254.10s] English:** Right, and not right. So, for instance, you can analyze a program to see if  
**Translation:** 

**[2263.88s] English:** Resources are leaked — that's one of my favorite problems. It's not actually all that hard, and...  
**Translation:** 

**[2274.66s] English:** You can do it if you're writing in C-level—you have to have a mallet.  
**Translation:** Vocabulary: leaked: 泄露; mallet: 大锤

**[2280.00s] English:** And it's free, and they have to match. If you have them in a single function,  
**Translation:** 

**[2287.44s] English:** You can usually do it very easily. If there's a malloc here, there should be a free there.  
**Translation:** 

**[2294.32s] English:** On the other hand, in between can be during complete code, and then it becomes impossible.  
**Translation:** 

**[2299.76s] English:** If you pass that pointer to the memory out of a function, and then...  
**Translation:** 

**[2305.52s] English:** You want to make sure that the fix is done somewhere else; now it gets really difficult.  
**Translation:** 

**[2314.00s] English:** For static analysis, you can run through a program, and you can try and figure out:  
**Translation:** 

**[2320.56s] English:** If there are any leaks, what you will probably find is that you will find some leaks.  
**Translation:** 

**[2328.16s] English:** And you will find quite a few places where your analysis cannot be complete.  
**Translation:** Vocabulary: cannot: 不能

**[2333.76s] English:** It might depend on runtime.  
**Translation:** 

**[2335.52s] English:** It might depend on the cleverness of your analyzer, and it might take a long time.  
**Translation:** Vocabulary: analyzer: 分析器; runtime: 运行时

**[2343.44s] English:** Some of these programs run for a long time. But if you combine such analysis,  
**Translation:** 

**[2352.32s] English:** With a set of rules that says how people could use it, you can actually see why the  
**Translation:** 

**[2357.60s] English:** Rules are violated, and that stops you from getting into the impossible complexities. You'd  
**Translation:** 

**[2365.52s] English:** We want to solve the holding problem.  
**Translation:** Vocabulary: complexities: 复杂性; violated: 违反

**[2368.64s] English:** So, static analysis is looking at the code without running the code?  
**Translation:** 

**[2372.16s] English:** Yes.  
**Translation:** 

**[2372.96s] English:** And thereby, it's almost not production code, but it's almost like an educational tool.  
**Translation:** 

**[2380.56s] English:** Of how the language should be used. It guides you at its best, right? It would...  
**Translation:** 

**[2387.44s] English:** Guide you in how to write future code, as well, and you learn together.  
**Translation:** 

**[2392.32s] English:** Yes. So, basically, you need a set of rules for how you...  
**Translation:** 

**[2395.52s] English:** You use the language, then you need a static analysis that...  
**Translation:** 

**[2400.00s] English:** Catches your mistakes when you violate the rules, or when your code ends up doing things that it  
**Translation:** Vocabulary: violate: 违反规则

**[2408.80s] English:** Shouldn't we break the rules despite the restrictions, because there's often more we can achieve, and again, it's  
**Translation:** 

**[2415.32s] English:** Back to my idea: I would much rather find errors before I start running the code.  
**Translation:** 

**[2420.14s] English:** If nothing else, once the code runs and if it catches an error at runtime, I have to have an error message.  
**Translation:** 

**[2426.96s] English:** Handler, and one of the hardest things to write in code is error handling code because you know.  
**Translation:** Vocabulary: runtime: 运行时

**[2434.34s] English:** Something went wrong. Do you know exactly what went wrong? Usually, we don't. How can you recover?  
**Translation:** 

**[2441.48s] English:** When you don't know what the problem was, you can't be a hundred percent sure what the problem was.  
**Translation:** 

**[2447.00s] English:** Many, many cases, and this is part of it. So, yes, we need good languages with good types.  
**Translation:** 

**[2455.78s] English:** Systems we need.  
**Translation:** 

**[2456.94s] English:** Rules for how to use them; we need static analysis, and the ultimate form of static analysis is...  
**Translation:** 

**[2463.34s] English:** Course, program, proof — but that still doesn't scale to the kind of systems we deploy, then we start.  
**Translation:** Vocabulary: deploy: 部署

**[2470.58s] English:** Needing some testing and the rest of the stuff, so C++ is an object-oriented programming language.  
**Translation:** 

**[2480.00s] English:** That creates, especially with its newer versions, as we'll talk about, higher and higher levels of.  
**Translation:** 

**[2485.06s] English:** Abstraction  
**Translation:** 

**[2485.62s] English:** So,  
**Translation:** Vocabulary: abstraction: 抽象

**[2486.94s] English:** How do you design something, let's even go back to the origin of C++, how do you design something with?  
**Translation:** 

**[2493.94s] English:** So much abstraction that's still efficient and is still something you can manage.  
**Translation:** 

**[2504.74s] English:** Do static analysis on what you can have; you can have constraints, and they can be reliable. All those things we've  
**Translation:** 

**[2510.90s] English:** Talked about, so create the thing. To me, there's a slight tension between the static and...  
**Translation:** Vocabulary: constraints: 限制; slight: 轻微

**[2516.82s] English:** Analysis, and the high-level abstraction, and the high-level abstraction, and the high-level abstraction.  
**Translation:** 

**[2520.00s] English:** Efficiency: that's a good question; I could probably have a year's worth of coursework just trying to answer it.  
**Translation:** 

**[2528.40s] English:** Yes, there's a tension between efficiency and abstraction, but you also get the interesting  
**Translation:** 

**[2535.44s] English:** Situation that you get the best efficiency out of the best abstraction, and my main tool.  
**Translation:** 

**[2542.80s] English:** For efficiency and performance, abstraction is key. So, let's go back to how C++ does it.  
**Translation:** 

**[2550.08s] English:** Got there, you said it was an object-oriented programming language, but I actually never said that.  
**Translation:** 

**[2556.08s] English:** It's always quoted, but I never did. I said C++ supports object-oriented programming, but it's  
**Translation:** 

**[2563.48s] English:** Not and other techniques, and that's important because I think that the best solution to most  
**Translation:** Vocabulary: quoted: 引用

**[2572.80s] English:** Complex, interesting problems require ideas and techniques from things that have been called  
**Translation:** 

**[2581.28s] English:** Object-Oriented, Data Abstraction, Functional, Traditional C-Style Code  
**Translation:** Vocabulary: abstraction: 抽象; functional: 函数式

**[2591.84s] English:** All of the above, and so when I was designing C++, I soon realized I couldn't just add.  
**Translation:** 

**[2601.12s] English:** Features:  
**Translation:** 

**[2603.44s] English:** If you just add what looks pretty, or what people ask for, or what you think is good one by one, you're  
**Translation:** 

**[2611.12s] English:** Not going to get a coherent whole; what you need is a set of guidelines that guide your  
**Translation:** Vocabulary: coherent: 连贯的整体; guidelines: 指导原则

**[2619.20s] English:** Decisions: Should this feature be included, or should it be removed? How should a feature be modified?  
**Translation:** 

**[2626.24s] English:** Before it can go in, and such, there's a section in the book I wrote about that, which is about science and evolution.  
**Translation:** 

**[2632.80s] English:** G++, there's a whole bunch of rules like that.  
**Translation:** 

**[2636.78s] English:** Most of them are not language-technical.  
**Translation:** 

**[2640.00s] English:** There are things like don't violate the static type system.  
**Translation:** 

**[2644.86s] English:** Because I like static type systems for the obvious reasons.  
**Translation:** Vocabulary: violate: 违反

**[2648.36s] English:** That I like things to be reliable on reasonable amounts of hardware.  
**Translation:** 

**[2656.56s] English:** But one of these rules is the zero-overhead principle.  
**Translation:** 

**[2661.44s] English:** What kind of principle?  
**Translation:** 

**[2662.08s] English:** The Zero Overhead Principle.  
**Translation:** 

**[2664.10s] English:** It basically says that if you have an abstraction,  
**Translation:** 

**[2669.60s] English:** It should not cost anything compared to writing the equivalent code at a lower level.  
**Translation:** Vocabulary: abstraction: 抽象

**[2680.10s] English:** So, if I have a matrix multiplication, say:  
**Translation:** 

**[2684.44s] English:** It should be written in such a way that you could not drop to the C level of abstraction.  
**Translation:** Vocabulary: matrix: 矩阵; multiplication: 乘法

**[2692.58s] English:** And use arrays and pointers, and run faster.  
**Translation:** 

**[2697.86s] English:** And so, people have written such.  
**Translation:** Vocabulary: arrays: 数组

**[2699.60s] English:** And so, people have written such matrix multiplications.  
**Translation:** 

**[2702.42s] English:** And they've actually gotten code that ran faster than Fortran.  
**Translation:** Vocabulary: multiplications: 矩阵乘法

**[2706.76s] English:** Because once you had the right abstraction,...  
**Translation:** 

**[2709.10s] English:** You can eliminate temporaries.  
**Translation:** Vocabulary: temporaries: 临时变量

**[2713.24s] English:** And you can do loop fusion and other good stuff like that.  
**Translation:** 

**[2717.94s] English:** That's quite hard to do by hand, and in a lower-level language.  
**Translation:** Vocabulary: fusion: 融合

**[2722.24s] English:** And there are some really nice examples of that.  
**Translation:** 

**[2725.48s] English:** And the key here is that the matrix,  
**Translation:** 

**[2728.78s] English:** That's a matrix, that's a matrix, that's a matrix, that's a matrix, that's a matrix.  
**Translation:** 

**[2730.54s] English:** The matrix abstraction allows you to write code that is simple and easy.  
**Translation:** 

**[2735.94s] English:** You can do that in any language.  
**Translation:** 

**[2737.70s] English:** But with C++, it has the features so that you can also have this thing run faster.  
**Translation:** 

**[2742.68s] English:** Than if you hand-coded it.  
**Translation:** 

**[2745.16s] English:** Now, people have given that lecture many times—I and others.  
**Translation:** 

**[2750.34s] English:** And a very common question after the talk is:  
**Translation:** 

**[2753.40s] English:** Where you have demonstrated that you can outperform Fortran.  
**Translation:** 

**[2756.14s] English:** For dense matrix multiplication.  
**Translation:** 

**[2758.90s] English:** People come up and say,  
**Translation:** 

**[2759.56s] English:** Says yes.  
**Translation:** 

**[2760.00s] English:** But that was C++. If I rewrote your code in C, how much faster would it run? The answer is much.  
**Translation:** Vocabulary: rewrote: 重写

**[2768.08s] English:** Slower. This happened the first time, actually, back in the '80s, with a friend of mine called  
**Translation:** 

**[2774.88s] English:** Doug McElroy, who demonstrated exactly this effect. And so the principle is: you should give programmers  
**Translation:** 

**[2785.12s] English:** The tools so that the abstractions can follow the zero-word principle. Furthermore, when you put in  
**Translation:** 

**[2791.92s] English:** A language feature in C++, or a standard library feature, you try to meet this. It doesn't mean  
**Translation:** Vocabulary: abstractions: 抽象

**[2798.72s] English:** It's absolutely optimal, but it means if you hand-code it with the usual facilities in the language,...  
**Translation:** 

**[2806.88s] English:** In C++, in C, you should not be able to better it. Usually, you can do better if you use embedded.  
**Translation:** Vocabulary: embedded: 嵌入式的; optimal: 最优化的

**[2815.12s] English:** Assembler for machine code for some of the details to utilize part of a computer that the  
**Translation:** 

**[2822.64s] English:** Compiler doesn't know about it. But you should get to that point before you beat the abstraction.  
**Translation:** Vocabulary: assembler: 汇编器; utilize: 利用

**[2829.12s] English:** So, that's a beautiful ideal to reach for.  
**Translation:** 

**[2832.96s] English:** And we meet it quite often.  
**Translation:** 

**[2834.64s] English:** Quite often. So, where's the magic of that coming from? Some of it is the compilation.  
**Translation:** 

**[2841.36s] English:** Process. So, the implementation is in C++. Some of it,...  
**Translation:** Vocabulary: compilation: 编译; implementation: 实现

**[2844.48s] English:** Is the design of C++?  
**Translation:** 

**[2845.04s] English:** So, the implementation is in C++. Some of it is due to the design of C++, and some of it is due to the design of C++.  
**Translation:** 

**[2845.12s] English:** Some of it is the design of the feature itself, the guidelines. So, I've recently and often talked about it.  
**Translation:** 

**[2852.24s] English:** To Chris Ladner, so Clang. Just out of curiosity, is your relationship in general with the different...  
**Translation:** Vocabulary: clang: 编译器; guidelines: 准则

**[2862.64s] English:** Implementations in C++, as you think about it, you and the committee, and other people in C++.  
**Translation:** 

**[2868.72s] English:** Think about the design of new features or previous features.  
**Translation:** Vocabulary: implementations: 实现

**[2872.08s] English:** In trying to reach the ideal of zero overhead, we  
**Translation:** 

**[2880.00s] English:** Does the magic come from the design, the guidelines, or from the implementations?  
**Translation:** 

**[2886.56s] English:** And, not all.  
**Translation:** 

**[2889.68s] English:** You focus on programming techniques, programming language features, and implementation techniques.  
**Translation:** 

**[2897.30s] English:** You need all three.  
**Translation:** 

**[2898.94s] English:** And how can you think about all three at the same time?  
**Translation:** 

**[2903.30s] English:** It takes some experience, some practice, and sometimes you get it wrong.  
**Translation:** 

**[2907.94s] English:** But after a while, you sort of get it right.  
**Translation:** 

**[2911.42s] English:** I don't write compilers anymore.  
**Translation:** 

**[2914.62s] English:** But Brian Kernighan pointed out that one of the reasons C++ succeeded was some of the craftsmanship I put into the early compilers.  
**Translation:** Vocabulary: compilers: 编译器; craftsmanship: 工艺

**[2930.96s] English:** And, of course, I did the language design.  
**Translation:** 

**[2932.74s] English:** And, of course, I wrote a fair amount of code using this kind of stuff.  
**Translation:** 

**[2936.44s] English:** And I think...  
**Translation:** 

**[2937.66s] English:** Most of the successes involve progress in all three areas together.  
**Translation:** 

**[2945.34s] English:** A small group of people can do that.  
**Translation:** 

**[2948.36s] English:** Two or three people can work together to do something like that.  
**Translation:** 

**[2952.16s] English:** It's ideal if it's one person who has all the skills necessary.  
**Translation:** 

**[2955.62s] English:** But nobody has all the skills necessary in all the fields where C++ is used.  
**Translation:** 

**[2961.44s] English:** So, if you want to approach my ideal in, say, concurrent programming,  
**Translation:** 

**[2966.34s] English:** You need to know about...  
**Translation:** Vocabulary: concurrent: 并发的

**[2967.66s] English:** You need to know about algorithms for concurrent programming.  
**Translation:** 

**[2970.48s] English:** You need to know the trigger of lock-free programming.  
**Translation:** 

**[2974.34s] English:** You need to know something about compiler techniques.  
**Translation:** 

**[2978.02s] English:** And then you have to know some of the application areas where this is used, like some forms of graphics or some forms of what we call web-serving kind of stuff.  
**Translation:** 

**[2995.62s] English:** And that's very hard to get into.  
**Translation:** 

**[2997.34s] English:** It's very hard to get into a single head.  
**Translation:** 

**[3000.00s] English:** Do it, too. So, are there differences in your view? Not saying which is better or so on, but differences in...  
**Translation:** 

**[3008.72s] English:** The Different Implementations of C++: Why Are There Several Sort of Maybe Naive Questions?  
**Translation:** Vocabulary: implementations: 实现; naive: 幼稚的

**[3015.76s] English:** For me, GCC and Clang are very reasonable choices when I designed C++.  
**Translation:** 

**[3025.68s] English:** Most languages have multiple implementations because, if you want an IBM implementation, you can run it on a Sun system.  
**Translation:** Vocabulary: clang: LLVM编译器; implementation: 实现版本

**[3036.96s] English:** If you want a Motorola, there were just many, many companies, and they each had their own.  
**Translation:** 

**[3042.16s] English:** Compilation structure and their old compilers; it was just fairly common that there were many of.  
**Translation:** Vocabulary: compilation: 编译; compilers: 编译器

**[3048.00s] English:** They and I wrote Cfront, assuming that other people would write compilers for C++.  
**Translation:** 

**[3055.68s] English:** If I were successful, and furthermore, I wanted to utilize all the backend infrastructures.  
**Translation:** Vocabulary: backend: 后端; infrastructures: 基础设施; utilize: 利用

**[3064.16s] English:** That were available, I soon realized that my users were using 25 different linkers, and I couldn't write  
**Translation:** 

**[3070.08s] English:** My own linker, yes, I could do it, but I couldn't write 25 linkers and still get any work done on the language.  
**Translation:** Vocabulary: linker: 链接器; linkers: 多种链接器

**[3080.08s] English:** And so, it came from a world where there were many linkers, many optimized.  
**Translation:** 

**[3085.68s] English:** As many compiler front ends, however, do not start but operate on many operating systems.  
**Translation:** Vocabulary: optimized: 优化过的

**[3094.40s] English:** The whole world was not an 86 and a Linux box, or something; whatever is the standard today.  
**Translation:** 

**[3101.36s] English:** In the old days, they said "a set of backs," so basically, I assumed there would be lots of.  
**Translation:** 

**[3108.24s] English:** Compilers: It was not a decision that there should be many compilers; it was just a fact.  
**Translation:** 

**[3114.80s] English:** The way the world is.  
**Translation:** 

**[3115.68s] English:** And, yes, many.  
**Translation:** 

**[3120.00s] English:** Hylas emerged, and today there are at least four front-ends: Clang, GCC, Microsoft, and  
**Translation:** Vocabulary: clang: 编译器

**[3131.56s] English:** EDG, it is the Design Group.  
**Translation:** 

**[3135.24s] English:** They supply a lot of the independent organizations and the embedded systems industry, and there's  
**Translation:** Vocabulary: embedded: 嵌入式

**[3143.90s] English:** Lots and lots of back-ends.  
**Translation:** 

**[3145.76s] English:** We have to think about how many dozen back-ends there are, because different machines have  
**Translation:** 

**[3153.40s] English:** Different things, especially in the embedded world, the machines are very different, the  
**Translation:** 

**[3158.52s] English:** Architectures are very different, and so having a single implementation was never an option.  
**Translation:** Vocabulary: implementation: 实现方式

**[3168.84s] English:** Now, I also happen to dislike monocultures.  
**Translation:** 

**[3173.28s] English:** Monocultures.  
**Translation:** Vocabulary: monocultures: 单一作物种植

**[3174.00s] English:** They are dangerous.  
**Translation:** 

**[3176.72s] English:** Because whoever owns the monoculture can go stale, and there's no competition, and  
**Translation:** Vocabulary: monoculture: 单一作物; stale: 陈旧

**[3183.48s] English:** There's no incentive to innovate.  
**Translation:** 

**[3185.98s] English:** There's a lot of incentive to put barriers in the way of change, because, hey, we own those barriers.  
**Translation:** Vocabulary: barriers: 障碍; incentive: 激励; innovate: 创新

**[3192.46s] English:** The world, and it's a very comfortable world for us, and who are you to mess with that?  
**Translation:** 

**[3198.68s] English:** So, I really am very happy that there are four front-ends for C++.  
**Translation:** 

**[3205.76s] English:** Clang is great, but GCC was great, but then it got somewhat stale. Clang came along, and  
**Translation:** 

**[3214.76s] English:** GCC is much better now.  
**Translation:** Vocabulary: clang: 撞击声

**[3217.26s] English:** Competition is good.  
**Translation:** 

**[3218.20s] English:** Microsoft is much better now.  
**Translation:** 

**[3221.20s] English:** So, at least a low number of front-end developers puts a lot of pressure on standards compliance.  
**Translation:** 

**[3232.28s] English:** And also, on performance and error messages.  
**Translation:** 

**[3235.76s] English:** And at compile-time, speed—and all this good stuff that we want.  
**Translation:** 

**[3240.00s] English:** Do you think, crazy question, there might come along an implementation of C++, given all its history, written from scratch? Do you hope there might come along such an implementation?  
**Translation:** Vocabulary: implementation: 实现; scratch: 从头开始

**[3256.34s] English:** So, written today from scratch.  
**Translation:** 

**[3259.12s] English:** Well, Clang and the LLVM are more or less written from scratch.  
**Translation:** 

**[3264.48s] English:** But there have been C++ 11, 14, 17, and 20—there have been a lot of features.  
**Translation:** 

**[3271.04s] English:** I think sooner or later, someone is going to try again.  
**Translation:** 

**[3274.08s] English:** There have been attempts to write new C++ compilers, and some of them have been used, while some have been absorbed into others and such.  
**Translation:** 

**[3283.40s] English:** Yeah, it will happen.  
**Translation:** Vocabulary: compilers: 编译器

**[3284.98s] English:** So, what are the key features of C++?  
**Translation:** 

**[3288.06s] English:** And let's use that as a way to sort of talk about it.  
**Translation:** 

**[3294.48s] English:** The evolution of C++ and the new feature.  
**Translation:** 

**[3297.16s] English:** So, at the highest level, what were the features that were there in the beginning?  
**Translation:** 

**[3302.08s] English:** What features were added?  
**Translation:** 

**[3304.52s] English:** Let's first get a principle or an aim in place.  
**Translation:** 

**[3310.04s] English:** C++ is for people who want to use hardware really well, and then manage the complexity of doing that through abstraction.  
**Translation:** 

**[3321.74s] English:** And so, the first facility.  
**Translation:** Vocabulary: abstraction: 抽象; complexity: 复杂性

**[3324.48s] English:** You have a way of manipulating the machines at a fairly low level that looks very much like C.  
**Translation:** 

**[3334.12s] English:** It has loops, it has variables, and it has pointers (like machine addresses). It can access memory directly and can allocate stuff in the absolute minimum of space needed on the machine.  
**Translation:** Vocabulary: allocate: 分配; manipulating: 操作

**[3351.08s] English:** There's a machine facing part of C++.  
**Translation:** 

**[3354.48s] English:** Which is roughly equivalent to C.  
**Translation:** 

**[3357.42s] English:** I said that C++ could beat C, and it can.  
**Translation:** 

**[3360.00s] English:** And it doesn't mean I dislike C. If I disliked C, I wouldn't have built on it.  
**Translation:** 

**[3366.58s] English:** Furthermore, after Dennis Ritchie, I'm probably the major contributor to modern C.  
**Translation:** 

**[3373.90s] English:** And, well, I had lunch with Dennis most days for 16 years, and we never had a harsh word between us.  
**Translation:** Vocabulary: contributor: 贡献者; ritchie: 里奇

**[3384.20s] English:** So, these C versus C++ fights are for people who don't quite understand what's going on.  
**Translation:** 

**[3392.08s] English:** Then the other part is the abstraction.  
**Translation:** 

**[3395.66s] English:** And there, the key is the class, which is a user-defined type.  
**Translation:** 

**[3400.30s] English:** And my idea for the class is that you should be able to build a type that's just like the built-in types.  
**Translation:** 

**[3407.24s] English:** In the way you use them, in the way you declare them, and in the way you get the memory.  
**Translation:** 

**[3413.32s] English:** Okay.  
**Translation:** 

**[3413.42s] English:** And you can do just as well.  
**Translation:** 

**[3415.78s] English:** So, in C++, as an int (like in C), you should be able to build an abstraction, a class, which we can call CapitalInt.  
**Translation:** Vocabulary: abstraction: 抽象

**[3427.38s] English:** That you can use exactly like an integer, and run just as fast as an integer.  
**Translation:** 

**[3433.66s] English:** There's the idea right there.  
**Translation:** Vocabulary: integer: 整数

**[3436.22s] English:** And, of course, you probably don't want to use the int itself, but it has happened.  
**Translation:** 

**[3441.78s] English:** People have wanted integers.  
**Translation:** Vocabulary: integers: 整数

**[3443.42s] English:** Integers that were range-checked so that you couldn't overflow, and such.  
**Translation:** 

**[3448.12s] English:** Especially for very safety-critical applications, such as the fuel injection for a marine diesel engine on the largest ships.  
**Translation:** Vocabulary: diesel: 柴油; injection: 喷射; overflow: 溢出

**[3457.18s] English:** This is a real example, by the way.  
**Translation:** 

**[3458.96s] English:** This has been done.  
**Translation:** 

**[3460.84s] English:** They built themselves an integer that was just like an integer, except that it couldn't overflow.  
**Translation:** 

**[3467.42s] English:** If there was an overflow, you would go into error handling.  
**Translation:** 

**[3471.30s] English:** And then you built more.  
**Translation:** 

**[3473.42s] English:** More interesting types.  
**Translation:** 

**[3474.48s] English:** You can build a matrix, which you need to do graphics.  
**Translation:** 

**[3480.00s] English:** Or, you could build a gnome for a video game, and all these are classes, and they appear just  
**Translation:** Vocabulary: gnome: 矮人; matrix: 矩阵

**[3487.04s] English:** Like the built-in types, exactly, in terms of efficiency, and so on. So, what else is there?  
**Translation:** 

**[3491.76s] English:** And flexibility, so uh, I don't know, for people who are not familiar with object-oriented programming,...  
**Translation:** Vocabulary: flexibility: 灵活性

**[3499.92s] English:** There's inheritance, and there's a hierarchy of classes. You can just, like you said, create a generic...  
**Translation:** 

**[3506.72s] English:** A vehicle that can turn left, so what people found was that you don't actually know how to say this.  
**Translation:** Vocabulary: generic: 通用; hierarchy: 等级体系; inheritance: 继承

**[3520.48s] English:** A lot of types are related. That is, all vehicles are related.  
**Translation:** 

**[3528.72s] English:** Bicycles, cars, fire engines, and tanks have some things in common and some things that differ.  
**Translation:** 

**[3536.72s] English:** And you would like to have the common things in common and having the differences.  
**Translation:** 

**[3542.40s] English:** Specifically, and when you didn't want to know about the differences, just turn left.  
**Translation:** 

**[3549.12s] English:** You don't have to worry about it. That's how you get the traditional object-oriented.  
**Translation:** 

**[3554.48s] English:** Programming coming out of similar adopted by Small Talk and C++, and all the others.  
**Translation:** 

**[3560.48s] English:** Languages: The other kind of obvious similarity between types comes when you have something.  
**Translation:** 

**[3566.56s] English:** Like a vector, a fortune gave us an array of doubles, but the minute you have  
**Translation:** Vocabulary: similarity: 相似性

**[3576.56s] English:** A vector of doubles. You want a vector of double-precision doubles, and for short doubles, for  
**Translation:** 

**[3583.68s] English:** Graphics, and why should you have a vector of integers while you're adding or a vector of?  
**Translation:** Vocabulary: integers: 整数

**[3591.68s] English:** Vectors and a vector of vectors of chess pieces—now you have a board.  
**Translation:** 

**[3596.56s] English:** Right, so this  
**Translation:** Vocabulary: vectors: 向量

**[3600.00s] English:** Is it expressed as the idea of a vector, and the variations come through?  
**Translation:** 

**[3608.08s] English:** Parameterization, and so here we get the two fundamental ways of abstracting: of having.  
**Translation:** Vocabulary: abstracting: 抽象; parameterization: 参数化; variations: 变化

**[3615.60s] English:** Similarities of types in C++ include inheritance and parameterization.  
**Translation:** 

**[3624.32s] English:** There's object-oriented programming, and there's generic programming.  
**Translation:** Vocabulary: generic: 泛型编程; inheritance: 继承

**[3630.00s] English:** Yeah, so you've presented it very nicely, but now you have to make all that happen and make  
**Translation:** 

**[3639.28s] English:** It can be efficient, so generic programming with templates—there's all kinds of magic going on, especially.  
**Translation:** Vocabulary: nicely: 漂亮地; templates: 模板

**[3645.84s] English:** Recently, you can help catch up, but it feels to me like you can do way more than what.  
**Translation:** 

**[3652.80s] English:** You just said that with templates, you can start doing this kind of metaprogramming, and you can.  
**Translation:** Vocabulary: metaprogramming: 元编程

**[3658.56s] English:** Do metaprogramming also?  
**Translation:** 

**[3660.00s] English:** Uh, I didn't go there, and in that explanation, we're trying to be very basic but go back.  
**Translation:** 

**[3666.40s] English:** On to the implementation. If you couldn't implement this efficiently,  
**Translation:** 

**[3671.52s] English:** If you couldn't use it so that it became efficient, it has no place in C++ because it will...  
**Translation:** Vocabulary: efficiently: 高效地; implement: 实现; implementation: 实施

**[3678.16s] English:** Violate the zero overhead principle, so when I had to get object-oriented programming inheritance.  
**Translation:** 

**[3687.36s] English:** I took the idea of virtual functions.  
**Translation:** Vocabulary: violate: 违反

**[3690.00s] English:** From similar virtual functions, "is a" is a similar term; "class" is a similar term; if you ever use those.  
**Translation:** 

**[3698.08s] English:** Words say thanks to Christian Nygaard and Oliver, and I did the simplest implementation I could.  
**Translation:** Vocabulary: nygaard: 南耶格

**[3706.72s] English:** Knew that it was basically a jump table, so you get the virtual function table, and the function goes in.  
**Translation:** 

**[3715.68s] English:** It does an indirect call through a table to get the right function—that's how you pick it.  
**Translation:** 

**[3720.00s] English:** The right thing there, and I thought that was trivial; it's close to optimal, and it was.  
**Translation:** 

**[3728.32s] English:** Obvious, it turned out that the simulator had a more complicated way of doing it, and therefore was slower.  
**Translation:** Vocabulary: optimal: 最优化的; simulator: 模拟器; trivial: 琐碎的

**[3733.76s] English:** And, um, it turns out that most languages have something that's a little bit more complicated.  
**Translation:** 

**[3738.88s] English:** Sometimes, it is more flexible, but you pay for it. And one of the strengths of C++ was that you could have both.  
**Translation:** Vocabulary: flexible: 有弹性的

**[3744.88s] English:** Could actually do this object-oriented stuff, and your overhead compared to ordinary functions.  
**Translation:** 

**[3752.40s] English:** There's no indirection; it's sort of in 5-10 to 25 percent. Uh, just the core—it's down there.  
**Translation:** 

**[3760.64s] English:** Not two, and that means you can afford to use it. Furthermore, in C++, you have the distinction.  
**Translation:** 

**[3768.16s] English:** Between a virtual function and a non-virtual function, if you don't want any overhead, if you  
**Translation:** 

**[3774.32s] English:** Don't need to use it; you can use it in C++. You have the distinction between a virtual function and a non-virtual function if you don't want any overhead or if you don't need.  
**Translation:** 

**[3774.88s] English:** The interaction that gives you the flexibility in object-oriented programming just doesn't ask for it.  
**Translation:** Vocabulary: flexibility: 灵活性

**[3782.56s] English:** So, the idea is that you only use virtual functions if you actually need the flexibility.  
**Translation:** 

**[3788.64s] English:** So, it's not zero overhead, but it's zero overhead compared to any other way of achieving the  
**Translation:** 

**[3794.00s] English:** Flexibility now, auto-parameterization: basically, the compiler looks at  
**Translation:** 

**[3804.88s] English:** At the template, it says the vector and it looks at the parameter, and then combines the two.  
**Translation:** Vocabulary: parameter: 参数; template: 模板

**[3817.04s] English:** Generates a piece of code that is exactly as if you had written a vector of that specific type.  
**Translation:** 

**[3824.00s] English:** Yes, so that's the minimal overhead. If you have many template parameters, you can  
**Translation:** Vocabulary: generates: 生成; minimal: 最小

**[3830.32s] English:** Actually, combine code that the compiler couldn't usually see at the same time.  
**Translation:** 

**[3834.88s] English:** And therefore, get code that is faster than  
**Translation:** 

**[3840.00s] English:** If you had handwritten the stuff, unless you were very, very clever.  
**Translation:** 

**[3844.84s] English:** So the thing is, parameterized code,  
**Translation:** Vocabulary: handwritten: 亲手写的; parameterized: 带参数的

**[3848.54s] English:** The compiler fills in stuff during the compilation process.  
**Translation:** 

**[3853.20s] English:** Not during runtime.  
**Translation:** Vocabulary: compilation: 编译; runtime: 运行时

**[3854.88s] English:** That's right.  
**Translation:** 

**[3856.06s] English:** And furthermore, it gives all the information it has gotten.  
**Translation:** 

**[3861.26s] English:** Which is the template, the parameter, and the context of use?  
**Translation:** 

**[3866.16s] English:** It combines the three and generates good code.  
**Translation:** 

**[3869.60s] English:** But it can generate, now, it's a little outside of what I'm even comfortable thinking about.  
**Translation:** 

**[3877.82s] English:** But it can generate a lot of code.  
**Translation:** 

**[3880.16s] English:** Yes.  
**Translation:** 

**[3881.48s] English:** And how do you remember being both amazed at the power of that idea?  
**Translation:** 

**[3888.20s] English:** And how ugly the debugging looked.  
**Translation:** 

**[3893.56s] English:** Yes, debugging can be truly horrid.  
**Translation:** Vocabulary: horrid: 糟糕的

**[3896.48s] English:** Come back to this because I have a solution.  
**Translation:** 

**[3899.60s] English:** Anyway, the debugging was ugly.  
**Translation:** 

**[3902.34s] English:** The code generated by C++ has always been ugly.  
**Translation:** 

**[3908.90s] English:** Because there are these inherent optimizations.  
**Translation:** Vocabulary: optimizations: 优化

**[3912.30s] English:** A modern C++ compiler has a front-end, middle-end, and back-end for optimizations.  
**Translation:** 

**[3917.72s] English:** Even cfront, back in 1983, had front-end and back-end optimizations.  
**Translation:** 

**[3923.70s] English:** I actually took the code, generated an internal representation,  
**Translation:** 

**[3928.64s] English:** Monotone.  
**Translation:** Vocabulary: monotone: 单调的声音

**[3929.60s] English:** I changed that implementation and representation to generate good code.  
**Translation:** 

**[3934.34s] English:** So, people say it's not a compiler; generate C.  
**Translation:** Vocabulary: implementation: 实现

**[3937.28s] English:** The reason it generated C was that I wanted to use C's code generators.  
**Translation:** 

**[3941.18s] English:** That was really good at back-end optimizations.  
**Translation:** Vocabulary: generators: 代码生成器

**[3944.18s] English:** But I needed front-end optimizations, and therefore, the C I generated was optimized C.  
**Translation:** 

**[3951.38s] English:** The way a really good, handcrafted optimizer, human could generate it,  
**Translation:** Vocabulary: handcrafted: 手工制作; optimized: 优化; optimizer: 优化器

**[3959.92s] English:** It was that the function didn't have to be too complex or too large.  
**Translation:** 

**[3960.00s] English:** Was not meant for humans; it was the output of a program, and it's much worse today—and with  
**Translation:** 

**[3960.72s] English:** It was able to do transcendental stuff well.  
**Translation:** 

**[3961.22s] English:** There are cacti, millions of jackals, creatures, characters, and things.  
**Translation:** Vocabulary: cacti: 仙人掌; transcendental: 超验的

**[3961.64s] English:** I got enough of that crap on my channel.  
**Translation:** 

**[3962.22s] English:** This is the end of the presentation.  
**Translation:** 

**[3962.72s] English:** See you again in another video!  
**Translation:** 

**[3963.34s] English:** TavaX out.  
**Translation:** 

**[3963.84s] English:** .  
**Translation:** 

**[3964.34s] English:** .  
**Translation:** 

**[3964.84s] English:** .  
**Translation:** 

**[3965.44s] English:** .  
**Translation:** 

**[3965.52s] English:** Templates; it gets much worse still, so it's hard to combine simple debugging with.  
**Translation:** 

**[3965.84s] English:** .  
**Translation:** 

**[3966.22s] English:** .  
**Translation:** 

**[3966.68s] English:** .  
**Translation:** 

**[3967.38s] English:** .  
**Translation:** 

**[3967.94s] English:** .  
**Translation:** 

**[3968.48s] English:** .  
**Translation:** 

**[3970.38s] English:** .  
**Translation:** 

**[3970.88s] English:** .  
**Translation:** 

**[3971.38s] English:** .  
**Translation:** 

**[3971.88s] English:** .  
**Translation:** 

**[3972.38s] English:** .  
**Translation:** 

**[3973.44s] English:** .  
**Translation:** 

**[3973.98s] English:** .  
**Translation:** 

**[3974.40s] English:** .  
**Translation:** 

**[3974.40s] English:** Symbol with the optimal code, because the idea is to drag in information from different parts.  
**Translation:** Vocabulary: optimal: 最佳的

**[3974.90s] English:** .  
**Translation:** 

**[3975.28s] English:** .  
**Translation:** 

**[3975.48s] English:** .  
**Translation:** 

**[3976.40s] English:** .  
**Translation:** 

**[3976.46s] English:** .  
**Translation:** 

**[3976.96s] English:** .  
**Translation:** 

**[3977.44s] English:** .  
**Translation:** 

**[3977.64s] English:** .  
**Translation:** 

**[3978.14s] English:** .  
**Translation:** 

**[3978.74s] English:** .  
**Translation:** 

**[3979.16s] English:** .  
**Translation:** 

**[3979.54s] English:** .  
**Translation:** 

**[3979.96s] English:** .  
**Translation:** 

**[3980.26s] English:** .  
**Translation:** 

**[3980.52s] English:** .  
**Translation:** 

**[3981.14s] English:** .  
**Translation:** 

**[3981.36s] English:** Of the code to generate good code, a machine code and that's not readable, so  
**Translation:** 

**[3981.68s] English:** .  
**Translation:** 

**[3982.14s] English:** .  
**Translation:** 

**[3983.14s] English:** .  
**Translation:** 

**[3983.52s] English:** .  
**Translation:** 

**[3984.02s] English:** .  
**Translation:** 

**[3984.92s] English:** .  
**Translation:** 

**[3985.46s] English:** .  
**Translation:** 

**[3987.40s] English:** .  
**Translation:** 

**[3988.06s] English:** .  
**Translation:** 

**[3988.90s] English:** .  
**Translation:** 

**[3991.52s] English:** What people often do for debugging is to turn the optimizer off.  
**Translation:** 

**[3997.20s] English:** And so, you get code that when something in your source code looks like a  
**Translation:** 

**[4003.28s] English:** A function call is a function call, but when the optimizer is turned on, it may disappear.  
**Translation:** 

**[4010.48s] English:** The function call  
**Translation:** 

**[4011.36s] English:** It may inline, and so one of the things you can do is actually get code.  
**Translation:** Vocabulary: inline: 内联

**[4019.68s] English:** That is smaller than the function call because you eliminate the function preamble and  
**Translation:** 

**[4026.32s] English:** Return, and there's just the operation there. One of the key things when I did  
**Translation:** 

**[4034.56s] English:** Templates, I wanted to make sure that if you have a say a sorting algorithm and you give it a  
**Translation:** 

**[4042.32s] English:** Sorting Criteria  
**Translation:** Vocabulary: algorithm: 算法; criteria: 标准; sorting: 排序; templates: 模板

**[4046.08s] English:** If that sorting criterion is simply comparing things, the code generated should  
**Translation:** 

**[4053.20s] English:** Be the less-than not an indirect function call to a compression object, which is what it is.  
**Translation:** Vocabulary: compression: 压缩; criterion: 标准

**[4062.24s] English:** Is in the source code, but we really want to get down to the single instruction, um, but anyway, turn off.  
**Translation:** 

**[4071.36s] English:** The optimizer, and you can debug it at the first level of debugging.  
**Translation:** Vocabulary: optimizer: 优化器

**[4076.16s] English:** Can be done, and I always do it without the optimization on.  
**Translation:** 

**[4079.76s] English:** It  
**Translation:** Vocabulary: optimization: 优化

**[4079.84s] English:** So,  
**Translation:** 

**[4080.00s] English:** Then I can see what's going on, and then there's this idea of concepts that puts some  
**Translation:** 

**[4088.40s] English:** Okay.  
**Translation:** 

**[4088.96s] English:** Now, I've never even known if it was ever available in any form, but it puts some.  
**Translation:** 

**[4095.92s] English:** So,  
**Translation:** 

**[4096.08s] English:** Constraints on the stuff you can parameterize essentially, uh, let me try and explain, yes.  
**Translation:** Vocabulary: constraints: 限制; parameterize: 参数化

**[4099.92s] English:** Okay.  
**Translation:** 

**[4101.92s] English:** So,  
**Translation:** 

**[4101.92s] English:** Um, so yes, it wasn't there 10 years ago. We have had versions of it that actually work.  
**Translation:** 

**[4103.92s] English:** So,  
**Translation:** 

**[4104.00s] English:** So,  
**Translation:** 

**[4108.08s] English:** So,  
**Translation:** 

**[4108.16s] English:** So,  
**Translation:** 

**[4108.56s] English:** So,  
**Translation:** 

**[4112.24s] English:** For the last four or five years, it was a design by Gabby, Drew Sutton, and me.  
**Translation:** 

**[4120.96s] English:** We were professors and postdocs in Texas at the time, and  
**Translation:** Vocabulary: postdocs: 博士后; texas: 德克萨斯州

**[4127.68s] English:** The implementation by Andrew Sutton has been available for  
**Translation:** 

**[4132.48s] English:** That time, and it is part of C++20. There's a standard library that uses it, so this.  
**Translation:** Vocabulary: implementation: 实现; sutton: 斯图顿

**[4143.12s] English:** It is becoming really, really real. It's available in Clang and GCC. GCC has had it for a couple of years.  
**Translation:** 

**[4153.92s] English:** And I believe Microsoft is soon going to do it. We expect all of C++20 to be available.  
**Translation:** Vocabulary: clang: LLVM编译器

**[4160.00s] English:** So, in all the major  
**Translation:** 

**[4161.92s] English:** Compilers in 20 years, but this kind of stuff is available now. I'm just saying that because.  
**Translation:** Vocabulary: compilers: 编译器

**[4170.88s] English:** Otherwise, people might think I was talking about science fiction.  
**Translation:** 

**[4174.72s] English:** And so, what I'm going to say is really concrete; you can run it today.  
**Translation:** 

**[4179.84s] English:** And there are production uses of it, so the basic idea is that when you have a generic component,...  
**Translation:** 

**[4190.16s] English:** Like a sort function.  
**Translation:** Vocabulary: generic: 通用的

**[4191.92s] English:** The `sort` function will require at least two parameters: one, a data structure with a given type.  
**Translation:** 

**[4200.00s] English:** Type, and a comparison criterion.  
**Translation:** Vocabulary: criterion: 标准

**[4204.96s] English:** And these things are related, but obviously, you can't compare them if you don't know  
**Translation:** 

**[4209.56s] English:** What are the types of things you compare?  
**Translation:** 

**[4213.88s] English:** And so you want to be able to say, "I'm going to sort something," and it is to be sortable.  
**Translation:** 

**[4220.70s] English:** What does it mean to be sortable?  
**Translation:** Vocabulary: sortable: 可排序的

**[4222.02s] English:** You look it up in the standard.  
**Translation:** 

**[4223.56s] English:** It has to be a sequence with a beginning and an end.  
**Translation:** 

**[4228.06s] English:** There has to be random access to that sequence, and the element types have to be comparable.  
**Translation:** 

**[4237.14s] English:** By default.  
**Translation:** 

**[4238.14s] English:** Which means the less-than operator can operate on them.  
**Translation:** 

**[4241.06s] English:** Yes.  
**Translation:** 

**[4242.06s] English:** Less-than logical operator can operate on them.  
**Translation:** 

**[4243.34s] English:** Basically, what concepts are, they're compile-time predicates.  
**Translation:** Vocabulary: predicates: 断言

**[4247.50s] English:** They're predicates you can ask: "Are you a sequence?  
**Translation:** 

**[4250.82s] English:** Yes.  
**Translation:** 

**[4251.82s] English:** I have a beginning and an end.  
**Translation:** 

**[4254.12s] English:** Are you a random-access sequence?  
**Translation:** 

**[4256.22s] English:** Yes.  
**Translation:** 

**[4257.22s] English:** I have subscripting and plus.  
**Translation:** 

**[4261.32s] English:** Is your element type something that has a <less than>?  
**Translation:** 

**[4264.04s] English:** Yes.  
**Translation:** 

**[4265.04s] English:** I have a less-than.  
**Translation:** 

**[4267.54s] English:** So, basically, that's the system.  
**Translation:** 

**[4269.78s] English:** And so instead of saying, "I will take a parameter of any type," it'll say, "I'll take something.  
**Translation:** 

**[4274.60s] English:** That's sortable.  
**Translation:** Vocabulary: parameter: 参数

**[4277.36s] English:** And it's well-defined.  
**Translation:** 

**[4279.04s] English:** And so you say, okay, you can sort with less than.  
**Translation:** 

**[4281.92s] English:** I don't want less than.  
**Translation:** 

**[4283.22s] English:** I want something greater than, or something I invent.  
**Translation:** 

**[4285.84s] English:** So, you have two parameters.  
**Translation:** 

**[4287.02s] English:** There's the sortable thing, and the comparison criteria.  
**Translation:** Vocabulary: criteria: 标准

**[4291.80s] English:** And the comparison criteria will say: "Well, it should operate...  
**Translation:** 

**[4299.64s] English:** On the element type, and it has the comparison operations.  
**Translation:** 

**[4305.92s] English:** So, that's simply the fundamental thing.  
**Translation:** 

**[4308.84s] English:** It's compile-time predicates.  
**Translation:** 

**[4310.38s] English:** Do you have the properties I need?  
**Translation:** 

**[4312.74s] English:** So, it specifies the requirements for the code on the element.  
**Translation:** Vocabulary: specifies: 规定

**[4316.84s] English:** The parameters that it gets.  
**Translation:** 

**[4320.00s] English:** Very similar to types, actually, but operating in the space of concepts. The word "concept" was  
**Translation:** 

**[4331.52s] English:** Used by Alex Stefanov, who is sort of the father of generic programming in the context of C++.)  
**Translation:** 

**[4340.00s] English:** There are other places that use that word, but the way we call it "generic programming" is Alex's.  
**Translation:** Vocabulary: generic: 泛型

**[4346.08s] English:** And he called them concepts because he said they're the sort of fundamental.  
**Translation:** 

**[4350.32s] English:** Concepts of an area, so they should be called concepts, and we've had concepts all the time.  
**Translation:** 

**[4356.48s] English:** If you look at the KnR book, about C, it has arithmetic types and it has  
**Translation:** 

**[4365.76s] English:** Integral types, it says so in the book, and then it lists what they are; they have certain  
**Translation:** Vocabulary: arithmetic: 运算; integral: 整数的

**[4372.48s] English:** Properties: The difference today is that we can actually write.  
**Translation:** 

**[4376.08s] English:** A concept that will ask: Are you an integral type? Do you have the properties necessary to be an...  
**Translation:** 

**[4384.08s] English:** Integral: type, do you have plus, minus, divide, and such? So, uh, maybe the story of concepts.  
**Translation:** 

**[4393.92s] English:** Because I thought it might be part of C++11, but it was COX or something like that at the time.  
**Translation:** 

**[4403.76s] English:** What was the reason? Why didn't it happen like that?  
**Translation:** 

**[4406.08s] English:** What we'll talk a little bit about this fascinating process of standards, because I think  
**Translation:** 

**[4411.12s] English:** It's really interesting for people, it's interesting for me, but why did it take so long? What shapes did  
**Translation:** 

**[4418.24s] English:** The idea of concepts: Take what were the challenges back in 1987, or thereabouts.  
**Translation:** Vocabulary: thereabouts: 左右

**[4431.20s] English:** When I was designing templates, obviously I wanted to express the notion,  
**Translation:** 

**[4436.08s] English:** Of what is required by a template for its argument.  
**Translation:** Vocabulary: template: 模版; templates: 模版

**[4440.00s] English:** And so I looked at this, and basically, for templates, I wanted three properties.  
**Translation:** 

**[4446.28s] English:** I wanted to be very flexible; it had to be able to express things I couldn't imagine.  
**Translation:** Vocabulary: flexible: 有弹性

**[4455.34s] English:** Because I know I can't imagine everything, and I've been suffering from languages that try to.  
**Translation:** 

**[4461.84s] English:** Constrain you to only do what the designer thought was good; didn't want to do that. Secondly, it  
**Translation:** Vocabulary: constrain: 限制

**[4469.94s] English:** Had to run faster, as fast or faster than handwritten code. So, basically, if I have a vector,...  
**Translation:** 

**[4476.88s] English:** Of T, and I, take a vector of chars; it should run as fast as you build a vector of chars yourself.  
**Translation:** Vocabulary: chars: 字符; handwritten: 手工编写的

**[4484.84s] English:** Without parameterization, and secondly, I wanted to be able to express the constraints of  
**Translation:** 

**[4496.70s] English:** Of the arguments, there should be proper type checking of the  
**Translation:** Vocabulary: constraints: 限制; parameterization: 参数化

**[4499.80s] English:** Interpositions.  
**Translation:** 

**[4499.94s] English:** Interfaces, and neither I nor anybody else at the time knew how to get all three.  
**Translation:** Vocabulary: interfaces: 接口

**[4508.08s] English:** And I thought for C++, I must have the two first, otherwise it's not C++.  
**Translation:** 

**[4515.22s] English:** And it bothered me for another couple of decades that I couldn't solve the third one.  
**Translation:** Vocabulary: bothered: 烦扰

**[4519.50s] English:** I mean, I was the one who put function argument type checking into C. I know the value of.  
**Translation:** 

**[4526.92s] English:** Good interfaces.  
**Translation:** 

**[4528.00s] English:** I didn't invent that idea; it's very common, but I did it.  
**Translation:** 

**[4533.02s] English:** And I wanted to do the same for templates, of course, but I couldn't.  
**Translation:** Vocabulary: templates: 模版

**[4537.84s] English:** So, it bothered me.  
**Translation:** 

**[4539.74s] English:** Then we tried again in 2002 and 2003, and I started analyzing the problem and explaining possible solutions.  
**Translation:** 

**[4551.52s] English:** Solutions.  
**Translation:** 

**[4552.52s] English:** It was not a complete design.  
**Translation:** 

**[4554.04s] English:** A group at the University of Indiana.  
**Translation:** 

**[4558.00s] English:** An old friend of mine.  
**Translation:** 

**[4560.00s] English:** They started a project at Indiana, and we thought we could get a good system of concepts in another two or three years that would have made C++ 11 better than C++ 06 or 07.  
**Translation:** 

**[4584.54s] English:** Well, it turns out that I think we got a lot of the fundamental ideas wrong.  
**Translation:** 

**[4593.02s] English:** They were too conventional.  
**Translation:** 

**[4596.04s] English:** They didn't quite fit C++ in my opinion.  
**Translation:** Vocabulary: conventional: 墨守成规的

**[4599.36s] English:** It didn't serve implicit conversions very well.  
**Translation:** 

**[4602.46s] English:** It didn't serve mixed-type arithmetic or mixed-type computations very well.  
**Translation:** 

**[4609.72s] English:** A lot of stuff came out of the function.  
**Translation:** 

**[4612.60s] English:** There was no community, and that community didn't deal with multiple types in the same way as C++, had more constraints on what you could express, and didn't have the draconian performance requirements.  
**Translation:** Vocabulary: constraints: 限制; draconian: 苛刻的

**[4636.14s] English:** And basically, we tried.  
**Translation:** 

**[4638.10s] English:** We tried very hard.  
**Translation:** 

**[4639.20s] English:** We had some successes.  
**Translation:** 

**[4641.48s] English:** But it just...  
**Translation:** 

**[4642.60s] English:** In the end, it wasn't....  
**Translation:** 

**[4645.66s] English:** Didn't compile fast enough, was too hard to use, and didn't run fast enough unless you had optimizers that were beyond the state of the art.  
**Translation:** Vocabulary: compile: 编译; optimizers: 优化器

**[4659.68s] English:** They still are.  
**Translation:** 

**[4660.78s] English:** So, we had to do something else.  
**Translation:** 

**[4662.72s] English:** Basically, it was the idea that a set of parameters defines a set of operations, and you go through it.  
**Translation:** 

**[4672.60s] English:** And then, you try to optimize it by putting an indirection table, just like for virtual functions.  
**Translation:** Vocabulary: optimize: 优化

**[4675.96s] English:** And then you try to optimize the indirection away, or a set of parameters.  
**Translation:** 

**[4680.00s] English:** To get performance,  
**Translation:** 

**[4682.16s] English:** And we just couldn't do all of that.  
**Translation:** 

**[4686.10s] English:** But get back to standardization.  
**Translation:** Vocabulary: standardization: 标准化

**[4688.58s] English:** We are standardizing C++ under ISO rules.  
**Translation:** 

**[4693.22s] English:** Which are very open processes.  
**Translation:** Vocabulary: standardizing: 制定标准

**[4695.60s] English:** People come in; there are no requirements.  
**Translation:** 

**[4697.52s] English:** For education or experience.  
**Translation:** 

**[4700.86s] English:** So, you've started to develop C++.  
**Translation:** 

**[4703.02s] English:** And there's a whole...  
**Translation:** 

**[4707.28s] English:** What was the first standard established?  
**Translation:** 

**[4709.04s] English:** What is that like?  
**Translation:** 

**[4710.68s] English:** The ISO standard: Is there a committee?  
**Translation:** 

**[4713.46s] English:** That you're referring to?  
**Translation:** 

**[4714.78s] English:** There's a group of people.  
**Translation:** 

**[4716.06s] English:** What's that like?  
**Translation:** 

**[4717.54s] English:** How often do you meet?  
**Translation:** 

**[4719.06s] English:** What's the discussion about?  
**Translation:** 

**[4719.76s] English:** I'll try and explain that.  
**Translation:** 

**[4722.04s] English:** So, sometime in early 1989,  
**Translation:** 

**[4727.82s] English:** Two people: one from IBM, one from HP.  
**Translation:** 

**[4732.92s] English:** Turned up in my office and told me  
**Translation:** 

**[4735.86s] English:** I would like to standardize C++.  
**Translation:** 

**[4739.04s] English:** This was a new idea to me, and I pointed it out.  
**Translation:** Vocabulary: standardize: 使标准化

**[4744.20s] English:** That it wasn't finished yet.  
**Translation:** 

**[4747.16s] English:** It wasn't ready for formal standardization and such.  
**Translation:** 

**[4750.54s] English:** And they say, "No, Bjarne, you haven't gotten it.  
**Translation:** 

**[4752.92s] English:** You really want to do this.  
**Translation:** 

**[4756.22s] English:** Our organizations depend on C++.  
**Translation:** 

**[4758.90s] English:** We cannot depend on something that's owned.  
**Translation:** 

**[4763.24s] English:** By another corporation, which might be a competitor.  
**Translation:** 

**[4766.80s] English:** Of course, we could rely on you.  
**Translation:** 

**[4769.04s] English:** But you might get run over by a bus.  
**Translation:** 

**[4772.26s] English:** Right, the old boss.  
**Translation:** 

**[4773.84s] English:** We really need to get this out in the open.  
**Translation:** 

**[4776.46s] English:** It has to be standardized under formal rules.  
**Translation:** Vocabulary: standardized: 规范化

**[4782.02s] English:** And we are going to standardize it under ISO rules.  
**Translation:** 

**[4788.78s] English:** And you really want to be part of it?  
**Translation:** 

**[4790.70s] English:** Because, basically, otherwise we'll have to do it ourselves.  
**Translation:** 

**[4794.54s] English:** And we know you can do it better.  
**Translation:** 

**[4796.42s] English:** Yeah.  
**Translation:** 

**[4797.16s] English:** So, through...  
**Translation:** 

**[4799.04s] English:** Through C++.  
**Translation:** 

**[4800.00s] English:** A combination of arm-twisting and flattery got started.  
**Translation:** Vocabulary: flattery: 奉承

**[4805.54s] English:** So, in late 1989, there was a meeting in D.C., but actually, it was not ISO then.  
**Translation:** 

**[4817.74s] English:** It was ANSI, the American National Standards Institute, doing that.  
**Translation:** 

**[4822.88s] English:** We met there, and we were lectured on the rules of how to do an ANSI standard.  
**Translation:** 

**[4828.34s] English:** There were about 25 of us there, which apparently was a new record for that kind of meeting.  
**Translation:** 

**[4835.82s] English:** And some of the old C guys who had been standardized in C were there, so we got some expertise in.  
**Translation:** 

**[4843.04s] English:** So, the way this works is that it's an open process.  
**Translation:** 

**[4846.94s] English:** Anybody can sign up if they pay the minimal fee, which is about $1,000.  
**Translation:** 

**[4853.34s] English:** There was less than before, but it's a little bit more now.  
**Translation:** Vocabulary: minimal: 最低的

**[4855.88s] English:** And I think it's $1,200.  
**Translation:** 

**[4858.34s] English:** It's not going to kill you.  
**Translation:** 

**[4861.82s] English:** And we have three meetings a year.  
**Translation:** 

**[4866.06s] English:** This is fairly standard.  
**Translation:** 

**[4868.16s] English:** We tried two meetings a year for a couple of years, but that didn't work too well.  
**Translation:** 

**[4873.38s] English:** So, three one-week meetings a year.  
**Translation:** 

**[4878.72s] English:** And you meet, and you have technical discussions.  
**Translation:** 

**[4884.10s] English:** And then you bring proposals forward for votes.  
**Translation:** 

**[4888.74s] English:** The votes are done: one person per, one vote per organization.  
**Translation:** 

**[4895.80s] English:** So, you can't have IBM come in with 10 people and dominate things—that's not allowed.  
**Translation:** Vocabulary: dominate: 控制局面

**[4902.74s] English:** And these are organizations that extend to the UC++.  
**Translation:** 

**[4906.10s] English:** Yes.  
**Translation:** 

**[4907.10s] English:** Or, individuals.  
**Translation:** 

**[4908.96s] English:** Or, individuals.  
**Translation:** 

**[4909.60s] English:** I mean, it's a bunch of people in a room deciding the design of a language.  
**Translation:** 

**[4915.90s] English:** Based on which, a lot of the world doesn't support.  
**Translation:** 

**[4917.90s] English:** Then it's C++, one person per organization.  
**Translation:** 

**[4918.02s] English:** Yes.  
**Translation:** 

**[4918.18s] English:** Or individuals, yes.  
**Translation:** 

**[4918.28s] English:** Or, individuals.  
**Translation:** 

**[4918.34s] English:** Systems run.  
**Translation:** 

**[4920.00s] English:** That's right. Well, I think most people would agree it's better than if I decided it, or better than if a single organization like AT&T decided it.  
**Translation:** 

**[4932.04s] English:** I don't know if everyone agrees with that, by the way. Bureaucracies have their critics, too.  
**Translation:** 

**[4937.20s] English:** Yes. Look, standardization is not pleasant. It's horrifying.  
**Translation:** 

**[4945.86s] English:** It's like democracy.  
**Translation:** 

**[4947.14s] English:** Exactly. As Churchill says, "democracy is the worst form of government except for all those that have been tried," and I would say the same applies to formal standardization.  
**Translation:** Vocabulary: churchill: 丘吉尔; standardization: 标准化

**[4956.86s] English:** But anyway, so we meet and we have these votes, and that determines what the standard is.  
**Translation:** 

**[4965.76s] English:** A couple of years later....  
**Translation:** 

**[4967.20s] English:** We extended this so it became worldwide. We have standard organizations that are active in currently 15 to 20 countries, and another 15 to 20 are sort of looking into and voting on the rest of the work.  
**Translation:** 

**[4991.64s] English:** And we meet three times a year. Next week, I'll be in Cologne, Germany.  
**Translation:** Vocabulary: cologne: 科隆

**[4997.20s] English:** We'll be spending a week doing standardization, and we'll vote on the committee draft (or C++20), which goes to the National Standards Committees for comments and requests for changes and improvements.  
**Translation:** 

**[5015.20s] English:** Then we do that, and there's a second set of votes, where hopefully everybody votes in favor.  
**Translation:** 

**[5021.30s] English:** This has happened several times.  
**Translation:** 

**[5023.74s] English:** The first time we finished, we started in the first round.  
**Translation:** 

**[5025.88s] English:** The first time we finished, we started in the first round.  
**Translation:** 

**[5026.66s] English:** The first time we finished, we started in the first round.  
**Translation:** 

**[5027.00s] English:** The first time we finished, we started in the first round.  
**Translation:** 

**[5027.20s] English:** The first technical meeting was in 1990.  
**Translation:** 

**[5031.68s] English:** The last one was in 1898.  
**Translation:** 

**[5033.86s] English:** We voted it out.  
**Translation:** 

**[5034.92s] English:** That was the standard that people used until 11, or a little bit past 11.  
**Translation:** 

**[5040.00s] English:** Um, and it was an international standard; all the countries voted in favor.  
**Translation:** 

**[5047.68s] English:** It took longer with 11, and I'll mention why, but all the nations voted in favor.  
**Translation:** 

**[5055.04s] English:** And we work on the basis of consensus—that is, we do not want something that passes 60/40.  
**Translation:** Vocabulary: consensus: 一致意见

**[5063.44s] English:** Uh, because then we're going to get dialects, and opponents, and people complain too much—they all  
**Translation:** 

**[5070.40s] English:** Complain too much, but basically, it has no real effect; the standards have been obeyed.  
**Translation:** Vocabulary: dialects: 方言; obeyed: 遵守; opponents: 反对者

**[5077.52s] English:** Been working to make it easier to use with many compilers, many computers, and all of that kind.  
**Translation:** 

**[5084.80s] English:** Of stuff, and so the first thing is that traditionally, with ISO standards, it took 10 years.  
**Translation:** Vocabulary: compilers: 编译器

**[5092.48s] English:** We did the first one.  
**Translation:** 

**[5093.44s] English:** And eight brilliant! We thought we were going to do the next one in six months, because now we're good.  
**Translation:** 

**[5099.52s] English:** At it, right? It took 13. Yeah, it was uh-named O-X. They hoped that you would at least...  
**Translation:** 

**[5110.00s] English:** I got it within the single-digit odds. I thought we would get there, but I thought  
**Translation:** 

**[5115.52s] English:** Would get six, seven, or eight— the confidence of youth, yes, right? Well, the point is that this was.  
**Translation:** 

**[5122.00s] English:** Sort of like a second.  
**Translation:** 

**[5123.44s] English:** Um, we now know how to do it, and so we're going to do it much better.  
**Translation:** 

**[5129.20s] English:** And we got more ambitious, and it took longer. Furthermore, there is this.  
**Translation:** 

**[5135.04s] English:** Tendency, because it's a 10-year cycle, or age doesn't matter.  
**Translation:** 

**[5142.72s] English:** Just before you're about to ship, somebody has a bright idea.  
**Translation:** 

**[5149.20s] English:** Yeah, and so we really must  
**Translation:** 

**[5151.68s] English:** We got that in, and we did that successfully with the STR. Yeah, we got it done.  
**Translation:** 

**[5160.00s] English:** The standard library that gives us all the STL stuff—that, I basically think, saved C++.  
**Translation:** 

**[5166.72s] English:** Plus, it was beautiful, yes. And then people tried it with other things, and it didn't work.  
**Translation:** 

**[5173.20s] English:** So, well, they got things in, but it wasn't as dramatic, and it took longer and longer and longer.  
**Translation:** 

**[5178.80s] English:** So, after C++11, which was a huge improvement, and what basically made it possible for most  
**Translation:** 

**[5187.32s] English:** People are using "today, we decided never again," and so, how do you avoid those slips?  
**Translation:** 

**[5195.80s] English:** And the answer is that you ship more often, so that if you have a slip or mistake, it doesn't impact as much.  
**Translation:** 

**[5203.44s] English:** On the 10-year cycle, by the time you know it's a slip, there are 11 years till you get it.  
**Translation:** 

**[5209.62s] English:** Yeah, now with a three-year cycle, there is about three to four years till you get it.  
**Translation:** 

**[5217.04s] English:** Right.  
**Translation:** 

**[5217.30s] English:** The delay between feature freeze and shipping is so you always get one or two years more.  
**Translation:** 

**[5225.02s] English:** And so, we shipped 14 on time, we shipped 17 on time, and we will ship 20 on time.  
**Translation:** 

**[5235.60s] English:** It will happen, and furthermore, this allows a predictability that gives implementers confidence.  
**Translation:** Vocabulary: implementers: 实施者

**[5244.26s] English:** The compiler implementers, the library implementers.  
**Translation:** 

**[5247.30s] English:** To they have a target and they deliver on it, it took two years before most compilers were good enough.  
**Translation:** Vocabulary: compilers: 编译器

**[5255.98s] English:** Most compilers were actually getting pretty good by 2014, and everyone shipped in 2017, well, we...  
**Translation:** 

**[5266.72s] English:** We are going to have at least almost everybody ship almost everything in 20, and I know this because  
**Translation:** 

**[5274.62s] English:** They're shipping in 19.  
**Translation:** 

**[5277.30s] English:** Predictability is good; delivery on time.  
**Translation:** 

**[5280.00s] English:** Is good, and so yeah, that's great. So, that's how it works. There are a lot of features that came in.  
**Translation:** 

**[5287.62s] English:** In C++11, there are lots of features at the birth of C++ that were amazing and ideas with concepts.  
**Translation:** 

**[5296.20s] English:** In 2020, what do you consider the most just and beautiful thing, just to you personally?  
**Translation:** 

**[5305.90s] English:** Just sit back and think, "Wow, that's just a nice and clean feature of C++.  
**Translation:** 

**[5315.32s] English:** I have written two papers for the History of Programming Languages conference, which basically  
**Translation:** 

**[5324.08s] English:** Asked me such questions, and I'm writing a third one which I will deliver at the history of...  
**Translation:** 

**[5330.98s] English:** Programming languages conference in London next year, so I've been thinking about that.  
**Translation:** 

**[5335.80s] English:** You.  
**Translation:** 

**[5335.88s] English:** There is one clear answer: constructors and destructors. The way a constructor can establish  
**Translation:** 

**[5343.32s] English:** The environment for the use of an object of a certain type and the destructor that cleans up anything  
**Translation:** Vocabulary: constructor: 构造函数; constructors: 构造函数; destructor: 析构函数; destructors: 析构函数

**[5350.52s] English:** Messes at the end of it—that is the key to C++. That's why we don't have to use garbage collection.  
**Translation:** 

**[5357.16s] English:** Connection: that's how we can get predictable performance. That's how you can get the minimal.  
**Translation:** Vocabulary: messes: 混乱; minimal: 最小化; predictable: 可预测的

**[5364.60s] English:** Overhead, in many cases, is really minimal, and it's the idea of a constructive destructor.  
**Translation:** 

**[5373.40s] English:** Pairs sometimes it comes out under the name, or I.A.R.A. (Resource Acquisition Initialization).  
**Translation:** Vocabulary: acquisition: 资源获取; initialization: 初始化

**[5382.44s] English:** Which is the idea that you grab resources, and the constructor, and release them, and the destructor.  
**Translation:** 

**[5388.52s] English:** It's also the best example of why I shouldn't be in advertising; I get the best ideas.  
**Translation:** 

**[5394.28s] English:** I call it a cleaner. There's always a camera. A full vorillion of categories — there's always one.  
**Translation:** 

**[5394.52s] English:** Camera, a full clinician, all of these things: see which one goes up, so I can leave my slides over.  
**Translation:** Vocabulary: clinician: 医生

**[5394.54s] English:** To you, no, but the infrastructure design; master, you have to go through here. You go through there's.  
**Translation:** 

**[5394.58s] English:** Call it "resource acquisition is initialization," not the  
**Translation:** 

**[5400.00s] English:** Naming I've ever heard, so it's types of abstraction. You said, I want to.  
**Translation:** 

**[5412.18s] English:** Create my own types; so, types are an essential part of C++, and making them is crucial.  
**Translation:** Vocabulary: abstraction: 抽象; crucial: 至关重要的

**[5417.66s] English:** Efficient is the key part, and if it is, this is almost getting there.  
**Translation:** 

**[5424.84s] English:** Philosophical, but the construction and the destruction, the creation of an  
**Translation:** Vocabulary: philosophical: 哲学性的

**[5430.34s] English:** An instance of a type and the freeing of resources from that instance of a type.  
**Translation:** 

**[5437.26s] English:** Is what defines the object, like birth and death, is what defines.  
**Translation:** 

**[5444.88s] English:** Human life, yeah, that's right. By the way, philosophy is important; you can't do  
**Translation:** 

**[5450.88s] English:** Good language design without philosophy.  
**Translation:** 

**[5454.66s] English:** Because you can't do good language design without philosophy, because you  
**Translation:** 

**[5454.82s] English:** Because what you are determining is what people can express, and how this is  
**Translation:** 

**[5459.64s] English:** Very important by the way; constructors and destructors came into C++ in 1979, in about  
**Translation:** 

**[5468.00s] English:** The second week of my work with what was then called See the Classes, it is a  
**Translation:** Vocabulary: constructors: 构造函数; destructors: 析构函数

**[5472.94s] English:** Fundamental idea next comes the fact that you need to control copying, because  
**Translation:** 

**[5479.66s] English:** Once you control, as you said, birth and death, you have to control taking.  
**Translation:** 

**[5484.64s] English:** Copies, which is another way of creating an object, and finally, you have to be.  
**Translation:** 

**[5490.58s] English:** Able to move things around, so you get the move operations, and that's the set.  
**Translation:** 

**[5496.16s] English:** Of key operations you can define on a C++ type, and so to you, those things are  
**Translation:** 

**[5504.98s] English:** Just a beautiful part of C++ that is at the core of it all, yes. You mentioned  
**Translation:** 

**[5513.50s] English:** That you hope there will be  
**Translation:** 

**[5514.46s] English:** One unified set of guidelines in the future for how to construct the  
**Translation:** Vocabulary: guidelines: 准则

**[5518.66s] English:** Programming language  
**Translation:** 

**[5520.00s] English:** So, perhaps not just one programming language, but a unification of how we build programming languages.  
**Translation:** Vocabulary: unification: 统一

**[5528.40s] English:** If you remember such statements, I have some trouble remembering it, but I know the origin.  
**Translation:** 

**[5533.76s] English:** Of that idea, so maybe you can talk about how C++ has been improving; there's been  
**Translation:** 

**[5539.12s] English:** A lot of programming languages, do you know where the arc of history is taking us? Do you hope that?  
**Translation:** 

**[5544.88s] English:** There is a unified understanding about the languages with which we communicate in the digital space.  
**Translation:** 

**[5552.56s] English:** Well, I think that languages should be designed not by clobbering language features together and  
**Translation:** 

**[5563.44s] English:** Doing slightly different versions of somebody else's ideas, but through the creation of a set,...  
**Translation:** Vocabulary: clobbering: 胡乱拼凑

**[5571.12s] English:** Of principles and rules of thought.  
**Translation:** 

**[5574.88s] English:** And we're trying to teach people in the standards committee about these rules because a lot of people  
**Translation:** 

**[5582.56s] English:** Come in and say, "I've got a great idea. Let's put it in the language," and then you have to ask why.  
**Translation:** 

**[5588.88s] English:** Does it fit in the language? Why does it fit in this language? It may fit in another language, and...  
**Translation:** 

**[5594.40s] English:** Not here, or it may fit here. Not the other language, so you have to work from a set of principles and  
**Translation:** 

**[5600.40s] English:** You have to develop a set of principles, and you have to develop a set of principles to make it work.  
**Translation:** 

**[5604.56s] English:** To develop that set of principles and  
**Translation:** 

**[5610.96s] English:** One example that I sometimes remember is that I was sitting down.  
**Translation:** 

**[5617.04s] English:** With some of the designers of Common Lisp, and we were talking about languages and language features.  
**Translation:** 

**[5625.52s] English:** And obviously, we didn't agree about anything because, well, this was not C++, and vice versa.  
**Translation:** Vocabulary: designers: 设计者; versa: 反之

**[5632.96s] English:** Vera, it's too many parentheses.  
**Translation:** 

**[5634.56s] English:** But suddenly, we started making progress.  
**Translation:** Vocabulary: parentheses: 圆括号

**[5640.00s] English:** I said, "I had this problem, and I developed it according to these ideas.  
**Translation:** 

**[5646.66s] English:** And they said, "Why?  
**Translation:** 

**[5647.52s] English:** We had that problem, a different problem, and we developed it with the same kind of principles.  
**Translation:** 

**[5653.40s] English:** And so we worked through large chunks of C++ and large chunks of Common Lisp.  
**Translation:** Vocabulary: chunks: 部分

**[5661.02s] English:** And we figured out that we actually had similar sets of principles of how to do it.  
**Translation:** 

**[5667.88s] English:** But the constraints on our designs were very different, and the aims for its usage were very different.  
**Translation:** Vocabulary: constraints: 限制条件

**[5676.06s] English:** But there was commonality in the way you reason about language features.  
**Translation:** 

**[5682.62s] English:** And the fundamental principles you are trying to uphold.  
**Translation:** 

**[5686.54s] English:** So, do you think that's possible?  
**Translation:** 

**[5687.74s] English:** So, just like there is perhaps a unified theory of physics for the fundamental forces of physics,...  
**Translation:** 

**[5697.30s] English:** And...  
**Translation:** 

**[5697.88s] English:** I'm sure there are commonalities among the languages,  
**Translation:** 

**[5702.42s] English:** But there are also people involved who help drive the development of these languages.  
**Translation:** 

**[5707.64s] English:** Do you have any hope or optimism that there will be a unification?  
**Translation:** Vocabulary: optimism: 乐观; unification: 统一

**[5715.02s] English:** If you think about physics and Einstein in simpler language, do you think that's possible?  
**Translation:** 

**[5724.10s] English:** Let's remember some modern physics.  
**Translation:** Vocabulary: einstein: 爱因斯坦

**[5727.30s] English:** Modern physics, I think, started with Galileo in the 1600s, so they've had 700 years to get going.  
**Translation:** 

**[5735.34s] English:** Modern computing started in about 1846.  
**Translation:** Vocabulary: computing: 计算; galileo: 伽利略

**[5740.42s] English:** We've got about 70 years.  
**Translation:** 

**[5743.92s] English:** They have 10 times.  
**Translation:** 

**[5746.24s] English:** Yeah.  
**Translation:** 

**[5746.40s] English:** And furthermore, they're not as bothered by people using physics the way we are worried about how programming is done by humans.  
**Translation:** Vocabulary: bothered: 在意

**[5756.54s] English:** And furthermore, they're not as bothered by people using physics the way we are worried about how programming is done by humans.  
**Translation:** 

**[5756.98s] English:** So, each has...  
**Translation:** 

**[5760.00s] English:** Problems and constraints that others have, but we are very immature compared to.  
**Translation:** 

**[5764.30s] English:** Physics, so I would look at the philosophical level and see if there are any relevant concepts.  
**Translation:** Vocabulary: constraints: 限制; immature: 不成熟; philosophical: 哲学的

**[5772.76s] English:** Fundamental principles, like "you don't leak resources" — you shouldn't.  
**Translation:** 

**[5780.96s] English:** Take errors at runtime that you don't need to, you don't violate some kind of.  
**Translation:** Vocabulary: runtime: 运行时; violate: 违反

**[5789.78s] English:** Type systems: there are many kinds of type systems, but when you have one, you don't  
**Translation:** 

**[5793.76s] English:** Break it down, etc., etc. There will be quite a few, and it won't be the same for everyone.  
**Translation:** 

**[5802.28s] English:** All languages, but I think we, if we step back to some kind of philosophical level,  
**Translation:** 

**[5808.08s] English:** We could agree on sets of principles that applied to sets of  
**Translation:** 

**[5815.34s] English:** Problem areas, and within,  
**Translation:** 

**[5818.18s] English:** You.  
**Translation:** 

**[5819.78s] English:** An area of use, like in C++, this case, what used to be called "systems.  
**Translation:** 

**[5826.78s] English:** Programming the area between the hardware and the fluffier parts.  
**Translation:** Vocabulary: fluffier: 较轻盈的部分

**[5832.54s] English:** Of the system, you might very well see a convergence. So these days, you see,...  
**Translation:** 

**[5838.48s] English:** Rust has adopted RAII, and sometimes accuse me of having borrowed it in 20.  
**Translation:** Vocabulary: convergence: 趋同

**[5845.34s] English:** Years before they discovered it, but it's  
**Translation:** 

**[5849.78s] English:** Not anything wrong with that.  
**Translation:** 

**[5852.62s] English:** It's just not getting there. Then, if you take a closer look, uh-oh.  
**Translation:** 

**[5854.90s] English:** When you do that again, like your last time, I won't let you get away with it.  
**Translation:** 

**[5869.06s] English:** By the fixed state or juice, s  
**Translation:** 

**[5876.54s] English:** But I think we have to step back to the philosophical when you say it.  
**Translation:** Vocabulary: philosophical: 哲学的

**[5878.66s] English:** To the philosophical level,  
**Translation:** 

**[5880.00s] English:** Agree on principles, and then we'll see some convergences; and it will be  
**Translation:** Vocabulary: convergences: 汇合点

**[5888.32s] English:** Application domain-specific, so a crazy question, but I work a lot with machine learning with deep  
**Translation:** 

**[5896.80s] English:** Learning; I'm not sure if you touch that world much, but you could think of programming as a  
**Translation:** 

**[5904.08s] English:** The thing that takes some input in programming is the task of creating a program, and a program takes  
**Translation:** 

**[5909.52s] English:** Some input and produces some output, so machine learning systems train on data in order to be  
**Translation:** 

**[5917.60s] English:** Able to take an input and produce output, but they're messy, fuzzy things, much like...  
**Translation:** 

**[5926.32s] English:** We, as children, grow up, you know, taking in some input and making some output, but we're noisy.  
**Translation:** 

**[5932.48s] English:** Mess up a lot; we're definitely not a reliable biological system, or a giant mess, so there's  
**Translation:** 

**[5939.36s] English:** A  
**Translation:** 

**[5939.52s] English:** Sense in which machine learning is a kind of way of programming, but just fuzzy; it's very, very, very.  
**Translation:** 

**[5947.04s] English:** Different than C++, because C++ is, as you said, extremely  
**Translation:** Vocabulary: fuzzy: 模糊的

**[5953.76s] English:** Reliable, it's efficient. It's, uh, you know, you can measure and test in batches.  
**Translation:** 

**[5959.60s] English:** Different ways with biological systems or machine learning systems, you can't say much except sort of.  
**Translation:** 

**[5967.52s] English:** Empirically, it can be said that 99.9 percent of machine learning systems are indeed machine learning systems.  
**Translation:** 

**[5969.36s] English:** You can say that 99.8 percent of the time it seems to work. Uh, what do you think about this fuzzy kind?  
**Translation:** Vocabulary: empirically: 根据经验

**[5975.84s] English:** Of programming, and do you even see it as programming? Is it solely and totally another kind?  
**Translation:** 

**[5982.40s] English:** Of the world, I think it's a different kind of world, and it is fussy. In my domain, I don't like it.  
**Translation:** Vocabulary: fussy: 挑剔的

**[5989.52s] English:** Fussiness that is, people say things like, "they want everybody to be able to program.  
**Translation:** 

**[5997.84s] English:** But I don't want everybody to be able to program.  
**Translation:** Vocabulary: fussiness: 琐碎要求

**[6000.00s] English:** Everybody should program my airplane controls or car controls.  
**Translation:** 

**[6008.20s] English:** I want that to be done by engineers.  
**Translation:** 

**[6010.68s] English:** I want that to be done with people who are specifically educated and trained.  
**Translation:** 

**[6015.88s] English:** For building things, and it is not for everybody.  
**Translation:** Vocabulary: educated: 受过教育的

**[6022.64s] English:** Similarly, a language like C++ is not for everyone.  
**Translation:** 

**[6026.08s] English:** It is designed to be a sharp and effective tool for  
**Translation:** 

**[6032.96s] English:** Professionals, basically, and definitely for people who aim at some kind of precision.  
**Translation:** 

**[6040.84s] English:** You don't have people doing calculations without understanding math, right?  
**Translation:** 

**[6046.84s] English:** Counting on your fingers is not going to cut it if you want to fly to the moon.  
**Translation:** 

**[6051.44s] English:** And  
**Translation:** 

**[6053.32s] English:** So, there are areas where  
**Translation:** 

**[6056.24s] English:** An 84% accuracy rate, 16% false positive rate is perfectly acceptable.  
**Translation:** 

**[6066.64s] English:** And where people will probably get no more than 70%.  
**Translation:** 

**[6070.80s] English:** You said 98%.  
**Translation:** 

**[6072.80s] English:** What I have seen is more like 84%.  
**Translation:** 

**[6076.48s] English:** And, by really a lot of blood, sweat, and tears, you can get up to 92 and a half.  
**Translation:** 

**[6081.72s] English:** Right.  
**Translation:** 

**[6082.52s] English:** So, this is fine if it is.  
**Translation:** 

**[6085.92s] English:** Say "pre-screening.  
**Translation:** 

**[6089.28s] English:** Stuff before the human looks at it.  
**Translation:** 

**[6092.52s] English:** It is not good enough for life-threatening situations.  
**Translation:** 

**[6097.36s] English:** And so, there are lots of areas where the fuzziness is perfectly acceptable and  
**Translation:** Vocabulary: fuzziness: 模糊性

**[6104.08s] English:** Good, and better than humans; cheaper than humans.  
**Translation:** 

**[6107.68s] English:** But it's not the kind of engineering stuff I'm mostly interested in.  
**Translation:** 

**[6112.72s] English:** I worry a bit about.  
**Translation:** 

**[6115.12s] English:** Machine learning in the context of cars.  
**Translation:** 

**[6118.44s] English:** You know much more about this than I do.  
**Translation:** 

**[6120.00s] English:** Do I worry too? But I'm, I'm, I'm sort of an amateur here; I've read some of the papers, but I've not.  
**Translation:** Vocabulary: amateur: 业余爱好者

**[6127.04s] English:** Ever done it, and the idea that scares me the most is one I've heard, and I don't know.  
**Translation:** 

**[6136.64s] English:** How common it is that you have this AI system, machine-learning all of these trained neural nets!  
**Translation:** Vocabulary: neural: 神经网络; scares: 令人害怕

**[6150.40s] English:** And when there's something that's too complicated, they ask the human for help.  
**Translation:** 

**[6157.28s] English:** But the human is reading a book or sleeping, and he has 30 seconds or three seconds to figure.  
**Translation:** 

**[6165.84s] English:** Figure out what the problem was that the AI system couldn't handle and do the right thing.  
**Translation:** 

**[6171.04s] English:** This is scary. I mean, how do you do the cut-over between the machine and the human?  
**Translation:** 

**[6178.72s] English:** Very, very  
**Translation:** 

**[6180.00s] English:** Difficult, and for the designer of one of the most reliable, efficient, and powerful programming languages.  
**Translation:** 

**[6187.84s] English:** Languages C++, I can understand why that world is actually unappealing; it is for most.  
**Translation:** 

**[6195.92s] English:** Engineers find it extremely appealing because we don't know how to get that interaction right.  
**Translation:** Vocabulary: appealing: 吸引人的; unappealing: 不吸引人的

**[6202.88s] English:** But I think it's possible, but it's very, very hard. It is, and now it's stating a problem, not yes, that.  
**Translation:** 

**[6210.56s] English:** I mean, I would much rather never rely on a human if you're driving a nuclear reactor, if you're  
**Translation:** 

**[6216.72s] English:** For an autonomous vehicle, it's much better to design systems written in C++.  
**Translation:** 

**[6221.60s] English:** Plus, don't ever ask a human for help; let's just get one fact in, yeah. All of this AI stuff is on top of...  
**Translation:** Vocabulary: autonomous: 独立操作的

**[6233.76s] English:** So, that's one reason I have to keep a weather eye out on what's going on in that field, but  
**Translation:** 

**[6240.00s] English:** I will never become an expert in that area, but it's a good example of how you separate.  
**Translation:** 

**[6245.76s] English:** Different areas of application, and you have to have different tools and principles.  
**Translation:** 

**[6251.84s] English:** Um, and then they interact. No major system is written in just one language today.  
**Translation:** 

**[6257.76s] English:** And there are good reasons for that when you look back at your life's work.  
**Translation:** 

**[6264.08s] English:** What is a moment, or an event, that you're really proud of? They say.  
**Translation:** 

**[6274.24s] English:** Damn, I did pretty good there. Is it as obvious as the creation of C++? It's obvious I've spent a lot.  
**Translation:** 

**[6282.96s] English:** Of time with C++, and there's a combination of a few good ideas, a lot of hard work, and a bit of  
**Translation:** 

**[6290.86s] English:** Luck, and I've tried to do a lot of work, and I've tried to do a lot of work, and I've tried to do a lot more.  
**Translation:** 

**[6294.06s] English:** To get away from it a few times, but I get dragged in again. Partly because I'm most effective in this.  
**Translation:** 

**[6299.98s] English:** Area, and partly because what I do has much more impact if I do it in the context of C++, I  
**Translation:** 

**[6309.10s] English:** I have four and a half million people who will pick it up tomorrow if I get something right; if I did.  
**Translation:** 

**[6314.94s] English:** It in another field, I would have to start learning again, then I have to build it, and then we'll see if.  
**Translation:** 

**[6319.26s] English:** Anybody wants to use it, one of the things that has kept me going for all of these years is one.  
**Translation:** 

**[6327.90s] English:** The good things that people do with it, and the interesting things they do with it, and also,...  
**Translation:** 

**[6336.46s] English:** I get to see a lot of interesting stuff and talk to a lot of interesting people.  
**Translation:** 

**[6343.42s] English:** I mean, if it has just been statements on paper or on a screen.  
**Translation:** 

**[6349.42s] English:** I don't think I could have kept going, but I get to see the telescopes up on  
**Translation:** Vocabulary: telescopes: 望远镜

**[6354.62s] English:** Monarchy, and I actually went and saw how Ford built cars.  
**Translation:** 

**[6360.00s] English:** I got to JPL and see how they do the Mars rovers.  
**Translation:** Vocabulary: monarchy: 君主制; rovers: 探测车

**[6367.10s] English:** There's so much cool stuff going on.  
**Translation:** 

**[6369.76s] English:** And most of the cool stuff is done by pretty nice people.  
**Translation:** 

**[6372.86s] English:** And sometimes in very nice places, such as Cambridge, Sofia, Antibes, and Silicon Valley.  
**Translation:** 

**[6383.70s] English:** There's more to it than just code.  
**Translation:** Vocabulary: antibes: 法国蔚蓝海岸地名; sofia: 索菲亚

**[6386.28s] English:** But code is central.  
**Translation:** 

**[6387.38s] English:** So, on top of the code, are the people in very nice places.  
**Translation:** 

**[6392.46s] English:** Well, I think I speak for millions of people.  
**Translation:** 

**[6395.88s] English:** We are in saying thank you for creating this language that so many systems are built upon, making a better world.  
**Translation:** 

**[6407.02s] English:** So, thank you.  
**Translation:** 

**[6408.00s] English:** And thank you for talking today.  
**Translation:** 

**[6409.36s] English:** Yeah, thanks.  
**Translation:** 

**[6410.40s] English:** And we'll make it even better.  
**Translation:** 

**[6412.06s] English:** Good.  
**Translation:** 

**[6417.38s] English:** Thank you.  
**Translation:** 


<!-- TRANSCRIPTION_COMPLETE -->
