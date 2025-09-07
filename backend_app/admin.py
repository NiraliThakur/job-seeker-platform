from django.contrib import admin
from backend_app.models import JobseekerProfile, Job, JobApplication

# Register your models here.
admin.site.register(JobseekerProfile)
admin.site.register(Job)
admin.site.register(JobApplication)