print('Введите Ваш рост в сантиметрах: ')
a = int(input())
print('Введите Ваш вес в килограммах: ')
b = int(input())
a = a / 100
m = b // a ** 2
m1 = int(m)
print('Ваш индекс массы тела:', m1)
x = 70 - m
x1 = int(x)
y = m - 10
y1 = int(y)
print('10',y1 * '=',m1,x1 * '=','70')