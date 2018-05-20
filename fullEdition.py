#encoding=utf-8
import requests
from bs4 import BeautifulSoup

import jieba
import csv
import json

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pylab

horoscope =["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricornus","Aquarius","Pisces"]
hash1 ={}
jieba.set_dictionary('dict.txt.big.txt')
jieba.load_userdict("userdict.txt")

#download the information from ptt
for i in range(len(horoscope)):
    url = "https://www.ptt.cc/bbs/"+horoscope[i]+"/index.html"
    title =[]
    for round in range(10):
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        tag_name = "div.title a"
        articles = soup.select(tag_name)
        page2 = "div.btn-group-paging a"
        paging = soup.select(page2)
        next_url ="https://www.ptt.cc"+paging[1]["href"]
        url = next_url
        for art in articles:
            title.append(art.text)

    word = str(title)  
    cutWords = jieba.cut(word,cut_all=False)   #cut words
    wordFinal =[]
    for j in cutWords:
        if (j != "問題" and j != "運勢" and j != "唐綺陽" and j != "唐老師" and j != "唐立"
      and j != "星座" and j != "每日" and j != "禪卡" and j != "生日" and j != "生日快樂"
      and j != "今日" and j != "奧修" and  j != "Alex是大叔" and j != "紫微網"
      and j != "石井" and j != "DailyHoroscope" and j != "Daily" and j != "daily"
      and j != "The" and j != "Weekly" and j != "日誌" and j != "日運"
      and j != "Horoscope" and j != "horoscope" and j != "情報" and j != "塔羅" 
      and j != "n'" and j != "週末" and j != "本週" and j != "n'" and j != "米薩"
      and j != "小姐" and j != "[" and j != "]" and j != "Re"):
            wordFinal.append(j)    
    
    file_name =horoscope[i]   #put the data into file
    f = open(file_name+".txt","w",encoding='utf-8')
    for w in wordFinal:
        f.write(str(w))
        f.write('\n')
    f.close()
    f = open(file_name+".txt",'r',encoding='utf-8')
    word = f.read()
    wordcloud = WordCloud().generate(word)

    #pylab inline
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(file_name+".png")
    pylab.show()
    
    

    



    


    


    












   
