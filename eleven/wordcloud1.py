import wordcloud

txt="Youth will come to an end, but memeory will last forever."

#实例化词云对象
img_cloud=wordcloud.WordCloud(background_color="white")

#使用词云对象方法，往里面传入数据
img_cloud.generate(txt)

#使用相对路径的方式，保存图片
img_cloud.to_file("词云图.png")
print("词云图已经生成")
