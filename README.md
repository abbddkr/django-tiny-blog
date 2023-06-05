# Django Tiny Blog

Django Tiny Blog is a RESTful API-based tiny blog application built with Django Rest Framework. It allows users to create, read, update, and delete blog posts and users. The API is secured, and users must provide a JSON Web Token key to perform CRUD operations.

## Features
- Authentication: Users can obtain a JWT token by providing valid credentials.
- Create, Read, Update, and Delete Posts: Users can perform CRUD operations on blog posts.
- Create, Read, Update, and Delete Users: Admin users can manage user accounts.
- Security: JWT authentication is implemented to ensure secure access to the API.
- Easy Admin Panel: This project includes Django's built-in Admin Dashboard, providing an easy interface for managing and updating content with a great markdown editor for post content field [martor](https://pypi.org/project/martor/).

## Installation

Follow these steps to set up the Django Tiny Blog project:

1. Clone the repository:

`git clone https://github.com/abbddkr/django-tiny-blog.git`


2. Change to the project directory:

`cd django-tiny-blog`


3. Create a virtual environment and activate it (optional):
```
python -m venv env

source env/bin/activate # for macOS/Linux
env\Scripts\activate # for Windows
```

4. Install the project dependencies:

`pip install -r requirements.txt`

5. Set up the database:

`python manage.py migrate`


6. Run the development server:

`python manage.py runserver`


7. The Django Tiny Blog API will now be accessible at `http://localhost:8000`.

## Usage

To use the Django Tiny Blog API, you can make HTTP requests to the available endpoints below.

### Authentication

To access protected endpoints, you need to include the JWT token in the request header as follows:

`Authorization: Bearer YOUR_TOKEN`


## Generate a Token

To obtain a JWT token, follow these steps:

Send a POST request to `http://localhost:8000/api/token/` with your username and password in the request body.
```
POST /api/token/
Content-Type: application/json

{
    "username": "your-username",
    "password": "your-password"
}
```

### Endpoints

The following are some of the key API endpoints available in this project:
- `/api/posts/`: CRUD operations for blog posts.
- `/api/users/`: CRUD operations for users (admin access only).
