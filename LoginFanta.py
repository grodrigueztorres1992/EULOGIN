#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

#hora = time.strftime("%c")
controlador = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

controlador.get("https://www.fantasilandia.cl/")
#time.sleep(5)

BotonLogin = controlador.find_element(By.CLASS_NAME, "btn.btn-ingresar-header.dropdown-toggle")

BotonLogin.click()

usuario = controlador.find_element(By.NAME, "txtUser")
clave = controlador.find_element(By.NAME, "txtPassword")

#paso 1
usuario.send_keys("grodriguez@proredes.net")
#time.sleep(2)
#paso 2
clave.send_keys("Guille_2")
#time.sleep(2)
#paso 3
boton = controlador.find_element(By.CLASS_NAME, "btn.btn-iniciar-new")

boton.click()
#time.sleep(10)
controlador.quit()
print(time.strftime("%c")+" OK")
