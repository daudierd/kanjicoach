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
