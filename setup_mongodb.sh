#!/bin/bash
# MongoDB Setup Script for Habit Tracker

echo "🗄️  Habit Tracker - MongoDB Setup"
echo "=================================="
echo ""

# Step 1: Install dependencies
echo "📦 Step 1: Installing Python dependencies..."
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Step 2: Check MongoDB
echo "🔍 Step 2: Checking MongoDB..."
if command -v mongod &> /dev/null; then
    echo "✅ MongoDB is installed"
    mongod --version
else
    echo "⚠️  MongoDB not found. Please install MongoDB first."
    echo "Download from: https://www.mongodb.com/try/download/community"
fi
echo ""

# Step 3: Run migrations
echo "🔄 Step 3: Running database migrations..."
python manage.py makemigrations
python manage.py migrate
echo "✅ Migrations completed"
echo ""

# Step 4: Create superuser
echo "👤 Step 4: Create admin user"
python manage.py createsuperuser
echo ""

# Step 5: Ready
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the server, run:"
echo "   python manage.py runserver"
echo ""
echo "Then visit:"
echo "   http://localhost:8000 (website)"
echo "   http://localhost:8000/admin (admin panel)"
