import argparse, sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--tool", '-t', type= str, metavar= "[ bin-info | checker ]", 
                                help="Carding tools", default="Choise option")

    args = parser.parse_args()

    tool = str(args.tool).lower()

    if tool != None:
        print(""" Try:
        python azathot.py --help or use python azathot.py --tool""")

    if tool == 'bin-info':
        import tools.bin_info

    elif tool == 'checker':
        print("This tool was deleted")