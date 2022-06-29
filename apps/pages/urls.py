from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('contact-submit', views.contactSubmit, name="submit")
]