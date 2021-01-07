import argparse, sys, os
from huepy import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", '-t', type= str, metavar= "[ bin-info | checker ]", 
                                help="Carding tools", default="Choise option")

    args = parser.parse_args()
    tool = str(args.tool).lower()

    if tool == 'bin-info':
        import tools.azathot.bin_info

    elif tool == 'checker':
        print(bad(yellow("This tool was deleted")))

    else:
        print(red("\n AZATHOT CHECKER > @ByDog3r \n"))
        os.system('python azathot.py -h')