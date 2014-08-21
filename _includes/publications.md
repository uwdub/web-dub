{% assign param_id_author = include.id_author %}

{% assign filtered_journalpapers = site.data.journalpapers | id_author: param_id_author %}
{% assign filtered_conferencepapers = site.data.conferencepapers | id_author: param_id_author %}
{% assign filtered_workshoppapers = site.data.workshoppapers | id_author: param_id_author %}

{% if filtered_journalpapers.size > 0 %}
## Journal Articles
<table class="table table-bordered">
  {% for item_paper in filtered_journalpapers %}
    {% assign id_paper = item_paper[0] %}
    {% include publication.md type="journalpaper" id=id_paper %}
  {% endfor %}
</table>
{% endif %}

{% if filtered_conferencepapers.size > 0 %}
## Conference Articles
<table class="table table-bordered">
  {% for item_paper in filtered_conferencepapers %}
    {% assign id_paper = item_paper[0] %}
    {% include publication.md type="conferencepaper" id=id_paper %}
  {% endfor %}
</table>
{% endif %}

{% if filtered_workshoppapers.size > 0 %}
## Workshop Papers
<table class="table table-bordered">
  {% for item_paper in filtered_workshoppapers %}
    {% assign id_paper = item_paper[0] %}
    {% include publication.md type="workshoppaper" id=id_paper %}
  {% endfor %}
</table>
{% endif %}

