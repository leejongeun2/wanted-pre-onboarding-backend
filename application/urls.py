from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('apply-to-job/', views.apply_to_job, name='apply_to_job'),
]