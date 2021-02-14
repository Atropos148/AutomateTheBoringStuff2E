from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


def main():
    browser = webdriver.Edge('msedgedriver.exe')
    browser.get('https://stackedit.io/')
    browser.implicitly_wait(10)

    # try:
    time.sleep(2)
    write_button = browser.find_element_by_css_selector(
        'a.navigation-bar__button')
    write_button.click()

    time.sleep(4)
    print('Waiting for page to load...')
    skip_tutorial_button = browser.find_element_by_xpath(
        "//div[@class='tour-step__button-bar']//button[@class='button']")
    print("We will skip the tutorial")
    skip_tutorial_button.click()

    print("Let's clear the editor first")
    editor = browser.find_element_by_css_selector('pre.editor__inner')
    time.sleep(.3)
    editor.click()
    time.sleep(.3)
    editor.send_keys(Keys.CONTROL, 'a')
    time.sleep(.3)
    editor.send_keys(Keys.DELETE)
    time.sleep(.3)

    print("Let's write that CV")
    unordered_list_button = browser.find_element_by_xpath(
        "//button[@title='Unordered list – Ctrl+Shift+U']")
    bold_button = browser.find_element_by_xpath(
        "//button[@title='Bold – Ctrl+Shift+B']")

    editor.send_keys('# Tibor Hrdlovič')
    editor.send_keys(Keys.ENTER)
    editor.send_keys("## Programmer")
    editor.send_keys(Keys.ENTER, Keys.ENTER)
    time.sleep(.3)

    print('Some info')
    editor.send_keys('### Basic Info')
    editor.send_keys(Keys.ENTER)
    unordered_list_button.click()
    editor.send_keys('Lives in Modra')
    editor.send_keys(Keys.ENTER)
    editor.send_keys("Born 15. 1. 1995")
    editor.send_keys(Keys.ENTER)
    editor.send_keys(Keys.BACKSPACE, Keys.BACKSPACE)
    time.sleep(.3)

    print('You can contact me here')
    editor.send_keys('### Contact')
    editor.send_keys(Keys.ENTER)
    unordered_list_button.click()
    editor.send_keys('Phone number: +421 915 708 263')
    editor.send_keys(Keys.ENTER)
    editor.send_keys('Email: tibor.h148@google.com')
    editor.send_keys(Keys.ENTER)
    editor.send_keys('Twitter: https://twitter.com/Atropos148')
    editor.send_keys(Keys.ENTER)
    editor.send_keys(Keys.BACKSPACE, Keys.BACKSPACE)
    time.sleep(.3)

    print("Some programming stuff now...")
    editor.send_keys("## Skills")
    editor.send_keys(Keys.ENTER)
    unordered_list_button.click()

    editor.send_keys('English - B2 Maturita')
    editor.send_keys(Keys.CONTROL, Keys.SHIFT, Keys.LEFT, Keys.LEFT)
    bold_button.click()
    editor.send_keys(Keys.END, Keys.ENTER)

    editor.send_keys('Programming')
    editor.send_keys(Keys.ENTER, Keys.TAB)

    editor.send_keys("Python")
    editor.send_keys(Keys.ENTER, "Java")
    editor.send_keys(Keys.UP, Keys.CONTROL, Keys.RIGHT)

    editor.send_keys(Keys.CONTROL, Keys.SHIFT, Keys.LEFT)
    bold_button.click()
    editor.send_keys(Keys.RIGHT, Keys.RIGHT, Keys.RIGHT)
    editor.send_keys(
        " - I finished almost all assignments from https://automatetheboringstuff.com/k")
    editor.send_keys(Keys.END, Keys.ENTER, Keys.TAB)

    editor.send_keys(
        'Solutions can be seen on my Github: https://github.com/Atropos148/AutomateTheBoringStuff')
    editor.send_keys(Keys.ENTER)

    editor.send_keys(
        "I'm now working on refreshing my memory with the Web Automation chapter, that can be seen here: https://github.com/Atropos148/AutomateTheBoringStuff2E")
    editor.send_keys(Keys.ENTER)

    editor.send_keys(
        "Solved about 15 days from Advent of Code 2020 (at least so far)")
    editor.send_keys(Keys.ENTER, Keys.TAB)
    editor.send_keys(
        "Solutions can be seen here: https://github.com/Atropos148/AdventOfCode2020")
    editor.send_keys(Keys.ENTER)
    editor.send_keys("This repo has the most branches I ever used")

    editor.send_keys(Keys.DOWN, Keys.CONTROL, Keys.RIGHT)
    editor.send_keys(Keys.CONTROL, Keys.SHIFT, Keys.LEFT)
    bold_button.click()
    editor.send_keys(Keys.RIGHT, Keys.RIGHT, Keys.RIGHT)
    editor.send_keys(
        " - I am currently working thru assignments that are interesting to me from here http://programmingbydoing.com/")
    editor.send_keys(Keys.ENTER, Keys.TAB)
    editor.send_keys(
        "Solutions can be seen here: https://github.com/Atropos148/Programming-by-Doing")

    time.sleep(1000)

    # except Exception:
    #     print("I didn't find an element with that name")


if __name__ == "__main__":
    main()
