import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://store.steampowered.com/search/?start={0}&count=50&maxprice={1}&category1=998&untags=3799%2C4085%2C9130%2C9551&unvrsupport=401&os=win&supportedlang=english'
PAGES = 1

MIN_REVIEW_PERCENT = 80
MIN_REVIEW_COUNT = 100
MAX_PRICE = 30

games = []

for page in range(max(PAGES, 1)):
    print(f'Fetching page {page + 1}/{max(PAGES, 1)}')

    url = BASE_URL.format(page * 50, MAX_PRICE)

    # send request and validate response

    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        print(f'Error fetching page {page + 1} ({response.status_code})')
        continue

    # parse data from response

    content = BeautifulSoup(response.content, 'html.parser')
    rows = content.find_all(class_='search_result_row')

    for row in rows:
        link = row.get('href').split('?')[0]
        name = row.find(class_='title').text

        # get reviews

        elem = row.find(class_='search_review_summary')

        if elem:
            review_text = elem.get('data-tooltip-html').split('<br>')[1]
            review_percent = int(review_text.split(' ')[0][:-1])
            review_count = int(review_text.split(' ')[3].replace(',', ''))
        else:
            review_percent = 0
            review_count = 0

        # get price

        elem = row.find(class_='discount_final_price')

        if elem and elem.text != 'Free':
            price = float(elem.text[:-1].replace(',', '.'))
        else:
            price = 0.0

        # get discount

        elem = row.find(class_='discount_pct')

        if elem:
            discount = int(elem.text[1:-1])
        else:
            discount = 0

        # filter and add game to list

        if review_percent >= MIN_REVIEW_PERCENT and review_count >= MIN_REVIEW_COUNT:
            games.append([link, name, review_percent, review_count, price, discount])
    
    # if somehow the last page is reached, exit the loop early

    if len(rows) < 50:
        break

# TODO: sort results
# TODO: output into a file

for game in games:
    print(game[1:])

print(f'{len(games)} games found.')
