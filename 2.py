import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv)>=2 else '2.in'
D = open(infile).read().strip()
print(D)