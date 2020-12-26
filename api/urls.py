from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register('polls', views.PollViewSet)
router.register(
    'polls/(?P<id>\d+)/questions',
    views.QuestionViewSet,
    basename='questions'
)
router.register(
    'polls/(?P<id>\d+)/questions/(?P<question_pk>\d+)/choices',
    views.ChoiceViewSet,
    basename='choices'
)
router.register('active_polls', views.ActivePollListViewSet)
router.register(
    'polls/(?P<id>\d+)/questions/(?P<question_pk>\d+)/answers',
    views.AnswerCreateViewSet,
    basename='answers'
)
router.register(
    'my_polls',
    views.UserIdPollListViewSet,
    basename='list_userid_polls'
)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
