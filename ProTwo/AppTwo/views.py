from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import UsersRecord

# Create your views here.


def index(request):
    return render(request,'new_app/index.html')

def users(request):
    #the order is optional
    users_list = UsersRecord.objects.order_by('name')
    users_dict = {'users_records': users_list}
    return render(request,'new_app/users.html', context = users_dict)
