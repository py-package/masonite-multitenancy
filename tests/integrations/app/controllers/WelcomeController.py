"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from tests.integrations.app.models.User import User


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return User.all()
        # return view.render("welcome")

    def index(self):
        User.create({"name": "John Doe", "email": "john@doe.com", "password": "capslock"})
