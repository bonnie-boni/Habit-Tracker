@echo off
REM MongoDB Setup Script for Habit Tracker (Windows)

echo.
echo ========================================
echo MongoDB Setup for Habit Tracker
echo ========================================
echo.

REM Step 1: Install dependencies
echo Step 1: Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

REM Step 2: Check MongoDB
echo Step 2: Checking MongoDB...
where mongod >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] MongoDB is installed
    mongod --version
) else (
    echo [WARNING] MongoDB not found
    echo Please download and install MongoDB from:
    echo https://www.mongodb.com/try/download/community
)
echo.

REM Step 3: Run migrations
echo Step 3: Running database migrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERROR: makemigrations failed
    pause
    exit /b 1
)

python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: migrate failed
    pause
    exit /b 1
)
echo [OK] Migrations completed
echo.

REM Step 4: Create superuser
echo Step 4: Create admin user
echo Enter credentials for your admin account:
python manage.py createsuperuser
echo.

REM Step 5: Ready
echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then visit:
echo   http://localhost:8000 (website)
echo   http://localhost:8000/admin (admin panel)
echo.
pause
