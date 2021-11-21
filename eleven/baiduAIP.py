from aip  import AipOcr 
""" 你的 APPID AK SK """
APP_ID = '25203439'
API_KEY = 'FeRq59kZpMWOkWfkqD4EfC4O'
SWCRET_KEY = 'frcmL5OsaKCAgFTojH8j15xytqETNI9G'
client=AipOcr(APP_ID, API_KEY, SWCRET_KEY)

#读取图片
def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()

option={"detect_directions": True}
image=get_file_content(r"F:\python\eleven\玄幻小说.png")
data=client.basicGeneral(image,option)
print(data)