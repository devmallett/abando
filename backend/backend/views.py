from django.shortcuts import render
import requests 


def index(request):
    return render(request ,'index.html')




def home(request):
    response=requests.get('https://api.covid19api.com/countries')
    return render(request)

# https://api.covid19api.com/countries