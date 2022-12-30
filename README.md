
### Installation and run
***
Please follow the instructions below to use and run the application :

Clone the repository

```
git clone https://github.com/antoinekk/Python_Testing_Fork.git <your path>
```

Create and activate the virtual environment

```
cd Python_Testing_Fork
python3 -m venv env
source env\bin\activate
```

Install python modules provided in the "requirements.txt" file by using your terminal

```
pip install -r requirements.txt
```

Run Flask server

```
export FLASK_APP=server
flask run
```

### Tests / Report
***

Unit and integration tests

```
cd tests/unit_tests/ or cd tests/integration_tests/
pytest <test_file>.py
```

Performance tests

```
cd tests/performance_tests
locust
```

Coverage report

```
cd Python_Testing_Fork
coverage report
```
