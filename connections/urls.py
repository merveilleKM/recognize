from django.urls import path
from . import views


urlpatterns = [
    path('', views.connection, name='connection'),
    path('inscription', views.inscription, name='inscription'),
    path('deconnection', views.deconnection, name='deconnection'),
]
