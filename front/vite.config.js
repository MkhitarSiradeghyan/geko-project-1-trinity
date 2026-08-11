import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';


export default defineConfig({
  plugins: [react()],

  css: {
    preprocessorOptions: {
      sass: {
        additionalData: 
        `@use "@/styles/variables" as *\n` +
        `@use "@/styles/mixins" as *\n` +
        `@use "@/styles/functions" as *\n`
      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },

});