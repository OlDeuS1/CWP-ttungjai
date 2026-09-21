import sys
if len(sys.argv) == 2 and sys.argv[1].count("z"):
    print("z" * sys.argv[1].count("z"))
else:
    print("none")
