# Used according to license:
#
# https://github.com/michaelx/jekyll_file_exists
#
# The MIT License (MIT)
#
# Copyright (c) 2015 Michael Xander
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

module Jekyll
    class FileExistsTag < Liquid::Tag

        def initialize(tag_name, path, tokens)
            super
            @path = path
        end

        def render(context)
            # ref https://gist.github.com/vanto/1455726
            # pipe param through liquid to make additional replacements possible
            url = Liquid::Template.parse(@path).render context

            # check if file exists (returns true or false)
            "#{File.exist?(url.strip!)}"
        end
    end
end

Liquid::Template.register_tag('file_exists', Jekyll::FileExistsTag)