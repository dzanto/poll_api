from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Poll(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    # После создания поле "дата старта" у опроса менять нельзя
    start_date = models.DateField(auto_now_add=True, verbose_name='Start date')
    end_date = models.DateField(verbose_name='End date')
    description = models.CharField(max_length=200, verbose_name='Description')

    def __str__(self):
        return self.name


QUESTION_TYPES = (
    ('text_field', 'Ответ текстом'),
    ('radio', 'Один вариант'),
    ('check_boxes', 'Выбор нескольких вариантов'),
)


class Question(models.Model):
    text = models.TextField()
    type_question = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        verbose_name='Тип вопроса',
    )
    poll = models.ForeignKey(
        Poll, blank=True, on_delete=models.CASCADE,
        related_name="questions"
    )
    first_choice = models.TextField(blank=True, null=True)
    second_choice = models.TextField(blank=True, null=True)
    third_choice = models.TextField(blank=True, null=True)
    true_choice = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    author = models.TextField(default='admin')
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    first_answer = models.TextField(blank=True, null=True)
    second_answer = models.TextField(blank=True, null=True)
    third_answer = models.TextField(blank=True, null=True)
    text_answer = models.TextField(blank=True, null=True)
    choice_answer = models.CharField(max_length=200, blank=True, null=True)
    # multi_choice_answer = models.

