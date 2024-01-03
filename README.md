# Official Website

This website is coded using Python and powered by Django. The purpose of the project
is [brief description about the project].

## Installation

To set up the project in your local environment, follow the steps below:

1. Go to our [project repository](https://github.com/musakavus/render_test_django).
2. Clone the code to your computer:
    ```bash
    git clone https://github.com/musakavus/render_test_django.git
    ```
3. Create a virtual environment and install the required packages:
    ```bash
    cd project
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. Create the database and perform migrations:
    ```bash
    python manage.py migrate
    ```
5. Configure the environment variables in your `settings.py` file:

    - Open the `settings.py` file located in the project directory.
    - Find the section related to environment variables.
    - Update the values of the environment variables according to your configuration.
