from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm, FinancialSummaryForm
from .models import Transaction, FinancialSummary

# Transaction CRUD Views


from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count, Sum
from django.utils import timezone
from django.db.models.functions import TruncWeek
from .models import Transaction

from django.db.models import Count
from django.db.models.functions import TruncDay

def transaction_list(request):
    query = request.GET.get('q', '')  # Get search query
    filter_type = request.GET.get('filter', '')  # Get transaction filter (Income/Expense)

    # Filter transactions for the logged-in user
    transactions = Transaction.objects.filter(user=request.user)

    # Apply transaction type filter
    if filter_type in ['IN', 'EX']:
        transactions = transactions.filter(transaction_type=filter_type)

    # Apply search query on description, amount, or date
    if query:
        transactions = transactions.filter(
            Q(description__icontains=query) | Q(amount__icontains=query) | Q(date__icontains=query)
        )

    # Get the total, today's, weekly, and monthly transactions
    total_transactions = transactions.count()
    todays_transactions = transactions.filter(date__date=timezone.now().date()).count()
    weekly_transactions = transactions.filter(date__gte=timezone.now() - timezone.timedelta(days=7)).count()
    monthly_transactions = transactions.filter(date__gte=timezone.now() - timezone.timedelta(days=30)).count()

    total_income = transactions.filter(transaction_type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = transactions.filter(transaction_type='EX').aggregate(Sum('amount'))['amount__sum'] or 0
    total_balance = total_income - total_expenses

    return render(request, 'transaction/transaction_list.html', {
        'transactions': transactions,
        'total_balance': total_balance,
        'query': query,
        'filter_type': filter_type,
        'total_transactions': total_transactions,
        'todays_transactions': todays_transactions,
        'weekly_transactions': weekly_transactions,
        'monthly_transactions': monthly_transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
    })

# def transaction_create(request):
#     transactions = Transaction.objects.filter(user=request.user)
#     total_income = transactions.filter(transaction_type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
#     total_expenses = transactions.filter(transaction_type='EX').aggregate(Sum('amount'))['amount__sum'] or 0
#     total_balance = total_income - total_expenses

#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             transaction = form.save(commit=False)
#             transaction.user = request.user  # Set the current user
#             transaction.save()
#             return redirect('transaction_success')  # Redirect to a success page or list
#     else:
#         form = TransactionForm()
#     return render(request, 'transaction/transaction_form.html', {'form': form,'total_balance':total_balance})

from django.contrib.auth.decorators import login_required

@login_required
def transaction_create(request):
    transactions = Transaction.objects.filter(user=request.user)
    total_income = transactions.filter(transaction_type='IN').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = transactions.filter(transaction_type='EX').aggregate(Sum('amount'))['amount__sum'] or 0
    total_balance = total_income - total_expenses

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_success')
    else:
        form = TransactionForm()
    return render(request, 'transaction/transaction_form.html', {'form': form, 'total_balance': total_balance})


def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    return render(request, 'transaction/transaction_detail.html', {'transaction': transaction})


def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction/transaction_form.html', {'form': form})


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transaction/transaction_confirm_delete.html', {'transaction': transaction})

# Financial Summary Views


def financial_summary_update(request):
    user_summary, created = FinancialSummary.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = FinancialSummaryForm(request.POST, instance=user_summary)
        if form.is_valid():
            form.save()
            return redirect('financial_summary_success')
    else:
        form = FinancialSummaryForm(instance=user_summary)
    return render(request, 'transaction/financial_summary_form.html', {'form': form})


def financial_summary_detail(request):
    user_summary = get_object_or_404(FinancialSummary, user=request.user)
    return render(request, 'transaction/financial_summary_detail.html', {'user_summary': user_summary})

def transaction_success(request):
    return render(request, 'transaction/transaction_success.html')

def financial_summary_success(request):
    return render(request, 'transaction/financial_summary_success.html')

# views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Transaction
# from .serializers import TransactionSerializer

# @api_view(['GET', 'POST'])
# def transaction_list_create(request):
#     if request.method == 'GET':
#         transactions = Transaction.objects.filter(user=request.user)
#         serializer = TransactionSerializer(transactions, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             transaction = serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def transaction_update_delete(request, pk):
#     try:
#         transaction = Transaction.objects.get(pk=pk, user=request.user)
#     except Transaction.DoesNotExist:
#         return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = TransactionSerializer(transaction, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         transaction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import Http404

class TransactionListCreateView(APIView):
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user=request.user)
        serializer = self.serializer_class(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionUpdateDeleteView(APIView):
    serializer_class = TransactionSerializer

    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk, user=self.request.user)
        except Transaction.DoesNotExist:
            raise Http404

    def put(self, request, pk, *args, **kwargs):
        transaction = self.get_object(pk)
        serializer = self.serializer_class(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404
# from .models import Transaction
# from .serializers import TransactionSerializer

# class TransactionListCreateView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TransactionSerializer

#     def get(self, request, *args, **kwargs):
#         transactions = Transaction.objects.filter(user=request.user)
#         serializer = self.serializer_class(transactions, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             transaction = serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TransactionUpdateDeleteView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TransactionSerializer

#     def get_object(self, pk):
#         try:
#             return Transaction.objects.get(pk=pk, user=self.request.user)
#         except Transaction.DoesNotExist:
#             raise Http404

#     def put(self, request, pk, *args, **kwargs):
#         transaction = self.get_object(pk)
#         serializer = self.serializer_class(transaction, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, *args, **kwargs):
#         transaction = self.get_object(pk)
#         transaction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
