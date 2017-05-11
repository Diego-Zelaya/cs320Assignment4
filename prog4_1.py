import sys

[ print(','.join(x.split())) for x in open(sys.argv[1]).readlines() if len(x.split())>0]

