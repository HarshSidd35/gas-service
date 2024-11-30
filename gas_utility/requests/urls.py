from django.urls import path
from . import views

urlpatterns = [
    path('request/new/', views.request_form, name='request_form'),
    path('requests/', views.request_list, name='request_list'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
]