---
layout: base/bar/bar-sidebar-right
title: "DUB Seminar"
---

<div class="sidebar_start"></div>

<h4>Seminar Schedule</h4>
<ul id="seminar-tabs" class="nav nav-pills nav-stacked" data-tabs="tabs">
  <li class="active"><a href="#upcoming_seminars" data-toggle="tab">Upcoming Seminars</a></li>
  <li><a href="#previous_seminars" data-toggle="tab">Previous Seminars</a></li>
</ul>

<h4>Calendar Subscriptions</h4>
<ul class="nav nav-pills nav-stacked">
    <li><a href="https://calendar.google.com/calendar/r?cid=webcal%3A%2F%2Fdub.washington.edu%2Fcalendar.ics">Google Calendar</a></li>
    <li><a href="webcal://dub.washington.edu/calendar.ics">iCal / Webcal</a></li>
</ul>

<div class="sidebar_end"></div>

The weekly DUB seminar is the primary gathering point for the DUB community.
The seminar features talks from diverse leading perspectives in Human Computer Interaction & Design,
presented by members of the DUB community and by visiting researchers and practitioners.
All members of the DUB community are welcome and encouraged to attend the weekly DUB seminar.

- If you are interested in hosting a DUB speaker, or are yourself interested in speaking in the DUB seminar,
contact the [DUB Seminar Coordinators]({{ site.baseurl }}/gettinginvolved.html#tab_coordinators) 
via email at speak [at] dub [dot] washington [dot] edu. 

- If you are interested in presenting a paper in our DUB Shorts format, submit our form:
  
  <https://tiny.cc/uwdubshorts>

Seminars begin with some time for socializing, and then transition to the talk.
Seminars during the academic year often attract 100 to 120 people,
with seminars during the summer more often attracting 60 to 80 people. 
The seminar can also be taken for credit in various programs.

Seminar announcements are distributed on the [DUB mailing lists]({{ site.baseurl }}/gettinginvolved.html#tab_mailing_lists_and_slack).

With speaker permission, 
videos are posted in [Previous Seminars]({{ site.baseurl }}/seminar.html#tab_previous_seminars)
and the [DUB Vimeo channel](http://vimeo.com/designusebuild).

The DUB seminar schedule is coordinated through grassroots identification of compelling speakers.
This generally leverages a potential speaker's existing plans for visiting the University of Washington community,
but very limited support is available in situations where costs would be a barrier to a potential speaker.

<div id="seminar-tabs-content" class="tab-content" markdown="block">

<!----------------------------------------------------------------------------->

  <div class="tab-pane active" id="upcoming_seminars" markdown="block">
## Upcoming DUB Seminars
{% include seminartable.md seminars="upcoming" %}
  </div>

<!----------------------------------------------------------------------------->

  <div class="tab-pane" id="previous_seminars" markdown="block">
## Previous DUB Seminars
{% include seminartable.md seminars="previous" %}
  </div>

<!----------------------------------------------------------------------------->

</div>
