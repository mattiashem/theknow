#
# Api andpoint for the app 
# will be  used with js frontend app
#  gunicorn -b 0.0.0.0:8080 api_endpoint:api --reload
#



import falcon
import dbconnection as db

class GetFiles:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.media = db.getUrl()


class GetAlerts:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.media = db.getAlerts()



api = falcon.API()
api.add_route('/api/files', GetFiles())
api.add_route('/api/alerts', GetAlerts())