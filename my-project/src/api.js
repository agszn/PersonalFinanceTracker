// src/api.js
import axios from 'axios';

// Create an Axios instance with default settings
const api = axios.create({
  baseURL: 'http://localhost:8000/api',  // Replace with your backend URL
  timeout: 10000,  // Timeout setting
  headers: {
    'Content-Type': 'application/json',
  },
});

// Export API functions using the `api` instance
export const getTransactions = () => api.get('/transactions');
export const createTransaction = (transaction) => api.post('/transactions', transaction);
export const updateTransaction = (id, transaction) => api.put(`/transactions/${id}`, transaction);
export const deleteTransaction = (id) => api.delete(`/transactions/${id}`);
export const getFinancialSummary = () => api.get('/financial-summary');
