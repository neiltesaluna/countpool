# countpool

This web application allows users to save their countdown timers in their browser's **local storage** or in a persistant **MySQL database**.

To display the timers to the user, these two data structures are then merged and ordered using JavaScript. Coutdown timers that are saved in the database are visible to anyone.

This project is using the **Flask web framework** and also incorporates **Bootstrap 4** styling. **Nginx** is used as a Webserver, **Gunicorn** as a WSGI, hosted on an **EC2 Instance** and is using **MySQL RDS** on AWS.

https://countpool.tesaluna.com/


# Initial Setup
We need to first set up a few environment variables for the project.
I have attached an **.env_example** file, you can change the desired variables and **rename the file** to **.env**

```
SECRET_KEY='string_of_random_stuff'
MYSQL_DATABASE='dbname'
MYSQL_USER='mysqluser'
MYSQL_PASSWORD='mysqlpassword'
MYSQL_PORT='3306'
# this is from the name of the docker container in the docker-compose file.
MYSQL_HOST='sqldb'
```

## Running the application locally
In the countpool/\_\_init\_\_.py file, we need to change the SQLALCHEMY_DATABASE_URI variable to the following below to run this project locally.<br />

`SQLALCHEMY_DATABASE_URI = sqlite:///database.db`


## DOCKER COMPOSE - Installation to use MySQL database image
After setting up the .env file, to run this project using docker compose, in your terminal enter:<br />
`docker compose up`


## DOCKER - Installation to use local SQLite database
First set up the application to use an **SQLite database**, then run the following commands below. <br />

To run this project using docker, in your terminal enter to build the docker image:<br />
`docker build -t countpool .`

Then initialize the docker container by entering the command:<br />
`docker run -p 5000:5000 --env-file ./.env countpool`

Access the website using http://0.0.0.0:5000/

#### NOTE
If you want to see changes to the APP while you edit, you need to enter this command instead:<br />
`docker run -p 5000:5000 --env-file ./.env -v [PROJECT FULL PATH]/countpool:/usr/src/app countpool`<br /><br />
*(-v) Volumes gives the ability for the container to see files on the host machine*
