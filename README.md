# PythonApp
# FastAPI Application

This is a FastAPI application that generates tokens and provides an API to generate checksums. It uses the Uvicorn web server for running the application.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Uvicorn web server:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI application on `http://localhost:8000`.

2. Access the application in your web browser:

    - To access the HTML form, go to: `http://localhost:8000/`
    - To access the welcome page, go to: `http://localhost:8000/welcome`
    - To generate a token using the HTML form, submit the form at: `http://localhost:8000/generate-token`
    - To generate a token using the API, send a GET request to: `http://localhost:8000/api/generate-token`
    - To generate a checksum using the API, send a POST request to: `http://localhost:8000/api/generate-tokens`

## API Documentation

The API endpoints are documented using Swagger UI. You can access the API documentation at: `http://localhost:8000/docs`

## License

This project is licensed under the [MIT License](LICENSE).
