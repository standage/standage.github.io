Title: New lab notebook setup: my motivation
Date: 2015-11-17
Author: Daniel S. Standage
Category: blog
Tags: meta

My first research blog was a self-hosted Wordpress blog run from an Ubuntu server in our lab.
I was initially enamored by the supposed control and flexibility this gave me, but when I changed institutions a year or so later I was not quite as enamored with the work that went into migrating the content, nor the time I spent in sysadmin troubleshooting (I hate SELinux with a passion).
During that time I had also become familiar with the disheartening statistics on the half-life of links to academic department/lab websites.
I so decided that in the long run it would be more sustainable for me to let someone else handle the hosting concerns, so I could focus just on the content.
Version 2 of my blog was (well, is) [hosted at Wordpress.com](http://biowize.wordpress.com).

I've continued posting content to the blog over the last couple of years—though not as frequently as I would like—but recently I've become increasingly dissatisfied.
I found myself saving electronic "scribbles" in Evernote or my wiki (also self-hosted on a server in our lab) and IPython/Jupyter notebooks in GitHub gists, saving the blog for when I really wanted to stretch my writing legs and produce some polished, contextualized thoughts.
But with notes and code and blog posts scattered all over the place, my setup felt harried and scrambled.
I need a more organized and streamlined solution.

In working out the setup for this notebook, I have the following considerations in mind.

- **One-stop shop**. With the exception of my software engineering work (which benefits immensely from the development workflow provided by git and GitHub), I want to be able to store all of my notes, scribbles, code snippets, Jupyter notebooks, and blog posts in one convenient location.
- **Markdown support**. I was never a fan of web-based WYSIWYG text editors, and so I've been writing all of my blog content in raw HTML.
  It's a travesty that this is still happening in 2015.
  I would much prefer to format my content with Markdown.
  (Ironically, I just learned recently that Wordpress.com now has integrated support for Markdown, so this would make a poor excuse if it was my only reason for changing.)
- **Embedded JavaScript**. Wordpress.com does not allow users to embed `<script>` tags in blog posts.
  "Shortcodes" are available for embedding content from a variety of popular media sources (Youtube, GitHub gist, and Twitter, for example), but you're out of luck if you want to embed video or other rich content from a different source (such as an [asciicast](https://asciinema.org/)).
  Support for embedded JavaScript is high on my priority list for this new setup.
- **Control and accessibility**. The first self-hosted version of the blog gave me the illusion of control and accessibility with respect to content, but really I was stuck to the web authoring interface (behind the scenes it was raw HTML stored in a MySQL database, and I wanted nothing to do with that bidness).
  The second version of my blog relieved me of the tedium of hosting, but only by relinquishing even more accessibility and control over my content.
  For my new setup, I would like the ability to write my content in vim or Komodo Edit; to search the content with shell tools or with custom Python scripts; to set up automated backup procedures using cron.

Taking all this into account, it's pretty clear that I need a solution based on a [static site generator](https://wiki.python.org/moin/StaticSiteGenerator).