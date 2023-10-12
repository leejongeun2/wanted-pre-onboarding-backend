from django.db import models

class JobPosting(models.Model):
    company_id = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name='job_postings') # 1
    position = models.CharField(max_length=100)
    compensation = models.DecimalField(max_digits=10, decimal_places=2)  # 채용 보상금
    description = models.TextField()  # 채용 내용
    technologies = models.CharField(max_length=200)  # 사용 기술

    def __str__(self):
        return f"{self.position} at {self.company_id}"  # company_id.name은 회사 모델의 회사명 필드를 참조해야 합니다.