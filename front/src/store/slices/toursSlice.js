import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  tours: [],
  loading: false,
  error: null,
};

const toursSlice = createSlice({
  name: "tours",
  initialState,
  reducers: {},
});

export default toursSlice.reducer;