# -*- coding: utf-8 -*-

import os

# File path to the configuration file
config_file = os.path.join(os.path.dirname(__file__), 'kanjicoach.conf')

# Path to resources folder
res_folder = os.path.join(os.path.dirname(__file__), 'res')

# File path to kanjax database
kanjax_db = os.path.join(res_folder,'kanji.db')
# File path to kanjax stroke diagrams
kanjax_zip = os.path.join(res_folder,'kanjax.zip')
# File path to gif stroke animations
gifs_zip = os.path.join(res_folder,'gifs.zip')

# The following dictionaries ensure proper binding between field names displayed
# in the configuration form and the values registered in configuration files.
strokes_dict = {"Animated" : "gif",
                "Kanjax diagrams": "kanjax"}

order_dict = {"JLPT" : "ord_jlpt.txt",
              "Grade" : "ord_grade.txt",
              "Frequency" : "ord_frequency.txt",
              "Heisig" : "ord_heisig.txt",
              u"みんなの日本語" : "ord_minna.txt"}

# Load the configuration
config = Configuration()
