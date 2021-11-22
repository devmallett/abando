from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request handler 
#an action

def say_hello(request):
    # return HttpResponse('Wazzzz Up')
    return render(request ,"hello.html")