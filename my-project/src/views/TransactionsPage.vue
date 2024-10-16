<template>
    <div>
      <h1>Add Transaction</h1>
      <TransactionForm /> <!-- Use the TransactionForm component here -->
      <div>
        <h2>Transaction List</h2>
        <ul>
          <li v-for="transaction in transactions" :key="transaction.description">
            {{ transaction.description }}: ${{ transaction.amount }} ({{ transaction.type }})
          </li>
        </ul>
        <h2>Financial Summary</h2>
        <p>Total Income: ${{ totalIncome }}</p>
        <p>Total Expenses: ${{ totalExpenses }}</p>
        <p>Balance: ${{ balance }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import TransactionForm from '@/components/TransactionForm.vue';
  
  export default {
    components: {
      TransactionForm
    },
    computed: {
      transactions() {
        return this.$store.getters.allTransactions;
      },
      totalIncome() {
        return this.$store.getters.totalIncome;
      },
      totalExpenses() {
        return this.$store.getters.totalExpenses;
      },
      balance() {
        return this.$store.getters.balance;
      }
    }
  };
  </script>
  