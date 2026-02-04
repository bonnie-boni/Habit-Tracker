# 🚀 QUICK START GUIDE

## Getting Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Admin User
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 4: Run Development Server
```bash
python manage.py runserver
```

### Step 5: Access the Application
- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Login Page**: http://localhost:8000/login

---

## 📋 What You Get Out of the Box

### Public Pages
- Landing page with features overview
- Login page with form

### Authenticated Pages
- Onboarding wizard for habit setup
- Dual dashboards (build vs drop habits)
- Reading interface
- Video player page
- Analytics dashboard
- User profile & settings
- Content library browser
- Event activity log

### Components
- Sticky navigation bar with theme toggle
- Collapsible sidebar with app navigation
- Responsive design for all devices

### Database
- User profiles with customization
- Habit tracking with streak counters
- Session management
- Content library
- Event logging
- Monthly statistics

---

## 🎯 Next Steps

### 1. Add Sample Content
Log in to admin panel and add some content:
```
Go to: http://localhost:8000/admin/content/content/add/
```

### 2. Customize Colors
Edit theme colors in `static/css/theme.css`

### 3. Update Templates
Modify HTML templates in `templates/pages/`

### 4. Add Functionality
Create new views in each app's `views.py`

### 5. Add Models
Modify each app's `models.py` and run migrations

---

## 📁 Key Files to Know

| File | Purpose |
|------|---------|
| `config/settings.py` | Django configuration |
| `config/urls.py` | URL routing |
| `templates/base/base.html` | Main template |
| `static/css/main.css` | Main styles |
| `static/css/theme.css` | Theme variables |
| `static/js/main.js` | JavaScript functions |

---

## 🔧 Common Commands

```bash
# Make new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Run tests
python manage.py test

# Collect static files (production)
python manage.py collectstatic

# Create new app
python manage.py startapp appname
```

---

## 🎨 Customization Quick Tips

### Change Default Theme
Edit `static/css/theme.css`:
```css
:root {
    --primary-color: #3b82f6;  /* Change this */
    --bg-primary: #1a1a1a;     /* Change this */
}
```

### Modify Navigation
Edit `templates/components/navbar.html` and `templates/components/sidebar.html`

### Add New Pages
1. Create view in appropriate app's `views.py`
2. Add URL in app's `urls.py`
3. Create template in `templates/pages/`

### Update Homepage
Edit `templates/pages/landing.html`

---

## 🐛 Troubleshooting

### Migrations Error
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Locked
```bash
rm db.sqlite3
python manage.py migrate
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

---

## 📚 Documentation Files

- **README.md** - Project overview
- **PROJECT_STRUCTURE.md** - Detailed architecture
- **TEMPLATE_SUMMARY.md** - Complete feature list
- **QUICK_START.md** - This file

---

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Templates Guide](https://docs.djangoproject.com/en/6.0/topics/templates/)
- [Django Models Reference](https://docs.djangoproject.com/en/6.0/topics/db/models/)
- [Django Views Guide](https://docs.djangoproject.com/en/6.0/topics/http/views/)

---

## 💡 Tips for Success

1. **Start Simple** - Get the basic flow working before adding complex features
2. **Use Django Admin** - It's perfect for managing data during development
3. **Read the Docs** - Django has excellent documentation
4. **Test Early** - Write tests as you build features
5. **Keep it DRY** - Use template inheritance and reusable components

---

## ✅ Deployment Checklist

Before going live:
- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up environment variables
- [ ] Use PostgreSQL instead of SQLite
- [ ] Configure static file serving
- [ ] Set up HTTPS
- [ ] Run tests
- [ ] Configure email backend
- [ ] Set up backup strategy
- [ ] Review security settings

---

## 🆘 Getting Help

1. Check the documentation files in your project
2. Review Django's official documentation
3. Search Stack Overflow for common issues
4. Check the template's GitHub repository (if applicable)

---

**Ready to build? Start the server and begin customizing!** 🎯
