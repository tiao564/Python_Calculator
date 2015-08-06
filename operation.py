##############################################
#Handles operations to perform on the numbers#
##############################################
################################
#Import class for exit function#
################################
import sys
############
#Variables?#
############
last_op = ""
#######################################################
#define different operations that the calc and preform#
#######################################################
def operation(op,a,answer):
	b=get_Second_Num(answer)
	if (op=="+" or op=="+ " or op==" +"):       #addition
		answer=a+b
		last_op = op
		return answer

	elif (op=="-" or op=="- " or op==" -"):     #subtraction
		answer=a-b
		last_op = op
		return answer

	elif (op=="*" or op=="* " or op==" *"):     #multiplication
		answer=a*b
		last_op = op
		return answer

	elif (op=="/" or op=="/ " or op==" /"):     #devision
		answer=a/b
		last_op = op
		return answer

	elif (op=="help" or op=="Help" or op=="help " or op=="Help "):  #help function
                helping()

	elif (op=="d" or op==" d" or op=="d "):     #repeat last operation, first number stays the same
		a=answer
		print a
		operation(last_op)

	elif (op=="help" or op=="Help" or op=="help " or op=="Help "):  #help function
                helping()

        else:                                       #other
		print "Not a valid operation"

################################
#define inputs for user numbers#
################################
def get_First_Num(answer):
	a = raw_input("Enter first number to operate on: ")
	if(a=="a" or a=="a " or a=="A" or a=="A "):                 #allows for last answer to be used again
            return answer
	if(a=="d" or a=="d " or a=="D" or a=="D "):
	    return "d"
	elif (a=="help" or a=="Help" or a=="help " or a=="Help "):  #help function
            helping()
            a = get_First_Num(answer)
        elif (a=="exit" or a=="exit "):                             #exit function
            print "Thank you, have a nice day"
            sys.exit(0)
        else:                                                       #if not input function, attempt to cast to float for operation
            try:
                a=float(a)
            except ValueError:
                print "Oops, that's not a valid operation or number, try again. \n"
                a=get_First_Num(answer)
        return a

def get_Second_Num(answer):
	b = raw_input("Enter second number to operate on: ")
        if(b=="a" or b=="a " or b=="A" or b=="A "):                 #allows for last answer to be used
            b = answer
            return b
	elif (b=="help" or b=="Help" or b=="help " or b=="Help "):  #help function
            helping()
            b=get_Second_Num(answer)
        elif (b=="exit" or b=="exit "):                             #exit function
            print "Thank you have a good day"
            sys.exit(0)
        else:                                                       #if not input function, attempt to cast to float for operation
            try:
                b=float(b)
            except ValueError:
                print "Oops, that's not a valid operation or number, try again.\n"
                b=get_Second_Num(answer)
        return b

#########################################
#define helper, lists available commands#
#########################################
def helping():
	print "List of commands: "
        print "   +: addition on two numbers"
        print "   -: subtraction on two numbers"
        print "   *: multiplication on two numbers"
        print "   /: devision on two numbers"
        print "   d: performs last operation again using last answer and a new input"
        print "   a: *when asked for first number* uses last answer for a"
        print "exit: leaves program\n"
