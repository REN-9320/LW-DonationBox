from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.
def index_1(request):
    return render(request, "donation_box/index_1.html")

def index_2(request):
    return render(request, "donation_box/index_2.html")

def index_3(request):
    return render(request, "donation_box/index_3.html")

def index_4(request):
    return render(request, "donation_box/index_4.html")


prev_datetime = 0000000000

def data_api(request):
    global prev_datetime
    
    url = 'https://5oaj55b1vk.execute-api.ap-northeast-1.amazonaws.com/prod/payforword-prod-getdonationInfoNow'
    headers = {
    'Content-Type': 'application/json',
    'X-API-KEY': "56SD7Ozka82xBbOlrwoGN80RL1Azg2iP60WKyw5n"
    }   
    payload = {'prev_datetime': prev_datetime}
    
    response = requests.post(url, headers=headers, json=payload)
    
    raw_data = response.json()
    response_data = []
    if raw_data["status"] == "1":
        prev_datetime = raw_data["datetime"]
        donation_boxes = raw_data["donation_boxes"]
        if donation_boxes:
            for box in donation_boxes:
                response_data.append(box["d"])
        return JsonResponse(response_data, safe=False)
