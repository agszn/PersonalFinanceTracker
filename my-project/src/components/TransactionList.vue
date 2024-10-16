<!-- TransactionList.vue -->
<template>
    <div>
      <h2>Transactions</h2>
      <ul>
        <li v-for="transaction in transactions" :key="transaction.id">
          {{ transaction.description }} - {{ transaction.amount }} - {{ transaction.transaction_type }}
          <button @click="editTransaction(transaction)">Edit</button>
          <button @click="deleteTransaction(transaction.id)">Delete</button>
        </li>
      </ul>
      <TransactionForm @transactionCreated="fetchTransactions"/>
    </div>
  </template>
  
  <script>
  import { getTransactions, deleteTransaction } from '@/api';
  
  export default {
    data() {
      return {
        transactions: [],
      };
    },
    methods: {
      async fetchTransactions() {
        const response = await getTransactions();
        this.transactions = response.data;
      },
      async deleteTransaction(id) {
        await deleteTransaction(id);
        this.fetchTransactions();
      },
      editTransaction(transaction) {
        // Handle editing transaction
      }
    },
    created() {
      this.fetchTransactions();
    }
  };
  </script>
  