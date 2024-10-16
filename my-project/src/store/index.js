import { createStore } from 'vuex';
import axios from 'axios';  // Ensure axios is installed

export default createStore({
  state: {
    transactions: [],
  },
  mutations: {
    setTransactions(state, transactions) {
      state.transactions = transactions;
    },
  },
  actions: {
    async fetchTransactions({ commit }) {
      try {
        const response = await axios.get('/api/transactions');
        commit('setTransactions', response.data);
      } catch (error) {
        console.error('Error fetching transactions:', error);
      }
    },
  },
  modules: {},
});
