import time
while True:
    import datetime
    tn = datetime.datetime.now()
    t = tn.strftime("%H%M%S")
    t1 = t[0]
    t2 = t[1]
    t3 = t[2]
    t4 = t[3]
    t5 = t[4]
    t6 = t[5]
    zero = {0: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
        1: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        2: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        3: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        4: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    one = {0: "\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B",
       1: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1B\u2B1B\u2B1B",
       2: "\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B",
       3: "\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B",
       4: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1B\u2B1B"}
    two = {0: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
       1: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
       2: "\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B",
       3: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B",
       4: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    three = {0: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
         1: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
         2: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
         3: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
         4: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    four = {0: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        1: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        2: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
        3: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        4: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B"}
    five = {0: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
        1: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B",
        2: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
        3: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        4: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    six = {0: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
       1: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B",
       2: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
       3: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
       4: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    seven = {0: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
         1: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
         2: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B",
         3: "\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B",
         4: "\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1B"}
    eight = {0: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
         1: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
         2: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
         3: "\u2B1B\u2B1C\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
         4: "\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    nine = {0: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
        1: "\u2B1B\u2B1B\u2B1C\u2B1B\u2B1B\u2B1C\u2B1B",
        2: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B",
        3: "\u2B1B\u2B1B\u2B1B\u2B1B\u2B1B\u2B1C\u2B1B",
        4: "\u2B1B\u2B1B\u2B1C\u2B1C\u2B1C\u2B1C\u2B1B"}
    on = {0: "\u2B1B\u2B1B\u2B1B",
              1: "\u2B1B\u2B1C\u2B1B",
              2: "\u2B1B\u2B1B\u2B1B",
              3: "\u2B1B\u2B1C\u2B1B",
              4: "\u2B1B\u2B1B\u2B1B"}
    off = {0: "\u2B1B\u2B1B\u2B1B",
              1: "\u2B1B\u2B1B\u2B1B",
              2: "\u2B1B\u2B1B\u2B1B",
              3: "\u2B1B\u2B1B\u2B1B",
              4: "\u2B1B\u2B1B\u2B1B"}
    d = {
    '0':zero,
    '1':one,
    '2':two,
    '3':three,
    '4':four,
    '5':five,
    '6':six,
    '7':seven,
    '8':eight,
    '9':nine,
    }
    for i in range(0,4):
        print(d[t1][i], d[t2][i], on[i], d[t3][i], d[t4][i], off[i] d[t5][i], d[t6][i])
    time.sleep(0.9)
    import os
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
    cls()