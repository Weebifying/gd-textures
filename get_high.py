import os, sys, shutil
from os.path import join
import glob

resources = sys.argv[1]
path = sys.argv[2]
try:
    os.mkdir(join(path, "icons"))
except:
    pass

files = glob.glob(resources + "**\\*-uhd.*", recursive=True)

for file in files:
    dest = join(path, file.replace(resources, ""))
    print(f"{file} -> {dest}")
    shutil.copyfile(file, dest)