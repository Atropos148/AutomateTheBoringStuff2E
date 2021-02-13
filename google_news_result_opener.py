from typing import List
import webbrowser
import sys
import requests
import bs4


def main():
    print("hello")

    search_url: List = ["https://www.google.com/search?q=", "&tbm=nws"]

    # if len(sys.argv) == 2:
    #     topic_name: str = sys.argv[1]

    while True:
        topic_name = input("What do you want to search? > ")
        if topic_name == 'exit':
            break

        print("Opening: " + (search_url[0]+topic_name+search_url[1]))
        res = requests.get(search_url[0]+topic_name+search_url[1])
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        clean_search_results: List = []

        search_results = soup.select("div > div > div > a")
        for result in search_results:
            if result.get('href')[:4] == '/url':
                dirty_url: str = result.get('href')[7:]
                ending_position: int = dirty_url.find('&sa=')
                clean_url: str = dirty_url[:ending_position]
                clean_search_results.append(clean_url)

        tabs_to_open: int = min(5, len(clean_search_results))

        for i in range(tabs_to_open):
            url_to_open = clean_search_results[i]
            print("Opening: " + url_to_open)

            webbrowser.open(url_to_open)


if __name__ == "__main__":
    main()

# https://www.google.com/search?q=dfs&tbm=nws
# rso > div:nth-child(2) > g-card > div > div > div.dbsr > a
# rso > div:nth-child(1) > g-card > div > div > div.dbsr > a
