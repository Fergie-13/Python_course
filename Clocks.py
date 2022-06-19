import time
import os
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
    separator1 = {0: "\u2B1B\u2B1B\u2B1B",
              1: "\u2B1B\u2B1C\u2B1B",
              2: "\u2B1B\u2B1B\u2B1B",
              3: "\u2B1B\u2B1C\u2B1B",
              4: "\u2B1B\u2B1B\u2B1B"}
    separator2 = {0: "\u2B1B\u2B1B\u2B1B",
              1: "\u2B1B\u2B1B\u2B1B",
              2: "\u2B1B\u2B1B\u2B1B",
              3: "\u2B1B\u2B1B\u2B1B",
              4: "\u2B1B\u2B1B\u2B1B"}
    d = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    'sep1':'separator1',
    'sep2':'separator2'
    }
    for i in range(0,6):
        print(t1[i], t2[i], t3[i], t4[i], t5[i], t6[i])
    time.sleep()
    os.system('CLS')