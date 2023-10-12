from django.db import models

class Application(models.Model): # 지원 내역(지원서)
    job_posting = models.ForeignKey('job_posting.JobPosting', on_delete=models.CASCADE, related_name='applications') # 1
    applicant = models.ForeignKey('users.Applicant', on_delete=models.CASCADE, related_name='applications') # 1
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Application for {self.job_posting} by {self.applicant}'
