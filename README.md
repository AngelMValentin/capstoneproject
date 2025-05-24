Surgical Tech Companion App

This Django-based web application helps surgical technologists study for AST / NBSTSA Certification Exams using flashcards, 3D models, and quizzes.

Project Requirements

- Python 3.10+
- Django 4.x
- SQLite3 (default)
- pip (Python package installer)
- Git (optional)

Setup Instructions


1. Clone the Repository (or copy project files)

    git clone https://github.com/AngelMValentin/capstoneproject
    cd capstoneproject

2. Set Up and Activate Virtual Environment

    python3 -m venv venv
    source venv/bin/activate        # macOS/Linux
    venv\Scripts\activate           # Windows

3. Install Required Packages

    pip install -r requirements.txt

4. Run Initial Migrations

    python manage.py migrate

5. Create Superuser (for admin access)

    python manage.py createsuperuser

6. Load Initial Data (Optional)

If you're using fixtures or loading instruments via script:

   python manage.py loaddata instruments.json

Or if loading via CSV, use the management command or script you created.

7. Run the Development Server

    python manage.py runserver

8. Access the App

    Visit http://127.0.0.1:8000 in your browser.

    Admin panel: http://127.0.0.1:8000/admin

Database Structure (Key Models)

- InstrumentType: Categories (e.g., Scalpels, Retractors)
- Instrument_NameAndDescription: Contains specific instrument names and their descriptions.
- QuizQuestion: Questions with four multiple-choice options related to instruments.
- Flashcard: Flashcard content related to surgical procedures and principles.
- AnatomySystem: Contains anatomical system names and their respective specialty.

Populating the Database via CSV

To load instruments using a CSV:
- Make sure your CSV file is formatted with columns:
    instrumentType, specificInstrument, description
- Use a script or Django management command to read and populate models using the Django ORM.

Contact

If you encounter issues or have suggestions, feel free to reach out:
- Email: angelvalentinusmc@gmail.com
