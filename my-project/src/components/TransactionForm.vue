<!-- TransactionForm.vue -->
<template>
    <form @submit.prevent="submitForm">
      <input v-model="description" placeholder="Description" required />
      <input v-model="amount" type="number" step="0.01" placeholder="Amount" required />
      <select v-model="transactionType" required>
        <option value="IN">Income</option>
        <option value="EX">Expense</option>
      </select>
      <button type="submit">Add Transaction</button>
    </form>
  </template>
  
  <script>
  import { createTransaction } from '@/api';
  
  export default {
    data() {
      return {
        description: '',
        amount: '',
        transactionType: 'IN',
      };
    },
    methods: {
      async submitForm() {
        const data = {
          description: this.description,
          amount: this.amount,
          transaction_type: this.transactionType,
        };
        await createTransaction(data);
        this.$emit('transactionCreated');
        this.description = '';
        this.amount = '';
        this.transactionType = 'IN';
      }
    }
  };
  </script>
  