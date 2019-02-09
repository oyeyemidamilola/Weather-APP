# Weather-APP
This web app uses the openweather API to make queries of weather status based on country zip code. 


## Getting Started

### Prerequisites
Python 3+ installed on your local machine

### Steps to run code

1. Clone the repo to your local machine
2. Install virtualvenv 
```
py -m pip install --user virtualenv
```
3. Create a virtual environment on your local machine in the your current directory

```
py -m virtualenv <your_environment_name>
```
4. Activate the environment
```
<your_environment_name>\Scripts\activate
```
5. Install the requirements recursively by following command in the project folder directory

```
pip install -r <path to the 'requirements.txt'>
```
6. Navigate to the project folder and set up flask project
    
    On Windows: run
    ```
    set FLASK_APP = weather_app.py 
    ```
    On Mac OS: run
    ```
    export FLASK_APP = weather_app.py 
    ```
7. Start local server with ``` flask run```

A local server server is started on your machine. Open a browser(Chrome) and navigate to the /home
    
