import sys

def shrink(t):
    print(t[:8])

def enlarge(t):
    if len(t) < 8:
        for i in range(len(t), 8):
            t += "Z"
    print(t)

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        for i in range(1, len(sys.argv)):
            if len(sys.argv[i]) < 8:
                enlarge(sys.argv[i])
            elif len(sys.argv[i]) > 8:
                shrink(sys.argv[i])
            else:
                print(sys.argv[i])

main()