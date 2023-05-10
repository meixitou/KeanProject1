import numpy as np
import random
import math

def daan():                                          #we use this function to generate an actul answer
    shudu = np.zeros((9,9),dtype=int)                 #generate an array of all 0 ready to be used
    while (sum(sum(shudu[:,:]))!=405):                #judge is the answer correct
        n = 1
        A = np.zeros((9,9), dtype=int)
        a = [x for x in range(1, 10)]                 #generate an array of 1-9 ready to be used
        b = [x for x in range(1, 10)]
        random.shuffle(b)                              #generate random 1-9 array used for the first line of Sudoku
        A[0,:] = b                                     #here we given value
        for i in range(1,9):                            #start fill numbers in
            for j in range(0,9):
                x = A[i,:]                              #get the row out
                y = A[:,j]                               #get the column out
                if 0<=j and j<3:
                    z = A[:,0:3]
                elif 3<=j and j<6:
                    z = A[:,3:6]
                else :
                    z = A[:,6:9]
                if 0 <= i and i < 3:
                    z = z[0:3,:]
                elif 3 <= i and i < 6:
                    z = z[3:6,:]
                else:
                    z = z[6:9,:]                         #get the 3x3 box out

                x_pos = np.nonzero(x)[0]                   #get all none 0 value in all row, column and box
                X = np.zeros((len(x_pos)), dtype=int)
                for p in range(0, len(x_pos)):
                    X[p] = x[x_pos[p]]

                y_pos = np.nonzero(y)[0]
                Y = np.zeros((len(y_pos)), dtype=int)
                for p in range(0, len(y_pos)):
                    Y[p] = y[y_pos[p]]

                z_pos = np.transpose(np.nonzero(z))
                Z = np.zeros((len(z_pos)), dtype=int)
                for p in range(0,len(z_pos)):
                    m = z_pos[p,0]
                    n = z_pos[p,1]
                    Z[p] = z[m,n]


                t = list(set(X).union(set(Y)))
                t = list(set(t).union(set(Z)))                 #union all none 0 value

                n = list(set(a).difference(set(t)))            #find difference and judge what numbers can still be fill

                try:
                    L = len(n)                                #judge if there is number left
                except BaseException as e:
                    L = 0

                r = random.random()

                h = math.ceil(r*L)                            #randomly choose one
                try:
                    A[i,j] = n[h-1]                            #give value to empty space
                except BaseException as e:
                    n = 2                                      #if get wrong, then means we have error when fill the number
                    break
            if n == 2:
                break
        if n == 2:
            continue                                          #restart the loop
        shudu = A                                              #if all 81 numbers are correct, then given value to the Sudoku
    return shudu                                               #given Sudoku


def chansheng(shudu,grade):                                  #randomly get numbers out to create different difficulty of our Sudoku
    for i in range(0,9):
        b = [x for x in range(0, 9)]
        random.shuffle(b)
        for j in range(0,grade):
            shudu[i,b[j]] = 0
    return shudu


def xiugai(shudu,pos,pos_nonling):                          #input parameter to change the number
    x = int(pos/100)                                        #get position of row
    y = int((pos%100)/10)                                  #get position of column
    for i in range(0,len(pos_nonling)):                     #pos_nonling represents all none 0 value in our question
        a = int(pos_nonling[i,0])
        b = int(pos_nonling[i,1])
        if x-1 == a and y-1 == b:
            print('You can not change anything here, please choose again!')                    #numbers on these position can not be changed
            n = 2
            return shudu,n
    num = int((pos%100)%10)                                   #if not, we can change the value in Sudoku
    shudu[x-1,y-1] = num
    n = 1                  #check if we changed correctly
    return shudu,n           #return results after changing



def jiancha(shudu,pos,shibai):                     #check if the number that user input is correct or not
    a = int(pos/100)                                        #get value of row
    b = int((pos%100)/10)                                  #get value of column
    c = int((pos%100)%10)                                   #get value that input
    shudu[a-1,b-1] = 0

    x = shudu[a-1, :]
    y = shudu[:, b-1]
    if 0 <= b-1 and b-1 < 3:
        z = shudu[:, 0:3]
    elif 3 <= b-1 and b-1 < 6:
        z = shudu[:, 3:6]
    else:
        z = shudu[:, 6:9]


    if 0 <= a-1 and a-1 < 3:
        z = z[0:3, :]
    elif 3 <= a-1 and a-1 < 6:
        z = z[3:6, :]
    else:
        z = z[6:9, :]

    x_pos = np.nonzero(x)[0]
    X = np.zeros((len(x_pos)), dtype=int)
    for p in range(0, len(x_pos)):
        X[p] = x[x_pos[p]]

    y_pos = np.nonzero(y)[0]
    Y = np.zeros((len(y_pos)), dtype=int)
    for p in range(0, len(y_pos)):
        Y[p] = y[y_pos[p]]

    z_pos = np.transpose(np.nonzero(z))
    Z = np.zeros((len(z_pos)), dtype=int)
    for p in range(0, len(z_pos)):
        m = z_pos[p, 0]
        n = z_pos[p, 1]
        Z[p] = z[m, n]

    t = list(set(X).union(set(Y)))
    t = list(set(t).union(set(Z)))                          #here we use the same logic of generating answers，we get all numbers that can not be input

    if c in t:                                                #same as numbers that can not be input
        shibai = shibai+1
        print('You can not put anything here!', c)
        print("You have failed %d times!" % (shibai))
        print("Fail time left：", shibaicishu - shibai)
        shudu[a-1, b-1] = 0                                   #vanish this time of input
        return  shibai
    else:
        shudu[a-1, b-1] = c                                  #if it is differnet, then we give value
        return  shibai


def jieshu(shudu):                                      #we check if the game is over
    if sum(sum(shudu[:, :])) == 405:
        return 1
    else:
        return 2


def show(shudu,pos_nonling):                          #show every step
    for i in range(0,10):
        for j in range(0,10):
            if i == 0 and j == 0:
                print('\t',end='')
            if i == 0 and j != 0:
                print('\033[34m',j,'\t',end='')         #we use purple as row index
                if j == 9:
                    print('\n')                               #we change row here
            if i != 0 and j == 0:
                print('\033[34m',i,'\t',end='')              #we use purple as column index
            if i != 0 and j != 0:
                if shudu[i-1,j-1] == 0:
                    print('\033[0m',' ', '\t', end='')          #we dont show the empty number
                else:
                    for m in range(0, len(pos_nonling)):
                        a = int(pos_nonling[m, 0])
                        b = int(pos_nonling[m, 1])
                        if i - 1 == a and j - 1 == b:
                            key = 1
                            break
                        else:
                            key = 2
                    if key == 1:
                        print('\033[0m', shudu[i-1,j-1], '\t', end='')               #we use white as problem numbers
                    else:
                        print('\033[31m', shudu[i - 1, j - 1], '\t', end='')         #we use red to show the numbers that can be input
                if j == 9:
                    print('\n')                                                        #change row


if __name__ == '__main__':


    print('Game Start!')
    global shibai
    shibai = 0    #count fail time


    try:
        grand = int(input('Please choose your difficulty from 1-6：'))                                          #get empty space
        while (grand < 1 or grand > 6):                                           #minimum get 1 empty, maximum 6
            try:
                grand = int(input('Wrong input, please enter an integer between 1-6：'))
            except BaseException as e:
                continue
    except BaseException as e:
        grand = 0
        while(grand<1 or grand>6):
            try:
                grand = int(input('Wrong input, please enter an integer between 1-6：'))
            except BaseException as e:
                continue

    try:
        shibaicishu = int(input('Please choose the error time that you pre-set：'))                           #wrong input time that we allowed
        while (shibaicishu < 1):
            try:
                shibaicishu = int(input('Wrong input, please given an positive integer：'))
            except BaseException as e:
                continue
    except BaseException as e:
        shibaicishu = 0
        while(shibaicishu<1):
            try:
                shibaicishu = int(input('Wrong input, please given an positive integer：'))
            except BaseException as e:
                continue

    shudu_answer= daan()                                           #generate Sudoku


    shudu_question = chansheng(shudu_answer,grand)               #get empty
    pos_nonling = np.transpose(np.nonzero(shudu_question))         #get position of none 0
    show(shudu_question,pos_nonling)                             #show

    while(1):
        n = 2                                               #we sign here whether the input is correct or not
        while(n == 2):
            try:
                pos = int(input('Please enter a number that you want:'))          #given a 3 digit number, first represents row number, second column, third is what
                while (pos < 111 or pos > 999):                #you want to input, minimum 111, maximum 999
                    try:
                        pos = int(input('You have error on input，please give a three digit number，first row，second column，third is what you want to inpupt:'))
                    except BaseException as e:
                        continue
            except BaseException as e:
                pos = 0
                while (pos < 111 or pos > 999):
                    try:
                        pos = int(input('You have error on input，please give a three digit number，first row，second column，third is what you want to inpupt: '))
                    except BaseException as e:
                        continue
            [shudu_change,n] = xiugai(shudu_question,pos,pos_nonling)                                        #change the Sudoku

        shibai = jiancha(shudu_change,pos,shibai)                                                            #judge if the wrong or not
        if shibai == shibaicishu:                                                                            #if the wrong time meet the set up time, then we lost
            key_finish = 1
            break
        show(shudu_change,pos_nonling)
        stop = jieshu(shudu_change)                   #judge if all empty are filled up
        if stop == 1:
            key_finish = 2
            break
    if key_finish == 1:
        print('GAME OVER, YOU FAILED!')
    else:
        print('CONGRATULATIONS, YOU ARE ALL CORRECT!')








