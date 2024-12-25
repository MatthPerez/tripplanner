from django.urls import path
from .views import ExpenseView, NewExpense, ExpenseUpdate, ExpenseDelete

urlpatterns = [
    path("", ExpenseView.as_view(), name="expense"),
    path("ajouter/", NewExpense.as_view(), name="expense_new"),
    path("<int:pk>/modifier/", ExpenseUpdate.as_view(), name="expense_update"),
    path("<int:pk>/supprimer/", ExpenseDelete.as_view(), name="expense_delete"),
]
