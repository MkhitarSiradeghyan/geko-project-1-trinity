# 📘 Deployment Guide

## 📌 Purpose

This document describes the process of preparing, building, and deploying the Trinity Tour Agency project.

The goal is to create a predictable deployment process similar to real production environments.

---

## 🌍 Deployment Overview

The project deployment flow:

```
Development → Production Build → Docker Image → Server → Nginx → Domain → SSL Certificate
```

---

## 🏗 Production Environment

Production server requirements:

- Linux server;
- Docker;
- Nginx;
- Domain name;
- SSL certificate.

Recommended:

- Ubuntu Server;
- Docker Compose;
- Nginx Reverse Proxy.

---

## 📁 Project Structure

Deployment is prepared from the repository root:

```
geko-project-1-trinity/
├── front/
├── back/
├── Docker files
└── documentation files
```

---

## ⚛️ Frontend Deployment

The frontend application is located in:

```
front/
```

Technology:

- React;
- Vite;
- Sass Modules.

Before deployment:

Install dependencies:

```bash
npm install
```

Create production build:

```bash
npm run build
```

After successful build, the production files are generated inside:

```
dist/
```

---

## 🐳 Docker Deployment

The frontend application is deployed using Docker.

Production flow:

```
React Application → npm build → Docker Image → Nginx Container → Server
```

### Docker Requirements

Required files:

```
Dockerfile
docker-compose.yml
nginx.conf
```

Example future structure:

```
geko-project-1-trinity/
└── front/
    ├── Dockerfile
    ├── docker-compose.yml
    └── nginx.conf
```

---

## 🌐 Nginx Configuration

Nginx is responsible for:

- serving static files;
- handling client routes;
- connecting domain;
- SSL configuration.

**Important:** React SPA requires fallback routing.

All unknown routes must return:

```
index.html
```

Example:

User opens:

```
domain.com/tours
```

Nginx should return `index.html`, and React Router handles the page rendering.

---

## 🔐 Environment Variables

Sensitive data must not be stored in the repository.

Use:

```
.env
```

Example — `.env.example` contains:

```
VITE_APP_NAME=
VITE_API_URL=
```

Production environment variables are configured on the server.

---

## 🚀 Deployment Steps

### 1. Prepare Server

Install:

- Docker;
- Docker Compose;
- Nginx;
- Git.

### 2. Clone Repository

Download project:

```bash
git clone repository-url
```

Go to project:

```bash
cd geko-project-1-trinity
```

### 3. Build Frontend

Go to frontend:

```bash
cd front
```

Install packages:

```bash
npm install
```

Create build:

```bash
npm run build
```

### 4. Build Docker Image

Create Docker image:

```bash
docker build -t trinity-front .
```

### 5. Start Container

Run container:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

### 6. Configure Nginx

Configure:

- domain;
- static files;
- proxy rules;
- SPA routing.

### 7. Configure SSL

Enable HTTPS.

Required:

- valid domain;
- SSL certificate.

Recommended tool: **Certbot**.

---

## 🔄 Update Deployment

When new changes are ready:

1. Pull latest code.

```bash
git pull
```

2. Rebuild application.

```bash
docker compose build
```

3. Restart containers.

```bash
docker compose up -d
```

4. Check logs.

```bash
docker logs container_name
```

---

## 🧪 Production Checklist

Before publishing:

- ✅ Production build completed
- ✅ No console errors
- ✅ Responsive layout checked
- ✅ Environment variables configured
- ✅ Docker container works
- ✅ Nginx configured
- ✅ HTTPS enabled
- ✅ Domain connected

---

## 🔐 Security Rules

Never upload:

```
.env
node_modules
private keys
server credentials
```

Always:

- use environment variables;
- keep dependencies updated;
- use HTTPS;
- restrict server access.

---

## 📦 Future Backend Deployment

The backend directory:

```
back/
```

is reserved for future development.

Possible future deployment:

```
Frontend → Nginx → Backend API → Database
```

Backend deployment will have separate configuration when implemented.

---

## 👨‍💻 Final Rule

Deployment is part of development.

A finished feature is not only code.

A finished feature must be ready to work in a real production environment.
