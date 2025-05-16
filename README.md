# 1. Project Description

## Project Goal
The goal of the project is to develop a system for storing user data (first name, last name, email) and enabling user searches based on various criteria (e.g., last name, email address). A NoSQL database, such as MongoDB, can be used to store the data.

## Scope
- Ability to add new entries  
- Search by last name and email address  

## Technologies
- Python  
- MongoDB

---

# 2. Requirements Analysis and System Design

## Functional Requirements
- The user can add a new entry containing a first name, last name, and email address.  
- The system allows searching users by last name.  
- The system allows searching users by email address.  
- The system enables filtering search results using multiple criteria simultaneously.  
- Search results should include the full user data (first name, last name, email).  
- The system should validate data, e.g., check the email format.  
- The system provides an API for integration or communication with the front-end.  
- The system should report errors, e.g., missing required fields or invalid data formats.

## Non-functional Requirements
- User searches should be fast.  
- The application should support easy expansion of the user database without performance degradation.  
- The system should operate stably without unexpected errors.  
- User data should be protected from unauthorized access.  
- Input data should be validated and sanitized to prevent attacks (e.g., injection).  
- The application should be deployable both locally and in the cloud (e.g., Heroku, Railway, Vercel).  
- The application code should be clean and well-documented.  
- The API should be accessible via HTTP, preferably using a standard data format (e.g., JSON).  
- Compatibility with MongoDB as the NoSQL database.

---

## System Design

The system follows a **client-server architecture** with a clear separation of layers:
- **Data Layer:** MongoDB – stores user documents.  
- **Business Logic Layer:** Backend application – handles CRUD operations, validation, and search logic.  
- **Presentation Layer:** Frontend and Postman for endpoint testing.

### Data Model

Data is stored as documents, which are data structures similar to JSON objects:

```json
{
  "firstName": "Jan",
  "lastName": "Kowalski",
  "email": "jan.kowalski@example.com"
}
 ```

# 3. Application Setup

## 1. Installing Dependencies

To run the application, you need to install the required dependencies. This includes **Flask**, **Flask-PyMongo**, and **Flask-CORS**.

### Step 1: Create a Virtual Environment (optional)
It is recommended to create a virtual environment to avoid conflicts with package versions.

For Unix/MacOS/Linux systems:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Required Packages
Install Flask and other dependencies:

```bash
pip install flask flask-pymongo flask-cors
```

### Step 3: Ensure MongoDB is Available
The application uses MongoDB as the database. If you don't have MongoDB installed locally, you can use MongoDB Atlas (a cloud-hosted MongoDB service).

1. Create an account on MongoDB Atlas.
2. Create a new cluster.
3. Copy the connection URI of your cluster, which will be used in the application configuration.

---

## 2. Preparing the Application

### Step 1: Create the Configuration File
Create a `config.py` file in the main project directory and insert the following content:

```python
MONGO_URI = "mongodb+srv://user:password@cluster.mongodb.net/dbname?retryWrites=true&w=majority"
```

### Step 2: Run the Application
Run the Flask application using the following command:

```bash
python app.py
```

The application should now be running on the local server at:

```bash
http://127.0.0.1:5000/
```

# 4. API Endpoints

The application exposes several endpoints to manage users.

---

### 1. List Available API Routes – `/routes`

This endpoint returns all available routes in the API.

**Example:**
```http
GET http://127.0.0.1:5000/routes
```

**Response:**

```
[
  "/api/users/",
  "/api/users/search",
  "/api/users/<id>"
]
```

### 2. Get All Users – /api/users/ (GET)
This endpoint returns all users in the database.

**Example:**
```
GET http://127.0.0.1:5000/api/users/
```
**Response:**
```
[
  {
    "id": "60b72f3a9f1b2c4e6c1a7d3b",
    "first_name": "Anna",
    "last_name": "Nowak",
    "email": "anna.nowak@example.com"
  },
  {
    "id": "60b72f3a9f1b2c4e6c1a7d3c",
    "first_name": "Jan",
    "last_name": "Kowalski",
    "email": "jan.kowalski@example.com"
  }
]
```


### 3. Add a New User – /api/users/ (POST)
This endpoint allows you to add a new user to the database. You must send the data in JSON format:

**Example:**
```
POST http://127.0.0.1:5000/api/users/
```
**JSON data:**

```
{
  "first_name": "Piotr",
  "last_name": "Nowak",
  "email": "piotr.nowak@example.com"
}
```
**Response:**
```
{
  "id": "60b72f3a9f1b2c4e6c1a7d3d",
  "first_name": "Piotr",
  "last_name": "Nowak",
  "email": "piotr.nowak@example.com"
}
```

### 4. Get a User by ID – /api/users/<id> (GET)
This endpoint retrieves user details based on the unique _id.

**Example:**
```
GET http://127.0.0.1:5000/api/users/60b72f3a9f1b2c4e6c1a7d3b
```
**Response:**
```
{
  "id": "60b72f3a9f1b2c4e6c1a7d3b",
  "first_name": "Anna",
  "last_name": "Nowak",
  "email": "anna.nowak@example.com"
}
```

### 5. Search Users – /api/users/search (GET)
You can search users by first name and last name.

**Example 1:** Search by first name:
```
GET http://127.0.0.1:5000/api/users/search?first_name=Anna
```
**Example 2:** Search by last name:
```
GET http://127.0.0.1:5000/api/users/search?last_name=Kowalski
```
**Example 3:** Search by first and last name:
```
GET http://127.0.0.1:5000/api/users/search?first_name=Piotr&last_name=Nowak
```
**Response:**
```
[
  {
    "id": "60b72f3a9f1b2c4e6c1a7d3d",
    "first_name": "Piotr",
    "last_name": "Nowak",
    "email": "piotr.nowak@example.com"
  }
]
```

# 5. Testing the API
You can use your browser, Postman, or Insomnia to test these endpoints.

To test the search, simply visit:
```
http://127.0.0.1:5000/api/users/search?first_name=Anna
```
This should return a list of users with the first name containing "Anna".
