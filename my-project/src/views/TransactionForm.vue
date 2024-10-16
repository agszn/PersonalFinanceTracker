// src/components/TransactionForm.vue
<template>
  <form @submit.prevent="submitForm">
    <!-- Your form elements -->
    <button type="submit">Submit</button>
  </form>
</template>

<script>
import { createTransaction } from '@/api';

export default {
  data() {
    return {
      formData: {
        // Your form data
      },
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await createTransaction(this.formData);
        console.log('Transaction created successfully:', response.data);
      } catch (error) {
        console.error('Error creating transaction:', error);
        alert('Failed to submit transaction. Please check the console for more details.');
      }
    },
  },
};
</script>
