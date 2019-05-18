# Fishing Polling &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Dragonite/CITS3403-Project/blob/master/LICENSE) [![Python 3.7.2](https://img.shields.io/badge/python-3.7.2-blue.svg)](https://www.python.org/downloads/release/python-372/) [![Flask 1.0.2](https://img.shields.io/badge/flask-1.0.2-blue.svg)](https://pypi.org/project/Flask/)


Fishing Polling Application written for CITS3403's [Project](http://teaching.csse.uwa.edu.au/units/CITS3403/index.php?fname=projects&project=yes) in Semester 1 2019.

Fishing Polling is a web-based polling system where a user can create polls to collect other peoples opinion and/or make responses to other people's polls. This application uses both **Preferential Voting** and **First Past the Post** voting method. 

The **Preferential Voting** result is displayed as *Current Winner* for ongoing polls and *Poll Winner* for completed polls.

**First Past the Post** voting result is displayed as a pie chart so that a user can navigate through a count of each preference for all users. 

## Supported Features

### User Types

**Anonymous User**: 
- Can view a list of polls, can register an account to the website.

**Registered User**:
- Can log in and out using their username and password.
- Can create polls(Open or Closed) with their own declared choices.
- Can vote on polls.

**Administrator**:
- Can delete a user*
- Can delete a poll*
- Can delete another user's vote*
- Can create a poll
- Can vote on polls.

### Poll Types

**Open/Closed Polls**:

Open Polls allow registered users to see current results when browsing a poll. Sometimes, a poll creator may not want
their users to see a current result, as it can affect their voting choice, so an option is made available for the poll creator.

**Current/Completed Polls**:

By default, polls created are *Current* polls. The creator of the poll has the option to make their poll *Completed*, so that
no more votes are accepted on it, and the poll is marked *Completed*.

*These are *soft deletes*, i.e. Archiving a poll, as we want to preserve the history of a poll or user.

Note: This site is made for Fishing Polling, but in theory, any poll of interest can be created.


## Explanation of Code
```
Explanation of Code can be found in `README.md` in further levels of the application.

Fishing Polling Application is constructed with three subsystems: RESTfulAPI, user authentication and main. Blueprints is implemented to user an application factory function to create the function that accepts a configuration object as an argument and returns a flask application instance. The application structure and the explanations are as below:

app/
		api/								    <-- blueprint package: RESTful API
			__init__.py						<-- blueprint creation for API
			auth.py							   <-- User Authentication and token verification place holder
			errors.py						  <-- Error handling placeholder
			routes.py						  <-- API resource placeholder
			tokens.py						  <-- Token handling placeholder
		auth/								    <-- blueprint package: User Authentication
			__init__.py						<-- blueprint creation for user authentication
			forms.py						  <-- login form
			routes.py						  <-- login view functions and authentication routes
		errors/                 <-- blueprint package
			__init__.py           <-- blueprint creation
			handlers.py           <-- error handlers
		main/								    <-- blueprint package: core functionalities 
			__init__.py						<-- blueprint creation for main app
			routes.py					  	<-- Main menu view and operation functions routes
		static/
			css/
			javascript/
		templates/							<-- collection of templates
			archive-components/
			auth/
			compenents/
			current-components/
			errors/                         
			help/
			index/
			poll-views/
			profile/
			users/
			.....html
		__init__.py             <-- blueprint registration
		controllers.py					<-- Poll and User CRUD operation controllers representation
		models.py							  <-- Poll and user model representation
		pollForms.py						<-- Poll registration and modification forms
		registrationForm.py			<-- User registration form
		views.py							  <-- Server-side rendering (not yet implemented)
	FishingPoll.py						<-- Main application module
	tests.py								  <-- Unit testing script: Testing configuration, creates an application for test suits and run tests

There are 2 main objects in Fishing Polling Application: User and Poll.
User represents each registered user. 
Poll represents poll and is a nested object that contains multiple Candidate objects and Response objects.

Both Poll and User objects are designed based on Single responsibility principle. 
Hence, User class defined in model.py has not only the properties required but also functions to provide the complete functionalities. Likewise, Poll class defined in model.py has all the properties as well as functions to provide all the functionlities that requires Poll object. 

Controller provides functions for database CRUD operation. 

Naming conventions are used to to reduce the effort needed to read and understand source code. So the detailed explation of each functions and variables are not listed here. 

```
## Explanation of Database
```
  [ER diagram](https://github.com/Dragonite/CITS3403-Project/wiki/DB-ER-diagram)

  users (
        token VARCHAR(32),
        token_expiration DATETIME,
        "userId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "firstName" VARCHAR(64) NOT NULL,
        "lastName" VARCHAR(64),
        username VARCHAR(64) NOT NULL,
        "pwdHash" VARCHAR(128),
        email VARCHAR(128) NOT NULL,
        ad_street VARCHAR(64),
        ad_suburb VARCHAR(64),
        ad_state VARCHAR(64),
        ad_country VARCHAR(64) DEFAULT 'Australia',
        "createdAt" DATETIME,
        "lastModifiedAt" DATETIME,
        "isActive" BOOLEAN,
        "isAdmin" BOOLEAN,
        "lastLogin" DATETIME,
        "currentLogin" DATETIME,
        UNIQUE (email),
        UNIQUE (username),
        CHECK ("isActive" IN (0, 1)),
        CHECK ("isAdmin" IN (0, 1))
  )

polls (
        "pollId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(64) NOT NULL,
        description VARCHAR(250),
        "createdAt" DATETIME,
        "lastModifiedAt" DATETIME,
        "completedAt" DATETIME,
        "orderCandidatesBy" VARCHAR(12),
        "minResponses" INTEGER,
        "openAt" DATETIME,
        "closeAt" DATETIME,
        "createdByUserId" INTEGER NOT NULL,
        "isOpenPoll" BOOLEAN,
        "isActive" BOOLEAN,
        FOREIGN KEY("createdByUserId") REFERENCES users ("userId"),
        UNIQUE (title),
        CHECK ("orderCandidatesBy" IN ('Desc', 'Acs', 'SpecialOrder')),
        CHECK ("isOpenPoll" IN (0, 1)),
        CHECK ("isActive" IN (0, 1))
)

candidates (
        "candidateId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "candidateDescription" VARCHAR(128) NOT NULL,
        "displayOrder" INTEGER,
        "isActive" BOOLEAN,
        "pollId" INTEGER NOT NULL,
        FOREIGN KEY("pollId") REFERENCES polls ("pollId"),
        CONSTRAINT unique_candidates UNIQUE ("pollId", "candidateDescription"),
        CHECK ("isActive" IN (0, 1))
);

responses (
        "responseId" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "userId" INTEGER NOT NULL,
        "pollId" INTEGER NOT NULL,
        "candidateId" INTEGER NOT NULL,
        "isActive" BOOLEAN,
        response INTEGER,
        "createdAt" DATETIME,
        FOREIGN KEY("candidateId") REFERENCES candidates ("candidateId"),
        FOREIGN KEY("pollId") REFERENCES polls ("pollId"),
        FOREIGN KEY("userId") REFERENCES users ("userId"),
        CONSTRAINT unique_resonses UNIQUE ("userId", "pollId", "candidateId", response),
        CHECK ("isActive" IN (0, 1))
);
```
## Planning and Agile Methodology

These resources can be found on the [Fishing Polling Wiki](https://github.com/Dragonite/CITS3403-Project/wiki).

[Project Management](https://github.com/Dragonite/CITS3403-Project/wiki/Project-Management-Details)

[Trello](https://trello.com/b/HJlN0mPe/cits3403-project)


## Installation
```
$ git clone https://github.com/Dragonite/CITS3403-Project.git
$ pip install -r requirements.txt
$ export FLASK_APP=FishingPoll.py
```

## Execution
```
$ FLASK_APP=FishingPoll.py FLASK_DEBUG=1 python -m flask run
```

## Executing Testing Suite
```
$ python -W ignore tests.py
```

## Libraries Used
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)
- [Notify.js](https://github.com/msroot/Notify.js/)
- [Chart.js](https://www.chartjs.org/)
- [Chart.js Datalabels](https://github.com/chartjs/chartjs-plugin-datalabels)
- [DataTables](https://datatables.net/)
- [Moment.js](https://momentjs.com/)
- [W3Schools](https://www.w3schools.com/)

## Authors
- Haolin Wu ([21706137](https://github.com/dragonite)) 
- Luna Sohee Lee ([22187554](https://github.com/lunico86))

## Acknowledgements

- Lecture slides and tutorials forming the base of the application written by [Dr. Tim French](https://github.com/drtnf).
- Flask Mega Tutorial written by [Miguel Grinberg](https://github.com/miguelgrinberg).

## License

[MIT License](https://github.com/Dragonite/CITS3403-Project/blob/master/LICENSE), Copyright © Haolin Wu 2019
