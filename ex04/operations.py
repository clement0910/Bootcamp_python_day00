import sys


def printmessage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n    python operations.py 10 3")
    exit()


if len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    printmessage()
if len(sys.argv) == 1:
    printmessage()
if sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
    print("InputError: only numbers\n")
    printmessage()
print("Sum:        ", int(sys.argv[1]) + int(sys.argv[2]))
print("Difference: ", int(sys.argv[1]) - int(sys.argv[2]))
print("Product:    ", int(sys.argv[1]) * int(sys.argv[2]))
if sys.argv[2] != "0":
    print("Quotient:   ", int(sys.argv[1]) / int(sys.argv[2]))
    print("Remainder:  ", int(sys.argv[1]) % int(sys.argv[2]))
else:
    print("Quotient:    ERROR (div by zero)")
    print("Remainder:   ERROR (modulo by zero)")
