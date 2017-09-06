# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from aqt import *

from kanjicoach import configure, lesson
from kanjicoach import res_folder

kanjicoachMenu = QMenu("Kanji Coach", mw)
kanjicoachMenu.setIcon(QIcon(os.path.join(res_folder, 'icon.png')))
mw.form.menuTools.addMenu(kanjicoachMenu)

configure.setup_menu(kanjicoachMenu)
lesson.setup_menu(kanjicoachMenu)
