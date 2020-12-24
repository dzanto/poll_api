from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from api.models import Poll, Question, Answer
from api.serializers import (
    PollSerializer, QuestionSerializer, AnswerSerializer,
    QuestionListSerializer, UserPollSerializer, AnswerOneTextSerializer,
    AnswerChoiceSerializer, AnswerMultipleChoiceSerializer
)
from datetime import datetime


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ActivePollListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Poll.objects.filter(end_date__gte=datetime.today())
    serializer_class = PollSerializer


class UserPollListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    def get_queryset(self):
        queryset = Poll.objects.filter(questions__answers__author='admin')
        return queryset
    serializer_class = UserPollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        poll = get_object_or_404(Poll, id=self.kwargs['id'])
        return poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['id'])
        serializer.save(poll=poll)





class AnswerListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class AnswerCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            poll__id=self.kwargs['id'],
        )
        if question.type_question == 'text_field':
            return AnswerOneTextSerializer
        elif question.type_question == 'radio':
            return AnswerChoiceSerializer
        else:
            return AnswerMultipleChoiceSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            poll__id=self.kwargs['id'],
        )
        serializer.save(question=question)
