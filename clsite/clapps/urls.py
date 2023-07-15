from django.urls import path, include
from .views import *

app_name = "clapps"
urlpatterns = [
    path("gensent/", GenerateSentence.as_view())
]