# WebFrameworksTests
Project is meant to load and performance test Python micro frameworks for web development.
Chosen frameworks:
* FastAPI - 0.78.0
* Flask -  2.1.2
* CherryPy -  18.6.1
* Falcon - 3.1.0
* Tornado - 6.1

## Environment setup
Create virtual environment and activate it. Install packages in new virtual environment:
* FastAPI 
```    
    $ pip3 install fastapi "uvicorn[standard]"
```
* Flask
```
    $ pip3 install falcon
```
* CherryPy
```
    $ pip3 install cherrypy
```
* Falcon
```
    $ pip3 install falcon cython "uvicorn[standard]"
```
* Tornado
```
    pip3 install tornado
```

## Run uvicorn server
In order to run a uvicorn server, there has to be python module containing app object.
```
    uvicorn module_name:app --reload
```
