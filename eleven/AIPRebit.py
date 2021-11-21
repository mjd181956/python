import requests
from aip import AipOcr
import os
class Robot:
    #构造函数
    def __init__(self, name):
        self.name = name

    #重命名文件方法
    def rename(self, path):
        #获取所有文件名
        file_name=[]
        for root, dirs, files in os.walk(path):
            for f in files:
                file_name.append(f)
            
            pass

        #修改所有文件名
        count=0
        for i in file_name:
            count+=1
            #文件原名
            old_path=path+"\\"+i
            #文件新名
            new_path=path+"\\"+str(count)+".txt"
            os.rename(old_path,new_path)
    
    #图像识别方法
    def imgclassify(self,path):
        #你的 APPID AK SWCRET_KEY
        APP_ID = '25203439'
        API_KEY = 'FeRq59kZpMWOkWfkqD4EfC4O'
        SWCRET_KEY = 'frcmL5OsaKCAgFTojH8j15xytqETNI9G'
        client=AipOcr(APP_ID, API_KEY, SWCRET_KEY)

        #读取图片
        def get_file_content(filepath):
            with open(filepath,"rb") as fp:
                return fp.read()
        image=get_file_content(path)
        data=client.basicGeneral(image)
        data=data["result"][0]["keyword"]
        return data

    def speak(self,info):
        url="http://i.itpk.cn/api.php?question={}".format(info)
        response=requests.get(url).text
        return response

if __name__ == "__main__":
    name=input("请给你的机器人起个名字：")
    robot=Robot(name)
    name=name+":"
    while 1:
        info=input("OWN:")
        if info in "重命名文件":
            print(name+"请输入文件所在的目录路径")
            path=input("OWN:")
            robot.rename(path)
            print(name+"文件重命名成功")
        elif info in "图片识别：":
            print(name+"请输入图片的路径")
            path=input("OWN:")
            data=robot.imgclassify(path)
            print(name+"图片识别成功")
            print(name+"这是一个{}".format(data))
        else:
            data=robot.speak(info)
            print(name+data)
