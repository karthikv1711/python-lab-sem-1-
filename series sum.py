#1/1!+2/2!+3/3!+..........+n/n!
n = int(input("n = "))
m = 1
sum = 0
for i in range (1,n+1,1) :
    m =m * i
    sum = sum + (i/m)
print("Series sum =",sum)
