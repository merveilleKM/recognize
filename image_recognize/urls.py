from django.urls import path
from . import views

app_name = 'image_recognize'

urlpatterns = [
    path('index', views.index, name='index'),
    path('recognize/', views.recognize_image, name='recognize_image'),
    path('result/<int:image_id>/', views.result, name='result'),
]