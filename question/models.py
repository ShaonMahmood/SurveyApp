from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel

# Create your models here.



class Question(BaseModel):
    TEXT, MULTILINE_TEXT, NUMBER, CHECKBOX, RADIO = 'text', 'multiline_text', 'number', 'checkbox', 'radio'
    QUESTION_TYPE = (
        (TEXT, _('Text')), (MULTILINE_TEXT, _('Multiline text')), (CHECKBOX, _('Checkbox')), (RADIO, _('Radio'))
    )

    ACTIVE, INACTIVE = 'active', 'inactive'
    QUESTION_STATUS = ((ACTIVE, _('Active')), (INACTIVE, _('Inactive')))

    survey = models.ForeignKey(
        to='survey.Survey', verbose_name=_('survey'), on_delete=models.CASCADE, related_name='questions',
        null=True, blank=True
    )
    
    text = models.TextField(verbose_name=_('text'), max_length=500)
    is_required = models.BooleanField(verbose_name=_('is required'), default=True)
    question_type = models.CharField(verbose_name=_('question type'), max_length=30, choices=QUESTION_TYPE)
    order = models.PositiveSmallIntegerField(verbose_name=_('order'), default=0)
    status = models.CharField(verbose_name=_('status'), max_length=30, choices=QUESTION_STATUS, default=ACTIVE)
    default_value = models.TextField(verbose_name=_('default value'), null=True, blank=True)
    placeholder = models.TextField(verbose_name=_('placeholder'), null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order']


class AnswerOption(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer_options")
    text = models.CharField(verbose_name=_('text'), max_length=50, null=True, blank=True)
    value = models.CharField(verbose_name=_('value'), max_length=50, null=True, blank=True)

    def __str__(self):
        return "{text}-{value}".format(text=self.text, value=self.value)
