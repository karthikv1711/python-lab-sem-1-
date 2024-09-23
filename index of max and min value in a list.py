# position of minimum and maximum value

l = []

n = int(input("Enter size of the list : "))

for i in range(n):
	val = float(input("enter the value :"))
	l.append(val)

maxi = max(l)
mini = min(l)
print("maximim value :",maxi," index :",l.index(maxi))
print("minimum value :",mini," index :",l.index(mini))
