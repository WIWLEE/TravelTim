from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def customer_support():

    data_send = text_response("If you wish to speak with a customer service representative, please contact with below user ID. \n\n io0818")
    return jsonify(data_send)
