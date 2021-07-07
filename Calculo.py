class Calculo:
    def calcvi(str1):

        c = str1.split(" ")
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
            leftside = calc2(str2.join(obj))
            rightside = calc2(str3.join(quant))
            ans = (-1 * rightside) / leftside

            answer = "X = ", ans

        return answer

    # 6. Method that calculates second degree equations
    def calcvi2(str1):
        c = str1.split(" ")
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
        a = calc2(str2.join(obj2))
        if xtrigger == True:
            b = calc2(str2.join(obj))
        else:
            b = 0
            g = calc2(str4.join(quant))
            d = b ** 2 - 4 * a * g
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            x1f = round(x1, 4)
            x2f = round(x2, 4)
            answer = "X1 =  " + str(x1f) + "   X2 = " + str(x2f)
        elif d == 0:
            x = (-b) / (2 * a)
            xf = round(x, 4)
            answer = "Single root found: " + str(xf)
        elif d < 0:
            answer = "No roots found."

        return answer

    # 7. Method that does final calculations
    def calc2(str1):
        tabl2 = str1.split(" ")
        tabl = tabl2.copy()
        res = []
        trig = False
        d = 0
        for i in range(0, len(tabl2)):

            if (
                tabl2[i] != "+"
                and tabl2[i] != "-"
                and tabl2[i] != "/"
                and tabl2[i] != "*"
                and tabl2[i] != "^"
                and tabl2[i] != "("
                and tabl2[i] != ")"
                and tabl2[i] != "π"
                and tabl2[i] != "sq"
            ):
                tabl2[i] = float(tabl2[i])

        for i in range(0, len(tabl)):
            if (
                tabl[i] != "+"
                and tabl[i] != "-"
                and tabl[i] != "/"
                and tabl[i] != "*"
                and tabl[i] != "^"
                and tabl[i] != "("
                and tabl[i] != ")"
                and tabl[i] != "π"
                and tabl[i] != "sq"
            ):
                tabl[i] = float(tabl[i])

        while "*" in tabl or "/" in tabl or "^" in tabl or "sq" in tabl:
            for i in range(0, len(tabl)):
                if (
                    tabl[i] == "*"
                    or tabl[i] == "/"
                    or tabl[i] == "^"
                    or tabl[i] == "sq"
                ):
                    if tabl[i] == "*":
                        tabl[i - 1] = tabl[i - 1] * tabl[i + 1]
                        tabl.pop(i)
                        tabl.pop(i)
                        break
                    if tabl[i] == "^":
                        tabl[i - 1] = tabl[i - 1] ** tabl[i + 1]
                        tabl.pop(i)
                        tabl.pop(i)
                        break
                    if tabl[i] == "/":
                        tabl[i - 1] = tabl[i - 1] / tabl[i + 1]
                        tabl.pop(i)
                        tabl.pop(i)
                        break
                    if tabl[i] == "sq":
                        tabl[i - 1] = math.sqrt(tabl[i - 1])
                        tabl.pop(i)
                        break
        final = tabl[0]
        for i in range(0, len(tabl)):
            if tabl[i] == "+":
                final = final + tabl[i + 1]
            if tabl[i] == "-":
                final = final - tabl[i + 1]
        return final
        # 8. Method that recognises where the calculations should begin depending on brackets

    def parenth(str1):
        tabl2 = str1.split(" ")
        tabl = tabl2.copy()
        res = []
        trig = False
        d = 0
        str2 = " "

        for i in range(0, len(tabl2)):
            if tabl2[i] == "π":
                tabl2[i] = math.pi
            if (
                tabl2[i] != "+"
                and tabl2[i] != "-"
                and tabl2[i] != "/"
                and tabl2[i] != "*"
                and tabl2[i] != "^"
                and tabl2[i] != "("
                and tabl2[i] != ")"
                and tabl2[i] != "sq"
            ):
                tabl2[i] = float(tabl2[i])

        for i in range(0, len(tabl)):
            if tabl[i] == "π":
                tabl[i] = math.pi
            if (
                tabl[i] != "+"
                and tabl[i] != "-"
                and tabl[i] != "/"
                and tabl[i] != "*"
                and tabl[i] != "^"
                and tabl[i] != "("
                and tabl[i] != ")"
                and tabl[i] != "sq"
            ):
                tabl[i] = float(tabl[i])

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

            tabl[p - 1] = Calculo.calc2(str2.join(tabl3))

        for i in range(0, len(tabl)):
            tabl[i] = str(tabl[i])

        return Calculo.calc2(str2.join(tabl))
