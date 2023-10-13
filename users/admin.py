from django.contrib import admin
from .models import Applicant  # 이 앱의 models.py에서 Applicant 모델을 import 합니다.

admin.site.register(Applicant)