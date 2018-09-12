from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import UsersRecord
from AppTwo import forms

# Create your views here.

def index(request):
    return render(request,'new_app/index.html')

def users(request):
    form = forms.MyForm()

    if request.method == 'POST':
        form = forms.MyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error from form')
    return render(request,'new_app/users.html',{'form':form})
