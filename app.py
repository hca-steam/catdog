"""Main application and routing logic for CatDog."""
import os
from flask import Flask
from views import views

# using .env file get DEBUG value

debug_env = bool(os.getenv("DEBUG", "False"))
# for some reason, when the server first launches,
# it immediately restarted with stat meaning "it detected a file change"

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=debug_env, host="0.0.0.0", port=8000)
