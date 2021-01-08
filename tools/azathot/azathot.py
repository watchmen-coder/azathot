import argparse, sys, os, time
from huepy import *

__version__ = "1.3.5"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", '-t', type= str, metavar= "[ BIN-INFO | temp-mail | CC-GEN ] ", 
                                help="Carding tools", default="Choise option")

    args = parser.parse_args()
    tool = str(args.tool).lower()

    if tool == 'bin-info':
        import tools.azathot.bin_info

    elif tool == 'temp-mail':
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(info(red("[ Q ] Exit.")))
        time.sleep(0.7)
        print(good("Generating Temp-Email."))
        time.sleep(5)
        os.system("w3m https://temp-mail.org/es/")
        print(good("Finish."))

    elif tool == 'cc-gen':
        import tools.azathot.cc_gen
    

    elif tool == 'checker':
        print(bad(yellow("This tool was deleted")))

    else:
        print(red("\n Carding ToolKit > Azathot \n"))
        os.system('python azathot.py -h')