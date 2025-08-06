# FastAPI Practice

A hands-on project to learn and demonstrate FastAPI, a modern Python web framework for building APIs quickly and efficiently.

## Table of Contents

- [FastAPI Practice](#fastapi-practice)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
  - [API Documentation](#api-documentation)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

This repository contains code samples, routers, database models, and authentication flows to help you understand FastAPI concepts, including routing, parameters, error handling, OAuth, and file handling.

## Features

- RESTful API endpoints
- User authentication (OAuth)
- Database integration (SQLite)
- File upload/download
- Modular routers
- Interactive API docs (Swagger UI & ReDoc)

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dpvasani/FastAPI.git
   cd FastAPI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API docs:**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure

```
fastapi_practice.db
main.py
schemas.py
auth/
db/
routers/
static/
Blogs/
FastAPI/
Pdf/
```

- `main.py`: FastAPI app entry point
- `auth/`: Authentication logic (OAuth)
- `db/`: Database models and utilities
- `routers/`: API route handlers
- `schemas.py`: Pydantic models for request/response validation

## Usage

- Explore the `Blogs/` and `FastAPI/` folders for tutorials and HTML guides.
- Check `routers/` for API endpoint implementations.
- Use the interactive docs to test endpoints.

## API Documentation

FastAPI provides automatic API documentation at `/docs` and `/redoc` when running the server.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.