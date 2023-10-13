from django.http import HttpResponse
from .forms import JobPostingForm, JobPostingUpdateForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from .models import JobPosting
from django.forms.models import model_to_dict


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



def list_job_postings(request):
    # 데이터베이스에서 모든 채용공고를 가져옵니다.
    job_postings = JobPosting.objects.all().select_related('company_id')  # 회사 정보를 함께 가져오기 위해 select_related 사용

    # 채용공고 및 회사 정보를 JSON으로 변환할 수 있는 형태로 만듭니다.
    job_postings_list = []
    for jp in job_postings:
        job_posting_dict = model_to_dict(jp)
        company_info = model_to_dict(jp.company_id, fields=["name", "location", "country"])  # 회사의 이름, 위치, 국가 정보를 가져옵니다.
        
        # 응답에 필요한 추가 필드를 설정합니다.
        response_data = {
            "채용공고_id": job_posting_dict['id'],
            "회사명": company_info['name'],
            "국가": company_info['country'],
            "지역": company_info['location'],
            "채용포지션": job_posting_dict['position'],
            "채용보상금": job_posting_dict['compensation'],
            "사용기술": job_posting_dict['technologies']
        }

        job_postings_list.append(response_data)

    # 결과를 JSON 형태로 반환합니다.
    return JsonResponse(job_postings_list, safe=False)  # safe=False는 non-dict 객체를 전달할 때 필요합니다.







