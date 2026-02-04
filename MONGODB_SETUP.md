# 🗄️ MongoDB Setup Guide for Habit Tracker

## Overview

This project has been configured to use **MongoDB** instead of SQLite. This guide will help you set up MongoDB and get the project running.

---

## 📋 Prerequisites

- Python 3.8+
- MongoDB Server (local or cloud)
- pip package manager

---

## 🚀 Installation Steps

### Step 1: Install MongoDB

#### Option A: Local MongoDB (Windows)

1. **Download MongoDB Community Server**
   - Visit: https://www.mongodb.com/try/download/community
   - Select Windows, MSI, and download

2. **Install MongoDB**
   - Run the installer
   - Choose "Install MongoDB as a Service"
   - Installation completes with MongoDB running in background

3. **Verify Installation**
   ```bash
   mongod --version
   ```

#### Option B: MongoDB Atlas (Cloud - Recommended)

1. **Create MongoDB Atlas Account**
   - Visit: https://www.mongodb.com/cloud/atlas
   - Sign up for free account

2. **Create a Cluster**
   - Click "Build a Database"
   - Select M0 (free tier)
   - Choose your region
   - Create cluster

3. **Get Connection String**
   - Click "Connect"
   - Select "Connect your application"
   - Copy the connection string
   - Replace `<password>` with your database password

4. **Update settings.py**
   ```python
   'host': 'mongodb+srv://username:password@cluster.mongodb.net/habit_tracker_db?retryWrites=true&w=majority'
   ```

---

## 📦 Step 2: Update Python Dependencies

```bash
# Install new requirements
pip install -r requirements.txt
```

This installs:
- **djongo** - Django MongoDB ORM
- **mongoengine** - MongoDB Python driver
- **pymongo** - MongoDB Python connector

---

## ⚙️ Step 3: Update Django Settings

The `config/settings.py` has already been updated with MongoDB configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'habit_tracker_db',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        }
    }
}
```

### For MongoDB Atlas (Cloud):

Edit `config/settings.py` and update the CLIENT section:

```python
'CLIENT': {
    'host': 'mongodb+srv://username:password@cluster.mongodb.net/habit_tracker_db?retryWrites=true&w=majority',
}
```

---

## 🔄 Step 4: Migrate Database

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations to MongoDB
python manage.py migrate
```

---

## 👤 Step 5: Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser account.

---

## 🚀 Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit:
- **Website**: http://localhost:8000
- **Admin**: http://localhost:8000/admin

---

## 📊 MongoDB Connection Verification

### Check Connection in Django Shell

```bash
python manage.py shell
```

```python
from django.db import connection
print(connection.get_connection_params())
```

### Verify MongoDB Collections

If using MongoDB locally:

```bash
# Open MongoDB shell
mongo

# List databases
show dbs

# Use habit_tracker database
use habit_tracker_db

# List collections
show collections

# View data in a collection
db.users_userprofile.find()
```

---

## 🔧 Configuration Options

### settings.py MongoDB Options

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'habit_tracker_db',
        'ENFORCE_SCHEMA': False,  # Allow schema-less documents
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'authSource': 'admin',  # If using authentication
            'username': 'username',  # If using authentication
            'password': 'password',  # If using authentication
            'retryWrites': True,
            'w': 'majority',
        }
    }
}
```

---

## 📝 Models are Ready

All models have been configured to work with MongoDB:

- **UserProfile** - User customization data
- **Habit** - User habits with streaks
- **Session** - Reading/activity sessions
- **Content** - Articles, videos, PDFs
- **AnalyticsData** - User statistics
- **MonthlyStats** - Monthly performance
- **Event** - Activity logging

No model changes are required!

---

## 🐛 Troubleshooting

### Error: "Connection refused"

**Solution**: Make sure MongoDB is running
```bash
# Check if MongoDB is running (Windows)
# Or start it manually
mongod
```

### Error: "No module named 'djongo'"

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Error: "Authentication failed"

**Solution**: Check your MongoDB credentials
- Verify username and password
- Check if authSource is correct (usually 'admin')
- Ensure user has access to the database

### Error: "Database name contains invalid characters"

**Solution**: Use only alphanumeric characters and underscores in database name

---

## 🔒 Security Best Practices

### Local Development
- Use local MongoDB on localhost
- No authentication required

### Production (MongoDB Atlas)
- Enable IP Whitelist
- Use strong passwords
- Enable SSL/TLS
- Use VPC/Network Access

---

## 🔄 Switching Back to SQLite

If you need to switch back to SQLite:

1. **Update settings.py**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

2. **Reinstall dependencies**:
```bash
pip uninstall djongo mongoengine pymongo
pip install Django==6.0.2
```

3. **Migrate**:
```bash
python manage.py migrate
```

---

## 📚 Useful MongoDB Commands

```bash
# Start MongoDB (if not running as service)
mongod

# Connect to MongoDB shell
mongo

# Show all databases
show dbs

# Create/use database
use habit_tracker_db

# Show collections
show collections

# View all documents in collection
db.users_userprofile.find()

# View with pretty format
db.users_userprofile.find().pretty()

# Count documents
db.users_userprofile.count()

# Find specific document
db.users_userprofile.findOne({_id: ObjectId("...")})

# Delete database
db.dropDatabase()
```

---

## 🎯 Next Steps

1. ✅ Install MongoDB
2. ✅ Install Python dependencies (`pip install -r requirements.txt`)
3. ✅ Update connection string if using MongoDB Atlas
4. ✅ Run migrations (`python manage.py migrate`)
5. ✅ Create superuser (`python manage.py createsuperuser`)
6. ✅ Start server (`python manage.py runserver`)
7. ✅ Access app at http://localhost:8000

---

## 📞 Resources

- [MongoDB Documentation](https://docs.mongodb.com/)
- [Djongo Documentation](https://djongo.readthedocs.io/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)

---

## ✅ Verification Checklist

- [ ] MongoDB installed and running
- [ ] Python dependencies installed (`pip install -r requirements.txt`)
- [ ] Database connection string configured in settings.py
- [ ] Migrations applied (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)
- [ ] Development server running (`python manage.py runserver`)
- [ ] Admin dashboard accessible at http://localhost:8000/admin

---

**MongoDB is now configured and ready to use!** 🎉

For questions, refer to the MongoDB and Djongo documentation linked above.
