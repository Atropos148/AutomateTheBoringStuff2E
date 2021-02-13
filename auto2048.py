from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():
    browser = webdriver.Edge('msedgedriver.exe')
    browser.get('https://gabrielecirulli.github.io/2048/')

    try:
        # element = browser.find_element_by_class_name('cover-thumb')
        # link = browser.find_element_by_link_text('Read Online for Free')

        # print(f'Found <{element.tag_name}> element with that name!')

        # type(link)
        # link.click()

        html_element = browser.find_element_by_tag_name('html')

        while True:
            html_element.send_keys(Keys.UP)
            time.sleep(0.3)
            html_element.send_keys(Keys.RIGHT)
            time.sleep(0.3)
            html_element.send_keys(Keys.DOWN)
            time.sleep(0.3)
            html_element.send_keys(Keys.LEFT)
            time.sleep(0.3)

    except Exception:
        print("I didn't find an element with that name")


if __name__ == "__main__":
    main()
