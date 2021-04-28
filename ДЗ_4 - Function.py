v1 = float(input("Введите первое число:  "))
oper = str(input("Выберите действие: (+,-,/,*)  "))
v2 = float(input("Введите второе число:  "))
def calc(v1, oper, v2):
    if oper == "+":
        res = v1 + v2
        print("RESULT is: ", res)
    elif oper == "-":
        res = v1 - v2
        print("RESULT is: ", res)
    elif oper == "*":
        res = v1 * v2
        print("RESULT is: ", res)
    elif oper == "/":
        if v2 != 0:
            v1 / v2
            print("RESULT is: ", v1/v2)
        elif v2 == 0:
            print("Wrong!!! No dividing on '0'!!!")
    else:
        oper != "+","-","/","*"
        print("No!!! You are wrong!!! Try Again!!!")

calc(v1, oper, v2)