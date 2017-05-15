import sys
import re

# import StackMachine.py
from StackMachine import *

print("Assignment #4-2, Diego Zelaya, Kidzeta2005@gmail.com")


FILE = open(sys.argv[1], "r")
#FILE = open("filename.txt", "r")

MYSTACK = StackMachine()

for line in FILE:
    s = line.split()
    if s[0] == "push":
        MYSTACK.push(s[1])

    if s[0] == "pop":
        MYSTACK.pop()

    if s[0] == "sub":
        MYSTACK.sub()

    if s[0] == "mul":
        MYSTACK.mul()

    if s[0] == "div":
        MYSTACK.div()

    if s[0] == "mod":
        MYSTACK.mod()

print(MYSTACK.items[0])


print("finnished...")
# 1, push
   