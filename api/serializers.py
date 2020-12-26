from rest_framework import serializers
from api.models import Poll, Question, Answer, Choice
from django.db.models import Q

# опросы
class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll


# варианты ответов
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
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

    def get_queryset(self):
        author_id = self.context.get('request').parser_context['kwargs']['id']
        request = self.context.get('request', None)
        queryset = super().get_queryset()
        print(author_id)
        if not request or not queryset:
            return None
        return queryset.exclude(~Q(author__id=author_id))


# вопросы с ответами пользователей
class QuestionListSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField('get_answers')

    class Meta:
        fields = ['text', 'answers']
        model = Question

    def get_answers(self, question):
        author_id = self.context.get('request').parser_context['kwargs']['id']
        answers = Answer.objects.filter(Q(question=question) & Q(author__id=author_id))
        serializer = AnswerSerializer(instance=answers, many=True)
        return serializer.data


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
        question_id = self.context.get('request').parser_context['kwargs']['question_pk']
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField,
                         self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(question_id=question_id)


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



