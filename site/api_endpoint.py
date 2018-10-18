#
# Api andpoint for the app 
# will be  used with js frontend app
#  gunicorn -b 0.0.0.0:8080 api_endpoint:api --reload
#



import falcon
import dbconnection as db

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.media = db.getUrl()

api = falcon.API()
api.add_route('/api/files', QuoteResource())