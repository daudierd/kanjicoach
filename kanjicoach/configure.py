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

def onConfigure(mw):
    dialog = ConfigureDialog(browser)
    dialog.exec_()

def setupMenu(mw):
    menu = mw.form.menuTools
    menu.addSeparator()
    action = menu.addAction('Configure Kanji Coach')
    action.setShortcut(QKeySequence("Ctrl+Alt+K"))
    mw.connect(a, SIGNAL("triggered()"), lambda: onConfigure(mw))
