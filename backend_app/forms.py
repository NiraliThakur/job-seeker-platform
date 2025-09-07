from django import forms
from .models import JobseekerProfile, Job

class JobseekerProfileForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfile
        fields = ['full_name', 'email', 'phone', 'current_location', 'skills', 'experience', 'education', 'resume']

class PostJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'experience_required', 'skills_required', 'salary', 'job_type', 'description', 'requirements']


    