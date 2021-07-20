# Sahara
Scientific calculator and equation solver made with Python and Tkinter.
# Sahara v1.0
[![Build Status](https://travis-ci.com/erictzimas/Sahara.svg?branch=main)](https://travis-ci.com/erictzimas/Sahara)
[(https://github.com/erictzimas/Sahara/blob/main/coverage/coverage.svg)]

Sahara is a scientific calculator that can also solve first and second degree equations, Tkinter GUI is configured for macOS.

Created on Mon Sep 21 22:38:24 2020

@author: Eric Tzimas

# Installation

Download sahara.py, enter $ python sahara.py on terminal or cmd to run

# Usage

You can type sentences of calculations via keyboard or GUI, or you can click on the text field and type your calculations there but in order for this to work you must include spaces.

Keyboard Shortcuts:
 Apart from the obvious ones,
   pi is 'p'
   square root is 'r' and it should be used right after the targeted number.
   x2 is 'd'

Equation mode: 
  This calculator can solve equations of 1st and 2nd degree. The input should be in this format(f(x)), taken from f(x)=0. The output is going to be the roots of the equation if they do exist. If the equation only includes 'x' (first degree) it will know to solve it as first degree equation. If it includes 'd' which is x2 (second degree) it will solve it as a second degree equation.

For example  '5x - 5' is going to output 1. 'd-2' is going to output 2, -2.

Equation mode restrictions
You cannot use brackets or decimals and must input the equation in this form 'ax2 + bx + c'
You are not required to do the final calculations as long as the equation is given in above mentioned format.
For example 5x-2x+3/5 will work.

