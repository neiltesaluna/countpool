# countpool-experimental

Exploring the ability to store timers in **local storage** and in a **SQLite database** using SQLAlchemy.
JavaScript handles the munipulation of timers stored locally, whereas Python is used for timers stored in the database.

To display the timers to the user, these two data structures are then merged and ordered using JavaScript.
JavaScript is also used to countdown the timers displayed.

This project is using the **Flask web framework** and also incorporates **Bootstrap** styling.


# Installation


## DOCKER
To run this project using docker, in your terminal enter to build the docker image: <code>docker build -t countpool .</code>

Then run initialize the docker container by entering the command: <code>docker run -p 5000:5000 countpool</code>

Access the website using http://0.0.0.0:5000/


## CMD
*it is strongly suggested to use virtualenv before installing the dependencies*

To install the dependencies for this project, while in the root folder enter: <code>pip install -r requirements.txt</code>

Then you'll be able to run the project using: <code>python3 run.py</code>

Access the website using http://0.0.0.0:5000/
