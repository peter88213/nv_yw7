"""Provide a parser to fix malformed XML.

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_yw7
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from html.parser import HTMLParser
from html import escape


class XmlFixer(HTMLParser):
    """Event driven parser that accepts malformed HTML."""

    def __init__(self):
        super().__init__()
        self._fixedXml = []
        self._em = False
        self._strong = False

    def feed(self, rawXml):
        """Return an XML string with <em> and <strong> nestings removed.
        
        Overrides the xml.sax.ContentHandler method             
        """
        super().feed(rawXml)
        newXml = ''.join(self._fixedXml)
        newXml = newXml.replace('<strong></strong>', '')
        newXml = newXml.replace('<em></em>', '')
        return newXml

    def handle_data(self, data):
        """Receive notification of character data.
        
        Overrides the xml.sax.ContentHandler method             
        """
        self._fixedXml.append(escape(data))

    def handle_endtag(self, tag):
        """Signals the end of an element in non-namespace mode.
        
        Overrides the xml.sax.ContentHandler method     
        """
        if tag == 'em':
            if not self._em:
                return

            self._em = False
        elif tag == 'strong':
            if not self._strong:
                return

            self._strong = False
        self._fixedXml.append(f'</{tag}>')

    def handle_starttag(self, tag, attrs):
        """Signals the start of an element in non-namespace mode.
        
        Overrides the xml.sax.ContentHandler method             
        """
        if tag == 'em':
            if self._em:
                return

            self._em = True
            if self._strong:
                self._fixedXml.append(f'</strong>')
                self._strong = False
        elif tag == 'strong':
            self._strong = True
            if self._em:
                self._fixedXml.append(f'</em>')
                self._em = False
        self._fixedXml.append(f'<{tag}>')

