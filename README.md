FastAPI-Django API 
===================================================================================================================================================================================
What is the FastAPI?
FastAPI is a python-framework which is faster than Flask for APIs. It is useful to create a RESTful API. In this Project I have created an API which utilizes the following methods:
 1. HTTP GET
 2. HTTP POST
 3. HTTP DELETE
 4. HTTP PATCH
 
 
These methods are implemented and they directly change the data using Django-ORM. The table mentioned in the models change with the methods.

Why FastAPI?
===================================================================================================================================================================================


Django Rest Framework is the go-to library for APIs of larger dimensions and projects. FastAPI  allows the developer to implement smaller APIs faster. MicroAPIs can be easily 
implemented with FastAPI. The integration of FastAPI is simpler and routing can be done in a clean and neat way. Multiple API Routers can be established using FastAPI.

How is FastAPI Integrated?
===================================================================================================================================================================================

The FastAPI can be interfaced with Django by mounting the features of API onto the ASGI/WSGI file. The specific instructions of setting the WSGI/ASGI is explained in the file 
TestingProject/asgi.py. WSGI --> Webserver Gateway Interface.

Currently there is a limitation to integrating ASGI to the API. FastAPI doesnot natively support ASGI integration currently.

For middleware references check out : https://fastapi.tiangolo.com/tutorial/middleware/

How to start the project and get it running?
===================================================================================================================================================================================
Step 1: Clone the repository
Step 2: Establish the Virtual Environment using Python or Conda
Step 3: Install the command using pip
Step 4: Run the app using command 4
```
1> git clone https://github.com/AbhijithGanesh/FastAPI-Django-Integration
2> python -m venv VirtualEnvironment
3> pip install -r requirements.txt
4> uvicorn TestingProject.asgi:app --debug
```
