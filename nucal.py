#!/usr/bin/python
import os
import sys, traceback
def f(x):
	return {
		'a':1,
		'i':1,
		'j':1,
		'q':1,
		'y':1,
		'b':2,
		'k':2,
		'r':2,
		'c':3,
		'g':3,
		'l':3,
		's':3,
		'd':4,
		'm':4,
		't':4,
		'e':5,
		'h':5,
		'n':5,
		'x':5,
		'u':6,
		'v':6,
		'w':6,
		'o':7,
		'z':7,
		'f':8,
		'p':8,
	}.get(x,0)
os.system('clear')
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()
while True:
	testVar = raw_input("Enter Name : ")
	print " "
	print "----------------------------------------------------------"
	print "----  %s ----" %testVar
	s = list(testVar.lower())
	value=0
	for i in s:
		value = value + f(i)
		temp= f(i)
		print("%s -> %d" %(i,temp))

	print "The value is %d" %value
	print " "



if __name__ == "__main__":
    main()
