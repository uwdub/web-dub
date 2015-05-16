module Jekyll
  module PeopleFilter
    def person_has_tag(people, tag)
      people.select { |person| item_property(person, "tags").include? tag }
    end
  end
end

Liquid::Template.register_filter(Jekyll::PeopleFilter)