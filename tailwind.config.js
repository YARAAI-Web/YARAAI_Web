// tailwind.config.js
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        // 경계선: rgba(0,0,0,0.15)
        'yara-border': 'rgba(0,0,0,0.15)',
        // 포인트 블루: #1b65fe
        'yara-blue': '#1b65fe',
        // 배경 그레이: #F2F2F7
        'yara-gray': '#F2F2F7',
      },
    },
  },
}
