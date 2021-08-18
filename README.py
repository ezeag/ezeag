from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

website = "https://docs.google.com/forms/d/e/1FAIpQLSfwKJbJYUScWbhMHeQuf0xWsvuutpZNZyGwsvbWptOxuj0Uyg/viewform"
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(website)


# Importantisimo el time sleep 1 seg para dar tiempo a que cargue la pagina.
time.sleep(1)
fullName = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
fullName.send_keys("Aaron Ezequiel Gomez")
dni = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
dni.send_keys("41812916")

fecha = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
fecha.send_keys("29031999")

telefono = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
telefono.send_keys("3624702539")

instagram = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
instagram.send_keys("gomez.a.ezequiel")

correo = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
correo.send_keys("gomez.a.ezequiel@gmail.com")

domicilio = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
domicilio.send_keys("Seitor 644 3 E")

zip = driver.find_element_by_xpath(
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
zip.send_keys("3500")

#Lo de abajo falta terminar, pueden buscar como DropDown Selenium en youTube
#provincia = driver.find_element_by_xpath(
#    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[1]/div[3]/span').click()
#driver.find_element_by_css_selector()
