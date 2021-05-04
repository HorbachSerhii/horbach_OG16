import random
a = int(input("Укажите, сколько случайных данных хотите видеть:"))
b = int(input("Укажите минимальное значение:"))
c = int(input("Укажите, максимальное значение:"))
li = [random.randint(b,c) for i in range(a)]

print(li)


