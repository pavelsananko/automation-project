import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://store.steampowered.com/search/?start={0}&count=50&maxprice={1}&category1=998&untags=3799%2C4085%2C9130%2C9551&unvrsupport=401&os=win&supportedlang=english'
PAGES = 1

MIN_REVIEW_PERCENT = 80
MIN_REVIEW_COUNT = 1000
MAX_PRICE = 30
TAGS = []

# fetch games from steam store

games = []

for page in range(max(PAGES, 1)):
    print(f'Fetching page {page + 1}/{max(PAGES, 1)}')

    # send request and validate response

    url = BASE_URL.format(page * 50, MAX_PRICE)
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

        # get tags

        tags = row.get('data-ds-tagids')[1:-1].split(',')
        tags = [int(tag) for tag in tags]

        # get reviews

        elem = row.find(class_='search_review_summary')

        if elem:
            review_text = elem.get('data-tooltip-html').split('<br>')[1]
            review_pct = int(review_text.split(' ')[0][:-1])
            review_cnt = int(review_text.split(' ')[3].replace(',', ''))
        else:
            review_pct = 0
            review_cnt = 0

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

        # add game to list

        if review_pct < MIN_REVIEW_PERCENT:
            continue

        if review_cnt < MIN_REVIEW_COUNT:
            continue

        if len(TAGS) > 0 and not any(tag in tags for tag in TAGS):
            continue

        games.append({'link': link, 'name': name, 'tags': tags,
                      'review_pct': review_pct, 'review_cnt': review_cnt,
                      'price': price, 'discount': discount})

    # if last page is reached before page limit, exit loop early

    if len(rows) == 0:
        break

# sort results by discount

games.sort(key=lambda row: row['discount'], reverse=True)

# write results to file

# TODO: output into a file
#with open('test.txt', '+w') as file:
#    for game in games:
#        pass

print(f'\n{len(games)} games found!')
