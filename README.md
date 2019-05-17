# Fishing Polling &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Dragonite/CITS3403-Project/blob/master/LICENSE) [![Python 3.7.2](https://img.shields.io/badge/python-3.7.2-blue.svg)](https://www.python.org/downloads/release/python-372/) [![Flask 1.0.2](https://img.shields.io/badge/flask-1.0.2-blue.svg)](https://pypi.org/project/Flask/)


Fishing Polling Application written for CITS3403's [Project](http://teaching.csse.uwa.edu.au/units/CITS3403/index.php?fname=projects&project=yes) in Semester 1 2019.

Fishing Polling is a web-based polling system where a user can create polls to collect other peoples opinion and/or make responses to other people's polls. This application uses both preferential voting and first past the post voting method. 

The preferential voting result is displayed as "current winner" for ongoing polls and "Poll winner" for completed polls.
First past the post voting result is displayed as a pie chart so that a user can navigate through a collection of peoples' each preference. 

Currently supporting features are as below:
1. An anonymous user can view the list of polls.
2. A user can create an account.
3. A user can login and logout using username and password
4. A User can create a poll with multiple prefilled choices
    - A user can decide whether the created poll is a open poll or close poll
      -open poll: A user can view the current result before the poll is completed.
      -close poll: A user can view the result only once the poll is completed.
    - A user can view a list polls that he/she created in the past and marke them as completed.
5. A user can make a response to a poll
6. There are two user roles: admin and normal user
    Admin user can
     Create user
     Delete user (soft delete-archive user)
     Create polls
     Archive polls
     Delete responses (soft delete-archive responses)
     Make a response to a poll 

Currently the theme is set to fishing but this application can be used for any type of survey. 

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
