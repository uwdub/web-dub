require 'date'
require 'time'

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
      seminars.select { |seminar| item_property(seminar, "date").to_date() < date.to_date() &&
          item_property(seminar, "archive") == true }
    end
  end

  module TimeConverter
    def convert_time(input_time)
      Time.parse(input_time).strftime("%H%M%S")
    end
  end
end

Liquid::Template.register_filter(Jekyll::PeopleFilter)
Liquid::Template.register_filter(Jekyll::SeminarFilter)
Liquid::Template.register_filter(Jekyll::TimeConverter)
