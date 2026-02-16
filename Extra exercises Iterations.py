divisor = 3
for num in range(0,12,3):
    print(num/divisor)
# This will print the divison of 0/3; 12/3, and 3/3: 0, 4, 1

for letter in 'Ahola':
    print(letter)
#this will print one by one the letters that compose Ahola

num = 0
while num <= 5:
    print(num)
    num += 2
print("out")
print(num)



#MULTIPLICTION TABLE
for a in range(1,11):
    for b in range(a, 11): #starting from a and not from 1 will avoid repetitions.
        print(f"{a} * {b} = {a*b}")

# Suppose you can only do additions. Write a program that reads two positive, integer numbers a and b. It
# computes a**b.

# Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same
# value. Example of palindrome numbers: 123454321, 999, 1598951)
num = (input("Enter a number: "))
if num == num[:: -1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

