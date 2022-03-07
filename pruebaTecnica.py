from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def main():
    item = input("Introduzca producto a buscar: ")
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://flow.bo/")
    cantidadProductos =int(0)
    while cantidadProductos < 3:
        buscar = driver.find_element(by=By.NAME, value="q")
        buscar.send_keys(item,Keys.ENTER)
        time.sleep(6)
        productos = driver.find_elements(by=By.CLASS_NAME, value="product-item-link")
        cantidadProductos = int(len(productos))
        print("Cantidad de productos: ",cantidadProductos)
        ordenarPorPrecio = driver.find_element(by=By.XPATH,value="/html/body/div[1]/main/div[3]/div[1]/div[4]/div[1]/div[3]/select[1]/option[2]").click()
        time.sleep(7)
        print("Ordenado por precio descententemente")

if __name__ == "__main__":
    main()
