##############################################
#Handles operatings to perform on the numbers#
##############################################
last_op = ""
answer = 0
def operating(op):
	if (op=="+" or op=="+ " or op==" +"):
		a=get_First_Num()
		if(a=="a" or a=="A"):
			a=answer
		b=get_Second_Num()
		answer=a+b
		last_op = op
		return answer

	elif (op=="-" or op=="- " or op==" -"):
		a=get_First_Num()
		if(a=="a" or a=="A"):
			a=answer
		b=get_Second_Num()
		answer=a-b
		last_op = op
		return answer

	elif (op=="*" or op=="* " or op==" *"):
		a=get_First_Num()
		if(a=="a" or a=="A"):
			a=answer
		b=get_Second_Num()
		answer=a*b
		last_op = op
		return answer

	elif (op=="/" or op=="/ " or op==" /"):
		a=get_First_Num()
		if(a=="a" or a=="A"):
			a=answer
		b=get_Second_Num()
		answer=a/b
		last_op = op
		return answer

	elif (op=="d" or op==" d" or op=="d "):
		a=answer
		print a
		operating(last_op)

	elif (op=="help" or op=="Help" or op=="help " or op=="Help "):
		print "List of commands: "
		print "   +: addition on two numbers"
		print "   -: subtraction on two numbers"
		print "   *: multiplication on two numbers"
		print "   /: devision on two numbers"
		print "   d: performs last operation again using last answer and a new input"
		print "   a: *when asked for first number* uses last answer for a"
		print "eixt: leaves program"

	else:
		 print "Not a valid operation"


def get_First_Num():
	a = input("Enter first number to operate on: ")
	return a

def get_Second_Num():
	b = input("Enter second number: ")
	return b

