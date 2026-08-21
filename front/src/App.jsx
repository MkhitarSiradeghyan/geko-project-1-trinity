import { useGetArticlesQuery } from "./store/api/newsApi";
import News from "./components/News/News";
import { BrowserRouter, Route, Routes } from "react-router-dom";

const App = () => {
 
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/News" element={<News />} />
    </Routes>
    </BrowserRouter>
  );
}

export default App