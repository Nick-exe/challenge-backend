# Project Setup
### Start the container

1. Requires `docker-compose` and `docker` installed.
2. Run `docker-compose build` in the project root
3. Run `docker-compose up` to start the server

### Django cli commands
Run the database migrations.

Run `docker-compose run app sh -c "python manage.py migrate`.

### Accessing Django Admin website

1. Run `docker-compose run app sh -c "python manage.py createsuperuser` and
   create an account using any email address.
2. Log into http://localhost:8000/admin/ using the account created in step 1.


### Stop the container

Run `docker-compose stop`.

### Destroy the container (except the volume and external network).

Run `docker-compose down`.


### Application Design
The application consists three main modules:

1. auth: Handles basic authentication against the api supplied for this challenge.
The authentication process is, first, check if the credentials are for an existing user
(Storing users in a local database to prevent unneccessary http calls), if the user does not exist
then we proceed to send a request to the provided login url, if successful, that user is stored on the DB.
This logic is handled by the 'CustomChallengeBackend' Class.
Auth methods are contained in views.py.

2. backend: This is to core of the app, it contains the settings file which holds the apps configurations.
It also unifies the other modules and urls.

3. transation: Contains logic for fetching transactions and cancelling transactions.
Cancelled transactions are logged to a "cancelled-transactions.log" file.
This file is autogenerated if one does not exist.

