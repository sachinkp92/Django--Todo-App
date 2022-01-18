from django.urls import path
from.views import *

urlpatterns = [
    path('',home),
    path('delete_todo/<id>/', delete_todo, name='delete_todo')

]