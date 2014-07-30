---
layout: default
title: James Fogarty
---

<div class="row-fluid">
    <div class="span4">
        <p><img src="{{ site.baseurl }}/img/jfogarty.jpg" class="img-responsive" alt="James Fogarty" width="300"></p>
    </div>
    <div class="span4">
        <div class="nowrap">
{% capture m %}
Associate Professor<br/>
Computer Science & Engineering<br/>
University of Washington
{% endcapture %}
{{ m | markdownify }}
        </div>
        <div class="nowrap fontsmall">
{% capture m %}
Paul G. Allen Center, Room 666<br/>
jfogarty [at] cs [dot] washington [dot] edu<br/>
{% endcapture %}
{{ m | markdownify }}
        </div>
    </div>
    <div class="span4">
        <div class="panel-group" id="contactAccordion">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <div class="panel-title">
                        <div class="accordion-toggle nowrap fontsmall marginbottom" data-toggle="collapse" data-parent="#contactAccordion" href="#contactAccordionOne">
                            Mailing Address &raquo;
                        </div>
                    </div>
                </div>
                <div id="contactAccordionOne" class="panel-collapse collapse">
                    <div class="panel-body nowrap fontsmall marginleft">
{% capture m %}
Computer Science &amp; Engineering<br/>
University of Washington<br/>
AC 101, Box 352350<br/>
Seattle, WA 98195
{% endcapture %}
{{ m | markdownify }}
                    </div>
                </div>
            </div>
            <div class="panel panel-default">
                <div class="panel-heading">
                    <div class="panel-title">
                        <div class="accordion-toggle nowrap fontsmall marginbottom" data-toggle="collapse" data-parent="#contactAccordion" href="#contactAccordionTwo">
                            Research Coordinator &raquo;
                        </div>
                    </div>
                </div>
                <div id="contactAccordionTwo" class="panel-collapse collapse">
                    <div class="panel-body nowrap fontsmall marginleft">
{% capture m %}
Melody Kadenko<br/>
melody [at] cs [dot] washington [dot] edu
{% endcapture %}
{{ m | markdownify }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row-fluid marginbottom">
</div>

<div class="row-fluid">
    <div class="span12">
{% capture m %}
I am an Associate Professor of Computer Science & Engineering at the University of Washington. I am also a core member of the DUB Group, our cross-campus initiative advancing Human-Computer Interaction and Design research and education.

My broad research interests are in Human-Computer Interaction, User Interface Software and Technology, and Ubiquitous Computing. My focus is on developing, deploying, and evaluating new approaches to the human obstacles surrounding widespread everyday adoption of ubiquitous sensing and intelligent computing technologies.

I pursue this work together with an outstanding group of collaborators and am fortunate to advise amazing students:

* [Felicia Cordeiro](http://www.feliciacordeiro.com/)
* [Morgan Dixon](http://homes.cs.washington.edu/~mdixon/)
* [Daniel Epstein](http://www.depstein.net/)
* [Katie Kuksenok](http://students.washington.edu/kuksenok/blog/about/)
* [Greg Nelson](http://www.greglnelson.info/)
* [Conrad Nied](http://homes.cs.washington.edu/~anied/)

My research has been generously supported by the National Science Foundation, FXPAL, Google, Intel, and Microsoft.
{% endcapture %}
{{ m | markdownify }}
    </div>
</div>