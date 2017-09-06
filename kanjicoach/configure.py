# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements UI functionalities and Widget subclass to display a
# configuration dialog box in Anki.

from aqt import *

class ConfigureDialog(QDialog):
    """Browser batch editing dialog"""
    def __init__(self, mw):
        QDialog.__init__(self)
        self.initUI()

    def initUI(self):
        """Initialize the UI"""
        pass

    def onConfirm(self, mode):
        pass
        self.close()

def configure(mw):
    dialog = ConfigureDialog(mw)
    dialog.exec_()

# add action as a new menu item
def setup_menu(menu):
    action = QAction("Configure", mw)
    action.setShortcut(QKeySequence("Ctrl+Shift+K"))
    action.triggered.connect(configure)
    menu.addAction(action)
