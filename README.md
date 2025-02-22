# FoodEdge Gourmet Catering Management System

## Project Overview

FoodEdge Gourmet Catering is a comprehensive web-based management system designed to streamline food catering operations, providing robust features for clients, operations staff, and management.

## Key Features

### Client Interface
- Menu browsing and ordering
- Account management
- Membership features
- Order tracking
- Event booking capabilities

### Operations Interface
- Order management
- Booking processing
- Payment handling
- Customer support tools

### Management Interface
- Business analytics
- Income tracking
- Food sales data management
- Menu configuration

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap (Responsive Design)

### Backend
- Django (Python Web Framework)
- Django ORM
- MySQL Database

### Development Tools
- XAMPP (Local Server Environment)
- GitHub (Version Control)
- Trello (Project Management)
- actiTIME (Time Tracking)

## Project Structure

```
FoodEdge-Catering/
│
├── foodcateringapp/             # Main application directory
│   ├── migrations/               # Database migration files
│   ├── templates/                # HTML templates
│   ├── models.py                 # Database models
│   ├── views.py                  # Business logic
│   └── urls.py                   # URL routing
│
├── static/                       # Static files (CSS, JS, Images)
│   ├── styles/
│   └── scripts/
│
├── templates/                    # Global templates
│   └── admin/                    # Admin interface templates
│
├── users/                        # User management app
│   ├── models.py
│   └── views.py
│
├── manage.py                     # Django project management script
└── requirements.txt              # Project dependencies
```

## Setup and Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- MySQL
- pip (Python Package Manager)

### Installation Steps
1. Clone the repository
   ```bash
   git clone https://github.com/your-username/FoodEdge-Catering.git
   cd FoodEdge-Catering
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Database Setup
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create Superuser
   ```bash
   python manage.py createsuperuser
   ```

6. Run Development Server
   ```bash
   python manage.py runserver
   ```

## Testing

- Selenium WebDriver used for comprehensive testing
- 100% test coverage across:
  - Menu functionality
  - Order processing
  - User authentication
  - Payment integration

## Deployment

Recommended deployment platforms:
- Heroku
- PythonAnywhere
- DigitalOcean

## Team Members

- Munieb Awad Elsheikhidris Abdelrahman
- Thaddeus Chong Zhuo Liang 
- Darren Lau Lit Zhang 
- Po Horng En 
- Munieb Awad Elsheikhidris Abdelrahman
- Wai Hpone 
- Min Thaw Khant 

## License

This project is licensed under the MIT License.

## Acknowledgments

- SWE30009 Software Testing and Reliability course
- Django Documentation
- Bootstrap Framework
