a = int(input("enter a number a = "))
if a > 0:
 print("the number is positive")
elif a < 0:
 print("the number is negative")
if a == 0:
 print("the number is 0")
b = int(input("enter a number b =  "))
if b%2 == 0:
 print("the number is even")
elif b%2 == 1:
 print("the number is odd")
#  program to check if the input number is prime or not

number = int(input("Enter any number: "))                                  
if number > 1:
    for i in range(2, number - 1):
        if number % i == 0 :

            print(number, "is not a prime number")
        break
    else:
        print("it is a prime number")

else:
 print("it is not a prime number")
n=int(input("Enter number:"))
fact=1
while(n > 0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)
o = int(input("please enter a number o = "))

value = 1
print("factors of a give number o {0} are:".format(o))


while (value <= o):
    if (o % value == 0):
     print("{0}".format(value))
     value = value + 1
