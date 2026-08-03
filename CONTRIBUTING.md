# 📘 Contribution Guide

## 📌 Purpose

This document describes the development workflow and collaboration rules for the Trinity Tour Agency project.

The purpose of this guide is to make teamwork predictable, organized, and close to real professional software development processes.

Every team member must follow these rules when contributing to the project.

---

## 🚀 Development Workflow

All development follows this workflow:

```
Task → Create Branch → Development → Testing → Pull Request → Code Review → Merge → Done
```

---

## 📋 Task Management

All tasks are managed through GitHub Projects.

Each task must have:

- clear description;
- assigned developer;
- current status.

Project workflow:

```
Todo → In Progress → In Review → Done
```

---

## 🌿 Branch Workflow

The project uses a Git Flow based workflow.

Main branches:

### `main`

The production branch.

Rules:

- contains stable code;
- direct push is forbidden;
- changes come only through Pull Requests.

### `dev`

The main development branch.

Rules:

- all completed features are merged here first;
- used for testing and integration.

---

## 🌱 Feature Development

New functionality must be developed in a separate branch.

Format:

```
feature/short-description
```

Examples:

```
feature/tour-page
feature/gallery-section
feature/contact-form
```

Development flow:

```
dev → feature branch → Pull Request → dev
```

---

## 🐛 Bug Fix Workflow

Bug fixes must use a separate branch.

Format:

```
bug/short-description
```

Examples:

```
bug/mobile-menu
bug/image-loading
bug/responsive-header
```

---

## 🚑 Hotfix Workflow

Hotfix branches are used only for urgent production problems.

Format:

```
hotfix/short-description
```

Examples:

```
hotfix/production-error
hotfix/broken-build
```

---

## 🔀 Pull Request Rules

### Before creating a Pull Request

Required:

- code must work locally;
- changes must be tested;
- code must follow `CODE_STYLE.md`;
- no unnecessary files should be included.

### Pull Request Title

Use the same format as commits:

```
Type - Description
```

Examples:

```
Feature - Add tours page
Fix - Correct mobile navigation
Style - Update header design
```

### Pull Request Description

Every Pull Request should contain:

**Description**

What was changed?

Example:

> Added new tours page with responsive layout.

**Changes**

List important changes:

- Added TourCard component
- Added Sass styles
- Updated routing

**Testing**

Explain how it was tested:

- Tested on desktop
- Tested on mobile resolution
- Checked browser console

---

## 👀 Code Review

Every Pull Request must be reviewed before merge.

Reviewer checks:

- code quality;
- project structure;
- naming;
- component responsibility;
- Sass rules;
- responsive behavior;
- possible bugs.

### Merge Rules

Allowed workflow:

```
feature branch → dev → main
```

Forbidden:

- ❌ Direct push to `main`
- ❌ Merge without Pull Request
- ❌ Merge without review
- ❌ Merge unfinished work

---

## 🧪 Testing Before Merge

Before merging, developer must check:

### Functionality

- feature works correctly;
- no broken pages;
- no unexpected behavior.

### UI

- desktop version;
- tablet version;
- mobile version.

### Code

- no console errors;
- no unused code;
- no debug logs.

---

## 📦 Keeping Branches Clean

After successful merge:

- delete merged branches;
- update local repository;
- continue work from updated `dev` branch.

Example workflow:

```bash
git checkout dev
git pull
git branch -d feature/example
```

---

## 🔐 Security Rules

Never commit:

```
.env
node_modules/
build/
dist/
private keys
```

Sensitive information must never be stored inside the repository.

---

## ✅ Definition of Done

A task is completed when:

- implementation is finished;
- code follows project standards;
- local testing is completed;
- Pull Request is created;
- Code Review is passed;
- changes are merged;
- GitHub Project status is updated.

---

## 👨‍💻 Team Responsibility

Every developer is responsible for:

- writing clean code;
- respecting project rules;
- communicating problems;
- reviewing teammates' code;
- improving the project.

A good team is built not only by writing code, but by following a clear process.
