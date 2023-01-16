barcode = input("Enter the Code Code Here: ")

def _12digit(bar):
	odd = 0
	even = 0
	for i in range(len(bar) - 1):
		if(i % 2) == 0:
			odd += int(bar[i])
		else:
			even += int(bar[i])
	odd *= 3
	total = odd + even
	rem = 10 - (total % 10)
	if int(bar[len(bar) - 1]) == rem:
		return "This is authentic"
	else:
		return "This is not"

def _13digit(bar):
	odd = 0
	even = 0
	for i in range(len(bar) - 1):
		if(i % 2) == 0:
			odd += int(bar[i])
		else:
			even += int(bar[i])
	even *= 3
	total = odd + even
	rem = total % 10
	if rem == 0:
		return "This is authentic"
	else:
		if int(bar[len(bar) - 1]) == rem:
			return "This is authentic"
		else:
			return "This is not"

if len(barcode) == 12:
	b = _12digit(barcode)
	print(b)
elif len(barcode) == 13:
	b = _13digit(barcode)
	print(b)
else:
	print("This is not 12 or 13 digit Barcode Numbers")