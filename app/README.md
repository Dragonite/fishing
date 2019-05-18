# App

## Main Files

### `__init__.py`  

  `__init.py__` creates the blueprint object for this application and registers in the application functions.

---

### `controllers.py` 

  `controllers.py` provides functions that takes each objects and commit to database as well as functions that query DB. It also contains the function to record user login time.
```
createUser(User, password) / takes a User object and password, set password hash, and commit all the attributes to database
modifyUser(User) / takes a User object and commit the changes to database
login_time(User) / takes User object, move current login time to last login time and then record current login time
archiveUser(User) / takes User object, set isActive to false and commit to database
getUserById(userId) / takes user ID and returns the matching user object
getUserByUsername(username) / takes username and returns the matching user object
getAllUsers() / returns a list of all users
createPoll(Poll) / takes a Poll object and commit the poll and its candidates to database
modifyPoll(Poll) / takes a Poll object and commit the changes to database
archivePoll(Poll) / takes poll object, set isActive to false and commit to database
getPollById(pollId) / takes poll ID and returns the matching poll object
getAllPolls() / returns a list of all polls
getClosedPolls(isAdmin=False) / returns a list of all completed and active polls as a default, if isAdmin is set to True, returns a list of all completed polls
getCurrentPolls(isAdmin=False)/ returns a list of all current standing and active polls as a default, if isAdmin is set to True, returns a list of all current standing polls
archiveResponse(Poll, userId) / takes a Poll object and user id and archive matching user's response for the poll 
```
---

### `models.py`

`models.py` represents User and Poll object. Each object contains neccessary properties and methods.
```
User Methods


User.validate() / returns true if User object has firstname, email and username
User.set_password('1234') / set password to 1234
User.check_password('1234') / returns true if 1234 is the right password
User.get_id() / returns id assigned by DB
User.get_token() / returns API token  for the user
User.revoke_token() / revokes token for the user
User.check_token('DFJIEW213') / returns true if the user token is correct 
User.howManyResponses() / returns the number of all the responses User ever made
User.howManyPolls() / returns the number of all the polls User ever made
User.to_dict() / returns all the properties in dictionary so it can be turned into Json
User.from_dict() / takes dictionary and sets all the attributes

```
```
Poll Methods


Poll.Candidate / returns a list of all candidates for this poll
Poll.Response / returns a list of all responses for this Poll
Poll.howManyCandidates() / returns a number of candidates this poll has
Poll.howManyResponses()/ returns a number of responses this poll has
Poll.getResponseDict() / returns all the responses for this poll inn dictionary
Poll.close() / change the poll status from current standing to completed and return true
Poll.isClosed() / return true for completed poll and false for current standing
Poll.validate() / returns true if Poll object title, orderCandidateBy, createdUserId and more than 1 candidates
Poll.get_id() / returns id assigned by DB
Poll.addCandidate(description, displayorder) / takes description, add to the poll as a candidate and then return true
Poll.getCandidateId(candidateDescription) / takes candidate description and return the id assigned by DB
Poll.getCandidateById(candidateId) / takes candidate ID and returns Candidate object that matches candidate ID
Poll.addResponse(userId, response) / take user id and response dictionary and create a response for this poll
Poll.get_rawResult()  / returns First Past the Post voting result for this poll 
Poll.get_prefResult() / returns Preferential Voting result for this poll 
Poll.to_dict() / returns all the properties in dictionary so it can be turned into Json
Poll.from_dict() / takes dictionary and sets all the attributes
```
---

### `pollForm.py`  

`pollForm.py` contains WTForm definitions for creating poll, making responses, closing poll and deleting user, poll and responses. 

---

### `registrationForm.py` 

`registrationForm.py` contains WTForm definition for creating user.

---

### `views.py` 

`views.py` will contain server-side rendering functions. However, other than dynamic forms in pollForm and main.routes render_template, server-side rendering is not implemented in this application.