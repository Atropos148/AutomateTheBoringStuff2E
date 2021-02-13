from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


def main():
    browser = webdriver.Edge('msedgedriver.exe')
    browser.get('https://stackedit.io/')
    browser.implicitly_wait(10)

    try:
        time.sleep(2)
        write_button = browser.find_element_by_css_selector(
            'a.navigation-bar__button')
        write_button.click()

        time.sleep(4)
        skip_tutorial_button = browser.find_element_by_css_selector(
            ".tour-step__button-bar")
        print(skip_tutorial_button)

        time.sleep(10000000)

    except Exception:
        print("I didn't find an element with that name")


if __name__ == "__main__":
    main()
