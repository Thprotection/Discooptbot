# API Documentation

## Overview
This document outlines the API endpoints available for the Discooptbot project.

## Endpoints

### 1. Get User Info
- **GET** `/api/user/{id}`
- **Description:** Retrieves information about a user by their ID.

### 2. Create User
- **POST** `/api/user`
- **Description:** Creates a new user in the system.
- **Request Body:** 
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```

### 3. Update User
- **PUT** `/api/user/{id}`
- **Description:** Updates the information of an existing user.
- **Request Body:** 
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```

### 4. Delete User
- **DELETE** `/api/user/{id}`
- **Description:** Deletes a user from the system.

## Authentication
Most endpoints require authentication via API tokens.

## Rate Limiting
Limit of 100 requests per hour per API token.