from .import views
from django.urls import path, include


app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit,name='profile_edit'),
   
]