module.exports = {
  theme: {
    extend: {
      colors: {
        'yaraai-light': '#7DAAFF',
      },
      borderColor: (theme) => ({
        ...theme('colors'),
        'yaraai-light': theme('colors.yaraai-light'),
      }),
    },
  },
}
