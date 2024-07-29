n = int(input("Enter the value :"))
m = 1
for i in range (1,n+1,1) :
    if n == 0 :
        m = 1
        break
    m = m*i
print(f"{n} factorial = ",m)
