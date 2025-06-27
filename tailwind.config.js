// tailwind.config.js
module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  safelist: ['mt-20', 'mb-8', 'w-[640px]', 'h-[240px]'],
  theme: {
    extend: {
      colors: {
        'yaraai-light': '#7DAAFF',
      },
    },
  },
  plugins: [],
}
