Title: Developer, pull request thyself
Date: 2019-12-31
Author: Daniel S. Standage
Category: blog
Tags: software; social
Summary: I contend that you should be treating your solo software projects like a collaborative project and using pull requests, an issue tracker, and other social development tools.

**TL;DR** I contend that you should be treating your solo software projects like a collaborative project and using pull requests, an issue tracker, and other social development tools.


## Preamble

I'm a huge fan of using [Git](https://git-scm.com/) to maintain a versioned history of my software and research projects.
As an undergraduate I flirted briefly with [Subversion](https://subversion.apache.org/), but by the time I was taking version control seriously as a first-year grad student this new upstart company [GitHub](https://github.com/) was driving rapid adoption of Git across the tech and science industries.
To anyone who has gotten into software more recently, it's difficult to effectively communicate the impact Git and GitHub have had on the practice of software development.
Leveraging Git's distributed design, GitHub provides a variety of collaborative development tools:

- one-click "forking" to create your own personal copy of any public project,  over which you have full control
- "pull requests" for submitting proposed changes from your personal fork back to the original repository (for example, to fix a bug or add a new feature); alternatively, for repositories to which you have write access, you can make a pull request to merge a feature branch into the main "master" branch
- an integrated issue tracker that scans commit messages and to link issue threads to relevant commits and automagically close issues once they're resolved
- various other project management features like [project boards](https://help.github.com/en/github/managing-your-work-on-github/about-project-boards) and [continuous integration](https://github.com/features/actions)

The creators of Git and GitHub didn't invent any of these terms/concepts/strategies, but they deserve a lot of credit for creating an intuitive system that propelled their nearly universal adoption into the programmer's lexicon and daily practice.

My own habits with respect to Git and GitHub have evolved in the last ~10 years.
This is due to a few factors: I was entirely self-taught at first; I gained experience over time contributing to a variety of open source software projects; and I began noticing and using some more recently introduced features of the GitHub platform itself.
In general, I don't claim any special expertise or profound insights into the *way of Git*.
But there is one way I use GitHub that seems uncommon, and that is **to make full use of its collaborative and social tools on projects to which I am the sole contributor**.
In other words, **I collaborate with myself on solo projects**.
I contend that GitHub's collaborative development features are underused in solo software development projects, and that these projects have a lot to gain by adopting them.


## Basically, an electronic lab notebook for software

My impression is that software developers don't generally make an active choice *not* to use GitHub's collaborative tools for solo projects.
Rather, these tools are always taught and discussed in the context of communicating with others to coordinate updates to some central code base.
For projects with only a single contributor there's nobody else to coordinate or communicate with, so most folks will default to the simplest strategy and just commit & push directly to the master branch.
If someone is particularly careful or responsible, they might use branches to isolate new features or bug fixes from the master branch until they have been well tested.
But even then, merging a feature branch to master locally and then pushing directly to master on Github seems to be the common practice for solo projects.

But let's consider for a moment what benefits GitHub's collaborative tools provide.

> In the ideal scenario, the need for each change (bug fix, refactoring, new feature, etc.) will first be described in a dedicated thread using the project's issue tracker.
> This thread creates a dedicated space for project contributors to discuss the merits of different potential solutions.
> If there is general consensus, somebody can make the proposed changes on a fork or branch and submit those changes as a pull request (PR).
> The main text of the PR refers to the problem described in the issue thread (GitHub automatically detects this and adds hyperlinks to each thread), and describes how the proposed changes were made and/or how they will affect the software's behavior.
> If there is *not* consensus, alternative solutions can be implemented, described, and submitted for consideration simultaneously in separate PRs.
> The discussion will continue as long as needed on the issue thread and any associated PR threads.
> This sometimes requires back-and-forth communication with a PR contributor and the collaborators reviewing the PR, and multiple updates to a PR before it is approved (or rejected).
> Once a PR is approved and merged into the master branch, the issue thread and PR threads are put into a "closed" or "resolved" state, but they remain a permanent searchable part of the GitHub repo.

So what benefits do GitHub's collaborative tools provide?

1. **They document changes to the project.** In all areas, but especially in science, it's important to know how a software package's implementation and behavior have evolved over time. Keeping a change log is a common way this is done, but change logs are a very concise and limited summary of the changes. GitHub's issue threads and PRs capture the much richer context around each change—what motivated it, what solutions were considered, and how the solution was implemented. Even after the relevant threads are closed, they remain a browsable and searchable part of the repo's permanent record, available for future reference to anyone with interest and access.
2. **They force the developers to reflect on proposed changes in the context of the project's status and trajectory.** If a contributor can't clearly describe a bug or the need for a new feature, it's unlikely they will be able to convince their collaborators to approve a set of proposed changes to the software. Communicating clearly about issues and proposed solutions requires contributors to think holistically about the project, which goes a long way to preventing half-baked ill-advised changes to the code that end up creating more problems down the road than they solve.
3. **They foster transparency in the development process.** When all updates to the software are submitted as PRs, and when each PR refers to a specific problem described in sufficient detail, and when each PR must be reviewed before it is approved and merged, there are multiple layers of defense against a single contributor making unilateral changes without consulting collaborators.

I don't think I have to work hard to convince anybody that these benefits are just as important for solo projects as they are for collaborative projects.
It's common for scientists to work on multiple projects at a time, and for each project to span months or years.
A scientist displays a lot of hubris when they claim that they can responsibly stay on top of this without **documenting changes**, **reflecting on proposed changes in the context of the project's status and trajectory**, and **fostering transparency in their development process**.
Many colleagues and acquaintances can relate when I share my frustration that I routinely struggle to understand code I wrote 2 months ago.
So if you ever plan on using your software on a continuous basis, or using it again some time in the near future, or reusing portions of it later for a new project, or, you know, re-analyzing your data when the reviewers raise concerns about the Methods section of your research manuscript, it's important to have something to fall back on.

For scientists working in a lab, keeping a detailed lab notebook is a professional (and, depending on the field, sometimes a legal) obligation.
But for some reason, this doesn't often get translated into the realm of scientific software.
I suggest that using GitHub's collaborative features as described above is a great way to maintain an electronic lab notebook for a software project, even if you are the only contributor.

## How about some examples?

Here are a few examples from solo projects I've worked on recently.
In each case, a dedicated issue thread was created to describe a bug or new feature, and later a PR to resolve that issue was submitted, reviewed (by myself!), and merged.

- Example 1: [issue](https://github.com/kevlar-dev/kevlar/issues/360) and [PR](https://github.com/kevlar-dev/kevlar/pull/361)
- Example 2: [issue](https://github.com/bioforensics/MicroHapDB/issues/43) and [PR](https://github.com/bioforensics/MicroHapDB/pull/46)
- Example 3: [issue](https://github.com/bioforensics/MicroHapulator/issues/52) and [PR](https://github.com/bioforensics/MicroHapulator/pull/53)

Occasionally I'll notice a bug, begin investigating it, and start implementing a fix before documenting the bug in a dedicated issue thread.
In these cases, I'll just provide a description of the bug in the main PR text.
Here's [an example](https://github.com/bioforensics/MicroHapulator/pull/70).


## Make it collaborative!

For solo projects where you're the only one doing the coding, it's still likely that your project is influenced directly or indirectly by interactions with your colleagues, advisors, and/or trainees.
Very little scientific work is done in total isolation.

So if you're using GitHub's issue tracker to describe bugs to be fixed and features to be implemented, and if you're using pull requests (PRs) to describe and evaluate updates to the code, it's very easy to turn your solo project into a collaborative project!
Here are a few ideas about how you might do that.

- You've created a new branch in your git repo to implement and test a new feature for your software. You've submitted a PR to merge this branch into the master branch. **Send a link to this PR to your collaborator and ask if she has any feedback on your proposed changes.**
- You recently noticed a bug in your software's behavior. You briefly described the bug in a new thread in the issue tracker, but you haven't had time to go back and fix it yet. **Send a link to the bug report to your rotation student, give him access to your repo, and invite him to create a new branch to fix the bug and then submit changes as a pull request.**
- In your last meeting with your advisor, she expressed concerns with some details of your software's core algorithm. **Take time to consider her concerns, write them down in a new issue thread, and then send her a link to the thread and ask if you've understood her concerns correctly.**


## Is it worth it?

Scientific software comes in many shapes and sizes.
You might implement software as a proof-of-concept, tailored for a specific task unique to a study you're conducting.
Alternatively, you might write a program that implements a method that you think would be useful to numerous scientists in a variety of similarly designed studies.
Or perhaps you implement your software as a library, intended to help other scientists write their own scripts and programs for simulating and analyzing data.

If your aspiration is for your solo software project to become widely used, then treating it like it's already a collaborative project is a no-brainer.
(Whether it is *actually* widely used depends on a variety of factors, some beyond your control: how easy it is to install; how helpful the documentation is; the journal(s) in which you've published papers describing it, and the results/findings described in those papers; who notices, uses, and cites it, or discusses it on social media.)

But even if you *don't* aspire for a particular solo software project to become widely used, I still propose that it is worth your time to treat it as a collaborative project.
There are a few good reasons for this.
While it may require a bit of time and deliberate effort at first, this time and effort will decrease as it becomes a habit.
And becoming comfortable with Git and GitHub's collaborative features will make it much easier for current or future projects that you *do* hope will be widely used and recognized.
These same skills will also come in handy if you ever want to contribute to an open source software project, science related or not.

In short: it doesn't take much extra time, especially once you've made a habit of using skills that will serve you well in a variety of contexts in the future.


## But won't I get scooped?

Statistically, the likelihood that your software will go largely unrecognized is much higher than the likelihood that someone will follow your GitHub repo closely, steal your ideas, and publish a paper describing your work before you can.
I certainly think that, as a general rule, scientists are best served by developing software in the open from the start.

But if you think you have valid concerns about making your software public at first, GitHub allows you to keep your repository private.
You can use all of the strategies discussed here, and for private repos visibility will be limited to you and those you specifically choose (if any).
Then, when you are ready to share your software more broadly, you can mark the repo as public.

If you publish a paper describing or referencing the software, you should definitely make the repo public by manuscript submission time at the latest.
Links to a private repository do not allow anonymous peer review, and "software available upon request" statements are completely inappropriate.


## Recommendations

To summarize, let me just clarify and reiterate a few recommendations for solo software development projects.

- **Use GitHub's issue tracker liberally.** Describe bugs to be fixed, features to be implemented, questions to ponder, and so on. You don't have to be verbose, just make sure that what you've written is clear.
- **Don't push changes directly to the master branch.** You can even have GitHub prevent you from doing this with your repository's [Branch Protection Rules](https://help.github.com/en/github/administering-a-repository/configuring-protected-branches). Instead, whenever you need to make an update, create a new branch, commit changes to that branch, push the branch to your GitHub repo, and submit the changes as a pull request (PR).
- **Review your own PRs before you merge them.** The PR thread has a "diff" view that displays the differences between your new branch and the master branch. Examine these differences carefully. Did any changes sneak through that shouldn't have been included? Did you forget to remove temporary `print`, `assert`, or other debugging statements? GitHub PRs also allow you to [select several lines of code in the diff and comment on those lines](https://stackoverflow.com/a/58190804/459780). Use these to:
    - highlight the most important changes in a PR; i.e. "*this change fixes the integer underflow bug*"
    - mark problems to be resolved; i.e. "*whoops, this needs to be fixed before the PR is merged*")
    - call out particularly messy or complicated code blocks; i.e., "*this works for now, but I should probably go back and clean this up when I have time*"
- **Compile an automated test suite.** I've [written previously about my strong opinions on testing scientific software](https://standage.github.io/the-joy-and-art-of-automated-testing.html). All the better if you can configure GitHub to run the automated test suite for you each time you create or update a PR. You can even configure GitHub to prevent PRs from being merged until the test suite passes—I highly recommend!
- **Try to find ways to involve others in your project.** Trainees, advisors, colleagues, and even acquaintances are often willing to respond favorably to a considerate and clearly communicated request to provide feedback, perform a brief review, or a collaborate on a software development task.


## Postscript

I've focused my discussion here entirely on GitHub, since it is by far the most popular platform for open source software and scientific software.
Alternatives exist however, such as GitLab and BitBucket.
All of the strategies discussed here should work regardless of what platform you're using.
In some cases, the terminology may be slightly different.
For example, GitLab uses the term **merge request** instead of **pull request**.
