import { apiSlice } from './apiSlice';

export const aboutApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getAboutInfo: builder.query({
      query: () => 'about/',
    }),
  }),
});

export const { useGetAboutInfoQuery } = aboutApi;