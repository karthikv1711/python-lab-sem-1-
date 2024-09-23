# reverse a list

l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = input("enter the value :")
	l.append(val)

print("list reverse using slicing : ",l[::-1])

r = []
for i in range(n-1,-1,-1):
	r.append(l[i])
	
print("reverse a list using for loop :",r)

l.reverse()
print("list reverse using method :",l)

