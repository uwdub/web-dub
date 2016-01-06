require 'date'

module Jekyll
  module PeopleFilter
    def person_has_role(people, tag)
      people.select { |person| item_property(person, "role").include? tag }
    end
  end

  module SeminarFilter
    def seminar_upcoming(seminars, date)
      seminars.select { |seminar| item_property(seminar, "date").to_date() >= date.to_date() }
    end

    def seminar_previous(seminars, date)
      seminars.select { |seminar| item_property(seminar, "date").to_date() < date.to_date() }
    end
  end
end

Liquid::Template.register_filter(Jekyll::PeopleFilter)
Liquid::Template.register_filter(Jekyll::SeminarFilter)
