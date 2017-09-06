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

def start_lesson(mw):
    dialog = LessonDialog(mw)
    dialog.exec_()

# add action as a new menu item
def setup_menu(menu):
    action = QAction("Start Lesson", mw)
    action.setShortcut(QKeySequence("Ctrl+Shift+L"))
    action.triggered.connect(start_lesson)
    menu.addAction(action)
