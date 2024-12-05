from django.urls import path
from .views import *

urlpatterns = [
    path('',user_index,name="index_link"),
    path('contact',user_contact,name="contact_link")
]