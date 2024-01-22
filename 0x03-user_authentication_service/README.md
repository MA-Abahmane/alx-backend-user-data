# User Authentication Service Cheat Sheet

## SQLAlchemy

### 1. Installation
```bash
pip install SQLAlchemy
```

### 2. Basic Setup
```python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)
```

### 3. User Model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
```

### 4. Create Table
```python
db.create_all()
```

### 5. Querying Users
```python
# Example: Retrieve a user by username
user = User.query.filter_by(username='example').first()
```

## Flask Documentation

### 1. Installation
```bash
pip install Flask
```

### 2. Basic Setup
```python
from flask import Flask, request, jsonify
app = Flask(__name__)
```

### 3. Route and Endpoint
```python
@app.route('/login', methods=['POST'])
def login():
    # Your authentication logic here
    return jsonify({'message': 'Login Successful'})
```

### 4. Accessing Request Data
```python
# Example: Accessing username and password from request
username = request.json.get('username')
password = request.json.get('password')
```

## Requests Module

### 1. Installation
```bash
pip install requests
```

### 2. Making HTTP Requests
```python
import requests

# Example: Sending a POST request
url = 'http://example.com/login'
data = {'username': 'user', 'password': 'pass'}
response = requests.post(url, json=data)
```

### 3. Handling Response
```python
# Example: Checking status code and accessing response data
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Error:', response.status_code)
```

## HTTP Status Codes

### 1. 2xx Success
- 200 OK
- 201 Created
- 204 No Content

### 2. 4xx Client Errors
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found

### 3. 5xx Server Errors
- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable