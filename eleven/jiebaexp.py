import jieba
jieba.setLogLevel(jieba.logging.INFO)
comment="""
    我觉得这件商品很智能，并且便宜又实用
    刚买的，感觉很好用，孩子很喜欢，最主要是价格便宜
    智能化家居，我最喜欢了，希望这家店继续出现新的家居产品
    智能电灯，不仅可以语音打开灯光还可以用手机操控
    下次再买这家店的智能产品
    必须给五星好评，真的智能空调又省电又智能，我很喜欢
    """

    #对文本数据进行分割
def data_split():
    data=jieba.lcut(comment)
    for i in data:
        if "\n" in i :
            data.remove(i)
        elif "," in i :
            data.remove(i)
        elif len(i)==1 :
            data.remove(i)
    return data

#对文本数据次数进行统计
def data_count():
    count={}
    info_save=[]
    for i in data_split():
        if i in info_save:
            count[i]=count.get(i,0)+1
        else:
            count[i]=count.get(i,0)
            info_save.append(i)
    count=list(count.items())
    return count

#对文本数据统计次数去除频次最高的前3
def data_ordinal():
    comment_data=data_count()
    comment_data=sorted(comment_data,key=lambda x:x[1],reverse=True)
    return comment_data[0:3]

#程序入口
if __name__=="__main__":
    print(data_ordinal())