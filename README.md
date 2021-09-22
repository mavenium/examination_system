### How to install and run (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/mavenium/examination_system		# clone the project
cd examination_system		                                        # go to the project DIR
virtualenv -p python3 .venv		                                # Create virtualenv named .venv
source .venv/bin/activate		                                # Active virtualenv named .venv
pip install -r requirements.txt		                                # Install project requirements in .venv
python manage.py makemigrations		                                # Create migrations files
python manage.py migrate		                                # Create database tables
python manage.py collectstatic		                                # Create statics files
python manage.py runserver		                                # Run the project