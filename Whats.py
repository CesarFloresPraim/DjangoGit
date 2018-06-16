from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
"""
service = service.Service('/usr/bin/safaridriver')
service.start()
capabilities = DesiredCapabilities.SAFARI
"""

service = service.Service('/usr/local/bin/chromedriver')
service.start()
capabilities = {'chrome.binary': '/usr/local/bin/chromedriver'}
#capabilities = {'safari.options': '/Applications/Safari.app/Contents/MacOS/safaridriver'}
#capabilities = {'safari.options': '/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'}

driver = webdriver.Remote(service.service_url, capabilities)
driver.get('https://web.whatsapp.com')

name = input('Nombre de usuario o grupo')
msg = input('Mensaje')
count = int(input('Numero de veces'))

input('Presiona cualquier tecla despues de haber escanedo el codigo QR')
#okbtn = driver.find_element_by_class_name('_1WZqU')
#okbtn.click()

user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
user.click()

msg_box= driver.find_element_by_class_name('_2bXVy')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_2lkdt')
    button.click()

input('salir')
"""
service = service.Service('/usr/local/bin/safaridriver')
service.start()
capabilities = {'chrome.binary': '/usr/local/bin/safaridriver'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
"""