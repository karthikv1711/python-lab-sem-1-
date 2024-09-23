# Seperate even and odd numbers from a list
l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = int(input("enter the value :"))
	l.append(val)
	
even = []
odd = []

for i in l :
	if i%2 == 0 :
		even.append(i)
	else :
		odd.append(i)

print("Even list = ",even)
print("Odd list = ",odd)
