from rest_framework import serializers
from api.models import Poll, Question, Answer, Choice


# опросы
class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll


# варианты ответов
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Choice


# вопросы
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question


# ответы пользователей
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer


# вопросы с ответами пользователей
class QuestionListSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        fields = ['text', 'answers']
        model = Question


# опросы с вопросами и ответами пользователей
class UserPollSerializer(serializers.ModelSerializer):
    questions = QuestionListSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Poll


# ответ своим текстом
class AnswerOneTextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['self_text']
        model = Answer


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        print(request)
        return queryset.filter(question_id=2)


# ответ выбором одного варианта
class AnswerOneChoiceSerializer(serializers.ModelSerializer):
    one_choice = UserFilteredPrimaryKeyRelatedField(
        many=False,
        queryset=Choice.objects.all()
    )

    class Meta:
        fields = ['one_choice']
        model = Answer


# ответ выбором нескольких вариантов
class AnswerMultipleChoiceSerializer(serializers.ModelSerializer):
    many_choice = UserFilteredPrimaryKeyRelatedField(
        many=True,
        queryset=Choice.objects.all()
    )

    class Meta:
        fields = ['many_choice']
        model = Answer



