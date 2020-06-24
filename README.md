# aws_elastic_beanstalk_flask
Quick walk-through on how to use AWS Elastic Beanstalk to deliver Python Flask web applications.

# Steps
## 0
Create your own virtual Python environment in your app directory
```bash
$ pip install flask
$ pip freeze > requirements.txt
```

## 1
```bash
$ cd ~/dev
$ mkdir eb-flask-app
$ cd eb-flask-app
$ git init
$ eb init
$ touch .ebignore
```

## 2
```bash
$ git checkout -b dev
$ git push --set-upstream origin dev
```

## 3
Set up basic files for Flask app and local setup and running the app.
```bash
$ touch application.py
$ touch run.sh && chmod +x ./run.sh
$ touch setup.sh && chmod +x ./setup.sh
$ mkdir templates
$ touch templates/index.html
$ touch templates/username.html
```

## 4
For local dev and testing
```bash
$ vim setup.sh
$ vim run.sh
```

## 5
```bash
$ vim application.py
$ vim templates/index.html
$ vim templates/username.html
```

## 6
Commit your changes to git
```bash
$ git status
$ git add .gitignore README.md .ebignore application.py requirements.txt run.sh setup.sh templates/
$ git commit -a -m "Initial commit for a barebone Python Flask web app."
```
Make sure it runs locally well.

## 7
Create and deploy EB dev environment
```bash
$ eb create eb-flask-app-DEV
$ eb list
$ eb deploy
$ eb open
```
Ensure it works on EB environment eb-flask-app-DEV.

## 8
Now merge work in dev branch into master branch and call it v1.0
```bash
$ git checkout master
$ git merge dev
$ git tag -a "v1.0" -m "First version."
$ eb deploy -l "eb-flask-app v1.0"
$ eb open
```

## 9
```bash
```

## 10
```bash
```

## 11
```bash
```

## 12
```bash
```

## 13
```bash
```

## 14
```bash
```

## 15
```bash
```

## 16
```bash
```

## 17
```bash
```

## 18
```bash
```

## 19
```bash
```

## 20
```bash
```

