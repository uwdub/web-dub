module Jekyll
  module PeopleFilter
    def person_has_role(people, tag)
      people.select { |person| item_property(person, "role").include? tag }
    end
  end
end

Liquid::Template.register_filter(Jekyll::PeopleFilter)