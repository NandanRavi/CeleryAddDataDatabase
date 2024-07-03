from django.urls import path
from .views import BooksView, UpdatedData, TriggerRatingUpdateView

urlpatterns = [
    path("books/", BooksView.as_view(), name='Books'),
    path('book-update/<int:pk>/update/', UpdatedData.as_view(), name='book-update'),
    path('trigger-rating-update/<int:start_id>/', TriggerRatingUpdateView.as_view(), name='trigger_rating_update'),
]
