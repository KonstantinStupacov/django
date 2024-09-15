from django.urls import path
from .views import SayHellow


urlpatterns = [
    path('', SayHellow.as_view()),
]