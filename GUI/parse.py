from bs4 import BeautifulSoup
import requests


def parsing_RBC():
    url = 'https://quote.rbc.ru/tag/stocks'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.findAll(class_=['q-item__link', 'news-feed__item js-news-feed-item js-yandex-counter'])
    titles = soup.findAll(class_=['q-item__title', 'news-feed__item__title'])
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
        result.append([d[i], t[i], l[i]])

    return result  # чтобы ф-ция выводила на консоль, необходимо написать инструкцию с print


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

    t = []
    for title in titles:
        t.append(title.text.strip())

    l = []
    for title in titles:
        l.append(title.get('href'))

    result = []
    for i in range(len(d)):
        result.append([d[i], t[i], 'https://investfunds.ru' + l[i]])

    return result


def parsing_moex():
    url = 'https://www.moex.com/ru/news/'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.findAll(class_='news-list__link')
    datas = soup.findAll(class_='col-lg-30')

    d = []
    for data in datas:
        d.append(data.text.strip())

    t = []
    for title in links:
        t.append(title.text.strip())

    l = []
    for link in links:
        l.append(link.get('href'))

    result = []
    for i in range(len(d)):
        result.append([d[i], t[i], 'https://www.moex.com/' + l[i]])

    return result


if __name__ == "__main__":
    parsing_RBC()
    parsing_invest_funds()
    parsing_moex()
