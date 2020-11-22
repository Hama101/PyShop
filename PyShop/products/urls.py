from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.index ),
    path('new/',v.new)
]
