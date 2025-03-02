#！/bin/zsh

export FLASK_APP=app.py
export FLASK_ENV=development
pipenv  run flask run --host=0.0.0.0 --port=5000