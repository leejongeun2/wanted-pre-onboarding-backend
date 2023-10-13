from django.contrib import admin
from .models import Company  # 이 앱의 models.py에서 Company 모델을 import 합니다.

admin.site.register(Company)