
from webbrowser import Chrome
from selenium import webdriver
import time


navegador = webdriver.Chrome(executable_path=r'./chromedriver')
navegador.get("https://notacarioca.rio.gov.br/senhaweb/login.aspx?ReturnUrl=%2Fcontribuinte%2Fnota.aspx")
time.sleep(1)
navegador.find_element("xpath",'//*[@id="ctl00_cphCabMenu_tbCpfCnpj"]').send_keys("")
navegador.find_element("xpath",'//*[@id="ctl00_cphCabMenu_tbSenha"]').send_keys("")
# THIS TIME YOU USE TO WRITE THE CAPTCHA / USE ESSE TEMPO PARA PREENCHER O CAPTCHA
time.sleep(15)
navegador.find_element("xpath",'//*[@id="ctl00_cphCabMenu_btEntrar"]').click()
time.sleep(1)

# navegador.find_element("xpath",'/html/body/form/div[3]/div[1]/div[6]/div/div/div/div/p/a[1]').click()

cnpjtomador = 00
tomador = navegador.find_element("xpath",'//*[@id="ctl00_cphCabMenu_tbCPFCNPJTomador"]')
tomador.get_attribute("type") == "number"
tomador.send_keys(cnpjtomador)

navegador.find_element("xpath",'//*[@id="ctl00_cphCabMenu_btAvancar"]').click()

navegador.find_element("xpath", '//*[@id="ctl00_cphCabMenu_tbDiscriminacao"]').send_keys("")
navegador.find_element("xpath", '//*[@id="ctl00_cphCabMenu_tbValor"]').send_keys("")

