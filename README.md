### **コンテナを起動します**
```bash
docker-compose up -d --build
```


### **frontend コンテナを一時的に起動し、シェル(sh)を開く**
```bash
docker-compose run --rm frontend sh
```


### **Vue 3 の依存関係をインストール**
```bash
npm install axios pinia
```



### **backend コンテナを一時的に起動し、シェル(sh)を開く**
```bash
docker-compose run --rm backend bash
```



### **frontend の起動と確認**
```
http://localhost:5173/
```


### **backend の起動と確認**
```
http://127.0.0.1:8000/
```