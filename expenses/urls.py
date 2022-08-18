from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExpenseListAPIView.as_view(), name="expense-list"),
    path("<int:id>/", views.ExpenseDetailAPIView.as_view(), name="expense-detail"),
]
