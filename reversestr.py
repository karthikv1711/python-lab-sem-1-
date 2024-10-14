#2. Write a python program to reverse a given string without using a slicing operator?
str = input('Enter a String : ')
rev = ""
for i in str:
    rev = i+rev
print('Reversed String : ',rev)







''' 
output:

Enter a String : hello
Reversed String :  olleh



'''
