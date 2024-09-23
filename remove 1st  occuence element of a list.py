# remove first occuance of a given element in a list without using any methods in python

l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = int(input("enter the value :"))
	l.append(val)
	
l.sort()
for i in l :
	c = l.count(i)
	if c>1 :
		l.remove(i)
		break	
print("list = ",l)
		
# l = [1,2,2,3,3]
# output : l = [1,2,3,3]
