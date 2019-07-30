from django.conf.urls import url
from django.urls import path
from .views import ListVideo

urlpatterns = [
    url('/', ListVideo.as_view()),
    
]

