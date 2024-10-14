#3. Write a python program to check if the given string is palindrome or not? 

str = input('Enter a String : ')

if str == str[::-1]:
    print('a Palindrome')
else :
    print('Not a Palindrome')

'''
output:
Enter a String : list
Not a Palindrome

'''
