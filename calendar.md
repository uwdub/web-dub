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
{% assign currentDate = site.time %}
{% assign upcoming = site.seminars | seminar_upcoming: currentDate %}
{% if upcoming == empty %}
  <br />
  No upcoming seminars have yet been scheduled. Please check back at a later date.
{% else %}
  {% include seminartable.md seminars = upcoming %}
{% endif %}

