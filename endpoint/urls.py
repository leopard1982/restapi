from django.contrib import admin
from django.urls import path
from tutorial1.views import hello_world
from tutorial1.viewsapi import viewAllUser

urlpatterns = [
    path('1/', viewAllUser, name="viewAllUser"),
]
