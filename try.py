import time
import os
import platform


def slowlyPrinting(strings):
    finalStr = ""
    for i in strings:
        finalStr += i
        print(finalStr)
        time.sleep(0.1)
        if i is not strings[-1]:
            if platform.system() == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
        else:
            time.sleep(1)
            if platform.system() == 'Windows':
                os.system("cls")
            else:
                os.system("clear")


def introduction():
    intro = ["You are going to see this effect. \n Just give the number of strings you want to print. \nThen simply enter the strings"]
    intro.append("Works on both Windows and Linux")
    for elements in intro:
        slowlyPrinting(elements)


if __name__ == "__main__":
    introduction()
    globalString = []
    numberOfInputs = int(input("Number of string: "))
    for inputs in range(numberOfInputs):
        string = input(f'{inputs}. Input String: ')
        globalString.append(string)

    for elements in globalString:
        slowlyPrinting(elements)
    print("Exiting program")
