from aip import AipFace
import base64
import datetime
import time
 
APP_ID = '17181119'
API_KEY = 'sMymC6r7FPylzxPUeDNRoECV'
SECRET_KEY = 'kpgZWsIPYVdb7Yes4wQuYx7WXdBiBBGv'
 
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
 
filePath = r'/home/lcdzhao/Downloads/fengjie.jpg'
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')
    


def get_gender_beauty_by_img_path(filePath):
    imageType = "BASE64"
    options = {}
    options["face_field"] = "age,gender,beauty"
    sex_and_beauty = {}
    result = aipFace.detect(get_file_content(filePath),imageType,options) 
    error_code = result['error_code']
    if error_code == 222202:
        return None
    try:
        sex_type = result['result']['face_list'][-1]['gender']['type']
        beauty = result['result']['face_list'][-1]['beauty']
        sex_and_beauty['sex'] = sex_type
        sex_and_beauty['beauty'] = beauty
        return sex_and_beauty
    except KeyError:
        return None
    except TypeError:
        return None



