from django.urls import path,include
from Subapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
]