from rest_framework import serializers

from question.models import AnswerOption, Question


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'text', 'value']


class QuestionSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['id', 'answer_options', 'text', 'is_required', 'question_type', 'order', 'placeholder']
