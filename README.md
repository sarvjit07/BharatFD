# FAQ Project

A Django-based FAQ system with multilingual support, WYSIWYG editor, caching, and REST API.

## 📂 Project Structure
```
faq_project/                # Root Directory
│── faq_system/             # Main Django Project
│   │── __init__.py
│   │── settings.py         # Django settings (Installed apps, middleware, database, etc.)
│   │── urls.py             # Main URL routing
│   │── wsgi.py
│   │── asgi.py
│
│── faqs/                   # FAQ App
│   │── migrations/         # Database migrations
│   │── __init__.py
│   │── admin.py           # Register models in Django Admin
│   │── apps.py
│   │── models.py          # FAQ Model
│   │── serializers.py     # DRF Serializers
│   │── views.py          # API Views
│   │── urls.py           # App-specific URL routing
│   │── tests.py          # Unit tests
│
│── static/                 # Static files (if needed)
│── templates/              # Templates (if using Django templates)
│── manage.py               # Django CLI management
│── requirements.txt        # Dependencies
│── README.md               # Project Documentation
│── .gitignore              # Ignore unnecessary files
│── Dockerfile              # Docker support (optional)
│── docker-compose.yml      # Docker setup (optional)
```

---

## 🚀 Features
- ✅ Store and manage FAQs
- ✅ CKEditor for rich text answers
- ✅ Google Translate API for automatic translations
- ✅ REST API with language selection (`?lang=hi`)
- ✅ Caching with Redis for fast responses
- ✅ Admin panel for easy management
- ✅ Docker support for easy deployment

---

## 🛠 Installation
```bash
git clone <your-github-repo-url>
cd faq_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📡 API Endpoints
```bash
# Fetch FAQs in English (default)
curl http://127.0.0.1:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://127.0.0.1:8000/api/faqs/?lang=hi

# Fetch FAQs in Bengali
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

---

## 🏗 Deployment
### **Docker**
```bash
docker-compose up --build
```
### **Heroku / AWS / Digital Ocean** *(Coming soon!)*

---

## 🧪 Running Tests
```bash
pytest
```

---

## ✅ Submission Steps
1. **Pushing  all changes to GitHub**
   ```bash
   git add .
   git commit -m "chore: finalize project for submission"
   git push origin main
   ```


---

## 📝 License
MIT License



## Connect 
Name : Sarvjit Kumar Gupta
EmailId : sarvjit1309@gmail.com
