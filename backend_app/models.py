from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class JobseekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="jobseeker_profile")
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, blank=True, null=True) 
    phone = models.CharField(max_length=15, blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    experience_required = models.TextField(blank=True)
    skills_required = models.TextField(blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=[
        ('full-time', 'Full-Time'), 
        ('part-time', 'Part-Time'),
        ('remote', 'Remote'),
        ('internship', 'Internship'),
    ])
    requirements = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs', null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume/')
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('awaiting recriters action', 'Awaiting recruiters action'),
        ('Shortlisted', 'Shortlisted'),
        ('not shortlisted', 'Not shortlisted')
    ], default='awaiting recriters action')

    def __str__(self):
        return f'{self.applicant.username} applied to {self.job.title}'

