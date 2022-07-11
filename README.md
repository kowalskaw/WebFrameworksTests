# WebFrameworksTests
Project is meant to load and performance test Python micro frameworks for web development.
Chosen frameworks:
* FastAPI - 0.78.0
* Falcon - 3.1.0
* Flask -  2.1.2
* CherryPy -  18.6.1
* Tornado - 6.1

## Environment setup
Create virtual environment and activate it. Install packages in new virtual environment:
* FastAPI 
```    
    $ pip3 install fastapi "uvicorn[standard]"
```
* Falcon
```
    $ pip3 install falcon cython "uvicorn[standard]"
    $ git clone https://github.com/falconry/falcon
```
* Flask
```
    $ pip3 install flask
```
* CherryPy
```
    $ pip3 install cherrypy
```
* Tornado
```
    $ pip3 install tornado
```
After installation of proper dependencies, activate the virtual environment.
```
    $ source venv/bin/activate
```

## Run uvicorn server
In order to run a uvicorn server, there has to be python module and filename specified. File should contain initialized app object.
```
    $ uvicorn module_name.app:app --reload
```
## Run Flask 
To run Flask server enter below command in terminal.
```
    $ cd ./servers/flask 
    $ flask run
```
## Run FastAPI server
To run Flask server enter below command in terminal.
```
    $ cd ./servers/fast_api 
    $ uvicorn main:app --reload

```
## Run locust
```
locust --host http://localhost:3000 --users number_of_users --spawnrate spawn_rate_number
```