from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'msg':"Blog Engine Developed By xHacker404"}
    return render(request, 'blog/index.html', context=my_dict)
