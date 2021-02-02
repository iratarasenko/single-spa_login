# single-spa-login

### Language and frameworks
Python, Selenium WebDriver, pytest

### Scenarios tested
1. User can log in with a valid email and password
2. User cannot log in when email and password fields are empty

### Project set up
1. Download the project folder
2. Create a virtual environment in a main project folder:
```
virtualenv venv 
```
in the project main folder
3. Activate a virtual environment executing a command 
```
source venv/bin/activate
```
from the project folder
4. To install requirements.txt run 
```
pip install -r requirements.txt
```
5. Install chromedriver from https://chromedriver.chromium.org/downloads. Version of chromedriver must be the same as a version of Google Chrome you use.
6. To run the tests execute
```
python -m pytest test.py
```
