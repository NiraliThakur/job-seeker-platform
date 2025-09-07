from pyexpat.errors import messages
from rest_framework import generics, permissions
from django.shortcuts import render, redirect, get_object_or_404
from backend_app.forms import JobseekerProfileForm, PostJobForm
from backend_app.models import *
from backend_app.serializers import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.

#Authentication
def index(request):
    return render(request, 'base.html')

def register_page(request):
    return render(request, 'auth/register.html')

def login_page(request):
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)  
    return redirect('login_page') 

# Job seeker function views
@login_required
def jobseeker_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login_page')  
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'jobs/jobseeker_dashboard.html', {'jobs': jobs})

@login_required
def jobseeker_profile(request):
    try:
        profile = request.user.jobseeker_profile  
    except JobseekerProfile.DoesNotExist:
        profile = None

    if request.method == "POST":
        if profile:  
            form = JobseekerProfileForm(request.POST, request.FILES, instance=profile)
        else:  
            form = JobseekerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                new_profile = form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
                return redirect("jobseeker_profile")
    else:
        form = JobseekerProfileForm(instance=profile)

    return render(request, "jobs/jobseeker_profile.html", {
        "form": form,
        "profile": profile,
    })

@login_required
def edit_jobseeker_profile(request):
    profile = get_object_or_404(JobseekerProfile, user=request.user)

    if request.method == 'POST':
        form = JobseekerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('jobseeker_profile')  
    else:
        form = JobseekerProfileForm(instance=profile)

    return render(request, 'jobs/edit_profile.html', {'form': form})
    
@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(applicant=request.user).select_related("job")
    return render(request, "jobs/my_applications.html", {"applications": applications})

@login_required
def job_search(request):
    jobs = Job.objects.all()

    title_query = request.GET.get('title', '')
    company_query = request.GET.get('company', '')
    location_query = request.GET.get('location', '')
    job_type_query = request.GET.get('job_type', '')

    if title_query:
        jobs = jobs.filter(title__icontains=title_query)
    if company_query:
        jobs = jobs.filter(company__icontains=company_query)
    if location_query:
        jobs = jobs.filter(location__icontains=location_query)
    if job_type_query:
        jobs = jobs.filter(job_type=job_type_query)
    
    paginator = Paginator(jobs, 5) 
    page_number = request.GET.get('page')
    page_jobs = paginator.get_page(page_number)

    context = {
        'jobs': jobs,
        'title_query': title_query,
        'company_query': company_query,
        'location_query': location_query,
        'job_type_query': job_type_query,

    }
    return render(request, 'jobs/job_search.html', context)

@login_required
def job_list(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    already_applied = JobApplication.objects.filter(job=job, applicant=request.user).exists()
    return render(request, 'jobs/job_details.html', {'job': job, 'already_applied': already_applied})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, "You have already applied for this job.")
        return redirect("my_applications")

    if request.method == "POST":
        resume = request.FILES.get("resume")
        cover_letter = request.POST.get("cover_letter", "")

        JobApplication.objects.create(
            job=job,
            applicant=request.user,
            resume=resume,
            cover_letter=cover_letter
        )
        messages.success(request, "Your application has been submitted successfully!")
        return redirect("my_applications")

    return render(request, "jobs/apply_job.html", {"job": job})


#Recruiter function views
@login_required
def recruiter_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login_page') 

    jobs = Job.objects.filter(recruiter=request.user).order_by('-posted_at')

    return render(request, 'recruiter/recruiter_dashboard.html', {'jobs': jobs})

@login_required
def post_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        skills_required = request.POST.get('skills_required')
        location = request.POST.get('location')
        salary = request.POST.get('salary')

        Job.objects.create(
            recruiter=request.user,
            title=title,
            description=description,
            skills_required=skills_required,
            location=location,
            salary=salary
        )
        return redirect('recruiter_dashboard')

    return render(request, 'recruiter/post_job.html')
   
@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, recruiter=request.user)  

    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.company = request.POST.get('company')
        job.job_type = request.POST.get('job_type')
        job.location = request.POST.get('location')
        job.experience_required = request.POST.get('experience_required')
        job.skills_required = request.POST.get('skills_required')
        job.requirements = request.POST.get('requirements')
        job.description = request.POST.get('description')
        job.salary = request.POST.get('salary') or None  

        job.save()
        return redirect('recruiter_dashboard')  

    return render(request, 'recruiter/edit_job.html', {'job': job})

@login_required
def view_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id, recruiter=request.user)  
    applications = JobApplication.objects.filter(job=job).select_related("applicant")  

    if request.method == "POST":
        app_id = request.POST.get("app_id")
        new_status = request.POST.get("status")
        application = get_object_or_404(JobApplication, id=app_id, job=job)
        application.status = new_status
        application.save()
        return redirect("view_applications", job_id=job.id)
    
    return render(request, 'recruiter/view_applications.html', {
        "job": job,
        "applications": applications
    })

@login_required
def update_application_status(request, application_id, status):
    application = get_object_or_404(JobApplication, id=application_id, job__recruiter=request.user)
    if status in ["Shortlisted", "not shortlisted"]:
        application.status = status
        application.save()
    return redirect("view_applications", job_id=application.job.id)

@login_required
def search_jobseekers(request):
    query = request.GET.get('q', '').strip()
    profiles = JobseekerProfile.objects.all()

    if query:
        profiles = profiles.filter(
            Q(skills__icontains=query) |
            Q(current_location__icontains=query) |
            Q(education__icontains=query)
        ).distinct()

    return render(request, 'recruiter/search_jobseekers.html', {'profiles': profiles, 'query': query})

@login_required
def view_jobseeker_profile(request, user_id):
    profile = get_object_or_404(JobseekerProfile, user__id=user_id)
    return render(request, 'recruiter/view_jobseeker_profile.html', {'profile': profile})


# API Views 
class JobListAPI(generics.ListAPIView):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

class JobDetailAPI(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

class CreateProfileAPI(generics.CreateAPIView):
    queryset = JobseekerProfile.objects.all()
    serializer_class = JobseekerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApplyToJobAPI(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]