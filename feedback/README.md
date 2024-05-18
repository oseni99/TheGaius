# TheGaius
My Django Project 
## Table of Contents 
This Project contains the code from what i practiced in Django 
# Features
- Two Apps that showcases different learning points 
- Django project setup and configuration
- Creating and managing models
- Building views and templates
- Handling forms and user input

## Setup Instructions

To get started with this project, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/oseni99/TheGaius.git
    cd feedback
    ```

2. **Create and activate a virtual environment:**

    ```sh
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.
