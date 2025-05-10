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
