
# This program get defference of the 2 main diagonals and return the difference
# Question and the sample is in the readme file

import math                                             # math library provides the abs () function

def MatrixInsertion ():
    n = int (input ("size = "))
    list = []                                           # get the 2D array to a list

    for i in range (n):
        rawList = []                                    # another list for get raw values
        for j in range (n): 
            rawList.append (int (input ("ele = ")))     # get input for raw values
        list.append (rawList)                           # append raw values in to the list

    #print (list [0][0])
    d_1 = 0                                             # left to right diagonal
    d_2 = 0                                             # right to left diagonal

    for i in range (n):
        d_1 = d_1 + list [i][i]                         # get the sum of left to right diagonal
        d_2 = d_2 + list [i][n-1-i]                     # get the sum of right to left diagonal

    #print (d_1)
    #print ("d_2 =", d_2)
    #res = getDifference (d_1, d_2)
    return getDifference(d_1, d_2)                      # call the getDifference function

def getDifference (x, y):                             # this function return the absolute difference between 2 diagnols 
    return abs (x-y)                                    # return the absolute difference

#answer = MatrixInsertion ()
print("difference =", MatrixInsertion())                # function calling and print the output


