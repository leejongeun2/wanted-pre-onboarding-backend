from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Application
from job_posting.models import JobPosting
from users.models import Applicant
import json



@csrf_exempt
def apply_to_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        applicant_id = data.get('사용자_id')
        job_posting_id = data.get('채용공고_id')

        try:
            applicant_instance = Applicant.objects.get(pk=applicant_id)
            job_posting = JobPosting.objects.get(pk=job_posting_id)

            existing_application = Application.objects.filter(applicant=applicant_instance).exists()
            if existing_application:
                return JsonResponse({'error': '이미 채용공고에 지원하셨습니다. 사용자는 한 번만 지원 가능합니다.'}, status=400)
            
            application = Application.objects.create(applicant=applicant_instance, job_posting=job_posting)

            return JsonResponse({'message': '지원이 성공적으로 제출되었습니다.'}, status=201)
        except (Applicant.DoesNotExist, JobPosting.DoesNotExist):
            return JsonResponse({'error': '채용 공고를 찾을 수 없습니다.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse(status=405)
