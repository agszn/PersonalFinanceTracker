import transactionService from '../../services/transactionService';

const state = {
  transactions: []
};

const getters = {
  allTransactions: state => state.transactions
};

const actions = {
  async fetchTransactions({ commit }) {
    const { data } = await transactionService.getTransactions();
    commit('setTransactions', data);
  },
  async addTransaction({ dispatch }, transaction) {
    await transactionService.createTransaction(transaction);
    dispatch('fetchTransactions');
  },
  async updateTransaction({ dispatch }, { id, transaction }) {
    await transactionService.updateTransaction(id, transaction);
    dispatch('fetchTransactions');
  },
  async deleteTransaction({ dispatch }, id) {
    await transactionService.deleteTransaction(id);
    dispatch('fetchTransactions');
  }
};

const mutations = {
  setTransactions: (state, transactions) => (state.transactions = transactions)
};

export default {
  state,
  getters,
  actions,
  mutations
};
