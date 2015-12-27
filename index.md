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
        <li data-target="#carousel-example-generic" data-slide-to="3"></li>
      </ol>

      <!-- Wrapper for slides -->
      <div class="carousel-inner" role="listbox">
        <div class="item active">
          <img src="{{ site.baseurl }}/images/slide_design.jpg" alt="design">
          <div class="carousel-caption">
            <h2>Design.</h2>
            <p>Design is becoming increasingly recognized as an important aspect of technology.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_use.jpg" alt="use">
          <div class="carousel-caption">
            <h2>Use.</h2>
            <p>Students and faculty work on research to make technology and products more usable.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_build.jpg" alt="build">
          <div class="carousel-caption">
            <h2>Build.</h2>
            <p>Students get hands-on experience prototyping and building products in class and in labs.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
          </div>
        </div>
        <div class="item">
          <img src="{{ site.baseurl }}/images/slide_dub.jpg" alt="dub">
          <div class="carousel-caption">
            <h2>DUB</h2>
            <p>DUB is a community that comes together to share ideas about human-computer interaction and design.</p>
            <!-- <a href="#" class="btn btn-default btn-lg">Learn more</a> -->
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
  <div class="col-md-4">
    <section>
      <h2>What is DUB?</h2>      
      <p>The DUB group is a grassroots, opt-in alliance of faculty, students, researchers, and industry affiliates interested in human-computer interaction and design at the University of Washington.</p>
      <p>The mission of DUB is to bring together an interdisciplinary set of people to discuss issues, share ideas, collaborate on research projects, and discuss teaching concerns related to the interaction between people and computers and major socio-technical phenomena surrounding them.</p>
      </section>
  </div>
  <div class="col-md-4">
    <section>
      <h2>Upcoming DUB Seminars</h2>
      {% assign currentDate = site.time %}
      {% assign upcoming = site.seminars | seminar_upcoming: currentDate %}
      {% if upcoming == empty %}
        No upcoming seminars have yet been scheduled.
      {% else %}
        {% for item_seminar in upcoming limit: 2 %}
          <div class = "row">
            <div class="col-md-2">
              {{ item_seminar.date | date: "%b" | upcase }}
              {{ item_seminar.date | date: "%-d"}}
            </div>
            <div class="col-md-10">
              <p>
                <a href="{{ item_seminar.url }}">
                  {{ item_seminar.title }}
                </a>
              </p>
              <p>
                <strong>
                  {{ item_seminar.time }}
                  &emsp;&emsp;
                  {{ item_seminar.location }}
                </strong>
              </p>
            </div>
          </div>
        {% endfor %}
      </div>
      {% endif %}
      <div class = "row">
        <div class="col-md-12"><hr /></div>
        <div class="col-md-2"></div>
        <div class="col-md-10">
          <p>
            <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span>
            &emsp;
            <a href="/calendar.html">View Full Calendar</a>
          </p>
        </div>
      </div>
    </section>
  </div>
  <div class="col-md-4">
    <section>
      <h2>Connect with DUB</h2>
      <p>Want to join one of the most vibrant HCI & Design communities in the world?</p>
      <p><a href="/mailinglists.html"><img src="logos/E-mail.png" alt="e-mail"></a>&nbsp;&nbsp;<strong>Join</strong> the DUB mailing list.</p>
      <p><a href="http://twitter.com/#!/uwdub"><img src="logos/Twitter.png" alt="twitter"></a>&nbsp;&nbsp;<strong>Follow</strong> us on Twitter.</p>
      <p><a href="/gettinginvolved.html"><img src="logos/UW.png" alt="u dub"></a>&nbsp;&nbsp;<strong>Learn</strong> how to get involved.</p>
    </section>
  </div>
</div>
<!-- Footer End -->
