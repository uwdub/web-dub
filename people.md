---
layout: base/sidebar-none
title: "People"
---

## Faculty
{% assign faculty = (site.people | person_has_role: 'faculty') %}
{% include peopletable.md people=faculty %}

## Doctoral Students
{% assign doctoralstudents = (site.people | person_has_role: 'doctoral-student') %}
{% include peopletable.md people=doctoralstudents %}

## Masters Students
{% assign mastersstudents = (site.people | person_has_role: 'masters-student') %}
{% include peopletable.md people=mastersstudents %}
