import LanguageSwitcher from './components/LanguageSwitcher/LanguageSwitcher'
import LanguageTest from './components/LanguageTest/LanguageTest'

function App() {
  return(
    <Routes>
      <Route path='/' element = {<Home />} />
      <Route path='/About' element = {<About />} />
      <Route path='/Tours' element = {<Tours />} />
      <Route path='/TourDetails' element = {<TourDetails />} />
      <Route path='/Gallery' element = {<Gallery />} />
      <Route path='/News' element = {<News />} />
      <Route path='/NewsDetails' element = {<NewsDetails />} />
      <Route path='/Contacts' element = {<Contacts />} />
      <Route path='/ThankYou' element = {<ThankYou />} />
      <Route path='/Privacy' element = {<Privacy />} />
      <Route path='/Terms' element = {<Terms />} />
      
      {/*404*/}
      <Route path='*' element = {<NotFound />} />
    </Routes>
  )
}

export default App