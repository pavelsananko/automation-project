import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/search'

# TODO: add filters to search

response = requests.get(url)

if response.status_code == 200:
    content = BeautifulSoup(response.content, 'html.parser')

    rows = content.find_all(class_='search_result_row')

    for row in rows:
        print(row)

        # TODO: extract info about the game
        #       (rating, price, discount price, discount %)
        #       (if possible, include tags/genre/type)
        #       (if possible, include length from HowLongToBeat)
        # TODO: add the info to games list

    # TODO: filter results
    # TODO: sort results
        
    # TODO: output into a file

else:
    print(f'Error {response.status_code}')