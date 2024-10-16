<template>
    <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-400 to-blue-500">
      <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h1 class="text-3xl font-bold mb-4">Contact Us</h1>
        <form>
          <div class="mb-4">
            <label for="name" class="block text-gray-700">Name</label>
            <input type="text" id="name" class="w-full p-2 border rounded-lg">
          </div>
          <div class="mb-4">
            <label for="email" class="block text-gray-700">Email</label>
            <input type="email" id="email" class="w-full p-2 border rounded-lg">
          </div>
          <div class="mb-4">
            <label for="message" class="block text-gray-700">Message</label>
            <textarea id="message" class="w-full p-2 border rounded-lg"></textarea>
          </div>
          <button type="submit" class="bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700">Send</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ContactPage',
  };
  </script>
  