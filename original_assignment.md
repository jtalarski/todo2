## W16 Replacement: Python To-Do List

## The To-Do App

Similar to the 'TO DO' application from the weekend challenge back in Week9, this type of application is very common to tackle when learning a new language so it is a perfect 1st app to do when creating your first python server.

**Here are the specific components for the challenge:**

* Create a front end experience that allows a user to create a Task.
* When the Task is created, it should be stored inside of a database (SQL)
* Whenever a Task is created the front end should refresh to show all tasks that need to be completed.
* Each Task should have an option to 'Complete' or 'Delete'.
* When a Task is complete, its visual representation should change on the front end. For example, the background of the task container could change from gray to green. The complete option should be  'checked off'. Each of these are accomplished in CSS, but will need to hook into logic to know whether or not the task is complete.
* Whether or not a Task is complete should also be stored in the database.
* Deleting a Task should remove it both from the front end as well as the Database.


### Approach

We would recommend you spend some time researching python, discussing with your cohortmates, and building a small test app in python first.

### Create a Database

Be sure to create a new database through Postico. Use the name `python-to-do-app`. You will need to use this name in your database connection configuration on your server.

### Database Structure

Please include a `database.sql` text file in your repo that includes all of your `CREATE TABLE` queries. This is so we can re-create your database while testing your app.