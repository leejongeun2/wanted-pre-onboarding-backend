from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['company_id', 'position', 'compensation', 'description', 'technologies']
