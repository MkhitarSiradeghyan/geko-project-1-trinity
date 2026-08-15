import { useTranslation } from 'react-i18next'
import { languages } from '../../i18n/languages'
import styles from './LanguageSwitcher.module.sass'

function LanguageSwitcher() {
  const { i18n } = useTranslation()

  return (
    <select
      value={i18n.language}
      onChange={(e) => i18n.changeLanguage(e.target.value)}
    >
      {languages.map(({ code, name }) => (
        <option key={code} value={code}>
          {name}
        </option>
      ))}
    </select>
  )
}

export default LanguageSwitcher