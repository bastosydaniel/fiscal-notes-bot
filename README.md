## fiscal-notes-bot / Robô para emissão de notas fiscais 🤖

HI, this repository contains a NFE-RJ Python bot (Fiscal Notes Generator) .

### to install Selenium
```console
$ pip install selenium
```

### to init:
1. First you have to download your browser driver version;<br>
[Click here](https://github.com/mozilla/geckodriver/releases) to install for Chrome<br>
[Click here](https://chromedriver.chromium.org/downloads) to install for Firefox<br>

2. After downloading you have to put the driver into your bot package
3. With your driver browser into your package you have to add him to your bot code;<br>
Like this:<br>
`navegador = webdriver.Chrome(executable_path=r'./chromedriver')`<br>
4. Add your infos into the bot code;<br>
Example:<br>`driver.find_element("xpath",'//*[@id="ctl00_cphCabMenu_tbSenha"]').send_keys("12345678")`
5. Now you can run and be happy!😀

### Versions
`Python 3.10.5`<br>
`pip 21.2.3`<br>



### By [@bastosydaniel](https://bastosydaniel.github.io/My-devfolio/)
