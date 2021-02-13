import os
import webbrowser
import requests
import bs4


def main():
    print("hello")

    # change this to ""https://xkcd.com"
    main_url: str = "https://xkcd.com"

    current_url: str = main_url
    total_files: int = 0

    while not current_url.endswith('#'):
        res = requests.get(current_url)
        print("Opening: " + current_url)

        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        skipped_urls = ["https://xkcd.com/2198/", "https://xkcd.com/2067/",
                        "https://xkcd.com/1663/", "https://xkcd.com/1608/", "https://xkcd.com/1525/", "https://xkcd.com/1416/", "https://xkcd.com/1350/", "https://xkcd.com/1331/", "https://xkcd.com/1037/"]

        if current_url in skipped_urls:
            print('Skipping ' + current_url)

            all_buttons = soup.select('ul.comicNav > li > a')

            prev_url = get_prev_image_url(all_buttons)

            next_url = main_url + prev_url
            current_url = next_url

            print("Going to " + current_url)

        else:
            try:
                image: str = soup.select('div#comic > img')[0]
            except IndexError:
                image: str = soup.select('div#comic > a > img')[0]

            image_url: str = image.get('src')
            all_buttons = soup.select('ul.comicNav > li > a')

            image = requests.get('https:' + image_url)
            image.raise_for_status()

            os.makedirs('xkcd', exist_ok=True)

            image_file_name = os.path.basename(image_url)
            image_file_folder = os.path.join(
                'xkcd', image_file_name).replace('\\', os.sep)
            total_files += 1

            if not os.path.isfile(image_file_folder):
                print("downloading image: " + image_file_folder)
                image_file = open(image_file_folder, 'wb')

                for chunk in image.iter_content(100000):
                    image_file.write(chunk)
                image_file.close()

            else:
                print("Image " + image_file_folder + " already exists")

            prev_url = get_prev_image_url(all_buttons)

            next_url = main_url + prev_url
            current_url = next_url

    print("Everything is now downloaded, number of files: " + str(total_files))


def get_prev_image_url(all_buttons) -> str:
    for button in all_buttons:
        if type(button.get('rel')) == list and button.get('rel')[0] == 'prev':
            prev_button = button
            break
    return prev_button.get('href')


if __name__ == "__main__":
    main()
