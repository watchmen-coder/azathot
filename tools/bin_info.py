import os, requests
from time import sleep

NONE, RED, GREEN, BLUE, PURPLE, YELLOW, WHITE = "\033[0m", "\033[0;31m", "\033[1;32m", "\033[0;34m", "\033[1;35m", "\033[1;33m", "\033[1;37m"

API = "https://lookup.binlist.net/"


def bin_info():

    def logo():
        print(PURPLE + """
                              .---.         ,,
                   ,,        /     \       ;,,'
                  ;, ;      (  o  o )      ; ;
                    ;,';,,,  \  \/ /      ,; ;
                ,,,  ;,,,,;;,`   '-,;'''',,,'
                ;,, ;,, ,,,,   ,;  ,,,'';;,,;''';
                    ;,,,;    ~~'  '';,,''',,;''''  
                                        ''' 
                        @ByDog3r - Ccheck.py   \n """ + NONE) 

    def clean():
        os.system('cls') if os.name == 'nt' else os.system('clear')

    def main():
        clean(); logo()
        try:
            BIN = input(RED + "Put a bin > " + YELLOW)

            MAPING = { ord('"'):"", ord(","):"\n", ord("}"):"", ord("{"):"" }

            post = requests.post(API+BIN)

            print(GREEN + post.text.translate(MAPING) + NONE)
        except:
            logo()
            print(f"{RED}Follow directions... " + NONE)
            exit()

    main()

if __name__ == "__main__":
    print(f"{RED}Follow directions... " + NONE)
    exit()
else:
    bin_info()