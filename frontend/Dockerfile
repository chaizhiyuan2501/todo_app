# Node.js 18 の公式イメージを使用
FROM node:18

# 作業ディレクトリを設定
WORKDIR /app

# package.json をコピーして依存関係をインストール
COPY package.json .
RUN npm install

# プロジェクトファイルをコピー
COPY . .

# Viteの開発サーバーを起動
CMD ["npm", "run", "dev"]

# ポート5173を公開
EXPOSE 5173