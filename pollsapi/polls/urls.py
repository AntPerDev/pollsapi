# from django.urls import path
# from .views import polls_list, polls_detail
#
#
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail"),
# ]

from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import PollViewSet, ChoiceList, CreateVote, PollDetail, PollList

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

]
urlpatterns += router.urls
