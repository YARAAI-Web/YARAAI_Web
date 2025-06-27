/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  safelist: ['fixed', 'bottom-12', 'right-12', 'z-50', 'mt-20', 'space-y-8'],
  theme: {
    extend: {
      colors: {
        'yaraai-light': '#7DAAFF',
      },
    },
  },
  plugins: [],
}
