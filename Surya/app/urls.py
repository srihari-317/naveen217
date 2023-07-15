from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact, name='contact'),
    path('about',views.about,name="about"),
    path('getaquote',views.getaquote,name="getaquote"),
    path('pricing',views.pricing,name="pricing"),
    path('sampleinnerpage',views.sampleinnerpage,name="sampleinnerpage"),
    path('servicedetails',views.servicedetails,name="service-details"),
    path('services',views.services,name="services"),
    path('view',views.view, name='view'),

]