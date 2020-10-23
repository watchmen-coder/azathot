def banner():
    print(color['purple'] + """
                            .---.         ,,
                 ,,        /     \       ;,,'
                ;, ;      (  o  o )      ; ;
                  ;,';,,,  \  \/ /      ,; ;
               ,,,  ;,,,,;;,`   '-,;'''',,,'
              ;,, ;,, ,,,,   ,;  ,,,'';;,,;''';
                 ;,,,;    ~~'  '';,,''',,;''''  
                                    ''' 
                    @ByDog3r - Ccheck.py   \n """ + end) 

from bylib.decorepy import *

def bin_info():

   clear(); banner()

   TextDecoration().c4c("Esta es una herramienta de hacking...", color['red']);

   time.sleep(3.0); clear(); banner()

   bin = input(color['red'] + "Ingrese un bin > " + color['yellow']); clear(); banner()

   mapeo = { ord('"'):"", ord(","):"\n", ord("}"):"", ord("{"):"" }

   post = requests.post("https://lookup.binlist.net/"+bin)

   print(color['green'] + post.text.translate(mapeo) + color['none'])

   exit()

if __name__ == "__main__":
   print("impossible to access")

else:
   bin_info()