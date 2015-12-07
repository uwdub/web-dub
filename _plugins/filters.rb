module Jekyll
  module PeopleFilter
    def person_has_role(people, tag)
      people.select { |person| item_property(person, "role").include? tag }
    end
  end

  module SeminarFilter
    def seminar_has_year(seminars, tag)
      seminars.select { |seminar| item_property(seminar, "date.year").include? tag }
    end
  end

  module UpcomingSeminarFilter
    def seminar_has_year(seminars, tag)
      seminars.select { |seminar| item_property(seminar, "date.year").include? tag }
    end
  end
end

Liquid::Template.register_filter(Jekyll::PeopleFilter)
Liquid::Template.register_filter(Jekyll::SeminarFilter)
Liquid::Template.register_filter(Jekyll::UpcomingSeminarFilter)
