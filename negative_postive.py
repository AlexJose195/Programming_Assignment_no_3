# Write a Python Program to Check if a Number is Positive, Negative or Zero.

print("Checking whether the number is Positive , Negative or Zero\n")
a = int(input("Enter any number : "))

if a < 0:
    print(a," is a Negative number.")

elif a>0:
    print(a," is a Positive number.")

else:
    print("The number is Zero.")