# Resume-Parser-Backend

- .\venv\Scripts\Activate.ps1
- pip freeze > requirements.txtpip install -r requirements.txt
- uvicorn app.main:app --reload
- http://127.0.0.1:8000/docs

### Folder Structure

resume-parser-api/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── api.py # All API routes
│ ├── services/
│ │ └── parser.py # Your resume parsing logic
│ └── models/
│ └── schemas.py # Pydantic request/response models
│
├── .gitignore
├── requirements.txt
├── venv/
