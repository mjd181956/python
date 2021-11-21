import jieba
import imageio
import wordcloud
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
import numpy as np

#小说数据读取
def re_data(path):
    with open(path,"r",encoding='utf-8') as file:
        data=file.read()
        return data
#小说词语分割
def re_split(text):
    Word_split=jieba.lcut(text)
    new_word=[]
    for i in Word_split:
        if "，" in i:
            Word_split.remove(i)
        elif " " in i:
            Word_split.remove(i)
        elif len(i) == 0:
            Word_split.remove(i)
        else:
            new_word.append(i)
    
    return new_word

#小说词语次数统计
def re_count(word_split):
    info_save={}
    info_pre=[]
    for i in word_split:
        if i in info_pre:
            info_save[i]=info_save.get(i,0)+1
        else:
            info_save[i]=info_save.get(i,0)
            info_pre.append(i)
    info_save=list(info_save.items())
    info_save=sorted(info_save,key=lambda x:x[1],reverse=True)
    return info_save[0:5]

#小说词云生成
def re_img(word_split):
    Word_split=" ".join(word_split)
    sw=set(STOPWORDS)
    sw.add("ok")
    im=np.array(Image.open(r"F:\python\eleven\爱心.png"))
    imagwc=wordcloud.WordCloud(mask=im,background_color="white",stopwords=sw,scale=4,font_path="msyh.ttf").generate(Word_split)
    imagwc.to_file("xy.jpg")

if __name__ == "__main__":
    text=re_data(r"F:\python\from\玄幻小说.txt")
    print("文本数据读取成功")
    word_split=re_split(text)
    print(re_count(word_split))
    re_img(word_split)
    os.system("start xy.jpg")
    print("词云图已打开")





