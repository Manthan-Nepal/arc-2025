# Task Management API Specification

## 1. Overview

API Name: Task Management API
Description:
A RESTful API that allows clients to manage a list of tasks stored locally in a tasks.json file. It provides endpoints to retrieve, add, and delete tasks.

Base URL: http://localhost:8080

## 2. Endpoints

### GET /tasks :

Retrieve the list of all tasks.

Error Responses:
404 Not Found: if the endpoint path is invalid.

### POST /tasks:

Add a new task to the list.

Error Responses:
400 Bad Request: if JSON is invalid or missing the task field.
409 Conflict: if the task already exists.

### DELETE /tasks/{taskname}:

Delete a task by name.
Error Responses:
404 Not Found: if the task does not exist or the endpoint path is invalid.

## 3.Request & Response Format

All requests and responses use;
Content-Type: application/json

## 4. Status Codes

200: OK (success)
201: Created (task added)
400: Bad Request (invalid input or JSON)
404: Not Found (invalid path or missing task)
409: Conflict (task already exists)

## 5. Example

Add a task:
curl -X POST -H "Content-Type: application/json" -d '{"task": "buy milk"}' http://localhost:8080/tasks

Get all tasks:
curl http://localhost:8080/tasks

Delete a task:
curl -X DELETE http://localhost:8080/tasks/buy%20milk

## 6. Dependencies

Python standard library used:

http.server for the HTTP server
json for JSON encoding/decoding
os for file checks
urllib.parse for URL parsing and decoding
