{% assign seminars = include.seminars | sort: 'date' %}

<html>
  <section>
    <div class="row">
      <div class="col-md-12">
        {% for item_seminar in seminars %}
          <h4>
          {{ item_seminar.title }}
          </h4>
          {{ item_seminar.date | date: '%B %d, %Y'}}
          <br />
          {% for item_names in item_seminar.name %}
              {% for item_name in item_names offset: 1 %}
                {{ item_name }}
              {% endfor %}
              {{ item_names[0] }}
              <br />
          {% endfor %}
          {{ item_seminar.affiliation }}
          <br />
          {{ item_seminar.location }}
          <br />
          <a href="{{ item_seminar.url }}">
            Read more...
          </a>
        {% endfor %}
       </div>
    </div>
  </section>
</html>
