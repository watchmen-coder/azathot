import os, requests, json, sys
from time import sleep
from huepy import *

__version__ = "1.3.5"

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
            
            BIN = input(red("   BIN > "))
            clean(); banner()

            data = requests.get(API+BIN).json()
            sys.stdout.flush()

            print(info(yellow("BIN INFORMATION " +red(BIN + "\n"))))
            sleep(0.7)
            print(good(red("[Country]: " +yellow(data['country']['name']))))
            sleep(0.7)
            print(good(red("[Sheme]: " +yellow(data['scheme']))))
            sleep(0.7)
            print(good(red("[Type]: " +yellow(data['type']))))
            sleep(0.7)
            print(good(red("[Brand]: " +yellow(data['brand']))))
            sleep(0.7)
            print(good(red("[Bank Name]: " +yellow(data['bank']['name']))))
            sleep(0.7)
            print(good(red("[Latitude]: " +yellow(data['country']['latitude']))))
            sleep(0.7)
            print(good(red("[Longitude]: " +yellow(data['country']['longitude']))))
            sleep(0.7)
            print(good(red("[Bank URL]: " +yellow(data['bank']['url']))))
            sleep(0.7)
            print(good(red("[Bank Phone]: " +yellow(data['bank']['phone']))))
            sleep(0.7)
            print(good(red("[Bank City]: " +yellow(data['bank']['city'] + "\n"))))

        except:

            print(bad(yellow("An Error Ocurred...")))
            exit()

    main()


if __name__ == "__main__":

    print(info(lightred(("An Error Ocurred..."))))

else:

    Bin_Info()