#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    res = 0
if len(sys.argv) == 1:
    print("{}".format(int(0)))
else:
    for i in range(1, len(sys.argv)):
        res = res + int(sys.argv[i])
        print(f"{res}")
