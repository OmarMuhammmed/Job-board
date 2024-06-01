from .import views
from django.urls import path, include

app_name = 'job'
from . import api  
urlpatterns = [
    path('', views.job_list,name='job_list'),
    path('add', views.add_job ,name='add_job'),
    path('<str:slug>', views.job_detail ,name='job_detail'),
    # API 
    path('api/jobs', api.job_list_api ,name='job_list_api'),
    path('api/jobs/<int:id>', api.job_deatail_api ,name='job_deatail_api'),
    # CBV
    path('api/v2/jobs', api.JobListApi.as_view() ,name='job_deatail_api'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view()  ,name='JobDetail'),

]