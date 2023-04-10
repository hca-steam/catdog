"""File containing all the comprehension for different routes."""

import requests
from flask import Blueprint, render_template

views = Blueprint("views", __name__)

# so I was thinking the index html has two buttons that say dog and cat
# then when you click one of them it links to the corresponding url
# then that page loads, and it does the thing


@views.route("/")
def index() -> str:
    """returns the index html WITH NO ANIMALS :((((("""
    return render_template(
        "index.html",
        names="John Paul Jones",
    )


@views.route("/dog")
def dog() -> str:
    """returns the index html WITH A DOG :)"""
    response = requests.get("https://dog.ceo/api/breeds/image/random", timeout=15)
    return render_template(
        "index.html",
        animal=response.json()["message"],
    )


@views.route("/cat")
def cat() -> str:
    """returns the index html WITH A CAT :)"""
    response = requests.get("https://cataas.com/cat", timeout=15)
    # that for some reason returns the actual full image, not a url

    return render_template(
        "index.html",
        animal=response.url,
    )
