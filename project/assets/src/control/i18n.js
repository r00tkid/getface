import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n);

let userLang = navigator.language || navigator.userLanguage;
let baseLocale, fallbackLocale;

if ([
    'ru', 'ru-RU', 'ru-UA', 'uk', 'uk-UA', 'uk-RU', 'be-BY', 'ba-RU'
].find(value => value === userLang)) {
    baseLocale = 'ru';
    fallbackLocale = 'en';
} else {
    baseLocale = 'en';
    fallbackLocale = 'ru';
}

const i18n = new VueI18n({
    locale: baseLocale,
    fallbackLocale: fallbackLocale,
});

Object.defineProperty(Vue.prototype, '$locale', {
    get: function () {
        return i18n.locale;
    },
    set: function (locale) {
        i18n.locale = locale;

        if (locale === 'en') {
            i18n.fallbackLocale = 'ru';
        } else {
            i18n.fallbackLocale = 'en';
        }
    }
});

Object.defineProperty(Vue.prototype, '$fallbackLocale', {
    get: function () {
        return i18n.fallbackLocale;
    }
});

export default i18n;
