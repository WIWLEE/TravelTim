from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def get_kth_area_tourist_spot_page(k, keyword, typeId) :
    now = time.strftime("%Y%m%d")
    print("현재 날짜 ", now)

    url = "https://apis.data.go.kr/B551011/EngService1/{}?serviceKey=R%2FfgdLzta7AkEc%2FYqk87JKFK9FUmhQG%2Fq%2BZAYS%2FMi8x1osYGN1H%2BI0ykuB%2BV4%2FfCr3A81KMGobYXBiDkrFt3Nw%3D%3D".format("searchKeyword1")
    params = {
        "keyword" : keyword,
        "numOfRows": k*5+5,
        "pageNo": 1,
        "MobileOS": "AND",
        "MobileApp": "appName",
        "contentTypeId" : typeId,
    }
    response = requests.get(url, params = params)
    dic = xmltodict.parse(response.content)
    print(dic)
    title_list = []
    image_list = []
    tel_list = []
    addr_list = []
    if dic['response']['body']['totalCount'] != '0' :
        for idx, item in enumerate(dic['response']['body']['items']['item']):
            title_list.append(item['title'])
            image_list.append(item['firstimage'])
            tel_list.append(item['tel'])
            addr_list.append(item['addr1'])
            print(idx)
        main_title = "List of {} tourist spots".format(keyword)
        data_send = card2(main_title, title_list[5*k:5*k+5], image_list[5*k:5*k+5], tel_list[5*k:5*k+5], addr_list[5*k:5*k+5])
        print(data_send)
    else :
        data_send = text_response("These is no current festival in this area")

    return data_send

def area_tourist_spot():
    content = request.get_json()
    content = content['userRequest']['utterance']

    keyword_list = ["seoul", "busan", "gyeongsangnamdo", "gyeongsangbukdo", "chungnam", "chungbuk", "deajeon", "daegu", "pohang", "yeosu", "jeju", "jeonju", "gwangju", "suwon", "incheon"]
    keyword_list += ["Seoul", "Busan", "Gyeongsangnamdo", "Gyeongsangbukdo", "Chungnam", "Chungbuk", "Deajeon", "Daegu", "Pohang", "Yeosu", "Jeju", "Jeonju", "Gwangju", "Suwon", "Incheon"]
    for idx, keyword in enumerate(keyword_list):
        print(keyword)
        if keyword in content and (u"more" in content or u"other" in content):
            data_send = get_kth_area_tourist_spot_page(1, keyword, 76)
            return data_send
        elif keyword in content :
            data_send = get_kth_area_tourist_spot_page(0, keyword, 76)
            return data_send
    data_send = text_response("Can you give me more specific regions that you want to know?")
    return jsonify(data_send)
           