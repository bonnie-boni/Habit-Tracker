# 🎯 Habit Tracker - Visual Navigation Map

## User Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      PUBLIC ZONE                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  LANDING PAGE (/)                                    │   │
│  │  • App description & features                        │   │
│  │  • Call-to-action buttons                            │   │
│  │  • Privacy & terms footer                            │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                     │ "Get Started"                          │
│                     ↓                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  LOGIN PAGE (/login/)                                │   │
│  │  • Username/password form                            │   │
│  │  • Google OAuth button                               │   │
│  │  • Sign-up link                                      │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                     │ Submit                                 │
│                     ↓                                        │
└─────────────────────┼────────────────────────────────────────┘
                      │
                      ↓
    ┌─────────────────────────────────────────┐
    │      AUTHENTICATED ZONE                 │
    │   (Navbar + Sidebar always visible)     │
    └─────────────────────────────────────────┘
            │
            ├─→ ONBOARDING (/habits/onboarding/) [FIRST TIME ONLY]
            │   • Step 1: Choose build or drop
            │   • Step 2: Select category
            │   • Step 3: Enter habit name
            │   └─→ Redirects to Dashboard
            │
            ├─→ DASHBOARD (multiple types)
            │   ├─→ BUILD HABIT (/habits/dashboard/)
            │   │   • Streak display (🔥)
            │   │   • Quick action button
            │   │   • Recent activity
            │   │   └─→ Read Page
            │   │
            │   └─→ DROP HABIT (/habits/dashboard/)
            │       • Days resisted display
            │       • Motivational message
            │       • Replacement activities
            │       └─→ Video Watch
            │
            ├─→ READ PAGE (/habits/read/)
            │   • PDF/article viewer
            │   • Progress bar
            │   • Navigation buttons
            │   └─→ Back to Dashboard
            │
            ├─→ VIDEO WATCH (/habits/watch/)
            │   • Video player
            │   • Related videos
            │   • Done button
            │   └─→ Back to Dashboard
            │
            ├─→ ANALYTICS (/analytics/)
            │   • Statistics cards
            │   • Monthly breakdown table
            │   • Chart visualizations
            │   • Insight messages
            │   └─→ Back to Dashboard
            │
            ├─→ CONTENT LIBRARY (/content/)
            │   • Content grid
            │   • Filter buttons
            │   • Search functionality
            │   └─→ Content Detail Page
            │
            ├─→ CONTENT DETAIL (/content/<id>/)
            │   • Full content info
            │   • Thumbnail/metadata
            │   • "Open Resource" button
            │   └─→ Back to Library
            │
            ├─→ PROFILE (/users/profile/)
            │   • Display name editor
            │   • Profile picture upload
            │   • Email display
            │   • Theme toggle
            │   • Sign-out button
            │   └─→ Logout → Landing
            │
            └─→ EVENT LOG (/events/log/)
                • Activity timeline
                • Event types (read, blocked, resisted, completed)
                • Timestamps
                └─→ Back to Dashboard

```

---

## Navigation Structure

### TOP NAVBAR
```
┌──────────────────────────────────────────────────────────┐
│ 🎯 Habit Tracker  |  🔥 5 day streak  |  ☀️ 🌙  |  👤  │
└──────────────────────────────────────────────────────────┘
                                            │
                                            └─→ Profile dropdown
                                                • Profile
                                                • Logout
```

### LEFT SIDEBAR
```
┌─────────────────┐
│  📊 Dashboard   │
│  📖 Read/Watch  │
│  📈 Analytics   │
│  ⚙️ Settings    │
└─────────────────┘
```

---

## App Relationships

```
USER (Django)
  │
  ├─── UserProfile (users app)
  │    └─ Theme preference
  │    └─ Profile picture
  │
  ├─── Habit (habits app)
  │    ├─ Type: build | drop
  │    ├─ Category: reading, fitness, etc.
  │    ├─ Current streak
  │    ├─ Best streak
  │    │
  │    └─── Session (habits app)
  │         ├─ Started at
  │         ├─ Progress %
  │         └─ Completed ✓
  │
  ├─── Event (events app)
  │    ├─ Type: read, blocked, resisted, completed
  │    ├─ Habit reference
  │    └─ Timestamp
  │
  ├─── AnalyticsData (analytics app)
  │    ├─ Total sessions
  │    ├─ Total reading time
  │    └─ Total resistances
  │
  └─── MonthlyStats (analytics app)
       ├─ Month
       ├─ Sessions completed
       ├─ Best streak
       └─ Total minutes

CONTENT (independent)
  ├─ Type: article, video, PDF, resource
  ├─ Title & description
  ├─ URL
  ├─ Category
  ├─ Thumbnail
  └─ Duration (optional)
```

---

## Page Components Map

### Landing Page
```
┌────────────────────────────────┐
│      HEADER/HERO SECTION       │
│    • Title & tagline           │
│    • Main CTA button           │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│      FEATURES GRID             │
│  ┌──────┐  ┌──────┐  ┌──────┐ │
│  │Build │  │ Drop │  │Track │ │
│  └──────┘  └──────┘  └──────┘ │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│    SECONDARY CTA SECTION       │
│    "Ready to start?"            │
│    [Get Started Button]         │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│       FOOTER                   │
│    • Privacy Policy            │
│    • Terms of Service          │
└────────────────────────────────┘
```

### Build Habit Dashboard
```
┌────────────────────────────────┐
│    HEADER                      │
│  Habit Name & Subtitle         │
└────────────────────────────────┘
         ↓
┌──────────────┬──────────────────┐
│  🔥 Current  │  ⭐ Best        │
│  Streak: 5   │  Streak: 12     │
└──────────────┴──────────────────┘
         ↓
┌────────────────────────────────┐
│  TODAY'S STATUS                │
│  Keep the momentum going!       │
│  [Start Reading Button]         │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│  RECENT ACTIVITY               │
│  • Yesterday: 30 mins          │
│  • 2 days ago: 45 mins         │
└────────────────────────────────┘
```

### Analytics Dashboard
```
┌────────────────────────────────┐
│  METRICS CARDS                 │
│  ┌──────┐  ┌──────┐  ┌──────┐ │
│  │100   │  │450m  │  │25    │ │
│  │Sess. │  │Read  │  │Days  │ │
│  └──────┘  └──────┘  └──────┘ │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│  CHARTS & VISUALIZATIONS       │
│  [Chart.js/Plotly Chart Area]  │
│  Performance over time         │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│  MONTHLY BREAKDOWN TABLE       │
│  Month | Sessions | Streak     │
│  Dec   │   10     │   8        │
│  Nov   │   15     │   12       │
└────────────────────────────────┘
         ↓
┌────────────────────────────────┐
│  INSIGHTS & MESSAGING          │
│  "You're on a 5-day roll!"     │
└────────────────────────────────┘
```

---

## Data Flow for Event Tracking

```
USER ACTION
    │
    ├─→ Clicks "Start Reading"
    │       │
    │       ↓
    │   Creates Session
    │   (habits.Session)
    │       │
    │       ├─→ Records start_time
    │       ├─→ Initializes progress = 0%
    │       └─→ is_completed = False
    │       │
    │       ↓
    │   Page renders read interface
    │   │
    │   ├─→ User scrolls/reads
    │   ├─→ Progress updates (25%, 50%, 75%, 100%)
    │   │
    │   └─→ User clicks "Complete"
    │           │
    │           ↓
    │       Updates Session
    │       (progress = 100%)
    │       (is_completed = True)
    │       (ended_at = now)
    │           │
    │           ↓
    │       Creates Event
    │       (events.Event)
    │       ├─ event_type = "completed"
    │       ├─ habit = session.habit
    │       └─ created_at = now
    │           │
    │           ↓
    │       Updates Analytics
    │       (analytics.AnalyticsData)
    │       ├─ total_sessions += 1
    │       ├─ total_reading_time += duration
    │       └─ updated_at = now
    │           │
    │           ↓
    │       Updates Streak
    │       (habits.Habit)
    │       ├─ current_streak += 1
    │       └─ best_streak = max(current, best)
```

---

## Responsive Behavior

### Desktop (>1024px)
```
┌───────────────────────────────────────┐
│          NAVBAR                       │
├──────────┬──────────────────────────┤
│ SIDEBAR  │                          │
│          │    MAIN CONTENT          │
│          │                          │
│          │                          │
└──────────┴──────────────────────────┘
```

### Tablet (768px - 1024px)
```
┌───────────────────────────────────────┐
│          NAVBAR (w/ hamburger)        │
├───────────────────────────────────────┤
│                                       │
│         MAIN CONTENT                  │
│      (full width)                     │
│                                       │
│                                       │
└───────────────────────────────────────┘
[Sidebar hidden, toggle with hamburger]
```

### Mobile (<768px)
```
┌────────────────────┐
│ NAVBAR (hamburger) │
├────────────────────┤
│                    │
│  MAIN CONTENT      │
│  (stacked)         │
│                    │
│                    │
└────────────────────┘
[Single column layout]
```

---

## Color System

### Dark Mode (Default)
```
Primary Background:    #1a1a1a  (very dark)
Secondary Background:  #2d2d2d  (dark gray)
Text Primary:          #e5e5e5  (light)
Text Secondary:        #a0a0a0  (muted)
Border:                #3f3f3f  (subtle)
Primary Button:        #3b82f6  (blue)
Success:               #10b981  (green)
```

### Light Mode
```
Primary Background:    #ffffff  (white)
Secondary Background:  #f5f5f5  (light gray)
Text Primary:          #1a1a1a  (dark)
Text Secondary:        #666666  (muted)
Border:                #e0e0e0  (subtle)
Primary Button:        #3b82f6  (blue - same)
Success:               #10b981  (green - same)
```

---

## File Organization Quick Reference

```
TEMPLATES
├── base/
│   └── base.html ..................... Main layout wrapper
├── components/
│   ├── navbar.html ................... Top navigation
│   └── sidebar.html .................. Side navigation
├── pages/
│   ├── landing.html .................. Public homepage
│   ├── onboarding.html ............... Setup wizard
│   ├── dashboard_build.html ........... Build habit dashboard
│   ├── dashboard_drop.html ............ Drop habit dashboard
│   ├── read_page.html ................ Reading interface
│   ├── video_watch.html .............. Video player
│   ├── analytics.html ................ Analytics dashboard
│   ├── profile.html .................. Settings page
│   ├── content_list.html ............. Content browser
│   ├── content_detail.html ........... Content viewer
│   └── event_log.html ................ Activity log
└── auth/
    └── login.html .................... Login page

STATIC
├── css/
│   ├── main.css ...................... Core styles
│   └── theme.css ..................... Color variables
├── js/
│   └── main.js ....................... Interactivity
└── images/
    └── (place logos, icons, etc here)

PYTHON
├── users/
│   └── models.py ..................... UserProfile
├── habits/
│   └── models.py ..................... Habit, Session
├── content/
│   └── models.py ..................... Content
├── analytics/
│   └── models.py ..................... Analytics data
└── events/
    └── models.py ..................... Event tracking
```

---

This visual map helps you understand the complete structure and flow of your Habit Tracker application! 🎯
