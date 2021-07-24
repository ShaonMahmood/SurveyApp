from django.urls import path

from survey.views import survey_view, survey_dashboard, survey_save_view, survey_taken_view, survey_taken_detail_view

urlpatterns = [
    # path('', SurveyListView.as_view(), name='main-view'),
    path('', survey_dashboard, name='main-view'),
    path('taken-survey/', survey_taken_view, name='survey-taken-view'),
    path('taken-survey/<pk>/', survey_taken_detail_view, name='survey-taken-detail-view'),
    path('<pk>/', survey_view, name='survey-view'),
    path('<pk>/save/', survey_save_view, name='survey-save-view')
]