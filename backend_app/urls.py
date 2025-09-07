from django.urls import path
from backend_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register_page/', views.register_page, name='register_page'),  
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('jobseeker/dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('recruiter/dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('jobseeker_profile/', views.jobseeker_profile, name='jobseeker_profile'),
    path('jobseeker_profile/edit/', views.edit_jobseeker_profile, name='edit_jobseeker_profile'),
    path('job_search/', views.job_search, name='job_search'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('recruiter/post-job/', views.post_job, name='post_job'),
    path('recruiter/edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('recruiter/view_applications/<int:job_id>/', views.view_applications, name='view_applications'),
    path('recruiter/search-jobseekers/', views.search_jobseekers, name='search_jobseekers'),
    path('recruiter/jobseeker/<int:user_id>/', views.view_jobseeker_profile, name='view_jobseeker_profile'),
       
    # API URls
    path('api/jobs/', views.JobListAPI.as_view()),
    path('api/jobs/<int:pk>/', views.JobDetailAPI.as_view()),
    path('api/apply/', views.ApplyToJobAPI.as_view()),
    path('api/create-profile/', views.CreateProfileAPI.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
