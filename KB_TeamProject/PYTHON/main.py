import EMOTION
import TITLE
from flask import Flask, request, jsonify
import random
import requests
import THUMBNAIL

application = Flask(__name__)

myreq1 = None
myreq2 = None
emo = EMOTION.EMOTION()
tit = TITLE.TITLE()
thu = THUMBNAIL.THUMBNAIL()


@application.route("/hello", methods=["POST"])
def handle_request1():
    global myreq1
    req = request.get_json()
    print(req["userRequest"]["utterance"])
    myreq1 = req["userRequest"]["utterance"]

    if request.path == "/hello":
        message_text = "오늘은 어떤 음악을 들으실 건가요?"
        quick_replies = [
            {"messageText": "힙합", "action": "message", "label": "힙합"},
            {"messageText": "아이돌", "action": "message", "label": "아이돌"},
            {"messageText": "인디", "action": "message", "label": "인디"},
            {"messageText": "발라드", "action": "message", "label": "발라드"},
            {"messageText": "검색할래", "action": "message", "label": "직접입력으로 검색하기"}
        ]
        # else:
        #     return None

        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": message_text
                        }
                    }
                ],
                "quickReplies": quick_replies
            }
        }
        return jsonify(res)
    else:
        return jsonify({"error": "Invalid request path"})
    
@application.route("/searching",methods=["POST"])
def seachingtap():
    req = request.get_json()
    myreq = req["userRequest"]["utterance"]
    
    res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "검색어를 입력하세요."
                        }
                    }
                ]
            }
    }
    return jsonify(res)

@application.route("/youtube", methods=["POST"])
def youtube_search():
    req = request.get_json()
    search_query = req["userRequest"]["utterance"]
    search_query = '/youtube ' + search_query 
    if search_query.startswith('/youtube '):
        search_term = search_query.replace('/youtube ', '')
        youtube_api_key = 'AIzaSyCMcHB5M_2ywcz44iob-cTniG3iHkk_low'
        try:
            response = requests.get('https://www.googleapis.com/youtube/v3/search', params={
                'part': 'snippet',
                'q': search_term,
                'key': youtube_api_key
            })
            search_results = response.json()['items']
            if search_results:
                cards = []
                for item in search_results:
                    video_title = item['snippet']['title'].replace('&quot;','"')
                    video_thumbnail = item['snippet']['thumbnails']['default']['url']
                    video_id = item['id']['videoId']

                    card = {
                        'title': video_title,
                        'description': 'YouTube Video',
                        #'thumbnail': {
                        'imageUrl': video_thumbnail,
                        #},
                        'link': {
                            'web': f'https://www.youtube.com/watch?v={video_id}'
                        }
                    }
                    cards.append(card)

                res = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "listCard": {
                                    "header": {
                                        "title": f"\"{search_term}\" 검색 결과"
                                    },
                                    "items": cards
                                }
                            }
                        ]
                    }
                }
                print(res)
                #res = res.replace('&quot;','"')
                return jsonify(res)
            else:
                return jsonify({'message': '검색 결과가 없습니다.'})
        except Exception as e:
            print('검색엔진 호출 중 오류:', e)
            return jsonify({'message': '검색엔진 호출 중 오류가 발생했습니다.'}), 500

    return jsonify({'message': ''})

@application.route("/category", methods=["POST"])
def handle_request2():
    global myreq2
    req = request.get_json()
    print(req["userRequest"]["utterance"])
    myreq2 = req["userRequest"]["utterance"]

    if request.path == "/category":
        message_text = "오늘의 기분은 어떠신가요?"
        quick_replies = [
            {"messageText": "기쁨", "action": "message", "label": "기쁨"},
            {"messageText": "슬픔", "action": "message", "label": "슬픔"},
            {"messageText": "분노", "action": "message", "label": "분노"},
            {"messageText": "불안", "action": "message", "label": "불안"},
            {"messageText": "심심", "action": "message", "label": "심심"}
        ]
        # else:
        #     return None

        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": message_text
                        }
                    }
                ],
                "quickReplies": quick_replies
            }
        }
        return jsonify(res)
    else:
        return jsonify({"error": "Invalid request path"})

@application.route("/wm", methods=["POST"])
def handle_request3():
    global myreq1
    global myreq2
    req = request.get_json()
    print(req["userRequest"]["utterance"])
    myreq = req["userRequest"]["utterance"]
    rn = random.randint(0, 4)
    if myreq2 == '인디':
        if myreq == '기쁨':
            getUrl = emo.indiJoy(rn)
            getTitle = tit.indiJoy(rn)
            getImage = thu.indiJoy(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
                                
            return jsonify(res)
        elif myreq == '슬픔':
            getUrl = emo.indiSad(rn)
            getTitle = tit.indiSad(rn)
            getImage = thu.indiSad(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '분노':
            getUrl = emo.indiAnger(rn)
            getTitle = tit.indiAnger(rn)
            getImage = thu.indiAnger(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '불안':
            getUrl = emo.indiUnrest(rn)
            getTitle = tit.indiUnrest(rn)
            getImage = thu.indiUnrest(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '심심':
            getUrl = emo.indiBoring(rn)
            getTitle = tit.indiBoring(rn)
            getImage = thu.indiBoring(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
    if myreq2 == '아이돌':
        if myreq == '기쁨':
            getUrl = emo.idolJoy(rn)
            getTitle = tit.idolJoy(rn)
            getImage = thu.idolJoy(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '슬픔':
            getUrl = emo.idolSad(rn)
            getTitle = tit.idolSad(rn)
            getImage = thu.idolSad(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '분노':
            getUrl = emo.idolAnger(rn)
            getTitle = tit.idolAnger(rn)
            getImage = thu.idolAnger(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '불안':
            getUrl = emo.idolUnrest(rn)
            getTitle = tit.idolUnrest(rn)
            getImage = thu.idolUnrest(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '심심':
            getUrl = emo.idolBoring(rn)
            getTitle = tit.idolBoring(rn)
            getImage = thu.idolBoring(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        
    if myreq2 == '힙합':
        if myreq == '기쁨':
            getUrl = emo.hipJoy(rn)
            getTitle = tit.hipJoy(rn)
            getImage = thu.hipJoy(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '슬픔':
            getUrl = emo.hipSad(rn)
            getTitle = tit.hipSad(rn)
            getImage = thu.hipSad(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '분노':
            getUrl = emo.hipAnger(rn)
            getTitle = tit.hipAnger(rn)
            getImage = thu.hipAnger(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '불안':
            getUrl = emo.hipUnrest(rn)
            getTitle = tit.hipUnrest(rn)
            getImage = thu.hipUnrest(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '심심':
            getUrl = emo.hipBoring(rn)
            getTitle = tit.hipBoring(rn)
            getImage = thu.hipBoring(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
    if myreq2 == '발라드':
        if myreq == '기쁨':
            getUrl = emo.balJoy(rn)
            getTitle = tit.balJoy(rn)
            getImage = thu.balJoy(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '슬픔':
            getUrl = emo.balSad(rn)
            getTitle = tit.balSad(rn)
            getImage = thu.balSad(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '분노':
            getUrl = emo.balAnger(rn)
            getTitle = tit.balAnger(rn)
            getImage = thu.balAnger(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '불안':
            getUrl = emo.balUnrest(rn)
            getTitle = tit.balUnrest(rn)
            getImage = thu.balUnrest(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        elif myreq == '심심':
            getUrl = emo.balBoring(rn)
            getTitle = tit.balBoring(rn)
            getImage = thu.balBoring(rn)
            res = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            'basicCard': {
                                'title': '이 노래는 어떠세요?',
                                'description': getTitle,
                                'thumbnail': {
                                    'imageUrl': getImage
                                },
                                'buttons': [
                                    {
                                        'action': 'webLink',
                                        'label': '들어보기',
                                        'webLinkUrl': getUrl
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
            return jsonify(res)
        
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
