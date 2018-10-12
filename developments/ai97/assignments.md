---
layout: page
title: Assignments
permalink: /assignments/
---

You can download the assignment here (in PDF format). Also check assignment's pages for any additional info.


<ul id="archive">
{% for asg in site.assignments %}
      <li class="archiveposturl">
        <span><a href="{{ asg.url | prepend: site.baseurl}}">{{ asg.title }}</a></span>
<strong style="font-size:100%; font-family: 'Titillium Web', sans-serif; float:right">
<a href="{{ asg.pdf | prepend: site.baseurl }}"><i class="fas fa-file-pdf"></i></a>
</strong> 
      </li>
{% endfor %}
</ul>