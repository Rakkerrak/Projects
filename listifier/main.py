
import itertools
import datetime
import sys


infilename = "stringin.txt"
outfilename = datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p") + ".txt"
listname = "output"

if len(sys.argv) > 1:
    outfilename = sys.argv[1]
if len(sys.argv) > 2:
    infilename = sys.argv[2]
if len(sys.argv) > 3:
    listname = sys.argv[3]




inputf = open(infilename, "r")
lists = [(line.split() for line in inputf)]
final = []
for section in lists:
    for subsection in section:
        final.extend(subsection)
inputf.close()


outputf = open(outfilename, "a")
outputf.write("\n" + listname + " = ")
outputf.write(str(final))
outputf.close()

print("Complete\nUsage: python main.py outfile infile listname \nDefault: <datetime>.txt stringin.txt output\nCovnerts single line words to a list.")
