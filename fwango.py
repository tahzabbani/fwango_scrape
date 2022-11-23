from time import sleep
from typing import Type
from selenium import webdriver
# from selenium import webelements
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import secret_tokens
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.fwango.io/signin")

# def check_if_elem_exists(css_selector):
#     try:
#         webdriver.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True

# def login():

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
driver.find_element(By.NAME, "email").send_keys(secret_tokens.email)
driver.find_element(By.NAME, "password").send_keys(secret_tokens.password)
# click on login button
driver.find_element(By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div[2]/div/div/div[2]/div[1]/form/div[2]/button").click()
sleep(1)

driver.get("https://fwango.io/dashboard?sport=roundnet&period=past")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[class*='TournamentCard__Container']")))
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# card_cont = soup.find_all("a", class_="TournamentCard__Container-sc-15zkmn8-0")
# find the 'next' button using xpath
    
href_list = []
current_page_num = "1"

def retrieve_all_links():
    global current_page_num
    global href_list
    next_button_class = ""
    while ("is-disabled" not in next_button_class):
        # find each tournament card
        card_list = driver.find_elements(By.CSS_SELECTOR, "a[class*='TournamentCard__Container']")
        for i in card_list:
            href_list.append(i.get_attribute("href"))
        #  find the next button at the bottom
        next_button = driver.find_element(By.XPATH, '//button[normalize-space()="Next"]')
        next_button_class = next_button.get_attribute("class")
        print(next_button_class)
        current_page_num = str(int(current_page_num) + 1)
        if ("is-disabled" not in next_button_class):
            # next_button.click()
            driver.get("https://fwango.io/dashboard?sport=roundnet&period=past&page=" + current_page_num)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Next"]')))
        else:
            break
        print(driver.current_url)
        # WebDriverWait(driver, 20).until(EC.url_contains("page=" + current_page_num))
        # sleep(1)

def retrieve_scores():
    
    # for i in hrefs:
    # driver.get(i)
    driver.get("https://fwango.io/intersquid")
    print(driver.current_url)
    # waits for results button i think?
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/nav/ul[2]/li[2]/div/a")))
    # click on results
    driver.find_element(By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/nav/ul[2]/li[2]/div/a").click()
    # wait until results title is located
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "team-column")))
    # find each team column
    teams = driver.find_elements(By.CLASS_NAME, "team-column")
    for i in teams[1:]:    
        # for some reason, find_element wasn't working when applied on a webelement, so 
        # using bs4 here to keep this data together for now
        html = i.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        team_name = soup.find('div', class_="team-name").get_text()
        # team_name = i.find_element(By.CSS_SELECTOR, "div[class*='team-name']").text
        # team_members = i.find_element(By.CLASS_NAME, "players").text
        # print(team_name, team_members)
        print(team_name)
    

# retrieve_all_links()
# retrieve_scores(href_list)
retrieve_scores()
# print(href_list)
# for i in href_list:
#     driver.get(i)
#     # waits for results button i think?
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/nav/ul[2]/li[2]/div/a")))
#     # click on results
#     driver.find_element(By.XPATH, "//*[@id=\"root\"]/span/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/nav/ul[2]/li[2]/div/a").click()
#     # wait until results title is located
#     WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/span/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]")))
driver.quit()


# html = driver.page_source
# print(html)