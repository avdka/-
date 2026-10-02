def f1(a, b):
    return a + b
def f2(a, b):
    return a - b
def f3(a, b):
    return a * b
def f4(a, b):
    return a / b

print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Введите нужную операцию")
c = input()
if c == "+":
    print(f1(a, b))
elif c == "-":
    print(f2(a, b))
elif c == "*":
    print(f3(a, b))
else:
    print(f4(a, b))
