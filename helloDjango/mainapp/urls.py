from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('list',user_list3),
    path('add',add_user),
    path('update',update_user),
    path('delete',delete_user),
    path('find',find_fruit),
    path('store',find_store),
    path('count',count_fruit)
]
