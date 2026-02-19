# 📈 Asset Tracker App

A complete desktop application and Web API solution for tracking personal investment assets and viewing live market data. This project consists of an Electron-based frontend dashboard, a .NET 10 backend for portfolio management, and a Python Flask service for live market data.

## ✨ Features

- **Portfolio Management**: View, add, and delete your assets (stocks, etc.) stored securely in a local database.
- **Market Data**: Check live market data for various categories (e.g., LQ45, Tech, Banks) via a dedicated Python service using the Yahoo Finance API.
- **Responsive Navigation**: Easy-to-use tab navigation for switching between Portfolio and Market views.
- **Auto-Refresh**: Automatically refreshes data every 5 seconds to stay up-to-date with backend changes.

## 🚀 Technologies

- **Portfolio API (Backend)**: .NET 10, ASP.NET Core, Entity Framework Core, SQLite
- **Finance Data Service**: Python 3.10+, Flask, yfinance

## 🛠️ Prerequisites

Ensure you have the following tools installed on your machine before running the application:
- **Node.js**: Required to run the Electron frontend.
- **.NET 10 SDK**: Required to build and run the backend API.
- **Python 3.x**: Required to run the finance data service.
- **SQLite**: (Optional) For viewing the database file directly.

## 💻 Installation & Usage

Follow these steps to get both the backend and frontend running locally on your machine.

### 1. Clone the Repository
```
git clone https://github.com/your-username/asset-tracker-app.git
cd asset-tracker-app
```

### 2. Start the Portfolio API (.NET)
```bash
cd BackendAPI
# Restore .NET dependencies
dotnet restore
# Update the database (run migrations)
dotnet ef database update
# Run the application (Default port: 5000)
dotnet run
```

### 3. Start the Finance Data Service (Python)
```bash
cd PythonService
# Install dependencies
pip install -r requirements.txt
# Run the service (Default port: 5050)
python StocksService.py
```

### 4. Start the Frontend Dashboard (Electron)
```bash
cd FrontendApp
# Install Node dependencies
npm install
# Start the application in development mode
npm start
```

## 📡 API Endpoints

### Portfolio API (.NET - Port 5000)
| Method   | Endpoint             | Description           |
| -------- | -------------------- | --------------------- |
| `GET`    | `/api/assets`        | Get all assets        |
| `POST`   | `/api/assets`        | Create a new asset    |
| `DELETE` | `/api/assets/{id}`   | Delete an asset by ID |

### Finance Data Service (Python - Port 5050)
| Method | Endpoint                  | Description                                      |
| ------ | ------------------------- | ------------------------------------------------ |
| `GET`  | `/api/finance/<category>` | Get stock data for a category (LQ45, BANK, TECH) |



## Example Asset JSON (POST):
```json
{
  "symbol": "BBCA",
  "quantity": 100,
  "buyPrice": 9500.0,
  "purchaseDate": "2025-01-15T00:00:00"
}