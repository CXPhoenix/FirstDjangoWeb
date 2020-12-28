from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('/helloWorld', views.helloWorld, name='helloWorld'),
    path('<int:pk>/', views.postDetail, name='detail'),
]