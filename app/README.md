# App
## Main Files
###`__init__.py`	 
`__init.py__` creates the blueprint object forthis application and registers in the application functions.
###`controllers.py` 
`controllers.py` provides functions that takes each objects and commit to database as well as functions that query DB. It also contains the function to record user login time.
###`models.py`
`models.py` represents User and Poll object. Each object contains neccessary properties and methods.
###`pollForm.py`  
`pollForm.py` contains WTForm definitions for creating poll, making responses, closing poll and deleting user, poll and responses. 
###`registrationForm.py` 
`registrationForm.py` contains WTForm definition for creating user.
###`views.py` 
`views.py` will contain server-side rendering functions. However, other than dynamic forms in pollForm and main.routes render_template, server-side rendering is not implemented in this application.