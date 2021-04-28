v1 = float(input("Введите первое число:  "))
v2 = float(input("Введите второе число:  "))

def compare(v1,v2):
    if v1>v2:
        return ("Success")
    elif v1==v2:
        return ("Almost")
    elif v1<v2:
        return ("Loser")
print("Result is:    ", compare(v1, v2))
compare(v1,v2)
