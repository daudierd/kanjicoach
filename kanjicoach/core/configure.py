# -*- coding: utf-8 -*-

# Kanji Coach for Anki
# Copyright (C) 2017-Present  Dorian DAUDIER
#
# This module implements the core self.configuration functionalities for Kanji Coach
# add-on.

import json

from .. import config_file
from .. import strokes_dict, order_dict

class Configuration():
    def __init__(self):
        """Initialize the self.configuration from the corresponding file."""
        self.config = dict()
        with open(config_file, 'r') as f:
            self.config = json.loads(f.read())

    def update(self, user, deck, kanji_fld, strokes, lesson_nb, order,
            parts_first, suspend_unlearnt):
        """Update the configuration object and save in a configuration file."""
        self.config['user'] = user
        self.config['deck'] = deck
        self.config['kanji_fld'] = kanji_fld
        self.config['strokes'] = strokes
        self.config['order'] = order
        self.config['lesson_nb'] = lesson_nb
        self.config['parts_first'] = parts_first
        self.config['suspend_unlearnt'] = suspend_unlearnt

        if self.is_valid:
            with open(config_file, 'w') as f:
                f.write(json.dumps(self.config))
                return true
        return false

    def is_valid(self):
        """Returns a boolean:
        True if the configuration is valid, False otherwise."""
        #TODO implement verification rules
        return True

    def get_data(self):
        """Get the current configuration data."""
        return self.config
