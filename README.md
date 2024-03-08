# flask_app
simple flask app with nginx proxy

structure:

* /flask: Contains the Jenkinsfile for the Flask application pipeline.
* /nginx: Contains the Jenkinsfile for the Nginx proxy pipeline.
* Root directory: Contains the Jenkinsfile for running integration tests between the Flask application and the Nginx proxy.


how to use?

in jenkins add a job DSL plugin and configure the seed script as follow:

pipelineJob('flask-list_docker') {
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        url('https://github.com/ddriham/flask_app.git')
                        credentials('git-creds')
                    }
                    branches('*/main')
                    scriptPath('flask/Jenkinsfile')
                }
            }
        }
    }
}
pipelineJob('nginx_proxy') {
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        url('https://github.com/ddriham/flask_app.git')
                        credentials('git-creds')
                    }
                    branches('*/main')
                    scriptPath('nginx/Jenkinsfile')
                }
            }
        }
    }
}
pipelineJob('run_test_flask_nginx_proxy') {
    definition {
        cpsScm {
            scm {
                git {
                    remote {
                        url('https://github.com/ddriham/flask_app.git')
                        credentials('git-creds')
                    }
                    branches('*/main')
                    scriptPath('jenkinsfile')
                }
            }
        }
    }
}


