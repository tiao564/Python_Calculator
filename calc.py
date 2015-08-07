#! /usr/bin/env python
####################
#A basic calculator#
####################

###############################################
#Will do basic addition, subtraction,         #
# multibplication and devision at first,      #
# will try to add more features down the line #
###############################################

###################
#Class importation#
###################
import sys
from operation import *
##################################################
#Query user for input, exit will be string "exit"#
##################################################
op = ""
last_op =""
answer = 0
print "Welcome! Use the calculator to do what you need, type \"help\" to get a list of commands. Type \"exit\" to exit the program.\n"
while (op != "exit" and op != "exit "):
	last_op=op
	a = get_First_Num(answer)
	if(a=="d" or a=="d " or a=="D" or a=="D  "):
            answer = operation(last_op,answer,answer)
            print"{}".format(answer)
            print "_____________\n"
        else:
	    op = raw_input("op: ")
	    answer=operation(op,a,answer)
            print "{}".format(answer)
            print "_____________\n"
if(op=="exit" or op=="exit "):
	print "Thank you, see you soon!"
	sys.exit(0)
