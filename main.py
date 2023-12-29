import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://store.steampowered.com/search'
MAX_PRICE = 30
MAX_RESULTS = 0 # TODO: floor to closest 50 and use to stop the page loop, go until total_games if 0

games = []



# TODO: do the following for multiple pages
# TODO: add filters to search

page = 0
url = f'{BASE_URL}/?start={page * 50}&count=50&maxprice={MAX_PRICE}&category1=998&sort_by=Reviews_DESC&ignore_preferences=1'

response = requests.get(url)

if response.status_code != 200:
    print(f'Error {response.status_code}')
    exit() # TODO: replace with continue when in a loop

# read info

content = BeautifulSoup(response.content, 'html.parser')

# TODO: maybe use this?
# total_games = int(content.find(class_='search_pagination_left').text.strip().split(' ')[-1])

rows = content.find_all(class_='search_result_row')

for row in rows:
    name = row.find(class_='title').text
    link = row.get('href').split('?')[0]

    elem = row.find(class_='search_review_summary').get('data-tooltip-html').split('<br>')[1]
    review_percent = int(elem.split(' ')[0][:-1])
    review_count = int(elem.split(' ')[3].replace(',', ''))

    elem = row.find(class_='discount_original_price')
    if elem:
        price_original = float(elem.text[:-1].replace(',', '.'))
    else:
        price_original = 0.0

    elem = row.find(class_='discount_final_price')
    price = float(elem.text[:-1].replace(',', '.'))

    if price_original != 0.0:
        discount = round((1 - price / price_original) * 100)
    else:
        discount = 0

    # TODO: if possible, include tags/genre/type
    # TODO: if possible, include length from HowLongToBeat

    games.append([name, link, review_percent, review_count, price, discount])



# TODO: filter results
# TODO: sort results
# TODO: output into a file

for game in games:
    print(game)