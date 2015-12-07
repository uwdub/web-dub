---
layout: base/bar-sidebar-right
title: "Calendar"
title_secondary: "HCI & Design at the University of Washington"
---

<div class="sidebar_start"></div>
  <a href="#" class="list-group-item active">Upcoming Seminars</a>
  <a href="/previousseminars.html" class="list-group-item">Previous Seminars</a>
<div class="sidebar_end"></div>

# Upcoming DUB Seminars
{% assign current = (site.seminars | ) %}
{% include seminartable.md seminars = current %}

