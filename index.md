---
layout: base/bar-sidebar-none
title: "HCI & Design at the University of Washington"
title_bar: "Design. Use. Build."
title_secondary: "HCI & Design at the University of Washington"
---

<!-- Carousel -->
<div class="row" id="carousel">
  <div class="col-md-12">
    <div id="carousel-main" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
        <li data-target="#carousel-example-generic" data-slide-to="1"></li>
        <li data-target="#carousel-example-generic" data-slide-to="2"></li>
{% comment %}        
        <li data-target="#carousel-example-generic" data-slide-to="3"></li>
        <li data-target="#carousel-example-generic" data-slide-to="4"></li>
{% endcomment %}        
      </ol>

      <!-- Wrapper for slides -->
      <div class="carousel-inner" role="listbox">
        <div class="item active">
          <img src="{{ site.baseurl }}/images/slide_design.jpg" alt="design">
          <div class="carousel-caption">
            <h2>Design.</h2>
            <p>Applying design thinking to improve the future.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_use.jpg" alt="use">
          <div class="carousel-caption">
            <h2>Use.</h2>
            <p>Creating better user experiences with technology.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_build.jpg" alt="build">
          <div class="carousel-caption">
            <h2>Build.</h2>
            <p>Prototyping and developing new technologies.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
{% comment %}        
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_research.jpg" alt="research">
          <div class="carousel-caption">
            <h2>Research</h2>
            <p>Students, faculty and industry collaborators work together on world-class research at UW.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_education.jpg" alt="education">
          <div class="carousel-caption">
            <h2>Education</h2>
            <p>Students regularly participate in discussions about HCI with UW faculty and peers.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
{% endcomment %}        
      </div>

      <!-- Controls -->
      <a class="left carousel-control" href="#carousel-main" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#carousel-main" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
</div>
<!-- Carousel End -->

<!-- Footer -->
<div class="row" id="footer">
  <div class="col-md-4" markdown="block">
## What is DUB?

DUB is a grassroots alliance of faculty, students, researchers, and industry partners
interested in Human Computer Interaction & Design research and education at the University of Washington.

The mission of DUB is to bring together an interdisciplinary set of people to share ideas,
collaborate on research, and discuss teaching related to the interaction between
design, people, and technology.
  </div>
  <div class="col-md-4">
    <section>
      <h2>Upcoming Seminars</h2>
      {% assign currentDate = site.time %}
      {% assign upcoming = site.seminars | seminar_upcoming: currentDate %}
      {% for item_seminar in upcoming limit: 2 %}
        <div class="row upcomingseminar">
          <div class="col-xs-4">
            <strong>{{ item_seminar.date | date: "%b %-d" | upcase }}</strong>
          </div>
          <div class="col-xs-8 text-right">
            {{ item_seminar.location }}
            {{ item_seminar.time }}
          </div>
          <div class="col-xs-12">
            <strong><a href="{{ site.baseurl }}{{ item_seminar.url }}">{{ item_seminar.title }}</a></strong>
          </div>
        </div>
      {% endfor %}
      <div class="row upcomingfullcalendar">
        <div class="col-xs-12">
          <hr />
        </div>
        <div class="col-xs-12 text-center">
            <p>
              <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span>
              &emsp;
              <a href="{{ site.baseurl }}/calendar.html">View Full Calendar</a>
            </p>
        </div>
      </div>
    </section>
  </div>
  <div class="col-md-4">
    <section>
      <h2>Connect with DUB</h2>
      <p>Join us in one of the world's most vibrant communities for research and education addressing all aspects of Human Computer Interaction & Design.</p>
      <a href="{{ site.baseurl }}/aboutdub.html">
        <p><img src="{{ site.baseurl }}/images/connect_uw.png" class="connecticon" alt="u dub"><strong>Learn</strong> about DUB.</p>
      </a>
      <a href="{{ site.baseurl }}/gettinginvolved.html#tab_mailing_lists">
        <p><img src="{{ site.baseurl }}/images/connect_email.png" class="connecticon" alt="e-mail"><strong>Join</strong> the DUB mailing lists.</p>
      </a>
      <a href="http://twitter.com/#!/uwdub">
        <p><img src="{{ site.baseurl }}/images/connect_twitter.png" class="connecticon" alt="twitter"><strong>Follow</strong> us on Twitter.</p>
      </a>
    </section>
  </div>
</div>
<!-- Footer End -->
