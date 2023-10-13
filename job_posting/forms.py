from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['company_id', 'position', 'compensation', 'description', 'technologies']


# 수정용 폼
class JobPostingUpdateForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        exclude = ['company_id']  # company_id 제외