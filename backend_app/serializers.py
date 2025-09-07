from rest_framework import serializers
from backend_app.models import *

class JobseekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobseekerProfile
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


        
