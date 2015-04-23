---
layout: main-no-sidebar
# title: "HCI & Design at the University of Washington"
current_page_item: "people"
---

<html>
<ul>
{% for item_person in site.people %}
  <li><a href="{{ item_person.url }}">
  {% for item_name in item_person.name offset:1 %}
    {{ item_name }}
  {% endfor %}
  {{ item_person.name[0] }}
  </a></li>
{% endfor %}
</ul>
</html>
  
  
