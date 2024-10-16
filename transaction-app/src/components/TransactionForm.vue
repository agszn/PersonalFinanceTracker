<!-- src/components/TransactionForm.vue -->
<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="amount">Amount:</label>
      <input v-model="form.amount" id="amount" type="number" required />
    </div>
    <div>
      <label for="transaction_type">Transaction Type:</label>
      <select v-model="form.transaction_type" id="transaction_type" required>
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>
    </div>
    <div>
      <label for="description">Description:</label>
      <input v-model="form.description" id="description" type="text" />
    </div>
    <div>
      <label for="date">Date:</label>
      <input v-model="form.date" id="date" type="date" required />
    </div>
    <button type="submit">Add Transaction</button>
  </form>
</template>

<script>
import { createTransaction } from '../services/transactionService';

export default {
  data() {
    return {
      form: {
        amount: '',
        transaction_type: 'income',
        description: '',
        date: '',
      },
    };
  },
  methods: {
    async submitForm() {
      await createTransaction(this.form);
      this.$emit('transaction-created');
    },
  },
};
</script>
