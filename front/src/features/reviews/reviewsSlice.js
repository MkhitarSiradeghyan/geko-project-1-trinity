import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/reviews/";


export const fetchReviews = createAsyncThunk(
    "reviews/fetchReviews",
    async ({ tour = "", rating = "" } = {}, thunkAPI) => {
        try {
            const params = {};

            if (tour) {
                params.tour = tour;
            }

            if (rating) {
                params.rating = rating;
            }

            const response = await axios.get(API_URL, {
                params,
            });

            return response.data;
        } catch (error) {
            return thunkAPI.rejectWithValue(
                error.response?.data || "Failed to load reviews"
            );
        }
    }
);



export const createReview = createAsyncThunk(
    "reviews/createReview",
    async (reviewData, thunkAPI) => {
        try {
            const token = localStorage.getItem("access_token");

            const response = await axios.post(
                API_URL,
                reviewData,
                {
                    headers: token
                        ? {
                              Authorization: `Bearer ${token}`,
                              "Content-Type": "application/json",
                          }
                        : {
                              "Content-Type": "application/json",
                          },
                }
            );

            return response.data;
        } catch (error) {
            return thunkAPI.rejectWithValue(
                error.response?.data || "Failed to create review"
            );
        }
    }
);


export const deleteReview = createAsyncThunk(
    "reviews/deleteReview",
    async (id, thunkAPI) => {
        try {
            const token = localStorage.getItem("access_token");

            await axios.delete(`${API_URL}${id}/`, {
                headers: token
                    ? {
                          Authorization: `Bearer ${token}`,
                      }
                    : {},
            });

            return id;
        } catch (error) {
            return thunkAPI.rejectWithValue(
                error.response?.data || "Failed to delete review"
            );
        }
    }
);


const initialState = {
    reviews: [],
    loading: false,
    creating: false,
    deleting: false,
    error: null,
};


const reviewsSlice = createSlice({
    name: "reviews",

    initialState,

    reducers: {},

    extraReducers: (builder) => {
        builder

            
            .addCase(fetchReviews.pending, (state) => {
                state.loading = true;
                state.error = null;
            })

            .addCase(fetchReviews.fulfilled, (state, action) => {
                state.loading = false;
                state.reviews = action.payload;
            })

            .addCase(fetchReviews.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            })

            
            .addCase(createReview.pending, (state) => {
                state.creating = true;
                state.error = null;
            })

            .addCase(createReview.fulfilled, (state, action) => {
                state.creating = false;
                state.reviews.unshift(action.payload);
            })

            .addCase(createReview.rejected, (state, action) => {
                state.creating = false;
                state.error = action.payload;
            })

            
            .addCase(deleteReview.pending, (state) => {
                state.deleting = true;
                state.error = null;
            })

            .addCase(deleteReview.fulfilled, (state, action) => {
                state.deleting = false;

                state.reviews = state.reviews.filter(
                    (review) => review.id !== action.payload
                );
            })

            .addCase(deleteReview.rejected, (state, action) => {
                state.deleting = false;
                state.error = action.payload;
            });
    },
});


export default reviewsSlice.reducer;