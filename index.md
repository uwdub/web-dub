---
layout: base/bar/bar-sidebar-none
title: "HCI & Design at the University of Washington"
title_bar: "Design. Use. Build."
title_bar_secondary: "HCI & Design at the University of Washington"
---

<!-- Carousel -->
<div class="row" id="carousel">
  <div class="col-md-12">
    <div id="carousel-main" class="carousel slide" data-ride="carousel" data-interval="10000">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#carousel-main" data-slide-to="0" class="active"></li>
        <li data-target="#carousel-main" data-slide-to="1"></li>
        <li data-target="#carousel-main" data-slide-to="2"></li>              
        <li data-target="#carousel-main" data-slide-to="3"></li>        
      </ol>

      <!-- Wrapper for slides -->
      <div class="carousel-inner" role="listbox">
        <div class="item active">
        
          <img src="{{ site.baseurl }}/posts/2022/chi2022_slide.jpg" alt="CHI 2022 Banner">
          <div class="carousel-caption">
            <div class="carousel-caption-inner">
            <h2>DUB at CHI 2022</h2>
            <p>
                HCI & Design at the University of Washington<br>has a large and quality presence at CHI 2022.
            </p>
            <p>
              <a href="{{ site.baseurl }}/posts/2022/chi2022papers.html" class="btn btn-default btn-lg">
                UW Research at CHI 2022
              </a>
            </p>
            </div>
          </div>
        </div>
        <div class="item">
        
          <img src="{{ site.baseurl }}/images/slide_design.jpg" alt="design">
          <div class="carousel-caption">
            <div class="carousel-caption-inner">
            <h2>Design</h2>
            <p>Applying design to improve the future.</p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_use.jpg" alt="use">
          <div class="carousel-caption">
            <div class="carousel-caption-inner">
            <h2>Use</h2>
            <p>Creating better experiences with technology.</p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_build.jpg" alt="build">
          <div class="carousel-caption">
            <div class="carousel-caption-inner">
            <h2>Build</h2>
            <p>Prototyping and developing new technologies.</p>
            </div>
          </div>
        </div>       
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

DUB is a grassroots alliance of faculty, students, researchers, and
industry partners interested in Human Computer Interaction & Design at the 
University of Washington. 

Our mission is to bring together an interdisciplinary group of people to share ideas, 
collaborate on research, and advance teaching related to the interaction between design, people, and technology.

</div>
    </section>
  </div>
  <div class="col-md-4 footer-panel">
    <section class="footer-content">
      <h2>Upcoming Seminars</h2>
      <div class="calendar-feed">
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
              {% unless item_seminar.no_seminar %}
                {{ item_seminar.time }}
              {% endunless %}
            </div>
            <div class="col-xs-12">

              {% unless item_seminar.tbd_title %}
                {% unless item_seminar.no_seminar %}
                  <a href="{{ site.baseurl }}{{ item_seminar.url }}">{{ item_seminar.title }}</a>
                {% else %}
                  <div class="text-muted no-seminar">
                    {{ item_seminar.title }}
                  </div>
                {% endunless %}
              {% else %}
                DUB Seminar
              {% endunless %}

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
        <div class="col-xs-12 calendar-button">
        <a href="{{ site.baseurl }}/seminar.html" type="button" class="btn btn-default btn-block">View Full Calendar</a>
        </div>
      </div>
    </section>
  </div>
  <div class="col-md-4 footer-panel">
    <section class="footer-content">
      <h2>Connect with DUB</h2>
      <p class="connect-text">Join one of the world's most vibrant communities for research and education addressing all aspects of Human Computer Interaction & Design.</p>
      <div class="icon-bottom">
        <a href="{{ site.baseurl }}/gettinginvolved.html#tab_mailing_lists">
          <p>
            <img src="{{ site.baseurl }}/images/connect_email.png" class="connecticon" alt="e-mail">
            <span class="icon-link-text"><strong>Join</strong> the mailing lists</span>
          </p>
        </a>
        <a href="http://twitter.com/#!/uwdub">
          <p>
            <img src="{{ site.baseurl }}/images/connect_twitter.png" class="connecticon" alt="twitter">
            <span class="icon-link-text"><strong>Tweet</strong> @uwdub</span>
          </p>
        </a>
        <a href="http://vimeo.com/designusebuild">
          <p>
            <img src="{{ site.baseurl }}/images/connect_vimeo.png" class="connecticon" alt="vimeo">
            <span class="icon-link-text"><strong>Follow</strong> us on Vimeo</span>
          </p>
        </a>
        <a href="https://medium.com/hci-design-at-uw">
          <p>
            <img src="{{ site.baseurl }}/images/connect_medium.png" class="connecticon" alt="medium">
            <span class="icon-link-text"><strong>Read</strong> more on Medium</span>
          </p>
        </a>
      </div>
    </section>
  </div>
</div>
<!-- Footer End -->
