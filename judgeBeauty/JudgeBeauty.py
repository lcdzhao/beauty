import requests
import base64
import json


token = "24.e7ff176af8a174ac8904e3ceab778248.2592000.1570343540.282335-17181119"

def get_request_url():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    request_url = request_url + "?access_token=" + token
    return request_url

def get_img_base(filepath):
    with open(filepath,'rb') as fp:
        content = base64.b64encode(fp.read())
        return content




def get_gender_beauty_by_img_path(filePath):
    params = {
        'image':get_img_base(filePath),
        'image_type':'BASE64',
        'face_field':'age,beauty,gender'
    }

    res = requests.post(get_request_url(),data=params)
    result = res.text
    result = json.loads(result)
    sex_and_beauty = {}
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
