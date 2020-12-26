from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

# список всех опросов
router.register('polls', views.PollViewSet)

# список активных опросов
router.register('active_polls', views.ActivePollListViewSet)

# список опросов с детализацией
# router.register('user_polls', views.UserPollListViewSet, basename='list_user_polls')

# опросы пользователя
router.register(
    'user_polls/(?P<id>\d+)',
    views.UserIdPollListViewSet, basename='list_userid_polls'
)

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

# варианты ответа для вопроса
router.register(
    'polls/(?P<id>\d+)/questions/(?P<question_pk>\d+)/choices',
    views.ChoiceListCreateViewSet, basename='perform_create_choice'
)

urlpatterns = [
    path('', include(router.urls)),
    # получение JWT токена
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
