import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],

  theme: {
    extend: {
      colors: {
        sonic: {
          50: "#f5f7ff",
          100: "#e9edff",
          200: "#d5dcff",
          300: "#b3bfff",
          400: "#8798ff",
          500: "#6075ff",
          600: "#4657e8",
          700: "#3946c5",
          800: "#303b9e",
          900: "#2d367e"
        }
      },

      borderRadius: {
        sonic: "18px"
      },

      boxShadow: {
        sonic: "0 10px 40px rgba(0, 0, 0, 0.18)"
      }
    }
  },

  plugins: []
};

export default config;
