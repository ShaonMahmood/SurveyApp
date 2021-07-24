import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from question.models import Question
from survey.models import Survey, TakenSurvey, SurveyAnswer


class SurveyListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'survey/main.html'

@staff_member_required
def survey_dashboard(request):
    surveys = Survey.objects.all()
    return render(request, 'survey/main.html', {'object_list': surveys})


@staff_member_required
def survey_view(request, pk):
    survey = Survey.objects.prefetch_related('questions__answer_options').get(pk=pk)
    user = request.user
    if TakenSurvey.objects.filter(participated_user=user, survey=survey).exists():
        return render(request, 'survey/survey.html', {'obj': survey, 'status': 'participated already'})
    return render(request, 'survey/survey.html', {'obj': survey, 'status': 'new'})


def survey_data_view(request, pk):
    survey = Survey.objects.prefetch_related('questions__answer_options').get(pk=pk)
    user = request.user
    if TakenSurvey.objects.filter(participated_user=user, survey=survey).exists():
        return JsonResponse(
            {
                'status': 'participated',
                'message': 'This survey is participated by the user already'
            }
        )

    questions = []
    for question in survey.questions.all().order_by("order"):
        q_dict = {
            "text": question.text,
            "order": question.order,
            "id": question.id,
            "type": question.question_type,
            "placeholder": question.placeholder
        }
        answer_options = []
        for option in question.answer_options.all():
            answer_dict = {
                "text": option.text,
                "id": option.id,
                "value": option.value
            }
            answer_options.append(answer_dict)
        q_dict["answer_options"] = answer_options
        questions.append(q_dict)

    return JsonResponse({
        "status": "success",
        "result": {
            "time": survey.time,
            "questions": questions
        }
    })



@login_required
def survey_taken_view(request):
    user = request.user
    if user.is_superuser:
        surveys = TakenSurvey.objects.select_related('participated_user', 'survey').all()
    else:
        surveys = TakenSurvey.objects.select_related('participated_user', 'survey').filter(participated_user=user)
    return render(request, 'survey/taken_surveys.html', {'object_list': surveys})

@login_required
def survey_taken_detail_view(request, pk):
    survey = TakenSurvey.objects.prefetch_related('survey_answers').get(pk=pk)
    return render(request, 'survey/taken_surveys_detail.html', {'object': survey})


@staff_member_required
def survey_save_view(request, pk):
    if request.is_ajax():
        result_data = json.loads(request.POST.get("answer_list"))
        print(result_data)
        user = request.user
        survey = Survey.objects.get(pk=pk)
        if TakenSurvey.objects.filter(participated_user=user, survey=survey).exists():
            return JsonResponse(
                {
                    'status': 'error',
                    'message': 'This survey is participated by the user already'
                }
            )
        else:
            tk_servey = TakenSurvey.objects.create(participated_user=user, survey=survey, status=TakenSurvey.COMPLETED)
            for tk_answer in result_data:
                q_id = tk_answer['question']
                question = Question.objects.get(id=q_id)
                q_answer = tk_answer.get('answer', '')
                survey_answer = SurveyAnswer.objects.create(question=question, taken_survey=tk_servey, text=q_answer)

            return JsonResponse(
                {
                    'status': 'success',
                    'message': 'survey answer has been recorded'
                }
            )
