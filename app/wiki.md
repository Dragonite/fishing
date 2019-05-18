# Wiki

## Project Management Details
We worked towards an Agile system of light documentation, simplified end-to-end user stories and detailed screen mock-ups containing high-level information only on user flows.

* **Initial Planning** – The overall scope of the project was outlined in this phase. High level workflows and the choice of algorithms were decided in this phase. 

* **Iteration Planning** – The scope for each iteration was outlined. Detailed screen mockup were created in this phase. Screen mock-ups are documented in wiki.

* **Requirements** – The specific requirements were gathered, defined and documented into PBIs. The high level workflows were captured as a UML diagram. During this phase, we made assumptions on business values we were trying to deliver. We have constructed our requirements using user stories. PBIs were written in the format of “As a **role** , I can **goal/need** so that **why** ”. **goal/need** contains project specifications and **why** contains all the assumptions we collectively made. Workflow diagrams and screen mock-ups are documented in wiki.

* **Analysis & Design** – Software architecture and code is designed.

* **Implementation** – Construction of the actual code.

* **Testing** – Done during the Implementation phase, and done as QA & User Acceptance Testing at the end. Basic unit testings were automated. QA & User Acceptance Testing were done manually. The testing details and known bugs are documented in wiki under web testing cases.

---

## DB ER diagram

![](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5cdfa0057da937331f56cb6a/ef0fc702f03fddd35d5d26efc8d66506/Capture.PNG)

---


## PBIs

### ***As an Anonymous User, I want to be able to create an account so I can create polls***<br>
 **MoSCoW - Must**<br>
    Given  a user is not logged in <br>
    When  a user fills up all the mandatory forms <br>
    And all the user inputs are valid<br>
    And a user click submit button<br>
    Then a user account is created<br>
    And automatically go to login page<br>
    <br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`



### ***As an Anonymous User, I want to be able to see the list of polls so that I can decide what to do next***<br>
 **MoSCoW - Must**<br>
Given a user is not logged in<br>
When a user clickes completed poll/current poll from side menu<br>
Then a list of completed and current standing poll should be displayed<br>
<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`


### ***As an Account User, I want to be able to view open polls and completed polls result so that I can see other people's responses***<br>
 **MoSCoW - Must**<br>
Given a user is logged in<br>
When a user clicks the completed poll<br>
Then the details and result of the poll should be displayed<br>
<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`

Tech debt - If all the candidates get equal amount of votes, the first candidate ordered by candidate ID will be selected as a winner.

### ***As a Account User, I want to be able to submit my response to a poll so that I can contribute to the poll***<br>
 **MoSCoW - Must**<br>
Given a user is logged in<br>
And a user clicked a particular current standing poll<br>
When a user enters the preference order<br>
Then the response should be added to the poll<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`

### ***As an Account User, I want to be able to create a poll so I can get other people's opinions on a certain matter***<br>
 **MoSCoW - Must**<br>
Given a user is logged in <br>
When a user enters the details for a new poll<br>
And all the user inputs are validated<br>
And a user click submit button<br>
Then the poll should be created <br>
And take the user back to the poll list page<br>
<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`

 

### ***As an Admin User, I want to be able to add a user so that I can let the user create polls***<br>
 **MoSCoW - Must**<br>
Given a user is logged in as admin<br>
And a user clicks Users menu<br>
And click create user <br>
And a user fills up all the mandatory forms <br>
And all the user inputs are validated<br>
And a user click submit button<br>
Then the new user should be created<br>


### ***As an Admin User, I want to be able to delete users so that I can prevent a bad user making inappropriate polls and responses***<br>
 **MoSCoW - Must**<br>
Given a user is logged in as admin<br>
And a user clicks Users menu<br>
And click archive user<br>
And enter a user ID<br>
Then that particular user should be set inactive <br>
<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`


### ***As an Admin User, I want to be able to add a poll***<br>
 **MoSCoW - Must**<br>
Given a user is logged in as admin<br>
When a user enters the details of new poll
And a user fills up all the mandatory forms <br>
And all the user inputs are validated<br>
And a user click submit button<br>
Then the poll should be created <br>

<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`



### ***As an Admin User, I want to be able to add responses to a poll***<br>
 **MoSCoW - Must**<br>
Given a user is logged in as admin<br>
And a user is in poll details view<br>
When a user enters the preference order<br>
Then the responses should be added to the poll<br>
And the current result should be displayed<br>
<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`


### ***As an Admin User, I want to be able to delete responses from a poll so that I can exclude inappropriate responses from the poll result***<br>
 **MoSCoW - Must**<br>
Given a user is logged in as admin<br>
And a user is in poll list view<br>
And a user click archive response<br>
And a user enter a voter's user ID <br>
Then the response should be set inactive <br>
And excluded from results<br>
<br>

    `Manual System Testing - passed`
    `Manual User Acceptance Testing - passed`


### ***As an Account user, I want my poll to be closed automatically so that I don't need to close my poll manually***<br>
 **MoSCoW - Should**<br>
Given a user did not specify when to close my poll <br>
When the poll matures 7 days<br>
Then the poll needs to be closed automatically<br>


### ***As an Account user, I want my poll to be closed automatically when the minimum responses are collected so that I don't need to close my poll manually***<br>
 **MoSCoW - Could **<br>
Given a user did not specify when to close my poll <br>
When the poll matures 7 days<br>
Then the poll needs to be closed automatically<br>


### ***As an Anonymous User, I want to be able to see the results of polls so that I can see other people's responses***<br>
**MoSCoW - Could**<br>
When a user clicks the completed poll<br>
Then the details and result of the poll should be displayed<br>



### As an Account User when creating a poll I want to be able to choose the poll completion time using a calendar.
**MoSCoW - Could**<br>

### As an Account user, when creating a poll I want to be able to associate a colour to the poll using a colourwheel
**MoSCoW - Won't**<br>
### As an Account user, I want to be able to see the responses on Google Map if candidates are locational data
**MoSCoW - Won't**<br>



---


## UML Workflow Diagrams
### High Level Workflows

[High Level Workflows [PDF Form]](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5c9ca3018dcdcb376a25fbc8/3cdd0eaeec75a4f56c22dd0a0c8f0ab1/HighLevelWorkFLow.pdf)

### Preferential Vote Workflows

![](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5c9ca3018dcdcb376a25fbc8/07dbeb7373188c3726a4a1c8c6cbc752/prefVoting_algo.PNG)
## UX UI Design
![](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5c9ca49c45dc4b4378c9a21d/3c91aab9a1cd529973997d1c809af725/ScreenDesign_CreatePollView.JPG)



![](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5c9ca49c45dc4b4378c9a21d/67551ee41bd38aceb3900b5d307fd420/ScreenDesign_UserProfileView.JPG)


![](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5c9ca49c45dc4b4378c9a21d/58c27d53a13df9f97e58419a4532dc8d/ScreenDesign_PollResult_AdminViewJPG.JPG)

![](https://trello-attachments.s3.amazonaws.com/5c93a05805ab36040793f2b1/5c9ca49c45dc4b4378c9a21d/3f693502f59532493129887012333beb/ScreenDesign_PollView.JPG)


---


## Web Testing Cases


# Functionality Testing
This is used to check if the product is as per the specifications intended for it as well as the functional requirements charted out for it in developmental documentation. 

●	Testing fields and forms accept correct format / length data
    
    `Register form - passed`
    `Create a Poll - failed` (creating choices do not validate the length of input)

●	Verifying validation errors are presented to a user where invalid data is entered
    
    `Response form - passed`
    `Register form - failed`
    `Create a poll form - passed`

●	Ensure both internal and external links on a site function correctly

    `passed`

●	Verifying default values are being populated

    `Create a poll form - passed`

●	Successful flow through of basic flows in end-to-end business scenarios

    `passed` (please see UAT testing results under PBIs)

●	Verifying validation errors are presented when the business scenarios are executed incorrectly

    `passed`

●	Data flow across integration systems

    `passed`


# Usability Testing
This is used to check if the application is consistent in look, feel, terminology and workflow.

●	Consistency of UI, including colours / fonts / layout

    `passed`

●	Consistency of field names / formatting

    `passed`

●	Consistency of validation error message text and display formatting

    `failed (User registration form does not show why validation has failed)`

●	Ensuring no grammatical or spelling errors are present in the application

    `passed`

●	Business workflow is intuitive

    `passed`


# Interface Testing
This is used to check that queries made between the application, web and database layers return correct data when queries, and that validation errors are handled correctly.

●	Database errors are not shown to the end user

    `passed`

●	Application requests are handing correctly without being denied by the server

    `passed`

●	Queries sent to the database return expected results

    `passed`

# Compatibility Testing

This is used to check that a web application displays correctly across different devices, or at different resolutions.  This is using either done based on either market share, or as per requirements.

●	Testing across different web browsers

    `Chrome - passed`
    `IE - failed (will not fix)`
    `Safari - failed (will not fix)`
    `Firefox - passed`
    `Chrome - passed`


●	Testing certain combinations of operations systems & browsers

    `Windows - passed`
    `Mac - passed`
    `Linux - Not tested`

# Performance Testin
This is used to check a web application works under load.  This encompasses load testing, stress testing and responsiveness.

A python script for creating and querying large amount of poll data and loaded to the running web as a stress testing. We did not see any abnormal results. 



●	Verifying response times are acceptable when executing large queries

    `Not tested`

●	Verifying system responsiveness when loading data or image heavy page elements

    `Not tested

●	Caching is implemented effectively

    `Not tested`

●	Verifying the system responsiveness when large numbers of users are present on the system, or are executing the same functions simultaneously

    `Not tested

# Security Testing
This is used to check the system contains restrictions for user types, and protects user sessions and data
●	Verifying access to unauthorised pages is not permitted

    `Front End Web - passed`
    `API - failed (access is always denied with @token_auth.login_required)`

●	Ensuring that passwords are stored encrypted

    `passed`


