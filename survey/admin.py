from django.contrib import admin
from survey.models import Survey
from question.admin import QuestionAdmin
import nested_admin

# Register your models here.

class SurveyAdmin(nested_admin.NestedModelAdmin):
    exclude = ('created_at', 'updated_at', 'updated_by', 'created_by')
    inlines = [QuestionAdmin]


admin.site.site_header = "Survey Administration"
admin.site.site_title = "Survey Admin Portal"
admin.site.index_title = "Welcome to Survey Admin Dashboard Portal"
admin.site.register(Survey, SurveyAdmin)
