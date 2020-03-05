import re
import sys
from Equation import Equation


def printAndCheckDegree(final):
    print('Polynomial degree:', final[len(final) - 1][1])
    if final[len(final) - 1][1] > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        sys.exit()


def printReducedForm(final):
    print("Reduced form:", end=' ')

    flag = True
    for i in range(len(final)):
        if final[i][0] != 0:
            flag = False
            if i == 0:
                print(final[i][0], "* X^", end='')
            else:
                if final[i][0] < 0:
                    print('-', -final[i][0], "* X^", end='')
                else:
                    print('+', final[i][0], "* X^", end='')
            print(final[i][1], end=' ')
    if flag:
        print("0 ", end='')
    print("= 0")


def createFinal(result):
    final = []
    flag = False
    for i in range(0, len(result)):
        if result[i][0] == '=':
            flag = True
        if result[i][0] == '-':
            final.append([-float(result[i][2]), int(result[i][3])])
        else:
            final.append([float(result[i][2]), int(result[i][3])])
        if flag:
            final[i][0] = -final[i][0]
    return final


def addAndSortFinal(final):
    for k in range(len(final) - 1):
        j = k + 1
        while j < len(final):
            if final[k][1] == final[j][1]:
                final[k][0] = final[k][0] + final[j][0]
                del final[j]
                j = k
            j += 1
    for i in range(0, len(final) - 1):
        for j in range(i + 1, len(final)):
            if final[i][1] > final[j][1]:
                final[i], final[j] = final[j], final[i]
    return final


def getInput():
    if len(sys.argv) == 1:
        try:
            string = input()
        except EOFError:
            sys.exit("EOF")
        except KeyboardInterrupt:
            sys.exit("")
    elif len(sys.argv) != 2:
        print("usage: python3 computorV1.py [square equation]")
        sys.exit()
    else:
        string = sys.argv[1]
    return string


if __name__ == "__main__":
    string = getInput()
    regex = r'\s*((([+-]?[\d]+\.?[\d]*)\s*\*\s*X\^([\d]+)))\s*(([+-])(\s*(([+-]?[\d]+\.?[\d]*)\s*\*\s*X\^([\d]+))\s*))*\s*\=\s*((([+-]?[\d]+\.?[\d]*)\s*\*\s*X\^([\d]+))\s*)(([+-])(\s*(([+-]?[\d]+\.?[\d]*)\s*\*\s*X\^([\d]+))\s*))*'
    check = re.fullmatch(regex, string)
    if check is not None:
        result = re.findall(r'\s*([+=-])?\s*(([+-]?[\d]+\.?[\d]*)\s*\*\s*X\^([\d]+))', string)
    else:
        sys.exit("ERROR INPUT")
    final = createFinal(result)
    final = addAndSortFinal(final)
    args = [0, 0, 0]
    for i in range(0, len(final)):
        if final[i][1] < 3:
            args[final[i][1]] = final[i][0]
    printReducedForm(final)
    printAndCheckDegree(final)
    solution = Equation()
    solution.solve(args[0], args[1], args[2])
    solution.printSolutions()
