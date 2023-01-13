{% if include.location == "CSE2/Gates 401 - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/cse2" target="_blank">{{ include.location }}</a>
{% elsif include.location == "MHCI+D Studio - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/aho" target="_blank">{{ include.location }}</a>
{% else %}
{{ include.location }}
{% endif %}
