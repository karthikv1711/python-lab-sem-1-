#5. Write a python program to count the number of vowels in the string? 

str = input('Enter a String : ')
count = 0
for i in str :
    if i in "'a','A','e','E','i','I','o','O','u','U'" :
        count += 1
print('vowel count :',count)


'''
output:
Enter a String : hello
vowel count : 2

'''
