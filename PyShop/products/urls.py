from django.urls import path
from . import views

#   --> when its empty, we means the root url and in path we refer to it as ''
# /products/1/details
# /products/new

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]

