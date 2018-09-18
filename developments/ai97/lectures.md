---
layout: page
title: Lectures
permalink: /lectures/
---

You can download the lectures here (in PDF format). I will try to upload lectures prior to their corresponding classes.


<ul id="archive">
{% for lecture in site.lectures %}
      <li class="archiveposturl">
        <span><a href="{{ lecture.slides }}">{{ lecture.title }}</a></span><br>
<span class = "postlower">
<strong>tl;dr:</strong> {{ lecture.tldr }}</span>
<strong style="font-size:100%; font-family: 'Titillium Web', sans-serif; float:right">
<a href="{{ lecture.slides | prepend: site.baseurl }}"><i class="fas fa-file-pdf"></i></a>
</strong> 
      </li>
{% endfor %}
</ul>