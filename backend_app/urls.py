from django.urls import path
from .views import *
from backend_app import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register_page/', views.register_page, name='register_page'),  
    path('login_page/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/jobseeker/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('dashboard/employer/', views.employer_dashboard, name='employer_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    # path('joblistcreate/', JobListCreateView.as_view, name='job-list'),
    # path('apply/', ApplyJobView.as_view(), name='apply-job'),
    # path('recruiter-jobs/', RecruiterJobsView.as_view()),
    # path('applications/<int:job_id>/', JobApplicationsView.as_view()),
    # path('applications/update/<int:pk>/', UpdateApplicationStatusView.as_view()),
    # path('profile/', update_profile, name='update_profile'),
    # path('job-profile/', JobProfileView.as_view(), name='job_profile'),
    # path('api/dashboard/', views.get_dashboard),
    # path('api/upload-resume/', views.upload_resume),
]

