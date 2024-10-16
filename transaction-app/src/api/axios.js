import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/' // Base URL for your Django API
});

export default instance;
