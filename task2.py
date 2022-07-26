"""Задача №2.

В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы
преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду
(у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям
уникальные и легко произносимые имена. Имя у нас состоит из прилагательного,
имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77".
Для генерации таких имен мы и решали следующую задачу: Получить с русской википедии
список всех животных (https://inlnk.ru/jElywR) и вывести количество животных
на каждую букву алфавита. Результат должен получиться в следующем виде:
А: 642
Б: 412
В:...."""
import requests
from bs4 import BeautifulSoup as BS


url = 'https://inlnk.ru/jElywR'

count = 0                               # счетчик для подсчета животных      
counter_pages = 2                       # цикл работает пока 
while counter_pages < 4:                # активна "Следующая страница"
    res = requests.get(url)
    soup = BS(res.content, 'html.parser') 
    div = soup.find('div', class_="mw-category mw-category-columns")
    list_animals = div.find_all('li')
    group = div.find_all('h3')          # следующая буква алфавита
    for category in group:
        for i in list_animals:
            animals = i.a.text
            abc = category.text
            if abc == animals[0]:
                count += 1
            else:
                count = 0
                continue
            print(f'{abc}: {count}')
    # обращаемся к кнопкам в dive животных
    div_link = soup.find('div', id="mw-pages")
    buttons = div_link.find_all('a',
                        title="Категория:Животные по алфавиту")
    link = div_link.find_all('a',
                        title="Категория:Животные по алфавиту")[1]['href']
    url = 'https://ru.wikipedia.org' + link

    # количество кнопок равно 2 либо на 1, либо на последней странице 
    if len(buttons) == 2:
        counter_pages += 1