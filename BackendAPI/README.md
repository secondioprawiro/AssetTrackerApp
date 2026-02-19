# Personal Asset Tracker - Backend API

A simple .NET 10 Web API for tracking personal investment assets, using Entity Framework Core with SQLite.

## 🚀 Technologies

- .NET 10
- ASP.NET Core Web API
- Entity Framework Core
- SQLite Database

## 🛠️ Getting Started

### Prerequisites

- .NET 10 SDK
- SQLite (optional, for viewing the database file directly)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd BackendAPI
   ```

2. Restore dependencies:

   ```bash
   dotnet restore
   ```

3. Update the database (run migrations):

   ```bash
   dotnet ef database update
   ```

4. Run the application:
   ```bash
   dotnet run
   ```

The API will be available at `http://localhost:5032` (or the port specified in your launch settings).

## 📡 API Endpoints

### Assets

| Method   | Endpoint           | Description           |
| -------- | ------------------ | --------------------- |
| `GET`    | `/api/assets`      | Get all assets        |
| `POST`   | `/api/assets`      | Create a new asset    |
| `DELETE` | `/api/assets/{id}` | Delete an asset by ID |

#### Example Asset JSON

```json
{
  "symbol": "BBCA",
  "quantity": 100,
  "buyPrice": 9500.0,
  "purchaseDate": "2025-01-15T00:00:00"
}
```

## 📝 Project Structure

- **Controllers/**: API endpoints logic (`AssetsController.cs`)
- **Models/**: Data models (`Asset.cs`)
- **Data/**: Database context (`AppDbContext.cs`)
- **Migrations/**: EF Core migration files
