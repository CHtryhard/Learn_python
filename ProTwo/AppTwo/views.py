from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<em> My Second App </em>')

def help(request):
    my_dict = {'insert1':"hello This is the Help page"}
    return render(request,'new_app/help.html', context = my_dict)
