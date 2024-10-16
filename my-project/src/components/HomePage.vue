<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-500 via-purple-600 to-pink-500 flex items-center justify-center">
    <div class="w-full max-w-4xl p-6 bg-white rounded-lg shadow-2xl transform transition-transform duration-500 hover:scale-105 hover:shadow-3xl">
      <h1 class="text-4xl font-bold text-center text-gray-800 mb-6">Welcome to Your Personal Finance Tracker</h1>
      <p class="text-lg text-gray-600 text-center mb-6">
        Manage your finances effectively with our comprehensive web application. Track transactions, generate summaries, and visualize spending patterns with ease.
      </p>
      <div class="flex justify-center space-x-4">
        <router-link to="http://localhost:8000/login/" class="bg-gradient-to-r from-teal-400 to-teal-600 text-white py-2 px-4 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">Login</router-link>
        <router-link to="http://localhost:8000/register/" class="bg-gradient-to-r from-yellow-400 to-yellow-600 text-white py-2 px-4 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">Register</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
@keyframes gradientAnimation {
  0% {
    background-position: 0% 0%;
  }
  50% {
    background-position: 100% 100%;
  }
  100% {
    background-position: 0% 0%;
  }
}

.bg-gradient-animation {
  background: linear-gradient(45deg, #6e8efb, #a777e3);
  background-size: 200% 200%;
  animation: gradientAnimation 10s ease infinite;
}
</style>
