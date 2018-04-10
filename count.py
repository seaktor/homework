# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
song = ""
for i in range(1,6):
    name = 'corpara/{}.txt'.format(i)
    f = open(name,'r',encoding='utf-8')
    for line in f:
        song += line;
    f.close()

song=song.lower()
for i in '''.,-\n\t\u3000'()"''':
    song=song.replace(i,'')
words=song.split(' ')
dic={}
keys=set(words)
for w in keys:
    dic[w]=words.count(w)

wc = list(dic.items())
wc.sort(key=lambda x:x[1],reverse=True)
for w in range(10):
    print(wc[w])