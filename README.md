# Professional To-Do App (React + Firebase)

This project is being upgraded from a Python Tkinter desktop app to a modern, full-featured web application using React and Firebase. The new app will support advanced features such as authentication, drag-and-drop, dark/light mode, notifications, statistics, and more.

## Features (Planned)

- **User Authentication:**
  - Email/password signup & login
  - Google Sign-in (via Firebase Auth)
- **Drag and Drop Tasks:**
  - Reorder tasks by importance
- **Dark Mode / Light Mode:**
  - Toggle switch for UI theme
- **Reminder Notifications:**
  - Browser notifications for due tasks
- **Search and Filter Tasks:**
  - By name, status, or priority
- **Progress Tracker / Statistics:**
  - Charts showing completed vs. pending tasks
- **Responsive Design:**
  - Works on both mobile and desktop
- **PWA Support:**
  - Installable on phone/home screen

## Getting Started

1. **Clone or download this repository.**
2. **Install Node.js and npm** if you haven't already.
3. **Create the React app:**
   ```bash
   npm create vite@latest my-todo-app -- --template react
   cd my-todo-app
   npm install
   ```
4. **Install dependencies:**
   ```bash
   npm install firebase react-router-dom react-beautiful-dnd recharts
   ```
5. **Set up Firebase:**
   - Go to [Firebase Console](https://console.firebase.google.com/), create a project, enable Authentication (Email/Password and Google), and Firestore.
   - Copy your Firebase config and add it to `src/firebase.js`.

## Project Structure (Planned)

```
my-todo-app/
  src/
    components/
    pages/
    App.jsx
    main.jsx
    firebase.js
    index.css
```

## Usage

- Start the development server:
  ```bash
  npm run dev
  ```
- Open your browser to the local server address shown in the terminal.

## Status

- The project is in transition to a web app. The previous Python/Tkinter code is deprecated and will be removed.
- All new features will be implemented in the React + Firebase app.

---

New feature updates coming soon! :)