n = int(input("Enter a number:"))
temp = n
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if n == reverse:
  print(f'{n} is a Palindrome')
else:
  print(f"{n} is not a Palindrome")

