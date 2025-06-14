from django.shortcuts import render
import requests
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is the home page.")

def index_1(request):
    return render(request, "donation_box/index_1.html")

def index_2(request):
    return render(request, "donation_box/index_2.html")

def index_3(request):
    return render(request, "donation_box/index_3.html")

def index_4(request):
    return render(request, "donation_box/index_4.html")

@csrf_exempt
def data_api(request):
    body = json.loads(request.body)
    prev_datetime = body.get("prev_datetime", "0000000000")  # フロントエンドから取得

    url = 'https://5oaj55b1vk.execute-api.ap-northeast-1.amazonaws.com/prod/payforword-prod-getdonationInfoNow'
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': "56SD7Ozka82xBbOlrwoGN80RL1Azg2iP60WKyw5n"
    }

    payload = {'prev_datetime': prev_datetime}
    response = requests.post(url, headers=headers, json=payload)
    raw_data = response.json()
    print(raw_data)
    response_data = []

    if raw_data["status"] == "1":
        new_datetime = raw_data["datetime"]
        mode = raw_data["mode"]
        donation_boxes = raw_data["donation_boxes"]
        if donation_boxes:
            for box in donation_boxes:
                response_data.append(box["d"])
        return JsonResponse({
            "response_data": response_data,
            "mode": mode,
            "datetime": new_datetime  # クライアントに返す
        })
    
    return JsonResponse({"response_data": [], "mode": "", "datetime": prev_datetime})
