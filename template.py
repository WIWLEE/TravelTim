import requests

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

def card(title_list, image_list, date_list, addr_list):
    
    items = []
    for idx in range(len(title_list)):
        title = title_list[idx]
        date = date_list[idx]
        location = addr_list[idx]
        item = {
            "title": title,
            "description": f"Date: {date[0:4]}/{date[4:6]}/{date[6:8]}",
            #"description2": f"address : {location}",
            "imageUrl": image_list[idx] if len(image_list) != 0 else tempimage,
            "link" : {
                "web" : "https://map.naver.com/search?query={}".format(location)
            }
        }
        items.append(item)

    # # 좌표
    # latitude = 37.5665
    # longitude = 126.9780

    # # 좌표를 이용하여 카카오맵 URL 가져오기
    # map_url = get_map_url(latitude, longitude)
    # print("카카오맵 URL:", map_url)

    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText" : {
                        "text" :"Here's the list for your request."
                    }
                },
                {
                    "listCard": {
                        "header": {
                            "title": "List of Festivals and Events"
                        },
                        "items": items,
                    },
                },
                {
                    "simpleText" : {
                        "text" : "If you want to know more informations, please let me know."
                    }
                }
            ]
        }
    }

def get_map_url(latitude, longitude):
    # 카카오맵 API 호출을 위한 URL
    api_url = f"https://dapi.kakao.com/v2/local/geo/coord2address.json?x={longitude}&y={latitude}"

    # 카카오맵 API 호출을 위한 헤더
    headers = {
        "Authorization": 'KakaoAK ' + "cb70afa7a953415d3cbba6eb70f892dd"  # 여기에 카카오 REST API 키를 입력하세요
    }

    # API 호출
    response = requests.get(api_url, headers=headers)
    data = response.json()['documents']['place_url']
    print(data)
