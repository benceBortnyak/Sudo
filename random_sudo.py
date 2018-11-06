# andom list generator

import random

rand_su_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rand_su_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def uu():

    random.shuffle(rand_su_1)
    random.shuffle(rand_su_2)
    random.shuffle(rand_su_3)
    random.shuffle(rand_su_4)
    random.shuffle(rand_su_5)
    random.shuffle(rand_su_6)
    random.shuffle(rand_su_7)
    random.shuffle(rand_su_8)
    random.shuffle(rand_su_9)

sudo_all = [
    rand_su_1,
    rand_su_2,
    rand_su_3,
    rand_su_4,
    rand_su_5,
    rand_su_5,
    rand_su_6,
    rand_su_7,
    rand_su_8,
    rand_su_9,
    ]


def check():
    for i in range(0, 9):
        avg = 0
        for j in range(0, 9):
            avg = avg + int((sudo_all[j][i]))
        endnum = (avg / 9)
        if endnum != 5:
            return False
        elif endnum == 5:
            return True


def main():
    while check() == False:
        uu()
        check()
    if check() == True:
            for u in range(0, 8):
                randr2 = random.randrange(1, 8)
                for u in range(0, 10):
                    randr = random.randrange(0, 7)
                    sudo_all[u][randr] = " "
            print(sudo_all)

main()