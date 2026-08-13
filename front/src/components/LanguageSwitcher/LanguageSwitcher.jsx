import { useTranslation } from 'react-i18next'
import { languages } from '@/i18n/languages'
import styles from './LanguageSwitcher.module.sass'


export default function LanguageSwitcher() {
  const { i18n } = useTranslation()

  return (
    <select
      className={styles.select}
      value={i18n.resolvedLanguage}
      onChange={(e) => i18n.changeLanguage(e.target.value)}
    >
      {languages.map((lang) => (
        <option key={lang.code} value={lang.code}>
          {lang.name}
        </option>
      ))}
    </select>
  )
}