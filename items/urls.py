from django.urls import path
from .views import ItemDetail, Items, ItemPurchase, ItemDelete

# ItemPhotos

urlpatterns = [
    path("", Items.as_view()),
    path("<int:pk>", ItemDetail.as_view()),
    path("<int:pk>/is_sold", ItemPurchase.as_view()),
    path("<int:pk>/is_deleted", ItemDelete.as_view()),
    # path("<int:pk>/photos", ItemPhotos.as_view()),
]
