from django.conf.urls import url
from django.urls import path, re_path
from AppTwo import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
