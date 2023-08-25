#!/usr/bin/env python

import sys

f = open("testfile1.txt" , "r")
print(f.read())

f = open("testfile1.txt" , "w")
f.write("HelloWorld")

f = open("testfile1.txt" , "a")
f.write("Appending hello world to existing file")

def Cat(filename):
  f = open(filename, "r")
  for line in f:
    print(line,)

if __name__ == "__main__":
  Cat("testfile1.txt") 
  #Cat(sys.argv[1])
