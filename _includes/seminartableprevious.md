{% assign seminars = include.seminars | sort: 'date' %}

<html>
  <section>
    <div class="row">
      <div class="col-md-12">
        {% for item_seminar in seminars reversed %}
          <div class="col-md-2">
            <h4>
              {{ item_seminar.date | date: "%m/%d/%y"}}
            </h4>
            {{ item_seminar.time }}
            &nbsp;{{ item_seminar.location }}
          </div>
          <div class="col-md-10">
            <h4>
              <a href="{{ item_seminar.url }}">
                {{ item_seminar.title }}
              </a>
            </h4>
            {% for item_names in item_seminar.name %}
                {% for item_name in item_names offset: 1 %}
                  {{ item_name }}
                {% endfor %}
                {{ item_names[0] }}
                <br />
            {% endfor %}
            {{ item_seminar.affiliation }}
          </div>
          <div class="col-md-12">
            <hr />
          </div>
        {% endfor %}
      </div>
    </div>
  </section>
</html>
