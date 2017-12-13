# request_counter
Description
This 0 points Assignment is a list of exercises for practicing Flask.

Steps
You can find multiple features which you can accomplish separately after the Preparation part. Do not forget to commit after you completed a part.

Preparation
First you should setup a completely new GitHub project for this Assignment.
Initialise a virtualenv for the project
Install Flask in the new virtualenv
Create an empty Flask application which you can use to implement the different features.
Install curl (Links to an external site.)Links to an external site., a command line request tool, to be able to send any type of HTTP requests.
Request counter - simple
Create a route called /request-counter. Every time someone makes a request to this route, increment a number (starting from zero)

Store the value in a global variable named counts
Redirect back to the frontend route
Request counter - pro
Upgrade the simple feature, but store different methods count in a global dict named counts where the keys are the method names: GET, POST, PUT, DELETE.

Request counter - save counts
Extend the pro or simple feature to store the request count data in a text file named request_counts.txt instead of global variable. The file should be located next to your python file. (Take care when you open the file HINT: http://stackoverflow.com/a/5137509 (Links to an external site.)Links to an external site.)
The request_counts.txt's content should look like this in case of the pro feature:
"GET: 5
POST: 3
DELETE: 1
PUT: 0"

HINT: to test DELETE/PUT request you can use curl after install it via apt get: https://www.garron.me/en/bits/curl-delete-request.html (Links to an external site.)Links to an external site. 

Frontend
Make a GET-Request link that sends a GET request to the /request-counter route.
Make a POST-Request button (in a form) that sends a POST request to the /request-counter route.
Make a Statistics link that navigates to the /statistics route.
Statistics
Create a route called /statistics.
Make a table that shows the request_counts.txt file's content.
Method	Count
GET	5
POST	3
DELETE	1
PUT	0
Make a link that navigates back to the frontend.
