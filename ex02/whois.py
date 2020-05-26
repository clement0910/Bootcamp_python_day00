import sys

if len(sys.argv) == 2:
    if sys.argv[1].isdigit() is False:
        print("ERROR")
        exit()
    if int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif (int(sys.argv[1]) % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
elif len(sys.argv) > 2:
    print("ERROR")
