# countpool-experimental

Exploring the ability to store timers in **local storage** and in a **SQLite database** using SQLAlchemy.
JavaScript handles the munipulation of timers stored locally, whereas Python is used for timers stored in the database.

To display the timers to the user, these two data structures are then merged and ordered using JavaScript.
JavaScript is also used to countdown the timers displayed.

This project is using the **Flask web framework** and also incorporates **Bootstrap** styling. Countpool is using **Nginx** as a Webserver, **Gunicorn** as a WSGI and is hosted on an **EC2 Instance** on AWS

https://countpool.tesaluna.com/


# Installation


## DOCKER
To run this project using docker, in your terminal enter to build the docker image:<br />
`docker build -t countpool .`

Then initialize the docker container by entering the command:<br />
`docker run -p 5000:5000 countpool`

Access the website using http://0.0.0.0:5000/

#### NOTE
If you want to see changes to the APP while you edit, you need to enter this command instead:<br />
`docker run -p 5000:5000 -v [PROJECT FULL PATH]/countpool-experimental:/usr/src/app countpool`<br /><br />
*Volumes just gives the ability for the container to see files on the host machine*


## CMD
*it is strongly suggested to use virtualenv before installing the dependencies*

To install the dependencies for this project, while in the root folder enter: `pip install -r requirements.txt`

Then you'll be able to run the project using: `python3 run.py`

Access the website using http://0.0.0.0:5000/
