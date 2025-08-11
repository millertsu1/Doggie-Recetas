/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      '../../templates/**/*.{html,py,js}',
      '../../../recetas/templates/**/*.{html,py,js}',
      '../../../../templates/**/*.{html,py,js}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('daisyui'),
  ],
  daisyui: {
    themes: ["light"],
  },
}