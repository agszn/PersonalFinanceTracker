<!-- FinancialSummary.vue -->
<template>
    <div>
      <h2>Financial Summary</h2>
      <p>Total Income: {{ summary.total_income }}</p>
      <p>Total Expenses: {{ summary.total_expenses }}</p>
      <p>Net Balance: {{ summary.net_balance }}</p>
    </div>
  </template>
  
  <script>
  import { getFinancialSummary } from '@/api';
  
  export default {
    data() {
      return {
        summary: {},
      };
    },
    async created() {
      const response = await getFinancialSummary();
      this.summary = response.data;
    }
  };
  </script>
  