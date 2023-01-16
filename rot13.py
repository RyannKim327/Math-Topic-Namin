alpha = "abcdefghijklm"
alpha2 = "nopqrstuvwxyz"

def isUp(x, y):
	if x.isupper():
		return y.upper()
	else:
		return y.lower()

txt = input("Enter your string: ")
output = ""

for i in range(len(txt)):
	x = True
	for j in range(len(alpha)):
		if(alpha[j] == txt[i].lower()):
			output += isUp(txt[i], alpha2[j])
			x = False
			break
		
		if(alpha2[j] == txt[i].lower()):
			output += isUp(txt[i], alpha[j])
			x = False
			break
		
	if x:
		output += txt[i]

print(f"Result: {output}")