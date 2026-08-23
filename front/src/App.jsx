import ReviewForm from "./components/ReviewForm";
import ReviewList from "./components/ReviewList";

import "./App.css";


function App() {
  return (
    <div className="app">

      <h1>Reviews & Ratings</h1>

      <ReviewForm />

      <ReviewList />

    </div>
  );
}


export default App;