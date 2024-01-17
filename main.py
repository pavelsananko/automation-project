from math import ceil

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Alignment

# input search settings

filter_review_pct = int(input('Min review percent: '))
filter_review_cnt = int(input('Min review count:   '))
filter_price      = int(input('Max product price:  '))
filter_tags       = str(input('Tags to search:     ')).split(',')
filter_pages      = int(input('Pages to scrape:    '))

filter_tags = [t.strip() for t in filter_tags]
filter_pages = max(filter_pages, 1)

print()

# fetch tag ids

tag_ids = []

for tag in filter_tags:
    print(f'Fetching tag "{tag}"')

    # send request and validate response

    url = f'https://store.steampowered.com/tags/en/{tag}'
    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        print(f'Error fetching tag "{tag}" ({response.status_code})')
        continue

    # parse data from response

    content = BeautifulSoup(response.content, 'html.parser')
    elem = content.find(id='application_config')

    if elem:
        tag_id = elem.get('data-ch_hub_data')
        tag_id = int(tag_id.split(':')[-1][:-1])

        tag_ids.append(tag_id)

print()

# fetch games from steam store

games = []

for page in range(filter_pages):
    print(f'Fetching page {page + 1}/{filter_pages}')

    req_start = page * 50
    req_price = ceil(filter_price / 5) * 5

    if req_price == 0:
        req_price = 'free'

    # send request and validate response

    url = f'https://store.steampowered.com/search/?start={req_start}&count=50&maxprice={req_price}&category1=998&untags=3799%2C4085%2C9130%2C9551&unvrsupport=401&os=win&supportedlang=english'
    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        print(f'Error fetching page {page + 1} ({response.status_code})')
        continue

    # parse data from response

    content = BeautifulSoup(response.content, 'html.parser')
    rows = content.find_all(class_='search_result_row')

    for row in rows:
        name = row.find(class_='title').text
        link = row.get('href').split('?')[0]

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

        # filter and add to list

        if review_pct < filter_review_pct:
            continue

        if review_cnt < filter_review_cnt:
            continue

        if price > filter_price:
            continue

        if len(tag_ids) > 0 and not any(tag in tags for tag in tag_ids):
            continue

        games.append({'name': name, 'link': link,
                      'review_pct': review_pct, 'review_cnt': review_cnt,
                      'price': price, 'discount': discount})

    # if last page is reached before page limit, exit loop early

    if len(rows) == 0:
        break

# sort games by discount

games.sort(key=lambda row: row['discount'], reverse=True)

# write games to file

workbook = Workbook()
sheet = workbook.active

sheet['A1'].value = 'NAME'
sheet['B1'].value = 'RATING'
sheet['C1'].value = 'REVIEWS'
sheet['D1'].value = 'PRICE'
sheet['E1'].value = 'DISCOUNT'

sheet['A1'].alignment = Alignment(horizontal='left')
sheet['B1'].alignment = Alignment(horizontal='right')
sheet['C1'].alignment = Alignment(horizontal='right')
sheet['D1'].alignment = Alignment(horizontal='right')
sheet['E1'].alignment = Alignment(horizontal='right')

sheet.column_dimensions['A'].width = 40
sheet.column_dimensions['B'].width = 10
sheet.column_dimensions['C'].width = 10
sheet.column_dimensions['D'].width = 10
sheet.column_dimensions['E'].width = 10

sheet.freeze_panes = sheet['A2'] # sticky first row

for i, game in enumerate(games):
    row = i + 2

    sheet[f'A{row}'].value = game['name']
    sheet[f'A{row}'].hyperlink = game['link']
    sheet[f'A{row}'].style = 'Hyperlink'

    sheet[f'B{row}'].value = game['review_pct'] / 100
    sheet[f'B{row}'].number_format = '0%'

    sheet[f'C{row}'].value = game['review_cnt']
    sheet[f'C{row}'].number_format = '#,##0'

    sheet[f'D{row}'].value = game['price']
    sheet[f'D{row}'].number_format = '#,##0.00\\ [$€-1]'

    sheet[f'E{row}'].value = game['discount'] / 100
    sheet[f'E{row}'].number_format = '0%'

workbook.save('result.xlsx')

print(f'\n{len(games)} games found!')
