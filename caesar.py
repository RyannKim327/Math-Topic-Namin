base = 97
characters = 26
txt = input("Enter your text here: ")
num = int(input("Enter number offset: "))
output = ""

for i in range(len(txt)):
	if txt[i].isalpha():
		conv = ord(txt[i].lower()) + num
		if conv < base:
			conv += characters
		elif conv > 122:
			conv -= characters
		
		if txt[i].isupper():
			output += chr(conv).upper()
		else:
			output += chr(conv).lower()
	else:
		output += txt[i]

print(output)