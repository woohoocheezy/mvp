from django.urls import path
from .views import MakeBidding

urlpatterns = [
    path("<str:item_pk>", MakeBidding.as_view()),
]
