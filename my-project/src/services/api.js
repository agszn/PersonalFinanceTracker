// src/api.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust base URL as needed
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getTransactions = () => apiClient.get('/transactions');
export const createTransaction = (transaction) => apiClient.post('/transactions', transaction);
export const updateTransaction = (id, transaction) => apiClient.put(`/transactions/${id}`, transaction);
export const deleteTransaction = (id) => apiClient.delete(`/transactions/${id}`);
export const getFinancialSummary = () => apiClient.get('/financial-summary');
