{% assign people = include.people | sort: 'name' %}
{% assign peoplesize = people | size %}
{% assign peoplemod = peoplesize | modulo: 2 %}
{% assign peoplesplit = peoplesize | divided_by: 2 | plus: peoplemod %}

<html>
  <section>
    <div class="row">
      {% for item_person in people %} 
        <div class="media col-md-6">
          <div class="media-left">
            <div class="media-object">
              <img src="{{ site.baseurl }}/logos/twitter.png" class="img-circle"/>
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
            {% for item_position in item_person.position %}
              {{ item_position.unit }}
              <br />
            {% endfor %}
            <br />
          </div>
        </div>
        {% assign loopindex = forloop.index | modulo: 2 %}
        {% if loopindex == 0 %}
          <div class="col-md-12"></div>
        {% endif %}
      {% endfor %}
    </div>
  </section>
</html>
