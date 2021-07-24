from django.contrib import admin
import nested_admin
from question.models import Question, AnswerOption

# Register your models here.

class AnswerOptionsInline(nested_admin.NestedTabularInline):
    exclude = ('created_at', 'updated_at', 'updated_by', 'created_by')
    model = AnswerOption
    extra = 1

class QuestionAdmin(nested_admin.NestedTabularInline):
    exclude = ('created_at', 'updated_at', 'updated_by', 'created_by', 'is_required', 'default_value')
    model = Question
    extra = 1
    inlines = [AnswerOptionsInline]


admin.site.register(Question)
admin.site.register(AnswerOption)
