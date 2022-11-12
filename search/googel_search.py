import time
from googlesearch import search
from .models import *

# data_search = SearchBox.objects.all().values()
# data_end = data_search[::-1][0]
# data_title = data_end['search_box']
# data_num = data_end['number']
#
# def search_results(query, number, advanced=True):
#     titles = []
#     urls = []
#     for title in search(query, num_results=number, advanced=advanced):
#         titles.append(title.title)
#         urls.append(title.url)
#         m = list(zip(titles, urls))
#         print(f'title = {titles} , urls = {urls}')
#         print(len(urls))
#         print(list(zip(titles, urls)))
#
#
# search_results(data_title, data_num)
# time.sleep(10)


# print(SearchBox.search_box, SearchBox.number)