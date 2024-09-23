l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = int(input("enter the value :"))
	l.append(val)

print("List = ",l)
sum = 0
for i in l :
	sum += i

avg = sum/n
print("SUM = ",sum)
print("Average : ",avg)
