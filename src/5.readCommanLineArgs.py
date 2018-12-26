
import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: Python %s inputfile outputfile\n" % sys.argv[0])
    raise SystemExit(1)
# print(sys.argv[0])
inputfile = sys.argv[1]
outoputfile = sys.argv[2]
