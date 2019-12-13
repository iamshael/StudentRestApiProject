from django.urls import path
from apiapp import views

urlpatterns = [
    path('home/', views.homeview),
]
