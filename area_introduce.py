from flask import request, jsonify
import requests
import xmltodict
import time
from template import card,card2
from template import text_response

def area_introduce():
    content = request.get_json()
    content = content['userRequest']['utterance']

    keyword_list = ["seoul", "busan", "gyeongsangnamdo", "gyeongsangbukdo", "chungnam", "chungbuk", "daejeon", "daegu", "pohang", "yeosu", "jeju", "jeonju", "gwangju", "suwon", "incheon"]
    keyword_list += ["Seoul", "Busan", "Gyeongsangnamdo", "Gyeongsangbukdo", "Chungnam", "Chungbuk", "Daejeon", "Daegu", "Pohang", "Yeosu", "Jeju", "Jeonju", "Gwangju", "Suwon", "Incheon"]
    if 'introduce' in content :
        for idx, keyword in enumerate(keyword_list):
            print(keyword)
            if keyword in content :
                if keyword == "seoul" or  keyword =="Seoul":
                    data_send = text_response("As the vibrant capital of South Korea, Seoul is a bustling metropolis that blends traditional charm with cutting-edge technology. Tourists can explore ancient palaces like Gyeongbokgung and Changdeokgung, visit unique neighborhoods like Insadong for traditional crafts, or experience the modern shopping mecca of Myeongdong. The city's night markets and Korean BBQ joints offer unforgettable culinary experiences.")
                elif keyword == "incheon" or  keyword =="Incheon":
                    data_send = text_response("Known as the gateway to Korea, Incheon boasts a rich history and modern attractions. The city is famous for its Chinatown, the only official Chinatown in Korea, and Wolmido Island, known for its amusement park and seaside views. Incheon is also home to the Incheon International Airport, making it the first stop for many international visitors.")
                elif keyword == "gwangju" or  keyword =="Gwangju":
                    data_send = text_response("Gwangju is the cultural hub of South Korea's southwestern region. It is celebrated for its rich artistic heritage and democratic uprising history. The Gwangju Biennale, a large arts festival, attracts international artists and tourists alike. Food lovers enjoy Gwangju for its famous cuisine, particularly its spicy and hearty dishes.")
                elif keyword == "suwon" or  keyword =="Suwon":
                    data_send = text_response("Just south of Seoul, Suwon is famous for its well-preserved Hwaseong Fortress, a UNESCO World Heritage site. Visitors can walk along the ancient walls for panoramic views of the city. Suwon is also known for its lively chicken street, where you can try Korean fried chicken paired with beer.")
                elif keyword == "jeonju" or  keyword =="Jeonju":
                    data_send = text_response("Jeonju is considered the birthplace of the Korean food bibimbap and is central to Korean culture and traditions. The Jeonju Hanok Village, with its traditional Korean houses, offers visitors a glimpse into Korea's past. The city also hosts various cultural festivals that celebrate its heritage and cuisine.")
                elif keyword == "jeju" or  keyword =="Jeju":
                    data_send = text_response("Jeju Island is a volcanic island known for its scenic natural beauty, including Hallasan Mountain, waterfalls, and unique volcanic cones. Beaches like Hamdeok and Hyeopjae offer stunning seaside relaxation. Jeju is also famous for its female divers, known as Haenyeo, and its unique island cuisine.")
                elif keyword == "yeosu" or  keyword =="Yeosu":
                    data_send = text_response("Located on the southern coast of Korea, Yeosu is famous for its beautiful coastal scenery and historic sites. Highlights include the Yeosu Ocean Expo Park and romantic sunset views from Dolsan Bridge. The city's seafood is a must-try, especially during the Yeosu Night Sea Festival.")
                elif keyword == "pohang" or  keyword =="Pohang":
                    data_send = text_response("A coastal city in the eastern part of Korea, Pohang is known for its steel industry and beautiful beaches. The city's Homigot Sunrise Plaza features a famous large hand sculpture emerging from the sea. Pohang is also a great spot for seafood lovers.")
                elif keyword == "daegu" or  keyword =="Daegu":
                    data_send = text_response("Nestled in the mountains of southeastern Korea, Daegu is known for its fashion industry and hot springs. The city offers numerous cultural sights, such as the Daegu Art Museum and the traditional Yangnyeongsi Medicine Market. The annual Daegu International Bodypainting Festival is a unique and colorful event.")
                elif keyword == "chungbuk" or  keyword =="Chungbuk":
                    data_send = text_response("This inland province is known for its mountainous terrain and numerous national parks, which offer great hiking opportunities. The city of Cheongju, the capital, hosts the annual Craft Biennale.")
                elif keyword == "chungnam" or  keyword =="Chungnam":
                    data_send = text_response("The province is known for its fertile plains and historical sites. Daecheon Beach, famous for the Boryeong Mud Festival, is a popular attraction. The region is also home to Buyeo and Gongju, ancient capitals of the Baekje Kingdom.")
                elif keyword == "busan" or  keyword =="Busan":
                    data_send = text_response("South Korea’s second-largest city, located on the southeastern coast, is famous for its beaches, mountains, and temples. Tourists flock to Haeundae Beach for its festive atmosphere and to Jagalchi Fish Market for fresh seafood. The Busan International Film Festival is a major annual event here.")
                elif keyword == "gyeongsangbukdo" or  keyword == "Gyeongsangbukdo":
                    data_send = text_response("This province is rich in historical and cultural heritage, featuring sites like Bulguksa Temple and Seokguram Grotto in Gyeongju. The region's rugged landscape also makes it ideal for outdoor activities.")
                elif keyword == "gyeongsangnamdo" or  keyword == "Gyeongsangnamdo":
                    data_send = text_response("Known for its coastal cities like Tongyeong and Geoje, the province offers stunning coastal views and maritime activities. The region's history is celebrated in the annual Jinju Lantern Festival.")
                return jsonify(data_send)


    if 'where' or 'location' in content :
        for idx, keyword in enumerate(keyword_list):
            if keyword in content :
                print(keyword)
                if keyword == "seoul" or keyword == "Seoul":
                    data_send = text_response("Located in the northwest part of South Korea, Seoul is the capital and largest city of the country, situated on the Han River. It's centrally positioned within easy reach of the surrounding Gyeonggi province and near the border with North Korea.")
                elif keyword == "incheon" or  keyword =="Incheon":
                    data_send = text_response("Incheon lies just to the west of Seoul, on the coast of the Yellow Sea. It forms part of the Seoul Metropolitan Area and is mainly known for its large international airport that serves as a gateway into Korea.")
                elif keyword == "gwangju" or  keyword == "Gwangju":
                    data_send = text_response("Gwangju is situated in the southwestern part of South Korea. It is the largest city in the Jeollanam-do province and acts as one of the main economic and cultural centers of the southern region.")
                elif keyword == "suwon" or  keyword =="Suwon":
                    data_send = text_response("Suwon is located just south of Seoul, in the northern part of the Gyeonggi province. It is easily accessible from the capital by subway, making it a popular destination for day trips.")
                elif keyword == "jeonju" or keyword == "Jeonju" or "not jeju" in content:
                    data_send = text_response("This city lies in the western part of South Korea, serving as the capital of the Jeollabuk-do province. It's well-known for its historical buildings and food culture, and it's roughly in the middle between Seoul and Gwangju.")
                elif keyword == "jeju" or  keyword =="Jeju" or "not jeonju" in content:
                    data_send = text_response("Jeju Island is located off the southern coast of South Korea. It's a large volcanic island, famous for its unique landscapes and mild climate, set apart from the mainland")
                elif keyword == "yeosu" or  keyword =="Yeosu":
                    data_send = text_response("Situated on the southern coast of the Korean Peninsula, Yeosu is part of the Jeollanam-do province. It's known for its beautiful coastal scenery and historic maritime role.")
                elif keyword == "pohang" or  keyword =="Pohang":
                    data_send = text_response("Located on the east coast of South Korea, Pohang is part of the Gyeongsangbuk-do province. It faces the East Sea (Sea of Japan) and is primarily known for its steel industry and seafood.")
                elif keyword == "daegu" or  keyword =="Daegu":
                    data_send = text_response("Daegu sits in the southeastern part of South Korea, nestled in a valley with surrounding mountains. It's the fourth largest city in South Korea and serves as the capital of the Gyeongsangbuk-do province.")
                elif keyword == "chungbuk" or  keyword =="Chungbuk":
                    data_send = text_response("This inland province is located in the center of South Korea. It's surrounded by Gyeonggi Province to the west, Gangwon Province to the north, and Gyeongsangbuk-do to the east.")
                elif keyword == "chungnam" or  keyword =="Chungnam":
                    data_send = text_response("Located just south of the Seoul Metropolitan Area, this province stretches from the west coast facing the Yellow Sea to the central part of the peninsula.")
                elif keyword == "busan" or  keyword =="Busan":
                    data_send = text_response("As the second-largest city in South Korea, Busan is located on the southeastern tip of the peninsula, facing the Korea Strait. It's known for its beaches, bustling port, and vibrant urban life.")
                elif keyword == "gyeongsangbukdo" or  keyword =="Gyeongsangbukdo":
                    data_send = text_response("Located in the southeastern part of the country, this province includes the cities of Daegu and Pohang. It is bordered by the East Sea and has a rugged terrain with numerous cultural sites.")
                elif keyword == "gyeongsangnamdo" or  keyword =="Gyeongsangnamdo":
                    data_send = text_response("Positioned further south of Gyeongsangbuk-do, it stretches from the southeastern coast to the southern parts of the peninsula. The region includes the major industrial city of Busan.")
                
                print(data_send)
                return jsonify(data_send)
                
    data_send = text_response("Sorry, I don't know what you mean")
    return jsonify(data_send)
           