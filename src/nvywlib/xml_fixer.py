"""Provide a parser to fix malformed XML.

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/nv_yw7
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from html.parser import HTMLParser
from html import escape


class XmlFixer(HTMLParser):
    """Event driven parser that accepts malformed XML."""

    def __init__(self):
        super().__init__()
        self._fixedXmlStr = []
        self._format = []

    def get_fixed_xml(self, xmlStr):
        """Return an XML string with wrong <em> and <strong> nestings fixed.
        
        Overrides the xml.sax.ContentHandler method             
        """
        self.feed(xmlStr)
        fixedXmlStr = ''.join(self._fixedXmlStr)
        fixedXmlStr = fixedXmlStr.replace('<em></em>', '')
        fixedXmlStr = fixedXmlStr.replace('<strong></strong>', '')
        fixedXmlStr = fixedXmlStr.replace('<em></em>', '')
        return fixedXmlStr

    def handle_data(self, data):
        """Generally keep all character data.
        
        Overrides the superclass method             
        """
        self._fixedXmlStr.append(escape(data))

    def handle_endtag(self, tag):
        """Close <em> and <strong> if needed to avoid overlapping.
        
        Overrides the superclass method             
        """
        if tag in ('em', 'strong'):
            if not tag in self._format:
                # formatting area is already closed
                return

            if  self._format[-1] != tag:
                self._fixedXmlStr.append(f'</{self._format.pop()}>')
                # closing overlapping formatting area

            self._format.remove(tag)
        self._fixedXmlStr.append(f'</{tag}>')

    def handle_starttag(self, tag, attrs):
        """Keep all tags, except multiple <em> and <strong>.
        
        Overrides the superclass method             
        """
        if tag in ('em', 'strong'):
            if tag in self._format:
                return

            self._format.append(tag)
        attrStr = ''
        for name, value in attrs:
            attrStr = f'{attrStr} {name}="{value}"'
        self._fixedXmlStr.append(f'<{tag}{attrStr}>')

