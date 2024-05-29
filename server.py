from flask import Flask, request, jsonify
import requests
import xmltodict
import time
from template import get_map_url
from PyKakao import Local
from global_festival import festival
from korea_introduce import korea_introduce
from area_tourist_spot import area_tourist_spot
from area_festival import area_festival
from area_accommodate import area_accommodate
from area_restaurant import area_restaurant
from area_shopping import area_shopping
from area_introduce import area_introduce
from user_manual import user_manual
from customer_support import customer_support
from template import card
from template import text_response

tempimage = "http://tong.visitkorea.or.kr/cms/resource/05/2689905_image2_1.png"

app = Flask(__name__)


#기본 쿼리
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

    if content == u"안녕":
        data_send = text_response("안녕하세요")
    elif content == u"도움말":
        data_send = text_response("도움말입니다")
    elif content == u"festival":
        data_send = text_response("Here are some festivals I would recommend!")
    else:
        data_send = text_response("이해할 수 없는 메시지입니다")
    return jsonify(data_send)

#festival query
@app.route('/festival', methods=['POST'])
def handle_festival():
    return festival()

#area_tourist_spot query
@app.route('/areatouristspot', methods=['POST'])
def handle_areatouristspot():
    return area_tourist_spot()

#area_festival_query
@app.route('/areafestival', methods=['POST'])
def handle_areafestival():
    return area_festival()


#area_accommodate_query
@app.route('/areaaccommodate', methods=['POST'])
def handle_areaaccommodatel():
    return area_accommodate()

#area_restaurant_query
@app.route('/arearestaurant', methods=['POST'])
def handle_arearestaurant():
    return area_restaurant()

#area_shopping_query
@app.route('/areashopping', methods=['POST'])
def handle_arearshopping():
    return area_shopping()

#area_introduce_query
@app.route('/areaintroduce', methods=['POST'])
def handle_arearintroduce():
    return area_introduce()

#korea_introduce_query
@app.route('/koreaintroduce', methods=['POST'])
def handle_koreaintroduce():
    return korea_introduce()

#global_accommodate_query
@app.route('/globalaccommodate', methods=['POST'])
def handle_globalaccommodate():
    return global_accommodate()

#user_manual
@app.route('/usermanual', methods=['POST'])
def handle_usermanual():
    return user_manual()

#customer support
@app.route('/customersupport', methods=['POST'])
def handle_customersupport():
    return customer_support()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
