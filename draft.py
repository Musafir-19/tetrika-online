

# url = 'https://inlnk.ru/jElywR'
# data = []
# for pages in range(201):
#     res = requests.get(url)
#     soup = BS(res.content, 'html.parser')
#     alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
#     div = soup.find('div', class_="mw-category mw-category-columns")
#     # group = div.h3.text
#     list_animals = div.find_all('li')
#     for i in list_animals:
#         animals = i.a.text
#         # data.append(animals)
#     div_link = soup.find('div', id="mw-pages")
#     link = div_link.find_all('a', title="Категория:Животные по алфавиту")[1]
#     # url = f'https://ru.wikipedia.org' + {link}
# print(link)

# url = 'https://inlnk.ru/jElywR'
# count = 0

# for pages in range(201): 
#     res = requests.get(url)
#     soup = BS(res.content, 'html.parser') 
#     div = soup.find('div', class_="mw-category mw-category-columns")
#     list_animals = div.find_all('li')
#     for i in list_animals:
#         animals = i.a.text
#         count += 1
#     print(count)
#     print(animals)
#     div_link = soup.find('div', id="mw-pages")
#     link = div_link.find_all('a',
#                         title="Категория:Животные по алфавиту")[1]['href']
#     url = 'https://ru.wikipedia.org' + link  