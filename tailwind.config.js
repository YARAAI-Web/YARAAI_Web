// tailwind.config.js
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        //Noto Sans KR 웹폰트
        sans: ['"Noto Sans KR"', 'ui-sans-serif', 'system-ui'],
      },
      colors: {
        'yara-border': 'rgba(0,0,0,0.15)',
        'yara-blue': '#1b65fe',
        'yara-gray': '#F2F2F7',
      },
    },
  },
}