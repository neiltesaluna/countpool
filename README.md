# countpool

Exploring the ability to store timers in **local storage** and in a **MySQL database** using SQLAlchemy.
JavaScript handles the timers stored locally, whereas Python is used for timers stored in the database.

To display the timers to the user, these two data structures are then merged and ordered using JavaScript.
JavaScript is also used to countdown the timers displayed.

This project is using the **Flask web framework** and also incorporates **Bootstrap** styling. **Nginx** is used as a Webserver, **Gunicorn** as a WSGI and is hosted on an **EC2 Instance** on AWS.

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
First we need to install the dependencies into a virtual environment, while in the project root:<br />`python3 -m venv env`

Now we need to activate the virtual environment using:<br />`source env/bin/activate`

You can confirm if you're in the virtual environment using:<br />`which python`

Now we can install the dependencies for this project in the virtual environment using:<br />`pip install -r requirements.txt`

Then you'll be able to run the project using:<br />`python3 run.py`

Access the website using http://0.0.0.0:5000/

to deactivate the virtual environment simply use:<br />
`deactivate`

You can confirm if you're out of the virtual environment using:<br />`which python`
