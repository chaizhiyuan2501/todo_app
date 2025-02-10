import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0", // 监听所有 IP
    port: 5173,      // 确保端口固定
    strictPort: true
  }
});