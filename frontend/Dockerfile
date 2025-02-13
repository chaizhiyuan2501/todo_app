# Node.js 18 の公式イメージを使用
FROM node:18

# 作業ディレクトリを設定
WORKDIR /app


# TODO: todo project作成後、コメントアウトを外す
COPY ./todo-project/package*.json /app/todo-project/
WORKDIR /app/todo-project
RUN npm install

# Viteの開発サーバーを起動
CMD ["npm", "run", "dev"]

# ポート5173を公開
EXPOSE 5173