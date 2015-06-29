{% assign people = include.people | sort: 'name' %}
{% assign peoplesize = people | size %}
{% assign peoplemod = peoplesize | modulo: 2 %}
{% assign peoplesplit = peoplesize | divided_by: 2 | plus: peoplemod %}

<html>
<section>
<div class="row">
  <div class="col-md-6">
    <ul>
{% for item_person in people limit: peoplesplit %}  
  <li><a href="{{ item_person.url }}">
  {% for item_name in item_person.name offset: 1 %}
    {{ item_name }}
  {% endfor %}
  {{ item_person.name[0] }}
  </a></li>
{% endfor %}
    </ul>
  </div>
  <div class="col-md-6">
    <ul>
{% for item_person in people offset: peoplesplit %}  
  <li><a href="{{ item_person.url }}">
  {% for item_name in item_person.name offset: 1 %}
    {{ item_name }}
  {% endfor %}
  {{ item_person.name[0] }}
  </a></li>
{% endfor %}
    </ul>
  </div>
</div>
</section>
</html>
