from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogCreateListView, name='name'),
    path('<str:pk>', views.blogDetailUpdate, name='name'),
]