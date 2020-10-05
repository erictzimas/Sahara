#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:38:24 2020

@author: Eric Tzimas
"""
from tkinter import *
import math


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

photo=PhotoImage(file= r"/Applications/sahara.app/Contents/MacOS/naveric.png")
photo2=PhotoImage(file= r"/Applications/sahara.app/Contents/MacOS/naveric2.png")
photo3=PhotoImage(file= r"/Applications/sahara.app/Contents/MacOS/naveric4.png")
photo4=PhotoImage(file= r"/Applications/sahara.app/Contents/MacOS/naveric6.png")

photoimage = photo.subsample(3,3)
photoimage2=photo2.subsample(3,3)
photoimage3=photo3.subsample(3,3)
photoimage4=photo4.subsample(3,3)


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
        
     input_text.set(calcvi(yo))
    elif "d" in yo:
        input_text.set(calcvi2(yo))
    else:
        input_text.set(parenth(yo))
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
def calcvi(str1):
    
    c=str1.split(" ")
    obj=[]
    obj2=[]
    quant=[]
    str2=" "
    str3=" "

    if "d" not in c:
        if "x" in c[0]:
                obj.append(c[0])
              
        elif c[0].isnumeric()  :
                quant.append(c[0])
                
        for i in range(1,len(c)):
            if "x" in c[i]:
                    obj.append(c[i-1])
                    obj.append(c[i])
               
                       
      
            elif c[i].isnumeric() :
                
                    
                    quant.append(c[i-1])
                    quant.append(c[i]) 
        for i in range(0,len(obj)):
            if "x" in obj[i]:
                s=obj[i].split()
                if not obj[i][0].isnumeric():
               
                    obj[i]=obj[i].replace("x","1")
                else:
                    
                    obj[i]=obj[i].replace("x"," * 1")
        if not obj[0].isnumeric():
            if obj[0]=="-":
                obj.remove(obj[0])
                obj[0]=str(-1*int(obj[0]))
            elif obj[0]=="+":
                obj.remove(obj[0])
        if not quant[0].isnumeric():
            if quant[0]=="-":
                quant.remove(quant[0])
                quant[0]=str(-1*int(quant[0]))
            elif quant[0]=="+":
                quant.remove(quant[0])
        leftside=calc2(str2.join(obj))
        rightside=calc2(str3.join(quant))
        ans= (-1*rightside)/leftside
       
        answer= "X = ", ans
   
    return answer
# 6. Method that calculates second degree equations
def calcvi2(str1):
 c=str1.split(" ")
 obj=[]
 obj2=[]
 quant=[]
 str2=" "
 str3=" "
 str4=" "
 xtrigger=False
 if "x" in c[0]:
     obj.append(c[0])
 elif "d" in c[0]:
     obj2.append(c[0])
    
 elif c[0].isnumeric():
     quant.append(c[0])
 for i in range(1,len(c)):
              if "x" in c[i]:
                    obj.append(c[i-1])
                    obj.append(c[i])
                    xtrigger=True
               
              if "d" in c[i]:
                    obj2.append(c[i-1])
                    obj2.append(c[i])
              elif c[i].isnumeric() :
                
                    
                    quant.append(c[i-1])
                    quant.append(c[i]) 
 if xtrigger==True:
     for i in range(0,len(obj)):
                if "x" in obj[i]:
                    s=obj[i].split()
                    if not obj[i][0].isnumeric():
                   
                        obj[i]=obj[i].replace("x","1")
                    else:
                        
                        obj[i]=obj[i].replace("x"," * 1")
                 
     if not obj[0].isnumeric():
                  if obj[0]=="-":
                    obj.remove(obj[0])
                    obj[0]="-"+obj[0]
                  elif obj[0]=="+":
                    obj.remove(obj[0])
 for i in range(0,len(obj2)):
            if "d" in obj2[i]:
                s=obj2[i].split()
                if not obj2[i][0].isnumeric():
               
                    obj2[i]=obj2[i].replace("d","1")
                else:
                    
                    obj2[i]=obj2[i].replace("d"," * 1")
 if not obj2[0].isnumeric():
             if obj2[0]=="-":
                obj2.remove(obj2[0])
                obj2[0]="-"+obj2[0]
             elif obj2[0]=="+":
                obj2.remove(obj2[0])
 if not quant[0].isnumeric():
            if quant[0]=="-":
                quant.remove(quant[0])
                quant[0]=str(-1*int(quant[0]))
            elif quant[0]=="+":
                quant.remove(quant[0])
 a=calc2(str2.join(obj2))
 if xtrigger==True:
  b=calc2(str2.join(obj))
 else:
  b=0
 g=calc2(str4.join(quant))
 d=b**2-4*a*g
 if d>0:
     x1=((-b+math.sqrt(d))/(2*a))
     x2=((-b-math.sqrt(d))/(2*a))
     x1f=round(x1,4)
     x2f=round(x2,4)
     answer="X1 =  " + str(x1f) + "   X2 = " +  str(x2f)
 elif d==0:
     x=(-b)/(2*a)
     xf=round(x,4)
     answer="Single root found: " + str(xf)
 elif d<0:
     answer="No roots found."
     
 return answer       
# 7. Method that does final calculations
def calc2(str1):
 tabl2=str1.split(" ")
 tabl=tabl2.copy()
 res=[]
 trig=False
 d=0
 for i in range(0,len(tabl2)):
         
         if tabl2[i]!="+" and tabl2[i]!="-" and tabl2[i]!="/" and tabl2[i]!="*" and tabl2[i]!="^" and tabl2[i]!="("and tabl2[i]!=")"  and tabl2[i]!="π" and tabl2[i]!="sq":
             tabl2[i]=float(tabl2[i])
       
 for i in range(0,len(tabl)):
         if tabl[i]!="+" and tabl[i]!="-" and tabl[i]!="/" and tabl[i]!="*" and tabl[i]!="^" and tabl[i]!="("and tabl[i]!=")" and tabl[i]!="π" and tabl[i]!="sq" :
             tabl[i]=float(tabl[i])
        
 
 
     
      
 while "*" in tabl or  "/" in tabl or "^" in tabl or "sq" in tabl:           
     for i in range(0,len(tabl)):
        if tabl[i]=="*" or tabl[i]=="/" or tabl[i]=="^" or tabl[i]=="sq":
            if tabl[i]=="*":
                tabl[i-1]=tabl[i-1]*tabl[i+1]
                tabl.pop(i)
                tabl.pop(i)
                break
            if tabl[i]=="^":
                tabl[i-1]=tabl[i-1]**tabl[i+1]
                tabl.pop(i)
                tabl.pop(i)
                break
            if tabl[i]=="/":
                tabl[i-1]=tabl[i-1]/tabl[i+1]
                tabl.pop(i)
                tabl.pop(i)
                break
            if tabl[i]=="sq":
                tabl[i-1]=math.sqrt(tabl[i-1])
                tabl.pop(i)
                break
 final = tabl[0]
 for i in range(0,len(tabl)):
     if tabl[i]=="+":
         final=final+tabl[i+1]
     if tabl[i]=="-":
         final=final-tabl[i+1]
 return final
# 8. Method that recognises where the calculations should begin depending on brackets
def parenth(str1):
 tabl2=str1.split(" ")
 tabl=tabl2.copy()
 res=[]
 trig=False
 d=0
 str2=" "

 for i in range(0,len(tabl2)):
         if tabl2[i]=="π":
             tabl2[i]= math.pi
         if tabl2[i]!="+" and tabl2[i]!="-" and tabl2[i]!="/" and tabl2[i]!="*" and tabl2[i]!="^" and tabl2[i]!="("and tabl2[i]!=")" and tabl2[i]!="sq":
             tabl2[i]=float(tabl2[i])
 
 for i in range(0,len(tabl)):
         if tabl[i]=="π":
             tabl[i]=math.pi
         if tabl[i]!="+" and tabl[i]!="-" and tabl[i]!="/" and tabl[i]!="*" and tabl[i]!="^" and tabl[i]!="("and tabl[i]!=")" and tabl[i]!="sq":
             tabl[i]=float(tabl[i])
        
       
 while "(" in tabl:
     for i in range(0,len(tabl)):
         if tabl[i]=="(" :
             p=i+1
             trig=True
         if tabl[i]==")":
             d=i
             trig=True
         if trig==True:
             tabl3=tabl[p:d]
     if trig==True:
    
         tabl[p-1:d]=[]
     for i in range(0,len(tabl3)):
         tabl3[i]=str(tabl3[i])

     tabl[p-1]=calc2(str2.join(tabl3))
  
      
 for i in range(0,len(tabl)):
    tabl[i]=str(tabl[i])
 
 return calc2(str2.join(tabl))
    
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





delete = Button(btns_frame, text = "Del",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0,borderwidth=0, bg = "white", cursor = "hand2", command = lambda: btn_del(event)).grid(row = 1, column = 4,  padx = 1, pady = 1)
clear = Button(btns_frame, text = "Clear",image=photoimage, fg = "white", width = 300,borderwidth=200,relief='flat',height = 25,compound="center", bd = 0, highlightbackground="white", bg = "white", cursor = "hand2", command = lambda: btn_clear(event)).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/",image=photoimage4,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" / ")).grid(row = 0, column = 3, padx = 1, pady = 1)


seven = Button(btns_frame, text = "7", image=photoimage3,compound="center",fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("7")).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", image=photoimage3,compound="center",fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("8")).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", image=photoimage3,compound="center",fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("9")).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*",image=photoimage4,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" * ")).grid(row = 1, column = 3, padx = 1, pady = 1)


four = Button(btns_frame, text = "4",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg='white', cursor = "hand2", command = lambda: btn_click("4")).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click("5")).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click("6")).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-",image=photoimage4,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click(" - ")).grid(row = 2, column = 3, padx = 1, pady = 1)


one = Button(btns_frame, text = "1", image=photoimage3,compound="center",fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("1")).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("2")).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("3")).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+",image=photoimage4,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" + ")).grid(row = 3, column = 3, padx = 1, pady = 1)
# The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
X2 = Button(btns_frame, text = "X2",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("d")).grid(row = 2,column = 4, padx = 1, pady = 1)
X = Button(btns_frame, text = "X",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = lambda: btn_click("x")).grid(row = 3, column = 4, columnspan = 1, padx = 1, pady = 1)
POW = Button(btns_frame, text = "x^n", image=photoimage3,compound="center",fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(" ^ ")).grid(row =0, column = 4, padx = 1, pady = 1)

zero = Button(btns_frame, text = "0",image=photoimage2,compound="center", fg = "white", width = 21, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click("0")).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=",image=photoimage,compound="center", fg = "white", width = 32, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_equal(event)).grid(row = 4, column = 3,columnspan=3, padx = 1, pady = 1)

par1 = Button(btns_frame, text = "(",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg='white', cursor = "hand2", command = lambda: btn_click("( ")).grid(row = 0, column = 5, padx = 1, pady = 1)
par2 = Button(btns_frame, text = ")",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click(" )")).grid(row = 1, column = 5, padx = 1, pady = 1)
pi = Button(btns_frame, text = "π",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click("π")).grid(row = 2, column = 5, padx = 1, pady = 1)
root = Button(btns_frame, text = "√x",image=photoimage3,compound="center", fg = "white", width = 10, height = 3, bd = 0, bg = 'white', cursor = "hand2", command = lambda: btn_click(" sq")).grid(row = 3, column = 5, padx = 1, pady = 1)

window.mainloop()
