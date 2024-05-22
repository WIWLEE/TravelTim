from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def get_kth_area_shopping_page(k, keyword, typeId) :
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
    title_list = []
    image_list = []
    tel_list = []
    addr_list = []
    if dic['response']['body']['totalCount'] == '1' :
        item = dic['response']['body']['items']['item']
        print("한개임. 근데 왜 나눠야해?")
        title_list.append(item['title'])
        image_list.append(item['firstimage'])
        if str(type(item['tel'])) == "<class 'NoneType'>" :
            tel_list.append(item['tel'])
        else :
            tel_list.append(item['tel'].split('<br>')[0])
        addr_list.append(item['addr1'])
        main_title = "List of {} shopping".format(keyword)
        data_send = card2(main_title, title_list[5*k:5*k+5], image_list[5*k:5*k+5], tel_list[5*k:5*k+5], addr_list[5*k:5*k+5])
        print(data_send)
    elif dic['response']['body']['totalCount'] != '0' : 
        for idx, item in enumerate(dic['response']['body']['items']['item']):
            title_list.append(item['title'])
            image_list.append(item['firstimage'])
            if str(type(item['tel'])) == "<class 'NoneType'>" :
                tel_list.append(item['tel'])
            else :
                tel_list.append(item['tel'].split('<br>')[0])
            addr_list.append(item['addr1'])
        main_title = "List of {} shoppings".format(keyword)
        data_send = card2(main_title, title_list[5*k:5*k+5], image_list[5*k:5*k+5], tel_list[5*k:5*k+5], addr_list[5*k:5*k+5])
        print(data_send)
    else :
        data_send = text_response("I can't find any shopping mall using this keyword area")

    return data_send

def area_shopping():
    content = request.get_json()
    content = content['userRequest']['utterance']

    keyword_list = ["seoul", "busan", "gyeongsangnamdo", "gyeongsangbukdo", "chungnam", "chungbuk", "daejeon", "daegu", "pohang", "yeosu", "jeju", "jeonju", "gwangju", "suwon", "incheon"]
    keyword_list += ["Seoul", "Busan", "Gyeongsangnamdo", "Gyeongsangbukdo", "Chungnam", "Chungbuk", "Daejeon", "Daegu", "Pohang", "Yeosu", "Jeju", "Jeonju", "Gwangju", "Suwon", "Incheon"]
    if 'shopping' in content or 'event' in content :
        for idx, keyword in enumerate(keyword_list):
            print(keyword)
            if keyword in content and (u"more" in content or u"other" in content):
                data_send = get_kth_area_shopping_page(1, keyword, 79)
                return data_send
            elif keyword in content :
                data_send = get_kth_area_shopping_page(0, keyword, 79)
                return data_send
        data_send = text_response("Can you give me more specific regions that you want to know?")
        return jsonify(data_send)
    data_send = text_response("Sorry, I don't know what you mean")
    return jsonify(data_send)
           