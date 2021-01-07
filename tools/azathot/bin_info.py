import os, requests
from time import sleep
from huepy import *

API = "https://lookup.binlist.net/"

def Bin_Info():


    def banner():
        print(purple("""
                              .---.         ,,
                   ,,        /     \       ;,,'
                  ;, ;      (  o  o )      ; ;
                    ;,';,,,  \  \/ /      ,; ;
                ,,,  ;,,,,;;,`   '-,;'''',,,'
                ;,, ;,, ,,,,   ,;  ,,,'';;,,;''';
                    ;,,,;    ~~'  '';,,''',,;''''  
                                        ''' 
                    GET INFORMATION ABOUT BIN \n"""))

    
    def clean():

        if os.name == 'nt':

            os.system('cls')

        else:

            os.system('clear')

    def main():

        clean() 
        banner()
        
        try:
            
            BIN = input(red("BIN > "))
            clean(); banner()

            MAPPING = { ord('"'):"", ord(","):"\n", ord("}"):"", ord("{"):"" }
            POST = requests.post(API+BIN)

            if """<!DOCTYPE html>""" in POST.text:
                print(bad(yellow("Follow Directions...")))

            else:
                print(green(POST.text.translate(MAPPING)))

        except:

            clean()
            banner()
            print(bad(yellow("An Error Ocurred...")))
            exit()

    main()

if __name__ == "__main__":

    print(info(lightred(("An Error Ocurred..."))))

else:

    Bin_Info()