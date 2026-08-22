import { Routes, Route } from 'react-router-dom';
import LanguageSwitcher from './components/LanguageSwitcher/LanguageSwitcher';
import LanguageTest from './components/LanguageTest/LanguageTest';
import ContactForm from './components/ContactForm/ContactForm';

// Import your page components (ensure these imports exist at the top)
import Home from './pages/Home';
import About from './pages/About';
import Tours from './pages/Tours';
import TourDetails from './pages/TourDetails';
import Gallery from './pages/Gallery';
import News from './pages/News';
import NewsDetails from './pages/NewsDetails';
import Contacts from './pages/Contacts';
import ThankYou from './pages/ThankYou';
import Privacy from './pages/Privacy';
import Terms from './pages/Terms';
import NotFound from './pages/NotFound';

function App() {
  return (
    <>
      {/* Renders on every page */}
      <LanguageSwitcher />

      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/About' element={<About />} />
        <Route path='/Tours' element={<Tours />} />
        <Route path='/TourDetails' element={<TourDetails />} />
        <Route path='/Gallery' element={<Gallery />} />
        <Route path='/News' element={<News />} />
        <Route path='/NewsDetails' element={<NewsDetails />} />
        <Route path='/Contacts' element={<Contacts />} />
        <Route path='/ThankYou' element={<ThankYou />} />
        <Route path='/Privacy' element={<Privacy />} />
        <Route path='/Terms' element={<Terms />} />
        
        {/* 404 */}
        <Route path='*' element={<NotFound />} />
      </Routes>
    </>
  );
}

export default App;