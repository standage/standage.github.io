Title: Setup
Category: blog
tags: meta
status: hidden

More details coming soon.
For now, linkfest.

- [Pelican](http://blog.getpelican.com/) static site generator, because Python
- [Bootstrap theme](https://github.com/getpelican/pelican-themes) for Pelican
    - mods detailed below, here's an explanatory [link](https://github.com/getpelican/pelican/issues/816)
- [pelican-ipynb plugin](https://github.com/danielfrg/pelican-ipynb) for integrating Jupyter/IPython notebooks ([more here](http://danielfrg.com/blog/2013/03/08/pelican-ipython-notebook-plugin/))

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