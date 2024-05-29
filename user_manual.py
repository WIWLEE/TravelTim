from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def user_manual():

    data_send = text_response("Feel free to ask me anything at any time. Here's the examples of the questions you can ask. \n\n EX) Can you recommend some restaurants in Seoul? \n EX) Is there any festival in Pohang?")
    return jsonify(data_send)
