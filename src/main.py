import random
 
 
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
 
def get_letters(length):
	string = ""
	for i in range(length):
		string += f"{letters[random.randint(0,len(letters)-1)]}"
	return string
 
def get_numbers(length):
	string = ""
	for i in range(length):
		string += f"{numbers[random.randint(0,len(numbers)-1)]}"
	return string
 
def get_both(length):
	string = ""
	for i in range(length):
		string += f"{letters[random.randint(0,len(letters)-1)] if random.randint(0,1) == 0 else numbers[random.randint(0,len(numbers)-1)]}"
	return string
 
setting = input("1=letters\n2=numbers\n3=both\n")
 
if setting == "1":
	for i in range(5):
		print(get_letters(random.randint(7, 14)))
elif setting == "2":
	for i in range(5):
		print(get_numbers(random.randint(7, 14)))
elif setting == "3":
	for i in range(5):
		print(get_both(random.randint(7, 14)))
else:
	print("Next time enter 1, 2, or 3")