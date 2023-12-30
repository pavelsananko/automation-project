import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://store.steampowered.com/search/?start={0}&count=50&maxprice={1}&category1=998&untags={2}&unvrsupport=401&os=win&supportedlang=english&ignore_preferences=1'
PAGES = 1

MIN_RATING = 80
MAX_PRICE = 30
BLACKLIST = ['3799', '4085', '9130', '9551']

games = []

for page in range(max(PAGES, 1)):
    print(f'Fetching page {page + 1}/{max(PAGES, 1)}')

    url = BASE_URL.format(page * 50, MAX_PRICE, "%2C".join(BLACKLIST))

    # send request and validate response

    response = requests.get(url)

    if response.status_code != 200:
        print(f'Error fetching page {page + 1} ({response.status_code})')

        continue

    # parse data from response

    content = BeautifulSoup(response.content, 'html.parser')

    # TODO: maybe use this?
    # total_games = int(content.find(class_='search_pagination_left').text.strip().split(' ')[-1])

    rows = content.find_all(class_='search_result_row')

    for row in rows:
        link = row.get('href').split('?')[0]
        name = row.find(class_='title').text

        # get reviews

        elem = row.find(class_='search_review_summary').get('data-tooltip-html').split('<br>')[1]
        review_percent = int(elem.split(' ')[0][:-1])
        review_count = int(elem.split(' ')[3].replace(',', ''))

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

        if review_percent >= MIN_RATING:
            games.append([link, name, review_percent, review_count, price, discount])

# TODO: sort results
# TODO: output into a file

for game in games:
    print(game[1:])
