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
answer = 0
print "Welcome! Use the calculator to do what you need, type \"help\" to get a list of commands.\n"
while (op != "exit" and op != "exit "):
    a = get_First_Num(answer)
    op = raw_input("Enter an operation to perform: ")
    answer=operation(op,a,answer)
    print answer
if(op=="exit" or op=="exit "):
	print "Thank you, see you soon!"
	sys.exit(0)
