Title: The Joy and Art of Automated Testing
Date: 2018-11-19
Author: Daniel S. Standage
Category: blog
Tags: software; testing
Summary: A primer on software testing for scientists and researchers.

<center>
![Retro tea cup advert: Serve up your software hot, fresh, and reliable with AUTOMATED TESTING!](https://i.imgflip.com/2lbq54.jpg)
</center>

If you're in the business of writing software, one of your primary concerns is whether your software does its intended job correctly. If, like me, you're in the business of writing software in a research or science context, ensuring the reliability of the software is of *critical* importance. Peer review of changes or updates to the code, in chunks of manageable size, is one of the best ways to find bugs and improve software quality. But sooner or later, you're going to need to **test** your software.

The purpose of this post is not to convince you that testing is an important professional obligation. If writing software is your daily bread, then this should already be a given. If, instead, you're a scientist or researcher that finds themself spending an increasing amount of time dabbling in code, think of testing as the positive and negative controls you design to ensure your experimental results are reliable. It's just not something you can compromise on without threatening the integrity of the entire process. (Note: you're likely engaged in some amount of testing already! If you execute code and evaluate its behavior or compare a result against your expectations, that's testing. Good for you!)

Rather, the purpose of this post is to persuade you that you can and probably should be testing more frequently and more comprehensively, and that automation is your friend. I discuss some of the concepts and strategies that make testing effective and that make it possible to test frequently without becoming overwhelmed. Perhaps, *you too* may come to more fully appreciate the joy and art of automated testing! :-)


## What is "correct"?

> *"Physicists worry about decimal places. Astronomers worry about exponents. Economists are happy if they've got the sign right."*  
> \-\-Someone wise

The purpose of testing is to verify that your software does its job correctly. Of course, what *correct* means will depend on the nature of the problems you work on and the types of tests you're writing. If your research focus is incrementally improving solutions to well-understood problems, then there are likely "gold standard" reference data sets that have been studied extensively by your community and where the "answers" are well known. If you're working on poorly understood cutting-edge problems in a novel discipline, you may have to rely more on deriving correct answers from first principles. Most researchers fall somewhere between these two extremes, and you should use your judgement and experience (and suggestions from trusted colleagues, if unsure) to determine what inputs to use for your tests and what results should be declared correct. For some problems an exact answer is required, while in other cases an exact solution is not feasible and an answer within a small numerical range is acceptable. This range defines the tolerance for error (or simply *tolerance*) of your test.

- Discrete numerical results often require an exact integer answer. Sometimes, a small range of integers can be specified.
- Text results also typically require an exact answer. Sometimes, a regular expression can be specified to indicate a particular pattern that must be satisfied.
- Continuous numerical values cannot be stored exactly even on modern computers, so evaluating floating point numerical results requires specifying an accepted tolerance.

There are numerous alternative ways to assess a result that may be more appropriate in some circumstances: set membership, similarity to a reference, number of results produced, etc. Ideally, you want to make the test reasonably stringent without causing failures for trivial reasons. And as you continue to test your software over time, you'll get a better feel for this balance and gradually tighten the stringency of your tests.


## Test automation

Once you have successfully completed the test(s), the next step is to *automate* test execution. It may be tempting to convince yourself that it is not worth the time required to automate your testing, but as you develop your software you will need to execute the tests over and over again to make sure your bug fixes and optimizations and new features don't introduce new bugs in the code.

Ideally, you should be able to execute your tests (or a relevant subset of tests) in as few keystrokes as possible. For each individual test, you write code to call the function/subroutine/module/script/program you want to test, store the result, and compare the result to the "correct" answer as discussed in the previous section. Then, you should have one master script or command that will run all of these tests for you. This is what we mean by **test automation** and **automated testing**.

Many programming languages have testing frameworks that provide convenient features and eliminate a lot of the pain associated with writing and running tests. I'll discuss these a bit in the **Testing Frameworks** section below.


## Types of tests

> *"Computers are useless. They can only give you answers."*  
> \-\-Pablo Picasso

There are a few different testing strategies you can use to evaluate different aspects of your software. These are not competitive or exclusive: sometimes a test doesn't fit cleanly into just one of these categories, and you'll want to use a combination of these approaches in your test suite.

- **smoke tests**: Here, you're simply asking *"Can I run this bit of code without things blowing up?"* Rather than testing that the software produces a specific result, it ensures the software can be run under normal conditions without producing a runtime error. This is a crude testing technique, but a valuable and easy one particularly appropriate for use early in the development process.
- **unit tests**: A unit test, well, tests a particular unit of code. (I know, deep stuff!) There are no strict rules about what qualifies as a "unit" of code. Often, unit tests are focused on functions, subroutines, or methods, and are intended to give you and other developers confidence that the function works as advertised. This will enable you to treat the function as a magic black box when calling it elsewhere in your code, allowing you to give all of your focus to the code you're currently working on. If you test each "unit" of your code individually, you'll find later on that fitting those units together into a larger program/workflow/pipeline comes with much less struggle.
- **functional tests**: Functional tests focus on larger-scale operations and behaviors implemented by the code. Again, there are no universally-defined rules about what does and does not qualify as a functional test, but tests for entire modules, scripts or programs often fall under this category. Functional tests focus on end users: what kind of operations will the end user perform with the software, and do these operations produce correct results? These kinds of tests are especially valuable when sharing your code with others, as they can determine whether the software has been set up and installed correctly.
- **regression tests**: Regression tests make sure that continued development of your code doesn't break features that are already working correctly. Regression tests are great for making sure that when you fix a bug, it *stays* fixed. More generally, regression testing can give you the confidence to reorganize large portions of your code (for example, to support new features) without worrying whether you're breaking the features that already work.
- **doctests**: A doctest is a test that is embedded within a comment or documentation string in the code. Doctests serve dual purposes: they serve as user documentation, showing how to invoke certain operations; doctests also show how the code should behave on certain inputs in a way that can be automatically tested. This strategy is not supported in all languages, but can be valuable when available.


## Testing frameworks

All of the most popular programming languages have testing frameworks designed to make it easier for you to write and run tests. Personally, I'm partial to the [pytest](https://docs.pytest.org) framework because

1. I write the majority of my code in Python; and
2. the project is actively developed and responsive to bug reports and help requests; and
3. it has all the features I'll ever need for testing (and more)

However, there are similarly convenient and modern testing frameworks available for R, Julia, C++, Java, and many other languages. If you're new to testing, the factors that will probably make the most difference to you are

1. how easy is the framework to install? and
2. how active is the community using this framework? how responsive will they be to my questions?

Typically, a test framework works as follows.

- You implement each test as an independent function, usually invoking `assert` statements.
- Each test produces a PASS, FAIL, or ERROR result. If all `assert` statements pass, the test PASSes. If any `assert` statement fails, the test FAILs. If there is a problem executing the test, the test ERRORs.
- Optionally, you can specify "fixtures" or "setup/teardown" procedures to make test data available to each test. Data that is reused by multiple tests within a module can be loaded with a single module-level fixture, while data that is used by multiple modules might by loaded with a single global fixture. Appropriately-scoped fixtures or setup/teardown procedures make sure that time isn't wasted loading test data multiple times.
- There is a "test runner" that finds the tests (from a config file or by traversing the file structure), executes each test, and reports the aggregate results.

If these concepts seem new and overwhelming, don't be intimidated. Start with small tests to understand the mechanics of your chosen framework, and then escalate gradually to more complex tests as you gain experience and confidence.


## Test coverage

> *QA Engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 999999999 beers. Orders a lizard. Orders -1 beers. Orders a sfdeljknesv.*  
> \-\- Bill Sempf ([@sempf](https://twitter.com/sempf/status/514473420277694465))

Many testing frameworks can report *test coverage*, or the precise lines of code that are (and are not) invoked during test execution. This valuable information will help you identify potentially risky regions of your codebase. If a line of code is never run during test execution, you can't really be confident it works correctly. In fact, you can't even be sure it won't cause a runtime error and halt program execution right away. The higher your test coverage, the more confidence you can have that your software is going to 1) run; and 2) do its job correctly. If there are large blocks of important code that have no test coverage, you should consider writing tests that will invoke these lines of code.

If you can get 100% test coverage for your software, that's tremendous. Often this isn't feasible, and regardless it doesn't mean your software has no defects. Aiming for 80-90% coverage is usually a healthy target in my experience. Regardless, the overall percent coverage is only part of the story (more on that below). The take-home message is that you want to avoid large drops in coverage as you update your code over time. 

**NOTE**: It's also worth mentioning that the notion of test coverage discussed above, while common and useful, is also a bit shallow. Let's call it *statement coverage*. In the strictest sense, statement coverage can really only tell you which lines of code were executed without causing an unexpected error. They **do not** measure how much thought you put into your tests, what your tests actually measure, or how comprehensively your tests handle the full range of possible inputs. To illustrate, imagine writing lots of smoke tests that collectively invoke every function and instantiate every object in your codebase without examining any outputs or behavior. This approach could achieve very high statement coverage, maybe even 100%! But coverage would be a pretty useless measure of the software's reliability in this case since the tests don't actually, you know, test anything.

In traditional software engineering, a lot of time is spent up front drafting formal requirements in precise technical language to describe what types of inputs a software product will accept, the range of values those inputs can take, the outputs the software will produce, and the acceptable level of precision. Most scientists are not trained in this kind of requirements planning. In any case, this level of formality is poorly suited to research science, where our conceptual models of the problem space are typically rudimentary, incomplete, and rapidly evolving. The point, again, is that 100% statement coverage is not a guarantee that your code will work correctly for all valid inputs. The more thought and effort you put in to designing inputs, outputs, tolerances, and edge cases for your tests, the more closely your test coverage will reflect the true and practical (but difficult-to-measure) accuracy and reliability of your software.

**ANOTHER NOTE**: If you're feeling particularly adventurous, property-based testing strategies provide an effective means to address software quality in a fairly rigorous way without resorting to formal engineering methods. The idea is that you write a test not knowing what the input data will be, instead testing that the output has certain properties that should be true *in every case* (i.e. a numerical operation should be commutative, or the number of distinct outputs depends on an easily computed characteristic of the input). You then invoke the test with a large number of (possibly randomly generated) inputs and see whether the code you're testing works correctly on each input—see the joke above about the QA engineer. To the extent you use property-based testing in your test suite, your test coverage will be a much better reflection of the true accuracy of your software. To learn more, do a Google search for "property based testing python", replacing "python" with your favorite language, of course!


## Test-driven development

> *"Technology is a word that describes something that doesn't work yet."*  
> \-\-Douglas Adams

The idea behind *test-driven development (TDD)* is to write tests that don't pass or even run initially because the code they are intended to test doesn't exist yet. This might seem like a backwards approach to writing software, but TDD advocates claim it is a more responsible strategy. They claim it forces you to formulate the correctness tests *a priori*, and thus help avoid confirmation bias. They also claim that it forces you spend more time upfront considering how code will be structured and how data will be passed around, since tests cannot be written without these considerations.

While these sound like plausible benefits, empirical studies testing the effectiveness of TDD are as yet inconclusive. Many proficient programmers swear by TDD, so it's definitely worth giving an honest and deliberate try, especially if you struggle to find time to go back and write tests for your code. But if you're disciplined and have success using a different strategy, don't stress about TDD too much. :-)

Regression tests for bugfixes provide a particularly appropriate opportunity to put TDD into practice. When a bug is found in your code, your first task is to reproduce the bug. Once you've successfully done so, TDD prescribes that you write a new test to isolate and reproduce the faulty behavior. At first, this new regresssion test will fail. That's the idea, since you haven't fixed the bug yet! Once the regression test is complete and accurate, *then* you can go update your code to fix the bug. You'll know it's fixed when your new regression test finally passes!


## Continuous integration and peer review

Whether you update your code on a frequent basis or only touch it occasionally, *continuous integration (CI)* is one of the best ways to ensure your software is always in a runnable state. There are two complementary approaches to CI: automatically running tests as a "cron job" on a schedule (nightly, weekly, etc.) and automatically running tests whenever an update to the code is committed. If you've posted your code on Github or Gitlab, there are a variety of free CI services (such as [Travis CI](https://travis-ci.org), [Drone.io](https://drone.io/), and [Circle CI](https://circleci.com/)) that will run your tests for you, post the results, and send notifications if the test build fails. [Jenkins](https://jenkins.io/) is a similar service that you can download and install for free on your own system if you're restricted from posting your code publicly.

If you're lucky enough to have colleagues or collaborators contributing to your software, you've probably established some kind of protocol for peer review of code, even if it's informal and *ad hoc*. Code review is big and important topic and out of scope for this post, so I'll just briefly mention that CI can be an extremely valuable asset in the code review process. The Github "pull request" mechanism allows you to review any proposed changes to your code before you finalize them, and will also trigger a CI build. In addition to your typical review process, you should require at a minimum that all tests pass before you accept any proposed changes.


## Compromise

> *"Given the pace of technology, I propose we leave math to the machines and go play outside."*  
> \-\-Bill Watterson (Calvin from *Calvin and Hobbes*)

As a concluding thought, I'll just re-emphasize the sentiment that we write software *to solve problems* and *to more clearly understand the world*. Within any project, some of the code you write is directly related to the software's purpose, while much of the rest is involved in sundry routine and uninteresting operations: opening files, reading data into memory, parsing arguments or config files, and so on. I'm not going to say that these other bits of code are unimportant, but if one is not careful it's possible to spend an inordinate amount of time applying and re-applying all kinds of software engineering best practices to portions of the code that, at the end of the day, contribute very little to science. When time and resources and experience are limited, it's important that we focus our energy on the most important priorities.

A few years ago, [Titus Brown](https://twitter.com/ctitusbrown) wrote a great post on what he calls ["stupidity driven development."](http://ivory.idyll.org/blog/2014-research-coding.html) He argues that inaccurate results have much more dire consequences than software crashes, and thus he and his colleagues delayed fixing some annoying bugs for quite a while so that they could instead focus on the science questions they were using the code to explore. I think this is a winning strategy. The scientific core of your code deserves all the time, attention, and "best practices" you can afford to invest in it. The rest doesn't deserve any more than you feel like giving it, and I hereby grant you permission to compromise on any of the strategies I've discussed to the extent that doing so helps you focus more on testing the scientifically critical portions of your code more rigorously!

On the other hand, some of the most widely used (and widely cited!) software tools in my field (genomics and bioinformatics) initially gained their notoriety from the fact that in an ocean of poorly documented and unusable tools they could actually compile and run on most people's systems without too much hassle. Time spent improving the "user experience" for your software may not make for better science directly, but it *may* make it easier for others to appreciate and build on your science.


## Acknowledgements

This post is based on material developed by [Greg Wilson](https://twitter.com/gvwilson) and myself for teaching [Software Carpentry](https://software-carpentry.org/) workshops on [managing research software projects](https://swcarpentry.github.io/managing-research-software-projects/). Greg is a great mentor and friend and I want thank him for his consistent generosity and for simply being A Good Guy. I'd also like to thank Morgan Taschuk ([@morgantaschuk](http://twitter.com/morgantaschuk/)), Luiz Irber ([@luizirber](https://twitter.com/luizirber)), and Titus Brown ([@ctitusbrown](https://twitter.com/ctitusbrown)) for insightful comments on early drafts of this blog post.
