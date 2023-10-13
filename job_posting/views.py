from django.http import HttpResponse
from .forms import JobPostingForm, JobPostingUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from .models import JobPosting


@csrf_exempt
@require_http_methods(["POST"])
def create_job_posting(request):
    try:
        data = json.loads(request.body) # 파싱된 JSON 데이터
        form = JobPostingForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse("Job posting created successfully.")
        else:
            return JsonResponse(form.errors, status=400)
    except json.JSONDecodeError:
        return HttpResponse("Error: Submitted data is not in JSON format", status=400)
    



@csrf_exempt
@require_http_methods(["POST"])
def update_job_posting(request, posting_id):
    data = json.loads(request.body)
    job_posting = JobPosting.objects.get(pk=posting_id)
    form = JobPostingUpdateForm(data, instance=job_posting)

    if form.is_valid():
        form.save()
        return HttpResponse("Job posting updated successfully.")
    else:
        return JsonResponse(form.errors, status=400)
    