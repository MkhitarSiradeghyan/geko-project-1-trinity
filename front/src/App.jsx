<<<<<<< HEAD
import React from 'react'
=======
import React from 'react';
import { useGetToursQuery } from './store/api/toursApi';

function App() {
  const { data: tours, isLoading, isError, error } = useGetToursQuery();

  if (isLoading) return <div>Բեռնվում է...</div>;
  if (isError) return <div>Սխալ: {error?.message || 'Տվյալները չստացվեցին'}</div>;
>>>>>>> feature/setup-redux-rtk-query

const App = () => {
  return (
<<<<<<< HEAD
    <div>App</div>
  )
}

export default App
=======
    <div style={{ padding: '20px' }}>
      <h1>Tours</h1>
      <ul>
        {tours?.map((tour) => (
          <li key={tour.id}>{tour.title || tour.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
>>>>>>> feature/setup-redux-rtk-query
