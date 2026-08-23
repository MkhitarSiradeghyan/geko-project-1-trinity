import { configureStore } from "@reduxjs/toolkit";
import reviewsReducer from "../features/reviews/reviewsSlice";

export const store = configureStore({
    reducer: {
        reviews: reviewsReducer,
    },
});