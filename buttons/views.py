import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def buttons(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['a', 'b', 'c', 'd'],
    })


@csrf_exempt
def message(request):
    json_str = request.body.decode('utf-8')
    json_data = json.loads(json_str)
    selected = json_data['content']

    return JsonResponse({
        "message": {
            "text": "네 놈이 선택한 값은 {}입니다!!".format(selected)
        },
        "keyboard": {
            "type": "buttons",
            "buttons": ['a', 'b', 'c', 'd'],
        }
    })
