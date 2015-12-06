---
layout: base/bar-sidebar-right
title: "Previous Seminars"
title_secondary: "HCI & Design at the University of Washington"
---

<div class="sidebar_start"></div>
  <a href="/calendar.html" class="list-group-item">Upcoming Seminars</a>
  <a href="#" class="list-group-item active">Previous Seminars</a>
<div class="sidebar_end"></div>

# Previous DUB Seminars
{% assign previous = (site.seminars) %}
{% include seminartable.md seminars = previous %}