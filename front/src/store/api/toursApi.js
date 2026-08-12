import { apiSlice } from './apiSlice';

export const toursApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getTours: builder.query({
      query: () => 'tours/',
      providesTags: (result = []) => [
        'Tour',
        ...result.map(({ id }) => ({ type: 'Tour', id })),
      ],
    }),
    getTourById: builder.query({
      query: (id) => `tours/${id}/`,
      providesTags: (result, error, id) => [{ type: 'Tour', id }],
    }),
  }),
});

export const { useGetToursQuery, useGetTourByIdQuery } = toursApi;