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
  <div class="col-md-4 footer-panel">
    <section class="footer-content">
      <div markdown="block">
## What is DUB?

DUB is a grassroots alliance of faculty, students, researchers, and industry partners
interested in Human Computer Interaction & Design research and education at the University of Washington.

The mission of DUB is to bring together an interdisciplinary set of people to share ideas,
collaborate on research, and discuss teaching related to the interaction between
design, people, and technology.
</div>
      <div class="row icon-bottom">
        <div class="col-xs-12">
          <a href="{{ site.baseurl }}/aboutdub.html">
            <p><img src="{{ site.baseurl }}/images/dub_icon.png" class="connecticon" alt="dub">Learn about DUB</p>
          </a>
        </div>
      </div>
    </section>
  </div>
  <div class="col-md-4 footer-panel">
    <section class="footer-content">
      <h2>Upcoming Seminars</h2>
      <div>
        {% assign upcoming = site.seminars | seminar_upcoming: site.time %}
        {% for item_seminar in upcoming limit: 2 %}
          <div class="row upcomingseminar">
            <div class="col-xs-4">
              <strong>{{ item_seminar.date | date: "%b %-d" | upcase }}</strong>
            </div>
            <div class="col-xs-8 text-right">
              {% unless item_seminar.tbd_location %}
                {{ item_seminar.location }}
              {% endunless %}
              {{ item_seminar.time }}
            </div>
            <div class="col-xs-12">
              <strong>
              {% unless item_seminar.tbd_title %}
                <a href="{{ site.baseurl }}{{ item_seminar.url }}">{{ item_seminar.title }}</a>
              {% else %}
                DUB Seminar
              {% endunless %}
              </strong>
            </div>
            <div class="col-xs-12">
              {% assign speaker_names = '' | split: ' ' %}
              {% for item_speaker in item_seminar.speakers %}
                {% assign item_full_name = '' %}
                {% for item_name in item_speaker.name offset: 1 %}
                  {% assign item_full_name = item_full_name | append: ' ' | append: item_name %}
                  {% if forloop.last %}
                    {% assign item_full_name = item_full_name | append: ' ' | append: item_speaker.name[0] %}
                  {% endif %}
                {% endfor %}
                {% assign speaker_names = speaker_names | push: item_full_name %}
              {% endfor %}
              {% assign speaker_names = speaker_names | join: ', ' %}
              {{ speaker_names}}
            </div>
          </div>
        {% endfor %}
      </div>
      <div class="row icon-bottom">
        <div class="col-xs-12">
          <div>
            <div class="col-md-12">
              <hr></hr>
            </div>
            <a href="{{ site.baseurl }}/calendar.html">
              <p><img src="{{ site.baseurl }}/images/calendar_icon.png" class="connecticon" alt="calendar">View Full Calendar</p>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
  <div class="col-md-4 footer-panel">
    <section class="footer-content">
      <h2>Connect with DUB</h2>
        <p class="connect-text">Join us in one of the world's most vibrant communities for research and education addressing all aspects of Human Computer Interaction & Design.</p>
      <div class="row connect-link">
        <div class="col-xs-12 connect-link-item">
          <a href="{{ site.baseurl }}/gettinginvolved.html#tab_mailing_lists">
            <p><img src="{{ site.baseurl }}/images/connect_email.png" class="connecticon" alt="e-mail"><strong>Join</strong> the DUB mailing lists</p>
          </a>
          <a href="http://twitter.com/#!/uwdub">
            <p><img src="{{ site.baseurl }}/images/connect_twitter.png" class="connecticon" alt="twitter"><strong>Tweet</strong>@uwdub</p>
          </a>
          <a href="http://vimeo.com/designusebuild">
            <p><img src="{{ site.baseurl }}/images/connect_vimeo.png" class="connecticon" alt="vimeo"><strong>Follow</strong> us on Vimeo</p>
          </a>
        </div>
      </div>
    </section>
  </div>
</div>
<!-- Footer End -->
