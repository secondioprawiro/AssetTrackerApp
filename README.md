# 📈 Asset Tracker App

A complete desktop application and Web API solution for tracking personal investment assets and viewing live market data. This project consists of an Electron-based frontend dashboard and a .NET 10 backend powered by Entity Framework Core and SQLite.

## ✨ Features

- **Portfolio Management**: View, add, and delete your assets (stocks, etc.) stored securely in a local database.
- **Market Data**: Check live market data for various categories (e.g., LQ45, Tech, Banks) via Yahoo Finance API (fetching via backend).
- **Responsive Navigation**: Easy-to-use tab navigation for switching between Portfolio and Market views.
- **Auto-Refresh**: Automatically refreshes data every 5 seconds to stay up-to-date with backend changes.

## 🚀 Technologies

- **Frontend**: Electron, Node.js, HTML/JS/CSS
- **Backend**: .NET 10, ASP.NET Core Web API, Entity Framework Core, SQLite

## 🛠️ Prerequisites

Ensure you have the following tools installed on your machine before running the application:
- **Node.js**: Required to run the Electron frontend.
- **.NET 10 SDK**: Required to build and run the backend API.
- **SQLite**: (Optional) For viewing the database file directly.

## 💻 Installation & Usage

Follow these steps to get both the backend and frontend running locally on your machine.

### 1. Clone the Repository
```
git clone https://github.com/your-username/asset-tracker-app.git
cd asset-tracker-app
```

### 2. Start the Backend API
```
cd BackendAPI
# Restore .NET dependencies
dotnet restore
# Update the database (run migrations)
dotnet ef database update
# Run the application
dotnet run
```

### 3. Start the Frontend Dashboard
```
cd FrontendApp
# Install Node dependencies
npm install
# Start the application in development mode
npm start
```

## 📡 API Endpoints (for now)

The backend provides the following RESTful endpoints for managing your assets:

| Method   | Endpoint             | Description           |
| -------- | -------------------- | --------------------- |
| `GET`    | `/api/assets`        | Get all assets        |
| `POST`   | `/api/assets`        | Create a new asset    |
| `DELETE` | `/api/assets/{id}`   | Delete an asset by ID |



## Example Asset JSON (POST):
```json
{
  "symbol": "BBCA",
  "quantity": 100,
  "buyPrice": 9500.0,
  "purchaseDate": "2025-01-15T00:00:00"
}