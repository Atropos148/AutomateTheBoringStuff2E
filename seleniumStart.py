from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    browser = webdriver.Edge('msedgedriver.exe')
    browser.get('https://nostarch.com')

    try:
        # element = browser.find_element_by_class_name('cover-thumb')
        # link = browser.find_element_by_link_text('Read Online for Free')

        # print(f'Found <{element.tag_name}> element with that name!')

        # type(link)
        # link.click()

        html_element = browser.find_element_by_tag_name('html')

        html_element.send_keys(Keys.END)
        time.sleep(1)
        html_element.send_keys(Keys.HOME)
        time.sleep(1)

    except Exception:
        print("I didn't find an element with that name")


if __name__ == "__main__":
    main()
