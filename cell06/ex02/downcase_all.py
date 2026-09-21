import sys

def downcase_it(t):
    return t.lower()

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        for i in range(1, len(sys.argv)):
            print(downcase_it(sys.argv[i]) )

main()