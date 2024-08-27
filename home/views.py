from django.shortcuts import render
from job.models import Job, Category
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def home(request):
    jobs = Job.objects.all()
    count = Job.objects.count()
    categoreis = Category.objects.all()
    
    if 'search_name' in request.GET:
        if request.user.is_authenticated:
            search = request.GET['search_name']
            if search:
                jobs = jobs.filter(title__icontains=search)
                return render(request, 'home.html', { 
                                        "jobs": jobs,
                                        "count": count,
                                        "categoreis": categoreis, 
                                        })
        else:
            return redirect('accounts:signup')

    return render(request, 'home.html', { 
                                        "count": count,
                                        })