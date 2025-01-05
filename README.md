# My Portfolio Project Website Using Django

Full Blog on this [Medium tutorial](https://tusher16.medium.com/make-a-simple-django-3-2-portfolio-project-as-data-scientist-part-1-72dfa4992b85)  
Live at: https://tusher.site

---

## Getting Started

### Prerequisites

1. **Install Docker**: Ensure Docker is installed on your system. [Install Docker](https://docs.docker.com/get-docker/).
2. **Install Docker Compose**: Ensure Docker Compose is installed. [Install Docker Compose](https://docs.docker.com/compose/install/).

---

### Running the Project with Docker

The project has been updated to use Docker and Nginx for deployment. Follow these steps to run it:

#### 1. Clone the Repository

```bash
git clone https://github.com/tusher16/My-portfolio-project.git
cd My-portfolio-project
```

#### 2. Build and Start the Docker Containers

```bash
sudo docker-compose up --build
```

- **`django_gunicorn`**: Runs the Django app with Gunicorn.
- **`nginx`**: Serves as the reverse proxy to manage requests.

#### 3. Access the Application

Once the containers are up and running, the application will be accessible at:  
**http://localhost** (or public domain: https://tusher.site)

---

### Database Configuration

By default, this project uses SQLite. If using another database:

1. Update the `.env` file with the appropriate `DATABASE_URL`.
2. Run the following commands to apply migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

### Creating a Superuser

To access the admin interface:

```bash
python3 manage.py createsuperuser
```

---

### Local Development Without Docker

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run migrations:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Start the development server:

```bash
python3 manage.py runserver
```

Access the application at **http://127.0.0.1:8000**.

---

### Features Added:

1. **Dockerized Setup**: Added support for Docker and Docker Compose.
2. **Nginx Integration**: Added Nginx as a reverse proxy for production.
3. **Environment Variables**: Centralized configuration with `.env` for sensitive data.
4. **Static and Media Management**: Configured Docker volumes for handling static and media files.

---

### How to Contribute

Feel free to fork this repository, make your changes, and submit a pull request!