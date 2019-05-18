# Main
## Main Files
###`__init__.py`	 
`__init.py__` creates the blueprint object for core functionalities of this application and registers in the application functions.
###`routes.py` 
```
`routes.py` has the differnt URLs that this applcation implements. Functionalities defined in view functions for each URL are as below:
    index - main page view.
    create - provides a form for creating poll and renders templates for before/after creating poll.
    help - renders template for help page.
    current - provides a list of current standing poll and user objects to display the list of polls.
    current/<int:pollId> - provide a specific current standing poll object and a form for taking a response. 
    completed - provides a list of completed polls.
    completed/<int:pollId> - provide a specific completed poll object.
    archive - provides a form and functionality of archiving a poll
    users - provides a list of users
    users/archive - provides a form and functionality of archiving a user
    profile - renders template for profile page
    register - provides a form for user registration and renders templage for before/after creating a user
    users/create - provides a functionality for admin user to create a user.


```


