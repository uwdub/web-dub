{% assign people = include.people | sort: 'name' %}
{% assign peoplesize = people | size %}
{% assign peoplemod = peoplesize | modulo: 2 %}
{% assign peoplesplit = peoplesize | divided_by: 2 | plus: peoplemod %}

<html>
  <section>
    <div class="row">
      {% for item_person in people %} 
        {% assign photo_path = item_person.path | split:"." | first | append:".jpg" %}
        {% capture photo_exists %}{% file_exists {{ photo_path }} %}{% endcapture %}
        {% if photo_exists == 'true' %}
          {% assign photo_url = photo_path | remove: "_" | prepend: "/" | prepend: site.baseurl %}
        {% else %}
          {% assign photo_url = "default.jpg" | prepend: "/people/" | prepend: site.baseurl %}
        {% endif %}
        <div class="media col-md-4">
          <div class="media-left">
            <div class="media-object">
              {% assign assuming_photo_exists_url = photo_path | prepend: "/" | prepend: site.baseurl %}
              <img src="{{ photo_url }}" class="img-circle"/>
            </div>
          </div>
          <div class="media-body">
            <h4 class="media-heading">
              <a href="{{ item_person.web }}">
                {% for item_name in item_person.name offset: 1 %}
                  {{ item_name }}
                {% endfor %}
                {{ item_person.name[0] }}
                {{index}}
              </a>
            </h4>
            {% for item_position in item_person.positions %}
              {{ item_position.affiliation }}
              <br />
            {% endfor %}
            <br />
          </div>
        </div>
        {% assign loopindex = forloop.index | modulo: 3 %}
        {% if loopindex == 0 %}
          <div class="col-md-12"></div>
        {% endif %}
      {% endfor %}
    </div>
  </section>
</html>
