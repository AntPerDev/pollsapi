# from django.urls import path
# from .views import polls_list, polls_detail
#
#
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail"),
# ]

from django.urls import path

from .apiviews import ChoiceList, CreateVote, PollDetail, PollList

urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

]