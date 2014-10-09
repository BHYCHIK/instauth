from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def redirect_view(request):
    html = '<html><head><title>hw</title></head><body><h1>HELLO!</h1></body></html>'
    return HttpResponse(html);
