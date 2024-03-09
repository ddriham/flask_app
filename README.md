# flask_app
simple flask app with nginx proxy.
the flask container must be named flask_app.

structure:

* /flask: Contains the Jenkinsfile for the Flask application pipeline.
* /nginx: Contains the Jenkinsfile for the Nginx proxy pipeline.
* Root directory: Contains the Jenkinsfile for running integration tests between the Flask application and the Nginx proxy.


works with job DSL plugin


