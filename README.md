# mca204-networks

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

Standard Networking Protocols using [flask socketIO](https://github.com/miguelgrinberg/Flask-SocketIO/tree/master/example)

For more details, refer the [detailed readme](./README-detailed.md)

## Todo

* [x] shift google font to online version to remove mixed content error
* [ ] unipage deployment to heroku
  * merge all three with namespaces and serve in `app.py`
  * test local, test heroku local and deploy

## How to run

* git clone the repo and navigate to directory
* make sure you have pipenv installed, or run `brew install pipenv`
* type `pipenv shell` to activate the virtual environment
* install requirements from `requirements.txt` or pip lock file
* run `python app.py` and navigate to `localhost:5000` in browser
* disable debugging in `app.py` if you don't want messages in terminal
* similarly, run `stop-and-wait.py`, `go-back-N.py`, and `selective-repeat.py`

## How to deploy

* refer [heroku docs](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)  for more info
* `git add .` to stage everything
* `git status` to verify
* `git commit -m "Committing changes"`
* `git push`
* `heroku login`
* `heroku create <unique-app-name>`
* `git push heroku master`
* `heroku ps:scale web=1` to scale a dyno 
* `heroku open` to see the app

## Screenshots

### Stop and Wait

![Stop and Wait](./screenshots/stop-and-wait.png)

### Go Back N

![Go Back N](./screenshots/go-back-N.png)

### Selective Repeat

![Selective Repeat](./screenshots/selective-repeat.png)
