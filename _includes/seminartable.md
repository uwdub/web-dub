{% if include.seminars == "upcoming" %}
  {% assign seminars = site.seminars | seminar_upcoming: site.time | sort: 'date' %}
{% elsif include.seminars == "previous" %}
  {% assign seminars = site.seminars | seminar_previous: site.time | sort: 'date' | reverse %}
{% endif %}

<html>
  <section>
    <div class="row">
        <div class="col-xs-12">
          <hr />
        </div>
      {% for item_seminar in seminars %}
        <div class="col-md-3">
          <div class="col-xs-12">
            <h4 class="tableheading">
              {{ item_seminar.date | date: "%m/%d/%y"}}
            </h4>
          </div>
          {% if include.seminars == "upcoming" %}
            {% unless item_seminar.no_seminar == true %}
              <div class="col-xs-12">
                {{ item_seminar.time }}
              </div>
            {% endunless %}
            {% unless item_seminar.tbd_location %}
              <div class="col-xs-12">
                {{ item_seminar.location }}
              </div>
            {% endunless %}
          {% endif %}
        </div>
        <div class="col-md-9">
          {% unless item_seminar.tbd_title %}
            <div class="col-xs-12">
              {% if item_seminar.no_seminar == true %}
                <div class="tableheading text-muted no-seminar">
                  {{ item_seminar.title }}
                </div>
              {% else %}
                <h4 class="tableheading">
                  <a href="{{ item_seminar.url }}">{{ item_seminar.title }}</a>
                </h4>
              {% endif %}
            </div>
          {% else %}
            <div class="col-xs-12">
              <h4 class="tableheading">DUB Seminar</h4>
            </div>
          {% endunless %}
          {% unless item_seminar.tbd_speakers %}
            {% if item_seminar.speakers_no_collapse %}
              {% for item_speaker in item_seminar.speakers %}
                {% assign item_full_name = '' %}
                {% for item_name in item_speaker.name offset: 1 %}
                  {% assign item_full_name = item_full_name | append: ' ' | append: item_name %}
                  {% if forloop.last %}
                    {% assign item_full_name = item_full_name | append: ' ' | append: item_speaker.name[0] %}
                  {% endif %}
                {% endfor %}
                <div class="col-xs-12">
                  {{ item_full_name }}
                </div>
                {% unless item_speaker.affiliation == 'None' %}
                  <div class="text-muted col-xs-12">
                    {{ item_speaker.affiliation }}
                  </div>
                {% endunless %}
              {% endfor %}
            {% else %}
              {% assign item_affiliations = '' | split: ',' %}
              {% for item_speaker in item_seminar.speakers %}
                {% if item_speaker.affiliation_none %}
                  {% assign item_affiliations = item_affiliations | push: 'None' | uniq %}
                {% else %}
                  {% assign item_affiliations = item_affiliations | push: item_speaker.affiliation | uniq %}
                {% endif %}
              {% endfor %}
            
              {% for item_affiliation in item_affiliations %}
                {% assign item_affiliation_speakers = '' | split: ',' %}
                {% if item_affiliation == 'None' %}
                  {% for item_speaker in item_seminar.speakers %}
                    {% if item_speaker.affiliation_none %}
                      {% assign item_affiliation_speakers = item_affiliation_speakers | push: item_speaker %}
                    {% endif %}
                  {% endfor %}
                {% else %}
                  {% for item_speaker in item_seminar.speakers %}
                    {% if item_speaker.affiliation == item_affiliation %}
                      {% assign item_affiliation_speakers = item_affiliation_speakers | push: item_speaker %}
                    {% endif %}
                  {% endfor %}
                {% endif %}

                {% assign item_affiliation_names = '' | split: ' ' %}
                {% for item_speaker in item_affiliation_speakers %}
                  {% assign item_full_name = '' %}
                  {% for item_name in item_speaker.name offset: 1 %}
                    {% assign item_full_name = item_full_name | append: ' ' | append: item_name %}
                    {% if forloop.last %}
                      {% assign item_full_name = item_full_name | append: ' ' | append: item_speaker.name[0] %}
                    {% endif %}
                  {% endfor %}
                  {% assign item_affiliation_names = item_affiliation_names | push: item_full_name %}
                {% endfor %}
              
                <div class="col-xs-12">
                  {{ item_affiliation_names | join: ', ' }}
                </div>
                {% unless item_affiliation == 'None' %}
                  <div class="text-muted col-xs-12">
                    {{ item_affiliation }}
                  </div>
                {% endunless %}
              {% endfor %}
            {% endif %}
          {% endunless %}
        </div>
        <div class="col-xs-12">
          <hr />
        </div>
      {% endfor %}
    </div>
  </section>
</html>
