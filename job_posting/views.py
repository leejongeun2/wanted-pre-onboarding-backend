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
    


@csrf_exempt
@require_http_methods(["DELETE"])  # DELETE 요청만 허용
def delete(request, posting_id):
    try:
        # 데이터베이스에서 해당 ID의 채용공고를 찾습니다.
        job_posting = JobPosting.objects.get(pk=posting_id)
    except JobPosting.DoesNotExist:
        # 존재하지 않는 경우, 오류 메시지를 반환합니다.
        return JsonResponse({'error': 'Job posting not found'}, status=404)

    # 채용공고를 삭제합니다.
    job_posting.delete()

    # 성공 메시지를 반환합니다.
    return JsonResponse({'message': 'Job posting deleted successfully'}, status=200)