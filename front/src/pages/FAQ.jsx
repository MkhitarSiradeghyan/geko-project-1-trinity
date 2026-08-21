import { useGetFaqsQuery } from '../store/api/faqApi';

function FAQ() {
  const { data, isLoading, isError } = useGetFaqsQuery();

  if (isLoading) {
    return <h1>Loading...</h1>;
  }

  if (isError) {
    return <h1>Failed to load FAQ</h1>;
  }

  return (
    <div>
      <h1>FAQ</h1>

      {data?.map((faq) => (
        <div key={faq.id}>
          <h2>{faq.question}</h2>
          <p>{faq.answer}</p>
        </div>
      ))}
    </div>
  );
}

export default FAQ;