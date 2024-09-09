from job.api.serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from job.models import Job
from django.shortcuts import redirect

class HomeAPI(APIView):

     def post(self, request):
        jobs = Job.objects.all()
        count = Job.objects.count()

        search = request.data.get('search_name') 
        if search:
            if request.user.is_authenticated:
                jobs = jobs.filter(title__icontains=search)
                jobs_data = JobSerializer(jobs, many=True).data
                return Response({
                    "jobs": jobs_data,
                    "count": count
                }, status=status.HTTP_200_OK)
            else:
                return redirect('accounts:signup')

       
        return Response({
            "count": count
        }, status=status.HTTP_200_OK)