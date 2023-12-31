from django.urls import path
from . import views

app_name = 'job_posting'

urlpatterns = [
    path('create/', views.create_job_posting, name='create_job_posting'),
    path('<int:posting_id>/update/', views.update_job_posting, name='update_job_posting'),
    path("<int:posting_id>/delete/", views.delete, name="delete"),
    path('list_job_postings/', views.list_job_postings, name='list_job_postings'),
    path('<int:posting_id>/', views.job_posting_detail, name='job_posting_detail'),
    path('some/url', views.search_job_postings),
]