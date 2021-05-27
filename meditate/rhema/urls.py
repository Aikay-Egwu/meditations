from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('new/', views.CreateNew.as_view())
]
