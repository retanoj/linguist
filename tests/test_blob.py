# -*- coding: utf-8 -*-

from os.path import realpath, dirname, join
from pygments.lexers import find_lexer_class
from .framework import LinguistTestBase, main
from linguist.libs.file_blob import FileBlob
from linguist.libs.samples import Samples

DIR = dirname(dirname(realpath(__file__)))
SAMPLES_PATH = join(DIR, "samples")

colorize = """<div class="highlight"><pre><span></span><span class="k">module</span> <span class="nn">Foo</span>
<span class="k">end</span>
</pre></div>
"""

colorize_without_wrapper = """<span class="k">module</span> <span class="nn">Foo</span>
<span class="k">end</span>
"""


class TestFileBob(LinguistTestBase):

    def blob(self, name):
        if not name.startswith('/'):
            name = join(SAMPLES_PATH, name)
        return FileBlob(name, SAMPLES_PATH)

    def script_blob(self, name):
        blob = self.blob(name)
        blob.name = 'script'
        return blob

    def test_name(self):
        assert 'foo.rb' == self.blob('foo.rb').name

    def test_mime_type(self):
        assert 'application/x-ruby' == self.blob("Ruby/grit.rb").mime_type
        assert "application/x-sh" == self.blob("Shell/script.sh").mime_type
        assert "application/xml" == self.blob("XML/FXMLSample.xml").mime_type

    def test_data(self):
        assert "module Foo\nend\n" == self.blob("Ruby/foo.rb").data

    def test_lines(self):
        assert ["module Foo", "end", ""] == self.blob("Ruby/foo.rb").lines

    def test_size(self):
        assert 15 == self.blob("Ruby/foo.rb").size

    def test_loc(self):
        assert 3 == self.blob("Ruby/foo.rb").loc

    def test_sloc(self):
        assert 2 == self.blob("Ruby/foo.rb").sloc

    def test_viewable(self):
        assert self.blob("Ruby/foo.rb").is_viewable
        assert self.blob("Perl/script.pl").is_viewable

        # Generated .NET Docfiles
        assert self.blob("XML/net_docfile.xml").is_generated

        # Long line
        assert not self.blob("JavaScript/uglify.js").is_generated

        # Inlined JS, but mostly code
        assert not self.blob("JavaScript/json2_backbone.js").is_generated

        # Minified JS
        assert not self.blob("JavaScript/jquery-1.6.1.js").is_generated
        assert self.blob("JavaScript/jquery-1.4.2.min.js").is_generated

        # PEG.js-is_generated parsers
        assert self.blob("JavaScript/parser.js").is_generated

        # These examples are too basic to tell
        assert not self.blob("JavaScript/hello.js").is_generated

        assert self.blob("JavaScript/intro-old.js").is_generated
        assert self.blob("JavaScript/classes-old.js").is_generated

        assert self.blob("JavaScript/intro.js").is_generated
        assert self.blob("JavaScript/classes.js").is_generated

        # Protocol Buffer generated code
        assert self.blob("C++/protocol-buffer.pb.h").is_generated
        assert self.blob("C++/protocol-buffer.pb.cc").is_generated
        assert self.blob("Java/ProtocolBuffer.java").is_generated
        assert self.blob("Python/protocol_buffer_pb2.py").is_generated

        # Generated JNI
        assert self.blob("C/jni_layer.h").is_generated

    # def test_language(self):
    #     def _check_lang(sample):
    #         blob = self.blob(sample['path'])
    #         assert blob.language, 'No language for %s' % sample['path']
    #         assert sample['language'] == blob.language.name, blob.name
    #
    #     Samples.each(_check_lang)

    def test_lexer(self):
        assert find_lexer_class('Ruby') == self.blob("Ruby/foo.rb").lexer

    def test_colorize(self):
        assert colorize == self.blob("Ruby/foo.rb").colorize()

    # Pygments.rb was taking exceeding long on this particular file
    def test_colorize_doesnt_blow_up_with_files_with_high_ratio_of_long_lines(self):
        assert None == self.blob("JavaScript/steelseries-min.js").colorize()


if __name__ == '__main__':
    main()
