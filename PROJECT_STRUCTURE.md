# Habit Tracker - Project Structure Guide

## 📁 Directory Structure

```
habit_tracker/
├── manage.py                          # Django management commands
├── db.sqlite3                         # SQLite database (development)
│
├── config/                            # Django configuration
│   ├── __init__.py
│   ├── settings.py                   # Settings (apps, middleware, db, static files)
│   ├── urls.py                       # Main URL routing
│   ├── asgi.py                       # ASGI configuration
│   └── wsgi.py                       # WSGI configuration
│
├── users/                             # User authentication & profiles
│   ├── __init__.py
│   ├── models.py                     # UserProfile model
│   ├── views.py                      # Profile and logout views
│   ├── urls.py                       # User app URLs
│   ├── admin.py                      # Django admin configuration
│   ├── apps.py                       # App configuration
│   └── migrations/
│
├── habits/                            # Core habit management
│   ├── __init__.py
│   ├── models.py                     # Habit, Session models
│   ├── views.py                      # Dashboard, onboarding, read, watch
│   ├── urls.py                       # Habit app URLs
│   ├── admin.py                      # Django admin
│   ├── apps.py                       # App configuration
│   └── migrations/
│
├── content/                           # Content library management
│   ├── __init__.py
│   ├── models.py                     # Content model
│   ├── views.py                      # Content list and detail views
│   ├── urls.py                       # Content app URLs
│   ├── admin.py                      # Django admin
│   ├── apps.py                       # App configuration
│   └── migrations/
│
├── analytics/                         # User analytics & statistics
│   ├── __init__.py
│   ├── models.py                     # AnalyticsData, MonthlyStats
│   ├── views.py                      # Analytics dashboard
│   ├── urls.py                       # Analytics URLs
│   ├── admin.py                      # Django admin
│   ├── apps.py                       # App configuration
│   └── migrations/
│
├── events/                            # Event tracking (source of truth)
│   ├── __init__.py
│   ├── models.py                     # Event model
│   ├── views.py                      # Event log view
│   ├── urls.py                       # Events URLs
│   ├── admin.py                      # Django admin
│   ├── apps.py                       # App configuration
│   └── migrations/
│
├── my_app/                            # Original app (custom features)
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
│
├── templates/                         # Django templates
│   ├── base/
│   │   └── base.html                 # Main layout template
│   ├── components/
│   │   ├── navbar.html               # Navigation bar
│   │   └── sidebar.html              # Sidebar navigation
│   ├── pages/
│   │   ├── landing.html              # Public landing page
│   │   ├── onboarding.html           # Habit setup
│   │   ├── dashboard_build.html      # Build habit dashboard
│   │   ├── dashboard_drop.html       # Drop habit dashboard
│   │   ├── read_page.html            # E-reader page
│   │   ├── video_watch.html          # Video player page
│   │   ├── analytics.html            # Analytics dashboard
│   │   └── profile.html              # Profile & settings
│   └── auth/
│       └── login.html                # Login page
│
├── static/                            # Static files
│   ├── css/
│   │   ├── main.css                  # Main stylesheet
│   │   └── theme.css                 # Theme variables
│   ├── js/
│   │   └── main.js                   # Main JavaScript
│   └── images/                        # Images & icons
│
├── extension/                         # Browser extension
│   └── (Chrome extension files)
│
└── README.md                          # Project documentation
```

---

## 🗄️ Database Models

### Users App
- **UserProfile**: Extended user information (display name, profile picture, theme preference)

### Habits App
- **Habit**: User habits with type (build/drop), category, and streak tracking
- **Session**: Reading/activity sessions with progress tracking

### Content App
- **Content**: Articles, videos, PDFs, and resources for habit support

### Analytics App
- **AnalyticsData**: Aggregated user statistics
- **MonthlyStats**: Monthly performance tracking

### Events App
- **Event**: Low-level event tracking (read, blocked, resisted, completed)

---

## 🛣️ URL Routing Map

```
/                           → Landing page
/login/                     → Login page
/logout/                    → Logout

/habits/dashboard/          → Main dashboard
/habits/onboarding/         → Habit setup
/habits/read/               → Reading page
/habits/watch/              → Video watch page

/users/profile/             → User profile & settings

/analytics/                 → Analytics dashboard

/content/                   → Content library
/content/<id>/              → Content detail

/events/log/                → Event log

/admin/                     → Django admin
```

---

## 📝 Page Descriptions

### 1. **Landing Page** (`landing.html`)
- Public entry point
- Features overview
- Call-to-action for sign-up
- Privacy & terms links

### 2. **Login Page** (`auth/login.html`)
- Username/password login
- Google OAuth integration (placeholder)
- Sign-up redirect

### 3. **Onboarding** (`onboarding.html`)
- Habit type selection (build/drop)
- Category selection
- Initial habit setup
- Progress indicator

### 4. **Build Habit Dashboard** (`dashboard_build.html`)
- Current streak display
- Best streak milestone
- Quick action button
- Recent activity

### 5. **Drop Habit Dashboard** (`dashboard_drop.html`)
- Days resisted counter
- Best streak
- Motivational messaging
- Replacement activity suggestions

### 6. **Read Page** (`read_page.html`)
- PDF/article viewer
- Progress percentage
- Navigation controls
- Session tracking

### 7. **Video Watch** (`video_watch.html`)
- Embedded video player
- Progress tracking
- Related videos
- Completion action

### 8. **Analytics** (`analytics.html`)
- Total sessions count
- Reading time tracker
- Resistance count
- Monthly breakdown table
- Chart visualizations
- Performance insights

### 9. **Profile** (`profile.html`)
- Display name editor
- Profile picture upload
- Email display
- Theme toggle
- Sign-out button

---

## 🧩 Component Structure

### Navbar (`components/navbar.html`)
- App logo
- Streak indicator
- Theme toggle
- Profile dropdown
- Sticky on scroll
- Responsive hamburger menu

### Sidebar (`components/sidebar.html`)
- Dashboard link
- Read/Watch link
- Analytics link
- Settings link
- Icon + text navigation
- Collapsible on mobile

---

## 🎨 Styling System

### Theme Variables (`static/css/theme.css`)
- **Dark Mode** (default)
  - Primary background: `#1a1a1a`
  - Secondary background: `#2d2d2d`
  - Text: `#e5e5e5`

- **Light Mode**
  - Primary background: `#ffffff`
  - Secondary background: `#f5f5f5`
  - Text: `#1a1a1a`

### Main Styles (`static/css/main.css`)
- Navbar styling
- Sidebar styling
- Button styles
- Form styling
- Card components
- Grid layouts
- Responsive breakpoints

---

## 🔄 User Flow

```
1. User lands on landing page
   ↓
2. Clicks "Get Started" → Login page
   ↓
3. Authenticates (username/OAuth)
   ↓
4. Redirected to onboarding (if first time)
   ↓
5. Selects habit type & category
   ↓
6. Taken to dashboard based on habit type
   ↓
7. Can navigate to:
   - Read/Watch (activity)
   - Analytics (progress)
   - Profile (settings)
```

---

## 🚀 Getting Started

1. Install dependencies:
   ```bash
   pip install django pillow
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run development server:
   ```bash
   python manage.py runserver
   ```

5. Access:
   - App: http://localhost:8000
   - Admin: http://localhost:8000/admin

---

## 📦 Key Features Implemented

✅ Multi-app Django architecture
✅ User authentication & profiles
✅ Habit management (build & drop)
✅ Content library
✅ Event tracking
✅ Analytics dashboard
✅ Responsive templates
✅ Dark/Light theme toggle
✅ Static file management
✅ Admin interface

---

## 🔮 Next Steps

1. Implement Google OAuth integration
2. Add PDF/video viewer functionality
3. Create real analytics visualizations
4. Build browser extension
5. Add notification system
6. Implement recommendation engine
7. Add user testing & validation

---

Generated with Habit Tracker Template System
