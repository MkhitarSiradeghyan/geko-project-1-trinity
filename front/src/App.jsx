import { BrowserRouter, Routes, Route } from 'react-router-dom'
import MainLayout from './layouts/MainLayout/MainLayout'
import LanguageTest from './components/LanguageTest/LanguageTest'

function App() {
  return (
    <BrowserRouter>
      <LanguageTest />

      <Routes>
        <Route element={<MainLayout />}>
          {/* your routes */}
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App