from job.models import Job
from.serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import PermissionDenied




@permission_classes([AllowAny])
@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all() 
    data = JobSerializer(all_jobs, many=True).data
    return Response({'data':data})


class JobApiView(APIView):

    def get_object(self, id):  
        try:
            return Job.objects.get(id=id)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, id):
        if not request.user.is_authenticated:
            raise PermissionDenied("You must be authenticated to view this.")
        queryset = self.get_object(id)
        serializer = JobSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        if not request.user.is_staff:  
            raise PermissionDenied("Only admins can update jobs.")
        queryset = self.get_object(id)
        serializer = JobSerializer(queryset, data=request.data, partial=True)
        if 'image' in request.FILES:
            serializer._validated_data.update({'image': request.FILES['image']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if not request.user.is_staff:  
            raise PermissionDenied("Only admins can delete jobs.")
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)