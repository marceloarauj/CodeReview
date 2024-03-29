from distutils.core import setup
import py2exe
import sys
import glob
import os

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")


datafiles = []
# i18n
def walk_callback(args, dirname, fnames):
    hasfile = False
    for f in fnames:
        if os.path.isfile(os.path.join(dirname, f)):
            hasfile = True
            break
    if hasfile:
        datafiles.append((dirname,glob.glob(os.path.join(dirname, '*'))))

os.path.walk('locale', walk_callback, None)


setup(
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 1,
                          "bundle_files": 1}},
    zipfile = None,
    console = ["myprogram.py"],
    data_files = datafiles
    )