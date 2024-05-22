from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def korea_introduce():
    content = request.get_json()
    content = content['userRequest']['utterance']

    if 'introduce' in content :
        data_send = text_response("Welcome to South Korea, a dynamic destination where ancient traditions meet cutting-edge modernity. South Korea offers something for every traveler, from bustling urban landscapes to tranquil rural settings and everything in between.")
        data_send['template']['outputs'][0]['simpleText']['text'] += "\n\n"
        data_send['template']['outputs'][0]['simpleText']['text'] += "Seoul: Start your journey in Seoul, the heart of South Korea, where skyscrapers and K-pop culture blend seamlessly with historic sites like Gyeongbokgung Palace and Bukchon Hanok Village. Be sure to visit the lively districts of Hongdae for its youth culture and Itaewon for international cuisine and nightlife. Don't miss the chance to shop in Myeongdong or take a peaceful walk along the Cheonggyecheon stream."
        data_send['template']['outputs'][0]['simpleText']['text'] += "\n\n"
        data_send['template']['outputs'][0]['simpleText']['text'] += "Busan: Head to the coastal city of Busan, known for its beautiful beaches, the bustling Jagalchi Fish Market, and the scenic Taejongdae Resort Park. Enjoy fresh seafood and relax at Haeundae Beach, or soak in the panoramic city views from the Busan Tower in Yongdusan Park."
        data_send['template']['outputs'][0]['simpleText']['text'] += "\n\n"
        data_send['template']['outputs'][0]['simpleText']['text'] += "Jeju Island: A UNESCO World Heritage site wonders such as the Hallasan Mountain, a dormant volcano and the highest peak in South Korea, and the mysterious lava tubes. The island's picturesque waterfalls and beaches, like Jungmun and Hamdeok, make it a perfect spot for relaxation and exploration. Don’t miss the unique cultural experience of watching the Haenyeo, female divers, skillfully gathering seafood without using breathing equipment."
        data_send['template']['outputs'][0]['simpleText']['text'] += "\n\n"
        return jsonify(data_send)
        
    data_send = text_response("Sorry, I don't know what you mean")
    return jsonify(data_send)
