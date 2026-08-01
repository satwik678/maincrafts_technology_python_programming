#1. Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

#2. Odd or Even Checker
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#3. Factorial Calculation
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


#4. Fibonacci Sequence
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
    
#5. String Reverse
text = input("Enter a string: ")

print("Reversed string:", text[::-1])


#6. Palindrome Check
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
    
#7. Leap Year Check
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
    
#8. Armstrong Number
num = int(input("Enter a number: "))

total = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")