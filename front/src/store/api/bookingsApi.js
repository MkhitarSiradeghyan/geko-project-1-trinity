import { apiSlice } from './apiSlice';

export const bookingsApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getBookings: builder.query({
      query: () => 'bookings/',
      providesTags: ['Booking'],
    }),
    createBooking: builder.mutation({
      query: (newBooking) => ({
        url: 'bookings/',
        method: 'POST',
        body: newBooking,
      }),
      invalidatesTags: ['Booking', 'Tour'],
    }),
  }),
});

export const { useGetBookingsQuery, useCreateBookingMutation } = bookingsApi;