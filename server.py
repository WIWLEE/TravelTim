from flask import Flask, request, jsonify
import requests
import xmltodict

app = Flask(__name__)

def text_response(text):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }

def card(title_list):
    items = []
    for idx, title in enumerate(title_list, start=1):
        item = {
            "title": title,
            "description": "축제에 대한 정보",
            "imageUrl": "https://store.stocksidekick.xyz/static/images/ryan.png",
            "link": {
                "web": "https://www.naver.com"
            }
        }
        items.append(item)

    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "축제 리스트"
                        },
                        "items": items,
                        "buttons": [
                            {
                                "label": "축제 자세히 보기",
                                "action": "webLink",
                                "webLinkUrl": "https://www.naver.com"
                            }
                        ]
                    }
                }
            ]
        }
    }


@app.route('/keyboard')
def keyboard():
    data_send = {
        "Subject": "OSSP",
        "user": "corona_chatbot"
    }
    return jsonify(data_send)

@app.route('/message', methods=['POST'])
def message():
    content = request.get_json()
    content = content['userRequest']['utterance']
    print(content)

    if content == u"안녕":
        data_send = text_response("안녕하세요")
    elif content == u"도움말":
        data_send = text_response("도움말입니다")
    elif content == u"festival":
        data_send = text_response("Here are some festivals I would recommend!")
    else:
        data_send = text_response("이해할 수 없는 메시지입니다")
    return jsonify(data_send)

@app.route('/festival', methods=['POST'])
def festival():
    content = request.get_json()
    content = content['userRequest']['utterance']
    print(content)

    if u"event" in content or u"festival" in content:
        url = "https://apis.data.go.kr/B551011/EngService1/searchFestival1?serviceKey=R%2FfgdLzta7AkEc%2FYqk87JKFK9FUmhQG%2Fq%2BZAYS%2FMi8x1osYGN1H%2BI0ykuB%2BV4%2FfCr3A81KMGobYXBiDkrFt3Nw%3D%3D&numOfRows=10&pageNo=1&MobileOS=AND&MobileApp=appName&eventStartDate=20210207"
        response = requests.get(url)
        dic = xmltodict.parse(response.content)
        title_list = []
        for item in dic['response']['body']['items']['item']:
            title_list.append(item['title'])
        data_send = card(title_list[0:5])
    else:
        data_send = text_response("이해할 수 없는 메시지입니다")
    
    return jsonify(data_send)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
