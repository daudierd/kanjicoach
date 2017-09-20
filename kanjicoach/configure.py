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
        self.setWindowTitle("Configure Kanji Coach")

        #TODO Uncomment last instruction line when tooltips are implemented
        instructions = QLabel("<h4>Instructions:</h4>" +
            "<p>This window allows you to configure and customize Kanji Coach "+
            "add-on according to your learning style and objectives." +
            #"<br/>Just hover your mouse on a field to display related information." +
            "<hr/></p>")
        instructions.setWordWrap(True)
        instructions.setAlignment(Qt.AlignJustify)

        grid = QGridLayout()
        # First line allows the user to specify the deck used by the add-on
        grid.addWidget(QLabel("Study deck"), 1, 0)
        self.deck = QComboBox()
        self.deck.addItems(self.getDecks())
        self.deck.currentIndexChanged.connect(
            lambda: self.updateFields(self.deck.currentText()))
        grid.addWidget(self.deck, 1, 1)
        # Second line allows the user to specify which field in the deck
        # contains the kanji
        grid.addWidget(QLabel("Kanji field"), 2, 0)
        self.kanji_fld = QComboBox()
        grid.addWidget(self.kanji_fld, 2, 1)
        # Third line allows the user to choose which stroke diagrams to display
        grid.addWidget(QLabel("Stroke diagrams"), 3, 0)
        self.strokes = QComboBox()
        self.strokes.addItems(["Animated", "Kanjax diagrams"])
        grid.addWidget(self.strokes, 3, 1)
        # In case the user wants to use a custom field, a combo box will be
        # displayed
        self.strokes_fld = QComboBox()
        grid.addWidget(self.strokes_fld, 4, 1)
        self.strokes_fld.hide()

        # Letting the user customize lessons' length
        grid.addWidget(QLabel("Number of kanji per lesson"), 5, 0)
        self.lesson_nb = QSpinBox()
        grid.addWidget(self.lesson_nb, 5, 1)

        # Letting the user choose a preferred learning order
        grid.addWidget(QLabel("Preferred learning order"), 6, 0)
        self.order = QComboBox()
        for option in ["JLPT", "Grade", "Frequency", "Heisig", u"みんなの日本語"]:
            self.order.addItem(option)
        grid.addWidget(self.order, 6, 1)

        # The user can choose to learn primitives before the kanji that contain
        # them, as it is the case in Heisig's method
        self.parts_first = QCheckBox("Learn primitives first (Heisig)")
        # To prevent Anki from showing cards for kanji that haven't been viewed
        # with Kanji Coach, the user can suspend them.
        self.suspend_unlearnt = QCheckBox("Suspend unlearnt cards")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.onConfirm)
        btn_cancel = QPushButton("Cancel")
        btn_cancel.clicked.connect(self.onCancel)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)

        vbox = QVBoxLayout()
        vbox.setSpacing(15)
        vbox.addWidget(instructions)
        vbox.addLayout(grid)
        vbox.addWidget(self.parts_first)
        vbox.addWidget(self.suspend_unlearnt)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.resize(480, 550)

    def getDecks(self):
        #TODO Exclude empty decks
        decks = mw.col.decks.allNames()
        return sorted(decks)

    def updateFields(self, deckName):
        did = mw.col.decks.id(deckName)
        cids = mw.col.decks.cids(did)
        if cids:
            # We assume that alls cards share the same model
            card0 = mw.col.getCard(cids[0])
            model = mw.col.models.get(card0.note().mid)
            fields = mw.col.models.fieldNames(model)
            self.kanji_fld.addItems(fields)
        else:
            QMessageBox.about(self, "Warning",
                "Your deck does not contain any card!")

    def onCancel(self, mode):
        self.close()

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
