#  READ ME
# 1.  В задании не четко сформулировано - то ли надо выводить 10 топ слов по каждой новостной ленте , то ли общий топ ..
# сделал общий топ 10 по всем лентам
#
# 2.  файл новостей newsfr.json - у него не определить кодировку , ни перебором в Sublime ни с помщью автоопределения
# через код :
# import chardet
# def check_encoding(fname):
#     rawdata = open(fname, "rb").read()
#     result = chardet.detect(rawdata)
#     return result['encoding']
# Более того , если посмотреть содержание этого файла на Github , то выясняется , что он совпадает с newscy.json.
# Так что , я не стал включать этот файл в список новостей.
#
# 3.  Структура новостных лент отличается друг от друга , поэтому я не стал делать универсальную функцию парсинга ,
# а ручками настроил путь к тексту новостей для каждой ленты .
#

import json
import re
import collections

def modify_list(l):
    index =[]  # список индексов на удаление
    cnt = 0
    for i in range(len(l)):
        if len(l[i]) < 6 : index.append(i)
    for k in index:
        l.pop(k-cnt)
        cnt += 1

def prnt_10_most_common(lst):
    c = collections.Counter()
    for word in lst:
        c[word] += 1
    for i in range(10):
        print(*c.most_common(10)[i])

text = ""

with open("newsit.json" , encoding="cp1251") as f:
    data = json.load(f, encoding="cp1251")
for i in range(len(data['rss']["channel"]["item"])):
    text += data['rss']["channel"]["item"][i]["description"] + ' '

with open("newsafr.json" , encoding="utf8") as f:
    data = json.load(f, encoding="utf8")
for i in range(len(data['rss']["channel"]["item"])):
    text += data['rss']["channel"]["item"][i]["description"]["__cdata"]


with open("newscy.json" , encoding="koi8_r") as f:
    data = json.load(f, encoding="koi8_r")
for i in range(len(data['rss']["channel"]["item"])):
    text += data['rss']["channel"]["item"][i]["description"]["__cdata"]

lst = re.findall(r"\w+", text)

modify_list(lst)
prnt_10_most_common(lst)

