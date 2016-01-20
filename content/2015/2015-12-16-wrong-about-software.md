Title: Misconceptions about research software
Date: 2015-12-16
Author: Daniel S. Standage
Category: blog
Tags: software; academics; credit

I stumbled across [the following question][quora] the other day in an email digest from Quora.

> I have 5 years of working experience, but I still code very slow.
> How can I code faster? What should I learn?

Most of the responses don't answer the question directly, but instead make the point that speed is a very poor metric by which to measure quality or productivity in software engineering.
Carefully designing, documenting, implementing, and testing code requires considerable time and resources upfront, but not nearly as much time and resources as is required in later stages to maintain or fix code that was written quickly and sloppily.

In this case, I think the [OP][op] fell into the trap of thinking that writing code is just about writing code.
In reality, code is just a projection of a programmer's conceptual model of something onto a representation that a computer can interpret and execute.
If your initial conceptual model is clear, your code will be clear and easy to write.
If your initial conceptual model is fuzzy, you'll probably end up taking the long way to a workable solution, leaving lots of crufty code in your wake.
Research software engineering is so much more than just "writing code".

In the ideal situation (i.e., with a clear and accurate mathematical model in hand, and with informed choices about which algorithms and data structures provide an efficient computational solution), writing the actual code is almost an afterthought.
Once the model is nailed down, the programmer has quite a bit of technical freedom when it comes to implementation and testing, but the precise details of implementation are of little interest compared to the results produced by the software.

In the real world, I get the impression that most programmers and programmer-scientists rarely achieve this ideal, and end up developing and refining their models *as they write the code*.
I think some of this has to do with lack of discipline, which each scientist has to address on a personal level.
I think it also has to do with lack of training, of which I think we could be doing much better job as a field.

But I think the notion (all too common in academics) that research software engineering is a technical exercise ("just writing code") rather than an intellectual one is particularly problematic.
It's problematic for those that create the software, who all too often jump head-first into *writing code* without having done the proper modeling and design upfront.
It's problematic for those in a position to supervise or evaluate or fund research, who all too often trivialize software because it's "just writing code".

A few months ago the bioinformatics twittersphere/blogosphere got caught up in a great discussion on the purpose of software in academic research.
I was able to dig through some old notes and find a link to [an excellent blog post][kaiblin] which provides links to lots of good reading on the topic.
I particularly like the analogy he made between experiments (design vs execution) and software (design vs implementation).

> Software development in science is often compared to conductiong [sic] experimental work, and because most people argue that experimental work is a means to an end, that is not a primary product of science.
> So, by analogy, neither should software development be.
> The actual *scientific* contribution is designing the experiment in the first place.
> Now, the analogy has one slight problem here, and I'm tempted to blame that problem on the pretty shoddy practices around software development in science, people have written about this before.
> Mainly, people seem to assume that **implementing** the software is all there is for software development.
> I humbly disagree.
> I would argue that the analogy with wet lab work would be that **designing experiments** is like **designing software**, and **conducting experiments** is like **implementing software**.
> Now if we follow the general agreement that designing experiments is a valuable intellectual input to the scientific endeavour, by analogy so should designing software.
> So, the answer the question I asked in the topic of the post "Is software development in science an intellectual contribution?" would be "Yes, parts of it at least".

I agree: the design of research software should be treated as a valid intellectual contribution in the academic science enterprise, and credit should be rendered accordingly.

[quora]: https://www.quora.com/I-have-5-years-of-working-experience-but-I-still-code-very-slow-How-can-I-code-faster-What-should-I-learn
[op]: http://meta.stackexchange.com/a/146514/151867
[kaiblin]: http://phdops.kblin.org/software-dev-intellectual-contribution.html