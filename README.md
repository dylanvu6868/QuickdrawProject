# QuickDraw AI Project

## 1. Introduction
QuickDraw AI is an application that recognizes hand-drawn sketches from a camera and predicts the object being drawn. The project uses **FastAPI** for the backend, **Streamlit** for the frontend, and **TensorFlow** to train the sketch recognition model.

---

## 2. Installation
Requires **Python 3.9 or 3.10**. If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### 2.1. Install Required Libraries
```bash
pip install -r requirements.txt
```

---

## 3. Create a Virtual Environment
### 3.1. On Windows (Command Prompt / PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
```
### 3.2. On macOS/Linux (Terminal)
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Run Backend API
```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000
```
📌 The API will be available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 5. Run Frontend
```bash
streamlit run frontend/app.py
```
📌 The application will be available at: [http://localhost:8501](http://localhost:8501)

---

## 6. Run with Docker (Optional)
If you want to run the project using Docker, ensure **Docker** is installed, then execute:
```bash
docker build -t quickdraw-ai .
docker run -p 8000:8000 quickdraw-ai
```

---

## 7. Train the Model (Optional)
To retrain the model from scratch, run:
```bash
python train_model.py
```
The trained model will be saved in the **quickdraw_model/** directory.

---

## 8. Notes
- The project requires **Python 3.9 or 3.10** (not compatible with Python 3.12 or later).
- If you encounter TensorFlow installation issues, try:
  ```bash
  pip install tensorflow==2.12.0
  ```

---

## 9. Exit the Virtual Environment
When finished, you can deactivate the virtual environment with:
```bash
deactivate
```

Good luck! 🚀
