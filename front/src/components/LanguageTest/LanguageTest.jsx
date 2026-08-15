import { useTranslation } from 'react-i18next'
import { languages } from '../../i18n/languages'
import styles from './LanguageTest.module.sass'

export default function LanguageTest() {
  const { t, i18n } = useTranslation('home')

  const handleLanguageChange = (event) => {
    i18n.changeLanguage(event.target.value)
  }

  return (
    <div className={styles.container}>
      <h1>{t('title')}</h1>

      <p>{t('subtitle')}</p>

      <select
        value={i18n.language}
        onChange={handleLanguageChange}
      >
        {languages.map((language) => (
          <option
            key={language.code}
            value={language.code}
          >
            {language.name}
          </option>
        ))}
      </select>

      <p>
        Current language:{' '}
        <strong>{i18n.language}</strong>
      </p>
    </div>
  )
}