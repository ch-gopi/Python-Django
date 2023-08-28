#This is my views.py file
from django.shortcuts import render


def home(request):
    import json
    import requests
    api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=fdd6f6b779b24469970122029232808&q=hyderabad&aqi=no")
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api= "Error"

    return render(request,'home.html', {'api':api} )
def about(request):
    return render(request,'about.html', {} )

