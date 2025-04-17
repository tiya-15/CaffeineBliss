# Caffeine Bliss ☕

A modern coffee shop website built with Django, featuring user authentication, a beautiful UI, and responsive design.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Setup Instructions

### 1. Clone the Repository

```bash
# Clone this repository
git clone <your-repository-url>

# Navigate to the project directory
cd coffeebliss
```

### 2. Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 4. Database Setup

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
# Create an admin user
python manage.py createsuperuser
# Follow the prompts to set username, email, and password
```

### 6. Collect Static Files

```bash
# Collect static files
python manage.py collectstatic --noinput
```

### 7. Run the Development Server

```bash
# Start the development server
python manage.py runserver
```

The website should now be accessible at `http://127.0.0.1:8000/`

## Project Structure

```
coffeebliss/
├── coffee/                 # Main app directory
│   ├── static/            # Static files (CSS, JS, images)
│   │   └── images/        # Image files including logo
│   ├── templates/         # HTML templates
│   │   ├── index.html     # Home page template
│   │   ├── login.html     # Login page template
│   │   └── signup.html    # Registration page template
│   ├── models.py          # Database models
│   └── views.py           # View functions
├── coffeebliss/           # Project settings directory
│   ├── settings.py        # Project settings
│   └── urls.py            # URL configurations
├── static/                # Global static files
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Features

- User Authentication
  - Login
  - Signup
  - Logout
- Responsive Design
  - Mobile-friendly layout
  - Modern UI components
- Navigation
  - Smooth scrolling
  - Fixed header
- Sections
  - Home
  - About
  - Contact

## Making Changes and Pushing to Your Repository

1. Create a new repository on GitHub
2. Initialize git and push to your repository:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-new-repository-url>
git push -u origin main
```

## Common Issues and Solutions

1. **Static files not loading**
   - Make sure you've run `python manage.py collectstatic`
   - Verify static files configuration in settings.py
   - Check if the static files are in the correct directories

2. **Database errors**
   - Delete db.sqlite3 file
   - Run migrations again:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

3. **Port already in use**
   - Kill the process using the port or use a different port:
     ```bash
     python manage.py runserver 8001
     ```

## Development Workflow

1. Create a new branch for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test them

3. Commit your changes
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

4. Push to your repository
   ```bash
   git push origin feature/your-feature-name
   ```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to your fork
5. Create a Pull Request

## License

This project is open-source and available under the MIT License.

## Support

If you encounter any issues or need help:
1. Check the Common Issues section above
2. Create an issue in the GitHub repository
3. Contact the project maintainers