
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import pandas as pd
import time
import sys


def get_singer_song(url,name):
    url_singer = url
    response = requests.get(url_singer)
    soup = BeautifulSoup(response.text,"lxml")

    hd3 = soup.find("span",class_="hd3").find("a",href=True)
    url_songlist = urljoin(url_singer, hd3['href'])
    url_songlist

    response = requests.get(url_songlist)
    soup = BeautifulSoup(response.text,"lxml")


    hb2 = soup.find_all("dd",class_="hb2")
    hb3 = soup.find_all("dd",class_="hb3")
    
    
    

    link1 = [tag.find('a', href=True) for tag in hb2]
    link2 = [tag.find('a', href=True) for tag in hb3]
    
    hc1_1 = [tag.find(class_="hc1").text for tag in hb2]
    hc2_1 = [tag.find(class_="hc2").text for tag in hb2]
    hc3_1 = [tag.find(class_="hc3").text for tag in hb2]
    hc4_1 = [tag.find(class_="hc4").text for tag in hb2]
    hc1_2 = [tag.find(class_="hc1").text for tag in hb3]
    hc2_2 = [tag.find(class_="hc2").text for tag in hb3]
    hc3_2 = [tag.find(class_="hc3").text for tag in hb3]
    hc4_2 = [tag.find(class_="hc4").text for tag in hb3]
    #print(link1)
    
    song_name_list = []
    wait_list = []
    wait_list_2 = []
    word_list = []
    writer_list = []
    composer_list = []
    day_list = []
    singer_list = []
    
    for namee in hc1_1:
        song_name_list.append(namee)
    for namee in hc1_2:
        song_name_list.append(namee)

    for writer in hc2_1:
        writer_list.append(writer)
    for writer in hc2_2:
        writer_list.append(writer)

    for composer in hc3_1:
        composer_list.append(composer)
    for composer in hc3_2:
        composer_list.append(composer)

    for day in hc4_1:
        day_list.append(day)
    for day in hc4_2:
        day_list.append(day)

    for link in link1:
        wait_list.append(link)
    for link in link2:
        wait_list.append(link)
        

    for link in wait_list:
        # 透過 urljoin 確認超連結是絕對位置
        url_song = urljoin(url_songlist, link['href'])
        wait_list_2.append(url_song)
    
    hd4 = soup.find_all("span",class_="hd4")
    if len(hd4):
        link_more_song = hd4[0].find_all('a', href=True)
        for link in link_more_song[1:]:
            url_more_song = urljoin(url_singer, link['href'])
            wait_list_2 = get_more_song(url_more_song,wait_list_2)
            song_name_list,writer_list,composer_list,day_list = get_more_song_name(url_more_song,song_name_list,writer_list,composer_list,day_list)
    
    
    
    for link in wait_list_2:
        for i in range(10):
            try:
                response = requests.get(link)
            except:
                if i >= 9:
                    do_some_log()
                else:
                    time.sleep(0.5)
            else:
                time.sleep(0.1)
                break
        soup = BeautifulSoup(response.text,"lxml")
        word = [text for text in soup.find("dd",id="fsZx3").stripped_strings]
        word_str = "\n".join(word)
        word_list.append(word_str)

    for i in range(len(song_name_list)):
        singer_list.append(name);

    word_df = pd.DataFrame(
        {
            "歌手":singer_list,
            "歌名":song_name_list,
            "作詞":writer_list,
            "作曲":composer_list,
            "日期":day_list,
            "歌詞":word_list
        },
        columns = ["歌手","歌名","作詞","作曲","日期","歌詞"]
    )
    name = name.replace("/"," ")
    name = name.replace("*"," ")
    name = name.replace("-"," ")
    name = name.replace("+"," ")
    word_df.to_csv("./{}/{}.csv".format(sys.argv[1],name),index=False,encoding="utf_8_sig")
    print("{}.csv completed!".format(name))
    
def get_more_song(url,wait_list_2):
    url_song_list = url
    response = requests.get(url_song_list)
    soup = BeautifulSoup(response.text,"lxml")
    
    hb2 = soup.find_all("dd",class_="hb2")
    hb3 = soup.find_all("dd",class_="hb3")
    
    link1 = [tag.find('a', href=True) for tag in hb2]
    link2 = [tag.find('a', href=True) for tag in hb3]

    wait_list = []
    
    for link in link1:
        wait_list.append(link)
    for link in link2:
        wait_list.append(link)
    
    for link in wait_list:
        # 透過 urljoin 確認超連結是絕對位置
        url_song = urljoin(url_song_list, link['href'])
        wait_list_2.append(url_song)
    
    return wait_list_2

def get_more_song_name(url,song_name_list,writer_list,composer_list,day_list):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    
    hb2 = soup.find_all("dd",class_="hb2")
    hb3 = soup.find_all("dd",class_="hb3")
    
    hc1_1 = [tag.find(class_="hc1").text for tag in hb2]
    hc2_1 = [tag.find(class_="hc2").text for tag in hb2]
    hc3_1 = [tag.find(class_="hc3").text for tag in hb2]
    hc4_1 = [tag.find(class_="hc4").text for tag in hb2]
    hc1_2 = [tag.find(class_="hc1").text for tag in hb3]
    hc2_2 = [tag.find(class_="hc2").text for tag in hb3]
    hc3_2 = [tag.find(class_="hc3").text for tag in hb3]
    hc4_2 = [tag.find(class_="hc4").text for tag in hb3]
    
    for namee in hc1_1:
        song_name_list.append(namee)
    for namee in hc1_2:
        song_name_list.append(namee)

    for writer in hc2_1:
        writer_list.append(writer)
    for writer in hc2_2:
        writer_list.append(writer)

    for composer in hc3_1:
        composer_list.append(composer)
    for composer in hc3_2:
        composer_list.append(composer)

    for day in hc4_1:
        day_list.append(day)
    for day in hc4_2:
        day_list.append(day)
    
    return song_name_list,writer_list,composer_list,day_list
    
    

##男:https://mojim.com/twza1.htm
##女:https://mojim.com/twzb1.htm
##團體:https://mojim.com/twzc1.htm
##日韓:https://mojim.com/twzf1.htm
##歐美:https://mojim.com/twze1.htm
##其他:https://mojim.com/twzz1.htm
start = {}
start['male'] = 'https://mojim.com/twza1.htm'
start['female'] = 'https://mojim.com/twzb1.htm'
start['group'] = 'https://mojim.com/twzc1.htm'
start['JapanKorea'] = 'https://mojim.com/twzf1.htm'
start['EUNA'] = 'https://mojim.com/twze1.htm'
start['else'] = 'https://mojim.com/twzz1.htm'
start['test'] = 'https://mojim.com/twza1.htm'

url_singerlist = start[sys.argv[1]] ##起始網址

response = requests.get(url_singerlist)
soup = BeautifulSoup(response.text,"lxml")

wait_list_singer = []

man_singer = soup.find("ul",class_="s_list").find_all("li")
link_list = [tag.find('a', href=True) for tag in man_singer]

for link in link_list:
    # 透過 urljoin 確認超連結是絕對位置
    if link != None:
        url_singer = urljoin(url_singerlist, link['href'])
        wait_list_singer.append(url_singer)


for link in wait_list_singer:
    url_singerlist2 = link
    response = requests.get(url_singerlist2)
    soup = BeautifulSoup(response.text,"lxml")

    wait_list_singer2 = []

    man_singer2 = soup.find("ul",class_="s_listA").find_all("li")
    singer_name_list2 = [tag.text for tag in man_singer2]
    link_list2 = [tag.find('a', href=True) for tag in man_singer2]

    for link2 in link_list2:
        # 透過 urljoin 確認超連結是絕對位置
        url_singer2 = urljoin(url_singerlist2, link2['href'])
        wait_list_singer2.append(url_singer2)
    for i in range(len(wait_list_singer2)):
        if sys.argv[1] == 'test' and i == 5:
            exit(0)
        try:
            get_singer_song(wait_list_singer2[i],singer_name_list2[i])
        except KeyboardInterrupt:
            exit(0)
        except:
            print("此歌手爬取失敗")

