---
layout: base/bar/bar-sidebar-right
title: "Calendar"
title_secondary: "HCI & Design at the University of Washington"
---

<div class="sidebar_start"></div>

<ul id="seminar-tabs" class="nav nav-pills nav-stacked" data-tabs="tabs">
  <li class="active"><a href="#upcoming_seminars" data-toggle="tab">Upcoming Seminars</a></li>
  <li><a href="#previous_seminars" data-toggle="tab">Previous Seminars</a></li>
</ul>

<div class="sidebar_end"></div>

<div id="seminar-tabs-content" class="tab-content">
  <div class="tab-pane active" id="upcoming_seminars" markdown="block">
# Upcoming DUB Seminars
{% include seminartable.md seminars="upcoming" %}
  </div>
  <div class="tab-pane" id="previous_seminars" markdown="block">
# Previous DUB Seminars
{% include seminartable.md seminars="previous" %}
  </div>
</div>
