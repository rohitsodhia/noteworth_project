## Notes:
- As I had mentioned to Daniel, I'm not a pro at Django, specially as an app. My experience is more with APIs.


# App
This app is used to get an auth token and use the token to pull the following information:
- Providers

## Setup
To setup the app, make sure Poetry is installed.

Run `poetry install` to install all dependencies.

Use `poetry run ./manage.py runserver` to start the Django server, which by default will run at `http://127.0.0.1:8000/`.

## To-dos/Considerations

- Write tests
  - Honestly I didn't get to tests just because it took me a while to get the Django app setup, as I don't do the base apps with HTML views often.
  - Most of the code that exists is relatively simple and uses methods from other packages, which should be tested. Tests should be written for the view methods to make sure they return errors in the correct states.
- We should put together an error class and templates to handle the more common/modular errors.
- Currently, only the latest providers are shown, but all are stored with timestamps. Given there's no unique identifiers for returned providers, we could get an infinite list, and this is problematic.
  - Perhaps we should tag the providers by the auth key used to pull them, to help group the list.
