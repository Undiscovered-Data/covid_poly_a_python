#!/usr/bin/python3

import sys

def start_it():
    print("\n  ***            Percent Complete                ***")
    print("  |                                                |")
    print("  0% ################## 50% ################### 100%")
    print("  |                                                |")
    sys.stdout.write("  ")
    sys.stdout.flush()

def add_star():
    sys.stdout.write("*")
    sys.stdout.flush()

def end_it():
    sys.stdout.write("\n\n")
