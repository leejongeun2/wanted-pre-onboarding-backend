from django.urls import path
from . import views

app_name = 'job_posting'

urlpatterns = [
    path('create/', views.create_job_posting, name='create_job_posting'),
    path('<int:posting_id>/update/', views.update_job_posting, name='update_job_posting'),
    path("<int:posting_id>/delete/", views.delete, name="delete"),

]