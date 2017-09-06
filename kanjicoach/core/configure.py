# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements the core configuration functionalities for Kanji Coach
# add-on.

from .. import config_file

class Configuration():
    def __init__(self):
        """Initialize the configuration from the corresponding file."""
        pass

    def update(self, user, deck, kanji_fld, strokes, lesson_nb, order,
            parts_first, suspend_unlearnt):
        """Update the configuration object and save in a configuration file."""
        pass

    def is_valid(self):
        """Returns a boolean:
        True if the configuration is valid, False otherwise."""
        pass

    def get_data(self):
        """Get the current configuration data."""
        pass
