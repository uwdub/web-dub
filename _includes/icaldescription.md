{% capture line_breaks %}
{% assign speakers = 'SPEAKER:\n\n' %}
{% assign abstract = 'ABSTRACT:\n\n' %}
{% assign bio = 'BIO:\n\n' %}
{% assign full_description = '' %}
{% unless item_seminar.tbd_speakers %}
   {% for item_speaker in item_seminar.speakers %}
       {% unless forloop.first %}
         {% assign speakers = speakers | append: '\n' %}
       {% endunless %}
       {% assign item_full_name = '' %}
       {% for item_name in item_speaker.name offset: 1 %}
         {% if forloop.first %}
           {% assign item_full_name = item_full_name | append: item_name %}
         {% else %}
           {% assign item_full_name = item_full_name | append: ' ' | append: item_name %}
         {% endif %}
         {% if forloop.last %}
           {% assign item_full_name = item_full_name | append: ' ' | append: item_speaker.name[0] %}
         {% endif %}
       {% endfor %}
       {% assign speakers = speakers | append: item_full_name %}
       {% unless item_speaker.affiliation_none %}
          {% assign speakers = speakers | append: ' (' | append: item_speaker.affiliation | append: ')' %}
       {% endunless %}
   {% endfor %}
   {% assign full_description = full_description | append: speakers %}
{% endunless %}
{% unless item_seminar.tbd_abstract %}
   {% assign abstract = abstract | append: item_seminar.abstract %}
   {% assign full_description = full_description | append: '\n\n' | append: abstract %}
{% endunless %}
{% unless item_seminar.tbd_bio %}
   {% assign bio = bio | append: item_seminar.bio %}
   {% assign full_description = full_description | append: '\n\n' | append: bio %}
{% endunless %}
{% assign full_description = full_description |
                                newline_to_br | strip_newlines | 
                                replace: '<br /><br />','\n\n' | 
                                replace: '<br />- ','\n- ' | 
                                replace: '<br />* ','\n- ' |          
                                remove: '<br />' %}
{% endcapture %}{% assign line_breaks = nil %}{{ full_description }}
