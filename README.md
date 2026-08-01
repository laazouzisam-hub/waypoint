# Waypoint

Waypoint is my Django project for the term assignment.

## What is in the project

The project includes:

- a home page
- a report form
- a thank-you page
- a search page
- shared templates and CSS
- a trail catalog
- a Trail model connected to the database
- Django admin for managing trail data

For Week 12, I moved the trail data into the database and used Django admin to manage it instead of keeping everything hardcoded in the views [file:371].

## Tools used

This project uses:

- Python
- Django 4.2
- SQLite
- HTML templates
- CSS

## Important note

One of the main problems I faced was a Python and Django version incompatibility.  
At first, my environment was using a newer Python version, and that caused issues with Django and the admin setup. To move forward, I had to create a new virtual environment with a lower Python version, reinstall the project requirements, and then continue working from that environment.

## How to run the project

First clone the repository:

```bash
git clone <your-repo-link>
cd waypoint
```

Create a virtual environment:

```bash
python -m venv env
```

Activate it.

On Windows:

```bash
env\Scripts\activate
```

On macOS or Linux:

```bash
source env/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Then open this in your browser:

```text
http://127.0.0.1:8000/
```

## Main pages

Some main routes in the project are:

- `/` for the home page
- `/report/` for the trail report form
- `/search/` for search
- `/catalog/` for the catalog page
- `/trails/` for trails coming from the database
- `/admin/` for the Django admin

## Admin

The admin page is used to add, edit, and manage trail records.  
For Week 12, the public trails page shows open trails, while all trail records can still be managed in the admin area [file:371].

If needed, create an admin account with:

```bash
python manage.py createsuperuser
```

Then go to:

```text
http://127.0.0.1:8000/admin/
```

## Running tests

To run tests:

```bash
python manage.py test
```

## Git and submission

This project was built in weekly branches and merged into `main` after each part.  
The assignment also requires the README to be updated when setup steps change, and the grader should be able to run the project using the README instructions [file:371].

## AI use

I used Perplexity.ai to help me understand some setup and debugging issues, especially around the Python/Django compatibility problem.  
All code I submitted was reviewed by me and I understand the work I turned in, which is required by the assignment rules for AI use.
