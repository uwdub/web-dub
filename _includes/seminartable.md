{% if include.seminars == "upcoming" %}
  {% assign seminars = site.seminars | seminar_upcoming: site.time | sort: 'date' %}
{% elsif include.seminars == "previous" %}
  {% assign seminars = site.seminars | seminar_previous: site.time | sort: 'date' | reverse %}
{% endif %}

<html>
  <section>
    <div class="row">
      {% for item_seminar in seminars %}
        <div class="col-md-3">
          <div class="col-xs-12">
            <h4 class="tableheading">
              {{ item_seminar.date | date: "%m/%d/%y"}}
            </h4>
          </div>
          {% if include.seminars == "upcoming" %}
            <div class="col-xs-12">
              {% unless item_seminar.tbd_location %}
                {{ item_seminar.location }}
                <br class="md-hidden"/>
              {% endunless %}
              {{ item_seminar.time }}
            </div>
          {% elsif include.seminars == "previous" %}
            <div class="col-md-12 hidden-xs hidden-sm">
              {% unless item_seminar.tbd_video %}
                {% assign vimeo_url = "https://vimeo.com/" | append: item_seminar.video %}
                <a href="{{ vimeo_url }}" target="new">
                  <img src="{{ site.baseurl }}/images/vimeo_icon.png" alt="vimeo" class="vimeo-icon">
                </a>
              {% endunless %}
            </div>
          {% endif %}
        </div>
        <div class="col-md-9">
          {% unless item_seminar.tbd_title %}
            <div class="col-xs-12">
              <h4 class="tableheading">            
                <a href="{{ item_seminar.url }}">{{ item_seminar.title }}</a>
              </h4>
            </div>
          {% else %}
            <div class="col-xs-12">
              <h4 class="tableheading">DUB Seminar</h4>
            </div>
          {% endunless %}
          {% unless item_seminar.tbd_speakers %}
            {% assign item_affiliations = '' | split: ',' %}
            {% for item_speaker in item_seminar.speakers %}
              {% assign item_affiliations = item_affiliations | push: item_speaker.affiliation | uniq %}
            {% endfor %}
            {% for item_affiliation in item_affiliations %}
              {% assign item_affiliation_names = '' | split: ' ' %}
              {% for item_speaker in item_seminar.speakers %}
                {% if item_speaker.affiliation == item_affiliation %}
                  {% assign item_full_name = '' %}
                  {% for item_name in item_speaker.name offset: 1 %}
                    {% assign item_full_name = item_full_name | append: ' ' | append: item_name %}
                    {% if forloop.last %}
                      {% assign item_full_name = item_full_name | append: ' ' | append: item_speaker.name[0] %}
                    {% endif %}
                  {% endfor %}
                  {% assign item_affiliation_names = item_affiliation_names | push: item_full_name %}
                {% endif %}
              {% endfor %}
              <div class="col-xs-12">
                {{ item_affiliation_names | join: ', ' }}
              </div>
              <div class="text-muted col-xs-12">
                {{ item_affiliation }}
              </div>
            {% endfor %}
          {% endunless %}
          <div class="col-xs-12 hidden-md hidden-lg">
            {% unless item_seminar.tbd_video %}
              {% assign vimeo_url = "https://vimeo.com/" | append: item_seminar.video %}
              <a href="{{ vimeo_url }}" target="new">Video</a>
            {% endunless %}
          </div>
        </div>
        <div class="col-xs-12">
          <hr />
        </div>
      {% endfor %}
    </div>
  </section>
</html>
