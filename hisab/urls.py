from django.urls import path
from .views import hello,register

urlpatterns = [
    path('', hello, name='hello'),
    path('register',register, name='register')
]