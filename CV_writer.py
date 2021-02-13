from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


def main():
    browser = webdriver.Edge('msedgedriver.exe')
    browser.get('https://write.as/')

    try:
        time.sleep(2)
        im_not_a_robot_button = browser.find_element_by_css_selector(
            'a.btn.cta')
        im_not_a_robot_button.click()
        time.sleep(5)
        dark_theme_button = browser.find_element_by_id('toggle-theme')
        dark_theme_button.click()

        time.sleep(100)

    except Exception:
        print("I didn't find an element with that name")


if __name__ == "__main__":
    main()
