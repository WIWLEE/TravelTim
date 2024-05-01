from flask import Flask, request, jsonify
import requests
import xmltodict
import time
from template import get_map_url
from PyKakao import Local
from festival import festival
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
