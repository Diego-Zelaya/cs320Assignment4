import sys

print("Assignment #4-1, Diego Zelaya, Kidzeta2005@gmail.com")
[ print(','.join(x.split())) for x in open(sys.argv[1]).readlines() if len(x.split())>0]
