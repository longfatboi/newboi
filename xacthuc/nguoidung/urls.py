from django.urls import path
from . import views
app_name = 'nguoidung'
urlpatterns = [
    path('', views.index),
]
