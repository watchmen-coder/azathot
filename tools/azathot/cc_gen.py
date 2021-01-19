import os, time, sys, datetime
from random import randint
from huepy import *

__version__ = "1.3.6"

def cc_gen(bin):

    cc = ""

    if len(bin) != 16:

        while len(bin) != 16:
            bin += 'x'

    else:
        pass

    if len(bin) == 16:

        for x in range(15):

            if bin[x] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                cc += bin[x]
                continue

            elif bin[x] in ('x'):
                cc += str(randint(0,9))

            else:
                print(bad(f"Invalid Format Bin: {bin}"))
                sys.exit()


        for i in range(10):
            check_cc = cc
            check_cc += str(i)

            if ValidCC(check_cc):
                cc = check_cc
                break
            else:
                check_cc = cc

    else:
        print(bad(f"Invalid Format BIN: {bin}"))

    return(cc)

def ValidCC(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )


def dategen(month, year):

    if month == 'rnd' and year == 'rnd':
        now = datetime.datetime.now()
        month = int(randint(1, 12))
        current_year = str(now.year)
        year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))

        if month < 10:
            month = '0'+str(month)
        
        else:
            month = str(month)

        date = month + "|" + year
        return date

    elif month == 'rnd' and year != 'rnd':
        now = datetime.datetime.now()
        month = int(randint(1,12))

        if month < 10:
            month = '0'+str(month)
        
        else:
            month = str(month)

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