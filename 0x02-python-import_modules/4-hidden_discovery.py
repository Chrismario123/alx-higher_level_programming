#!/usr/bin/python3
import hidden_4

def print_module_names():
    module_names = dir(hidden_4)
    fn = [n for n in module_names if not n.startswith('__')]
    fn.sort()
    for name in fn:
        print(name)

if _name_ == '_main_':
    print_module_names()
