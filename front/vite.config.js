import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';


export default defineConfig({
  plugins: [react()],

  css: {
    preprocessorOptions: {
      sass: {
        additionalData: 
        `@use "@/styles/abstracts/variables" as *\n` +
        `@use "@/styles/abstracts/mixins" as *\n` +
        `@use "@/styles/abstracts/functions" as *\n`

      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },

});