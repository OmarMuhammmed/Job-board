from .import views
from django.urls import path, include
from .api import views as apiviews

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit,name='profile_edit'),
    path('logout_user/', views.logout_user,name='logout_user'),
    # Api
    path('api/sinup/', apiviews.SignUpView.as_view()),
    path('api/login/', apiviews.LoginView.as_view())
   
]