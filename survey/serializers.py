from rest_framework import serializers

from question.serializers import QuestionSerializer
from survey.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Survey
        fields = ['id', 'questions', 'name', 'number_of_questions', 'time']