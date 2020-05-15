"""Core Flask app routes."""
#from flask import current_app #as app


#@app.route("/")
#def home():
#    return redirect(url_for('/projects/covid-19-dashboards/'))

#@app.route('/contact/')
#def contact():
#    return "Success"

#import dash

from FlaskApp.flask_app import create_app

server = create_app()



