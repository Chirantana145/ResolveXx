🏛️ SAKSHAM - Smart Civic Issue Reporting System
SAKSHAM Logo Version License

SC-village Amenities & Knowledge System for Holistic Assessment and Monitoring

A comprehensive Progressive Web App (PWA) for rural development issue reporting and management, built for the Smart India Hackathon.

Live Demo · Report Bug · Request Feature

📖 Table of Contents
About the Project
Key Features
How to Access Features
Tech Stack
Installation
Configuration
Database Setup
Deployment
User Roles
Keyboard Shortcuts
API Reference
Contributing
🎯 About the Project
SAKSHAM is a citizen-centric platform designed to bridge the gap between rural communities and local governance. It enables citizens to report civic issues (roads, water supply, sanitation, electricity, etc.) with photo evidence and GPS location, while providing government staff and administrators with powerful tools to track, assign, and resolve these issues efficiently.

The Problem
Citizens struggle to report village-level issues effectively
No centralized tracking of civic complaints
Lack of transparency in issue resolution
Language barriers for rural users
No accountability with SLA tracking
Our Solution
Easy-to-use mobile-friendly interface
Multi-language support (11 Indian languages)
Real-time status tracking with notifications
AI-powered chatbot assistance
Staff assignment with SLA tracking
Comprehensive admin dashboard with analytics
✨ Key Features
🌓 Dark/Light Mode Toggle
Switch between light and dark themes for comfortable viewing.

📱 Progressive Web App (PWA)
Install on your device for offline access and native app experience.

🤖 AI Chatbot (Gemini)
Get instant answers about government schemes, report status, and platform help.

🗣️ Voice Input
Speak to fill forms and chat with the AI assistant.

📍 GPS Location
Auto-detect location or pick from interactive map.

📸 Photo Upload
Attach evidence photos with automatic compression.

💬 In-App Messaging
Direct communication between citizens and staff.

⏱️ SLA Tracking
Priority-based deadlines with visual indicators.

🌐 Multilingual (11 Languages)
English, Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Odia.

♿ Accessibility (WCAG 2.1)
Skip links, keyboard navigation, screen reader support, high contrast mode.

📊 Analytics Dashboard
Charts, statistics, and exportable reports (PDF/Excel).

🔔 Real-time Notifications
Instant updates when your report status changes.

📴 Offline Support
Queue reports when offline, auto-sync when back online.

🚀 How to Access Features
🌓 Dark/Light Mode
Method	Action
Button	Click the 🌙 Dark / ☀️ Light button in the top navigation bar
Auto	System preference is auto-detected on first visit
Persistent	Your preference is saved and remembered
The toggle appears on all pages in the navigation bar.

How it works:

Light Mode (Default): White background with dark text, optimized for daylight viewing
Dark Mode: Dark background with light text, reduces eye strain in low-light conditions
Click the button to switch instantly - no page reload required!
🌐 Language Selection
Method	Action
Selector	Click 🌐 English dropdown in the navigation bar
Choose	Select from 11 available languages
Auto	Browser language is auto-detected initially
Supported Languages:

🇬🇧 English
🇮🇳 हिन्दी (Hindi)
🇮🇳 தமிழ் (Tamil)
🇮🇳 తెలుగు (Telugu)
🇮🇳 বাংলা (Bengali)
🇮🇳 मराठी (Marathi)
🇮🇳 ગુજરાતી (Gujarati)
🇮🇳 ಕನ್ನಡ (Kannada)
🇮🇳 മലയാളം (Malayalam)
🇮🇳 ਪੰਜਾਬੀ (Punjabi)
🇮🇳 ଓଡ଼ିଆ (Odia)
♿ Accessibility Settings
Method	Action
Button	Click the ♿ button (bottom-left floating button)
Shortcut	Press Alt + 0
Available Settings:

🔤 Text Size: Adjust from 80% to 150%
🎨 High Contrast: Enhanced visibility mode
🚫 Reduce Motion: Disable animations
🎯 Focus Indicators: Enhanced keyboard focus
💬 In-App Messaging
Method	Action
Button	Click the 💬 floating button (bottom-right)
Tabs	Switch between Inbox, Sent, and Assignments
Features:

📥 Inbox: Receive messages from staff/admin
📤 Sent: View your sent messages
👥 Assignments: (Staff/Admin) View assigned reports with SLA
✏️ Compose: Send new messages to staff
SLA Priority Levels:

Priority	Deadline	Badge Color
Urgent	4 hours	🔴 Red
High	1 day	🟠 Orange
Medium	3 days	🟡 Yellow
Low	7 days	🟢 Green
🤖 AI Chatbot
Method	Action
Button	Click the 💬 Chat button on the landing page
Voice	Click the 🎤 microphone for voice input
Ask About:

Government schemes (PM Awas Yojana, MGNREGA, etc.)
How to submit a report
Track your report status
Platform navigation help
📝 Submit a Report (Citizens)
Login as Citizen
Click "Report Issue" or "New Report"
Fill the form:
Select Category (Water, Roads, Electricity, etc.)
Select Subcategory
Write Description (min 20 characters)
Upload Photo (optional but recommended)
Mark Location on map or use GPS
Click Submit
Categories Available:

💧 Water Supply
🛣️ Roads & Infrastructure
⚡ Electricity
🚽 Sanitation
🏥 Health Services
📚 Education
🏗️ Construction
🌳 Environment
📱 Other
📊 Admin Dashboard
Feature	How to Access
View All Reports	Login as Admin → Dashboard shows all reports
Assign to Staff	Click "Assign" on any report → Select staff + priority
View Statistics	Dashboard shows charts and metrics
Export Data	Click "Export PDF" or "Export Excel"
Manage Users	Settings → User Management
Dashboard Sections:

📈 Statistics Cards: Total, Pending, In Progress, Resolved counts
📊 Charts: Category distribution, Status breakdown, Trends
📋 Reports Table: Sortable, filterable list of all reports
🗺️ Map View: Geographic distribution of issues
👷 Staff Dashboard
Feature	How to Access
View Assigned	Login as Staff → See assigned reports
Update Status	Click report → Change status → Save
SLA Tracking	Color indicators show deadline status
Message Citizen	Click message icon on report
Status Options:

⏳ Pending
👤 Assigned
🔄 In Progress
✅ Resolved
❌ Rejected
📱 Install as App (PWA)
On Mobile (Android/iOS):

Open the website in Chrome/Safari
Tap the browser menu (⋮ or share icon)
Select "Add to Home Screen" / "Install App"
On Desktop (Chrome/Edge):

Look for the install icon (⊕) in the address bar
Click "Install"
Benefits:

Works offline
Faster loading
Push notifications
Full-screen experience
⌨️ Keyboard Shortcuts
Shortcut	Action
Alt + 1	Go to Home
Alt + 2	Go to My Reports
Alt + 3	New Report Form
Alt + 0	Accessibility Settings
Escape	Close modal/overlay
Tab	Navigate forward
Shift + Tab	Navigate backward
🛠️ Tech Stack
Category	Technology
Frontend	HTML5, CSS3, Vanilla JavaScript
Backend	Supabase (PostgreSQL + Auth + Realtime)
AI/ML	Google Gemini 2.0 Flash
Maps	Leaflet.js + OpenStreetMap
Charts	Chart.js
Hosting	Vercel (Serverless)
PWA	Service Worker + Web App Manifest
📦 Installation
Prerequisites
Node.js 18+ (for local development)
Git
Supabase account
Google AI Studio account (for Gemini API)
1. Clone the Repository
git clone https://github.com/Bhanutejayadalla/saksham-civic-report.git
cd saksham-civic-report
2. Install Dependencies (Optional)
npm install
3. Start Local Server
# Using Python
python -m http.server 8080

# Using Node.js
npx serve -p 8080

# Using VS Code Live Server
# Right-click index.html → "Open with Live Server"
4. Open in Browser
http://localhost:8080
⚙️ Configuration
Environment Variables (for Vercel)
Set these in your Vercel project settings → Environment Variables:

Variable	Description
SUPABASE_URL	Your Supabase project URL
SUPABASE_ANON_KEY	Supabase anonymous/public key
GEMINI_API_KEY	Google Gemini API key
Local Development
Create js/config.js (this file is auto-generated during Vercel build):

const Config = {
    supabase: {
        url: 'https://your-project.supabase.co',
        anonKey: 'your-anon-key'
    },
    gemini: {
        apiKey: 'your-gemini-api-key',
        model: 'gemini-2.0-flash',
        endpoint: 'https://generativelanguage.googleapis.com/v1beta/models',
        rateLimitPerMinute: 10,
        minRequestInterval: 4000
    },
    app: {
        name: 'SAKSHAM',
        version: '1.0.0',
        environment: 'development'
    }
};
🗄️ Database Setup
Required Tables
Run these SQL commands in Supabase SQL Editor:

-- Users/Profiles table
CREATE TABLE profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id),
    full_name TEXT,
    role TEXT DEFAULT 'citizen',
    department TEXT,
    phone TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Reports table
CREATE TABLE reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id),
    category TEXT NOT NULL,
    subcategory TEXT,
    description TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'medium',
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    address TEXT,
    image_url TEXT,
    assigned_to UUID REFERENCES profiles(id),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Messages table
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    from_user_id UUID REFERENCES profiles(id),
    from_name TEXT,
    to_user_id UUID REFERENCES profiles(id),
    to_name TEXT,
    subject TEXT,
    body TEXT,
    report_id UUID REFERENCES reports(id),
    read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Report Assignments table (for SLA tracking)
CREATE TABLE report_assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id UUID REFERENCES reports(id),
    assigned_to UUID REFERENCES profiles(id),
    assigned_by UUID REFERENCES profiles(id),
    priority TEXT,
    notes TEXT,
    sla_deadline TIMESTAMP,
    completed_at TIMESTAMP,
    status TEXT DEFAULT 'assigned',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Categories table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    department_mapping TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Departments table
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    contact_email TEXT,
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE reports ENABLE ROW LEVEL SECURITY;
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE report_assignments ENABLE ROW LEVEL SECURITY;

-- RLS Policies (example)
CREATE POLICY "Users can view own profile" ON profiles
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Citizens can view own reports" ON reports
    FOR SELECT USING (auth.uid() = user_id OR 
        EXISTS (SELECT 1 FROM profiles WHERE id = auth.uid() AND role IN ('admin', 'staff')));
🚀 Deployment
Deploy to Vercel
Push code to GitHub

git add .
git commit -m "Initial commit"
git push origin main
Go to vercel.com

Import your GitHub repository

Click "New Project"
Select your repository
Click "Import"
Add environment variables

Go to Project Settings → Environment Variables
Add SUPABASE_URL, SUPABASE_ANON_KEY, GEMINI_API_KEY
Deploy!

Vercel will automatically build and deploy
You'll get a URL like your-project.vercel.app
The vercel.json is already configured:

{
    "version": 2,
    "builds": [
        { "src": "api/*/.js", "use": "@vercel/node" },
        { "src": "build-config.js", "use": "@vercel/node" }
    ],
    "routes": [
        { "src": "/api/(.*)", "dest": "/api/$1" }
    ],
    "buildCommand": "node build-config.js",
    "outputDirectory": "."
}
👥 User Roles
👤 Citizen
Register/Login with email
Submit issue reports with photos
Track report status in real-time
Chat with AI assistant
Receive push notifications
Send messages to staff
👷 Staff
View reports assigned to them
Update report status
Communicate with citizens
Track SLA deadlines
View department statistics
🔐 Administrator
Full dashboard access
Assign reports to any staff
Manage users and roles
View all statistics and analytics
Export reports (PDF/Excel)
Manage categories and departments
Image moderation queue
Default Test Credentials
Role	Email	Password
Admin	admin@city.gov	admin123
Staff	staff@city.gov	staff123
Citizen	(Register new account)	(Your choice)
⚠️ Important: Change default passwords in production!

📁 Project Structure
saksham-civic-report/
│
├── 📄 index.html              # Main HTML file (single-page app)
├── 📄 app.js                  # Main application logic (3000+ lines)
├── 📄 style.css               # Main stylesheet
├── 📄 service-worker.js       # PWA service worker (offline support)
├── 📄 manifest.json           # PWA manifest (app metadata)
├── 📄 vercel.json             # Vercel deployment configuration
├── 📄 build-config.js         # Build-time config generator
├── 📄 package.json            # Node.js dependencies
├── 📄 README.md               # This documentation
│
├── 📁 api/                    # Serverless API functions (Vercel)
│   └── gemini.js              # AI proxy (hides API key server-side)
│
├── 📁 css/
│   ├── loading-validation.css # Loading spinners, validation states
│   └── advanced-features.css  # Dark mode, messaging, accessibility
│
├── 📁 js/
│   ├── config.js              # Configuration (auto-generated)
│   ├── auth.js                # Authentication (Supabase Auth)
│   ├── validation.js          # Form validation utilities
│   ├── loading.js             # Loading state management
│   ├── utils.js               # Common utility functions
│   ├── darkmode.js            # 🌓 Dark/Light theme toggle
│   ├── voice-input.js         # 🎤 Voice recognition
│   ├── realtime.js            # 🔔 Real-time notifications
│   ├── pwa.js                 # 📱 PWA install prompt
│   ├── offline-sync.js        # 📴 Offline queue & sync
│   ├── image-moderation.js    # 🖼️ Image auto-moderation
│   ├── rbac.js                # 🔐 Role-based access control
│   ├── messaging.js           # 💬 In-app messaging & SLA
│   ├── i18n.js                # 🌐 Internationalization (11 languages)
│   ├── a11y.js                # ♿ Accessibility features
│   └── export.js              # 📊 PDF/Excel export
│
└── 📁 icons/                  # PWA icons (various sizes)
    ├── icon-72x72.png
    ├── icon-96x96.png
    ├── icon-128x128.png
    ├── icon-144x144.png
    ├── icon-152x152.png
    ├── icon-192x192.png
    ├── icon-384x384.png
    └── icon-512x512.png
🔒 Security Features
✅ Server-side API key protection - Gemini API key never exposed to client
✅ Role-based access control (RBAC) - Different permissions per role
✅ Session timeout - Auto-logout after inactivity
✅ CSRF protection - Token-based request validation
✅ Input validation - Client and server-side validation
✅ Image moderation - AI-powered content filtering
✅ Rate limiting - 10 AI requests per minute per IP
✅ Supabase Row Level Security - Database-level access control
🧪 Testing
Manual Testing Checklist
 Login as Citizen, Staff, Admin
 Submit a report with photo and location
 Toggle dark/light mode
 Change language
 Use keyboard navigation
 Test on mobile device
 Install as PWA
 Test offline submission
 Test AI chatbot
 Assign report (as admin)
 Update report status (as staff)
🤝 Contributing
We welcome contributions! Here's how:

Fork the repository
Create a feature branch
git checkout -b feature/amazing-feature
Make your changes
Commit with clear message
git commit -m 'Add amazing feature'
Push to your fork
git push origin feature/amazing-feature
Open a Pull Request
Code Style
Use meaningful variable names
Add comments for complex logic
Follow existing code patterns
Test before submitting PR
📄 License
Distributed under the MIT License. See LICENSE for more information.

👨‍💻 Team
Built with ❤️ for Smart India Hackathon 2024

Contributors
Bhanu Teja Yadalla - Full Stack Developer
[Add team members]
📞 Support
Having issues? Here's how to get help:

📧 Email: support@saksham.gov.in
📱 Helpline: 1800-XXX-XXXX
💬 In-app: Use the AI chatbot for instant help
🐛 Bugs: Open an issue
🙏 Acknowledgments
Supabase - Backend infrastructure
Google Gemini - AI capabilities
Leaflet - Interactive maps
Chart.js - Beautiful charts
Vercel - Hosting platform
OpenStreetMap - Map data
🇮🇳 Made in India
Empowering Rural India, One Report at a Time

⭐ Star this repo if you found it helpful!
