#!/usr/bin/env python
from django.core.management import execute_from_command_line
import imp
import os
import sys

try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the module 'settings' in the directory containing %r.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    # execute_from_command_line(settings)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings") #path to the settings py file
    execute_from_command_line(sys.argv)
