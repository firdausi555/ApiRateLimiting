# api/urls.py

from django.urls import path
from .views import HelloWorldView, CustomThrottledView

urlpatterns = [
    path('hello/', HelloWorldView.as_view()),
    path('custom/', CustomThrottledView.as_view()),
]
