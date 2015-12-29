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
          {% for item_speaker in item_publish_speakers %}
            <div class="col-xs-12">
              {% for item_name in item_speaker.name offset:1 %}
                {{ item_name }}
              {% endfor %}
              {{ item_speaker.name[0] }}
            </div>
            <div class="col-xs-12">
              {{ item_speaker.affiliation }}
            </div>
          {% endfor %}
        </div>
        <div class="col-md-12">
          <hr />
        </div>
      {% endfor %}
    </div>
  </section>
</html>
