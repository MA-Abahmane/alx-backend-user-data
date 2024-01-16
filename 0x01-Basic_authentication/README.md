# Python Basic Authentication Cheatsheet

## REST API Authentication Mechanisms

### 1. Basic Authentication
   - Simplest authentication mechanism
   - Sends credentials (username and password) with each request
   - Not secure for transmitting sensitive information without encryption

### 2. Token-based Authentication
   - Token generated on successful login
   - Token sent with each request for authentication
   - Offers better security than Basic Authentication

### 3. OAuth Authentication
   - Delegated authorization protocol
   - Allows third-party applications limited access to resources without sharing credentials
   - Widely used for authentication in web and mobile applications

## Base64 in Python

### 1. Encoding
   ```python
   import base64

   data_to_encode = "Hello, World!"
   encoded_data = base64.b64encode(data_to_encode.encode('utf-8')).decode('utf-8')
   print(encoded_data)
   ```

### 2. Decoding
   ```python
   decoded_data = base64.b64decode(encoded_data).decode('utf-8')
   print(decoded_data)
   ```

## HTTP Header Authorization

### 1. Basic Authentication Header
   - Format: `Authorization: Basic <base64_encoded_credentials>`
   - Example:
     ```http
     GET /api/resource HTTP/1.1
     Host: example.com
     Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
     ```

## Flask - Basic Authentication Example

### 1. Install Flask
   ```bash
   pip install flask
   ```

### 2. Flask App with Basic Authentication
   ```python
   from flask import Flask, request
   from flask_httpauth import HTTPBasicAuth

   app = Flask(__name__)
   auth = HTTPBasicAuth()

   @auth.verify_password
   def verify_password(username, password):
       # Replace with actual user authentication logic
       return username == 'user' and password == 'password'

   @app.route('/api/resource', methods=['GET'])
   @auth.login_required
   def get_resource():
       return jsonify({'data': 'Secure Data'})

   if __name__ == '__main__':
       app.run(debug=True)
   ```

   - Run the Flask app and test Basic Authentication:
     ```bash
     curl -u user:password http://127.0.0.1:5000/api/resource
     ```

## Base64 - Concept

### 1. Purpose
   - Encoding binary data as ASCII text
   - Used for data transmission, such as in email attachments and HTTP requests

### 2. Encoding Process
   - Divides input data into 6-bit chunks
   - Converts each chunk to a corresponding ASCII character
   - Concatenates ASCII characters to form the Base64 encoded string

<br>


***.MAA***