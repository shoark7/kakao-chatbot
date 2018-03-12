import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apis.dict_apis import dict_search


def buttons(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['영어사전', '케이블 영화채널 시간표'],
    })


@csrf_exempt
def message(request):
    json_str = request.body.decode('utf-8')
    json_data = json.loads(json_str)
    selected = json_data['content']
    res_text = "영어 -> 한글, 한글 -> 영어를 지원합니다.\n없는 단어이거나 잘못 입력하면 결과가 없을 수도 있습니다."

    if selected == '영어사전':
        return JsonResponse({
            'type': 'text',
            'message': res_text,
        })

    elif selected == '케이블 영화채널 시간표':
        return JsonResponse({
            "message": {
                "text": "네 놈이 선택한 값은 {}입니다!!".format(selected)
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ['a', 'b', 'c', 'd'],
            }
        })
    else:
        search_result = dict_search(selected)
        print(search_result)
        return JsonResponse({
            'type': 'text',
            'message': {
                "text": search_result + '\n by dict search',
            }
        })
