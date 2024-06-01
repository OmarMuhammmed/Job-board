from .import views
from django.urls import path, include

app_name = 'contact'

urlpatterns = [
    path('', views.send_message,name='contact'),

]