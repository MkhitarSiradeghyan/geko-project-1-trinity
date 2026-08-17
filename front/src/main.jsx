import React from "react";
import App from "./App.jsx";
import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import { store } from "./store/store";
import "./styles/global.sass";
import { BrowserRouter } from "react-router-dom";
import './i18n/config';

createRoot(document.getElementById("root")).render(
    <BrowserRouter>
        <Provider store={store}>
            <App />
        </Provider>
    </BrowserRouter>,
);
