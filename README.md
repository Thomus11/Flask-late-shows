├── app.py             # Main application with all routes

├── models.py          # Contains database models

├── seed,py            # contains the data

├── migrations/        # Auto-generated folder for Flask-Migrate

├── database.db        # SQLite database

├── README.md          


Summary of the Project

This project is a Flask API that manages a podcast database. It allows users to interact with three main entities: Episodes , Guests , and Appearances . The API provides endpoints to:
  Retrieve a list of episodes or details of a specific episode (including appearances).
  Retrieve a list of guests.
  Create new appearances, associating a guest with an episode and assigning a rating.
  
The relationships between these entities are as follows:
   An Episode has many Guests through Appearances .
   A Guest appears in many Episodes through Appearances .
  An Appearance belongs to both an Episode and a Guest .
  The project uses Flask-SQLAlchemy for database management, SQLAlchemy SerializerMixin for serialization, and Flask-Migrate for database migrations

Imports necessary libraries:
  flask_sqlalchemy.SQLAlchemy for ORM and database operations.
  sqlalchemy.orm.validates for validation logic.
  sqlalchemy_serializer.SerializerMixin for automatic serialization.
  flask_migrate.Migrate for database migrations

Imports necessary modules:
  Flask for creating the application.
  jsonify and request for handling HTTP requests and responses.
  Migrate for database migrations.
  Models (db, Episode, Guest, Appearance) from models.py

Endpoints:

  1:GET /episodes - List all episodes:
                                    Retrieves all episodes from the database.
                                    Serializes each episode using to_dict() and returns them as JSON

  2:GET /episodes/<int:id>  - Get episode details:
                                      Retrieves a specific episode by its id.
                                      If the episode does not exist, returns a 404 Not Found error.
                                      Serializes the episode and includes its appearances in the response

 3:GET /guests - List all guests:
                             Retrieves all guests from the database.
                             Serializes each guest using to_dict() and returns them as JSON
                             
 4:POST /appearances - Create new appearance:
                                         Accepts a POST request to create a new appearance.
    Validates the input data:
        Ensures the rating is between 1 and 5.
        Ensures episode_id and guest_id are provided and valid.
        Creates a new Appearance record and commits it to the database.
        Returns the created appearance with details of the episode and guest in the response


200 OK: Request successful
GET /episodes
GET /guests

201 Created: Resource successfully created
POST /appearances

400 Bad Request :Invalid  data
Missing fields, invalid rating in POST /appearances

404 Not Found: Resource not found
Non-existent episode or guest in GET /episodes/<int:id> or POST /appearances

  
