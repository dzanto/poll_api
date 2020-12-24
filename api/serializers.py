from rest_framework import serializers
from api.models import Poll, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    # question = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='text'
    # )

    class Meta:
        fields = '__all__'
        model = Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question


class QuestionListSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        fields = ['text', 'answers']
        model = Question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Answer


class AnswerOneTextSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['second_answer', 'third_answer']
        model = Answer


QUESTION_TYPES = (
    ('text_field', 'Ответ 1'),
    ('radio', 'Один 2'),
    ('check_boxes', 'Выбор 3'),
)


class AnswerChoiceSerializer(serializers.ModelSerializer):
    true_answer = serializers.ChoiceField(choices=QUESTION_TYPES)

    class Meta:
        exclude = ['second_answer', 'third_answer']
        model = Answer


class AnswerMultipleChoiceSerializer(serializers.ModelSerializer):
    true_answer = serializers.MultipleChoiceField(choices=QUESTION_TYPES)

    class Meta:
        exclude = ['second_answer', 'third_answer']
        model = Answer


class UserPollSerializer(serializers.ModelSerializer):
    questions = QuestionListSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Poll


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Poll


# class QuestionWriteSerializer(serializers.ModelSerializer):
#     poll = serializers.SlugRelatedField(
#         queryset=Poll.objects.all(),
#         many=True,
#         slug_field='name'
#     )
#
#     class Meta:
#         fields = '__all__'
#         model = Question
#
#
# class QuestionReadSerializer(serializers.ModelSerializer):
#     poll = PollSerializer(read_only=True, many=True)
#
#     class Meta:
#         fields = '__all__'
#         model = Question





# class AnswerWriteSerializer(serializers.ModelSerializer):
#     poll = serializers.SlugRelatedField(
#         queryset=Poll.objects.all(),
#         many=True,
#         slug_field='name'
#     )
#
#     class Meta:
#         fields = '__all__'
#         model = Answer
#
#
# class AnswerReadSerializer(serializers.ModelSerializer):
#     poll = PollSerializer(read_only=True)
#
#     class Meta:
#         fields = '__all__'
#         model = Answer
