def gen_number():
    num = 1
    while True:
        if num % 3 == 0:
            print('Василий')
            num = num + 1
        yield num
        num += 1
gen = gen_number()
for _ in range(1,11):
    print(next(gen))