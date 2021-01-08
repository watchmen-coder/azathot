import os, time, sys, datetime
from random import randint
from huepy import *


def cc_gen(bin):

    cc = ""

    if len(bin) == 16:

        for x in range(16):

            if bin[x] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                cc += bin[x]
                continue

            elif bin[x] in ('x'):
                cc += str(randint(0,9))

            else:
                print(bad(f"Invalid Format Bin: {bin}"))
                sys.exit()

    else:
        print(bad(f"Invalid Format BIN: {bin}"))

    return(cc)

def ccvgen(cvv):
        
    if cvv == 'rnd':

        ccv = ""
        num = randint(10,999)

        if num < 100:

            ccv = "0" + str(num)
        
        else:
            ccv = str(num)

        return(ccv)

    else:
        return(cvv)

def dategen(month, year):

    if month == 'rnd' and year == 'rnd':
        now = datetime.datetime.now()
        month = str(randint(1, 12))
        current_year = str(now.year)
        year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
        date = month + "|" + year
        return date

    elif month == 'rnd' and year != 'rnd':
        now = datetime.datetime.now()
        month = str(randint(1,12))
        date = month + "|" + year
        return date

    elif month != 'rnd' and year == 'rnd':
        now = datetime.datetime.now()
        current_year = str(now.year)
        year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
        date = month + "|" + year
        return date

    elif month != 'rnd' and year != 'rnd':
        date = month + "|" + year
        return date



def clean():

    if os.name == 'nt':

        os.system('cls')

    else:

        os.system('clear')

def banner():
    print(purple("""
                  .---.         ,,
       ,,        /     \       ;,,'
      ;, ;      (  o  o )      ; ;
        ;,';,,,  \  \/ /      ,; ;
    ,,,  ;,,,,;;,`   '-,;'''',,,'
    ;,, ;,, ,,,,   ,;  ,,,'';;,,;''';
        ;,,,;    ~~'  '';,,''',,;''''  
                                    
             CC GENERATE \n"""))

def main():
    
    clean()
    banner()


    try:

        seses = int(input(info("Quantity > ")))
        counter = 0

        BIN = input(info("BIN > "))
        MONTH = input(info("Month [MM / RND] > ")).lower()
        YEAR = input(info("Year [YY / RND] > ")).lower()
        CVV = input(info("CVV [CVV / RND] > ")).lower()

        month = MONTH
        year = YEAR

        clean()
        banner()
        
        while counter != seses:
            print(good(cc_gen(BIN) + "|" + dategen(month, year) + "|" + ccvgen(CVV)))
            counter +=1

    except:
        print(bad(yellow("An Error Ocurred...")))
        sys.exit()

if __name__ == "__main__":
    print(info(lightred(("An Error Ocurred..."))))

else:
    main()