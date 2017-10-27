---
layout: base/bar/bar-sidebar-none
title: "Faculty"
---

## Faculty
{% assign faculty = (site.people | person_has_role: 'faculty') %}
{% include peopletable.md people=faculty %}
