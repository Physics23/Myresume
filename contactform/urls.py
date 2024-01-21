from django.urls import path, include
from contactform import views

urlpatterns = [

    path('contactform/', views.contactform, name ='contactform'),
]
