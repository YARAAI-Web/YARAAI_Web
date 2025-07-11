// vite.config.ts

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/reports': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        secure: false,
      },
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        secure: false,
      },
      '/static': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        secure: false,
      },
      // Suricata 룰 JSON 다운로드용 proxy
      '/meta_json': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        secure: false,
        // 경로 재작성 없이 그대로 전달
        rewrite: (path) => path,
      },
    },
    watch: {
      ignored: [
        // ignore all files under backend/services/CAPA/capa_json
        path.resolve(__dirname, 'backend/services/CAPA/capa_json/**'),
      ],
    },
  },
})
