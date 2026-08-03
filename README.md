# 🌍 Trinity Tour Agency

## 📌 About Project

Trinity Tour Agency is a production-oriented SPA website for a real tourism company.

The project is developed as a real commercial product using professional software development practices:

- team collaboration through Git workflow;
- task management through GitHub Projects;
- Pull Requests and Code Review;
- clean code standards;
- project documentation;
- Docker preparation;
- production deployment.

The goal of this project is not only to create a website, but to follow a real development process used by professional frontend teams.

---

## 🛠 Technology Stack

### Frontend

- React
- JavaScript
- React Router
- Vite
- CSS Modules
- Sass Modules

TypeScript is not used in this project.

### Backend

The backend is not implemented in the current stage.

The repository contains a reserved directory for future backend development.

Possible future stack:

- Python
- Django
- Django REST Framework
- PostgreSQL

### Development Tools

- Git
- GitHub
- GitHub Projects
- npm
- ESLint

### Deployment

- Docker
- Nginx
- Linux Server
- SSL Certificate

---

## 📁 Project Structure

The project uses a monorepo structure.

Frontend and backend are separated into independent applications.

Current development is focused on the frontend application.

The backend directory is reserved for future development.

```
geko-project-1-trinity/
├── front/
│   └── React application
│
├── back/
│   └── Backend application (future development)
│
├── README.md
├── CONTRIBUTING.md
├── CODE_STYLE.md
├── ARCHITECTURE.md
├── DEPLOYMENT.md
│
├── .gitignore
├── .editorconfig
└── .env.example
```

---

## ⚛️ Frontend Application

Frontend application is located in:

```
front/
```

Technology stack:

- React
- JavaScript
- Vite
- React Router
- CSS Modules
- Sass Modules

Frontend structure:

```
front/
├── public/
│
├── src/
│   ├── assets/
│   ├── components/
│   ├── features/
│   ├── layouts/
│   ├── pages/
│   ├── router/
│   ├── services/
│   ├── styles/
│   ├── utils/
│   ├── App.jsx
│   └── main.jsx
│
├── package.json
├── package-lock.json
├── vite.config.js
└── eslint.config.js
```

---

## 📂 Folder Description

### assets/

Contains static project resources:

- images;
- icons;
- fonts;
- illustrations.

### components/

Reusable UI components.

Examples:

- Button
- Navbar
- Footer
- Modal
- Card

### features/

Contains independent application features.

Examples:

- tours
- gallery
- news
- booking

### layouts/

Contains application layouts.

Examples:

- MainLayout
- HeaderLayout

### pages/

Contains application pages.

Examples:

- HomePage
- ToursPage
- GalleryPage
- NewsPage
- ContactPage

### services/

Contains external communication logic.

Examples:

- apiService.js
- tourService.js
- contactService.js

### styles/

Contains global styles and shared Sass resources.

Examples:

- variables.sass
- mixins.sass
- reset.sass

### utils/

Contains reusable helper functions.

Examples:

- formatDate.js
- validateEmail.js
- getImageUrl.js

---

## ⚙️ Local Development Setup

### Requirements

Install before starting:

- Git
- Node.js
- npm

### Installation

Clone repository:

```bash
git clone repository-url
```

Go to project folder:

```bash
cd geko-project-1-trinity
```

Go to frontend:

```bash
cd front
```

Install dependencies:

```bash
npm install
```

### Environment Setup

Create:

```
.env
```

based on:

```
.env.example
```

Example:

```
VITE_APP_NAME=Trinity Tour
VITE_API_URL=
```

### Run Development Server

Start project:

```bash
npm run dev
```

### Production Build

Create production build:

```bash
npm run build
```

Preview production build:

```bash
npm run preview
```

---

## 🌿 Development Workflow

The project uses professional Git workflow principles.

Main branches:

**`main`** — Production-ready code.

**`dev`** — Main development branch.

Feature development is done through separate branches.

Examples:

```
feature/tour-page
feature/gallery-section
feature/contact-form
```

Bug fixes:

```
bug/mobile-menu
bug/image-loading
```

Urgent fixes:

```
hotfix/production-error
```

---

## 📋 GitHub Projects

All development tasks are managed through GitHub Projects.

Workflow:

```
Todo → In Progress → In Review → Done
```

Every task should have:

- clear description;
- responsible developer;
- current status.

---

## 🔀 Pull Request Workflow

Development process:

```
Task → Create Branch → Development → Push Changes → Create Pull Request → Code Review → Merge
```

Rules:

- Do not push directly to `main`.
- Every change must go through Pull Request.
- Code must pass review before merge.

---

## 📚 Documentation

The project contains additional documentation:

### CONTRIBUTING.md

Team workflow rules:

- development process;
- branch workflow;
- Pull Request rules;
- Code Review process.

### CODE_STYLE.md

Coding standards:

- React rules;
- file naming;
- component structure;
- Sass rules;
- commit conventions.

### ARCHITECTURE.md

Project architecture:

- application structure;
- data flow;
- component organization.

### DEPLOYMENT.md

Production deployment:

- server setup;
- Docker configuration;
- Nginx setup;
- SSL configuration.

---

## 🐳 Docker

The project must be prepared for containerized deployment.

Production environment:

```
Frontend → Docker → Nginx → Linux Server
```

Docker configuration is added during the final project stage.

---

## 🔐 Security Rules

Never commit:

```
.env
node_modules/
dist/
build/
*.log
```

Sensitive information must always be stored using environment variables.

---

## ✅ Definition of Done

A feature is completed when:

- Code is implemented.
- Code follows `CODE_STYLE.md`.
- Tested locally.
- Responsive design checked.
- Pull Request created.
- Code Review completed.
- Changes merged successfully.
- Documentation updated if needed.

---

## 👨‍💻 Development Philosophy

We build products, not just pages.

This project follows real frontend development principles:

- clean architecture;
- predictable code structure;
- teamwork;
- documentation;
- review process;
- production preparation.

Every developer is responsible for code quality and project success.
