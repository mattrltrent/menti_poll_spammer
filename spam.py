from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

# USER VARIABLES

number_of_spams = 5  # How many times we input our answer
menti_code = '37801126'  # Menti code of meeting
# For example, if there are 3 answers, you can input 1, 2 or 3 as what to press
answer_number = 1

# USER VARIABLES

tab_load_delay = 4


menti_code = int(input("Enter Menti Code: "))
number_of_spams = int(input("Times to Spam: "))
answer_number = int(input("Answer number (example: 2): "))


def spam():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())

        chrome_options = Options()
        chrome_options.add_argument("--incognito")

        url = 'https://www.menti.com/'

        driver.get(url)

        # Enter game code
        myElem1 = WebDriverWait(driver, tab_load_delay).until(
            EC.presence_of_element_located((By.ID, 'enter-vote-key')))
        search_input = driver.find_element_by_id('enter-vote-key')
        search_input.send_keys(menti_code)

        # Click submit game code; proceeds to game
        myElem2 = WebDriverWait(driver, tab_load_delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-bm.m-cn.m-ah.m-cu.m-f.m-cj.m-c')))
        driver.find_elements_by_css_selector(
            '.m-bm.m-cn.m-ah.m-cu.m-f.m-cj.m-c')[0].click()

        # Select multiple choice answer
        myElem3 = WebDriverWait(driver, tab_load_delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-l.m-en')))
        driver.find_elements_by_css_selector(
            '.m-a .m-gk')[answer_number - 1].click()

        # Submit multiple choice answer
        myElem4 = WebDriverWait(driver, tab_load_delay).until(
            EC.presence_of_element_located((By.TAG_NAME, 'button')))
        driver.find_element_by_tag_name(
            'button').click()

        # Allow time for answer to register and close out current running chrome application
        time.sleep(1)
        driver.close()

    except:
        print("Error caught and handled.")
        driver.close()
        spam()


for x in range(number_of_spams):
    spam()
print("Spam complete")
