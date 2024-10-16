// src/services/transactionService.js
import axios from '../plugins/axios';

export const getTransactions = async () => {
  const response = await axios.get('/transactions/');
  return response.data;
};

export const createTransaction = async (transactionData) => {
  const response = await axios.post('/transactions/', transactionData);
  return response.data;
};

export const updateTransaction = async (id, transactionData) => {
  const response = await axios.put(`/transactions/${id}/`, transactionData);
  return response.data;
};

export const deleteTransaction = async (id) => {
  await axios.delete(`/transactions/${id}/`);
};
