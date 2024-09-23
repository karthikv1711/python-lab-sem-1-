#interchage first and last element of the list

l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = input("enter the value :")
	l.append(val)
	
temp = l[n-1]
l[n-1] = l[0]
l[0] = temp

print(l)
