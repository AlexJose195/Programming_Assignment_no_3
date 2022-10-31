# Write a Python Program to Print all Prime Numbers in an Interval of 1-10000.
k=10000

l=[]
for a in range(k):
    if a == 0:
        continue
    elif a == 1:
        continue
    elif a == 2:
        l.append(a)
    elif a == 3:
        l.append(a)
    else:
        for i in range(2, a):
            if a % i == 0:
                break
        else:
          l.append(a)
print(l)
