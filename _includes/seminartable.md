{% if include.seminars == "upcoming" %}
  {% assign seminars = site.seminars | seminar_upcoming: site.time | sort: 'date' %}
{% elsif include.seminars == "previous" %}
  {% assign seminars = site.seminars | seminar_previous: site.time | sort: 'date' | reverse %}
{% endif %}

<html>
  <section>
    <div class="row">
      {% for item_seminar in seminars %}
        {% if item_seminar.tbd %}
          {% assign item_publish_speakers = null %}
          {% assign item_publish_title = "TBD" %}
        {% else %}
          {% assign item_publish_speakers = item_seminar.speakers %}
          {% assign item_publish_title = item_seminar.title %}
        {% endif %}
        <div class="col-md-3">
          <div class="col-xs-12">
            <h4>
              {{ item_seminar.date | date: "%m/%d/%y"}}
            </h4>
          </div>
          <div class="col-xs-12">
            {{ item_seminar.time }}&nbsp;
          </div>
          <div class="col-xs-12">
            {{ item_seminar.location }}
          </div>
        </div>
        <div class="col-md-9">
          <div class="col-xs-12">
            <h4>            
              <a href="{{ item_seminar.url }}">
                {{ item_publish_title }}
              </a>
            </h4>
          </div>
          {% assign item_affiliations = '' | split: ',' %}
          {% if item_publish_speakers && item_publish_speakers.size > 0 %}
            {% for item_speaker in item_publish_speakers %}
              {% assign item_affiliations = item_affiliations | push: item_speaker.affiliation | uniq %}
            {% endfor %}
          {% endif %}
          {% for item_affiliation in item_affiliations %}
            {% assign item_affiliation_names = '' | split: ' ' %}
            {% for item_speaker in item_publish_speakers %}
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
        </div>
        <div class="col-xs-12">
          <hr />
        </div>
      {% endfor %}
    </div>
  </section>
</html>
