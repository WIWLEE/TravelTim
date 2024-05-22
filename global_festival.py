from flask import request, jsonify
import requests
import xmltodict
import time
from template import card
from template import text_response

def get_kth_festival_page(k) :
    now = time.strftime("%Y%m%d")
    print("현재 날짜 ", now)

    url = "https://apis.data.go.kr/B551011/EngService1/{}?serviceKey=R%2FfgdLzta7AkEc%2FYqk87JKFK9FUmhQG%2Fq%2BZAYS%2FMi8x1osYGN1H%2BI0ykuB%2BV4%2FfCr3A81KMGobYXBiDkrFt3Nw%3D%3D".format("searchFestival1")
    params = {
        "numOfRows": k*5+5,
        "pageNo": 1,
        "MobileOS": "AND",
        "MobileApp": "appName",
        "eventStartDate": now
    }
    response = requests.get(url, params = params)
    dic = xmltodict.parse(response.content)
    title_list = []
    image_list = []
    date_list = []
    addr_list = []
    for idx, item in enumerate(dic['response']['body']['items']['item']):
        title_list.append(item['title'])
        image_list.append(item['firstimage'])
        date_list.append(item['eventstartdate'])
        addr_list.append(item['addr1'])
        print(idx)
    data_send = card(title_list[5*k:5*k+5], image_list[5*k:5*k+5], date_list[5*k:5*k+5], addr_list[5*k:5*k+5])
    print(data_send)

    return data_send


def festival():
    content = request.get_json()
    content = content['userRequest']['utterance']

    if (u"event" in content or u"festival" in content) and (u"more" in content or u"other"in content) :
        data_send = get_kth_festival_page(1)
        return data_send
    if u"event" in content or u"festival" in content:
        data_send = get_kth_festival_page(0)
        return data_send
    else:
        data_send = text_response("Sorry, I don't know what you mean")
        return jsonify(data_send)