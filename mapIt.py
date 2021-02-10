import webbrowser
import sys
import pyperclip as pc


def main():
    print("Open Google Maps location")
    if len(sys.argv) == 2:
        webbrowser.open(
            "https://www.google.com/maps/place/" + sys.argv[1])
        print(sys.argv)
    else:
        webbrowser.open("https://www.google.com/maps/place/" + pc.paste())
        print(pc.paste())


if __name__ == "__main__":
    main()
