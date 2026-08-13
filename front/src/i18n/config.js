import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'
import LanguageDetector from 'i18next-browser-languagedetector'
import { languageCodes, defaultLanguage } from './languages'

// Vite glob-import: eagerly pulls in every JSON file under locales/*/*.json.
// Adding a new language folder or a new namespace file requires ZERO
// changes to this file — it's picked up automatically on next build/reload.
const modules = import.meta.glob('../locales/*/*.json', { eager: true })

const resources = {}
const namespaceSet = new Set()

for (const path in modules) {
  // path looks like: ../locales/en/common.json
  const match = path.match(/\.\.\/locales\/([^/]+)\/([^/]+)\.json$/)
  if (!match) continue

  const [, lang, namespace] = match
  namespaceSet.add(namespace)
  resources[lang] = resources[lang] || {}
  resources[lang][namespace] = modules[path].default ?? modules[path]
}

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources,
    ns: Array.from(namespaceSet),
    defaultNS: 'common',
    fallbackLng: defaultLanguage,   // never show a broken key — fall back to English
    supportedLngs: languageCodes,   // driven entirely by the control panel

    interpolation: {
      escapeValue: false, // React already escapes output, no need for i18next to do it too
    },

    detection: {
      order: ['localStorage', 'navigator'], // saved choice first, then browser language
      caches: ['localStorage'],
      lookupLocalStorage: 'trinity_lang',
    },

    saveMissing: import.meta.env.DEV,
    missingKeyHandler: (lngs, ns, key) => {
      if (import.meta.env.DEV) {
        console.warn(`[i18n] Missing translation: [${lngs.join(', ')}] ${ns}:${key}`)
      }
    },

    returnEmptyString: false,
  })

export default i18n