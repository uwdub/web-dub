---
layout: base/bar-sidebar-right
title: "Calendar"
title_secondary: "HCI & Design at the University of Washington"
---

<div class="sidebar_start"></div>
  <a href="/calendar.html" class="list-group-item">Upcoming Seminars</a>
  <a href="#" class="list-group-item active">Previous Seminars</a>
<div class="sidebar_end"></div>

# Previous DUB Seminars
{% assign currentDate = site.time %}
{% assign previous = site.seminars | seminar_previous: currentDate %}
{% include seminartableprevious.md seminars = previous %}