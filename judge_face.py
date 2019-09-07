import requests
import base64
import json


token = "24.e7ff176af8a174ac8904e3ceab778248.2592000.1570343540.282335-17181119"

def get_request_url():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    request_url = request_url + "?access_token=" + token
    return request_url



def get_gender_beauty_by_img_path(url):
    params = {
        'image':url,
        'image_type':'URL',
        'face_field':'age,beauty,gender'
    }

    res = requests.post(get_request_url(),data=params)
    result = res.text
    result = json.loads(result)
    error_code = result['error_code']
    if error_code == 222202:
        return None
    try:
# 数据形式为{'face_num': 1,
# 'face_list': [{'face_token': '59ef0f1eec25475cfe4a9f9c8112db00',
# 'location': {'left': 4182.09, 'top': 1865.79, 'width': 1121, 'height': 994, 'rotation': 177},
# 'face_probability': 0.65,
# 'angle': {'yaw': 57.11, 'pitch': 12.35, 'roll': -182.51},
# 'age': 19,
# 'beauty': 39.94,
# gender': {'type': 'female', 'probability': 0.73}}]}

        return result['result']
    except KeyError:
        return None
    except TypeError:
        return None


#print(get_gender_beauty_by_img_path("D:/Entertainment Resources/Pictures/Wallpaper/1.jpg"))