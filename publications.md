---
layout: default
title: Publications
---

## Journal Articles
<table class="table table-bordered">
    {% for item_paper in site.data.journalpapers %}
    {% assign paper = item_paper[1] %}
    <tr>
        <td class="nowrap">
            [{{ paper.pubnum }}]
            <span class="fontsmall">
                <br/><a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">local PDF</a>
                {% if paper.officialurl %}
                <br/><a href="{{ paper.officialurl }}">official PDF</a>
                {% endif %}
            </span>
        </td>
        <td width="90" height="90">
            <a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">
                <img src="{{ site.baseurl }}/publications/{{ paper.localthumb }}" width="90" height="90">
            </a>
        </td>
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
            {% assign journal = site.data.journals[paper.journal] %}
            <i>{{ journal.longname }}</i>{% if journal.shortname %}<span class="nowrap"> ({{ journal.shortname }})</span>{% endif %}.
            <span class="nowrap">Vol. {{ paper.volume }},</span>
            <span class="nowrap">Iss. {{ paper.issue }},</span>
            <span class="nowrap">pp. {{ paper.pages }}.</span>
        </td>
    </tr>
    {% endfor %}
</table>

## Conference Articles
<table class="table table-bordered">
    {% for item_paper in site.data.conferencepapers %}
    {% assign paper = item_paper[1] %}
    <tr>
        <td class="nowrap">
            [{{ paper.pubnum }}]
            <span class="fontsmall">
                <br/><a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">local PDF</a>
                {% if paper.localvideo %}
                <br/><a href="{{ site.baseurl }}/publications/{{ paper.localvideo }}">local video</a>
                {% endif %}
                {% if paper.officialurl %}
                <br/><a href="{{ paper.officialurl }}">official PDF</a>
                {% endif %}
            </span>
        </td>
        <td width="90" height="90">
            <a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">
                <img src="{{ site.baseurl }}/publications/{{ paper.localthumb }}" width="90" height="90">
            </a>
        </td>
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
            {% assign conference = site.data.conferences[paper.conference] %}
            <i>{{ conference.longname }}</i>{% if conference.shortname %}<span class="nowrap"> ({{ conference.shortname }})</span>{% endif %}.
            {% if paper.pages %}
            <span class="nowrap">pp. {{ paper.pages }}.</span>
            {% endif %}
        </td>
    </tr>
    {% endfor %}
</table>

## Workshop Papers
<table class="table table-bordered">
    {% for item_paper in site.data.workshoppapers %}
    {% assign paper = item_paper[1] %}
    <tr>
        <td class="nowrap">
            [{{ paper.pubnum }}]
            <span class="fontsmall">
                <br/><a href="{{ site.baseurl }}/publications/{{ paper.localpdf }}">local PDF</a>
            </span>
        </td>
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
            {% assign workshop = site.data.workshops[paper.workshop] %}
            <i>{{ workshop.longname }}</i>{% if workshop.shortname %}<span class="nowrap"> ({{ workshop.shortname }})</span>{% endif %}.
        </td>
    </tr>
    {% endfor %}
</table>
