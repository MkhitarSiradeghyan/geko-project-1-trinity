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

## 🔌 Future Backend Integration

The repository contains a reserved backend directory:

```
back/
```

Future backend communication will be connected through:

```
services/
```

Frontend responsibilities:

- display data;
- handle user interaction;
- send requests;
- manage UI state.

Backend responsibilities in future:

- database;
- authentication;
- business logic;
- API.

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

## Sass Architecture & Entry Point Setup

- `styles/index.sass`: Central global entry point forwarding variables/tokens and mixins.
- **Vite Integration**: Auto-injects `@use "@/styles/index.sass" as t` into every Sass module via `additionalData`.
- **Usage**: Components directly access tokens and mixins using the `t.` namespace without manual imports.