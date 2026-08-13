<<<<<<< HEAD
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './styles/global.sass'

createRoot(document.getElementById('root')).render(
    <App />
)
=======
import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './store/store';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);
>>>>>>> feature/setup-redux-rtk-query
