from general import *
try:
    from local import *
except ImportError:
    import sys
    sys.stderr.write("Create local settings!\n")
    sys.exit(1)

