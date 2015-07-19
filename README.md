# Osler

This is our clintools project, which is a collection for all our
patient tracking. It's a django project.

## Running locally

First, clone our repository

```bash
git clone https://github.com/SaturdayNeghborhoodHealthClinic/clintools.git
```

First, get [pip](https://pip.pypa.io/en/stable/).

We also recommend running Osler in a virtual environment.
If you're going to run our project in a virtual env do th following:

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Then use pip install our dependencies with 

```bash
pip install -r requirements.txt
```

(Python dependencies are stored in `requirements.txt`)

Once you've done that, *from the `clintools/` build the test database with

```bash
sh scripts/reset_db.sh
```

This script is also used to rebuild the test database after making database
changes require migrations. Then, you can run the project in debug mode with

```bash
python manage.py runserver --settings clintools.debug_settings
```
