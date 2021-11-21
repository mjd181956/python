import wordcloud
import jieba
import imageio
jieba.setLogLevel(jieba.logging.INFO)

txt="""
我觉得这件商品很智能，并且便宜又实用
刚买的，感觉很好用，孩子很喜欢，最主要是价格便宜
智能化家居，我最喜欢了，希望这家店继续出现新的家居产品
智能电灯，不仅可以语音打开灯光还可以用手机操控
下次再买这家店的智能产品
必须给五星好评，真的智能空调又省电又智能，我很喜欢

主人公继承了家族血脉，天生拥有霸王神力
然后在继承家族血脉的同时自己已经过后天的努力，有学会了更多的技能。假如因为敌人强大，对战的时候导致血脉之力尽失，也就是失去了家族血脉之力，本来以为此生再无踏入修炼之路，却因为偶然机遇，得到了上古神兽的血脉，因此血脉重洗，并拥有神兽的技能
    """

#对文字进行分割成词语，并且以空格形式隔开
data=jieba.lcut(txt)
data=" ".join(data)
# print(data)

im = imageio.imread(r"F:\python\爱心.png")
#实例化词云对象
img_cloud=wordcloud.WordCloud(mask=im,background_color="white",width=800,height=600,font_path="msyh.ttf")
#使用词云对象的方式往里传入数据
img_cloud.generate(data)
#使用相对路径方式，保存图片
img_cloud.to_file("词云爱心.png")
print("词云图已生成")
