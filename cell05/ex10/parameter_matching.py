import sys
if len(sys.argv) != 2:
    print("none")
else:
    t = input("What was the parameter? ")
    if t == sys.argv[1]:
        print("Good job")
    else:
        print("Nope, sorry...")