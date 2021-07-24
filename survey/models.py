from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from core.models import BaseModel
# Create your models here.


class Survey(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=50, null=True, blank=True)
    details = models.TextField(verbose_name=_('details'))
    order = models.PositiveSmallIntegerField(verbose_name=_('order'), default=0)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class TakenSurvey(BaseModel):

    user_model = get_user_model()

    DRAFT = 'draft'
    NOTCOMPLETED = 'notcompleted'
    COMPLETED = 'completed'

    SURVEY_STATUS = (
        (DRAFT, _('Draft')),
        (NOTCOMPLETED, _('Not Completed')),
        (COMPLETED, _('Completed'))
    )
    survey = models.ForeignKey(
        to='survey.Survey', verbose_name=_('survey'), on_delete=models.CASCADE, related_name='taken_surveys',
        null=True, blank=True
    )
    participated_user = models.ForeignKey(
        to=user_model, verbose_name=_('participate by'), 
        null=True, blank=True, related_name='taken_surveys', on_delete=models.SET_NULL
    )
    status = models.CharField(verbose_name=_('status'), max_length=20, choices=SURVEY_STATUS, default=DRAFT)


                    

class SurveyAnswer(BaseModel):
    text = models.CharField( verbose_name=_('survey answer text'), max_length=1023, null=True, blank=True )
    question = models.ForeignKey(
        to='question.Question', verbose_name=_('question'), on_delete=models.CASCADE, related_name="survey_answers", null=True, blank=True
    )
    taken_survey = models.ForeignKey(
        to='survey.TakenSurvey', verbose_name=_('taken survey'), on_delete=models.CASCADE, related_name='survey_answers'
    )
    