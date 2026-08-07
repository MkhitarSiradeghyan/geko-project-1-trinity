# 📘 Project Architecture

## 📌 Purpose

This document describes the architecture and organization of the Trinity Tour Agency project.

The goal of this architecture is to create a simple, scalable, and maintainable frontend structure.

The project follows modern frontend development principles:

- separation of responsibilities;
- reusable components;
- clear project structure;
- simple data flow;
- easy onboarding for new developers.

---

## 🏗 Project Architecture Overview

The repository uses a monorepo structure.

Main structure:

```
geko-project-1-trinity/
├── front/  → React Frontend Application
└── back/   → Reserved directory for future backend development
```

The current project stage focuses only on frontend development.

---

## ⚛️ Frontend Architecture

Frontend technology stack:

- React;
- JavaScript;
- Vite;
- React Router;
- CSS Modules;
- Sass Modules.

TypeScript is not used in this project.

### 📁 Frontend Structure

```
front/
└── src/
    ├── assets/
    ├── components/
    ├── features/
    ├── layouts/
    ├── pages/
    ├── services/
    ├── styles/
    ├── utils/
    ├── App.jsx
    └── main.jsx
```

---

## 📂 Folder Responsibilities

### assets/

**Purpose:** Stores static project resources.

Contains:

- images;
- icons;
- fonts;
- illustrations;
- static files.

Example:

```
assets/
├── images/
├── icons/
└── fonts/
```

---

### components/

**Purpose:** Contains reusable UI components.

Components in this folder should be independent and reusable.

Examples:

- Button;
- Navbar;
- Footer;
- Modal;
- Card;
- Loader.

Structure example:

```
components/
└── Button/
    ├── Button.jsx
    └── Button.module.sass
```

Rules:

- one component = one responsibility;
- component should not contain unrelated business logic;
- styles should be stored near the component.

---

### features/

**Purpose:** Contains independent application functionality.

A feature represents a specific part of the application.

Examples:

```
features/
├── tours/
├── gallery/
├── news/
└── booking/
```

A feature may contain:

- components;
- services;
- helpers;
- styles;
- logic related only to this feature.

Example:

```
features/tours/
├── components/
├── services/
└── styles/
```

---

### layouts/

**Purpose:** Contains application layouts.

Layouts define the common page structure.

Examples:

- MainLayout;
- EmptyLayout.

Example:

```
layouts/
└── MainLayout/
    ├── MainLayout.jsx
    └── MainLayout.module.sass
```

MainLayout usually contains:

- Navbar;
- Footer;
- common page wrapper;
- Outlet for pages.

---

### pages/

**Purpose:** Contains complete application pages.

Pages are connected with routes.

Examples:

```
pages/
├── HomePage/
│   ├── HomePage.jsx
│   └── HomePage.module.sass
│
├── ToursPage/
│   ├── ToursPage.jsx
│   └── ToursPage.module.sass
│
└── GalleryPage/
    ├── GalleryPage.jsx
    └── GalleryPage.module.sass
```

Rules:

- Pages combine components and features.
- Pages should not contain large reusable UI blocks.

---

### services/

**Purpose:** Contains communication logic with external systems.

Examples:

- API requests;
- external services;
- data loading.

Example:

```
services/
├── apiService.js
├── tourService.js
└── contactService.js
```

Components should not directly handle API communication.

---

### styles/

**Purpose:** Contains global Sass resources.

Used for:

- variables;
- mixins;
- reset;
- global styles.

Example:

```
styles/
├── variables.sass
├── mixins.sass
├── reset.sass
└── global.sass
```

---

### utils/

**Purpose:** Contains reusable helper functions.

Examples:

- formatting;
- validation;
- calculations;
- data transformation.

Example:

```
utils/
├── formatDate.js
├── validateEmail.js
└── getImageUrl.js
```

---

## 🔀 Routing Architecture

Routing is handled directly inside `App.jsx`.

Separate router folder is not used.

The project uses:

- BrowserRouter;
- Routes;
- Route;
- Outlet.

Example structure:

```
App.jsx → BrowserRouter → Routes → MainLayout → Pages
```

---

## 📄 Application Flow

```
User opens website
        ↓
BrowserRouter checks URL
        ↓
Route selects required page
        ↓
Layout wraps the page
        ↓
Page renders features and components
        ↓
User interacts with interface
```

---

## 🧩 Component Architecture

Components are divided into two types.

### Shared Components

Reusable components used across the application.

Location: `components/`

Examples:

- Button;
- Navbar;
- Footer;
- Modal.

### Feature Components

Components related only to a specific feature.

Location: `features/`

Example: `TourCard` used only inside tours functionality.

---

## 🎨 Styling Architecture

The project uses:

- CSS Modules;
- Sass indented syntax.

Each component owns its styles.

Example:

```
components/
└── TourCard/
    ├── TourCard.jsx
    └── TourCard.module.sass
```

Global styles are used only for:

- reset;
- variables;
- mixins;
- common styles.

---

## 🔄 Data Flow

The application follows a simple data flow:

```
User Action → Component → Feature Logic → Service → External Data → State Update → UI Update
```

---

## 🐍 Backend Architecture

The backend is built with:

- Python
- Django
- Django REST Framework
- PostgreSQL

The backend follows a modular architecture where every application is placed inside the `apps/` directory.

---

## 📁 Backend Structure

```
back/
├── apps/
│   ├── users/
│   ├── tours/
│   ├── bookings/
│   └── ...
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   │
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── requirements.txt
├── .env
├── .env.example
├── manage.py
└── venv/
```

---

# 📂 Folder Responsibilities

## apps/

All Django applications are stored inside the `apps/` directory.

Example:

```
apps/
├── users/
├── tours/
├── bookings/
└── reviews/
```

Each application is responsible for a single business domain.

Examples:

- `users` → authentication and user management
- `tours` → tour management
- `bookings` → reservations
- `reviews` → customer reviews

---

## config/

The `config/` directory is the main Django project configuration.

```
config/
├── settings/
├── urls.py
├── asgi.py
└── wsgi.py
```

---

## settings/

Project settings are separated by environment.

```
config/
└── settings/
    ├── base.py
    ├── dev.py
    └── prod.py
```

### base.py

Contains common project configuration shared across all environments.

Examples:

- INSTALLED_APPS
- Middleware
- REST Framework
- Database configuration
- Static & Media files
- Authentication
- Internationalization

### dev.py

Contains development configuration.

Examples:

- DEBUG=True
- Local PostgreSQL database
- Development-specific settings

### prod.py

Contains production configuration.

Examples:

- DEBUG=False
- Security settings
- Production database
- Logging

---

# 📦 Installed Apps

All local Django applications must be registered using the `apps.` prefix.

Example:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "apps.users",
    "apps.tours",
    "apps.bookings",
]
```

Keeping every project application inside `apps/` makes the project easier to navigate and maintain.

---

# 🌱 Environment Variables

Sensitive configuration must never be committed to GitHub.

The project uses:

```
.env
```

A template file is provided:

```
.env.example
```

Each developer should create their own `.env` file based on `.env.example`.

Typical variables include:

- SECRET_KEY
- DEBUG
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_HOST
- DATABASE_PORT

---

# 🗄 Database

The project uses **PostgreSQL**.

SQLite is not used.

Every developer must create a local PostgreSQL database before running the project.

---

# 📦 Python Environment

The project uses a Python virtual environment.

```
venv/
```

All Python packages are installed inside the virtual environment.

Dependencies are managed through:

```
requirements.txt
```

---

# 🌐 API Architecture

The backend exposes a REST API.

The project uses **Function-Based Views** with the `@api_view` decorator.

Example:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def tour_list(request):
    return Response([])
```

Class-Based Views are not used unless explicitly required.

---

# 🔄 Frontend–Backend Communication

Application data flow:

```
React
   ↓
HTTP Request
   ↓
Django REST API
   ↓
Business Logic
   ↓
PostgreSQL
   ↓
JSON Response
   ↓
React UI
```

---

# 🚀 Initial Project Setup

After cloning the repository from GitHub, every developer must complete the following steps.

## 1. Clone the repository

```bash
git clone <repository-url>
```

---

## 2. Backend Setup

Go to the backend folder.

```bash
cd back
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create your environment file.

```
Copy:

.env.example

to

.env
```

Configure your PostgreSQL credentials inside `.env`.

Run migrations.

```bash
python manage.py migrate
```

Start the backend server.

```bash
python manage.py runserver
```

---

## 3. Frontend Setup

Open another terminal.

```bash
cd front
```

Install packages.

```bash
npm install
```

Run the frontend.

```bash
npm run dev
```

---

# 🔄 Working After Pulling New Changes

Whenever you pull the latest changes from GitHub:

```bash
git pull
```

Backend:

```bash
cd back

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Frontend:

```bash
cd front

npm install

npm run dev
```

> `pip install -r requirements.txt` and `npm install` are safe to run every time after pulling updates. If no dependencies changed, they will simply verify that everything is up to date.

---

# 📋 Backend Development Rules

- Every Django application must be placed inside the `apps/` directory.
- Every local application must be registered using the `apps.` prefix.
- All project configuration belongs inside `config/`.
- Environment-specific settings belong inside `config/settings/`.
- Sensitive information must be stored in `.env`.
- `.env.example` must be updated whenever new environment variables are introduced.
- PostgreSQL is the only supported database.
- Every developer must use a Python virtual environment.
- Dependencies are managed through `requirements.txt`.
- API endpoints should use Function-Based Views with `@api_view`.
- Business logic should remain separated from routing and presentation.
- The backend should expose clean REST endpoints for the React frontend.

---

## ✅ Backend Principles

**Modularity**

Each Django application has a single responsibility.

**Maintainability**

Project configuration is centralized inside `config/`.

**Consistency**

All developers follow the same project structure and workflow.

**Scalability**

New functionality should be added as a separate application inside `apps/`.

**Security**

Secrets and credentials must never be committed to the repository.
---

## 📈 Scalability Rules

When adding new functionality:

1. Create a feature folder.
2. Add feature-specific components.
3. Add services if external communication is required.
4. Keep reusable UI in components.
5. Keep pages simple.

---

## 🚫 Architecture Rules

Forbidden:

- ❌ putting all components into one file;
- ❌ creating huge pages;
- ❌ duplicating components;
- ❌ mixing API logic with UI;
- ❌ storing global styles inside components;
- ❌ creating unnecessary folders.

---

## ✅ Architecture Principles

**Single Responsibility**

Each file and component has one clear purpose.

**Reusability**

Reusable elements should not be duplicated.

**Separation of Concerns**

UI, logic, services, and styles should be separated.

**Simplicity**

The architecture should be understandable for every team member.

**Scalability**

The structure should support future project growth.

---

## 👨‍💻 Final Rule

The architecture exists to make development easier.

A good structure helps developers:

- find code faster;
- avoid duplication;
- work together efficiently;
- maintain the project long-term.

Clean architecture is not about creating more folders.

Clean architecture is about creating clear responsibility.
