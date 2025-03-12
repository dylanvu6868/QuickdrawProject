
# QuickDraw AI Project

## 1. Cài đặt
```bash
pip install -r requirements.txt
```

## 2. Chạy Backend API
```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```

## 3. Chạy Frontend
```bash
streamlit run frontend/app.py
```

## 4. Chạy bằng Docker
```bash
docker build -t quickdraw-ai .
docker run -p 8000:8000 quickdraw-ai
```
