# VRV Security

VRV Security is a Flask-based web application that provides user authentication and authorization using JWT (JSON Web Tokens).

## Features

- User registration
- User login
- JWT-based authentication

## Project Structure
```
VRV_Security/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   └── .env
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/vrv_security.git
    cd vrv_security
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the `app/` directory and add the following:
    ```
    SECRET_KEY=your_secret_key
    ```

## Usage

1. Run the application:
    ```sh
    flask run
    ```

2. The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- `POST /auth/register`: Register a new user
- `POST /auth/login`: Login a user

## License

This project is licensed under the MIT License.