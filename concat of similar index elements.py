# concatenation of two lists

l1 = ["M","na","i","Abhi"]
l2 = ["y","me","s","Ram"]


for i in l1 :
	for j in l2 :
		if l1.index(i) == l2.index(j) :
			print(i+j,end=" ")
print()

# Output : My name is AbhiRam
