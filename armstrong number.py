n = int(input("Enter the number:"))
num = n
sum = 0
r = 0
while num>0 :
   r = num%10
   sum = sum + (r ** 3)
   num = num//10 
if (sum == n ):
   print(f"{n} is a Armstrong number")
else :
    print(f"{n} is not a Armstrong number")
