import { apiSlice } from './apiSlice';

export const faqApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getFaqs: builder.query({
      query: () => 'faq/',
      providesTags: (result = []) => [
        'FAQ',
        ...result.map(({ id }) => ({ type: 'FAQ', id })),
      ],
    }),

    getFaqById: builder.query({
      query: (id) => `faq/${id}/`,
      providesTags: (result, error, id) => [{ type: 'FAQ', id }],
    }),
  }),
});

export const {
  useGetFaqsQuery,
  useGetFaqByIdQuery,
} = faqApi;