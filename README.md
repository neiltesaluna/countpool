# countpool-experimental

Exploring the ability to store timers in **local storage** and in a **SQLite database** using SQLAlchemy.
JavaScript handles the munipulation of timers stored locally, whereas Python is used for timers stored in the database.

To display the timers to the user, these two data structures are then merged and ordered using JavaScript.
JavaScript is also used to countdown the timers displayed.

This project is using the **Flask web framework** and also incorporates **Bootstrap** styling.


## installation

To install the dependencies for this project, while in the root folder enter
<code>pip install -r requirements.txt</code>

Then you'll be able to run the project using
<code>python run.py</code>
