<!-- src/pages/TransactionsPage.vue -->
<template>
  <div>
    <h1>Transactions</h1>
    <TransactionForm @transaction-created="fetchTransactions" />
    <TransactionList 
      :transactions="transactions" 
      @transaction-updated="fetchTransactions" 
      @transaction-deleted="fetchTransactions"
    />
  </div>
</template>

<script>
import TransactionList from '../components/TransactionList.vue';
import TransactionForm from '../components/TransactionForm.vue';
import { getTransactions } from '../services/transactionService';

export default {
  components: {
    TransactionList,
    TransactionForm,
  },
  data() {
    return {
      transactions: [],
    };
  },
  created() {
    this.fetchTransactions();
  },
  methods: {
    async fetchTransactions() {
      this.transactions = await getTransactions();
    },
  },
};
</script>
