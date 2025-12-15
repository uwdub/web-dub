{% if include.location == "CSE/Allen 691" %}
<a href="https://www.washington.edu/maps/#!/cse" target="_blank">{{ include.location }}</a>
{% elsif include.location == "CSE2/Gates G20" %}
<a href="https://www.washington.edu/maps/#!/cse2" target="_blank">{{ include.location }}</a>
{% elsif include.location == "CSE2/Gates 271" %}
<a href="https://www.washington.edu/maps/#!/cse2" target="_blank">{{ include.location }}</a>
{% elsif include.location == "CSE2/Gates 371" %}
<a href="https://www.washington.edu/maps/#!/cse2" target="_blank">{{ include.location }}</a>
{% elsif include.location == "CSE2/Gates 401" %}
<a href="https://www.washington.edu/maps/#!/cse2" target="_blank">{{ include.location }}</a>
{% elsif include.location == "CSE2/Gates 401 - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/cse2" target="_blank">CSE2/Gates 401</a>
<br>Hybrid via Zoom
{% elsif include.location == "Kane 225" %}
<a href="https://www.washington.edu/maps/#!/kne" target="_blank">{{ include.location }}</a>
{% elsif include.location == "Kane 225 - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/kne" target="_blank">Kane 225</a>
<br>Hybrid via Zoom
{% elsif include.location == "HUB 160 - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/hub" target="_blank">HUB 160</a>
<br>Hybrid via Zoom
{% elsif include.location == "HUB 332 - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/hub" target="_blank">HUB 332</a>
<br>Hybrid via Zoom
{% elsif include.location == "HUB 334 - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/hub" target="_blank">HUB 334</a>
<br>Hybrid via Zoom
{% elsif include.location == "Oak Hall Denny Room" %}
<a href="https://www.washington.edu/maps/#!/oak" target="_blank">Oak Hall<br>Denny Room</a>
{% elsif include.location == "Oak Hall Denny Room - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/oak" target="_blank">Oak Hall<br>Denny Room</a>
<br>Hybrid via Zoom
{% elsif include.location == "MHCI+D Studio - Hybrid via Zoom" %}
<a href="https://www.washington.edu/maps/#!/aho" target="_blank">{{ include.location }}</a>
{% else %}
{{ include.location }}
{% endif %}
