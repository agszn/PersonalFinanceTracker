from django.urls import path
from . import views
from .views import TransactionListCreateView, TransactionUpdateDeleteView
urlpatterns = [
    # Transaction URLs
    path('transactions/create/', views.transaction_create, name='transaction_create'),
    path('transaction/', views.transaction_list, name='transaction_list'),
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/<int:pk>/update/', views.transaction_update, name='transaction_update'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),

    # Financial Summary URLs
    path('financial-summary/', views.financial_summary_update, name='financial_summary_update'),
    path('financial-summary/detail/', views.financial_summary_detail, name='financial_summary_detail'),

    # Success pages
    path('transactions/success/', views.transaction_success, name='transaction_success'),
    path('financial-summary/success/', views.financial_summary_success, name='financial_summary_success'),

    # RESTApi pages
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionUpdateDeleteView.as_view(), name='transaction-update-delete'),
]


