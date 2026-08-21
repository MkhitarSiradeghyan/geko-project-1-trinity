import { useGetArticlesQuery } from "../../store/api/newsApi";

function News() {
  const {
    data: articles,
    isLoading,
    isError,
  } = useGetArticlesQuery();

  if (isLoading) {
    return <div>Загрузка новостей...</div>;
  }

  if (isError) {
    return <div>Не удалось загрузить новости</div>;
  }

  return (
    <section>
      <h1>Новости</h1>

      {articles?.map((article) => (
        <article key={article.id}>
          <h2>{article.title}</h2>

          {article.cover_image && (
            <img
              src={article.cover_image}
              alt={article.title}
            />
          )}

          <p>{article.short_description}</p>
        </article>
      ))}
    </section>
  );
}

export default News;