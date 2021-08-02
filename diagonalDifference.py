
# This program get defference of the 2 main diagonals and return the difference

import math

def MatrixInsertion ():
    n = int (input ("size = "))
    list = []

    for i in range (n):
        rawList = []
        for j in range (n):
            rawList.append (int (input ("ele = ")))
        list.append (rawList)

    #print (list [0][0])
    d_1 = 0                                             # left to right diagonal
    d_2 = 0

    for i in range (n):
        d_1 = d_1 + list [i][i]
        d_2 = d_2 + list [i][n-1-i]

    #print (d_1)
    #print ("d_2 =", d_2)
    #res = getDifference (d_1, d_2)
    return getDifference(d_1, d_2)

def getDifference (x, y):                             # this function return the absolute difference between 2 diagnols 
    return abs (x-y)

#answer = MatrixInsertion ()
print("difference =", MatrixInsertion())                # function calling


