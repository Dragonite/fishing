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

Explanation of Code can be found in `README.md` in further levels of the application.



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
