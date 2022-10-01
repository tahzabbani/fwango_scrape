from time import sleep
from selenium import webdriver
# from selenium import webelements
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import secret_tokens
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.fwango.io/signin")

# def login():

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
driver.find_element(By.NAME, "email").send_keys(secret_tokens.email)
driver.find_element(By.NAME, "password").send_keys(secret_tokens.password)
driver.find_element(By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div[2]/div/div/div[2]/div[1]/form/div[2]/button").click()
sleep(1)

driver.get("https://fwango.io/dashboard?sport=roundnet&period=past")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "TournamentCard__Container-sc-15zkmn8-0")))
card_list = driver.find_elements(By.CLASS_NAME, "TournamentCard__Container-sc-15zkmn8-0")
for i in card_list:
    i.click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/nav/ul[2]/li[2]/div/a")))
    driver.find_element(By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/nav/ul[2]/li[2]/div/a").click()


# html = driver.page_source
# print(html)