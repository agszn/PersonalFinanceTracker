from django import forms
from .models import Transaction, FinancialSummary

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'description']

class FinancialSummaryForm(forms.ModelForm):
    class Meta:
        model = FinancialSummary
        fields = ['total_income', 'total_expenses', 'net_balance']


