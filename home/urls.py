from .import views
from django.urls import path
from .api import views as apiviews 
app_name = 'home'


urlpatterns = [ 
  path('', views.home, name='home'),
  # Api 
  path('home-api/', apiviews.HomeAPI.as_view(), name='home-api'),
  
]