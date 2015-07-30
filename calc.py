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
again = ""
while (again != "exit" or again != "exit "):
	op = raw_input("Enter an operation for perform use \"help\" to get a list of tools and \"exit\" to end: ")
	if(op!="exit"):
		operating(op)
if(again=="exit" or again=="exit "):
	print "Thank you, see you soon!"
	sys.exit(0)
