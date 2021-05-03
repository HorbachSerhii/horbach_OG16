variable1 = float(input("Введите первое число:  "))
operation: list[str] = str(input("Выберите действие: (+,-,/,*)  "),)
variable2 = float(input("Введите второе число:  "))

if operation == '+':    result: float = variable1 + variable2
elif operation == '-':    result: float = variable1 - variable2
elif operation == '*':    result: float = variable1 * variable2
elif operation == '/':    result: float = variable1 / variable2
print("Результат:   ",str(result))
