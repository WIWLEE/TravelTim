from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def area_introduce():
    content = request.get_json()
    content = content['userRequest']['utterance']

    keyword_list = ["seoul", "busan", "gyeongsangnamdo", "gyeongsangbukdo", "chungnam", "chungbuk", "deajeon", "daegu", "pohang", "yeosu", "jeju", "jeonju", "gwangju", "suwon", "incheon"]
    keyword_list += ["Seoul", "Busan", "Gyeongsangnamdo", "Gyeongsangbukdo", "Chungnam", "Chungbuk", "Deajeon", "Daegu", "Pohang", "Yeosu", "Jeju", "Jeonju", "Gwangju", "Suwon", "Incheon"]
    for idx, keyword in enumerate(keyword_list):
        print(keyword)
        if keyword in content :
            data_send = ""
            data_send = get_kth_area_tourist_spot_page(1, keyword, 76)
            return data_send
    data_send = text_response("Sorry, I don't know what you mean")
    return jsonify(data_send)
           