import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';


export default defineConfig({
  plugins: [react()],

  css: {
    preprocessorOptions: {
      sass: {
        additionalData: 
<<<<<<< HEAD
        `@use "@/styles/abstracts/variables" as *\n` +
        `@use "@/styles/abstracts/mixins" as *\n` +
        `@use "@/styles/abstracts/functions" as *\n`

=======
        `@use "@/styles/variables" as *\n` +
        `@use "@/styles/mixins" as *\n` +
        `@use "@/styles/functions" as *\n`
>>>>>>> feature/setup-redux-rtk-query
      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },

});