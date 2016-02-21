# Adapted from https://github.com/gummesson/jekyll-vimeo-plugin

module Jekyll
  class Vimeo < Liquid::Tag
    @@width = 600
    @@height = 338

    def initialize(name, id, tokens)
      super
      @id = id
    end

    def look_up(context, name)
      lookup = context

      name.split(".").each do |value|
        lookup = lookup[value]
      end

      lookup
    end

    def render(context)
      output = super
      if @id =~ /([\w]+(\.[\w]+)*)/i
        @idvalue = look_up(context, $1)
      end

      %(<iframe width="#{@@width}" height="#{@@height}" src="https://player.vimeo.com/video/#{@idvalue}" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>)
    end
  end
end

Liquid::Template.register_tag('vimeo', Jekyll::Vimeo)