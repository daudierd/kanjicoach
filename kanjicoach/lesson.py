# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements UI functionalities and Widget subclass to show a new
# lesson with KanjiCoach

from aqt import *

class LessonDialog(QDialog):
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

def onLessonStart(mw):
    dialog = ConfigureDialog(browser)
    dialog.exec_()

def setupMenu(mw):
    menu = mw.form.menuTools
    menu.addSeparator()
    action = menu.addAction('Start lesson with Kanji Coach')
    action.setShortcut(QKeySequence("Ctrl+Alt+L"))
    mw.connect(a, SIGNAL("triggered()"), lambda: onLessonStart(mw))
