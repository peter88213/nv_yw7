"""Plugin template for novelyst.

Requires Python 3.6+
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_plugin
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import sys
import os
import tkinter as tk
import locale
import gettext
import webbrowser
from novelystlib.plugin.plugin_base import PluginBase

# Initialize localization.
LOCALE_PATH = f'{os.path.dirname(sys.argv[0])}/locale/'
try:
    CURRENT_LANGUAGE = locale.getlocale()[0][:2]
except:
    # Fallback for old Windows versions.
    CURRENT_LANGUAGE = locale.getdefaultlocale()[0][:2]
try:
    t = gettext.translation('novelyst_plugin', LOCALE_PATH, languages=[CURRENT_LANGUAGE])
    _ = t.gettext
except:

    def _(message):
        return message


class Plugin(PluginBase):
    """Template plugin class.
    
    Public methods:
        install(ui) -- Install the plugin and extend the novelyst user interface.
    """
    VERSION = '@release'
    NOVELYST_API = '4.30'
    DESCRIPTION = 'Plugin template'
    URL = 'https://peter88213.github.io/novelyst_plugin'
    _HELP_URL = 'https://peter88213.github.io/novelyst_plugin/usage'

    def install(self, ui):
        """Install the plugin and extend the novelyst user interface.
        
        Positional arguments:
            ui -- reference to the NovelystTk instance of the application.
        """
        self._ui = ui

        # Add an entry to the Help menu.
        self._ui.helpMenu.add_command(label=_('novelyst_plugin Online help'), command=lambda: webbrowser.open(self._HELP_URL))

