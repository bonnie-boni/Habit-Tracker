# Habit Tracker - Django Application

A comprehensive web-based habit transformation platform combining a Django backend with browser extension integration.

## ✨ Features

- **Build & Drop Habits**: Support for both positive habit building and harmful habit elimination
- **Progress Tracking**: Streak counters, session tracking, and detailed analytics
- **Content Library**: Curated articles, videos, and resources
- **Event Tracking**: Detailed event logging for accountability
- **User Profiles**: Customizable profiles with theme preferences
- **Responsive Design**: Dark/light theme toggle with mobile support
- **Dashboard**: Personalized dashboards based on habit type

## 🏗️ Architecture

### Apps Structure
- **users**: User authentication and profile management
- **habits**: Core habit and session management
- **content**: Content library and recommendations
- **analytics**: User statistics and performance tracking
- **events**: Event logging and tracking
- **config**: Django configuration

### Technology Stack
- Backend: Django 6.0+
- Database: SQLite (development), PostgreSQL (production)
- Frontend: Django Templates + Vanilla JavaScript
- Styling: Custom CSS with theme variables

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
cd habit_tracker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django pillow
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application:
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## 📁 Project Structure

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed folder and page information.

## 🛣️ URL Endpoints

### Public Routes
- `/` - Landing page
- `/login/` - User login
- `/logout/` - User logout

### Authenticated Routes
- `/habits/dashboard/` - Main dashboard
- `/habits/onboarding/` - Habit setup wizard
- `/habits/read/` - Reading interface
- `/habits/watch/` - Video player
- `/users/profile/` - Profile settings
- `/analytics/` - Performance analytics
- `/content/` - Content library
- `/events/log/` - Event history

### Admin
- `/admin/` - Django admin panel

## 🗄️ Models Overview

### Habit
- Type: build or drop
- Category: reading, fitness, meditation, learning, addiction, etc.
- Tracking: current_streak, best_streak

### UserProfile
- Extended user information
- Theme preferences
- Profile customization

### Session
- Temporary reading/activity sessions
- Progress tracking
- Completion status

### Event
- Low-level action tracking
- Types: read, blocked, resisted, completed
- Timestamped for accountability

### AnalyticsData
- Aggregated user statistics
- Session counts, reading time, resistances

## 🎨 Theming

### Dark Mode (Default)
- Primary: `#1a1a1a`
- Secondary: `#2d2d2d`

### Light Mode
- Primary: `#ffffff`
- Secondary: `#f5f5f5`

Theme toggle available in navbar and profile settings.

## 🔐 Security Features

- Django CSRF protection
- User authentication required for protected views
- OAuth integration ready (Google)
- Media file handling with proper permissions

## 📊 Available Analytics

- Total sessions completed
- Reading time tracking
- Resistance counts
- Monthly performance breakdown
- Streak trends and milestones
- Insight generation

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 🚧 Development Roadmap

- [ ] Google OAuth integration
- [ ] Advanced analytics with charts
- [ ] PDF and video viewer implementation
- [ ] Browser extension finalization
- [ ] Notification system
- [ ] ML-powered recommendations
- [ ] Mobile app
- [ ] Community features

## 📄 Configuration

### settings.py Key Settings
- `INSTALLED_APPS`: Configured with all required apps
- `TEMPLATES`: Pointing to custom templates folder
- `STATIC_FILES`: Static file configuration
- `MEDIA_FILES`: User uploads handling

## 🤝 Contributing

Development setup:
1. Make changes to models/views
2. Create migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Run tests: `python manage.py test`

## 📝 License

All rights reserved © 2026 Habit Tracker

## 🆘 Support

For issues and questions, refer to the [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed architecture information.

---

**Ready to build better habits?** Start at `http://localhost:8000` 🎯
