from django.shortcuts import get_object_or_404
from job.models import Job
from.serializers import JobSerializer, ApplySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import PermissionDenied
from job.forms import Jobform
from job.tasks import email_apply


@permission_classes([AllowAny])
@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all() 
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data':data})


@api_view(['POST'])
def add_job(request):
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Job added successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPI(APIView):
    permission_classes = [IsAuthenticated]  
    
    def get(self, request, slug):
        job_detail = get_object_or_404(Job, slug=slug)
        return Response({
            "job": {
                "title": job_detail.title,
                "description": job_detail.description,
                "salary": job_detail.salary,
                "experience": job_detail.experience,
                "num_applyed": job_detail.num_applyed,
            }
        }, status=status.HTTP_200_OK)
    
    def post(self, request, slug):
        
        job_detail = get_object_or_404(Job, slug=slug)
        serializer = ApplySerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data['job'] = job_detail
            serializer.save(job=job_detail)
            
            email_apply(request, slug)

            return Response({
                "message": "Your application was submitted successfully.",
                "job": job_detail.title,
                "application": serializer.data
            }, status=status.HTTP_201_CREATED)

        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

