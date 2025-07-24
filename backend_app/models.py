from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=[('jobseeker', 'Job seeker'), ('recruiter', 'Recruiter')], default='jobseeker')
#     skills = models.TextField(blank=True)
#     experience = models.TextField(blank=True)
#     education = models.TextField(blank=True)
#     resume = models.FileField(upload_to='resume/', blank=True, null=True)

#     def __str__(self):
#         return self.user.username
     
# class JobApplication(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=250)
#     company = models.CharField(max_length=250)
#     status = models.CharField(max_length=20, choices=[('Applied', 'Applied'), ('In Review', 'In Reveiw'), ('Rejected', 'Rejected'), ('Shortlisted', 'Shortlisted')], default='Applied')
#     applied_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.job_title}"
    
# class Jobs(models.Model):
#     title = models.CharField(max_length=255)
#     company = models.CharField(max_length=255)
#     description = models.TextField()
#     location = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

# class Application(models.Model):
#     job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
#     jobseeker = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
#     applied_at = models.DateTimeField(auto_now_add=True)