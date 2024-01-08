from django.urls import path
from .views import homePageView

urlpatterns = [
  path("hello/", homePageView, name="hello")
]