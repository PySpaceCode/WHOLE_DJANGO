
from multiprocessing import context
from django.urls import path
from .views import *
urlpatterns = [
    path('cal/',cal_view),
]
