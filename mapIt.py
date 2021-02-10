import webbrowser
import sys
import pyperclip as pc
import tkinter as tk


def main():
    print("Open Google Maps location")
    open_map()

    cities = ["New York", "Paris", "Prague", "Seoul"]
    for city in cities:
        open_map_specific(city)


def open_map_specific(location: str):
    webbrowser.open(
        "https://www.google.com/maps/place/" + location)


def open_map():
    if len(sys.argv) == 2:
        webbrowser.open(
            "https://www.google.com/maps/place/" + sys.argv[1])
        print(sys.argv)
    else:
        webbrowser.open("https://www.google.com/maps/place/" + pc.paste())
        print(pc.paste())


if __name__ == "__main__":
    main()
