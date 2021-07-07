#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:38:24 2020

@author: Eric Tzimas
"""
from tkinter import *
import math
from Calculo import Calculo


# Creating the Tkinter window
window = Tk()
window.configure(bg='white')
# Defining the size of the window in width and height using the 'geometry' method
window.geometry("600x355")

# Preventing the window from getting resized
window.resizable(0, 0)

#Defining the title of the window

window.title("Sahara")
window.tk.call('tk','scaling',3.0)

# Defining the required functions for the Calculator to function properly.
con=[]
event=""

# 1. First is the button click 'btn_click' function which will continuously update the input field whenever a number is entered or any button is pressed it will act as a button click update.
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    con.append(item)    
# 2. Second is the button clear 'btn_clear' function clears the input field or previous calculations using the button "C"
def btn_clear(event):
    global expression
    expression = ""
    input_text.set("0")
    con.clear()
# 3. Third and the final function is button equal ("=") 'btn_equal' function which will calculate the expression present in input field. For example: User clicks button 2, + and 3 then clicks "=" will result in an output 5.
def btn_equal(event):
    

    global expression
    # 'eval' function is used for evaluating the string expressions directly
    # you can also implement your own function to evalute the expression istead of 'eval' function
    str1=""
    yo=str(str1.join(con))
    expression = ""
    if "x" in yo and "d" not in yo:
        
        input_text.set(Calculo.calcvi(yo))
    elif "d" in yo:
        input_text.set(Calculo.calcvi2(yo))
    else:
        input_text.set(Calculo.parenth(yo))
# 4. Fourth function deletes previous addition
def btn_del(event):
    global expression
    con.pop()
    stt=""
    input_text.set(str(stt.join(con)))
    if not con:
        input_text.set("0")
    expression=str(stt.join(con))
# 5. Method that calculates first degree equations   

    
expression = ""
# In order to get the instance of the input field 'StringVar()' is used
input_text = StringVar(value='0')

# Once all the functions are defined then comes the main section where you will start defining the structure of the calculator inside the GUI.

# The first thing is to create a frame for the input field
input_frame = Frame(window, width = 400, height = 50, bd = 0, bg = "white", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)


# Then you will create an input field inside the 'Frame' that was created in the previous step. Here the digits or the output will be displayed as 'right' aligned
input_field = Entry(input_frame, font = ('MS Serif', 35, 'bold'),fg='#111D3B', textvariable = input_text, width = 50, bg = 'white', bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is an internal padding to increase the height of input field


# Once you have the input field defined then you need a separate frame which will incorporate all the buttons inside it below the 'input field'
btns_frame = Frame(window, width = 465, height = 272.5, bg = 'white')

btns_frame.pack()

# Binding keys with widget functions

window.bind('<Return>',btn_equal)
window.bind('=',btn_equal)
window.bind('<c>',btn_clear)
window.bind('<BackSpace>',btn_del)
window.bind('0',lambda x: btn_click("0"))
window.bind('1',lambda x: btn_click("1"))
window.bind('2',lambda x: btn_click("2"))
window.bind('3',lambda x: btn_click("3"))
window.bind('4',lambda x: btn_click("4"))
window.bind('5',lambda x: btn_click("5"))
window.bind('6',lambda x: btn_click("6"))
window.bind('7',lambda x: btn_click("7"))
window.bind('8',lambda x: btn_click("8"))
window.bind('9',lambda x: btn_click("9"))
window.bind('.',lambda x: btn_click("."))
window.bind('/',lambda x: btn_click(" / "))
window.bind('*',lambda x: btn_click(" * "))
window.bind('-',lambda x: btn_click(" - "))
window.bind('+',lambda x: btn_click(" + "))
window.bind('d',lambda x: btn_click("d"))
window.bind('x',lambda x: btn_click("x"))
window.bind('^',lambda x: btn_click(" ^ "))
window.bind('(',lambda x: btn_click("( "))
window.bind(')',lambda x: btn_click(" )"))
window.bind('p',lambda x: btn_click("π"))
window.bind('r',lambda x: btn_click(" sq"))

delete = Button(btns_frame, text = "Del", fg = "black", width = 10, height = 3, bd = 0,borderwidth=0, bg = "white", cursor = "hand2", command = lambda: btn_del(event)).grid(row = 1, column = 4,  padx = 1, pady = 1)
clear = Button(btns_frame, text = "Clear", fg = "black", width = 32,relief='flat',height = 3, bd = 0, highlightbackground="white", bg = "white", cursor = "hand2", command = lambda: btn_clear(event)).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" / ")).grid(row = 0, column = 3, padx = 1, pady = 1)


seven = Button(btns_frame, text = "7",fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("7")).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("8")).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("9")).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" * ")).grid(row = 1, column = 3, padx = 1, pady = 1)


four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg='white', cursor = "hand2", command = lambda: btn_click("4")).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click("5")).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click("6")).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click(" - ")).grid(row = 2, column = 3, padx = 1, pady = 1)


one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("1")).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("2")).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("3")).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" + ")).grid(row = 3, column = 3, padx = 1, pady = 1)
# The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
X2 = Button(btns_frame, text = "X2", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("d")).grid(row = 2,column = 4, padx = 1, pady = 1)
X = Button(btns_frame, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("x")).grid(row = 3, column = 4, columnspan = 1, padx = 1, pady = 1)
POW = Button(btns_frame, text = "x^n", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" ^ ")).grid(row =0, column = 4, padx = 1, pady = 1)

zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("0")).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".",fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 32, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_equal(event)).grid(row = 4, column = 3,columnspan=3, padx = 1, pady = 1)

par1 = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg='white', cursor = "hand2", command = lambda: btn_click("( ")).grid(row = 0, column = 5, padx = 1, pady = 1)
par2 = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click(" )")).grid(row = 1, column = 5, padx = 1, pady = 1)
pi = Button(btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click("π")).grid(row = 2, column = 5, padx = 1, pady = 1)
root = Button(btns_frame, text = "√x", fg = "black", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click(" sq")).grid(row = 3, column = 5, padx = 1, pady = 1)

window.mainloop()
