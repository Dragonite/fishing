# CITS3403 Project: Fishing Polling

Fishing Poll application written for CITS3403's [Project](http://teaching.csse.uwa.edu.au/units/CITS3403/index.php?fname=projects&project=yes) in Semester 1 2019.

About Fishing Polls:

Fishing Poll is a web-based polling system where a user can create polls to collect other peoples opinion and/or make responses to other people's polls. This application uses both preferencial voting and first past the post voting method. 

The preferencial voting result is displayed as "current winner" for ongoing polls and "Poll winner" for completed polls.
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

Currently the theme is set to fishing but this application can be used for any type of surveys. 



## Project Management Details
Appstablishment are working towards an Agile system of light documentation, moderately detailed user stories and detailed screen mock-ups containing high-level information only on user flows.  

●	Initial Planning – The overall scope of the project was outlined in this phase. High level workflows and the choice of algorithms were decided in this phase. 
●	Iteration Planning – The scope for this iteration was outlined. Detailed screen mockup were created in this phase. Screen mockup is documented in wiki.
●	Requirements – The specific requirements were gathered and documented into PBIs. The high level workflows were captured as a UML diagram. During this phase, we made assumptions on business values we were trying to deliver. We have constructed our requirements using user stories. PBIs were written in the format of “As a <role or persona>, I can <goal/need> so that <why>”. <goal/need> contains project specifications and <why> contains all the assumptions we collectively made.  Workflow diagrams and screen mockups are documented in wiki.
●	Analysis & Design – Software architecture and code is designed. 
●	Implementation – Construction of the actual code. 
●	Testing – Doneduring the Implementation phase, and done as QA & User Acceptance Testing at the end. Basic unit testings were automated.  QA & User Acceptance Testing details and known bugs are documented in wiki.


Please see the [wiki](https://github.com/Dragonite/CITS3403-Project/wiki) 


## Virtual environment requrement
$ pip install -r requirements.txt


## How to Launch app
1. git clone
2. pip install -r requirements.txt
3. export FLASK_APP=FishingPoll.py

## How to Launch testing suite
1. python -W ignore tests.py

## Libraries Used
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)
- [Notify.js](https://github.com/msroot/Notify.js/)
- [Chart.js](https://www.chartjs.org/)
- [Chart.js Datalabels](https://github.com/chartjs/chartjs-plugin-datalabels)
- [DataTables](https://datatables.net/)
- [W3Schools](https://www.w3schools.com/)

## Authors
- Haolin Wu ([21706137](https://github.com/dragonite)) 
- Luna Sohee Lee ([22187554](https://github.com/lunico86))

## Acknowledgements

- Lecture slides and tutorials forming the base of the application written by [Dr. Tim French](https://github.com/drtnf).
- Flask Mega Tutorial written by [Miguel Grinberg](https://github.com/miguelgrinberg).

## License

MIT License, Copyright © Haolin Wu 2019
