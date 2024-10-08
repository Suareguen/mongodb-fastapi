# FastAPI + MongoDB CRUD API

This project is a simple **CRUD API** built using **FastAPI** and **MongoDB**. The API allows you to create, read, update, and delete items from a MongoDB database. It uses asynchronous capabilities for efficient interaction with the database, utilizing `Motor`, an async driver for MongoDB.

## Features

- **FastAPI** for building a high-performance API.
- **Motor** for async interaction with MongoDB.
- Basic CRUD functionality: create, read, update, delete items in the database.
- Easy setup and configuration for local development.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.11** or higher installed.
- **MongoDB** installed locally or an Atlas MongoDB cluster.
- **Git** installed on your machine.

## Getting Started

### Clone the Repository

1. Clone the repository to your local machine using Git.

2. Navigate to the project directory.

### Set Up the Environment

1. Create a virtual environment (optional but recommended).

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

### Set Up MongoDB

1. If you're using a local MongoDB instance, ensure it is running.

```bash
sudo systemctl start mongod
```

### Running the Application

1. Run the FastAPI application with **Uvicorn**.

```bash
uvicorn app.main:app --reload
```

2. The API will be available at the local host address.

```bash
http://127.0.0.1:8000
```

3. You can access the **Swagger UI** to interact with the API.

### API Endpoints

Here are the available API endpoints for interacting with the items in the MongoDB database:

- **Create an item**: `POST /items/`
```json
{
  "name": "Item Name",
  "description": "Item Description",
  "price": 100.00,
  "stock": 10
}
```


- **Get all items**: `GET /items/`
- **Get a single item by ID**: `GET /items/{item_id}`
- **Update an item**: `PUT /items/{item_id}`
- **Delete an item**: `DELETE /items/{item_id}`

### Testing with Postman

You can use **Postman** or **cURL** to interact with the API.

1. Set the method to **POST**.
2. Use the correct URL for the endpoint.
3. Set the **Body** to `raw` JSON and provide the item data.

```json
{
  "name": "Laptop",
  "description": "A powerful gaming laptop",
  "price": 1500.0,
  "stock": 10
}
```

