# Sales Data Fetcher

This project was created as part of a machine test.

The script fetches sales data from the provided Petpooja API and stores the records in a local SQLite database.

## Prerequisites

- Python 3.x
- requests library

Install the required package:

pip install requests

## How to Run

Run the script using:

python sales_data_fetcher.py

## What the Script Does

- Fetches sales data from the API
- Creates a SQLite database named `sales_data.db`
- Creates the `sales_data` table if it does not already exist
- Inserts the fetched records into the database

## Files Included

- sales_data_fetcher.py
- sales_data.db
- README.md
- requirements.txt

## Database

All sales records are stored in the `sales_data` table.

## Notes

Basic error handling has been added for API requests and database operations.
