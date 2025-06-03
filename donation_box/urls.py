from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('1/', views.index_1, name='index_1'),
    path('2/', views.index_2, name='index_2'),
    path('3/', views.index_3, name='index_3'),
    path('4/', views.index_4, name='index_4'),
    path('api/', views.data_api, name="data_api")
]