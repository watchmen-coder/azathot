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
from io import open
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def checker():

    PATH="C:\Program Files (x86)\chromedriver.exe"; clear(); banner()

    class Forms_selenium():

        def __init__(self):
            self.driv3r=""
            self.answer=""

        def sel_id(self, id, answer):
            self.driv3r = driver.find_element_by_id(id)
            self.answer = self.driver.send_keys(answer)
            self.answer.send_keys(Keys.RETURN)

        def sel_name(self, name, answer):
            self.name = driver.find_element_by_name(name)
            self.name.send_keys(answer)
            self.name.send_keys(Keys.ENTER)

        def sel_xpath(self, xpath, answer):
            self.driv3r = driver.find_element_by_xpath(xpath)
            self.answer = self.driver.send_keys(answer)
            self.answer.send_keys(Keys.RETURN)

        def button(self, xpath):
            self.driv3r = driver.find_element_by_xpath(xpath).click()

        def multio(self, op1, op2):
            self.option = Select(driver.find_element_by_name(op1))
            self.option.select_by_visible_text(op2)

    PROXY = "<IP:PORT>"
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }

    mi_script = TextDecoration(); mi_script.c4c("This tool is a hacking script...", color['red']); clear(), banner()

    driver = webdriver.Chrome(executable_path=PATH)

    driver.get("https://www.aldoshoes.com/us/en_US/women/cremma-black/p/13176163")


    Mi_formulario = Forms_selenium() 

    Mi_formulario.button("//*[@id='c-product-detail__parallax']/div/div[1]/div/div[3]/div[2]/button[1]"); time.sleep(8)

    Mi_formulario.button("//*[@id='root']/div/div[1]/div[2]/div/div/main/div/div[2]/div[1]/button/span"); time.sleep(5)

    Mi_formulario.sel_name("email", "azathotchecker@bydog3r.com")

    Mi_formulario.sel_name("firstName", "ByDoger")

    Mi_formulario.sel_name("lastName", "Hacking")

    Mi_formulario.sel_name("addressLine1", "New York Street")

    Mi_formulario.sel_name("city", "New York")

    Mi_formulario.multio("state", 'NY')

    Mi_formulario.sel_name("zipCode", "10080")

    Mi_formulario.sel_name("phoneNumber", "7842563764"); time.sleep(1)

    Mi_formulario.button("//*[@id='root']/div/div[2]/div[2]/div[1]/main/div[2]/fieldset/div/div/button/span"); time.sleep(6)

    Mi_formulario.button("//*[@id='overlay-modal']/div/div/div/div[3]/button"); input("Press enter to close..."); exit()

if __name__ == "__main__":
    print("impossible to access")

else:
    checker()