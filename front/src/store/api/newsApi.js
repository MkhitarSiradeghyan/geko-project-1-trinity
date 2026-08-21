import { apiSlice } from "./apiSlice";

export const newsApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getArticles: builder.query({
      query: () => "news/articles/",
    }),

    getArticle: builder.query({
      query: (slug) => `news/articles/${slug}/`,
    }),

    getCategories: builder.query({
      query: () => "news/categories/",
    }),

    getCategory: builder.query({
      query: (slug) => `news/categories/${slug}/`,
    }),
  }),
});

export const {
  useGetArticlesQuery,
  useGetArticleQuery,
  useGetCategoriesQuery,
  useGetCategoryQuery,
} = newsApi;