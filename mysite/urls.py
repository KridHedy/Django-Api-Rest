from django.urls import path, include
from myapi import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('Customers', views.CustomerView)

urlpatterns = [

    path('',views.index),
    path('framework', include(router.urls)),
    path('index',views.index),
    path('event',views.event)

]