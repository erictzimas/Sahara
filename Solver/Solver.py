import math

"""
Created on Mon Sep 21 22:38:24 2020

@author: Eric Tzimas
"""


class Solver:
    def __init__(self, equation):
        self.equation = equation

    def solve(self):
        print(self.equation)

    def floatEquation(self):
        frequencyTable = self.equation.split(" ")
        symbols = ["+", "-", "/", "*", "^", "(", ")", "π", "sq", "x"]

        for i in range(0, len(frequencyTable)):
            if frequencyTable[i] not in symbols:
                frequencyTable[i] = float(frequencyTable[i])
        return frequencyTable

    def finalCalculations(self):
        frequencyTable = Solver.floatEquation(self)
        res = []
        trig = False
        basic_symbols = ["+", "-", "(", ")"]
        expert_symbols = ["*", "/", "^", "sq", "π"]
        d = 0
        expert_symbols

        while (
            "*" in frequencyTable
            or "/" in frequencyTable
            or "^" in frequencyTable
            or "sq" in frequencyTable
            or "π" in frequencyTable
        ):
            for i in range(0, len(frequencyTable)):
                if frequencyTable[i] in expert_symbols:
                    if frequencyTable[i] == "π":
                        frequencyTable[i] = math.pi
                    if frequencyTable[i] == "*":
                        frequencyTable[i - 1] = (
                            frequencyTable[i - 1] * frequencyTable[i + 1]
                        )
                        frequencyTable.pop(i)
                        frequencyTable.pop(i)
                        break
                    if frequencyTable[i] == "^":
                        frequencyTable[i - 1] = (
                            frequencyTable[i - 1] ** frequencyTable[i + 1]
                        )
                        frequencyTable.pop(i)
                        frequencyTable.pop(i)
                        break
                    if frequencyTable[i] == "/":
                        frequencyTable[i - 1] = (
                            frequencyTable[i - 1] / frequencyTable[i + 1]
                        )
                        frequencyTable.pop(i)
                        frequencyTable.pop(i)
                        break
                    if frequencyTable[i] == "sq":
                        frequencyTable[i - 1] = math.sqrt(frequencyTable[i - 1])
                        frequencyTable.pop(i)
                        break
        final = frequencyTable[0]
        for i in range(0, len(frequencyTable)):
            if frequencyTable[i] == "+":
                final = final + frequencyTable[i + 1]
            if frequencyTable[i] == "-":
                final = final - frequencyTable[i + 1]
        return final

    def parenthesis(self):
        tabl = Solver.floatEquation(self)
        symbols = ["+", "-", "/", "*", "^", "(", ")", "π", "sq"]
        res = []
        trig = False
        d = 0
        str2 = " "

        while "(" in tabl:
            for i in range(0, len(tabl)):

                if tabl[i] == "(":
                    p = i + 1
                    trig = True
                if tabl[i] == ")":
                    d = i
                    trig = True
                if trig == True:
                    tabl3 = tabl[p:d]
            if trig == True:

                tabl[p - 1 : d] = []
            for i in range(0, len(tabl3)):
                tabl3[i] = str(tabl3[i])
            self.equation = str2.join(tabl3)
            tabl[p - 1] = Solver.finalCalculations(self)

        for i in range(0, len(tabl)):
            tabl[i] = str(tabl[i])
        self.equation = str2.join(tabl)
        self.equation = Solver.finalCalculations(self)
        return self.equation

    def firstDegreeCalculations(self):
        c = self.equation.split(" ")
        obj = []
        obj2 = []
        quant = []
        str2 = " "
        str3 = " "
        if "d" not in c:
            if "x" in c[0]:
                obj.append(c[0])
            elif c[0].isnumeric():
                quant.append(c[0])
            for i in range(1, len(c)):
                if "x" in c[i]:
                    obj.append(c[i - 1])
                    obj.append(c[i])
                elif c[i].isnumeric():
                    quant.append(c[i - 1])
                    quant.append(c[i])
            for i in range(0, len(obj)):
                if "x" in obj[i]:
                    s = obj[i].split()
                    if not obj[i][0].isnumeric():
                        obj[i] = obj[i].replace("x", "1")
                    else:
                        obj[i] = obj[i].replace("x", " * 1")
            if not obj[0].isnumeric():
                if obj[0] == "-":
                    obj.remove(obj[0])
                    obj[0] = str(-1 * int(obj[0]))
                elif obj[0] == "+":
                    obj.remove(obj[0])
            if not quant[0].isnumeric():
                if quant[0] == "-":
                    quant.remove(quant[0])
                    quant[0] = str(-1 * int(quant[0]))
                elif quant[0] == "+":
                    quant.remove(quant[0])
            self.equation = str2.join(obj)
            leftside = Solver.finalCalculations(self)
            self.equation = str3.join(quant)
            rightside = Solver.finalCalculations(self)
            ans = (-1 * rightside) / leftside

        return ans

    def secondDegreeCalculations(self):
        c = self.equation.split(" ")
        obj = []
        obj2 = []
        quant = []
        str2 = " "
        str3 = " "
        str4 = " "
        xtrigger = False
        if "x" in c[0]:
            obj.append(c[0])
        elif "d" in c[0]:
            obj2.append(c[0])

        elif c[0].isnumeric():
            quant.append(c[0])
        for i in range(1, len(c)):
            if "x" in c[i]:
                obj.append(c[i - 1])
                obj.append(c[i])
                xtrigger = True

            if "d" in c[i]:
                obj2.append(c[i - 1])
                obj2.append(c[i])
            elif c[i].isnumeric():

                quant.append(c[i - 1])
                quant.append(c[i])
        if xtrigger == True:
            for i in range(0, len(obj)):
                if "x" in obj[i]:
                    s = obj[i].split()
                    if not obj[i][0].isnumeric():

                        obj[i] = obj[i].replace("x", "1")
                    else:

                        obj[i] = obj[i].replace("x", " * 1")

            if not obj[0].isnumeric():
                if obj[0] == "-":
                    obj.remove(obj[0])
                    obj[0] = "-" + obj[0]
                elif obj[0] == "+":
                    obj.remove(obj[0])
        for i in range(0, len(obj2)):
            if "d" in obj2[i]:
                s = obj2[i].split()
                if not obj2[i][0].isnumeric():

                    obj2[i] = obj2[i].replace("d", "1")
                else:

                    obj2[i] = obj2[i].replace("d", " * 1")
        if not obj2[0].isnumeric():
            if obj2[0] == "-":
                obj2.remove(obj2[0])
                obj2[0] = "-" + obj2[0]
            elif obj2[0] == "+":
                obj2.remove(obj2[0])
        if not quant[0].isnumeric():
            if quant[0] == "-":
                quant.remove(quant[0])
                quant[0] = str(-1 * int(quant[0]))
            elif quant[0] == "+":
                quant.remove(quant[0])
        self.equation = str2.join(obj2)
        a = Solver.finalCalculations(self)
        if xtrigger == True:
            self.equation = str2.join(obj)
            b = Solver.finalCalculations(self)
        else:
            b = 0
            self.equation = str4.join(quant)
            g = Solver.finalCalculations(self)
            d = b ** 2 - 4 * a * g
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            x1f = round(x1, 4)
            x2f = round(x2, 4)
            answer = "X1 = " + str(x1f) + " X2 = " + str(x2f)
        elif d == 0:
            x = (-b) / (2 * a)
            xf = round(x, 4)
            answer = "Single root found: " + str(xf)
        elif d < 0:
            answer = "No roots found."

        return answer
