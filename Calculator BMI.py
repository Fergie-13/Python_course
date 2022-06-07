print('Введите Ваш рост в сантиметрах: ')
a = int(input())
print('Введите Ваш вес в килограммах: ')
b = int(input())
a = a / 100
m = b // a ** 2
m1 = int(m)
print('Ваш индекс массы тела:', m1)
x = 50 - m
x1 = int(x)
y = m - 15
y1 = int(y)
print('15',y1 * '=',m1,x1 * '=','50')
print('Введите Ваш пол строчными буквами: ')
c = input()
print('Введите Ваш возраст: ')
d = int(input())
if 18.5 < m1 < 25:
    print('Ваш показатель ИМТ в пределах нормы. Однако не стоит расслабляться, он может быстро измениться.\n Следите за своим здоровьем и все будет хорошо:) ')

if m1 < 18.5 and c == 'мужской':
    if d < 14:
        print('Mtest1')
    elif 15 < d < 50:
        print('Mtest2')
    elif d > 50:
        print('Mtest3')
        
if m1 < 18.5 and c == 'женский':
    if d < 14:
        print('Ftest1')
    elif 15 < d < 50:
        print('Ftest2')
    elif d > 50:
        print('Ftest3')
        
if 25 < m1 < 30 and (c == 'мужской' or c == 'женский'):
    if d < 14:
        print('MMtest1')
    elif 15 < d < 50:
        print('MMtest2')
    elif d > 50:
        print('MMtest3')
    
if m1 > 30 and (c == 'мужской' or c == 'женский':
    if d < 14:
        print('MMMMtest1')
    elif 15 < d < 50:
        print('MMMMtest2')
    elif d > 50:
        print('MMMMtest3')    