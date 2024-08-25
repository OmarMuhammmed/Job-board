from django.shortcuts import render
from job.models import Job
# Create your views here.

def home(request):
   jobs = Job.objects.all()
   count = Job.objects.count()
   return render(request,'home.html',{ 
                                        "jobs" :jobs ,
                                        "count" : count ,
                                        })