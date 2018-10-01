from django.urls import path, include, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(), name='list'),
    re_path('(?P<pk>\d+)/',views.SchoolDetailView.as_view(), name = 'detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.SchoolDeleteView.as_view(),name='delete'),
]
