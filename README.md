Django Ecommerce Website
Django Ecommerce Website using Tailwind, htmx, and Django.

Features
User authentication with email and phone number
Shopping cart functionality
Product filtering and searching
Product listing and detail pages
Checkout and order confirmation
Requirements
Django 3.2 or higher
Python 3.8 or higher
Tailwind CSS
htmx
Pillow (for image resizing)
Installation
Clone the repository
git clone https://github.com/yourusername/your-repository.git



Create a virtual environment and activate it
python3 -m venv env
source env/bin/activate



Install the requirements
pip install -r requirements.txt



Run migrations
python manage.py migrate



Create a superuser
python manage.py createsuperuser



Run the server
python manage.py runserver



Access the website at http://localhost:8000
Testing
To run the tests, execute the following command:

python manage.py test



Deployment
To deploy the website, follow these steps:

Build static files
python manage.py collectstatic



Apply database migrations
python manage.py migrate



Create a superuser
python manage.py createsuperuser



Run the server
python manage.py runserver



Built with
Django
Tailwind CSS
htmx
Pillow
License
This project is licensed under the MIT License.



