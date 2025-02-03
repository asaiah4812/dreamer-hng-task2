from django.urls import path
from . import views

urlpatterns = [
    path('classify-number', views.my_data, name='classify-number')
]
