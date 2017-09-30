# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements basic core functions used to generate lessons.

import os
from aqt import *

class Lesson():
    def __init__(self, config):
        """Initializes the lesson with a Configuration object."""
        # Can't initialize lesson without configuration
        self.config = config

    def generate_lesson(self):
        """Returns a list of (kanji, meaning, parts, stroke_diagram) tuples for
        the next lesson using the existing configuration and stores the
        corresponding notes ids"""
        pass

    def submit_lesson(self):
        """Reschedules notes for kanji returned on the last call of
        generate_lesson, using the notes ids stored."""
        pass
