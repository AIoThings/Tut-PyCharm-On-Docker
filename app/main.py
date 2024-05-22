import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument('--Headless')
    options.add_argument('--disable-dev-shm-usage')  # /tmp, not share memory!

    driver = webdriver.Chrome(options=options)

    url = "https://www.google.com"
    driver.get(url)
    driver.save_screenshot('screenshot.png')
    # time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    headings = soup.find_all('div', {'class': 'szppmdbYutt__middle-slot-promo'})
    for heading in headings:
        print(heading.getText())

    # time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    print("Hello, I am inside!")
    main()
