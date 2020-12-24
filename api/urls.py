from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register('polls', views.PollViewSet)
router.register('active_polls', views.ActivePollListViewSet)
router.register('user_polls', views.UserPollListViewSet, basename='list_user_polls')

router.register('answers', views.AnswerListViewSet)
router.register('questions', views.QuestionListViewSet)

router.register(
    'polls/(?P<id>\d+)/questions',
    views.QuestionViewSet, basename='perform_create_questions'
)
router.register(
    'polls/(?P<id>\d+)/questions/(?P<question_pk>\d+)/answers',
    views.AnswerCreateViewSet, basename='perform_create_answers'
)

urlpatterns = [
    path('', include(router.urls)),
]
