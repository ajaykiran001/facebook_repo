from django.urls import path
from . import views

app_name = 'admin'
urlpatterns=[
    path('home',views.home,name='home'),
    path('service',views.service,name='service'),
]