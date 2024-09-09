from rest_framework import serializers 
from job.models import Job, Apply


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ('slug','owner')
        

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        exclude =[ 'job' ]
        