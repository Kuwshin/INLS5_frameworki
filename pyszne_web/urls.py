
from django.urls import path
from pyszne_web.views import articles, index

urlpatterns = [
    path('index/', index, name='index'),
]
