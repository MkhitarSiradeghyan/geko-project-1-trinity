# 🔐 Security Policy

## 📌 Purpose

This document describes security rules and recommendations for the Trinity Tour Agency project.

The goal is to keep the project secure during development, testing, and production deployment.

Every developer must follow these rules.

---

## 🔒 General Security Rules

Developers must:

- protect sensitive information;
- avoid exposing private data;
- keep dependencies updated;
- follow secure coding practices.

---

## 🚫 Forbidden Files

The following files must never be committed to Git:

```
.env
node_modules/
dist/
build/
*.log
private keys
server credentials
```

---

## 🔑 Environment Variables

Sensitive information must always be stored in environment variables.

Examples:

- API keys;
- secret tokens;
- passwords;
- private configuration.

Never write sensitive data directly inside source code.

❌ Wrong:

```js
const API_KEY = "secret_key"
```

✅ Correct:

```js
const API_KEY = import.meta.env.VITE_API_KEY
```

---

## 📁 Environment Files

The repository contains:

```
.env.example
```

Purpose:

- show required variables;
- help developers configure local environment.

Real environment files (`.env`) must remain private.

---

## 📦 Dependencies Security

Before adding new packages, check:

- package popularity;
- maintenance status;
- security issues;
- unnecessary permissions.

Regularly update dependencies.

Recommended command:

```bash
npm audit
```

---

## 🛡 Frontend Security Rules

Developers must consider:

- XSS protection;
- safe rendering of user data;
- secure external links;
- avoiding unsafe HTML injection.

---

## ⚠️ User Input

Never trust user input.

Always validate:

- forms;
- search fields;
- URL parameters;
- external data.

---

## 🌐 External Resources

When using external resources, check:

- source reliability;
- HTTPS availability;
- required permissions.

Avoid loading unknown scripts.

---

## 🖼 Images and Files

Uploaded or external files must be handled safely.

Check:

- file type;
- file size;
- source.

Do not include unknown executable files.

---

## 🔄 Code Review Security Check

During Pull Request review, check:

- no secrets in code;
- no suspicious dependencies;
- no unsafe practices;
- no accidental data exposure.

---

## 🐳 Docker Security

For production deployment:

- use official images;
- keep images updated;
- do not store secrets inside Docker files;
- limit unnecessary permissions.

---

## 🌍 Production Security

Production environment must use:

- HTTPS;
- secure server configuration;
- updated software;
- restricted access.

---

## 🚨 Reporting Security Issues

If a security problem is discovered:

- Do not publish it publicly.
- Report it to the project maintainer.

Provide:

- problem description;
- steps to reproduce;
- possible impact.

---

## ✅ Security Checklist

Before release:

- ✅ No secrets in repository
- ✅ Environment variables configured
- ✅ Dependencies checked
- ✅ HTTPS enabled
- ✅ Production settings reviewed
- ✅ Security issues resolved

---

## 👨‍💻 Final Rule

Security is everyone's responsibility.

A secure application is built by good habits during development, not only after problems appear.
