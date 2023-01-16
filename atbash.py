alpha = "abcdefghijklmnopqrstuvwxyz"
pelindrome = ""

def isUp(x, y):
	if x.isupper():
		return y.upper()
	else:
		return y.lower()


for i in range(len(alpha) - 1, -1, -1):
	pelindrome += alpha[i]

txt = input("Enter your string: ")
output = ""

for i in range(len(txt)):
	x = True
	for j in range(len(alpha)):
		if pelindrome[j] == txt[i].lower():
			output += isUp(txt[i], alpha[j])
			x = False
			break
	if x:
		output += txt[i]

print(f"Result: {output}")