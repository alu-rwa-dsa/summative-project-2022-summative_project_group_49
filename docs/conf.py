# project assumes
# python 3.7

import os
import sys
sys.path.insert(0, 'module/core.py')
sys.path.insert(1, 'module/play_list.py')
sys.path.insert(2, 'tests/core.py')
sys.path.insert(3, 'play_list_gui.py')

# The master toctree document.
master_doc = 'play_list_gui.py'

project = u'MusicPlaylist'
copyright = u'Nahashon'
version = '1.0.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['conf.py', 'README.md', 'index.rst', '_init_.py', 'contributors.md', 'licence.md', 'requirements.txt', 'setup.py']
