chars = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter your string: ")
formula = input("Enter your formula: ")

output = ""

for i in range(len(word)):
	b = True
	for j in range(len(chars)):
		if word[i].lower() == chars[j].lower():
			x = j
			form = eval(formula.replace("x", str(x)))
			form2 = form % 26
			if word[i].isupper():
				output += chars[form2].upper()
			else:
				output += chars[form2].lower()
			b = False
	if b:
		output += word[i]


print(output)