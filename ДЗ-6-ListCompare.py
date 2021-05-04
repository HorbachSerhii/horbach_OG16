import random
a = int(input("Please, write the quantity of items You want to see:"))
b = int(input("Write the minimum value:"))
c = int(input("Write the maximum value:"))
li = [random.randint(b,c) for i in range(a)]

print(li)

a = input("Type some theese or else numbers with 'spacebar':").split()
a = [int(i) for i in a]
print(a)


if li==a:
    print("List are equal")
while li != a:
    c = []
    d = []
    for x in li:
        if not x in a:
            c.append(x)
    print("The number in 1st list that don`t appear in 2nd",c)

    for x in a:
        if not x in li:
         d.append(x)
    print("The number in 2nd list that don`t appear in 1st",d)
    break
