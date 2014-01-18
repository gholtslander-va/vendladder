"""
-
"""

from google.appengine.api import users
from webapp2 import RequestHandler, cached_property
from webapp2_extras import jinja2

class UserView(RequestHandler):

    @cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, template, **context):
        """ Pass a template (html) and a dictionary :) """

        if "logout" not in context.keys() or "login" not in context.keys():
            user = users.get_current_user()
            if user:
                if users.is_current_user_admin():
                    context["is_admin"] = True
                context["logout"] = users.create_logout_url("/")
            else:
                context["login"] = users.create_login_url("/")
        # Seasonal constants
        season = "Winter"
        season_number = "1"
        year = "2014"
        context["year"] = year
        context["season"] = season
        context["season_no"] = season_number
        content = self.jinja2.render_template(template, **context)
        self.response.write(content)