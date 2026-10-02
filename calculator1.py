print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Введите нужную операцию")
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
else:
    print(a / b)
