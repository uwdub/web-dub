module Jekyll
  module PaperFilter
    def id_author(hash, id_author)
      hash.reject { |id, paper| paper["authors"].index(id_author) == nil}
    end
  end
end

Liquid::Template.register_filter(Jekyll::PaperFilter)