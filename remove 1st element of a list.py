# remove first occuance of a list

l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = input("enter the value :")
	l.append(val)
	
l.remove(l[0])
print(l)
