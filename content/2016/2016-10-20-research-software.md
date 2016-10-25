Title: Thoughts on research software from the PSRN workshop
Date: 2016-10-20 9:30
Author: Daniel S. Standage
Category: blog
Tags: software; science; cyberinfrastructure
Summary: In which I ramble on about experimental science, research software, and cyberinfrastructure engineering.

\*_In which I ramble on about experimental science, research software, and cyberinfrastructure engineering._\*

I'm on my way home from a workshop on cyberinfrastructure and postgraduate training hosted by the [Plant Science Research Network](http://bti.cornell.edu/news/plant-science-research-network-launches/).
I, like all the other participants, had some assigned prep work prior to the workshop, which got me thinking ([again]({filename}../2015/2015-12-16-wrong-about-software.md)) about research software.
The purpose of this post is to summarize my thoughts while they're fresh in my head.

*To be clear, the contents of this post represent my personal perspectives, and I do not imply that any of these perspectives are endorsed by the PSRN or any institution with which I'm affiliated.
I do hope, however, that they turn out to be useful.*

## Setup

Several days in advance, the workshop organizers sent out some material to introduce the subject matter and prime everyone for productive discourse.
Each of us was assigned to one of four extreme scenarios regarding resource availability (high vs. low) and research motivation ("advancement" / curiosity-driven / proactive vs. "necessity" / problem-solving / reactive), and then asked to consider the plant science community's opportunities and challenges with respect to cyberinfrastructure and postgraduate training in the given scenario.
Specifically, we were asked to come to the workshop ready to share an "early indicator" that would suggest a trend in the direction of our assigned scenario.
I've summarized my overall experience at the workshop [here]({filename}2016-10-20-psrn-retreat.md).

## Initial concern

The prep material referred quite a bit to software, but it was almost exclusively mentioned<sup>1</sup> in the context of cyberinfrastructure components integration—in other words, very low-level systems engineering.
One of my initial reactions was that the prep material failed to acknowledge the wider spectrum of research software that exists, with systems engineering at one extreme and very domain-specific (and sometimes study-specific) research codes at the other extreme.
The former requires deep engineering expertise with some minimal exposure to plant science domain knowledge, while the latter requires extensive plant science expertise with minimal (perhaps even self-taught) programming experience.
But there is a lot of middle ground there, with most research software closer to the "domain expertise" extreme.
And it doesn't do any good to lump everything together under one umbrella.
This too often results in software being designated as second-class, with plant science (or another life science discipline, more generally) being elevated as the "real" science and software demoted to a purely technical exercise best delegated to trainees (or technicians, if you're fortunate enough to afford them) or outsourced to engineers for heavy technical lifting.

## Pleasant surprise

Despite my concern coming into the workshop, I must say that I was pleasantly surprised with the discussions around software.
This point was acknowledged throughout the discussion, and it was quite well received, and even connected to other relevant concerns and takeaways.
I'm not sure I can even take credit for this, since I don't remember if I was the only or even the first person to raise the issue.
I'm cautiously optimistic that the plant science community can foster continued dialog and perhaps even (crossed fingers!!!) catalyze some actual cultural change in this regard.

## Stepping back: research software and experiments

All of this has me [thinking again]({filename}../2015/2015-12-16-wrong-about-software.md) about *why* research software is rarely considered a legitimate intellectual contribution to science.<sup>2</sup>
As I've said before, I think it's important to compare software to experiments.
Which components of experiments are valued as legitimate intellectual research activities?
Of course you must include the design of the experiment, the evaluation of the experimental results, and the interpretation and dissemination of the findings.
The actual execution of the experiment, on the other hand, is a purely technical exercise.
An important one no doubt, but something that could be delegated to a competent technician with minimal domain expertise.
The keeping of a detailed and accurate lab notebook could be argued either way, but is probably more on the technical side than the intellectual.

So how does this translate to software?
I will again echo [Kai Blin's argument](http://phdops.kblin.org/software-dev-intellectual-contribution.html) that designing research software is like designing experiments, and just as with experiments, you must evaluate, interpret, and disseminate computational results.
These are all inherently intellectual activities.
Ideally, with some upfront design, *implementing* the software and then *executing* it should be a fairly straightforward technical exercise, also perfectly fine to designate to competent technicians with minimal domain expertise as resources allow.
But research software is so much more than just "writing code", and should definitely not be treated the same as code for systems-level cyberinfrastructure engineering.

## An ideal world

In an ideal world, design is completely separated from execution.
Entire experiments are thoroughly designed and critically evaluated before a single sample is collected or reagent is touched.
Consideration is given to what controls are in place to validate assumptions and verify experimental integrity, to how the results will be evaluated, and to which statistics and data visualizations will be most interesting to report—regardless of the result!
Once all this is fleshed out, conducting the experiment is almost mechanical, with little or no critical thinking required.
Collecting, formatting, interpreting, and disseminating the results is not quite so formulaic, but the critical thinking required at this stage has been well primed by the upfront design.

The ideal world of research software looks very similar.
The software is thoroughly spec'd out before a single line of code is written.
Consideration is given to what automated tests are in place to validate assumptions and verify computational accuracy, to how the results will be evaluated, and to which statistics and data visualizations will be most interesting to report.
Once the design is critically vetted, implementing the software is almost mechanical, with little or no critical thinking required.<sup>3</sup>
Collecting, formatting, interpreting, and disseminating the results is not quite so formulaic, but the critical thinking required at this stage has been well primed by the upfront design.

## We do not live in that world

I have enough [exposure to experimental molecular biology](https://udall-lab.byu.edu/LabPersonnel) to know that these ideals are rarely met in experimental science.
However, my experience allows me to speak in more depth about why these ideals are rarely met in computational science.

Part of the problem is that as time- and resource-strapped scientists, often poorly trained with respect to software, we rarely invest sufficient time in the upfront design.
As a result, we often end up taking the less than optimal approach of design-by-implementation, which can lead to messy and inflexible and inaccurate software.
Perhaps now is a good time to reiterate the fact that this workshop focused on both cyberinfrastructure *and training*.
Training won't necessarily help with time and resource limitations, but it can certainly expose a nacent plant-scientist-programmer to some basic software development principles that help avoid common pitfalls.

The other side of this coin is that software requirements are often hard to specify for cutting-edge research.
The problem spaces are typically underdefined and rife with subtle complexity, making it difficult to clearly articulate solid software requirements before some initial data exploration, which itself requires some software/computing literacy.
It often makes sense, therefore, to adopt an iterative approach to research software development: building a rudimentary prototype, evaluating its behavior/accuracy/utility, refining the design requirements, and then repeating.
Again, a minimal amount of training with basic software development practices can make a huge difference in the scientist's effectiveness and morale, as well as the desired research outcomes.

## Reusable software libraries

Taking things a step further, it's important to note that research software can be a powerful platform in which to explore and evaluate conceptual models.
One of the discussion points that came up in the workshop is that building and reusing software libraries is not incentivized in the current plant science (and wider science) culture.
All of the professional incentives push scientists toward implementing new ideas from scratch (and getting a paper out of it, which can then be cited), rather than building on existing tools (nobody will publish or credit contributions like this).

Building on existing code requires more attention to software engineering than is realistic to invest in the current funding/career/credit landscape.
Imagine a scientist interested in exploring the nuances of transcriptome assembly.
The most common scenarios in the current climate involve the scientist either 1) losing their sanity trying to understand and extend existing assembly software that the original scientist was never supported to clean up, organize, and document, or 2) building the assembler software components (de Bruijn graph implementation, assembly algorithm, etc.) from scratch.
This is a genomics example (that's my research interest), but the principle can apply to research software in any area of plant research.

Those that produce good software in today's academic environment do so *in spite* of the system and at great personal sacrifice, not *because* the system supports them in doing so.
Not all research software warrants this additional attention—there is definitely a place for ["single-use" research software](http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html)—but there is a critical need in some cases to support development of reusable software libraries.<sup>4</sup>
The plant science community has a huge opportunity to address this with relevant career support and incentives.

## Closing thoughts

I'm encouraged that the diverse plant science community is beginning to acknowledge that software is a critical component of the plant research enterprise, not only for what it brings to the table in a technical sense but also what it represents in an intellectual sense.
Transforming this understanding into cultural change is a much bigger challenge, but one I hope this community is willing to fight for.

And if my lengthy ramblings have not yet diverted your attention to more important matters, I salute you!
Thanks for humoring me!
More importantly, I'm interested in your feedback.
What do you think?
Did I miss an important point or get something completely wrong?
Leave a note in the comments if you feel so inclined.

----------

<sup>1</sup>It's possible that I just perceived it that way, but the language and context seemed skewed towards cyberinfrastructure engineering.  
<sup>2</sup>I think we're at the point that many people have recognized this as a problem, but the incentive structures and culture have not yet changed to reflect this.  
<sup>3</sup>This is only partially true. Sometimes multiple implementation approaches exist and tradeoffs must be considered, but really these are technical considerations rather than scientific considerations. Of course, the same can be said of lab techniques...  
<sup>4</sup>This is quickly becoming a complex multi-dimensional space. We've already discussed the "domain" axis (cyberinfrastructure engineering <---> highly specialized plant science analysis) and the "re-use" axis (libraries <---> single-use proof-of-concept software), but another axis that was brought up was the "scale and integration" axis (research <---> production). The cutting edge of plant science insights happens at the small-scale research level, whereas the integration of critical cyberinfrastructure components requires production-scale strategies.
