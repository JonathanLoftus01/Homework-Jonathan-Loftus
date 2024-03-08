/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/App.css",
    "./src/App.js",
    "./src/App.test.js",
    "./src/index.css",
    "./src/index.js",
    "./src/logo.svg",
    "./src/reportWebVitals.js",
    "./src/setupTest.js"
  ],
  theme: {
    container:{
      center: true,
      padding:{
        Defulat:"1rem",
        sm: "2rem",
        lg: "5rem",
        xl: "8rem",
        "2xl":"12rem"
      },
    },
    extend: {},
  },
  plugins: [],
}

