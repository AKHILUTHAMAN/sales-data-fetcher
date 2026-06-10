# PetPooja Sales Data ETL

Fetches sales data from the PetPooja API and stores it in a local SQLite database (`sales_data.db`).

## Requirements

- Python 3.9+
- No third-party packages needed (uses stdlib only: `sqlite3`, `urllib`, `json`, `os`, `time`)

## Setup

```bash
git clone <your-repo-url>
cd <repo-folder>
```

## Usage

### Run with default credentials (from the task)
```bash
python3 fetch_sales.py
```

### Run with environment variables (recommended)
```bash
export APP_KEY="your_app_key"
export APP_SECRET="your_app_secret"
export ACCESS_TOKEN="your_access_token"
export REST_ID="your_rest_id"
export FROM_DATE="2025-01-20 00:00:00"
export TO_DATE="2025-01-20 23:59:59"

python3 fetch_sales.py
```

## Environment Variables

| Variable       | Description                        | Default (task value)              |
|----------------|------------------------------------|-----------------------------------|
| `APP_KEY`      | PetPooja API app key               | `srd2neaq1xg7bzc6uyk5jmwv98o4tpfh` |
| `APP_SECRET`   | PetPooja API app secret            | `fd08934c5224af4c975015e599d60a74bf857b4a` |
| `ACCESS_TOKEN` | PetPooja access token              | `0442e1ee9899bc3806f1a40be490af4ec5c6602a` |
| `REST_ID`      | Restaurant ID                      | `51wok2zxnsad`                    |
| `FROM_DATE`    | Start of date range (YYYY-MM-DD HH:MM:SS) | `2025-01-20 00:00:00`      |
| `TO_DATE`      | End of date range (YYYY-MM-DD HH:MM:SS)   | `2025-01-20 23:59:59`      |
| `DB_PATH`      | Path to SQLite database file       | `sales_data.db`                   |

## Database Schema

```sql
CREATE TABLE sales_data (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_number     TEXT,
    sale_date          TEXT,
    transaction_time   TEXT,
    sale_amount        REAL,
    tax_amount         REAL,
    discount_amount    REAL,
    round_off          REAL,
    net_sale           REAL,
    payment_mode       TEXT,
    order_type         TEXT,
    transaction_status TEXT
);
```

## Features

- ✅ Fetches sales data from PetPooja REST API
- ✅ Parses and maps API fields to DB schema
- ✅ Stores data in SQLite with proper types
- ✅ Retry mechanism (3 attempts, linear back-off) for API failures
- ✅ Environment variable support for credentials
- ✅ Comprehensive error handling (HTTP errors, JSON errors, DB errors)
- ✅ Clean, well-commented code

## Files

| File             | Description                          |
|------------------|--------------------------------------|
| `fetch_sales.py` | Main ETL script                      |
| `sales_data.db`  | SQLite database (created on first run) |
| `README.md`      | This file                            |
