from bs4 import BeautifulSoup
import requests


def parsing_RBC():
    url = 'https://quote.rbc.ru/tag/stocks'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    titles = soup.findAll(class_=['q-item__title', 'news-feed__item__title'])
    links = soup.findAll(class_=['q-item__link', 'news-feed__item js-news-feed-item js-yandex-counter'])
    datas_n_time = soup.findAll(class_=['q-item__date__text', 'news-feed__item__date-text'])

    d = []
    for data in datas_n_time:
        d.append(data.text.strip())

    t = []
    for title in titles:
        t.append(title.text.strip())

    l = []
    for link in links:
        l.append(link.get('href'))

    result = []
    for i in range(len(d)):
        result.append('<a href=' + '"' + l[i] + '"'  + '>' + t[i] + '</a>')

    res = ' \n'.join(str(li).replace('\n', '') for li in result)

    res = res.split('\n')

    r = (d[i] + ' ' + res[i] for i in range(0, len(d)))

    list_r = list(r)

    string_r = '<br />'.join(str(i) for i in list_r)

    while "  " in string_r:
        string_r = string_r.replace("  ", " ")

    return string_r


def parsing_invest_funds():
    import datetime
    now = datetime.datetime.now()
    today = str(now.day) + '.' + now.strftime('%m') + '.' + str(now.year)

    url = 'https://investfunds.ru/news/?action=search&news_source_comp=1&stocks=1&beginDate=' + today + '&endDate=' + today
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    titles = soup.findAll(class_='indent_right_10 left')
    times = soup.findAll(class_='time')

    d = []
    for time in times:
        d.append(time.text)

    for t in titles:
        t['href'] = 'https://investfunds.ru' + t['href']

    res = ' \n'.join(str(t).replace('\n', '') for t in titles)

    while "  " in res:
        res = res.replace("  ", " ")

    res = res.split('\n')

    r = (d[i] + ' ' + res[i] for i in range(0, len(d)))

    list_r = list(r)

    string_r = '<br />'.join(str(i) for i in list_r)

    while "  " in string_r:
        string_r = string_r.replace("  ", " ")

    return string_r


def parsing_moex():
    url = 'https://www.moex.com/ru/news/'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.findAll(class_='new-moex-news-list__link')
    times = soup.findAll(class_='new-moex-news-list__time')
    datas = soup.findAll(class_='new-moex-news-list__date')

    d = []
    for data in datas:
        d.append(data.text.strip())

    t = []
    for time in times:
        t.append(time.text.strip())

    for l in links:
        l['href'] = 'https://www.moex.com' + l['href']

    res = ' \n'.join(str(li).replace('\n', '') for li in links)

    while "  " in res:
        res = res.replace("  ", " ")

    res = res.split('\n')

    r = (d[i] + ' ' + t[i] + ' ' + res[i] for i in range(0, len(d)))

    list_r = list(map(lambda x: x.replace('\r', ''), r))

    string_r = '<br />'.join(str(i) for i in list_r)

    while "  " in string_r:
        string_r = string_r.replace("  ", " ")

    return string_r


if __name__ == "__main__":
    print(parsing_RBC())
    print(parsing_moex())