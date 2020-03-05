import sys


class Equation:
    def __init__(self):
        self.__solution1 = 0
        self.__solution2 = 0
        self.__discriminant = -1

    def __root(self, n):
        lo = 0
        hi = n
        mid = 0
        for i in range(1000):
            mid = (lo + hi) / 2
            if mid * mid == n:
                return mid
            if mid * mid > n:
                hi = mid
            else:
                lo = mid
        return mid

    def solve(self, c, b, a):
        if a == 0 and b != 0:
            self.__solution1 = -c / b
            self.__solution2 = -c / b
            return
        if a == 0 and b == 0 and c != 0:
            print("Equation has not the solutions")
            sys.exit()
        if a == 0 and b == 0 and c == 0:
            print('The solutions are all real numbers.')
            sys.exit()
        self.__discriminant = b ** 2 - 4 * a * c
        if self.__discriminant < 0:
            print("Discriminant less than 0")
            sys.exit()
        self.__solution1 = (-b + self.__root(self.__discriminant)) / (2 * a)
        self.__solution2 = (-b - self.__root(self.__discriminant)) / (2 * a)

    def printSolutions(self):
        if self.__solution1 == self.__solution2:
            if self.__discriminant == -1:
                print("The solution is :")
            else:
                print("Discriminant is equal zero, the solution are :")
            print(self.__solution1)
        else:
            print("Discriminant is strictly positive, the two solutions are :")
            print(self.__solution1, "\n", self.__solution2)
