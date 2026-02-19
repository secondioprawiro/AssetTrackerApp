# Asset Tracker Dashboard

A desktop application built with Electron for tracking personal assets and viewing live market data.

## Features

- **Portfolio Management**: View, add, and delete your assets (stocks, etc.).
- **Market Data**: Check live market data for various categories (e.g., LQ45, Tech, Banks) via Yahoo Finance API (fetching via backend).
- **Responsive Navigation**: Easy-to-use tab navigation for switching between Portfolio and Market views.
- **Auto-Refresh**: Automatically refreshes data every 5 seconds to stay up-to-date with backend changes.

## Prerequisites

- **Node.js**: Ensure you have Node.js installed on your machine.
- **Backend API**: This frontend expects a .NET backend running at `http://localhost:5199/api/assets`. Make sure your backend service is running for full functionality.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/asset-tracker-dashboard.git
    cd asset-tracker-dashboard
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

## Usage

To start the application in development mode:

```bash
npm start
```

This will launch the Electron window loading `index.html`.

## Project Structure

- **`main.js`**: The main process file for Electron, handling window creation and app lifecycle.
- **`index.html`**: The main UI file containing the structure and logic for the dashboard.
- **`package.json`**: Project metadata and dependencies.
