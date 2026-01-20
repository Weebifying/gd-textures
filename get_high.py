import os, sys, shutil
from os.path import join, abspath, basename
import glob

resources = abspath(sys.argv[1])
path = sys.argv[2]
try:
    os.mkdir(join(path, "icons"))
except:
    pass

files = glob.glob(resources + "**\\*-uhd.*", recursive=True) # recursive doesn't actually work tho... cba to fix

for file in files:
    dest = join(path, basename(file))
    print(f"{file} -> {dest}")
    shutil.copyfile(file, dest)