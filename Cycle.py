a = int(input())
b = int(input())
c = int(input())
V = a == 0 or b == 0 or c == 0 or 'Нет нулевых значений!!!'
print(V)
S = a or b or c or 'Введены все нули!'
S
if a > b + c:
    print(a - b - c)
elif a < b + c:
    print(b + c - a)
if a > 50 and (a < b or a < c):
    print('Вася')
elif a > 5 or (b == 7 and c == 7):
    print('Петя')