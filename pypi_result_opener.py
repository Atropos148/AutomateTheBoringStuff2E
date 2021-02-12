import webbrowser
import sys
import requests
import bs4


def main():
    print("hello")

    search_url: str = "https://pypi.org/search/?q="

    if len(sys.argv) == 2:
        package_name: str = sys.argv[1]

        res = requests.get(search_url+package_name)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        search_results = soup.select('.package-snippet')

        tabs_to_open: int = min(5, len(search_results))

        for i in range(tabs_to_open):
            url_to_open = "https://pypi.org/" + search_results[i].get('href')
            print("Opening: " + url_to_open)

            webbrowser.open(url_to_open)


if __name__ == "__main__":
    main()
