from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.see, name="Search"),
]
