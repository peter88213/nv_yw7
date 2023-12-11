"""yw7 file import/export plugin for noveltree.

Requires Python 3.6+
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/nv_yw7
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import sys
import os
import locale
import gettext
from tkinter import filedialog
from novxlib.novx_globals import *
from novxlib.model.novel import Novel
from novxlib.model.nv_tree import NvTree
from novxlib.yw.yw7_file import Yw7File
from novxlib.novx.novx_file import NovxFile

APPLICATION = 'yw7 file import/export plugin'

# Initialize localization.
try:
    t = gettext.translation('nv_yw7', LOCALE_PATH, languages=[CURRENT_LANGUAGE])
    _ = t.gettext
except:
    pass


class Plugin:
    """yw7 file import/export plugin class.
    
    Public methods:
        disable_menu() -- disable menu entries when no project is open.
        enable_menu() -- enable menu entries when a project is open.
        on_close() -- Actions to be performed when a project is closed.       
        on_quit() -- Actions to be performed when noveltree is closed.               
    """
    VERSION = '@release'
    NOVELYST_API = '0.1'
    DESCRIPTION = 'yw7 file import/export plugin'
    URL = 'https://peter88213.github.io/noveltree'

    _YW_CLASS = Yw7File
    _NOVX_CLASS = NovxFile

    def disable_menu(self):
        """Disable menu entries when no project is open."""
        self._ui.fileMenu.entryconfig(_('Export to yw7'), state='disabled')

    def enable_menu(self):
        """Enable menu entries when a project is open."""
        self._ui.fileMenu.entryconfig(_('Export to yw7'), state='normal')

    def install(self, ui):
        """Add a submenu to the 'Tools' menu.
        
        Positional arguments:
            ui -- reference to the NoveltreeUi instance of the application.
        """
        self._ui = ui
        try:
            self._ui.fileMenu.insert_command(_('Reload'), label=_('Import from yw7...'), command=self.import_yw7)
        except:
            self._ui.fileMenu.add_command(label=_('Import from yw7...'), command=self.import_yw7)
        try:
            self._ui.fileMenu.insert_command(_('Close'), label=_('Export to yw7'), command=self.export_yw7)
        except:
            self._ui.fileMenu.add_command(label=_('Export to yw7'), command=self.export_yw7)

    def export_yw7(self):
        """Export the current project to yw7.
        
        Return True on success, otherwise return False.
        """
        if self._ui.prjFile.filePath is None:
            return False

        path, __ = os.path.splitext(self._ui.prjFile.filePath)
        yw7Path = f'{path}{self._YW_CLASS.EXTENSION}'
        if os.path.isfile(yw7Path):
            if not self._ui.ask_yes_no(_('Overwrite existing file "{}"?').format(norm_path(yw7Path))):
                self._ui.set_info_how(f'!{_("Action canceled by user")}.')
                return False

        yw7File = Yw7File(yw7Path)
        yw7File.novel = self._ui.novel
        yw7File.wcLog = self._ui.prjFile.wcLog
        try:
            yw7File.write()
        except TypeError as ex:
            self._ui.set_info_how(f'!{str(ex)}')
            return False

        self._ui.set_info_how(f'{_("File exported")}: {yw7Path}')
        return True

    def import_yw7(self, yw7Path=''):
        """Convert a yw7 file to novx and open the novx file.
        
        Return True on success, otherwise return False.
        """
        self._ui.restore_status()
        initDir = os.path.dirname(self._ui.kwargs.get('last_open', ''))
        if not initDir:
            initDir = './'
        if not yw7Path or not os.path.isfile(yw7Path):
            fileTypes = [(self._YW_CLASS.DESCRIPTION, self._YW_CLASS.EXTENSION)]
            yw7Path = filedialog.askopenfilename(filetypes=fileTypes,
                                                  defaultextension=self._YW_CLASS.EXTENSION,
                                                  initialdir=initDir)
        if not yw7Path:
            return False

        try:
            filePath, extension = os.path.splitext(yw7Path)
            if extension == self._YW_CLASS.EXTENSION:
                novxPath = f'{filePath}{self._NOVX_CLASS.EXTENSION}'
                if os.path.isfile(novxPath):
                    if not self._ui.ask_yes_no(_('Overwrite existing file "{}"?').format(norm_path(novxPath))):
                        self._ui.set_info_how(f'!{_("Action canceled by user")}.')
                        return False

                self._ui.close_project()
                yw7File = self._YW_CLASS(yw7Path)
                yw7File.novel = Novel(tree=NvTree())
                yw7File.read()
                novxFile = self._NOVX_CLASS(novxPath)
                novxFile.novel = yw7File.novel
                novxFile.wcLog = yw7File.wcLog
                novxFile.write()
            else:
                self._ui.set_info_how(f'!{_("File type is not supported")}.')
                return False

        except Exception as ex:
            self._ui.set_info_how(f'!{str(ex)}')
            return False

        self._ui.open_project(novxFile.filePath)
        self._ui.set_info_how(f'{_("File imported")}: {yw7Path}')
        return True

