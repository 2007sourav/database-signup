import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import csv

########################################################################################################################################
def create():             # FUNCTION TO CHECK IF RECORDS FILE IS PRESENT (INCASE IF ITS THE FIRST RECORD)
    if os.path.isfile("D:\\pythonpro\\login\\records.txt"):
        pass
    else:
        f=open("D:\\pythonpro\\login\\records.txt","w")
        f.close()
                        #########################################################################################
def signup():             # FUNCTION FOR SIGNUP
    record=[]
    user=input("Enter Username :- ")
    create()
    fr=open("D:\\pythonpro\\login\\records.txt","r")
    r=csv.reader(fr)
    for i in r:
        if i[0]==user:
            print("Error : Username Already Exists")
            user=input("Enter Username :- ")
        else:
            break
    fr.close()
    pwd=input("Enter Password :- ")
    fw=open("D:\\pythonpro\\login\\records.txt","a",newline='')
    w=csv.writer(fw)
    w.writerow([user,pwd])
    fw.close()
########################################################################################################################################
flag=0
def check():
    if os.path.isfile("D:\\pythonpro\\login\\records.txt"):
        pass
    else:
        print("Database Is Empty")
        global flag
        flag=1






def login():             # FUNCTION FOR LOGGING IN
    user=input("Enter Username :- ")
    pwd=input("Enter Password :- ")
    check()
    if flag==0:
        fr=open("D:\\pythonpro\\login\\records.txt","r")
        r=csv.reader(fr)
        for i in r:
            if i[0]==user and i[1]==pwd:
                print("Worked")
                break
            else:
                print("Username And Password Combination Is Incorrect")
                user=input("Enter Username :- ")
                pwd=input("Enter Password :- ")
        print("you have entered congrats")
        fr.close()
    else:
        pass
########################################################################################################################################
print("Choose An Option")             # MAIN BODY
print("1. Sign Up")
print("2. Login")
x=int(input("Choose An Option (1/2) :- "))
if x==1:
    signup()
else:
    login()



