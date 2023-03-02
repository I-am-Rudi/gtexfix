import os
import re

results = []

for f in os.listdir("./input/"):
    if re.search('.tex', f):
        results += [f]

for f in results:
    os.system("./to.py " + f)
    os.system("./from.py " + f.replace(".tex", ".txt"))
    os.system("rm " + f.replace(".tex", ".txt"))