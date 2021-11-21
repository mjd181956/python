import jieba

jieba.setLogLevel(jieba.logging.INFO)
data = """
    主人公继承了家族血脉，天生拥有霸王神力。
    然后在继承家族血脉的同时自己已经过后天的努力，有学会了更多的技能。假如因为敌人强大，对战的时候导致血脉之力尽失，
    也就是失去了家族血脉之力，本来以为此生再无踏入修炼之路，却因为偶然机遇，得到了上古神兽的血脉，因此血脉重洗，并拥有神兽的技能。
    """
#精确模式
# mode1=jieba.lcut(data)
# #全模式
# mode2=jieba.lcut(data,cut_all=True)

# #搜索引擎模式
# mode3=jieba.lcut_for_search(data)

# print(mode1)
# print("\n")
# print(mode2)
# print("\n")
# print(mode3)

data="幽默的司徒小生是男生"

#新增词语
jieba.add_word("司徒小生")

mode1=jieba.lcut(data)
print(mode1)
