import re
def div(num):
	return float(num[0]) / float(num[1])

def add(num):
	#if there is the ".", the number should be converted to float type;
	if re.findall("\\.",num[0]):
		a = float(num[0])
	else:
		a = int(num[0])
	if re.findall("\\.",num[1]):
		b = float(num[1])
	else:
		b = int(num[1])
	return a + b

def sub(num):
	#if there is the ".", the number should be converted to float type;
	if re.findall("\\.",num[0]):
		a=float(num[0])
	else:
		a=int(num[0])
	if re.findall("\\.",num[1]):
		b=float(num[1])
	else:
		b=int(num[1])
	return a-b

print("Welcome!!!")
print("This is a simple calculator with four functions,")
print("which are addition, subtraction, multiplication and division.")
print('You can input "help" for the usage example, "exit" to exit.')

while True:
	cmd = input(":")
	if cmd == "exit":
		exit()
	if cmd == "help":
		print("This calculator is just with the function of binary operation")
		print("Here are the examples:")
		print("1+1")
		print("1-1")
		print("2*2")
		print("3/2")
		print("Be careful that multiplication and division will be forced to excute float-point operation")
	num = re.findall("\d+\.\d|\d+", cmd)
	operator = re.findall("\\+|\\-|\\*|\\/",cmd)
	if operator[0] == "+":
		result = add(num);
	if operator[0] == "-":
		result = sub(num);
	if operator[0] == "*":
		result = mul(num);
	if operator[0] == "/":
		result = div(num);
	print(result)
	
