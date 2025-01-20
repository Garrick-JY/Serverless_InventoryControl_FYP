module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}', // Adjust paths based on your project structure
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss-primeui'), // Add the PrimeUI plugin here
  ],
};
