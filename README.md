# 🍵 Chai Spice - Django Chai Application

A beautifully crafted Django web application showcasing authentic Indian chai varieties with a clean frontend and robust backend architecture.

![Chai Spice Banner](elaichi_chai.jpeg)

## ✨ Features

- **Chai Collection Display**: Showcase different chai varieties with images and details
- **Dynamic Content Management**: Easy content updates through Django admin
- **Responsive Design**: Clean layout that works on all devices
- **Static File Handling**: Proper management of chai images and CSS/JS files
- **Database Integration**: SQLite database with Django ORM models
- **Image Gallery**: Beautiful display of various chai types

## 📁 Project Structure

```
djangoproject/
├── chai/                           # Main chai application
│   ├── migrations/                 # Database migrations
│   ├── __init__.py
│   ├── admin.py                   # Admin panel configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Database models
│   ├── views.py                   # Business logic
│   ├── urls.py                    # URL routing
│   └── tests.py                   # Test cases
├── chais/                          # Additional app (if any)
├── djangoproject/                 # Project settings folder
│   ├── __init__.py
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration
├── media/                          # Uploaded media files
│   └── images/
│       └── chaitypes/            # Chai type images
├── myapp/                          # Additional application
├── static/                         # Static assets
│   ├── css/                      # Stylesheets
│   ├── js/                       # JavaScript files
│   └── images/                   # Static images
├── templates/                     # HTML templates
│   ├── base.html                 # Base template
│   ├── home.html                 # Homepage
│   └── chai_detail.html          # Chai details page
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── elaichi_chai.jpeg              # Elaichi chai image
├── masala_tea.jpeg                # Masala tea image
├── tea with ginger.png            # Ginger tea image
└── README.md                      # This file
```

## 🎯 Our Chai Collection

### Elaichi Latte  
**Type:** Elaichi Chai  
**Price:** ₹150  
![Elaichi Chai](elaichi_chai.jpeg)  
[View Details](#)

---

### Ginger Spiced Tea  
**Type:** Ginger Chai  
**Price:** ₹140  
![Ginger Tea](tea%20with%20ginger.png)  
[View Details](#)

---

### Masala Chai  
**Type:** Masala Chai  
**Price:** ₹200  
![Masala Chai](masala_tea.jpeg)  
[View Details](#)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vidhi-sys/djangoproject.git
   cd djangoproject
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional - for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🗄️ Database Models

The application uses Django models to manage chai data:

```python
# Example model structure
class ChaiVariety(models.Model):
    name = models.CharField(max_length=100)
    chai_type = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/chaitypes/')
    created_at = models.DateTimeField(auto_now_add=True)
```

## 🎨 Frontend Design

The application features a clean, responsive design with:

- **Homepage**: Displays all chai varieties in a grid layout
- **Chai Cards**: Each chai displayed with image, name, type, and price
- **Responsive Layout**: Adapts to mobile, tablet, and desktop screens
- **Clean Typography**: Easy-to-read text with proper spacing

## ⚙️ Configuration

### Settings Highlights
- **Database**: SQLite (development), can be switched to PostgreSQL/MySQL
- **Media Files**: Stored in `media/` directory
- **Static Files**: Served from `static/` directory
- **Templates**: Located in `templates/` directory
- **Debug Mode**: Enabled for development, disabled for production

### URLs Configuration
```python
# Main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('chai/<int:id>/', views.chai_detail, name='chai_detail'),
]
```

## 🔧 Admin Panel Features

Access the Django admin panel to:

1. **Manage Chai Varieties**
   - Add new chai types
   - Edit existing chai information
   - Upload chai images
   - Set prices and descriptions

2. **User Management**
   - Create and manage users
   - Set permissions and groups
   - Monitor user activity

3. **Database Management**
   - View all database entries
   - Filter and search records
   - Export data if needed

## 📱 Static Files Management

The application properly handles static files:

1. **Development**: Files served directly by Django
2. **Production**: Use `collectstatic` command
3. **Organization**:
   - CSS files in `static/css/`
   - JavaScript in `static/js/`
   - Images in `static/images/`

## 🔄 Deployment Guide

### For Production Deployment:

1. **Update Settings**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

2. **Set up Production Database**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'chaidb',
           'USER': 'username',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

4. **Configure Web Server**
   - Use Gunicorn or uWSGI as application server
   - Configure Nginx or Apache as reverse proxy
   - Set up SSL certificate for HTTPS

### Heroku Deployment (Quick)
```bash
# Add Procfile
web: gunicorn djangoproject.wsgi --log-file -

# Deploy
heroku create chai-spice-app
git push heroku main
heroku run python manage.py migrate
```

## 🐛 Troubleshooting

### Common Issues and Solutions:

1. **Media files not displaying**
   ```python
   # In urls.py, add:
   from django.conf import settings
   from django.conf.urls.static import static
   
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

2. **Static files not loading**
   ```bash
   python manage.py collectstatic
   ```

3. **Database migration errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Port already in use**
   ```bash
   python manage.py runserver 8080
   ```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/new-chai-type
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m "Add new chai variety: Kashmiri Chai"
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/new-chai-type
   ```
6. **Open a Pull Request**

### Contribution Guidelines:
- Follow PEP 8 style guide for Python code
- Add tests for new features
- Update documentation accordingly
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**vidhi-sys**
- GitHub: [@vidhi-sys](https://github.com/vidhi-sys)
- Project Maintainer

## 🙏 Acknowledgments

- Django framework and its amazing community
- Bootstrap for responsive design components
- All chai lovers worldwide for inspiration
- Open source contributors who make projects like this possible

## 🔗 Related Projects

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Packaging Authority](https://pypi.org/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)

## 📞 Support

For support, please:
1. Check the [Issues](https://github.com/vidhi-sys/djangoproject/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide detailed information about the problem

## 📊 Project Status

**Current Version:** 1.0.0  
**Last Updated:** January 2026  
**Django Version:** 4.x  
**Python Version:** 3.8+  
**Active Development:** Yes  

---

© 2026 Chai Spice | Made with 🍵 using Django | Freshly brewed Indian chai | All rights reserved
