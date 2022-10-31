# Write a Python Program to Check Prime Number.

print("\nChecking whether the number is Prime or not.\n")
a = int(input("Enter any number : "))

if a == 0:
    print(a," is a not a prime number")

elif a < 0 :
    print(" Please enter positive number")

elif a == 1:
    print(a," is a not a prime number")


elif a == 2:
    print(a," is  prime number")

elif a == 3:
    print(a," is  prime number")
else:
    for i in range(2,a):
        if a%i ==0:
         print(a," is a not Prime Number")
         break
    else:
     print(a," is a Prime number")



