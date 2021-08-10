import os
import shutil

def swapFileData():
    nameOfFile1 = input("Enter the name of the first file ")
    nameOfFile2 = input("Enter the name of the second file ")
    '''data_a = open(nameOfFile1,"r")
    data_b = open(nameOfFile2, "r")
    open(nameOfFile1,"w")'''
    with open(nameOfFile1,'r') as a:
        data_a = a.read()

    with open(nameOfFile2,'r') as b:
        data_b = b.read()

    with open(nameOfFile1,'w') as a:
        a.write(data_b)

    with open(nameOfFile2,'w') as b:
        b.write(data_a)

swapFileData()