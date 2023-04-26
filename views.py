"""File containing all the comprehension for different routes."""

import requests
from flask import Blueprint, render_template

views = Blueprint("views", __name__)


# EXAMPLE FUNCTION IS index()!! Use it to learn! Play around with it!
@views.route("/")
def index() -> str:
    """returns the index html WITH NO ANIMALS :("""
    return render_template(
        "index.html",
        names="John Paul Jones",
    )


# The `dog()` and `cat()` functions in this code use external APIs to retrieve images of a dog and a cat, respectively, and then render the `index.html` template with the retrieved image.

# Here is what you need to do:

# Install dependiencies: (use requirements.txt)
# run `pip install -r requirements.txt` in your VSCODE terminal

# 1. Import the necessary modules. (already done for you)
#    - `requests` to make HTTP requests to the external APIs.
#    - `render_template` from Flask to render the HTML template.

# 2. Create a new route for each function using the `@views.route()` decorator.
#    - The decorator specifies the URL path for the route.
#    - The function name will be used to generate a URL for the route.

# 3. In each function, make an HTTP request to the appropriate API to retrieve an image.
#    - Use the `requests.get()` method to make the request.
#    - The response will contain the image data, which you can extract using the appropriate method for the API.

# 4. Render the `index.html` template with the image data.
#    - Pass the image data to the template as a variable.

# Hint for requests:
# - The `requests.get()` method returns a `Response` object.
# - To make a request, use `requests.get("url", timeout=15)`.
# - To access the response data, use `response.json()["message"]` for the dog function, and `response.url` for the cat function.

# how to use render template in flask python


@views.route("/dog")
def dog() -> str:
    """returns the index html WITH A DOG :)
    Api url: https://dog.ceo/api/breeds/image/random"""


@views.route("/cat")
def cat() -> str:
    """returns the index html WITH A CAT :)
    Api url: https://cataas.com/cat"""


# When you are ready to test, navigate to the root directory of the project
# in your VSCODE terminal and run the following command:
# `python app.py`
