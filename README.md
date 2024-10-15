# Event Management API

## Overview
This API provides a system for managing events, including functionalities for creating, retrieving, updating, and deleting events, as well as managing reviews and invited users for those events. 

## Features
- User authentication with JWT
- CRUD operations for events and reviews
- RSVP functionality for events
- Management of invited users

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Setup](#setup)
4. [API Endpoints](#api-endpoints)
5. [Testing the API](#testing-the-api)
6. [Conclusion](#conclusion)

## Requirements
- Python 3.12.7
- Django
- Django REST Framework
- Simple JWT
- Other necessary libraries as specified in `requirements.txt`

## Installation
1. **Clone the Repository**
   
   git clone <https://github.com/prajoshi121/Event_management_api>
   cd <repository-directory>

2.Create a Virtual Environment

   python -m venv venv
   On Windows use `venv\Scripts\activate`

3.Install Required Packages
   
   pip install -r requirements.txt

*Setup
1.Run Migrations: Apply the database migrations to set up the database:
   python manage.py migrate

2.Create User and UserProfile: You can create a user along with a user profile using the command:
   python manage.py create_user_user_profile

This command will create both the user and their profile simultaneously.

3.Run the Development Server: Start the Django development server:
    python manage.py runserver


API Endpoints
Authentication
**Obtain JWT Token:

Endpoint: POST /api/token/
Description: Obtain a JWT token for authentication.

Refresh JWT Token
Endpoint: POST /api/token/refresh/
Description: Refresh the JWT token.

**Event Management:
List and Create Events

Endpoint: GET /api/events/
Description: Retrieve a list of events.

Endpoint: POST /api/events/
Description: Create a new event.

*Retrieve, Update, and Delete an Event

Endpoint: GET /api/events/<int:pk>/
Description: Retrieve a specific event by ID.

Endpoint: PUT /api/events/<int:pk>/
Description: Update a specific event by ID.

Endpoint: DELETE /api/events/<int:pk>/
Description: Delete a specific event by ID.

**RSVP for an Event

Endpoint: POST /api/events/<int:pk>/rsvp/
Description: RSVP for a specific event.

**Event Reviews
List and Create Reviews

Endpoint: GET /api/events/<int:event_id>/reviews/
Description: Retrieve a list of reviews for a specific event.

Endpoint: POST /api/events/<int:event_id>/reviews/
Description: Create a new review for a specific event.

*Retrieve, Update, and Delete a Review

Endpoint: GET /api/events/<int:event_id>/reviews/<int:pk>/
Description: Retrieve a specific review by ID.

Endpoint: PUT /api/events/<int:event_id>/reviews/<int:pk>/
Description: Update a specific review by ID.

Endpoint: DELETE /api/events/<int:event_id>/reviews/<int:pk>/
Description: Delete a specific review by ID.

**Invited Users
List and Create Invited Users

Endpoint: GET /api/events/<int:event_id>/inviteduser/
Description: Retrieve a list of invited users for a specific event.

Endpoint: POST /api/events/<int:event_id>/inviteduser/
Description: Create a new invited user for a specific event.

**Retrieve Invited User Details

Endpoint: GET /api/events/<int:event_id>/inviteduser/<int:pk>/
Description: Retrieve details of a specific invited user by ID.


***Testing the API:
You can test the API using Postman or any other API testing tool. Here are some sample requests:

Obtain JWT Token
Method: POST
URL: http://localhost:8000/api/token/

Body (JSON):
  {
  "username": "your_username",
  "password": "your_password"
}

*List Events
Method: GET
URL: http://localhost:8000/api/events/

*Create an Event
Method: POST
URL: http://localhost:8000/api/events/

Body (JSON):
 {
  "title": "Sample Event",
  "description": "Sample Description"
  "location": "Sample Location",
  "start_time": "2024-10-20T10:00:00Z",
  "end_time": "2024-10-20T12:00:00Z",
  
}

*Conclusion
This API provides a comprehensive way to manage events and their related data. Ensure you authenticate before making any requests that require user privileges. Feel free to customize the API according to your needs!
