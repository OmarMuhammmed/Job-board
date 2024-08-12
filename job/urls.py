from .import views
from django.urls import path, include
app_name = 'job'
from .api import api  

urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('add/', views.add_job ,name='add_job'),
    path('<str:slug>', views.job_detail ,name='job_detail'), 
    path('api/jobs/', api.job_list_api ,name='job_list_api'),
     path('api/jobs/<int:id>/', api.ManageJob.as_view(), name='ManageJob'),
]