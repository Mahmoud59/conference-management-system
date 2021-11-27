Conference Management System.

To run project:

1 - Clone project from GitHub 
    
    git clone https://github.com/Mahmoud59/conference-management-system

2 - In project directory beside requirements directory, 
    create a virtual environment by 

    virtualenv venv
    source venv/bin/activate

3 - Install packages in virtual environment by 

    pip install -r requirements/requirements.txt

    pip install -r requirements/test-requirements.txt 

4 - Create postgresql `conference` database.

5 - Migrate apps migrations 

    ./manage.py makemigrations
    ./manage.py migrate

6 - In main app directory Create super user 'Admin' 
    
    ./manage.py createsuperuser
    username: 'admin'
    email: 'admin@admin.com'
    password: '####'

7 - After run project, open swagger docs in a main link 
    
    http://127.0.0.1:8000

8 - For login in with username: 'admin', password: '###'

    127.0.0.1:8000/api/v1/participants/login/
    
9 - For create Conferences

    127.0.0.1:8000/api/conferences/

10 - For create Conferences Talks 

    127.0.0.1:8000/api/v1/conferences/conference_id/talks/

11 - For modify Talks Participants or Talks Speakers

    127.0.0.1:8000/api/v1/talks/talk_id/participants/

12 - For run unit test, run `pytest` in apps src directory.

13 - You can run `flake8 --statistics` for characters limited in one line.

14 - You can run `isort .` for sort importing packages, function, and classes.
