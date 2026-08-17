import { Outlet } from 'react-router-dom'
import LanguageSwitcher from '../../components/LanguageSwitcher/LanguageSwitcher'
import styles from './MainLayout.module.sass'

function MainLayout() {
  return (
    <div className={styles.layout}>
      <header className={styles.header}>
        <LanguageSwitcher />
      </header>

      <main className={styles.main}>
        <Outlet />
      </main>

      <footer className={styles.footer}>
        {/* footer content later */}
      </footer>
    </div>
  )
}

export default MainLayout