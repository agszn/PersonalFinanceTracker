// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import TransactionsPage from '../pages/TransactionsPage.vue';
import TransactionForm from '../components/TransactionForm.vue';

const routes = [
  {
    path: '/transactions',
    name: 'Transactions',
    component: TransactionsPage,
  },
  {
    path: '/transactions/new',
    name: 'NewTransaction',
    component: TransactionForm,
  },
  {
    path: '/transactions/:id/edit',
    name: 'EditTransaction',
    component: TransactionForm,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
