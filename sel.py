import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("http://hackertyper.com/")
driver.fullscreen_window()
test = driver.find_element_by_xpath("//*[@id=\"console\"]")
elaptime = 0
start = time.time()
while True:
    end = time.time()
    driver.execute_script("Typer.write(Typer.addText)")
    elaptime = end - start
    print(elaptime)
    if elaptime > 30.0:
        driver.refresh()
        start = time.time()

# time.sleep(1)
