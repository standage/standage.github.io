Title: Notebook Setup
Category: blog
tags: meta
status: hidden

Over the last several years I've used a motley assortment of blogs, wikis, and web-hosted documents to keep records of my research activities, mostly for personal reference but also occasionally to share with colleagues and collaborators.
This lab notebook is the latest iteration of my effort to streamline the documentation of my research.
It is built on my laptop using the static site generator [Pelican][], and hosted on [GitHub Pages][].
I've included some details on my setup below.

## Why the new setup?

I discuss this question at length [in this post]({filename}/2015-11-17-setup-motivation.md), but in brief I wanted a solution that offers the following.

- A one-stop shop for all my research notes, scribbles, commands, notebooks, and blog posts.
- Support for formatting content with Markdown.
- Support for embedded JavaScript.
- More accessibility and control over the content.

Static site generators, with which I had become acquainted in the last couple of years, seemed well-suited for my needs.

## Why Pelican? Why not Jekyll?

Because Python.

## Seriously, why?

I'm joking of course, this is actually a fair question.
Jekyll far outstrips Pelican in terms of popularity and name recognition, no doubt because of its privileged integration with [GitHub Pages][].
The popularity is nothing to sniff at: it means a lot more digital ink is spilled writing questions and answers about Jekyll on sites like [StackOverflow][], making it much more likely to find a quick solution to basic troubleshooting issues with a simple Google search.
The privileged integration with GitHub is also a very nice feature: they handle the Markdown-to-HTML conversion on their back end, so you just have to worry about the raw content. 

That said, the reasons I decided to go with Pelican instead of Jekyll have a lot to do Python vs Ruby.

- I suspected (and later confirmed) that integrating IPython/Jupyter notebooks is much more straightforward with a Python-based platform than a Ruby-based one.
  This was a big selling point for me, since I really want to make these a bigger part of my research record.
- Heaven forbid I should ever have to write a plugin or extension for *any* static site generator, but if for some reason I decided this was a good idea, I would much rather do it in Python than have to slop something together in Ruby.
  And just to be clear, when I say *slop* I refer to my inexperience with Ruby, not to its inferiority to Python or any other language (I've never written a single line of Ruby, so I wouldn't know).
- Maybe I'm mistaken on the following points, but I get the sense that Ruby is a slow language, and that its performance is not improving as quickly as many had hoped and expected, and that the Rails web framework (Ruby's biggest selling point) is losing popularity to JavaScript-based web back ends.
  Performance probably won't be a big deal for a small blog/notebook that I pre-generate on my laptop, but looking forward 5-10 years from now my predictions for the Python ecosystem and community are brighter than those of Ruby.

## Okay, so what's the setup?

### Pelican

- Installation was trivial: `pip install pelican` and I was ready to go.
- Creating a new site is trivial: `pelican-quickstart` creates a basic scaffolding for the site.
- It took a bit of work to refine the site configuration, but (unless I've forgotten something) all of my changes are restricted to the `pelicanconf.py` configuration file, which is ideal.
- Had to change the `ghp-import` interpreter for `make github` to work: see [this](https://github.com/davisp/ghp-import/issues/49).

### Bootstrap theme

- [https://github.com/getpelican/pelican-themes](https://github.com/getpelican/pelican-themes)
- Installation was easy with `git clone`.
- Some defaults did not work well out-of-the-box and needed to be modified.
    - The disqus plugin attempts to load over HTTP by default, which is a problem when viewing the blog over HTTPS.
      Modifying the theme to load over HTTPS fixed this.
    - Changing the `DEFAULT_DATE_FORMAT` setting in the Pelican config file did not have the desired effect.
      It turns out the date format was hard-coded into the Bootstrap theme, and I had to replace it with `{{ article.locale_date }}` (see [this](https://github.com/getpelican/pelican/issues/816)).
- Made various adjustments to the theme (see below).

### pelican-ipynb plugin

- [https://github.com/danielfrg/pelican-ipynb](https://github.com/danielfrg/pelican-ipynb)
- Installation was trivial (as documented), and no changes were required

## Appendix: theme changes

```diff
diff -r bootstrap/static/bootstrap.min.css ../pelican-themes/bootstrap/static/bootstrap.min.css
78c78
< p{font-size:13px;font-weight:normal;line-height:18px;margin-bottom:9px;}p small{font-size:11px;}
---
> p{font-size:13px;font-weight:normal;line-height:18px;margin-bottom:9px;}p small{font-size:11px;color:#bfbfbf;}
91c91
< li{line-height:18px;}
---
> li{line-height:18px;color:#808080;}
diff -r bootstrap/static/local.css ../pelican-themes/bootstrap/static/local.css
14,18d13
< .well ul {
< 	list-style-type: none;
< 	margin-left: 0;
< }
< 
41d35
< .social a[href*='stackexchange.com']:before {content: url('./images/icons/stackoverflow.png'); margin-right: 2px; vertical-align: -3px;}
diff -r bootstrap/templates/archives.html ../pelican-themes/bootstrap/templates/archives.html
2c2
< {% block title %}Notebook <small>[archive]</small>{% endblock %}
---
> {% block title %}{{ SITENAME }} <small>[archive]</small>{% endblock %}
diff -r bootstrap/templates/base.html ../pelican-themes/bootstrap/templates/base.html
55,60c55,57
< 				{% if DISPLAY_CATEGORIES_ON_MENU %}
< 					{% for cat, null in categories %}
< 						<li {% if cat == category %}class="active"{% endif %}><a href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
< 					{% endfor %}
< 				{% endif %}
< 				<li><a href="{{ SITEURL }}/notebook.html">Notebook</a></li>
---
> 				{% for cat, null in categories %}
> 					<li {% if cat == category %}class="active"{% endif %}><a href="{{ SITEURL }}/{{ cat.url }}">{{ cat }}</a></li>
> 				{% endfor %}
62c59
< 			<p class="pull-right"><a href="{{ SITEURL }}/archives.html">[archives]</a> <a href="{{ SITEURL }}/categories.html">[categories]</a> <a href="{{ SITEURL }}/tags.html">[tags]</a></p>
---
> 			<p class="pull-right"><a href="{{ SITEURL }}/archives.html">[archives]</a> <a href="{{ SITEURL }}/tags.html">[tags]</a></p>
70,77c67
< 			<img src="http://1.gravatar.com/avatar/fe326141c425326acf247aef9c475c03?size=180" alt="Daniel Standage" />
< 			<h3>{{ AUTHOR }}</h3>
< 			<p>
< 				{% for addr in ADDRESS %}
< 				{{ addr }}<br />
< 				{% endfor %}
< 			</p>
< 			<h3>Affiliations</h3>
---
> 			<h3>Blogroll</h3>
94c84
< 			{% block indextitle %}<div class="page-header"><h1>{% block title %} Notebook {% endblock %}</h1></div>{% endblock %}
---
> 			{% block indextitle %}<div class="page-header"><h1>{% block title %} {{ self.windowtitle() }} {% endblock %}</h1></div>{% endblock %}
97,102c87,88
< 		  <p>
< 			<a href="http://creativecommons.org/licenses/by/4.0/"><img src="{{ SITEURL }}/images/cc-by-88x31.png" alt="CC BY 4.0" /></a><br />
< 		    &copy; 2015 {{ AUTHOR }}.<br />
< 			Unless otherwise noted, all content on this site is posted under a <a href="http://creativecommons.org/licenses/by/4.0/">CC BY license</a>.</p>
< 		  <p></p>
< 		  <p>This site is powered by <a href="http://getpelican.com/">Pelican</a>, its theme based on <a href="http://twitter.github.com/bootstrap/">Twitter Bootstrap</a>.</p>
---
> 		  <p>Powered by <a href="http://getpelican.com/">Pelican</a>. Theme based on <a href="http://twitter.github.com/bootstrap/">Twitter Bootstrap</a>.</p>
> 		  <p>&copy; {{ AUTHOR }}</p>
diff -r bootstrap/templates/categories.html ../pelican-themes/bootstrap/templates/categories.html
2c2
< {% block title %}Notebook <small>[categories]</small>{% endblock %}
---
> {% block title %}{{ SITENAME }} <small>[categories]</small>{% endblock %}
diff -r bootstrap/templates/category.html ../pelican-themes/bootstrap/templates/category.html
2c2
< {% block title %}Notebook <small>{{ category }}</small>{% endblock %}
\ No newline at end of file
---
> {% block title %}{{ SITENAME }} <small>{{ category }}</small>{% endblock %}
\ No newline at end of file
diff -r bootstrap/templates/index.html ../pelican-themes/bootstrap/templates/index.html
4,5d3
< <p>Psst! I've posted details about my notebook setup <a href="{{ SITEURL }}/pages/setup.html">here</a>.</p>
< 
diff -r bootstrap/templates/metadata.html ../pelican-themes/bootstrap/templates/metadata.html
1c1
< Permalink: <a class="more" href="{{ SITEURL }}/{{ article.url }}">{{ article.locale_date }}</a>
---
> Permalink: <a class="more" href="{{ SITEURL }}/{{ article.url }}">{{ article.date }}</a>
diff -r bootstrap/templates/tag.html ../pelican-themes/bootstrap/templates/tag.html
2c2
< {% block title %}Notebook <small>{{ tag }}</small>{% endblock %}
\ No newline at end of file
---
> {% block title %}{{ SITENAME }} <small>{{ tag }}</small>{% endblock %}
\ No newline at end of file
diff -r bootstrap/templates/tags.html ../pelican-themes/bootstrap/templates/tags.html
2c2
< {% block title %}Notebook <small>[tags]</small>{% endblock %}
---
> {% block title %}{{ SITENAME }} <small>[tags]</small>{% endblock %}
```


[Pelican]: http://blog.getpelican.com/
[GitHub Pages]: http://pages.github.com
[StackOverflow]: http://stackoverflow.com
