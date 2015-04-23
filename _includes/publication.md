{% assign param_type = include.type %}
{% assign param_id = include.id %}

{% case param_type %}
{% when "journalpaper" %}
{% assign paper = site.data.journalpapers[param_id] %}
{% when "conferencepaper" %}
{% assign paper = site.data.conferencepapers[param_id] %}
{% when "workshoppaper" %}
{% assign paper = site.data.workshoppapers[param_id] %}
{% endcase %}

<tr>

    <td class="nowrap">
        <span class="fontsmall">
            <a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">local PDF</a>
            {% if paper.officialurl %}
            <br/>
            <a href="{{ paper.officialurl }}">official PDF</a>
            {% endif %}
        </span>
    </td>

{% case param_type %}
{% when "journalpaper" or "conferencepaper" %}
    <td width="90" height="90">
        <a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">
            <img src="{{ site.baseurl }}/publications/{{ paper.localthumb }}" width="90" height="90">
        </a>
    </td>
{% endcase %}

    <td>
        {% for id_author in paper.authors %}
        {% assign author = site.data.authors[id_author] %}
            {% for name in author['name'] offset:1 %}
                {% unless name.first %}
                    {{ name }}
                {% endunless %}
            {% endfor %}
            {{ author['name'][0] }}{% if forloop.last %}.{% else %},{% endif %}
        {% endfor %}
        <a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">{{ paper.title }}</a>.

{% case param_type %}
{% when "journalpaper" %}
        {% assign journal = site.data.journals[paper.journal] %}
        <i>{{ journal.longname }}</i>{% if journal.shortname %}<span class="nowrap"> ({{ journal.shortname }})</span>{% endif %}.
        <span class="nowrap">Vol. {{ paper.volume }},</span>
        <span class="nowrap">Iss. {{ paper.issue }},</span>
        <span class="nowrap">pp. {{ paper.pages }}.</span>
{% when "conferencepaper" %}
        {% assign conference = site.data.conferences[paper.conference] %}
        <i>{{ conference.longname }}</i>{% if conference.shortname %}<span class="nowrap"> ({{ conference.shortname }})</span>{% endif %}.
        {% if paper.pages %}
        <span class="nowrap">pp. {{ paper.pages }}.</span>
        {% endif %}
{% when "workshoppaper" %}
        {% assign workshop = site.data.workshops[paper.workshop] %}
        <i>{{ workshop.longname }}</i>{% if workshop.shortname %}<span class="nowrap"> ({{ workshop.shortname }})</span>{% endif %}.
{% endcase %}
    </td>
</tr>
