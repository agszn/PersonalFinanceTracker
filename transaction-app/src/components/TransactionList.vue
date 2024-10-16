<!-- src/components/TransactionList.vue -->
<template>
  <div>
    <ul>
      <li v-for="transaction in transactions" :key="transaction.id">
        {{ transaction.description }} - {{ transaction.amount }}
        <button @click="deleteTransaction(transaction.id)">Delete</button>
        <router-link :to="`/transactions/${transaction.id}/edit`">Edit</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { deleteTransaction } from '../services/transactionService';

export default {
  props: {
    transactions: Array,
  },
  methods: {
    async deleteTransaction(id) {
      await deleteTransaction(id);
      this.$emit('transaction-deleted');
    },
  },
};
</script>
